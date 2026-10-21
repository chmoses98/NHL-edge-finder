"""Pre-registered hypothesis registry and evaluation rules (Phases C/F).

REGISTERED BEFORE THE LIVE-TIER TESTS WERE RUN. This file is committed first; the runner reads it and nothing else.
Everything below is fixed in advance: one decision horizon (T-60 min), selectors, sides, statistic, the multiple-
comparison correction and the evidence classes. No registered hypothesis may be edited after its first live-tier run;
a changed idea is a NEW id.

Tiers
    HIST_DISC   2025-26 regular season, first 60% of games by date (Kalshi hourly candles; no depth)
    HIST_HOLD   2025-26 regular season, last 40%                    (chronological holdout)
    LIVE        2026-27 live archive 2026-09-29..2026-10-20, 151 final games (bid/ask board; depth for 4 families)

Disclosure: before registration the full-season 2025-26 history was inspected descriptively (calibration by price band, by
total line, by month). HIST_* tiers are therefore NOT clean out-of-sample for hypotheses that descriptive pass suggested
(M6 in particular, which was suggested by the October-2025 month). LIVE had not been examined against prices or outcomes
for any registered hypothesis. Only LIVE can validate.

Statistic: net ROI = sum(profit)/sum(cost) buying the selected side at the DISPLAYED ASK with the quadratic taker fee,
game-clustered bootstrap (4000 resamples of whole games). Slippage stress: ask + 1 cent. The pre-friction gap
mean(y - mid) (side-adjusted) is reported as the efficiency diagnostic.

Evidence classes (deterministic, see ``classify``):
    VALIDATED     LIVE n_games>=100, one-sided bootstrap p (BH-adjusted over the LIVE family) <= 0.10, LIVE 90% lower bound of
                  net ROI > 0, ROI>0 under +1c slippage, AND HIST_HOLD net ROI > 0 where testable.
    PROMISING     net ROI > 0 on every testable tier, but VALIDATED not met.
    REJECTED      every testable tier has point ROI < 0 and the 95% upper bound of at least one tier with >=100 games is < 0.
    UNTESTABLE    fewer than 30 independent games on every tier.
    INCONCLUSIVE  anything else.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import cluster_ratio_ci, taker_fee

REGISTRY_VERSION = "nhl-hypotheses-1.0"
DECISION_HORIZON_MIN = 60
N_BOOT = 4000
FULL_GAME = ("winner", "spread", "total", "team_total")


@dataclass(frozen=True)
class Hypothesis:
    id: str
    title: str
    statement: str
    side: str  # yes | no | model (model-driven side) | move (price-move side)
    select: Callable[[pd.DataFrame], pd.Series]
    tiers: tuple[str, ...]
    post_hoc: bool = False  # suggested by a descriptive look at the history tier before registration
    group: str = "market_structure"


def _mid_between(df: pd.DataFrame, lo: float, hi: float) -> pd.Series:
    return (df["mid"] >= lo) & (df["mid"] <= hi)


REGISTRY: tuple[Hypothesis, ...] = (
    Hypothesis("M1", "Full-game Under", "Buying NO (Under) on full-game total lines priced 0.30-0.70 has positive net ROI.", "no",
               lambda d: (d["kind"] == "total") & _mid_between(d, 0.30, 0.70), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M2", "Full-game Over", "Buying YES (Over) on full-game total lines priced 0.30-0.70 has positive net ROI.", "yes",
               lambda d: (d["kind"] == "total") & _mid_between(d, 0.30, 0.70), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M3", "Fade longshots", "Buying NO on any full-game contract whose YES mid is <= 0.20 has positive net ROI (favourite-longshot bias).", "no",
               lambda d: d["kind"].isin(FULL_GAME) & (d["mid"] <= 0.20), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M4", "Back favourites", "Buying YES on any full-game contract whose YES mid is >= 0.80 has positive net ROI.", "yes",
               lambda d: d["kind"].isin(FULL_GAME) & (d["mid"] >= 0.80), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M5", "Fade alternate-spread YES", "Buying NO on 'wins by over 2.5/3.5/...' alternate puck lines has positive net ROI.", "no",
               lambda d: (d["kind"] == "spread") & (d["threshold"] >= 2.5), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M6", "Early-season Overs", "In the first 21 days of a season, Over on totals priced 0.20-0.80 has positive net ROI.", "yes",
               lambda d: (d["kind"] == "total") & _mid_between(d, 0.20, 0.80) & d["early_season"], ("HIST_DISC", "HIST_HOLD", "LIVE"), post_hoc=True),
    Hypothesis("M7", "Team-total Under", "Buying NO (Under) on team totals priced 0.30-0.70 has positive net ROI.", "no",
               lambda d: (d["kind"] == "team_total") & _mid_between(d, 0.30, 0.70), ("LIVE",)),
    Hypothesis("M8", "Team-total Over", "Buying YES (Over) on team totals priced 0.30-0.70 has positive net ROI.", "yes",
               lambda d: (d["kind"] == "team_total") & _mid_between(d, 0.30, 0.70), ("LIVE",)),
    Hypothesis("M9", "Period-total Under", "Buying NO (Under) on period totals priced 0.30-0.70 has positive net ROI.", "no",
               lambda d: (d["kind"] == "period_total") & _mid_between(d, 0.30, 0.70), ("LIVE",)),
    Hypothesis("M10", "Period-total Over", "Buying YES (Over) on period totals priced 0.30-0.70 has positive net ROI.", "yes",
               lambda d: (d["kind"] == "period_total") & _mid_between(d, 0.30, 0.70), ("LIVE",)),
    Hypothesis("M11", "Late-move continuation", "On moneylines, buying the side a >=2c mid move (T-24h -> T-60m) favoured has positive net ROI.", "move",
               lambda d: (d["kind"] == "winner") & (d["move"].abs() >= 0.02), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M12", "Late-move reversal", "On moneylines, buying the side a >=2c mid move (T-24h -> T-60m) went AGAINST has positive net ROI.", "move_rev",
               lambda d: (d["kind"] == "winner") & (d["move"].abs() >= 0.02), ("HIST_DISC", "HIST_HOLD", "LIVE")),
    Hypothesis("M13", "Overtime NO", "Buying NO on 'game goes to overtime' has positive net ROI.", "no",
               lambda d: d["kind"] == "overtime", ("LIVE",)),
    Hypothesis("M14", "Early-goal Under", "Buying NO on 'goal in first 10 minutes' has positive net ROI.", "no",
               lambda d: d["kind"] == "early_goal", ("LIVE",)),
    Hypothesis("C1", "V1 disagreement", "Buying the side DATA_ONLY_V1 favours by >=5 points vs the market mid has positive net ROI.", "model",
               lambda d: d["model_gap"].abs() >= 0.05, ("HIST_DISC", "HIST_HOLD", "LIVE"), group="model"),
    Hypothesis("C2", "V2 disagreement", "Buying the side DATA_ONLY_V2 favours by >=5 points vs the market mid has positive net ROI.", "model",
               lambda d: d["model_gap"].abs() >= 0.05, ("HIST_DISC", "HIST_HOLD", "LIVE"), group="model"),
)
BY_ID = {h.id: h for h in REGISTRY}


def side_columns(d: pd.DataFrame, side: str, slip: float = 0.0) -> pd.DataFrame:
    """pnl/cost of the hypothesis' side at the displayed ask (+ ``slip`` dollars of slippage)."""
    d = d.copy()
    if side in ("model", "move", "move_rev"):
        sig = d["model_gap"] if side == "model" else (d["move"] if side == "move" else -d["move"])
        buy_yes = sig > 0
    else:
        buy_yes = pd.Series(side == "yes", index=d.index)
    ask = np.where(buy_yes, d["yes_ask"], d["no_ask"]) + slip
    ask = np.clip(ask, 0.01, 0.99)
    win = np.where(buy_yes, d["y"], 1 - d["y"])
    d["cost"] = ask + taker_fee(ask)
    d["pnl"] = win - d["cost"]
    d["gap_side"] = np.where(buy_yes, d["y"] - d["mid"], (1 - d["y"]) - (1 - d["mid"]))
    d["buy_yes"] = buy_yes
    return d


