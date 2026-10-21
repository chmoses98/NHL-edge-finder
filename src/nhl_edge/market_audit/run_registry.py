"""Run the pre-registered hypothesis registry (once) and write machine-readable results.

``python -m nhl_edge.market_audit.run_registry --derived <dir> --wf-csv <walk_forward_games.csv> --out <results.json>``
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.market_audit import hypotheses as H

HIST_SEASON = ("2025-10-01", "2026-04-17")
EARLY_DAYS = 21


def add_move(p: pd.DataFrame) -> pd.DataFrame:
    """mid(T-60m) - mid(T-24h) per ticker, attached to the T-60m rows. Positive = the market moved toward YES."""
    a = p[p["horizon_min"] == 1440].set_index("ticker")["mid"]
    b = p[p["horizon_min"] == 60].set_index("ticker")["mid"]
    mv = (b - a).dropna().rename("move")
    return p.merge(mv, left_on="ticker", right_index=True, how="left")


def early_flag(p: pd.DataFrame, season_start: str) -> pd.Series:
    d0 = pd.Timestamp(season_start)
    return (pd.to_datetime(p["game_date"]) - d0).dt.days.between(0, EARLY_DAYS - 1)


def hist_model_gaps(p: pd.DataFrame, wf_csv: Path) -> pd.DataFrame:
    wf = pd.read_csv(wf_csv)
    wf["game_id"] = wf["game_id"].astype(int)
    out = []
    for _arm, pre, col in (("v1", "V1_", "model_gap_v1"), ("v2", "SIM2_ST_", "model_gap_v2")):
        m = wf.set_index("game_id")
        q = p[["ticker", "game_id", "kind", "threshold", "subject_team_id", "home_team_id", "mid"]].drop_duplicates("ticker")
        q = q[q["game_id"].isin(m.index)]
        pm = []
        for r in q.itertuples():
            row = m.loc[r.game_id]
            if r.kind == "winner":
                ph = row[pre + "p_home_win"]
                pr = ph if r.subject_team_id == r.home_team_id else 1 - ph
            elif r.kind == "total":
                key = f"{pre}p_over_{r.threshold}"
                pr = row[key] if key in m.columns else np.nan
            elif r.kind == "spread" and r.threshold == 1.5:
                pr = row[pre + ("p_home_minus_1_5" if r.subject_team_id == r.home_team_id else "p_away_minus_1_5")]
            else:
                pr = np.nan
            pm.append(pr - r.mid)
        out.append(pd.Series(pm, index=q["ticker"].to_numpy(), name=col))
    mg = pd.concat(out, axis=1)
    return p.merge(mg, left_on="ticker", right_index=True, how="left")


def live_model_gaps(p: pd.DataFrame, derived: Path) -> pd.DataFrame:
    """Last production prediction (V1 / V2) at or before the T-60m cut, minus the T-60m mid. Never a later prediction."""
    out = []
    for _kind, fn, col, pcol in (("v1", "raw_predictions.parquet", "model_gap_v1", "p_data_only"),
                                ("v2", "raw_predictions_v2.parquet", "model_gap_v2", "p_data_only_v2")):
        pr = pd.read_parquet(derived / fn, columns=["ticker", "predicted_at_utc", "market_observed_at_utc", pcol])
        pr = pr[pr[pcol].notna()].copy()
        pr["pa"] = pd.to_datetime(pr["predicted_at_utc"], utc=True)
        pr = pr.sort_values("pa")
        q = p[p["horizon_min"] == H.DECISION_HORIZON_MIN][["ticker", "cut", "mid"]].drop_duplicates("ticker").sort_values("cut")
        m = pd.merge_asof(q, pr[["ticker", "pa", pcol]], left_on="cut", right_on="pa", by="ticker", direction="backward")
        m[col] = m[pcol] - m["mid"]
        out.append(m.set_index("ticker")[col])
    mg = pd.concat(out, axis=1)
    return p.merge(mg, left_on="ticker", right_index=True, how="left")


def run(derived: Path, wf_csv: Path, out: Path) -> dict:
    hist = pd.read_parquet(derived / "hist_reg_panel.parquet")
    hist = hist[(hist["game_date"] >= HIST_SEASON[0]) & (hist["game_date"] <= HIST_SEASON[1])].copy()
    games_dates = hist.drop_duplicates("game_id").sort_values("game_date")
    cutoff = games_dates["game_date"].iloc[int(0.6 * len(games_dates))]
    hist = add_move(hist)
    hist["early_season"] = early_flag(hist, "2025-10-07")
    hist = hist_model_gaps(hist, wf_csv)
    tiers = {"HIST_DISC": hist[hist["game_date"] < cutoff], "HIST_HOLD": hist[hist["game_date"] >= cutoff]}
    live = pd.read_parquet(derived / "live_panel.parquet")
    live = add_move(live)
    live["early_season"] = early_flag(live, "2026-09-29")
    live = live[live["horizon_min"].isin([60, 1440])].copy()
    live = live_model_gaps(live, derived)
    tiers["LIVE"] = live
    results: dict[str, dict] = {}
    for h in H.REGISTRY:
        per = {}
        for t in h.tiers:
            df = tiers[t].copy()
            if h.side == "model":
                df["model_gap"] = df["model_gap_v1"] if h.id == "C1" else df["model_gap_v2"]
            per[t] = H.evaluate(h, df)
        results[h.id] = per
    live_p = {k: v["LIVE"]["p_one_sided"] for k, v in results.items() if "LIVE" in v and v["LIVE"].get("roi") is not None}
    q = H.bh_adjust(live_p)
    final = {}
    for h in H.REGISTRY:
        final[h.id] = {"title": h.title, "statement": h.statement, "side": h.side, "post_hoc_suggested": h.post_hoc, "group": h.group,
                       "tiers": results[h.id], "q_live_bh": q.get(h.id), "class": H.classify(results[h.id], q.get(h.id))}
    meta = {"registry_version": H.REGISTRY_VERSION, "decision_horizon_min": H.DECISION_HORIZON_MIN, "hist_disc_hold_cutoff_date": str(cutoff),
            "tier_games": {k: int(v["game_id"].nunique()) for k, v in tiers.items()}, "n_boot": H.N_BOOT}
    out.write_text(json.dumps({"meta": meta, "results": final}, indent=1, default=float))
    return {"meta": meta, "results": final}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--wf-csv", type=Path, required=True, help="docs/research/walk_forward_v2_wf2_20260929_games.csv")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = run(a.derived, a.wf_csv, a.out)
    print(json.dumps(r["meta"], indent=1))
    for k, v in r["results"].items():
        print(k, v["class"], {t: (x.get("n_games"), None if x.get("roi") is None else round(x["roi"], 3)) for t, x in v["tiers"].items()})
