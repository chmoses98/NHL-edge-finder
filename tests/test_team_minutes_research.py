"""The two team-minute research modules on synthetic frames: no leakage across seasons in the fit, the pregame filter of the shadow scorer, marker rows, degenerate samples."""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.research import team_minutes_recal as R
from nhl_edge.research import team_minutes_shadow as S


def _frame(season: int, n_games: int = 40, scale: float = 1.0, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed + season)
    rows = []
    for g in range(n_games):
        for team in (1, 2):
            for p in range(18):
                r = {"game_id": season * 1000 + g, "team_id": team, "player_id": team * 100 + p, "season": season, "p_pp": 0.21, "ppmin_for": 4.6, "ppmin_opp": 4.6, "game_ot": False}
                for s, (sh, y) in {"ev": (0.27, 13.5), "pp": (0.28, 1.3), "sh": (0.22, 1.1), "ea": (0.16, 0.2), "en": (0.15, 0.15), "ot": (0.0, 0.0)}.items():
                    r[f"ch_share_{s}"] = sh
                    r[f"ch_toi_{s}"] = sh * {"ev": 50.6, "pp": 4.4, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}[s]
                    r[f"y_toi_{s}"] = y * scale * rng.uniform(0.8, 1.2)
                rows.append(r)
    return pd.DataFrame(rows)


def _reg(seasons, n_games=40):
    rows = []
    for season in seasons:
        for g in range(n_games):
            for team in (1, 2):
                rows.append({"game_id": season * 1000 + g, "team_id": team, "is_home": team == 1, "season": season, "game_type": 2, "n_seconds": 3600, "sec_ev": 2900.0, "sec_pp": 310.0,
                             "sec_sh": 310.0, "sec_ea": 40.0, "sec_en": 40.0})
    return pd.DataFrame(rows)


INFO = {"expected_ot_clock_min_by_season": {2022: 0.7, 2023: 0.7, 2024: 0.7}, "n_games_by_season": {2022: 40, 2023: 40, 2024: 40}}


def test_the_fit_uses_only_the_requested_seasons():
    train = pd.concat([_frame(2022), _frame(2023), _frame(2024, scale=3.0)], ignore_index=True)       # a "future" season with wildly different minutes
    reg = _reg((2022, 2023, 2024))
    a = R.fit_params(train, reg, INFO, (2022, 2023))
    b = R.fit_params(train[train["season"] != 2024], reg, INFO, (2022, 2023))
    assert a.kappa == b.kappa and a.pp_per_ppmin == b.pp_per_ppmin and a.ot_min == b.ot_min
    assert a.provenance["train_seasons"] == [2022, 2023]
    c = R.fit_params(train, reg, INFO, (2022, 2023, 2024))
    assert c.kappa["ev"] > 1.5 * a.kappa["ev"]                                                       # and the future season does move the fit when it IS requested


def test_minutes_arms_score_a_season_with_parameters_from_earlier_seasons_only():
    tr, te = pd.concat([_frame(2022), _frame(2023)], ignore_index=True), _frame(2024, scale=1.0)
    arms, prm = R.minutes_arms(te, tr, _reg((2022, 2023, 2024)), INFO, (2022, 2023))
    assert prm.provenance["train_seasons"] == [2022, 2023] and set(arms) == {"L0_incumbent", "L1_level_refit", "L2_ot_memo", "L3_clock_no_matchup", "L4_candidate"}
    assert (arms["L2_ot_memo"]["ot"] == 0).all() and (arms["L4_candidate"]["ot"] == 0).all()


def test_identities_and_skater_budget_on_a_consistent_frame():
    reg = _reg((2022,))
    ident = R.identities(reg.assign(sec_ev=2900.0))
    assert ident["pp_home_equals_sh_away"] == 1.0 and ident["states_sum_to_3600"] == 1.0
    sb = R.skater_budget(_frame(2022), reg)
    assert sb["n_regulation_team_games"] == 80 and 4.0 < sb["by_state"]["ev"]["skaters_on_ice"] < 6.0


