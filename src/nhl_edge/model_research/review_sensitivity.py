"""Sensitivity of the frozen v1.0 LIVE hypothesis results to data-review defect D2 (quiet-market age rule).

Builds the LIVE panel twice from the market-audit work tables (v1.0 ``age_rule='event'`` and corrected ``'tick'``), restricted to games that started before the
prospective freeze, and evaluates the market-structure hypotheses (M1-M14; model-driven C1/C2 need prediction joins and are not re-run) on the LIVE tier only.
This is a sensitivity analysis: the frozen v1.0 results are NOT replaced.
    python -m nhl_edge.model_research.review_sensitivity --derived <work dir> --out docs/research/nhl-model-improvement/data
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from nhl_edge.market_audit import dev_only
from nhl_edge.market_audit import efficiency as E
from nhl_edge.market_audit import hypotheses as H
from nhl_edge.market_audit.run_registry import add_move, early_flag


def panel(derived: Path, rule: str) -> pd.DataFrame:
    ev, cm, g, oc, st = (pd.read_parquet(derived / f"{n}.parquet") for n in ("quote_events", "contract_master", "games", "outcomes_audit", "market_static"))
    p = E.with_returns(E.build_live_panel(ev, cm, g, oc, st, age_rule=rule))
    p = dev_only(p)
    p = add_move(p)
    p["early_season"] = early_flag(p, "2026-09-29")
    p = p[p["horizon_min"].isin([60, 1440])].copy()
    p["model_gap"] = np.nan
    return p


def run(derived: Path) -> dict:
    out: dict = {"rules": {}}
    for rule in ("event", "tick"):
        p = panel(derived, rule)
        n60 = int((p["horizon_min"] == 60).sum())
        res = {}
        for h in H.REGISTRY:
            if h.side == "model" or "LIVE" not in h.tiers:
                continue
            r = H.evaluate(h, p)
            res[h.id] = {k: r.get(k) for k in ("n_games", "n_contracts", "roi", "roi_lo95", "roi_hi95", "roi_slip_1c")}
        out["rules"][rule] = {"rows_T60": n60, "hypotheses": res}
    ev, tk = out["rules"]["event"]["hypotheses"], out["rules"]["tick"]["hypotheses"]
    out["max_abs_roi_change_pts"] = max(abs((tk[k]["roi"] or 0) - (ev[k]["roi"] or 0)) * 100 for k in ev if ev[k]["roi"] is not None and tk[k]["roi"] is not None)
    out["sign_flips"] = [k for k in ev if ev[k]["roi"] is not None and tk[k]["roi"] is not None and (ev[k]["roi"] > 0) != (tk[k]["roi"] > 0)]
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = run(a.derived)
    (a.out / "review_sensitivity_d2.json").write_text(json.dumps(r, indent=1, default=float))
    print({k: v["rows_T60"] for k, v in r["rules"].items()}, "max |ΔROI| pts", round(r["max_abs_roi_change_pts"], 2), "sign flips", r["sign_flips"])
    for k in r["rules"]["event"]["hypotheses"]:
        e, t = r["rules"]["event"]["hypotheses"][k], r["rules"]["tick"]["hypotheses"][k]
        print(k, e["n_games"], e["n_contracts"], t["n_contracts"], None if e["roi"] is None else round(e["roi"], 4), None if t["roi"] is None else round(t["roi"], 4))
