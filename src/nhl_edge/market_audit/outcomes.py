"""Deterministic outcome resolver, written independently of ``nhl_edge.settlement`` so the two can be reconciled.

``resolve(spec, facts, player_ref)`` is a pure function: same inputs, same output, no clock, no network, no randomness.
It never guesses: anything the contract text or the data cannot decide returns an explicit non-YES/NO outcome.

Outcomes
    YES / NO            decided
    VOID_FAIR_PRICE     the contract's own rule voids it to a fair price (player active but never enters the game)
    NOT_FINAL           the game has no archived official final
    DATA_INCONSISTENT   official final / play-by-play / boxscore do not reconcile for this game
    PLAYER_UNMATCHED    contract player is ambiguous, or found only outside the named team (stale identity): not settled
    PLAYER_NOT_IN_BOXSCORE  the named player is on neither club's boxscore (not dressed). The contract text only voids a
                        player who is "active but never enters"; a scratch is NOT stated, so it is held out, never scored
    RULE_SILENT         the contract text does not cover this situation (e.g. first goal when no goal is scored)
    UNRESOLVED_SPEC     the spec itself was not PROVEN

Shootout convention (stated by the contracts' own rules): a shootout decides the game by exactly one goal for
winner/spread/total/team-total markets; it never counts for periods, early-goal or player stat lines.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from typing import Any

from nhl_edge.market_audit.taxonomy import PROVEN, ContractSpec

YES, NO = "YES", "NO"
VOID, NOT_FINAL, INCONSISTENT = "VOID_FAIR_PRICE", "NOT_FINAL", "DATA_INCONSISTENT"
UNMATCHED, SILENT, BAD_SPEC = "PLAYER_UNMATCHED", "RULE_SILENT", "UNRESOLVED_SPEC"
NOT_IN_BOX = "PLAYER_NOT_IN_BOXSCORE"
DECIDED = (YES, NO)


@dataclass
class GameFacts:
    game_id: str
    home_id: int
    away_id: int
    is_final: bool
    home_final: int | None
    away_final: int | None
    home_reg: int | None
    away_reg: int | None
    last_period_type: str | None  # REG | OT | SO
    goals: list[dict[str, Any]] = field(default_factory=list)  # period, t_s, team_id, scorer_id
    skaters: list[dict[str, Any]] = field(default_factory=list)  # player_id, team_id, name, sweater, goals, assists, points, toi_s
    goalies: list[dict[str, Any]] = field(default_factory=list)  # player_id, team_id, name, sweater, saves, toi_s
    have_player_events: bool = True

    def problems(self) -> list[str]:
        """Reconciliation of three independent sources: official final, play-by-play goals, boxscore lines."""
        out: list[str] = []
        if not self.is_final:
            return ["not final"]
        if None in (self.home_final, self.away_final, self.home_reg, self.away_reg):
            return ["official final incomplete"]
        so = self.last_period_type == "SO"
        for tid, fin, reg in ((self.home_id, self.home_final, self.home_reg), (self.away_id, self.away_final, self.away_reg)):
            ev_all = sum(1 for g in self.goals if g["team_id"] == tid)
            ev_reg = sum(1 for g in self.goals if g["team_id"] == tid and g["period"] <= 3)
            if ev_reg != reg:
                out.append(f"team {tid}: play-by-play regulation goals {ev_reg} != official regulation {reg}")
            expected_final_no_so = fin - (1 if so and fin > (self.away_final if tid == self.home_id else self.home_final) else 0)
            if ev_all != expected_final_no_so:
                out.append(f"team {tid}: play-by-play goals {ev_all} != official final {fin} less shootout credit")
            gids = {g["player_id"] for g in self.goalies if g["team_id"] == tid}
            sk = sum(int(s["goals"]) for s in self.skaters if s["team_id"] == tid)
            sk += sum(1 for g in self.goals if g["team_id"] == tid and g["scorer_id"] in gids)  # a goalie can score (empty net)
            if self.skaters and sk != ev_all:
                out.append(f"team {tid}: boxscore skater goals {sk} != play-by-play {ev_all}")
        if (self.last_period_type == "REG") != (self.home_final == self.home_reg and self.away_final == self.away_reg):
            out.append("last_period_type disagrees with regulation-vs-final scores")
        return out


@dataclass(frozen=True)
class Resolution:
    outcome: str
    value: float | None
    reason: str


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z ]", "", s.replace("-", " ").replace("'", "")).strip()


_SUFFIX = {"jr", "sr", "ii", "iii", "iv"}


def _name_tokens(full: str) -> list[str]:
    return [t for t in _norm(full).split() if t not in _SUFFIX]


def names_match(contract_name: str, box_name: str) -> bool:
    """Contract names are full ('Charles Alexis Legault', 'Alex DeBrincat'); boxscore names are 'C. Legault'.
    Match = same first initial AND the boxscore surname equals some trailing run of the contract name's tokens."""
    ct, bt = _name_tokens(contract_name), _name_tokens(box_name)
    if len(ct) < 2 or len(bt) < 2:
        return False
    if ct[0][0] != bt[0][0]:
        return False
    box_last = "".join(bt[1:])
    return any("".join(ct[i:]) == box_last for i in range(1, len(ct)))


