"""Shot-quality (expected goals) model for PLAYER_SIM_V1, fit on official play-by-play shot coordinates.

Why our own xG: MoneyPuck's shot file is historical only (no live per-game feed here), and the live settle job stores
the same official play-by-play rows the history pull does, so one model scores both identically.

Unblocked attempts (goal / shot-on-goal / missed) with the opponent's goalie in net. Features: distance and angle to
the attacked net (``|x|`` folds both ends; the NHL feed puts nets at x = +-89), their logs, shot type, rebound (the
same team's previous attempt <= 3 s earlier), and strength (PP / SH / EA vs EV). Logistic regression by IRLS with a
small ridge penalty; coefficients are stored with their training seasons. Blocked attempts get no xG (no location
quality is recorded for the shooter); empty-net attempts are excluded (their conversion is modelled separately).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np
import pandas as pd

SHOT_TYPES = ("wrist", "snap", "slap", "backhand", "tip-in", "deflected", "wrap-around")
STRENGTHS = ("PP", "SH", "EA")


def design(shots: pd.DataFrame) -> np.ndarray:
    x = pd.to_numeric(shots["x"], errors="coerce").fillna(60.0).abs().clip(upper=99.0).to_numpy(float)
    y = pd.to_numeric(shots["y"], errors="coerce").fillna(0.0).abs().to_numpy(float)
    dx = np.abs(89.0 - x)
    dist = np.sqrt(dx**2 + y**2).clip(1.0, 200.0)
    ang = np.arctan2(y, np.maximum(89.0 - x, 0.5))
    behind = (x > 89.0).astype(float)
    reb = pd.to_numeric(shots.get("since_prev_s"), errors="coerce").fillna(999).to_numpy(float) <= 3.0
    st = shots.get("shot_type", pd.Series([None] * len(shots))).astype(str).str.lower().to_numpy()
    strength = shots.get("strength", pd.Series(["EV"] * len(shots))).astype(str).to_numpy()
    cols = [np.ones(len(shots)), np.log(dist), dist / 30.0, ang, ang**2, behind, reb.astype(float)]
    cols += [(st == t).astype(float) for t in SHOT_TYPES[1:]]
    cols += [(strength == s).astype(float) for s in STRENGTHS]
    cols += [reb * ang]
    return np.column_stack(cols)


@dataclass
class XGModel:
    coef: np.ndarray
    train_seasons: list[int] = field(default_factory=list)
    n_train: int = 0
    base_rate: float = 0.0

    def predict(self, shots: pd.DataFrame) -> np.ndarray:
        if not len(shots):
            return np.zeros(0)
        z = design(shots) @ self.coef
        return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))

    def to_dict(self) -> dict[str, Any]:
        return {"coef": [float(c) for c in self.coef], "train_seasons": self.train_seasons, "n_train": self.n_train, "base_rate": self.base_rate,
                "features": "1,log_dist,dist/30,angle,angle^2,behind_net,rebound," + ",".join(SHOT_TYPES[1:]) + "," + ",".join(STRENGTHS) + ",rebound*angle"}

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> XGModel:
        return cls(np.asarray(d["coef"], float), list(d.get("train_seasons") or []), int(d.get("n_train") or 0), float(d.get("base_rate") or 0.0))


def model_rows(shots: pd.DataFrame) -> pd.DataFrame:
    """Unblocked, non-empty-net, non-shootout attempts with a known location."""
    s = shots[shots["kind"].isin(["GOAL", "SOG", "MISS"]) & (shots["strength"] != "EN")]
    return s[s["x"].notna() & s["y"].notna()]


def fit(shots: pd.DataFrame, seasons: list[int] | None = None, ridge: float = 1.0, iters: int = 30) -> XGModel:
    s = model_rows(shots)
    X = design(s)
    y = (s["kind"] == "GOAL").to_numpy(float)
    w = np.zeros(X.shape[1])
    w[0] = np.log(y.mean() / (1 - y.mean()))
    lam = np.full(X.shape[1], ridge)
    lam[0] = 0.0
    for _ in range(iters):
        p = 1.0 / (1.0 + np.exp(-np.clip(X @ w, -30, 30)))
        W = p * (1 - p)
        g = X.T @ (y - p) - lam * w
        H = (X * W[:, None]).T @ X + np.diag(lam)
        step = np.linalg.solve(H, g)
        w += step
        if np.abs(step).max() < 1e-7:
            break
    return XGModel(w, sorted(int(x) for x in s["season"].unique()) if "season" in s.columns else (seasons or []), int(len(s)), float(y.mean()))


def score(shots: pd.DataFrame, model: XGModel) -> pd.Series:
    """xG for every attempt row (0 for blocked, empty-net handled by the caller)."""
    out = pd.Series(0.0, index=shots.index)
    m = model_rows(shots)
    if len(m):
        out.loc[m.index] = model.predict(m)
    return out
