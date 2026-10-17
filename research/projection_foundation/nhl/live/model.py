"""Heavy step of the live projector: the frozen walk-forward models evaluated for one slate (no re-tuning).

This is `nhl.project.run` with the I/O stripped out: same placeholder-row mechanism, same pipeline stages (frozen
development parameters, season-blocked LightGBM), same distribution fits and selection from results/summary.json. It
returns a plain table (means, pmfs, thresholds, opportunity, gate histories) for every player-row it was given, so the
availability-dependent parts (who is projected, participation, gate status, P(start)) can be recomputed cheaply and
repeatedly on the same table. The table is cached under `NHL_PF_MODELS` keyed by (code, slate, final games); a later
pregame run on the same slate with the same (or a smaller) roster reuses it instead of paying the ~30-40 min rebuild.

Point-in-time: history = final games dated strictly before the slate date (`data.set_cutoff`); the slate's games enter as
placeholder rows whose dummy outcomes can only feed later games, and none exist.
"""
from __future__ import annotations

import hashlib
import json
import os
import pickle
import time
from pathlib import Path

import numpy as np
import pandas as pd

from pf_core import VERSION as PF_VERSION

from nhl import data, project
from nhl import VERSION as NHL_VERSION


PF = project.PF
TABLES = Path(os.environ.get("NHL_PF_MODELS", str(data.CACHE / "model_tables")))
MODEL_NAMES = {"A": "A_season_avg_shrunk", "B": "B_ewma_shrunk", "C": "C_toi_x_rate", "D": "D_opp_adjusted",
               "E": "E_lightgbm", "F": "F_stack"}


def code_hash() -> str:
    h = hashlib.sha256()
    for sub in ("nhl", "pf_core"):
        for f in sorted((PF / sub).glob("*.py")):
            h.update(f.name.encode() + f.read_bytes())
    h.update((PF / "results" / "summary.json").read_bytes())
    return h.hexdigest()[:12]


def finals_hash() -> str:
    """Identity of the history the models see (final games before the cutoff, incl. their stat lines)."""
    p = data.load_kind("players")
    g = data.load_kind("goalies")
    a = pd.util.hash_pandas_object(p[["game_id", "player_id", "goals", "assists", "sog", "toi_s"]], index=False).sum()
    b = pd.util.hash_pandas_object(g[["game_id", "player_id", "saves", "toi_s"]], index=False).sum()
    return hashlib.sha256(f"{len(p)}|{len(g)}|{a}|{b}".encode()).hexdigest()[:12]


def base_key(slate_date: str) -> str:
    """One table per (code, slate date, final-game history): later runs on the same date, when games have started and the
    slate has shrunk, still hit it (`covers` checks the players and goalies they need)."""
    return hashlib.sha256(json.dumps([code_hash(), slate_date, finals_hash()]).encode()).hexdigest()[:16]


def covers(table: dict, lu: pd.DataFrame, gs: pd.DataFrame) -> bool:
    have_s = set(table["skater_keys"])
    have_g = set(table["goalie_keys"])
    need_s = {(int(g), int(p)) for g, p in zip(lu["game_id"], lu["player_id"])}
    need_g = {(int(g), int(p)) for g, p in zip(gs["game_id"], gs["player_id"])} if len(gs) else set()
    return need_s <= have_s and need_g <= have_g


def load_table(key: str) -> dict | None:
    f = TABLES / f"{key}.pkl"
    if f.exists():
        try:
            return pickle.load(open(f, "rb"))
        except Exception:  # noqa: BLE001 - a corrupt cache entry is just a miss
            return None
    return None


