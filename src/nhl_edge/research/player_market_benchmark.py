"""PLAYER_SIM_V1 vs Kalshi player-prop prices (RESEARCH_ONLY, historical 2025-26).

Joins settled KXNHLPTS / KXNHLGOAL / KXNHLAST / KXNHLSAVE markets (``data/history/players_kalshi``) to the official game
and player (team + jersey + name against the game's official boxscore lines; ambiguous -> dropped, counted), to the
walk-forward PLAYER_SIM_V1 probability for the same player-game and threshold, and to the market quote at each horizon
before the scheduled start (``horizon_quote``: the newest hourly candle that CLOSED at or before the instant; never a
later one). Quotes are candle best bid/ask midpoints: NOT executable history (no depth), labelled as such.

Questions answered, each on identical rows:
* Brier / log loss of the model, the market midpoint and the 0.8 market-anchored blend;
* does the model add information given the market? ``y ~ a + b*logit(market) + c*logit(model)`` (logistic, Newton;
  standard errors from the observed information): c's z-score;
* the sign-agreement of large disagreements (model - market > 0.10) with outcomes.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research.kalshi_history import horizon_quote, market_game, read_candles, read_jsonl_gz, schedule_index
from nhl_edge.research.player_eval import brier, logloss, score
from nhl_edge.settlement.player import _match

SERIES = {"KXNHLPTS": "points", "KXNHLGOAL": "goals", "KXNHLAST": "assists", "KXNHLSAVE": "saves"}
HORIZONS = ((360, "T-6h"), (180, "T-3h"), (90, "T-90m"), (60, "T-60m"), (30, "T-30m"), (10, "T-10m"))
MAX_AGE_S = 3 * 3600


def _logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def logistic(X: np.ndarray, y: np.ndarray, iters: int = 50) -> tuple[np.ndarray, np.ndarray]:
    w = np.zeros(X.shape[1])
    for _ in range(iters):
        p = 1 / (1 + np.exp(-(X @ w)))
        H = (X * (p * (1 - p))[:, None]).T @ X + 1e-9 * np.eye(X.shape[1])
        st = np.linalg.solve(H, X.T @ (y - p))
        w += st
        if np.abs(st).max() < 1e-10:
            break
    p = 1 / (1 + np.exp(-(X @ w)))
    cov = np.linalg.inv((X * (p * (1 - p))[:, None]).T @ X)
    return w, np.sqrt(np.diag(cov))


def model_prob(stat: str, k: int, sk_row: Any | None, gl_row: Any | None) -> float | None:
    col = {"points": "p_p", "goals": "p_g", "assists": "p_a"}.get(stat)
    if stat == "saves":
        return None if gl_row is None or f"p_s{k}" not in gl_row else float(gl_row[f"p_s{k}"])
    if sk_row is None or col is None or f"{col}{k}" not in sk_row:
        return None
    return float(sk_row[f"{col}{k}"])


def build_rows(history: Path, kalshi_root: Path, sk: pd.DataFrame, gl: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    from nhl_edge.data.history import load_nhl_games
    from nhl_edge.data.player_history import load_player_tables
    from nhl_edge.players.identity import parse_player_market

    idx = schedule_index(load_nhl_games(history))
    players = load_player_tables(history, "players", [2025])
    goalies = load_player_tables(history, "goalies", [2025])
    candles = read_candles(kalshi_root)
    by_ticker = {t: g.to_dict("records") for t, g in candles.groupby("ticker")} if len(candles) else {}
    skx = sk.set_index(["game_id", "player_id"])
    glx = gl.set_index(["game_id", "player_id"])
    rows, why = [], Counter()
    for series, stat in SERIES.items():
        for m in read_jsonl_gz(kalshi_root / "kalshi" / f"markets_{series}.jsonl.gz"):
            res = str(m.get("result") or "").lower()
            if res not in ("yes", "no"):
                why["no yes/no result"] += 1
                continue
            g, reason = market_game(m, idx)
            if g is None:
                why[reason] += 1
                continue
            floor = m.get("floor_strike")
            try:
                k = int(math.floor(float(floor)) + 1)
            except (TypeError, ValueError):
                why["no strike"] += 1
                continue
            ref = parse_player_market(m["ticker"], m.get("title"))
            box = (goalies if stat == "saves" else players)
            box = box[box["game_id"] == g["game_id"]]
            hit, how = _match(ref, box) if ref is not None else (None, "unparsed")
            if hit is None:
                why[f"player: {how}"] += 1
                continue
            pid = int(hit["player_id"])
            key = (int(g["game_id"]), pid)
            sk_row = skx.loc[key].to_dict() if (stat != "saves" and key in skx.index) else None
            gl_row = glx.loc[key].to_dict() if (stat == "saves" and key in glx.index) else None
            p = model_prob(stat, k, sk_row, gl_row)
            if p is None:
                why["no model row (not simulated / threshold outside ladder / goalie did not start)"] += 1
                continue
            rec = {"ticker": m["ticker"], "stat": stat, "k": k, "game_id": g["game_id"], "player_id": pid, "y": 1 if res == "yes" else 0, "p_model": p,
                   "start_ts": g["start_ts"]}
            cs = by_ticker.get(m["ticker"], [])
            for mins, lab in HORIZONS:
                q = horizon_quote(cs, int(g["start_ts"]) - mins * 60, MAX_AGE_S) if g.get("start_ts") else None
                rec[f"mid_{lab}"] = q["mid"] if q else None
                rec[f"spread_{lab}"] = q["spread"] if q else None
            rows.append(rec)
            why["joined"] += 1
    return pd.DataFrame(rows), dict(why)


def benchmark(df: pd.DataFrame) -> dict[str, Any]:
    out: dict[str, Any] = {"n_joined": int(len(df))}
    for _mins, lab in HORIZONS:
        col = f"mid_{lab}"
        d = df[df[col].notna()] if len(df) and col in df.columns else df.iloc[0:0]
        if len(d) < 50:
            out[lab] = {"n": int(len(d)), "note": "fewer than 50 quoted rows"}
            continue
        y, pm, pk = d["y"].to_numpy(float), d["p_model"].to_numpy(float), d[col].to_numpy(float)
        pa = 1 / (1 + np.exp(-(0.8 * _logit(pk) + 0.2 * _logit(pm))))
        X = np.column_stack([np.ones(len(d)), _logit(pk), _logit(pm)])
        w, se = logistic(X, y)
        big = (pm - pk) > 0.10
        small = (pk - pm) > 0.10
        rec = {"n": int(len(d)), "PLAYER_SIM_V1": score(pm, y), "KALSHI_MID": score(pk, y), "MARKET_ANCHORED_PLAYER_V1": score(pa, y),
               "combo": {"b_market": float(w[1]), "se_market": float(se[1]), "c_model": float(w[2]), "se_model": float(se[2]), "z_model": float(w[2] / se[2])},
               "model_above_market_by_10pts": {"n": int(big.sum()), "outcome_minus_market": float((y[big] - pk[big]).mean()) if big.any() else None},
               "model_below_market_by_10pts": {"n": int(small.sum()), "outcome_minus_market": float((y[small] - pk[small]).mean()) if small.any() else None},
               "by_stat": {}}
        for stat, g in d.groupby("stat"):
            if len(g) >= 30:
                rec["by_stat"][stat] = {"n": int(len(g)), "brier_model": brier(g["p_model"], g["y"]), "brier_market": brier(g[col], g["y"]),
                                        "logloss_model": logloss(g["p_model"], g["y"]), "logloss_market": logloss(g[col], g["y"])}
        out[lab] = rec
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.player_market_benchmark")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--kalshi", default="data/history/players_kalshi")
    ap.add_argument("--wf", default="docs/research/player_sim_v1")
    ap.add_argument("--out", default="docs/research/player_sim_v1/market_benchmark.json")
    a = ap.parse_args(argv)
    sk = pd.read_parquet(Path(a.wf) / "skaters_2025.parquet")
    gl = pd.read_parquet(Path(a.wf) / "goalies_2025.parquet")
    df, why = build_rows(Path(a.history), Path(a.kalshi), sk, gl)
    res = {"join": why, "benchmark": benchmark(df), "quote_note": "hourly candle best bid/ask midpoint at or before the horizon; not executable history"}
    Path(a.out).write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float)[:6000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