def _ticker_jersey(ticker: str) -> int | None:
    suffix = ticker.split("-")[2] if ticker.count("-") >= 2 else ""
    m = re.search(r"(\d+)$", suffix)
    return int(m[1]) if m else None


def match_player(spec: ContractSpec, ticker: str, team_id: int | None, rows: list[dict[str, Any]]) -> tuple[dict[str, Any] | None, str]:
    """Prove a contract's player is ONE boxscore player: team + (first initial, last name); jersey breaks ties only."""
    if not spec.player_name:
        return None, "no player name on contract"
    pool = [r for r in rows if team_id is None or r["team_id"] == team_id]
    hits = [r for r in pool if names_match(spec.player_name, str(r.get("name") or ""))]
    if len(hits) == 1:
        j = _ticker_jersey(ticker)
        note = "name" + ("+jersey" if j == hits[0].get("sweater") else " (jersey differs: stale Kalshi jersey)")
        return hits[0], note
    if len(hits) > 1:
        j = _ticker_jersey(ticker)
        by_j = [h for h in hits if h.get("sweater") == j]
        if len(by_j) == 1:
            return by_j[0], "name+jersey tie-break"
        return None, "ambiguous: several boxscore players share first initial + last name"
    return None, "no boxscore player with that first initial + last name on the team"


def _scores(facts: GameFacts, spec: ContractSpec) -> tuple[int, int] | None:
    """(subject_goals, opponent_goals) on the official final (shootout credited as one goal)."""
    if spec.subject_team_id is None:
        return None
    if spec.subject_team_id == facts.home_id:
        return int(facts.home_final), int(facts.away_final)  # type: ignore[arg-type]
    if spec.subject_team_id == facts.away_id:
        return int(facts.away_final), int(facts.home_final)  # type: ignore[arg-type]
    return None


def _period_goals(facts: GameFacts, q: int) -> tuple[int, int]:
    h = sum(1 for g in facts.goals if g["period"] == q and g["team_id"] == facts.home_id)
    a = sum(1 for g in facts.goals if g["period"] == q and g["team_id"] == facts.away_id)
    return h, a


