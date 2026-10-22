"""Proper scoring rules and game-clustered paired bootstrap (all intervals resample GAMES, never contracts)."""

from __future__ import annotations

import math
from collections.abc import Callable

import numpy as np

EPS = 1e-6


def brier(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    return (np.asarray(p, float) - np.asarray(y, float)) ** 2


def logloss(p: np.ndarray, y: np.ndarray) -> np.ndarray:
    p = np.clip(np.asarray(p, float), EPS, 1 - EPS)
    y = np.asarray(y, float)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def logit(p: np.ndarray | float) -> np.ndarray:
    p = np.clip(np.asarray(p, float), EPS, 1 - EPS)
    return np.log(p / (1 - p))


def expit(x: np.ndarray | float) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.asarray(x, float)))


def rps_from_pmf(pmf: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Ranked probability score = discrete CRPS on integer support 0..K-1 (``pmf`` is n x K, mass beyond K-1 pooled in the last bin).

    CRPS(F, y) = sum_k (F(k) - 1{y <= k})^2 for integer-valued y, so it is in goals (lower is better) and comparable with MAE.
    """
    cdf = np.cumsum(pmf, axis=1)
    k = np.arange(pmf.shape[1])[None, :]
    ind = (np.asarray(y)[:, None] <= k).astype(float)
    return ((cdf - ind) ** 2).sum(axis=1)


def pit_randomized(pmf: np.ndarray, y: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Randomised PIT for discrete forecasts: U ~ Uniform[F(y-1), F(y)]; uniform on [0,1] iff the forecasts are calibrated."""
    cdf = np.cumsum(pmf, axis=1)
    y = np.minimum(np.asarray(y, int), pmf.shape[1] - 1)
    hi = cdf[np.arange(len(y)), y]
    lo = np.where(y > 0, cdf[np.arange(len(y)), np.maximum(y - 1, 0)], 0.0)
    return lo + rng.random(len(y)) * (hi - lo)


def boot_mean_ci(x: np.ndarray, n_boot: int = 4000, seed: int = 0, level: float = 0.95) -> tuple[float, float, float]:
    """Mean and percentile CI of per-game values (one row == one independent game)."""
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return math.nan, math.nan, math.nan
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    m = x[idx].mean(axis=1)
    a = (1 - level) / 2
    return float(x.mean()), float(np.quantile(m, a)), float(np.quantile(m, 1 - a))


def paired_delta(loss_a: np.ndarray, loss_b: np.ndarray, n_boot: int = 4000, seed: int = 0, level: float = 0.95) -> dict[str, float]:
    """mean(loss_a - loss_b) with a game-level bootstrap CI and the one-sided bootstrap p that A is NOT better (mean >= 0).

    Negative delta = A is better. ``n`` is the number of independent games.
    """
    d = np.asarray(loss_a, float) - np.asarray(loss_b, float)
    ok = ~np.isnan(d)
    d = d[ok]
    mean, lo, hi = boot_mean_ci(d, n_boot, seed, level)
    rng = np.random.default_rng(seed + 1)
    idx = rng.integers(0, len(d), size=(n_boot, len(d)))
    boots = d[idx].mean(axis=1)
    p_not_better = float((boots >= 0).mean())
    se = float(d.std(ddof=1) / math.sqrt(len(d))) if len(d) > 1 else math.nan
    return {"n": int(len(d)), "delta": mean, "lo95": lo, "hi95": hi, "se": se, "z": mean / se if se and se > 0 else math.nan, "p_A_not_better": p_not_better}


def calibration_table(p: np.ndarray, y: np.ndarray, bins: int = 8) -> list[dict[str, float]]:
    """Equal-count bins of the forecast: mean forecast vs observed rate with a Wilson interval (independent games only)."""
    p = np.asarray(p, float)
    y = np.asarray(y, float)
    order = np.argsort(p)
    out = []
    for chunk in np.array_split(order, bins):
        n = len(chunk)
        if n == 0:
            continue
        ph = float(y[chunk].mean())
        z = 1.96
        den = 1 + z * z / n
        centre = (ph + z * z / (2 * n)) / den
        half = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / den
        out.append({"n": n, "mean_p": float(p[chunk].mean()), "obs": ph, "lo": centre - half, "hi": centre + half})
    return out


def ece(p: np.ndarray, y: np.ndarray, bins: int = 10) -> float:
    t = calibration_table(p, y, bins)
    n = sum(r["n"] for r in t)
    return float(sum(r["n"] * abs(r["mean_p"] - r["obs"]) for r in t) / n)


def paired_metric(f: Callable[[np.ndarray, np.ndarray], np.ndarray], p_a: np.ndarray, p_b: np.ndarray, y: np.ndarray, **kw: float) -> dict[str, float]:
    return paired_delta(f(p_a, y), f(p_b, y), **kw)  # type: ignore[arg-type]
