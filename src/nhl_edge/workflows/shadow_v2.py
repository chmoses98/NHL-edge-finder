"""DATA_ONLY_V2 shadow arm for RUN NHL (RESEARCH_ONLY; never a gate, never an authority, never replaces V1).

``nhl simulate`` builds V1 exactly as before. Afterwards, from the SAME point-in-time context it already read (no
extra network request), this module:

1. reuses V1's team ratings, rest and goalie observations for each game;
2. adds nhl-features-2.0: explicit special teams (situation rows: the archived ``context/team_games_st`` kind when
   present, else the repository's historical MoneyPuck situation rows, which are all from completed past seasons)
   and point-in-time goalie true talent (repository goalie game logs, strictly before the game date), mixed over
   plausible starters with the same status confidences as V1 but start-share-weighted alternatives;
3. simulates with nhl-sim-2.0 (``data/params/nhl-sim-2.0.json``) and prices every contract V1 priced plus the period
   families (tagged PARTIAL_NEEDS_RULE_REVIEW);
4. returns rows for the separate ``predictions_v2`` ledger kind and a comparison block (V1, V2, market, the three
   differences) for the slate / packet.

Any exception here is caught by the caller and recorded; V1 output is identical with or without this module (tested).
"""

from __future__ import annotations

import json
import os
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge import AUTHORITY, DATA_ONLY_V2_MODEL_VERSION, FEATURE_V2_VERSION, SIM_V2_VERSION
from nhl_edge.config import REPO_ROOT
from nhl_edge.features import goalie_talent as gt
from nhl_edge.features import special_teams as stm
from nhl_edge.goalies.state import GoalieState, GoalieStatus
from nhl_edge.log import get_logger, kv
from nhl_edge.pricing.price_v2 import price_contract_v2
from nhl_edge.sim.engine import TeamParams, ladder_violations
from nhl_edge.sim.engine_v2 import load_params, period_violations, simulate_game_v2

log = get_logger(__name__)

FEATURE_PARAMS_PATH = REPO_ROOT / "data" / "params" / "nhl-features-2.0.json"
DISAGREEMENT_FLAG = 0.04  # |V1 - V2| on any supported contract above this is highlighted for human review


def enabled() -> bool:
    return os.environ.get("NHL_EDGE_V2_SHADOW", "1") not in ("0", "false", "False", "")


def load_feature_params(path: Path | None = None) -> dict[str, Any]:
    p = Path(path) if path else FEATURE_PARAMS_PATH
    base = {"use_special_teams": True, "goalie_model": "true_talent", "goalie_prior_xg": gt.DEFAULT_PRIOR_XG, "goalie_b2b_mult": 1.0}
    return base | (json.loads(p.read_text()) if p.exists() else {})


@dataclass
class V2Context:
    st_rows: pd.DataFrame
    st_source: str
    book: gt.GoalieBook | None
    goalie_source: str
    sim_params: Any
    fparams: dict[str, Any]


def build_context(data_root: Path, live_st_rows: list[dict[str, Any]] | None) -> V2Context:
    """Load everything V2 needs once per run. ``data_root`` is the repository ``data`` directory (history lives there)."""
    from nhl_edge.data.history import load_nhl_games, load_team_games
    from nhl_edge.data.shots import load_shots

    hist = Path(data_root) / "history"
    tg = load_team_games(hist)
    frames = []
    src = []
    if len(tg):
        frames.append(tg[tg["game_type"] == 2] if "game_type" in tg.columns else tg)
        src.append(f"history parquet seasons {sorted(int(s) for s in tg['season'].dropna().unique())}")
    if live_st_rows:
        live = pd.DataFrame(live_st_rows)
        if len(frames):
            seen = set(zip(frames[0]["gameId"].astype(str), frames[0]["situation"].astype(str), frames[0]["team"].astype(str)))
            live = live[[k not in seen for k in zip(live["gameId"].astype(str), live["situation"].astype(str), live["team"].astype(str))]]
        frames.append(live)
        src.append(f"archived context/team_games_st ({len(live)} new rows)")
    st_rows = stm.prepare_situation_log(pd.concat(frames, ignore_index=True)) if frames else pd.DataFrame()
    fparams = load_feature_params()
    book = None
    gsrc = "none (goalie factor 1.0)"
    shots = load_shots(hist)
    if len(shots):
        glog = gt.goalie_game_log(shots, load_nhl_games(hist))
        book = gt.GoalieBook(glog, prior_xg=float(fparams["goalie_prior_xg"]), b2b_mult=float(fparams["goalie_b2b_mult"]))
        gsrc = f"MoneyPuck goalie game logs {sorted(int(s) for s in glog['season'].unique())} (history, strictly before the game date)"
    return V2Context(st_rows, "; ".join(src) or "none", book, gsrc, load_params(), fparams)


