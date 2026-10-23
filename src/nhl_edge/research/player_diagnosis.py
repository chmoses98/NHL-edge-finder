"""Diagnosis of the incumbent skater projections: ice time, power-play time, shots, assists, points (RESEARCH_ONLY, read-only).

Questions answered, leakage-safe and without touching any model, parameter or published number:

1. How large are the errors of the incumbent's expected TOI / PP TOI / shots, and where do they sit (position, role, game type)?
2. Which part of the error is game-level (how many penalties are called) and which is allocation among teammates?
3. Which candidate signals add information *net of a level correction*, when each coefficient is fitted on earlier seasons only and scored on a later one?
   opponent shot suppression, the team's own shot environment, recent usage, recent power-play deployment, lagged line-mates, and the opposing goalie's lagged
   quality. A signal is only tested where a point-in-time source exists (see ``docs/research/player_diagnosis/RESULTS.md`` for the ones that cannot be).
4. For assists and points: is the incumbent biased, compressed, or already at the count-noise floor?

The incumbent rows are the derived champion stand-in of the workload replication (``workload_replication.derive_wf``), the same rows against which
WORKLOAD_V1 and WORKLOAD_V1_LC were scored. Nothing here is a promotion candidate; a signal that helps is a hypothesis for a pre-registered test, not a model.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

SEASONS = (2022, 2023, 2024, 2025)
TEST_SEASONS = (2023, 2024, 2025)
N_BOOT = 2000
SEED = 20261023


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def load_champion(cache: Path, seasons: tuple[int, ...] = SEASONS) -> pd.DataFrame:
    d = pd.concat([pd.read_parquet(Path(cache) / f"champ_sk_{s}.parquet") for s in seasons], ignore_index=True)
    return d.sort_values(["date_int", "game_id", "team_id", "player_id"]).reset_index(drop=True)


def err(pred: np.ndarray, act: np.ndarray) -> dict[str, float]:
    pred, act = np.asarray(pred, float), np.asarray(act, float)
    e = pred - act
    return {"n": int(len(e)), "mean_pred": float(pred.mean()), "mean_actual": float(act.mean()), "bias": float(e.mean()),
            "bias_pct": float(e.mean() / act.mean() * 100) if act.mean() else float("nan"), "mae": float(np.abs(e).mean()), "rmse": float(np.sqrt((e ** 2).mean()))}


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. error tables and cuts
# --------------------------------------------------------------------------------------------------------------------------------------------------------
TARGETS = {"toi": ("ch_toi", "y_toi"), "toi_ev": ("ch_toi_ev", "y_toi_ev"), "toi_pp": ("ch_toi_pp", "y_toi_pp"), "toi_sh": ("ch_toi_sh", "y_toi_sh"), "sog": ("ch_sog", "y_sog")}


STATE_TARGETS = ("toi_ev", "toi_pp", "toi_sh")


def with_shifts(d: pd.DataFrame) -> pd.DataFrame:
    """Rows whose by-state minutes are known (2024-25 has games without shift charts: their state minutes are recorded as zero, which is a data gap, not an error)."""
    return d[d["shifts_ok"].astype(bool)]


def error_table(d: pd.DataFrame) -> dict[str, dict[str, Any]]:
    ds = with_shifts(d)
    out: dict[str, dict[str, Any]] = {}
    for s in sorted(d["season"].unique()):
        g, gs = d[d["season"] == s], ds[ds["season"] == s]
        out[str(s)] = {k: err((gs if k in STATE_TARGETS else g)[p], (gs if k in STATE_TARGETS else g)[a]) for k, (p, a) in TARGETS.items()}
        out[str(s)]["rows_without_shift_charts"] = int(len(g) - len(gs))
    return out


def cuts(d: pd.DataFrame, season: int) -> dict[str, Any]:
    g = with_shifts(d[d["season"] == season]).copy()
    g["q_toi"] = pd.qcut(g["ch_toi"], 5, labels=False, duplicates="drop")
    g["q_pp"] = pd.qcut(g["ch_toi_pp"].rank(method="first"), 5, labels=False)
    g["ot"] = g["game_ot"].astype(bool)
    out: dict[str, Any] = {}
    for name, key in (("position", "pos"), ("predicted_toi_quintile", "q_toi"), ("predicted_pp_quintile", "q_pp"), ("overtime_game", "ot"), ("home", "is_home")):
        out[name] = {str(k): {t: err(x[TARGETS[t][0]], x[TARGETS[t][1]]) for t in ("toi", "toi_pp", "sog")} for k, x in g.groupby(key)}
    return out


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. game-level vs allocation (power play)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def team_frame(d: pd.DataFrame) -> pd.DataFrame:
    """One row per team-game: realised power-play minutes (the sum of skater PP minutes over the five on the ice), the incumbent's expected team PP minutes, shots."""
    t = (d.groupby(["game_id", "team_id", "opp_id", "season", "date_int"], sort=False)
         .agg(pp=("y_toi_pp", "sum"), sh=("y_toi_sh", "sum"), pred_pp=("team_pp_min", "first"), sog=("y_sog", "sum"), n=("player_id", "size")).reset_index())
    t["pp"] = t["pp"] / 5.0
    t["sh"] = t["sh"] / 4.0                      # four skaters on the ice when short-handed; equals the opponent's PP minutes
    return t.sort_values(["date_int", "game_id"]).reset_index(drop=True)


