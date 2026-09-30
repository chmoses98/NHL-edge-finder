"""PLAYER_SIM_V1 walk-forward research harness (RESEARCH_ONLY; offline, from the repository's history tables).

Two evaluations, never mixed:

1. **Allocation test** (``allocation``): for every real goal of a test season, given its team, strength state and the
   team's dressed skaters, how much probability did the model put on the actual scorer, primary and secondary
   assister? Mean log-likelihood per goal vs baselines and ablations. It isolates the player layer from the team
   layer; it is how line/co-ice, finishing and individual-assist features earn (or lose) their place.
2. **Full simulation** (``simulate``): nhl-sim-2.0 with the V2 walk-forward's point-in-time team lambdas
   (docs/research/walk_forward_v2_*_games.csv) + PLAYER_SIM_V1 for every game, then Brier / log loss / calibration
   buckets for goals 1+/2+, assists 1+/2+, points 1+/2+/3+ and goalie saves ladders, against simple baselines.

Point-in-time: every player / team quantity for a game on date D uses rows with date < D only; parameters (league
priors, strength table, saves model) are fit on seasons strictly before the test season; the xG model on 2021-22.
Label ``REALISTIC_PIT``: deployment = the player's recent shift-derived shares and the team's recent co-ice (what a
pregame model could know). The dressed lineup is the actual one (in production it is known from warmups; and Kalshi
settles a non-entering player's contract at the pre-game fair price, so the target is P(event | player plays)).
``ORACLE_DEPLOYMENT`` (diagnostic only, never reported as model skill) replaces deployment with the game's own shares.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import replace
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.player_history import load_player_tables
from nhl_edge.players import xg as X
from nhl_edge.players.engine import ALL_STATES, S_IDX, simulate_players
from nhl_edge.players.features import PlayerBook, PlayerParams, build_player_games, coice_fractions, league_priors
from nhl_edge.players.params import fit_saves, shot_rates, strength_table, team_game_frame, toi_noise
from nhl_edge.players.roster import build_roster, team_pp_shares
from nhl_edge.players.saves import simulate_saves
from nhl_edge.sim.engine import TeamParams
from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

SEASONS = [2021, 2022, 2023, 2024, 2025]
TEAM_MIN = {"ev": 50.6, "pp": 4.4, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 0.0}


class Data:
    def __init__(self, history: Path, seasons: list[int] = SEASONS, xg_train: tuple[int, ...] = (2021, 2022)):
        t = {k: load_player_tables(history, k, seasons) for k in ("players", "goalies", "goals", "shots", "coice", "team_states")}
        self.players, self.goalies, self.goals, self.shots, self.coice, self.team_states = (t[k] for k in ("players", "goalies", "goals", "shots", "coice", "team_states"))
        for df in (self.players, self.goalies, self.goals, self.coice, self.team_states):
            df["date_int"] = df["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
        self.goals = self.goals[self.goals["game_type"] == 2] if "game_type" in self.goals.columns else self.goals
        self.xg_model = X.fit(self.shots[self.shots["season"].isin(xg_train)])
        self.shots["xg"] = X.score(self.shots, self.xg_model).values
        self.pg = build_player_games(self.players, self.goals, self.shots, self.team_states, self.shots["xg"])
        self.tg = team_game_frame(self.goalies, self.goals)
        self.toi_games = self.pg[["game_id", "player_id", "toi_ev", "toi_pp", "toi_sh"]]


def fit_season_params(data: Data, test_season: int, params: PlayerParams) -> dict[str, Any]:
    tr = [s for s in SEASONS if s < test_season]
    pg_tr = data.pg[data.pg["season"].isin(tr)]
    pri = league_priors(pg_tr, data.goals[data.goals["season"].isin(tr)])
    sig, exit_rate = toi_noise(pg_tr)
    prm = replace(params, toi_sigma=sig, p_early_exit=exit_rate)
    rates = shot_rates(data.tg)
    return {"priors": pri, "params": prm, "strength": strength_table(data.goals[data.goals["season"].isin(tr)]),
            "saves": fit_saves(data.goalies, data.goals, data.tg, rates, tr[-2:]), "rates": rates, "train": tr}


def dressed(data: Data, game_id: int, team_id: int) -> list[dict[str, Any]]:
    d = data.players[(data.players["game_id"] == game_id) & (data.players["team_id"] == team_id)]
    return [{"player_id": int(r.player_id), "name": r.name, "position": r.position} for r in d.itertuples(index=False)]


def roster_for(data: Data, book: PlayerBook, game_id: int, team_id: int, date_int: int, season: int, p_pp: float = 0.215, p_sh: float = 0.028,
               coice_mode: str = "observed") -> Any:
    pl = dressed(data, game_id, team_id)
    pids = [p["player_id"] for p in pl]
    F = coice_fractions(data.coice, team_id, date_int, pids, data.toi_games) if coice_mode == "observed" else None
    return build_roster(book, team_id, str(team_id), date_int, pl, F, p_pp, p_sh, TEAM_MIN, season=season)


# ---------------------------------------------------------------------------------------------------------------------
# 1. allocation test
# ---------------------------------------------------------------------------------------------------------------------
def allocation(data: Data, test_season: int, variants: dict[str, dict[str, Any]], max_games: int | None = None) -> dict[str, Any]:
    fp = fit_season_params(data, test_season, PlayerParams())
    g = data.goals[(data.goals["season"] == test_season)]
    games = sorted(g["game_id"].unique())[: max_games or None]
    out: dict[str, Any] = {}
    for name, v in variants.items():
        prm = replace(fp["params"], **v.get("params", {}))
        book = PlayerBook(data.pg, fp["priors"], prm)
        ll_s, ll_1, ll_2, n = 0.0, 0.0, 0.0, 0
        cache: dict[tuple[int, int], Any] = {}
        for gid in games:
            gg = g[g["game_id"] == gid]
            di = int(gg["date_int"].iloc[0])
            for r in gg.itertuples(index=False):
                key = (gid, int(r.team_id))
                if key not in cache:
                    cache[key] = roster_for(data, book, gid, int(r.team_id), di, test_season, coice_mode=v.get("coice", "observed")).roster
                ro = cache[key]
                st = "ot" if r.period >= 4 else str(r.strength).lower()
                si = S_IDX.get(st, 0)
                pid = list(ro.player_ids)
                if int(r.scorer_id) not in pid:
                    continue
                w = ro.w_goal[si].copy()
                if v.get("scorer") == "share_only":
                    w = cache_share(book, ro, di, st)
                if w.sum() <= 0:
                    w = ro.w_goal[0].copy()
                i_s = pid.index(int(r.scorer_id))
                ll_s += np.log(max(w[i_s] / w.sum(), 1e-9))
                fi = {"ev": 0, "pp": 1, "sh": 2}.get(st, 0)
                row = ro.F[fi, i_s].copy()
                a1r = ro.a1[si] if v.get("assist") != "position" else np.array([book.priors.a1.get((ro.pos[k], st), 0.2) for k in range(ro.n)])
                a2r = ro.a2[si] if v.get("assist") != "position" else np.array([book.priors.a2.get((ro.pos[k], st), 0.15) for k in range(ro.n)])
                W1 = row * a1r
                W1[i_s] = 0
                un = ro.unassisted[si]
                if pd.isna(r.a1_id) or int(r.a1_id) not in pid:
                    ll_1 += np.log(max(un, 1e-9)) if pd.isna(r.a1_id) else 0.0
                    n += 1
                    continue
                i1 = pid.index(int(r.a1_id))
                ll_1 += np.log(max((1 - un) * W1[i1] / max(W1.sum(), 1e-12), 1e-9))
                no2 = ro.no_a2[si]
                W2 = 0.5 * (row + ro.F[fi, i1]) * a2r
                W2[i_s] = 0
                W2[i1] = 0
                if pd.isna(r.a2_id):
                    ll_2 += np.log(max(no2, 1e-9))
                elif int(r.a2_id) in pid:
                    ll_2 += np.log(max((1 - no2) * W2[pid.index(int(r.a2_id))] / max(W2.sum(), 1e-12), 1e-9))
                n += 1
        out[name] = {"n_goals": n, "ll_scorer": ll_s / max(n, 1), "ll_a1": ll_1 / max(n, 1), "ll_a2": ll_2 / max(n, 1),
                     "ll_total": (ll_s + ll_1 + ll_2) / max(n, 1)}
        print(name, json.dumps(out[name]), flush=True)
    return out


def cache_share(book: PlayerBook, ro: Any, di: int, st: str) -> np.ndarray:
    """Deployment-only scorer weights (share of the state's time, no talent)."""
    s = st if st in ALL_STATES else "ev"
    return np.array([book.profile(int(p), di).share[s] for p in ro.player_ids])


# ---------------------------------------------------------------------------------------------------------------------
# 2. full simulation
# ---------------------------------------------------------------------------------------------------------------------
def simulate(data: Data, wf_games: pd.DataFrame, test_season: int, n_sims: int = 4000, max_games: int | None = None, variant: dict[str, Any] | None = None,
             progress_every: int = 100) -> tuple[pd.DataFrame, pd.DataFrame]:
    v = variant or {}
    fp = fit_season_params(data, test_season, PlayerParams())
    prm = replace(fp["params"], **v.get("params", {}))
    book = PlayerBook(data.pg, fp["priors"], prm)
    sp = load_params()
    wf = wf_games[wf_games["season"] == test_season].sort_values(["game_date", "game_id"])
    if max_games:
        wf = wf.head(max_games)
    ppm = wf_games[["ppmin_home", "ppmin_away"]].stack().mean()
    ppo = wf_games[["home_pp_off", "away_pp_off"]].stack().mean()
    pkd = wf_games[["home_pk_def", "away_pk_def"]].stack().mean()
    known_games = set(data.players["game_id"].unique())
    sk_rows, g_rows, game_rows = [], [], []
    t0 = time.time()
    for k, r in enumerate(wf.itertuples(index=False)):
        gid = int(r.game_id)
        if gid not in known_games:
            continue
        di = int(str(r.game_date).replace("-", "")[:8])
        box = data.players[data.players["game_id"] == gid]
        hid = int(box.loc[box["is_home"], "team_id"].iloc[0])
        aid = int(box.loc[~box["is_home"], "team_id"].iloc[0])
        hpp, hsh = team_pp_shares(r.ppmin_home / ppm * 4.3, r.ppmin_away / ppm * 4.3, r.home_pp_off / ppo, r.away_pk_def / pkd)
        app, ash = team_pp_shares(r.ppmin_away / ppm * 4.3, r.ppmin_home / ppm * 4.3, r.away_pp_off / ppo, r.home_pk_def / pkd)
        rb_h = roster_for(data, book, gid, hid, di, test_season, hpp, hsh, v.get("coice", "observed"))
        rb_a = roster_for(data, book, gid, aid, di, test_season, app, ash, v.get("coice", "observed"))
        seed = gid % (2**31)
        res = simulate_game_v2(TeamParams(hid, "H", float(r.lam_st_home)), TeamParams(aid, "A", float(r.lam_st_away)), seed=seed, n_sims=n_sims, params=sp,
                               record_steps=True)
        ps = simulate_players(res, rb_h.roster, rb_a.roster, fp["strength"], seed + 1)
        gg = data.goals[data.goals["game_id"] == gid].sort_values(["period", "t_s"])
        first_scorer_actual = int(gg.iloc[0]["scorer_id"]) if len(gg) else 0
        game_rows.append({"game_id": gid, "season": test_season, "p_home_first": float((ps.first_team == hid).mean()), "p_no_goal": float((ps.first_team == 0).mean()),
                          "y_home_first": int(len(gg) > 0 and int(gg.iloc[0]["team_id"]) == hid), "y_no_goal": int(len(gg) == 0)})
        for d, ro, rb in ((ps.home, rb_h.roster, rb_h), (ps.away, rb_a.roster, rb_a)):
            act = box.set_index("player_id")
            pts = d.points
            for i, pid in enumerate(ro.player_ids):
                a = act.loc[int(pid)]
                gi, ai, pi = d.goals[:, i], d.assists[:, i], pts[:, i]
                m = rb.player_meta[int(pid)]
                sk_rows.append({"game_id": gid, "season": test_season, "date_int": di, "player_id": int(pid), "team_id": ro.team_id, "pos": ro.pos[i],
                                "p_first": float((ps.first_scorer == int(pid)).mean()), "y_first": int(first_scorer_actual == int(pid)),
                                "exp_toi_ev": m["expected_toi_min"]["ev"], "exp_toi_pp": m["expected_toi_min"]["pp"], "toi_ev_s": a.get("toi_ev_s"), "toi_pp_s": a.get("toi_pp_s"),
                                "toi_recent_min": m.get("toi_recent_mean_min"),
                                "n_games": m["n_games"], "quality": m["projection_quality"], "role_conf": m["role_confidence"],
                                "flags": ",".join(m["uncertainty_flags"]), "exp_toi": m["expected_toi_total_min"],
                                "p_g1": float((gi >= 1).mean()), "p_g2": float((gi >= 2).mean()), "p_g3": float((gi >= 3).mean()),
                                "p_a1": float((ai >= 1).mean()), "p_a2": float((ai >= 2).mean()),
                                "p_p1": float((pi >= 1).mean()), "p_p2": float((pi >= 2).mean()), "p_p3": float((pi >= 3).mean()),
                                "e_g": float(gi.mean()), "e_a": float(ai.mean()), "e_p": float(pi.mean()),
                                "y_g": int(a["goals"]), "y_a": int(a["assists"]), "y_p": int(a["points"]), "toi_s": a["toi_s"]})
        gl = data.goalies[(data.goalies["game_id"] == gid) & (data.goalies["starter"].astype(bool))]
        for gr in gl.itertuples(index=False):
            home_g = bool(gr.is_home)
            tid, oid = (hid, aid) if home_g else (aid, hid)
            ef = fp["rates"].expected_faced(tid, oid, di, home_g)
            sd = simulate_saves(res, ps, home_g, fp["saves"], ef, seed + 7)
            row = {"game_id": gid, "season": test_season, "date_int": di, "player_id": int(gr.player_id), "team_id": tid, "expected_faced": ef,
                   "e_saves": float(sd.saves.mean()), "sd_saves": float(sd.saves.std()), "y_saves": int(gr.saves or 0), "y_sa": int(gr.shots_against or 0),
                   "toi_s": gr.toi_s, "p_replaced": float(sd.replaced.mean())}
            for t in range(14, 41):
                row[f"p_s{t}"] = float((sd.saves >= t).mean())
            g_rows.append(row)
        if progress_every and (k + 1) % progress_every == 0:
            print(f"season {test_season}: {k + 1}/{len(wf)} games, {time.time() - t0:.0f}s", flush=True)
    simulate.last_games = pd.DataFrame(game_rows)  # type: ignore[attr-defined]  # team-to-score-first rows of the last call
    return pd.DataFrame(sk_rows), pd.DataFrame(g_rows)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.player_walk_forward")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--wf-games", default="docs/research/walk_forward_v2_wf2_20260929_games.csv")
    ap.add_argument("--out", default="docs/research/player_sim_v1")
    ap.add_argument("--mode", choices=["allocation", "simulate"], default="simulate")
    ap.add_argument("--seasons", default="2024,2025")
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--max-games", type=int, default=None)
    a = ap.parse_args(argv)
    data = Data(Path(a.history))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    seasons = [int(s) for s in a.seasons.split(",")]
    if a.mode == "allocation":
        res = {s: allocation(data, s, DEFAULT_VARIANTS, a.max_games) for s in seasons}
        (out / "allocation.json").write_text(json.dumps(res, indent=1))
        return 0
    wf = pd.read_csv(a.wf_games)
    for s in seasons:
        sk, gl = simulate(data, wf, s, a.n_sims, a.max_games)
        sk.to_parquet(out / f"skaters_{s}.parquet", index=False)
        gl.to_parquet(out / f"goalies_{s}.parquet", index=False)
    return 0


DEFAULT_VARIANTS: dict[str, dict[str, Any]] = {
    "PLAYER_SIM_V1": {},
    "no_finishing": {"params": {"use_finishing": False}},
    "uniform_coice (no line effects)": {"coice": "uniform"},
    "position_assist_rates": {"assist": "position"},
    "deployment_share_only (no talent)": {"scorer": "share_only"},
}

if __name__ == "__main__":
    sys.exit(main())
