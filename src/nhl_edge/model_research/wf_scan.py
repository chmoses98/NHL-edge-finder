"""Systematic-error scan of V1 on the 2,624 walk-forward games: do residuals (regulation goals - V1 expected goals) line up with
information V1 already holds? Each row is one pre-declared feature; Benjamini-Hochberg over the whole table (reported both raw and adjusted).

A pattern here is a candidate class-A error (repeatable, statistically supported), not a trading signal: it must survive the rolling
challenger test (exp_cal) and an out-of-time check before it is called an improvement.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm

from nhl_edge.model_research.challengers import add_regulation_columns


def bh(p: np.ndarray, q: float = 0.10) -> tuple[np.ndarray, np.ndarray]:
    p = np.asarray(p, float)
    m = len(p)
    order = np.argsort(p)
    ranked = p[order] * m / (np.arange(m) + 1)
    adj = np.minimum.accumulate(ranked[::-1])[::-1]
    out = np.empty(m)
    out[order] = np.minimum(adj, 1.0)
    return out, out <= q


def features(df: pd.DataFrame) -> dict[str, tuple[str, np.ndarray]]:
    """(target, standardised-feature) pairs; every feature uses only information stamped before the game."""
    df = add_regulation_columns(df)
    gu = np.minimum(df["home_games_used"], df["away_games_used"])
    f: dict[str, tuple[str, np.ndarray]] = {}
    f["total~early_season(games_used<=15)"] = ("tot", (gu <= 15).astype(float).to_numpy())
    f["total~log_games_used"] = ("tot", np.log1p(gu).to_numpy())
    f["total~lam_sum"] = ("tot", df["s"].to_numpy())
    f["total~either_b2b"] = ("tot", (df["home_b2b"] | df["away_b2b"]).astype(float).to_numpy())
    f["total~both_b2b"] = ("tot", (df["home_b2b"] & df["away_b2b"]).astype(float).to_numpy())
    f["total~mean_rest_days(cap 7)"] = ("tot", np.minimum((df["home_rest_days"] + df["away_rest_days"]) / 2, 7).to_numpy())
    f["total~finish_sum"] = ("tot", (df["home_finish"] + df["away_finish"]).to_numpy())
    f["total~off_xg_sum"] = ("tot", (df["home_off_xg60"] + df["away_off_xg60"]).to_numpy())
    f["total~def_xg_sum"] = ("tot", (df["home_def_xg60"] + df["away_def_xg60"]).to_numpy())
    f["margin~lam_diff"] = ("mar", df["d"].to_numpy())
    f["margin~home_b2b"] = ("mar", df["home_b2b"].astype(float).to_numpy())
    f["margin~away_b2b"] = ("mar", df["away_b2b"].astype(float).to_numpy())
    f["margin~rest_diff(cap 5)"] = ("mar", (np.minimum(df["home_rest_days"], 5) - np.minimum(df["away_rest_days"], 5)).to_numpy())
    f["margin~finish_diff"] = ("mar", (df["home_finish"] - df["away_finish"]).to_numpy())
    f["margin~early_season"] = ("mar", (gu <= 15).astype(float).to_numpy())
    f["margin~is_2025"] = ("mar", (df["season"] == 2025).astype(float).to_numpy())
    f["total~is_2025"] = ("tot", (df["season"] == 2025).astype(float).to_numpy())
    return f


def scan(df: pd.DataFrame) -> pd.DataFrame:
    df = add_regulation_columns(df)
    resid = {"tot": (df["reg_s"] - df["s"]).to_numpy(), "mar": (df["reg_d"] - df["d"]).to_numpy()}
    rows = []
    for name, (tgt, x) in features(df).items():
        x = np.asarray(x, float)
        ok = np.isfinite(x)  # rest days are undefined for a team's first game of a season
        x, r = x[ok], resid[tgt][ok]
        sd = x.std()
        if sd == 0:
            continue
        z = (x - x.mean()) / sd
        m = sm.OLS(r, sm.add_constant(z)).fit(cov_type="HC1")
        rows.append({"test": name, "target": "reg total - lam_sum" if tgt == "tot" else "reg margin - lam_diff", "coef_per_sd": float(m.params[1]), "se": float(m.bse[1]),
                     "t": float(m.tvalues[1]), "p": float(m.pvalues[1]), "n": int(len(z))})
    out = pd.DataFrame(rows)
    out["p_bh"], out["bh_sig_q10"] = bh(out["p"].to_numpy())
    return out
