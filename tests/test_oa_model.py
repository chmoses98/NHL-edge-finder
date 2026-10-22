from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.features.ratings import LeagueRates
from nhl_edge.research.oa_model import OAConfig, OAData, fit_oa, oa_team_ratings

TEAMS = [f"T{i:02d}" for i in range(12)]
START = pd.Timestamp("2025-01-01")


def _dates(days):
    ts = START + pd.to_timedelta(np.asarray(days, int), unit="D")
    return ts.strftime("%Y%m%d").astype(int).to_numpy(), ((ts - pd.Timestamp("1970-01-01")).days).to_numpy(float)


def _after(data):
    return int((pd.Timestamp(str(int(data.date.max()))) + pd.Timedelta(days=1)).strftime("%Y%m%d"))


def _cut(day):
    return int((START + pd.Timedelta(days=day)).strftime("%Y%m%d"))


def _data(seed=0, n_days=120, att=None, dfn=None, home=0.25, mu=3.0):
    """Round-robin-ish schedule with a planted attack/defence structure; Gaussian noise on the per-60 rate."""
    rng = np.random.default_rng(seed)
    n = len(TEAMS)
    att = rng.normal(0, 0.3, n) if att is None else att
    dfn = rng.normal(0, 0.3, n) if dfn is None else dfn
    rows = []
    for day in range(n_days):
        order = rng.permutation(n)
        for k in range(0, n, 2):
            h, a = order[k], order[k + 1]
            rows.append((day, h, a, 1, mu + home / 2 + att[h] + dfn[a] + rng.normal(0, 0.5)))
            rows.append((day, a, h, 0, mu - home / 2 + att[a] + dfn[h] + rng.normal(0, 0.5)))
    date, day = _dates([r[0] for r in rows])
    y = np.array([r[4] for r in rows])
    return OAData(date=date, day=day, season=np.full(len(rows), 2025), att=np.array([r[1] for r in rows]), dfn=np.array([r[2] for r in rows]),
                  home=np.array([r[3] for r in rows]), minutes=np.full(len(rows), 60.0), y={"xg": y, "xg_sva": y, "goals": y}, teams=list(TEAMS)), att, dfn


def test_ridge_recovers_planted_attack_and_defence():
    data, att, dfn = _data()
    fit = fit_oa(data, _after(data), 2025, OAConfig(half_life_days=1e6, ridge=2.0, season_discount=1.0, target="xg"))
    assert np.corrcoef(fit.a, att)[0, 1] > 0.9 and np.corrcoef(fit.d, dfn)[0, 1] > 0.9
    assert abs(fit.mu - 3.0) < 0.1 and abs(fit.home_effect - 0.25) < 0.15


def test_opponent_adjustment_separates_schedule_from_strength():
    """Team 0 is average but only ever plays terrible defences: the raw average is inflated, the adjusted attack must not be."""
    n = len(TEAMS)
    att = np.zeros(n)
    dfn = np.zeros(n)
    dfn[1:4] = 0.8                                   # three terrible defences
    rng = np.random.default_rng(3)
    date, tm, op, hm, y = [], [], [], [], []
    for day in range(150):
        for t in range(n):
            opp = rng.choice([1, 2, 3]) if t == 0 else rng.choice([o for o in range(n) if o != t])
            date.append(day)
            tm.append(t)
            op.append(opp)
            hm.append(int(rng.integers(0, 2)))
            y.append(3.0 + att[t] + dfn[opp] + rng.normal(0, 0.4))
    date, day = _dates(date)
    data = OAData(date=date, day=day, season=np.full(len(y), 2025), att=np.array(tm), dfn=np.array(op),
                  home=np.array(hm), minutes=np.full(len(y), 60.0), y={"xg": np.array(y), "xg_sva": np.array(y), "goals": np.array(y)}, teams=list(TEAMS))
    raw0 = data.y["xg"][data.att == 0].mean() - data.y["xg"].mean()
    fit = fit_oa(data, _after(data), 2025, OAConfig(half_life_days=1e6, ridge=5.0, season_discount=1.0, target="xg"))
    assert raw0 > 0.4                      # the raw view says team 0 is a strong attack
    assert abs(fit.a[0]) < 0.25            # the adjusted view says it is average


