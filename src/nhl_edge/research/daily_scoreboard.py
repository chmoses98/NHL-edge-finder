"""Daily settled-game scoreboard: every projection family against the market and the outcome, pregame forecasts only (RESEARCH_ONLY; read-only).

For each FINAL game since the prospective freeze (``PROSPECTIVE_FREEZE_UTC``) the winner probability of the **last pregame forecast** of each model
is paired with the Kalshi midpoint carried by that same forecast row and the official result:

    V1 (DATA_ONLY_V1)   ``predictions``     game_winner home-team row, ``p_data_only``
    V2 (shadow)         ``predictions_v2``  same ticker, ``p_data_only_v2``
    OA_SVA, OA_SVA_C1   ``predictions_oa``  ``p_home_win`` (the prospective record the promotion scorecard's G9/G10 gates need)
    MARKET              the row's ``p_market`` (midpoint at the forecast's own market observation time)

Rows written at or after puck drop (``pregame`` false) are never used. Games without results are pending, games without a pregame forecast are listed
as missing; nothing is imputed. The cumulative table carries paired Brier differences with a game bootstrap interval once there are >= 30 games; below
that only the point estimate is shown, labelled with n -- at a handful of games nothing here can distinguish models and nothing here promotes one.

``python -m nhl_edge.research.daily_scoreboard --archive DIR --out OUT``
"""

from __future__ import annotations

import gzip
import json
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import numpy as np

from nhl_edge.model_research.scoring import brier, paired_delta
from nhl_edge.timeutil import iso, parse_iso, utcnow

PROSPECTIVE_FREEZE_UTC = "2026-10-21T17:13:05Z"
MIN_GAMES_FOR_INTERVAL = 30
MODELS = ("V1", "V2", "OA_SVA", "OA_SVA_C1", "MARKET")


def _rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def _files(archive: Path, kind: str, dates: list[str]) -> list[Path]:
    out: list[Path] = []
    for d in dates:
        out += sorted((archive / kind / f"dt={d}").glob("*.jsonl.gz"))
    return out


def load_results(archive: Path, dates: list[str]) -> dict[str, dict[str, Any]]:
    """Latest FINAL result per game (a later fetch with a correction supersedes an earlier one)."""
    out: dict[str, dict[str, Any]] = {}
    for p in _files(archive, "results", dates):
        for r in _rows(p):
            if r.get("status") != "final" or r.get("home_final") is None:
                continue
            gid = str(r["game_id"])
            if gid not in out or int(r.get("stat_correction_version") or 0) >= int(out[gid].get("stat_correction_version") or 0):
                out[gid] = r
    return out


def _last_pregame(archive: Path, kind: str, dates: list[str], keep, value: str) -> dict[tuple[str, ...], dict[str, Any]]:
    """Latest pregame row per key. ``keep(row)`` -> key tuple or None; ``value`` is the probability column."""
    best: dict[tuple[str, ...], dict[str, Any]] = {}
    for p in _files(archive, kind, dates):
        for r in _rows(p):
            pre = r.get("pregame")
            if pre is None:                    # predictions_v2 rows carry no flag: pregame == the forecast was made before the start
                pre = r.get("minutes_to_start") is not None and float(r["minutes_to_start"]) > 0
            if not pre or r.get(value) is None:
                continue
            k = keep(r)
            if k is None:
                continue
            cur = best.get(k)
            if cur is None or r["predicted_at_utc"] > cur["predicted_at_utc"]:
                best[k] = r
    return best


