"""Challenger forecasters built ON TOP OF V1 expected goals (never replacing production): each is a pure function of strictly
earlier games, so a rolling-origin evaluation cannot leak. All simulate with the production engine and the production seed.

C1 SCALE       : linear recalibration of the sum s = lam_h + lam_a and the difference d = lam_h - lam_a of regulation expected goals.
C2 SCALE+SIGMA : C1 plus antithetic strength uncertainty on the matchup (lam_h x exp(+sigma z), lam_a x exp(-sigma z)).
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research import dist_eval as D
from nhl_edge.model_research.wf_data import MARGIN_LO, simulate_row
from nhl_edge.sim.engine import SimConfig

B_MIN, B_MAX = 0.2, 2.0
SIGMA_GRID = [0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40]
N_NODES = 8
# equal-probability normal quantile nodes (midpoints of 8 equal-mass bins)
_Z = np.array([-1.5341, -0.8871, -0.4888, -0.1573, 0.1573, 0.4888, 0.8871, 1.5341])


def add_regulation_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Regulation goals: an OT/SO winner is credited one extra goal in the official final, so subtract it."""
    ot = df["y_overtime"].to_numpy().astype(bool)
    hw = (df["home_score"] > df["away_score"]).to_numpy()
    df = df.copy()
    df["reg_h"] = df["home_score"] - (ot & hw).astype(int)
    df["reg_a"] = df["away_score"] - (ot & ~hw).astype(int)
    df["s"] = df["lam_home"] + df["lam_away"]
    df["d"] = df["lam_home"] - df["lam_away"]
    df["reg_s"] = df["reg_h"] + df["reg_a"]
    df["reg_d"] = df["reg_h"] - df["reg_a"]
    return df


def ols(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    xm, ym = x.mean(), y.mean()
    vx = ((x - xm) ** 2).sum()
    b = float(((x - xm) * (y - ym)).sum() / vx) if vx > 0 else 1.0
    return float(ym - b * xm), b


def fit_c1(train: pd.DataFrame) -> dict[str, float]:
    a_s, b_s = ols(train["s"].to_numpy(), train["reg_s"].to_numpy())
    a_d, b_d = ols(train["d"].to_numpy(), train["reg_d"].to_numpy())
    b_s, b_d = float(np.clip(b_s, B_MIN, B_MAX)), float(np.clip(b_d, B_MIN, B_MAX))
    sbar, dbar = float(train["s"].mean()), float(train["d"].mean())
    # re-centre with the clipped slope so the fitted line still passes through the training means
    return {"s_mean_target": float(train["reg_s"].mean()), "sbar": sbar, "b_s": b_s, "d_mean_target": float(train["reg_d"].mean()), "dbar": dbar, "b_d": b_d,
            "raw_b_s": a_s and float(ols(train["s"].to_numpy(), train["reg_s"].to_numpy())[1]), "raw_b_d": float(ols(train["d"].to_numpy(), train["reg_d"].to_numpy())[1]),
            "n_train": int(len(train))}


def apply_c1(p: dict[str, float], s: float, d: float) -> tuple[float, float]:
    s2 = p["s_mean_target"] + p["b_s"] * (s - p["sbar"])
    d2 = p["d_mean_target"] + p["b_d"] * (d - p["dbar"])
    s2 = max(s2, 2.0)
    d2 = float(np.clip(d2, -(s2 - 0.4), s2 - 0.4))
    return (s2 + d2) / 2, (s2 - d2) / 2


def simulate_noisy(lam_h: float, lam_a: float, seed: int, sigma: float, n_total: int = 4000) -> Any:
    """Mixture over 8 equal-mass strength nodes (antithetic); returns concatenated arrays wrapped like a SimResult."""
    from types import SimpleNamespace

    per = n_total // N_NODES
    parts = []
    for k, z in enumerate(_Z):
        parts.append(simulate_row(lam_h * np.exp(sigma * z), lam_a * np.exp(-sigma * z), seed + 1000003 * k, per, SimConfig(n_sims=per)))
    cat = {a: np.concatenate([getattr(p, a) for p in parts]) for a in ("home_final", "away_final", "overtime", "shootout")}
    return SimpleNamespace(n_sims=per * N_NODES, total=cat["home_final"] + cat["away_final"], margin=cat["home_final"] - cat["away_final"], **cat)


def rolling_c1(df: pd.DataFrame, burn_in: int = 300) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    """Per-game C1 expected goals using only strictly earlier DATES. Returns the frame with lam1_home/lam1_away and a parameter trace."""
    df = add_regulation_columns(df).reset_index(drop=True)
    lam1_h = np.full(len(df), np.nan)
    lam1_a = np.full(len(df), np.nan)
    trace: list[dict[str, Any]] = []
    for date, idx in df.groupby("game_date", sort=True).indices.items():
        prior = df[df["game_date"] < date]
        if len(prior) < burn_in:
            continue
        p = fit_c1(prior)
        trace.append({"date": str(pd.Timestamp(date).date()), **p})
        for i in idx:
            lam1_h[i], lam1_a[i] = apply_c1(p, df.at[i, "s"], df.at[i, "d"])
    df["lam1_home"], df["lam1_away"] = lam1_h, lam1_a
    return df, trace


def sigma_by_date(df: pd.DataFrame, margin_logpmf: dict[float, np.ndarray], burn_in: int = 300) -> tuple[np.ndarray, list[dict[str, Any]]]:
    """Rolling sigma: grid value maximising the margin log score of strictly earlier games (``margin_logpmf[sigma][i]`` = log pmf of game i's margin)."""
    sig = np.full(len(df), np.nan)
    trace = []
    for date, idx in df.groupby("game_date", sort=True).indices.items():
        prior = np.where(df["game_date"].to_numpy() < date)[0]
        if len(prior) < burn_in:
            continue
        scores = {s: float(margin_logpmf[s][prior].sum()) for s in SIGMA_GRID}
        best = max(scores, key=lambda k: scores[k])
        sig[idx] = best
        trace.append({"date": str(pd.Timestamp(date).date()), "sigma": best, "n_prior": int(len(prior))})
    return sig, trace


def margin_logpmf(P: dict[str, np.ndarray], y_margin: np.ndarray) -> np.ndarray:
    k = np.clip(y_margin, -10, 10) - MARGIN_LO
    return np.log(np.maximum(P["margin"][np.arange(len(k)), k], 1e-4))


D_ = D  # re-export for convenience
