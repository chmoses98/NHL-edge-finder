"""Side-by-side shadow expression challenger, never an order or staking authority.

Unlike the incumbent optimizer's growth-sorted 40-side shortlist, this looks at ALL
eligible equivalent-deduplicated candidate sides and limits its selection to
game/team markets. Period markets are displayed as research-only alternatives.
Calibration and script tiers are diagnostics, NOT proven profitability signals.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

import numpy as np

from nhl_edge.thesis.fidelity import fidelity
from nhl_edge.thesis.mapping import MIN_THESIS_PHI, associations
from nhl_edge.scripts_v1.survival import ROBUST, MODERATE

VERSION = "NHL_EXPRESSION_CHALLENGER_V1"
BROAD_FAMILIES = frozenset((
    "game_winner", "game_spread", "game_total", "team_total",
    "game_overtime", "period_winner", "period_spread", "period_total",
))
UNVALIDATED_PERIOD_FAMILIES = frozenset(("period_winner", "period_spread", "period_total"))
MAX_ROWS = 8


def _safe(x: Any, nd: int = 4) -> float | None:
    if x is None:
        return None
    return round(float(x), nd)


def _key(row: dict[str, Any]) -> tuple:
    """Predeclared research preference; not presented as an empirically fitted edge."""
    tier = {"ROBUST": 2, "MODERATE": 1}.get(row["robustness"], 0)
    quality = {"STRUCTURAL": 2, "DIRECT": 1}.get(row["fidelity"], 0)
    return (row["settlement_verified"], tier, quality,
            row["mass_survived"] or 0.0, row["ev_adjusted"] or 0.0,
            row["thesis_capture"] or 0.0, -(row["ask_cents"] or 100),
            row["bet_id"])


def build_expression_challenger(a: dict[str, Any], survival: dict[str, Any], limit: int = MAX_ROWS) -> dict[str, Any]:
    """Return a shadow comparison of broad expressions from the FULL eligible board.

    Caller supplies existing pregame analysis plus script survival computed from the
    SAME joint draws. No model probabilities, optimizer, research governance, or
    published wagers are altered. Never infer an edge from unpriced contracts.
    """
    candidates = [b for b in a["candidates"]
                  if b.family in BROAD_FAMILIES
                  and a["econ"][b.bet_id].eligible
                  and survival[b.bet_id].data_quality == "OK"]
    excluded_players = sum(b.family not in BROAD_FAMILIES for b in a["candidates"])
    game = a["gd"]
    em = a["em"]
    if not candidates:
        return {
            "version": VERSION, "authority": "RESEARCH_ONLY", "status": "NO_ELIGIBLE_BROAD_MARKET",
            "n_full_board_eligible": len(a["candidates"]), "n_compared": 0,
            "n_player_candidates_excluded": excluded_players, "selected": [],
            "alternatives": [], "selection_method": "shadow comparison only",
        }
    Y = np.stack([b.y for b in candidates])
    PHI, PAB, _ = associations(Y, em)
    n = game.features.n
    rows: list[dict[str, Any]] = []
    for i, b in enumerate(candidates):
        e = a["econ"][b.bet_id]
        sv = survival[b.bet_id]
        j = int(np.argmax(PHI[i])) if PHI.shape[1] else -1
        identified = j >= 0 and PHI[i, j] >= MIN_THESIS_PHI
        primary = em.events[j] if identified else None
        if primary is not None:
            pe = int(np.count_nonzero(em.E[j]))
            both = int(round(float(PAB[i, j]) * n))
            f = fidelity(n, int(np.count_nonzero(b.y)), pe, both, b.family, primary.key)
        else:
            f = fidelity(n, int(np.count_nonzero(b.y)), 0, 0, b.family, None)
        rows.append({
            "bet_id": b.bet_id, "ticker": b.ticker, "title": b.title,
            "side": b.side, "family": b.family,
            "ask_cents": b.price_cents, "cost_per_contract": _safe(b.cost),
            "p_model": _safe(b.p), "p_adjusted": _safe(e.p_adj),
            "ev_adjusted": _safe(e.ev_adj), "bet_up_to_cents": e.bet_up_to_adj,
            "reliability": a["rel"].get(b.bet_id),
            "robustness": sv.tier, "mass_survived": _safe(sv.mass),
            "major_scripts_survived": sv.n_major_survived,
            "failure_script": sv.to_dict().get("failure_script"),
            "worst_major_script_ev": _safe(sv.worst_major_ev),
            "thesis_key": primary.key if primary else "DIFFUSE",
            "thesis": primary.label if primary else "No unique thesis",
            "thesis_capture": _safe(f["thesis_capture"]),
            "fidelity": f["fidelity_class"],
            "settlement_verified": b.family not in UNVALIDATED_PERIOD_FAMILIES,
            "authority": "RESEARCH_ONLY", "stake_dollars": 0,
        })
    rows.sort(key=_key, reverse=True)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(row["thesis_key"], []).append(row)
    leaders = []
    for key, members in grouped.items():
        m = members[0].copy()
        alt = members[1] if len(members) > 1 else None
        m["best_alternative"] = None if alt is None else {
            "bet_id": alt["bet_id"], "ask_cents": alt["ask_cents"],
            "ev_adjusted": alt["ev_adjusted"], "mass_survived": alt["mass_survived"],
            "fidelity": alt["fidelity"],
        }
        m["other_expressions_compared"] = len(members) - 1
        leaders.append(m)
    leaders.sort(key=_key, reverse=True)
    return {
        "version": VERSION, "authority": "RESEARCH_ONLY", "status": "SHADOW_READY",
        "n_full_board_eligible": len(a["candidates"]), "n_compared": len(rows),
        "n_player_candidates_excluded": excluded_players,
        "family_counts": dict(sorted(Counter(r["family"] for r in rows).items())),
        "selected": leaders[:max(0, min(int(limit), MAX_ROWS))],
        "alternatives": rows[:max(0, min(int(limit), MAX_ROWS))],
        "selection_method": (
            "Per thesis: settlement-verified before research-only periods; "
            "script survival tier; thesis fidelity; mass survived; adjusted EV. "
            "All side prices include executable ask and taker fee. "
            "Ranking is prospective and NOT proof of an edge."
        ),
        "caveats": [
            "No goal-scorer or other single-player bets eligible for selection.",
            "Unvalidated period-contract settlement stays shadow-only.",
            "Existing optimizer/card/governance/stakes remain unchanged.",
            "All model inputs are matchup-conditioned; opponent-adjusted research is not a projection-model input.",
            "One top expression per thesis is a research ranking, not a diversified portfolio.",
        ],
    }
