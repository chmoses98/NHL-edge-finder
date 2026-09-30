"""Player-prop settlement from the official NHL record (PLAYER_SIM_V1 evaluation; RESEARCH_ONLY).

Rule text (every KXNHLGOAL / KXNHLAST / KXNHLPTS / KXNHLSAVE / KXNHLFIRSTGOAL market, 2026-09-29):
  primary   "If <player> records N+ goals|assists|points|saves in the <A> vs <B> NHL game originally scheduled for <date>,
            then the market resolves to Yes."  /  "If <player> scores the 1st goal in ..."
  secondary "If a player is active but never enters the game, the market settles to the last fair market price before
            game start. Once a player enters the game, the market settles based on the player's <stat> recorded."
  source    NHL (https://www.nhl.com)

Mapping (engine ``nhl-player-settle-1.0``):
* the official boxscore line decides goals, assists, points (= goals + assists) and a goalie's saves; OT counts, the
  shootout does not (the boxscore already excludes it);
* the player is NOT in the boxscore (scratched / not dressed) or dressed with 00:00 ice time (never entered) ->
  UNSETTLEABLE ("fair price" is Kalshi's call; we never invent it);
* first goal: the scorer of the first non-shootout goal in the official play-by-play; a game with no goal before the
  shootout -> UNSETTLEABLE (the rules do not say what happens; Kalshi's result is recorded next to it);
* the game must be FINAL; postponed / suspended -> UNSETTLEABLE;
* Kalshi's own result is compared, never allowed to override; disagreement is flagged ``DISAGREES_WITH_KALSHI:``.
Stat corrections: the record carries the boxscore fetch time; a later corrected boxscore appends a new record version.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

import pandas as pd

from nhl_edge.players.identity import parse_player_market
from nhl_edge.players.pricing import PLAYER_FAMILIES
from nhl_edge.schemas.market import Contract
from nhl_edge.settlement.engine import (
    DISAGREE_PREFIX,
    SettlementOutcome,
    SettlementRecord,
    _kalshi_outcome,
    idempotency_key,
)

PLAYER_ENGINE_VERSION = "nhl-player-settle-1.0"


def _match(ref: Any, rows: pd.DataFrame) -> tuple[pd.Series | None, str]:
    from nhl_edge.data.lines import fold

    if ref is None or ref.team_id is None:
        return None, "ticker did not parse to a team + player"
    t = rows[rows["team_id"] == ref.team_id]
    frag = fold(ref.last_fragment)
    full_last = fold(ref.name.split(" ", 1)[1]) if ref.name and " " in ref.name else None

    def ok(nm: Any) -> bool:
        # boxscore names are "F. Lastname" (or "J.T. Miller" style)
        s = str(nm or "")
        parts = s.split(" ", 1)
        last = fold(parts[1]) if len(parts) > 1 else fold(s)
        init = fold(parts[0])[:1] if len(parts) > 1 else ""
        name_ok = (last.startswith(frag) or frag.startswith(last)) and (full_last is None or last == full_last or full_last.startswith(last) or last.startswith(full_last))
        return name_ok and (not ref.initial or not init or init == ref.initial.lower())

    hit = t[(t["sweater"] == ref.jersey) & t["name"].map(ok)]
    if len(hit) == 1:
        return hit.iloc[0], "team+jersey+name"
    hit = t[t["name"].map(ok)]
    if len(hit) == 1:
        return hit.iloc[0], "team+name"
    return None, "not in the official boxscore (did not dress) or ambiguous"


def settle_player_contract(c: Contract, skaters: pd.DataFrame, goalies: pd.DataFrame, goals: pd.DataFrame, final: bool, kalshi_result: str | None,
                           now: datetime, source: str, correction: int = 0) -> SettlementRecord:
    stat = PLAYER_FAMILIES.get(c.family)
    gid = c.game_id or ""

    def rec(outcome: SettlementOutcome, value: float | None, reason: str) -> SettlementRecord:
        k = _kalshi_outcome(kalshi_result)
        if k is not None and outcome in (SettlementOutcome.YES, SettlementOutcome.NO) and k != outcome:
            reason = f"{DISAGREE_PREFIX} kalshi={kalshi_result}; ours={outcome.value}; {reason}"
        elif kalshi_result:
            reason = f"{reason}; kalshi={kalshi_result}"
        return SettlementRecord(ticker=c.ticker, game_id=gid, outcome=outcome, value=value, reason=reason[:400], settled_at_utc=now, result_source=source,
                                stat_correction_version=correction, engine_version=PLAYER_ENGINE_VERSION,
                                idempotency_key=idempotency_key(c.ticker, gid, PLAYER_ENGINE_VERSION, correction, c), settles_on="PLAYER_OFFICIAL_STAT")

    if stat is None:
        return rec(SettlementOutcome.UNSETTLEABLE, None, f"family {c.family} is not a player family")
    if not final:
        return rec(SettlementOutcome.UNSETTLEABLE, None, "game not final")
    ref = parse_player_market(c.ticker, c.title)
    if stat == "saves":
        row, how = _match(ref, goalies)
        if row is None:
            return rec(SettlementOutcome.UNSETTLEABLE, None, f"goalie {how}")
        if not row.get("toi_s"):
            return rec(SettlementOutcome.UNSETTLEABLE, None, "goalie dressed but never entered: Kalshi settles at the pre-game fair price")
        value = float(row["saves"])
    else:
        row, how = _match(ref, skaters)
        if row is None:
            return rec(SettlementOutcome.UNSETTLEABLE, None, f"player {how}")
        if not row.get("toi_s"):
            return rec(SettlementOutcome.UNSETTLEABLE, None, "player dressed but never entered: Kalshi settles at the pre-game fair price")
        if stat == "first_goal":
            g = goals.sort_values(["period", "t_s"]) if len(goals) else goals
            if not len(g):
                return rec(SettlementOutcome.UNSETTLEABLE, None, "no goal before the shootout: first-goal rule does not cover it")
            first = int(g.iloc[0]["scorer_id"])
            value = 1.0 if first == int(row["player_id"]) else 0.0
            return rec(SettlementOutcome.YES if value else SettlementOutcome.NO, value, f"first goal scorer {first} ({how})")
        value = float(row[stat])
    if c.threshold is None or c.comparator not in ("gt", "ge"):
        return rec(SettlementOutcome.UNSETTLEABLE, value, f"unrecognised threshold {c.comparator} {c.threshold}")
    yes = value > c.threshold if c.comparator == "gt" else value >= c.threshold
    return rec(SettlementOutcome.YES if yes else SettlementOutcome.NO, value, f"{stat}={value:g} {c.comparator} {c.threshold:g} ({how})")
