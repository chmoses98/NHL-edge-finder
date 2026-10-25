"""Further development research on ice time on top of WORKLOAD_V1 minutes (RESEARCH_ONLY; development evidence, validates nothing).

The frozen `player-minutes-1.0` specification (usage window = last 3 games, coefficient 0.23) is NOT touched. This asks what a *future, separately registered* version could add: other
recent-usage windows, rest / back-to-back and venue, and a position interaction -- each stacked on WORKLOAD_V1's total ice time, fitted on earlier seasons only, scored on 2024 and 2025
with game-clustered paired intervals (same machinery as ``player_challengers.stack_on``). Seasons 2022-2025 are exposed development seasons; only the write-once prospective records can validate.

    python -m nhl_edge.research.minutes_extra_research --cache <derived cache> --history data/history --out out/minutes_extra.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import player_challengers as PC
from nhl_edge.research import player_diagnosis as PD


def usage_features(champ: pd.DataFrame) -> pd.DataFrame:
    """Per skater-game, from strictly earlier games only: mean ice time over the last 1/3/5/10 games."""
    c = champ.sort_values(["player_id", "date_int", "game_id"]).reset_index(drop=True)
    g = c.groupby("player_id", sort=False)["y_toi"]
    for k in (1, 3, 5, 10):
        c[f"last{k}_toi"] = g.transform(lambda x, k=k: x.shift(1).rolling(k, min_periods=k).mean())
    return c


def rest_features(champ: pd.DataFrame) -> pd.DataFrame:
    """Days of rest for the player's team and for the opponent (calendar days since that team's previous game in the frame; the first game of the frame has none)."""
    tg = champ[["team_id", "game_id", "date_int"]].drop_duplicates().copy()
    tg["day"] = (pd.to_datetime(tg["date_int"].astype(str), format="%Y%m%d") - pd.Timestamp("2000-01-01")).dt.days
    tg = tg.sort_values(["team_id", "day", "game_id"])
    tg["rest"] = tg.groupby("team_id")["day"].diff()
    r = tg[["team_id", "game_id", "rest"]]
    out = champ.merge(r, on=["team_id", "game_id"], how="left").rename(columns={"rest": "team_rest"})
    out = out.merge(r.rename(columns={"team_id": "opp_id", "rest": "opp_rest"}), on=["opp_id", "game_id"], how="left")
    return out


def build(champ: pd.DataFrame, wl: pd.DataFrame) -> pd.DataFrame:
    c = rest_features(usage_features(champ))
    keep = ["game_id", "player_id", "date_int", "pos", "is_home", "team_rest", "opp_rest"] + [f"last{k}_toi" for k in (1, 3, 5, 10)]
    M = wl.merge(c[keep], on=["game_id", "player_id"], how="left").sort_values(["date_int", "game_id"]).reset_index(drop=True)
    for k in (1, 3, 5, 10):
        M[f"u{k}"] = np.log((M[f"last{k}_toi"] + 1.0) / (M["wl_toi"] + 1.0))
    M["b2b"] = (M["team_rest"].fillna(2) <= 1).astype(float)
    M["opp_b2b"] = (M["opp_rest"].fillna(2) <= 1).astype(float)
    M["home"] = M["is_home"].astype(float)
    M["u3_x_D"] = M["u3"].fillna(0) * (M["pos"] == "D").astype(float)
    return M


CANDIDATES: dict[str, list[str]] = {
    "usage last 1 (alone)": ["u1"], "usage last 3 (frozen spec, alone)": ["u3"], "usage last 5 (alone)": ["u5"], "usage last 10 (alone)": ["u10"],
    "usage 3 + 10": ["u3", "u10"], "usage 3 + back-to-back + opponent back-to-back": ["u3", "b2b", "opp_b2b"], "usage 3 + home": ["u3", "home"],
    "usage 3 + usage 3 x defenseman": ["u3", "u3_x_D"],
}


def run(history: Path, cache: Path, prereg: Path, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    wl = PC.workload_frames(history, cache, prereg)
    champ = PD.load_champion(cache).reset_index(drop=True)
    M = build(champ, wl)
    out: dict[str, Any] = {"evidence": "development (exposed seasons 2022-2025): selects nothing that is frozen, validates nothing", "n_rows": int(len(M)), "stacks": {}}
    base = None
    for name, feats in CANDIDATES.items():
        r = PC.stack_on(M, "wl_toi", "y_toi", feats, "sq", (2024, 2025), n_boot=n_boot)
        r["relative_mse_vs_workload"] = r["loss_stack"] / r["loss_base"] - 1.0
        out["stacks"][name] = r
        if name.startswith("usage last 3"):
            base = r
    if base is not None:
        out["frozen_spec_relative_mse"] = base["relative_mse_vs_workload"]
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.minutes_extra_research")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache/derived")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--prereg", default="docs/research/workload_v1/preregistration.json")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    Path(a.out).write_text(json.dumps(run(Path(a.history), Path(a.cache), Path(a.prereg)), indent=1, default=float))
    print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
