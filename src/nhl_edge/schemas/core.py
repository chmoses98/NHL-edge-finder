"""Core NHL entities. Every timestamp is timezone-aware UTC; every game resolves to the official NHL game id."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SeasonType(StrEnum):
    PRESEASON = "preseason"
    REGULAR = "regular"
    PLAYOFFS = "playoffs"
    ALLSTAR = "allstar"
    OTHER = "other"


# api-web.nhle.com gameType: 1 preseason, 2 regular season, 3 playoffs, 4 all-star (observed 2023-2026)
GAME_TYPE_MAP = {1: SeasonType.PRESEASON, 2: SeasonType.REGULAR, 3: SeasonType.PLAYOFFS, 4: SeasonType.ALLSTAR}


def season_type_from_game_id(game_id: str | int) -> SeasonType:
    """NHL game ids: ``YYYY`` season start year + ``TT`` game type + ``NNNN`` sequence, e.g. 2026020001."""
    s = str(game_id)
    if len(s) != 10 or not s.isdigit():
        return SeasonType.OTHER
    return GAME_TYPE_MAP.get(int(s[4:6]), SeasonType.OTHER)


def season_from_game_id(game_id: str | int) -> str:
    s = str(game_id)
    if len(s) != 10 or not s.isdigit():
        return ""
    y = int(s[:4])
    return f"{y}-{str(y + 1)[2:]}"


def season_label(season_id: int | str) -> str:
    """20262027 -> '2026-27'."""
    s = str(season_id)
    return f"{s[:4]}-{s[6:8]}" if len(s) == 8 else s


class GameStatus(StrEnum):
    """Game-start gate states. Anything but NOT_STARTED is post-start information and never pregame."""

    NOT_STARTED = "not_started"
    LIVE = "live"
    FINAL = "final"
    POSTPONED = "postponed"
    CANCELED = "canceled"
    SUSPENDED = "suspended"
    UNKNOWN = "unknown"


class FinalPeriodType(StrEnum):
    REG = "REG"
    OT = "OT"
    SO = "SO"


class Game(Strict):
    game_id: str  # official NHL id, e.g. '2026020001'
    season: str  # '2026-27'
    season_type: SeasonType
    game_date_et: str  # YYYY-MM-DD (NHL 'gameDate')
    start_time_utc: datetime
    home_team_id: int
    away_team_id: int
    home_abbrev: str
    away_abbrev: str
    status: GameStatus = GameStatus.NOT_STARTED
    venue: str | None = None
    neutral_site: bool = False
    source: str = "nhl_api_schedule"
    home_score: int | None = None
    away_score: int | None = None
    last_period_type: FinalPeriodType | None = None  # populated only once final
    source_game_state: str | None = None  # raw gameState / gameScheduleState for provenance

    @field_validator("start_time_utc")
    @classmethod
    def _aware(cls, v: datetime) -> datetime:
        if v.tzinfo is None:
            raise ValueError("datetime must be timezone-aware")
        return v


class GoalieStatus(StrEnum):
    UNKNOWN = "UNKNOWN"
    PROJECTED = "PROJECTED"
    PROBABLE = "PROBABLE"
    CONFIRMED = "CONFIRMED"


GOALIE_STATUS_RANK = {GoalieStatus.UNKNOWN: 0, GoalieStatus.PROJECTED: 1, GoalieStatus.PROBABLE: 2, GoalieStatus.CONFIRMED: 3}


class GoalieObservation(Strict):
    """What we knew about a team's starting goalie at ``observed_at_utc``. Append-only; never edited."""

    game_id: str
    team_id: int
    player_id: int | None
    player_name: str | None
    status: GoalieStatus
    observed_at_utc: datetime
    source: str
    source_reported_at_utc: datetime | None = None
    confidence: float | None = None  # P(this goalie starts) when not CONFIRMED
    alternatives: list[dict[str, Any]] = Field(default_factory=list)  # [{player_id, player_name, p}]
    note: str | None = None


class Provenance(Strict):
    produced_at_utc: datetime
    producer: str
    code_version: str
    model_version: str | None = None
    inputs: dict[str, Any] = Field(default_factory=dict)
    data_cutoff_utc: datetime | None = None


class FinalResult(Strict):
    """Official final result of one game, as the settlement engine needs it. Built from the NHL boxscore.

    ``home_reg`` / ``away_reg`` are the scores at the end of the third period. For an OT or SO game they are equal;
    the ``home_final`` / ``away_final`` include the one deciding goal the NHL credits to the winner.
    """

    game_id: str
    status: GameStatus
    home_team_id: int
    away_team_id: int
    home_final: int | None = None
    away_final: int | None = None
    home_reg: int | None = None
    away_reg: int | None = None
    last_period_type: FinalPeriodType | None = None
    source: str = "nhl_api_boxscore"
    fetched_at_utc: datetime | None = None
    stat_correction_version: int = 0
    home_starting_goalie_id: int | None = None
    away_starting_goalie_id: int | None = None
    home_empty_net_goals: int | None = None
    away_empty_net_goals: int | None = None

    @property
    def is_final(self) -> bool:
        return self.status == GameStatus.FINAL and self.home_final is not None and self.away_final is not None and self.last_period_type is not None

    def opponent_of(self, team_id: int) -> int:
        if team_id == self.home_team_id:
            return self.away_team_id
        if team_id == self.away_team_id:
            return self.home_team_id
        raise KeyError(f"team {team_id} not in game {self.game_id}")

    def final_for(self, team_id: int) -> int:
        return self.home_final if team_id == self.home_team_id else self.away_final  # type: ignore[return-value]

    def reg_for(self, team_id: int) -> int:
        return self.home_reg if team_id == self.home_team_id else self.away_reg  # type: ignore[return-value]

    @property
    def went_to_overtime(self) -> bool:
        return self.last_period_type in (FinalPeriodType.OT, FinalPeriodType.SO)

    @property
    def went_to_shootout(self) -> bool:
        return self.last_period_type == FinalPeriodType.SO
