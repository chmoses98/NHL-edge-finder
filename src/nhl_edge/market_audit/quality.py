"""Data-quality and temporal-integrity audit (Phase A). Pure functions over the derived tables; every number is reported,
nothing is silently dropped.

Checks
    Q1  one-sided / missing quotes at the last pregame tick, by family
    Q2  tip-straddle contamination: ticks stamped before puck drop whose capture window ends AFTER it
    Q3  order-book sampling bias: which families / horizons ever receive a depth sample
    Q4  board vs order book, same tick: best bid agreement (the book is fetched ~60 s after the board)
    Q5  capture-time family classification (``_family``) vs the independent taxonomy
    Q6  production prediction inputs vs the archived board at the instant they claim (input fidelity)
    Q7  duplicate / repeated-evidence accounting (rows vs independent games)
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from nhl_edge.market_audit import MARKET_AVAILABLE_LAG_S, ORDERBOOK_AVAILABLE_LAG_S


def q1_onesided(ev: pd.DataFrame, cm: pd.DataFrame, games: pd.DataFrame) -> list[dict[str, Any]]:
    e = ev.merge(cm[["ticker", "game_id", "family"]], on="ticker").merge(games[["game_id", "start_time_utc", "is_final"]], on="game_id")
    e = e[e["is_final"] & (e["available_at"] <= e["start_time_utc"])].sort_values("observed_at").groupby("ticker", as_index=False).tail(1)
    out = []
    for fam, x in e.groupby("family"):
        out.append({"family": fam, "contracts": int(len(x)), "two_sided_pct": round(100 * float((x["yes_bid"].notna() & x["yes_ask"].notna()).mean()), 1),
                    "no_bid_pct": round(100 * float(x["yes_bid"].isna().mean()), 1), "no_ask_pct": round(100 * float(x["yes_ask"].isna().mean()), 1),
                    "median_spread_cents": float(((x["yes_ask"] - x["yes_bid"]).dropna()).median()) if (x["yes_ask"] - x["yes_bid"]).notna().any() else None})
    return out


def q2_straddle(ticks_m: pd.DataFrame, ticks_b: pd.DataFrame, games: pd.DataFrame) -> dict[str, Any]:
    fin = games[games["is_final"]]
    mt, bt = ticks_m["observed_at"].sort_values().reset_index(drop=True), ticks_b["observed_at"].sort_values().reset_index(drop=True)
    n_m = n_b = 0
    worst = []
    for g in fin.itertuples():
        pre_m = mt[mt < g.start_time_utc]
        pre_b = bt[bt < g.start_time_utc]
        if len(pre_m) and (g.start_time_utc - pre_m.iloc[-1]).total_seconds() < MARKET_AVAILABLE_LAG_S:
            n_m += 1
            worst.append(g.game_id)
        if len(pre_b) and (g.start_time_utc - pre_b.iloc[-1]).total_seconds() < ORDERBOOK_AVAILABLE_LAG_S:
            n_b += 1
    return {"final_games": int(len(fin)), "games_whose_last_stamped_pregame_market_tick_ends_after_start": n_m,
            "games_whose_last_stamped_pregame_book_tick_ends_after_start": n_b,
            "note": f"stamp = capture START; fully written ~{MARKET_AVAILABLE_LAG_S}s (markets) / ~{ORDERBOOK_AVAILABLE_LAG_S}s (books) later. "
                    "Point-in-time logic uses stamp+lag, so these ticks are EXCLUDED from pregame use; a naive stamp-only filter would have admitted them."}


def q3_book_sampling(book_ev: pd.DataFrame, cm: pd.DataFrame, ev: pd.DataFrame, games: pd.DataFrame) -> dict[str, Any]:
    b = book_ev.merge(cm[["ticker", "family", "game_id"]], on="ticker", how="left")
    live = ev.merge(cm[["ticker", "family", "game_id"]], on="ticker").merge(games[["game_id", "is_final"]], on="game_id")
    live = live[live["is_final"]].drop_duplicates("ticker")
    cov = []
    live_tickers = set(live["ticker"])
    for fam, x in live.groupby("family"):
        have = b[(b["family"] == fam) & b["ticker"].isin(live_tickers)]["ticker"].nunique()
        cov.append({"family": fam, "contracts": int(len(x)), "with_any_book": int(have), "pct": round(100 * have / len(x), 1)})
    return {"by_family": cov, "selection_rule": "snapshot_orderbooks(): live markets sorted by (support rank MODELABLE first, has a quote, earliest expiry), "
            "first 300 per tick. Only game_winner/game_spread/game_total/team_total are MODELABLE, so only they can ever be sampled."}


def q4_board_vs_book(ev: pd.DataFrame, book_ev: pd.DataFrame) -> dict[str, Any]:
    """Compare best yes bid on the board with best yes bid in the order book, at the tick pair (board tick t, book tick t)."""
    e = ev[["ticker", "observed_at", "yes_bid", "yes_ask"]].dropna()
    b = book_ev[["ticker", "observed_at", "best_yes_bid", "best_no_bid"]].dropna(subset=["best_yes_bid"])
    m = e.merge(b, on=["ticker", "observed_at"], how="inner")
    if m.empty:
        return {"n": 0}
    m["bid_diff"] = m["yes_bid"] - m["best_yes_bid"]
    m["ask_diff"] = m["yes_ask"] - (100 - m["best_no_bid"])
    return {"n_event_pairs_compared": int(len(m)), "bid_exact_pct": round(100 * float((m["bid_diff"] == 0).mean()), 2),
            "ask_exact_pct": round(100 * float((m["ask_diff"].dropna() == 0).mean()), 2),
            "bid_abs_diff_cents_p50_p90_p99": [float(m["bid_diff"].abs().quantile(q)) for q in (.5, .9, .99)],
            "note": "pairs exist only where BOTH the board row and the book row changed at that tick, so this OVERSTATES disagreement; quiet-market agreement is "
                    "not observable from a change log."}


def q5_family_classification(static: pd.DataFrame, cm: pd.DataFrame) -> dict[str, Any]:
    m = static[["ticker", "_family", "_support"]].merge(cm[["ticker", "family"]], on="ticker")
    mism = m[m["_family"] != m["family"]]
    return {"n": int(len(m)), "n_mismatch": int(len(mism)), "mismatch_pairs": mism.groupby(["_family", "family"]).size().reset_index(name="n").to_dict("records"),
            "capture_support_by_family": m.groupby(["family", "_support"]).size().reset_index(name="n").to_dict("records")}


def q6_prediction_inputs(p1: pd.DataFrame, ev: pd.DataFrame, sample: int = 20000, seed: int = 5) -> dict[str, Any]:
    """Do the market fields frozen on a V1 prediction equal the archived board AT the claimed ``market_observed_at_utc`` tick?"""
    s = p1.sample(min(sample, len(p1)), random_state=seed)[["ticker", "market_observed_at_utc", "market_yes_bid", "market_yes_ask"]].copy()
    s["obs"] = pd.to_datetime(s["market_observed_at_utc"], utc=True)
    e = ev.sort_values("observed_at")[["ticker", "observed_at", "yes_bid", "yes_ask"]]
    m = pd.merge_asof(s.sort_values("obs"), e, left_on="obs", right_on="observed_at", by="ticker", direction="backward")
    ok = m.dropna(subset=["yes_bid", "market_yes_bid"])
    return {"n": int(len(ok)), "bid_match_pct": round(100 * float((ok["market_yes_bid"] == ok["yes_bid"]).mean()), 2),
            "ask_match_pct": round(100 * float((m.dropna(subset=["yes_ask", "market_yes_ask"])["market_yes_ask"] == m.dropna(subset=["yes_ask", "market_yes_ask"])["yes_ask"]).mean()), 2),
            "max_tick_gap_s": float((m["obs"] - m["observed_at"]).dt.total_seconds().max())}


def q7_repeated_evidence(p1: pd.DataFrame, td: pd.DataFrame, games: pd.DataFrame) -> dict[str, Any]:
    return {"v1_prediction_rows": int(len(p1)), "v1_unique_tickers": int(p1["ticker"].nunique()),
            "v1_decision_runs_per_game_median": float(p1.groupby("game_id")["_run_id"].nunique().median()),
            "thesis_decision_rows": int(len(td)), "thesis_unique_logical_bets": int(td["logical_wager_key"].nunique()),
            "independent_final_games": int(games["is_final"].sum()),
            "rows_per_independent_game_v1": round(len(p1) / max(int(games["is_final"].sum()), 1), 1)}
