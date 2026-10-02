"""Expression fidelity: how directly a contract cashes when its thesis happens (RESEARCH_ONLY decision-layer metric).

A +EV contract can still be a poor EXPRESSION of the idea behind it. "UTA offense succeeds (4+ goals)" happening says
little about whether one named Utah forward scores; a UTA team-total over 3.5 settles from the thesis itself. This
module makes that difference explicit from quantities the engine already computes on the joint draw:

    thesis_capture   = P(bet | thesis)                      how often the bet cashes when the thesis is right
    p_bet_not_thesis = P(bet | not thesis)
    thesis_lift      = P(bet | thesis) - P(bet | not thesis)  how much the thesis actually moves the bet
    tracking         = P(bet | thesis) * P(not bet | not thesis)   1.0 only for a contract equivalent to the thesis
    relation         = EQUIVALENT | IMPLIED_BY_THESIS (thesis => bet on every draw: the bet settles from the thesis
                       itself) | IMPLIES_THESIS (bet => thesis: a narrower version, e.g. "wins by 3+" for "wins") |
                       CORRELATED (neither contains the other)
    contract_scope   = GAME | TEAM | PLAYER | GOALIE | PERIOD | OTHER (from the contract family); GAME/TEAM are
                       "broad" expressions, PLAYER/GOALIE "fragile" single-player expressions

Classification (``fidelity_class``), with cut points fixed BEFORE any prospective profitability was examined and taken
from logic, not from data:

    STRUCTURAL  relation EQUIVALENT or IMPLIED_BY_THESIS: when the thesis is right the bet cannot lose
    DIRECT      thesis_capture >= 0.50: when the thesis is right the bet is more likely than not to cash
    FRAGILE     thesis_capture <  0.50: when the thesis is right the bet still usually LOSES
    NONE        no thesis (diffuse script dependence)

0.50 is the "more likely than not" boundary, not a fitted value; the classes are ordinal (STRUCTURAL > DIRECT >
FRAGILE > NONE) and are used only for (a) the expression preference when two expressions of one thesis have similar
adjusted value (``thesis.engine.prefer_expressions``) and (b) reporting. They never change a model probability.

Containment is tested on the integer draw counts with zero tolerance (``n_bet_and_thesis == n_thesis``); on 10,000
draws a containment that is not logical can only appear for extremely rare theses, which is why the contract scope is
reported next to it.
"""

from __future__ import annotations

from typing import Any

STRUCTURAL = "STRUCTURAL"
DIRECT = "DIRECT"
FRAGILE = "FRAGILE"
NONE = "NONE"
CLASS_RANK = {STRUCTURAL: 3, DIRECT: 2, FRAGILE: 1, NONE: 0}
DIRECT_MIN_CAPTURE = 0.50

SCOPE_BY_FAMILY = {
    "game_winner": "GAME", "game_total": "GAME", "game_spread": "GAME", "game_overtime": "GAME", "game_early_goal": "GAME",
    "team_total": "TEAM",
    "player_goals": "PLAYER", "player_assists": "PLAYER", "player_points": "PLAYER", "first_goal": "PLAYER",
    "goalie_saves": "GOALIE",
    "period_winner": "PERIOD", "period_spread": "PERIOD", "period_total": "PERIOD",
}
BROAD_SCOPES = ("GAME", "TEAM")
PLAYER_PROP_FAMILIES = ("player_goals", "player_assists", "player_points", "first_goal", "goalie_saves")


def contract_scope(family: str) -> str:
    return SCOPE_BY_FAMILY.get(family, "OTHER")


def is_player_prop(family: str) -> bool:
    return family in PLAYER_PROP_FAMILIES


def expression_kind(family: str) -> str:
    sc = contract_scope(family)
    return "BROAD" if sc in BROAD_SCOPES else "FRAGILE_PLAYER" if sc in ("PLAYER", "GOALIE") else "OTHER"


