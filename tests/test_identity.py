"""Team identity: every current club, aliases, Kalshi/MoneyPuck codes, Utah/Arizona history, no name-string ambiguity."""

import pytest

from nhl_edge.identity.teams import TeamIdentityError, registry

CURRENT = ["ANA", "BOS", "BUF", "CAR", "CBJ", "CGY", "CHI", "COL", "DAL", "DET", "EDM", "FLA", "LAK", "MIN", "MTL", "NJD", "NSH", "NYI", "NYR", "OTT",
           "PHI", "PIT", "SEA", "SJS", "STL", "TBL", "TOR", "UTA", "VAN", "VGK", "WPG", "WSH"]


def test_all_32_current_clubs_present_and_active():
    reg = registry()
    assert [t.abbrev for t in reg.active_teams] == CURRENT
    assert len({t.team_id for t in reg.active_teams}) == 32


@pytest.mark.parametrize("alias,abbrev", [("T.B", "TBL"), ("TB", "TBL"), ("N.J", "NJD"), ("NJ", "NJD"), ("L.A", "LAK"), ("LA", "LAK"), ("S.J", "SJS"), ("SJ", "SJS"),
                                          ("MON", "MTL"), ("WAS", "WSH"), ("CAL", "CGY"), ("VEG", "VGK"), ("WIN", "WPG"), ("CLB", "CBJ"), ("UTAH", "UTA"), ("sjs", "SJS")])
def test_abbreviation_aliases(alias, abbrev):
    assert registry().by_abbrev(alias).abbrev == abbrev


def test_utah_history_resolves_without_renaming_the_past():
    reg = registry()
    assert reg.by_abbrev("UTA").team_id == 68  # Utah Mammoth, api-web id verified 2026-09-29
    assert reg.by_id(59).abbrev == "UHC" and not reg.by_id(59).active  # Utah Hockey Club 2024-25
    assert reg.by_id(53).abbrev == "ARI" and not reg.by_id(53).active
    assert reg.successor("ARI").abbrev == "UTA" and reg.successor("UHC").abbrev == "UTA" and reg.successor("BOS").abbrev == "BOS"


def test_unknown_codes_raise():
    with pytest.raises(TeamIdentityError):
        registry().by_abbrev("XXX")
    with pytest.raises(TeamIdentityError):
        registry().by_id(9999)


@pytest.mark.parametrize("text,abbrev", [("San Jose wins", "SJS"), ("Vancouver wins by over 2.5 goals", "VAN"), ("Vegas Golden Knights", "VGK"), ("Utah Mammoth", "UTA"),
                                         ("New York Rangers", "NYR"), ("New York Islanders", "NYI"), ("Montréal Canadiens", "MTL"), ("Tampa Bay", "TBL"), ("St. Louis", "STL"),
                                         ("Los Angeles Kings", "LAK"), ("Columbus Blue Jackets", "CBJ")])
def test_name_resolution_exact_single_hit(text, abbrev):
    assert registry().resolve_name(text).abbrev == abbrev


def test_name_resolution_is_ambiguous_for_bare_new_york_and_wildcard_words():
    reg = registry()
    assert reg.resolve_name("New York") is None
    assert reg.resolve_name("Vikings") is None  # "Kings" must not match inside "Vikings"
    assert reg.resolve_name("New York", candidates=["NYR", "BOS"]).abbrev == "NYR"  # candidates disambiguate
