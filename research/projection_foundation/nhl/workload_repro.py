"""Reproduce WORKLOAD_V1 skater SOG means (frozen preregistered parameters) for a season, read-only.

Imports the merged production research module `nhl_edge.research.workload_v1` exactly as PR #28 ran it
(constants fitted on seasons before the scored season, params from docs/research/workload_v1/
preregistration.json). Nothing is written outside the gitignored cache.

    PYTHONPATH=../../src python -m nhl.workload_repro 2025
"""
from __future__ import annotations

import json
import sys

import pandas as pd

from .data import CACHE, ROOT


def reproduce(season: int = 2025) -> pd.DataFrame:
    f = CACHE / f"workload_v1_sog_{season}.parquet"
    if f.exists():
        return pd.read_parquet(f)
    sys.path.insert(0, str(ROOT / "src"))
    from nhl_edge.research import workload_v1 as W
    from nhl_edge.research.player_walk_forward import Data

    pre = json.loads((ROOT / "docs" / "research" / "workload_v1" / "preregistration.json").read_text())
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    seasons = [2021, 2022, 2023, 2024, 2025]
    d = Data(ROOT / "data" / "history", seasons)
    tg = W.team_games(d.players, d.team_states, d.shots, d.goals)
    sk = W.skater_table(d.players, tg, d.shots)
    c = W.fit_constants(sk, tg, d.goalies, [s for s in seasons if s < season])
    pred = W.skater_predictions(sk, tg, c, prm)
    pred = pred[(pred["season"] == season) & (pred["game_type"] == 2)]
    out = pred[["game_id", "player_id", "wl_sog", "wl_toi"]].rename(columns={"wl_sog": "inc_sog", "wl_toi": "inc_toi"})
    out.to_parquet(f)
    return out


if __name__ == "__main__":
    r = reproduce(int(sys.argv[1]) if len(sys.argv) > 1 else 2025)
    print(r.shape, r.describe().T)
