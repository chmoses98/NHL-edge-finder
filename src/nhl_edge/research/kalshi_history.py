"""Historical Kalshi NHL markets + candlesticks for the market benchmark (research only; adapted from nba-edge-finder).

What this pulls (from a network-capable runner; the dev container reaches no Kalshi host):

1. For every requested series, settled/finalized markets closing in ``[min_close, max_close]`` from BOTH the
   historical host (``/historical/markets``) and the live host (``/markets?status=settled``), merged by ticker
   (historical keys win, live fills gaps, ``_source`` records which). Written to ``markets_<SERIES>.jsonl.gz``.
2. Candlesticks, aligned to the official NHL start time of the game each market belongs to (joined from the
   NHL history Parquet, never guessed):
   * hourly candles over ``[start - 48h, start + 1h]`` (horizons T-24h .. T-3h);
   * one-minute candles over ``[start - 3h15m, start + 5m]`` (horizons T-90m .. T-10m) for the priority families.
   Candle rows are slimmed to what the benchmark reads: ``end_period_ts``, YES bid/ask close (and OHLC),
   trade price close/mean, volume, open interest. A candle's quote describes the book at ``end_period_ts``;
   the benchmark only ever reads candles whose ``end_period_ts`` is at or before the horizon instant.
3. ``MANIFEST.json`` with counts, coverage, errors and the exact windows used.

Candle pulls are incremental (tickers already present in a file are skipped) and bounded by a wall-clock budget
so a slow host yields a partial but honest file rather than a timed-out job. Selection is priority ordered:
KXNHLGAME first, then the common total / spread / team-total strikes, then the rest.

Nothing here is an executable historical price: Kalshi candles expose the best bid/ask at the close of each
period, not depth. The benchmark says so on every table.
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import pandas as pd

from nhl_edge.kalshi.client import KalshiClient, KalshiError, RateLimiter
from nhl_edge.kalshi.ticker import parse_ticker
from nhl_edge.log import get_logger, kv
from nhl_edge.timeutil import iso, parse_iso, utcnow

log = get_logger(__name__)

ET = ZoneInfo("America/New_York")
CORE_SERIES = ("KXNHLGAME", "KXNHLTOTAL", "KXNHLSPREAD", "KXNHLTEAMTOTAL")
EXTRA_SERIES = ("KXNHLOT", "KXNHLOVERTIME", "KXNHL1P", "KXNHL2P", "KXNHL3P", "KXNHL1PTOTAL", "KXNHL2PTOTAL", "KXNHL3PTOTAL",
                "KXNHL1PSPREAD", "KXNHL2PSPREAD", "KXNHL3PSPREAD", "KXNHLF10G", "KXNHL1PBTTS", "KXNHLFIRSTGOAL")
MINUTE_SERIES = ("KXNHLGAME", "KXNHLTOTAL")
# strikes pulled first for the ladder families (the common thresholds the benchmark scores); the rest follow
PRIORITY_STRIKES = {"KXNHLTOTAL": {5.5, 6.5}, "KXNHLSPREAD": {1.5}, "KXNHLTEAMTOTAL": {2.5, 3.5}}
SERIES_PRIORITY = {"KXNHLGAME": 0, "KXNHLTOTAL": 1, "KXNHLSPREAD": 2, "KXNHLTEAMTOTAL": 3}
HOURLY_BEFORE_S = 48 * 3600
MINUTE_BEFORE_S = 3 * 3600 + 15 * 60

# Kalshi NHL tickers use short codes for a few clubs; history uses canonical abbreviations. Franchise-level keys
# so a 2024-25 Utah Hockey Club game (UHC) matches Kalshi's "UTA". This is identity, not inference: the NHL
# schedule decides the game, the ticker only has to name the same two franchises on the same ET date.
FRANCHISE = {"UHC": "UTA", "ARI": "UTA", "LA": "LAK", "NJ": "NJD", "SJ": "SJS", "TB": "TBL", "MON": "MTL", "WAS": "WSH",
             "VEG": "VGK", "LV": "VGK", "CAL": "CGY", "WIN": "WPG", "NAS": "NSH", "CLB": "CBJ", "UTAH": "UTA"}


def fkey(abbrev: str | None) -> str | None:
    if not abbrev:
        return None
    a = str(abbrev).upper()
    return FRANCHISE.get(a, a)


def _ts(value: str) -> int:
    v = value.strip()
    if len(v) == 10:
        return int(datetime.fromisoformat(v).replace(tzinfo=UTC).timestamp())
    return int(parse_iso(v).timestamp())


def _ts_or_none(value: Any) -> int | None:
    if value in (None, ""):
        return None
    if isinstance(value, int | float):
        return int(value)
    try:
        return int(parse_iso(str(value)).timestamp())
    except (ValueError, TypeError):
        return None


def _write_jsonl_gz(path: Path, rows: list[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "wt") as f:
        for r in rows:
            f.write(json.dumps(r, default=str, sort_keys=True) + "\n")
    return len(rows)


def read_jsonl_gz(path: Path) -> list[dict[str, Any]]:
    if not Path(path).exists():
        return []
    out = []
    with gzip.open(path, "rt") as f:
        for line in f:
            if line.strip():
                out.append(json.loads(line))
    return out


def merge_markets(historical: list[dict[str, Any]], live: list[dict[str, Any]], series: str) -> list[dict[str, Any]]:
    """Merge by ticker. Historical keys win; live fills missing keys. ``_source`` records provenance."""
    merged: dict[str, dict[str, Any]] = {}
    for m in live:
        tk = m.get("ticker")
        if tk:
            merged[tk] = dict(m) | {"_source": "live"}
    for m in historical:
        tk = m.get("ticker")
        if not tk:
            continue
        if tk in merged:
            merged[tk].update({k: v for k, v in m.items() if v not in (None, "")})
            merged[tk]["_source"] = "both"
        else:
            merged[tk] = dict(m) | {"_source": "historical"}
    for row in merged.values():
        row.setdefault("series_ticker", series)
    return [merged[k] for k in sorted(merged)]


# ------------------------------------------------------------------------------------------------------------------
# game identity
# ------------------------------------------------------------------------------------------------------------------
def schedule_index(nhl_games: pd.DataFrame) -> dict[tuple[str, frozenset[str]], dict[str, Any]]:
    """(ET date, {franchise keys}) -> game row with its UTC start. Games with an ambiguous key are dropped."""
    idx: dict[tuple[str, frozenset[str]], dict[str, Any]] = {}
    dup: set[tuple[str, frozenset[str]]] = set()
    for r in nhl_games.itertuples(index=False):
        h, a = fkey(getattr(r, "home_abbrev", None)), fkey(getattr(r, "away_abbrev", None))
        if not h or not a:
            continue
        k = (str(r.game_date)[:10], frozenset({h, a}))
        start = None
        st = getattr(r, "start_time_et", None)
        if st is not None and str(st) not in ("", "None", "nan", "NaT"):
            t = pd.Timestamp(str(st))
            t = t.tz_localize(ET) if t.tzinfo is None else t
            start = int(t.tz_convert("UTC").timestamp())
        if k in idx:
            dup.add(k)
        idx[k] = {"game_id": int(r.game_id), "season": int(r.season), "game_type": int(r.game_type), "home": h, "away": a,
                  "start_ts": start, "game_date": str(r.game_date)[:10]}
    for k in dup:
        idx.pop(k, None)
    return idx


def market_game(m: dict[str, Any], idx: dict[tuple[str, frozenset[str]], dict[str, Any]]) -> tuple[dict[str, Any] | None, str]:
    """Join one Kalshi market to the NHL game it is about, or say why not. Uses the event ticker's date and team pair."""
    pt = parse_ticker(str(m.get("event_ticker") or m.get("ticker") or ""))
    if not pt.game_date or not pt.away_tricode or not pt.home_tricode:
        return None, "ticker not game-scoped"
    a, h = fkey(pt.away_tricode), fkey(pt.home_tricode)
    g = idx.get((pt.game_date.isoformat(), frozenset({a, h})))
    if g is None:
        # tolerant split: short codes (LA, NJ, SJ, TB) change where AWAY/HOME split; try every cut
        teams = str(pt.away_tricode) + str(pt.home_tricode)
        for cut in range(2, len(teams) - 1):
            k = (pt.game_date.isoformat(), frozenset({fkey(teams[:cut]), fkey(teams[cut:])}))
            if k in idx:
                g = idx[k]
                break
    if g is None:
        return None, "no NHL game with that date and team pair"
    return g, "ok"


