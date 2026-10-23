"""WORKLOAD_V1_LC: the level factor uses only strictly earlier days, shrinks to 1 with no history, and removes a constant bias."""

from __future__ import annotations

import numpy as np

from nhl_edge.research import workload_level_cal as L


def test_first_day_and_same_day_rows_get_factor_one_and_never_inform_each_other():
    day = np.array([10, 10, 10, 11])
    y = np.array([3.0, 3.0, 3.0, 1.0])
    yhat = np.array([1.0, 1.0, 1.0, 1.0])
    f = L.level_factors(day, y, yhat)
    assert f[0] == f[1] == f[2] == 1.0 and f[3] > 1.0           # day 11 sees day 10's outcomes (9 vs 3 expected shots)


def test_a_future_outcome_cannot_change_an_earlier_factor():
    rng = np.random.default_rng(0)
    day = np.repeat(np.arange(30), 20)
    yhat = rng.uniform(0.5, 2.0, len(day))
    y = rng.poisson(yhat).astype(float)
    f1 = L.level_factors(day, y, yhat)
    y2 = y.copy()
    y2[day == 20] += 50.0
    f2 = L.level_factors(day, y2, yhat)
    assert np.array_equal(f1[day <= 20], f2[day <= 20]) and not np.allclose(f1[day > 20], f2[day > 20])


def test_a_constant_overprediction_is_corrected_and_the_prior_limits_early_overreaction():
    rng = np.random.default_rng(1)
    day = np.repeat(np.arange(120), 200)
    yhat = np.full(len(day), 1.6)
    y = rng.poisson(1.6 * 0.97, len(day)).astype(float)         # model is 3% too high
    f = L.level_factors(day, y, yhat)
    assert abs(f[day >= 60].mean() - 0.97) < 0.01
    assert abs(f[day == 1].mean() - 1.0) < 0.2                   # K = 1,000 shots keeps day-2 from swinging on 200 rows


def test_decay_forgets_old_level_errors():
    day = np.concatenate([np.zeros(500, int), np.full(500, 400)])
    y = np.concatenate([np.full(500, 2.0), np.full(500, 1.0)])
    yhat = np.ones(1000)
    f = L.level_factors(day, y, yhat, half_life=60.0)
    assert f[-1] < 1.01 * (500 * 0.5 ** (400 / 60) * 2 + 1000) / (500 * 0.5 ** (400 / 60) + 1000)


def test_constants_are_the_registered_ones():
    assert L.H_DAYS == 60.0 and L.K_SHOTS == 1000.0 and L.BIAS_LIMIT == 0.02
