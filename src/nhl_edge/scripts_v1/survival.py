"""Script-conditioned market pricing and SCRIPT SURVIVAL (``nhl-survival-1.0``).

For every bet side ``b`` the joint draw already holds a per-draw settlement indicator ``y_b`` (the exact indicator the
production pricer averaged; ``thesis.outcomes``). With the NHL_SCRIPT_V1 label of every draw:

    P(b | script s)        = sum(y_b[s]) / n_s                                     (integer counts, same draws)
    conservative haircut   delta_b = p_b - p_adj_b                                 (the card's confidence adjustment,
                                                                                    applied as a per-contract cost so the
                                                                                    dependence structure is untouched --
                                                                                    exactly how thesis.portfolio does it)
    EV(b | s)              = P(b | s) - delta_b - cost_b,   cost = executable ask of THIS side + Kalshi taker fee
    identity               sum_s freq_s * EV(b | s) == EV_adjusted(b)              (tested)

``b`` SURVIVES script ``s`` when EV(b | s) >= ``MIN_EV`` (1.0c per contract, the card's ``min_ev_adjusted`` floor) AND
the bet passes the data-quality gates (an executable ask on a board that is neither stale nor crossed, pregame).

Aggregates per bet side: probability mass survived = sum of freq_s over survived scripts; number of MAJOR scripts
(freq >= 5%) survived; worst / best major-script EV; expected EV across scripts (== adjusted EV); the PRIMARY FAILURE
SCRIPT (the major script with the most negative freq-weighted EV) and downside concentration (that script's share of
all negative freq-weighted EV).

Robustness tiers (documented thresholds, fixed a priori; probability MASS matters, not script counts):

    ROBUST            adjusted EV >= 2c, mass survived >= 0.65 and >= 3 major scripts survived
    MODERATE          adjusted EV >= 1c, mass survived >= 0.45 and >= 2 major scripts survived
    FRAGILE           adjusted EV > 0 otherwise (positive on average, but the value sits in a narrow set of scripts)
    DOES_NOT_SURVIVE  adjusted EV <= 0 (negative expected value after the conservative adjustment)
    UNAVAILABLE       no executable ask, stale / crossed board, or not pregame (data-quality gate failed)

A binary contract always loses everything in some script (a home moneyline cannot win the AWAY_CONTROL script), so the
worst-script EV alone cannot define robustness; the tiers are mass-based for that reason.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from nhl_edge.scripts_v1.taxonomy import MAJOR_MIN_FREQ, N_SCRIPTS, SCRIPTS

MIN_EV = 0.01
ROBUST_MIN_EV = 0.02  # a robust candidate also needs an adjusted edge clearly above model noise (2c per contract)
ROBUST_MASS, ROBUST_MAJOR = 0.65, 3
MODERATE_MASS, MODERATE_MAJOR = 0.45, 2
ROBUST, MODERATE, FRAGILE, DOES_NOT_SURVIVE, UNAVAILABLE = "ROBUST", "MODERATE", "FRAGILE", "DOES_NOT_SURVIVE", "UNAVAILABLE"
TIER_RANK = {ROBUST: 4, MODERATE: 3, FRAGILE: 2, DOES_NOT_SURVIVE: 1, UNAVAILABLE: 0}
TIER_WORD = {ROBUST: "Robust", MODERATE: "Moderate", FRAGILE: "Fragile", DOES_NOT_SURVIVE: "Does not survive", UNAVAILABLE: "Unavailable"}
TIERS = {"ROBUST": f"adjusted EV >= {ROBUST_MIN_EV:.2f} and mass survived >= {ROBUST_MASS} and >= {ROBUST_MAJOR} major scripts survived",
         "MODERATE": f"adjusted EV >= {MIN_EV:.2f} and mass survived >= {MODERATE_MASS} and >= {MODERATE_MAJOR} major scripts survived",
         "FRAGILE": "adjusted EV > 0 but below the MODERATE thresholds",
         "DOES_NOT_SURVIVE": "adjusted EV <= 0 at the executable ask",
         "UNAVAILABLE": "no executable ask, stale or crossed board, or not pregame"}


def data_quality(meta: dict[str, Any], cost: float | None) -> str:
    if cost is None:
        return "NO_EXECUTABLE_PRICE"
    if meta.get("not_pregame"):
        return "NOT_PREGAME"
    if meta.get("stale"):
        return "STALE_QUOTE"
    if meta.get("crossed"):
        return "CROSSED_BOOK"
    return "OK"


@dataclass
class SideSurvival:
    bet_id: str
    p: float
    p_by_script: np.ndarray  # nan where the script has no draws
    delta: float
    cost: float | None
    ev_by_script: np.ndarray | None
    survives: np.ndarray | None
    mass: float | None
    n_major_survived: int | None
    n_major: int
    worst_major_ev: float | None
    best_major_ev: float | None
    expected_ev: float | None
    failure_script: int | None
    downside_concentration: float | None
    tier: str
    data_quality: str

    def to_dict(self, nd: int = 4) -> dict[str, Any]:
        r = lambda x: None if x is None or (isinstance(x, float) and np.isnan(x)) else round(float(x), nd)  # noqa: E731
        return {"bet_id": self.bet_id, "p": r(self.p), "delta": r(self.delta), "cost": r(self.cost),
                "ev_by_script": None if self.ev_by_script is None else [r(x) for x in self.ev_by_script],
                "survives": None if self.survives is None else [bool(x) for x in self.survives],
                "mass_survived": r(self.mass), "n_major_survived": self.n_major_survived, "n_major": self.n_major,
                "worst_major_ev": r(self.worst_major_ev), "best_major_ev": r(self.best_major_ev), "expected_ev": r(self.expected_ev),
                "failure_script": None if self.failure_script is None else SCRIPTS[self.failure_script].id,
                "downside_concentration": r(self.downside_concentration), "tier": self.tier, "data_quality": self.data_quality}


def conditional_matrix(Y: np.ndarray, codes: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """(P(bet | script) [n_bets x 7] with nan for empty scripts, win counts [n_bets x 7], draws per script [7])."""
    n_s = np.bincount(codes.astype(np.int64), minlength=N_SCRIPTS)
    oh = np.zeros((len(codes), N_SCRIPTS), dtype=np.float32)
    oh[np.arange(len(codes)), codes] = 1.0
    counts = (Y.astype(np.float32) @ oh) if len(Y) else np.zeros((0, N_SCRIPTS), np.float32)
    counts = np.rint(counts).astype(np.int64)
    with np.errstate(invalid="ignore", divide="ignore"):
        p = np.where(n_s > 0, counts / np.maximum(n_s, 1), np.nan)
    return p, counts, n_s


def tier_for(ev_adj: float | None, mass: float | None, n_major_survived: int | None, dq: str) -> str:
    if dq != "OK" or ev_adj is None:
        return UNAVAILABLE
    if ev_adj <= 0:
        return DOES_NOT_SURVIVE
    if ev_adj >= ROBUST_MIN_EV and (mass or 0) >= ROBUST_MASS and (n_major_survived or 0) >= ROBUST_MAJOR:
        return ROBUST
    if ev_adj >= MIN_EV and (mass or 0) >= MODERATE_MASS and (n_major_survived or 0) >= MODERATE_MAJOR:
        return MODERATE
    return FRAGILE


def side_survival(bet_id: str, p: float, p_s: np.ndarray, freq: np.ndarray, p_adj: float | None, cost: float | None, dq: str) -> SideSurvival:
    major = freq >= MAJOR_MIN_FREQ
    delta = float(p - p_adj) if p_adj is not None else 0.0
    n_major = int(major.sum())
    if cost is None:
        return SideSurvival(bet_id, p, p_s, delta, None, None, None, None, None, n_major, None, None, None, None, None, UNAVAILABLE, dq)
    ev = p_s - delta - cost
    ev_f = np.where(np.isnan(ev), -np.inf, ev)
    surv = (ev_f >= MIN_EV) & (freq > 0) & (dq == "OK")
    mass = float(freq[surv].sum())
    expected = float(np.nansum(freq * np.where(np.isnan(ev), 0.0, ev)))
    mev = ev[major & ~np.isnan(ev)]
    worst = float(mev.min()) if len(mev) else None
    best = float(mev.max()) if len(mev) else None
    contrib = np.where(major & ~np.isnan(ev), freq * ev, 0.0)
    neg = contrib[contrib < 0]
    fail = int(np.argmin(contrib)) if len(neg) else None
    conc = float(contrib[fail] / neg.sum()) if fail is not None and neg.sum() < 0 else None
    n_maj_s = int((surv & major).sum())
    tier = tier_for(expected, mass, n_maj_s, dq)
    return SideSurvival(bet_id, p, p_s, delta, cost, ev, surv, mass, n_maj_s, n_major, worst, best, expected, fail, conc, tier, dq)


def game_survival(bets: list[Any], econ: dict[str, Any], codes: np.ndarray) -> tuple[dict[str, SideSurvival], np.ndarray, np.ndarray]:
    """Survival of every bet side of one game. ``bets``: thesis ``Bet`` objects (both sides of every priced contract);
    ``econ``: bet_id -> ``thesis.expression.Econ`` (p_adj, cost). Returns (bet_id -> SideSurvival, P(bet|script), freq)."""
    from nhl_edge.scripts_v1.taxonomy import frequencies

    freq = frequencies(codes)
    Y = np.stack([b.y for b in bets]) if bets else np.zeros((0, len(codes)), bool)
    P, _, _ = conditional_matrix(Y, codes)
    out = {}
    for i, b in enumerate(bets):
        e = econ.get(b.bet_id)
        p_adj = getattr(e, "p_adj", None)
        out[b.bet_id] = side_survival(b.bet_id, float(b.p), P[i], freq, p_adj, b.cost, data_quality(b.meta, b.cost))
    return out, P, freq
