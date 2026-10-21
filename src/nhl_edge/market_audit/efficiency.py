"""Market-efficiency tooling (Phase C): calibration, price-band returns, cluster bootstrap.

Unit of independence is the GAME. All confidence intervals resample whole games (cluster bootstrap), never rows,
snapshots or contracts: several lines / both legs / repeated ticks of one game share one outcome path.

Returns are per-contract and fee-adjusted with the quadratic taker fee (the schedule the router verified to the cent):
    buy YES at ask a:  profit = 1{YES} - a - 0.07 a (1-a)
    buy NO  at ask b:  profit = 1{NO}  - b - 0.07 b (1-b)
ROI = total profit / total cost. Prices are DISPLAYED quotes (best ask); candle history carries no depth, so
history-tier returns assume the displayed ask is fillable at the sizes of interest (optimistic; see the live tier).
"""

from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.identity.teams import registry
from nhl_edge.kalshi.ticker import parse_ticker
from nhl_edge.market_audit.history_validation import load_history_games

TAKER = 0.07


def taker_fee(p: np.ndarray | float) -> np.ndarray | float:
    return TAKER * p * (1.0 - p)


def build_history_panel(history_dir: Path, horizons_min: tuple[int, ...] = (1440, 360, 60, 0)) -> pd.DataFrame:
    """One row per (ticker, horizon): the last hourly-candle close at least ``horizon`` minutes before puck drop."""
    hist = Path(history_dir) / "kalshi"
    reg = registry()
    games = load_history_games(history_dir)
    by_key = {(r.game_date, frozenset((int(r.home_team_id), int(r.away_team_id)))): r for r in games.itertuples()}
    kind_of = {"KXNHLGAME": "winner", "KXNHLSPREAD": "spread", "KXNHLTOTAL": "total"}
    known = reg.tricodes | set(reg.by_abbrev_map)

    meta: list[dict[str, Any]] = []
    for series, kind in kind_of.items():
        for line in gzip.open(hist / f"markets_{series}.jsonl.gz", "rt"):
            m = json.loads(line)
            res = str(m.get("result") or "")
            if res not in ("yes", "no"):
                continue
            pt = parse_ticker(m["ticker"], known)
            try:
                away, home = reg.by_abbrev(pt.away_tricode or ""), reg.by_abbrev(pt.home_tricode or "")
            except KeyError:
                continue
            g = by_key.get((pt.game_date.isoformat() if pt.game_date else "", frozenset((home.team_id, away.team_id))))
            if g is None:
                continue
            subject = None
            if kind in ("winner", "spread"):
                import re

                try:
                    subject = reg.by_abbrev(re.sub(r"\d+$", "", pt.market_suffix)).team_id
                except KeyError:
                    continue
            thr = float(m["floor_strike"]) if m.get("floor_strike") not in (None, "") else None
            meta.append({"ticker": m["ticker"], "series": series, "kind": kind, "game_id": int(g.game_id), "result": res, "threshold": thr,
                         "subject_team_id": subject, "home_team_id": int(g.home_team_id), "away_team_id": int(g.away_team_id),
                         "period_type": g.last_period_type, "home_score": int(g.home_score), "away_score": int(g.away_score),
                         "game_date": pt.game_date.isoformat() if pt.game_date else None})
    mk = pd.DataFrame(meta)

    c = pd.concat([pd.read_parquet(hist / "candles_core.parquet"), pd.read_parquet(hist / "candles_ladders.parquet")], ignore_index=True)
    c = c[(c["interval"] == 60) & c["end_period_ts"].notna() & c["yes_bid_close"].notna() & c["yes_ask_close"].notna()]
    c = c[c["ticker"].isin(set(mk["ticker"]))].copy()
    c["end"] = c["end_period_ts"].astype("int64")
    c = c.sort_values(["ticker", "end"])
    start = c.groupby("ticker")["start_ts"].first()
    out = []
    for h in horizons_min:
        cut = (start - h * 60).rename("cut").reset_index()
        cc = c.merge(cut, on="ticker")
        cc = cc[cc["end"] <= cc["cut"]]
        last = cc.groupby("ticker", as_index=False).tail(1)[["ticker", "end", "cut", "yes_bid_close", "yes_ask_close", "volume", "open_interest"]]
        last["horizon_min"] = h
        last["quote_age_min"] = (last["cut"] - last["end"]) / 60.0
        out.append(last)
    q = pd.concat(out, ignore_index=True)
    p = mk.merge(q, on="ticker")
    p["yes_bid"], p["yes_ask"] = p["yes_bid_close"].astype(float), p["yes_ask_close"].astype(float)
    p["mid"] = (p["yes_bid"] + p["yes_ask"]) / 2.0
    p["spread"] = p["yes_ask"] - p["yes_bid"]
    p["y"] = (p["result"] == "yes").astype(int)
    p["no_ask"] = 1.0 - p["yes_bid"]
    return p.drop(columns=["yes_bid_close", "yes_ask_close"])


def cluster_ratio_ci(df: pd.DataFrame, num: str, den: str | None = None, cluster: str = "game_id", n: int = 4000, seed: int = 7) -> tuple[float, float, float]:
    """Point estimate + 95% percentile CI of sum(num)/sum(den) (or mean(num) when ``den`` is None), resampling whole
    ``cluster`` units. Vectorised: per-cluster sums are resampled with multinomial weights."""
    g = df.groupby(cluster)
    a = g[num].sum().to_numpy(dtype=float)
    b = g[den].sum().to_numpy(dtype=float) if den else g[num].size().to_numpy(dtype=float)
    k = len(a)
    if k == 0 or b.sum() == 0:
        return (np.nan, np.nan, np.nan)
    rng = np.random.default_rng(seed)
    w = rng.multinomial(k, np.full(k, 1.0 / k), size=n).astype(float)
    draws = (w @ a) / np.where((w @ b) == 0, np.nan, (w @ b))
    lo, hi = np.nanpercentile(draws, [2.5, 97.5])
    return float(a.sum() / b.sum()), float(lo), float(hi)


