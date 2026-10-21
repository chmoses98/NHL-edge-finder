"""Matchup-factor study (Phase D): do timestamp-safe, opponent-adjusted hockey factors add information BEYOND the market?

Independent challenger features (not the production model), all computed from games dated STRICTLY BEFORE the game date:

* ``oa_xg_diff``    opponent-adjusted 5v5 xG-rate differential (home minus away), ridge fit on decayed prior games, refit daily
* ``oa_exp_total``  opponent-adjusted expected 5v5 xG total of the two clubs (pace/environment)
* ``fin_diff``      shrunken finishing (goals - xG per game) differential
* ``pp_edge``       power-play xG rate minus opponent penalty-kill xG-against rate, both directions, differenced
* ``rest_diff``, ``b2b_home``, ``b2b_away``  days since previous game (capped), back-to-back flags
* ``tz_away``       timezone hours the away club crossed since its previous game

Test = logistic ``y ~ offset(logit(market mid)) + beta * x`` per feature block. Fitted on the chronologically FIRST 60% of
games, scored on the LAST 40% (never refit). Reported: beta with game-clustered SE (fit window), out-of-sample change in log
loss versus the market alone with a game-clustered bootstrap CI (negative = the feature helps). Starting-goalie identity is
deliberately NOT used: the archive does not say when the starter became known, so any goalie feature risks leaking.
"""

from __future__ import annotations

from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import cluster_ratio_ci

HALF_LIFE_DAYS = 45.0
RIDGE = 25.0


def _utc_offset_hours(tz: str, date: str) -> float:
    return pd.Timestamp(f"{date} 12:00", tz=ZoneInfo(tz)).utcoffset().total_seconds() / 3600.0


def load_team_games(history_dir: Path, seasons: tuple[int, ...]) -> pd.DataFrame:
    fr = [pd.read_parquet(Path(history_dir) / "moneypuck" / f"team_games_{s}.parquet") for s in seasons]
    t = pd.concat(fr, ignore_index=True)
    t = t[(t["game_type"] == 2)]
    return t


def _rates(t: pd.DataFrame, situation: str, f_for: str, f_ag: str) -> pd.DataFrame:
    s = t[t["situation"] == situation][["game_id", "game_date", "team_id", "opp_team_id", "home", "iceTime", f_for, f_ag]].copy()
    s["hours"] = s["iceTime"] / 3600.0 if s["iceTime"].max() > 400 else s["iceTime"] / 60.0
    s["for60"] = s[f_for] / s["hours"].where(s["hours"] > 0)
    s["ag60"] = s[f_ag] / s["hours"].where(s["hours"] > 0)
    return s


def fit_ratings(rows: pd.DataFrame, asof: pd.Timestamp, team_ids: list[int]) -> tuple[dict[int, float], dict[int, float], float, float]:
    """Decayed ridge: for60 = mu + ha*home + off[team] - dfn[opp]. Returns (off, dfn, mu, ha). dfn>0 = leaks more."""
    r = rows[rows["date"] < asof].dropna(subset=["for60"])
    if len(r) < 200:
        return {}, {}, float("nan"), 0.0
    age = (asof - r["date"]).dt.days.to_numpy(float)
    w = np.power(0.5, age / HALF_LIFE_DAYS) * r["hours"].to_numpy(float)
    idx = {t: i for i, t in enumerate(team_ids)}
    n = len(team_ids)
    X = np.zeros((len(r), 2 * n + 2))
    X[:, 0] = 1.0
    X[:, 1] = r["home"].astype(float).to_numpy()
    ti = r["team_id"].map(idx).to_numpy()
    oi = r["opp_team_id"].map(idx).to_numpy()
    ok = ~(pd.isna(ti) | pd.isna(oi))
    X, ti, oi, w, y = X[ok], ti[ok].astype(int), oi[ok].astype(int), w[ok], r["for60"].to_numpy(float)[ok]
    X[np.arange(len(X)), 2 + ti] = 1.0
    X[np.arange(len(X)), 2 + n + oi] = -1.0
    P = np.diag([0.0, 0.0] + [RIDGE] * (2 * n))
    A = X.T @ (X * w[:, None]) + P
    beta = np.linalg.solve(A, X.T @ (w * y))
    return ({t: beta[2 + i] for t, i in idx.items()}, {t: beta[2 + n + i] for t, i in idx.items()}, float(beta[0]), float(beta[1]))


