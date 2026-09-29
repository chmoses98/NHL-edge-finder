"""Authority ledger: how much a model family has EARNED the right to influence anything.

Stages are assigned per family from PROSPECTIVE evidence only. Tonight and until an explicit promotion decision,
every family is RESEARCH_ONLY. Thresholds are conservative placeholders and must never be tuned on backtests.
Promotion is a separate, explicit decision recorded in docs/AUTHORITY.md; this module only REPORTS eligibility.
"""

from __future__ import annotations

from typing import Any

from nhl_edge.evaluation.metrics import brier, brier_skill_score, ece, log_loss

SHADOW_MIN_N = 100
LIMITED_MIN_N = 300
TRUSTED_MIN_N = 1000
MAX_ECE = 0.05


def eligibility(rows: list[dict[str, Any]], p_key: str = "p_data_only") -> dict[str, Any]:
    """Report what the prospective evidence would support. Never assigns authority."""
    xs = [(float(r[p_key]), int(r["y"]), r.get("p_market"), r.get("clv_signed")) for r in rows if r.get("pregame") and r.get(p_key) is not None]
    n = len(xs)
    out: dict[str, Any] = {"n_settled_pregame": n, "current_authority": "RESEARCH_ONLY", "eligible_for": "RESEARCH_ONLY"}
    if n == 0:
        return out
    p = [x[0] for x in xs]
    y = [x[1] for x in xs]
    out["brier"] = brier(p, y)
    out["log_loss"] = log_loss(p, y)
    out["ece"] = ece(p, y) if n >= 20 else None
    mk = [(x[0], x[1], float(x[2])) for x in xs if x[2] is not None]
    if mk:
        out["n_with_market"] = len(mk)
        out["brier_market"] = brier([m[2] for m in mk], [m[1] for m in mk])
        out["brier_skill_vs_market"] = brier_skill_score([m[0] for m in mk], [m[1] for m in mk], [m[2] for m in mk])
    clv = [float(x[3]) for x in xs if x[3] is not None]
    out["clv_mean"] = sum(clv) / len(clv) if clv else None
    if n >= SHADOW_MIN_N:
        out["eligible_for"] = "SHADOW"
    if n >= LIMITED_MIN_N and (out.get("brier_skill_vs_market") or 0) > 0 and (out.get("clv_mean") or 0) > 0 and (out.get("ece") or 1) < MAX_ECE:
        out["eligible_for"] = "LIMITED"
    out["note"] = "eligibility is informational; promotion requires an explicit owner decision (docs/AUTHORITY.md)"
    return out
