"""Daily research feedback loop (RESEARCH_ONLY, manual dispatch, publish=false by default).

    python -m nhl_edge.model_research.daily ingest    --dev-dry-run --archive <data-archive> --date <development-window date> --repo . --ledger <scratch.jsonl>
    python -m nhl_edge.model_research.daily scorecard --ledger <plaintext ledger> --out <dir>      # development / owner-local use only

The PROSPECTIVE daily path is ``python -m nhl_edge.sealed_ledger.runner`` (outcome-bearing rows are encrypted before they leave the runner; see
``docs/research/nhl-model-improvement/SEALED_LEDGER_DESIGN.md``). This module's plaintext ledger is for development-window dry runs and for the owner's local look.

``ingest`` (development dry run) / ``build_rows`` (used by the sealed runner) settle one slate date: for every FINAL game that day it freezes the pregame state at T-60 (the last production slate run at or before the cut), regenerates the
production V1 predictive distribution bit-for-bit, scores it against the final (randomised PIT, win-probability surprise), applies the frozen challenger C1 (parameters from
``data/cal_experiments.json``; never refitted here), classifies the miss (attribution classes A-F, see ``attribution.py``) and yields ONE row per game for an append-only, idempotent (by game_id) ledger. Nothing is retrained and no model is promoted by a night's results.

``scorecard`` never reveals aggregate model-vs-market performance on the PROSPECTIVE tier before the first predeclared look (150 independent games). Until then it reports counts,
pregame data-quality measures only (no outcome-derived number of any kind); at 150 games it writes LOOK_150.json exactly once (later looks 300 / 450 likewise).
The development tier (games started before the 2026-10-21T17:13:05Z freeze) is never ingested here.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research import PROSPECTIVE_FREEZE_UTC
from nhl_edge.model_research import attribution as AT
from nhl_edge.model_research import challengers as C
from nhl_edge.model_research import dist_eval as D
from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.live_dataset import build_live_dataset
from nhl_edge.model_research.slates import build_slate_table

LOOKS = (150, 300, 450)
LEDGER_FIELDS = ["game_id", "game_date_et", "start_time_utc", "cut_utc", "slate_run_id", "slate_generated_at", "slate_age_min", "v1_p_home_win", "v1_lam_home", "v1_lam_away", "v2_p_home_win",
                 "c1_p_home_win", "sb_p_home", "sb_n_providers", "y_home_win", "y_total", "home_final", "away_final", "last_period_type", "pit_total", "pit_margin", "brier_v1", "rps_total",
                 "attribution_class", "attribution_evidence", "any_goalie_mismatch", "home_goalie_status", "away_goalie_status"]


def _clean(v: Any) -> Any:
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating, float)):
        return None if (isinstance(v, float) and math.isnan(v)) or (isinstance(v, np.floating) and np.isnan(v)) else float(v)
    if isinstance(v, (pd.Timestamp,)):
        return v.isoformat()
    if isinstance(v, (np.bool_,)):
        return bool(v)
    return v


def read_ledger(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def append_rows(path: Path, rows: list[dict[str, Any]]) -> int:
    """Idempotent append: a game already in the ledger is never rewritten or duplicated."""
    have = {r["game_id"] for r in read_ledger(path)}
    new = [r for r in rows if r["game_id"] not in have]
    if new:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a") as fh:
            if path.exists() and path.stat().st_size and not path.read_text().endswith("\n"):
                fh.write("\n")
            for r in new:
                fh.write(json.dumps(r, sort_keys=True, default=str) + "\n")
    return len(new)


def scheduled_games(archive: Path, date_et: str, dev_dry_run: bool = False) -> pd.DataFrame:
    """Every regular-season game of ``date_et`` on the prospective side of the freeze (final or not): the day's eligible set, a public schedule fact."""
    from nhl_edge.market_audit.games import build_games

    g = build_games(archive)
    fz = pd.Timestamp(PROSPECTIVE_FREEZE_UTC)
    after = (g["start_time_utc"] < fz) if dev_dry_run else (g["start_time_utc"] >= fz)
    g = g[(g["season_type"] == "regular") & (g["game_date_et"] == date_et) & after].copy()
    g["game_id"] = g["game_id"].astype(str)
    return g.sort_values(["start_time_utc", "game_id"]).reset_index(drop=True)