def pp_error_split(d: pd.DataFrame) -> dict[str, Any]:
    """Share of the player-level squared PP-minute error that is the game-level penalty count (rescale each player's expectation by realised / expected team PP)."""
    d = with_shifts(d)
    t = team_frame(d)[["game_id", "team_id", "pp", "pred_pp"]]
    x = d.merge(t, on=["game_id", "team_id"])
    out = {}
    for s, g in x.groupby("season"):
        base = ((g["ch_toi_pp"] - g["y_toi_pp"]) ** 2).mean()
        orc = ((g["ch_toi_pp"] * (g["pp"] / g["pred_pp"]) - g["y_toi_pp"]) ** 2).mean()
        out[str(s)] = {"mse": float(base), "mse_with_realised_team_pp": float(orc), "share_game_level": float(1 - orc / base),
                       "team_pp_corr_pred_actual": float(np.corrcoef(g.groupby("game_id").first()["pred_pp"], g.groupby("game_id").first()["pp"])[0, 1])}
    return out


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 3. walk-forward signal tests
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def _ewm_prior(values: np.ndarray, keys: np.ndarray, half_life: float, prior_value: np.ndarray, k: float) -> np.ndarray:
    """Per key (in row order), the exponentially weighted mean of earlier rows only, shrunk with ``k`` pseudo-observations of ``prior_value``."""
    out = np.empty(len(values))
    lam = 0.5 ** (1.0 / half_life)
    num: dict[Any, float] = {}
    den: dict[Any, float] = {}
    for i, (v, key) in enumerate(zip(values, keys, strict=True)):
        n_, d_ = num.get(key, 0.0), den.get(key, 0.0)
        out[i] = (n_ + k * prior_value[i]) / (d_ + k)
        num[key] = n_ * lam + v
        den[key] = d_ * lam + 1.0
    return out


def team_shot_context(d: pd.DataFrame, half_life: float = 30.0, k: float = 8.0) -> pd.DataFrame:
    """Point-in-time shot environment per team-game: the team's own shots-for and its opponent's shots-against relative to the league, from earlier games only."""
    t = team_frame(d)
    league = t["sog"].expanding().mean().shift(1).fillna(t["sog"].iloc[:50].mean()).to_numpy()      # league mean shots per team-game before this game
    t["sf_ewm"] = _ewm_prior(t["sog"].to_numpy(float), t["team_id"].to_numpy(), half_life, league, k)
    opp_sog = t.merge(t[["game_id", "team_id", "sog"]].rename(columns={"team_id": "opp_id", "sog": "opp_sog"}), on=["game_id", "opp_id"], how="left")["opp_sog"].to_numpy(float)
    t["sa_ewm"] = _ewm_prior(opp_sog, t["team_id"].to_numpy(), half_life, league, k)
    t["league"] = league
    t["x_own_sf"] = np.log(t["sf_ewm"] / t["league"])
    t["x_own_sa"] = np.log(t["sa_ewm"] / t["league"])
    ctx = t[["game_id", "team_id", "opp_id", "x_own_sf", "x_own_sa"]]
    opp = ctx.rename(columns={"team_id": "opp_id", "opp_id": "team_id", "x_own_sf": "x_opp_sf", "x_own_sa": "x_opp_sa"})
    return ctx.merge(opp[["game_id", "team_id", "x_opp_sf", "x_opp_sa"]], on=["game_id", "team_id"], how="left")


