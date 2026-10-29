"""NHL_SHOT_VOLUME_V1: a bounded research challenger to PLAYER_SIM_V1's team shot-volume layer (RESEARCH_ONLY).

What the opportunity / efficiency decomposition isolated (``research.opportunity_efficiency``, 2024-25 development
season): a goalie's saves error is dominated by the volume of shots his team faces (scoring the incumbent's own
saves-per-shot ratio against the ACTUAL shots faced cuts saves MAE from 5.30 to 2.04), and the incumbent's expected
shots faced was biased +0.59 shots per team-game. The cause is structural: ``players.params.ShotRates`` averages raw
shots-for / shots-against over the last 82 team-games, so when the league-wide shot level falls (31.4 -> 28.1 per
team-game between 2021-22 and 2024-25) last season's higher counts leak into every team rate, and
``lg x (sf_opp / lg) x (sa_own / lg)`` = ``sf_opp x sa_own / lg`` divides two lagged absolute rates by a lagged
level. Opponent strength is also ignored (a team that played weak shooting teams looks like a good suppressor).

ONE change, in the team shot-volume layer only:

    expected shots faced = league level now x opponent shot-generation ratio x own shot-suppression ratio x venue

where each past team-game is first expressed RELATIVE to the league level at that game's date (``sf / lg_then``,
``sa / lg_then``) and then adjusted once for the opponent faced in that game (``sf_ratio / opp_sa_ratio``,
``sa_ratio / opp_sf_ratio``, opponents' unadjusted ratios as of the forecast date). Half-life (25 games), shrinkage
(15 pseudo-games at ratio 1.0), window (82 team-games), league window (1,200 team-games) and venue factors
(0.985 / 1.015) are the incumbent's, unchanged. The saves negative binomial is RE-FIT with the challenger's offset by
the incumbent's own procedure (``players.params.fit_saves``, same two training seasons).

The shot volume then drives two outputs from ONE draw, keeping the joint simulation coherent:

* goalie saves: the incumbent saves simulator (``players.saves.simulate_saves``: game-script NB, goalie pull) with the
  challenger's expected shots faced;
* skater shots on goal (NEW, coherent): in every draw the opposing net's non-goal shots (its full-game saves before
  the starter-replacement thinning) are allocated to the team's skaters, multinomially, with weight = the incumbent's
  own expected SOG (expected TOI by state x shots on goal per 60, ``roster.build_roster`` meta) minus the skater's
  simulated goal expectation (floored at 5% of his expected SOG), x the draw's TOI multiplier; each skater's SOG = his simulated goals (incl. empty-net, never shootout) + his allocated non-goal shots.
  So per draw: SOG >= goals for every skater, Σ team skater SOG = opposing net shots faced + empty-net goals, and
  points = goals + assists are untouched.

Team goals, goals / assists / points of every skater and every TOI multiplier are bit-identical to PLAYER_SIM_V1
(same seeds, same draws); only saves and SOG change. No market input is read: the CLI accepts a ``--market`` path
only so that the runtime non-leakage rerun can mutate it, and ignores it unless ``--use-market-center`` (the negative
control) is given.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from nhl_edge.players.engine import PlayerSimResult, TeamDraws, simulate_players
from nhl_edge.players.features import PlayerBook, PlayerParams
from nhl_edge.players.params import fit_saves
from nhl_edge.players.saves import SavesDraws, simulate_saves
from nhl_edge.sim.engine import TeamParams
from nhl_edge.sim.engine_v2 import load_params, simulate_game_v2

MODEL_VERSION = "NHL_SHOT_VOLUME_V1"
INCUMBENT_VERSION = "PLAYER_SIM_V1"
BASELINE_VERSION = "RECENT_MEAN_10"
QUANTILES = (0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95)
LADDERS: dict[str, list[float]] = {
    "shots_on_goal": [1, 2, 3, 4, 5, 6],
    "points": [1, 2, 3],
    "assists": [1, 2, 3],
    "time_on_ice_min": [8, 10, 12, 14, 16, 18, 20, 22, 24, 26],
    "goalie_saves": list(range(15, 41)),
}
STATS = tuple(LADDERS)
ET = ZoneInfo("America/New_York")


# ---------------------------------------------------------------------------------------------------------------------
# the challenger shot-volume layer
# ---------------------------------------------------------------------------------------------------------------------
@dataclass
class RelativeShotRates:
    """Team shot generation / suppression in league-relative units, opponent-adjusted once, strictly before the date.

    ``tg``: ``players.params.team_game_frame`` output (one row per team-game: sf, sa, opp_id, date_int)."""

    tg: pd.DataFrame
    league_window: int = 1200
    half_life: float = 25.0
    prior_games: float = 15.0
    max_games: int = 82
    opp_adjust: bool = True
    venue: tuple[float, float] = (0.985, 1.015)  # (home, road) multipliers, the incumbent's
    _cache: dict[int, dict[int, tuple[float, float]]] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        self.tg = self.tg.sort_values(["date_int", "game_id"]).reset_index(drop=True)
        self._dates = self.tg["date_int"].to_numpy()
        self._sa = self.tg["sa"].to_numpy(float)
        self.league_sog = float(self._sa.mean())  # fallback only before any team-game exists (as the incumbent)
        # league level at each past game's date (strictly before it), then the game's relative rates
        # a team-game with no earlier league history (the first date of the data) has no relative value: dropped, so
        # nothing after a game ever enters it
        lg = np.array([self.league_at(int(d)) if np.searchsorted(self._dates, int(d), side="left") > 0 else np.nan for d in self._dates])
        self.tg["lg_then"] = lg
        self.tg["sf_r"] = self.tg["sf"].to_numpy(float) / lg
        self.tg["sa_r"] = self.tg["sa"].to_numpy(float) / lg
        ok = self.tg[np.isfinite(lg)]
        self._by = {int(k): (v["date_int"].to_numpy(), v["opp_id"].to_numpy().astype(int), v["sf_r"].to_numpy(float), v["sa_r"].to_numpy(float))
                    for k, v in ok.groupby("team_id")}

    def league_at(self, date_int: int) -> float:
        hi = int(np.searchsorted(self._dates, date_int, side="left"))
        if hi == 0:
            return self.league_sog
        return float(self._sa[max(0, hi - self.league_window):hi].mean())

    def _shrunk(self, x: np.ndarray) -> float:
        w = 0.5 ** (np.arange(len(x))[::-1] / self.half_life)
        return float((np.sum(w * x) + self.prior_games * 1.0) / (w.sum() + self.prior_games))

    def ratings(self, date_int: int) -> dict[int, tuple[float, float]]:
        """{team: (shot-generation ratio, shot-suppression ratio)} from team-games strictly before ``date_int``."""
        if date_int in self._cache:
            return self._cache[date_int]
        win = {}
        for t, (d, o, sf, sa) in self._by.items():
            hi = int(np.searchsorted(d, date_int, side="left"))
            lo = max(0, hi - self.max_games)
            win[t] = (o[lo:hi], sf[lo:hi], sa[lo:hi])
        raw = {t: (self._shrunk(sf) if len(sf) else 1.0, self._shrunk(sa) if len(sa) else 1.0) for t, (_, sf, sa) in win.items()}
        if not self.opp_adjust:
            self._cache[date_int] = raw
            return raw
        adj = {}
        for t, (o, sf, sa) in win.items():
            if not len(sf):
                adj[t] = (1.0, 1.0)
                continue
            opp_sa = np.array([raw.get(int(x), (1.0, 1.0))[1] for x in o])
            opp_sf = np.array([raw.get(int(x), (1.0, 1.0))[0] for x in o])
            adj[t] = (self._shrunk(sf / np.maximum(opp_sa, 1e-6)), self._shrunk(sa / np.maximum(opp_sf, 1e-6)))
        self._cache[date_int] = adj
        return adj

    def expected_faced(self, team_id: int, opp_id: int, date_int: int, home: bool) -> float:
        r = self.ratings(int(date_int))
        own = r.get(int(team_id), (1.0, 1.0))
        opp = r.get(int(opp_id), (1.0, 1.0))
        return float(self.league_at(int(date_int)) * opp[0] * own[1] * (self.venue[0] if home else self.venue[1]))

    def features(self, team_id: int, opp_id: int, date_int: int) -> dict[str, float]:
        r = self.ratings(int(date_int))
        return {"league_shots_per_team_game": self.league_at(int(date_int)), "opp_shot_generation_ratio": r.get(int(opp_id), (1.0, 1.0))[0],
                "own_shot_suppression_ratio": r.get(int(team_id), (1.0, 1.0))[1]}


def allocate_sog(rng: np.random.Generator, draws: TeamDraws, weight: np.ndarray, nongoal: np.ndarray) -> np.ndarray:
    """Per draw, the team's non-goal shots on goal (= the opposing net's saves before replacement thinning) allocated
    multinomially over the skaters with weight x the draw's TOI multiplier; plus each skater's goals."""
    W = np.maximum(np.asarray(weight, float), 1e-9)[None, :] * draws.toi_mult.astype(np.float64)
    P = W / W.sum(axis=1, keepdims=True)
    alloc = rng.multinomial(np.asarray(nongoal, dtype=np.int64), P)
    return draws.goals.astype(np.int64) + alloc


def coherence_violations(ps: PlayerSimResult, sog: dict[str, np.ndarray], net_nongoal: dict[str, np.ndarray]) -> list[str]:
    """Checks of the challenger's joint draw (reported, never repaired)."""
    out = []
    for side, d in (("home", ps.home), ("away", ps.away)):
        s = sog.get(side)
        if s is None:
            continue
        if (s < d.goals).any():
            out.append(f"{side}: a skater has fewer shots on goal than goals")
        if not np.array_equal(s.sum(axis=1), d.goals.sum(axis=1).astype(np.int64) + net_nongoal[side]):
            out.append(f"{side}: team skater SOG != team goals + opposing net non-goal shots")
        if not np.array_equal(d.points, d.goals + d.a1 + d.a2):
            out.append(f"{side}: points != goals + assists")
    # goals against each net = the other side's non-empty-net goals: net shots faced = saves + those goals
    return out


