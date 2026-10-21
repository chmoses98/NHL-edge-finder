"""Registry rule set ``nhl-hypotheses-1.1`` (RESEARCH_ONLY): a stricter, separately versioned classification of hypothesis results.

Why a new version: v1.0 (``hypotheses.classify``, frozen at git 627b5fa7) labels a hypothesis PROMISING when its net ROI is positive on
every testable tier. For a single-tier hypothesis that is a point-estimate coin flip: M14 (early-goal Under) was PROMISING at +0.1% ROI with a
95% interval of roughly +/-18 points and a negative ROI after one cent of slippage. v1.0 is NOT edited and its historical labels are NOT relabelled;
v1.1 is a second, parallel reading of the same numbers (``reclassify``) and the rule that governs every FUTURE (prospective) look.

v1.1 classes
    VALIDATED       v1.0's rule, plus: a hypothesis whose HIST_HOLD tier was registered must have a TESTABLE hold-out with ROI>0 (v1.0 let an untestable
                    hold-out pass), and a post-hoc-suggested hypothesis can never be VALIDATED from HIST evidence.
    PROMISING_V11   ROI>0 on every testable tier AND ROI>0 at +1c slippage on every testable tier AND at least one tier with n_games>=100 whose
                    lower-90% bound is > 0 AND (when a BH q is available) q<=0.25.
    POINT_POSITIVE  ROI>0 on every testable tier but the evidence bar above is not met (reported for transparency, never a candidate for action).
    UNPROFITABLE_AT_ASK  (v1.0 "REJECTED", renamed: negative ROI after half-spread and fee is what a perfectly efficient market produces, so this label says
                    "not profitable at the ask", never "no mispricing"). Needs ROI<0 on every testable tier and a tier with n_games>=100 whose upper 95% bound is below
                    -0.01 (one point of margin so a 4,000-resample percentile endpoint cannot flip the class: M9 sat at -0.0006).
    UNTESTABLE      unchanged.
    INCONCLUSIVE    anything else.
Power disclosure (new): ``mde80`` = the ROI a one-sided 5% test would detect with 80% power given each tier's standard error; a result whose
mde80 exceeds 0.10 is flagged UNDERPOWERED, because "no effect" there only means "no effect larger than mde80".
"""

from __future__ import annotations

from typing import Any

from nhl_edge.market_audit import hypotheses as H

REGISTRY_VERSION_V11 = "nhl-hypotheses-1.1"
MIN_GAMES_STRONG = 100
Q_PROMISING = 0.25
Z_ONE_SIDED_5 = 1.645
Z_POWER_80 = 0.8416


def tier_se(r: dict[str, Any]) -> float | None:
    if r.get("roi_lo95") is None or r.get("roi_hi95") is None:
        return None
    return (r["roi_hi95"] - r["roi_lo95"]) / (2 * 1.96)


def mde80(r: dict[str, Any]) -> float | None:
    se = tier_se(r)
    return None if se is None else (Z_ONE_SIDED_5 + Z_POWER_80) * se


REJECT_MARGIN = 0.01


def classify_v11(per_tier: dict[str, dict[str, Any]], q_live: float | None, h: H.Hypothesis | None = None) -> str:
    v10 = H.classify(per_tier, q_live)
    testable = {t: r for t, r in per_tier.items() if r.get("roi") is not None and r["n_games"] >= 30}
    if v10 == "VALIDATED":
        if h is not None:
            hold_registered = "HIST_HOLD" in h.tiers
            if hold_registered and "HIST_HOLD" not in testable:
                return "PROMISING_V11"
            if h.post_hoc and any(t.startswith("HIST") for t in h.tiers):
                return "PROMISING_V11"
        return "VALIDATED"
    if v10 == "REJECTED":
        big = [r for r in testable.values() if r["n_games"] >= MIN_GAMES_STRONG]
        return "UNPROFITABLE_AT_ASK" if any(r["roi_hi95"] < -REJECT_MARGIN for r in big) else "INCONCLUSIVE"
    if v10 != "PROMISING":
        return v10
    testable = {t: r for t, r in per_tier.items() if r.get("roi") is not None and r["n_games"] >= 30}
    strong_ok = any(r["n_games"] >= MIN_GAMES_STRONG and r.get("roi_lo90") is not None and r["roi_lo90"] > 0 for r in testable.values())
    slip_ok = all(r.get("roi_slip_1c") is not None and r["roi_slip_1c"] > 0 for r in testable.values())
    q_ok = q_live is None or q_live <= Q_PROMISING
    return "PROMISING_V11" if (strong_ok and slip_ok and q_ok) else "POINT_POSITIVE"


def reclassify(results: dict[str, Any]) -> dict[str, Any]:
    """Side-by-side v1.0 / v1.1 table from a committed ``hypothesis_results.json`` payload. The input is never modified."""
    out: dict[str, Any] = {}
    for hid, r in results["results"].items():
        tiers = {t: x for t, x in r["tiers"].items()}
        v11 = classify_v11(tiers, r.get("q_live_bh"), H.BY_ID.get(hid))
        powers = {t: mde80(x) for t, x in tiers.items() if x.get("roi") is not None}
        out[hid] = {"title": r["title"], "class_v10": r["class"], "class_v11": v11, "changed": v11 != r["class"], "mde80_by_tier": powers,
                    "underpowered_tiers": [t for t, m in powers.items() if m is not None and m > 0.10]}
    return {"registry_version": REGISTRY_VERSION_V11, "supersedes": H.REGISTRY_VERSION, "source_registry_version": results.get("meta", {}).get("registry_version"),
            "rows": out}
