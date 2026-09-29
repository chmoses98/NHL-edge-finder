from __future__ import annotations

from enum import StrEnum

from pydantic import Field

from nhl_edge.schemas.core import Strict


class Side(StrEnum):
    YES = "yes"
    NO = "no"


class Contract(Strict):
    """Our semantic reading of a Kalshi market: what quantity, what threshold, what YES means, and how it settles.

    ``settles_on`` is the NHL-specific axis that a basketball contract does not have: the same word "winner" can mean
    the final result including OT/SO, or regulation only. It is read from the ontology family and cross-checked
    against the market's ``rules_primary`` text in :func:`nhl_edge.kalshi.contracts.build_contract`.
    """

    ticker: str
    event_ticker: str | None = None
    series_ticker: str | None = None
    family: str
    scope: str  # game | player | season | other
    stat: str | None
    period: str
    settles_on: str = "FINAL_INCL_OT_SO"  # FINAL_INCL_OT_SO | REGULATION | PERIOD | EVENT | SEASON | OTHER
    game_id: str | None = None
    game_date: str | None = None  # from the ticker / rules, used to join to the schedule
    team_id: int | None = None  # the team the YES side refers to (winner/spread/team total)
    opponent_team_id: int | None = None
    game_team_ids: list[int] = Field(default_factory=list)  # both clubs in the game, order-free
    player_id: int | None = None
    threshold: float | None = None
    comparator: str | None = None  # 'ge' | 'gt' | 'le' | 'lt' | 'eq' | 'in_range'
    upper: float | None = None
    support: str = "UNRESOLVED"
    semantics_confidence: str = "low"
    notes: list[str] = Field(default_factory=list)
    entity_name: str | None = None
    kalshi_entity_uuid: str | None = None
    title: str | None = None
    rules_primary: str | None = None
