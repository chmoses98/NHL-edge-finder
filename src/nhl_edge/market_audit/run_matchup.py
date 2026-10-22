"""Run the matchup-factor study. Blocks are declared here and committed BEFORE results were computed.

``python -m nhl_edge.market_audit.run_matchup --derived <dir> --history <data/history> --teams-csv <teams.csv> --out <json>``
"""

from __future__ import annotations

import argparse
import json
import warnings
from pathlib import Path

import pandas as pd

from nhl_edge.market_audit import matchup_study as M

DISC_CUT = "2026-01-21"  # same chronological split as the hypothesis registry (first 60% of games / last 40%)
WINNER_BLOCKS = {
    "W1_oa_xg": ["oa_xg_diff"],
    "W2_rest_travel": ["rest_diff", "b2b_home", "b2b_away", "tz_away"],
    "W3_finishing_specialteams": ["fin_diff", "pp_edge"],
    "W4_all": ["oa_xg_diff", "rest_diff", "b2b_home", "b2b_away", "tz_away", "fin_diff", "pp_edge"],
}
TOTAL_BLOCKS = {
    "T1_oa_exp_total": ["oa_exp_total"],
    "T2_b2b_travel": ["b2b_home", "b2b_away", "tz_away"],
    "T3_all": ["oa_exp_total", "b2b_home", "b2b_away", "tz_away"],
}


def run(derived: Path, history: Path, teams_csv: Path) -> dict:
    warnings.filterwarnings("ignore")
    games = pd.concat([pd.read_parquet(history / "nhl" / f"games_{y}.parquet") for y in (2024, 2025)])
    feats = M.build_features(history, games, teams_csv)
    p = pd.read_parquet(derived / "hist_reg_panel.parquet")
    p = p[(p["horizon_min"] == 60) & (p["game_date"] >= "2025-10-01") & (p["game_date"] <= "2026-04-17")]
    p = p.merge(feats, on="game_id", how="inner")
    out: dict[str, dict] = {}
    w = p[(p["kind"] == "winner") & (p["subject_team_id"] == p["home_team_id"])]
    for name, cols in WINNER_BLOCKS.items():
        out[name] = M.incremental_test(w, cols, name, DISC_CUT)
    t = p[p["kind"] == "total"]
    for name, cols in TOTAL_BLOCKS.items():
        out[name] = M.incremental_test(t, cols, name, DISC_CUT)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--history", type=Path, required=True)
    ap.add_argument("--teams-csv", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    res = run(a.derived, a.history, a.teams_csv)
    a.out.write_text(json.dumps(res, indent=1, default=float))
    for k, v in res.items():
        print(k, "disc/hold games", v["n_disc_games"], v["n_hold_games"], f"block Wald p={v['wald_p_block']:.3f}",
              f"OOS dLL={v['oos_delta_logloss_vs_market']:.5f} [{v['oos_dll_lo95']:.5f}, {v['oos_dll_hi95']:.5f}]")
        print("   z:", {f: round(z, 2) for f, z in v["beta_z"].items()})
