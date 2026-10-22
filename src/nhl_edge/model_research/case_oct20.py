"""Explanatory case study of the four 2026-10-20 routed wagers (NOT a validation sample; nothing is tuned to these games).

For each wager: the contract, the production V1/V2 probabilities at the T-60 cut, the Kalshi mid at the cut, the actual fill (price, fee, minutes vs scheduled drop), the
model's net EV at the fill price, where the realised score fell in the V1 predictive distribution, goalie facts and the result. Wager facts come from the review's reconstruction
(``wager_rows.csv``, built from the accounting ledger; the ledger is never modified).
    python -m nhl_edge.model_research.case_oct20 --live <live_t60.parquet> --attr <live_attr.parquet> --derived <work dir> --wagers <wager_rows.csv> --out <data dir>
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge.market_audit.expression_engine import fee
from nhl_edge.model_research.wf_data import simulate_row
from nhl_edge.sim.engine import SimConfig


def contract_prob(res: Any, family: str, line: float, subj_home: bool | None, side: str) -> float:
    if family == "game_total":
        p_yes = float((res.total > line).mean())
    else:  # team_total: subject team goals over the line
        p_yes = float(((res.home_final if subj_home else res.away_final) > line).mean())
    return p_yes if side == "YES" else 1 - p_yes


def run(live: pd.DataFrame, attr: pd.DataFrame, derived: Path, wagers: pd.DataFrame) -> list[dict[str, Any]]:
    w = wagers[wagers["game_date_et"] == "2026-10-20"]
    p2 = pd.read_parquet(derived / "raw_predictions_v2.parquet", columns=["ticker", "predicted_at_utc", "p_data_only_v2"])
    lp = pd.read_parquet(derived / "live_panel.parquet")
    out = []
    for r in w.itertuples():
        away, home = [x.strip() for x in r.game.split("@")]
        g = attr[(attr["home"] == home) & (attr["away"] == away)].iloc[0]
        lv = live[live["game_id"] == g["game_id"]].iloc[0]
        res = simulate_row(lv["v1_lam_home"], lv["v1_lam_away"], int(lv["v1_seed"]), int(lv["v1_n_sims"]), SimConfig(n_sims=int(lv["v1_n_sims"])))
        subj_home = None
        if r.market_family == "team_total":
            subj = r.ticker.split("-")[-1][:-1]  # LA3 -> LA, ANA3 -> ANA (Kalshi club code; a prefix of the NHL abbreviation here)
            subj_home = bool(home.startswith(subj) and not away.startswith(subj))
        side = r.side
        p_side = contract_prob(res, r.market_family, float(r.line), subj_home, side)
        cut = pd.Timestamp(lv["cut_utc"])
        v2 = p2[(p2["ticker"] == r.ticker) & (pd.to_datetime(p2["predicted_at_utc"], utc=True) <= cut)].sort_values("predicted_at_utc").tail(1)
        v2_yes = float(v2["p_data_only_v2"].iloc[0]) if len(v2) else None
        mid = lp[(lp["ticker"] == r.ticker) & (lp["horizon_min"] == 60)]
        mid_yes = float(mid["mid"].iloc[0]) if len(mid) else None
        price = float(r.price)
        row = {"wager_id": r.wager_id, "ticker": r.ticker, "game": r.game, "family": r.market_family, "line": float(r.line), "side": side, "fill_utc": r.executed_at,
               "minutes_vs_scheduled_drop": float(r.minutes_vs_puck_drop), "contracts": float(r.contracts), "price": price, "fee": float(r.fee), "net_pl": float(r.net_pl_ledger), "result": r.ledger_result,
               "v1_p_side": p_side, "v1_net_ev_per_contract_at_fill": p_side - price - fee(price),
               "v2_p_side": None if v2_yes is None else (v2_yes if side == "YES" else 1 - v2_yes),
               "kalshi_mid_yes_at_cut": mid_yes, "kalshi_p_side_at_cut": None if mid_yes is None else (mid_yes if side == "YES" else 1 - mid_yes),
               "score": f"{away} {int(g['away_final'])} - {int(g['home_final'])} {home}", "period_type": g["last_period_type"], "pit_total": float(g["pit_total"]), "pit_margin": float(g["pit_margin"]),
               "attribution_class": g["attribution_class"], "lam_home": float(lv["v1_lam_home"]), "lam_away": float(lv["v1_lam_away"]),
               "goalies_at_cut": f"{lv['home_goalie_name']} ({lv['home_goalie_status']}) / {lv['away_goalie_name']} ({lv['away_goalie_status']})",
               "goalie_of_record_matches_named": not bool(g["any_goalie_mismatch"]),
               "home_goalie_sv": f"{int(g['actual_home_saves'])}/{int(g['actual_home_shots_against'])}", "away_goalie_sv": f"{int(g['actual_away_saves'])}/{int(g['actual_away_shots_against'])}",
               "thesis_status_before_fill": r.thesis_last_before_fill_status if isinstance(r.thesis_last_before_fill_status, str) else None}
        out.append(row)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", type=Path, required=True)
    ap.add_argument("--attr", type=Path, required=True)
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--wagers", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    rows = run(pd.read_parquet(a.live), pd.read_parquet(a.attr), a.derived, pd.read_csv(a.wagers))
    (a.out / "oct20_case_model_view.json").write_text(json.dumps(rows, indent=1, default=float))
    print(json.dumps(rows, indent=1, default=float)[:6000])
    print("net", round(sum(r["net_pl"] for r in rows), 4), "n", len(rows))
