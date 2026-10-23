"""Regime diagnostics: the per-season statistics recover planted structure, and the oracle machinery behaves."""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.research import regime_analysis as RA


def _games(seed=0, seasons=(2014, 2015), n_teams=12, per=300, spread=0.5):
    rng = np.random.default_rng(seed)
    rows = []
    gid = 0
    for s in seasons:
        strength = rng.normal(0, spread, n_teams)
        for i in range(per):
            h, a = rng.choice(n_teams, 2, replace=False)
            lam_h, lam_a = 3.0 + 0.5 * (strength[h] - strength[a]) / 2, 3.0 - 0.5 * (strength[h] - strength[a]) / 2
            rows.append({"game_id": gid, "season": s, "game_date": f"{s}-{1 + i // 30:02d}-{1 + i % 28:02d}", "home": f"T{h}", "away": f"T{a}", "home_score": rng.poisson(lam_h), "away_score": rng.poisson(lam_a),
                         "last_period_type": "REG", "home_b2b": False, "away_b2b": False})
            gid += 1
    return pd.DataFrame(rows)


def test_season_stats_and_strength_spread_recover_the_planted_scale():
    g = _games()
    st = RA.season_stats(g)
    assert abs(st["goals_per_game"].mean() - 6.0) < 0.3 and set(st.index) == {2014, 2015}
    wide = RA.team_strength_spread(_games(spread=1.5, per=600))
    narrow = RA.team_strength_spread(_games(spread=0.1, per=600))
    assert wide["sd_gd_true"].mean() > narrow["sd_gd_true"].mean() + 0.1
    assert (wide["reliability"] > narrow["reliability"]).all() or wide["reliability"].mean() > narrow["reliability"].mean()


def test_persistence_is_high_when_strength_carries_over():
    rng = np.random.default_rng(1)
    rows = []
    strength = rng.normal(0, 1.0, 16)
    for s in (2014, 2015, 2016):
        st = strength if s != 2016 else rng.normal(0, 1.0, 16)           # 2015 repeats 2014's strengths, 2016 is a reshuffle
        for i in range(800):
            h, a = rng.choice(16, 2, replace=False)
            rows.append({"season": s, "home": f"T{h}", "away": f"T{a}", "home_score": rng.poisson(max(3 + 0.4 * (st[h] - st[a]), 0.5)), "away_score": rng.poisson(max(3 - 0.4 * (st[h] - st[a]), 0.5))})
    p = RA.persistence(pd.DataFrame(rows))
    assert p[2015] > 0.6 and abs(p[2016]) < 0.6 and p[2015] > p[2016]


def test_calibration_drift_slopes_are_one_for_a_calibrated_model_and_flag_overspread():
    rng = np.random.default_rng(2)
    n = 6000
    lam_h, lam_a = rng.uniform(2.4, 3.6, n), rng.uniform(2.4, 3.6, n)
    g = pd.DataFrame({"season": 2020, "V1_lam_home": lam_h, "V1_lam_away": lam_a, "home_score": rng.poisson(lam_h), "away_score": rng.poisson(lam_a)})
    d = RA.calibration_drift(g, "V1")
    assert abs(d.loc[2020, "V1_slope_total"] - 1.0) < 0.12 and abs(d.loc[2020, "V1_slope_margin"] - 1.0) < 0.12
    over = g.assign(V1_lam_home=2.0 + 2.0 * (lam_h - 3.0) + 3.0 - 2.0 + 0.0, V1_lam_away=2.0 + 2.0 * (lam_a - 3.0) + 3.0 - 2.0 + 0.0)
    assert RA.calibration_drift(over, "V1").loc[2020, "V1_slope_total"] < 0.7                   # predictions spread twice as much as outcomes -> slope ~ 0.5


def test_approx_brier_prefers_the_true_rates_and_oracle_reports_the_production_cell():
    rng = np.random.default_rng(3)
    n = 4000
    lh, la = rng.uniform(2.2, 3.8, n), rng.uniform(2.2, 3.8, n)
    hs, as_ = rng.poisson(lh), rng.poisson(la)
    good = RA.approx_brier(lh, la, hs, as_)
    flat = RA.approx_brier(np.full(n, 3.0), np.full(n, 3.0), hs, as_)
    assert good < flat
    combos = {(hl, pr): ((lh, la) if (hl, pr) == (40.0, 5.0) else (np.full(n, 3.0), np.full(n, 3.0))) for hl in RA.GRID_HL for pr in RA.GRID_PRIOR}
    o = RA.oracle_surface(2020, combos, hs.astype(float), as_.astype(float))
    assert o["best_cell"] == "40|5" and o["oracle_gain"] < 0 and o["production_brier"] > o["best_brier"] and o["n_games"] == n


def test_relate_uses_the_previous_season_as_the_leakage_safe_predictor():
    idx = pd.Index(range(2010, 2026), name="season")
    f = pd.DataFrame({"x": np.arange(16, dtype=float)}, index=idx)
    gain = pd.Series(-np.arange(16, dtype=float), index=idx)
    r = RA.relate(gain, f)["x"]
    assert r["same_season"]["rho"] < -0.99 and r["previous_season"]["rho"] < -0.99 and r["previous_season"]["n"] == 15
