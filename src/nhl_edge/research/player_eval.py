"""Scoring PLAYER_SIM_V1 walk-forward output against outcomes and simple point-in-time baselines (RESEARCH_ONLY).

Baselines (all strictly pre-game, from the official per-game player lines):

* ``SEASON_RATE``   Poisson with the player's recent per-game rate (exponentially weighted, half-life 20 games, last 82
                    games, shrunk to the position mean with 5 pseudo-games) -- the "historical hit rate" handicap.
* ``ROLE_RATE``     Poisson with the player's shrunk per-60 rate x his recent (6-game half-life) ice time -- role-adjusted.
* goalies: ``POISSON_SHOTS`` Poisson(expected shots faced x league save %) -- "opponent shots minus goals" -- and
  ``NB_STATIC`` the fitted negative binomial mean without the simulated game script (does the game script add value?).

Metrics: Brier, log loss, ECE (10 equal-width bins), and a calibration table in 5-point buckets.
"""

from __future__ import annotations

import math
from typing import Any

import numpy as np
import pandas as pd

EPS = 1e-6


def poisson_ge(lam: np.ndarray, k: int) -> np.ndarray:
    """P(X >= k) for X ~ Poisson(lam)."""
    lam = np.asarray(lam, float)
    cdf = np.zeros_like(lam)
    term = np.exp(-lam)
    for j in range(k):
        cdf += term
        term = term * lam / (j + 1)
    return np.clip(1.0 - cdf, 0.0, 1.0)


def nb_ge(mu: np.ndarray, alpha: float, k: int) -> np.ndarray:
    """P(X >= k) for a negative binomial with mean mu and var mu + alpha mu^2."""
    mu = np.asarray(mu, float)
    if alpha <= 0:
        return poisson_ge(mu, k)
    r = 1.0 / alpha
    p = r / (r + mu)
    cdf = np.zeros_like(mu)
    for j in range(k):
        logpmf = math.lgamma(j + r) - math.lgamma(r) - math.lgamma(j + 1) + r * np.log(p) + j * np.log1p(-p)
        cdf += np.exp(logpmf)
    return np.clip(1.0 - cdf, 0.0, 1.0)


def brier(p: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean((np.asarray(p, float) - np.asarray(y, float)) ** 2))


def logloss(p: np.ndarray, y: np.ndarray) -> float:
    p = np.clip(np.asarray(p, float), EPS, 1 - EPS)
    y = np.asarray(y, float)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def ece(p: np.ndarray, y: np.ndarray, bins: int = 10) -> float:
    p, y = np.asarray(p, float), np.asarray(y, float)
    idx = np.minimum((p * bins).astype(int), bins - 1)
    tot = 0.0
    for b in range(bins):
        m = idx == b
        if m.any():
            tot += m.sum() * abs(p[m].mean() - y[m].mean())
    return float(tot / max(len(p), 1))


def buckets(p: np.ndarray, y: np.ndarray, width: float = 0.05, min_n: int = 1) -> list[dict[str, Any]]:
    p, y = np.asarray(p, float), np.asarray(y, float)
    out = []
    edges = np.arange(0.0, 1.0 + 1e-9, width)
    for lo in edges[:-1]:
        hi = lo + width
        m = (p >= lo) & (p < hi) if hi < 1.0 - 1e-9 else (p >= lo)
        n = int(m.sum())
        if n >= min_n:
            out.append({"bucket": f"{lo * 100:.0f}-{hi * 100:.0f}%", "n": n, "mean_pred": float(p[m].mean()), "hit_rate": float(y[m].mean()),
                        "gap": float(y[m].mean() - p[m].mean()), "se": float(math.sqrt(max(y[m].mean() * (1 - y[m].mean()), 1e-9) / n))})
    return out


def score(p: np.ndarray, y: np.ndarray) -> dict[str, Any]:
    p, y = np.asarray(p, float), np.asarray(y, float)
    base = y.mean()
    return {"n": int(len(y)), "base_rate": float(base), "mean_pred": float(p.mean()), "brier": brier(p, y), "logloss": logloss(p, y), "ece": ece(p, y),
            "brier_skill_vs_constant": float(1 - brier(p, y) / max(brier(np.full_like(y, base), y), EPS)), "sharpness_sd": float(p.std())}


