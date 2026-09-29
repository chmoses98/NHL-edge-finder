"""Settlement engine: ``Contract`` + ``FinalResult`` -> ``SettlementRecord``.

Fail-closed rules (see ``settle_contract``):

* Only a FINAL, ``is_final`` result can settle anything. Postponed / canceled / suspended games are UNSETTLEABLE;
  Kalshi decides whether they void, we never guess.
* Only contracts whose semantics we have proven (support MODELABLE/BUILDABLE, confidence high/medium) settle, and
  only game-scope contracts: player props, period markets and futures need data a ``FinalResult`` does not carry.
* ``settles_on`` picks the score the contract is read against: ``FINAL_INCL_OT_SO`` uses the official final (the
  OT/SO deciding goal included, so a shootout win is a one-goal margin), ``REGULATION`` uses the end-of-third-period
  score. Anything else (PERIOD, EVENT, SEASON, OTHER) is UNSETTLEABLE here.
* A supplied ``kalshi_result`` never overrides our computed outcome; a disagreement is flagged in the reason with the
  ``DISAGREES_WITH_KALSHI:`` prefix so the caller must surface it.
* Records are keyed by (ticker, game_id, engine_version, stat_correction_version, semantics fingerprint). A stat
  correction or a corrected contract reading appends a new record with a new key; existing records are never
  rewritten (``settle_many``).

RESEARCH_ONLY: this module settles *records* for evaluation and calibration. It places nothing anywhere.
"""

from __future__ import annotations

import hashlib
from collections.abc import Iterable
from datetime import datetime
from enum import StrEnum
from typing import Any

from nhl_edge.schemas.core import FinalPeriodType, FinalResult, GameStatus, Strict
from nhl_edge.schemas.market import Contract
from nhl_edge.timeutil import parse_iso, utcnow

ENGINE_VERSION = "nhl-settle-1.0"

SETTLEABLE_SUPPORT = frozenset({"MODELABLE", "BUILDABLE"})
SETTLEABLE_CONFIDENCE = frozenset({"high", "medium"})
COMPARATORS = frozenset({"ge", "gt", "le", "lt", "eq", "in_range"})
PUSH_ON_TIE_NOTE = "push_on_tie"
DISAGREE_PREFIX = "DISAGREES_WITH_KALSHI:"

SETTLES_FINAL = "FINAL_INCL_OT_SO"
SETTLES_REGULATION = "REGULATION"
SETTLEABLE_BASES = frozenset({SETTLES_FINAL, SETTLES_REGULATION})
FULL_GAME_PERIOD = "FULL"

WINNER_STATS = frozenset({"winner", "reg_winner"})
THRESHOLD_STATS = frozenset({"margin", "total", "team_total", "margin_bucket"})
EVENT_STATS = frozenset({"overtime", "shootout", "btts"})
GAME_STATS = WINNER_STATS | THRESHOLD_STATS | EVENT_STATS
TEAM_STATS = frozenset({"winner", "reg_winner", "margin", "team_total", "margin_bucket"})

UNSETTLEABLE_STATUSES = (GameStatus.POSTPONED, GameStatus.CANCELED, GameStatus.SUSPENDED)


class SettlementOutcome(StrEnum):
    YES = "YES"
    NO = "NO"
    VOID = "VOID"
    PUSH = "PUSH"
    UNSETTLEABLE = "UNSETTLEABLE"


class SettlementRecord(Strict):
    """Immutable settlement of one contract against one final-result version."""

    ticker: str
    game_id: str
    outcome: SettlementOutcome
    value: float | None  # realized goals / margin / total (or 1.0/0.0 for event stats); None if unsettleable
    reason: str
    settled_at_utc: datetime
    result_source: str
    stat_correction_version: int
    engine_version: str
    idempotency_key: str
    settles_on: str


# ---- keys ----------------------------------------------------------------------------------------