def strike_of(m: dict[str, Any]) -> float | None:
    for k in ("floor_strike", "cap_strike"):
        v = m.get(k)
        if v not in (None, ""):
            try:
                return float(v)
            except (TypeError, ValueError):
                pass
    return None


def _slim_candle(c: dict[str, Any]) -> dict[str, Any]:
    yb, ya, pr = c.get("yes_bid") or {}, c.get("yes_ask") or {}, c.get("price") or {}

    def px(d: Any, k: str) -> float | None:
        """Dollar price: ``<k>_dollars`` strings win; a bare ``<k>`` is dollars when it is a decimal string/float and
        cents when it is an integer (the two payload generations Kalshi has served)."""
        if not isinstance(d, dict):
            return None
        v = d.get(f"{k}_dollars")
        if v not in (None, ""):
            return _num(v)
        v = d.get(k)
        if v in (None, ""):
            return None
        if isinstance(v, int) or (isinstance(v, str) and v.strip().lstrip("-").isdigit()):
            return _num(v) / 100.0 if _num(v) is not None else None
        return _num(v)

    return {"end_period_ts": c.get("end_period_ts"), "yes_bid_close": px(yb, "close"), "yes_ask_close": px(ya, "close"),
            "yes_bid_open": px(yb, "open"), "yes_ask_open": px(ya, "open"), "yes_bid_high": px(yb, "high"), "yes_ask_low": px(ya, "low"),
            "price_close": px(pr, "close"), "price_mean": px(pr, "mean"), "price_previous": px(pr, "previous"),
            "volume": c.get("volume") if c.get("volume") is not None else c.get("volume_fp"),
            "open_interest": c.get("open_interest") if c.get("open_interest") is not None else c.get("open_interest_fp")}


