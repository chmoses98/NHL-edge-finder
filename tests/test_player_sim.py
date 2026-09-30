"""PLAYER_SIM_V1: official-event parsing, joint goal / assist / point simulation invariants, saves, ladders, identity
resolution, settlement semantics and point-in-time guarantees. No network."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from nhl_edge.data.lines import fold, is_confirmed_source, line_rows, parse_line_page, resolve_line_rows
from nhl_edge.data.player_events import check_game, derive_game, parse_situation, team_state
from nhl_edge.players.engine import ALL_STATES, StrengthTable, TeamRoster, invariant_violations, simulate_players
from nhl_edge.players.features import (
    LeaguePriors,
    PlayerBook,
    PlayerParams,
    build_player_games,
    coice_fractions,
    league_priors,
)
from nhl_edge.players.identity import parse_player_market, resolve_player
from nhl_edge.players.params import SavesModel
from nhl_edge.players.pricing import ladder_violations, price_player
from nhl_edge.players.saves import simulate_saves
from nhl_edge.schemas.market import Contract
from nhl_edge.settlement.engine import SettlementOutcome
from nhl_edge.settlement.player import settle_player_contract
from nhl_edge.sim.engine import TeamParams
from nhl_edge.sim.engine_v2 import DIFFS, TIME_EDGES, load_params, simulate_game_v2

SAMPLES = Path(__file__).resolve().parents[1] / "docs" / "probe" / "samples"
NOW = pd.Timestamp("2026-09-30T12:00:00Z").to_pydatetime()


# ------------------------------------------------------------------------------------------------ synthetic game
def _pl(per, t, typ, code, **d):
    return {"periodDescriptor": {"number": per, "periodType": "REG" if per < 4 else ("OT" if per == 4 else "SO")}, "timeInPeriod": t, "situationCode": code,
            "typeDescKey": typ, "details": d, "sortOrder": 0}


def synthetic_game():
    sk = lambda pid, num, nm, pos, g, a, sog, toi="10:00": {"playerId": pid, "sweaterNumber": num, "name": {"default": nm}, "position": pos, "goals": g,  # noqa: E731
                                                          "assists": a, "points": g + a, "sog": sog, "toi": toi, "powerPlayGoals": 0, "pim": 0, "shifts": 10}
    box = {"id": 2025020001, "gameDate": "2025-10-07", "homeTeam": {"id": 13, "score": 2}, "awayTeam": {"id": 16, "score": 2}, "gameOutcome": {"lastPeriodType": "SO"},
           "playerByGameStats": {
               "homeTeam": {"forwards": [sk(1, 9, "A. One", "C", 1, 1, 3), sk(2, 10, "B. Two", "L", 1, 1, 1)], "defense": [sk(3, 2, "C. Three", "D", 0, 1, 0)],
                            "goalies": [{"playerId": 30, "sweaterNumber": 35, "name": {"default": "G. Home"}, "saveShotsAgainst": "20/22", "saves": 20, "shotsAgainst": 22,
                                         "goalsAgainst": 2, "starter": True, "toi": "65:00"}]},
               "awayTeam": {"forwards": [sk(4, 11, "D. Four", "C", 1, 0, 2), sk(5, 12, "E. Five", "R", 1, 0, 2), sk(6, 13, "F. Scratchless", "L", 0, 0, 0, "00:00")],
                            "defense": [],
                            "goalies": [{"playerId": 31, "sweaterNumber": 31, "name": {"default": "G. Away"}, "saveShotsAgainst": "18/20", "saves": 18, "shotsAgainst": 20,
                                         "goalsAgainst": 2, "starter": True, "toi": "65:00"},
                                        {"playerId": 32, "sweaterNumber": 1, "name": {"default": "B. Backup"}, "saves": 0, "shotsAgainst": 0, "goalsAgainst": 0,
                                         "starter": False, "toi": "00:00"}]}}}
    plays = [_pl(1, "00:00", "period-start", "1551"), _pl(1, "05:00", "faceoff", "1451"),
             _pl(1, "06:00", "goal", "1451", eventOwnerTeamId=13, scoringPlayerId=1, assist1PlayerId=2, assist2PlayerId=3, goalieInNetId=31),
             _pl(1, "06:00", "faceoff", "1551"), _pl(2, "00:00", "period-start", "1551"),
             _pl(2, "03:00", "shot-on-goal", "1551", eventOwnerTeamId=16, shootingPlayerId=4, xCoord=70, yCoord=5),
             _pl(2, "03:02", "goal", "1551", eventOwnerTeamId=16, scoringPlayerId=4, goalieInNetId=30),
             _pl(3, "00:00", "period-start", "1551"), _pl(3, "10:00", "goal", "1551", eventOwnerTeamId=16, scoringPlayerId=5, goalieInNetId=30),
             _pl(3, "19:00", "faceoff", "0651"), _pl(3, "19:30", "goal", "0651", eventOwnerTeamId=13, scoringPlayerId=2, assist1PlayerId=1),
             _pl(5, "00:00", "goal", "1010", eventOwnerTeamId=13, scoringPlayerId=1)]  # shootout: never a player goal
    pbp = {"id": 2025020001, "homeTeam": {"id": 13}, "awayTeam": {"id": 16}, "plays": plays}
    sh = lambda pid, tid, per, s, e: {"playerId": pid, "teamId": tid, "period": per, "startTime": s, "endTime": e, "typeCode": 517}  # noqa: E731
    shifts = {"data": [sh(1, 13, 1, "04:00", "07:00"), sh(2, 13, 1, "04:00", "07:00"), sh(3, 13, 1, "04:30", "06:00"), sh(4, 16, 1, "05:30", "06:30"),
                       sh(4, 16, 2, "02:00", "04:00"), sh(3, 13, 2, "02:30", "03:30"), sh(5, 16, 3, "09:00", "10:30"), sh(1, 13, 3, "18:00", "20:00"),
                       sh(2, 13, 3, "18:00", "20:00"), sh(4, 16, 3, "18:30", "20:00")]}
    return box, pbp, shifts


def test_situation_code_strength_states():
    assert team_state(parse_situation("1451"), home=True) == "PP" and team_state(parse_situation("1451"), home=False) == "SH"
    assert team_state(parse_situation("0651"), home=True) == "EN"  # away net empty: a home goal is into the empty net
    assert team_state(parse_situation("0651"), home=False) == "EA"  # away extra attacker
    assert team_state(parse_situation("1551"), home=True) == "EV" and team_state(parse_situation("1441"), home=False) == "EV"
    assert parse_situation("15") is None and team_state(None, True) is None


def test_derive_game_reconciles_with_the_official_boxscore_and_drops_the_shootout():
    box, pbp, shifts = synthetic_game()
    t = derive_game(box, pbp, shifts, {"season": 2025})
    assert check_game(t, box) == []  # A1 + A2 == official assists, pbp goals == official goals, shootout goal excluded
    g = t["goals"]
    assert len(g) == 4 and set(g["strength"]) == {"PP", "EV", "EN"}
    assert g.iloc[0]["for_on_ice"] == [1, 2, 3] and g.iloc[0]["against_on_ice"] == [4]
    p = t["players"].set_index("player_id")
    assert p.loc[1, "a1"] == 1 and p.loc[2, "a1"] == 1 and p.loc[3, "a2"] == 1
    assert p.loc[1, "toi_pp_s"] == 60 and p.loc[1, "gf_pp"] == 1 and p.loc[4, "ga_sh"] == 1
    assert p.loc[2, "toi_en_s"] > 0 and p.loc[4, "toi_ea_s"] > 0
    assert t["players"]["shifts_ok"].all()
    c = t["coice"].set_index(["p1", "p2"])
    assert c.loc[(1, 2), "shared_pp_s"] == 60 and c.loc[(1, 2), "shared_s"] >= c.loc[(1, 3), "shared_s"]


def test_derive_game_without_shifts_keeps_official_lines():
    box, pbp, _ = synthetic_game()
    t = derive_game(box, pbp, {"data": []}, {})
    assert not t["players"]["shifts_ok"].any() and t["players"]["toi_ev_s"].isna().all()
    assert t["players"]["goals"].sum() == 4 and t["goals"]["for_on_ice"].isna().all()


@pytest.mark.skipif(not (SAMPLES / "player_game" / "nhl_boxscore_2025020001.json").exists(), reason="real payload fixture not present")
def test_real_official_payloads_parse_consistently():
    d = SAMPLES / "player_game"
    box = json.loads((d / "nhl_boxscore_2025020001.json").read_text())
    pbp = json.loads((d / "nhl_pbp_2025020001.json").read_text())
    shifts = json.loads((d / "nhl_shiftcharts_2025020001.json").read_text())
    t = derive_game(box, pbp, shifts, {"season": 2025})
    assert check_game(t, box) == []
    assert t["players"]["shifts_ok"].all() and len(t["coice"]) > 50
    ts = t["team_states"]
    assert (ts["sec_unknown"] == 0).all() and (ts[["sec_ev", "sec_pp", "sec_sh", "sec_ea", "sec_en"]].sum(axis=1) == ts["n_seconds"]).all()


# ------------------------------------------------------------------------------------------------ joint simulation
def _roster(team_id: int, n: int = 18, seed: int = 0) -> TeamRoster:
    rng = np.random.default_rng(seed)
    w = rng.gamma(2.0, 1.0, (len(ALL_STATES), n))
    F = rng.uniform(0, 0.6, (3, n, n))
    for k in range(3):
        np.fill_diagonal(F[k], 0.0)
    return TeamRoster(team_id, f"T{team_id}", np.arange(team_id * 100, team_id * 100 + n), [f"p{i}" for i in range(n)], ["F"] * 12 + ["D"] * (n - 12), w,
                      rng.uniform(0.1, 0.4, (len(ALL_STATES), n)), rng.uniform(0.05, 0.3, (len(ALL_STATES), n)), F, np.full(n, 0.15), np.full(n, 0.01), 0.21, 0.03,
                      np.array([0.06, 0.012, 0.2, 0.017, 0.19, 0.05]), np.array([0.2, 0.05, 0.56, 0.08, 0.43, 0.28]))


def _strength() -> StrengthTable:
    nb, nd = len(TIME_EDGES) - 1, len(DIFFS)
    p_en = np.zeros((nb, nd))
    p_ea = np.zeros((nb, nd))
    p_en[-3:, 4:6] = 0.8
    p_ea[-3:, 1:3] = 0.3
    return StrengthTable(TIME_EDGES, DIFFS, p_en, p_ea)


def _sim(lh=3.2, la=2.8, seed=7, n=3000):
    res = simulate_game_v2(TeamParams(1, "H", lh), TeamParams(2, "A", la), seed=seed, n_sims=n, params=load_params(), record_steps=True)
    ps = simulate_players(res, _roster(1, seed=seed), _roster(2, seed=seed + 1), _strength(), seed + 99)
    return res, ps


def test_recording_steps_changes_no_v2_outcome():
    a = simulate_game_v2(TeamParams(1, "H", 3.1), TeamParams(2, "A", 2.9), seed=11, n_sims=4000, params=load_params())
    b = simulate_game_v2(TeamParams(1, "H", 3.1), TeamParams(2, "A", 2.9), seed=11, n_sims=4000, params=load_params(), record_steps=True)
    for k in ("home_reg", "away_reg", "home_final", "away_final", "overtime", "shootout", "home_periods", "away_periods"):
        assert np.array_equal(getattr(a, k), getattr(b, k)), k
    assert np.array_equal(b.home_steps.sum(axis=1), b.home_reg) and np.array_equal(b.away_steps.sum(axis=1), b.away_reg)
    assert a.home_steps is None


@settings(max_examples=12, deadline=None, suppress_health_check=[HealthCheck.too_slow])
@given(lh=st.floats(1.5, 4.5), la=st.floats(1.5, 4.5), seed=st.integers(0, 10_000))
def test_player_goals_reconcile_exactly_with_team_goals(lh, la, seed):
    res, ps = _sim(lh, la, seed, 1500)
    assert invariant_violations(res, ps) == []
    assert ladder_violations(ps) == []
    for d in (ps.home, ps.away):
        assert (d.points == d.goals + d.a1 + d.a2).all()
        assert (d.a2.sum(axis=1) <= d.a1.sum(axis=1)).all() and (d.a1.sum(axis=1) <= d.goals.sum(axis=1)).all()


def test_shootout_creates_no_player_goal_and_first_goal_is_from_event_order():
    res, ps = _sim(n=6000)
    so_home_win = res.shootout & (res.home_final > res.away_final)
    assert np.array_equal(ps.home.goals.sum(axis=1)[so_home_win], res.home_reg[so_home_win])
    no_goal = (res.home_reg + res.away_reg == 0) & ~(res.overtime & ~res.shootout)
    assert (ps.first_scorer[no_goal] == 0).all()
    scored = res.home_final + res.away_final - res.shootout.astype(int) > 0
    assert (ps.first_scorer[scored] != 0).all()
    # the first scorer is always on the first-scoring team
    home_ids = set(ps.home_roster.player_ids.tolist())
    assert all((s in home_ids) == (t == 1) for s, t in zip(ps.first_scorer[scored][:500], ps.first_team[scored][:500]))


def test_no_player_is_credited_twice_on_one_goal():
    # a 3-skater roster forces the constraint: scorer, A1 and A2 must be three different players
    r = _roster(1, n=3, seed=3)
    res = simulate_game_v2(TeamParams(1, "H", 4.0), TeamParams(2, "A", 2.0), seed=5, n_sims=3000, params=load_params(), record_steps=True)
    ps = simulate_players(res, r, _roster(2, seed=4), _strength(), 6)
    d = ps.home
    per_player_max = np.maximum(d.goals, 0)
    assert ((d.goals + d.a1 + d.a2) <= d.goals.sum(axis=1, keepdims=True) + d.a1.sum(axis=1, keepdims=True)).all()
    one_goal = d.goals.sum(axis=1) == 1
    assert ((d.goals + d.a1 + d.a2)[one_goal] <= 1).all()  # on a single-goal game nobody holds two roles
    assert per_player_max.shape == (3000, 3)


def test_simulation_is_reproducible_with_a_fixed_seed():
    _, a = _sim(seed=21)
    _, b = _sim(seed=21)
    assert np.array_equal(a.home.points, b.home.points) and np.array_equal(a.first_scorer, b.first_scorer)


def test_saves_never_exceed_shots_and_goals_plus_saves_equal_shots():
    res, ps = _sim(n=4000)
    sm = SavesModel(np.array([0.0, 1.0, 0.014, -0.004, 0.033]), 0.017, {1: 0.005, 2: 0.01, 3: 0.034, 4: 0.095, 5: 0.16, 6: 0.26, 7: 0.2}, 100, 0.906)
    sd = simulate_saves(res, ps, True, sm, 29.0, 3)
    assert (sd.saves <= sd.shots_faced).all() and (sd.saves + sd.goals_against == sd.shots_faced).all()
    assert (sd.goals_against <= ps.ga_home).all()
    ladder = [np.mean(sd.saves >= k) for k in range(15, 40)]
    assert all(x >= y for x, y in zip(ladder, ladder[1:]))
    assert 22 < sd.saves.mean() < 29


def test_empty_net_goals_never_count_against_the_goalie():
    res, ps = _sim(n=4000)
    # GA against the home goalie can never exceed the away team's non-shootout goals
    away_nonso = res.away_final - ((res.away_final > res.home_final) & res.shootout)
    assert (ps.ga_home <= away_nonso).all()
    assert (ps.ga_home < away_nonso).any()  # some away goals were into an empty net (late leads in the strength table)


def test_price_player_ladders_and_fail_closed():
    res, ps = _sim(n=4000)
    pid = int(ps.home_roster.player_ids[0])
    p1 = price_player("player_points", "gt", 0.5, pid, ps).p
    p2 = price_player("player_points", "gt", 1.5, pid, ps).p
    g1 = price_player("player_goals", "gt", 0.5, pid, ps).p
    a1 = price_player("player_assists", "gt", 0.5, pid, ps).p
    assert p1 >= p2 and p1 >= g1 and p1 >= a1 and p1 <= g1 + a1 + 1e-12
    assert not price_player("player_points", "gt", 0.5, None, ps).supported
    assert not price_player("player_points", "gt", 0.5, 999999, ps).supported
    assert not price_player("player_points", "between", 0.5, pid, ps).supported
    assert not price_player("game_winner", "gt", 0.5, pid, ps).supported
    fg = sum(price_player("first_goal", None, None, int(p), ps).p for p in list(ps.home_roster.player_ids) + list(ps.away_roster.player_ids))
    assert fg == pytest.approx(float((ps.first_scorer != 0).mean()), abs=1e-9)


# ------------------------------------------------------------------------------------------------ Kalshi identity
ROSTER = [
    {"player_id": 8480000, "team_id": 13, "sweater": 8, "first_name": "Brady", "last_name": "Tkachuk", "position": "L"},
    {"player_id": 8479314, "team_id": 13, "sweater": 19, "first_name": "Matthew", "last_name": "Tkachuk", "position": "L"},
    {"player_id": 8478000, "team_id": 8, "sweater": 20, "first_name": "Juraj", "last_name": "Slafkovsky", "position": "L"},
    {"player_id": 8477000, "team_id": 16, "sweater": 30, "first_name": "Spencer", "last_name": "Knight", "position": "G"},
    {"player_id": 8471000, "team_id": 16, "sweater": 12, "first_name": "Sam", "last_name": "Smith", "position": "C"},
    {"player_id": 8471001, "team_id": 16, "sweater": 14, "first_name": "Sean", "last_name": "Smith", "position": "C"},
]


def test_player_ticker_resolution_real_shapes():
    ref = parse_player_market("KXNHLPTS-26SEP29FLACAR-FLABTKACHUK7-1", "Brady Tkachuk: 1+ points")
    assert ref.team_code == "FLA" and ref.jersey == 7 and ref.initial == "B"
    assert resolve_player(ref, ROSTER) == (8480000, "team+name (jersey differs)")  # Kalshi jersey stale: the name + initial decide
    ref = parse_player_market("KXNHLGOAL-26SEP29MTLTOR-MTLJSLAFKOVSK20-1", "Juraj Slafkovsky: 1+ goals")
    assert resolve_player(ref, ROSTER)[0] == 8478000  # truncated last name
    ref = parse_player_market("KXNHLSAVE-26SEP29CHIVGK-CHISKNIGHT30-26", "Spencer Knight: 26+ saves")
    assert ref.threshold_suffix == 26 and resolve_player(ref, ROSTER)[0] == 8477000
    ref = parse_player_market("KXNHLFIRSTGOAL-26SEP29CHIVGK-CHISSMITH99", "S Smith: First Goalscorer")
    assert resolve_player(ref, ROSTER) == (None, "ambiguous name on team")  # two S. Smiths, wrong jersey -> refuse
    assert parse_player_market("KXNHLPTS-26SEP29CHIVGK-XXXJDOE9-1") is None  # team code not in the event -> no parse


# ------------------------------------------------------------------------------------------------ settlement
def _contract(ticker, family, thr, title):
    return Contract(ticker=ticker, family=family, scope="player", stat=family, period="FULL", settles_on="FINAL_INCL_OT", game_id="2025020001",
                    threshold=thr, comparator="gt" if thr is not None else None, support="RESEARCH", semantics_confidence="medium", title=title)


def test_player_settlement_semantics():
    box, pbp, shifts = synthetic_game()
    t = derive_game(box, pbp, shifts, {"season": 2025})
    sk, gl, goals = t["players"], t["goalies"], t["goals"]
    c = _contract("KXNHLPTS-25OCT07CHIFLA-FLAAONE9-2", "player_points", 1.5, "A. One: 2+ points")
    r = settle_player_contract(c, sk, gl, goals, True, "yes", NOW, "test")
    assert r.outcome == SettlementOutcome.YES and r.value == 2.0 and "DISAGREES" not in r.reason
    r = settle_player_contract(_contract("KXNHLGOAL-25OCT07CHIFLA-FLAAONE9-2", "player_goals", 1.5, "A. One: 2+ goals"), sk, gl, goals, True, "yes", NOW, "test")
    assert r.outcome == SettlementOutcome.NO and r.reason.startswith("DISAGREES_WITH_KALSHI")  # the shootout goal is not a goal
    r = settle_player_contract(_contract("KXNHLFIRSTGOAL-25OCT07CHIFLA-FLAAONE9", "first_goal", None, "A. One: First Goalscorer"), sk, gl, goals, True, None, NOW, "t")
    assert r.outcome == SettlementOutcome.YES
    r = settle_player_contract(_contract("KXNHLPTS-25OCT07CHIFLA-CHIFSCRATCHLESS13-1", "player_points", 0.5, "F. Scratchless: 1+ points"), sk, gl, goals, True, None, NOW, "t")
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "never entered" in r.reason
    r = settle_player_contract(_contract("KXNHLPTS-25OCT07CHIFLA-CHIZNOBODY77-1", "player_points", 0.5, "Z. Nobody: 1+ points"), sk, gl, goals, True, None, NOW, "t")
    assert r.outcome == SettlementOutcome.UNSETTLEABLE
    r = settle_player_contract(_contract("KXNHLSAVE-25OCT07CHIFLA-FLAGHOME35-20", "goalie_saves", 19.5, "G. Home: 20+ saves"), sk, gl, goals, True, None, NOW, "t")
    assert r.outcome == SettlementOutcome.YES and r.value == 20
    r = settle_player_contract(_contract("KXNHLSAVE-25OCT07CHIFLA-CHIBBACKUP1-20", "goalie_saves", 19.5, "B. Backup: 20+ saves"), sk, gl, goals, True, None, NOW, "t")
    assert r.outcome == SettlementOutcome.UNSETTLEABLE
    assert settle_player_contract(c, sk, gl, goals, False, None, NOW, "t").outcome == SettlementOutcome.UNSETTLEABLE


# ------------------------------------------------------------------------------------------------ point in time
def _pg_rows():
    box, pbp, shifts = synthetic_game()
    rows = []
    for k, day in enumerate(("2025-10-07", "2025-10-09", "2025-10-11")):
        b = json.loads(json.dumps(box))
        b["id"] = 2025020001 + k
        p = json.loads(json.dumps(pbp))
        p["id"] = b["id"]
        t = derive_game(b, p, shifts, {"season": 2025, "game_date": day, "game_type": 2})
        rows.append(t)
    cat = {k: pd.concat([r[k] for r in rows], ignore_index=True) for k in rows[0]}
    return cat


def test_profiles_and_coice_use_only_games_strictly_before_the_date():
    t = _pg_rows()
    pg = build_player_games(t["players"], t["goals"], t["shots"], t["team_states"], pd.Series(0.1, index=t["shots"].index))
    pri = league_priors(pg, t["goals"])
    book = PlayerBook(pg, pri, PlayerParams())
    before = book.profile(1, 20251009)
    # poison the future: a monster game on 2025-10-09 must not change what was known before it
    pg2 = pg.copy()
    pg2.loc[pg2["date_int"] >= 20251009, ["g_ev", "ixg_ev", "a1_ev", "toi_ev"]] = 99.0
    after = PlayerBook(pg2, pri, PlayerParams()).profile(1, 20251009)
    assert before.ixg60 == after.ixg60 and before.share == after.share and before.a1 == after.a1 and before.n_games == 1
    assert book.profile(1, 20251007).n_games == 0 and "NO_HISTORY" in book.profile(1, 20251007).flags
    t["coice"]["date_int"] = t["coice"]["game_date"].str.replace("-", "").astype(int)
    toi = pg[["game_id", "player_id", "toi_ev", "toi_pp", "toi_sh"]]
    F = coice_fractions(t["coice"], 13, 20251009, [1, 2, 3], toi)
    c2 = t["coice"].copy()
    c2.loc[c2["date_int"] >= 20251009, "shared_ev_s"] = 99999
    F2 = coice_fractions(c2, 13, 20251009, [1, 2, 3], toi)
    assert np.allclose(np.nan_to_num(F["ev"]), np.nan_to_num(F2["ev"]))
    assert coice_fractions(t["coice"], 13, 20251007, [1, 2, 3], toi) is None


def test_league_priors_round_trip():
    t = _pg_rows()
    pg = build_player_games(t["players"], t["goals"], t["shots"], t["team_states"], pd.Series(0.1, index=t["shots"].index))
    pri = league_priors(pg, t["goals"])
    assert LeaguePriors.from_dict(json.loads(json.dumps(pri.to_dict()))).to_dict() == pri.to_dict()


# ------------------------------------------------------------------------------------------------ lines
@pytest.mark.skipif(not (SAMPLES / "player_sources" / "dfo_lines_edmonton-oilers.html").exists(), reason="DailyFaceoff fixture not present")
def test_dailyfaceoff_line_page_parses_and_resolves_by_jersey_and_name():
    html = (SAMPLES / "player_sources" / "dfo_lines_edmonton-oilers.html").read_bytes()
    combo = parse_line_page(html)
    assert combo is not None and combo["teamAbbreviation"] == "EDM"
    rows = line_rows(combo, "EDM", "2026-09-30T05:28:56Z")
    units = {r["unit"] for r in rows}
    assert {"f1", "f2", "f3", "f4", "d1", "d2", "d3", "pp1", "pp2", "pk1"} <= units
    roster = [{"player_id": 8478402, "team_abbrev": "EDM", "sweater": 97, "last_name": "McDavid"}, {"player_id": 8477934, "team_abbrev": "EDM", "sweater": 29, "last_name": "Draisaitl"}]
    rr = resolve_line_rows(rows, roster)
    mcd = [r for r in rr if r["name"] == "Connor McDavid"]
    assert mcd and all(r["player_id"] == 8478402 for r in mcd) and {r["unit"] for r in mcd} >= {"f1", "pp1"}
    assert is_confirmed_source(combo["sourceName"]) and not is_confirmed_source("Projected lines")
    assert fold("Stützle") == "stutzle"


# ------------------------------------------------------------------------------------------------ period + settle job
def test_period_settlement_semantics():
    from nhl_edge.settlement.period import settle_period_contract

    box, pbp, shifts = synthetic_game()
    goals = derive_game(box, pbp, shifts, {})["goals"]  # P1: home 1-0 (PP); P2: away 0-1; P3: away 1, home 1 (EN); OT none; SO dropped
    mk = lambda tk, fam, per, team, thr: Contract(ticker=tk, family=fam, scope="game", stat="x", period=per, settles_on="PERIOD", game_id="2025020001",  # noqa: E731
                                                  team_id=team, threshold=thr, comparator="gt" if thr is not None else None, support="RESEARCH", semantics_confidence="high")
    s = lambda c, **k: settle_period_contract(c, goals, 13, 16, k.get("final", True), k.get("ok", True), k.get("kres"), NOW)  # noqa: E731
    assert s(mk("KXNHL1P-X-FLA", "period_winner", "P1", 13, 0.0)).outcome == SettlementOutcome.YES
    assert s(mk("KXNHL2P-X-FLA", "period_winner", "P2", 13, 0.0)).outcome == SettlementOutcome.NO
    assert s(mk("KXNHL3P-X-TIE", "period_winner", "P3", None, None)).outcome == SettlementOutcome.YES  # 1-1 in the third (EN goal counts)
    assert s(mk("KXNHL1PTOTAL-X-1", "period_total", "P1", None, 0.5)).outcome == SettlementOutcome.YES
    assert s(mk("KXNHL3PTOTAL-X-2", "period_total", "P3", None, 1.5)).outcome == SettlementOutcome.YES
    assert s(mk("KXNHL2PSPREAD-X-CHI2", "period_spread", "P2", 16, 1.5)).outcome == SettlementOutcome.NO
    r = s(mk("KXNHL1P-X-FLA", "period_winner", "P1", 13, 0.0), kres="no")
    assert r.reason.startswith("DISAGREES_WITH_KALSHI")
    assert s(mk("KXNHL1P-X-FLA", "period_winner", "P1", 13, 0.0), ok=False).outcome == SettlementOutcome.UNSETTLEABLE
    assert s(mk("KXNHL1P-X-FLA", "period_winner", "P1", 13, 0.0), final=False).outcome == SettlementOutcome.UNSETTLEABLE
    assert s(mk("KXNHL1P-X-XXX", "period_winner", "P1", 99, 0.0)).outcome == SettlementOutcome.UNSETTLEABLE


def test_settle_job_ingests_player_events_once_and_settles_player_and_period_contracts(tmp_path):
    from datetime import timedelta

    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.schemas.core import FinalPeriodType, FinalResult, GameStatus
    from nhl_edge.workflows.settle import run_settle

    box, pbp, shifts = synthetic_game()
    led = Ledger(tmp_path, run_id="t")
    start = NOW - timedelta(hours=6)
    led.append_rows("context/schedule", [{"game_id": "2025020001", "game_date_et": "2025-10-07", "start_time_utc": start.isoformat().replace("+00:00", "Z"),
                                          "status": "final", "home_team_id": 13, "away_team_id": 16}], observed_at=start - timedelta(hours=1))
    cs = [_contract("KXNHLPTS-25OCT07CHIFLA-FLAAONE9-2", "player_points", 1.5, "A. One: 2+ points"),
          Contract(ticker="KXNHL1P-25OCT07CHIFLA-FLA", family="period_winner", scope="game", stat="winner", period="P1", settles_on="PERIOD", game_id="2025020001",
                   team_id=13, threshold=0.0, comparator="gt", support="RESEARCH", semantics_confidence="high")]
    led.append_rows("contracts", [c.model_dump(mode="json") for c in cs], observed_at=start - timedelta(minutes=30))
    calls = []

    def fetch_result(gid):
        return FinalResult(game_id=gid, status=GameStatus.FINAL, home_team_id=13, away_team_id=16, home_final=3, away_final=2, home_reg=2, away_reg=2,
                           last_period_type=FinalPeriodType.SO), []

    def fetch_events(gid, meta):
        calls.append(gid)
        return derive_game(box, pbp, shifts, meta), []

    run_settle(tmp_path, tmp_path, fetch_result=fetch_result, now=NOW, fetch_player_events=fetch_events)
    recs = {r["ticker"]: r for r in Ledger(tmp_path).iter_rows("settlements")}
    assert recs["KXNHLPTS-25OCT07CHIFLA-FLAAONE9-2"]["outcome"] == "YES" and recs["KXNHLPTS-25OCT07CHIFLA-FLAAONE9-2"]["engine_version"] == "nhl-player-settle-1.0"
    assert recs["KXNHL1P-25OCT07CHIFLA-FLA"]["outcome"] == "YES" and recs["KXNHL1P-25OCT07CHIFLA-FLA"]["engine_version"] == "nhl-period-settle-1.0"
    assert {r["game_id"] for r in Ledger(tmp_path).iter_rows("player_events/players")} == {2025020001}
    # a second run: nothing new, and no network (the game is ingested and every contract already has a record)
    run_settle(tmp_path, tmp_path, fetch_result=fetch_result, now=NOW + timedelta(minutes=30), fetch_player_events=fetch_events)
    assert calls == ["2025020001"]
    assert len(list(Ledger(tmp_path).iter_rows("player_events/players"))) == len(derive_game(box, pbp, shifts, {})["players"])


def test_goal_copresence_counts_teammates_on_ice_at_goals_point_in_time():
    from nhl_edge.players.features import goal_copresence

    t = _pg_rows()
    g = t["goals"].copy()
    g["date_int"] = g["game_date"].str.replace("-", "").astype(int)
    G = goal_copresence(g, 13, 20251011, [1, 2, 3])
    Gev, nev = G["pp"]
    assert nev[0] > 0 and Gev[0, 1] == pytest.approx(1.0) and Gev[0, 2] == pytest.approx(1.0)  # the PP goal: 1, 2, 3 all on
    assert np.isnan(G["ev"][0]).all() or G["ev"][1].sum() == 0  # home EV goals: none in regulation (the 3rd-period goal is EN)
    g2 = g.copy()
    g2.loc[g2["date_int"] >= 20251011, "for_on_ice"] = pd.Series([[1, 2, 3, 4, 5]] * int((g2["date_int"] >= 20251011).sum()),
                                                                   index=g2.index[g2["date_int"] >= 20251011])
    G2 = goal_copresence(g2, 13, 20251011, [1, 2, 3])
    assert np.allclose(np.nan_to_num(G["pp"][0]), np.nan_to_num(G2["pp"][0]))  # later games cannot change it
    assert goal_copresence(g, 13, 20251007, [1, 2, 3]) == {}


def test_market_benchmark_scores_only_two_sided_quotes():
    """An empty book (0.01 / 0.99) has a 0.50 'midpoint' that is not a price: it must not enter the market score."""
    import numpy as np

    from nhl_edge.research.player_market_benchmark import MAX_SPREAD, benchmark

    rng = np.random.default_rng(0)
    n = 400
    p = rng.uniform(0.1, 0.6, n)
    y = (rng.uniform(size=n) < p).astype(int)
    mid = np.clip(p + rng.normal(0, 0.05, n), 0.02, 0.98)
    tight = pd.DataFrame({"stat": "points", "y": y, "p_model": p, "mid_T-10m": mid, "spread_T-10m": 0.04})
    empty = pd.DataFrame({"stat": "points", "y": y, "p_model": p, "mid_T-10m": 0.5, "spread_T-10m": 0.98})
    r = benchmark(pd.concat([tight, empty], ignore_index=True))["T-10m"]
    assert r["n"] == n and r["n_quoted_any_spread"] == 2 * n and r["max_spread"] == MAX_SPREAD
    assert abs(r["KALSHI_MID"]["mean_pred"] - mid.mean()) < 1e-9
    assert r["by_spread"]["(0.20,1.00]"]["n"] == n
