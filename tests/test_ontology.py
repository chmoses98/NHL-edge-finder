"""Every discovered NHL series must map to a family; families carry a settlement basis; support is conservative."""

import json

from nhl_edge.config import REPO_ROOT
from nhl_edge.kalshi.discovery import is_nhl_series
from nhl_edge.kalshi.ontology import Ontology, Support


def test_ontology_loads_with_settlement_bases():
    o = Ontology.load()
    assert o.families["game_winner"].settles_on == "FINAL_INCL_OT_SO"
    assert o.families["game_regulation_winner"].settles_on == "REGULATION"
    assert o.families["game_winner"].support == Support.MODELABLE
    modelable = {n for n, f in o.families.items() if f.support == Support.MODELABLE}
    assert modelable == {"game_winner", "game_spread", "game_total", "team_total"}, "only the four settled-and-tested families are MODELABLE"


def test_known_series_map():
    o = Ontology.load()
    assert o.family_for_series("KXNHLGAME") == "game_winner"
    assert o.family_for_series("KXNHLSPREAD") == "game_spread"
    assert o.family_for_series("KXNHLTOTAL") == "game_total"
    assert o.family_for_series("KXNHL1PWINNER") == "period_winner"
    assert o.family_for_series("KXSTANLEYCUP") == "season_champion"
    assert o.family_for_series("KXNHLNOPE") is None


def test_every_discovered_series_is_in_the_ontology():
    """Enforced against the committed discovery summary once it exists (written by `nhl discover` on a runner)."""
    p = REPO_ROOT / "data" / "catalog" / "discovery_summary.json"
    if not p.exists():
        return
    o = Ontology.load()
    missing = [s["ticker"] for s in json.loads(p.read_text())["nhl_series"] if o.family_for_series(s["ticker"]) is None]
    assert missing == [], f"series without an ontology family: {missing}"


def test_is_nhl_series_rules():
    assert is_nhl_series({"ticker": "KXNHLGAME", "title": "NHL Game", "tags": ["Hockey"]})[0]
    assert not is_nhl_series({"ticker": "KXPWHLGAME", "title": "PWHL Game", "tags": ["Hockey"]})[0]
    assert not is_nhl_series({"ticker": "KXNCAAHOCKEY", "title": "NCAA Hockey", "tags": ["Hockey"]})[0]
    assert is_nhl_series({"ticker": "KXSTANLEYCUP", "title": "Stanley Cup winner", "tags": ["Hockey"]})[0]
    assert not is_nhl_series({"ticker": "KXNBAGAME", "title": "NBA Game", "tags": ["Basketball"]})[0]
