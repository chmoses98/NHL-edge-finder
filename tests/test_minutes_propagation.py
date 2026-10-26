from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.research import minutes_propagation as P


def _frame(n=6):
    rng = np.random.default_rng(0)
    last3 = np.resize([15.0, 20.0, np.nan, 17.0, 14.0, 18.0], n)
    d = pd.DataFrame({"game_id": np.arange(n) // 2, "player_id": np.arange(n), "season": [2023] * (n // 2) + [2024] * (n - n // 2), "shifts_ok": True, "last3_toi": last3})
    for s, m in (("ev", 13.0), ("pp", 1.2), ("sh", 1.0), ("ea", 0.2), ("en", 0.1), ("ot", 0.04)):
        d[f"ch_toi_{s}"] = m
        d[f"y_toi_{s}"] = m * (1.2 if s in ("pp", "sh") else 1.0)
    d["ch_rate_ev"], d["ch_rate_pp"], d["ch_rate_sh"] = 6.0, 7.0, 2.0
    d["ch_toi"] = sum(d[f"ch_toi_{s}"] for s in P.STATES)
    d["y_toi"] = sum(d[f"y_toi_{s}"] for s in P.STATES)
    d["y_toi_pp"] = d["y_toi_pp"]
    d["y_sog"] = rng.poisson(2.0, n).astype(float)
    return d


def test_shots_identity_state_minutes_times_rate_per_60():
    d = _frame()
    toi = {s: d[f"ch_toi_{s}"].to_numpy(float) for s in P.STATES}
    got = P.shots_from_states(d, toi)
    assert np.allclose(got, (13.0 * 6.0 + 1.2 * 7.0 + 1.0 * 2.0) / 60.0)


def test_state_factors_fit_on_training_rows_only_and_recover_the_bias():
    d = _frame()
    k = P.fit_state_factors(d[d["season"] == 2023])
    assert abs(k["pp"] - 1.2) < 1e-9 and abs(k["sh"] - 1.2) < 1e-9 and abs(k["ev"] - 1.0) < 1e-9
    d2 = d[d["season"] == 2024].copy()
    for s in P.STATES:
        d2[f"k_{s}"] = k[s]
    arms = P.arm_table(d2, None)
    assert abs((arms["CH_STATECAL"]["pp"] - d2["y_toi_pp"].to_numpy(float)).mean()) < 1e-9 and (arms["CH"]["pp"] < arms["CH_STATECAL"]["pp"]).all()


def test_usage_multiplier_is_neutral_without_three_known_games_and_clipped():
    d = _frame()
    u = P.usage_multiplier(d, np.full(len(d), 16.0))
    assert u[2] == 1.0 and u[1] > 1.0 > u[4] and (u >= np.exp(-1)).all() and (u <= np.e).all()
    assert abs(u[1] - np.exp(0.23 * np.log(21.0 / 17.0))) < 1e-12


def test_poisson_deviance_is_zero_at_the_observation_and_positive_elsewhere():
    y = np.array([0.0, 2.0, 5.0])
    assert np.allclose(P.poisson_dev(y, y + 1e-12), 0.0, atol=1e-6) and (P.poisson_dev(y, np.array([1.0, 1.0, 1.0])) > 0).all()


def test_scoring_reports_paired_differences_against_the_champion_arm():
    d = _frame(40)
    d["game_id"] = np.arange(40) // 2
    d["season"] = 2024
    for s in P.STATES:
        d[f"k_{s}"] = 1.2 if s in ("pp", "sh") else 1.0
    out = P.score(d, P.arm_table(d, None), n_boot=200)
    assert out["CH_STATECAL"]["vs_CH"]["toi"]["delta"] < 0 and "vs_CH" not in out["CH"] and out["CH"]["bias"]["pp"] < 0