def test_no_lookahead_rows_on_or_after_as_of_never_change_the_fit():
    data, _, _ = _data(seed=5)
    cut = _cut(60)
    cfg = OAConfig(half_life_days=60.0, ridge=10.0, season_discount=0.5, target="xg")
    base = fit_oa(data, cut, 2025, cfg)
    poisoned = OAData(**{**data.__dict__, "y": {k: np.where(data.date >= cut, 99.0, v) for k, v in data.y.items()}})
    again = fit_oa(poisoned, cut, 2025, cfg)
    assert np.array_equal(base.a, again.a) and np.array_equal(base.d, again.d) and base.mu == again.mu


def test_ridge_shrinks_sparse_teams_toward_league_average():
    data, _, _ = _data(seed=7, n_days=6)
    loose = fit_oa(data, _after(data), 2025, OAConfig(half_life_days=1e6, ridge=0.5, season_discount=1.0, target="xg"))
    tight = fit_oa(data, _after(data), 2025, OAConfig(half_life_days=1e6, ridge=80.0, season_discount=1.0, target="xg"))
    assert np.abs(tight.a).mean() < np.abs(loose.a).mean() and np.abs(tight.d).mean() < np.abs(loose.d).mean()


def test_team_ratings_are_v1_compatible_and_cold_teams_are_league_average():
    data, _, _ = _data()
    fit = fit_oa(data, _after(data), 2025, OAConfig(target="xg"))
    lg = LeagueRates(xg60=3.0, g60=3.0, n_games=100, as_of="2025-05-01")
    h, a = oa_team_ratings(fit, data, "T00", "ZZZ", lg)       # ZZZ never played
    assert h.games_used > 0 and h.off_xg60 > 0 and h.def_xg60 > 0
    assert a.off_xg60 == 3.0 and a.def_xg60 == 3.0 and a.games_used == 0.0


def test_slope_calibrator_identity_until_burn_in_then_corrects_over_spread_totals():
    from nhl_edge.research.oa_model import SlopeCalibrator

    rng = np.random.default_rng(0)
    cal = SlopeCalibrator(burn_in=50)
    days = pd.date_range("2025-01-01", periods=400, freq="D").strftime("%Y-%m-%d")
    for i, day in enumerate(days):
        s = 6.2 + rng.normal(0, 0.4)                       # predicted total varies a lot ...
        d = 0.2 + rng.normal(0, 0.15)                      # ... predicted difference varies little
        lam_h, lam_a = (s + d) / 2, (s - d) / 2
        if i < 10:
            assert cal.transform(day, lam_h, lam_a) == (lam_h, lam_a)   # burn-in: untouched
        total = 6.2 + 0.1 * (s - 6.2) + rng.normal(0, 2.3)             # truth: totals barely depend on s ...
        margin = 0.2 + 3.0 * (d - 0.2) + rng.normal(0, 2.3)            # ... margins depend on d three times more than predicted
        cal.observe(day, lam_h, lam_a, total, margin)
    b_s, b_d = cal.slopes("2026-02-01")
    assert b_s < 0.5 and b_d > 1.5
    h, a = cal.transform("2026-02-01", 3.4, 2.8)
    assert abs((h + a) - 6.2) < abs(3.4 + 2.8 - 6.2) + 1e-9 or abs((h + a) - (3.4 + 2.8)) < 0.5   # total pulled toward the prior mean level
    assert (h - a) > (3.4 - 2.8)                                                                       # difference stretched


def test_slope_calibrator_never_uses_same_day_games():
    from nhl_edge.research.oa_model import SlopeCalibrator

    cal = SlopeCalibrator(burn_in=2)
    for i in range(3):
        cal.observe("2025-01-01", 3.0, 3.0, 6.0 + i, 0.0)
    assert cal.slopes("2025-01-01") == (1.0, 1.0)      # three games on the same day: none is yet committed
    assert len(cal._s) == 0
    cal.slopes("2025-01-02")
    assert len(cal._s) == 3
