"""Pregame slate readiness check: ``nhl slate-check``.

Reads a published ``packet.json`` (and, when given, the archive's schedule snapshot for the same ET date) and reports,
per game, whether the projection is complete, fresh and internally coherent *before puck drop*. It reads only; it
publishes nothing, prices nothing and touches no wager path. A finding is ERROR (do not rely on this game's numbers),
WARN (usable, degraded input) or INFO. The verdict is the worst severity found: READY / DEGRADED / NOT_READY.

It does not repair anything and invents no data: a missing input is reported as missing.
"""

from __future__ import annotations

import gzip
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge.timeutil import iso, parse_iso, utcnow

# Thresholds, in one place so the report can print them.
GOALIE_OBS_STALE_MIN = 180.0      # goalie source observation older than this, with the game inside GOALIE_WINDOW_MIN
GOALIE_WINDOW_MIN = 240.0
LINES_STALE_H = 36.0
MARKET_STALE_MIN = 30.0
PROJECTION_STALE_MIN = 120.0      # a projection older than this with the game inside PROJECTION_WINDOW_MIN
PROJECTION_WINDOW_MIN = 240.0
MIN_PRICED_PLAYERS = 20
SEV_ORDER = {"INFO": 0, "WARN": 1, "ERROR": 2}


def _age_min(ts: str | None, now: datetime) -> float | None:
    if not ts:
        return None
    try:
        return (now - parse_iso(ts)).total_seconds() / 60.0
    except ValueError:
        return None


def load_schedule(path: Path) -> list[dict[str, Any]]:
    with gzip.open(path, "rt") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def _f(findings: list[dict[str, Any]], sev: str, code: str, msg: str) -> None:
    findings.append({"severity": sev, "code": code, "message": msg})


def _ladder_monotone(ladder: dict[str, float]) -> bool:
    keyed = sorted(((float(k.rsplit("_", 1)[-1]), v) for k, v in ladder.items()))
    return all(b <= a + 1e-9 for (_, a), (_, b) in zip(keyed, keyed[1:], strict=False))


