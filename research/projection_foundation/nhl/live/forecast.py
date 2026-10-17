"""Project stage: slate -> availability-conditioned challenger forecasts + the incumbent's own forecasts, archived.

    availability snapshots (as of now) -> who is projected, goalie per team, participation per player
    frozen models (nhl.live.model, cached per slate)                 -> means / pmfs / thresholds / TOI
    pf_core.gate with participation                                  -> PASS / REVIEW / BLOCK
    pf_core.prospective.archive_forecasts(model_role="challenger")   -> immutable pregame forecasts
    PLAYER_SIM_V1 archived predictions, unchanged                    -> model_role="incumbent"

Never generates or archives anything for a game that has already started (the slate only contains games whose scheduled
start is after `now`; pf_core.archive_forecasts rejects anything generated or archived at/after the start as a second line).
"""
from __future__ import annotations

import math
from datetime import datetime, timedelta
from typing import Any

import numpy as np
import pandas as pd

from pf_core import availability as av
from pf_core import gate, prospective as pr

from nhl import data

from . import availability as A
from . import common as C
from . import model as M

CHALLENGER = "challenger"
INCUMBENT = "incumbent"
INCUMBENT_ID = "PLAYER_SIM_V1"
FAMILIES = ("shots", "goals", "assists", "points", "saves", "team_goals", "toi_minutes")
SKATER_STATS = {"sog": "shots", "goals": "goals", "assists": "assists", "points": "points"}
MIN_LINEUP = 15           # a DailyFaceoff capture with fewer even-strength skaters is not a lineup (as nhl.project)
INC_FAMILIES = ("player_goals", "player_assists", "player_points", "goalie_saves")   # first_goal is not a stat family here
RECENT_GAMES = 2          # roster superset: players who dressed in a team's last N games (cache stays valid when the lineup shifts)


# --------------------------------------------------------------------------- slate
def pick_slate(archive: str, now: datetime, date: str | None = None) -> tuple[pd.DataFrame, str | None, pd.DataFrame]:
    """Regular-season games that have not started by `now`, on the earliest ET date that has any (or `date`)."""
    s = C.schedule_asof(archive, now, back_days=10)
    if s.empty:
        return s, None, s
    s = s[s["game_id"].map(C.is_regular)]
    fut = s[(s["start"] > pd.Timestamp(now)) & (s["status"] != "final")]
    if date:
        fut = fut[fut["game_date_et"] == date]
    if fut.empty:
        return fut, None, s
    d = fut["game_date_et"].min()
    return fut[fut["game_date_et"] == d].sort_values("start").reset_index(drop=True), d, s


# --------------------------------------------------------------------------- rows from availability
def _team_ab(tid: int) -> str:
    return C.abbrev_by_id().get(int(tid), str(tid))


