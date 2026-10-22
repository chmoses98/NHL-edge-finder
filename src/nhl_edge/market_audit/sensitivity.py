"""Sensitivity of registered strategies' net ROI to fees, slippage and decision timing (Phase H).

ROI = sum(win - ask_with_slippage - fee_mult * 0.07 p (1-p)) / sum(ask_with_slippage + fee). Fee multiplier 0 shows the
pre-fee (spread-only) economics; 1.0 is Kalshi's published taker schedule (verified to the cent on routed fills).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from nhl_edge.market_audit import hypotheses as H
from nhl_edge.market_audit.efficiency import cluster_ratio_ci


def roi_grid(df: pd.DataFrame, h: H.Hypothesis, horizons=(60, 10, 0), fee_mults=(0.0, 1.0, 1.5), slips=(0.0, 0.01, 0.02)) -> list[dict]:
    out = []
    for hz in horizons:
        d = df[(df["horizon_min"] == hz)]
        if d.empty:
            continue
        sel = d[h.select(d)]
        if sel.empty:
            continue
        buy_yes = h.side == "yes"
        for fm in fee_mults:
            for sl in slips:
                ask = np.clip((sel["yes_ask"] if buy_yes else sel["no_ask"]) + sl, 0.01, 0.99)
                fee = fm * 0.07 * ask * (1 - ask)
                win = sel["y"] if buy_yes else 1 - sel["y"]
                t = sel.assign(pnl=win - ask - fee, cost=ask + fee)
                roi, lo, hi = cluster_ratio_ci(t, "pnl", "cost", n=1000)
                out.append({"id": h.id, "horizon_min": hz, "fee_mult": fm, "slip": sl, "roi": roi, "lo95": lo, "hi95": hi, "n_games": int(t["game_id"].nunique())})
    return out
