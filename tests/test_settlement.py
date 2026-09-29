"""Deterministic settlement tests: no network, no clock. FLA (home, 13) vs CHI (away, 16), game 2025020001."""

from datetime import UTC, datetime

import pytest

from nhl_edge.schemas.core import FinalPeriodType, FinalResult, GameStatus
from nhl_edge.schemas.market import Contract
from nhl_edge.settlement.engine import (
    DISAGREE_PREFIX,
    ENGINE_VERSION,
    SettlementOutcome,
    _kalshi_outcome,
    _reconcile_with_kalshi,
    final_result_from_boxscore,
    idempotency_key,
    semantics_fingerprint,
    settle_contract,
    settle_many,
)

HOME, AWAY = 13, 16  # FLA, CHI
GAME = "2025020001"
NOW = datetime(2025, 10, 8, 3, 0, tzinfo=UTC)


def result(**over) -> FinalResult:
    """Regulation game: FLA 3, CHI 2."""
    base = dict(
        game_id=GAME, status=GameStatus.FINAL, home_team_id=HOME, away_team_id=AWAY,
        home_final=3, away_final=2, home_reg=3, away_reg=2, last_period_type=FinalPeriodType.REG,
        source="test", fetched_at_utc=NOW,
    )
    base.update(over)
    return FinalResult(**base)


def ot_result(**over) -> FinalResult:
    """OT game: FLA 3, CHI 2 after overtime; regulation 2-2."""
    return result(home_final=3, away_final=2, home_reg=2, away_reg=2, last_period_type=FinalPeriodType.OT, **over)


def so_result(**over) -> FinalResult:
    """Shootout game: CHI 4, FLA 3 in a shootout; regulation 3-3."""
    return result(home_final=3, away_final=4, home_reg=3, away_reg=3, last_period_type=FinalPeriodType.SO, **over)


def contract(**over) -> Contract:
    base = dict(
        ticker="KXNHLGAME-25OCT07CHIFLA-FLA", family="game_winner", scope="game", stat="winner", period="FULL",
        settles_on="FINAL_INCL_OT_SO", game_id=GAME, team_id=HOME, opponent_team_id=AWAY,
        game_team_ids=[HOME, AWAY], comparator="gt", threshold=0.0, support="MODELABLE", semantics_confidence="high",
    )
    base.update(over)
    return Contract(**base)


def spread(team_id: int, line: float, **over) -> Contract:
    opp = AWAY if team_id == HOME else HOME
    base = dict(ticker=f"KXNHLSPREAD-25OCT07CHIFLA-{team_id}-{line}", family="game_spread", stat="margin",
                team_id=team_id, opponent_team_id=opp, comparator="gt", threshold=line)
    return contract(**{**base, **over})


def total(line: float, comparator: str = "gt", **over) -> Contract:
    base = dict(ticker=f"KXNHLTOTAL-25OCT07CHIFLA-{line}-{comparator}", family="game_total", stat="total",
                team_id=None, opponent_team_id=None, comparator=comparator, threshold=line)
    return contract(**{**base, **over})


def team_total(team_id: int, line: float, comparator: str = "gt", **over) -> Contract:
    opp = AWAY if team_id == HOME else HOME
    base = dict(ticker=f"KXNHLTEAMTOTAL-25OCT07CHIFLA-{team_id}-{line}", family="team_total", stat="team_total",
                team_id=team_id, opponent_team_id=opp, comparator=comparator, threshold=line)
    return contract(**{**base, **over})


def event(stat: str, **over) -> Contract:
    base = dict(ticker=f"KXNHL{stat.upper()}-25OCT07CHIFLA", family=f"game_{stat}", stat=stat, team_id=None,
                opponent_team_id=None, comparator="ge", threshold=1.0, support="BUILDABLE", semantics_confidence="medium")
    return contract(**{**base, **over})


