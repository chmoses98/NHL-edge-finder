"""Opportunity: skater time on ice (total, non-PP = EV+SH+other, PP), modelled before production.

Ladder
  T_A  season-to-date mean (+ last season), shrunk to a point-in-time role prior
  T_B  EWMA (halflife chosen on development), shrunk to the role prior
  T_C  role / share model: shrunk EWMA share of the team's non-PP and PP time x the team's expected
       non-PP and PP minutes (team PP drawn + opponent PK taken, PIT; expected game length incl. OT)
  T_E  LightGBM on PIT role features (last game's line rank and PP unit from shift data, co-ice line
       continuity, shares, schedule, absences), refitted walk-forward each season

Role buckets come from the previous game's shift data: forwards ranked by non-PP TOI within the team
(F1 = top 3, ... F4), defence by pairs (D1..D3), PP unit by PP-TOI rank (PP1 = top 5).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from pf_core import models, pit

from . import SPLITS

TOI_FEATURES = [
    "toi_ewm3", "toi_ewm10", "toi_ewm30", "toi_last", "toi_std", "toi_prev", "toi_career", "toi_n", "toi_std_n",
    "toi_pp_ewm3", "toi_pp_ewm10", "toi_pp_ewm30", "toi_pp_last", "toi_np_ewm3", "toi_np_ewm10", "toi_np_last",
    "pp_share_ewm3", "pp_share_ewm10", "pp_share_ewm30", "np_share_ewm3", "np_share_ewm10", "np_share_ewm30",
    "rank_np_last", "rank_np_ewm3", "pp_unit_last", "line_last", "is_d", "team_pp_exp", "len_exp",
    "b2b", "rest_days", "missed_games", "new_team", "is_home_i", "travel_km", "opp_b2b", "days_since_last",
    "line_changed_pit", "toi_sh_ewm10",
]


def add_roles(sk: pd.DataFrame) -> pd.DataFrame:
    sk["line_last"] = sk["line_now_last"]
    sk["pp_unit_last"] = sk["pp_unit_now_last"]
    sk["is_d"] = (sk["pos"] == "D").astype(int)
    sk["is_home_i"] = sk["is_home"].astype(int)
    ln = sk["line_last"]
    cap = np.where(sk["pos"] == "D", 3, 4)
    lab = np.where(ln.isna(), "NA", np.minimum(ln.fillna(1), cap).astype(int).astype(str))
    sk["role"] = sk["pos"] + lab
    pu = sk["pp_unit_last"].fillna(-1).astype(int)
    sk["pp_role"] = np.where(pu == 1, "PP1", np.where(pu == 2, "PP2", np.where(pu == 0, "noPP", "NA")))
    sk["team_pp_exp"] = 0.5 * (sk["pp_min_ewm10"].fillna(5.2) + sk["opp_sh_min_ewm10"].fillna(5.2))
    sk["len_exp"] = sk["len_min_ewm30"].fillna(61.0)
    return sk


def role_prior(sk: pd.DataFrame, col: str, by=("role",)) -> pd.Series:
    from .ladder import gprior  # leakage-safe fallback (pf_core group_prior_pit bug)
    return gprior(sk, by, col)


def fit_k(sk: pd.DataFrame, col: str) -> float:
    dev = sk[sk["season"].isin(SPLITS["development"])]
    return pit.estimate_shrinkage_k(dev[col], dev["player_id"].astype(str) + "_" + dev["season"].astype(str))


def toi_models(sk: pd.DataFrame, log: list) -> tuple[pd.DataFrame, dict]:
    """Adds toi_A, toi_B, toi_C(+np/pp), toi_E(+np/pp) columns. Returns (sk, params)."""
    dev = sk["season"].isin(SPLITS["development"]).to_numpy()
    prm = {}
    pri = {c: role_prior(sk, c) for c in ("toi", "toi_np")}
    pri["toi_pp"] = role_prior(sk, "toi_pp", by=("pp_role",))
    for c in ("toi", "toi_np", "toi_pp", "np_share", "pp_share"):
        prm[f"k_{c}"] = fit_k(sk, c)
    sk["toi_A"] = models.est_A(sk, "toi", pri["toi"], prm["k_toi"])
    # halflife for B chosen on development by MSE
    best = None
    for h in (3, 10, 30):
        m = models.est_B(sk, "toi", pri["toi"], prm["k_toi"], h)
        e = float(np.nanmean((m[dev] - sk.loc[dev, "toi"]) ** 2))
        log.append({"step": "toi_B_halflife", "halflife": h, "dev_mse": e})
        if best is None or e < best[1]:
            best = (h, e)
    prm["hl_toi"] = best[0]
    sk["toi_B"] = models.est_B(sk, "toi", pri["toi"], prm["k_toi"], best[0])
    # C: shares of the team's time
    np_pri = role_prior(sk, "np_share")
    pp_pri = role_prior(sk, "pp_share", by=("pp_role",))
    bestc = None
    for h in (3, 10):
        nps = models.est_B(sk, "np_share", np_pri, prm["k_np_share"], h)
        pps = models.est_B(sk, "pp_share", pp_pri, prm["k_pp_share"], h)
        tnp = nps * (sk["len_exp"] - sk["team_pp_exp"])
        tpp = pps * sk["team_pp_exp"]
        e = float(np.nanmean(((tnp + tpp)[dev] - sk.loc[dev, "toi"]) ** 2))
        log.append({"step": "toi_C_halflife", "halflife": h, "dev_mse": e})
        if bestc is None or e < bestc[1]:
            bestc = (h, e, tnp, tpp)
    prm["hl_share"] = bestc[0]
    sk["toi_np_C"], sk["toi_pp_C"] = bestc[2], bestc[3]
    sk["toi_C"] = sk["toi_np_C"] + sk["toi_pp_C"]
    # E: LightGBM, walk-forward by season (train on seasons < s)
    feats = TOI_FEATURES + ["toi_np_C", "toi_pp_C", "toi_B"]
    for tgt in ("toi_np", "toi_pp"):
        sk["_t"] = sk[tgt]
        pred = models.lgbm_walkforward(sk, feats, "_t", "season", objective="regression", min_train_blocks=1,
                                       params={"n_estimators": 300, "learning_rate": 0.05, "num_leaves": 31,
                                               "min_child_samples": 200})
        sk[f"{tgt}_E"] = pred.clip(lower=0)
    sk = sk.drop(columns=["_t"])
    sk["toi_E"] = sk["toi_np_E"] + sk["toi_pp_E"]
    # fallbacks where E has no training block (first season): use C
    for c in ("toi_np", "toi_pp", "toi"):
        sk[f"{c}_E"] = sk[f"{c}_E"].fillna(sk[f"{c}_C"] if c != "toi" else sk["toi_C"])
    prm["features_E"] = feats
    return sk, prm


def toi_eval(sk: pd.DataFrame, mask, models_=("toi_A", "toi_B", "toi_C", "toi_E")) -> list[dict]:
    rows = []
    d = sk[mask]
    for m in models_:
        for tgt, col in (("toi", m), ("toi_pp", m.replace("toi_", "toi_pp_") if m in ("toi_C", "toi_E") else None)):
            if col is None or col not in d:
                continue
            ok = d[tgt].notna() & d[col].notna()
            e = d.loc[ok, col] - d.loc[ok, tgt]
            rows.append({"model": m, "target": tgt, "n": int(ok.sum()), "mae": float(e.abs().mean()),
                         "rmse": float(np.sqrt((e ** 2).mean())), "bias": float(e.mean())})
    return rows


def toi_by_role(sk: pd.DataFrame, mask, col: str, tgt: str = "toi", by: str = "role") -> list[dict]:
    d = sk[mask & sk[tgt].notna() & sk[col].notna()]
    out = []
    for k, g in d.groupby(by):
        e = g[col] - g[tgt]
        out.append({"segment": k, "n": int(len(g)), "mae": float(e.abs().mean()), "bias": float(e.mean()),
                    "mean_actual": float(g[tgt].mean())})
    return out
