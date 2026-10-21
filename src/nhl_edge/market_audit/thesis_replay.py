"""Walk-forward audit of the existing thesis workflow's selections (Phase H). RESEARCH SELECTIONS ONLY -- never mixed
with routed wagers.

Each LOGICAL bet (game|ticker|side) is scored ONCE, at the first snapshot where it met the selection rule, using the
executable price recorded in that snapshot (no hindsight price) and OUR independent outcome (not the production
postmortem). Repeated snapshots of one bet are not independent observations.

Controls: the workflow's own non-selected candidates for the same game, same family, same side, executable price within
+/-5c, scored at THEIR first snapshot. The matched-control test asks whether the selection layer (model EV ranking) picks
better contracts than comparable candidates it passed over -- i.e. whether selection carries skill beyond the market price.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import cluster_ratio_ci, taker_fee

GOAL_SCORER = ("player_goals", "first_goal")


def prepare(td: pd.DataFrame, outcomes: pd.DataFrame) -> pd.DataFrame:
    d = td.copy()
    d["t"] = pd.to_datetime(d["decided_at_utc"], utc=True)
    d["start"] = pd.to_datetime(d["start_time_utc"], utc=True)
    d = d.sort_values("t")
    oc = outcomes.set_index("ticker")["outcome"]
    d["outcome"] = d["ticker"].map(oc)
    d["price"] = d["executable_price_cents"] / 100.0
    d["cost"] = d["price"] + taker_fee(d["price"])
    d["win"] = np.where(d["side"] == "yes", d["outcome"] == "YES", d["outcome"] == "NO").astype(float)
    d["decided"] = d["outcome"].isin(["YES", "NO"])
    d["pnl"] = d["win"] - d["cost"]
    d["funded"] = d["research_status"] == "FUNDED_RESEARCH"
    return d


def first_snapshot(d: pd.DataFrame, mask: pd.Series) -> pd.DataFrame:
    return d[mask].groupby("logical_wager_key", as_index=False).head(1)


def last_card(d: pd.DataFrame) -> pd.DataFrame:
    """The final pre-start card: per game, the last snapshot's chosen bets."""
    last_t = d.groupby("game_id")["t"].transform("max")
    return d[(d["t"] == last_t) & d["chosen"]]


def score(sel: pd.DataFrame, label: str) -> dict:
    s = sel[sel["decided"]]
    if s.empty:
        return {"label": label, "n_bets": 0}
    roi = cluster_ratio_ci(s, "pnl", "cost")
    stake_w = None
    if "research_stake_dollars" in s and s["research_stake_dollars"].sum() > 0:
        w = s["research_stake_dollars"]
        stake_w = float((w * s["pnl"] / s["cost"]).sum() / w.sum())
    return {"label": label, "n_bets": int(len(s)), "n_games": int(s["game_id"].nunique()), "n_void_or_unscored": int(len(sel) - len(s)),
            "mean_price": float(s["price"].mean()), "hit_rate": float(s["win"].mean()), "roi_net": roi[0], "roi_lo95": roi[1], "roi_hi95": roi[2],
            "stake_weighted_roi": stake_w, "mean_ev_adjusted_claimed": float(s["ev_adjusted"].mean()) if "ev_adjusted" in s else None,
            "realized_minus_claimed_ev_per_contract": float((s["pnl"] / 1.0).mean() - s["ev_adjusted"].mean()) if "ev_adjusted" in s else None}


def matched_control_test(sel: pd.DataFrame, pool: pd.DataFrame, n_draw: int = 2000, seed: int = 3) -> dict:
    """Permutation test: does ``sel`` beat randomly drawn comparable non-selected candidates (same game/family/side, +-5c)?"""
    rng = np.random.default_rng(seed)
    s = sel[sel["decided"]]
    cand = pool[pool["decided"] & ~pool["logical_wager_key"].isin(set(sel["logical_wager_key"]))]
    groups = {k: v for k, v in cand.groupby(["game_id", "family", "side"])}
    matches = []
    for r in s.itertuples():
        g = groups.get((r.game_id, r.family, r.side))
        if g is None:
            continue
        m = g[(g["price"] - r.price).abs() <= 0.05]
        if len(m):
            matches.append((r.pnl, r.cost, m["pnl"].to_numpy(), m["cost"].to_numpy()))
    if len(matches) < 20:
        return {"n_matched": len(matches), "note": "too few matched candidates"}
    sel_roi = sum(a for a, *_ in matches) / sum(b for _, b, *_ in matches)
    draws = np.empty(n_draw)
    for i in range(n_draw):
        num = den = 0.0
        for _, _, pn, cs in matches:
            j = rng.integers(len(pn))
            num += pn[j]
            den += cs[j]
        draws[i] = num / den
    return {"n_matched": len(matches), "selected_roi": float(sel_roi), "control_roi_mean": float(draws.mean()), "control_roi_lo95": float(np.percentile(draws, 2.5)),
            "control_roi_hi95": float(np.percentile(draws, 97.5)), "p_selected_beats_control": float((np.sum(draws >= sel_roi) + 1) / (n_draw + 1))}


def ev_quintiles(sel: pd.DataFrame) -> list[dict]:
    s = sel[sel["decided"]].copy()
    s["q"] = pd.qcut(s["ev_adjusted"], 5, duplicates="drop")
    out = []
    for q, x in s.groupby("q", observed=True):
        r = cluster_ratio_ci(x, "pnl", "cost", n=1000)
        out.append({"ev_adjusted_bin": str(q), "n": int(len(x)), "games": int(x["game_id"].nunique()), "claimed_ev": float(x["ev_adjusted"].mean()),
                    "realized_roi": r[0], "lo95": r[1], "hi95": r[2]})
    return out