def semantics_fingerprint(contract: Contract | None) -> str:
    """Hash of exactly the contract fields that decide the outcome.

    Kalshi semantics are reverse-engineered, so "we parsed a threshold (or the settlement basis) wrong and fixed
    it" is a case this project must survive. Without the fingerprint the key was ticker+game+engine+correction,
    which says nothing about WHAT YES meant, and ``settle_many`` would reuse the stale record forever. Corrected
    semantics must produce a NEW record (the old one stays; the ledger is append-only), hence a different key.
    ``settles_on`` is in the hash because for NHL it is the axis that changes a winner's meaning entirely.
    """
    if contract is None:
        return "-"
    parts = (contract.scope, contract.stat, contract.period, contract.settles_on, contract.comparator,
             contract.threshold, contract.upper, contract.team_id)
    return hashlib.sha256("|".join("" if x is None else str(x) for x in parts).encode("utf-8")).hexdigest()[:16]


def idempotency_key(
    ticker: str, game_id: str, engine_version: str, stat_correction_version: int, contract: Contract | None = None
) -> str:
    raw = f"{ticker}|{game_id}|{engine_version}|{stat_correction_version}|{semantics_fingerprint(contract)}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


# ---- comparator ----------------------------------------------------------------------------------


def _apply_comparator(value: float, contract: Contract, allow_push: bool = True) -> tuple[SettlementOutcome, str]:
    """Compare ``value`` with the contract's threshold.

    Exact hits on an integer line are YES/NO per the comparator ('gt 1' at margin 1 is NO); they PUSH only when
    the contract notes explicitly carry ``push_on_tie``. Half-goal lines can never hit exactly.
    """
    cmp, t, u = contract.comparator, contract.threshold, contract.upper
    if cmp not in COMPARATORS:
        return SettlementOutcome.UNSETTLEABLE, f"unknown comparator {cmp!r}"
    if t is None:
        return SettlementOutcome.UNSETTLEABLE, "threshold missing"
    if cmp == "in_range" and u is None:
        return SettlementOutcome.UNSETTLEABLE, "upper bound missing for in_range"
    if allow_push and PUSH_ON_TIE_NOTE in contract.notes and value == t:
        return SettlementOutcome.PUSH, f"value {value:g} == threshold {t:g} (push_on_tie)"
    hit = {
        "ge": value >= t,
        "gt": value > t,
        "le": value <= t,
        "lt": value < t,
        "eq": value == t,
        "in_range": u is not None and t <= value <= u,
    }[cmp]
    desc = f"value {value:g} {cmp} {t:g}" + (f"..{u:g}" if cmp == "in_range" else "")
    return (SettlementOutcome.YES if hit else SettlementOutcome.NO), desc


# ---- scores by settlement basis ------------------------------------------------------------------


def _scores(result: FinalResult, settles_on: str) -> tuple[int, int]:
    """(home, away) goals on the contract's settlement basis. Raises KeyError when the basis is unavailable."""
    if settles_on == SETTLES_FINAL:
        if result.home_final is None or result.away_final is None:
            raise KeyError("final score missing")
        return result.home_final, result.away_final
    if settles_on == SETTLES_REGULATION:
        if result.home_reg is None or result.away_reg is None:
            raise KeyError("regulation score missing")
        return result.home_reg, result.away_reg
    raise KeyError(f"settles_on {settles_on!r} not derivable from a final result")


def _team_scores(result: FinalResult, team_id: int, settles_on: str) -> tuple[int, int]:
    """(own, opponent) goals for ``team_id`` on the settlement basis."""
    home, away = _scores(result, settles_on)
    result.opponent_of(team_id)  # KeyError if the team is not in this game
    return (home, away) if team_id == result.home_team_id else (away, home)


# ---- game scope ----------------------------------------------------------------------------------