def reg_winner(team_id: int, **over) -> Contract:
    opp = AWAY if team_id == HOME else HOME
    base = dict(ticker=f"KXNHLREGWINNER-25OCT07CHIFLA-{team_id}", family="game_regulation_winner", stat="reg_winner",
                settles_on="REGULATION", team_id=team_id, opponent_team_id=opp, support="BUILDABLE",
                semantics_confidence="medium")
    return contract(**{**base, **over})


# ---- regulation game ------------------------------------------------------------------------------


def test_regulation_winner_yes_and_no():
    r = settle_contract(contract(), result(), now=NOW)
    assert r.outcome == SettlementOutcome.YES and r.value == 1.0
    assert r.settles_on == "FINAL_INCL_OT_SO" and r.engine_version == ENGINE_VERSION and r.game_id == GAME
    r = settle_contract(contract(team_id=AWAY, opponent_team_id=HOME), result(), now=NOW)
    assert r.outcome == SettlementOutcome.NO and r.value == -1.0


def test_regulation_game_regulation_winner_matches_final_winner():
    assert settle_contract(reg_winner(HOME), result()).outcome == SettlementOutcome.YES
    assert settle_contract(reg_winner(AWAY), result()).outcome == SettlementOutcome.NO


def test_regulation_puck_line_both_sides():
    # FLA won by 1: FLA -1.5 NO, CHI +1.5 YES; FLA +1.5 YES; CHI -1.5 NO
    assert settle_contract(spread(HOME, -1.5), result()).outcome == SettlementOutcome.YES
    r = settle_contract(spread(HOME, 1.5), result())
    assert r.outcome == SettlementOutcome.NO and r.value == 1.0
    r = settle_contract(spread(AWAY, -1.5), result())
    assert r.outcome == SettlementOutcome.YES and r.value == -1.0
    assert settle_contract(spread(AWAY, 1.5), result()).outcome == SettlementOutcome.NO


def test_regulation_total_over_under():
    r = settle_contract(total(4.5), result())
    assert r.outcome == SettlementOutcome.YES and r.value == 5.0
    assert settle_contract(total(5.5), result()).outcome == SettlementOutcome.NO
    assert settle_contract(total(5.5, "lt"), result()).outcome == SettlementOutcome.YES
    assert settle_contract(total(4.5, "lt"), result()).outcome == SettlementOutcome.NO
    rng = total(4, "in_range", upper=6)
    assert settle_contract(rng, result()).outcome == SettlementOutcome.YES


def test_regulation_team_totals():
    r = settle_contract(team_total(HOME, 2.5), result())
    assert r.outcome == SettlementOutcome.YES and r.value == 3.0
    assert settle_contract(team_total(HOME, 3.5), result()).outcome == SettlementOutcome.NO
    r = settle_contract(team_total(AWAY, 2.5), result())
    assert r.outcome == SettlementOutcome.NO and r.value == 2.0
    assert settle_contract(team_total(AWAY, 1.5), result()).outcome == SettlementOutcome.YES


def test_regulation_game_events_all_no():
    assert settle_contract(event("overtime"), result()).outcome == SettlementOutcome.NO
    assert settle_contract(event("shootout"), result()).outcome == SettlementOutcome.NO
    r = settle_contract(event("btts"), result())
    assert r.outcome == SettlementOutcome.YES and r.value == 1.0
    r = settle_contract(event("btts"), result(away_final=0, away_reg=0))
    assert r.outcome == SettlementOutcome.NO and r.value == 0.0


# ---- overtime game --------------------------------------------------------------------------------


def test_overtime_game_winner_incl_ot_and_regulation_winner_both_no():
    r = settle_contract(contract(), ot_result())
    assert r.outcome == SettlementOutcome.YES and r.value == 1.0
    assert settle_contract(contract(team_id=AWAY, opponent_team_id=HOME), ot_result()).outcome == SettlementOutcome.NO
    home = settle_contract(reg_winner(HOME), ot_result())
    away = settle_contract(reg_winner(AWAY), ot_result())
    assert home.outcome == SettlementOutcome.NO and "regulation tie 2-2" in home.reason and home.value == 0.0
    assert away.outcome == SettlementOutcome.NO and away.value == 0.0


