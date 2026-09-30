"""Fit and persist PLAYER_SIM_V1's live parameters (``data/params/player-sim-1.0.json``) from the repository history.

Everything the production shadow arm needs that is estimated rather than read point-in-time: the shot-quality model,
league/position priors, the empty-net / extra-attacker strength table, the saves model and goalie-pull hazards, the
ice-time noise, and the hyper-parameters selected on the 2023-24 validation season (docs/research/PLAYER_SIM_V1.md).
Training seasons are recorded; re-fitting is a new, explicit commit, never a runtime side effect.

Run: ``python -m nhl_edge.players.fit --history data/history --out data/params/player-sim-1.0.json``
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any

from nhl_edge.config import REPO_ROOT
from nhl_edge.data.player_history import load_player_tables
from nhl_edge.players import PLAYER_FEATURE_VERSION, PLAYER_MODEL_VERSION, PLAYER_SIM_VERSION
from nhl_edge.players import xg as X
from nhl_edge.players.features import PlayerParams, build_player_games, league_priors
from nhl_edge.players.params import fit_saves, shot_rates, strength_table, team_game_frame, toi_noise

PARAMS_PATH = REPO_ROOT / "data" / "params" / "player-sim-1.0.json"
TRAIN_SEASONS = [2021, 2022, 2023, 2024, 2025]


def fit_all(history: Path, seasons: list[int] = TRAIN_SEASONS, params: PlayerParams | None = None) -> dict[str, Any]:
    t = {k: load_player_tables(history, k, seasons) for k in ("players", "goalies", "goals", "shots", "team_states")}
    goals = t["goals"][t["goals"]["game_type"] == 2]
    for k in ("goalies", "players"):
        t[k] = t[k][t[k]["game_type"] == 2]
    xg = X.fit(t["shots"][t["shots"]["game_type"] == 2])
    pg = build_player_games(t["players"], goals, t["shots"], t["team_states"], X.score(t["shots"], xg))
    pri = league_priors(pg, goals)
    sig, exit_rate = toi_noise(pg)
    prm = replace(params or PlayerParams(), toi_sigma=sig, p_early_exit=exit_rate)
    for df in (t["goalies"],):
        df["date_int"] = df["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
    tg = team_game_frame(t["goalies"], goals)
    saves = fit_saves(t["goalies"], goals, tg, shot_rates(tg), seasons[-2:])
    return {"model_version": PLAYER_MODEL_VERSION, "sim_version": PLAYER_SIM_VERSION, "feature_version": PLAYER_FEATURE_VERSION,
            "provenance": {"train_seasons": seasons, "game_type": "regular season", "source": "official NHL boxscore + play-by-play + shift charts",
                           "n_player_games": int(len(pg)), "n_goals": int(len(goals))},
            "xg": xg.to_dict(), "priors": pri.to_dict(), "player_params": prm.to_dict(), "strength": strength_table(goals).to_dict(),
            "saves": saves.to_dict(), "league_shots_per_game": float(tg["sa"].mean())}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.players.fit")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", default=str(PARAMS_PATH))
    a = ap.parse_args(argv)
    d = fit_all(Path(a.history))
    Path(a.out).write_text(json.dumps(d, indent=1))
    print(json.dumps(d["provenance"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