def skater_baselines(players: pd.DataFrame, sk: pd.DataFrame, pos_of: dict[int, str]) -> pd.DataFrame:
    """SEASON_RATE and ROLE_RATE expected goals / assists / points for every evaluated skater-game (pre-game only)."""
    pl = players[["player_id", "game_id", "date_int", "goals", "assists", "points", "toi_s"]].copy()
    pl = pl.sort_values(["player_id", "date_int", "game_id"])
    pl["toi_s"] = pd.to_numeric(pl["toi_s"], errors="coerce").fillna(0.0)
    league = {s: pl[s].sum() / len(pl) for s in ("goals", "assists", "points")}
    league60 = {s: pl[s].sum() / (pl["toi_s"].sum() / 3600.0) for s in ("goals", "assists", "points")}
    by = {int(k): v for k, v in pl.groupby("player_id")}
    rows = []
    for r in sk[["player_id", "game_id", "date_int"]].itertuples(index=False):
        d = by.get(int(r.player_id))
        rec: dict[str, Any] = {"player_id": r.player_id, "game_id": r.game_id}
        if d is not None:
            d = d[d["date_int"] < r.date_int].tail(82)
        n = 0 if d is None else len(d)
        k = np.arange(n)[::-1]
        w20 = 0.5 ** (k / 20.0)
        w6 = 0.5 ** (k / 6.0)
        toi_recent = float((w6 * d["toi_s"].to_numpy()).sum() / w6.sum()) / 60.0 if n else 15.0
        for s in ("goals", "assists", "points"):
            x = d[s].to_numpy(float) if n else np.zeros(0)
            rec[f"season_{s}"] = float(((w20 * x).sum() + 5 * league[s]) / (w20.sum() + 5))
            mins = float((w20 * d["toi_s"].to_numpy()).sum() / 60.0) if n else 0.0
            per60 = ((w20 * x).sum() + league60[s] * 120.0 / 60.0) / (mins + 120.0) * 60.0  # 120 prior minutes at the league rate
            rec[f"role_{s}"] = float(per60 * toi_recent / 60.0)
        rows.append(rec)
    return pd.DataFrame(rows)


TARGETS = (("goals 1+", "p_g1", "y_g", 1, "goals"), ("goals 2+", "p_g2", "y_g", 2, "goals"), ("assists 1+", "p_a1", "y_a", 1, "assists"),
           ("assists 2+", "p_a2", "y_a", 2, "assists"), ("points 1+", "p_p1", "y_p", 1, "points"), ("points 2+", "p_p2", "y_p", 2, "points"),
           ("points 3+", "p_p3", "y_p", 3, "points"))


def evaluate_skaters(sk: pd.DataFrame, base: pd.DataFrame | None = None) -> dict[str, Any]:
    d = sk.merge(base, on=["player_id", "game_id"], how="left") if base is not None else sk
    out: dict[str, Any] = {}
    for label, pcol, ycol, k, stat in TARGETS:
        y = (d[ycol] >= k).astype(float).to_numpy()
        res = {"PLAYER_SIM_V1": score(d[pcol].to_numpy(), y), "buckets": buckets(d[pcol].to_numpy(), y)}
        if base is not None:
            res["SEASON_RATE"] = score(poisson_ge(d[f"season_{stat}"].to_numpy(), k), y)
            res["ROLE_RATE"] = score(poisson_ge(d[f"role_{stat}"].to_numpy(), k), y)
        out[label] = res
    for stat, e, ycol in (("goals", "e_g", "y_g"), ("assists", "e_a", "y_a"), ("points", "e_p", "y_p")):
        out[f"expected {stat}"] = {"mean_pred": float(d[e].mean()), "mean_actual": float(d[ycol].mean()), "mae": float((d[e] - d[ycol]).abs().mean()),
                                   "rmse": float(np.sqrt(((d[e] - d[ycol]) ** 2).mean()))}
    return out