def evaluate(h: Hypothesis, df: pd.DataFrame, seed: int = 11) -> dict:
    sel = df[(df["horizon_min"] == DECISION_HORIZON_MIN) & h.select(df)]
    if h.side in ("model", "move", "move_rev"):
        col = "model_gap" if h.side == "model" else "move"
        sel = sel[sel[col].notna()]
    out = {"id": h.id, "n_contracts": int(len(sel)), "n_games": int(sel["game_id"].nunique())}
    if out["n_games"] == 0:
        return {**out, "roi": None}
    s = side_columns(sel, h.side)
    roi, lo, hi = cluster_ratio_ci(s, "pnl", "cost", n=N_BOOT, seed=seed)
    gp = cluster_ratio_ci(s, "gap_side", None, n=N_BOOT, seed=seed)
    # one-sided bootstrap p-value for ROI <= 0 (H1: ROI > 0)
    g = s.groupby("game_id")
    a, b = g["pnl"].sum().to_numpy(float), g["cost"].sum().to_numpy(float)
    rng = np.random.default_rng(seed)
    w = rng.multinomial(len(a), np.full(len(a), 1.0 / len(a)), size=N_BOOT).astype(float)
    draws = (w @ a) / (w @ b)
    p_one = float((np.sum(draws <= 0) + 1) / (N_BOOT + 1))
    lo90 = float(np.percentile(draws, 10))
    ss = side_columns(sel, h.side, slip=0.01)
    roi_slip = float(ss["pnl"].sum() / ss["cost"].sum())
    return {**out, "roi": roi, "roi_lo95": lo, "roi_hi95": hi, "roi_lo90": lo90, "p_one_sided": p_one, "gap": gp[0], "gap_lo95": gp[1],
            "gap_hi95": gp[2], "roi_slip_1c": roi_slip, "mean_cost": float(s["cost"].mean()), "mean_spread": float(sel["spread"].mean())}


def bh_adjust(pvals: dict[str, float]) -> dict[str, float]:
    items = sorted(pvals.items(), key=lambda kv: kv[1])
    m, out, prev = len(items), {}, 1.0
    for rank, (k, p) in reversed(list(enumerate(items, start=1))):
        prev = min(prev, p * m / rank)
        out[k] = prev
    return out


def classify(per_tier: dict[str, dict], q_live: float | None) -> str:
    testable = {t: r for t, r in per_tier.items() if r.get("roi") is not None and r["n_games"] >= 30}
    if not testable:
        return "UNTESTABLE"
    live, hold = testable.get("LIVE"), testable.get("HIST_HOLD")
    if live and live["n_games"] >= 100 and q_live is not None and q_live <= 0.10 and live["roi_lo90"] > 0 and live["roi_slip_1c"] > 0 \
            and (hold is None or hold["roi"] > 0):
        return "VALIDATED"
    if all(r["roi"] > 0 for r in testable.values()):
        return "PROMISING"
    big = [r for r in testable.values() if r["n_games"] >= 100]
    if all(r["roi"] < 0 for r in testable.values()) and any(r["roi_hi95"] < 0 for r in big):
        return "REJECTED"
    return "INCONCLUSIVE"
