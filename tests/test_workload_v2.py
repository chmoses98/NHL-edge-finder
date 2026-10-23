from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import workload_v1 as W
from nhl_edge.research import workload_v2 as V2


def _pred(seasons=(2021, 2022, 2023), n=4000, seed=3, planted=(0.7, 0.85, 1.0, 1.15, 1.3)):
    """Point-in-time prediction frame as ``skater_predictions`` returns it: predicted TOI, league-rate columns, state seconds and actual shots whose true
    multiplier over the league rate depends on the TOI quintile (depth players shoot less)."""
    rng = np.random.default_rng(seed)
    rows = []
    for s in seasons:
        for pos, base in (("F", 14.0), ("D", 17.0)):
            toi = np.clip(rng.normal(base, 3.0, n), 4, 28)
            edges = np.quantile(toi, [0.2, 0.4, 0.6, 0.8])
            tier = np.searchsorted(edges, toi, side="right")
            lgr = 8.0 if pos == "F" else 5.0                       # league shots per 60
            t_ev = toi * 60.0
            exp = t_ev / 3600.0 * lgr
            mult = np.asarray(planted)[tier]
            shots = rng.poisson(exp * mult * 1.0)
            d = pd.DataFrame({"season": s, "game_type": 2, "pos": pos, "wl_toi": toi, "wl_adj": 1.0, "sog": shots, "t_evreg": t_ev})
            for st in W.STATES_W:
                if st != "evreg":
                    d[f"t_{st}"] = 0.0
                d[f"lgr_{st}"] = lgr
            rows.append(d)
    return pd.concat(rows, ignore_index=True)


def test_fit_role_prior_recovers_the_planted_role_multipliers():
    rp = V2.fit_role_prior(_pred(n=30000), [2021, 2022])
    for pos in ("F", "D"):
        assert rp["mu"][pos] == pytest.approx([0.7, 0.85, 1.0, 1.15, 1.3], abs=0.03)
        assert len(rp["edges"][pos]) == 4 and sorted(rp["edges"][pos]) == rp["edges"][pos]
    assert rp["seasons"] == [2021, 2022] and rp["n_buckets"] == 5


def test_fit_role_prior_uses_only_the_seasons_it_is_given_and_skips_rows_without_minutes():
    p = _pred(n=2000)
    p.loc[p["season"] == 2023, "sog"] = 999                                  # a later season with absurd shots must not leak into an earlier fit
    rp = V2.fit_role_prior(p, [2021, 2022])
    assert max(max(v) for v in rp["mu"].values()) <= V2.MU_CLIP[1] and max(max(v) for v in rp["mu"].values()) < 1.5
    q = p.copy()
    q.loc[q["season"] == 2021, "t_evreg"] = np.nan                           # no shift-chart minutes -> excluded from the multipliers
    rp2 = V2.fit_role_prior(q, [2021, 2022])
    assert sum(rp2["n_rows"]["F"]) == int(((q["season"] == 2022) & (q["pos"] == "F")).sum())


def test_multipliers_are_clipped_and_empty_buckets_default_to_one():
    p = _pred(n=2000)
    p.loc[p["pos"] == "D", "sog"] = 0
    assert V2.fit_role_prior(p, [2021])["mu"]["D"] == [V2.MU_CLIP[0]] * 5
    only_f = V2.fit_role_prior(p[p["pos"] == "F"], [2021])
    assert only_f["mu"]["D"] == [1.0] * 5 and only_f["n_rows"]["D"] == [0] * 5            # no defencemen in training: neutral prior, no crash


def test_role_multiplier_is_one_without_a_prior_and_picks_the_quintile_with_one():
    pos = np.array(["F", "F", "F", "D", "D"])
    toi = np.array([8.0, 14.0, 22.0, 12.0, 25.0])
    assert W.role_multiplier(pos, toi, None).tolist() == [1.0] * 5
    rp = {"edges": {"F": [10.0, 13.0, 16.0, 19.0], "D": [14.0, 16.0, 18.0, 20.0]}, "mu": {"F": [0.7, 0.85, 1.0, 1.15, 1.3], "D": [0.6, 0.8, 1.0, 1.2, 1.4]}}
    # F: 8 < 10 -> bucket 0; 14 in [13,16) -> bucket 2; 22 > 19 -> bucket 4.  D: 12 < 14 -> bucket 0; 25 > 20 -> bucket 4
    assert W.role_multiplier(pos, toi, rp).tolist() == [0.7, 1.0, 1.3, 0.6, 1.4]


def test_tier_bias_cuts_by_predicted_toi_and_reports_signed_error():
    m = pd.DataFrame({"wl_toi": np.arange(100.0), "wl_sog": np.r_[np.full(50, 1.2), np.full(50, 2.0)], "y_sog": np.r_[np.full(50, 1.0), np.full(50, 2.0)]})
    t = V2.tier_bias(m, "wl_sog", n=2)
    assert [round(x["bias"], 6) for x in t] == [0.2, 0.0] and [x["n"] for x in t] == [50, 50]


def test_acceptance_adds_one_check_and_leaves_the_frozen_ones_alone():
    rule = {"max_abs_bias_sog": 0.05, "coverage80_band": [0.77, 0.83], "max_abs_tier_bias_sog": 0.06}
    arm = {"bias": 0.01, "coverage80": 0.8, "crps": 0.7}
    ci = {"crps": {"ci95": [-0.01, -0.001]}, "rmse": {"ci95": [-0.01, -0.001]}, "ladder_brier": {"ci95": [-0.01, -0.001]}}
    rep = {"diffs": {"WORKLOAD_V1_minus_CHAMPION": ci, "WORKLOAD_V1_minus_CHAMPION_NB": ci}, "arms": {"WORKLOAD_V1": arm},
           "subgroups": {p: {"WORKLOAD_V1": {"crps": 0.6}, "CHAMPION_NB": {"crps": 0.7}} for p in ("F", "D")},
           "bias_by_tier": {"WORKLOAD_V2": [{"bias": 0.02}, {"bias": -0.03}]}}
    ok = V2.accept_v2(rep, rule)
    assert ok["verdict"] == "ACCEPTED" and len(ok["checks"]) == 8 and ok["checks"]["abs_tier_bias_le_max"]
    rep["bias_by_tier"]["WORKLOAD_V2"][0]["bias"] = 0.13
    bad = V2.accept_v2(rep, rule)
    assert bad["verdict"] == "REJECTED" and not bad["checks"]["abs_tier_bias_le_max"] and bad["checks"]["abs_bias_le_max"]