def ewma_rate(rows: pd.DataFrame, asof: pd.Timestamp, team: int, col: str, prior: float, k: float = 20.0) -> float:
    """Decayed weighted mean of ``col`` over the team's games BEFORE ``asof``, shrunk toward ``prior`` with weight ``k`` (in game-equivalents)."""
    r = rows[(rows["date"] < asof) & (rows["team_id"] == team)].dropna(subset=[col])
    if r.empty:
        return prior
    age = (asof - r["date"]).dt.days.to_numpy(float)
    w = np.power(0.5, age / HALF_LIFE_DAYS)
    mean = float(np.sum(w * r[col].to_numpy(float)) / max(np.sum(w), 1e-9))
    shrink = float(np.sum(w) / (np.sum(w) + k))
    return mean * shrink + prior * (1.0 - shrink)


def build_features(history_dir: Path, games: pd.DataFrame, teams_csv: Path, target_season: int = 2025) -> pd.DataFrame:
    """One row per target-season game_id with the PIT feature set. ``games`` = NHL results (both seasons) with dates."""
    tg = load_team_games(history_dir, (target_season - 1, target_season))
    tg["date"] = pd.to_datetime(tg["game_date"])
    five = _rates(tg, "5on5", "xGoalsFor", "xGoalsAgainst")
    five["date"] = pd.to_datetime(five["game_date"])
    pp = _rates(tg, "5on4", "xGoalsFor", "xGoalsAgainst")
    pk = _rates(tg, "4on5", "xGoalsAgainst", "xGoalsFor")  # for60 here = xGA while shorthanded
    for d in (pp, pk):
        d["date"] = pd.to_datetime(d["game_date"])
    allr = tg[tg["situation"] == "all"][["game_id", "date", "team_id", "goalsFor", "xGoalsFor"]].copy()
    allr["fin"] = allr["goalsFor"] - allr["xGoalsFor"]
    team_ids = sorted(set(five["team_id"]) | set(five["opp_team_id"]))
    tz = pd.read_csv(teams_csv).set_index("team_id")["timezone"].to_dict()

    gm = games[games["season"].isin([target_season - 1, target_season]) & (games["game_type"] == 2)].copy()
    gm["date"] = pd.to_datetime(gm["game_date"])
    long = pd.concat([gm[["game_id", "date", "home_team_id", "home_team_id"]].set_axis(["game_id", "date", "team_id", "venue_team"], axis=1),
                      gm[["game_id", "date", "away_team_id", "home_team_id"]].set_axis(["game_id", "date", "team_id", "venue_team"], axis=1)]).sort_values(["team_id", "date"])
    long["prev_date"] = long.groupby("team_id")["date"].shift(1)
    long["prev_venue"] = long.groupby("team_id")["venue_team"].shift(1)
    long["rest"] = ((long["date"] - long["prev_date"]).dt.days).clip(upper=6).fillna(6)
    long["tzx"] = [abs(_utc_offset_hours(tz.get(int(v), "America/New_York"), str(d.date())) - _utc_offset_hours(tz.get(int(p), tz.get(int(v), "America/New_York")), str(d.date())))
                   if pd.notna(p) else 0.0 for v, p, d in zip(long["venue_team"], long["prev_venue"], long["date"], strict=True)]
    lk = long.set_index(["game_id", "team_id"])

    league_fin = 0.0
    out = []
    cache: dict[pd.Timestamp, tuple] = {}
    league_pp, league_pk = pp["for60"].mean(), pk["for60"].mean()
    for g in gm[gm["season"] == target_season].itertuples():
        d = g.date
        if d not in cache:
            cache[d] = fit_ratings(five, d, team_ids)
        off, dfn, mu, ha = cache[d]
        if not off:
            continue
        h, a = int(g.home_team_id), int(g.away_team_id)
        xg_h = mu + ha + off[h] - dfn[a]
        xg_a = mu - ha + off[a] - dfn[h]
        fin_h = ewma_rate(allr.rename(columns={"fin": "v"}), d, h, "v", league_fin)
        fin_a = ewma_rate(allr.rename(columns={"fin": "v"}), d, a, "v", league_fin)
        pp_h = ewma_rate(pp.rename(columns={"for60": "v"}), d, h, "v", league_pp)
        pp_a = ewma_rate(pp.rename(columns={"for60": "v"}), d, a, "v", league_pp)
        pk_h = ewma_rate(pk.rename(columns={"for60": "v"}), d, h, "v", league_pk)
        pk_a = ewma_rate(pk.rename(columns={"for60": "v"}), d, a, "v", league_pk)
        rh, ra = lk.loc[(g.game_id, h)], lk.loc[(g.game_id, a)]
        out.append({"game_id": int(g.game_id), "oa_xg_diff": xg_h - xg_a, "oa_exp_total": xg_h + xg_a, "fin_diff": fin_h - fin_a,
                    "pp_edge": (pp_h - pk_a) - (pp_a - pk_h), "rest_diff": float(rh["rest"] - ra["rest"]), "b2b_home": float(rh["rest"] <= 1),
                    "b2b_away": float(ra["rest"] <= 1), "tz_away": float(ra["tzx"])})
    return pd.DataFrame(out)