def evaluate_goalies(gl: pd.DataFrame, saves_alpha: float, lg_sv: float, mu_static: np.ndarray | None = None, thresholds: tuple[int, ...] = tuple(range(18, 36))) -> dict[str, Any]:
    out: dict[str, Any] = {"n_starts": int(len(gl)), "mean_pred_saves": float(gl["e_saves"].mean()), "mean_actual_saves": float(gl["y_saves"].mean()),
                           "mae_saves": float((gl["e_saves"] - gl["y_saves"]).abs().mean()), "rmse_saves": float(np.sqrt(((gl["e_saves"] - gl["y_saves"]) ** 2).mean())),
                           "ladder": {}}
    pois_mu = gl["expected_faced"].to_numpy() * lg_sv
    out["mae_poisson_shots"] = float(np.abs(pois_mu - gl["y_saves"]).mean())
    allp, ally, allpb = [], [], []
    for t in thresholds:
        y = (gl["y_saves"] >= t).astype(float).to_numpy()
        p = gl[f"p_s{t}"].to_numpy()
        pb = poisson_ge(pois_mu, t)
        rec = {"PLAYER_SIM_V1": score(p, y), "POISSON_SHOTS": score(pb, y)}
        if mu_static is not None:
            rec["NB_STATIC"] = score(nb_ge(mu_static, saves_alpha, t), y)
        out["ladder"][f"{t}+"] = rec
        allp.append(p)
        ally.append(y)
        allpb.append(pb)
    P, Y, PB = np.concatenate(allp), np.concatenate(ally), np.concatenate(allpb)
    out["pooled_ladder"] = {"PLAYER_SIM_V1": score(P, Y), "POISSON_SHOTS": score(PB, Y), "buckets": buckets(P, Y)}
    return out


def evaluate_first_goal(sk: pd.DataFrame, games: pd.DataFrame | None) -> dict[str, Any]:
    out: dict[str, Any] = {"first_scorer": score(sk["p_first"].to_numpy(), sk["y_first"].to_numpy()),
                           "first_scorer_buckets": buckets(sk["p_first"].to_numpy(), sk["y_first"].to_numpy(), width=0.02)}
    if games is not None and len(games):
        out["home_scores_first"] = score(games["p_home_first"].to_numpy(), games["y_home_first"].to_numpy())
    return out


def evaluate_toi(sk: pd.DataFrame) -> dict[str, Any]:
    d = sk[sk["toi_s"].notna()].copy()
    act = pd.to_numeric(d["toi_s"], errors="coerce") / 60.0
    out = {"n": int(len(d)), "mae_model_total_min": float((d["exp_toi"] - act).abs().mean()), "bias_model_total_min": float((d["exp_toi"] - act).mean())}
    if "toi_recent_min" in d:
        r = pd.to_numeric(d["toi_recent_min"], errors="coerce")
        ok = r.notna()
        out["mae_recent_mean_total_min"] = float((r[ok] - act[ok]).abs().mean())
    for s in ("ev", "pp"):
        if f"exp_toi_{s}" in d and f"toi_{s}_s" in d:
            a = pd.to_numeric(d[f"toi_{s}_s"], errors="coerce") / 60.0
            ok = a.notna()
            out[f"mae_{s}_min"] = float((d.loc[ok, f"exp_toi_{s}"] - a[ok]).abs().mean())
    return out


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json
    from pathlib import Path

    from nhl_edge.players.features import PlayerParams
    from nhl_edge.research import player_walk_forward as W

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.player_eval")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--wf", default="docs/research/player_sim_v1")
    ap.add_argument("--seasons", default="2024,2025")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    data = W.Data(Path(a.history))
    res: dict[str, Any] = {}
    for s in (int(x) for x in a.seasons.split(",")):
        sk = pd.read_parquet(Path(a.wf) / f"skaters_{s}.parquet")
        gl = pd.read_parquet(Path(a.wf) / f"goalies_{s}.parquet")
        gp = Path(a.wf) / f"games_{s}.parquet"
        games = pd.read_parquet(gp) if gp.exists() else None
        base = skater_baselines(data.players, sk, {})
        fp = W.fit_season_params(data, s, PlayerParams())
        sm = fp["saves"]
        mu_static = np.array([sm.mean(ef * sm.lg_sv, np.array([0.0]), np.array([ef * (1 - sm.lg_sv)]), np.array([0.2]))[0] for ef in gl["expected_faced"]])
        res[str(s)] = {"skaters": evaluate_skaters(sk, base), "goalies": evaluate_goalies(gl, sm.alpha, sm.lg_sv, mu_static),
                       "first_goal": evaluate_first_goal(sk, games) if "p_first" in sk else None, "toi": evaluate_toi(sk) if "exp_toi" in sk else None}
    out = Path(a.out) if a.out else Path(a.wf) / "eval.json"
    out.write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps({s: {k: (v.get("points 1+", {}).get("PLAYER_SIM_V1") if k == "skaters" else None) for k, v in r.items()} for s, r in res.items()}, indent=1, default=float))
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
