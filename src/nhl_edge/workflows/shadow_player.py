"""PLAYER_SIM_V1 shadow arm for RUN NHL (RESEARCH_ONLY; never a gate, never an authority, never alters V1 or V2).

After ``nhl simulate`` has written V1 and the DATA_ONLY_V2 shadow, this module (same point-in-time snapshot, no extra
network request):

1. loads the persisted parameters (``data/params/player-sim-1.0.json``), the repository's official player-event history
   and every archived ``player_events/*`` partition observed at or before ``now`` (games ingested by the settle job);
2. projects each team's dressed skaters and deployment: tonight's DailyFaceoff lines (``context/lines``) when present
   (confirmed from warmups / morning skate, else projected), otherwise the team's most recent dressed lineup
   intersected with the current roster; ESPN "Out" / IR players are removed;
3. re-draws the game with nhl-sim-2.0 from the V2 shadow's own lambdas and seed (identical team outcomes to the V2
   shadow) with per-step recording, allocates every goal (``players.engine``), simulates both goalies' saves;
4. prices every joined player contract (goals / assists / points / saves / first goal) and writes one row per contract
   to the separate ``predictions_player`` kind, plus a per-game block (players, goalies, correlation of the game's
   modelled contracts) for the packet.

Any failure is caught by the caller and recorded; V1 and V2 rows are byte-identical with or without this module.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge import AUTHORITY
from nhl_edge.data.lines import is_confirmed_source
from nhl_edge.data.player_history import load_player_tables
from nhl_edge.log import get_logger, kv
from nhl_edge.players import PLAYER_ANCHORED_VERSION, PLAYER_FEATURE_VERSION, PLAYER_MODEL_VERSION, PLAYER_SIM_VERSION
from nhl_edge.players import xg as X
from nhl_edge.players.engine import StrengthTable, invariant_violations, simulate_players
from nhl_edge.players.features import (
    LeaguePriors,
    PlayerBook,
    PlayerParams,
    build_player_games,
    coice_fractions,
    pos_group,
)
from nhl_edge.players.fit import PARAMS_PATH
from nhl_edge.players.identity import parse_player_market, resolve_player
from nhl_edge.players.params import SavesModel, ShotRates, team_game_frame
from nhl_edge.players.pricing import PLAYER_FAMILIES, ladder_violations, price_player
from nhl_edge.players.roster import Deployment, build_roster
from nhl_edge.players.saves import simulate_saves
from nhl_edge.sim.engine import TeamParams
from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

log = get_logger(__name__)

TABLES = ("players", "goalies", "goals", "shots", "coice", "team_states")
ANCHOR_WEIGHT = 0.80  # MARKET_ANCHORED_PLAYER_V1 prior weight on the market (as MARKET_ANCHORED_V1); not independent evidence
LINES_MAX_AGE_H = 72.0
CORR_MAX_CONTRACTS = 40


def enabled() -> bool:
    return os.environ.get("NHL_EDGE_PLAYER_SHADOW", "1") not in ("0", "false", "False", "")


def _date_int(s: Any) -> int:
    return int(str(s).replace("-", "")[:8])


@dataclass
class PlayerRuntime:
    params: dict[str, Any]
    book: PlayerBook
    players: pd.DataFrame
    goalies: pd.DataFrame
    coice: pd.DataFrame
    toi_games: pd.DataFrame
    rates: ShotRates
    strength: StrengthTable
    saves: SavesModel
    sources: dict[str, Any]


def load_runtime(data_root: Path, live: dict[str, list[dict[str, Any]]] | None = None, params_path: Path | None = None) -> PlayerRuntime:
    prm = json.loads(Path(params_path or PARAMS_PATH).read_text())
    hist = Path(data_root) / "history"
    t = {k: load_player_tables(hist, k) for k in TABLES}
    n_live = 0
    for k in TABLES:
        rows = (live or {}).get(k) or []
        if rows:
            df = pd.DataFrame(rows).drop(columns=[c for c in ("_observed_at_utc", "_run_id") if c in (rows[0] or {})], errors="ignore")
            known = set(t[k]["game_id"].unique()) if len(t[k]) else set()
            df = df[~df["game_id"].isin(known)]
            if k == "players":
                n_live = int(df["game_id"].nunique()) if len(df) else 0
            t[k] = pd.concat([t[k], df], ignore_index=True) if len(t[k]) else df
    for k in TABLES:
        if len(t[k]):
            t[k]["date_int"] = t[k]["game_date"].map(_date_int)
    goals = t["goals"][t["goals"].get("game_type", 2) == 2] if "game_type" in t["goals"].columns else t["goals"]
    xg = X.XGModel.from_dict(prm["xg"])
    pg = build_player_games(t["players"], goals, t["shots"], t["team_states"], X.score(t["shots"], xg))
    pri = LeaguePriors.from_dict(prm["priors"])
    book = PlayerBook(pg, pri, PlayerParams.from_dict(prm["player_params"]))
    tg = team_game_frame(t["goalies"], goals)
    rates = ShotRates(float(prm.get("league_shots_per_game") or tg["sa"].mean()), tg)
    src = {"history_seasons": sorted(int(s) for s in t["players"]["season"].dropna().unique()) if len(t["players"]) else [],
           "live_games_ingested": n_live, "params": prm.get("provenance"), "last_game_date": str(t["players"]["game_date"].max()) if len(t["players"]) else None}
    return PlayerRuntime(prm, book, t["players"], t["goalies"], t["coice"], pg[["game_id", "player_id", "toi_ev", "toi_pp", "toi_sh"]], rates,
                         StrengthTable.from_dict(prm["strength"]), SavesModel.from_dict(prm["saves"]), src)


def _injured(injuries: list[dict[str, Any]], team_id: int) -> set[str]:
    from nhl_edge.data.lines import fold

    out = set()
    for i in injuries or []:
        st = str(i.get("status") or "").lower()
        if i.get("team_id") == team_id and (st in ("out", "injured reserve", "ir", "long-term ir", "suspension") or "reserve" in st):
            out.add(fold(i.get("player_name")))
    return out


def project_lineup(rt: PlayerRuntime, team_id: int, date_int: int, roster: list[dict[str, Any]], lines: list[dict[str, Any]], injuries: list[dict[str, Any]],
                   now: datetime) -> tuple[list[dict[str, Any]], Deployment, list[str], list[dict[str, Any]]]:
    """(dressed skaters, deployment, notes, goalies on the team) for one team."""
    from nhl_edge.data.lines import fold
    from nhl_edge.timeutil import parse_iso

    notes: list[str] = []
    ro = [r for r in roster if r.get("team_id") == team_id]
    goalies = [r for r in ro if r.get("position") == "G"]
    skaters_ro = {int(r["player_id"]): r for r in ro if r.get("position") != "G" and r.get("player_id") is not None}
    out_names = _injured(injuries, team_id)
    lr = [r for r in lines if r.get("team_id") == team_id and r.get("player_id") is not None]
    dep = None
    if lr:
        upd = lr[0].get("lines_updated_at_utc")
        try:
            age_h = (now - parse_iso(upd)).total_seconds() / 3600 if upd else 1e9
        except ValueError:
            age_h = 1e9
        if age_h <= LINES_MAX_AGE_H:
            confirmed = is_confirmed_source(lr[0].get("lines_source")) and age_h <= 12
            dep = Deployment.from_line_rows(lr, confirmed)
            notes.append(f"lines: {lr[0].get('lines_source')} updated {upd} ({age_h:.1f} h old)")
        else:
            notes.append(f"lines older than {LINES_MAX_AGE_H:.0f} h ignored")
    if dep is not None and len(dep.ev) >= 16:
        ids = [p for p in dep.ev if p not in dep.out]
        dressed = [{"player_id": p, "name": f"{skaters_ro.get(p, {}).get('first_name', '')} {skaters_ro.get(p, {}).get('last_name', '')}".strip() or str(p),
                    "position": skaters_ro.get(p, {}).get("position") or ("D" if dep.ev[p].startswith("d") else "C")} for p in ids]
        return dressed, dep, notes, goalies
    # fallback: the team's most recent dressed lineup, restricted to the current roster, topped up by ice time
    pl = rt.players[(rt.players["team_id"] == team_id) & (rt.players["date_int"] < date_int)]
    last_ids: list[int] = []
    if len(pl):
        last_gid = pl.loc[pl["date_int"].idxmax(), "game_id"]
        last_ids = [int(x) for x in pl[pl["game_id"] == last_gid]["player_id"]]
    cand = [p for p in last_ids if p in skaters_ro]
    notes.append(f"no usable lines: last lineup ({len(cand)}/{len(last_ids)} still on roster) + roster fill")
    pool = [p for p in skaters_ro if p not in cand]
    pool.sort(key=lambda p: -(rt.book.profile(p, date_int).toi_mean_s if np.isfinite(rt.book.profile(p, date_int).toi_mean_s) else 0.0))
    chosen = [p for p in cand if fold(f"{skaters_ro[p].get('first_name', '')}{skaters_ro[p].get('last_name', '')}") not in out_names]
    nf = sum(1 for p in chosen if pos_group(skaters_ro[p].get("position")) == "F")
    nd = len(chosen) - nf
    for p in pool:
        if fold(f"{skaters_ro[p].get('first_name', '')}{skaters_ro[p].get('last_name', '')}") in out_names:
            continue
        g = pos_group(skaters_ro[p].get("position"))
        if g == "F" and nf < 12:
            chosen.append(p)
            nf += 1
        elif g == "D" and nd < 6:
            chosen.append(p)
            nd += 1
    dressed = [{"player_id": p, "name": f"{skaters_ro[p].get('first_name', '')} {skaters_ro[p].get('last_name', '')}".strip(), "position": skaters_ro[p].get("position")}
               for p in chosen]
    return dressed, Deployment(), notes, goalies


def _anchored(p: float | None, m: float | None, w: float = ANCHOR_WEIGHT) -> float | None:
    if p is None or m is None or not (0 < m < 1):
        return None
    lg = lambda x: np.log(min(max(x, 1e-4), 1 - 1e-4) / (1 - min(max(x, 1e-4), 1 - 1e-4)))  # noqa: E731
    return float(1 / (1 + np.exp(-(w * lg(m) + (1 - w) * lg(p)))))


def run_player_shadow(items: list[dict[str, Any]], v2_blocks: list[dict[str, Any]], data_root: Path, now: datetime, market_ts: datetime | None, run_id: str,
                      rosters: list[dict[str, Any]], lines: list[dict[str, Any]], injuries: list[dict[str, Any]], live: dict[str, list[dict[str, Any]]],
                      fee_for: Any, goalie_states: dict[str, dict[str, Any]] | None = None, n_sims: int = 10000) -> dict[str, Any]:
    from nhl_edge.execution.economics import compute_economics, market_implied_probability
    from nhl_edge.timeutil import iso

    rt = load_runtime(data_root, live)
    sp = load_params()
    lam_by_game = {str(b["game_id"]): b for b in v2_blocks or []}
    rows_all: list[dict[str, Any]] = []
    blocks: list[dict[str, Any]] = []
    def _one_game(it: dict[str, Any]) -> None:
        gi = it["gi"]
        gid = str(gi.game_id)
        b = lam_by_game.get(gid)
        if b is None:
            blocks.append({"game_id": gid, "error": "no V2 lambdas for this game (V2 shadow failed or disabled)"})
            return
        di = _date_int(gi.game_date_et)
        detail = b.get("detail") or {}
        comp = detail.get("components") or {}
        teams = {}
        for side, tid, ab in (("home", gi.home_team_id, gi.home_abbrev), ("away", gi.away_team_id, gi.away_abbrev)):
            dressed, dep, notes, goalies = project_lineup(rt, int(tid), di, rosters, lines, injuries, now)
            if len(dressed) < 12:
                raise ValueError(f"{ab}: only {len(dressed)} projected skaters (no roster / lineup source): UNPRICEABLE")
            ev, pp, sh = comp.get(f"ev_{side}"), comp.get(f"pp_{side}"), comp.get(f"sh_{side}")
            p_pp = float(pp / (ev + pp + sh)) if ev and pp is not None and sh is not None and (ev + pp + sh) > 0 else 0.215
            p_sh = float(sh / (ev + pp + sh)) if ev and pp is not None and sh is not None and (ev + pp + sh) > 0 else 0.028
            team_min = {"ev": 50.6, "pp": 4.4 * p_pp / 0.215, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}
            pids = [p["player_id"] for p in dressed]
            F = coice_fractions(rt.coice, int(tid), di, pids, rt.toi_games)
            rb = build_roster(rt.book, int(tid), ab, di, dressed, F, p_pp, p_sh, team_min, season=int(str(gi.game_date_et)[:4]) - (1 if int(str(gi.game_date_et)[5:7]) < 7 else 0),
                              deployment=dep)
            teams[side] = {"rb": rb, "notes": notes, "goalies": goalies, "dep": dep}
        seed = int(it["seed"]) ^ 0x5F3759DF  # the V2 shadow's seed: identical team outcomes
        res = simulate_game_v2(TeamParams(gi.home_team_id, gi.home_abbrev, float(b["v2"]["lam_home"])), TeamParams(gi.away_team_id, gi.away_abbrev, float(b["v2"]["lam_away"])),
                               seed=seed, n_sims=n_sims, params=sp, record_steps=True)
        ps = simulate_players(res, teams["home"]["rb"].roster, teams["away"]["rb"].roster, rt.strength, seed + 11)
        viol = invariant_violations(res, ps) + ladder_violations(ps)
        saves = {}
        goalie_team: dict[int, int] = {}
        goalie_blocks = []
        for side, tid, oid, home in (("home", gi.home_team_id, gi.away_team_id, True), ("away", gi.away_team_id, gi.home_team_id, False)):
            ef = rt.rates.expected_faced(int(tid), int(oid), di, home)
            sd = simulate_saves(res, ps, home, rt.saves, ef, seed + (21 if home else 22))
            saves[int(tid)] = sd
            for g in teams[side]["goalies"]:
                goalie_team[int(g["player_id"])] = int(tid)
            gstate = (goalie_states or {}).get(f"{gid}|{side}") or {}
            goalie_blocks.append({"team": gi.home_abbrev if home else gi.away_abbrev, "projected_starter": gstate.get("player_name"),
                                  "starter_status": gstate.get("status"), "starter_confidence": gstate.get("confidence"), "expected_shots_faced": round(ef, 2),
                                  "expected_saves": round(float(sd.saves.mean()), 2), "saves_sd": round(float(sd.saves.std()), 2),
                                  "expected_goals_against": round(float(sd.goals_against.mean()), 2), "pull_risk": round(float(sd.replaced.mean()), 3),
                                  "saves_ladder": {k: round(v, 4) for k, v in sd.ladder(15, 40).items()},
                                  "note": "conditional on this net's starter playing; Kalshi settles a goalie who never enters at the pre-game fair price"})
        # contracts
        rows = []
        corr_cols: list[tuple[str, np.ndarray]] = []
        for m, c in it["contracts"]:
            if c.family not in PLAYER_FAMILIES:
                return
            ref = parse_player_market(m["ticker"], m.get("title"))
            pid, how = resolve_player(ref, rosters) if ref else (None, "ticker suffix not parsed")
            pr = price_player(c.family, c.comparator, c.threshold, pid, ps, saves, goalie_team)
            mi = market_implied_probability(m)
            p_mkt = mi.p_mid
            econ = compute_economics(m, pr.p, pr.se or 0.0, schedule=fee_for(m), observed_at=market_ts, now=now) if pr.p is not None else None
            meta: dict[str, Any] = {}
            found = ps.player(pid) if pid is not None else None
            if found is not None:
                d, ro, i = found
                side = "home" if ro.team_id == gi.home_team_id else "away"
                pm = teams[side]["rb"].player_meta.get(int(pid), {})
                meta = {"team": ro.abbrev, "opponent": gi.away_abbrev if side == "home" else gi.home_abbrev, "expected_toi_min": round(pm.get("expected_toi_total_min", 0.0), 2),
                        "expected_pp_toi_min": round(pm.get("expected_toi_min", {}).get("pp", 0.0), 2), "expected_shots": round(pm.get("expected_sog", 0.0), 2),
                        "expected_goals": round(float(d.goals[:, i].mean()), 3), "expected_assists": round(float(d.assists[:, i].mean()), 3),
                        "expected_points": round(float(d.points[:, i].mean()), 3),
                        "toi_p10_p50_p90_min": [round(float(x), 1) for x in np.percentile(d.toi_mult[:, i] * pm.get("expected_toi_total_min", 0.0), [10, 50, 90])],
                        "projection_quality": pm.get("projection_quality"),
                        "role_confidence": pm.get("role_confidence"), "uncertainty_flags": pm.get("uncertainty_flags"), "ev_slot": pm.get("ev_slot"),
                        "pp_unit": pm.get("pp_unit"), "deployment_source": pm.get("deployment_source"), "n_games_history": pm.get("n_games")}
                if pr.p is not None:
                    x = {"goals": d.goals[:, i], "assists": d.assists[:, i], "points": d.points[:, i]}.get(PLAYER_FAMILIES[c.family])
                    if x is not None and c.threshold is not None:
                        corr_cols.append((m["ticker"], (x > c.threshold).astype(np.float32)))
            elif pid is not None and c.family == "goalie_saves":
                tid = goalie_team.get(int(pid))
                sd = saves.get(tid) if tid is not None else None
                if sd is not None:
                    meta = {"team": gi.home_abbrev if tid == gi.home_team_id else gi.away_abbrev, "expected_shots_faced": round(sd.expected_faced, 2),
                            "expected_saves": round(float(sd.saves.mean()), 2), "pull_risk": round(float(sd.replaced.mean()), 3)}
                    if c.threshold is not None and pr.p is not None:
                        corr_cols.append((m["ticker"], (sd.saves > c.threshold).astype(np.float32)))
            q = m.get("_quote_cents") or {}
            rows.append({
                "prediction_id": f"{m['ticker']}|{iso(now)}|{PLAYER_MODEL_VERSION}|{run_id}", "ticker": m["ticker"], "game_id": gid, "family": c.family,
                "title": m.get("title"), "player_id": pid, "player_resolution": how, "player_name": (ref.name if ref else None), "threshold": c.threshold,
                "comparator": c.comparator, "predicted_at_utc": iso(now), "data_cutoff_utc": iso(now), "model_version": PLAYER_MODEL_VERSION,
                "sim_version": PLAYER_SIM_VERSION, "feature_version": PLAYER_FEATURE_VERSION, "n_sims": n_sims, "seed": seed,
                "p_player": pr.p, "p_player_se": pr.se, "priced": pr.supported, "price_reason": pr.reason, "p_market": p_mkt,
                "p_market_anchored": _anchored(pr.p, p_mkt), "market_anchored_model_version": PLAYER_ANCHORED_VERSION, "market_anchor_weight": ANCHOR_WEIGHT,
                "player_minus_market": (pr.p - p_mkt) if (pr.p is not None and p_mkt is not None) else None,
                "market_yes_bid": q.get("yes_bid"), "market_yes_ask": q.get("yes_ask"), "market_no_bid": q.get("no_bid"), "market_no_ask": q.get("no_ask"),
                "edge_yes_raw": econ.yes.gross_edge if econ else None, "edge_yes_after_fee": econ.yes.ev_per_contract if econ else None,
                "edge_no_raw": econ.no.gross_edge if econ else None, "edge_no_after_fee": econ.no.ev_per_contract if econ else None,
                "market_observed_at_utc": iso(market_ts) if market_ts else None, "minutes_to_start": it.get("minutes"), "horizon_label": it.get("horizon"),
                "pregame": (it.get("minutes") or 0) > 0, "role": "SHADOW", "authority": AUTHORITY, "support": "MODELLED_RESEARCH_ONLY" if pr.supported else "UNPRICED",
                **{f"meta_{k}": v for k, v in meta.items()},
            })
        rows_all.extend(rows)
        # correlation among this game's priced contracts with the most informative prices (for exposure research)
        corr_cols.sort(key=lambda kv: -float(kv[1].mean() * (1 - kv[1].mean())))
        corr_cols = corr_cols[:CORR_MAX_CONTRACTS]
        team_cols = [(f"{gi.home_abbrev}_goals", res.home_final.astype(np.float32)), (f"{gi.away_abbrev}_goals", res.away_final.astype(np.float32)),
                     (f"{gi.home_abbrev}_win", (res.home_final > res.away_final).astype(np.float32))]
        allc = corr_cols + team_cols
        cm = None
        if len(allc) >= 2:
            M = np.stack([v for _, v in allc])
            with np.errstate(invalid="ignore", divide="ignore"):
                cm = np.nan_to_num(np.corrcoef(M)).round(2).tolist()
        top = []
        for side in ("home", "away"):
            d = ps.home if side == "home" else ps.away
            ro = teams[side]["rb"].roster
            for i in np.argsort(-d.points.mean(axis=0))[:8]:
                pm = teams[side]["rb"].player_meta[int(ro.player_ids[i])]
                top.append({"team": ro.abbrev, "player_id": int(ro.player_ids[i]), "name": ro.names[i], "exp_goals": round(float(d.goals[:, i].mean()), 3),
                            "exp_points": round(float(d.points[:, i].mean()), 3), "p_point": round(float((d.points[:, i] >= 1).mean()), 3),
                            "p_goal": round(float((d.goals[:, i] >= 1).mean()), 3), "exp_toi_min": round(pm["expected_toi_total_min"], 1),
                            "exp_pp_toi_min": round(pm["expected_toi_min"]["pp"], 2), "quality": pm["projection_quality"], "role_confidence": pm["role_confidence"],
                            "pp_unit": pm.get("pp_unit"), "ev_slot": pm.get("ev_slot")})
        fs = ps.first_team
        blocks.append({
            "game_id": gid, "home": gi.home_abbrev, "away": gi.away_abbrev, "model_version": PLAYER_MODEL_VERSION, "role": "SHADOW", "authority": AUTHORITY,
            "lam_home": b["v2"]["lam_home"], "lam_away": b["v2"]["lam_away"], "n_sims": n_sims, "invariant_violations": viol,
            "lineups": {side: {"deployment_source": teams[side]["dep"].source, "notes": teams[side]["notes"], "n_dressed": teams[side]["rb"].roster.n,
                               "p_pp_share": teams[side]["rb"].roster.p_pp} for side in ("home", "away")},
            "p_home_scores_first": round(float((fs == gi.home_team_id).mean()), 4), "p_no_goal_before_shootout": round(float((fs == 0).mean()), 4),
            "goalies": goalie_blocks, "top_players": top, "n_contracts": len(rows), "n_priced": sum(1 for r in rows if r["priced"]),
            "correlation": {"labels": [k for k, _ in allc], "matrix": cm, "note": "Pearson correlation of YES indicators across the joint draw (exposure research only)"},
        })
        log.info(kv(event="player_shadow_game", game=gid, priced=sum(1 for r in rows if r["priced"]), contracts=len(rows), violations=len(viol)))

    for it in items:
        try:
            _one_game(it)
        except Exception as e:  # noqa: BLE001 - one bad game never takes the other games down
            gid = str(getattr(it.get("gi"), "game_id", "?"))
            log.warning(kv(event="player_shadow_game_failed", game=gid, err=str(e)[:200]))
            blocks.append({"game_id": gid, "error": f"{type(e).__name__}: {str(e)[:200]}"})
    return {"rows": rows_all, "blocks": blocks, "context": rt.sources}


def markdown(blocks: list[dict[str, Any]], rows: list[dict[str, Any]], note: str | None = None, per_game: int = 6) -> str:
    f = lambda x, n=3: "" if x is None else f"{x:.{n}f}"  # noqa: E731
    L = ["", "## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)", ""]
    for b in blocks:
        if b.get("error"):
            L.append(f"- {b.get('game_id')}: {b['error']}")
            continue
        L.append(f"**{b['away']} @ {b['home']}** · priced {b['n_priced']}/{b['n_contracts']} player contracts · lineups {b['lineups']['home']['deployment_source']}/{b['lineups']['away']['deployment_source']}"
                 + (f" · VIOLATIONS {b['invariant_violations']}" if b["invariant_violations"] else ""))
        for g in b["goalies"]:
            L.append(f"- {g['team']} net: {g.get('projected_starter') or '?'} ({g.get('starter_status')}) exp shots {g['expected_shots_faced']}, exp saves {g['expected_saves']} (sd {g['saves_sd']}), pull risk {g['pull_risk']}")
        gr = [r for r in rows if r["game_id"] == b["game_id"] and r.get("p_player") is not None and r.get("p_market") is not None]
        gr.sort(key=lambda r: -abs(r["player_minus_market"]))
        if gr:
            L += ["", "| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |", "|---|---:|---:|---|---:|---|"]
            for r in gr[:per_game]:
                ev = max(r.get("edge_yes_after_fee") or -9, r.get("edge_no_after_fee") or -9)
                L.append(f"| {r['title']} | {f(r['p_player'])} | {f(r['p_market'])} | {r.get('market_yes_ask') or ''}/{r.get('market_no_ask') or ''} | "
                         f"{'' if ev == -9 else f'{ev:+.3f}'} | {r.get('meta_projection_quality') or ''} |")
        L.append("")
    if note:
        L.append(f"_{note}_")
    return "\n".join(L) + "\n"
