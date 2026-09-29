"""DATA_ONLY_V2 research arm: simulator invariants, hazard estimation, special teams, goalie point-in-time discipline."""

import numpy as np
import pandas as pd
import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from nhl_edge import DATA_ONLY_MODEL_VERSION, FEATURE_VERSION, SIM_VERSION
from nhl_edge.features import goalie_talent as gt
from nhl_edge.features import special_teams as stm
from nhl_edge.features.ratings import LeagueRates, TeamRating, expected_goals
from nhl_edge.goalies.state import GoalieState, GoalieStatus
from nhl_edge.research import state_hazards as sh
from nhl_edge.sim.engine import TeamParams, ladder_violations
from nhl_edge.sim.engine_v2 import DIFFS, TIME_EDGES, SimV2Params, load_params, period_violations, simulate_game_v2


def _params(**kw) -> SimV2Params:
    return SimV2Params(**kw)


# ---------------------------------------------------------------------------------------------- versioning
def test_v1_versions_are_frozen():
    assert (DATA_ONLY_MODEL_VERSION, SIM_VERSION, FEATURE_VERSION) == ("DATA_ONLY_V1", "nhl-sim-1.1", "nhl-features-1.0")
    from nhl_edge import DATA_ONLY_V2_MODEL_VERSION, FEATURE_V2_VERSION, SIM_V2_VERSION

    assert DATA_ONLY_V2_MODEL_VERSION == "DATA_ONLY_V2" and SIM_V2_VERSION == "nhl-sim-2.0" and FEATURE_V2_VERSION == "nhl-features-2.0"
    assert DATA_ONLY_V2_MODEL_VERSION != DATA_ONLY_MODEL_VERSION and SIM_V2_VERSION != SIM_VERSION


def test_shipped_sim_params_load_and_have_the_table_shape():
    p = load_params()
    assert np.asarray(p.mult).shape == (len(TIME_EDGES) - 1, len(DIFFS))
    assert 0.4 < p.p_ot_goal < 0.9 and 0.8 < p.scale < 1.2


# ---------------------------------------------------------------------------------------------- simulator
@settings(max_examples=25, deadline=None)
@given(lh=st.floats(1.5, 5.0), la=st.floats(1.5, 5.0), seed=st.integers(0, 2**31 - 1))
def test_periods_sum_to_regulation_on_every_draw_and_probabilities_are_coherent(lh, la, seed):
    res = simulate_game_v2(TeamParams(1, "H", lh), TeamParams(2, "A", la), seed=seed, n_sims=2000, params=load_params())
    assert period_violations(res) == []
    assert np.array_equal(res.home_periods.sum(1), res.home_reg) and np.array_equal(res.away_periods.sum(1), res.away_reg)
    assert ladder_violations(res) == []
    # OT/SO semantics: final = regulation + exactly one goal for the OT/SO winner when tied, nothing otherwise
    tied = res.home_reg == res.away_reg
    assert np.array_equal(res.overtime, tied)
    assert np.all((res.home_final - res.home_reg) + (res.away_final - res.away_reg) == tied.astype(int))
    assert np.all(res.home_final != res.away_final)
    assert abs(res.p_reg_win(True)[0] + res.p_reg_win(False)[0] + res.p_reg_tie()[0] - 1) < 1e-12
    for q in (1, 2, 3):
        assert abs(res.p_period_win(q, True)[0] + res.p_period_win(q, False)[0] + res.p_period_tie(q)[0] - 1) < 1e-12


def test_same_seed_reproduces_and_flat_table_matches_poisson_mean():
    p = _params()
    a = simulate_game_v2(TeamParams(1, "H", 3.2), TeamParams(2, "A", 2.8), seed=11, n_sims=20000, params=p)
    b = simulate_game_v2(TeamParams(1, "H", 3.2), TeamParams(2, "A", 2.8), seed=11, n_sims=20000, params=p)
    assert np.array_equal(a.home_final, b.home_final)
    assert a.home_reg.mean() == pytest.approx(3.2, abs=0.05) and a.away_reg.mean() == pytest.approx(2.8, abs=0.05)