def candle_jobs(markets: list[dict[str, Any]], idx: dict[tuple[str, frozenset[str]], dict[str, Any]], skip: set[tuple[str, int]]) -> list[dict[str, Any]]:
    """Every (ticker, interval, window) fetch the benchmark wants, priority ordered."""
    jobs = []
    for m in markets:
        st = m.get("series_ticker") or str(m.get("ticker", "")).split("-")[0]
        g, why = market_game(m, idx)
        if g is None or g.get("start_ts") is None:
            continue
        start = int(g["start_ts"])
        pri = SERIES_PRIORITY.get(st, 9)
        strikes = PRIORITY_STRIKES.get(st)
        if strikes is not None:
            s = strike_of(m)
            pri = pri + (0 if (s is not None and s in strikes) else 10)
        open_ts = _ts_or_none(m.get("open_time")) or start - HOURLY_BEFORE_S
        base = {"ticker": m["ticker"], "series_ticker": st, "game_id": g["game_id"], "start_ts": start}
        if (m["ticker"], 60) not in skip:
            jobs.append(base | {"interval": 60, "t0": max(open_ts - 3600, start - HOURLY_BEFORE_S), "t1": start + 3600, "_pri": pri})
        if st in MINUTE_SERIES and (m["ticker"], 1) not in skip:
            jobs.append(base | {"interval": 1, "t0": start - MINUTE_BEFORE_S, "t1": start + 300, "_pri": pri + 0.5})
    jobs.sort(key=lambda j: (j["_pri"], j["start_ts"], j["ticker"], j["interval"]))
    return jobs


