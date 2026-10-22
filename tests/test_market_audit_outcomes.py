"""Regression tests for the independent market-audit taxonomy + outcome resolver (RESEARCH_ONLY)."""

from __future__ import annotations

import pytest

from nhl_edge.identity.teams import registry
from nhl_edge.market_audit.outcomes import (
    NO,
    NOT_IN_BOX,
    SILENT,
    VOID,
    YES,
    GameFacts,
    names_match,
    resolve,
)
from nhl_edge.market_audit.taxonomy import KALSHI_NAME_ALIASES, PROVEN, UNRESOLVED, build_spec

HOME, AWAY = 3, 14  # NYR hosts TBL


def facts(hf, af, hr, ar, lpt, goals=None, skaters=None, goalies=None) -> GameFacts:
    return GameFacts("g1", HOME, AWAY, True, hf, af, hr, ar, lpt, goals or [], skaters or [], goalies or [])


def row(series, ticker, title, sub, strike_type="greater", floor=None, rules="", rules2="", cs=None):
    return {"ticker": ticker, "event_ticker": ticker.rsplit("-", 1)[0], "series_ticker": series, "title": title, "yes_sub_title": sub,
            "strike_type": strike_type, "floor_strike": floor, "custom_strike": cs, "rules_primary": rules, "rules_secondary": rules2}


GAME = "the New York R vs Tampa Bay NHL game originally scheduled for Oct 1, 2026"
SO_TXT = "If the game is decided by a shootout, the shootout result will be recorded as one goal awarded to the winning team."


def total_spec(floor=5.5):
    return build_spec(row("KXNHLTOTAL", "KXNHLTOTAL-26OCT01TBNYR-6", "Full Game: Over 5.5 goals scored", "Over 5.5 goals scored", floor=floor,
                          rules=f"If the teams collectively score more than {floor} goals in {GAME}, then the market resolves to Yes.", rules2=SO_TXT))


def test_every_kalshi_alias_resolves_to_the_registry_club():
    reg = registry()
    assert {reg.by_abbrev(c).abbrev for c in KALSHI_NAME_ALIASES.values()} == {"NYI", "NYR", "UTA"}


def test_total_counts_shootout_as_one_goal():
    # 3-3 after OT, NYR wins the shootout: official final 4-3 => total 7 => Over 5.5 YES, Over 6.5 YES, Over 7.5 NO
    f = facts(4, 3, 3, 3, "SO")
    assert resolve(total_spec(5.5), f).outcome == YES
    assert resolve(total_spec(6.5), f).outcome == YES
    assert resolve(total_spec(7.5), f).outcome == NO
    assert resolve(total_spec(6.5), f).value == 7.0


def test_unproven_spec_never_settles():
    bad = build_spec(row("KXNHLTOTAL", "KXNHLTOTAL-26OCT01TBNYR-6", "t", "Over 5.5", floor=5.5,
                         rules=f"If the teams collectively score more than 6.5 goals in {GAME}, then yes.", rules2=SO_TXT))
    assert bad.semantics_status == UNRESOLVED and "6.5" in bad.issues[0]
    assert resolve(bad, facts(4, 3, 3, 3, "SO")).outcome == "UNRESOLVED_SPEC"


def test_spread_shootout_margin_is_one_goal():
    spec = build_spec(row("KXNHLSPREAD", "KXNHLSPREAD-26OCT01TBNYR-NYR2", "New York R wins by over 1.5 goals", "New York R wins by over 1.5 goals",
                          floor=1.5, rules=f"If New York R wins by over 1.5 goals in {GAME}, then the market resolves to Yes."))
    assert spec.semantics_status == PROVEN and spec.subject_team_id == HOME
    assert resolve(spec, facts(4, 3, 3, 3, "SO")).outcome == NO  # SO win = one-goal margin
    assert resolve(spec, facts(5, 1, 5, 1, "REG")).outcome == YES


def test_overtime_market_and_tie_leg_semantics():
    ot = build_spec(row("KXNHLOT", "KXNHLOT-26OCT01TBNYR-1", "Game goes to overtime", "Game goes to overtime", floor=0.5,
                        rules=f"If at least 1 overtime period is played in {GAME}, then the market resolves to Yes.",
                        rules2='an overtime period is "played" if and only if the opening faceoff is taken'))
    assert resolve(ot, facts(4, 3, 3, 3, "OT")).outcome == YES
    assert resolve(ot, facts(5, 1, 5, 1, "REG")).outcome == NO


def goals(*items):
    return [{"period": p, "t_s": t, "team_id": tid, "scorer_id": sid} for p, t, tid, sid in items]


def test_period_three_excludes_overtime_and_shootout():
    p3 = build_spec(row("KXNHL3PTOTAL", "KXNHL3PTOTAL-26OCT01TBNYR-1", "3rd Period: Over 0.5 goals scored", "Over 0.5 goals", floor=0.5,
                        rules=f"If the teams collectively score more than 0.5 goals in the 3rd Period of {GAME}, then yes.",
                        rules2="Note: 3rd Period markets do not include overtime."))
    assert p3.semantics_status == PROVEN
    # regulation 1-1 (goals only in P1/P2), OT winner in period 4: P3 total is 0 => NO
    g = goals((1, 300, HOME, 1), (2, 1500, AWAY, 2), (4, 3800, HOME, 3))
    f = facts(2, 1, 1, 1, "OT", g, [{"player_id": i, "team_id": t, "name": "X. Y", "sweater": 1, "goals": 1, "assists": 0, "points": 1, "toi_s": 900}
                                    for i, t in ((1, HOME), (2, AWAY), (3, HOME))])
    assert f.problems() == []
    assert resolve(p3, f).outcome == NO


