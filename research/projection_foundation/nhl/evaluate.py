"""Scoring helpers: point + distribution metrics, game-clustered comparisons, calibration.

All metrics are on independent player-games (one row per player-game-family), clusters are games.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pf_core import dists, metrics, models

THRESHOLDS = {
    "sog": [2, 3, 4, 5], "goals": [1, 2], "assists": [1, 2], "points": [1, 2, 3], "saves": [20, 25, 30],
    "team_goals": [2, 3, 4, 5], "game_total": [5, 6, 7], "toi": [], "toi_pp": [],
}
SUPPORT_K = {"sog": 20, "goals": 8, "assists": 8, "points": 10, "saves": 70, "team_goals": 16, "game_total": 25}


def fit_dist(kind: str, y, mu, family: str) -> dict:
    K = SUPPORT_K[family]
    p = models.fit_dist_params(kind, y, mu, K=K, lo=0, n_bins=6)
    p["K"] = K
    return p


def make(params: dict, mu) -> dists.DistBatch:
    return models.make_dist(params, np.maximum(np.asarray(mu, float), 1e-4))


def score(y, mu, dparams: dict, family: str) -> tuple[dict, np.ndarray]:
    """Return (metrics dict, per-row CRPS)."""
    y = np.asarray(y, float)
    mu = np.asarray(mu, float)
    d = make(dparams, mu)
    pm = metrics.point_metrics(y, mu)
    dm = metrics.dist_metrics(y, d, thresholds=THRESHOLDS.get(family) or None)
    out = {**pm, **dm}
    crps = d.crps(y)
    out["zero_mass_pred"] = float(d.P[:, 0].mean())
    out["zero_mass_obs"] = float((y == 0).mean())
    return out, crps


def sq(y, mu):
    return (np.asarray(mu, float) - np.asarray(y, float)) ** 2


def compare(loss_a, loss_b, clusters, n_boot=1000) -> dict:
    r = metrics.cluster_bootstrap_diff(loss_a, loss_b, clusters, n_boot=n_boot)
    return {"mean_diff": round(r["mean_diff"], 6), "ci95": [round(x, 6) for x in r["ci95"]],
            "n_obs": r["n_obs"], "n_clusters": r["n_clusters"]}


def brier_rows(p, y, k):
    o = (np.asarray(y) >= k).astype(float)
    return (np.asarray(p, float) - o) ** 2


def calib_threshold(d: dists.DistBatch, y, k, bins=10) -> dict:
    p = d.prob_ge(k)
    o = (np.asarray(y) >= k).astype(float)
    return {"k": k, "ece": metrics.ece(p, o, bins), "table": metrics.calibration_table(p, o, bins)}


def model_row(model: str, split: str, y, mu, dparams, family, clusters, crps_base=None, crps_inc=None,
              verdict="") -> dict:
    m, crps = score(y, mu, dparams, family)
    row = {"model": model, "split": split, "n_obs": int(len(y)), "n_clusters": int(pd.Series(clusters).nunique()),
           "mae": m["mae"], "rmse": m["rmse"], "bias": m["bias"], "crps": m["crps"], "log_score": m["log_score"],
           "cover_50": m["cover_50"], "cover_80": m["cover_80"], "cover_90": m["cover_90"],
           "pit_var_ratio": m["pit_var_ratio"], "vs_baseline": None, "vs_incumbent": None, "verdict": verdict,
           "_thresholds": m.get("thresholds", {}), "_zero": [m["zero_mass_pred"], m["zero_mass_obs"]]}
    if crps_base is not None:
        row["vs_baseline"] = compare(crps, crps_base, clusters)
    if crps_inc is not None:
        row["vs_incumbent"] = compare(crps, crps_inc, clusters)
    return row, crps