def v2_goalie_factor(state: GoalieState, book: gt.GoalieBook | None, as_of: str, team_abbrev: str,
                     roster_goalies: list[int] | None = None) -> tuple[float, dict[str, Any]]:
    """Confidence-weighted mixture (V1's status ladder) of the named goalie's true talent and the START-SHARE-weighted
    talent of the plausible alternatives (V1 used a plain average of the observation's alternatives).

    Alternatives, in order of preference: the observation's own alternatives; else the CURRENT roster goalies
    (``context/rosters``); else last season's starters for this club from the goalie log (stale after trades, so only
    a last resort). Start share = the goalie's starts in his previous 82 appearances (any club) + 1.
    UNKNOWN -> the alternatives mixture alone (1.0 when nothing is known)."""
    if book is None:
        return 1.0, {"method": "no_goalie_data", "weight_named": 0.0}
    lr = book.league_ratio(as_of)
    alts = [int(a["player_id"]) for a in (state.alternatives or []) if a.get("player_id") is not None and a.get("player_id") != state.player_id]
    source = "observation"
    if not alts and roster_goalies:
        alts = [int(g) for g in roster_goalies if int(g) != state.player_id]
        source = "current_roster"
    if not alts:
        recent = book.log[(book.log["game_date"].astype(str) < as_of) & (book.log["team"] == team_abbrev)].tail(82)
        starts_team = Counter(int(x) for x in recent.loc[recent["starter"] == 1, "goalie_id"])
        alts = [g for g, _ in starts_team.most_common(3) if g != state.player_id]
        source = "last_season_team_starters"

    def starts(g: int) -> float:
        d = book.by_goalie.get(g)
        if d is None:
            return 0.0
        d = d[d["game_date"].astype(str) < as_of].tail(82)
        return float(d["starter"].sum())

    alt_w = np.array([starts(a) + 1.0 for a in alts]) if alts else np.array([])
    alt_f = np.array([book.factor(a, as_of, lr) for a in alts]) if alts else np.array([])
    alt = float((alt_w * alt_f).sum() / alt_w.sum()) if alts else 1.0
    alt_detail = {str(a): {"factor": round(float(f), 4), "weight": round(float(w / alt_w.sum()), 3)} for a, f, w in zip(alts, alt_f, alt_w)} if alts else {}
    if state.status == GoalieStatus.UNKNOWN or state.player_id is None:
        return alt, {"method": "unknown_starter_start_share_mixture", "alt_factor": alt, "alternatives": alt_detail, "alternatives_source": source,
                     "weight_named": 0.0}
    named_t = book.talent(state.player_id, as_of, lr)
    named = named_t.factor * named_t.workload_mult
    w = min(max(state.confidence, 0.0), 1.0)
    return w * named + (1 - w) * alt, {"method": "mixture_start_share_alternatives", "named_factor": named, "named_apps": named_t.apps_used,
                                       "named_rest_days": named_t.rest_days, "named_b2b": named_t.b2b, "alt_factor": alt, "weight_named": w,
                                       "alternatives": alt_detail, "alternatives_source": source}