def fit_scale(pred: np.ndarray, X: np.ndarray, y: np.ndarray, loss: str, iters: int = 60) -> np.ndarray:
    """Coefficients b of ``pred * exp(X b)`` (first column of X is the constant) fitted by Poisson deviance (counts) or squared error (minutes); damped Newton / Gauss-Newton."""
    pred = np.maximum(pred, 1e-6)
    b = np.zeros(X.shape[1])

    def obj(b_: np.ndarray) -> float:
        mu_ = pred * np.exp(np.clip(X @ b_, -3, 3))
        return float(np.sum(mu_ - y * np.log(mu_))) if loss == "poisson" else float(np.sum((mu_ - y) ** 2))
    cur = obj(b)
    for _ in range(iters):
        mu = pred * np.exp(np.clip(X @ b, -3, 3))
        if loss == "poisson":
            grad, w = X.T @ (mu - y), mu
        else:                                                     # Gauss-Newton on 0.5 * sum (mu - y)^2
            grad, w = X.T @ ((mu - y) * mu), mu ** 2
        H = (X * w[:, None]).T @ X + 1e-9 * np.eye(X.shape[1])
        step = np.linalg.solve(H, grad)
        t = 1.0
        while t > 1e-4:
            new = obj(b - t * step)
            if new <= cur:
                break
            t /= 2
        else:
            break
        b = b - t * step
        done = cur - new < 1e-9 * max(abs(cur), 1.0)
        cur = new
        if done:
            break
    return b


def row_loss(mu: np.ndarray, y: np.ndarray, loss: str) -> np.ndarray:
    mu = np.maximum(mu, 1e-6)
    if loss == "poisson":
        with np.errstate(divide="ignore", invalid="ignore"):
            term = np.where(y > 0, y * np.log(y / mu), 0.0)
        return 2.0 * (mu - y + term)                         # Poisson deviance contribution
    return (mu - y) ** 2


def paired_game_ci(delta: np.ndarray, game: np.ndarray, n_boot: int = N_BOOT, seed: int = SEED) -> dict[str, float]:
    """Mean of per-row loss differences with a game-clustered bootstrap interval."""
    _, inv = np.unique(game, return_inverse=True)
    s = np.bincount(inv, weights=delta)
    c = np.bincount(inv).astype(float)
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(s), size=(n_boot, len(s)))
    m = s[idx].sum(1) / c[idx].sum(1)
    return {"delta": float(delta.mean()), "lo95": float(np.quantile(m, 0.025)), "hi95": float(np.quantile(m, 0.975))}


def signal_test(d: pd.DataFrame, features: dict[str, np.ndarray], pred_col: str, act_col: str, loss: str, seasons: tuple[int, ...] = TEST_SEASONS) -> dict[str, Any]:
    """For each test season: fit (level) and (level + feature) on earlier seasons, score both on the test season. Negative delta = the feature helps net of level."""
    season = d["season"].to_numpy()
    pred, y, game = d[pred_col].to_numpy(float), d[act_col].to_numpy(float), d["game_id"].to_numpy()
    out: dict[str, Any] = {}
    names = list(features)
    F = np.column_stack([features[k] for k in names]) if names else np.zeros((len(d), 0))
    ok = np.isfinite(F).all(1) if names else np.ones(len(d), bool)
    for s in seasons:
        tr, te = (season < s) & ok, (season == s) & ok
        if tr.sum() < 1000 or te.sum() < 1000:
            continue
        mu = {}
        for label, cols in (("raw", None), ("level", []), ("level+feat", list(range(len(names))))):
            if cols is None:
                mu[label] = pred[te]
                continue
            Xtr = np.column_stack([np.ones(tr.sum())] + [F[tr][:, c] for c in cols])
            Xte = np.column_stack([np.ones(te.sum())] + [F[te][:, c] for c in cols])
            b = fit_scale(pred[tr], Xtr, y[tr], loss)
            mu[label] = pred[te] * np.exp(np.clip(Xte @ b, -3, 3))
            mu[f"b_{label}"] = b
        l_raw, l_lvl, l_ft = (row_loss(mu[k], y[te], loss) for k in ("raw", "level", "level+feat"))
        out[str(s)] = {"n": int(te.sum()), "loss_raw": float(l_raw.mean()), "loss_level": float(l_lvl.mean()), "loss_level_feat": float(l_ft.mean()),
                       "level_gain": paired_game_ci(l_lvl - l_raw, game[te]), "feature_gain_net_of_level": paired_game_ci(l_ft - l_lvl, game[te]),
                       "coef_level_feat": [float(x) for x in mu["b_level+feat"]], "feature_names": names}
    return out