def current_rows(lat: dict, games: pd.DataFrame, hist: pd.DataFrame, ghist: pd.DataFrame, ref: A.PlayerRef) \
        -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Skater rows (`lu`, with extra=True for roster-superset fillers) and goalie rows (`gs`) for the slate."""
    abbr = C.abbrev_by_id()
    lu_rows, gs_rows = [], []
    info = {"teams": 0, "teams_with_lines": 0, "teams_last_dressed": 0, "official_confirmed_teams": 0,
            "goalie_teams": 0, "goalie_named": 0, "goalie_fallback": 0, "goalie_unresolved_history": 0}
    by_ev_kind: dict[tuple[str, str], list[dict]] = {}
    for (ev, _ent, kind), r in lat.items():
        by_ev_kind.setdefault((ev, kind), []).append(r)
    for g in games.itertuples():
        ev = str(int(g.game_id))
        for tid, home in ((int(g.home_team_id), True), (int(g.away_team_id), False)):
            ab = abbr[tid]
            info["teams"] += 1
            line = [r for r in by_ev_kind.get((ev, "line"), []) if r["team"] == ab]
            chosen: dict[int, dict] = {}
            src = None
            if line:
                mx = max(r["captured_utc"] for r in line)
                cur = [r for r in line if r["captured_utc"] == mx]
                if len(cur) >= MIN_LINEUP:
                    for r in cur:
                        d = r.get("detail") or {}
                        chosen[int(r["entity_id"])] = {
                            "name": r["entity_name"], "slot": d.get("slot"), "unit": d.get("ev_unit"),
                            "pp": d.get("pp_unit"), "conf": 1.0 if d.get("identity") in ("jersey+name", "archive", "name_team") else 0.95,
                            "src": f"DailyFaceoff lines ({d.get('lines_source')}) captured {mx}"}
                    src = "lines"
            official = [r for r in by_ev_kind.get((ev, "lineup"), []) if r["team"] == ab and r["status"] == "ACTIVE"
                        and r["certainty"] == "CONFIRMED"]
            if official:
                info["official_confirmed_teams"] += 1
                for r in official:
                    chosen.setdefault(int(r["entity_id"]), {"name": r["entity_name"], "slot": None, "unit": None, "pp": None,
                                                            "conf": 1.0, "src": f"official pregame roster ({r['source']})"})
                src = src or "official"
            h = hist[hist["team_id"] == tid]
            if src is None:
                info["teams_last_dressed"] += 1
                last = h[h["game_date"] == h["game_date"].max()] if len(h) else h
                for r in last.itertuples():
                    chosen[int(r.player_id)] = {"name": r.name, "slot": None, "unit": None, "pp": None, "conf": 1.0,
                                                "src": f"team's last dressed lineup ({r.game_date:%Y-%m-%d}); no lines captured"}
            else:
                info["teams_with_lines"] += 1
            for pid, d in chosen.items():
                lu_rows.append({"game_id": int(g.game_id), "team_id": tid, "is_home": home, "player_id": pid, "name": d["name"],
                                "slot": d["slot"], "unit": d["unit"], "pp_unit_proj": d["pp"], "lineup_source": d["src"],
                                "identity_confidence": d["conf"], "lines_injury": None, "extra": False})
            # roster-superset fillers: recent dressers (not published; they keep the cached model table valid)
            recent_dates = sorted(h["game_date"].unique())[-RECENT_GAMES:] if len(h) else []
            for r in h[h["game_date"].isin(recent_dates)].drop_duplicates("player_id").itertuples():
                if int(r.player_id) not in chosen:
                    lu_rows.append({"game_id": int(g.game_id), "team_id": tid, "is_home": home, "player_id": int(r.player_id),
                                    "name": r.name, "slot": None, "unit": None, "pp_unit_proj": None, "lineup_source": "filler",
                                    "identity_confidence": 1.0, "lines_injury": None, "extra": True})
            # goalie
            info["goalie_teams"] += 1
            st = [r for r in by_ev_kind.get((ev, "starter"), []) if r["team"] == ab]
            th = ghist[ghist["team_id"] == tid].sort_values("game_date")
            pick = None
            if st:
                r = max(st, key=lambda x: x["captured_utc"])
                if int(r["entity_id"]) in set(ghist["player_id"]):
                    nm = ghist[ghist["player_id"] == int(r["entity_id"])]["name"].iloc[-1]
                    pick = (int(r["entity_id"]), nm, (r.get("detail") or {}).get("dfo_status"), r["captured_utc"], True)
                    info["goalie_named"] += 1
                else:
                    info["goalie_unresolved_history"] += 1       # named goalie has no NHL history: no model row, no substitute
                    pick = (int(r["entity_id"]), r["entity_name"], (r.get("detail") or {}).get("dfo_status"), r["captured_utc"], False)
            if pick is None:
                s = th[th["starter"]]
                if len(s):
                    pick = (int(s["player_id"].iloc[-1]), s["name"].iloc[-1], None, None, True)
                    info["goalie_fallback"] += 1
            if pick:
                gs_rows.append({"game_id": int(g.game_id), "team_id": tid, "is_home": home, "player_id": pick[0], "name": pick[1],
                                "dfo_status": pick[2], "captured_utc": pick[3], "has_history": pick[4],
                                "fallback": pick[2] is None})
    return pd.DataFrame(lu_rows), pd.DataFrame(gs_rows), info


# --------------------------------------------------------------------------- incumbent (PLAYER_SIM_V1, unchanged)
def incumbent_records(archive: str, now: datetime, games: pd.DataFrame) -> tuple[list[dict], dict]:
    """The incumbent's own latest pregame snapshot per (game, player), as archived by the capture worker. Mean + the
    ladder it published (P(X >= k)); no pmf exists, so `probs` stays empty and scoring falls back to its published rungs."""
    ids = {int(x) for x in games["game_id"]}
    d = C.read_kind(archive, "predictions_player", since=now - timedelta(hours=48), until=now)
    st = {"rows": int(len(d)), "players": 0, "records": 0}
    if d.empty:
        return [], st
    d["game_id"] = pd.to_numeric(d["game_id"], errors="coerce")
    d = d[d["game_id"].isin(ids) & d["player_id"].notna() & d["family"].isin(INC_FAMILIES)].copy()
    d = d[(d["pregame"] == True) & (pd.to_numeric(d["minutes_to_start"], errors="coerce") > 0)]  # noqa: E712
    d["t"] = pd.to_datetime(d["predicted_at_utc"], utc=True)
    d = d[d["t"] <= pd.Timestamp(now)]
    if d.empty:
        return [], st
    d["player_id"] = pd.to_numeric(d["player_id"]).astype("int64")
    d["k"] = np.floor(pd.to_numeric(d["threshold"]) + 1).astype(int)
    start = {int(r.game_id): C.iso(r.start.to_pydatetime()) for r in games.itertuples()}
    recs: list[dict] = []
    for (gid, pid), g in d.groupby(["game_id", "player_id"]):
        last_t = g["t"].max()
        snap = g[g["t"] == last_t].iloc[0]
        gen = C.iso(last_t.to_pydatetime())
        ladders: dict[str, dict[str, float]] = {}
        for fam, gg in g.groupby("family"):
            lad = gg.sort_values("t").groupby("k").tail(1)
            ladders[fam] = {str(int(k)): round(float(p), 6) for k, p in zip(lad["k"], lad["p_player"])}
        base = {"sport": C.SPORT, "model_id": INCUMBENT_ID, "model_role": INCUMBENT, "model_version": str(snap["model_version"]),
                "game_id": str(int(gid)), "game_start_utc": start[int(gid)], "entity_id": str(int(pid)),
                "entity_name": snap["player_name"], "team": snap.get("meta_team"), "generated_utc": gen,
                "data_asof_utc": snap.get("data_cutoff_utc") or gen, "lo": 0, "probs": [], "gate_status": None,
                "participation": None, "readiness": "INCUMBENT", "role": "incumbent", "authority": "research_only",
                "quality": snap.get("meta_projection_quality")}
        st["players"] += 1
        pairs = [("shots", "meta_expected_shots", None), ("goals", "meta_expected_goals", "player_goals"),
                 ("assists", "meta_expected_assists", "player_assists"), ("points", "meta_expected_points", "player_points"),
                 ("toi_minutes", "meta_expected_toi_min", None), ("saves", "meta_expected_saves", "goalie_saves")]
        for fam, col, lad_fam in pairs:
            v = snap.get(col)
            if v is None or (isinstance(v, float) and not math.isfinite(v)):
                continue
            recs.append({**base, "family": fam, "mean": float(v), "ladder": ladders.get(lad_fam, {}) if lad_fam else {}})
    st["records"] = len(recs)
    return recs, st


# --------------------------------------------------------------------------- assemble
def assemble(table: dict, games: pd.DataFrame, lu: pd.DataFrame, gs: pd.DataFrame, rows_av: list[dict], now: datetime,
             pstart_table: dict, model_version: str) -> tuple[dict, list[dict], dict]:
    """Challenger projections (sift.projections.v1 + live fields) and forecast-archive records from the model table."""
    abbr = C.abbrev_by_id()
    now_s = C.iso(now)
    lat = av.asof(rows_av, now_s)
    idx = A.capture_index(rows_av)
    gmap = games.set_index("game_id")
    players, recs = [], []
    stats = {"players": 0, "rows": 0, "gate": {"PASS": 0, "REVIEW": 0, "BLOCK": 0}, "participation": {}, "goalies": 0,
             "goalie_unverified": 0, "skipped_no_model_row": 0}
    recon: dict[tuple[int, int], float] = {}
    fam_meta = table["families"]
    rq = table["rq"]
    asof = table["asof"]
    pub = lu[~lu["extra"]]

    def add_rec(r: dict, fam: str, mean: float, probs, gr: dict, p: av.Participation | None, readiness: str, extra: dict):
        recs.append({"sport": C.SPORT, "family": fam, "model_id": f"pf-nhl-{extra.pop('model')}", "model_role": CHALLENGER,
                     "model_version": model_version, "game_id": str(r["game_id"]), "game_start_utc": r["start"],
                     "entity_id": r["entity_id"], "entity_name": r["name"], "team": r["team"], "generated_utc": now_s,
                     "data_asof_utc": asof, "mean": round(float(mean), 6), "lo": 0, "probs": probs, "gate_status": gr["status"],
                     "participation": p.status if p else None, "readiness": readiness, "role": "shadow",
                     "authority": "research_only", **extra})

    for r in pub.itertuples():
        key = (int(r.game_id), int(r.player_id))
        e = table["skaters"].get(key)
        if e is None:
            stats["skipped_no_model_row"] += 1
            continue
        g = gmap.loc[r.game_id]
        start = C.iso(g.start.to_pydatetime())
        ab, opp = abbr[int(r.team_id)], abbr[int(e["opp_id"])]
        ev = str(int(r.game_id))
        p = A.participation(lat, ev, str(int(r.player_id)), now_s, idx=idx)
        pd_ = A.participation_dict(p)
        stats["players"] += 1
        stats["participation"][p.status] = stats["participation"].get(p.status, 0) + 1
        base = {"game_id": int(r.game_id), "start": start, "entity_id": str(int(r.player_id)), "name": e["name"], "team": ab}
        for stat, s in e["stats"].items():
            fam = s["family"]
            oppf = s["oppf"]
            adj = []
            if abs(oppf - 1) >= 0.03:
                adj.append(f"opponent {opp} {'allows more' if oppf > 1 else 'suppresses'} {'shots' if stat == 'sog' else 'scoring'}: "
                           f"x{oppf:.2f} (schedule-adjusted ridge rating)")
            if e["b2b"] == 1:
                adj.append("team on the second night of a back-to-back")
            if e["toi_n"] < 10:
                adj.append(f"only {int(e['toi_n'])} prior NHL games since 2021-22: rates lean on the role prior")
            if isinstance(r.pp_unit_proj, str):
                adj.append(f"projected {r.pp_unit_proj.upper()} by DailyFaceoff (role uses the previous game's PP unit)")
            if p.status != av.CONFIRMED_ACTIVE:
                adj.append(f"conditional on dressing; participation {p.status.replace('_', ' ').lower()}")
            gr = gate.evaluate(gate.GateInput(
                sport="NHL", family=fam, entity_id=base["entity_id"], entity_name=e["name"], team=ab, game_id=ev,
                game_start_utc=start, mean=s["mu"], identity_confidence=float(r.identity_confidence), team_verified=True,
                data_asof_utc=asof, injury_status=None, expected_opportunity=e["toi_E"], opportunity_history=e["hist_toi"],
                stat_history=e["hist"].get(stat), opponent_sample_games=None, opponent_factor=oppf, support_lo=0,
                probs=s["probs"], thresholds=s["thresholds"], sd=s["sd"], model_n_obs=int(e["toi_n"]),
                participation=p.status, participation_reasons=p.reasons), now_utc=now_s)
            stats["gate"][gr["status"]] += 1
            stats["rows"] += 1
            rd = fam_meta[fam]["readiness"]
            players.append({
                "player_id": base["entity_id"], "name": e["name"], "team": ab, "opponent": opp, "game_id": ev, "family": fam,
                "mean": round(s["mu"], 4), "median": s["median"], "p10": s["p10"], "p90": s["p90"],
                "thresholds": s["thresholds"],
                "opportunity": {"family": "toi_minutes", "mean": round(e["toi_E"], 2),
                                "p10": round(max(0.0, e["toi_E"] + rq[0]), 2), "p90": round(e["toi_E"] + rq[1], 2),
                                "pp_mean": round(e["toi_pp_E"], 2)},
                "opponent_adjustment": {"factor": round(oppf, 4), "sample_games": None}, "adjustments": adj, "readiness": rd,
                "participation": pd_, "role": "shadow", "conditional_on": "dressing",
                "gate": {"status": gr["status"], "findings": [{k: f[k] for k in ("check", "severity", "what", "category", "action")}
                                                              for f in gr["findings"]]},
                "lineup_source": r.lineup_source, "data_asof_utc": asof})
            add_rec(base | {"start": start}, fam, s["mu"], s["probs"], gr, p, rd,
                    {"model": s["model"], "opponent": opp, "conditional_on": "dressing", "participation_certainty": p.certainty})
            if stat == "goals":
                recon[(int(r.game_id), int(r.team_id))] = recon.get((int(r.game_id), int(r.team_id)), 0.0) + s["mu"]
        # TOI (opportunity family): mean only
        gr = gate.evaluate(gate.GateInput(
            sport="NHL", family="toi_minutes", entity_id=base["entity_id"], entity_name=e["name"], team=ab, game_id=ev,
            game_start_utc=start, mean=e["toi_E"], identity_confidence=float(r.identity_confidence), team_verified=True,
            data_asof_utc=asof, model_n_obs=int(e["toi_n"]), participation=p.status, participation_reasons=p.reasons),
            now_utc=now_s)
        stats["gate"][gr["status"]] += 1
        add_rec(base | {"start": start}, "toi_minutes", e["toi_E"], [], gr, p, "SHADOW VALIDATION",
                {"model": "E_lightgbm", "opponent": opp, "conditional_on": "dressing", "participation_certainty": p.certainty})
    # goalies
    for r in gs.itertuples():
        key = (int(r.game_id), int(r.player_id))
        e = table["goalies"].get(key)
        if e is None or not getattr(r, "has_history", True):
            stats["skipped_no_model_row"] += 1
            continue
        g = gmap.loc[r.game_id]
        start = C.iso(g.start.to_pydatetime())
        ab, opp = abbr[int(r.team_id)], abbr[int(e["opp_id"])]
        ev = str(int(r.game_id))
        p = A.participation(lat, ev, str(int(r.player_id)), now_s, goalie=True, idx=idx)
        hours = (g.start.to_pydatetime() - now).total_seconds() / 3600
        ps, basis = A.p_start(pstart_table, r.dfo_status if isinstance(r.dfo_status, str) else None, hours)
        if p.status == av.UNVERIFIED:
            stats["goalie_unverified"] += 1
            if ps is None:
                basis = "no DailyFaceoff starter observation: goalie is the team's most recent starter (unverified)"
        stats["goalies"] += 1
        stats["participation"][p.status] = stats["participation"].get(p.status, 0) + 1
        findings_extra = []
        gr = gate.evaluate(gate.GateInput(
            sport="NHL", family="saves", entity_id=str(int(r.player_id)), entity_name=e["name"], team=ab, game_id=ev,
            game_start_utc=start, mean=e["mu"], data_asof_utc=asof, expected_opportunity=e["sa_D"], support_lo=0,
            probs=e["probs"], thresholds=e["thresholds"], model_n_obs=e["saves_n"], participation=p.status,
            participation_reasons=p.reasons), now_utc=now_s)
        if p.status != av.CONFIRMED_ACTIVE and gr["status"] == "PASS":
            findings_extra.append({"check": "starter", "severity": "REVIEW", "category": "uncertainty",
                                   "what": f"starter {p.status.replace('_', ' ').lower()}"
                                           + (f"; P(start) {ps:.2f}" if ps is not None else ""),
                                   "action": "Re-run after the starter is confirmed."})
            gr["status"] = "REVIEW"
        stats["gate"][gr["status"]] += 1
        stats["rows"] += 1
        rd = fam_meta["saves"]["readiness"]
        adj = [f"conditional on {e['name']} starting"
               + (f" (P(start) {ps:.2f}: {basis})" if ps is not None else f" ({basis})")]
        players.append({
            "player_id": str(int(r.player_id)), "name": e["name"], "team": ab, "opponent": opp, "game_id": ev, "family": "saves",
            "mean": round(e["mu"], 3), "median": e["median"], "p10": e["p10"], "p90": e["p90"], "thresholds": e["thresholds"],
            "opportunity": {"family": "shots_against", "mean": round(e["sa_D"], 2) if e["sa_D"] is not None else None,
                            "p10": None, "p90": None},
            "opponent_adjustment": {"factor": None, "sample_games": None}, "adjustments": adj, "readiness": rd,
            "participation": A.participation_dict(p), "role": "shadow", "conditional_on": "starting",
            "p_start": ps, "p_start_basis": basis,
            "gate": {"status": gr["status"], "findings": [{k: f[k] for k in ("check", "severity", "what", "category", "action")}
                                                          for f in gr["findings"] + findings_extra]},
            "data_asof_utc": asof})
        add_rec({"game_id": int(r.game_id), "start": start, "entity_id": str(int(r.player_id)), "name": e["name"], "team": ab},
                "saves", e["mu"], e["probs"], gr, p, rd,
                {"model": e["model"], "opponent": opp, "conditional_on": "starting", "p_start": ps, "p_start_basis": basis,
                 "participation_certainty": p.certainty, "dfo_status": r.dfo_status if isinstance(r.dfo_status, str) else None})
    # games + team goals
    games_out = []
    for g in games.itertuples():
        tl = []
        start = C.iso(g.start.to_pydatetime())
        for tid in (int(g.home_team_id), int(g.away_team_id)):
            t = table["teams"].get((int(g.game_id), tid))
            if t is None:
                continue
            rec = gate.team_reconciliation(recon.get((int(g.game_id), tid), 0.0), t["mu"], "team goals")
            ab = abbr[tid]
            gr = gate.evaluate(gate.GateInput(
                sport="NHL", family="team_goals", entity_id=ab, entity_name=C.team_name_by_abbrev().get(ab, ab), team=ab,
                game_id=str(int(g.game_id)), game_start_utc=start, mean=t["mu"], data_asof_utc=asof, support_lo=0,
                probs=t["probs"]), now_utc=now_s)
            stats["gate"][gr["status"]] += 1
            tl.append({"team": ab, "family": "team_goals", "mean": round(t["mu"], 3), "p10": t["p10"], "p90": t["p90"],
                       "player_goal_sum": round(recon.get((int(g.game_id), tid), 0.0), 3),
                       "reconciliation": {"status": rec["status"], "ratio": rec.get("ratio")}, "role": "shadow",
                       "gate": {"status": gr["status"], "findings": [{k: f[k] for k in ("check", "severity", "what", "category", "action")}
                                                                      for f in gr["findings"]]}})
            add_rec({"game_id": int(g.game_id), "start": start, "entity_id": ab, "name": C.team_name_by_abbrev().get(ab, ab),
                     "team": ab}, "team_goals", t["mu"], t["probs"], gr, None, fam_meta["team_goals"]["readiness"],
                    {"model": t["model"], "opponent": abbr[int(g.away_team_id) if tid == int(g.home_team_id) else int(g.home_team_id)],
                     "conditional_on": "game played"})
        games_out.append({"game_id": str(int(g.game_id)), "start_utc": start, "home": abbr[int(g.home_team_id)],
                          "away": abbr[int(g.away_team_id)], "teams": tl})
    payload = {
        "schema": "sift.projections.v1", "sport": "NHL", "generated_utc": now_s, "data_asof_utc": asof,
        "model": {"id": "pf-nhl", "version": model_version, "authority": "research_only"},
        "families": fam_meta | {"toi_minutes": {"readiness": "SHADOW VALIDATION", "model": "E_lightgbm",
                                                 "reason": "opportunity family: holdout TOI MAE 1.82 min"}},
        "games": games_out, "players": players,
        "gate_summary": gate.summarize([{"status": p["gate"]["status"], "findings": p["gate"]["findings"]} for p in players]),
    }
    return payload, recs, stats


# --------------------------------------------------------------------------- archive (changed-only)
def archive_changed(recs: list[dict], out_root: str, now: datetime) -> dict[str, Any]:
    """Archive forecasts that differ from the latest archived pregame version of the same key (mean, pmf, gate status or
    participation class changed); identical re-runs add nothing. pf_core.archive_forecasts still rejects late/invalid."""
    if not recs:
        return {"written": 0, "unchanged": 0, "late_rejected": 0, "invalid": 0, "duplicates": 0}
    days = sorted({r["game_start_utc"][:10] for r in recs})
    prev = pr.latest_pregame(pr.load_forecasts(out_root, C.SPORT, days))
    def sig(mean, probs, gate_status, participation, ladder) -> tuple:
        part = None if participation is None or (isinstance(participation, float) and math.isnan(participation)) else participation
        gs_ = None if gate_status is None or (isinstance(gate_status, float) and math.isnan(gate_status)) else gate_status
        # the archive stores probs rounded to 7 decimals: compare what would be stored, not the raw floats
        return (round(float(mean), 5), tuple(round(round(float(x), 7), 5) for x in (probs if probs is not None else [])), gs_, part,
                json_ladder(ladder))

    last: dict[tuple, tuple] = {}
    if len(prev):
        for r in prev.itertuples():
            last[(str(r.game_id), str(r.entity_id), r.family, r.model_id)] = sig(r.mean, list(r.probs), r.gate_status, r.participation,
                                                                                   getattr(r, "ladder", None))
    fresh, unchanged = [], 0
    for r in recs:
        k = (r["game_id"], r["entity_id"], r["family"], r["model_id"])
        if last.get(k) == sig(r["mean"], r["probs"], r["gate_status"], r["participation"], r.get("ladder")):
            unchanged += 1
            continue
        fresh.append(r)
    s = pr.archive_forecasts(fresh, out_root, now_utc=C.iso(now))
    s["unchanged"] = unchanged
    s["offered"] = len(recs)
    return s


def json_ladder(x) -> str:
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return ""
    return str(sorted((str(k), round(float(v), 5)) for k, v in dict(x).items()))


# --------------------------------------------------------------------------- stage entry point
def newest_final_observation(dar: str, now: datetime, slate_date: str) -> str:
    """data_asof: when the newest final game used as history was ingested (always before the slate's first start)."""
    best = None
    for f in C.archive_files(dar, "player_events/players", until=now)[-6:]:
        d = pd.read_json(f, lines=True, dtype=False)
        d = d[pd.to_datetime(d["game_date"]) < pd.Timestamp(slate_date)]
        if len(d):
            m = d["_observed_at_utc"].max()
            best = m if best is None or m > best else best
    return best or C.iso(now)


def with_cached_fillers(lu: pd.DataFrame, table: dict | None, games: pd.DataFrame) -> pd.DataFrame:
    """When the model must be recomputed, keep everything the stale table already modelled (for games still on the slate)
    so the new table is a superset and later runs on this slate keep hitting the cache."""
    if table is None:
        return lu
    live = {int(g) for g in games["game_id"]}
    have = {(int(g), int(p)) for g, p in zip(lu["game_id"], lu["player_id"])}
    rows = [{"game_id": g, "team_id": e["team_id"], "is_home": e["is_home"], "player_id": p, "name": e["name"], "slot": None,
             "unit": None, "pp_unit_proj": None, "lineup_source": "filler", "identity_confidence": 1.0, "lines_injury": None,
             "extra": True} for (g, p), e in table["skaters"].items() if (g, p) not in have and g in live]
    return pd.concat([lu, pd.DataFrame(rows)], ignore_index=True) if rows else lu


def run_project(dar: str, arch: str, now: datetime, work, date: str | None = None, log=print, clock=None,
                refresh=None) -> dict[str, Any]:
    """Slate -> (cached) frozen-model table -> availability-conditioned forecasts -> archive. Returns the run summary.

    `clock()` (live runs) is the real time: the model can take 30-40 minutes, so afterwards the availability is refreshed
    (`refresh(now)` re-captures), games that have started in the meantime are dropped, and the archive is written with the
    real clock (pf_core rejects anything archived at/after a start). With a fixed `--now` (replay/tests) clock is None."""
    try:
        return _run_project(dar, arch, now, work, date, log, clock, refresh)
    finally:
        data.set_cutoff(None)          # the as-of history cut-off is a property of this stage only (results/score read all finals)
        data.set_future({})


def _situation(dar: str, arch: str, now: datetime, date: str | None):
    games, slate_date, _ = pick_slate(dar, now, date)
    if slate_date is None:
        return None
    data.set_cutoff(slate_date)                       # history = final games dated before the slate
    hist, ghist = data.load_kind("players"), data.load_kind("goalies")
    rows_av = A.load_rows(arch, now)
    lat = av.asof(rows_av, C.iso(now))
    lu, gs, info = current_rows(lat, games, hist, ghist, A.player_ref())
    return games, slate_date, rows_av, lu, gs, info


def _run_project(dar: str, arch: str, now: datetime, work, date: str | None, log, clock, refresh) -> dict[str, Any]:
    import json
    import os
    import time

    os.makedirs(work, exist_ok=True)
    if os.path.exists(os.path.join(work, "projection.json")):
        os.remove(os.path.join(work, "projection.json"))      # never publish a previous run's projection
    sit = _situation(dar, arch, now, date)
    if sit is None:
        return {"slate_date": None, "note": "no regular-season game starts after now in the archived schedule"}
    games, slate_date, rows_av, lu, gs, info = sit
    gs_ok = gs[gs["has_history"]] if len(gs) else gs
    key = M.base_key(slate_date)
    table = M.load_table(key)
    reused = table is not None and M.covers(table, lu, gs_ok)
    t0 = time.time()
    if not reused:
        table = M.compute(games, with_cached_fillers(lu, table, games), gs_ok, slate_date,
                          newest_final_observation(dar, now, slate_date), key, log=log)
        M.save_table(table)
        if clock is not None:                          # the clock moved on while the models ran: re-read the world
            now = clock()
            if refresh is not None:
                refresh(now)
            sit = _situation(dar, arch, now, date)
            if sit is None or sit[1] != slate_date:
                return {"slate_date": None, "model_table_key": key, "model_seconds": round(time.time() - t0, 1),
                        "note": "every game of the slate started while the models were running; the table is cached for the next slate"}
            games, slate_date, rows_av, lu, gs, info = sit
            gs_ok = gs[gs["has_history"]] if len(gs) else gs
            if not M.covers(table, lu, gs_ok):
                log("[project] the refreshed lineups contain players the model table does not cover; they are skipped this run")
    now_arch = clock() if clock is not None else now
    pst = A.start_probability_table(dar, now)
    version = f"{table['version']}+{M.project._sha()}"
    payload, recs, st = assemble(table, games, lu, gs, rows_av, now, pst, version)
    exp: dict[str, set[str]] = {}
    for p in payload["players"]:
        exp.setdefault(p["game_id"], set()).add(p["player_id"])         # skaters and goalies, one entry each
    expected = {ev: sorted(ids) for ev, ids in exp.items()}
    cov = av.coverage(rows_av, expected, {ev: C.iso(now) for ev in expected}, C.iso(now_arch))
    inc, inc_st = incumbent_records(dar, now, games)
    ch_arch = archive_changed(recs, arch, now_arch)
    inc_arch = archive_changed(inc, arch, now_arch)
    payload["slate"] = {"date": slate_date, "label": f"{slate_date} slate: {len(games)} games not started at {C.iso(now)}",
                        "conditioning": "skater rows are conditional on dressing, saves on the listed goalie starting (P(start) published)",
                        "lineup_info": info}
    with open(os.path.join(work, "projection.json"), "w") as f:
        json.dump(payload, f, separators=(",", ":"), default=str)
    summ = {"slate_date": slate_date, "games": [int(x) for x in games["game_id"]], "now": C.iso(now), "archived_at": C.iso(now_arch),
            "model_table_key": key, "model_reused": bool(reused), "model_seconds": 0.0 if reused else round(time.time() - t0, 1),
            "lineup_info": info, "assemble": st, "coverage": cov, "p_start_table": pst,
            "archive": {"challenger": ch_arch, "incumbent": inc_arch}, "incumbent_source": inc_st,
            "late_rejected": ch_arch.get("late_rejected", 0) + inc_arch.get("late_rejected", 0),
            "gate": payload["gate_summary"]["status_counts"]}
    path = os.path.join(arch, "runs", "nhl", now.strftime("%Y-%m-%d"), f"{now.strftime('%H%M%S')}Z_project.json")
    if not os.path.exists(path):
        C.write_json_once(path, summ)
    return {k: summ[k] for k in ("slate_date", "model_reused", "model_seconds", "lineup_info", "assemble", "archive", "late_rejected",
                                 "gate", "incumbent_source")} | {"coverage_mean": cov["mean_coverage"], "coverage_events": cov["n_events"]}