# ---------------------------------------------------------------------------------------------------------------------
# distribution summaries and scoring from draws
# ---------------------------------------------------------------------------------------------------------------------
def summarize(x: np.ndarray, ladder: list[float], discrete: bool) -> dict[str, Any]:
    """mean / quantiles / threshold probabilities of one player-game-stat from its draws."""
    x = np.asarray(x, float)
    qs = np.quantile(x, QUANTILES, method="inverted_cdf" if discrete else "linear")
    thr = [float(np.mean(x >= t)) for t in ladder]
    for i in range(1, len(thr)):  # exact monotone (it already is; guard float noise)
        thr[i] = min(thr[i], thr[i - 1])
    return {"mean": float(x.mean()), "q": [float(v) for v in qs], "thr": thr}


def crps_draws(x: np.ndarray, y: float) -> float:
    """CRPS of the empirical distribution of draws ``x`` at ``y`` (E|X - y| - 0.5 E|X - X'|, sorted-draw form)."""
    s = np.sort(np.asarray(x, float))
    n = len(s)
    e1 = np.mean(np.abs(s - y))
    i = np.arange(1, n + 1)
    e2 = 2.0 * np.sum((2 * i - n - 1) * s) / (n * n)
    return float(e1 - 0.5 * e2)


def log_score_draws(x: np.ndarray, y: float) -> float:
    """-log P(X = y) of the draws' empirical PMF, floored at 1 / (2 n) (preregistered)."""
    x = np.asarray(x)
    n = len(x)
    p = max(float(np.mean(x == y)), 1.0 / (2.0 * n))
    return float(-np.log(p))


