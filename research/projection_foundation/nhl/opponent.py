"""Schedule-adjusted team ratings (pf_core.pit.rolling_ridge_ratings), refitted before every game date.

y = mu + off[team] + def[opponent] + h*home on team-games strictly before the date, previous
seasons down-weighted by 0.5 per season. Ridge alpha (pooling, in games) is chosen on the
development seasons only. The raw comparator is pf_core.pit.rolling_opponent_allowed.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pf_core import pit

from . import SPLITS
from .data import CACHE


def ratings(tg: pd.DataFrame, y: str, alpha: float, seasons=None) -> pd.DataFrame:
    key = f"ridge_{y}_a{alpha:g}" + ("" if seasons is None else "_" + "-".join(map(str, seasons)))
    f = CACHE / f"{key}.parquet"
    if f.exists():
        return pd.read_parquet(f)
    g = tg if seasons is None else tg[tg["season"].isin(seasons)]
    g = g[["game_id", "game_date", "season", "franchise", "opp_franchise", "is_home", y]].copy()
    g["block"] = g["game_date"].dt.strftime("%Y%m%d").astype(int)
    r = pit.rolling_ridge_ratings(g, "block", "franchise", "opp_franchise", y, home_col="is_home", alpha=alpha,
                                  season_col="season", prior_season_decay=0.5, min_rows=40)
    r.to_parquet(f)
    return r


def attach(tg: pd.DataFrame, r: pd.DataFrame, y: str) -> pd.DataFrame:
    """Per team-game: expected y from ratings, opponent defence rating, own offence rating."""
    g = tg[["game_id", "team_id", "game_date", "franchise", "opp_franchise", "is_home"]].copy()
    g["block"] = g["game_date"].dt.strftime("%Y%m%d").astype(int)
    own = r.rename(columns={"team": "franchise", "off_rating": "off", "def_rating": "_d1", "n_off": "n_off",
                            "n_def": "_n1"})[["block", "franchise", "off", "n_off", "intercept", "home_adv"]]
    opp = r.rename(columns={"team": "opp_franchise", "def_rating": "opp_def", "n_def": "opp_n"})[
        ["block", "opp_franchise", "opp_def", "opp_n"]]
    g = g.merge(own, on=["block", "franchise"], how="left").merge(opp, on=["block", "opp_franchise"], how="left")
    g[f"{y}_ridge"] = g["intercept"] + g["off"] + g["opp_def"] + g["home_adv"] * g["is_home"].astype(float)
    # opponent factor relative to the league (multiplicative, for player-level adjustment)
    g[f"{y}_oppf"] = (g["intercept"] + g["opp_def"]) / g["intercept"]
    g[f"{y}_ownf"] = (g["intercept"] + g["off"]) / g["intercept"]
    g[f"{y}_homef"] = (g["intercept"] + g["home_adv"] * g["is_home"].astype(float)) / g["intercept"]
    g = g.rename(columns={"opp_n": f"{y}_opp_n", "intercept": f"{y}_icpt"})
    return g[["game_id", "team_id", f"{y}_ridge", f"{y}_oppf", f"{y}_ownf", f"{y}_homef", f"{y}_opp_n", f"{y}_icpt"]]


def choose_alpha(tg: pd.DataFrame, y: str, grid=(3.0, 10.0, 30.0)) -> tuple[float, list[dict]]:
    """Pick ridge alpha on development seasons only (fit on 2021 + 2022, score 2022 team-games)."""
    dev = SPLITS["development"]
    rows = []
    for a in grid:
        r = ratings(tg, y, a, seasons=dev)
        g = attach(tg[tg["season"].isin(dev)], r, y).merge(tg[["game_id", "team_id", "season", y]], on=["game_id", "team_id"])
        g = g[(g["season"] == dev[-1]) & g[f"{y}_ridge"].notna()]
        rows.append({"alpha": a, "y": y, "n": int(len(g)), "mse": float(np.mean((g[f"{y}_ridge"] - g[y]) ** 2))})
    best = min(rows, key=lambda r: r["mse"])["alpha"]
    return best, rows


def raw_allowed(tg: pd.DataFrame, y: str, k_prior: float = 10.0) -> pd.DataFrame:
    """Raw comparator: opponent's shrunk prior-games mean allowed (season-to-date) / PIT league mean."""
    g = tg[["game_id", "team_id", "opp_id", "game_date", "season", y]].copy()
    # y allowed by the opponent = y for this team; rate is indexed by the defending team
    g = g.rename(columns={"opp_id": "def_team"})
    d = pit.rolling_opponent_allowed(g, "def_team", "game_date", y, k_prior=k_prior, season_col="season")
    return d[["game_id", "team_id", "opp_factor_raw", "opp_n"]].rename(
        columns={"opp_factor_raw": f"{y}_oppf_raw", "opp_n": f"{y}_opp_n_raw"})
