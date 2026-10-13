"""Unit tests for the opportunity / efficiency decomposition utilities (research-only; no network, no market input)."""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.research import opportunity_efficiency as oe


def test_recent_mean_is_strictly_before_and_plain():
    df = pd.DataFrame({"player_id": [1] * 13 + [2] * 2, "date_int": list(range(20240101, 20240114)) + [20240101, 20240102],
                       "game_id": list(range(13)) + [100, 101], "x": list(range(1, 14)) + [5.0, 7.0]})
    rm = oe.recent_mean(df, "player_id", ["x"], n=10)
    # first row of each player has no history
    assert np.isnan(rm.loc[0, "rm_x"]) and np.isnan(rm.loc[13, "rm_x"])
    # second row sees only the first game
    assert rm.loc[1, "rm_x"] == 1.0 and rm.loc[14, "rm_x"] == 5.0
    # row 12 (13th game) is the plain mean of games 3..12 (values 3..12), never including itself
    assert rm.loc[12, "rm_x"] == np.mean(np.arange(3, 13))
    assert rm.loc[12, "rs_x"] == np.sum(np.arange(3, 13))
    assert rm.loc[12, "rn"] == 10


def test_recent_mean_ignores_row_order():
    df = pd.DataFrame({"player_id": [1, 1, 1], "date_int": [3, 1, 2], "game_id": [3, 1, 2], "x": [30.0, 10.0, 20.0]})
    rm = oe.recent_mean(df, "player_id", ["x"], n=10)
    assert rm.loc[0, "rm_x"] == 15.0  # date 3 sees dates 1 and 2
    assert np.isnan(rm.loc[1, "rm_x"])


def test_poisson_deviance_zero_at_truth_and_positive_elsewhere():
    y = np.array([0, 1, 4])
    assert np.allclose(oe.poisson_dev(y, np.array([1e-12, 1.0, 4.0])), 0.0, atol=1e-6)
    assert (oe.poisson_dev(y, np.array([1.0, 2.0, 2.0])) > 0).all()


def test_binomial_nll_prefers_the_true_rate():
    rng = np.random.default_rng(0)
    n = rng.integers(1, 10, 5000)
    k = rng.binomial(n, 0.3)
    assert oe.binom_nll(k, n, np.full(len(n), 0.3)).mean() < oe.binom_nll(k, n, np.full(len(n), 0.5)).mean()


def test_cluster_bootstrap_is_paired_deterministic_and_signed():
    g = np.repeat(np.arange(50), 10)
    a = np.ones(500)
    b = np.ones(500) * 0.9
    r1 = oe.cluster_boot(g, a, b, B=200, seed=1)
    r2 = oe.cluster_boot(g, a, b, B=200, seed=1)
    assert r1 == r2
    assert np.isclose(r1["delta"], -0.1) and np.isclose(r1["lo"], -0.1) and np.isclose(r1["hi"], -0.1)
    assert r1["n_games"] == 50 and r1["n_rows"] == 500


def test_cluster_bootstrap_needs_three_games():
    r = oe.cluster_boot(np.array([1, 1, 2]), np.zeros(3), np.ones(3))
    assert np.isnan(r["lo"]) and r["delta"] == 1.0