def test_empty_net_cells_move_late_goals_to_the_leader_and_widen_two_goal_margins():
    flat = _params()
    mult = np.ones((len(TIME_EDGES) - 1, len(DIFFS)))
    mult[-3:, DIFFS.index(1)] = 5.0  # leader by one, final three minutes (empty net)
    en = _params(mult=tuple(map(tuple, mult)))
    a = simulate_game_v2(TeamParams(1, "H", 3.0), TeamParams(2, "A", 3.0), seed=3, n_sims=40000, params=flat)
    b = simulate_game_v2(TeamParams(1, "H", 3.0), TeamParams(2, "A", 3.0), seed=3, n_sims=40000, params=en)
    assert np.mean(np.abs(b.margin) == 2) > np.mean(np.abs(a.margin) == 2) + 0.02
    assert np.mean(np.abs(b.margin) == 1) < np.mean(np.abs(a.margin) == 1)
    # an empty-netter never creates a tie, and a two-goal lead is harder to erase: fewer late equalisers
    assert b.p_reg_tie()[0] < a.p_reg_tie()[0]


def test_tied_state_slowdown_raises_regulation_ties():
    mult = np.ones((len(TIME_EDGES) - 1, len(DIFFS)))
    mult[2:, DIFFS.index(0)] = 0.75
    a = simulate_game_v2(TeamParams(1, "H", 3.0), TeamParams(2, "A", 3.0), seed=5, n_sims=40000, params=_params())
    b = simulate_game_v2(TeamParams(1, "H", 3.0), TeamParams(2, "A", 3.0), seed=5, n_sims=40000, params=_params(mult=tuple(map(tuple, mult))))
    assert b.p_reg_tie()[0] > a.p_reg_tie()[0] + 0.01