def pit_mid(x: np.ndarray, y: float) -> float:
    x = np.asarray(x, float)
    return float(np.mean(x < y) + 0.5 * np.mean(x == y))


# ---------------------------------------------------------------------------------------------------------------------
# walk-forward harness (same games, seeds and rosters as research.player_walk_forward.simulate)
# ---------------------------------------------------------------------------------------------------------------------
def kickoff_utc(start_time_et: str) -> datetime:
    return datetime.fromisoformat(str(start_time_et)).replace(tzinfo=ET).astimezone(UTC)


def baseline_frames(data: Any, season: int) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, float]]:
    """RECENT_MEAN_10 for every regular-season skater-game (official lines, all dressed games) and team-game."""
    from nhl_edge.research.opportunity_efficiency import recent_mean

    pl = data.players[data.players["game_type"] == 2].copy()
    pl["toi_min"] = pl["toi_s"] / 60.0
    cols = ["toi_min", "sog", "points", "assists"]
    rm = recent_mean(pl, "player_id", cols)
    pl = pl.join(rm)
    tr = pl[pl["season"] < season]
    pos = tr["position"].map(lambda p: "D" if str(p).upper().startswith("D") else "F")
    pos_mean = tr.groupby(pos)[cols].mean()
    resid = (tr["toi_min"] - tr["rm_toi_min"]).dropna()
    toi_sd = float(resid.std())
    cur = pl[pl["season"] == season].copy()
    cpos = cur["position"].map(lambda p: "D" if str(p).upper().startswith("D") else "F")
    for c in cols:
        cur[f"base_{c}"] = cur[f"rm_{c}"].fillna(cpos.map(pos_mean[c]))
    tg = data.tg[data.tg["game_id"].astype(str).str[4:6] == "02"]
    trm = recent_mean(tg, "team_id", ["sa"])
    tg = tg.join(trm)
    return cur, tg, {"toi_resid_sd_min": toi_sd}