def check_game(game: dict[str, Any], v2: dict[str, Any] | None, player: dict[str, Any] | None, now: datetime) -> dict[str, Any]:
    ident, model, gt, ctx = game["identity"], game["model"], game["goaltending"], game.get("context") or {}
    start = parse_iso(ident["start_time_utc"])
    to_start = (start - now).total_seconds() / 60.0
    out: list[dict[str, Any]] = []
    if to_start <= 0:
        _f(out, "INFO", "STARTED", "game has started; this projection is the pregame record and must not be refreshed")

    # model sanity (regulation + OT consistency, plausible rates, ladder coherence, the simulator's own trust flags)
    sim = model.get("sim") or {}
    p_home, p_ot, tot = sim.get("p_home_win"), sim.get("p_overtime"), sim.get("total_mean")
    lam_h, lam_a = sim.get("home_lambda"), sim.get("away_lambda")
    if p_home is None or tot is None:
        _f(out, "ERROR", "MODEL_MISSING", "no win probability / expected total")
    else:
        if not 0.05 < p_home < 0.95:
            _f(out, "ERROR", "P_HOME_RANGE", f"P(home)={p_home:.3f} outside (0.05, 0.95)")
        if not 3.5 <= tot <= 8.5:
            _f(out, "ERROR", "TOTAL_RANGE", f"expected total {tot:.2f} outside [3.5, 8.5]")
        if lam_h is not None and lam_a is not None and not (0.5 < lam_h < 6 and 0.5 < lam_a < 6):
            _f(out, "ERROR", "LAMBDA_RANGE", f"lam {lam_h:.2f}/{lam_a:.2f}")
        if abs((sim.get("p_home_win", 0) + sim.get("p_away_win", 0)) - 1.0) > 1e-3:
            _f(out, "ERROR", "WIN_PROBS_NOT_NORMALISED", "P(home)+P(away) != 1")
    if p_ot is not None and not 0.05 < p_ot < 0.5:
        _f(out, "ERROR", "OT_RANGE", f"P(OT)={p_ot:.3f}")
    for lad in ("total_ladder", "home_team_total_ladder", "away_team_total_ladder"):
        if sim.get(lad) and not _ladder_monotone(sim[lad]):
            _f(out, "ERROR", f"{lad.upper()}_NOT_MONOTONE", f"V1 {lad} is not monotone")
    if model.get("ladder_violations"):
        _f(out, "ERROR", "LADDER_VIOLATIONS", str(model["ladder_violations"])[:200])
    if model.get("inputs_trusted") is False:
        _f(out, "WARN", "INPUTS_NOT_TRUSTED", "; ".join(map(str, model.get("input_reasons") or []))[:300] or "simulator flagged its inputs")

    # goaltending: status, source age, how close the game is
    for side in ("home", "away"):
        g = gt.get(side) or {}
        st = g.get("status", "UNKNOWN")
        age = _age_min(g.get("observed_at_utc"), now)
        if st == "UNKNOWN" or not g.get("player_name"):
            _f(out, "ERROR" if to_start < 120 else "WARN", f"GOALIE_{side.upper()}_UNKNOWN", f"{side} starter unknown (league-average net assumed)")
        elif st == "PROJECTED" and to_start < 90:
            _f(out, "WARN", f"GOALIE_{side.upper()}_UNCONFIRMED", f"{side} {g['player_name']} still PROJECTED {to_start:.0f} min before puck drop")
        if age is not None and age > GOALIE_OBS_STALE_MIN and to_start < GOALIE_WINDOW_MIN:
            _f(out, "WARN", f"GOALIE_{side.upper()}_STALE", f"{side} goalie observation is {age:.0f} min old")

    # market snapshot
    kal = game.get("kalshi") or {}
    mage = kal.get("market_age_min")
    if not kal.get("contracts"):
        _f(out, "WARN", "NO_MARKET", "no Kalshi contracts joined to this game")
    elif mage is not None and mage > MARKET_STALE_MIN:
        _f(out, "WARN", "MARKET_STALE", f"market snapshot {mage:.0f} min old")
    fams = (kal.get("coverage") or {}).get("by_family") or {}
    missing = [f for f in ("game_winner", "game_total", "game_spread", "team_total", "game_overtime") if not fams.get(f)]
    if missing:
        _f(out, "WARN", "FAMILIES_MISSING", "no board for " + ", ".join(missing))

    # injuries / lines inputs
    snap = (ctx.get("injury_snapshot") or {}).get("age_min")
    if snap is not None and snap > 360:
        _f(out, "WARN", "INJURY_SNAPSHOT_STALE", f"injury snapshot {snap:.0f} min old")
    if v2 is None:
        _f(out, "INFO", "NO_V2", "no DATA_ONLY_V2 shadow block (OT/tie shape comes from V1 only)")
    elif v2.get("v2", {}).get("total_ladder") and not _ladder_monotone(v2["v2"]["total_ladder"]):
        _f(out, "ERROR", "V2_LADDER_NOT_MONOTONE", "V2 total ladder is not monotone")

    # player layer
    if player is None:
        _f(out, "WARN", "NO_PLAYER_BLOCK", "no PLAYER_SIM_V1 block")
    else:
        if player.get("invariant_violations"):
            _f(out, "ERROR", "PLAYER_INVARIANTS", "; ".join(map(str, player["invariant_violations"]))[:300])
        if (player.get("n_priced") or 0) < MIN_PRICED_PLAYERS:
            _f(out, "WARN", "FEW_PLAYERS", f"only {player.get('n_priced', 0)} priced player contracts")
        for side in ("home", "away"):
            lu = (player.get("lineups") or {}).get(side) or {}
            src = lu.get("deployment_source", "")
            if not str(src).startswith("LINES"):
                _f(out, "WARN", f"LINES_{side.upper()}_FALLBACK", f"{side} deployment source {src or 'none'}")
            for note in lu.get("notes") or []:
                if "h old)" in note:
                    try:
                        hrs = float(note.rsplit("(", 1)[1].split("h old")[0])
                    except ValueError:
                        continue
                    if hrs > LINES_STALE_H:
                        _f(out, "WARN", f"LINES_{side.upper()}_STALE", f"{side} line source {hrs:.0f} h old")

    # projection freshness against puck drop
    pred_ts = next((c.get("predicted_at_utc") for c in (kal.get("contracts") or [])), None)
    page = _age_min(pred_ts, now)
    if page is not None and page > PROJECTION_STALE_MIN and 0 < to_start < PROJECTION_WINDOW_MIN:
        _f(out, "WARN", "PROJECTION_STALE", f"projection {page:.0f} min old with puck drop in {to_start:.0f} min")

    worst = max((SEV_ORDER[x["severity"]] for x in out), default=0)
    return {"game_id": ident["game_id"], "matchup": f"{ident['away']} @ {ident['home']}", "start_time_utc": ident["start_time_utc"],
            "minutes_to_start": round(to_start, 1), "projection_age_min": None if page is None else round(page, 1),
            "worst": {0: "OK", 1: "WARN", 2: "ERROR"}[worst], "findings": out}


