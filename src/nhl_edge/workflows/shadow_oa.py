"""OA_RIDGE_V1 shadow arm for RUN NHL (RESEARCH_ONLY; never a gate, never an authority, never replaces V1).

``nhl simulate`` builds V1 exactly as before. Afterwards, from the SAME point-in-time context it already read (no extra network request),
this module re-rates every game with the opponent-adjusted ridge ratings of ``research.oa_model`` (fit on MoneyPuck rows dated strictly
before the game's date: the repository history plus the archived ``context/team_games`` snapshot), keeps V1's own finishing ratio,
goalie factors, home advantage and back-to-back terms, simulates with V1's simulator, seed and draw count, and returns

* ``OA_SVA``     the opponent-adjusted rates as fitted, and
* ``OA_SVA_C1``  the same with the sum / difference of the two rates recalibrated by the slopes frozen in ``data/params/oa-ridge-1.0.json``
                 (the second primary challenger of docs/research/oa-walk-forward/PREREGISTRATION.md),

each with the incumbent V1 probabilities beside it, so a prospective paired comparison needs nothing but this ledger kind (``predictions_oa``)
and the official results. Any exception is caught by the caller and recorded; V1 output is identical with or without this module (tested).
"""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import replace
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from nhl_edge import AUTHORITY
from nhl_edge.config import REPO_ROOT
from nhl_edge.features.ratings import expected_goals
from nhl_edge.log import get_logger
from nhl_edge.research.oa_model import OAConfig, OAData, build_oa_data, fit_oa, oa_team_ratings
from nhl_edge.sim.engine import SimConfig, TeamParams, simulate_game
from nhl_edge.timeutil import iso

log = get_logger(__name__)

MODEL_VERSION = "OA_RIDGE_V1"
PARAMS_PATH = REPO_ROOT / "data" / "params" / "oa-ridge-1.0.json"
ARMS = ("OA_SVA", "OA_SVA_C1")


def enabled() -> bool:
    return os.environ.get("NHL_EDGE_OA_SHADOW", "1") not in ("0", "false", "False", "")


def load_params(path: Path | None = None) -> dict[str, Any]:
    return json.loads(Path(path or PARAMS_PATH).read_text())


def normalize_live_team_games(rows: list[dict[str, Any]]) -> pd.DataFrame:
    """Archived ``context/team_games`` rows (MoneyPuck game-by-game, ``situation == 'all'``) in the schema ``build_oa_data`` reads."""
    if not rows:
        return pd.DataFrame()
    d = pd.DataFrame(rows)
    for col in ("playoffGame", "opposingTeam", "opp_abbrev"):
        if col not in d.columns:
            d[col] = None
    d = d[d["situation"] == "all"].copy()
    d["team_abbrev"] = d["team"]
    d["mp_team"] = d["team"]
    d["opp_abbrev"] = d["opp_abbrev"].where(d["opp_abbrev"].notna(), d["opposingTeam"])
    d["mp_opposing_team"] = d["opposingTeam"]
    d["home"] = d["home_or_away"].astype(str).str.upper().eq("HOME")
    d["game_id"] = pd.to_numeric(d["gameId"], errors="coerce")
    gd = d["gameDate"].astype(str).str.replace("-", "").str[:8]
    d["game_date"] = gd.str[:4] + "-" + gd.str[4:6] + "-" + gd.str[6:8]
    d["game_type"] = d["playoffGame"].fillna(0).astype(int).map(lambda v: 3 if v else 2)
    return d.dropna(subset=["game_id", "iceTime"])


def build_context(data_root: Path, live_rows: list[dict[str, Any]], params: dict[str, Any]) -> dict[str, Any]:
    from nhl_edge.data.history import load_team_games, pinned_seasons

    # fit_oa reads at most MAX_SEASONS_BACK seasons, so the recent pinned seasons are all it can use; reading older research history
    # (2008-2021) would only cost start-up time in the production simulate job
    hist = load_team_games(Path(data_root) / "history", pinned_seasons(Path(data_root) / "history", "moneypuck"))
    live = normalize_live_team_games(live_rows)
    frames = [hist]
    src = [f"history parquet seasons {sorted(int(s) for s in hist['season'].dropna().unique())}"]
    if len(live):
        seen = set(zip(hist["game_id"].astype(float), hist["team_abbrev"].where(hist["team_abbrev"].notna(), hist["mp_team"]), strict=False))
        keep = [(g, t) not in seen for g, t in zip(live["game_id"].astype(float), live["team_abbrev"], strict=False)]
        live = live[keep]
        frames.append(live)
        src.append(f"archived context/team_games ({len(live)} new rows)")
    allrows = pd.concat([f for f in frames if len(f)], ignore_index=True)
    data = build_oa_data(allrows)
    cfg = OAConfig(half_life_days=float(params["half_life_days"]), ridge=float(params["ridge"]), season_discount=float(params["season_discount"]), target=params["target"])
    return {"data": data, "cfg": cfg, "params": params, "source": "; ".join(src), "fits": {}}


