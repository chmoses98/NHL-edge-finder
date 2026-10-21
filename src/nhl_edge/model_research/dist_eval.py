"""Distribution-level evaluation of a set of per-game predictive distributions against realised scores."""

from __future__ import annotations

import math
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.wf_data import MARGIN_HI, MARGIN_LO, MAX_GOALS, MAX_TOTAL, pmfs, simulate_row


def simulate_pmfs(lam_h: np.ndarray, lam_a: np.ndarray, seeds: np.ndarray, n_sims: int = 4000, cfg: Any = None, tf: Any = None) -> dict[str, np.ndarray]:
    """Per-game predictive pmfs (one row per game) from the V1 engine; ``tf`` may transform the SimResult (e.g. strength noise)."""
    n = len(lam_h)
    out = {"total": np.zeros((n, MAX_TOTAL)), "home": np.zeros((n, MAX_GOALS)), "away": np.zeros((n, MAX_GOALS)),
           "margin": np.zeros((n, MARGIN_HI - MARGIN_LO + 1)), "p_home_win": np.zeros(n), "p_ot": np.zeros(n), "p_so": np.zeros(n),
           "mu_total": np.zeros(n), "var_total": np.zeros(n), "mu_margin": np.zeros(n), "var_margin": np.zeros(n)}
    for i in range(n):
        res = simulate_row(lam_h[i], lam_a[i], seeds[i], n_sims, cfg)
        if tf is not None:
            res = tf(res, i)
        p = pmfs(res)
        for k in ("total", "home", "away", "margin"):
            out[k][i] = p[k]
        out["p_home_win"][i], out["p_ot"][i], out["p_so"][i] = p["p_home_win"], p["p_ot"], p["p_so"]
        out["mu_total"][i], out["var_total"][i] = res.total.mean(), res.total.var()
        out["mu_margin"][i], out["var_margin"][i] = res.margin.mean(), res.margin.var()
    return out


def tail_prob(pm: np.ndarray, lo: int) -> np.ndarray:
    return pm[:, lo:].sum(axis=1)


def margin_tail(pm: np.ndarray, k: int) -> np.ndarray:
    off = -MARGIN_LO
    return pm[:, : off - k + 1].sum(axis=1) + pm[:, off + k :].sum(axis=1)


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    ph = k / n
    den = 1 + z * z / n
    c = (ph + z * z / (2 * n)) / den
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
    return c - h, c + h


def describe(P: dict[str, np.ndarray], df: pd.DataFrame, seed: int = 0) -> dict[str, Any]:
    """Descriptive fidelity statistics of the predictive distribution (independent unit: the game)."""
    y_t = df["y_total"].to_numpy()
    y_h, y_a = df["home_score"].to_numpy(), df["away_score"].to_numpy()
    y_m = df["margin"].to_numpy()
    n = len(df)
    z2 = (y_t - P["mu_total"]) ** 2 / P["var_total"]
    z2m = (y_m - P["mu_margin"]) ** 2 / P["var_margin"]
    out: dict[str, Any] = {"n_games": n}
    m, lo, hi = S.boot_mean_ci(z2, seed=seed)
    out["total_z2"] = {"mean": m, "lo95": lo, "hi95": hi, "note": "(y-mu)^2/sigma^2; 1 = right width, <1 = predictive distribution too WIDE"}
    m, lo, hi = S.boot_mean_ci(z2m, seed=seed)
    out["margin_z2"] = {"mean": m, "lo95": lo, "hi95": hi}
    out["mean_total"] = {"pred": float(P["mu_total"].mean()), "obs": float(y_t.mean())}
    out["var_total"] = {"pred_mean_var": float(P["var_total"].mean()), "obs_var": float(y_t.var(ddof=1))}
    tails: dict[str, Any] = {}
    for k in (6, 7, 8, 9, 10):
        pr = tail_prob(P["total"], k)
        ob = int((y_t >= k).sum())
        l, h = wilson(ob, n)
        tails[f"total>={k}"] = {"pred": float(pr.mean()), "obs": ob / n, "obs_lo95": l, "obs_hi95": h, "obs_in_ci_of_pred": bool(l <= pr.mean() <= h)}
    for k in (1, 2, 3, 4, 5):
        pr = margin_tail(P["margin"], k)
        ob = int((np.abs(y_m) >= k).sum())
        l, h = wilson(ob, n)
        tails[f"|margin|>={k}"] = {"pred": float(pr.mean()), "obs": ob / n, "obs_lo95": l, "obs_hi95": h, "obs_in_ci_of_pred": bool(l <= pr.mean() <= h)}
    ob = int(((y_h == 0) | (y_a == 0)).sum())
    pr = (P["home"][:, 0] + P["away"][:, 0] - P["home"][:, 0] * P["away"][:, 0])  # independence only approximately; descriptive
    l, h = wilson(ob, n)
    tails["shutout(either)"] = {"pred_indep_approx": float(pr.mean()), "obs": ob / n, "obs_lo95": l, "obs_hi95": h}
    tails["overtime"] = {"pred": float(P["p_ot"].mean()), "obs": float(df["y_overtime"].mean()), "obs_lo95": wilson(int(df["y_overtime"].sum()), n)[0],
                         "obs_hi95": wilson(int(df["y_overtime"].sum()), n)[1]}
    out["tails"] = tails
    rng = np.random.default_rng(seed)
    for k in ("total", "home", "away", "margin"):
        y = {"total": y_t, "home": y_h, "away": y_a, "margin": y_m - MARGIN_LO}[k]
        u = S.pit_randomized(P[k], y, rng)
        out[f"pit_{k}"] = {"deciles": np.histogram(u, bins=10, range=(0, 1))[0].tolist(), "mean": float(u.mean()), "expected_mean": 0.5,
                           "chi2_10bin": float(((np.histogram(u, bins=10, range=(0, 1))[0] - n / 10) ** 2 / (n / 10)).sum()), "chi2_crit_95_df9": 16.92}
    out["rps"] = {k: float(S.rps_from_pmf(P[k], {"total": y_t, "home": y_h, "away": y_a, "margin": y_m - MARGIN_LO}[k]).mean()) for k in ("total", "home", "away", "margin")}
    ho, hl = df["home_score"].corr(df["away_score"]), None
    out["observed_home_away_goal_corr"] = float(ho)
    del hl
    return out
