"""Historical base rates of the NHL_SCRIPT_V1 realised scripts (completed regular seasons, official events).

    python -m nhl_edge.research.script_base_rates --history data/history --out src/nhl_edge/scripts_v1/base_rates.json

Reads only committed history (``data/history/nhl/games_*.parquet`` + ``data/history/players/{goals,goalies}_*.parquet``)
and classifies every final regular-season game with the SAME rule the pregame layer uses
(``DrawFeatures.from_actual`` -> ``scripts_v1.taxonomy.classify``). The output is used two ways:

* as the league base rate shown next to each script ("historically ~21% of NHL games"), and
* as the climatology benchmark in the learning report: a script forecast that cannot beat "every game is the league
  base rate" on multiclass Brier has not learned anything game-specific.

Deterministic: same history -> byte-identical JSON (sorted keys, fixed rounding).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np

from nhl_edge.scripts_v1 import REALIZED_VERSION, SCRIPT_VERSION
from nhl_edge.scripts_v1.taxonomy import N_SCRIPTS, SCRIPTS, THRESHOLDS, classify
from nhl_edge.thesis.features import DrawFeatures


def realized_history(history: Path, seasons: list[int] | None = None) -> list[dict[str, Any]]:
    import pandas as pd

    rows: list[dict[str, Any]] = []
    for gp in sorted((history / "nhl").glob("games_*.parquet")):
        s = int(gp.stem.split("_")[1])
        if seasons and s not in seasons:
            continue
        goals_p, gl_p = history / "players" / f"goals_{s}.parquet", history / "players" / f"goalies_{s}.parquet"
        if not goals_p.exists() or not gl_p.exists():
            continue
        g = pd.read_parquet(gp)
        g = g[(g["game_type"] == 2) & (g["final"].astype(bool))]
        goals = {k: v.to_dict("records") for k, v in pd.read_parquet(goals_p).groupby("game_id")}
        goalies = {k: v.to_dict("records") for k, v in pd.read_parquet(gl_p).groupby("game_id")}
        for r in g.sort_values(["game_date", "game_id"]).to_dict("records"):
            gid = r["game_id"]
            if gid not in goalies:
                continue
            res = {"home_team_id": r["home_team_id"], "away_team_id": r["away_team_id"], "home_final": int(r["home_score"]),
                   "away_final": int(r["away_score"]), "last_period_type": r["last_period_type"]}
            f = DrawFeatures.from_actual(res, goals.get(gid, []), goalies[gid], r["home_abbrev"], r["away_abbrev"])
            rows.append({"season": s, "game_id": str(gid), "date": str(r["game_date"])[:10], "code": int(classify(f)[0])})
    return rows


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    codes = np.array([r["code"] for r in rows], dtype=np.int64)
    n = len(codes)
    freq = (np.bincount(codes, minlength=N_SCRIPTS) / max(n, 1)).round(4).tolist()
    by_season = {}
    for s in sorted({r["season"] for r in rows}):
        c = np.array([r["code"] for r in rows if r["season"] == s], dtype=np.int64)
        by_season[f"{s}-{str(s + 1)[2:]}"] = {"n_games": int(len(c)), "frequency": dict(zip([x.id for x in SCRIPTS],
                                                                                         (np.bincount(c, minlength=N_SCRIPTS) / max(len(c), 1)).round(4).tolist()))}
    seasons = sorted({r["season"] for r in rows})
    return {"script_version": SCRIPT_VERSION, "realized_version": REALIZED_VERSION, "n_games": n,
            "seasons": [f"{s}-{str(s + 1)[2:]}" for s in seasons], "frequency": dict(zip([x.id for x in SCRIPTS], freq)),
            "by_season": by_season, "thresholds": THRESHOLDS,
            "source": "official NHL finals (data/history/nhl games + data/history/players goals/goalies), completed regular seasons only",
            "note": "postgame classification of real games; used as the league base rate and as the climatology benchmark for script forecasts"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", default=str(Path(__file__).resolve().parents[1] / "scripts_v1" / "base_rates.json"))
    a = ap.parse_args(argv)
    doc = summarize(realized_history(Path(a.history)))
    Path(a.out).write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"n_games": doc["n_games"], "frequency": doc["frequency"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
