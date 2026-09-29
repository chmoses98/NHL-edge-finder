"""Contract semantics against the REAL Kalshi market objects captured by the probe (docs/probe/samples)."""

import json

import pytest

from nhl_edge.config import REPO_ROOT
from nhl_edge.kalshi.contracts import build_contract, game_key, settles_on_from_text
from nhl_edge.kalshi.ontology import Ontology, Support, classify_market
from nhl_edge.kalshi.ticker import parse_ticker

S = REPO_ROOT / "docs" / "probe" / "samples"


def markets(name):
    return [m for m in json.loads((S / f"{name}.json").read_text())["markets"] if isinstance(m, dict)]


@pytest.fixture(scope="module")
def onto():
    return Ontology.load()


def test_ticker_parse_short_tricodes():
    p = parse_ticker("KXNHLGAME-26OCT05SJDAL-SJ", {"SJ", "SJS", "DAL"})
    assert (p.game_date.isoformat(), p.away_tricode, p.home_tricode, p.market_suffix) == ("2026-10-05", "SJ", "DAL", "SJ")


def test_game_winner_real_market(onto):
    c = build_contract(markets("kalshi_api_markets_kxnhlgame_open")[0], onto)
    assert c.family == "game_winner" and c.stat == "winner" and c.settles_on == "FINAL_INCL_OT_SO"
    assert c.team_id == 28 and c.opponent_team_id == 25 and set(c.game_team_ids) == {25, 28}
    assert (c.comparator, c.threshold, c.support, c.semantics_confidence, c.game_date) == ("gt", 0.0, "MODELABLE", "high", "2026-10-05")
    assert game_key(c) == ("2026-10-05", frozenset({25, 28}))


def test_puck_line_real_market(onto):
    c = build_contract(markets("kalshi_api_markets_kxnhlspread_open")[0], onto)
    assert c.family == "game_spread" and c.stat == "margin" and c.comparator == "gt" and c.threshold == 2.5
    assert c.team_id == 23 and c.opponent_team_id == 22 and c.support == "MODELABLE"


def test_total_real_market_joins_without_a_team(onto):
    c = build_contract(markets("kalshi_api_markets_kxnhltotal_open")[0], onto)
    assert c.family == "game_total" and c.stat == "total" and c.threshold == 8.5 and c.team_id is None
    assert game_key(c) == ("2026-10-01", frozenset({22, 23}))


def test_every_real_sample_market_is_modelable_high_confidence(onto):
    for name in ("kalshi_api_markets_kxnhlgame_open", "kalshi_api_markets_kxnhlspread_open", "kalshi_api_markets_kxnhltotal_open"):
        for m in markets(name):
            c = build_contract(m, onto)
            assert c.support == "MODELABLE" and c.semantics_confidence == "high", (m["ticker"], c.notes)
            assert game_key(c) is not None, m["ticker"]


def test_regulation_wording_downgrades_to_needs_rule_review(onto):
    m = dict(markets("kalshi_api_markets_kxnhlgame_open")[0])
    m["rules_primary"] = "If San Jose wins in regulation the San Jose vs Dallas NHL game originally scheduled for Oct 5, 2026, then the market resolves to Yes."
    c = build_contract(m, onto)
    assert c.settles_on == "REGULATION" and c.support == "BUILDABLE"
    assert any("NEEDS_RULE_REVIEW" in n for n in c.notes)


def test_settles_on_cross_check():
    assert settles_on_from_text("FINAL_INCL_OT_SO", "Toronto wins in regulation", "")[0] == "REGULATION"
    assert settles_on_from_text("REGULATION", "Toronto wins", "including overtime and shootout")[0] == "FINAL_INCL_OT_SO"
    assert settles_on_from_text("FINAL_INCL_OT_SO", "Toronto wins", "")[0] == "FINAL_INCL_OT_SO"


def test_unknown_series_is_unresolved_not_dropped(onto):
    m = {"ticker": "KXNHLWEIRD-26OCT05SJDAL-X", "title": "Something new", "strike_type": "greater", "floor_strike": 1.5}
    cls = classify_market(m, onto)
    assert cls.support == Support.UNRESOLVED
    c = build_contract(m, onto)
    assert c.support == "UNRESOLVED"


def test_rules_date_mismatch_lowers_confidence(onto):
    m = dict(markets("kalshi_api_markets_kxnhlgame_open")[0])
    m["rules_primary"] = m["rules_primary"].replace("Oct 5, 2026", "Oct 6, 2026")
    c = build_contract(m, onto)
    assert c.semantics_confidence == "low" and c.support == "UNRESOLVED"