def compute(games: pd.DataFrame, lu: pd.DataFrame, gs: pd.DataFrame, slate_date: str, asof: str, key: str,
            log=print) -> dict:
    """Evaluate the frozen models for `games` with the given skater rows `lu` and goalie rows `gs`."""
    from nhl import evaluate as ev
    from nhl import pipeline

    t0 = time.time()
    for p in list(data.CACHE.glob("*.parquet")) + list(data.CACHE.glob("*.json")):
        p.unlink()          # frames built for another slate (placeholders) must never be reused
    hist = data.load_kind("players")
    ghist = data.load_kind("goalies")
    last_final = hist["game_date"].max()
    P, Gr = project.placeholder_rows(games, lu, gs, hist, ghist)
    data.set_future({"players": P, "goalies": Gr})
    pipeline.stage1(rebuild=True)
    sk, _ = pipeline.stage2(rebuild=True)
    gf, tg, _ = pipeline.stage3(rebuild=True)
    log(f"[model] frames built in {time.time() - t0:.0f}s")
    best, readiness = project._best(PF / "results" / "summary.json")
    gids = set(int(x) for x in games["game_id"])
    fut = sk[sk["game_id"].isin(gids)].copy()
    dev = sk["season"].isin([2021, 2022]) & (sk["toi_n"] >= 1)
    rq = np.nanquantile((sk.loc[dev, "toi"] - sk.loc[dev, "toi_E"]).to_numpy(float), [0.1, 0.9])
    # recent history per fut player for the gate (previous 10 games before the slate)
    keep = sk[sk["player_id"].isin(set(fut["player_id"])) & (sk["game_date"] < pd.Timestamp(slate_date))]
    keep = keep.sort_values(["player_id", "game_date", "game_id"]).groupby("player_id").tail(10)
    hist_by_pid = {pid: g for pid, g in keep.groupby("player_id")}

    skaters: dict[tuple[int, int], dict] = {}
    for stat, (fam, rungs) in project.FAMS.items():
        col = f"mu_{stat}_{best[stat]}"
        ok = dev & sk[col].notna()
        dp = ev.fit_dist("nb_binned", sk.loc[ok, stat], sk.loc[ok, col], stat)
        mu = fut[col].fillna(fut[f"mu_{stat}_D"]).to_numpy(float)
        dist = ev.make(dp, mu)
        med, p10, p90, sd = dist.median, dist.quantile(0.1), dist.quantile(0.9), np.sqrt(dist.var)
        thr = {k: dist.prob_ge(k) for k in rungs}
        for i, r in enumerate(fut.itertuples()):
            key_ = (int(r.game_id), int(r.player_id))
            e = skaters.setdefault(key_, {
                "game_id": int(r.game_id), "player_id": int(r.player_id), "team_id": int(r.team_id), "opp_id": int(r.opp_id),
                "name": r.name, "is_home": bool(r.is_home), "toi_E": float(r.toi_E), "toi_pp_E": float(r.toi_pp_E), "toi_n": float(r.toi_n),
                "b2b": int(r.b2b) if np.isfinite(r.b2b) else 0, "stats": {}, "hist_toi": [], "hist": {}})
            oppf = getattr(r, f"oppadj_{stat}")
            e["stats"][stat] = {
                "family": fam, "model": MODEL_NAMES[best[stat]], "mu": float(mu[i]), "probs": dist.P[i].tolist(),
                "median": int(med[i]), "p10": int(p10[i]), "p90": int(p90[i]), "sd": float(sd[i]),
                "thresholds": {str(k): round(float(v[i]), 4) for k, v in thr.items()},
                "oppf": float(oppf) if np.isfinite(oppf) else 1.0}
            h = hist_by_pid.get(r.player_id)
            if h is not None:
                e["hist_toi"] = h["toi"].tolist()
                e["hist"][stat] = h[stat].tolist()
    # goalies
    gcol = f"mu_saves_{best['saves']}"
    gdev = gf["season"].isin([2021, 2022]) & (gf["saves_n"].fillna(0) >= 1) & gf[gcol].notna()
    gdp = ev.fit_dist("nb_binned", gf.loc[gdev, "saves"], gf.loc[gdev, gcol], "saves")
    gfut = gf[gf["game_id"].isin(gids)]
    gd = ev.make(gdp, gfut[gcol].fillna(gfut["mu_saves_D"]))
    goalies: dict[tuple[int, int], dict] = {}
    for i, r in enumerate(gfut.itertuples()):
        goalies[(int(r.game_id), int(r.player_id))] = {
            "game_id": int(r.game_id), "player_id": int(r.player_id), "team_id": int(r.team_id), "opp_id": int(r.opp_id),
            "name": r.name, "family": "saves", "model": MODEL_NAMES[best["saves"]], "mu": float(gd.mean[i]),
            "probs": gd.P[i].tolist(), "median": int(gd.median[i]), "p10": int(gd.quantile(0.1)[i]),
            "p90": int(gd.quantile(0.9)[i]), "thresholds": {str(k): round(float(gd.prob_ge(k)[i]), 4) for k in (20, 25, 30)},
            "sa_D": float(r.sa_D) if np.isfinite(r.sa_D) else None,
            "saves_n": int(r.saves_n) if np.isfinite(r.saves_n) else 0}
    # team goals
    tcol = f"mu_tg_{best['team_goals']}"
    tdev = tg["season"].isin([2021, 2022]) & (tg["goals_for_n"].fillna(0) >= 1) & tg[tcol].notna()
    tdp = ev.fit_dist("nb_binned", tg.loc[tdev, "tg"], tg.loc[tdev, tcol], "team_goals")
    tgf = tg[tg["game_id"].isin(gids)]
    teams = {}
    for r in tgf.itertuples():
        m = getattr(r, tcol)
        if m is None or not np.isfinite(m):
            continue
        d = ev.make(tdp, [m])
        teams[(int(r.game_id), int(r.team_id))] = {
            "game_id": int(r.game_id), "team_id": int(r.team_id), "model": MODEL_NAMES[best["team_goals"]], "mu": float(m),
            "probs": d.P[0].tolist(), "p10": int(d.quantile(0.1)[0]), "p90": int(d.quantile(0.9)[0]),
            "median": int(d.median[0])}
    fam_meta = {}
    for k, (fam, _) in list(project.FAMS.items()) + [("saves", ("saves", None)), ("team_goals", ("team_goals", None))]:
        rd = readiness.get(k, ("SHADOW VALIDATION", "no research summary found"))
        fam_meta[fam] = {"readiness": rd[0], "model": MODEL_NAMES[best[k]], "reason": rd[1]}
    data.set_future({})
    return {
        "key": key, "slate_date": slate_date, "asof": asof, "last_final": f"{last_final:%Y-%m-%d}", "rq": [float(x) for x in rq],
        "families": fam_meta, "skaters": skaters, "goalies": goalies, "teams": teams,
        "skater_keys": sorted(skaters), "goalie_keys": sorted(goalies), "code": code_hash(), "pf_core": PF_VERSION,
        "version": NHL_VERSION, "runtime_s": round(time.time() - t0, 1)}


def save_table(table: dict) -> str:
    TABLES.mkdir(parents=True, exist_ok=True)
    f = TABLES / f"{table['key']}.pkl"
    tmp = f.with_suffix(".tmp")
    with open(tmp, "wb") as fh:
        pickle.dump(table, fh)
    os.replace(tmp, f)
    for old in TABLES.glob("*.pkl"):          # keep the cache small: a table is useless once its slate is three days old
        if old != f and time.time() - old.stat().st_mtime > 3 * 86400:
            old.unlink()
    return str(f)