def simulate_game_shadow(gi: Any, game: dict[str, Any], ctx: V2Context, seed: int, n_sims: int,
                         roster_goalies: dict[int, list[int]] | None = None) -> tuple[Any, dict[str, Any]]:
    """V2 lambdas from V1's GameInputs + V2 features, then an nhl-sim-2.0 draw. Returns (result, detail)."""
    from nhl_edge.data.moneypuck import mp_season

    date = gi.game_date_et
    season = mp_season(date)
    lst = stm.league_st(ctx.st_rows, date, season) if len(ctx.st_rows) else stm.DEFAULT_LEAGUE_ST
    hst = stm.team_st(ctx.st_rows, gi.home_abbrev, date, lst, season) if len(ctx.st_rows) else None
    ast = stm.team_st(ctx.st_rows, gi.away_abbrev, date, lst, season) if len(ctx.st_rows) else None
    use_st = bool(ctx.fparams.get("use_special_teams")) and hst is not None and ast is not None
    if ctx.fparams.get("goalie_model") == "true_talent":
        rg = roster_goalies or {}
        hf, hdet = v2_goalie_factor(gi.home_goalie, ctx.book, date, gi.home_abbrev, rg.get(gi.home_team_id))
        af, adet = v2_goalie_factor(gi.away_goalie, ctx.book, date, gi.away_abbrev, rg.get(gi.away_team_id))
    else:
        hf, hdet, af, adet = gi.home_goalie_factor, {"method": "v1_factor"}, gi.away_goalie_factor, {"method": "v1_factor"}
    dummy = stm.TeamST("LG", lst.ev_xg60, lst.ev_xg60, lst.pp_xg60, lst.pp_xg60, lst.ppmin, lst.ppmin, 0.0, {})
    lam_h, lam_a, comp = stm.expected_goals_v2(gi.home_rating, gi.away_rating, hst or dummy, ast or dummy, gi.league, lst, home_goalie_factor=hf,
                                               away_goalie_factor=af, home_b2b=gi.home_b2b, away_b2b=gi.away_b2b,
                                               neutral_site=bool(game.get("neutral_site")), use_special_teams=use_st)
    res = simulate_game_v2(TeamParams(gi.home_team_id, gi.home_abbrev, lam_h), TeamParams(gi.away_team_id, gi.away_abbrev, lam_a), seed=seed,
                           n_sims=n_sims, params=ctx.sim_params)
    detail = {"lam_home": lam_h, "lam_away": lam_a, "components": comp, "home_goalie_factor": hf, "away_goalie_factor": af,
              "home_goalie_detail": hdet, "away_goalie_detail": adet, "special_teams_used": use_st, "st_source": ctx.st_source,
              "goalie_source": ctx.goalie_source, "ladder_violations": ladder_violations(res) + period_violations(res)}
    return res, detail


def contract_rows(gid: str, res: Any, contracts: list[tuple[dict[str, Any], Any]], v1_by_ticker: dict[str, dict[str, Any]], home_id: int, away_id: int,
                  now: datetime, market_ts: datetime | None, seed: int, minutes_to_start: float, horizon: str, run_id: str) -> list[dict[str, Any]]:
    from nhl_edge.execution.economics import market_implied_probability
    from nhl_edge.timeutil import iso

    rows = []
    for m, c in contracts:
        pr, v2_support = price_contract_v2(c, res, home_id, away_id)
        v1 = v1_by_ticker.get(m["ticker"]) or {}
        p_v1 = v1.get("p_data_only")
        p_mkt = market_implied_probability(m).p_mid
        p_v2 = pr.p
        rows.append({
            "prediction_id": f"{m['ticker']}|{iso(now)}|{DATA_ONLY_V2_MODEL_VERSION}|{run_id}", "ticker": m["ticker"], "game_id": gid, "family": c.family,
            "title": m.get("title"), "period": c.period, "settles_on": c.settles_on, "stat": c.stat, "team_id": c.team_id, "threshold": c.threshold,
            "comparator": c.comparator, "predicted_at_utc": iso(now), "data_cutoff_utc": iso(now), "model_version": DATA_ONLY_V2_MODEL_VERSION,
            "sim_version": SIM_V2_VERSION, "feature_version": FEATURE_V2_VERSION, "n_sims": res.n_sims, "seed": seed,
            "p_data_only_v2": p_v2, "p_data_only_v2_se": pr.se, "p_data_only_v1": p_v1, "p_market": p_mkt,
            "v2_minus_market": (p_v2 - p_mkt) if (p_v2 is not None and p_mkt is not None) else None,
            "v1_minus_market": (p_v1 - p_mkt) if (p_v1 is not None and p_mkt is not None) else None,
            "v2_minus_v1": (p_v2 - p_v1) if (p_v2 is not None and p_v1 is not None) else None,
            "priced": pr.supported, "price_reason": pr.reason, "v2_support": v2_support, "v1_gate": v1.get("gate"), "role": "SHADOW",
            "authority": AUTHORITY, "market_observed_at_utc": iso(market_ts) if market_ts else None, "minutes_to_start": round(minutes_to_start, 1),
            "horizon_label": horizon,
        })
    return rows