def test_overtime_game_puck_lines():
    r = settle_contract(spread(HOME, 1.5), ot_result())
    assert r.outcome == SettlementOutcome.NO and r.value == 1.0  # OT win is a one-goal margin
    r = settle_contract(spread(AWAY, -1.5), ot_result())
    assert r.outcome == SettlementOutcome.YES and r.value == -1.0


def test_overtime_game_total_and_events():
    r = settle_contract(total(4.5), ot_result())
    assert r.outcome == SettlementOutcome.YES and r.value == 5.0
    reg_total = total(4.5, settles_on="REGULATION", support="BUILDABLE")
    r = settle_contract(reg_total, ot_result())
    assert r.outcome == SettlementOutcome.NO and r.value == 4.0
    r = settle_contract(event("overtime"), ot_result())
    assert r.outcome == SettlementOutcome.YES and r.value == 1.0
    r = settle_contract(event("shootout"), ot_result())
    assert r.outcome == SettlementOutcome.NO and r.value == 0.0


# ---- shootout game --------------------------------------------------------------------------------


def test_shootout_game():
    r = settle_contract(event("shootout"), so_result())
    assert r.outcome == SettlementOutcome.YES and r.value == 1.0
    assert settle_contract(event("overtime"), so_result()).outcome == SettlementOutcome.YES
    assert settle_contract(contract(), so_result()).outcome == SettlementOutcome.NO  # CHI won the SO
    assert settle_contract(contract(team_id=AWAY, opponent_team_id=HOME), so_result()).outcome == SettlementOutcome.YES
    assert settle_contract(reg_winner(HOME), so_result()).outcome == SettlementOutcome.NO
    assert settle_contract(reg_winner(AWAY), so_result()).outcome == SettlementOutcome.NO
    r = settle_contract(total(6.5), so_result())
    assert r.outcome == SettlementOutcome.YES and r.value == 7.0
    r = settle_contract(total(6.5, settles_on="REGULATION", support="BUILDABLE"), so_result())
    assert r.outcome == SettlementOutcome.NO and r.value == 6.0
    r = settle_contract(team_total(AWAY, 3.5), so_result())
    assert r.outcome == SettlementOutcome.YES and r.value == 4.0
    r = settle_contract(team_total(AWAY, 3.5, settles_on="REGULATION", support="BUILDABLE"), so_result())
    assert r.outcome == SettlementOutcome.NO and r.value == 3.0
    assert settle_contract(spread(AWAY, -1.5), so_result()).outcome == SettlementOutcome.YES  # margin 1 > -1.5
    assert settle_contract(spread(AWAY, 1.5), so_result()).outcome == SettlementOutcome.NO


# ---- push_on_tie & integer lines ------------------------------------------------------------------


def test_integer_puck_line_exact_hit_follows_comparator_unless_push_on_tie():
    gt = spread(HOME, 1.0)
    assert settle_contract(gt, result()).outcome == SettlementOutcome.NO
    ge = spread(HOME, 1.0, comparator="ge")
    assert settle_contract(ge, result()).outcome == SettlementOutcome.YES
    push = spread(HOME, 1.0, notes=["push_on_tie"])
    r = settle_contract(push, result())
    assert r.outcome == SettlementOutcome.PUSH and "push_on_tie" in r.reason
    assert settle_contract(total(5, notes=["push_on_tie"]), result()).outcome == SettlementOutcome.PUSH
    assert settle_contract(total(5), result()).outcome == SettlementOutcome.NO


def test_regulation_tie_push_on_tie():
    r = settle_contract(reg_winner(HOME, notes=["push_on_tie"]), ot_result())
    assert r.outcome == SettlementOutcome.PUSH and r.value == 0.0
    r = settle_contract(reg_winner(HOME), ot_result())
    assert r.outcome == SettlementOutcome.NO


