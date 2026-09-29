"""Price a ``Contract`` from an nhl-sim-2.0 joint draw (DATA_ONLY_V2 shadow arm).

Full-game families use the unchanged V1 pricer (an :class:`SimV2Result` IS a ``SimResult``), so V1 and V2 differ only
through their draws. Period families (``period_winner``, ``period_spread``, ``period_total``) are priced from the same
draw's per-period goals, which sum to regulation on every draw.

Pricing a period contract is NOT the same as supporting it: the ontology keeps those families at RESEARCH until the
contract rules and settlement are verified (docs/KALSHI_MARKET_MAP.md). Every period price therefore carries
``v2_support`` = ``PARTIAL_RULES_VERIFIED_NO_SETTLEMENT`` (rule text reviewed 2026-09-29; the settlement engine does not
read period line scores yet) and never a gate of its own.
"""

from __future__ import annotations

from nhl_edge.pricing.price import Priced, _cmp, price_contract
from nhl_edge.schemas.market import Contract
from nhl_edge.sim.engine_v2 import SimV2Result

PERIOD_FAMILIES = ("period_winner", "period_spread", "period_total")
PERIOD_SUPPORT = "PARTIAL_RULES_VERIFIED_NO_SETTLEMENT"  # docs/KALSHI_MARKET_MAP.md: rules read 2026-09-29; settlement not built


def _period_index(c: Contract) -> int | None:
    p = str(c.period or "").upper()
    return {"P1": 1, "P2": 2, "P3": 3}.get(p)


def price_contract_v2(c: Contract, res: SimV2Result, home_team_id: int, away_team_id: int) -> tuple[Priced, str]:
    """(Priced, v2_support). ``v2_support`` is the contract's own support for full-game families."""
    if c.family not in PERIOD_FAMILIES:
        return price_contract(c, res, home_team_id, away_team_id), str(c.support)
    q = _period_index(c)
    if q is None:
        return Priced(None, None, False, f"period {c.period!r} not P1/P2/P3"), PERIOD_SUPPORT
    home: bool | None = None
    if c.team_id is not None:
        if c.team_id == home_team_id:
            home = True
        elif c.team_id == away_team_id:
            home = False
        else:
            return Priced(None, None, False, "contract team is not in this game"), PERIOD_SUPPORT
    h, a = res.period_goals(q, True), res.period_goals(q, False)
    try:
        if c.family == "period_winner":
            if home is None:  # the TIE market ('1st period tie')
                p, se = res.p(h == a)
            else:
                p, se = res.p(h > a) if home else res.p(a > h)
        elif c.family == "period_spread":
            if home is None:
                return Priced(None, None, False, "period spread without a team"), PERIOD_SUPPORT
            p, se = _cmp(res, (h - a) if home else (a - h), c)
        else:
            p, se = _cmp(res, h + a, c)
    except ValueError as e:
        return Priced(None, None, False, str(e)), PERIOD_SUPPORT
    return Priced(float(p), float(se), True, f"priced from nhl-sim-2.0 P{q} draws (period family support {PERIOD_SUPPORT})"), PERIOD_SUPPORT