def with_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Add per-contract fee-adjusted profit/cost columns for buying YES at the ask and NO at its ask."""
    d = df.copy()
    d["cost_yes"] = d["yes_ask"] + taker_fee(d["yes_ask"])
    d["pnl_yes"] = d["y"] - d["cost_yes"]
    d["cost_no"] = d["no_ask"] + taker_fee(d["no_ask"])
    d["pnl_no"] = (1 - d["y"]) - d["cost_no"]
    d["sq_err"] = (d["mid"] - d["y"]) ** 2
    d["one"] = 1.0
    d["gap"] = d["y"] - d["mid"]  # realised minus implied (signed, YES side)
    return d


def roi_yes(df: pd.DataFrame) -> float:
    cost = df["yes_ask"] + taker_fee(df["yes_ask"])
    return float((df["y"] - cost).sum() / cost.sum()) if len(df) else np.nan


def roi_no(df: pd.DataFrame) -> float:
    cost = df["no_ask"] + taker_fee(df["no_ask"])
    return float(((1 - df["y"]) - cost).sum() / cost.sum()) if len(df) else np.nan


def brier(df: pd.DataFrame, col: str = "mid") -> float:
    return float(((df[col] - df["y"]) ** 2).mean())


def logloss(df: pd.DataFrame, col: str = "mid") -> float:
    p = df[col].clip(0.005, 0.995)
    return float(-(df["y"] * np.log(p) + (1 - df["y"]) * np.log(1 - p)).mean())


def calibration_slope(df: pd.DataFrame, col: str = "mid") -> tuple[float, float, float, float]:
    """Logistic recalibration y ~ a + b*logit(p). Efficient & calibrated <=> a=0, b=1. Returns (a, b, se_a, se_b) with
    game-clustered covariance."""
    import statsmodels.api as sm

    p = df[col].clip(0.01, 0.99)
    x = sm.add_constant(np.log(p / (1 - p)).to_numpy())
    fit = sm.GLM(df["y"].to_numpy(), x, family=sm.families.Binomial()).fit(cov_type="cluster", cov_kwds={"groups": df["game_id"].to_numpy()})
    return float(fit.params[0]), float(fit.params[1]), float(fit.bse[0]), float(fit.bse[1])


def build_live_panel(ev: pd.DataFrame, cm: pd.DataFrame, games: pd.DataFrame, outcomes: pd.DataFrame, static: pd.DataFrame,
                     horizons_min: tuple[int, ...] = (1440, 360, 180, 60, 10, 0), max_age_min: float = 60.0) -> pd.DataFrame:
    """Point-in-time live-archive quotes: one row per (ticker, horizon).

    The quote is the last board state whose ``available_at`` (tick + capture-window lag) is at or before
    ``start - horizon``. State is taken from ALL events first and only THEN tested for two-sidedness/active status, so a
    one-sided or inactive state at the cut is a missing quote, never an older two-sided one. The state's staleness is
    bounded by the tick table (a quiet market is not stale), via the contract's last-seen tick.
    """
    base = ev.merge(cm[["ticker", "game_id", "family", "kind", "period", "threshold", "subject_team_id", "player_team_id", "is_tie_leg"]],
                    on="ticker", how="inner").merge(games[["game_id", "start_time_utc", "game_date_et", "home_team_id", "is_final"]], on="game_id")
    base = base[base["is_final"]].sort_values("available_at")
    keys = base.drop_duplicates("ticker")[["ticker", "game_id", "family", "kind", "period", "threshold", "subject_team_id", "start_time_utc",
                                            "game_date_et", "home_team_id", "is_tie_leg"]]
    last_seen = static.set_index("ticker")["last_seen"]
    out = []
    for h in horizons_min:
        k = keys.copy()
        k["cut"] = k["start_time_utc"] - pd.Timedelta(minutes=h)
        k = k.sort_values("cut")
        m = pd.merge_asof(k, base[["ticker", "available_at", "observed_at", "yes_bid", "yes_ask", "yes_bid_size", "yes_ask_size", "status", "volume"]],
                          left_on="cut", right_on="available_at", by="ticker", direction="backward")
        m["horizon_min"] = h
        m["quote_age_min"] = (m["cut"] - m["observed_at"]).dt.total_seconds() / 60.0
        m["last_seen"] = m["ticker"].map(last_seen)
        m = m[m["yes_bid"].notna() & m["yes_ask"].notna() & (m["status"] == "active")]
        m = m[(m["last_seen"] + pd.Timedelta(seconds=45)) >= m["cut"]]  # still on the board at the cut: the carried-forward state is current
        out.append(m)
    p = pd.concat(out, ignore_index=True)
    oc = outcomes.set_index("ticker")["outcome"]
    p["outcome"] = p["ticker"].map(oc)
    p = p[p["outcome"].isin(["YES", "NO"])].copy()
    p["y"] = (p["outcome"] == "YES").astype(int)
    p["yes_bid"], p["yes_ask"] = p["yes_bid"] / 100.0, p["yes_ask"] / 100.0
    p["mid"] = (p["yes_bid"] + p["yes_ask"]) / 2.0
    p["spread"] = p["yes_ask"] - p["yes_bid"]
    p["no_ask"] = 1.0 - p["yes_bid"]
    p["game_date"] = p["game_date_et"]
    p["game_id"] = p["game_id"].astype(str)
    return p[p["quote_age_min"] <= max_age_min].drop(columns=["status", "outcome"])
