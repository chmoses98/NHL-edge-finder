"""Historical Kalshi NHL market benchmark: V1 vs V2 vs MARKET on identical games at identical horizons (RESEARCH_ONLY).

HISTORICAL, NOT PROSPECTIVE. Inputs:

* ``data/history/kalshi/markets_<SERIES>.jsonl.gz`` + ``candles_*.parquet`` (``nhl_edge.research.kalshi_history``);
* a walk-forward per-game CSV (``walk_forward_v2_<run>_games.csv``) with every model arm's probabilities.

Market probability at horizon ``T-h`` = midpoint of the best YES bid / ask in the newest candle whose
``end_period_ts`` is at or before ``start - h`` (``kalshi_history.horizon_quote``): a price that existed at that
instant, never a later one. A quote older than the horizon's staleness limit, or missing one side, is no quote.
These are candle-close quotes, not executable depth: the tables measure forecast quality, not tradeable edge.

Model timing: walk-forward predictions use data from games dated strictly before the game date, i.e. information
complete by the morning of game day. At T-24h (the previous evening) the model may know previous-day results the
market could not yet have seen, so T-24h rows are flagged; T-12h and later are clean.

Also: market-anchored arm (MARKET_ANCHORED_V1's 0.8 logit blend, labelled as NOT independent) and a residual study:
does ``model - market`` predict ``outcome - market``?
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.history import load_nhl_games
from nhl_edge.evaluation.metrics import brier, ece, log_loss
from nhl_edge.research.kalshi_history import (
    fkey,
    horizon_quote,
    market_game,
    read_candles,
    read_jsonl_gz,
    schedule_index,
    strike_of,
)

HORIZONS: tuple[tuple[str, int, int], ...] = (  # label, minutes before start, max quote age (s)
    ("T-24h", 1440, 2 * 3600), ("T-12h", 720, 2 * 3600), ("T-6h", 360, 2 * 3600), ("T-3h", 180, 2 * 3600),
    ("T-90m", 90, 30 * 60), ("T-60m", 60, 30 * 60), ("T-30m", 30, 20 * 60), ("T-10m", 10, 15 * 60))
MODEL_ARMS = {"V1": "V1_", "V2 (SIM2_ST)": "SIM2_ST_", "SIM2 (V1 lambdas)": "SIM2_", "V2+goalie oracle": "SIM2_ST_GTT_"}
ANCHOR_W = 0.80
BANNER = ("HISTORICAL, NOT PROSPECTIVE. Market = Kalshi candle-close best bid/ask midpoint at or before each horizon "
          "(no depth; not executable history). Same games, same instants for every forecaster.")


def _logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def _inv(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def market_quotes(history: Path, series: str, want: Any) -> pd.DataFrame:
    """Rows (game_id, ticker, horizon, mid, bid, ask, spread, age_s, result, strike, team_side) for markets ``want(m, g)``
    selects. ``want`` returns a label (e.g. 'home', 'away', 'over_5.5') or None."""
    games = load_nhl_games(history)
    idx = schedule_index(games)
    ms = read_jsonl_gz(history / "kalshi" / f"markets_{series}.jsonl.gz")
    candles = read_candles(history)
    if candles.empty or not ms:
        return pd.DataFrame()
    by_ticker = {t: d.to_dict("records") for t, d in candles.groupby("ticker")}
    rows = []
    for m in ms:
        g, why = market_game(m, idx)
        if g is None or g.get("start_ts") is None or g.get("game_type") != 2:
            continue
        label = want(m, g)
        if label is None:
            continue
        cs = by_ticker.get(m["ticker"], [])
        for hl, mins, max_age in HORIZONS:
            q = horizon_quote(cs, int(g["start_ts"]) - mins * 60, max_age)
            rows.append({"game_id": g["game_id"], "ticker": m["ticker"], "label": label, "horizon": hl, "start_ts": g["start_ts"],
                         "result": m.get("result"), "strike": strike_of(m), "has_candles": bool(cs),
                         **({k: q[k] for k in ("mid", "yes_bid", "yes_ask", "spread", "age_s", "interval")} if q else {"mid": None})})
    return pd.DataFrame(rows)


def _side(m: dict[str, Any], g: dict[str, Any]) -> str | None:
    suf = str(m.get("ticker", "")).rsplit("-", 1)[-1].rstrip("0123456789")  # spread tickers carry the strike: '-ANA1'
    k = fkey(suf)
    if k == g["home"]:
        return "home"
    if k == g["away"]:
        return "away"
    # short Kalshi codes (LA / NJ / SJ / TB) resolve through fkey; anything else is not guessed
    return None


def moneyline_frame(history: Path) -> pd.DataFrame:
    q = market_quotes(history, "KXNHLGAME", _side)
    if q.empty:
        return q
    q = q[q["mid"].notna()].copy()
    # P(home) from the home market; the away market's complement when the home market has no quote
    q["p_home"] = np.where(q["label"] == "home", q["mid"], 1 - q["mid"])
    q["pref"] = (q["label"] == "home").astype(int)
    q = q.sort_values(["game_id", "horizon", "pref"], ascending=[True, True, False]).drop_duplicates(["game_id", "horizon"])
    return q[["game_id", "horizon", "p_home", "spread", "age_s", "interval", "label", "ticker"]]


def score(p: np.ndarray, y: np.ndarray) -> dict[str, Any]:
    return {"n": int(len(p)), "brier": brier(p, y), "log_loss": log_loss(p, y), "ece": ece(p, y, 10), "mean_p": float(np.mean(p)), "mean_y": float(np.mean(y))}


def _ols(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    s2 = float(resid @ resid) / max(len(y) - 2, 1)
    cov = s2 * np.linalg.inv(X.T @ X)
    return {"intercept": float(beta[0]), "slope": float(beta[1]), "slope_se": float(math.sqrt(cov[1, 1])), "t": float(beta[1] / math.sqrt(cov[1, 1])), "n": int(len(y))}


def _logit_combo(p_mkt: np.ndarray, p_mod: np.ndarray, y: np.ndarray, iters: int = 50) -> dict[str, float]:
    """y ~ Bernoulli(inv_logit(a + b*logit(p_mkt) + c*logit(p_model))) by Newton; c ~ 0 means no information beyond market."""
    X = np.column_stack([np.ones_like(p_mkt), _logit(p_mkt), _logit(p_mod)])
    w = np.zeros(3)
    for _ in range(iters):
        mu = _inv(X @ w)
        W = mu * (1 - mu)
        H = X.T @ (X * W[:, None]) + 1e-9 * np.eye(3)
        step = np.linalg.solve(H, X.T @ (y - mu))
        w = w + step
        if np.max(np.abs(step)) < 1e-10:
            break
    mu = _inv(X @ w)
    cov = np.linalg.inv(X.T @ (X * (mu * (1 - mu))[:, None]))
    se = np.sqrt(np.diag(cov))
    return {"a": float(w[0]), "b_market": float(w[1]), "b_market_se": float(se[1]), "c_model": float(w[2]), "c_model_se": float(se[2]),
            "c_model_z": float(w[2] / se[2]), "n": int(len(y))}


def residual_study(d: pd.DataFrame, prefix: str) -> dict[str, Any]:
    y = d["y_home_win"].astype(float).to_numpy()
    pm = d["p_home"].to_numpy(dtype=float)
    pr = d[f"{prefix}p_home_win"].to_numpy(dtype=float)
    diff = pr - pm
    res = y - pm
    out: dict[str, Any] = {"ols_residual_on_disagreement": _ols(diff, res), "logit_combination": _logit_combo(pm, pr, y)}
    bins = [-1, -0.10, -0.06, -0.03, 0.03, 0.06, 0.10, 1]
    tab = []
    for lo, hi in zip(bins[:-1], bins[1:]):
        s = (diff > lo) & (diff <= hi)
        if s.sum() == 0:
            continue
        r = res[s]
        tab.append({"disagreement": f"({lo:+.2f}, {hi:+.2f}]", "n": int(s.sum()), "mean_model_minus_market": float(diff[s].mean()),
                    "mean_outcome_minus_market": float(r.mean()), "se": float(r.std(ddof=1) / math.sqrt(s.sum())) if s.sum() > 1 else None})
    out["by_disagreement_bin"] = tab
    return out


def run(history: Path, wf_games_csv: Path) -> dict[str, Any]:
    wf = pd.read_csv(wf_games_csv)
    ml = moneyline_frame(history)
    manifest = json.loads((history / "kalshi" / "MANIFEST.json").read_text()) if (history / "kalshi" / "MANIFEST.json").exists() else {}
    rep: dict[str, Any] = {"banner": BANNER, "authority": "RESEARCH_ONLY", "wf_games_csv": wf_games_csv.name, "horizons": [h[0] for h in HORIZONS],
                           "kalshi_manifest_summary": {k: {kk: v.get(kk) for kk in ("merged", "join", "close_range", "results")} for k, v in (manifest.get("series") or {}).items()}}
    if ml.empty:
        rep["moneyline"] = "no KXNHLGAME quotes available"
        return rep
    d = ml.merge(wf, on="game_id", how="inner")
    rep["moneyline_games_with_any_quote"] = int(d["game_id"].nunique())
    rep["moneyline_date_range"] = [str(d["game_date"].min()), str(d["game_date"].max())]
    rep["moneyline"] = {}
    rep["residuals"] = {}
    for hl, _, _ in HORIZONS:
        h = d[d["horizon"] == hl]
        if h.empty:
            continue
        y = h["y_home_win"].astype(float).to_numpy()
        row: dict[str, Any] = {"n": int(len(h)), "seasons": sorted(int(s) for s in h["season"].unique()), "median_spread": float(h["spread"].median()),
                               "date_range": [str(h["game_date"].min()), str(h["game_date"].max())], "leak_flag": hl == "T-24h"}
        row["MARKET"] = score(h["p_home"].to_numpy(dtype=float), y)
        for name, pre in MODEL_ARMS.items():
            if f"{pre}p_home_win" in h.columns:
                row[name] = score(h[f"{pre}p_home_win"].to_numpy(dtype=float), y)
        for name, pre in (("MARKET_ANCHORED(V1, w=0.8)", "V1_"), ("MARKET_ANCHORED(V2, w=0.8)", "SIM2_ST_")):
            pa = _inv(ANCHOR_W * _logit(h["p_home"].to_numpy(dtype=float)) + (1 - ANCHOR_W) * _logit(h[f"{pre}p_home_win"].to_numpy(dtype=float)))
            row[name] = score(pa, y)
        tight = h[h["spread"] <= 0.03]
        if len(tight) >= 50:
            yt = tight["y_home_win"].astype(float).to_numpy()
            row["tight_spread_subset"] = {"n": int(len(tight)), "MARKET": score(tight["p_home"].to_numpy(dtype=float), yt),
                                          "V1": score(tight["V1_p_home_win"].to_numpy(dtype=float), yt), "V2 (SIM2_ST)": score(tight["SIM2_ST_p_home_win"].to_numpy(dtype=float), yt)}
        rep["moneyline"][hl] = row
        rep["residuals"][hl] = {"V1": residual_study(h, "V1_"), "V2 (SIM2_ST)": residual_study(h, "SIM2_ST_")}
    rep["totals"] = totals_benchmark(history, wf)
    rep["puck_line"] = puck_line_benchmark(history, wf)
    return rep


def puck_line_benchmark(history: Path, wf: pd.DataFrame) -> dict[str, Any]:
    """KXNHLSPREAD 'X wins by over 1.5' (final score incl. the OT/SO goal) vs the models' P(margin > 1.5) for that side."""
    def want(m: dict[str, Any], g: dict[str, Any]) -> str | None:
        side = _side(m, g)
        return f"{side}_-1.5" if side and strike_of(m) == 1.5 else None

    q = market_quotes(history, "KXNHLSPREAD", want)
    if q.empty:
        return {"note": "no KXNHLSPREAD quotes"}
    d = q[q["mid"].notna()].merge(wf, on="game_id", how="inner")
    out: dict[str, Any] = {}
    for (hl, lab), h in d.groupby(["horizon", "label"]):
        home = lab.startswith("home")
        margin = (h["home_score"] - h["away_score"]).to_numpy() * (1 if home else -1)
        y = (margin > 1.5).astype(float)
        col = "p_home_minus_1_5" if home else "p_away_minus_1_5"
        out.setdefault(hl, {})[lab] = {"n": int(len(h)), "MARKET": score(h["mid"].to_numpy(dtype=float), y), "V1": score(h[f"V1_{col}"].to_numpy(dtype=float), y),
                                       "V2 (SIM2_ST)": score(h[f"SIM2_ST_{col}"].to_numpy(dtype=float), y),
                                       "kalshi_result_agrees": float(np.mean((h["result"] == "yes").to_numpy() == (y == 1)))}
    return out