def run_kalshi_history(out_root: Path, history_root: Path, series: list[str], min_close: str, max_close: str, rate_per_s: float = 12.0,
                       client: Any | None = None) -> int:
    """Settled markets per series (historical + live hosts merged) and the manifest; candles are a separate pass."""
    from nhl_edge.data.history import load_nhl_games

    t_start = time.time()
    client = client or KalshiClient(rate=RateLimiter(rate_per_s=rate_per_s))
    out = Path(out_root) / "kalshi"
    out.mkdir(parents=True, exist_ok=True)
    min_ts, max_ts = _ts(min_close), _ts(max_close)
    games = load_nhl_games(Path(history_root))
    idx = schedule_index(games) if len(games) else {}
    manifest: dict[str, Any] = {"pulled_at": iso(utcnow()), "min_close": min_close, "max_close": max_close, "series": {}, "errors": [],
                                "candle_windows": {"hourly": "[start-48h, start+1h] period 60", "minute": "[start-3h15m, start+5m] period 1 (KXNHLGAME, KXNHLTOTAL)"},
                                "quote_note": "candles expose best YES bid/ask at each period close and trade prices; no depth; not executable history",
                                "n_schedule_games": len(idx)}
    all_markets: list[dict[str, Any]] = []
    for st in series:
        st = st.strip().upper()
        if not st:
            continue
        rep: dict[str, Any] = {"historical": 0, "live": 0, "merged": 0, "errors": []}
        hist: list[dict[str, Any]] = []
        live: list[dict[str, Any]] = []
        try:
            hist = list(client.iter_historical_markets(series_ticker=st, min_close_ts=min_ts, max_close_ts=max_ts))
        except KalshiError as e:
            rep["errors"].append(f"historical: {str(e)[:300]}")
        try:
            live = list(client.iter_markets(series_ticker=st, status="settled", min_close_ts=min_ts, max_close_ts=max_ts))
        except KalshiError as e:
            rep["errors"].append(f"live: {str(e)[:300]}")
        merged = merge_markets(hist, live, st)
        joined = Counter(market_game(m, idx)[1] for m in merged)
        rep.update({"historical": len(hist), "live": len(live), "merged": len(merged), "join": dict(joined),
                    "results": dict(Counter(str(m.get("result")) for m in merged)), "markets_file": f"markets_{st}.jsonl.gz"})
        closes = sorted(str(m.get("close_time")) for m in merged if m.get("close_time"))
        rep["close_range"] = [closes[0], closes[-1]] if closes else None
        _write_jsonl_gz(out / rep["markets_file"], merged)
        manifest["series"][st] = rep
        all_markets += merged
        log.info(kv(event="kalshi_history_series", series=st, historical=len(hist), live=len(live), merged=len(merged)))

    manifest["total_markets"] = len(all_markets)
    manifest["request_count"] = getattr(client, "request_count", None)
    manifest["elapsed_s"] = round(time.time() - t_start, 1)
    (out / "MANIFEST.json").write_text(json.dumps(manifest, indent=1, default=str))
    log.info(kv(event="kalshi_history_done", markets=len(all_markets), elapsed_s=manifest["elapsed_s"]))
    return 0 if all_markets else 1


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.kalshi_history")
    ap.add_argument("--out", default="data/history")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--series", default=",".join(CORE_SERIES + EXTRA_SERIES))
    ap.add_argument("--min-close", default="2024-09-01")
    ap.add_argument("--max-close", default="2026-07-15")
    ap.add_argument("--no-candles", action="store_true")
    ap.add_argument("--candle-series", default=None, help="restrict candle fetches to these series (default: core series)")
    ap.add_argument("--max-candle-jobs", type=int, default=40000)
    ap.add_argument("--max-minutes", type=float, default=150.0)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--rate", type=float, default=12.0)
    ap.add_argument("--tag", default="core", help="candle file tag (parallel jobs write different files)")
    ap.add_argument("--skip-markets", action="store_true", help="reuse markets_*.jsonl.gz already on disk")
    a = ap.parse_args(argv)
    series = [s for s in a.series.split(",") if s.strip()]
    rc = 0 if a.skip_markets else run_kalshi_history(Path(a.out), Path(a.history), series, a.min_close, a.max_close, rate_per_s=a.rate)
    if a.no_candles:
        return rc
    cs = [s for s in (a.candle_series or ",".join(CORE_SERIES)).split(",") if s.strip()]
    # candles only for the requested series: re-read what was just written rather than re-querying the markets
    out = Path(a.out) / "kalshi"
    markets = [m for s in cs for m in read_jsonl_gz(out / f"markets_{s}.jsonl.gz")]
    return run_candles_only(Path(a.out), Path(a.history), markets, a.max_candle_jobs, a.max_minutes, a.workers, a.rate, tag=a.tag)