def prospective_games(archive: Path, date_et: str, dev_dry_run: bool = False) -> pd.DataFrame:
    """Final games of ``date_et`` that started AFTER the freeze. ``dev_dry_run`` instead selects a DEVELOPMENT-window date so the code path can be exercised without
    touching the prospective tier (the output must go to a scratch ledger, never the real one)."""
    g = scheduled_games(archive, date_et, dev_dry_run)
    return g[g["is_final"]].reset_index(drop=True)


class PlaintextProspectiveLedgerForbidden(RuntimeError):
    """The plaintext ledger path exists only for development-window dry runs. Prospective outcome-bearing rows are sealed (``nhl_edge.sealed_ledger``)."""


def build_rows(archive: Path, date_et: str, repo: Path, dev_dry_run: bool = False) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Derive the ledger rows (in memory only) for the final games of one date, plus an OUTCOME-FREE info dict. Writes nothing."""
    sched = scheduled_games(archive, date_et, dev_dry_run)
    games = sched[sched["is_final"]].reset_index(drop=True)
    info: dict[str, Any] = {"date": date_et, "games_scheduled": int(len(sched)), "games_final": int(len(games)), "scheduled_game_ids": sorted(sched["game_id"]), "final_game_ids": sorted(games["game_id"]),
                            "all_scheduled_final": bool(len(sched)) and bool(sched["is_final"].all())}
    if games.empty:
        return [], {**info, "games_with_pregame_forecast": 0, "missing_pregame_forecast": [], "reproduction_max_abs_diff": None, "note": "no final post-freeze games on this date"}
    slates = build_slate_table(archive, date_et, date_et)
    live = build_live_dataset(archive, 60.0, slates, games)
    live = live[live["v1_lam_home"].notna()].reset_index(drop=True)  # a game without a pre-cut slate run is a data-quality gap, counted below
    params = json.loads((repo / "docs/research/nhl-model-improvement/data/cal_experiments.json").read_text())["c1_frozen_all_wf"]
    mp = AT.moneypuck_2026(archive, last_date="9999")
    d, summ = AT.run(live, mp)
    n = int(live["v1_n_sims"].iloc[0]) if len(live) else 20000
    c1 = [C.apply_c1(params, h + a, h - a) for h, a in zip(live["v1_lam_home"], live["v1_lam_away"], strict=True)]
    P1 = D.simulate_pmfs(np.array([x[0] for x in c1]), np.array([x[1] for x in c1]), live["v1_seed"].to_numpy().astype(int), n_sims=n)
    d = d.set_index("game_id")
    d["c1_p_home_win"] = pd.Series(P1["p_home_win"], index=live["game_id"].to_numpy())
    d = d.reset_index()
    order = {g: i for i, g in enumerate(games["game_id"])}
    rows = sorted(({k: _clean(r.get(k)) for k in LEDGER_FIELDS} for r in d.to_dict("records")), key=lambda r: order.get(str(r["game_id"]), 10**9))
    info.update({"games_with_pregame_forecast": int(len(live)), "missing_pregame_forecast": sorted(set(games["game_id"]) - set(live["game_id"])),
                 "reproduction_max_abs_diff": summ["reproduction_max_abs_diff_p_home_win"]})
    return rows, info


def ingest(archive: Path, date_et: str, repo: Path, ledger: Path, dev_dry_run: bool = False) -> dict[str, Any]:
    """DEVELOPMENT dry run only (plaintext scratch ledger, development-window date). A prospective date is refused: those rows are sealed, never written in clear."""
    if not dev_dry_run:
        raise PlaintextProspectiveLedgerForbidden("prospective rows are never written in plaintext; use `python -m nhl_edge.sealed_ledger.runner ingest`")
    rows, info = build_rows(archive, date_et, repo, dev_dry_run=True)
    if not rows:
        return {"date": date_et, "games": 0, "appended": 0, "note": info.get("note", "")}
    appended = append_rows(ledger, rows)
    return {"date": date_et, "games_final": info["games_final"], "games_with_pregame_forecast": info["games_with_pregame_forecast"], "appended": appended,
            "missing_pregame_forecast": info["missing_pregame_forecast"], "reproduction_max_abs_diff": info["reproduction_max_abs_diff"]}


def scorecard(rows: list[dict[str, Any]], out: Path | None = None) -> dict[str, Any]:
    """Blinded scorecard. Before the first look it contains ONLY counts and PREGAME data-quality measures (sportsbook coverage, slate age): nothing derived from a
    post-freeze outcome (no hit rate, Brier, extreme-miss share, attribution classes or goalie-mismatch share) is printed. Those appear only inside a look."""
    n = len(rows)
    sc: dict[str, Any] = {"n_prospective_games": n, "tier": "PROSPECTIVE", "looks": list(LOOKS)}
    sc["next_look_at_games"] = next((k for k in LOOKS if k > n), None)
    sc["data_quality"] = {"missing_sportsbook_share": sum(1 for r in rows if r.get("sb_p_home") is None) / n if n else None,
                          "mean_slate_age_min": float(np.mean([r["slate_age_min"] for r in rows if r.get("slate_age_min") is not None])) if n else None}
    alarms = []
    if n and sc["data_quality"]["missing_sportsbook_share"] > 0.2:
        alarms.append("WARN: more than 20% of games lack a sportsbook consensus")
    sc["alarms"] = alarms
    reached = [k for k in LOOKS if n >= k]
    if not reached:
        sc["status"] = "ACCUMULATING_BLINDED"
        sc["note"] = "Outcome-derived and model-vs-market measures on the prospective tier are withheld until the first predeclared look (150 games)."
        return sc
    k = max(reached)
    first = rows[:k]
    y = np.array([r["y_home_win"] for r in first], float)
    cols = {"V1": "v1_p_home_win", "V2": "v2_p_home_win", "C1_frozen": "c1_p_home_win", "sportsbook": "sb_p_home"}
    ok = np.array([r.get("sb_p_home") is not None for r in first])
    loss = {name: S.brier(np.array([r[c] if r.get(c) is not None else np.nan for r in first], float), y) for name, c in cols.items()}
    cls: dict[str, int] = {}
    for r in first:
        cls[r["attribution_class"]] = cls.get(r["attribution_class"], 0) + 1
    sc["status"] = f"AT_LOOK_{k}"
    sc["look"] = {"games": k, "brier": {n_: float(np.nanmean(v[ok])) for n_, v in loss.items()},
                  "paired_vs_sportsbook": {n_: S.paired_delta(loss[n_][ok], loss["sportsbook"][ok]) for n_ in ("V1", "V2", "C1_frozen")},
                  "paired_C1_vs_V1": S.paired_delta(loss["C1_frozen"], loss["V1"]),
                  "attribution_class_counts": cls, "extreme_miss_share": sum(v for c, v in cls.items() if not c.startswith("E_")) / k, "extreme_miss_share_expected_if_calibrated": 0.19,
                  "goalie_mismatch_share": float(np.mean([bool(r.get("any_goalie_mismatch")) for r in first])),
                  "note": "first-k games in chronological ledger order; written once"}
    if out is not None:
        look_path = out / f"LOOK_{k}.json"
        if not look_path.exists():  # a look is immutable once taken
            look_path.write_text(json.dumps(sc["look"], indent=1, default=float))
    return sc


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a1 = sub.add_parser("ingest")
    a1.add_argument("--archive", type=Path, required=True)
    a1.add_argument("--date", required=True)
    a1.add_argument("--repo", type=Path, default=Path("."))
    a1.add_argument("--ledger", type=Path, required=True)
    a1.add_argument("--summary-out", type=Path, help="write the (outcome-free) ingest summary here")
    a1.add_argument("--dev-dry-run", action="store_true", help="exercise the code path on a development-window date (scratch ledger only)")
    a2 = sub.add_parser("scorecard")
    a2.add_argument("--ledger", type=Path, required=True)
    a2.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    if a.cmd == "ingest":
        res = ingest(a.archive, a.date, a.repo, a.ledger, a.dev_dry_run)
        print(json.dumps(res, indent=1))
        if a.summary_out:
            a.summary_out.parent.mkdir(parents=True, exist_ok=True)
            a.summary_out.write_text(json.dumps(res, indent=1))
    else:
        a.out.mkdir(parents=True, exist_ok=True)
        sc = scorecard(read_ledger(a.ledger), a.out)
        (a.out / "SHADOW_SCORECARD.json").write_text(json.dumps(sc, indent=1, default=float))
        print(json.dumps(sc, indent=1, default=float))


if __name__ == "__main__":
    main()
