from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from nhl_edge.research import player_challengers as C


def _frame(seed=0, with_signal=True):
    rng = np.random.default_rng(seed)
    rows = []
    gid = 0
    for si, season in enumerate((2022, 2023, 2024, 2025)):
        for day in range(40):
            date = 20000101 + si * 10000 + (day // 28) * 100 + day % 28 + 100
            teams = rng.permutation(8)
            for k in range(4):
                gid += 1
                for t, o in ((teams[2 * k], teams[2 * k + 1]), (teams[2 * k + 1], teams[2 * k])):
                    for p in range(12):
                        pid = int(t) * 100 + p
                        exp_toi = 12 + p * 0.5
                        persist = 1.0 + (0.3 if (pid % 5 == 0 and day > 20) else 0.0)         # a role change halfway through the season
                        toi = max(exp_toi * persist * (1.04 if with_signal else 1.0) + rng.normal(0, 2), 0)
                        rows.append({"season": season, "date_int": date, "game_id": gid, "team_id": int(t), "opp_id": int(o), "player_id": pid, "pos": "F", "shifts_ok": True,
                                     "ch_toi": exp_toi, "y_toi": toi, "ch_toi_pp": 1.2, "y_toi_pp": max(rng.normal(1.4, 0.6), 0), "y_toi_sh": 1.0, "ch_toi_sh": 1.0, "team_pp_min": 4.3,
                                     "ch_sog": 1.5, "y_sog": float(rng.poisson(1.6)), "p_pp": 0.2, "game_ot": False, "is_home": True, "y_toi_ev": 10.0, "ch_toi_ev": 10.0})
    return pd.DataFrame(rows).sort_values(["date_int", "game_id"]).reset_index(drop=True)


def test_rolling_level_uses_only_strictly_earlier_days():
    d = _frame()
    base = C.rolling_level(d, "ch_toi", "y_toi")
    d2 = d.copy()
    last_day = d2["date_int"].max()
    d2.loc[d2["date_int"] == last_day, "y_toi"] += 100.0                       # change the outcomes of the final day only
    after = C.rolling_level(d2, "ch_toi", "y_toi")
    same_day = (d["date_int"] == last_day).to_numpy()
    assert np.allclose(base[same_day], after[same_day])                        # rows of that very day cannot see their own outcomes
    assert np.allclose(base[~same_day], after[~same_day])                      # earlier rows cannot see later days


def test_role_features_use_earlier_games_of_the_same_player_only():
    d = _frame()
    f = C.role_features(d)
    i = 5000
    pid = d.loc[i, "player_id"]
    hist = d[(d["player_id"] == pid) & (d.index < i)]["y_toi"].to_numpy()
    if len(hist) >= 9:
        want = np.log((hist[-3:].mean() + 1.0) / (hist[-15:-3].mean() + 1.0))
        assert f["x_role_toi"][i] == pytest.approx(want)


def test_each_stage_is_fitted_on_earlier_seasons_only():
    d = _frame()
    F = C.build_features(d, None)
    roll = np.nan_to_num(C.rolling_level(d, "ch_toi", "y_toi"))
    d_mod = d.copy()
    d_mod.loc[d_mod["season"] >= 2024, "y_toi"] += 50.0                         # corrupt the later seasons
    p1 = C.fit_predict(d, F, "toi", ["x_roll", "x_recent_toi"], 2023, roll)
    p2 = C.fit_predict(d_mod, F, "toi", ["x_roll", "x_recent_toi"], 2023, roll)
    te = (d["season"] == 2023).to_numpy()
    assert np.allclose(p1[te], p2[te]) and np.isnan(p1[~te]).all()               # the 2023 model never saw 2024 outcomes


def test_a_real_usage_signal_is_credited_and_noise_is_not():
    d = _frame(seed=1)
    F = C.build_features(d, None)
    r = C.evaluate_target(d, F, "toi", n_boot=200)
    usage = r["pooled"]["vs_previous"]["+USAGE"]
    assert usage["hi95"] < 0                                                     # the planted recent-usage effect is found
    assert r["pooled"]["loss"]["+USAGE"] < r["pooled"]["loss"]["LEVEL"] < r["pooled"]["loss"]["INCUMBENT"] + 1e-9
    sog = C.evaluate_target(d, F, "sog", n_boot=200)["pooled"]["vs_previous"]["+OPP"]
    assert abs(sog["delta"]) < 0.01 and sog["lo95"] < 0.0005                    # no opponent effect was planted: not credited


def test_stack_on_credits_a_planted_term_and_reports_paired_differences():
    rng = np.random.default_rng(5)
    n = 30_000
    M = pd.DataFrame({"season": np.repeat([2023, 2024, 2025], n // 3), "game_id": np.arange(n) // 12, "base": rng.uniform(10, 20, n), "x": rng.normal(0, 0.15, n)})
    M["y"] = M["base"] * np.exp(0.5 * M["x"]) + rng.normal(0, 2, n)
    r = C.stack_on(M, "base", "y", ["x"], "sq", (2024, 2025), n_boot=200)
    assert r["seasons"] == ["2024", "2025"] and r["loss_stack"] < r["loss_level"] <= r["loss_base"] + 1e-9
    assert r["stack_vs_level"]["hi95"] < 0 and abs(r["coef"]["2024"][1] - 0.5) < 0.1
    noise = M.assign(x=rng.normal(0, 0.15, n))
    r2 = C.stack_on(noise, "base", "y", ["x"], "sq", (2024, 2025), n_boot=200)
    assert r2["stack_vs_level"]["lo95"] < 0.01 < 1 and abs(r2["stack_vs_level"]["delta"]) < 0.02