def build_games(archive: Path, dates: list[str]) -> dict[str, Any]:
    results = load_results(archive, dates + [(date.fromisoformat(dates[-1]) + timedelta(days=1)).isoformat()])
    home_id = {gid: int(r["home_team_id"]) for gid, r in results.items()}

    def v1_key(r):
        if r.get("family") != "game_winner" or r.get("team_id") is None:
            return None
        gid = str(r["game_id"])
        return (gid,) if gid in home_id and int(r["team_id"]) == home_id[gid] else None

    v1 = _last_pregame(archive, "predictions", dates, v1_key, "p_data_only")
    v2 = _last_pregame(archive, "predictions_v2", dates, v1_key, "p_data_only_v2")
    oa = _last_pregame(archive, "predictions_oa", dates, lambda r: (str(r["game_id"]), r["arm"]), "p_home_win")
    games: dict[str, Any] = {}
    missing: list[str] = []
    pending: list[str] = []
    for (gid,), r in v1.items():
        res = results[gid]
        start = parse_iso(r["predicted_at_utc"]).timestamp() + float(r["minutes_to_start"]) * 60
        if start <= parse_iso(PROSPECTIVE_FREEZE_UTC).timestamp():
            continue
        y = 1.0 if res["home_final"] > res["away_final"] else 0.0
        g = {"game_id": gid, "y_home_win": y, "home_final": res["home_final"], "away_final": res["away_final"], "forecast_at_utc": r["predicted_at_utc"],
             "minutes_before_start": float(r["minutes_to_start"]), "p": {"V1": float(r["p_data_only"]), "MARKET": None if r.get("p_market") is None else float(r["p_market"])},
             "date_et": iso(parse_iso(r["predicted_at_utc"]) + timedelta(minutes=float(r["minutes_to_start"])) - timedelta(hours=5))[:10]}
        if (gid,) in v2:
            g["p"]["V2"] = float(v2[(gid,)]["p_data_only_v2"])
        for arm in ("OA_SVA", "OA_SVA_C1"):
            if (gid, arm) in oa:
                g["p"][arm] = float(oa[(gid, arm)]["p_home_win"])
        games[gid] = g
    all_pred_games = {str(r["game_id"]) for p in _files(archive, "predictions", dates) for r in _rows(p) if r.get("family") == "game_winner"}
    for gid in sorted(all_pred_games):
        if gid not in results:
            pending.append(gid)
        elif gid not in games:
            missing.append(gid)
    return {"games": games, "pending": pending, "no_pregame_or_before_freeze": missing}


def score(games: dict[str, Any]) -> dict[str, Any]:
    gl = list(games.values())
    out: dict[str, Any] = {"n_games": len(gl), "models": {}, "paired": {}}
    for m in MODELS:
        have = [g for g in gl if g["p"].get(m) is not None]
        if have:
            p = np.array([g["p"][m] for g in have])
            y = np.array([g["y_home_win"] for g in have])
            out["models"][m] = {"n": len(have), "brier": float(brier(np.clip(p, 0.005, 0.995), y).mean())}
    for a, b in (("V1", "MARKET"), ("V2", "V1"), ("OA_SVA", "V1"), ("OA_SVA_C1", "V1"), ("OA_SVA_C1", "MARKET"), ("OA_SVA_C1", "OA_SVA")):
        both = [g for g in gl if g["p"].get(a) is not None and g["p"].get(b) is not None]
        if not both:
            continue
        y = np.array([g["y_home_win"] for g in both])
        la = brier(np.clip(np.array([g["p"][a] for g in both]), 0.005, 0.995), y)
        lb = brier(np.clip(np.array([g["p"][b] for g in both]), 0.005, 0.995), y)
        rec: dict[str, Any] = {"n": len(both), "delta_brier": float(np.mean(la - lb))}
        if len(both) >= MIN_GAMES_FOR_INTERVAL:
            d = paired_delta(la, lb, n_boot=2000)
            rec.update({"lo95": d["lo95"], "hi95": d["hi95"]})
        out["paired"][f"{a}_minus_{b}"] = rec
    return out