def relation(n_bet: int, n_thesis: int, n_both: int) -> str:
    if n_thesis <= 0 or n_bet <= 0:
        return "CORRELATED"
    thesis_implies_bet = n_both == n_thesis
    bet_implies_thesis = n_both == n_bet
    if thesis_implies_bet and bet_implies_thesis:
        return "EQUIVALENT"
    if thesis_implies_bet:
        return "IMPLIED_BY_THESIS"
    if bet_implies_thesis:
        return "IMPLIES_THESIS"
    return "CORRELATED"


def classify(capture: float | None, rel: str | None) -> str:
    if capture is None:
        return NONE
    if rel in ("EQUIVALENT", "IMPLIED_BY_THESIS"):
        return STRUCTURAL
    return DIRECT if capture >= DIRECT_MIN_CAPTURE else FRAGILE


def fidelity(n: int, n_bet: int, n_thesis: int, n_both: int, family: str, thesis_key: str | None) -> dict[str, Any]:
    """Fidelity of one bet side to one thesis event, from integer draw counts (n = number of draws)."""
    if thesis_key is None or thesis_key == "DIFFUSE" or n_thesis <= 0 or n <= 0:
        return {"thesis": thesis_key, "fidelity_class": NONE, "contract_scope": contract_scope(family), "expression_kind": expression_kind(family),
                "thesis_capture": None, "p_bet_given_thesis": None, "p_bet_given_not_thesis": None, "thesis_lift": None, "tracking": None, "relation": None,
                "note": "no thesis: diffuse dependence on the game script"}
    cap = n_both / n_thesis
    nt = n - n_thesis
    pnot = (n_bet - n_both) / nt if nt > 0 else None
    rel = relation(n_bet, n_thesis, n_both)
    cls = classify(cap, rel)
    track = cap * (1.0 - pnot) if pnot is not None else None
    return {"thesis": thesis_key, "fidelity_class": cls, "contract_scope": contract_scope(family), "expression_kind": expression_kind(family),
            "thesis_capture": round(cap, 4), "p_bet_given_thesis": round(cap, 4), "p_bet_given_not_thesis": None if pnot is None else round(pnot, 4),
            "thesis_lift": None if pnot is None else round(cap - pnot, 4), "tracking": None if track is None else round(track, 4), "relation": rel,
            "note": {STRUCTURAL: "settles from the thesis itself: cannot lose when the thesis is right",
                     DIRECT: "usually cashes when the thesis is right",
                     FRAGILE: f"usually LOSES even when the thesis is right (cashes {100 * cap:.0f}% of thesis-true draws)"}[cls]}


def from_logged(primary_thesis: dict[str, Any] | None, family: str) -> dict[str, Any]:
    """Fidelity reconstructed from a logged decision row (legacy rows carry P(bet|thesis) and P(bet|not thesis) but no
    draw counts): containment is inferred only when the logged capture is exactly 1.0 to four decimals."""
    pt = primary_thesis or {}
    key = pt.get("key")
    cap = pt.get("p_bet_given_thesis")
    pnot = pt.get("p_bet_given_not_thesis")
    if not key or key == "DIFFUSE" or cap is None:
        return {"thesis": key, "fidelity_class": NONE, "contract_scope": contract_scope(family), "expression_kind": expression_kind(family), "thesis_capture": None,
                "p_bet_given_thesis": None, "p_bet_given_not_thesis": None, "thesis_lift": None, "relation": None, "reconstructed": True}
    rel = "IMPLIED_BY_THESIS" if float(cap) >= 0.99995 else "CORRELATED"
    return {"thesis": key, "fidelity_class": classify(float(cap), rel), "contract_scope": contract_scope(family), "expression_kind": expression_kind(family),
            "thesis_capture": float(cap), "p_bet_given_thesis": float(cap), "p_bet_given_not_thesis": pnot,
            "thesis_lift": None if pnot is None else round(float(cap) - float(pnot), 4), "relation": rel, "reconstructed": True}