def _shadow_rows(minutes_to_start, t, pid=1, game="2026020001", pos="F", marker=False, team="AAA"):
    r = {"game_id": game, "player_id": pid, "pos": pos, "name": f"P{pid}", "team": team, "predicted_at_utc": t, "minutes_to_start": minutes_to_start, "pregame": minutes_to_start > 0,
         "published_allocation": "team-minutes-0", "candidate_version": "team-minutes-1.0", "clock_fallback": False, "projection_quality": "STANDARD"}
    for k, (a, b) in {"toi": (16.0, 16.5), "ev": (13.0, 13.2), "pp": (1.5, 1.8), "sh": (1.0, 1.2), "sog": (2.0, 2.1)}.items():
        r[f"legacy_{k}"], r[f"cand_{k}"] = a, b
    for s in ("pp", "sh"):
        r[f"legacy_team_{s}"], r[f"cand_team_{s}"] = 4.4, 5.1
    if marker:
        return {"marker": True, "player_id": None, "predicted_at_utc": t, "default_reason": "x"}
    return r


def test_last_pregame_row_is_used_and_post_drop_rows_are_ineligible():
    rows = pd.DataFrame([_shadow_rows(120, "2026-10-25T20:00:00Z"), _shadow_rows(45, "2026-10-25T21:15:00Z"), _shadow_rows(-5, "2026-10-25T22:05:00Z")])
    last = S.last_pregame(rows)
    assert len(last) == 1 and float(last["minutes_to_start"].iloc[0]) == 45.0


def test_marker_rows_are_ignored_when_loading(tmp_path):
    import json

    f = tmp_path / "rows.json"
    f.write_text(json.dumps([_shadow_rows(45, "2026-10-25T21:15:00Z"), _shadow_rows(0, "2026-10-25T21:15:00Z", marker=True)]))
    d = S.load_rows(None, [f])
    assert len(d) == 1 and d["player_id"].notna().all()


def test_compare_on_a_tiny_or_one_sided_sample_does_not_crash_and_estimates_nothing():
    rows = pd.DataFrame([_shadow_rows(45, "2026-10-25T21:15:00Z", pid=i) for i in range(5)])
    act = pd.DataFrame([{"game_id": "2026020001", "player_id": i, "toi_s": 1000, "toi_pp_s": 90, "toi_sh_s": 60, "toi_ev_s": 850, "sog": 2} for i in range(5)])
    out = S.compare(rows, act, n_boot=50)
    assert out["n_paired_before_game_eligibility"] == 5 and out["n_paired_with_outcome"] == 0 and out["n_eligible_games"] == 0 and "note" in out       # 5 paired players is not a settled game
    assert S.representatives(S.merged_pairs(rows, act)) == []                                       # forwards only: no archetypes, no exception


def test_compare_reports_the_known_difference_between_arms():
    rng = np.random.default_rng(3)
    rows, act = [], []
    for g in range(30):
        for i in range(20):
            pid = g * 100 + i
            rows.append(_shadow_rows(45, "2026-10-25T21:15:00Z", pid=pid, game=f"20260200{g:02d}", pos="F" if i % 3 else "D", team="AAA" if i < 10 else "BBB"))
            act.append({"game_id": f"20260200{g:02d}", "player_id": pid, "toi_s": 16.5 * 60 + rng.normal(0, 60), "toi_pp_s": 108 + rng.normal(0, 20), "toi_sh_s": 72, "toi_ev_s": 800,
                        "sog": int(rng.poisson(2))})
    out = S.compare(pd.DataFrame(rows), pd.DataFrame(act), n_boot=200)
    r = out["results"]
    assert out["n_games"] == 30 and abs(r["cand"]["bias"]["toi"]) < abs(r["legacy"]["bias"]["toi"])
    assert r["cand_minus_legacy"]["mse_toi"]["delta"] < 0 and out["clock_fallback_share"] == 0.0 and out["both_arms_on_the_same_row"] is True
    assert len(S.representatives(S.merged_pairs(pd.DataFrame(rows), pd.DataFrame(act)))) >= 7