@dataclass
class ArmRows:
    """Compact per-row forecasts of one arm (summaries + exact scores), for sidecars and evaluation."""

    rows: list[dict[str, Any]] = field(default_factory=list)


def run(data: Any, wf_games: pd.DataFrame, season: int, n_sims: int = 4000, max_games: int | None = None, game_ids: list[int] | None = None,
        progress_every: int = 200) -> dict[str, Any]:
    """Simulate every game once (incumbent seeds) and emit, per player-game-stat, the incumbent, challenger and baseline
    forecasts with exact draw-based scores. Takes no market argument."""
    from nhl_edge.players.roster import team_pp_shares
    from nhl_edge.research.player_walk_forward import fit_season_params, roster_for

    fp = fit_season_params(data, season, PlayerParams())
    rel = RelativeShotRates(data.tg)
    saves_chal = fit_saves(data.goalies, data.goals, data.tg, rel, fp["train"][-2:])
    book = PlayerBook(data.pg, fp["priors"], fp["params"])
    sp = load_params()
    wf = wf_games[wf_games["season"] == season].sort_values(["game_date", "game_id"])
    if game_ids is not None:
        wf = wf[wf["game_id"].isin(game_ids)]
    if max_games:
        wf = wf.head(max_games)
    ppm = wf_games[["ppmin_home", "ppmin_away"]].stack().mean()
    ppo = wf_games[["home_pp_off", "away_pp_off"]].stack().mean()
    pkd = wf_games[["home_pk_def", "away_pk_def"]].stack().mean()
    known = set(data.players["game_id"].unique())
    games_tbl = data.games.set_index("game_id") if hasattr(data, "games") else None
    base_pl, base_tg, base_meta = baseline_frames(data, season)
    base_pl = base_pl.set_index(["game_id", "player_id"])
    base_tg = base_tg.set_index(["game_id", "team_id"])
    lg_sv = fp["saves"].lg_sv
    out: dict[str, list[dict[str, Any]]] = {INCUMBENT_VERSION: [], MODEL_VERSION: [], BASELINE_VERSION: []}
    invariants: dict[str, int] = {"games": 0, "draws_checked": 0, "violations": 0, "incumbent_invariant_violations": 0}
    excluded: dict[str, int] = {"game_not_in_player_tables": 0, "team_without_starter_row": 0}
    viol_examples: list[str] = []
    t0 = time.time()
    from nhl_edge.players.engine import invariant_violations

    for k, r in enumerate(wf.itertuples(index=False)):
        gid = int(r.game_id)
        if gid not in known:
            excluded["game_not_in_player_tables"] += 1
            continue
        di = int(str(r.game_date).replace("-", "")[:8])
        box = data.players[data.players["game_id"] == gid]
        hid = int(box.loc[box["is_home"], "team_id"].iloc[0])
        aid = int(box.loc[~box["is_home"], "team_id"].iloc[0])
        hpp, hsh = team_pp_shares(r.ppmin_home / ppm * 4.3, r.ppmin_away / ppm * 4.3, r.home_pp_off / ppo, r.away_pk_def / pkd)
        app, ash = team_pp_shares(r.ppmin_away / ppm * 4.3, r.ppmin_home / ppm * 4.3, r.away_pp_off / ppo, r.home_pk_def / pkd)
        rb_h = roster_for(data, book, gid, hid, di, season, hpp, hsh)
        rb_a = roster_for(data, book, gid, aid, di, season, app, ash)
        seed = gid % (2**31)
        res = simulate_game_v2(TeamParams(hid, "H", float(r.lam_st_home)), TeamParams(aid, "A", float(r.lam_st_away)), seed=seed, n_sims=n_sims, params=sp,
                               record_steps=True)
        ps = simulate_players(res, rb_h.roster, rb_a.roster, fp["strength"], seed + 1)
        invariants["incumbent_invariant_violations"] += len(invariant_violations(res, ps))
        ko = kickoff_utc(games_tbl.loc[gid, "start_time_et"]) if games_tbl is not None and gid in games_tbl.index else \
            datetime(int(str(di)[:4]), int(str(di)[4:6]), int(str(di)[6:8]), 23, 0, tzinfo=UTC)
        as_of = ko - timedelta(minutes=60)
        src_max = datetime(int(str(di)[:4]), int(str(di)[4:6]), int(str(di)[6:8]), 8, 0, tzinfo=UTC)
        if not src_max <= as_of < ko:
            raise ValueError(f"{gid}: time ordering violated ({src_max} / {as_of} / {ko})")
        meta = {"game_id": gid, "season": season, "date_int": di, "kickoff": ko, "as_of": as_of, "src_max": src_max}
        # saves for each net (the actual starter: conditional on starting), incumbent and challenger, same seed
        gl = data.goalies[(data.goalies["game_id"] == gid) & (data.goalies["starter"].astype(bool))]
        nets: dict[str, dict[str, Any]] = {}
        for gr in gl.itertuples(index=False):
            home_g = bool(gr.is_home)
            tid, oid = (hid, aid) if home_g else (aid, hid)
            ef_i = fp["rates"].expected_faced(tid, oid, di, home_g)
            ef_c = rel.expected_faced(tid, oid, di, home_g)
            sd_i = simulate_saves(res, ps, home_g, fp["saves"], ef_i, seed + 7)
            sd_c = simulate_saves(res, ps, home_g, saves_chal, ef_c, seed + 7)
            nets["home" if home_g else "away"] = {"row": gr, "tid": tid, "oid": oid, "ef_i": ef_i, "ef_c": ef_c, "sd_i": sd_i, "sd_c": sd_c}
        # challenger SOG: the shooting side's non-goal shots = the OPPOSING net's full-game saves (before thinning)
        rng = np.random.default_rng([seed, 11])
        sog: dict[str, np.ndarray] = {}
        nongoal: dict[str, np.ndarray] = {}
        for side, d, rb in (("home", ps.home, rb_h), ("away", ps.away, rb_a)):
            opp_net = nets.get("away" if side == "home" else "home")
            if opp_net is None:
                excluded["team_without_starter_row"] += 1
                continue
            sdc: SavesDraws = opp_net["sd_c"]
            ga_full = ps.ga_away if side == "home" else ps.ga_home
            ng = (sdc.net_shots_faced - ga_full).astype(np.int64)
            # weight on NON-goal shots = the incumbent's expected SOG minus the skater's simulated goal expectation (goals
            # are added back per draw, so a scorer is not counted twice); floored at 5% of his expected SOG
            esog = np.array([rb.player_meta[int(p)]["expected_sog"] for p in rb.roster.player_ids])
            w = np.maximum(esog - d.goals.mean(axis=0), 0.05 * esog)
            sog[side] = allocate_sog(rng, d, w, ng)
            nongoal[side] = ng
        v = coherence_violations(ps, sog, nongoal)
        invariants["games"] += 1
        invariants["draws_checked"] += n_sims
        invariants["violations"] += len(v)
        viol_examples.extend(v[:2])
        # incumbent SOG: PLAYER_SIM_V1 exposes only a mean (roster meta ``expected_sog``); its minimal distributional
        # reading is Poisson around that mean, drawn with a fixed per-game stream
        rng_i = np.random.default_rng([seed, 13])
        rng_b = np.random.default_rng([seed, 17])
        for side, d, rb in (("home", ps.home, rb_h), ("away", ps.away, rb_a)):
            ro = rb.roster
            for i, pid in enumerate(ro.player_ids):
                pid = int(pid)
                m = rb.player_meta[pid]
                toi_draw = m["expected_toi_total_min"] * d.toi_mult[:, i].astype(np.float64)
                sog_i = rng_i.poisson(max(m["expected_sog"], 1e-9), n_sims)
                bkey = (gid, pid)
                b = base_pl.loc[bkey] if bkey in base_pl.index else None
                lineage = {"prior_games": float(m["n_games"]), "share_ev": float(m["share"]["ev"]), "share_pp": float(m["share"]["pp"]),
                           "expected_toi_min": float(m["expected_toi_total_min"]), "expected_sog_incumbent": float(m["expected_sog"])}
                common = dict(meta, player_id=pid, team_id=int(ro.team_id), pos=ro.pos[i], lineage=lineage)
                arms = {INCUMBENT_VERSION: {"points": d.points[:, i], "assists": d.assists[:, i], "time_on_ice_min": toi_draw, "shots_on_goal": sog_i},
                        MODEL_VERSION: {"points": d.points[:, i], "assists": d.assists[:, i], "time_on_ice_min": toi_draw,
                                        "shots_on_goal": sog[side][:, i] if side in sog else None}}
                if b is not None:
                    arms[BASELINE_VERSION] = {"points": rng_b.poisson(max(float(b["base_points"]), 1e-9), n_sims),
                                              "assists": rng_b.poisson(max(float(b["base_assists"]), 1e-9), n_sims),
                                              "time_on_ice_min": np.maximum(rng_b.normal(float(b["base_toi_min"]), base_meta["toi_resid_sd_min"], n_sims), 0.0),
                                              "shots_on_goal": rng_b.poisson(max(float(b["base_sog"]), 1e-9), n_sims)}
                    actual = {"points": float(b["points"]), "assists": float(b["assists"]), "time_on_ice_min": float(b["toi_min"]), "shots_on_goal": float(b["sog"])}
                else:
                    a = box.set_index("player_id").loc[pid]
                    actual = {"points": float(a["points"]), "assists": float(a["assists"]), "time_on_ice_min": float(a["toi_s"]) / 60.0, "shots_on_goal": float(a["sog"])}
                for arm, stats in arms.items():
                    for stat, x in stats.items():
                        if x is None:
                            continue
                        out[arm].append(_row(common, stat, x, actual[stat]))
        for net in nets.values():
            gr = net["row"]
            y = float(gr.saves or 0)
            feats_c = rel.features(net["tid"], net["oid"], di)
            common = dict(meta, player_id=int(gr.player_id), team_id=int(net["tid"]), pos="G",
                          lineage={"expected_shots_faced": float(net["ef_c"]), **{k2: float(v2) for k2, v2 in feats_c.items()}})
            common_i = dict(common, lineage={"expected_shots_faced": float(net["ef_i"]), "league_shots_per_team_game": float(fp["rates"].league_at(di))})
            out[INCUMBENT_VERSION].append(_row(common_i, "goalie_saves", net["sd_i"].saves, y))
            out[MODEL_VERSION].append(_row(common, "goalie_saves", net["sd_c"].saves, y))
            bk = (gid, int(net["tid"]))
            if bk in base_tg.index:
                bsa = base_tg.loc[bk, "rm_sa"]
                bsa = float(bsa) if pd.notna(bsa) else float(fp["rates"].league_at(di))
                out[BASELINE_VERSION].append(_row(dict(common, lineage={"recent_mean_shots_against": bsa}), "goalie_saves",
                                                  rng_b.poisson(bsa * lg_sv, n_sims), y))
        if progress_every and (k + 1) % progress_every == 0:
            print(f"season {season}: {k + 1}/{len(wf)} games, {time.time() - t0:.0f}s", flush=True)
    return {"rows": out, "invariants": invariants, "violation_examples": viol_examples[:10], "excluded": excluded,
            "saves_model_challenger": saves_chal.to_dict(), "saves_model_incumbent": fp["saves"].to_dict(), "baseline_meta": base_meta}