def shot_environment_features(d: pd.DataFrame) -> dict[str, np.ndarray]:
    ctx = team_shot_context(d)
    m = d[["game_id", "team_id"]].merge(ctx, on=["game_id", "team_id"], how="left")
    return {c: m[c].to_numpy(float) for c in ("x_opp_sa", "x_own_sf", "x_opp_sf", "x_own_sa")}


def usage_features(d: pd.DataFrame, n: int = 3) -> dict[str, np.ndarray]:
    """Recent usage relative to what the incumbent expected: the player's own mean of the last ``n`` dressed games over his expectation (no current-game information)."""
    g = d.groupby("player_id", sort=False)
    last_toi = g["y_toi"].transform(lambda x: x.shift(1).rolling(n, min_periods=n).mean())
    last_pp = g["y_toi_pp"].transform(lambda x: x.shift(1).rolling(n + 2, min_periods=n + 2).mean())
    return {"x_recent_toi": np.log((last_toi + 1.0) / (d["ch_toi"] + 1.0)).to_numpy(float), "x_recent_pp": np.log((last_pp + 0.25) / (d["ch_toi_pp"] + 0.25)).to_numpy(float)}


def penalty_features(d: pd.DataFrame, half_life: float = 30.0, k: float = 6.0) -> pd.DataFrame:
    """Point-in-time penalty environment per team-game: the team's drawn PP minutes and its opponent's shorthanded minutes (earlier games only)."""
    t = team_frame(d)
    lg = t["pp"].expanding().mean().shift(1).fillna(t["pp"].iloc[:50].mean()).to_numpy()
    t["drawn"] = _ewm_prior(t["pp"].to_numpy(float), t["team_id"].to_numpy(), half_life, lg, k)
    t["taken"] = _ewm_prior(t["sh"].to_numpy(float), t["team_id"].to_numpy(), half_life, lg, k)
    opp = t[["game_id", "team_id", "drawn", "taken"]].rename(columns={"team_id": "opp_id", "drawn": "opp_drawn", "taken": "opp_taken"})
    return t.merge(opp, on=["game_id", "opp_id"], how="left")


def team_pp_minutes_test(d: pd.DataFrame, seasons: tuple[int, ...] = TEST_SEASONS) -> dict[str, Any]:
    """Can team PP minutes be predicted beyond a level? Linear model on earlier seasons only vs the incumbent and vs a constant (previous seasons' mean)."""
    t = penalty_features(with_shifts(d)).dropna(subset=["drawn", "opp_taken", "opp_drawn", "taken"]).reset_index(drop=True)
    out: dict[str, Any] = {}
    for s in seasons:
        tr, te = t[t["season"] < s], t[t["season"] == s]
        if len(tr) < 500:
            continue
        cols = ["drawn", "opp_taken", "taken", "opp_drawn"]
        Xtr, Xte = np.c_[np.ones(len(tr)), tr[cols].to_numpy()], np.c_[np.ones(len(te)), te[cols].to_numpy()]
        b = np.linalg.lstsq(Xtr, tr["pp"].to_numpy(), rcond=None)[0]
        p = Xte @ b
        # the same model with the current season's level learned from the season so far is not available to a pregame forecast, so the level comes from earlier seasons
        out[str(s)] = {"n_team_games": int(len(te)), "actual_mean": float(te["pp"].mean()), "actual_sd": float(te["pp"].std()),
                       "incumbent": {"bias": float((te["pred_pp"] - te["pp"]).mean()), "rmse": float(np.sqrt(((te["pred_pp"] - te["pp"]) ** 2).mean())),
                                     "corr": float(np.corrcoef(te["pred_pp"], te["pp"])[0, 1])},
                       "constant_prev_seasons": {"bias": float(tr["pp"].mean() - te["pp"].mean()), "rmse": float(np.sqrt(((tr["pp"].mean() - te["pp"]) ** 2).mean()))},
                       "penalty_rate_model": {"bias": float((p - te["pp"]).mean()), "rmse": float(np.sqrt(((p - te["pp"]) ** 2).mean())), "corr": float(np.corrcoef(p, te["pp"])[0, 1]),
                                              "coef": dict(zip(["const", *cols], [float(x) for x in b], strict=True))}}
    return out