def check_slate(packet: dict[str, Any], schedule: list[dict[str, Any]] | None = None, now: datetime | None = None) -> dict[str, Any]:
    now = now or utcnow()
    games = packet.get("games") or []
    v2 = {b["game_id"]: b for b in (packet.get("v2_shadow") or {}).get("blocks") or []}
    pl = {b["game_id"]: b for b in (packet.get("player_shadow") or {}).get("blocks") or []}
    date_et = (packet.get("slate") or {}).get("date_et")
    rows = [check_game(g, v2.get(g["identity"]["game_id"]), pl.get(g["identity"]["game_id"]), now) for g in games]
    slate_findings: list[dict[str, Any]] = []
    if schedule is not None and date_et:
        sched = {s["game_id"]: s for s in schedule if s.get("game_date_et") == date_et}
        pk = {g["identity"]["game_id"]: g["identity"] for g in games}
        for gid, s in sched.items():
            if gid not in pk and s.get("status") not in ("final", "live"):
                _f(slate_findings, "ERROR", "GAME_NOT_PROJECTED", f"{s['away_abbrev']} @ {s['home_abbrev']} ({gid}) is scheduled but absent from the packet")
        for gid, i in pk.items():
            s = sched.get(gid)
            if s is None:
                _f(slate_findings, "ERROR", "GAME_NOT_SCHEDULED", f"{i['away']} @ {i['home']} ({gid}) is projected but not on the official schedule")
                continue
            if (s["home_abbrev"], s["away_abbrev"]) != (i["home"], i["away"]) or s["home_team_id"] != i["home_team_id"] or s["away_team_id"] != i["away_team_id"]:
                _f(slate_findings, "ERROR", "TEAM_IDENTITY", f"{gid}: packet {i['away']}@{i['home']} vs schedule {s['away_abbrev']}@{s['home_abbrev']}")
            if s["start_time_utc"] != i["start_time_utc"]:
                _f(slate_findings, "WARN", "START_TIME_CHANGED", f"{gid}: packet {i['start_time_utc']} vs schedule {s['start_time_utc']}")
    alarms = (packet.get("slate") or {}).get("coverage") or {}
    if alarms.get("games_skipped"):
        _f(slate_findings, "ERROR", "GAMES_SKIPPED", f"simulator skipped {alarms['games_skipped']}")
    worst = max([SEV_ORDER[x["severity"]] for x in slate_findings] + [SEV_ORDER.get(r["worst"], 0) if r["worst"] != "OK" else 0 for r in rows], default=0)
    n_err = sum(1 for r in rows if r["worst"] == "ERROR")
    verdict = "NOT_READY" if worst == 2 else "DEGRADED" if worst == 1 else "READY"
    return {"checked_at_utc": iso(now), "date_et": date_et, "generated_at_utc": (packet.get("slate") or {}).get("generated_at_utc"),
            "model_version": (packet.get("slate") or {}).get("model_version"), "n_games": len(rows), "n_scheduled": None if schedule is None else len(sched) if date_et else None,
            "verdict": verdict, "n_games_error": n_err, "slate_findings": slate_findings, "games": rows,
            "thresholds": {"goalie_obs_stale_min": GOALIE_OBS_STALE_MIN, "lines_stale_h": LINES_STALE_H, "market_stale_min": MARKET_STALE_MIN,
                           "projection_stale_min": PROJECTION_STALE_MIN}}


def render_markdown(rep: dict[str, Any]) -> str:
    lines = [f"# NHL slate readiness — {rep['date_et']} — **{rep['verdict']}**", "",
             f"checked {rep['checked_at_utc']} · packet generated {rep['generated_at_utc']} · model {rep['model_version']} · games projected {rep['n_games']}"
             + (f" of {rep['n_scheduled']} scheduled" if rep.get("n_scheduled") is not None else ""), ""]
    for f in rep["slate_findings"]:
        lines.append(f"- **{f['severity']}** {f['code']}: {f['message']}")
    lines += ["", "| game | start UTC | to start (min) | proj age (min) | status | findings |", "|---|---|---:|---:|---|---|"]
    for r in rep["games"]:
        fs = "; ".join(f"{f['severity']} {f['code']}" for f in r["findings"] if f["severity"] != "INFO") or "—"
        lines.append(f"| {r['matchup']} | {r['start_time_utc']} | {r['minutes_to_start']} | {r['projection_age_min']} | {r['worst']} | {fs} |")
    detail = [(r["matchup"], f) for r in rep["games"] for f in r["findings"] if f["severity"] != "INFO"]
    if detail:
        lines += ["", "## Finding detail", ""] + [f"- {m}: **{f['severity']}** {f['code']} — {f['message']}" for m, f in detail]
    return "\n".join(lines) + "\n"


def run_slate_check(packet_path: Path, schedule_path: Path | None, out_dir: Path | None, now: datetime | None = None) -> int:
    packet = json.loads(Path(packet_path).read_text())
    schedule = load_schedule(schedule_path) if schedule_path else None
    rep = check_slate(packet, schedule, now)
    md = render_markdown(rep)
    print(md)
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "slate_check.json").write_text(json.dumps(rep, indent=1))
        (out_dir / "slate_check.md").write_text(md)
    return 0 if rep["verdict"] != "NOT_READY" else 2
