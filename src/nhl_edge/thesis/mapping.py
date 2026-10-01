"""Bet-to-script mapping: where each bet's modelled win probability comes from, and what thesis it depends on.

For a bet ``b`` with per-draw win indicator ``y`` and primary script labels ``s``:

    contribution_s   = P(b wins AND script s)              (sums EXACTLY to P(b): integer counts over the same draws)
    share_s          = contribution_s / P(b)
    THESIS_CONCENTRATION = share of the largest one (``top1``) and two (``top2``) scripts
    SCRIPT_BREADTH   = 1 / sum(share_s^2)  (effective number of scripts the bet wins in)
    relative breadth = breadth / (1 / sum(freq_s^2))   -- 1.0 means the bet wins across scripts in proportion to how
                       often they occur (script-neutral); << 1 means it needs specific scripts

Thesis association uses the phi coefficient between the bet indicator and every thesis event (Pearson correlation of
two binaries). The primary thesis is the event with the largest positive phi (>= ``MIN_THESIS_PHI``); the secondary is
the best event of a DIFFERENT category that is not a near-synonym of the primary; the failure case is the event with
the most negative phi plus the major script where the bet does worst.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from nhl_edge.thesis.events import ThesisEvent
from nhl_edge.thesis.scripts import N_PRIMARY, ScriptDistribution

MIN_THESIS_PHI = 0.10
SYNONYM_PHI = 0.70  # two thesis events this correlated are the same idea


@dataclass
class Bet:
    """One side of one contract: a candidate expression."""

    bet_id: str  # "<ticker>|yes" or "<ticker>|no"
    ticker: str
    side: str
    title: str
    family: str
    game_id: str
    y: np.ndarray  # per-draw: this side pays out
    p: float  # model probability this side pays (== y.mean())
    price_cents: int | None  # executable ask of this side
    fee: float | None  # dollars per contract at that ask
    p_mid: float | None  # Kalshi midpoint probability of this side
    team: str | None = None
    opponent: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)

    @property
    def cost(self) -> float | None:
        return None if self.price_cents is None or self.fee is None else self.price_cents / 100.0 + self.fee

    @property
    def ev(self) -> float | None:
        """Fee-adjusted EV per contract at the executable ask (model probability)."""
        return None if self.cost is None else self.p - self.cost


def phi(p_ab: np.ndarray, p_a: np.ndarray, p_b: np.ndarray) -> np.ndarray:
    den = np.sqrt(np.clip(p_a * (1 - p_a), 0, None) * np.clip(p_b * (1 - p_b), 0, None))
    return np.divide(p_ab - p_a * p_b, den, out=np.zeros_like(p_ab, dtype=float), where=den > 1e-12)


def script_counts(Y: np.ndarray, dist: ScriptDistribution) -> np.ndarray:
    """(n_bets, 18) integer counts of draws where the bet wins inside each primary script."""
    if Y.size == 0:
        return np.zeros((0, N_PRIMARY), dtype=np.int64)
    return np.rint(Y.astype(np.float32) @ dist.onehot()).astype(np.int64)


def concentration(counts_row: np.ndarray, freq: np.ndarray) -> dict[str, float | None]:
    wins = counts_row.sum()
    if wins <= 0:
        return {"top1": None, "top2": None, "breadth_eff": None, "breadth_rel": None}
    sh = np.sort(counts_row / wins)[::-1]
    b = 1.0 / float(np.sum(sh**2))
    b0 = 1.0 / float(np.sum(freq**2)) if np.sum(freq**2) > 0 else 1.0
    return {"top1": round(float(sh[0]), 4), "top2": round(float(sh[:2].sum()), 4), "breadth_eff": round(b, 2), "breadth_rel": round(b / b0, 3)}


@dataclass
class EventMatrix:
    events: list[ThesisEvent]
    E: np.ndarray  # (n_events, n) float32
    p: np.ndarray  # (n_events,)
    phi_ee: np.ndarray  # (n_events, n_events)

    @classmethod
    def build(cls, events: list[ThesisEvent]) -> EventMatrix:
        E = np.stack([e.mask for e in events]).astype(np.float32)
        n = E.shape[1]
        p = E.mean(axis=1).astype(float)
        pab = (E @ E.T) / n
        return cls(events, E, p, phi(pab, p[:, None], p[None, :]))

    def index(self, key: str) -> int | None:
        for i, e in enumerate(self.events):
            if e.key == key:
                return i
        return None


def associations(Y: np.ndarray, em: EventMatrix) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """(phi, P(bet AND event), P(bet)) with phi of shape (n_bets, n_events)."""
    n = Y.shape[1]
    pb = Y.mean(axis=1).astype(float)
    pab = (Y.astype(np.float32) @ em.E.T) / n
    return phi(pab, pb[:, None], em.p[None, :]), pab.astype(float), pb


def thesis_profile(i: int, bet: Bet, counts: np.ndarray, dist: ScriptDistribution, em: EventMatrix, PHI: np.ndarray, PAB: np.ndarray) -> dict[str, Any]:
    """Everything the card needs about one bet's dependence on the game script."""
    n = len(dist.labels)
    p = bet.p
    row = counts[i]
    conc = concentration(row, dist.freq)
    order = np.argsort(-row)
    top = []
    for s in order[:4]:
        if row[s] <= 0:
            break
        top.append({"script": dist.taxonomy.primary_name(int(s)), "key": dist.taxonomy.primary_key(int(s)), "contribution_pp": round(100.0 * row[s] / n, 2),
                    "share": round(float(row[s] / max(row.sum(), 1)), 3), "p_win_in_script": round(float(row[s] / max(dist.freq[s] * n, 1)), 3),
                    "script_frequency": round(float(dist.freq[s]), 4)})
    other = 100.0 * (row.sum() - sum(row[s] for s in order[:4])) / n
    major = [s for s in dist.major()]
    worst = min(major, key=lambda s: row[s] / max(dist.freq[s] * n, 1)) if major else None
    ph = PHI[i]
    o = np.argsort(-ph)
    prim = int(o[0]) if ph[o[0]] >= MIN_THESIS_PHI else None
    sec = None
    if prim is not None:
        for j in o[1:]:
            j = int(j)
            if ph[j] < MIN_THESIS_PHI:
                break
            if em.events[j].category != em.events[prim].category and abs(em.phi_ee[prim, j]) < SYNONYM_PHI:
                sec = j
                break
    fail = int(np.argmin(ph))

    def cond(j: int | None) -> dict[str, Any] | None:
        if j is None:
            return None
        e = em.events[j]
        pe = float(em.p[j])
        return {"key": e.key, "label": e.label, "category": e.category, "phi": round(float(ph[j]), 3), "p_thesis": round(pe, 4),
                "p_bet_given_thesis": round(float(PAB[i, j] / pe), 4) if pe > 0 else None,
                "p_thesis_given_bet": round(float(PAB[i, j] / p), 4) if p > 0 else None,
                "p_bet_given_not_thesis": round(float((p - PAB[i, j]) / (1 - pe)), 4) if pe < 1 else None}

    out = {"p": round(p, 4), "concentration": conc, "main_scripts": top, "other_scripts_pp": round(other, 2),
           "primary_thesis": cond(prim) or {"key": "DIFFUSE", "label": "no single thesis (diffuse dependence on the game script)", "category": "diffuse", "phi": round(float(ph[o[0]]), 3)},
           "secondary_thesis": cond(sec), "failure_thesis": cond(fail) if ph[fail] < 0 else None,
           "worst_major_script": ({"script": dist.taxonomy.primary_name(worst), "p_win_in_script": round(float(row[worst] / max(dist.freq[worst] * n, 1)), 3),
                                   "script_frequency": round(float(dist.freq[worst]), 4)} if worst is not None else None)}
    # explicit team-offense conditionals for player props (e.g. P(Rakell goal | PIT 4+) and P(PIT 4+ | Rakell goal))
    if bet.team and bet.family.startswith(("player_", "first_goal")):
        j = em.index(f"{bet.team}:OFFENSE_4PLUS")
        if j is not None:
            out["team_offense"] = cond(j)
    return out
