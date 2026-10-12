"""Workload vs efficiency decomposition of the production player projections (RESEARCH_ONLY; offline).

The question this module answers: when PLAYER_SIM_V1 (the production shadow arm behind ``player_shadow`` in every
packet) misses a skater's shots on goal or a goalie's saves, is it because it got the WORKLOAD wrong (time on ice,
power-play time, the shots a goalie faced) or the EFFICIENCY wrong (shots per minute given the minutes, saves given
the shots faced)? Nothing here changes the production model; it re-uses the production code paths to reproduce what
production would have said pregame, then scores the pieces separately.

Champion = the production code, walk-forward:

* skaters: ``players.roster.build_roster`` -> ``player_meta[...]["expected_toi_min"]`` (by state) and
  ``["expected_sog"]``, with the production team-minute template of ``workflows.shadow_player``
  (``ev 50.6, pp 4.4 * p_pp / 0.215, sh 4.4, ea 0.6, en 0.6, ot 1.2``). Production takes ``p_pp`` from the DATA_ONLY_V2
  goal components; those components are not stored historically, so ``p_pp`` here is the PLAYER_SIM_V1 walk-forward's
  own stand-in (``team_pp_shares`` from the V2 walk-forward's point-in-time penalty-minute and PP/PK ratings).
  Production emits only a MEAN for shots; for distributional metrics it is wrapped in Poisson(mean) (labelled).
* goalies: nhl-sim-2.0 with the V2 walk-forward's point-in-time ``lam_st`` + ``simulate_players`` +
  ``players.saves.simulate_saves`` (the exact code that prices KXNHLSAVE), with the walk-forward's seeds, so the means
  reproduce ``docs/research/player_sim_v1/goalies_<season>.parquet``.

Point-in-time: player / team rows strictly before the game date; league parameters (priors, strength table, saves
model, TOI noise) fit on seasons strictly before the test season (``player_walk_forward.fit_season_params``).
Lineups are the ACTUAL dressed skaters (production reads warmup lines; Kalshi settles a non-dressing skater at the
pre-game fair price, so the target is the stat given the player plays). Starting goalies: no point-in-time starter
source exists historically (DailyFaceoff is archived only from 2026-09-30), so saves are scored CONDITIONAL ON THE
ACTUAL STARTER (labelled ``CONDITIONAL_ON_ACTUAL_STARTER``); the separate ``starter_heuristic`` table measures how
often a pregame-computable rule would have named the wrong goalie and what that did to the error.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.players.engine import ALL_STATES, simulate_players
from nhl_edge.players.features import PlayerBook, PlayerParams
from nhl_edge.players.roster import build_roster, team_pp_shares
from nhl_edge.players.saves import simulate_saves
from nhl_edge.research.player_walk_forward import Data, dressed, fit_season_params
from nhl_edge.sim.engine import TeamParams
from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

LABEL_STARTER = "CONDITIONAL_ON_ACTUAL_STARTER"
SAVES_MAX = 80  # support of the stored saves pmf (0..SAVES_MAX-1; the tail mass is folded into the last cell)
SOG_STATES = ("ev", "pp", "sh")  # the states the production expected_sog sums over


def production_team_minutes(p_pp: float) -> dict[str, float]:
    """The team-minute template ``workflows.shadow_player`` hands to ``build_roster`` (verbatim)."""
    return {"ev": 50.6, "pp": 4.4 * p_pp / 0.215, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}


def wf_pp_shares(r: Any, wf: pd.DataFrame) -> tuple[tuple[float, float], tuple[float, float]]:
    """(home p_pp, p_sh), (away p_pp, p_sh) exactly as ``player_walk_forward.simulate`` computes them."""
    ppm = wf[["ppmin_home", "ppmin_away"]].stack().mean()
    ppo = wf[["home_pp_off", "away_pp_off"]].stack().mean()
    pkd = wf[["home_pk_def", "away_pk_def"]].stack().mean()
    h = team_pp_shares(r.ppmin_home / ppm * 4.3, r.ppmin_away / ppm * 4.3, r.home_pp_off / ppo, r.away_pk_def / pkd)
    a = team_pp_shares(r.ppmin_away / ppm * 4.3, r.ppmin_home / ppm * 4.3, r.away_pp_off / ppo, r.home_pk_def / pkd)
    return h, a


def ot_shots(data: Data) -> pd.DataFrame:
    """Shots on goal (incl. goals) taken in regular-season overtime (period 4), per (game, player)."""
    s = data.shots
    s = s[(s["period"] == 4) & s["kind"].isin(["GOAL", "SOG"]) & s["shooter_id"].notna()]
    if "game_type" in s.columns:
        s = s[s["game_type"] == 2]
    return s.groupby(["game_id", "shooter_id"]).size().rename("sog_ot").reset_index().rename(columns={"shooter_id": "player_id"})


def champion_skaters(data: Data, wf: pd.DataFrame, season: int, max_games: int | None = None) -> pd.DataFrame:
    """One row per regular-season skater-game of ``season``: production expected TOI by state / SOG + the actuals."""
    fp = fit_season_params(data, season, PlayerParams())
    book = PlayerBook(data.pg, fp["priors"], fp["params"])
    g = wf[wf["season"] == season].sort_values(["game_date", "game_id"])
    if max_games:
        g = g.head(max_games)
    pl = data.players
    pl = pl[(pl["season"] == season) & (pl["game_type"] == 2)]
    by_game = {int(k): v for k, v in pl.groupby("game_id")}
    rows: list[dict[str, Any]] = []
    for r in g.itertuples(index=False):
        gid = int(r.game_id)
        box = by_game.get(gid)
        if box is None:
            continue
        di = int(str(r.game_date).replace("-", "")[:8])
        hid = int(box.loc[box["is_home"], "team_id"].iloc[0])
        aid = int(box.loc[~box["is_home"], "team_id"].iloc[0])
        (hpp, hsh), (app, ash) = wf_pp_shares(r, wf)
        for tid, oid, p_pp, p_sh, home in ((hid, aid, hpp, hsh, True), (aid, hid, app, ash, False)):
            ppl = dressed(data, gid, tid)
            tm = production_team_minutes(p_pp)
            rb = build_roster(book, tid, str(tid), di, ppl, None, p_pp, p_sh, tm, season=season)
            for p in ppl:
                pid = int(p["player_id"])
                m = rb.player_meta[pid]
                pr = rb.profiles[pid]
                rate = {}
                for s in SOG_STATES:
                    v = pr.sog60.get(s, np.nan)
                    rate[s] = float(v) if np.isfinite(v) else float(book.priors.ixg60.get((pr.pos, s), 0.0) * 10)
                row = {"game_id": gid, "season": season, "date_int": di, "team_id": tid, "opp_id": oid, "is_home": home, "player_id": pid, "pos": pr.pos,
                       "n_games": pr.n_games, "quality": m["projection_quality"], "p_pp": p_pp, "team_pp_min": tm["pp"],
                       "ch_toi": m["expected_toi_total_min"], "ch_sog": m["expected_sog"]}
                for s in ALL_STATES:
                    row[f"ch_toi_{s}"] = m["expected_toi_min"][s]
                    row[f"ch_share_{s}"] = m["share"][s]
                for s in SOG_STATES:
                    row[f"ch_rate_{s}"] = rate[s]  # shots per 60 in the state that the production mean uses
                rows.append(row)
    out = pd.DataFrame(rows)
    act = pl[["game_id", "player_id", "toi_s", "sog", "toi_ev_s", "toi_pp_s", "toi_sh_s", "toi_ea_s", "toi_en_s", "toi_ot_s",
              "sog_ev", "sog_pp", "sog_sh", "sog_ea", "sog_en", "att_ev", "att_pp", "att_sh", "att_ea", "att_en", "shifts_ok"]].copy()
    act = act.merge(ot_shots(data), on=["game_id", "player_id"], how="left")
    act["sog_ot"] = act["sog_ot"].fillna(0).astype(int)
    out = out.merge(act, on=["game_id", "player_id"], how="left")
    otg = data.team_states[(data.team_states["game_type"] == 2)].groupby("game_id")["n_seconds"].max()
    out["game_ot"] = out["game_id"].map(otg).fillna(3600).gt(3600)
    for s in ("ev", "pp", "sh", "ea", "en", "ot"):
        out[f"y_toi_{s}"] = pd.to_numeric(out[f"toi_{s}_s"], errors="coerce").fillna(0.0) / 60.0
    out["y_toi"] = out["toi_s"] / 60.0
    out["y_sog"] = out["sog"].astype(float)
    return out


def champion_goalies(data: Data, wf: pd.DataFrame, season: int, n_sims: int = 4000, max_games: int | None = None) -> pd.DataFrame:
    """One row per regular-season STARTER of ``season`` (conditional on the actual starter): the production saves
    distribution, its decomposition into expected shots faced by the starter and implied save fraction, and actuals."""
    fp = fit_season_params(data, season, PlayerParams())
    book = PlayerBook(data.pg, fp["priors"], replace(fp["params"]))
    sp = load_params()
    g = wf[wf["season"] == season].sort_values(["game_date", "game_id"])
    if max_games:
        g = g.head(max_games)
    pl = data.players
    pl = pl[(pl["season"] == season) & (pl["game_type"] == 2)]
    by_game = {int(k): v for k, v in pl.groupby("game_id")}
    gl = data.goalies[(data.goalies["season"] == season) & (data.goalies["game_type"] == 2)]
    gl_by = {int(k): v for k, v in gl.groupby("game_id")}
    rows: list[dict[str, Any]] = []
    for r in g.itertuples(index=False):
        gid = int(r.game_id)
        box = by_game.get(gid)
        if box is None or gid not in gl_by:
            continue
        di = int(str(r.game_date).replace("-", "")[:8])
        hid = int(box.loc[box["is_home"], "team_id"].iloc[0])
        aid = int(box.loc[~box["is_home"], "team_id"].iloc[0])
        (hpp, hsh), (app, ash) = wf_pp_shares(r, wf)
        # co-ice does not touch goals against (team goals and their strength come from the team draw), so the rosters
        # are built without co-ice matrices: same random stream, same goals-against draws, much faster
        rb_h = build_roster(book, hid, "H", di, dressed(data, gid, hid), None, hpp, hsh, production_team_minutes(hpp), season=season)
        rb_a = build_roster(book, aid, "A", di, dressed(data, gid, aid), None, app, ash, production_team_minutes(app), season=season)
        seed = gid % (2**31)
        res = simulate_game_v2(TeamParams(hid, "H", float(r.lam_st_home)), TeamParams(aid, "A", float(r.lam_st_away)), seed=seed, n_sims=n_sims, params=sp,
                               record_steps=True)
        ps = simulate_players(res, rb_h.roster, rb_a.roster, fp["strength"], seed + 1)
        p_ot = float(res.overtime.mean())
        gg = gl_by[gid]
        for gr in gg[gg["starter"].astype(bool)].itertuples(index=False):
            home_g = bool(gr.is_home)
            tid, oid = (hid, aid) if home_g else (aid, hid)
            ef = fp["rates"].expected_faced(tid, oid, di, home_g)
            sd = simulate_saves(res, ps, home_g, fp["saves"], ef, seed + 7)
            pmf = np.bincount(np.minimum(sd.saves, SAVES_MAX - 1), minlength=SAVES_MAX) / len(sd.saves)
            others = gg[(gg["team_id"] == tid) & (gg["player_id"] != gr.player_id)]
            row = {"game_id": gid, "season": season, "date_int": di, "player_id": int(gr.player_id), "team_id": tid, "opp_id": oid, "is_home": home_g,
                   "label": LABEL_STARTER, "expected_faced": ef, "ch_saves": float(sd.saves.mean()), "ch_saves_sd": float(sd.saves.std()),
                   "ch_faced_starter": float(sd.shots_faced.mean()), "ch_ga_starter": float(sd.goals_against.mean()),
                   "ch_net_faced": float(sd.net_shots_faced.mean()) if sd.net_shots_faced is not None else np.nan,
                   "ch_p_replaced": float(sd.replaced.mean()), "p_ot": p_ot,
                   "y_saves": int(gr.saves or 0), "y_sa": int(gr.shots_against or 0), "y_ga": int(gr.goals_against or 0), "y_toi_s": int(gr.toi_s or 0),
                   "y_replaced": bool((others["toi_s"].fillna(0) > 0).any()),
                   "y_net_sa": int(gg[gg["team_id"] == tid]["shots_against"].fillna(0).sum())}
            row["ch_pmf"] = pmf.astype(np.float32).tolist()
            rows.append(row)
    out = pd.DataFrame(rows)
    otg = data.team_states[(data.team_states["game_type"] == 2)].groupby("game_id")["n_seconds"].max()
    out["game_ot"] = out["game_id"].map(otg).fillna(3600).gt(3600)
    return out


# ---------------------------------------------------------------------------------------------------------------------
# decompositions
# ---------------------------------------------------------------------------------------------------------------------
def _err(e: np.ndarray) -> dict[str, float]:
    e = np.asarray(e, float)
    return {"mae": float(np.mean(np.abs(e))), "rmse": float(np.sqrt(np.mean(e**2))), "bias": float(np.mean(e)), "mse": float(np.mean(e**2))}


def skater_decomposition(sk: pd.DataFrame) -> dict[str, Any]:
    """Shots on goal: total error = workload (TOI) part + efficiency (rate | actual TOI) part + states the production
    mean leaves out (overtime shots, extra-attacker / empty-net shots).

    ``pred``            = sum_s T^_s r^_s                 (production mean, s in ev/pp/sh, OT shots excluded)
    ``pred_oracle_toi`` = sum_s T_s  r^_s                 (same rates, ACTUAL minutes in those states)
    workload error      = pred - pred_oracle_toi
    efficiency error    = pred_oracle_toi - y_states      (y_states = actual SOG in ev/pp/sh, OT shots excluded)
    omitted             = - (y - y_states)                (OT + EA + EN shots the mean never counts)
    total               = pred - y = workload + efficiency + omitted   (exact identity)

    MSE shares are reported as "what fraction of the MSE disappears with oracle minutes" (the honest
    variance-attribution statement; the pieces are correlated, so they do not add)."""
    n_all = len(sk)
    d = sk[sk["shifts_ok"].fillna(False).astype(bool)].copy()  # state minutes need shift charts (boxscore TOI / SOG do not)
    reg = {s: d[f"y_toi_{s}"] - (d["y_toi_ot"] if s == "ev" else 0.0) for s in SOG_STATES}
    # production's EV rate excludes OT shots from the numerator but its EV minutes include OT minutes: the oracle uses
    # the production definitions (actual EV minutes incl. OT, actual EV shots excl. OT)
    d["pred_oracle_toi"] = sum(d[f"y_toi_{s}"] * d[f"ch_rate_{s}"] / 60.0 for s in SOG_STATES)
    d["y_states"] = d["sog_ev"] + d["sog_pp"] + d["sog_sh"] - d["sog_ot"].clip(upper=d["sog_ev"] + d["sog_pp"] + d["sog_sh"])
    d["workload_err"] = d["ch_sog"] - d["pred_oracle_toi"]
    d["eff_err"] = d["pred_oracle_toi"] - d["y_states"]
    d["omitted_err"] = d["y_states"] - d["y_sog"]
    tot = d["ch_sog"] - d["y_sog"]
    out: dict[str, Any] = {"n_skater_games": int(len(d)), "n_games": int(d["game_id"].nunique()),
                           "n_excluded_no_shift_charts": int(n_all - len(d)), "mean_actual_sog": float(d["y_sog"].mean()),
                           "mean_pred_sog": float(d["ch_sog"].mean()), "total": _err(tot), "workload_component": _err(d["workload_err"]),
                           "efficiency_component": _err(d["eff_err"]), "omitted_states_component": _err(d["omitted_err"]),
                           "oracle_toi_total_error": _err(d["pred_oracle_toi"] - d["y_sog"]),
                           "poisson_floor_mse": float(d["ch_sog"].clip(lower=0).mean())}
    out["mse_removed_by_oracle_toi"] = 1.0 - out["oracle_toi_total_error"]["mse"] / out["total"]["mse"]
    # TOI workload itself
    toi = {"total": _err(d["ch_toi"] - d["y_toi"])}
    for s in ("ev", "pp", "sh"):
        toi[s] = _err(d[f"ch_toi_{s}"] - d[f"y_toi_{s}"])
    toi["ev_regulation_only"] = _err(d["ch_toi_ev"] - reg["ev"])
    out["toi_minutes"] = toi
    # PP usage: team PP minutes and the player's share
    out["pp"] = {"team_pp_min_pred_mean": float(d.groupby(["game_id", "team_id"])["team_pp_min"].first().mean()),
                 "player_pp_toi_pred_mean": float(d["ch_toi_pp"].mean()), "player_pp_toi_actual_mean": float(d["y_toi_pp"].mean())}
    # overtime
    ot = {}
    for flag, dd in d.groupby("game_ot"):
        k = "ot_games" if flag else "regulation_games"
        ot[k] = {"n_skater_games": int(len(dd)), "n_games": int(dd["game_id"].nunique()), "sog_error": _err(dd["ch_sog"] - dd["y_sog"]),
                 "toi_error": _err(dd["ch_toi"] - dd["y_toi"]), "mean_actual_sog": float(dd["y_sog"].mean()), "mean_ot_sog": float(dd["sog_ot"].mean()),
                 "mean_actual_toi": float(dd["y_toi"].mean()), "mean_ot_toi": float(dd["y_toi_ot"].mean()),
                 "mean_pred_ot_toi": float(dd["ch_toi_ot"].mean())}
    out["overtime"] = ot
    out["overtime"]["share_of_games_with_ot"] = float(d.groupby("game_id")["game_ot"].first().mean())
    out["overtime"]["production_note"] = ("production adds share_ot x 1.2 min to expected TOI but the EV-minute template (50.6) already contains "
                                          "overtime minutes, and expected_sog sums only ev/pp/sh with an EV rate whose numerator excludes OT shots")
    # by position
    out["by_pos"] = {p: {"n": int(len(dd)), "sog": _err(dd["ch_sog"] - dd["y_sog"]), "toi": _err(dd["ch_toi"] - dd["y_toi"])} for p, dd in d.groupby("pos")}
    return out


def goalie_decomposition(gl: pd.DataFrame) -> dict[str, Any]:
    """Saves (conditional on the actual starter): total error = workload (shots he faced) + efficiency (save fraction).

    implied save fraction sv^ = E[saves] / E[shots faced by the starter] (from the same draws)
    workload error   = (E[faced] - SA) * sv^
    efficiency error = SA * sv^ - saves
    total            = E[saves] - saves = workload + efficiency (exact)."""
    d = gl.copy()
    d["sv_hat"] = d["ch_saves"] / d["ch_faced_starter"].clip(lower=1e-6)
    d["workload_err"] = (d["ch_faced_starter"] - d["y_sa"]) * d["sv_hat"]
    d["eff_err"] = d["y_sa"] * d["sv_hat"] - d["y_saves"]
    tot = d["ch_saves"] - d["y_saves"]
    out: dict[str, Any] = {"label": LABEL_STARTER, "n_starts": int(len(d)), "n_games": int(d["game_id"].nunique()), "mean_actual_saves": float(d["y_saves"].mean()),
                           "mean_pred_saves": float(d["ch_saves"].mean()), "mean_actual_sa": float(d["y_sa"].mean()),
                           "mean_pred_faced_starter": float(d["ch_faced_starter"].mean()), "mean_expected_faced_net": float(d["expected_faced"].mean()),
                           "total": _err(tot), "workload_component": _err(d["workload_err"]), "efficiency_component": _err(d["eff_err"]),
                           "oracle_sa_total_error": _err(d["y_sa"] * d["sv_hat"] - d["y_saves"]),
                           "shots_faced_error": _err(d["ch_faced_starter"] - d["y_sa"]),
                           "net_shots_error": _err(d["expected_faced"] - d["y_net_sa"]),
                           "implied_sv_mean": float(d["sv_hat"].mean()), "actual_sv_pooled": float(d["y_saves"].sum() / max(d["y_sa"].sum(), 1))}
    out["mse_removed_by_oracle_sa"] = 1.0 - out["oracle_sa_total_error"]["mse"] / out["total"]["mse"]
    full = d[~d["y_replaced"]]
    out["full_game_starters"] = {"n": int(len(full)), "total": _err(full["ch_saves"] - full["y_saves"]),
                                 "oracle_sa_total_error": _err(full["y_sa"] * full["sv_hat"] - full["y_saves"])}
    out["replaced_starters"] = {"n": int(d["y_replaced"].sum()), "rate_actual": float(d["y_replaced"].mean()), "rate_pred": float(d["ch_p_replaced"].mean()),
                                "total": _err(d.loc[d["y_replaced"], "ch_saves"] - d.loc[d["y_replaced"], "y_saves"])}
    ot = {}
    for flag, dd in d.groupby("game_ot"):
        ot["ot_games" if flag else "regulation_games"] = {"n": int(len(dd)), "saves_error": _err(dd["ch_saves"] - dd["y_saves"]),
                                                          "shots_faced_error": _err(dd["ch_faced_starter"] - dd["y_sa"]),
                                                          "mean_actual_saves": float(dd["y_saves"].mean()), "mean_pred_saves": float(dd["ch_saves"].mean())}
    out["overtime"] = ot
    out["overtime"]["mean_p_ot_pred"] = float(d.groupby("game_id")["p_ot"].first().mean())
    out["overtime"]["share_of_games_with_ot"] = float(d.groupby("game_id")["game_ot"].first().mean())
    return out


# ---------------------------------------------------------------------------------------------------------------------
# starting-goalie uncertainty (pregame-computable heuristic; no point-in-time starter source exists historically)
# ---------------------------------------------------------------------------------------------------------------------
def starter_heuristic(goalies: pd.DataFrame, season: int, window: int = 10) -> pd.DataFrame:
    """For every regular-season team-game of ``season``: the goalie a pregame rule would name, from games strictly
    before the date only. Rule: the goalie with the most starts in the team's last ``window`` games; on the second
    night of a back-to-back, the most-used OTHER goalie of that window if he exists (the common NHL rotation).
    Also records the previous game's starter (``prev_id``) as a second naive rule.
    Returns (game_id, team_id, heuristic_id, heuristic_rule, actual_id, b2b, prev_id)."""
    g = goalies[goalies["starter"].astype(bool)].copy()
    g["date_int"] = g["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
    g = g.sort_values(["team_id", "date_int", "game_id"])
    rows = []
    for tid, d in g.groupby("team_id"):
        d = d.reset_index(drop=True)
        dates = pd.to_datetime(d["game_date"].astype(str).str[:10])
        for i in range(len(d)):
            r = d.iloc[i]
            if int(r["season"]) != season or int(r["game_type"]) != 2:
                continue
            prev = d.iloc[max(0, i - window):i]
            if not len(prev):
                continue
            counts = prev["player_id"].value_counts()
            lead = int(counts.index[0])
            b2b = bool(i > 0 and (dates.iloc[i] - dates.iloc[i - 1]).days == 1)
            pick, rule = lead, "workload_leader"
            if b2b and int(d.iloc[i - 1]["player_id"]) == lead and len(counts) > 1:
                pick, rule = int(counts.index[1]), "b2b_rotation"
            rows.append({"game_id": int(r["game_id"]), "team_id": int(tid), "heuristic_id": pick, "heuristic_rule": rule, "actual_id": int(r["player_id"]), "b2b": b2b,
                         "prev_id": int(d.iloc[i - 1]["player_id"])})
    return pd.DataFrame(rows)


def starter_uncertainty(gl: pd.DataFrame, heur: pd.DataFrame, goalies: pd.DataFrame) -> dict[str, Any]:
    h = heur.copy()
    h["correct"] = h["heuristic_id"] == h["actual_id"]
    out: dict[str, Any] = {"note": ("no point-in-time starting-goalie source exists for 2021-26 (DailyFaceoff is archived only from 2026-09-30); "
                                    "this is a pregame-COMPUTABLE rule, a lower bound on what a confirmed-starter feed would know"),
                           "n_team_games": int(len(h)), "heuristic_accuracy": float(h["correct"].mean()),
                           "accuracy_b2b": float(h.loc[h["b2b"], "correct"].mean()) if h["b2b"].any() else None,
                           "n_b2b": int(h["b2b"].sum()), "accuracy_not_b2b": float(h.loc[~h["b2b"], "correct"].mean()),
                           "previous_starter_rule_accuracy": float((h["prev_id"] == h["actual_id"]).mean())}
    m = gl.merge(h, on=["game_id", "team_id"], how="inner")
    m["err"] = m["ch_saves"] - m["y_saves"]
    out["saves_error_when_heuristic_right"] = _err(m.loc[m["correct"], "err"]) | {"n": int(m["correct"].sum())}
    out["saves_error_when_heuristic_wrong"] = _err(m.loc[~m["correct"], "err"]) | {"n": int((~m["correct"]).sum())}
    # efficiency: the actual starter's save fraction when the rule was wrong (usually a backup) vs right
    out["actual_sv_when_right"] = float(m.loc[m["correct"], "y_saves"].sum() / max(m.loc[m["correct"], "y_sa"].sum(), 1))
    out["actual_sv_when_wrong"] = float(m.loc[~m["correct"], "y_saves"].sum() / max(m.loc[~m["correct"], "y_sa"].sum(), 1))
    out["production_note"] = ("PLAYER_SIM_V1's saves mean does not depend on WHICH goalie starts (expected shots x league save fraction; the walk-forward "
                              "team lambdas carry no goalie term), so a wrong starter changes only which contract is live (Kalshi settles a goalie who never "
                              "enters at the pre-game fair price)")
    return out