def _logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-3, 1 - 1e-3)
    return np.log(p / (1 - p))


def fit_offset_logit(y, off, X, groups):
    import statsmodels.api as sm

    Xc = sm.add_constant(X, has_constant="add")
    return sm.GLM(y, Xc, family=sm.families.Binomial(), offset=off).fit(cov_type="cluster", cov_kwds={"groups": groups})


def incremental_test(panel: pd.DataFrame, feats: list[str], label: str, disc_cut: str, orient: dict[str, int] | None = None) -> dict:
    """``panel`` rows carry y, mid, game_id, game_date and the feature columns oriented toward YES."""
    d = panel.dropna(subset=feats + ["mid", "y"]).copy()
    disc, hold = d[d["game_date"] < disc_cut], d[d["game_date"] >= disc_cut]
    mu, sd = disc[feats].mean(), disc[feats].std().replace(0, 1.0)
    z = lambda x: ((x[feats] - mu) / sd).to_numpy()  # noqa: E731
    fit = fit_offset_logit(disc["y"].to_numpy(), _logit(disc["mid"].to_numpy()), z(disc), disc["game_id"].to_numpy())
    beta = fit.params[1:]
    lin = _logit(hold["mid"].to_numpy()) + z(hold) @ beta + fit.params[0]
    p_new = 1 / (1 + np.exp(-lin))
    pm = hold["mid"].clip(1e-3, 1 - 1e-3).to_numpy()
    ll = lambda p: -(hold["y"].to_numpy() * np.log(np.clip(p, 1e-6, 1 - 1e-6)) + (1 - hold["y"].to_numpy()) * np.log(np.clip(1 - p, 1e-6, 1 - 1e-6)))  # noqa: E731
    h = hold.assign(dll=ll(p_new) - ll(pm))
    ci = cluster_ratio_ci(h, "dll", None)
    return {"label": label, "features": feats, "n_disc_games": int(disc["game_id"].nunique()), "n_hold_games": int(hold["game_id"].nunique()),
            "n_disc_rows": int(len(disc)), "n_hold_rows": int(len(hold)),
            "beta_std": {f: float(b) for f, b in zip(feats, beta, strict=True)}, "beta_se": {f: float(s) for f, s in zip(feats, fit.bse[1:], strict=True)},
            "beta_z": {f: float(b / s) for f, b, s in zip(feats, beta, fit.bse[1:], strict=True)}, "wald_p_block": float(fit.wald_test(np.eye(len(fit.params))[1:], scalar=True).pvalue),
            "oos_delta_logloss_vs_market": ci[0], "oos_dll_lo95": ci[1], "oos_dll_hi95": ci[2]}
