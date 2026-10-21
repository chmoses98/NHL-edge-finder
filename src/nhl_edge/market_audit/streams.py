"""Stream every archived Kalshi board tick into compact, queryable event tables.

Reuses ``nhl_edge.archive.reconstruct.iter_board_ticks`` (checkpoint + hash-verified delta chain, fails closed), so the
reconstruction path is the one the production archive already trusts. This module only *reads*.

Outputs (parquet, derived, reproducible from the archive bytes):

* ``ticks``           one row per captured board tick and kind (markets / orderbooks): instant, run, encoding, size, hash
* ``quote_events``    one row per (ticker, tick) at which a game-scoped market's quote/state first appeared or CHANGED
* ``market_static``   one row per ticker: static contract facts + first/last tick seen + terminal status/result
* ``book_events``     one row per (ticker, tick) at which a sampled order book first appeared or changed

``quote_events`` is a change log, not a full panel. As-of lookups carry the last event forward and bound staleness by the
tick table, never by the event time (a quiet market is not a stale market).
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.archive.delta import ORDERBOOK_CHECKPOINT_KIND, ORDERBOOK_DELTA_KIND
from nhl_edge.archive.ledger import Ledger
from nhl_edge.archive.reconstruct import iter_board_ticks
from nhl_edge.kalshi.ticker import parse_ticker
from nhl_edge.market_audit import MARKET_AVAILABLE_LAG_S, ORDERBOOK_AVAILABLE_LAG_S
from nhl_edge.timeutil import iso

_QUOTE_FIELDS = ("yes_bid", "yes_ask", "no_bid", "no_ask", "last_price")
_STATE_FIELDS = ("status", "result")
_SIZE_FIELDS = ("yes_bid_size_fp", "yes_ask_size_fp")
_VOL_FIELDS = ("volume_fp", "open_interest_fp")

_STATIC_FIELDS = (
    "event_ticker", "series_ticker", "title", "yes_sub_title", "no_sub_title", "subtitle", "strike_type", "floor_strike",
    "custom_strike", "rules_primary", "rules_secondary", "open_time", "close_time", "expected_expiration_time",
    "expiration_time", "occurrence_datetime", "created_time", "market_type", "_family", "_support",
)


def _f(v: Any) -> float | None:
    if v in (None, ""):
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def is_game_scoped(ticker: str, _cache: dict[str, bool] = {}) -> bool:  # noqa: B006 - intentional memo
    """True when the event suffix encodes a game date (single-game markets, props included). Season futures/awards
    and other undated events are False. This is a SCOPE filter only; contract semantics come from structured fields."""
    hit = _cache.get(ticker)
    if hit is None:
        pt = parse_ticker(ticker)
        hit = pt.game_date is not None
        _cache[ticker] = hit
    return hit


def _quote_row(r: dict[str, Any]) -> dict[str, Any]:
    q = r.get("_quote_cents") or {}
    return {
        "yes_bid": q.get("yes_bid"), "yes_ask": q.get("yes_ask"), "no_bid": q.get("no_bid"), "no_ask": q.get("no_ask"),
        "last_price": q.get("last_price"),
        "yes_bid_size": _f(r.get("yes_bid_size_fp")), "yes_ask_size": _f(r.get("yes_ask_size_fp")),
        "volume": _f(r.get("volume_fp")), "open_interest": _f(r.get("open_interest_fp")),
        "status": r.get("status"), "result": r.get("result") or "",
    }


def iter_ticks(ledger: Ledger, *, orderbooks: bool = False) -> Iterator[tuple[datetime, str, dict[str, dict[str, Any]], bool]]:
    ck, dk = (ORDERBOOK_CHECKPOINT_KIND, ORDERBOOK_DELTA_KIND) if orderbooks else ("kalshi/markets", "kalshi/markets_delta")
    for at, run_id, board, raw in iter_board_ticks(ledger, checkpoint_kind=ck, delta_kind=dk):
        yield at, run_id, board, raw is not None


def stream_market_events(archive_root: Path) -> dict[str, pd.DataFrame]:
    ledger = Ledger(Path(archive_root))
    ticks: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    static: dict[str, dict[str, Any]] = {}
    prev: dict[str, tuple] = {}
    n_all_max = 0
    for at, run_id, board, is_ck in iter_ticks(ledger):
        ticks.append({"kind": "markets", "observed_at": at, "run_id": run_id, "encoding": "checkpoint" if is_ck else "delta",
                      "n_markets_all": len(board)})
        n_all_max = max(n_all_max, len(board))
        n_game = 0
        for tk, r in board.items():
            if "_error" in r or not is_game_scoped(tk):
                continue
            n_game += 1
            row = _quote_row(r)
            sig = tuple(row.values())
            if prev.get(tk) != sig:
                prev[tk] = sig
                row.update(ticker=tk, observed_at=at)
                events.append(row)
            s = static.get(tk)
            if s is None:
                s = {"ticker": tk, "first_seen": at, **{k: r.get(k) for k in _STATIC_FIELDS}}
                static[tk] = s
            s["last_seen"] = at
            for k in ("status", "result", "close_time", "expiration_time", "expected_expiration_time", "occurrence_datetime"):
                if r.get(k) not in (None, ""):
                    s[k] = r.get(k)
        ticks[-1]["n_game_markets"] = n_game
    st = pd.DataFrame(static.values())
    for c in ("custom_strike",):
        if c in st:
            st[c] = st[c].map(lambda v: json.dumps(v, sort_keys=True, default=str) if v is not None else None)
    ev = pd.DataFrame(events)
    tk_df = pd.DataFrame(ticks)
    ev["available_at"] = ev["observed_at"] + timedelta(seconds=MARKET_AVAILABLE_LAG_S)
    return {"ticks_markets": tk_df, "quote_events": ev, "market_static": st}


def _levels(v: Any) -> list[list[float]]:
    return [[float(p), float(s)] for p, s in (v or [])]


def stream_book_events(archive_root: Path) -> dict[str, pd.DataFrame]:
    ledger = Ledger(Path(archive_root))
    ticks: list[dict[str, Any]] = []
    events: list[dict[str, Any]] = []
    prev: dict[str, str] = {}
    for at, run_id, board, is_ck in iter_ticks(ledger, orderbooks=True):
        errs = sum(1 for r in board.values() if "_error" in r)
        ticks.append({"kind": "orderbooks", "observed_at": at, "run_id": run_id, "encoding": "checkpoint" if is_ck else "delta",
                      "n_books": len(board) - errs, "n_errors": errs})
        for tk, r in board.items():
            if "_error" in r:
                continue
            yes, no = _levels(r.get("yes")), _levels(r.get("no"))
            sig = json.dumps([yes, no], separators=(",", ":"))
            if prev.get(tk) == sig:
                continue
            prev[tk] = sig
            events.append({"ticker": tk, "observed_at": at, "yes_levels": json.dumps(yes), "no_levels": json.dumps(no),
                           "yes_bid_depth": sum(s for _, s in yes), "no_bid_depth": sum(s for _, s in no),
                           "best_yes_bid": max((p for p, _ in yes), default=None), "best_no_bid": max((p for p, _ in no), default=None)})
    ev = pd.DataFrame(events)
    ev["available_at"] = ev["observed_at"] + timedelta(seconds=ORDERBOOK_AVAILABLE_LAG_S)
    return {"ticks_orderbooks": pd.DataFrame(ticks), "book_events": ev}


def save_tables(tables: dict[str, pd.DataFrame], out_dir: Path) -> dict[str, dict[str, Any]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    info = {}
    for name, df in tables.items():
        p = out_dir / f"{name}.parquet"
        df.to_parquet(p, index=False)
        info[name] = {"rows": int(len(df)), "path": p.name}
    return info


def iso_or_none(v: Any) -> str | None:
    return iso(v) if isinstance(v, datetime) else None