def totals_benchmark(history: Path, wf: pd.DataFrame) -> dict[str, Any]:
    """KXNHLTOTAL over 5.5 / 6.5 vs the models' P(total > x) at the same horizons (settlement = official final incl. OT/SO goal)."""
    def want(m: dict[str, Any], g: dict[str, Any]) -> str | None:
        s = strike_of(m)
        return f"over_{s}" if s in (5.5, 6.5) else None

    q = market_quotes(history, "KXNHLTOTAL", want)
    if q.empty:
        return {"note": "no KXNHLTOTAL quotes"}
    q = q[q["mid"].notna()]
    d = q.merge(wf, on="game_id", how="inner")
    out: dict[str, Any] = {}
    for (hl, lab), h in d.groupby(["horizon", "label"]):
        x = float(lab.split("_")[1])
        y = (h["y_total"].to_numpy() > x).astype(float)
        row = {"n": int(len(h)), "MARKET": score(h["mid"].to_numpy(dtype=float), y),
               "kalshi_result_agrees_with_official_final": float(np.mean((h["result"] == "yes").to_numpy() == (y == 1)))}
        for name, pre in (("V1", "V1_"), ("V2 (SIM2_ST)", "SIM2_ST_")):
            col = f"{pre}p_over_{x}"
            if col in h.columns:
                row[name] = score(h[col].to_numpy(dtype=float), y)
        out.setdefault(hl, {})[lab] = row
    return out