def test_first_ten_minutes_window_excludes_exactly_ten():
    f10 = build_spec(row("KXNHLF10G", "KXNHLF10G-26OCT01TBNYR-Y", "Either team to score in the first 10 minutes", "Goal in first 10 min",
                         strike_type="greater_or_equal", floor=1.0,
                         rules=f"If at least 1 goal is scored by either NYR or TBL during the first 10 minutes of the first period in {GAME}, then yes.".replace("NYR or TBL", "New York R or Tampa Bay")))
    sk = [{"player_id": 1, "team_id": HOME, "name": "A. B", "sweater": 1, "goals": 1, "assists": 0, "points": 1, "toi_s": 900},
          {"player_id": 2, "team_id": HOME, "name": "C. D", "sweater": 2, "goals": 0, "assists": 0, "points": 0, "toi_s": 900}]
    on_ten = facts(1, 0, 1, 0, "REG", goals((1, 600, HOME, 1)), sk)
    assert resolve(f10, on_ten).outcome == NO  # 10:00 elapsed does not count
    before = facts(1, 0, 1, 0, "REG", goals((1, 599, HOME, 1)), sk)
    assert resolve(f10, before).outcome == YES


@pytest.mark.parametrize("contract,box,ok", [("Alex DeBrincat", "A. DeBrincat", True), ("Charles Alexis Legault", "C. Legault", True),
                                             ("Charle-Edouard D'Astous", "C. D'Astous", True), ("James van Riemsdyk", "J. van Riemsdyk", True),
                                             ("Alex DeBrincat", "B. DeBrincat", False), ("Josh Doan", "J. Doan Jr.", True)])
def test_name_matching(contract, box, ok):
    assert names_match(contract, box) is ok


def player_spec(stat_series="KXNHLGOAL", name="Mika Zibanejad", n=1, stat="goals"):
    return build_spec(row(stat_series, f"{stat_series}-26OCT01TBNYR-NYRMZIBANEJAD93-{n}", f"{name}: {n}+ {stat}", f"{name}: {n}+",
                          floor=n - 0.5, rules=f"If {name} records {n}+ {stat} in {GAME}, then the market resolves to Yes.",
                          rules2="If a player is active but never enters the game, the market settles to the last fair market price before game start.",
                          cs='{"hockey_player": "u1", "hockey_team": "u2"}'))


def test_player_markets_void_scratch_and_goalie_scorer_reconciliation():
    sk = [{"player_id": 93, "team_id": HOME, "name": "M. Zibanejad", "sweater": 93, "goals": 1, "assists": 0, "points": 1, "toi_s": 1100},
          {"player_id": 95, "team_id": HOME, "name": "Z. Benson", "sweater": 95, "goals": 0, "assists": 0, "points": 0, "toi_s": 0}]
    gl = [{"player_id": 31, "team_id": HOME, "name": "I. Shesterkin", "sweater": 31, "saves": 24, "toi_s": 3600}]
    # the 5th NYR goal is scored by the goalie (empty net): skater goals 1 + goalie goal 1 == play-by-play 2
    f = facts(2, 0, 2, 0, "REG", goals((1, 300, HOME, 93), (3, 3446, HOME, 31)), sk, gl)
    assert f.problems() == []
    # without counting the goalie scorer the same game would be (wrongly) flagged inconsistent
    f_bad = facts(2, 0, 2, 0, "REG", goals((1, 300, HOME, 93), (3, 3446, HOME, 77)), sk, gl)
    assert any("boxscore skater goals" in p for p in f_bad.problems())
    assert resolve(player_spec(), f, HOME).outcome == YES
    assert resolve(player_spec(name="Mitch Marner", stat="goals"), f, HOME).outcome == NOT_IN_BOX  # not on any boxscore
    sk_benson = player_spec(name="Zach Benson")
    assert resolve(sk_benson, f, HOME).outcome == VOID  # dressed, zero ice time => rule voids to fair price


def test_first_goal_silent_when_no_goal_before_shootout():
    fg = build_spec(row("KXNHLFIRSTGOAL", "KXNHLFIRSTGOAL-26OCT01TBNYR-NYRMZIBANEJAD93", "Mika Zibanejad: First Goalscorer", "Mika Zibanejad",
                        strike_type="structured", rules=f"If Mika Zibanejad scores the 1st goal in {GAME}, then the market resolves to Yes.",
                        rules2="If a player is active but never enters the game, the market settles to the last fair market price before game start.",
                        cs='{"hockey_player": "u1", "hockey_team": "u2"}'))
    sk = [{"player_id": 93, "team_id": HOME, "name": "M. Zibanejad", "sweater": 93, "goals": 0, "assists": 0, "points": 0, "toi_s": 1100}]
    f = facts(1, 0, 0, 0, "SO", [], sk, [])
    assert resolve(fg, f, HOME).outcome == SILENT


def test_not_final_is_not_settled():
    f = facts(None, None, None, None, None)
    f.is_final = False
    assert resolve(total_spec(), f).outcome == "NOT_FINAL"