def _calibrate(params: dict[str, Any], lam_h: float, lam_a: float) -> tuple[float, float]:
    s, d = lam_h + lam_a, lam_h - lam_a
    s2 = params["mean_sum"] + params["slope_total"] * (s - params["mean_sum"])
    d2 = params["mean_diff"] + params["slope_margin"] * (d - params["mean_diff"])
    return max((s2 + d2) / 2.0, 0.3), max((s2 - d2) / 2.0, 0.3)


def run_shadow(items: list[dict[str, Any]], ctx: dict[str, Any], season: int, n_sims: int, now: datetime, run_id: str) -> dict[str, Any]:
    data: OAData = ctx["data"]
    params, cfg = ctx["params"], ctx["cfg"]
    psha = params.get("sha256") or hashlib.sha256(json.dumps(params, sort_keys=True).encode()).hexdigest()
    rows: list[dict[str, Any]] = []
    blocks: list[dict[str, Any]] = []
    for it in items:
        gi, g, v1 = it["gi"], it["game"], it["gsum"]
        as_of = int(str(gi.game_date_et).replace("-", ""))
        fit = ctx["fits"].get(as_of)
        if fit is None:
            fit = ctx["fits"].setdefault(as_of, fit_oa(data, as_of, season, cfg))
        oh, oa = oa_team_ratings(fit, data, gi.home_abbrev, gi.away_abbrev, gi.league)
        oh, oa = replace(oh, finish=gi.home_rating.finish), replace(oa, finish=gi.away_rating.finish)
        lam_h, lam_a, _ = expected_goals(oh, oa, gi.league, gi.home_goalie_factor, gi.away_goalie_factor, gi.home_b2b, gi.away_b2b)
        lams = {"OA_SVA": (lam_h, lam_a), "OA_SVA_C1": _calibrate(params, lam_h, lam_a)}
        block: dict[str, Any] = {"game_id": gi.game_id, "home": gi.home_abbrev, "away": gi.away_abbrev, "v1": {k: v1.get(k) for k in ("lam_home", "lam_away", "p_home_win", "p_overtime", "exp_total")}}
        for arm, (lh, la) in lams.items():
            res = simulate_game(TeamParams(gi.home_team_id, gi.home_abbrev, lh), TeamParams(gi.away_team_id, gi.away_abbrev, la), seed=it["seed"], config=SimConfig(n_sims=n_sims))
            s = res.summary()
            rec = {"p_home_win": s["p_home_win"], "p_overtime": s["p_overtime"], "exp_total": s["total_mean"], "lam_home": lh, "lam_away": la,
                   "p_over_5.5": res.p_total_gt(5.5)[0], "p_over_6.5": res.p_total_gt(6.5)[0]}
            block[arm] = rec
            rows.append({"prediction_id": f"{gi.game_id}|{arm}|{iso(now)}|{run_id}", "game_id": gi.game_id, "arm": arm, "model_version": MODEL_VERSION, "params_sha256": psha,
                         "predicted_at_utc": iso(now), "data_cutoff_utc": iso(now), "start_time_utc": g["start_time_utc"], "minutes_to_start": it["minutes"], "horizon_label": it["horizon"],
                         "home": gi.home_abbrev, "away": gi.away_abbrev, "home_team_id": gi.home_team_id, "away_team_id": gi.away_team_id, "seed": it["seed"], "n_sims": n_sims, **rec,
                         "v1_p_home_win": v1.get("p_home_win"), "v1_p_overtime": v1.get("p_overtime"), "v1_exp_total": v1.get("exp_total"), "v1_lam_home": v1.get("lam_home"),
                         "v1_lam_away": v1.get("lam_away"), "home_goalie_status": gi.home_goalie.to_dict().get("status"), "away_goalie_status": gi.away_goalie.to_dict().get("status"),
                         "pregame": it["minutes"] > 0, "role": "SHADOW", "authority": AUTHORITY})
        blocks.append(block)
    return {"blocks": blocks, "rows": rows, "model_version": MODEL_VERSION, "role": "SHADOW", "authority": AUTHORITY, "params_sha256": psha,
            "context": {"source": ctx["source"], "params_version": params.get("version"), "season_params": params.get("season")},
            "note": "OA_RIDGE_V1 is a SHADOW research arm; it never gates, never replaces V1 and carries no authority. Validation: docs/research/oa-walk-forward/RESULTS.md."}
