"""Period-market settlement from official play-by-play goals (``nhl-period-settle-1.0``; RESEARCH_ONLY).

Rule text (reviewed 2026-09-29, docs/KALSHI_MARKET_MAP.md):
  KXNHL1P/2P/3P -<TEAM>  "If <team> wins the Nth period"; "Only goals scored during the Nth period count";
                         3rd period "(excluding overtime)"
  KXNHL1P/2P/3P -TIE     "If neither team wins the Nth period"
  KXNHL{N}PSPREAD        "If <team> wins by more than x goals in the Nth period"
  KXNHL{N}PTOTAL         "If the teams collectively score more than x goals in the Nth Period"

Period goals are counted from the official play-by-play goal events of periods 1-3 (the shootout and OT never count).
The per-game consistency check (play-by-play goals == official boxscore goals for every player and team) must be clean,
otherwise the contract is UNSETTLEABLE. Postponed / not-final games are UNSETTLEABLE. Kalshi's own result is recorded and
never overrides ours; a disagreement is flagged.
"""

from __future__ import annotations

from datetime import datetime

import pandas as pd

from nhl_edge.schemas.market import Contract
from nhl_edge.settlement.engine import (
    DISAGREE_PREFIX,
    SettlementOutcome,
    SettlementRecord,
    _kalshi_outcome,
    idempotency_key,
)

PERIOD_ENGINE_VERSION = "nhl-period-settle-1.0"
PERIOD_FAMILIES = ("period_winner", "period_spread", "period_total")


def settle_period_contract(c: Contract, goals: pd.DataFrame, home_id: int, away_id: int, final: bool, consistent: bool, kalshi_result: str | None,
                           now: datetime, correction: int = 0) -> SettlementRecord:
    gid = c.game_id or ""

    def rec(outcome: SettlementOutcome, value: float | None, reason: str) -> SettlementRecord:
        k = _kalshi_outcome(kalshi_result)
        if k is not None and outcome in (SettlementOutcome.YES, SettlementOutcome.NO) and k != outcome:
            reason = f"{DISAGREE_PREFIX} kalshi={kalshi_result}; ours={outcome.value}; {reason}"
        elif kalshi_result:
            reason = f"{reason}; kalshi={kalshi_result}"
        return SettlementRecord(ticker=c.ticker, game_id=gid, outcome=outcome, value=value, reason=reason[:400], settled_at_utc=now, result_source="nhl_pbp",
                                stat_correction_version=correction, engine_version=PERIOD_ENGINE_VERSION,
                                idempotency_key=idempotency_key(c.ticker, gid, PERIOD_ENGINE_VERSION, correction, c), settles_on="PERIOD")

    q = {"P1": 1, "P2": 2, "P3": 3}.get(str(c.period or "").upper())
    if c.family not in PERIOD_FAMILIES or q is None:
        return rec(SettlementOutcome.UNSETTLEABLE, None, f"not a period contract ({c.family} {c.period})")
    if not final:
        return rec(SettlementOutcome.UNSETTLEABLE, None, "game not final")
    if not consistent:
        return rec(SettlementOutcome.UNSETTLEABLE, None, "play-by-play goals do not reconcile with the official boxscore")
    g = goals[goals["period"] == q] if len(goals) else goals
    hg = int((g["team_id"] == home_id).sum()) if len(g) else 0
    ag = int((g["team_id"] == away_id).sum()) if len(g) else 0
    if c.family == "period_total":
        if c.threshold is None or c.comparator not in ("gt", "ge"):
            return rec(SettlementOutcome.UNSETTLEABLE, None, "period total without a threshold")
        v = hg + ag
        yes = v > c.threshold if c.comparator == "gt" else v >= c.threshold
        return rec(SettlementOutcome.YES if yes else SettlementOutcome.NO, float(v), f"P{q} goals {hg}+{ag}={v} vs {c.comparator} {c.threshold:g}")
    if c.family == "period_winner" and c.team_id is None:
        if not c.ticker.upper().endswith("-TIE"):
            return rec(SettlementOutcome.UNSETTLEABLE, None, "period winner without a team and not a TIE market")
        return rec(SettlementOutcome.YES if hg == ag else SettlementOutcome.NO, float(hg - ag), f"P{q} {hg}-{ag} (TIE market)")
    if c.team_id not in (home_id, away_id):
        return rec(SettlementOutcome.UNSETTLEABLE, None, "contract team is not in this game")
    margin = (hg - ag) if c.team_id == home_id else (ag - hg)
    if c.family == "period_winner":
        return rec(SettlementOutcome.YES if margin > 0 else SettlementOutcome.NO, float(margin), f"P{q} margin {margin:+d}")
    if c.threshold is None or c.comparator not in ("gt", "ge"):
        return rec(SettlementOutcome.UNSETTLEABLE, None, "period spread without a threshold")
    yes = margin > c.threshold if c.comparator == "gt" else margin >= c.threshold
    return rec(SettlementOutcome.YES if yes else SettlementOutcome.NO, float(margin), f"P{q} margin {margin:+d} vs {c.comparator} {c.threshold:g}")