def render(rep: dict[str, Any]) -> str:
    f = lambda x, n=4: "-" if x is None else f"{x:.{n}f}"  # noqa: E731
    L = ["# Historical Kalshi NHL market benchmark (MARKET_BENCHMARK)", "", f"> **{rep['banner']}**", ""]
    if isinstance(rep.get("moneyline"), str):
        return "\n".join(L + [rep["moneyline"], ""])
    L += [f"Walk-forward source `{rep['wf_games_csv']}` · games with any KXNHLGAME quote: {rep.get('moneyline_games_with_any_quote')} · "
          f"date range {rep.get('moneyline_date_range')}", "",
          "## Moneyline: same games, same instants", "",
          "| horizon | n | V1 Brier | V2 Brier | Kalshi Brier | V1 log loss | V2 log loss | Kalshi log loss | V1 ECE | V2 ECE | Kalshi ECE | median spread |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for hl, r in rep["moneyline"].items():
        v1, v2, mk = r["V1"], r["V2 (SIM2_ST)"], r["MARKET"]
        L.append(f"| {hl}{' (flag)' if r['leak_flag'] else ''} | {r['n']} | {f(v1['brier'])} | {f(v2['brier'])} | {f(mk['brier'])} | {f(v1['log_loss'])} | "
                 f"{f(v2['log_loss'])} | {f(mk['log_loss'])} | {f(v1['ece'])} | {f(v2['ece'])} | {f(mk['ece'])} | {f(r['median_spread'], 3)} |")
    L += ["", "T-24h (flag): the model's inputs are complete through the previous day, which the market had not fully seen 24h before puck drop.", "",
          "### Other arms (Brier / log loss)", "", "| horizon | SIM2 (V1 lambdas) | V2+goalie oracle (not a pregame arm) | MARKET_ANCHORED(V1) | MARKET_ANCHORED(V2) |", "|---|---|---|---|---|"]
    for hl, r in rep["moneyline"].items():
        cells = [f"{f(r[k]['brier'])} / {f(r[k]['log_loss'])}" if k in r else "-" for k in ("SIM2 (V1 lambdas)", "V2+goalie oracle", "MARKET_ANCHORED(V1, w=0.8)", "MARKET_ANCHORED(V2, w=0.8)")]
        L.append(f"| {hl} | " + " | ".join(cells) + " |")
    L += ["", "## Does the model add information beyond the market?", "",
          "Logistic combination `y ~ a + b*logit(p_market) + c*logit(p_model)` (c = 0: no information beyond the market) and OLS of "
          "`outcome - market` on `model - market` (slope 0: disagreements carry no signal; slope 1: the model's disagreement is fully right).", "",
          "| horizon | model | c (model) | se | z | OLS slope | se | n |", "|---|---|---:|---:|---:|---:|---:|---:|"]
    for hl, rr in rep["residuals"].items():
        for name, r in rr.items():
            c, o = r["logit_combination"], r["ols_residual_on_disagreement"]
            L.append(f"| {hl} | {name} | {f(c['c_model'], 3)} | {f(c['c_model_se'], 3)} | {f(c['c_model_z'], 2)} | {f(o['slope'], 3)} | {f(o['slope_se'], 3)} | {o['n']} |")
    main_h = "T-60m" if "T-60m" in rep["residuals"] else next(iter(rep["residuals"]), None)
    if main_h:
        L += ["", f"### Disagreement bins at {main_h} (V1 and V2): mean(outcome - market) by model - market", "",
              "| model | bin | n | mean model-market | mean outcome-market | se |", "|---|---|---:|---:|---:|---:|"]
        for name, r in rep["residuals"][main_h].items():
            for b in r["by_disagreement_bin"]:
                L.append(f"| {name} | {b['disagreement']} | {b['n']} | {f(b['mean_model_minus_market'], 3)} | {f(b['mean_outcome_minus_market'], 3)} | {f(b['se'], 3)} |")
    tt = rep.get("totals") or {}
    if tt and "note" not in tt:
        L += ["", "## Totals (KXNHLTOTAL over 5.5 / 6.5)", "", "| horizon | line | n | V1 Brier | V2 Brier | Kalshi Brier | V1 LL | V2 LL | Kalshi LL |", "|---|---|---:|---:|---:|---:|---:|---:|---:|"]
        for hl, _, _ in HORIZONS:
            for lab, r in sorted((tt.get(hl) or {}).items()):
                L.append(f"| {hl} | {lab} | {r['n']} | {f(r['V1']['brier'])} | {f(r['V2 (SIM2_ST)']['brier'])} | {f(r['MARKET']['brier'])} | {f(r['V1']['log_loss'])} | "
                         f"{f(r['V2 (SIM2_ST)']['log_loss'])} | {f(r['MARKET']['log_loss'])} |")
    pl = rep.get("puck_line") or {}
    if pl and "note" not in pl:
        L += ["", "## Puck line (KXNHLSPREAD, team wins by over 1.5; hourly candles only)", "",
              "| horizon | side | n | V1 Brier | V2 Brier | Kalshi Brier | V1 LL | V2 LL | Kalshi LL | settlement agrees |", "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for hl, _, _ in HORIZONS:
            for lab, r in sorted((pl.get(hl) or {}).items()):
                L.append(f"| {hl} | {lab} | {r['n']} | {f(r['V1']['brier'])} | {f(r['V2 (SIM2_ST)']['brier'])} | {f(r['MARKET']['brier'])} | {f(r['V1']['log_loss'])} | "
                         f"{f(r['V2 (SIM2_ST)']['log_loss'])} | {f(r['MARKET']['log_loss'])} | {f(r['kalshi_result_agrees'], 3)} |")
    L += ["", f"> {rep['banner']}", ""]
    return "\n".join(L)


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.market_benchmark")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--wf-games", required=True)
    ap.add_argument("--out", default="docs/research")
    a = ap.parse_args(argv)
    rep = run(Path(a.history), Path(a.wf_games))
    out = Path(a.out)
    (out / "market_benchmark.json").write_text(json.dumps(rep, indent=1, default=str))
    (out / "MARKET_BENCHMARK.md").write_text(render(rep))
    print(render(rep)[:4000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