def resolve(spec: ContractSpec, facts: GameFacts | None, team_for_player: int | None = None) -> Resolution:
    if spec.semantics_status != PROVEN:
        return Resolution(BAD_SPEC, None, spec.issues[0] if spec.issues else "spec not proven")
    if facts is None or not facts.is_final:
        return Resolution(NOT_FINAL, None, "no archived official final")
    kind, thr = spec.kind, spec.threshold

    # ---- full-game markets: need the official final only --------------------------------------------------
    if kind in ("winner", "spread", "total", "team_total", "overtime"):
        if None in (facts.home_final, facts.away_final) or facts.last_period_type not in ("REG", "OT", "SO"):
            return Resolution(INCONSISTENT, None, "official final incomplete")
        hf, af = int(facts.home_final), int(facts.away_final)  # type: ignore[arg-type]
        if hf == af:
            return Resolution(INCONSISTENT, None, "official final is tied")
        if kind == "overtime":
            return Resolution(YES if facts.last_period_type in ("OT", "SO") else NO, float(facts.last_period_type != "REG"), "overtime period played")
        if kind == "total":
            tot = hf + af  # shootout winner already carries the +1 on the official final
            return Resolution(YES if tot > thr else NO, float(tot), "official final total incl OT/SO credit")  # type: ignore[operator]
        sc = _scores(facts, spec)
        if sc is None:
            return Resolution(BAD_SPEC, None, "subject team not in this game")
        mine, theirs = sc
        if kind == "winner":
            return Resolution(YES if mine > theirs else NO, float(mine - theirs), "official final winner")
        if kind == "spread":
            return Resolution(YES if (mine - theirs) > thr else NO, float(mine - theirs), "official final margin")  # type: ignore[operator]
        return Resolution(YES if mine > thr else NO, float(mine), "official final team goals incl OT/SO credit")  # type: ignore[operator]

    # ---- everything else needs reconciled play-by-play / boxscore ------------------------------------------------
    if not facts.have_player_events:
        return Resolution(INCONSISTENT, None, "no archived player-event partition for this game")
    probs = facts.problems()
    if probs:
        return Resolution(INCONSISTENT, None, "; ".join(probs)[:200])

    if kind in ("period_winner", "period_spread", "period_total"):
        q = {"P1": 1, "P2": 2, "P3": 3}[spec.period]
        h, a = _period_goals(facts, q)  # periods 1-3 only: OT/SO never count
        if kind == "period_total":
            return Resolution(YES if (h + a) > thr else NO, float(h + a), f"period {q} goals")  # type: ignore[operator]
        if spec.is_tie_leg:
            return Resolution(YES if h == a else NO, float(h - a), f"period {q} tie")
        mine, theirs = (h, a) if spec.subject_team_id == facts.home_id else (a, h)
        if kind == "period_winner":
            return Resolution(YES if mine > theirs else NO, float(mine - theirs), f"period {q} winner")
        return Resolution(YES if (mine - theirs) > thr else NO, float(mine - theirs), f"period {q} margin")  # type: ignore[operator]

    if kind == "early_goal":
        n = sum(1 for g in facts.goals if g["period"] == 1 and g["t_s"] < 600)
        return Resolution(YES if n >= 1 else NO, float(n), "goals in first 10:00 of P1, 10:00 excluded")

    if kind in ("first_goal", "player_stat"):
        pool = facts.goalies if spec.stat == "saves" else facts.skaters
        row, how = match_player(spec, spec.ticker, team_for_player, pool)
        if row is None:
            if kind == "first_goal":  # first-goal markets name skaters; a goalie scorer is vanishingly rare, but check
                row, how = match_player(spec, spec.ticker, team_for_player, facts.goalies)
            if row is None:
                anywhere = [r for r in facts.skaters + facts.goalies if names_match(spec.player_name or "", str(r.get("name") or ""))]
                if not anywhere and how.startswith("no boxscore player"):
                    return Resolution(NOT_IN_BOX, None, "named player is on neither club's boxscore (not dressed); void basis not stated")
                return Resolution(UNMATCHED, None, how)
        if float(row.get("toi_s") or 0) <= 0:
            return Resolution(VOID, None, "player in boxscore with no ice time: market voids to fair price")
        if kind == "first_goal":
            if not facts.goals:
                return Resolution(SILENT, None, "no goal before the shootout: first-goal rule does not cover it")
            first = min(facts.goals, key=lambda g: (g["period"], g["t_s"]))
            return Resolution(YES if int(first["scorer_id"]) == int(row["player_id"]) else NO, None, "first goal scorer")
        val = float(row[{"goals": "goals", "assists": "assists", "points": "points", "saves": "saves"}[spec.stat]])  # type: ignore[index]
        return Resolution(YES if val > thr else NO, val, f"official {spec.stat}")  # type: ignore[operator]

    return Resolution(BAD_SPEC, None, f"no resolver for kind {kind}")
