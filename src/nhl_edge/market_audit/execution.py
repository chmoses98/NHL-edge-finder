"""Executability (Phase H): price a hypothetical taker order by WALKING the archived order book, never by assuming the touch.

Kalshi books list only bids. Buying YES at price p fills against resting NO bids at 100-p; buying NO fills against YES bids.
``walk(levels, n)`` takes the best prices first and returns (filled, vwap_cents); an order larger than visible depth is
partially filled and the shortfall is reported. The archive samples depth to 10 levels per side and only for the four
MODELABLE families, so executability is only measurable there; everything else is reported as DEPTH-UNOBSERVED.

Quote / liquidity / hypothetical-fill / real-fill are four different things and are kept apart: the board gives the quote,
the book gives liquidity, ``walk`` gives a hypothetical fill, and only the routed-wager ledger holds real fills.
"""

from __future__ import annotations

import json

import numpy as np
import pandas as pd

from nhl_edge.market_audit.efficiency import taker_fee


def walk(levels: list[list[float]], n: float) -> tuple[float, float]:
    """``levels`` = resting bid ladder of the OPPOSITE side as [price_cents, size]; returns (filled, vwap price in cents of the contract bought)."""
    got, cost = 0.0, 0.0
    for price, size in sorted(levels, key=lambda x: -x[0]):
        take = min(n - got, size)
        got += take
        cost += take * (100.0 - price)
        if got >= n:
            break
    return (got, cost / got if got else np.nan)


def book_at_cut(book_ev: pd.DataFrame, cuts: pd.DataFrame) -> pd.DataFrame:
    """Latest book whose ``available_at`` <= cut, per ticker (change log carried forward)."""
    b = book_ev.sort_values("available_at")
    c = cuts.sort_values("cut")
    return pd.merge_asof(c, b[["ticker", "available_at", "observed_at", "yes_levels", "no_levels"]], left_on="cut", right_on="available_at", by="ticker",
                         direction="backward", suffixes=("", "_book"))


def price_orders(df: pd.DataFrame, buy_yes: pd.Series, sizes: tuple[int, ...] = (50, 200)) -> pd.DataFrame:
    out = df.copy()
    ylv = out["yes_levels"].map(lambda s: json.loads(s) if isinstance(s, str) else [])
    nlv = out["no_levels"].map(lambda s: json.loads(s) if isinstance(s, str) else [])
    for n in sizes:
        res = [walk(nl if by else yl, n) for by, yl, nl in zip(buy_yes, ylv, nlv, strict=True)]
        out[f"filled_{n}"] = [r[0] for r in res]
        out[f"vwap_{n}"] = [r[1] / 100.0 for r in res]
    return out


def book_walk_roi(sel: pd.DataFrame, n: int) -> dict:
    """Net ROI when every selected order is a taker order of ``n`` contracts walking the book (partial fills scaled)."""
    s = sel[(sel[f"filled_{n}"] > 0)].copy()
    px = s[f"vwap_{n}"]
    cost = px + taker_fee(px)
    win = np.where(s["buy_yes"], s["y"], 1 - s["y"])
    w = s[f"filled_{n}"]
    return {"n_orders": int(len(sel)), "n_any_fill": int(len(s)), "full_fill_pct": round(100 * float((sel[f"filled_{n}"] >= n).mean()), 1),
            "mean_vwap_minus_touch_cents": round(float((100 * (px - s["touch_price"])).mean()), 2),
            "roi_net": float(((win - cost) * w).sum() / (cost * w).sum()) if len(s) else None}