def _settle_winner(contract: Contract, result: FinalResult) -> tuple[SettlementOutcome, float | None, str]:
    assert contract.team_id is not None
    basis = contract.settles_on
    if contract.stat == "reg_winner" and basis != SETTLES_REGULATION:
        return SettlementOutcome.UNSETTLEABLE, None, f"reg_winner contract with settles_on={basis}; contradiction"
    own, opp = _team_scores(result, contract.team_id, basis)
    margin = float(own - opp)
    label = "final incl. OT/SO" if basis == SETTLES_FINAL else "regulation"
    if own > opp:
        return SettlementOutcome.YES, margin, f"{own}-{opp} {label}"
    if own < opp:
        return SettlementOutcome.NO, margin, f"{own}-{opp} {label}"
    if basis == SETTLES_FINAL:
        # An NHL game always has a winner once OT/SO is included; a final tie is corrupt data, never a settlement.
        return SettlementOutcome.UNSETTLEABLE, None, f"final score tied {own}-{opp}: impossible for a final NHL game"
    if PUSH_ON_TIE_NOTE in contract.notes:
        return SettlementOutcome.PUSH, margin, f"regulation tie {own}-{opp} (push_on_tie)"
    return SettlementOutcome.NO, margin, f"regulation tie {own}-{opp}: no regulation winner"


def _threshold_value(contract: Contract, result: FinalResult) -> float:
    """Realized quantity for margin / total / team_total / margin_bucket on the contract's settlement basis."""
    stat, basis = contract.stat, contract.settles_on
    if stat == "total":
        home, away = _scores(result, basis)
        return float(home + away)
    if contract.team_id is None:
        raise KeyError("team_id missing")
    own, opp = _team_scores(result, contract.team_id, basis)
    if stat == "team_total":
        return float(own)
    return float(own - opp)  # margin, margin_bucket


def _event_value(contract: Contract, result: FinalResult) -> float:
    stat = contract.stat
    if stat == "overtime":
        return float(result.went_to_overtime)
    if stat == "shootout":
        return float(result.went_to_shootout)
    home, away = _scores(result, contract.settles_on)  # btts
    return float(home > 0 and away > 0)


def _settle_event(contract: Contract, result: FinalResult) -> tuple[SettlementOutcome, float | None, str]:
    if contract.stat in ("overtime", "shootout") and contract.settles_on != SETTLES_FINAL:
        return (SettlementOutcome.UNSETTLEABLE, None,
                f"{contract.stat} contract with settles_on={contract.settles_on}; OT/SO markets settle on the final result")
    value = _event_value(contract, result)
    happened = value == 1.0
    desc = f"{contract.stat} {'happened' if happened else 'did not happen'} (last period {result.last_period_type})"
    if contract.comparator is None:
        return (SettlementOutcome.YES if happened else SettlementOutcome.NO), value, desc
    # the contract builder expresses yes/no event markets as 'ge 1.0'; honour whatever comparator was parsed
    outcome, cdesc = _apply_comparator(value, contract, allow_push=False)
    return outcome, value, f"{desc}; {cdesc}"


def _settle_game(contract: Contract, result: FinalResult) -> tuple[SettlementOutcome, float | None, str]:
    stat = contract.stat
    if stat not in GAME_STATS:
        return SettlementOutcome.UNSETTLEABLE, None, f"unsupported game stat {stat!r}"
    if stat in TEAM_STATS and contract.team_id is None:
        return SettlementOutcome.UNSETTLEABLE, None, f"team_id missing for {stat} ({contract.settles_on})"
    try:
        if stat in WINNER_STATS:
            return _settle_winner(contract, result)
        if stat in EVENT_STATS:
            return _settle_event(contract, result)
        value = _threshold_value(contract, result)
    except KeyError as e:
        return SettlementOutcome.UNSETTLEABLE, None, f"scores unavailable: {e.args[0] if e.args else e}"
    except ValueError as e:
        return SettlementOutcome.UNSETTLEABLE, None, str(e)
    outcome, desc = _apply_comparator(value, contract)
    return outcome, value, f"{stat} {contract.settles_on}: {desc}"