def render(sb: dict[str, Any], by_day: dict[str, dict[str, Any]], now_iso: str) -> str:
    cum = sb["cumulative"]
    L = [f"# NHL daily scoreboard — {now_iso}", "",
         f"RESEARCH_ONLY · pregame forecasts only (the last forecast written before puck drop) · prospective window: games starting after {PROSPECTIVE_FREEZE_UTC} · "
         f"{cum['n_games']} settled games · {len(sb['pending'])} games pending results · {len(sb['no_pregame_or_before_freeze'])} final games excluded (no pregame forecast or before the freeze)", "",
         "## Cumulative (lower Brier = better; the market column is the Kalshi midpoint carried by the same forecast row)", "", "| model | games | Brier(home win) |", "|---|---:|---:|"]
    for m, v in cum["models"].items():
        L.append(f"| {m} | {v['n']} | {v['brier']:.4f} |")
    L += ["", "| paired (A − B, negative = A better) | games | Δ Brier | 95% CI |", "|---|---:|---:|---|"]
    for k, v in cum["paired"].items():
        ci = f"[{v['lo95']:+.4f}, {v['hi95']:+.4f}]" if "lo95" in v else f"n < {MIN_GAMES_FOR_INTERVAL}: no interval"
        L.append(f"| {k.replace('_minus_', ' − ')} | {v['n']} | {v['delta_brier']:+.4f} | {ci} |")
    L += ["", "Nothing in this table promotes a model: differences of ~0.004 Brier need hundreds of games to resolve (see `docs/research/PROMOTION_SCORECARD.md` gates G9/G10).", "",
          "## By ET game day", "", "| day | games | " + " | ".join(MODELS) + " |", "|---|---:|" + "---:|" * len(MODELS)]
    for d, v in sorted(by_day.items()):
        L.append(f"| {d} | {v['n_games']} | " + " | ".join(f"{v['models'][m]['brier']:.4f}" if m in v["models"] else "-" for m in MODELS) + " |")
    return "\n".join(L) + "\n"


def run(archive: Path, out: Path | None, since: str | None = None, until: str | None = None) -> dict[str, Any]:
    start = date.fromisoformat((since or PROSPECTIVE_FREEZE_UTC)[:10])
    end = date.fromisoformat(until) if until else utcnow().date()
    dates = [(start + timedelta(days=i)).isoformat() for i in range((end - start).days + 2)]
    built = build_games(archive, dates)
    games = built["games"]
    sb = {"generated_at_utc": iso(utcnow()), "freeze_utc": PROSPECTIVE_FREEZE_UTC, "cumulative": score(games), "pending": built["pending"],
          "no_pregame_or_before_freeze": built["no_pregame_or_before_freeze"]}
    by_day = {d: score({k: g for k, g in games.items() if g["date_et"] == d}) for d in sorted({g["date_et"] for g in games.values()})}
    md = render(sb, by_day, sb["generated_at_utc"])
    print(md)
    if out:
        out.mkdir(parents=True, exist_ok=True)
        (out / "scoreboard.json").write_text(json.dumps({**sb, "by_day": by_day, "games": games}, indent=1))
        (out / "scoreboard.md").write_text(md)
    return sb


def sparse_patterns(max_days: int = 60) -> list[str]:
    """Archive paths a sparse checkout needs for this report (the last ``max_days`` UTC dates since the freeze, plus the manifest)."""
    end = utcnow().date()
    start = max(date.fromisoformat(PROSPECTIVE_FREEZE_UTC[:10]), end - timedelta(days=max_days))
    days = [(start + timedelta(days=i)).isoformat() for i in range((end - start).days + 1)]
    return ["/manifest.jsonl"] + [f"/{k}/dt={d}/" for k in ("predictions", "predictions_v2", "predictions_oa", "results") for d in days]


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.daily_scoreboard")
    ap.add_argument("--sparse-patterns", action="store_true", help="print the sparse-checkout patterns and exit")
    ap.add_argument("--archive")
    ap.add_argument("--out")
    ap.add_argument("--since")
    ap.add_argument("--until")
    a = ap.parse_args(argv)
    if a.sparse_patterns:
        print("\n".join(sparse_patterns()))
        return 0
    if not a.archive:
        ap.error("--archive is required")
    run(Path(a.archive), Path(a.out) if a.out else None, a.since, a.until)
    return 0


if __name__ == "__main__":
    sys.exit(main())