def read_candles(out_root: Path) -> pd.DataFrame:
    """Every ``candles_*.parquet`` under ``<out_root>/kalshi`` (one per pull job), concatenated."""
    files = sorted((Path(out_root) / "kalshi").glob("candles_*.parquet"))
    return pd.concat([pd.read_parquet(f) for f in files], ignore_index=True) if files else pd.DataFrame()


def run_candles_only(out_root: Path, history_root: Path, markets: list[dict[str, Any]], max_jobs: int, max_minutes: float, workers: int,
                     rate: float, client: Any | None = None, tag: str = "core") -> int:
    """Candle pass over already-written market files into ``candles_<tag>.parquet``; appends to ``MANIFEST_candles_<tag>.json``."""
    from nhl_edge.data.history import load_nhl_games

    out = Path(out_root) / "kalshi"
    mpath = out / f"MANIFEST_candles_{tag}.json"
    manifest = json.loads(mpath.read_text()) if mpath.exists() else {}
    t0 = time.time()
    client = client or KalshiClient(rate=RateLimiter(rate_per_s=rate))
    games = load_nhl_games(Path(history_root))
    idx = schedule_index(games) if len(games) else {}
    cpath = out / f"candles_{tag}.parquet"
    prior = read_candles(out_root)
    existing = pd.read_parquet(cpath).to_dict("records") if cpath.exists() else []
    skip = {(str(t), int(i)) for t, i in zip(prior["ticker"], prior["interval"])} if len(prior) else set()
    jobs = candle_jobs([m for m in markets if m.get("ticker")], idx, skip)[: int(max_jobs)]
    deadline = t0 + max_minutes * 60
    n_ok: Counter[str] = Counter()
    n_err: Counter[str] = Counter()
    n_empty: Counter[str] = Counter()
    errors: list[dict[str, Any]] = []
    new_rows: list[dict[str, Any]] = []

    def fetch(j: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]], str | None]:
        if time.time() > deadline:
            return j, [], "deadline"
        try:
            return j, client.historical_candlesticks(j["ticker"], j["t0"], j["t1"], j["interval"]), None
        except KalshiError as e:
            try:
                return j, client.candlesticks(j["series_ticker"], j["ticker"], j["t0"], j["t1"], j["interval"]), None
            except KalshiError as e2:
                return j, [], f"hist: {str(e)[:120]} | live: {str(e2)[:120]}"

    with ThreadPoolExecutor(max_workers=max(1, int(workers))) as ex:
        futs = [ex.submit(fetch, j) for j in jobs]
        for i, fu in enumerate(as_completed(futs)):
            j, rows, err = fu.result()
            key = f"{j['series_ticker']}:{j['interval']}"
            if err == "deadline":
                n_err["deadline_skipped"] += 1
                continue
            if err:
                n_err[key] += 1
                if len(errors) < 100:
                    errors.append({"ticker": j["ticker"], "interval": j["interval"], "err": err})
                continue
            n_ok[key] += 1
            base = {"ticker": j["ticker"], "series_ticker": j["series_ticker"], "interval": j["interval"], "game_id": j["game_id"], "start_ts": j["start_ts"]}
            if not rows:
                n_empty[key] += 1
                new_rows.append(base | {"end_period_ts": None, "_empty": True})
            new_rows += [base | _slim_candle(c) for c in rows]
            if (i + 1) % 500 == 0:
                log.info(kv(event="candle_progress", done=i + 1, total=len(jobs), elapsed_s=round(time.time() - t0)))
    merged_rows = {(r["ticker"], r["interval"], r.get("end_period_ts")): r for r in existing}
    for r in new_rows:
        merged_rows[(r["ticker"], r["interval"], r.get("end_period_ts"))] = r
    rows_sorted = [merged_rows[k] for k in sorted(merged_rows, key=lambda k: (k[0], k[1], k[2] or 0))]
    if rows_sorted:
        df = pd.DataFrame(rows_sorted)
        for c in ("yes_bid_close", "yes_ask_close", "yes_bid_open", "yes_ask_open", "yes_bid_high", "yes_ask_low", "price_close", "price_mean",
                  "price_previous", "volume", "open_interest"):
            if c in df.columns:
                df[c] = pd.to_numeric(df[c], errors="coerce").astype("float32")
        df.to_parquet(cpath, index=False, compression="zstd")
    prev = manifest.get("candles_runs", [])
    prev.append({"at": iso(utcnow()), "jobs": len(jobs), "fetched_ok": dict(n_ok), "errors": dict(n_err), "empty": dict(n_empty),
                 "elapsed_s": round(time.time() - t0, 1), "sample_errors": errors[:20], "request_count": getattr(client, "request_count", None)})
    manifest["candles_runs"] = prev
    manifest["candles"] = {"file": cpath.name, "rows": len(rows_sorted),
                           "ticker_intervals": len({(r["ticker"], r["interval"]) for r in rows_sorted if not r.get("_empty")}),
                           "windows": {"hourly": "[start-48h, start+1h] period 60", "minute": "[start-3h15m, start+5m] period 1"}}
    mpath.write_text(json.dumps(manifest, indent=1, default=str))
    return 0