# ---- Kalshi reconciliation -----------------------------------------------------------------------

# Kalshi's own settlement vocabulary. "scalar" means the market settled to a value rather than to a side (the way
# Kalshi resolves markets it did not void outright but could not settle binary). VOID here means "did not resolve
# to a side"; it does NOT mean the stake was returned.
_KALSHI_RESULTS = {
    "yes": SettlementOutcome.YES,
    "no": SettlementOutcome.NO,
    "void": SettlementOutcome.VOID,
    "scalar": SettlementOutcome.VOID,
}


def _kalshi_outcome(kalshi_result: str | None) -> SettlementOutcome | None:
    if kalshi_result is None:
        return None
    return _KALSHI_RESULTS.get(kalshi_result.strip().lower())


def _reconcile_with_kalshi(
    outcome: SettlementOutcome, reason: str, kalshi_result: str | None
) -> tuple[SettlementOutcome, str]:
    """Never override our outcome; annotate the reason with any disagreement."""
    if kalshi_result is None:
        return outcome, reason
    if outcome == SettlementOutcome.UNSETTLEABLE:
        return outcome, f"{reason}; kalshi_result={kalshi_result}"
    k = _kalshi_outcome(kalshi_result)
    if k is None:
        return outcome, f"{reason}; kalshi_result={kalshi_result} (unrecognised)"
    if k != outcome:
        return outcome, f"{DISAGREE_PREFIX} ours={outcome.value} kalshi={k.value}; {reason}"
    return outcome, f"{reason}; agrees with Kalshi"


# ---- gates ---------------------------------------------------------------------------------------


def _gate(contract: Contract, result: FinalResult) -> str | None:
    """Return a reason the contract cannot be settled from this result, or None if settlement may proceed."""
    if result.status in UNSETTLEABLE_STATUSES:
        return f"game {result.status.value}: Kalshi decides void"
    if result.status != GameStatus.FINAL or not result.is_final:
        return f"game not final (status={result.status.value})"
    if contract.game_id is not None and contract.game_id != result.game_id:
        return f"game_id mismatch (contract {contract.game_id}, result {result.game_id})"
    if contract.support not in SETTLEABLE_SUPPORT or contract.semantics_confidence not in SETTLEABLE_CONFIDENCE:
        return f"semantics not proven (support={contract.support}, confidence={contract.semantics_confidence})"
    if contract.scope != "game":
        return f"unsupported scope {contract.scope!r}: only game-scope contracts settle from a final result"
    if contract.settles_on not in SETTLEABLE_BASES:
        return f"unsupported settles_on {contract.settles_on!r}: not derivable from a final result"
    if contract.period != FULL_GAME_PERIOD:
        return f"unsupported period {contract.period!r}: a final result carries no period scores"
    game_teams = {result.home_team_id, result.away_team_id}
    if contract.team_id is not None and contract.team_id not in game_teams:
        return f"team {contract.team_id} not in game {result.game_id} ({sorted(game_teams)})"
    if contract.opponent_team_id is not None and contract.opponent_team_id not in game_teams:
        return f"opponent {contract.opponent_team_id} not in game {result.game_id} ({sorted(game_teams)})"
    if contract.game_team_ids and set(contract.game_team_ids) != game_teams:
        return f"contract teams {sorted(contract.game_team_ids)} != game teams {sorted(game_teams)}"
    return None


# ---- public API ----------------------------------------------------------------------------------