def _row(common: dict[str, Any], stat: str, x: np.ndarray, y: float) -> dict[str, Any]:
    discrete = stat != "time_on_ice_min"
    s = summarize(x, LADDERS[stat], discrete)
    xr = np.asarray(x, float)
    return {**{k: v for k, v in common.items()}, "statistic": stat, "actual": y, "mean": s["mean"], "q": s["q"], "thr": s["thr"],
            "crps": crps_draws(xr, y), "log_score": log_score_draws(np.round(xr) if discrete else xr, y) if discrete else None,
            "pit": pit_mid(xr, y), "in80": bool(s["q"][1] <= y <= s["q"][9])}


# ---------------------------------------------------------------------------------------------------------------------
# PURE sidecar (pure_forecast.v1) and outcomes
# ---------------------------------------------------------------------------------------------------------------------
def iso(t: datetime) -> str:
    return t.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def frozen_hash(paths: list[Path]) -> str:
    h = hashlib.sha256()
    for p in paths:
        h.update(Path(p).read_bytes())
    return "sha256:" + h.hexdigest()


def model_files() -> list[Path]:
    root = Path(__file__).resolve().parents[1]
    return [root / "research" / "shot_volume_v1.py", root / "players" / "engine.py", root / "players" / "saves.py", root / "players" / "params.py",
            root / "players" / "features.py", root / "players" / "roster.py", root / "sim" / "engine_v2.py"]


