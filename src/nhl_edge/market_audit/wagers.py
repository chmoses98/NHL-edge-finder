"""Actual routed wagers (accounting-data ledger), audited SEPARATELY from every research selection.

Reads ``nhl_accounted_wager.v1`` / ``nhl_wager_settlement.v1`` rows. Never mixed with model recommendations or backtests.
For each wager: the displayed board at the fill instant, slippage against it, time relative to scheduled puck drop,
whether the production thesis workflow ever considered the bet, the last pregame V1/V2 view, and expected value at the ACTUAL
fill price under several probability views. The ledger result is cross-checked against the independent outcome resolver.

Side convention: ``execution_price`` is the price of the contract actually bought (the NO price for a NO order).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.market_audit.efficiency import taker_fee


def load_ledger(accounting_dir: Path) -> pd.DataFrame:
    d = Path(accounting_dir) / "data" / "accounting"
    w = pd.DataFrame([json.loads(x) for x in open(d / "wagers.jsonl")])
    s = pd.DataFrame([json.loads(x) for x in open(d / "settlements.jsonl")])
    out = w.merge(s[["source_bet_key", "result", "net_profit_loss", "gross_return", "settlement_status"]], on="source_bet_key", how="left")
    out["executed_at"] = pd.to_datetime(out["executed_at"], utc=True)
    return out


def _asof(ev: pd.DataFrame, ticker: str, when: pd.Timestamp) -> pd.Series | None:
    e = ev[(ev["ticker"] == ticker) & (ev["available_at"] <= when)]
    return e.iloc[-1] if len(e) else None


def audit_wagers(ledger: pd.DataFrame, cm: pd.DataFrame, games: pd.DataFrame, outcomes: pd.DataFrame, ev: pd.DataFrame,
                 td: pd.DataFrame, p1: pd.DataFrame, p2: pd.DataFrame) -> pd.DataFrame:
    oc = outcomes.set_index("ticker")["outcome"]
    rows: list[dict[str, Any]] = []
    for w in ledger.sort_values("executed_at").itertuples():
        c = cm[cm["ticker"] == w.market_ticker]
        r: dict[str, Any] = {"wager_id": w.wager_id, "ticker": w.market_ticker, "side": w.side, "executed_at": w.executed_at, "price": w.execution_price,
                             "contracts": w.contracts, "stake": w.stake, "fee": w.fees_paid, "ledger_result": w.result, "net_pl": w.net_profit_loss}
        if c.empty:
            rows.append({**r, "note": "ticker not in game-scoped archive universe"})
            continue
        c = c.iloc[0]
        g = games[games["game_id"] == c["game_id"]].iloc[0]
        r.update(game_id=c["game_id"], family=c["family"], start=g["start_time_utc"])
        r["min_after_start"] = (w.executed_at - g["start_time_utc"]).total_seconds() / 60.0
        r["mine"] = oc.get(w.market_ticker)
        r["mine_agrees_with_ledger"] = (r["mine"] == "YES") == ((w.side == "YES") == (w.result == "WON")) if r["mine"] in ("YES", "NO") else None
        q = _asof(ev, w.market_ticker, w.executed_at)
        if q is not None and pd.notna(q["yes_bid"]) and pd.notna(q["yes_ask"]):
            yb, ya = q["yes_bid"] / 100, q["yes_ask"] / 100
            ask_side = ya if w.side == "YES" else 1 - yb
            mid_yes = (yb + ya) / 2
            r.update(board_tick=q["observed_at"], board_age_min=(w.executed_at - q["observed_at"]).total_seconds() / 60, board_ask=ask_side,
                     slippage_vs_board=w.execution_price - ask_side, board_mid_yes=mid_yes)
            win_p_mkt = mid_yes if w.side == "YES" else 1 - mid_yes
            fee = float(taker_fee(w.execution_price))
            r["ev_per_contract_market"] = win_p_mkt - w.execution_price - fee
        t = td[(td["ticker"] == w.market_ticker) & (td["side"] == w.side.lower())]
        r["n_thesis_decisions"] = int(len(t))
        r["thesis_ever_funded"] = bool((t["research_status"] == "FUNDED_RESEARCH").any()) if len(t) else False
        for lab, pr, col in (("v1", p1, "p_data_only"), ("v2", p2, "p_data_only_v2")):
            x = pr[(pr["ticker"] == w.market_ticker) & (pd.to_datetime(pr["predicted_at_utc"], utc=True) <= w.executed_at)].sort_values("predicted_at_utc")
            if len(x) and pd.notna(x.iloc[-1][col]):
                py = float(x.iloc[-1][col])
                pw = py if w.side == "YES" else 1 - py
                r[f"{lab}_p_win"] = pw
                r[f"{lab}_ev_per_contract"] = pw - w.execution_price - float(taker_fee(w.execution_price))
                r[f"{lab}_minutes_before_fill"] = (w.executed_at - pd.to_datetime(x.iloc[-1]["predicted_at_utc"], utc=True)).total_seconds() / 60
        rows.append(r)
    out = pd.DataFrame(rows)
    out["family_or_none"] = out.get("family")
    return out


def pnl_summary(df: pd.DataFrame) -> dict[str, Any]:
    d = df[df["ledger_result"].isin(["WON", "LOST"])]
    return {"n": int(len(d)), "staked": float(d["stake"].sum()), "net_pl": float(d["net_pl"].sum()), "roi_on_stake": float(d["net_pl"].sum() / d["stake"].sum()),
            "wins": int((d["ledger_result"] == "WON").sum()), "fees": float(d["fee"].sum())}
