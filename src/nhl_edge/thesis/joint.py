"""Same-game joint outcome matrix: every pairwise relationship computed from the SAME simulation draws.

For bets A and B (per-draw win indicators): P(A), P(B), P(A and B), P(A|B), P(B|A), P(A xor B), phi, the expected
joint profit if both are bought ($1 each), P(both lose), and script overlap = sum_s min(share_A,s, share_B,s) (overlap
of where the two bets' wins come from, 0..1).

Base relationship labels (deterministic rules, thresholds fixed a priori):

* DUPLICATIVE: phi >= 0.60, or one bet (almost) implies the other (max conditional >= 0.97) with phi >= 0.30
  -> the two monetise the same event and share one exposure budget;
* REINFORCING: 0.15 <= phi < 0.60 -> mostly succeed in the same scripts;
* PARTIALLY_CONTRADICTORY: phi <= -0.15 -> one tends to win where the other is weakened;
* MOSTLY_INDEPENDENT: otherwise.

INTENTIONAL_DIVERSIFIER is assigned by the portfolio layer, never here: a non-positively correlated pair (phi < 0.15)
in which BOTH bets are individually +EV (confidence-adjusted), both keep a positive stake in the jointly optimised
portfolio, and the pair's optimal expected log growth beats either bet alone. Negative correlation is never labelled bad
by itself, and a -EV bet can never become a diversifier (it is not a candidate).
"""

from __future__ import annotations

from typing import Any

import numpy as np

from nhl_edge.thesis.mapping import Bet, phi

DUP_PHI = 0.60
NESTED_COND = 0.97
NESTED_PHI = 0.30
REINF_PHI = 0.15
CONTRA_PHI = -0.15

DUPLICATIVE = "DUPLICATIVE"
REINFORCING = "REINFORCING"
MOSTLY_INDEPENDENT = "MOSTLY_INDEPENDENT"
PARTIALLY_CONTRADICTORY = "PARTIALLY_CONTRADICTORY"
INTENTIONAL_DIVERSIFIER = "INTENTIONAL_DIVERSIFIER"


def base_label(ph: float, p_a_given_b: float | None, p_b_given_a: float | None) -> str:
    cmax = max(x for x in (p_a_given_b, p_b_given_a, 0.0) if x is not None)
    if ph >= DUP_PHI or (cmax >= NESTED_COND and ph >= NESTED_PHI):
        return DUPLICATIVE
    if ph >= REINF_PHI:
        return REINFORCING
    if ph <= CONTRA_PHI:
        return PARTIALLY_CONTRADICTORY
    return MOSTLY_INDEPENDENT


def joint_matrix(bets: list[Bet], script_counts: np.ndarray | None = None) -> dict[str, Any]:
    """Pairwise relationships for a (short) list of same-game bets. ``script_counts``: (n_bets, 18) win counts per primary
    script (for script overlap); optional."""
    k = len(bets)
    if k == 0:
        return {"bets": [], "pairs": []}
    Y = np.stack([b.y for b in bets]).astype(np.float32)
    n = Y.shape[1]
    pa = Y.mean(axis=1).astype(float)
    pab = (Y @ Y.T).astype(float) / n
    PH = phi(pab, pa[:, None], pa[None, :])
    shares = None
    if script_counts is not None and len(script_counts):
        tot = script_counts.sum(axis=1, keepdims=True)
        shares = np.divide(script_counts, tot, out=np.zeros(script_counts.shape, float), where=tot > 0)
    pairs = []
    for i in range(k):
        for j in range(i + 1, k):
            a, b = bets[i], bets[j]
            pij = pab[i, j]
            a_b = pij / pa[j] if pa[j] > 0 else None
            b_a = pij / pa[i] if pa[i] > 0 else None
            prof = None
            if a.cost and b.cost:
                ra = (a.y.astype(float) - a.cost) / a.cost
                rb = (b.y.astype(float) - b.cost) / b.cost
                prof = float(np.mean(ra + rb))
            pairs.append({
                "a": a.bet_id, "b": b.bet_id, "p_a": round(pa[i], 4), "p_b": round(pa[j], 4), "p_a_and_b": round(pij, 4),
                "p_a_given_b": None if a_b is None else round(a_b, 4), "p_b_given_a": None if b_a is None else round(b_a, 4),
                "p_a_xor_b": round(pa[i] + pa[j] - 2 * pij, 4), "p_both_lose": round(1 - pa[i] - pa[j] + pij, 4), "phi": round(float(PH[i, j]), 3),
                "expected_profit_1usd_each": None if prof is None else round(prof, 4),
                "script_overlap": None if shares is None else round(float(np.minimum(shares[i], shares[j]).sum()), 3),
                "relationship": base_label(float(PH[i, j]), a_b, b_a),
            })
    return {"bets": [b.bet_id for b in bets], "pairs": pairs}


def check_identities(pair: dict[str, Any], tol: float = 1e-3) -> list[str]:
    """Probability identities every pair must satisfy (used by tests and by the card gate)."""
    bad = []
    pa, pb, pab = pair["p_a"], pair["p_b"], pair["p_a_and_b"]
    if pab > min(pa, pb) + tol:
        bad.append("P(A and B) > min(P(A), P(B))")
    if pab < pa + pb - 1 - tol:
        bad.append("P(A and B) < P(A) + P(B) - 1")
    if pair["p_a_given_b"] is not None and abs(pair["p_a_given_b"] * pb - pab) > tol:
        bad.append("P(A|B) P(B) != P(A and B)")
    if pair["p_b_given_a"] is not None and abs(pair["p_b_given_a"] * pa - pab) > tol:
        bad.append("P(B|A) P(A) != P(A and B)")
    if abs(pair["p_a_xor_b"] - (pa + pb - 2 * pab)) > tol:
        bad.append("P(A xor B) != P(A) + P(B) - 2 P(A and B)")
    return bad
