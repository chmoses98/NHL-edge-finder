"""Market expression layer: confidence-adjusted economics of every bet side and the best expression of each thesis.

Confidence adjustment (a documented prior, not a fit): the model's gap to the Kalshi midpoint is credited only in part,

    p_adj = mid + k * (p - mid),   k = K_BASE[family reliability] + K_BENCH[sportsbook category], clipped to [0.10, 1.00]

    K_BASE  EVIDENCE_STRONGER 0.75 | EVIDENCE_MIXED 0.50 | EVIDENCE_THIN 0.35 | CALIBRATION_WARNING 0.25
    K_BENCH A +0.15 | B +0.05 | C -0.15 | D 0

and when the model is 10+ points from the midpoint ``k`` is capped at ``K_LARGE_GAP`` = 0.35: in the historical player
benchmark (``docs/research/player_sim_v1/market_benchmark.json``, T-10m) the 279 rows where the model sat 10+ points
BELOW the Kalshi mid settled only 3.0 points below the mid -- the market was closer. (The 41 rows 10+ points above
favoured the model, but 41 rows is too few to trust; the cap is symmetric.) So a large disagreement with the market
increases scrutiny rather than confidence, and the market stays the benchmark.
(With no midpoint the reference is the executable price.) Candidates must have positive fee-adjusted EV at the
executable ask under BOTH the model probability and ``p_adj``.

Best expression of a thesis: among every bet side in the game whose phi with the thesis event is >= ``FIT_MIN``,
the eligible one with the highest confidence-adjusted expected log growth at its fractional-Kelly stake

    g = p_adj log(1 + f (1 - cost) / cost) + (1 - p_adj) log(1 - f),   f = kelly_multiplier * (p_adj - cost) / (1 - cost)

-- a risk-adjusted EV that weighs edge against variance and evidence quality. The largest raw edge does NOT win
automatically; the comparison table shows raw edge, adjusted EV, growth, fit, breadth and reliability side by side.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any

from nhl_edge.execution.economics import bet_up_to_cents
from nhl_edge.kalshi.fees import DEFAULT_SCHEDULE, FeeSchedule
from nhl_edge.thesis.mapping import Bet
from nhl_edge.thesis.reliability import MIXED, STRONGER, THIN, WARNING

K_BASE = {STRONGER: 0.75, MIXED: 0.50, THIN: 0.35, WARNING: 0.25}
K_BENCH = {"A": 0.15, "B": 0.05, "C": -0.15, "D": 0.0}
K_LARGE_GAP = 0.35
LARGE_GAP = 0.10
FIT_MIN = 0.20
KELLY_MULT = 0.25


@dataclass
class Econ:
    p: float
    p_adj: float
    k: float
    cost: float | None
    ev_raw: float | None
    ev_adj: float | None
    roi_adj: float | None
    growth_bp: float | None
    bet_up_to_raw: int | None
    bet_up_to_adj: int | None
    eligible: bool
    reasons: list[str]
    notes: list[str] | None = None

    def to_dict(self) -> dict[str, Any]:
        r = lambda x, n=4: None if x is None else round(x, n)  # noqa: E731
        return {"p_model": r(self.p), "p_adjusted": r(self.p_adj), "confidence_k": r(self.k, 2), "cost": r(self.cost), "ev_raw": r(self.ev_raw), "ev_adjusted": r(self.ev_adj),
                "roi_adjusted": r(self.roi_adj), "growth_bp": r(self.growth_bp, 3), "bet_up_to_cents_raw": self.bet_up_to_raw, "bet_up_to_cents_adjusted": self.bet_up_to_adj,
                "eligible": self.eligible, "reasons": self.reasons, "notes": self.notes or []}


def growth(p: float, cost: float, mult: float = KELLY_MULT) -> float:
    if cost <= 0 or cost >= 1:
        return 0.0
    f = max(0.0, (p - cost) / (1 - cost)) * mult
    if f <= 0:
        return 0.0
    return p * math.log(1 + f * (1 - cost) / cost) + (1 - p) * math.log(1 - f)


def economics(bet: Bet, reliability: str, bench: str, schedule: FeeSchedule = DEFAULT_SCHEDULE, min_ev_adj: float = 0.0) -> Econ:
    schedule = bet.meta.get("_schedule") or schedule
    k = min(1.0, max(0.10, K_BASE.get(reliability, K_BASE[THIN]) + K_BENCH.get(bench, 0.0)))
    cost = bet.cost
    ref = bet.p_mid if bet.p_mid is not None else (bet.price_cents / 100.0 if bet.price_cents is not None else None)
    notes: list[str] = []
    if ref is not None and abs(bet.p - ref) >= LARGE_GAP and k > K_LARGE_GAP:
        k = K_LARGE_GAP
        notes.append(f"LARGE_DISAGREEMENT: model {bet.p:.3f} vs reference {ref:.3f}; confidence capped at k={K_LARGE_GAP}")
    p_adj = bet.p if ref is None else min(1.0, max(0.0, ref + k * (bet.p - ref)))
    reasons: list[str] = []
    ev_raw = ev_adj = roi = g = None
    if cost is None:
        reasons.append("no executable ask")
    else:
        ev_raw, ev_adj = bet.p - cost, p_adj - cost
        roi = ev_adj / cost
        g = 1e4 * growth(p_adj, cost)
        if ev_raw <= 0:
            reasons.append("raw EV <= 0 at the executable ask")
        if ev_adj <= 0:
            reasons.append("confidence-adjusted EV <= 0")
        elif ev_adj < min_ev_adj:
            reasons.append(f"confidence-adjusted EV {ev_adj:+.4f} below the {min_ev_adj:.3f}/contract floor")
    for flag in ("stale", "crossed", "not_pregame"):
        if bet.meta.get(flag):
            reasons.append(flag.replace("_", " "))
    up_raw = bet_up_to_cents(bet.p, schedule) if bet.p > 0 else None
    up_adj = bet_up_to_cents(p_adj, schedule) if p_adj > 0 else None
    return Econ(bet.p, p_adj, k, cost, ev_raw, ev_adj, roi, g, up_raw, up_adj, not reasons, reasons, notes)


def compare_expressions(event_key: str, event_label: str, bets: list[Bet], econ: dict[str, Econ], phi_col: dict[str, float],
                        purity: dict[str, float | None], cond: dict[str, float | None], conc: dict[str, dict[str, Any]], rel: dict[str, str],
                        bench: dict[str, str], max_rows: int = 10) -> dict[str, Any]:
    """Every bet side with thesis fit >= FIT_MIN, ranked by adjusted growth (eligible first)."""
    rows = []
    for b in bets:
        ph = phi_col.get(b.bet_id)
        if ph is None or ph < FIT_MIN:
            continue
        e = econ[b.bet_id]
        rows.append({"bet_id": b.bet_id, "title": b.title, "side": b.side, "family": b.family, "price_cents": b.price_cents, "thesis_fit_phi": round(ph, 3),
                     "p_thesis_given_bet": purity.get(b.bet_id), "p_bet_given_thesis": cond.get(b.bet_id),
                     "breadth_rel": (conc.get(b.bet_id) or {}).get("breadth_rel"), "concentration_top2": (conc.get(b.bet_id) or {}).get("top2"),
                     "reliability": rel.get(b.bet_id), "benchmark": bench.get(b.bet_id), **e.to_dict()})
    rows.sort(key=lambda r: (not r["eligible"], -(r["growth_bp"] or -1e9), -(r["ev_raw"] or -9)))
    best = next((r for r in rows if r["eligible"]), None)
    raw_leader = max((r for r in rows if r["ev_raw"] is not None), key=lambda r: r["ev_raw"], default=None)
    return {"thesis": event_key, "label": event_label, "n_expressions": len(rows), "n_eligible": sum(1 for r in rows if r["eligible"]),
            "best": best["bet_id"] if best else None, "raw_edge_leader": raw_leader["bet_id"] if raw_leader else None, "rows": rows[:max_rows],
            "rows_truncated": max(0, len(rows) - max_rows)}


def why_chosen(best: dict[str, Any], alt: dict[str, Any] | None) -> str:
    if alt is None:
        return "no other eligible expression of this thesis (every alternative is -EV at its ask, unadjusted or adjusted, or not executable)"
    bits = []
    if (best.get("growth_bp") or 0) > (alt.get("growth_bp") or 0):
        bits.append(f"higher confidence-adjusted growth ({best['growth_bp']:.2f} vs {alt.get('growth_bp') or 0:.2f} bp)")
    if (alt.get("ev_raw") or -9) > (best.get("ev_raw") or -9):
        bits.append(f"despite a smaller raw edge ({best['ev_raw']:+.3f} vs {alt['ev_raw']:+.3f}/contract)")
    if best.get("reliability") != alt.get("reliability"):
        bits.append(f"evidence {best.get('reliability')} vs {alt.get('reliability')}")
    if (best.get("breadth_rel") or 0) > (alt.get("breadth_rel") or 0) + 0.1:
        bits.append(f"wins across more scripts (relative breadth {best['breadth_rel']} vs {alt.get('breadth_rel')})")
    if not alt.get("eligible"):
        bits.append(f"alternative not eligible: {', '.join(alt.get('reasons') or [])}")
    return "; ".join(bits) or "best adjusted growth among the thesis's expressions"