def settle_contract(
    contract: Contract, result: FinalResult, kalshi_result: str | None = None, now: datetime | None = None
) -> SettlementRecord:
    """Settle one contract against one final result. Never raises for data problems: returns UNSETTLEABLE."""
    gate_reason = _gate(contract, result)
    if gate_reason is not None:
        outcome, value, reason = SettlementOutcome.UNSETTLEABLE, None, gate_reason
    else:
        outcome, value, reason = _settle_game(contract, result)
    outcome, reason = _reconcile_with_kalshi(outcome, reason, kalshi_result)
    if result.stat_correction_version > 0:
        reason = f"{reason} [stat correction v{result.stat_correction_version}]"
    return SettlementRecord(
        ticker=contract.ticker,
        game_id=result.game_id,
        outcome=outcome,
        value=value,
        reason=reason,
        settled_at_utc=now or utcnow(),
        result_source=result.source,
        stat_correction_version=result.stat_correction_version,
        engine_version=ENGINE_VERSION,
        idempotency_key=idempotency_key(contract.ticker, result.game_id, ENGINE_VERSION, result.stat_correction_version, contract),
        settles_on=contract.settles_on,
    )


def settle_many(
    contracts: Iterable[Contract],
    result: FinalResult,
    existing: dict[str, SettlementRecord],
    kalshi_results: dict[str, str] | None = None,
    now: datetime | None = None,
) -> list[SettlementRecord]:
    """Settle many contracts idempotently.

    ``existing`` maps idempotency_key -> record already persisted. A contract whose key is present returns the
    existing record unchanged. A result with a higher ``stat_correction_version`` yields a new key, hence a new
    record (append-only history); callers must never delete the earlier record.
    """
    kalshi_results = kalshi_results or {}
    out: list[SettlementRecord] = []
    for c in contracts:
        key = idempotency_key(c.ticker, result.game_id, ENGINE_VERSION, result.stat_correction_version, c)
        prior = existing.get(key)
        out.append(prior if prior is not None else settle_contract(c, result, kalshi_results.get(c.ticker), now=now))
    return out


# ---- boxscore -> FinalResult ---------------------------------------------------------------------


def _starter_id(goalies: Any) -> int | None:
    for g in goalies or []:
        if isinstance(g, dict) and g.get("starter") and g.get("player_id") is not None:
            return int(g["player_id"])
    return None


def _status(v: Any) -> GameStatus:
    if isinstance(v, GameStatus):
        return v
    try:
        return GameStatus(str(v))
    except ValueError:
        return GameStatus.UNKNOWN


def _period_type(v: Any) -> FinalPeriodType | None:
    if v is None:
        return None
    if isinstance(v, FinalPeriodType):
        return v
    s = str(v).upper()
    return FinalPeriodType(s) if s in ("REG", "OT", "SO") else None


def final_result_from_boxscore(
    box: dict[str, Any],
    source: str = "nhl_api_boxscore",
    fetched_at_utc: datetime | str | None = None,
    stat_correction_version: int = 0,
) -> FinalResult:
    """Build a ``FinalResult`` from the dict returned by :func:`nhl_edge.data.nhl_api.parse_boxscore`.

    Raises ``ValueError`` when the box does not identify the game or both clubs: a result with unknown teams
    could settle nothing, so it must not exist. Missing scores are allowed (the result is simply not ``is_final``).
    """
    gid = box.get("game_id")
    home_id, away_id = box.get("home_team_id"), box.get("away_team_id")
    if gid in (None, "", "None"):
        raise ValueError("boxscore has no game_id")
    if home_id is None or away_id is None:
        raise ValueError(f"boxscore {gid} does not identify both clubs (home={home_id}, away={away_id})")
    fetched = parse_iso(fetched_at_utc) if isinstance(fetched_at_utc, str) else fetched_at_utc
    return FinalResult(
        game_id=str(gid),
        status=_status(box.get("status")),
        home_team_id=int(home_id),
        away_team_id=int(away_id),
        home_final=box.get("home_score"),
        away_final=box.get("away_score"),
        home_reg=box.get("home_reg_score"),
        away_reg=box.get("away_reg_score"),
        last_period_type=_period_type(box.get("last_period_type")),
        source=source,
        fetched_at_utc=fetched,
        stat_correction_version=stat_correction_version,
        home_starting_goalie_id=_starter_id(box.get("home_goalies")),
        away_starting_goalie_id=_starter_id(box.get("away_goalies")),
    )
