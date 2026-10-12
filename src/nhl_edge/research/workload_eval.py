"""Scoring count forecasts (skater shots on goal, goalie saves) for the workload research (RESEARCH_ONLY).

Every arm is a predictive pmf over 0..K-1 (the last cell carries the tail mass). Metrics:

* point:  MAE / RMSE / bias of the predictive MEAN (RMSE is the proper score for a mean; MAE is reported as asked)
* CRPS:   the discrete CRPS (= ranked probability score summed over integer thresholds), sum_k (F(k) - 1{y <= k})^2
* ladder: pooled Brier of P(Y >= t) over the stated thresholds (the Kalshi "N+" shape)
* coverage: expected coverage of the central 50% / 80% intervals under the PIT of a discrete forecast, computed
            exactly (the share of the PIT interval [F(y-1), F(y)] inside [a, 1-a]) instead of with a random draw, so a
            calibrated count forecast scores the nominal value despite discreteness
* game-clustered bootstrap: games are resampled with replacement (one game's skaters / both nets are correlated),
  differences are challenger minus reference (negative = challenger better for every loss here)
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np

# ---------------------------------------------------------------------------------------------------------------------
# predictive distributions
# ---------------------------------------------------------------------------------------------------------------------


def poisson_pmf(mu: np.ndarray, K: int) -> np.ndarray:
    mu = np.maximum(np.asarray(mu, float), 1e-9)
    k = np.arange(K)
    lg = np.array([math.lgamma(j + 1) for j in range(K)])
    logp = k[None, :] * np.log(mu[:, None]) - mu[:, None] - lg[None, :]
    p = np.exp(logp)
    p[:, -1] = np.maximum(1.0 - p[:, :-1].sum(axis=1), 0.0)
    return p


def nb_pmf(mu: np.ndarray, alpha: float, K: int) -> np.ndarray:
    """Negative binomial with mean mu and variance mu + alpha mu^2 (alpha <= 0 -> Poisson)."""
    if alpha <= 1e-9:
        return poisson_pmf(mu, K)
    mu = np.maximum(np.asarray(mu, float), 1e-9)
    r = 1.0 / alpha
    k = np.arange(K)
    lg = np.array([math.lgamma(j + r) - math.lgamma(r) - math.lgamma(j + 1) for j in range(K)])
    logp = lg[None, :] + r * np.log(r / (r + mu[:, None])) + k[None, :] * np.log(mu[:, None] / (r + mu[:, None]))
    p = np.exp(logp)
    p[:, -1] = np.maximum(1.0 - p[:, :-1].sum(axis=1), 0.0)
    return p


def binomial_mixture_pmf(sa_pmf: np.ndarray, p_success: np.ndarray, K: int) -> np.ndarray:
    """pmf of saves when shots ~ sa_pmf (rows) and each shot is saved with probability p_success (per row)."""
    n, S = sa_pmf.shape
    out = np.zeros((n, K))
    lg = np.array([math.lgamma(j + 1) for j in range(S)])
    for s in range(S):
        w = sa_pmf[:, s]
        if not np.any(w > 1e-12):
            continue
        k = np.arange(min(s, K - 1) + 1)
        logc = lg[s] - lg[k] - lg[s - k]
        ps = np.clip(p_success, 1e-9, 1 - 1e-9)
        b = np.exp(logc[None, :] + k[None, :] * np.log(ps[:, None]) + (s - k)[None, :] * np.log1p(-ps[:, None]))
        out[:, : len(k)] += w[:, None] * b
    out[:, -1] += np.maximum(1.0 - out.sum(axis=1), 0.0)
    return out


def fit_nb_alpha(y: np.ndarray, mu: np.ndarray) -> float:
    """Method-of-moments NB2 dispersion on Pearson residuals (as ``players.params.fit_saves``)."""
    y, mu = np.asarray(y, float), np.maximum(np.asarray(mu, float), 1e-6)
    ok = mu > 0.05
    return float(max(np.sum((y[ok] - mu[ok]) ** 2 - mu[ok]) / np.sum(mu[ok] ** 2), 0.0))


# ---------------------------------------------------------------------------------------------------------------------
# per-observation losses
# ---------------------------------------------------------------------------------------------------------------------


def pmf_mean(p: np.ndarray) -> np.ndarray:
    return p @ np.arange(p.shape[1])


def crps_rows(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    F = np.cumsum(p, axis=1)
    y = np.minimum(np.asarray(y, int), p.shape[1] - 1)
    ind = (np.arange(p.shape[1])[None, :] >= y[:, None]).astype(float)
    return ((F - ind) ** 2).sum(axis=1)


def ladder_rows(p: np.ndarray, y: np.ndarray, thresholds: list[int]) -> np.ndarray:
    """Mean over thresholds of the Brier score of P(Y >= t), per row."""
    F = np.cumsum(p, axis=1)
    y = np.asarray(y, int)
    out = np.zeros(len(y))
    for t in thresholds:
        pt = 1.0 - F[:, t - 1] if t >= 1 else np.ones(len(y))
        out += (pt - (y >= t)) ** 2
    return out / len(thresholds)


def pit_coverage_rows(p: np.ndarray, y: np.ndarray, level: float) -> np.ndarray:
    """Expected indicator that the PIT falls in the central ``level`` interval (exact for discrete forecasts)."""
    a = (1.0 - level) / 2.0
    F = np.cumsum(p, axis=1)
    y = np.minimum(np.asarray(y, int), p.shape[1] - 1)
    hi = F[np.arange(len(y)), y]
    lo = np.where(y > 0, F[np.arange(len(y)), np.maximum(y - 1, 0)], 0.0)
    width = np.maximum(hi - lo, 1e-12)
    inter = np.clip(np.minimum(hi, 1 - a) - np.maximum(lo, a), 0.0, None)
    return inter / width


def score_arm(p: np.ndarray, y: np.ndarray, thresholds: list[int]) -> dict[str, np.ndarray]:
    mu = pmf_mean(p)
    e = mu - np.asarray(y, float)
    return {"abs": np.abs(e), "sq": e**2, "err": e, "crps": crps_rows(p, y), "ladder": ladder_rows(p, y, thresholds),
            "cov50": pit_coverage_rows(p, y, 0.5), "cov80": pit_coverage_rows(p, y, 0.8)}


def summarize(rows: dict[str, np.ndarray]) -> dict[str, float]:
    return {"mae": float(rows["abs"].mean()), "rmse": float(np.sqrt(rows["sq"].mean())), "bias": float(rows["err"].mean()),
            "crps": float(rows["crps"].mean()), "ladder_brier": float(rows["ladder"].mean()), "coverage50": float(rows["cov50"].mean()),
            "coverage80": float(rows["cov80"].mean()), "n": int(len(rows["abs"]))}


# ---------------------------------------------------------------------------------------------------------------------
# game-clustered bootstrap of differences
# ---------------------------------------------------------------------------------------------------------------------


def _group_sums(game_ids: np.ndarray, x: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    _, inv = np.unique(game_ids, return_inverse=True)
    return np.bincount(inv, weights=x), np.bincount(inv)


def bootstrap_diff(game_ids: np.ndarray, a: dict[str, np.ndarray], b: dict[str, np.ndarray], n_boot: int = 2000, seed: int = 20261012) -> dict[str, Any]:
    """Challenger ``a`` minus reference ``b``: point estimate and 95% game-clustered percentile CI for MAE, RMSE,
    CRPS, ladder Brier (all: negative = a better), and |bias| (negative = a less biased)."""
    rng = np.random.default_rng(seed)
    _, n_g = _group_sums(game_ids, np.ones(len(game_ids)))
    G = len(n_g)
    sums = {}
    for k in ("abs", "sq", "crps", "ladder", "err"):
        sums[(k, "a")], _ = _group_sums(game_ids, a[k])
        sums[(k, "b")], _ = _group_sums(game_ids, b[k])
    idx = rng.integers(0, G, size=(n_boot, G))
    W = np.zeros((n_boot, G))
    for i in range(n_boot):
        W[i] = np.bincount(idx[i], minlength=G)
    N = W @ n_g

    def stat(kind: str, w: np.ndarray | None = None) -> np.ndarray | float:
        if w is None:
            n = n_g.sum()
            sa, sb = sums[(kind, "a")].sum(), sums[(kind, "b")].sum()
        else:
            n = N
            sa, sb = W @ sums[(kind, "a")], W @ sums[(kind, "b")]
        if kind == "sq":
            return np.sqrt(sa / n) - np.sqrt(sb / n)
        if kind == "err":
            return np.abs(sa / n) - np.abs(sb / n)
        return (sa - sb) / n

    out = {}
    for k, name in (("abs", "mae"), ("sq", "rmse"), ("crps", "crps"), ("ladder", "ladder_brier"), ("err", "abs_bias")):
        bs = stat(k, W)
        out[name] = {"diff": float(stat(k)), "ci95": [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]}
    out["n_obs"] = int(len(game_ids))
    out["n_games"] = int(G)
    out["n_boot"] = int(n_boot)
    return out


def bootstrap_mean_diff(game_ids: np.ndarray, x: np.ndarray, n_boot: int = 2000, seed: int = 20261012) -> dict[str, Any]:
    """Mean of a per-row difference with a game-clustered 95% CI (e.g. absolute TOI error, challenger minus champion)."""
    rng = np.random.default_rng(seed)
    s, n = _group_sums(game_ids, np.asarray(x, float))
    G = len(n)
    bs = np.empty(n_boot)
    for i in range(n_boot):
        j = rng.integers(0, G, G)
        bs[i] = s[j].sum() / n[j].sum()
    return {"diff": float(s.sum() / n.sum()), "ci95": [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))], "n_obs": int(len(x)), "n_games": int(G)}
