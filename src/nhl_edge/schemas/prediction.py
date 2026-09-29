from __future__ import annotations

from datetime import datetime
from enum import StrEnum

from pydantic import Field

from nhl_edge.schemas.core import Strict


class View(StrEnum):
    DATA_ONLY = "DATA_ONLY_V1"
    MARKET_BASELINE = "MARKET_BASELINE"
    MARKET_ANCHORED = "MARKET_ANCHORED_V1"


class Authority(StrEnum):
    """Every family starts, and tonight stays, RESEARCH_ONLY. Promotion needs prospective evidence + an explicit decision."""

    RESEARCH_ONLY = "RESEARCH_ONLY"
    SHADOW = "SHADOW"
    LIMITED = "LIMITED"
    TRUSTED = "TRUSTED"


class Gate(StrEnum):
    OK = "OK"  # 'OK' here means "the row is evaluable", never "bet this"
    NO_EDGE = "NO_EDGE"
    CANNOT_TRUST_INPUTS = "CANNOT_TRUST_INPUTS"
    UNSUPPORTED = "UNSUPPORTED"
    NOT_PREGAME = "NOT_PREGAME"


class ContractPrediction(Strict):
    """Immutable prediction record. One row per (ticker, prediction instant, model_version, run)."""

    prediction_id: str
    ticker: str
    game_id: str | None
    family: str
    predicted_at_utc: datetime
    data_cutoff_utc: datetime
    model_version: str
    sim_version: str
    feature_version: str
    n_sims: int
    seed: int | None = None
    p_data_only: float | None = None
    p_market: float | None = None  # Kalshi midpoint at the market observation instant
    p_market_anchored: float | None = None
    p_data_only_se: float | None = None
    market_observed_at_utc: datetime | None = None
    market_yes_bid: int | None = None
    market_yes_ask: int | None = None
    market_no_bid: int | None = None
    market_no_ask: int | None = None
    executable_p_yes: float | None = None  # yes_ask / 100: what YES actually costs
    executable_p_no: float | None = None  # no_ask / 100
    edge_yes_raw: float | None = None
    edge_yes_after_fee: float | None = None
    edge_no_raw: float | None = None
    edge_no_after_fee: float | None = None
    gate: Gate = Gate.UNSUPPORTED
    gate_reasons: list[str] = Field(default_factory=list)
    authority: Authority = Authority.RESEARCH_ONLY
    support: str = "UNRESOLVED"
    pregame: bool = True
    minutes_to_start: float | None = None
    horizon_label: str | None = None  # nearest canonical horizon (T-24h, T-6h ...) for later grouping; derived, not authoritative
    home_goalie_status: str | None = None
    away_goalie_status: str | None = None
    input_snapshot_ids: dict[str, str] = Field(default_factory=dict)