# ---------------------------------------------------------------------------------------------- hazards
def _synthetic_shots(n_games: int = 600, lam: float = 3.0, seed: int = 1) -> pd.DataFrame:
    """Goals from a state-FREE Poisson process: the estimator must return a flat table (and no spurious score effect)."""
    rng = np.random.default_rng(seed)
    rows = []
    for g in range(n_games):
        gid = 20001 + g
        for is_home in (1, 0):
            k = rng.poisson(lam)
            for t in np.sort(rng.uniform(0, 3600, k)):
                rows.append({"season": 2023, "game_id": gid, "nhl_game_id": 2023_000_000 + gid, "isPlayoffGame": 0, "goal": 1, "period": int(t // 1200) + 1,
                             "time": float(t), "isHomeTeam": is_home, "homeTeamCode": "AAA", "awayTeamCode": "BBB", "homeEmptyNet": 0, "awayEmptyNet": 0,
                             "shotOnEmptyNet": 0, "homeSkatersOnIce": 5, "awaySkatersOnIce": 5})
        rows.append({"season": 2023, "game_id": gid, "nhl_game_id": 2023_000_000 + gid, "isPlayoffGame": 0, "goal": 0, "period": 1, "time": 1.0, "isHomeTeam": 1,
                     "homeTeamCode": "AAA", "awayTeamCode": "BBB", "homeEmptyNet": 0, "awayEmptyNet": 0, "shotOnEmptyNet": 0, "homeSkatersOnIce": 5, "awaySkatersOnIce": 5})
    return pd.DataFrame(rows)


def test_hazard_fit_recovers_a_flat_table_from_state_free_goals():
    s = _synthetic_shots()
    hd = sh.build_hazard_data(s)
    assert hd.exposure.sum() == pytest.approx(600 * 2 * 60.0)
    lam = pd.DataFrame([{"game_id": int(g), "home": h, "lam": 3.0} for g in hd.team_games["game_id"].unique() for h in (0, 1)])
    m, info = sh.fit_multipliers(hd, lam, shrink=25)
    busy = np.asarray(info["expected_by_cell"]) > 150  # cells with real exposure
    assert np.all(np.abs(m[busy] - 1) < 0.2)
    assert info["goals"] == int((s["goal"] == 1).sum())


# ---------------------------------------------------------------------------------------------- special teams
def _lst() -> stm.LeagueST:
    return stm.LeagueST(ev_xg60=2.45, ev_conv=0.97, pp_xg60=7.3, pp_conv=0.98, sh_g60=0.87, ppmin=4.4, ev_min=49.4, other_goals=0.45, g60_all=2.97, n_team_games=2000)


def _avg(lst: stm.LeagueST, name="LG") -> stm.TeamST:
    return stm.TeamST(name, lst.ev_xg60, lst.ev_xg60, lst.pp_xg60, lst.pp_xg60, lst.ppmin, lst.ppmin, 20.0, {})


def test_league_average_special_teams_reproduce_v1_exactly_no_double_counting():
    lg = LeagueRates(2.9, 3.0, 500, "2025-01-01")
    r = TeamRating("X", 2.9, 2.9, 1.0, 1.0, 20.0)
    lst = _lst()
    v2 = stm.expected_goals_v2(r, r, _avg(lst), _avg(lst), lg, lst)
    v1 = expected_goals(r, r, lg)
    assert v2[0] == pytest.approx(v1[0]) and v2[1] == pytest.approx(v1[1])
    off = stm.expected_goals_v2(r, r, _avg(lst), _avg(lst), lg, lst, use_special_teams=False)
    assert off[0] == pytest.approx(v1[0])


def test_power_play_edge_and_penalty_taking_move_the_right_side():
    lg = LeagueRates(2.9, 3.0, 500, "2025-01-01")
    r = TeamRating("X", 2.9, 2.9, 1.0, 1.0, 20.0)
    lst = _lst()
    base = stm.expected_goals_v2(r, r, _avg(lst), _avg(lst), lg, lst)
    strong_pp = stm.TeamST("H", lst.ev_xg60, lst.ev_xg60, lst.pp_xg60 * 1.3, lst.pp_xg60, lst.ppmin, lst.ppmin, 20, {})
    undisciplined_away = stm.TeamST("A", lst.ev_xg60, lst.ev_xg60, lst.pp_xg60, lst.pp_xg60, lst.ppmin, lst.ppmin * 1.4, 20, {})
    a = stm.expected_goals_v2(r, r, strong_pp, _avg(lst), lg, lst)
    b = stm.expected_goals_v2(r, r, _avg(lst), undisciplined_away, lg, lst)
    assert a[0] > base[0] and a[1] == pytest.approx(base[1])
    assert b[0] > base[0]  # the home team gets more power-play time
    c = stm.st_components(_avg(lst), undisciplined_away, lst, 1.0, 1.0)
    assert c["ev_min"] < lst.ev_min  # penalty time comes out of even strength


def test_special_teams_regress_small_samples_and_respect_the_cutoff():
    rows = []
    for i in range(3):
        d = f"202410{10 + i:02d}"
        for sit, ice, xgf, xga in (("5on5", 3000, 2.0, 2.0), ("5on4", 240, 3.0, 0.1), ("4on5", 240, 0.05, 0.3), ("all", 3600, 5.2, 2.5)):
            rows.append({"team": "AAA", "gameId": 2024020000 + i, "gameDate": d, "season": 2024, "situation": sit, "iceTime": ice, "xGoalsFor": xgf,
                         "xGoalsAgainst": xga, "goalsFor": 1, "goalsAgainst": 1, "game_type": 2})
    s = stm.prepare_situation_log(pd.DataFrame(rows))
    lst = _lst()
    t = stm.team_st(s, "AAA", "20241013", lst, 2024)
    raw_pp = t.raw["pp_off"]
    assert raw_pp > 40  # 3 xG in 4 minutes is an absurd raw rate ...
    assert abs(t.pp_off - lst.pp_xg60) < 0.1 * abs(raw_pp - lst.pp_xg60)  # ... and is shrunk almost all the way back
    early = stm.team_st(s, "AAA", "20241011", lst, 2024)  # only the first game is visible
    assert early.games_used < t.games_used
    none = stm.team_st(s, "AAA", "20241010", lst, 2024)  # nothing strictly before the first game
    assert none.games_used == 0 and none.pp_off == lst.pp_xg60


# ---------------------------------------------------------------------------------------------- goalies
def _glog() -> pd.DataFrame:
    rows = []
    dates = pd.date_range("2024-10-01", periods=40, freq="2D").strftime("%Y-%m-%d").tolist()
    for i, d in enumerate(dates):
        rows.append({"game_id": 2024020000 + i, "goalie_id": 1, "season": 2024, "playoff": 0, "team": "AAA", "def_home": 1, "xga": 3.0, "ga": 1.0, "sog": 30,
                     "first_t": 1.0, "last_t": 3600.0, "name": "Good", "starter": 1, "game_date": d})
        rows.append({"game_id": 2024020000 + i, "goalie_id": 2, "season": 2024, "playoff": 0, "team": "BBB", "def_home": 0, "xga": 3.0, "ga": 5.0, "sog": 30,
                     "first_t": 1.0, "last_t": 3600.0, "name": "Bad", "starter": 1, "game_date": d})
    rows.append({"game_id": 2024029999, "goalie_id": 1, "season": 2024, "playoff": 0, "team": "AAA", "def_home": 1, "xga": 3.0, "ga": 12.0, "sog": 30,
                 "first_t": 1.0, "last_t": 3600.0, "name": "Good", "starter": 1, "game_date": "2025-03-01"})
    return pd.DataFrame(rows).sort_values(["game_date", "game_id"]).reset_index(drop=True)


def test_goalie_talent_is_point_in_time_and_strongly_regressed():
    book = gt.GoalieBook(_glog(), prior_xg=300)
    good = book.talent(1, "2024-12-01", league_ratio=1.0)
    bad = book.talent(2, "2024-12-01", league_ratio=1.0)
    assert good.factor < 1.0 < bad.factor
    assert 1 / 3 < good.factor and bad.factor < 5 / 3  # far from the raw 0.33 / 1.67: regressed
    # a disastrous game on 2025-03-01 is invisible to a prediction on 2025-03-01 and visible the day after
    before = book.talent(1, "2025-03-01", league_ratio=1.0)
    after = book.talent(1, "2025-03-02", league_ratio=1.0)
    assert before.factor < after.factor
    assert book.talent(1, "2024-10-01", league_ratio=1.0).apps_used == 0  # nothing strictly before the first game
    assert book.talent(999, "2025-01-01").factor == 1.0


def test_goalie_rest_and_back_to_back():
    book = gt.GoalieBook(_glog(), prior_xg=300, b2b_mult=1.05)
    t = book.talent(1, "2024-10-02", league_ratio=1.0)
    assert t.rest_days == 1 and t.b2b and t.workload_mult == 1.05
    t2 = book.talent(1, "2024-10-03", league_ratio=1.0)
    assert t2.rest_days == 2 and not t2.b2b and t2.workload_mult == 1.0


def test_v2_goalie_mixture_respects_status_ladder():
    from nhl_edge.workflows.shadow_v2 import v2_goalie_factor

    book = gt.GoalieBook(_glog(), prior_xg=300)

    def state(status, conf):
        return GoalieState(team_id=1, status=status, player_id=2 if status != GoalieStatus.UNKNOWN else None, player_name="Bad", confidence=conf,
                           observed_at_utc=None, source="test", alternatives=[{"player_id": 1}])

    conf = {s: c for s, c in ((GoalieStatus.CONFIRMED, 0.985), (GoalieStatus.PROBABLE, 0.85), (GoalieStatus.PROJECTED, 0.70))}
    f_conf = v2_goalie_factor(state(GoalieStatus.CONFIRMED, conf[GoalieStatus.CONFIRMED]), book, "2024-12-01", "BBB")[0]
    f_proj = v2_goalie_factor(state(GoalieStatus.PROJECTED, conf[GoalieStatus.PROJECTED]), book, "2024-12-01", "BBB")[0]
    f_unk, det = v2_goalie_factor(state(GoalieStatus.UNKNOWN, 0.0), book, "2024-12-01", "BBB")
    named = book.talent(2, "2024-12-01").factor
    alt = book.talent(1, "2024-12-01").factor
    assert f_conf == pytest.approx(0.985 * named + 0.015 * alt)
    assert f_proj == pytest.approx(0.70 * named + 0.30 * alt)  # PROJECTED is not treated as CONFIRMED
    assert f_unk == pytest.approx(alt) and det["weight_named"] == 0.0
    assert v2_goalie_factor(state(GoalieStatus.CONFIRMED, 0.985), None, "2024-12-01", "BBB")[0] == 1.0
