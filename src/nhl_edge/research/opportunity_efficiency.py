"""Opportunity / efficiency decomposition of PLAYER_SIM_V1 (RESEARCH_ONLY; offline, committed history only).

Question: when the player engine misses a player's TOI, SOG, goals, assists, points or a goalie's saves, is the error in
OPPORTUNITY (ice time, power-play time, shot attempts, shots faced) or in EFFICIENCY (attempts that reach the net,
shots that become goals, shots that become saves)? Each stage is scored separately on matched player-game rows of the
FULL eligible population (every dressed skater with shift data; every starting goalie; regular season), against a plain
recent-mean baseline, with game-clustered paired bootstrap CIs. No market input is read anywhere in this module.

Incumbent quantities are reproduced from the incumbent code (``PlayerBook.profile`` shares x the walk-forward team
minutes, ``ShotRates.expected_faced``, ``SavesModel``) with parameters fitted on seasons strictly before the test season,
exactly as ``research.player_walk_forward`` does. The goals / assists / points / saves expectations of the incumbent
come from ``research.player_walk_forward.simulate`` (seed = game id; reproduces the committed walk-forward files).

Baseline ``RECENT_MEAN_10``: the unweighted mean of the player's (team's) last 10 games strictly before the date; a
player without history gets the training-season position mean (flagged ``NO_HISTORY``).

Run: ``python -m nhl_edge.research.opportunity_efficiency --season 2024 --out docs/research/opportunity_efficiency``
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.players.features import PlayerBook, PlayerParams

STATES_TOI = ("ev", "pp", "sh", "ea", "en", "ot")
RECENT_N = 10
BOOT_B = 2000
BOOT_SEED = 20261011


# ---------------------------------------------------------------------------------------------------------------------
# scoring utilities
# ---------------------------------------------------------------------------------------------------------------------
def poisson_dev(y: np.ndarray, mu: np.ndarray) -> np.ndarray:
    """Per-row Poisson deviance (lower is better)."""
    mu = np.maximum(np.asarray(mu, float), 1e-9)
    y = np.asarray(y, float)
    with np.errstate(divide="ignore", invalid="ignore"):
        t = np.where(y > 0, y * np.log(y / mu), 0.0)
    return 2.0 * (t - (y - mu))


def binom_nll(k: np.ndarray, n: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Per-row negative binomial-likelihood kernel of k successes in n trials (constant term dropped; lower is better)."""
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    k = np.asarray(k, float)
    n = np.asarray(n, float)
    return -(k * np.log(p) + (n - k) * np.log1p(-p))


def cluster_boot(game: np.ndarray, loss_a: np.ndarray, loss_b: np.ndarray, B: int = BOOT_B, seed: int = BOOT_SEED) -> dict[str, float]:
    """Paired, game-clustered percentile bootstrap of mean(loss_b) - mean(loss_a) (b = challenger / alternative)."""
    df = pd.DataFrame({"g": game, "d": np.asarray(loss_b, float) - np.asarray(loss_a, float)})
    s = df.groupby("g")["d"].agg(["sum", "count"])
    sums, cnt = s["sum"].to_numpy(), s["count"].to_numpy()
    rng = np.random.default_rng(seed)
    G = len(sums)
    if G < 3:
        return {"delta": float(df["d"].mean()) if len(df) else float("nan"), "lo": float("nan"), "hi": float("nan"), "n_games": int(G), "n_rows": int(len(df))}
    idx = rng.integers(0, G, size=(B, G))
    est = sums[idx].sum(axis=1) / cnt[idx].sum(axis=1)
    return {"delta": float(sums.sum() / cnt.sum()), "lo": float(np.quantile(est, 0.025)), "hi": float(np.quantile(est, 0.975)),
            "n_games": int(G), "n_rows": int(len(df))}