def horizon_quote(candles: list[dict[str, Any]], at_ts: int, max_age_s: int) -> dict[str, Any] | None:
    """The newest candle with ``end_period_ts <= at_ts`` and age <= ``max_age_s``: the quote as it stood at ``at_ts``.

    NEVER returns a candle that closed after ``at_ts`` (no future-price leakage). Returns None if nothing qualifies
    or the quote is unusable (no bid and no ask). ``candles`` may mix intervals; the newest qualifying one wins."""
    best = None
    for c in candles:
        e = c.get("end_period_ts")
        if e is None or c.get("_empty") is True or (isinstance(e, float) and e != e):
            continue
        e = int(e)
        if e > at_ts or at_ts - e > max_age_s:
            continue
        if best is None or e > int(best["end_period_ts"]):
            best = c
    if best is None:
        return None
    bid, ask = _f(best.get("yes_bid_close")), _f(best.get("yes_ask_close"))
    if bid is not None and bid <= 0:
        bid = None
    if ask is not None and ask >= 1:
        ask = None
    if bid is None and ask is None:
        return None
    mid = (bid + ask) / 2 if bid is not None and ask is not None else None
    return {"end_period_ts": int(best["end_period_ts"]), "interval": best.get("interval"), "yes_bid": bid, "yes_ask": ask, "mid": mid,
            "spread": (ask - bid) if (bid is not None and ask is not None) else None, "price_close": _f(best.get("price_close")),
            "age_s": at_ts - int(best["end_period_ts"])}


def _num(v: Any) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _f(v: Any) -> float | None:
    """Stored candle prices are already dollars (see ``_slim_candle``)."""
    return None if v in (None, "") else _num(v)


if __name__ == "__main__":
    sys.exit(main())


