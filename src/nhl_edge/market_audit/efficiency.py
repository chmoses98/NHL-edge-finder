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
                     horizons_min: tuple[int, ...] = (1440, 360, 180, 60, 10, 0), max_age_min: float = 60.0, age_rule: str = "event") -> pd.DataFrame:
    """Point-in-time live-archive quotes: one row per (ticker, horizon).

    The quote is the last board state whose ``available_at`` (tick + capture-window lag) is at or before
    ``start - horizon``. State is taken from ALL events first and only THEN tested for two-sidedness/active status, so a
    one-sided or inactive state at the cut is a missing quote, never an older two-sided one. The state's staleness is
    bounded by the tick table (a quiet market is not stale), via the contract's last-seen tick.

    ``age_rule="event"`` (v1.0, kept so the frozen registry reproduces) measures age from the last CHANGE event and drops rows older than ``max_age_min``; that
    contradicts the paragraph above, because a quiet market simply has no recent change (data review D2: 4.8% of T-60 rows dropped, mostly deep in-the-money
    low totals). ``age_rule="tick"`` bounds staleness only by ``last_seen`` and keeps quiet markets; ``quote_age_min`` is still reported.
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
    if age_rule == "tick":
        return p.drop(columns=["status", "outcome"])
    return p[p["quote_age_min"] <= max_age_min].drop(columns=["status", "outcome"])


def _band_table(d: pd.DataFrame, edges=(0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1.0), n_boot: int = 1000) -> list[dict]:
    out = []
    for b, x in d.assign(b=pd.cut(d["mid"], edges, include_lowest=True)).groupby("b", observed=True):
        gp = cluster_ratio_ci(x, "gap", None, n=n_boot)
        ry = cluster_ratio_ci(x, "pnl_yes", "cost_yes", n=n_boot)
        rn = cluster_ratio_ci(x, "pnl_no", "cost_no", n=n_boot)
        out.append({"band": str(b), "n": int(len(x)), "games": int(x["game_id"].nunique()), "mean_mid": float(x["mid"].mean()), "freq": float(x["y"].mean()),
                    "gap": gp[0], "gap_lo95": gp[1], "gap_hi95": gp[2], "roi_buy_yes": ry[0], "roi_buy_no": rn[0]})
    return out


def efficiency_report(p: pd.DataFrame, tier: str, with_months: bool = False) -> dict:
    """Calibration, price-band, line, side and time-stability diagnostics for one tier. Game-clustered throughout."""
    rep: dict = {"tier": tier, "games": int(p["game_id"].nunique())}
    hz = []
    for (k, h), d in p.groupby(["kind", "horizon_min"]):
        if len(d) < 60 or d["game_id"].nunique() < 30:
            continue
        a, b, _, sb = calibration_slope(d)
        ry, rn = cluster_ratio_ci(d, "pnl_yes", "cost_yes", n=1000), cluster_ratio_ci(d, "pnl_no", "cost_no", n=1000)
        gp = cluster_ratio_ci(d, "gap", None, n=1000)
        hz.append({"kind": k, "horizon_min": int(h), "n": int(len(d)), "games": int(d["game_id"].nunique()), "brier": float(d["sq_err"].mean()),
                   "calib_intercept": a, "calib_slope": b, "calib_slope_se": sb, "gap_yes_minus_mid": gp[0], "gap_lo95": gp[1], "gap_hi95": gp[2],
                   "roi_buy_yes": ry[0], "roi_yes_lo95": ry[1], "roi_yes_hi95": ry[2], "roi_buy_no": rn[0], "roi_no_lo95": rn[1], "roi_no_hi95": rn[2],
                   "mean_spread": float(d["spread"].mean())})
    rep["by_kind_horizon"] = hz
    d60 = p[p["horizon_min"] == 60]
    full = d60[d60["kind"].isin(["winner", "spread", "total", "team_total"])]
    rep["bands_pooled_full_game_T60"] = _band_table(full)
    for k in sorted(d60["kind"].unique()):
        x = d60[d60["kind"] == k]
        if x["game_id"].nunique() >= 40:
            rep.setdefault("bands_by_kind_T60", {})[k] = _band_table(x)
    t = d60[d60["kind"] == "total"]
    lines = []
    for ln, x in t.groupby("threshold"):
        if x["game_id"].nunique() < 40:
            continue
        gp, ru, ro = cluster_ratio_ci(x, "gap", None, n=1000), cluster_ratio_ci(x, "pnl_no", "cost_no", n=1000), cluster_ratio_ci(x, "pnl_yes", "cost_yes", n=1000)
        lines.append({"line": float(ln), "games": int(x["game_id"].nunique()), "mean_over_mid": float(x["mid"].mean()), "over_freq": float(x["y"].mean()),
                      "gap": gp[0], "gap_lo95": gp[1], "gap_hi95": gp[2], "roi_over": ro[0], "roi_under": ru[0]})
    rep["totals_by_line_T60"] = lines
    s = d60[d60["kind"] == "spread"]
    sl = []
    for ln, x in s.groupby("threshold"):
        if x["game_id"].nunique() < 40:
            continue
        gp, ry, rn = cluster_ratio_ci(x, "gap", None, n=1000), cluster_ratio_ci(x, "pnl_yes", "cost_yes", n=1000), cluster_ratio_ci(x, "pnl_no", "cost_no", n=1000)
        sl.append({"line": float(ln), "games": int(x["game_id"].nunique()), "mean_mid": float(x["mid"].mean()), "freq": float(x["y"].mean()), "gap": gp[0],
                   "gap_lo95": gp[1], "gap_hi95": gp[2], "roi_buy_yes": ry[0], "roi_buy_no": rn[0]})
    rep["spread_by_line_T60"] = sl
    w = d60[d60["kind"] == "winner"].copy()
    if "home_team_id" in w and "subject_team_id" in w:
        w["is_home"] = w["subject_team_id"] == w["home_team_id"]
        w["is_fav"] = w["mid"] > 0.5
        rep["winner_home_fav_T60"] = [{"home": bool(h), "favourite": bool(f), "n": int(len(x)), "mean_mid": float(x["mid"].mean()), "freq": float(x["y"].mean()),
                                       "gap": cluster_ratio_ci(x, "gap", None, n=1000)[0]} for (h, f), x in w.groupby(["is_home", "is_fav"])]
    mv = p.pivot_table(index="ticker", columns="horizon_min", values="mid")
    if 1440 in mv.columns and 60 in mv.columns:
        m = (mv[60] - mv[1440]).dropna()
        d = d60.merge(m.rename("move"), left_on="ticker", right_index=True)
        d["move_bin"] = pd.cut(d["move"], [-1, -0.05, -0.02, 0.02, 0.05, 1])
        rep["move_24h_to_60m_vs_residual"] = [{"move_bin": str(b), "n": int(len(x)), "games": int(x["game_id"].nunique()), "mean_residual_y_minus_mid": cluster_ratio_ci(x, "gap", None, n=1000)[0]}
                                              for b, x in d.groupby("move_bin", observed=True)]
    if with_months:
        tt = t.assign(month=t["game_date"].str[:7])
        rep["totals_gap_by_month_T60"] = [{"month": m, "games": int(x["game_id"].nunique()), "gap": cluster_ratio_ci(x, "gap", None, n=1000)[0],
                                           "roi_under": cluster_ratio_ci(x, "pnl_no", "cost_no", n=1000)[0]} for m, x in tt.groupby("month")]
    return rep


def power_table(p: pd.DataFrame, cost_col: str, pnl_col: str, effects=(0.01, 0.02, 0.03, 0.05, 0.10), alpha: float = 0.05, power: float = 0.8) -> dict:
    """Independent GAMES needed to detect a true net ROI of ``effect`` (one-sided), using the empirical per-game dispersion of normalised returns."""
    from scipy import stats

    g = p.groupby("game_id").agg(num=(pnl_col, "sum"), den=(cost_col, "sum"), k=(pnl_col, "size"))
    r = g["num"] / g["den"]
    sd_game = float(r.std(ddof=1))
    za, zb = stats.norm.ppf(1 - alpha), stats.norm.ppf(power)
    return {"bets_per_game": float(g["k"].mean()), "sd_of_per_game_roi": sd_game,
            "games_needed": {f"{e:.0%}": int(np.ceil(((za + zb) * sd_game / e) ** 2)) for e in effects}}