def to_pure(r: dict[str, Any], model_version: str, model_hash: str) -> dict[str, Any]:
    q = r["q"]
    src = iso(r["src_max"])
    sources = [{"source_id": "nhl_official_game_records", "class": "sports_only", "max_observed_at": src,
                "description": "official NHL boxscore, play-by-play and shift charts of games before the forecast date"},
               {"source_id": "v2_team_strength_walk_forward", "class": "sports_only", "max_observed_at": src,
                "description": "point-in-time DATA_ONLY_V2 team scoring rates (docs/research/walk_forward_v2_wf2_20260929_games.csv)"}]
    lineage = [{"name": k, "value": round(float(v), 6), "source": "nhl_official_game_records", "observed_at": src, "class": "sports_only"}
               for k, v in r["lineage"].items()]
    thresholds = [{"at_least": float(t), "probability": round(float(p), 6)} for t, p in zip(LADDERS[r["statistic"]], r["thr"])]
    for i in range(1, len(thresholds)):
        thresholds[i]["probability"] = min(thresholds[i]["probability"], thresholds[i - 1]["probability"])
    return {"schema_version": "pure_forecast.v1", "sport": "NHL", "game_id": str(r["game_id"]), "player_id": str(r["player_id"]), "statistic": r["statistic"],
            "as_of": iso(r["as_of"]), "kickoff": iso(r["kickoff"]), "source_max_observed_at": src, "projection_mode": "PURE_INDEPENDENT",
            "model_version": model_version, "model_frozen_hash": model_hash, "conditional_on_playing": True, "participation_probability": None,
            "projection": {"mean": round(r["mean"], 6), "median": q[5], "p10": q[1], "p90": q[9],
                           "quantiles": [{"q": lv, "value": v} for lv, v in zip(QUANTILES, q)], "thresholds": thresholds},
            "sources": sources, "feature_lineage": lineage, "x_population": "every dressed skater / starting goalie (conditional on playing / starting)"}