def point_metrics(y: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    e = np.asarray(pred, float) - np.asarray(y, float)
    return {"n": int(len(e)), "mae": float(np.mean(np.abs(e))), "rmse": float(np.sqrt(np.mean(e**2))), "bias": float(np.mean(e)),
            "mean_pred": float(np.mean(pred)), "mean_actual": float(np.mean(y))}


def compare_point(game: np.ndarray, y: np.ndarray, a: np.ndarray, b: np.ndarray, count: bool = False) -> dict[str, Any]:
    """Point-forecast comparison of a (reference) vs b on identical rows; deltas are b - a (negative = b better)."""
    out = {"a": point_metrics(y, a), "b": point_metrics(y, b),
           "d_mae": cluster_boot(game, np.abs(a - y), np.abs(b - y)), "d_mse": cluster_boot(game, (a - y) ** 2, (b - y) ** 2)}
    if count:
        out["a"]["poisson_dev"] = float(poisson_dev(y, a).mean())
        out["b"]["poisson_dev"] = float(poisson_dev(y, b).mean())
        out["d_poisson_dev"] = cluster_boot(game, poisson_dev(y, a), poisson_dev(y, b))
    return out


# ---------------------------------------------------------------------------------------------------------------------
# frames
# ---------------------------------------------------------------------------------------------------------------------
def recent_mean(df: pd.DataFrame, key: str, cols: list[str], n: int = RECENT_N, order: tuple[str, ...] = ("date_int", "game_id")) -> pd.DataFrame:
    """Unweighted mean (and sum) of the last ``n`` rows of each ``key`` strictly before each row (shift 1)."""
    d = df.sort_values([key, *order])
    out = pd.DataFrame(index=d.index)
    g = d.groupby(key, sort=False)
    for c in cols:
        sh = g[c].shift(1)
        out[f"rm_{c}"] = sh.groupby(d[key]).rolling(n, min_periods=1).mean().reset_index(level=0, drop=True)
        out[f"rs_{c}"] = sh.groupby(d[key]).rolling(n, min_periods=1).sum().reset_index(level=0, drop=True)
    out["rn"] = g.cumcount().clip(upper=n)
    return out.reindex(df.index)


def skater_frame(data: Any, season: int, fp: dict[str, Any], team_min: dict[str, float]) -> pd.DataFrame:
    """One row per regular-season skater-game of ``season`` with shift data: actuals, incumbent and RECENT_MEAN_10."""
    pg = data.pg[data.pg["game_type"] == 2].copy()
    pl = data.players[data.players["game_type"] == 2]
    att = pl[["game_id", "player_id"]].copy()
    att["att"] = pl[[f"att_{s}" for s in ("ev", "pp", "sh", "ea", "en")]].sum(axis=1).to_numpy()
    att["sog_pbp"] = pl[[f"sog_{s}" for s in ("ev", "pp", "sh", "ea", "en")]].sum(axis=1).to_numpy()
    pg = pg.merge(att, on=["game_id", "player_id"], how="left")
    pg["toi_min"] = pg["toi_s"] / 60.0
    pg["toi_pp_min"] = pg["toi_pp"] / 60.0
    pg["toi_ev_min"] = pg["toi_ev"] / 60.0
    pg["toi_sh_min"] = pg["toi_sh"] / 60.0
    cols = ["toi_min", "toi_pp_min", "sog", "att", "goals", "assists", "points"]
    rm = recent_mean(pg, "player_id", cols)
    pg = pg.join(rm)
    d = pg[pg["season"] == season].copy()
    # position means of the training seasons (players without history)
    tr = pg[pg["season"] < season]
    pos_mean = tr.groupby("pos")[cols].mean()
    for c in cols:
        d[f"base_{c}"] = d[f"rm_{c}"].fillna(d["pos"].map(pos_mean[c]))
    d["no_history"] = d["rn"] == 0
    # incumbent: point-in-time profile shares x the walk-forward team minutes; sog60 as in roster meta
    book = PlayerBook(data.pg, fp["priors"], fp["params"])
    pri = fp["priors"]
    inc_toi, inc_pp, inc_ev, inc_sh, inc_sog, prior_pp_share, last_team, n_games = [], [], [], [], [], [], [], []
    for r in d[["player_id", "date_int", "position"]].itertuples(index=False):
        pr = book.profile(int(r.player_id), int(r.date_int), r.position, season)
        exp = {s: pr.share[s] * team_min.get(s, 0.0) for s in STATES_TOI}
        inc_toi.append(sum(exp.values()))
        inc_pp.append(exp["pp"])
        inc_ev.append(exp["ev"])
        inc_sh.append(exp["sh"])
        inc_sog.append(sum(exp[s] * (pr.sog60[s] if np.isfinite(pr.sog60.get(s, np.nan)) else pri.ixg60.get((pr.pos, s), 0) * 10) / 60.0
                           for s in ("ev", "pp", "sh")))
        prior_pp_share.append(pr.share["pp"])
        last_team.append(pr.last_team_id)
        n_games.append(pr.n_games)
    d["inc_toi_min"] = inc_toi
    d["inc_toi_pp_min"] = inc_pp
    d["inc_toi_ev_min"] = inc_ev
    d["inc_toi_sh_min"] = inc_sh
    d["inc_sog"] = inc_sog
    d["prior_pp_share"] = prior_pp_share
    d["n_prior_games"] = n_games
    d["new_team"] = [lt is not None and int(lt) != int(t) for lt, t in zip(last_team, d["team_id"])]
    d["ot_game"] = d["tsec_ot"] > 0
    return d.reset_index(drop=True)


def goalie_frame(data: Any, season: int, fp: dict[str, Any]) -> pd.DataFrame:
    """One row per regular-season starting goalie of ``season``: team shots faced, saves, incumbent expected faced and
    RECENT_MEAN_10 team / opponent shot rates."""
    tg = data.tg.copy()
    tg = tg[tg["game_id"].astype(str).str[4:6] == "02"]
    rm = recent_mean(tg, "team_id", ["sa", "sf"])
    tg = tg.join(rm)
    opp = tg[["game_id", "team_id", "rm_sf", "rm_sa"]].rename(columns={"team_id": "opp_id", "rm_sf": "opp_rm_sf", "rm_sa": "opp_rm_sa"})
    tg = tg.merge(opp, on=["game_id", "opp_id"], how="left")
    g = data.goalies[(data.goalies["game_type"] == 2) & data.goalies["starter"].astype(bool) & (data.goalies["season"] == season)]
    d = g.merge(tg[["game_id", "team_id", "opp_id", "sa", "sf", "rm_sa", "rm_sf", "opp_rm_sf", "opp_rm_sa", "reg_gf", "reg_ga", "max_period"]],
                on=["game_id", "team_id"], how="inner")
    rates = fp["rates"]
    d["inc_faced"] = [rates.expected_faced(int(t), int(o), int(di), bool(h)) for t, o, di, h in zip(d["team_id"], d["opp_id"], d["date_int"], d["is_home"])]
    d["lg_at"] = [rates.league_at(int(di)) for di in d["date_int"]]
    d["base_faced_own"] = d["rm_sa"].fillna(d["lg_at"])
    d["base_faced_mult"] = d["lg_at"] * (d["opp_rm_sf"].fillna(d["lg_at"]) / d["lg_at"]) * (d["rm_sa"].fillna(d["lg_at"]) / d["lg_at"])
    used = data.goalies[data.goalies["toi_s"].fillna(0) > 0].groupby(["game_id", "team_id"]).size().rename("n_goalies_used")
    d = d.join(used, on=["game_id", "team_id"])
    # goalie save% history (strictly before the date; any team), for the efficiency stage
    gl = data.goalies[(data.goalies["game_type"] == 2) & (data.goalies["toi_s"].fillna(0) > 0)].sort_values(["player_id", "date_int", "game_id"])
    cs = gl.groupby("player_id")[["saves", "shots_against"]].cumsum() - gl[["saves", "shots_against"]]
    gl = gl.assign(prior_sv=cs["saves"].to_numpy(), prior_sa=cs["shots_against"].to_numpy())
    d = d.merge(gl[["game_id", "player_id", "prior_sv", "prior_sa"]], on=["game_id", "player_id"], how="left")
    return d.reset_index(drop=True)


# ---------------------------------------------------------------------------------------------------------------------
# decomposition
# ---------------------------------------------------------------------------------------------------------------------
def subgroup_masks(d: pd.DataFrame) -> dict[str, np.ndarray]:
    return {"F": (d["pos"] == "F").to_numpy(), "D": (d["pos"] == "D").to_numpy(),
            "pp_role (prior PP share >= 0.40)": (d["prior_pp_share"] >= 0.40).to_numpy(),
            "non_pp_role": (d["prior_pp_share"] < 0.40).to_numpy(),
            "new_team": d["new_team"].to_numpy(bool), "lt10_prior_games": (d["n_prior_games"] < 10).to_numpy(),
            "ot_game": d["ot_game"].to_numpy(bool), "regulation_game": ~d["ot_game"].to_numpy(bool)}


def skater_decomposition(d: pd.DataFrame, sim: pd.DataFrame | None) -> dict[str, Any]:
    gm = d["game_id"].to_numpy()
    out: dict[str, Any] = {"n_rows": int(len(d)), "n_games": int(d["game_id"].nunique()), "n_no_history": int(d["no_history"].sum()),
                           "n_new_team": int(d["new_team"].sum())}
    y_toi = d["toi_min"].to_numpy()
    # --- opportunity: TOI and PP TOI -------------------------------------------------------------------------------
    opp: dict[str, Any] = {}
    opp["toi_total_min"] = compare_point(gm, y_toi, d["base_toi_min"].to_numpy(), d["inc_toi_min"].to_numpy())
    opp["toi_pp_min"] = compare_point(gm, d["toi_pp_min"].to_numpy(), d["base_toi_pp_min"].to_numpy(), d["inc_toi_pp_min"].to_numpy())
    # where the total-TOI gap comes from: regulation-only actual TOI (OT excluded) vs the incumbent (whose team minutes
    # carry no OT), by state
    y_reg = (d["toi_s"] - d["toi_ot"]).to_numpy() / 60.0
    opp["toi_regulation_only_min"] = compare_point(gm, y_reg, d["base_toi_min"].to_numpy(), d["inc_toi_min"].to_numpy())
    opp["toi_ev_min_incumbent"] = point_metrics(d["toi_ev_min"].to_numpy(), d["inc_toi_ev_min"].to_numpy())
    opp["toi_sh_min_incumbent"] = point_metrics(d["toi_sh_min"].to_numpy(), d["inc_toi_sh_min"].to_numpy())
    opp["by_subgroup_toi"] = {k: compare_point(gm[m], y_toi[m], d["base_toi_min"].to_numpy()[m], d["inc_toi_min"].to_numpy()[m])
                              for k, m in subgroup_masks(d).items() if m.sum() > 50}
    opp["by_subgroup_pp_toi"] = {k: compare_point(gm[m], d["toi_pp_min"].to_numpy()[m], d["base_toi_pp_min"].to_numpy()[m], d["inc_toi_pp_min"].to_numpy()[m])
                                 for k, m in subgroup_masks(d).items() if m.sum() > 50}
    # attempts per game (opportunity of the shot chain) vs RECENT_MEAN_10; attempts given actual TOI (rate)
    att_rate_base = np.where(d["rs_toi_min"].fillna(0) > 1, d["rs_att"].fillna(0) / d["rs_toi_min"].clip(lower=1e-6), np.nan)
    pos_att_rate = (d["base_att"] / d["base_toi_min"]).to_numpy()
    att_rate_base = np.where(np.isfinite(att_rate_base), att_rate_base, pos_att_rate)
    opp["attempts_per_game_recent_mean"] = point_metrics(d["att"].to_numpy(), d["base_att"].to_numpy())
    opp["attempts_given_actual_toi"] = {"recent_rate_x_actual_toi": point_metrics(d["att"].to_numpy(), att_rate_base * y_toi),
                                        "recent_mean_attempts": point_metrics(d["att"].to_numpy(), d["base_att"].to_numpy())}
    out["opportunity"] = opp
    # --- efficiency -----------------------------------------------------------------------------------------------
    eff: dict[str, Any] = {}
    att = d["att"].to_numpy(float)
    sog_pbp = d["sog_pbp"].to_numpy(float)
    m = att > 0
    lg_q = float(d["rs_sog"].sum() / max(d["rs_att"].sum(), 1))  # pooled prior-games on-net rate (point-in-time pooled)
    q_plain = np.where(d["rs_att"].fillna(0) > 0, d["rs_sog"].fillna(0) / d["rs_att"].clip(lower=1e-6), lg_q)
    q_shrunk = (d["rs_sog"].fillna(0) + 20 * lg_q) / (d["rs_att"].fillna(0) + 20)
    eff["sog_given_attempts"] = {"n_rows_with_attempts": int(m.sum()), "pooled_on_net_rate": lg_q,
                                 "nll_pooled": float(binom_nll(sog_pbp[m], att[m], np.full(m.sum(), lg_q)).mean()),
                                 "nll_player_last10_plain": float(binom_nll(sog_pbp[m], att[m], q_plain[m]).mean()),
                                 "nll_player_last10_shrunk20": float(binom_nll(sog_pbp[m], att[m], q_shrunk[m]).mean()),
                                 "d_shrunk_vs_pooled": cluster_boot(gm[m], binom_nll(sog_pbp[m], att[m], np.full(m.sum(), lg_q)),
                                                                    binom_nll(sog_pbp[m], att[m], q_shrunk[m]))}
    # SOG rate given ACTUAL TOI: isolates per-60 shot generation from ice-time forecasting
    sog = d["sog"].to_numpy(float)
    inc_rate = d["inc_sog"].to_numpy() / np.maximum(d["inc_toi_ev_min"] + d["inc_toi_pp_min"] + d["inc_toi_sh_min"], 1e-6)
    base_rate = np.where(d["rs_toi_min"].fillna(0) > 1, d["rs_sog"].fillna(0) / d["rs_toi_min"].clip(lower=1e-6), (d["base_sog"] / d["base_toi_min"]).to_numpy())
    eff["sog_rate_given_actual_toi"] = compare_point(gm, sog, base_rate * y_toi, inc_rate * y_toi, count=True)
    # SOG end to end, and the share of the error that is ice time: incumbent rate x incumbent TOI vs x actual TOI vs
    # x RECENT_MEAN_10 TOI
    eff["sog_end_to_end_incumbent_vs_recent_mean"] = compare_point(gm, sog, d["base_sog"].to_numpy(), d["inc_sog"].to_numpy(), count=True)
    eff["sog_incumbent_rate_swap_toi"] = {"incumbent_toi": point_metrics(sog, inc_rate * d["inc_toi_min"].to_numpy()),
                                          "recent_mean_toi": point_metrics(sog, inc_rate * d["base_toi_min"].to_numpy()),
                                          "actual_toi (oracle)": point_metrics(sog, inc_rate * y_toi),
                                          "d_recent_mean_toi_vs_incumbent_toi": cluster_boot(gm, poisson_dev(sog, inc_rate * d["inc_toi_min"].to_numpy()),
                                                                                             poisson_dev(sog, inc_rate * d["base_toi_min"].to_numpy()))}
    # goals given SOG (conversion)
    gl = d["goals"].to_numpy(float)
    ms = sog > 0
    lg_sh = float(d["rs_goals"].sum() / max(d["rs_sog"].sum(), 1))
    sh_shrunk = (d["rs_goals"].fillna(0) + 30 * lg_sh) / (d["rs_sog"].fillna(0) + 30)
    eff["goals_given_sog"] = {"n_rows_with_sog": int(ms.sum()), "pooled_shooting_pct": lg_sh,
                              "nll_pooled": float(binom_nll(np.minimum(gl[ms], sog[ms]), sog[ms], np.full(ms.sum(), lg_sh)).mean()),
                              "nll_player_last10_shrunk30": float(binom_nll(np.minimum(gl[ms], sog[ms]), sog[ms], sh_shrunk[ms]).mean()),
                              "n_goals_exceeding_official_sog": int((gl > sog).sum())}
    out["efficiency"] = eff
    # --- incumbent stat forecasts (joint simulation) vs RECENT_MEAN_10, and the TOI share of their error ------------------
    if sim is not None and len(sim):
        j = d.merge(sim[["game_id", "player_id", "e_g", "e_a", "e_p", "exp_toi"]], on=["game_id", "player_id"], how="inner")
        gj = j["game_id"].to_numpy()
        stats = {}
        for stat, e, b in (("goals", "e_g", "base_goals"), ("assists", "e_a", "base_assists"), ("points", "e_p", "base_points")):
            y = j[stat].to_numpy(float)
            stats[stat] = compare_point(gj, y, j[b].to_numpy(), j[e].to_numpy(), count=True)
            # per-60 rate implied by the incumbent x actual TOI: how much of the stat error is ice time
            rate = j[e].to_numpy() / np.maximum(j["exp_toi"].to_numpy(), 1e-6)
            stats[stat]["incumbent_rate_x_actual_toi (oracle)"] = point_metrics(y, rate * j["toi_min"].to_numpy())
            stats[stat]["incumbent_rate_x_recent_mean_toi"] = point_metrics(y, rate * j["base_toi_min"].to_numpy())
            stats[stat]["d_recent_mean_toi_vs_incumbent_toi"] = cluster_boot(gj, poisson_dev(y, j[e].to_numpy()), poisson_dev(y, rate * j["base_toi_min"].to_numpy()))
        stats["n_matched"] = int(len(j))
        out["incumbent_sim_stats"] = stats
    return out


def goalie_decomposition(g: pd.DataFrame, sim_g: pd.DataFrame | None, lg_sv: float) -> dict[str, Any]:
    gm = g["game_id"].to_numpy()
    y_sa_team = g["sa"].to_numpy(float)
    out: dict[str, Any] = {"n_starts": int(len(g)), "n_games": int(g["game_id"].nunique()),
                           "n_starter_replaced": int((g["n_goalies_used"].fillna(1) > 1).sum())}
    out["team_shots_faced"] = {"incumbent_vs_recent_mean_own_sa": compare_point(gm, y_sa_team, g["base_faced_own"].to_numpy(), g["inc_faced"].to_numpy(), count=True),
                               "incumbent_vs_recent_mean_multiplicative": compare_point(gm, y_sa_team, g["base_faced_mult"].to_numpy(), g["inc_faced"].to_numpy(), count=True)}
    # efficiency: starter saves given the starter's ACTUAL shots against
    k, n = g["saves"].to_numpy(float), g["shots_against"].to_numpy(float)
    m = n > 0
    p_g = ((g["prior_sv"].fillna(0) + 300 * lg_sv) / (g["prior_sa"].fillna(0) + 300)).to_numpy()
    out["saves_given_shots_against"] = {"n": int(m.sum()), "league_sv_used_by_incumbent": lg_sv,
                                        "nll_league": float(binom_nll(k[m], n[m], np.full(m.sum(), lg_sv)).mean()),
                                        "nll_goalie_shrunk300": float(binom_nll(k[m], n[m], p_g[m]).mean()),
                                        "d_goalie_vs_league": cluster_boot(gm[m], binom_nll(k[m], n[m], np.full(m.sum(), lg_sv)), binom_nll(k[m], n[m], p_g[m]))}
    if sim_g is not None and len(sim_g):
        j = g.merge(sim_g[["game_id", "player_id", "e_saves", "expected_faced"]], on=["game_id", "player_id"], how="inner")
        gj = j["game_id"].to_numpy()
        y = j["saves"].to_numpy(float)
        base_sv = j["base_faced_own"].to_numpy() * lg_sv
        st = {"incumbent_vs_recent_mean_own_sa_x_lg_sv": compare_point(gj, y, base_sv, j["e_saves"].to_numpy(), count=True)}
        ratio = j["e_saves"].to_numpy() / np.maximum(j["inc_faced"].to_numpy(), 1e-6)
        st["incumbent_ratio_x_actual_team_sa (oracle volume)"] = point_metrics(y, ratio * j["sa"].to_numpy())
        st["incumbent_ratio_x_recent_mean_sa"] = point_metrics(y, ratio * j["base_faced_own"].to_numpy())
        st["n_matched"] = int(len(j))
        out["incumbent_saves"] = st
    return out


def main(argv: list[str] | None = None) -> int:
    from nhl_edge.research.player_walk_forward import TEAM_MIN, Data, fit_season_params, simulate

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.opportunity_efficiency")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--wf-games", default="docs/research/walk_forward_v2_wf2_20260929_games.csv")
    ap.add_argument("--season", type=int, default=2024)
    ap.add_argument("--out", default="docs/research/opportunity_efficiency")
    ap.add_argument("--sim-cache", default=None, help="directory holding/receiving incumbent walk-forward outputs skaters_<s>.parquet / goalies_<s>.parquet")
    ap.add_argument("--n-sims", type=int, default=4000)
    a = ap.parse_args(argv)
    data = Data(Path(a.history))
    fp = fit_season_params(data, a.season, PlayerParams())
    sk = skater_frame(data, a.season, fp, TEAM_MIN)
    gf = goalie_frame(data, a.season, fp)
    cache = Path(a.sim_cache) if a.sim_cache else None
    sim_s = sim_g = None
    if cache and (cache / f"skaters_{a.season}.parquet").exists():
        sim_s = pd.read_parquet(cache / f"skaters_{a.season}.parquet")
        sim_g = pd.read_parquet(cache / f"goalies_{a.season}.parquet")
    else:
        sim_s, sim_g = simulate(data, pd.read_csv(a.wf_games), a.season, a.n_sims, progress_every=200)
        if cache:
            cache.mkdir(parents=True, exist_ok=True)
            sim_s.to_parquet(cache / f"skaters_{a.season}.parquet", index=False)
            sim_g.to_parquet(cache / f"goalies_{a.season}.parquet", index=False)
    res = {"season": a.season, "label": "REALISTIC_PIT walk-forward; parameters fit on seasons < test season; no market input",
           "baseline": f"RECENT_MEAN_{RECENT_N}", "team_minutes_incumbent": TEAM_MIN, "bootstrap": {"B": BOOT_B, "seed": BOOT_SEED, "cluster": "game_id"},
           "skaters": skater_decomposition(sk, sim_s), "goalies": goalie_decomposition(gf, sim_g, fp["saves"].lg_sv)}
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"decomposition_{a.season}.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps({"season": a.season, "n_skater_rows": res["skaters"]["n_rows"], "n_goalie_starts": res["goalies"]["n_starts"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
