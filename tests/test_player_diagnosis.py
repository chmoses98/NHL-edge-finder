from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import player_diagnosis as P


def test_fit_scale_recovers_a_planted_multiplier_for_counts_and_minutes():
    rng = np.random.default_rng(0)
    n = 40_000
    pred = rng.uniform(0.5, 3.0, n)
    x = rng.normal(0, 0.3, n)
    X = np.c_[np.ones(n), x]
    y = rng.poisson(pred * np.exp(0.05 + 0.8 * x)).astype(float)
    b = P.fit_scale(pred, X, y, "poisson")
    assert b[0] == pytest.approx(0.05, abs=0.02) and b[1] == pytest.approx(0.8, abs=0.06)
    ym = pred * np.exp(0.03 + 0.4 * x) + rng.normal(0, 0.5, n)
    bm = P.fit_scale(pred, X, ym, "sq")
    assert bm[0] == pytest.approx(0.03, abs=0.02) and bm[1] == pytest.approx(0.4, abs=0.05)


def test_ewm_prior_uses_only_earlier_rows_and_shrinks_to_the_prior():
    v = np.array([10.0, 10.0, 10.0, 0.0])
    key = np.array(["a", "a", "b", "a"])
    out = P._ewm_prior(v, key, half_life=1e9, prior_value=np.full(4, 4.0), k=1.0)
    assert out[0] == 4.0                                    # nothing before the first row: the prior
    assert out[1] == pytest.approx((10.0 + 4.0) / 2)        # one earlier observation of 10 and one pseudo-observation of 4
    assert out[2] == 4.0                                    # a different key has no history
    assert out[3] == pytest.approx((20.0 + 4.0) / 3)        # the current row (0) never enters its own expectation


def test_signal_test_credits_an_informative_feature_and_not_noise_and_never_looks_ahead():
    rng = np.random.default_rng(1)
    n_per = 6000
    rows = []
    for s in (2022, 2023, 2024, 2025):
        x = rng.normal(0, 0.4, n_per)
        pred = rng.uniform(0.8, 2.5, n_per)
        y = rng.poisson(pred * np.exp(0.9 * x)).astype(float)
        rows.append(pd.DataFrame({"season": s, "game_id": np.arange(n_per) // 10 + s * 100_000, "pred": pred, "y": y, "x": x, "noise": rng.normal(0, 1, n_per)}))
    d = pd.concat(rows, ignore_index=True)
    good = P.signal_test(d, {"x": d["x"].to_numpy()}, "pred", "y", "poisson", seasons=(2023, 2024))
    bad = P.signal_test(d, {"noise": d["noise"].to_numpy()}, "pred", "y", "poisson", seasons=(2023, 2024))
    for s in ("2023", "2024"):
        assert good[s]["feature_gain_net_of_level"]["hi95"] < 0
        assert bad[s]["feature_gain_net_of_level"]["lo95"] < 0 < bad[s]["feature_gain_net_of_level"]["hi95"] or abs(bad[s]["feature_gain_net_of_level"]["delta"]) < 5e-4
    # the 2023 fit uses 2022 only: the first test season's training rows are exactly the earlier season
    assert good["2023"]["n"] == n_per


def test_pp_error_split_attributes_game_level_error_to_the_penalty_count():
    rng = np.random.default_rng(2)
    rows = []
    for g in range(400):
        team_pp = rng.gamma(4, 1.2)                            # realised team PP minutes, unpredictable
        pred_team = 4.8
        share = rng.dirichlet(np.ones(5) * 3)
        for j in range(5):
            rows.append({"game_id": g, "team_id": 1, "opp_id": 2, "season": 2025, "date_int": g, "player_id": j, "y_toi_pp": 5 * team_pp * share[j],   # five skaters share each PP minute
                         "ch_toi_pp": pred_team, "team_pp_min": pred_team, "y_toi_sh": 0.0, "y_sog": 0.0, "shifts_ok": True})
    d = pd.DataFrame(rows)
    out = P.pp_error_split(d)["2025"]
    assert 0.0 < out["share_game_level"] <= 1.0 and out["mse_with_realised_team_pp"] < out["mse"]


def test_points_diagnosis_reports_bias_slope_and_oracles():
    rng = np.random.default_rng(3)
    n = 20_000
    e_g = rng.uniform(0.05, 0.4, n)
    e_a = rng.uniform(0.1, 0.6, n)
    sk = pd.DataFrame({"game_id": np.arange(n) // 18, "team_id": (np.arange(n) // 9) % 2, "pos": np.where(np.arange(n) % 3 == 0, "D", "F"), "date_int": np.arange(n) // 18,
                       "e_g": e_g, "e_a": e_a, "e_p": e_g + e_a, "exp_toi": 16.0, "toi_s": 16 * 60.0})
    sk["y_g"], sk["y_a"] = rng.poisson(e_g).astype(float), rng.poisson(e_a).astype(float)
    sk["y_p"] = sk["y_g"] + sk["y_a"]
    out = P.points_diagnosis(sk)
    assert abs(out["points"]["bias"]) < 0.02 and out["points"]["calibration_slope"] == pytest.approx(1.0, abs=0.08)
    assert out["points"]["dispersion_mse_over_mean"] == pytest.approx(1.0, abs=0.05)
    assert abs(out["oracle_toi"]["p"]) < 1e-9                 # realised TOI equals expected TOI here, so rescaling by it changes nothing
