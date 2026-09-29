"""Simulator invariants: reproducible seed, probability sums, monotone ladders, OT/SO handling, sane distributions."""

import numpy as np
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from nhl_edge.sim.engine import SimConfig, TeamParams, ladder_violations, simulate_game


def sim(lh=3.2, la=2.8, seed=11, n=20000, **kw):
    return simulate_game(TeamParams(1, "H", lh), TeamParams(2, "A", la), seed=seed, config=SimConfig(n_sims=n, **kw))


def test_reproducible_seed():
    a, b = sim(seed=5), sim(seed=5)
    assert np.array_equal(a.home_final, b.home_final) and np.array_equal(a.away_final, b.away_final) and np.array_equal(a.shootout, b.shootout)
    assert not np.array_equal(sim(seed=6).home_final, a.home_final)


def test_no_ladder_violations_default():
    assert ladder_violations(sim()) == []


@settings(max_examples=25, deadline=None)
@given(lh=st.floats(1.5, 5.0), la=st.floats(1.5, 5.0), seed=st.integers(0, 10_000))
def test_ladders_and_sums_hold_for_any_strengths(lh, la, seed):
    r = sim(lh, la, seed=seed, n=4000)
    assert ladder_violations(r) == []
    ph, pa = r.p_win(True)[0], r.p_win(False)[0]
    assert ph + pa == pytest.approx(1.0)
    assert (r.home_final != r.away_final).all(), "NHL games always have a winner"


def test_overtime_and_shootout_semantics():
    r = sim()
    tied = r.home_reg == r.away_reg
    assert np.array_equal(r.overtime, tied)
    assert r.shootout[~tied].sum() == 0
    # winner of OT/SO gets exactly one extra goal; regulation-decided games keep their score
    assert ((r.home_final + r.away_final) - (r.home_reg + r.away_reg))[tied].tolist() == [1] * int(tied.sum())
    assert ((r.home_final + r.away_final) - (r.home_reg + r.away_reg))[~tied].sum() == 0
    p_ot = r.p_overtime()[0]
    assert 0.10 < p_ot < 0.35
    assert r.p_shootout()[0] == pytest.approx(p_ot * (1 - SimConfig().p_ot_goal), abs=0.02)


def test_score_distribution_is_sane():
    r = sim(3.1, 3.1)
    s = r.summary()
    assert 5.5 < s["total_mean"] < 7.5
    assert 0.7 < s["total_var_over_mean"] < 1.4
    assert abs(s["p_home_win"] - 0.5) < 0.03
    assert s["home_puckline_ladder"]["home_by_more_than_-1.5"] > s["home_puckline_ladder"]["home_by_more_than_1.5"]
    assert 0.5 < s["p_btts"] < 0.98


def test_stronger_team_wins_more_and_scores_more():
    r = sim(3.8, 2.4)
    assert r.p_win(True)[0] > 0.65
    assert r.home_final.mean() > r.away_final.mean() + 0.8


def test_empty_net_window_raises_puckline_cover_vs_plain_poisson():
    base = sim(3.0, 3.0, en_leader_mult=1.0, pull_attack_mult=1.0)
    en = sim(3.0, 3.0)
    # goalie pulls convert some one-goal leads into two-goal wins: P(margin > 1.5) rises, P(margin == 1) falls
    assert en.p_margin_gt(True, 1.5)[0] > base.p_margin_gt(True, 1.5)[0]


def test_environment_dispersion_is_off_by_default_and_widens_totals_when_on():
    off = sim(3.0, 3.0)
    on = sim(3.0, 3.0, env_dispersion=0.15)
    assert SimConfig().env_dispersion == 0.0
    assert on.total.var() > off.total.var()


def test_invalid_lambda_rejected():
    with pytest.raises(ValueError):
        sim(0.0, 3.0)
