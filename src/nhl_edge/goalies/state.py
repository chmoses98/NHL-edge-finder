"""Starting goalies as first-class, point-in-time state.

Status ladder: UNKNOWN < PROJECTED < PROBABLE < CONFIRMED. A status never silently upgrades: every observation is a
row in the append-only ``context/goalie_observations`` ledger kind with the instant it was observed and its source,
and a simulation reads the LATEST observation at or before its data cutoff. A goalie CONFIRMED at 17:00 is UNKNOWN
or PROJECTED to a 15:00 simulation, forever.

V1 uncertainty handling: when the starter is not CONFIRMED the simulator prices a MIXTURE of plausible starters
(``confidence`` on the named goalie, the remainder on the listed alternative / an average backup). Concretely the
goalie factor fed to the sim is the confidence-weighted average of the candidates' factors, and the packet reports
the spread between the candidates so a reader sees how much the goalie question is worth.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

from nhl_edge.schemas.core import GOALIE_STATUS_RANK, GoalieObservation, GoalieStatus
from nhl_edge.timeutil import parse_iso

# Confidence that the named goalie actually starts, by status. Priors; to be measured from the archive (observed
# status vs. the boxscore ``starter`` flag) once a few weeks of prospective data exist.
STATUS_CONFIDENCE = {GoalieStatus.CONFIRMED: 0.985, GoalieStatus.PROBABLE: 0.85, GoalieStatus.PROJECTED: 0.70, GoalieStatus.UNKNOWN: 0.0}

# DailyFaceoff "news strength" labels -> status. Anything unrecognised with a name is PROJECTED.
DFO_STRENGTH_MAP = {
    "confirmed": GoalieStatus.CONFIRMED, "official": GoalieStatus.CONFIRMED,
    "likely": GoalieStatus.PROBABLE, "expected": GoalieStatus.PROBABLE, "probable": GoalieStatus.PROBABLE,
    "unconfirmed": GoalieStatus.PROJECTED, "projected": GoalieStatus.PROJECTED, "possible": GoalieStatus.PROJECTED,
}


def status_from_label(label: str | None, has_name: bool) -> GoalieStatus:
    if not has_name:
        return GoalieStatus.UNKNOWN
    if not label:
        return GoalieStatus.PROJECTED
    return DFO_STRENGTH_MAP.get(label.strip().lower(), GoalieStatus.PROJECTED)


@dataclass(frozen=True)
class GoalieState:
    """What a simulation knows about one team's net at its cutoff."""

    team_id: int
    status: GoalieStatus
    player_id: int | None
    player_name: str | None
    confidence: float
    observed_at_utc: str | None
    source: str | None
    alternatives: list[dict[str, Any]]
    note: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "team_id": self.team_id, "status": self.status.value, "player_id": self.player_id, "player_name": self.player_name,
            "confidence": self.confidence, "observed_at_utc": self.observed_at_utc, "source": self.source,
            "alternatives": self.alternatives, "note": self.note,
        }


def unknown_state(team_id: int, note: str = "no goalie observation at or before the data cutoff") -> GoalieState:
    return GoalieState(team_id=team_id, status=GoalieStatus.UNKNOWN, player_id=None, player_name=None, confidence=0.0,
                       observed_at_utc=None, source=None, alternatives=[], note=note)