def lagged_linemate_feature(d: pd.DataFrame, history: Path, n_games: int = 5) -> np.ndarray:
    """Quality of the player's line-mates as seen in the team's previous ``n_games`` games (even-strength shared seconds), measured by the line-mates' own earlier shot rate.

    Point-in-time: only co-ice minutes of games strictly before the game, and line-mate rates computed from games before the pair's game.
    """
    co = pd.concat([pd.read_parquet(Path(history) / "players" / f"coice_{s}.parquet", columns=["game_id", "team_id", "p1", "p2", "shared_ev_s"]) for s in sorted(d["season"].unique())], ignore_index=True)
    order = d[["game_id", "team_id", "date_int"]].drop_duplicates().sort_values(["team_id", "date_int", "game_id"])
    order["gi"] = order.groupby("team_id").cumcount()
    co = co.merge(order[["game_id", "team_id", "gi"]], on=["game_id", "team_id"], how="inner")
    co = pd.concat([co, co.rename(columns={"p1": "p2", "p2": "p1"})], ignore_index=True)
    # rate of p2 before the pair's game: shots per game over its earlier dressed games (expanding mean, shrunk to the league mean)
    pg = d[["player_id", "team_id", "game_id", "y_sog", "date_int"]].sort_values(["player_id", "date_int", "game_id"])
    pg["cum"] = pg.groupby("player_id")["y_sog"].cumsum() - pg["y_sog"]
    pg["cnt"] = pg.groupby("player_id").cumcount()
    league = float(d["y_sog"].mean())
    pg["rate"] = (pg["cum"] + 10 * league) / (pg["cnt"] + 10)
    co = co.merge(pg[["player_id", "game_id", "rate"]].rename(columns={"player_id": "p2", "rate": "r2"}), on=["p2", "game_id"], how="left").dropna(subset=["r2"])
    # expand each pair-game to the next n_games games of the same team
    parts = []
    for lag in range(1, n_games + 1):
        x = co[["team_id", "gi", "p1", "shared_ev_s", "r2"]].copy()
        x["gi"] = x["gi"] + lag
        parts.append(x)
    ex = pd.concat(parts, ignore_index=True)
    ex["wr"] = ex["shared_ev_s"] * ex["r2"]
    agg = ex.groupby(["team_id", "gi", "p1"], as_index=False).agg(w=("shared_ev_s", "sum"), wr=("wr", "sum"))
    agg["q"] = agg["wr"] / agg["w"]
    cur = d[["game_id", "team_id", "player_id"]].merge(order[["game_id", "team_id", "gi"]], on=["game_id", "team_id"], how="left")
    m = cur.merge(agg.rename(columns={"p1": "player_id"}), on=["team_id", "gi", "player_id"], how="left")
    return np.log(m["q"].to_numpy(float) / league)


