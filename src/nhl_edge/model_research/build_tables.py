"""Build the derived LIVE tables used by the experiments (written OUTSIDE the repository; reproducible from the archive bytes + this code).

    python -m nhl_edge.model_research.build_tables --archive ../rdata/data-archive --out ../rdata/model_research
Outputs: slate_runs.parquet (every slate run x game), live_t60.parquet (pregame record at T-60), live_attr.parquet (per-game attribution).
Only DEVELOPMENT-window games (started before the prospective freeze) are ever built here.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from nhl_edge.model_research import DEV_LAST_GAME_DATE_ET
from nhl_edge.model_research import attribution as AT
from nhl_edge.model_research.live_dataset import build_live_dataset
from nhl_edge.model_research.slates import build_slate_table


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    slates = build_slate_table(a.archive, DEV_LAST_GAME_DATE_ET)
    slates.to_parquet(a.out / "slate_runs.parquet")
    live = build_live_dataset(a.archive, 60.0, slates)
    live.to_parquet(a.out / "live_t60.parquet")
    d, summ = AT.run(live, AT.moneypuck_2026(a.archive))
    d.to_parquet(a.out / "live_attr.parquet")
    print({"games": len(live), "class_counts": summ["class_counts"], "reproduction_max_abs_diff": summ["reproduction_max_abs_diff_p_home_win"]})


if __name__ == "__main__":
    main()