def test_margin_bucket_in_range():
    bucket = contract(ticker="KXNHLWINMARGIN-25OCT07CHIFLA-FLA1", family="game_win_margin", stat="margin_bucket",
                      comparator="in_range", threshold=1, upper=1, support="BUILDABLE", semantics_confidence="medium")
    assert settle_contract(bucket, result()).outcome == SettlementOutcome.YES
    assert settle_contract(bucket, ot_result()).outcome == SettlementOutcome.YES
    wide = bucket.model_copy(update={"threshold": 2.0, "upper": 99.0})
    assert settle_contract(wide, result()).outcome == SettlementOutcome.NO
    missing = bucket.model_copy(update={"upper": None})
    r = settle_contract(missing, result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "upper bound" in r.reason


# ---- gates ----------------------------------------------------------------------------------------


def test_postponed_canceled_suspended_are_unsettleable():
    for status in (GameStatus.POSTPONED, GameStatus.CANCELED, GameStatus.SUSPENDED):
        r = settle_contract(contract(), result(status=status, home_final=None, away_final=None, home_reg=None,
                                               away_reg=None, last_period_type=None))
        assert r.outcome == SettlementOutcome.UNSETTLEABLE and status.value in r.reason and "Kalshi decides void" in r.reason
        assert r.value is None


def test_live_and_incomplete_games_are_unsettleable():
    r = settle_contract(contract(), result(status=GameStatus.LIVE, home_reg=None, away_reg=None, last_period_type=None))
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "not final" in r.reason
    r = settle_contract(contract(), result(status=GameStatus.NOT_STARTED, home_final=None, away_final=None,
                                           home_reg=None, away_reg=None, last_period_type=None))
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "not final" in r.reason
    # FINAL status but the result is not is_final (no last period type) still fails closed
    r = settle_contract(contract(), result(last_period_type=None))
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "not final" in r.reason


def test_regulation_basis_without_regulation_scores_is_unsettleable():
    r = settle_contract(reg_winner(HOME), result(home_reg=None, away_reg=None))
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "regulation score missing" in r.reason


def test_unsupported_support_or_confidence_is_unsettleable():
    for support in ("RESEARCH", "UNRESOLVED", "UNMODELABLE"):
        r = settle_contract(contract(support=support), result())
        assert r.outcome == SettlementOutcome.UNSETTLEABLE and "semantics not proven" in r.reason
    r = settle_contract(contract(semantics_confidence="low"), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "semantics not proven" in r.reason


def test_game_id_and_team_mismatches_are_unsettleable():
    r = settle_contract(contract(game_id="2025020002"), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "mismatch" in r.reason
    r = settle_contract(contract(team_id=10, opponent_team_id=None, game_team_ids=[]), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "not in game" in r.reason
    r = settle_contract(contract(game_team_ids=[HOME, 10]), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "game teams" in r.reason


def test_non_game_scope_and_non_final_bases_are_unsettleable():
    r = settle_contract(contract(scope="player", stat="goals", team_id=None, opponent_team_id=None, player_id=1), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "scope" in r.reason
    r = settle_contract(contract(scope="season", stat="champion", period="SEASON", settles_on="SEASON",
                                 opponent_team_id=None, game_team_ids=[]), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE
    r = settle_contract(contract(period="P1", settles_on="PERIOD"), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "settles_on" in r.reason
    r = settle_contract(contract(period="P1"), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "period" in r.reason


def test_contradictory_stat_and_basis_combinations_are_unsettleable():
    r = settle_contract(reg_winner(HOME, settles_on="FINAL_INCL_OT_SO"), ot_result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "reg_winner" in r.reason
    r = settle_contract(event("overtime", settles_on="REGULATION"), ot_result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "overtime" in r.reason
    r = settle_contract(spread(HOME, 1.5).model_copy(update={"team_id": None, "opponent_team_id": None}), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "team_id missing" in r.reason
    r = settle_contract(contract(stat="first_goal"), result())
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "unsupported game stat" in r.reason


def test_final_tie_is_corrupt_data_not_a_settlement():
    r = settle_contract(contract(), result(home_final=2, away_final=2, home_reg=2, away_reg=2))
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and "tied" in r.reason


# ---- idempotency ----------------------------------------------------------------------------------


def test_settle_many_returns_existing_record_unchanged():
    c = contract()
    first = settle_contract(c, result(), now=NOW)
    assert settle_contract(c, result(), now=NOW) == first
    existing = {first.idempotency_key: first}
    later = settle_many([c], result(), existing, now=datetime(2027, 1, 1, tzinfo=UTC))
    assert later[0] is first
    fresh = settle_many([c, total(4.5)], result(), existing, now=NOW)
    assert fresh[0] is first and fresh[1].outcome == SettlementOutcome.YES
    assert existing[first.idempotency_key] is first


def test_changed_threshold_or_basis_produces_a_new_key():
    args = ("KXNHLTOTAL-X", GAME, ENGINE_VERSION, 0)
    original = idempotency_key(*args, total(4.5))
    assert idempotency_key(*args, total(4.5)) == original
    assert idempotency_key(*args, total(5.5)) != original
    assert idempotency_key(*args, total(4.5, "lt")) != original
    assert idempotency_key(*args, total(4.5, settles_on="REGULATION")) != original
    assert semantics_fingerprint(spread(HOME, 1.5)) != semantics_fingerprint(spread(AWAY, 1.5))
    assert semantics_fingerprint(None) == "-"


def test_stat_correction_bump_produces_a_new_record_and_keeps_the_old():
    c = spread(HOME, 1.5)
    first = settle_contract(c, result(), now=NOW)
    assert first.outcome == SettlementOutcome.NO
    existing = {first.idempotency_key: first}
    corrected = settle_many([c], result(stat_correction_version=1, home_final=4, home_reg=4), existing, now=NOW)[0]
    assert corrected.idempotency_key != first.idempotency_key
    assert corrected.outcome == SettlementOutcome.YES and corrected.value == 2.0
    assert "stat correction v1" in corrected.reason and corrected.stat_correction_version == 1
    assert existing[first.idempotency_key] is first


# ---- Kalshi reconciliation ------------------------------------------------------------------------


def test_disagreement_with_kalshi_is_flagged_not_overridden():
    r = settle_contract(contract(), result(), kalshi_result="no")
    assert r.outcome == SettlementOutcome.YES and r.reason.startswith(DISAGREE_PREFIX)
    assert "ours=YES kalshi=NO" in r.reason
    r = settle_contract(contract(), result(), kalshi_result="yes")
    assert r.outcome == SettlementOutcome.YES and "agrees with Kalshi" in r.reason
    r = settle_contract(contract(), result(), kalshi_result="scalar")
    assert r.outcome == SettlementOutcome.YES and "kalshi=VOID" in r.reason
    r = settle_contract(contract(), result(), kalshi_result="partially")
    assert r.outcome == SettlementOutcome.YES and "(unrecognised)" in r.reason
    r = settle_contract(contract(support="UNRESOLVED"), result(), kalshi_result="yes")
    assert r.outcome == SettlementOutcome.UNSETTLEABLE and r.reason.endswith("kalshi_result=yes")


def test_settle_many_passes_kalshi_results_by_ticker():
    c = contract()
    out = settle_many([c], result(), {}, kalshi_results={c.ticker: "no"}, now=NOW)
    assert out[0].outcome == SettlementOutcome.YES and out[0].reason.startswith(DISAGREE_PREFIX)


def test_kalshi_vocabulary():
    assert _kalshi_outcome("YES") is SettlementOutcome.YES
    assert _kalshi_outcome(" no ") is SettlementOutcome.NO
    assert _kalshi_outcome("void") is SettlementOutcome.VOID
    assert _kalshi_outcome("scalar") is SettlementOutcome.VOID
    assert _kalshi_outcome("other") is None and _kalshi_outcome(None) is None
    outcome, reason = _reconcile_with_kalshi(SettlementOutcome.NO, "x", "yes")
    assert outcome is SettlementOutcome.NO and reason.startswith(DISAGREE_PREFIX)


# ---- final_result_from_boxscore -------------------------------------------------------------------

# Shape of nhl_edge.data.nhl_api.parse_boxscore output for docs/probe/samples/nhl_boxscore_final_2025.json
# (FLA 3, CHI 2, regulation; Bobrovsky and Knight started).
BOX_FLA_CHI = {
    "game_id": "2025020001", "status": "final", "game_state": "OFF", "schedule_state": "OK",
    "home_team_id": 13, "away_team_id": 16, "home_abbrev": "FLA", "away_abbrev": "CHI",
    "home_score": 3, "away_score": 2, "last_period_type": "REG", "home_reg_score": 3, "away_reg_score": 2,
    "home_sog": 37, "away_sog": 19,
    "home_goalies": [
        {"player_id": 8480193, "name": "D. Tarasov", "starter": False, "decision": None, "toi": "00:00",
         "shots_against": 0, "goals_against": 0, "save_pct": None},
        {"player_id": 8475683, "name": "S. Bobrovsky", "starter": True, "decision": "W", "toi": "60:00",
         "shots_against": 19, "goals_against": 2, "save_pct": 0.894737},
    ],
    "away_goalies": [
        {"player_id": 8481519, "name": "S. Knight", "starter": True, "decision": "L", "toi": "59:04",
         "shots_against": 37, "goals_against": 3, "save_pct": 0.918919},
        {"player_id": 8482821, "name": "A. Soderblom", "starter": False, "decision": None, "toi": "00:00",
         "shots_against": 0, "goals_against": 0, "save_pct": None},
    ],
    "start_time_utc": "2025-10-07T21:00:00Z", "game_date": "2025-10-07", "period_number": 3,
}


def test_final_result_from_boxscore_fixture():
    fr = final_result_from_boxscore(BOX_FLA_CHI, fetched_at_utc="2025-10-08T03:00:00Z", stat_correction_version=0)
    assert fr.game_id == GAME and fr.status == GameStatus.FINAL and fr.is_final
    assert (fr.home_team_id, fr.away_team_id) == (HOME, AWAY)
    assert (fr.home_final, fr.away_final, fr.home_reg, fr.away_reg) == (3, 2, 3, 2)
    assert fr.last_period_type == FinalPeriodType.REG and not fr.went_to_overtime and not fr.went_to_shootout
    assert fr.home_starting_goalie_id == 8475683 and fr.away_starting_goalie_id == 8481519
    assert fr.source == "nhl_api_boxscore" and fr.fetched_at_utc == NOW and fr.stat_correction_version == 0
    r = settle_contract(contract(), fr, now=NOW)
    assert r.outcome == SettlementOutcome.YES and r.result_source == "nhl_api_boxscore"


def test_final_result_from_boxscore_overtime_and_live_shapes():
    ot = dict(BOX_FLA_CHI, home_score=3, away_score=2, last_period_type="OT", home_reg_score=2, away_reg_score=2)
    fr = final_result_from_boxscore(ot)
    assert fr.went_to_overtime and not fr.went_to_shootout and fr.reg_for(HOME) == 2 and fr.final_for(HOME) == 3
    live = dict(BOX_FLA_CHI, status="live", last_period_type=None, home_reg_score=None, away_reg_score=None,
                home_score=1, away_score=1, home_goalies=[], away_goalies=[])
    fr = final_result_from_boxscore(live)
    assert fr.status == GameStatus.LIVE and not fr.is_final and fr.home_starting_goalie_id is None
    assert settle_contract(contract(), fr).outcome == SettlementOutcome.UNSETTLEABLE
    weird = dict(BOX_FLA_CHI, status="???", last_period_type="XX")
    fr = final_result_from_boxscore(weird)
    assert fr.status == GameStatus.UNKNOWN and fr.last_period_type is None and not fr.is_final


def test_final_result_from_boxscore_rejects_unidentified_games():
    with pytest.raises(ValueError):
        final_result_from_boxscore(dict(BOX_FLA_CHI, home_team_id=None))
    with pytest.raises(ValueError):
        final_result_from_boxscore(dict(BOX_FLA_CHI, game_id=None))