def goalie_context_feature(d: pd.DataFrame, history: Path, half_life: float = 25.0, k: float = 300.0) -> np.ndarray:
    """Opposing team's last-game starting goalie's lagged save percentage relative to the league (a pregame proxy; the true starter is not archived for 2021-25)."""
    gl = pd.concat([pd.read_parquet(Path(history) / "players" / f"goalies_{s}.parquet", columns=["game_id", "game_date", "team_id", "player_id", "starter", "shots_against", "saves"])
                    for s in sorted(d["season"].unique())], ignore_index=True)
    gl = gl[gl["starter"].astype(bool)].sort_values(["game_date", "game_id"])
    gl["sv"] = gl.groupby("player_id")["saves"].cumsum() - gl["saves"]
    gl["sa"] = gl.groupby("player_id")["shots_against"].cumsum() - gl["shots_against"]
    lg = float(gl["saves"].sum() / gl["shots_against"].sum())
    gl["q"] = (gl["sv"] + k * lg) / (gl["sa"] + k) - lg                  # lagged save% above league (expanding, shrunk)
    last = gl.sort_values(["team_id", "game_date", "game_id"]).copy()
    last["prev_q"] = last.groupby("team_id")["q"].shift(1)               # quality of the team's previous starter, as known before this game
    # the quality of the goalie who actually starts is only knowable after the fact; the proxy uses the previous game's starter
    mp = last[["game_id", "team_id", "prev_q", "q"]]
    cur = d[["game_id", "opp_id"]].merge(mp.rename(columns={"team_id": "opp_id", "prev_q": "opp_prev_q", "q": "opp_actual_q"}), on=["game_id", "opp_id"], how="left")
    return cur["opp_prev_q"].to_numpy(float), cur["opp_actual_q"].to_numpy(float)


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. assists and points (PLAYER_SIM_V1 skater rows, 2025-26)
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def points_diagnosis(sk: pd.DataFrame) -> dict[str, Any]:
    out: dict[str, Any] = {"n": int(len(sk))}
    for k, nm in (("g", "goals"), ("a", "assists"), ("p", "points")):
        e, y = sk[f"e_{k}"].to_numpy(float), sk[f"y_{k}"].to_numpy(float)
        slope = float(np.polyfit(e, y, 1)[0])
        out[nm] = {**err(e, y), "corr": float(np.corrcoef(e, y)[0, 1]), "calibration_slope": slope,
                   "poisson_noise_floor_mse": float(e.mean()), "dispersion_mse_over_mean": float(((e - y) ** 2).mean() / e.mean())}
    sk = sk.copy()
    sk["q"] = pd.qcut(sk["e_p"], 5, labels=False)
    out["points_by_predicted_quintile"] = {str(q): {"e_p": float(g["e_p"].mean()), "y_p": float(g["y_p"].mean()), "e_a": float(g["e_a"].mean()), "y_a": float(g["y_a"].mean()),
                                                    "e_g": float(g["e_g"].mean()), "y_g": float(g["y_g"].mean())} for q, g in sk.groupby("q")}
    out["by_position"] = {str(q): {t: err(g[f"e_{t}"], g[f"y_{t}"]) for t in ("g", "a", "p")} for q, g in sk.groupby("pos")}
    toi = sk["toi_s"] / 60.0
    r = (toi / sk["exp_toi"]).clip(0.3, 3.0)
    out["oracle_toi"] = {t: float(1 - ((sk[f"e_{t}"] * r - sk[f"y_{t}"]) ** 2).mean() / ((sk[f"e_{t}"] - sk[f"y_{t}"]) ** 2).mean()) for t in ("g", "a", "p")}
    team = sk.groupby(["game_id", "team_id"])[["e_g", "y_g"]].sum().rename(columns={"e_g": "t_eg", "y_g": "t_yg"}).reset_index()
    z = sk.merge(team, on=["game_id", "team_id"])
    s = (z["t_yg"] / z["t_eg"].clip(lower=0.5)).clip(0, 4)
    out["oracle_team_goals"] = {t: float(1 - ((z[f"e_{t}"] * s - z[f"y_{t}"]) ** 2).mean() / ((z[f"e_{t}"] - z[f"y_{t}"]) ** 2).mean()) for t in ("g", "a", "p")}
    out["team_goals"] = {"corr_pred_actual": float(np.corrcoef(team["t_eg"], team["t_yg"])[0, 1]), "mean_pred": float(team["t_eg"].mean()), "mean_actual": float(team["t_yg"].mean())}
    return out