def game_block(gid: str, gsum_v1: dict[str, Any], res: Any, detail: dict[str, Any], rows: list[dict[str, Any]]) -> dict[str, Any]:
    s = res.summary()
    big = sorted((r for r in rows if r.get("v2_minus_v1") is not None), key=lambda r: -abs(r["v2_minus_v1"]))
    flagged = [r for r in big if abs(r["v2_minus_v1"]) >= DISAGREEMENT_FLAG]
    return {
        "game_id": gid, "home": gsum_v1.get("home"), "away": gsum_v1.get("away"), "model_version": DATA_ONLY_V2_MODEL_VERSION, "sim_version": SIM_V2_VERSION,
        "feature_version": FEATURE_V2_VERSION, "role": "SHADOW", "authority": AUTHORITY,
        "v1": {k: gsum_v1.get(k) for k in ("p_home_win", "p_reg_tie", "exp_total", "exp_home_goals", "exp_away_goals", "lam_home", "lam_away")},
        "v2": {"p_home_win": s["p_home_win"], "p_reg_tie": s["p_reg_tie"], "p_overtime": s["p_overtime"], "exp_total": s["total_mean"],
               "exp_home_goals": s["home_goals_mean"], "exp_away_goals": s["away_goals_mean"], "lam_home": detail["lam_home"], "lam_away": detail["lam_away"],
               "periods": {k: s[k] for k in ("p1", "p2", "p3")}, "total_ladder": s["total_ladder"], "home_puckline_ladder": s["home_puckline_ladder"]},
        "detail": detail, "n_contracts": len(rows), "n_priced": sum(1 for r in rows if r["priced"]),
        "largest_v1_v2_disagreements": [{k: r[k] for k in ("ticker", "family", "p_data_only_v1", "p_data_only_v2", "p_market", "v2_minus_v1")} for r in big[:5]],
        "flagged_for_review": [r["ticker"] for r in flagged],
    }


def markdown(blocks: list[dict[str, Any]], note: str | None = None) -> str:
    f = lambda x, n=3: "" if x is None else f"{x:.{n}f}"  # noqa: E731
    L = ["", "## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)", "",
         "| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |", "|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for b in blocks:
        top = b["largest_v1_v2_disagreements"][0] if b["largest_v1_v2_disagreements"] else None
        gap = f"{top['ticker']} {top['v2_minus_v1']:+.3f}" if top else ""
        d = b["detail"]
        L.append(f"| {b['away']} @ {b['home']} | {f(b['v1']['p_home_win'])} | {f(b['v2']['p_home_win'])} | {f(b['v1']['p_reg_tie'])} | {f(b['v2']['p_reg_tie'])} | "
                 f"{f(b['v1']['exp_total'], 2)} | {f(b['v2']['exp_total'], 2)} | {f(d['home_goalie_factor'])}/{f(d['away_goalie_factor'])} | {gap} |")
    if note:
        L += ["", f"_{note}_"]
    return "\n".join(L) + "\n"


def run_shadow(games: list[dict[str, Any]], data_root: Path, live_st_rows: list[dict[str, Any]] | None, n_sims: int, now: datetime, market_ts: datetime | None,
               run_id: str, roster_rows: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    """games: [{"game": g, "gi": GameInputs, "gsum": V1 slate summary, "contracts": [(market, contract)], "v1_rows": [...], "seed": int,
    "minutes": float, "horizon": str}] -> {"rows": [...], "blocks": [...], "context": {...}}"""
    ctx = build_context(data_root, live_st_rows)
    roster_goalies: dict[int, list[int]] = {}
    for r in roster_rows or []:
        if r.get("position") == "G" and r.get("player_id") and r.get("team_id"):
            roster_goalies.setdefault(int(r["team_id"]), []).append(int(r["player_id"]))
    rows_all: list[dict[str, Any]] = []
    blocks = []
    for item in games:
        gi = item["gi"]
        seed = int(item["seed"]) ^ 0x5F3759DF
        res, detail = simulate_game_shadow(gi, item["game"], ctx, seed, n_sims, roster_goalies)
        v1_by_ticker = {r["ticker"]: r for r in item["v1_rows"]}
        rows = contract_rows(gi.game_id, res, item["contracts"], v1_by_ticker, gi.home_team_id, gi.away_team_id, now, market_ts, seed, item["minutes"],
                             item["horizon"], run_id)
        rows_all += rows
        blocks.append(game_block(gi.game_id, item["gsum"], res, detail, rows))
        log.info(kv(event="v2_shadow_game", game=gi.game_id, p_home_v2=round(res.p_win(True)[0], 3), p_ot_v2=round(res.p_overtime()[0], 3)))
    return {"rows": rows_all, "blocks": blocks, "context": {"st_source": ctx.st_source, "goalie_source": ctx.goalie_source,
                                                            "sim_params_provenance": ctx.sim_params.provenance, "feature_params": ctx.fparams}}
