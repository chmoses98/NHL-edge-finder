"""Walk-forward sanity check of the opponent-adjustment layer (``features.opponent_adjust``).

    python -m nhl_edge.research.opponent_adjust_eval --history data/history --out docs/research/opponent_adjustment

For each target season (2023-24, 2024-25, 2025-26) and each 14-day checkpoint from day 21 of the season, the layer is
refit on games STRICTLY BEFORE the checkpoint (current + previous season), then scored on the next 14 days of regular
season 5v5 team-games it has not seen:

* game rate prediction (per 60, ice-time weighted MSE) for the team's 5v5 metric:
    league mean  |  raw additive (raw_off_t + raw_def_o - L)  |  raw multiplicative (raw_off_t x raw_def_o / L)  |  ADJUSTED
* game share prediction (MSE of the team's share of the game's 5v5 metric);
* forward stability: correlation of each team's share at the checkpoint (raw vs adjusted) with its REST-OF-SEASON raw share.

Diagnostic only. It decides nothing automatically and grants nothing: it is the evidence that the layer is not leaking
and behaves at least as well as raw numbers, which is the bar for RESEARCH status (not VERIFIED).
"""

from __future__ import annotations

import argparse
import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import numpy as np

from nhl_edge.features.opponent_adjust import METRICS, OPP_ADJ_VERSION, fit, methodology

COLS = {"toi": "iceTime", "xgf": "xGoalsFor", "xga": "xGoalsAgainst", "gf": "goalsFor", "ga": "goalsAgainst", "cf": "shotAttemptsFor",
        "ca": "shotAttemptsAgainst", "ff": "unblockedShotAttemptsFor", "fa": "unblockedShotAttemptsAgainst", "sf": "shotsOnGoalFor",
        "sa": "shotsOnGoalAgainst", "hdxgf": "highDangerxGoalsFor", "hdxga": "highDangerxGoalsAgainst"}


def load_rows(history: Path, situation: str = "5on5") -> list[dict[str, Any]]:
    import pandas as pd

    rows: list[dict[str, Any]] = []
    for p in sorted((history / "moneypuck").glob("team_games_*.parquet")):
        d = pd.read_parquet(p)
        d = d[(d["situation"] == situation) & (d["game_type"] == 2)]
        for r in d.to_dict("records"):
            if r.get("team_id") is None or r.get("opp_team_id") is None:
                continue
            row = {"team_id": int(r["team_id"]), "opp_team_id": int(r["opp_team_id"]), "home": bool(r["home"]), "date": str(r["game_date"])[:10],
                   "season": int(r["season"]), "situation": situation, "game_id": str(r["game_id"])}
            for k, c in COLS.items():
                v = r.get(c)
                row[k] = None if v is None or (isinstance(v, float) and v != v) else float(v)
            rows.append(row)
    rows.sort(key=lambda r: (r["date"], r["game_id"], r["team_id"]))
    return rows


def _wmse(err: np.ndarray, w: np.ndarray) -> float:
    return float((w * err**2).sum() / w.sum())


