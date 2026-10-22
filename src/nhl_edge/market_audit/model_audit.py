"""Model-vs-market audit (Phase E). Same games, same instant (T-60m), same outcomes for every forecaster.

Measures, per market family:
* Brier and log loss of model, market mid, and the market-anchored blend;
* paired difference model - market with a game-clustered bootstrap CI (negative = model better);
* incremental information: logistic ``y ~ offset(logit(mid)) + c * (logit(p_model) - logit(mid))`` with game-clustered SE
  (c = 0: the model adds nothing beyond the market; c = 1: the model's disagreement is fully right);
* reliability of the model in 5 equal-count bins (model p vs frequency).

A model that is worse than the market on Brier AND adds no incremental information is reported as exactly that.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import cluster_ratio_ci


def _logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-3, 1 - 1e-3)
    return np.log(p / (1 - p))


def anchored(p_model: np.ndarray, p_mid: np.ndarray, w: float = 0.8) -> np.ndarray:
    z = w * _logit(p_mid) + (1 - w) * _logit(p_model)
    return 1 / (1 + np.exp(-z))


def incremental_info(d: pd.DataFrame, pcol: str) -> dict[str, float]:
    import statsmodels.api as sm

    x = (_logit(d[pcol].to_numpy()) - _logit(d["mid"].to_numpy()))
    off = _logit(d["mid"].to_numpy())
    if len(d) < 30 or np.std(x) < 1e-9:
        return {"c": np.nan, "se": np.nan, "z": np.nan}
    fit = sm.GLM(d["y"].to_numpy(), sm.add_constant(x), family=sm.families.Binomial(), offset=off).fit(
        cov_type="cluster", cov_kwds={"groups": d["game_id"].to_numpy()})
    return {"c": float(fit.params[1]), "se": float(fit.bse[1]), "z": float(fit.params[1] / fit.bse[1])}


def compare(d: pd.DataFrame, pcol: str, label: str) -> dict[str, Any]:
    d = d[d[pcol].notna()].copy()
    if d.empty:
        return {"label": label, "n_contracts": 0, "n_games": 0}
    d["se_model"] = (d[pcol] - d["y"]) ** 2
    d["se_mid"] = (d["mid"] - d["y"]) ** 2
    d["se_anch"] = (anchored(d[pcol].to_numpy(), d["mid"].to_numpy()) - d["y"]) ** 2
    d["dB"] = d["se_model"] - d["se_mid"]
    d["dB_anch"] = d["se_anch"] - d["se_mid"]
    pm = d[pcol].clip(1e-3, 1 - 1e-3)
    d["ll_model"] = -(d["y"] * np.log(pm) + (1 - d["y"]) * np.log(1 - pm))
    mm = d["mid"].clip(1e-3, 1 - 1e-3)
    d["ll_mid"] = -(d["y"] * np.log(mm) + (1 - d["y"]) * np.log(1 - mm))
    d["dLL"] = d["ll_model"] - d["ll_mid"]
    dB = cluster_ratio_ci(d, "dB", None)
    dBa = cluster_ratio_ci(d, "dB_anch", None)
    dLL = cluster_ratio_ci(d, "dLL", None)
    out = {"label": label, "n_contracts": int(len(d)), "n_games": int(d["game_id"].nunique()),
           "brier_model": float(d["se_model"].mean()), "brier_market": float(d["se_mid"].mean()), "brier_anchored": float(d["se_anch"].mean()),
           "d_brier_model_minus_market": dB[0], "d_brier_lo95": dB[1], "d_brier_hi95": dB[2],
           "d_brier_anchored_minus_market": dBa[0], "d_brier_anch_lo95": dBa[1], "d_brier_anch_hi95": dBa[2],
           "d_logloss_model_minus_market": dLL[0], "d_logloss_lo95": dLL[1], "d_logloss_hi95": dLL[2],
           "mean_abs_disagreement": float((d[pcol] - d["mid"]).abs().mean()), "incremental": incremental_info(d, pcol)}
    try:
        d["bin"] = pd.qcut(d[pcol], 5, duplicates="drop")
        out["reliability"] = [{"bin": str(b), "n": int(len(x)), "mean_p": float(x[pcol].mean()), "freq": float(x["y"].mean()),
                               "mean_market": float(x["mid"].mean())} for b, x in d.groupby("bin", observed=True)]
    except ValueError:
        out["reliability"] = []
    return out
