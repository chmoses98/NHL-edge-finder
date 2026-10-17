"""A..F candidate ladders for skater counts (SOG, goals, assists, points), goalie saves and team goals.

Every scalar parameter (shrinkage k, halflife, opponent elasticity beta, home factors, stack weights)
is fitted on DEVELOPMENT rows only and frozen. LightGBM (E) is refitted walk-forward by season on all
earlier seasons (that is how it would run live); its hyper-parameters are fixed a priori.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pf_core import models, pit

from . import SPLITS

DEV = SPLITS["development"]
LGB = {"n_estimators": 300, "learning_rate": 0.04, "num_leaves": 31, "min_child_samples": 300,
       "colsample_bytree": 0.7, "subsample": 0.8}


def gprior(df: pd.DataFrame, by, col: str) -> pd.Series:
    """pf_core.models.group_prior_pit with a leakage-safe fallback.

    pf_core 1.0.0 BUG (reported, not edited): group_prior_pit's default fallback for rows whose group
    has no earlier dates is df[col].mean() over the WHOLE frame, i.e. it includes future rows. We pass
    the development-season mean instead (development data may be fitted on)."""
    dev = df["season"].isin(DEV) if "season" in df else pd.Series(True, index=df.index)
    fb = float(df.loc[dev, col].mean()) if dev.any() else float("nan")
    return models.group_prior_pit(df, list(by), "game_date", col, fallback=fb)


def recent_prior(df: pd.DataFrame, col: str, window: int = 1200, date_col: str = "game_date") -> pd.Series:
    """League level from the last `window` rows played on EARLIER dates (point-in-time).

    Fix for a verified drift defect: expanding-mean priors (group_prior_pit) and season-decayed ridge
    intercepts lag a moving league level (shots on goal per team-game fell from 31.6 in 2021-22 to
    27.7 in 2025-26), which biased frozen-scalar saves models upward on validation (+0.6 saves)."""
    order = np.argsort(df[date_col].to_numpy(), kind="mergesort")
    dates = df[date_col].to_numpy()[order]
    x = df[col].to_numpy(float)[order]
    ok = np.isfinite(x)
    cs = np.concatenate([[0.0], np.cumsum(np.where(ok, x, 0.0))])
    cn = np.concatenate([[0.0], np.cumsum(ok.astype(float))])
    i0 = np.searchsorted(dates, dates, side="left")
    lo = np.maximum(0, i0 - window)
    n = cn[i0] - cn[lo]
    val = np.where(n > 0, (cs[i0] - cs[lo]) / np.maximum(n, 1), np.nan)
    out = np.empty(len(df))
    out[order] = val
    dev = df["season"].isin(DEV).to_numpy() if "season" in df else np.ones(len(df), bool)
    return pd.Series(out, index=df.index).fillna(float(np.nanmean(df.loc[dev, col])))


def _poisson_nll(y, mu):
    mu = np.maximum(np.asarray(mu, float), 1e-6)
    y = np.asarray(y, float)
    return float(np.mean(mu - y * np.log(mu)))


def _prior_rate(sk, num, den, by=("role",)):
    a = gprior(sk, by, num)
    b = gprior(sk, by, den)
    return a / b.clip(lower=1e-3)


# =========================================================================== skaters
def skater_ladder(sk: pd.DataFrame, stat: str, log: list, toi_src: str = "E") -> dict:
    """Adds mu_<stat>_{A,B,C,D,E,F} to sk. Returns frozen params."""
    dev = (sk["season"].isin(DEV) & (sk["toi_n"] >= 1)).to_numpy()
    y = sk[stat].to_numpy(float)
    P = {"stat": stat, "toi_src": toi_src}
    prior = gprior(sk, ["role"], stat)
    d = sk[sk["season"].isin(DEV)]
    P["k"] = pit.estimate_shrinkage_k(d[stat], d["player_id"].astype(str) + "_" + d["season"].astype(str))
    sk[f"mu_{stat}_A"] = models.est_A(sk, stat, prior, P["k"])
    best = None
    for h in (3, 10, 30):
        m = models.est_B(sk, stat, prior, P["k"], h)
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": stat, "step": "B_halflife", "value": h, "dev_poisson_nll": e})
        if best is None or e < best[1]:
            best = (h, e, m)
    P["hl_B"] = best[0]
    sk[f"mu_{stat}_B"] = best[2]

    # ---- C: TOI x per-minute rates, non-PP and PP separately, EB shrinkage in TOI units
    tnp, tpp = sk[f"toi_np_{toi_src}"], sk[f"toi_pp_{toi_src}"]
    pr_np = _prior_rate(sk, f"{stat}_np", "toi_np")
    pr_pp = _prior_rate(sk, f"{stat}_pp", "toi_pp", by=("pp_role",))
    bestc = None
    for h in (10, 30):
        for k_np in (60.0, 200.0, 600.0, 1500.0):
            r_np = models.ratio_rate(sk, f"{stat}_np", "toi_np", h, pr_np, k_np)
            m = tnp * r_np + tpp * pr_pp  # PP at prior while scanning the non-PP grid
            e = _poisson_nll(y[dev], m[dev])
            log.append({"family": stat, "step": "C_np_grid", "value": [h, k_np], "dev_poisson_nll": e})
            if bestc is None or e < bestc[1]:
                bestc = ((h, k_np), e, r_np)
    (P["hl_C"], P["k_np_min"]) = bestc[0]
    r_np = bestc[2]
    bestp = None
    for k_pp in (10.0, 30.0, 100.0, 300.0):
        r_pp = models.ratio_rate(sk, f"{stat}_pp", "toi_pp", P["hl_C"], pr_pp, k_pp)
        m = tnp * r_np + tpp * r_pp
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": stat, "step": "C_pp_grid", "value": k_pp, "dev_poisson_nll": e})
        if bestp is None or e < bestp[1]:
            bestp = (k_pp, e, r_pp)
    P["k_pp_min"] = bestp[0]
    sk[f"rate_np_{stat}"], sk[f"rate_pp_{stat}"] = r_np, bestp[2]
    sk[f"mu_{stat}_C"] = tnp * r_np + tpp * bestp[2]

    # ---- D: C x schedule-adjusted opponent factor ^ beta x venue
    cands = ["sog_for_oppf"] if stat == "sog" else ["goals_for_oppf", "xg_for_oppf"]
    bestd = None
    for c in cands:
        lf = np.log(sk[c].clip(0.5, 2.0)).fillna(0.0).to_numpy()
        beta = models.fit_opponent_beta(y[dev], sk.loc[dev, f"mu_{stat}_C"], lf[dev])
        m = sk[f"mu_{stat}_C"] * np.exp(beta * lf)
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": stat, "step": "D_factor", "value": [c, beta], "dev_poisson_nll": e})
        if bestd is None or e < bestd[1]:
            bestd = (c, e, beta, m)
    P["opp_factor"], P["beta"] = bestd[0], bestd[2]
    m = bestd[3]
    home = sk["is_home"].to_numpy(bool)
    P["home_scale"] = models.fit_calibration_scale(y[dev & home], m[dev & home])
    P["away_scale"] = models.fit_calibration_scale(y[dev & ~home], m[dev & ~home])
    sk[f"mu_{stat}_D"] = m * np.where(home, P["home_scale"], P["away_scale"])
    sk[f"oppadj_{stat}"] = np.exp(P["beta"] * np.log(sk[P["opp_factor"]].clip(0.5, 2.0)).fillna(0.0))
    return P


SK_E_FEATURES = [
    "{s}_ewm3", "{s}_ewm10", "{s}_ewm30", "{s}_std", "{s}_prev", "{s}_career", "{s}_n", "{s}_std_n",
    "{s}_pp_ewm30", "{s}_np_ewm30", "rate_np_{s}", "rate_pp_{s}", "mu_{s}_C", "mu_{s}_D", "oppadj_{s}",
    "ixg_ewm10", "ixg_ewm30", "ixg_pp_ewm30", "att_ewm10", "att_ewm30", "sog_ewm30", "points_ewm30", "a1_ewm30",
    "gf_on_ewm30", "toi_E", "toi_np_E", "toi_pp_E", "toi_ewm10", "pp_share_ewm10", "rank_np_last", "pp_unit_last",
    "is_d", "is_home_i", "b2b", "opp_b2b", "rest_days", "travel_km", "missed_games", "new_team", "mate_p60_last",
    "line_changed_pit", "goals_for_ewm10", "xg_for_ewm10", "sog_for_ewm10", "team_pp_exp",
    "sog_for_oppf", "goals_for_oppf", "xg_for_oppf", "sog_for_ownf", "goals_for_ownf", "xg_for_ownf",
]


def skater_E(sk: pd.DataFrame, stat: str) -> list[str]:
    feats = list(dict.fromkeys(f.format(s=stat) for f in SK_E_FEATURES))
    feats = [f for f in feats if f in sk.columns]
    sk["_y"] = sk[stat].astype(float)
    sk["_train"] = sk["toi_n"] >= 1
    pred = models.lgbm_walkforward(sk, feats, "_y", "season", objective="poisson", min_train_blocks=1,
                                   params=LGB, train_mask_col="_train")
    sk[f"mu_{stat}_E"] = pred
    sk.drop(columns=["_y", "_train"], inplace=True)
    return feats


def stack_F(df: pd.DataFrame, stat: str, members=("A", "B", "C", "D", "E"), fit_seasons=None) -> dict:
    cols = [f"mu_{stat}_{m}" for m in members]
    fs = fit_seasons or [DEV[-1]]
    m = df["season"].isin(fs) & df[cols].notna().all(axis=1) & (df.get("toi_n", pd.Series(1, index=df.index)) >= 1)
    w = models.fit_stack_weights(df.loc[m, stat], df.loc[m, cols].to_numpy())
    X = df[cols].copy()
    for c in cols:  # rows lacking a member (E warm-up): fall back to D
        X[c] = X[c].fillna(df[f"mu_{stat}_D"])
    df[f"mu_{stat}_F"] = X.to_numpy() @ w
    return {"members": list(members), "weights": [float(x) for x in w], "fit_seasons": fs}


# =========================================================================== goalies
def goalie_ladder(gf: pd.DataFrame, log: list) -> tuple[pd.DataFrame, dict]:
    """Saves for the (actual) starting goalie. gf = starters only, PIT goalie + team features attached."""
    P = {}
    dev = gf["season"].isin(DEV).to_numpy() & (gf["saves_n"].fillna(0) >= 1).to_numpy()
    y = gf["saves"].to_numpy(float)
    gf["all"] = "G"
    P["league_level"] = "rolling last 1200 starts (PIT)"
    prior = recent_prior(gf, "saves")
    d = gf[gf["season"].isin(DEV)]
    P["k"] = pit.estimate_shrinkage_k(d["saves"], d["player_id"].astype(str) + "_" + d["season"].astype(str))
    gf["mu_saves_A"] = models.est_A(gf, "saves", prior, P["k"])
    best = None
    for h in (10, 30):
        m = models.est_B(gf, "saves", prior, P["k"], h)
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": "saves", "step": "B_halflife", "value": h, "dev_poisson_nll": e})
        if best is None or e < best[1]:
            best = (h, e, m)
    P["hl_B"] = best[0]
    gf["mu_saves_B"] = best[2]
    # league PIT shots against per team-game and save fraction
    lg_sa = recent_prior(gf, "shots_against")
    sv_prior = 1 - recent_prior(gf, "goals_against") / lg_sa.clip(lower=1)
    # C: team's own recent shots allowed (EWMA, shrunk) x goalie shrunk save fraction
    sa_raw = gf["sog_against_ewm10"]
    n_t = gf["sog_against_n"].fillna(0).clip(upper=29)
    bestk = None
    for k_t in (5.0, 15.0, 40.0):
        sa_hat = pit.eb_shrink(sa_raw, n_t, lg_sa, k_t)
        for k_sv in (300.0, 1000.0, 3000.0):
            sv = pit.eb_shrink(gf["sv_career"], gf["shots_against_cum"], sv_prior, k_sv)
            m = sa_hat * sv
            e = _poisson_nll(y[dev], m[dev])
            log.append({"family": "saves", "step": "C_grid", "value": [k_t, k_sv], "dev_poisson_nll": e})
            if bestk is None or e < bestk[1]:
                bestk = ((k_t, k_sv), e, sa_hat, sv)
    P["k_team_sa"], P["k_sv_shots"] = bestk[0]
    gf["sa_C"], gf["sv_hat"] = bestk[2], bestk[3]
    gf["mu_saves_C"] = gf["sa_C"] * gf["sv_hat"]
    # D: schedule-adjusted shots against from ridge (opponent generation + own suppression + venue)
    # recentre the ridge level on the recent league level (ridge intercepts are season-decayed means)
    team_lvl = recent_prior(gf, "sog_against")
    sa_d = (gf["sa_ridge"] - gf["sa_icpt"] + team_lvl).fillna(gf["sa_C"])
    m = sa_d * gf["sv_hat"]
    P["d_scale"] = models.fit_calibration_scale(y[dev], m[dev])
    gf["sa_D"] = sa_d * P["d_scale"]
    gf["mu_saves_D"] = gf["sa_D"] * gf["sv_hat"]
    return gf, P


GOALIE_E_FEATURES = ["saves_ewm10", "saves_ewm30", "saves_std", "saves_prev", "saves_n", "shots_against_ewm30",
                     "sv_career", "shots_against_cum", "sv_hat", "sa_C", "sa_D", "sa_ridge", "mu_saves_C", "mu_saves_D",
                     "sog_against_ewm10", "sog_against_ewm30", "opp_sog_for_ewm30", "xg_against_ewm30",
                     "opp_xg_for_ewm30", "is_home_i", "b2b", "opp_b2b", "rest_days", "travel_km", "toi_ewm10",
                     "starts_ewm10", "pulled_ewm30"]


# =========================================================================== team goals
def team_ladder(tg: pd.DataFrame, log: list) -> tuple[pd.DataFrame, dict]:
    P = {}
    dev = tg["season"].isin(DEV).to_numpy() & (tg["goals_for_n"].fillna(0) >= 1).to_numpy()
    y = tg["goals_for"].to_numpy(float)
    tg["all"] = "T"
    prior = gprior(tg, ["all"], "goals_for")
    d = tg[tg["season"].isin(DEV)]
    P["k"] = pit.estimate_shrinkage_k(d["goals_for"], d["team_id"].astype(str) + "_" + d["season"].astype(str))
    tg["mu_tg_A"] = models.est_A(tg, "goals_for", prior, P["k"])
    best = None
    for h in (10, 30):
        m = models.est_B(tg, "goals_for", prior, P["k"], h)
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": "team_goals", "step": "B_halflife", "value": h, "dev_poisson_nll": e})
        if best is None or e < best[1]:
            best = (h, e, m)
    P["hl_B"] = best[0]
    tg["mu_tg_B"] = best[2]
    # C: own attack x opponent defence (log5 on EWMA rates, each shrunk to the PIT league mean)
    n = tg["goals_for_n"].fillna(0).clip(upper=87)
    on = tg["opp_goals_against_ewm30"].notna()
    bestc = None
    for k in (10.0, 30.0, 80.0):
        att = pit.eb_shrink(tg["goals_for_ewm30"], n, prior, k)
        dfn = pit.eb_shrink(tg["opp_goals_against_ewm30"], np.where(on, n, 0), prior, k)
        m = att * dfn / prior
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": "team_goals", "step": "C_k", "value": k, "dev_poisson_nll": e})
        if bestc is None or e < bestc[1]:
            bestc = (k, e, m)
    P["k_C"] = bestc[0]
    tg["mu_tg_C"] = bestc[2]
    # D: schedule-adjusted ridge (goals and xG), blend weight on development
    g_r, x_r = tg["goals_for_ridge"], tg["xg_for_ridge"]
    xscale = models.fit_calibration_scale(y[dev], x_r.fillna(g_r)[dev])
    bestw = None
    for w in (0.0, 0.25, 0.5, 0.75, 1.0):
        m = (w * g_r + (1 - w) * xscale * x_r.fillna(g_r)).fillna(tg["mu_tg_C"])
        e = _poisson_nll(y[dev], m[dev])
        log.append({"family": "team_goals", "step": "D_goal_vs_xg_weight", "value": w, "dev_poisson_nll": e})
        if bestw is None or e < bestw[1]:
            bestw = (w, e, m)
    P["D_w_goals"], P["D_xg_scale"] = bestw[0], xscale
    tg["mu_tg_D"] = bestw[2]
    return tg, P


TEAM_E_FEATURES = ["goals_for_ewm10", "goals_for_ewm30", "goals_for_std", "goals_for_prev", "xg_for_ewm10",
                   "xg_for_ewm30", "sog_for_ewm30", "goals_against_ewm30", "opp_goals_against_ewm30",
                   "opp_xg_against_ewm30", "opp_sog_against_ewm30", "pp_min_ewm10", "opp_sh_min_ewm10",
                   "goals_for_ridge", "xg_for_ridge", "sog_for_ridge", "mu_tg_C", "mu_tg_D", "is_home_i",
                   "b2b", "opp_b2b", "rest_days", "opp_rest_days", "travel_km", "opp_travel_km", "goals_for_n"]