def to_outcome(r: dict[str, Any]) -> dict[str, Any]:
    return {"sport": "NHL", "game_id": str(r["game_id"]), "player_id": str(r["player_id"]), "statistic": r["statistic"], "actual": r["actual"], "played": True,
            "source": "nhl_api_boxscore", "observed_at": "2026-09-30T05:35:53Z"}


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, sort_keys=True) + "\n")


# ---------------------------------------------------------------------------------------------------------------------
# CLI: --mode rerun is the upstream command the pure_gate rerun executes; --mode eval writes the scored frames
# ---------------------------------------------------------------------------------------------------------------------
ANCHOR_WEIGHT = 0.80  # MARKET_ANCHORED_PLAYER_V1's weight on the market (workflows.shadow_player.ANCHOR_WEIGHT)


def market_centered(rows: list[dict[str, Any]], quotes: pd.DataFrame) -> list[dict[str, Any]]:
    """NEGATIVE CONTROL ONLY (never a PURE output): the existing market-anchored blend, logit(p) = 0.8 logit(mid) +
    0.2 logit(model), applied to every threshold that has a quote. Exists so the rerun gate can show the mutation of
    the market file reaches a reader."""
    q = {(str(int(r.game_id)), str(int(r.player_id)), str(r.statistic), float(r.at_least)): float(r.mid) for r in quotes.itertuples(index=False)}
    lg = lambda x: np.log(min(max(x, 1e-4), 1 - 1e-4) / (1 - min(max(x, 1e-4), 1 - 1e-4)))  # noqa: E731
    out = []
    for r in rows:
        r = json.loads(json.dumps(r))
        th = r["projection"]["thresholds"]
        for t in th:
            m = q.get((r["game_id"], r["player_id"], r["statistic"], float(t["at_least"])))
            if m is not None:
                z = ANCHOR_WEIGHT * lg(m) + (1 - ANCHOR_WEIGHT) * lg(t["probability"])
                t["probability"] = round(float(1 / (1 + np.exp(-z))), 6)
        for i in range(1, len(th)):
            th[i]["probability"] = min(th[i]["probability"], th[i - 1]["probability"])
        r["model_version"] = "NEGATIVE_CONTROL_MARKET_ANCHORED"
        out.append(r)
    return out