def latest_state(observations: list[dict[str, Any] | GoalieObservation], game_id: str, team_id: int, cutoff: datetime) -> GoalieState:
    """The latest observation for (game, team) observed at or before ``cutoff``. Later observations are invisible."""
    best: dict[str, Any] | None = None
    best_ts: datetime | None = None
    for o in observations:
        d = o.model_dump() if isinstance(o, GoalieObservation) else o
        if str(d.get("game_id")) != str(game_id) or int(d.get("team_id", -1)) != int(team_id):
            continue
        ts = d.get("observed_at_utc")
        ts = parse_iso(ts) if isinstance(ts, str) else ts
        if ts is None or ts > cutoff:
            continue
        if best_ts is None or ts > best_ts or (ts == best_ts and GOALIE_STATUS_RANK[GoalieStatus(d["status"])] > GOALIE_STATUS_RANK[GoalieStatus(best["status"])]):
            best, best_ts = d, ts
    if best is None:
        return unknown_state(team_id)
    status = GoalieStatus(best["status"])
    conf = best.get("confidence")
    return GoalieState(
        team_id=team_id, status=status, player_id=best.get("player_id"), player_name=best.get("player_name"),
        confidence=float(conf) if conf is not None else STATUS_CONFIDENCE[status],
        observed_at_utc=best_ts.isoformat().replace("+00:00", "Z") if best_ts else None, source=best.get("source"),
        alternatives=list(best.get("alternatives") or []), note=best.get("note"),
    )


def mixture_factor(state: GoalieState, factor_for: dict[int | None, float], backup_factor: float = 1.0) -> tuple[float, dict[str, Any]]:
    """Confidence-weighted goalie factor. ``factor_for`` maps player_id -> regressed GA/xGA factor (1.0 = average).

    UNKNOWN -> the backup/average factor with full uncertainty flagged. Returns (factor, detail)."""
    if state.status == GoalieStatus.UNKNOWN or state.player_id is None:
        return backup_factor, {"method": "unknown_starter_average", "named_factor": None, "alt_factor": backup_factor, "weight_named": 0.0}
    named = factor_for.get(state.player_id, backup_factor)
    alt_ids = [a.get("player_id") for a in state.alternatives if a.get("player_id") is not None]
    alt = sum(factor_for.get(i, backup_factor) for i in alt_ids) / len(alt_ids) if alt_ids else backup_factor
    w = min(max(state.confidence, 0.0), 1.0)
    f = w * named + (1 - w) * alt
    return f, {"method": "mixture", "named_factor": named, "alt_factor": alt, "weight_named": w, "spread": abs(named - alt)}


def parse_dailyfaceoff_next_data(page_props: dict[str, Any], observed_at: datetime, registry_resolve) -> tuple[list[GoalieObservation], list[str]]:
    """DailyFaceoff starting-goalies page (__NEXT_DATA__.props.pageProps). Shape verified 2026-09-29 (docs/probe/samples).

    Each ``data`` row carries home/away team name, goalie name, a news-strength label (Confirmed/Likely/Unconfirmed
    or null) and ``dateGmt``. The row ALSO carries sportsbook prices (moneyline/spread): those are deliberately NOT
    read here — DATA_ONLY inputs must never see a market price. ``registry_resolve(name) -> team_id | None``.
    """
    obs: list[GoalieObservation] = []
    problems: list[str] = []
    for row in page_props.get("data") or []:
        date = row.get("date")
        for side in ("home", "away"):
            tname = row.get(f"{side}TeamName")
            tid = registry_resolve(tname) if tname else None
            if tid is None:
                problems.append(f"unresolved team {tname!r}")
                continue
            name = row.get(f"{side}GoalieName")
            label = row.get(f"{side}NewsStrengthName")
            status = status_from_label(label, bool(name))
            reported = row.get(f"{side}NewsCreatedAt")
            try:
                reported_dt = parse_iso(reported) if reported else None
            except ValueError:
                reported_dt = None
            obs.append(GoalieObservation(
                game_id=f"dfo:{date}:{tid}",  # placeholder; resolved to the NHL game id by the context job via (date, team)
                team_id=int(tid), player_id=None, player_name=name, status=status, observed_at_utc=observed_at,
                source="dailyfaceoff", source_reported_at_utc=reported_dt, confidence=STATUS_CONFIDENCE[status],
                alternatives=[], note=f"dfo_label={label!r}; dfo_goalie_id={row.get(f'{side}GoalieId')}; game_time_gmt={row.get('dateGmt')}",
            ))
    return obs, problems
