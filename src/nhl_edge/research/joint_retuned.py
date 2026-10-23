"""J2: retuned and recalibrated V1 rates through the V2 simulator, scored jointly (RESEARCH_ONLY; docs/research/v2-joint-retuned/PREREGISTRATION.md).

Reuses ``joint_eval.run_joint`` unchanged (same V2 fits, features, seeds and draw counts); the retuned rates come from the committed per-game tables of the
registered retune study and enter as ``extra_lams``. A ``collect`` hook adds the per-arm probabilities the preregistration scores beyond ``joint_eval``'s own:
the regulation 3-class outcome, team totals and puck lines.

    python -m nhl_edge.research.joint_retuned run --seasons 2010,2011 --out OUT/shard0
    python -m nhl_edge.research.joint_retuned evaluate --dirs OUT/shard* --out OUT
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

RATE_FILES = ("docs/research/v1-retune/data/v1r_games_fresh2.csv.gz", "docs/research/v1-retune/data/v1r_games_main.csv.gz")
RATE_ARMS = {"R": "V1_R", "RC": "V1_R_C1"}                 # extra_lams name -> column prefix in the retune tables
TEAM_LINES = (1.5, 2.5, 3.5, 4.5)


def load_rates(root: Path) -> dict[str, pd.DataFrame]:
    frames = [pd.read_csv(root / f) for f in RATE_FILES]
    df = pd.concat(frames, ignore_index=True).drop_duplicates("game_id").set_index("game_id")
    return {name: df[[f"{pre}_lam_home", f"{pre}_lam_away"]].rename(columns={f"{pre}_lam_home": "lam_home", f"{pre}_lam_away": "lam_away"}) for name, pre in RATE_ARMS.items()}


def collect(sims: dict[str, Any]) -> dict[str, float]:
    """Per arm: regulation 3-class probabilities, final-margin puck lines (win by 2+) and each team's over-lines, all from the simulator draws."""
    out: dict[str, float] = {}
    for a, r in sims.items():
        hr, ar = np.asarray(r.home_reg), np.asarray(r.away_reg)
        hf, af = np.asarray(r.home_final), np.asarray(r.away_final)
        out[f"{a}_p_reg_home"] = float((hr > ar).mean())
        out[f"{a}_p_reg_tie"] = float((hr == ar).mean())
        out[f"{a}_p_reg_away"] = float((hr < ar).mean())
        out[f"{a}_p_home_pl"] = float((hf - af >= 2).mean())
        out[f"{a}_p_away_pl"] = float((af - hf >= 2).mean())
        out[f"{a}_mean_total"] = float((hf + af).mean())
        for L in TEAM_LINES:
            out[f"{a}_p_home_o{L}"] = float((hf > L).mean())
            out[f"{a}_p_away_o{L}"] = float((af > L).mean())
    return out


def main(argv: list[str] | None = None) -> int:
    import argparse
    import json

    from nhl_edge.research import joint_eval as J

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.joint_retuned")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--history", default="data/history")
    r.add_argument("--seasons", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--n-sims", type=int, default=4000)
    r.add_argument("--max-games", type=int)
    a = ap.parse_args(argv)
    if a.cmd == "run":
        seasons = [int(s) for s in a.seasons.split(",")]
        df, cm, ct, pm, meta = J.run_joint(a.history, seasons, n_sims=a.n_sims, first_shots_season=2008, train_window=4, min_season=2008,
                                           extra_shots_dir="data/history/shots_extension", max_games=a.max_games, extra_lams=load_rates(Path(".")), collect=collect)
        J._save_shard(a.out, df, cm, ct, pm, {**meta, "seasons": seasons, "n_sims": a.n_sims, "first_shots_season": 2008, "train_window": 4})
        print(json.dumps({"n_games": len(df), **meta["fits"]}, default=str)[:300])
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
