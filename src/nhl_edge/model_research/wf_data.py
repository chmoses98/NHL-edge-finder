"""Walk-forward game tables (2024 and 2025 regular seasons, 2,624 games): the largest chronologically valid model-only sample.

``docs/research/walk_forward_*_games.csv`` are committed outputs of the production walk-forward (every parameter fitted on
earlier seasons only). ``lam_home`` / ``lam_away`` / ``seed`` regenerate the V1 predictive distribution bit-for-bit.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.sim.engine import SimConfig, SimResult, TeamParams, simulate_game

V1_CSV = "docs/research/walk_forward_36570274279_games.csv"
V2_CSV = "docs/research/walk_forward_v2_wf2_20260929_games.csv"

MAX_TOTAL = 20
MAX_GOALS = 14
MARGIN_LO, MARGIN_HI = -10, 10


def load_wf(repo: Path) -> pd.DataFrame:
    v1 = pd.read_csv(repo / V1_CSV)
    v2 = pd.read_csv(repo / V2_CSV)
    assert (v1["game_id"].to_numpy() == v2["game_id"].to_numpy()).all()
    keep_v2 = [c for c in v2.columns if c.startswith(("SIM2_ST_", "lam_st_", "V2_")) or c in ("home_starter", "away_starter", "home_gtt", "away_gtt")]
    df = pd.concat([v1, v2[keep_v2]], axis=1)
    df["game_date"] = pd.to_datetime(df["game_date"])
    df = df.sort_values(["game_date", "game_id"]).reset_index(drop=True)
    df["margin"] = df["home_score"] - df["away_score"]
    return df


def simulate_row(lam_h: float, lam_a: float, seed: int, n_sims: int = 4000, cfg: SimConfig | None = None) -> SimResult:
    return simulate_game(TeamParams(0, "H", float(lam_h)), TeamParams(1, "A", float(lam_a)), int(seed), cfg or SimConfig(n_sims=n_sims))


def pmfs(res: SimResult) -> dict[str, np.ndarray]:
    n = res.n_sims
    tot = np.minimum(res.total, MAX_TOTAL - 1)
    mar = np.clip(res.margin, MARGIN_LO, MARGIN_HI) - MARGIN_LO
    return {
        "total": np.bincount(tot, minlength=MAX_TOTAL) / n,
        "home": np.bincount(np.minimum(res.home_final, MAX_GOALS - 1), minlength=MAX_GOALS) / n,
        "away": np.bincount(np.minimum(res.away_final, MAX_GOALS - 1), minlength=MAX_GOALS) / n,
        "margin": np.bincount(mar, minlength=MARGIN_HI - MARGIN_LO + 1) / n,
        "p_home_win": float((res.home_final > res.away_final).mean()),
        "p_ot": float(res.overtime.mean()),
        "p_so": float(res.shootout.mean()),
    }
