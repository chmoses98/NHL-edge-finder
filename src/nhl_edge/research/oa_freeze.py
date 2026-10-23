"""Freeze the live parameters of the ``OA_RIDGE_V1`` shadow arm for one season (RESEARCH_ONLY).

Run once per season start (the "controlled retrain schedule"). Hyper-parameters are selected exactly as in the walk-forward: for target
season S from the two seasons BEFORE S only. The calibration slopes are the state the walk-forward's ``SlopeCalibrator`` reaches after
every game of seasons < S (they are then held fixed for the whole of S, which is slightly more conservative than updating daily).
The output carries its own provenance and a sha256 of the parameters so every prediction row can name the exact parameter set it used.

``python -m nhl_edge.research.oa_freeze --history data/history --games docs/research/oa-walk-forward/data/oa_games.csv.gz --season 2026 --out data/params/oa-ridge-1.0.json``
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.data.history import load_nhl_games, load_team_games
from nhl_edge.research.oa_model import SlopeCalibrator, build_oa_data, select_hyperparameters
from nhl_edge.timeutil import iso, utcnow

PARAMS_VERSION = "oa-ridge-1.0"


def params_sha(p: dict) -> str:
    core = {k: p[k] for k in ("season", "target", "half_life_days", "ridge", "season_discount", "slope_total", "slope_margin", "mean_sum", "mean_diff", "burn_in_games")}
    return hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def freeze(history: Path, games_csv: Path, season: int) -> dict:
    ng = load_nhl_games(history, None)
    final = ng[(ng["game_type"] == 2) & ng["final"].astype(bool)].dropna(subset=["home_score", "away_score"])
    data = build_oa_data(load_team_games(history, None))
    prior = final[final["season"] < season]
    cfg, grid = select_hyperparameters(data, prior, season, target="xg_sva")
    wf = pd.read_csv(games_csv)
    wf = wf[wf["season"] < season].sort_values(["game_date", "game_id"])
    cal = SlopeCalibrator()
    for r in wf.itertuples(index=False):
        cal.observe(str(r.game_date), r.OA_SVA_lam_home, r.OA_SVA_lam_away, float(r.home_score + r.away_score), float(r.home_score - r.away_score))
    b_s, b_d = cal.slopes("9999-12-31")
    out = {"version": PARAMS_VERSION, "season": season, "target": "xg_sva", "half_life_days": cfg.half_life_days, "ridge": cfg.ridge, "season_discount": cfg.season_discount,
           "slope_total": b_s, "slope_margin": b_d, "mean_sum": float(np.mean(cal._s)), "mean_diff": float(np.mean(cal._d)), "burn_in_games": len(cal._s),
           "selected_from_seasons": [season - 2, season - 1], "calibration_games": len(cal._s), "validation_goals_nll": float(grid.iloc[0]["val_goals_nll"]),
           "generated_at_utc": iso(utcnow()), "authority": "RESEARCH_ONLY", "role": "SHADOW"}
    out["sha256"] = params_sha(out)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.oa_freeze")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--games", required=True, help="oa_games.csv (or .gz) from oa_walk_forward covering every season before --season")
    ap.add_argument("--season", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    p = freeze(Path(a.history), Path(a.games), a.season)
    Path(a.out).write_text(json.dumps(p, indent=1))
    print(json.dumps(p, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
