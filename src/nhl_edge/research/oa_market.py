"""Independent-model vs Kalshi market comparison at a matched timestamp for the walk-forward arms (RESEARCH_ONLY).

Question 2 of the market benchmark ("does it outperform the market as a forecasting benchmark?"), kept apart from question 3
(executability): the market price is the Kalshi candle-close best bid/ask MIDPOINT at or before the horizon (default T-60 min),
the same instant for every forecaster, with no depth, fee or slippage. A midpoint advantage is therefore NOT an execution edge.

Targets: home win, total over 5.5 / 6.5, puck line (side wins by 2+). Arms come from ``oa_walk_forward`` (their probabilities are
produced from information dated before each game's date; the market quote is dated before puck drop, which is the information
disadvantage the model has to overcome). Hybrids blend the market in logit space with a fixed, pre-declared weight and are
labelled MARKET-INFORMED: they are not independent forecasts.

Only 2025-26 has Kalshi candle history in ``data/history/kalshi``; no number here says anything about earlier seasons.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.model_research.scoring import brier, expit, logit, logloss, paired_delta
from nhl_edge.research.market_benchmark import _side, market_quotes, moneyline_frame
from nhl_edge.research.oa_evaluate import _cluster_boot

HYBRID_WEIGHTS = (0.8, 0.9)   # weight on the market logit; fixed in advance, never tuned on these games


def _arm_prefixes(df: pd.DataFrame) -> list[str]:
    return [c[: -len("p_home_win")] for c in df.columns if c.endswith("_p_home_win") and "constant" not in c]


def build_targets(history: Path, games: pd.DataFrame, pm: dict[str, np.ndarray], horizon: str) -> dict[str, pd.DataFrame]:
    """Per target: a frame with game_id, market mid, outcome y, and one probability column per arm."""
    arms = [str(a) for a in pm["arms"]]
    g = games.reset_index(drop=True)
    out: dict[str, pd.DataFrame] = {}
    ml = moneyline_frame(history)
    ml = ml[ml["horizon"] == horizon]
    d = g.merge(ml[["game_id", "p_home", "spread"]], on="game_id", how="inner")
    d["market"] = d["p_home"]
    d["y"] = d["y_home_win"].astype(float)
    for a in arms:
        d[f"p_{a}"] = d[f"{a}_p_home_win"]
    out["home_win"] = d

    def totals_want(m: dict[str, Any], gg: dict[str, Any]) -> str | None:
        from nhl_edge.research.kalshi_history import strike_of

        s = strike_of(m)
        return f"over_{s}" if s in (5.5, 6.5) else None

    q = market_quotes(history, "KXNHLTOTAL", totals_want)
    if not q.empty:
        q = q[(q["horizon"] == horizon) & q["mid"].notna()]
        for lab, grp in q.groupby("label"):
            x = float(lab.split("_")[1])
            dd = g.merge(grp[["game_id", "mid", "spread"]].drop_duplicates("game_id"), on="game_id", how="inner")
            dd["market"] = dd["mid"]
            dd["y"] = (dd["y_total"].to_numpy() > x).astype(float)
            for a in arms:
                dd[f"p_{a}"] = dd[f"{a}_p_over_{x}"]
            out[f"total_over_{x}"] = dd

    def puck_want(m: dict[str, Any], gg: dict[str, Any]) -> str | None:
        from nhl_edge.research.kalshi_history import strike_of

        side = _side(m, gg)
        return f"{side}_-1.5" if side and strike_of(m) == 1.5 else None

    q = market_quotes(history, "KXNHLSPREAD", puck_want)
    if not q.empty:
        q = q[(q["horizon"] == horizon) & q["mid"].notna()]
        mar = pm["margin"]                      # n x arms x 21 bins (margin -10..10)
        lo = 10
        for lab, grp in q.groupby("label"):
            home = lab.startswith("home")
            dd = g.assign(_row=np.arange(len(g))).merge(grp[["game_id", "mid", "spread"]].drop_duplicates("game_id"), on="game_id", how="inner")
            sgn = 1 if home else -1
            margin = (dd["home_score"] - dd["away_score"]).to_numpy() * sgn
            dd["market"] = dd["mid"]
            dd["y"] = (margin > 1.5).astype(float)
            rows = dd["_row"].to_numpy()
            for k, a in enumerate(arms):
                pmf = mar[rows, k, :]
                dd[f"p_{a}"] = pmf[:, lo + 2:].sum(axis=1) if home else pmf[:, : lo - 1].sum(axis=1)
            out[f"puck_{'home' if home else 'away'}_-1.5"] = dd
    return out


def compare_target(df: pd.DataFrame, arms: list[str], clusters: np.ndarray | None = None, n_boot: int = 3000) -> dict[str, Any]:
    y = df["y"].to_numpy(float)
    mk = np.clip(df["market"].to_numpy(float), 0.005, 0.995)
    clusters = df["game_date"].astype(str).to_numpy() if clusters is None else clusters
    res: dict[str, Any] = {"n": int(len(df)), "market_brier": float(brier(mk, y).mean()), "market_logloss": float(logloss(mk, y).mean()), "forecasters": {}}
    for a in arms:
        p = np.clip(df[f"p_{a}"].to_numpy(float), 0.005, 0.995)
        res["forecasters"][a] = _vs_market(p, mk, y, clusters, n_boot, kind="INDEPENDENT")
        for w in HYBRID_WEIGHTS:
            ph = expit(w * logit(mk) + (1 - w) * logit(p))
            res["forecasters"][f"{a}+mkt(w={w})"] = _vs_market(ph, mk, y, clusters, n_boot, kind="MARKET-INFORMED")
    return res


def _vs_market(p: np.ndarray, mk: np.ndarray, y: np.ndarray, clusters: np.ndarray, n_boot: int, kind: str) -> dict[str, Any]:
    d = paired_delta(brier(p, y), brier(mk, y), n_boot=n_boot)
    lo_c, hi_c = _cluster_boot(brier(p, y) - brier(mk, y), clusters, n_boot=min(n_boot, 2000))
    return {"kind": kind, "brier": float(brier(p, y).mean()), "logloss": float(logloss(p, y).mean()), "delta_brier_vs_market": d["delta"], "lo95": d["lo95"], "hi95": d["hi95"],
            "lo95_slate": lo_c, "hi95_slate": hi_c, "model_better_than_market": bool(d["hi95"] < 0 and hi_c < 0), "market_better_than_model": bool(d["lo95"] > 0 and lo_c > 0)}


def run(history: Path, games_csv: Path, pmf_npz: Path, horizon: str = "T-60m", seasons: list[int] | None = None) -> dict[str, Any]:
    games = pd.read_csv(games_csv)
    pm = dict(np.load(pmf_npz, allow_pickle=False))
    if seasons:
        keep = games["season"].isin(seasons).to_numpy()
        games = games[keep].reset_index(drop=True)
        pm = {"arms": pm["arms"], "total": pm["total"][keep], "margin": pm["margin"][keep]}
    arms = [str(a) for a in pm["arms"]]
    targets = build_targets(history, games, pm, horizon)
    return {"horizon": horizon, "seasons": sorted(int(s) for s in games["season"].unique()), "note": "Kalshi candle-close midpoint; no depth, fee or slippage. A midpoint advantage is not an execution edge.",
            "targets": {t: compare_target(d, arms) for t, d in targets.items() if len(d) >= 100}}


def render(rep: dict[str, Any]) -> str:
    lines = ["# Independent models vs Kalshi mid at matched timestamp", "", f"horizon {rep['horizon']} · seasons {rep['seasons']} · {rep['note']}", ""]
    for t, r in rep["targets"].items():
        lines += [f"## {t} (n={r['n']}; market Brier {r['market_brier']:.4f})", "", "| forecaster | kind | Brier | Δ vs market | 95% CI games | 95% CI slates | verdict |", "|---|---|---:|---:|---|---|---|"]
        for a, m in r["forecasters"].items():
            v = "model better" if m["model_better_than_market"] else "market better" if m["market_better_than_model"] else "indistinguishable"
            lines.append(f"| {a} | {m['kind']} | {m['brier']:.4f} | {m['delta_brier_vs_market']:+.4f} | [{m['lo95']:+.4f}, {m['hi95']:+.4f}] | [{m['lo95_slate']:+.4f}, {m['hi95_slate']:+.4f}] | {v} |")
        lines.append("")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.oa_market")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--dir", required=True)
    ap.add_argument("--horizon", default="T-60m")
    ap.add_argument("--seasons", default="2025")
    a = ap.parse_args(argv)
    d = Path(a.dir)
    rep = run(Path(a.history), d / "oa_games.csv", d / "oa_pmfs.npz", a.horizon, [int(s) for s in a.seasons.split(",")])
    (d / "oa_market.json").write_text(json.dumps(rep, indent=1))
    md = render(rep)
    (d / "oa_market.md").write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