def evaluate(rows: list[dict[str, Any]], seasons: list[int], metric: str = "xg", step_days: int = 14, start_day: int = 21) -> dict[str, Any]:
    fcol, acol, _ = METRICS[metric]
    acc: dict[str, list[float]] = {k: [] for k in ("w", "y", "league", "raw_add", "raw_mult", "adj", "share_y", "share_raw", "share_adj")}
    stab = {"raw": [], "adj": []}
    checkpoints = 0
    for s in seasons:
        srows = [r for r in rows if r["season"] == s and r.get("toi")]
        if not srows:
            continue
        d0, d1 = date.fromisoformat(srows[0]["date"]), date.fromisoformat(srows[-1]["date"])
        c = d0 + timedelta(days=start_day)
        while c < d1:
            cs, ce = c.isoformat(), (c + timedelta(days=step_days)).isoformat()
            fitted = fit(rows, as_of=cs, season=s, metric=metric)
            if fitted.mu is None:
                c += timedelta(days=step_days)
                continue
            checkpoints += 1
            L = float(np.mean([a.off_raw for a in fitted.teams.values() if a.off_raw is not None]))
            test = [r for r in srows if cs <= r["date"] < ce and r.get(fcol) is not None]
            for r in test:
                a, b = fitted.teams.get(r["team_id"]), fitted.teams.get(r["opp_team_id"])
                if a is None or b is None or a.off_raw is None or b.def_raw is None or a.off_adj is None:
                    continue
                hrs = r["toi"] / 3600.0
                acc["w"].append(hrs)
                acc["y"].append(r[fcol] / hrs)
                acc["league"].append(L)
                acc["raw_add"].append(a.off_raw + b.def_raw - L)
                acc["raw_mult"].append(a.off_raw * b.def_raw / L)
                acc["adj"].append(fitted.predict(r["team_id"], r["opp_team_id"], r["home"]))
                tot = r[fcol] + (r.get(acol) or 0.0)
                if tot > 0:
                    acc["share_y"].append(r[fcol] / tot)
                    pr_o = b.off_raw + a.def_raw - L
                    pr_t = a.off_raw + b.def_raw - L
                    acc["share_raw"].append(pr_t / (pr_t + pr_o))
                    pa_t = fitted.predict(r["team_id"], r["opp_team_id"], r["home"])
                    pa_o = fitted.predict(r["opp_team_id"], r["team_id"], not r["home"])
                    acc["share_adj"].append(pa_t / (pa_t + pa_o))
                else:
                    pass
            # forward stability: checkpoint share vs rest-of-season raw share
            rest = [r for r in srows if r["date"] >= cs]
            if len(rest) > 200:
                fwd: dict[int, list[float]] = {}
                for r in rest:
                    f_ = fwd.setdefault(r["team_id"], [0.0, 0.0])
                    f_[0] += r[fcol] or 0.0
                    f_[1] += r.get(acol) or 0.0
                xs_r, xs_a, ys = [], [], []
                for t, a in fitted.teams.items():
                    if t in fwd and a.share_raw is not None and a.share_adj is not None and sum(fwd[t]) > 0:
                        xs_r.append(a.share_raw)
                        xs_a.append(a.share_adj)
                        ys.append(fwd[t][0] / sum(fwd[t]))
                if len(ys) >= 20:
                    stab["raw"].append(float(np.corrcoef(xs_r, ys)[0, 1]))
                    stab["adj"].append(float(np.corrcoef(xs_a, ys)[0, 1]))
            c += timedelta(days=step_days)
    w = np.array(acc["w"])
    y = np.array(acc["y"])
    res: dict[str, Any] = {"metric": metric, "situation": "5on5", "seasons": [f"{s}-{str(s + 1)[2:]}" for s in seasons], "checkpoints": checkpoints,
                           "n_team_games": int(len(y))}
    if len(y):
        res["rate_wmse"] = {k: round(_wmse(np.array(acc[k]) - y, w), 5) for k in ("league", "raw_add", "raw_mult", "adj")}
        base = res["rate_wmse"]["raw_mult"]
        res["adj_vs_raw_mult_pct"] = round(100.0 * (res["rate_wmse"]["adj"] - base) / base, 2)
        sy = np.array(acc["share_y"])
        res["share_mse"] = {"raw": round(float(np.mean((np.array(acc["share_raw"]) - sy) ** 2)), 6),
                            "adjusted": round(float(np.mean((np.array(acc["share_adj"]) - sy) ** 2)), 6), "n": int(len(sy))}
    if stab["raw"]:
        res["forward_stability_corr"] = {"raw_mean": round(float(np.mean(stab["raw"])), 4), "adjusted_mean": round(float(np.mean(stab["adj"])), 4),
                                         "n_checkpoints": len(stab["raw"]),
                                         "adjusted_better_share": round(float(np.mean(np.array(stab["adj"]) > np.array(stab["raw"]))), 3)}
    return res


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", default="docs/research/opponent_adjustment")
    ap.add_argument("--seasons", default="2023,2024,2025")
    a = ap.parse_args(argv)
    rows = load_rows(Path(a.history))
    seasons = [int(x) for x in a.seasons.split(",")]
    out = {"version": OPP_ADJ_VERSION, "methodology": methodology(), "results": [evaluate(rows, seasons, m) for m in ("xg", "cf", "hdxg", "g")],
           "note": "walk-forward: each checkpoint refits on games strictly before it and is scored on the next 14 days; diagnostic only"}
    od = Path(a.out)
    od.mkdir(parents=True, exist_ok=True)
    (od / "eval.json").write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps([{k: r.get(k) for k in ("metric", "n_team_games", "rate_wmse", "adj_vs_raw_mult_pct", "share_mse", "forward_stability_corr")} for r in out["results"]], indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