def calibration_walk(sk: pd.DataFrame, target: str, split_date: int) -> dict[str, Any]:
    """Chronological split inside the one season we have: a power-law (slope) correction fitted on the early part, scored on the later part."""
    e, y = sk[f"e_{target}"].to_numpy(float), sk[f"y_{target}"].to_numpy(float)
    tr, te = sk["date_int"].to_numpy() < split_date, sk["date_int"].to_numpy() >= split_date
    X = np.c_[np.ones(len(sk)), np.log(np.maximum(e, 1e-3)) - np.log(e[tr].mean())]
    b = fit_scale(e[tr], X[tr], y[tr], "poisson")
    mu = e[te] * np.exp(X[te] @ b)
    base, cal = row_loss(e[te], y[te], "poisson"), row_loss(mu, y[te], "poisson")
    return {"n_test": int(te.sum()), "coef": [float(x) for x in b], "poisson_deviance_raw": float(base.mean()), "poisson_deviance_corrected": float(cal.mean()),
            "gain": paired_game_ci(cal - base, sk["game_id"].to_numpy()[te])}


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def run(cache: Path, history: Path, sk_points: Path, with_lines: bool = True) -> dict[str, Any]:
    d = load_champion(cache)
    res: dict[str, Any] = {"seasons": list(SEASONS), "test_seasons": list(TEST_SEASONS), "n_rows": int(len(d)), "errors": error_table(d), "cuts": {str(s): cuts(d, s) for s in TEST_SEASONS},
                           "pp_split": pp_error_split(d), "team_pp_minutes": team_pp_minutes_test(d)}
    env = shot_environment_features(d)
    tests: dict[str, Any] = {}
    tests["sog|opponent_suppression"] = signal_test(d, {"x_opp_sa": env["x_opp_sa"]}, "ch_sog", "y_sog", "poisson")
    tests["sog|own_shot_environment"] = signal_test(d, {"x_own_sf": env["x_own_sf"]}, "ch_sog", "y_sog", "poisson")
    tests["sog|opponent+own"] = signal_test(d, {"x_opp_sa": env["x_opp_sa"], "x_own_sf": env["x_own_sf"]}, "ch_sog", "y_sog", "poisson")
    u = usage_features(d)
    tests["toi|recent_usage"] = signal_test(d, {"x_recent_toi": u["x_recent_toi"]}, "ch_toi", "y_toi", "sq")
    ok = d["shifts_ok"].astype(bool).to_numpy()
    tests["toi_pp|recent_pp_deployment"] = signal_test(d[ok].reset_index(drop=True), {"x_recent_pp": u["x_recent_pp"][ok]}, "ch_toi_pp", "y_toi_pp", "sq")
    tests["sog|recent_usage"] = signal_test(d, {"x_recent_toi": u["x_recent_toi"]}, "ch_sog", "y_sog", "poisson")
    if with_lines:
        q = lagged_linemate_feature(d, history)
        tests["sog|lagged_linemates"] = signal_test(d, {"x_linemates": q}, "ch_sog", "y_sog", "poisson")
        prev_q, act_q = goalie_context_feature(d, history)
        tests["sog|opp_goalie_prev_starter_proxy"] = signal_test(d, {"x_goalie": prev_q}, "ch_sog", "y_sog", "poisson")
        res["goalie_proxy_vs_actual_starter_corr"] = float(pd.Series(prev_q).corr(pd.Series(act_q)))
    res["signal_tests"] = tests
    if Path(sk_points).exists():
        sk = pd.read_parquet(sk_points)
        res["points_assists"] = points_diagnosis(sk)
        mid = int(sk["date_int"].quantile(0.5))
        res["points_assists"]["slope_correction_chronological_split"] = {t: calibration_walk(sk, t, mid) for t in ("a", "p")}
    return res


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.player_diagnosis")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache/derived")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--skaters", default="docs/research/player_sim_v1/skaters_2025.parquet")
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-lines", action="store_true")
    a = ap.parse_args(argv)
    res = run(Path(a.cache), Path(a.history), Path(a.skaters), with_lines=not a.no_lines)
    Path(a.out).write_text(json.dumps(res, indent=1, default=float))
    print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