def rows_frame(rows: list[dict[str, Any]]) -> pd.DataFrame:
    df = pd.DataFrame(rows)
    df["lineage"] = df["lineage"].map(lambda d: json.dumps(d, sort_keys=True))
    for c in ("kickoff", "as_of", "src_max"):
        df[c] = df[c].map(iso)
    return df


def frame_rows(df: pd.DataFrame) -> list[dict[str, Any]]:
    out = []
    for r in df.to_dict("records"):
        r["lineage"] = json.loads(r["lineage"])
        for c in ("kickoff", "as_of", "src_max"):
            r[c] = datetime.strptime(r[c], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC)
        r["q"] = [float(v) for v in r["q"]]
        r["thr"] = [float(v) for v in r["thr"]]
        out.append(r)
    return out


def main(argv: list[str] | None = None) -> int:
    from nhl_edge.research.player_walk_forward import Data

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.shot_volume_v1")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--wf-games", default="docs/research/walk_forward_v2_wf2_20260929_games.csv")
    ap.add_argument("--season", type=int, default=2025)
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--max-games", type=int, default=None)
    ap.add_argument("--game-ids", default=None, help="comma-separated game ids (rerun snapshot)")
    ap.add_argument("--mode", choices=["eval", "rerun"], default="eval")
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=0, help="accepted for the rerun gate; the walk-forward seeds are the game ids")
    ap.add_argument("--market", default=None, help="market quotes CSV (IGNORED by the PURE model; read only with --use-market-center)")
    ap.add_argument("--use-market-center", action="store_true", help="NEGATIVE CONTROL: the existing market-anchored blend")
    a = ap.parse_args(argv)
    data = Data(Path(a.history))
    data.games = pd.read_parquet(Path(a.history) / "nhl" / f"games_{a.season}.parquet")
    wf = pd.read_csv(a.wf_games)
    gids = [int(x) for x in a.game_ids.split(",")] if a.game_ids else None
    res = run(data, wf, a.season, a.n_sims, a.max_games, game_ids=gids, progress_every=0 if a.mode == "rerun" else 200)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    h = frozen_hash(model_files())
    if a.mode == "rerun":
        pure = [to_pure(r, MODEL_VERSION, h) for r in res["rows"][MODEL_VERSION]]
        if a.use_market_center:
            pure = market_centered(pure, pd.read_csv(a.market))  # the control reads the market file: deleted -> fails
        write_jsonl(out / "pure_forecasts.jsonl", pure)
        return 0
    for arm, rows in res["rows"].items():
        rows_frame(rows).to_parquet(out / f"rows_{arm}_{a.season}.parquet", index=False)
    meta = {k: v for k, v in res.items() if k != "rows"}
    meta["model_frozen_hash"] = h
    (out / f"run_meta_{a.season}.json").write_text(json.dumps(meta, indent=1, default=str))
    print(json.dumps({"season": a.season, "rows": {k: len(v) for k, v in res["rows"].items()}, "invariants": res["invariants"], "excluded": res["excluded"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
