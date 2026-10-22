"""Market-expression engine -- SHADOW ONLY, DISABLED BY DEFAULT (Phase G). Pure functions: no I/O, no clock, no network.

For one game it ranks the eligible Kalshi expressions of a thesis and returns a card, or PASS. It never places, routes or
sizes a real wager, never touches a stake/cap, and is not imported by any production path.

Probability policy (the heart of the design, and what the audit evidence supports)
    p_hat = mid + w * (p_model - mid),   w = max(0, c_lo90)  -- c_lo90 = the model's AUDITED incremental-information coefficient
    minus 1.28 standard errors (market_audit.model_audit). Today every audited c is indistinguishable from 0 or negative, so
    w = 0 and p_hat = the market mid: the market is the best probability estimate available, and every contract then has
    negative EV by exactly (half-spread + fee). The engine PASSes -- correctly -- until a model earns weight.
Uncertainty: se^2 = floor^2 + (0.5 * |p_v1 - p_v2|)^2 + (w * |p_model - mid|)^2 ; floor = 0.025 (the +-2-3 pt band within which
    the efficiency study found the market calibrated). p_low = p_hat - 1.28 se.
Selection rule: a candidate is only eligible when its family has evidence class VALIDATED (strict policy) AND net EV at the
    EXECUTABLE price using p_low is positive AND script survival >= 0.5. Two COUNTERFACTUAL policies exist only to measure what
    ignoring the evidence would have cost: ``research_unvalidated`` (gate waived, w fixed at 0.5, uncertainty kept) and ``naive_ev``
    (gate waived, w = 1, uncertainty ignored, EV >= 1c on the point estimate -- what a plain EV chaser would do).
Goal-scorer families (player_goals, first_goal) are researched but NEVER recommended.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any

TAKER = 0.07
Z90 = 1.2816
UNC_FLOOR = 0.025
NO_RECOMMEND = ("player_goals", "first_goal")
RESEARCH_BANKROLL = 250.0  # existing NHL research limits are preserved; this module never raises them
RESEARCH_MAX_STAKE = 5.0


def fee(p: float) -> float:
    return TAKER * p * (1.0 - p)


def max_entry_price(p_low: float) -> float:
    """Highest price x (dollars) with p_low - x - fee(x) >= 0, i.e. the break-even entry using the LOW probability."""
    a, b, c = TAKER, -(1.0 + TAKER), p_low
    disc = b * b - 4 * a * c
    return max(0.0, (-b - math.sqrt(max(disc, 0.0))) / (2 * a))


@dataclass
class Candidate:
    ticker: str
    title: str
    family: str
    side: str  # yes | no
    ask: float  # executable price of the contract bought, dollars
    mid_yes: float
    p_model: float | None = None  # P(YES) from the model, when one prices this contract
    p_model_alt: float | None = None  # a second model's P(YES) (V1 vs V2 disagreement widens the range)
    depth_contracts: float | None = None  # visible contracts at/near the ask (None = depth unobserved)
    survival: float | None = None  # share of scripts where the bet stays +EV at this price
    factor: str = ""  # shared-risk tag for correlation ("LOW_SCORING", "WIN:NYR", ...)
    thesis: str = ""
    evidence: list[str] = field(default_factory=list)
    counter: str = ""


def evaluate(c: Candidate, w: float, family_class: str, policy: str = "strict") -> dict[str, Any]:
    naive = policy == "naive_ev"
    p_mid = c.mid_yes if c.side == "yes" else 1.0 - c.mid_yes
    p_mod = None if c.p_model is None else (c.p_model if c.side == "yes" else 1.0 - c.p_model)
    p_alt = None if c.p_model_alt is None else (c.p_model_alt if c.side == "yes" else 1.0 - c.p_model_alt)
    wt = w if p_mod is not None else 0.0
    p_hat = p_mid + wt * ((p_mod - p_mid) if p_mod is not None else 0.0)
    se = math.sqrt(UNC_FLOOR**2 + (0.5 * abs(p_mod - p_alt) if (p_mod is not None and p_alt is not None) else 0.0) ** 2
                   + (wt * abs(p_mod - p_mid) if p_mod is not None else 0.0) ** 2)
    z = 0.0 if naive else Z90
    p_low, p_high = p_hat - z * se, p_hat + z * se
    cost = c.ask + fee(c.ask)
    ev = p_hat - cost
    ev_low = p_low - cost
    reasons: list[str] = []
    if c.family in NO_RECOMMEND:
        reasons.append("goal-scorer family: researched, never recommended")
    if policy == "strict" and family_class != "VALIDATED":
        reasons.append(f"no VALIDATED evidence for family {c.family} (class {family_class})")
    if ev_low <= (0.01 if naive else 0.0):
        reasons.append(f"net EV at the executable price is not positive even before uncertainty ({ev:+.3f}); lower-bound {ev_low:+.3f}")
    if c.survival is not None and c.survival < 0.5:
        reasons.append(f"fragile: stays +EV in only {c.survival:.0%} of script mass")
    if c.depth_contracts is not None and c.depth_contracts < 25:
        reasons.append(f"thin: {c.depth_contracts:.0f} contracts visible")
    elig = not reasons
    return {"ticker": c.ticker, "bet": f"{c.title} -- buy {c.side.upper()}", "family": c.family, "side": c.side, "current_price": round(c.ask, 4),
            "max_acceptable_entry_price": round(max_entry_price(p_low), 4), "estimated_probability": round(p_hat, 4),
            "uncertainty_range": [round(p_low, 4), round(p_high, 4)], "net_ev_per_contract": round(ev, 4), "net_ev_lower_bound": round(ev_low, 4),
            "market_implied_probability": round(p_mid, 4), "model_probability": None if p_mod is None else round(p_mod, 4), "model_weight": round(wt, 3),
            "primary_thesis": c.thesis, "supporting_evidence": c.evidence, "main_counterargument": c.counter,
            "script_resilience": c.survival, "factor": c.factor, "evidence_class": family_class, "eligible": elig, "reject_reasons": reasons}


def research_stake(ev_low: float, p_low: float, ask: float) -> float:
    """Quarter-Kelly on the LOWER probability bound, capped by the existing research limits. Zero unless ev_low > 0."""
    if ev_low <= 0:
        return 0.0
    f = max(0.0, (p_low - ask) / (1.0 - ask)) * 0.25
    return round(min(RESEARCH_MAX_STAKE, RESEARCH_BANKROLL * f), 2)


def build_card(game: str, cands: list[Candidate], w_by_family: dict[str, float], class_by_family: dict[str, str], policy: str = "strict",
               max_positions: int = 2) -> dict[str, Any]:
    w_pol = {"strict": None, "research_unvalidated": 0.5, "naive_ev": 1.0}[policy]
    ev = [evaluate(c, w_by_family.get(c.family, 0.0) if w_pol is None else w_pol, class_by_family.get(c.family, "UNTESTED"), policy) for c in cands]
    ranked = sorted(ev, key=lambda r: (not r["eligible"], -((r["script_resilience"] if r["script_resilience"] is not None else 0.5) * r["net_ev_lower_bound"])))
    chosen: list[dict[str, Any]] = []
    used_factors: set[str] = set()
    for r in ranked:
        if not r["eligible"] or len(chosen) >= max_positions:
            continue
        if r["factor"] and r["factor"] in used_factors:
            r["correlation_warning"] = f"shares risk factor {r['factor']} with an already-selected expression; skipped (no double-counting)"
            continue
        r["research_stake_dollars"] = research_stake(r["net_ev_lower_bound"], r["uncertainty_range"][0], r["current_price"])
        used_factors.add(r["factor"])
        chosen.append(r)
    top_rejected = [r for r in ranked if not r["eligible"]][:3]
    return {"game": game, "decision": "BET" if chosen else "PASS", "n_candidates": len(ev), "n_eligible": sum(r["eligible"] for r in ev),
            "selected": chosen, "best_rejected": top_rejected, "policy": policy,
            "pass_reason": None if chosen else "no expression clears the evidence gate with positive lower-bound net EV after fee and executable price"}
