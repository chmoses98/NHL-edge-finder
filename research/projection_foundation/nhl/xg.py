"""Expected-goals (shot quality) model on official play-by-play unblocked attempts.

Logistic regression on distance, angle, shot type, strength, rebound and behind-the-net,
fitted on DEVELOPMENT seasons only (2021-22, 2022-23) and then frozen. Applied to every
season, it turns the shots table into per-player-game individual xG (ixG) — a lower-variance
shooting signal than goals — and per-team-game xG for/against.

Leakage: the coefficients are fitted on development outcomes, so ixG features inside the
development seasons are in-sample (a mild optimism confined to development); validation,
holdout and prospective seasons use a model that never saw them.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from . import SPLITS
from .data import shot_frame

TYPES = ["wrist", "snap", "slap", "tip-in", "backhand", "deflected", "wrap-around", "unknown"]
STRENGTHS = ["EV", "PP", "SH", "EA", "EN"]


def design(s: pd.DataFrame) -> np.ndarray:
    d = s["dist"].to_numpy(float)
    cols = [np.log1p(d), d / 100.0, s["angle"].to_numpy(float) / 90.0, s["rebound"].to_numpy(float),
            s["behind"].to_numpy(float), (s["rebound"] * s["angle"] / 90.0).to_numpy(float)]
    st = s["shot_type"].where(s["shot_type"].isin(TYPES), "unknown")
    cols += [(st == t).to_numpy(float) for t in TYPES[1:]]
    cols += [(s["strength"] == k).to_numpy(float) for k in STRENGTHS[1:]]
    return np.column_stack(cols)


def fit_and_score(seasons=None) -> tuple[pd.DataFrame, dict]:
    s = shot_frame() if seasons is None else shot_frame(tuple(seasons))
    dev = s["season"].isin(SPLITS["development"]).to_numpy()
    X = design(s)
    m = LogisticRegression(C=1.0, max_iter=500)
    m.fit(X[dev], s.loc[dev, "is_goal"])
    s["xg"] = m.predict_proba(X)[:, 1]
    rep = {}
    for sp in ("development", "validation", "holdout", "prospective"):
        mm = s["season"].isin(SPLITS[sp]).to_numpy()
        if mm.sum() == 0:
            continue
        y = s.loc[mm, "is_goal"].to_numpy()
        p = np.clip(s.loc[mm, "xg"].to_numpy(), 1e-6, 1 - 1e-6)
        base = np.clip(s.loc[dev, "is_goal"].mean(), 1e-6, 1)
        rep[sp] = {"n_attempts": int(mm.sum()), "goals": int(y.sum()), "xg_sum": float(p.sum()),
                   "log_loss": float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p))),
                   "log_loss_constant": float(-np.mean(y * np.log(base) + (1 - y) * np.log(1 - base)))}
    return s, rep


def player_xg(s: pd.DataFrame) -> pd.DataFrame:
    s = s.assign(xg_pp=np.where(s["strength"] == "PP", s["xg"], 0.0))
    return (s.groupby(["game_id", "shooter_id"]).agg(ixg=("xg", "sum"), ixg_pp=("xg_pp", "sum"))
            .reset_index().rename(columns={"shooter_id": "player_id"}))


def team_xg(s: pd.DataFrame) -> pd.DataFrame:
    return s.groupby(["game_id", "team_id"]).agg(xg_for=("xg", "sum")).reset_index()
