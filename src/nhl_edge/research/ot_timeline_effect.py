"""Before / after effect of the overtime-timeline fix on PLAYER_SIM_V1 (RESEARCH_ONLY; offline; deploys nothing).

``data.player_events`` used to lay every overtime game out to 80:00, booking the phantom seconds after the final
whistle to the last strength state; deployment shares (player seconds / team seconds) were deflated in every OT game.
This module quantifies what the fix changes, given two copies of the official player-event tables:

* ``--old``  the committed history (``data/history``, schema nhl-player-events-1.0)
* ``--new``  the same games re-derived with the fixed code (schema 1.1), e.g. a scratch rebuild

It reports (1) which tables / columns actually differ, (2) the production TOI / PP-share / SOG path
(``players.roster.build_roster`` with the production team-minute template of ``workflows.shadow_player``) and the
PLAYER_SIM_V1 walk-forward (``research.player_walk_forward.simulate``: goals / assists / points / saves), each scored on
2024-25 and 2025-26 with paired game-clustered bootstrap CIs (after minus before), and (3) how ``players.fit.fit_all``
would change ``data/params/player-sim-1.0.json``. It never writes the parameter file.

    python -m nhl_edge.research.ot_timeline_effect --old data/history --new <rebuilt history> --out docs/research/ot_timeline_fix
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.player_history import TABLES, load_player_tables
from nhl_edge.players.features import PlayerBook, PlayerParams
from nhl_edge.players.roster import build_roster, team_pp_shares
from nhl_edge.research.player_walk_forward import Data, dressed, fit_season_params, simulate

SEASONS_ALL = [2021, 2022, 2023, 2024, 2025]
WF_GAMES = "docs/research/walk_forward_v2_wf2_20260929_games.csv"
SEED = 20261012


def production_team_minutes(p_pp: float) -> dict[str, float]:
    """``workflows.shadow_player``'s team-minute template (verbatim; a test pins it)."""
    return {"ev": 50.6, "pp": 4.4 * p_pp / 0.215, "sh": 4.4, "ea": 0.6, "en": 0.6, "ot": 1.2}


# ---------------------------------------------------------------------------------------------------------------------
# 1. what changed in the tables
# ---------------------------------------------------------------------------------------------------------------------
def compare_tables(old: Path, new: Path, seasons: list[int]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for t in TABLES:
        a, b = load_player_tables(old, t, seasons), load_player_tables(new, t, seasons)
        cols = [c for c in a.columns if c in b.columns and c != "schema_version"]
        key = [c for c in ("game_id", "team_id", "player_id", "p1", "p2", "period", "t_s", "shooter_id", "kind") if c in cols]
        a2 = a[cols].sort_values(key).reset_index(drop=True)
        b2 = b[cols].sort_values(key).reset_index(drop=True)
        rec: dict[str, Any] = {"rows_old": int(len(a)), "rows_new": int(len(b))}
        if len(a2) == len(b2):
            diff_cols = [c for c in cols if not a2[c].equals(b2[c]) and not (a2[c].fillna(-999).astype(str) == b2[c].fillna(-999).astype(str)).all()]
            rec["columns_differing"] = diff_cols
        else:
            rec["columns_differing"] = "row count differs"
        out[t] = rec
    a, b = load_player_tables(old, "team_states", seasons), load_player_tables(new, "team_states", seasons)
    m = a.merge(b, on=["game_id", "team_id"], suffixes=("_old", "_new"))
    reg = m["game_type_old"] == 2
    ot = reg & (m["n_seconds_old"] > 3600)
    st = ["sec_ev", "sec_pp", "sec_sh", "sec_ea", "sec_en"]
    removed = {s: float((m.loc[ot, f"{s}_old"] - m.loc[ot, f"{s}_new"]).sum() / 60.0) for s in st}
    n_states_changed = sum((m.loc[ot, f"{s}_old"] != m.loc[ot, f"{s}_new"]).astype(int) for s in st)
    out["team_states_ot_detail"] = {
        "regular_season_ot_team_rows": int(ot.sum()), "n_seconds_old_values": sorted(int(x) for x in m.loc[ot, "n_seconds_old"].unique()),
        "n_seconds_new_mean": float(m.loc[ot, "n_seconds_new"].mean()), "n_seconds_new_min": int(m.loc[ot, "n_seconds_new"].min()),
        "n_seconds_new_max": int(m.loc[ot, "n_seconds_new"].max()),
        "new_states_sum_to_n_seconds": bool((m.loc[reg, [f"{s}_new" for s in st]].sum(axis=1) + m.loc[reg, "sec_unknown_new"] == m.loc[reg, "n_seconds_new"]).all()),
        "phantom_minutes_removed_by_state": removed, "rows_by_number_of_states_changed": {int(k): int(v) for k, v in n_states_changed.value_counts().items()},
        "regulation_rows_unchanged": bool((m.loc[reg & ~ot, [f"{s}_old" for s in st]].to_numpy() == m.loc[reg & ~ot, [f"{s}_new" for s in st]].to_numpy()).all()),
    }
    return out


# ---------------------------------------------------------------------------------------------------------------------
# 2a. production TOI / PP share / SOG path
# ---------------------------------------------------------------------------------------------------------------------
def production_rows(data: Data, wf: pd.DataFrame, season: int) -> pd.DataFrame:
    fp = fit_season_params(data, season, PlayerParams())
    book = PlayerBook(data.pg, fp["priors"], fp["params"])
    ppm = wf[["ppmin_home", "ppmin_away"]].stack().mean()
    ppo = wf[["home_pp_off", "away_pp_off"]].stack().mean()
    pkd = wf[["home_pk_def", "away_pk_def"]].stack().mean()
    pl = data.players[(data.players["season"] == season) & (data.players["game_type"] == 2)]
    by_game = {int(k): v for k, v in pl.groupby("game_id")}
    ts = data.team_states.set_index(["game_id", "team_id"])
    rows = []
    for r in wf[wf["season"] == season].sort_values(["game_date", "game_id"]).itertuples(index=False):
        gid = int(r.game_id)
        box = by_game.get(gid)
        if box is None:
            continue
        di = int(str(r.game_date).replace("-", "")[:8])
        hid = int(box.loc[box["is_home"], "team_id"].iloc[0])
        aid = int(box.loc[~box["is_home"], "team_id"].iloc[0])
        hpp, hsh = team_pp_shares(r.ppmin_home / ppm * 4.3, r.ppmin_away / ppm * 4.3, r.home_pp_off / ppo, r.away_pk_def / pkd)
        app, ash = team_pp_shares(r.ppmin_away / ppm * 4.3, r.ppmin_home / ppm * 4.3, r.away_pp_off / ppo, r.home_pk_def / pkd)
        for tid, p_pp, p_sh in ((hid, hpp, hsh), (aid, app, ash)):
            ppl = dressed(data, gid, tid)
            rb = build_roster(book, tid, str(tid), di, ppl, None, p_pp, p_sh, production_team_minutes(p_pp), season=season)
            sec_pp = float(ts.loc[(gid, tid), "sec_pp"]) if (gid, tid) in ts.index else np.nan
            for p in ppl:
                m = rb.player_meta[int(p["player_id"])]
                rows.append({"game_id": gid, "team_id": tid, "player_id": int(p["player_id"]), "pos": rb.profiles[int(p["player_id"])].pos,
                             "e_toi": m["expected_toi_total_min"], "e_toi_ev": m["expected_toi_min"]["ev"], "e_toi_pp": m["expected_toi_min"]["pp"],
                             "e_toi_sh": m["expected_toi_min"]["sh"], "e_share_pp": m["share"]["pp"], "e_sog": m["expected_sog"], "team_sec_pp": sec_pp})
    out = pd.DataFrame(rows)
    act = pl[["game_id", "player_id", "toi_s", "toi_ev_s", "toi_pp_s", "toi_sh_s", "sog", "shifts_ok"]]
    out = out.merge(act, on=["game_id", "player_id"], how="left")
    otg = data.team_states[data.team_states["game_type"] == 2].groupby("game_id")["n_seconds"].max()
    out["ot_game"] = out["game_id"].map(otg).fillna(3600).gt(3600)
    return out


# ---------------------------------------------------------------------------------------------------------------------
# metrics
# ---------------------------------------------------------------------------------------------------------------------
def _boot(game_ids: np.ndarray, x: np.ndarray, n_boot: int = 2000) -> list[float]:
    _, inv = np.unique(game_ids, return_inverse=True)
    s = np.bincount(inv, weights=x)
    n = np.bincount(inv)
    rng = np.random.default_rng(SEED)
    G = len(n)
    bs = np.empty(n_boot)
    for i in range(n_boot):
        j = rng.integers(0, G, G)
        bs[i] = s[j].sum() / n[j].sum()
    return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def paired(game_ids: np.ndarray, before: np.ndarray, after: np.ndarray, y: np.ndarray, kind: str) -> dict[str, Any]:
    """Before / after of one prediction column against outcome ``y``: MAE, RMSE, bias (or Brier for kind='prob'), and
    the after-minus-before difference of the per-row loss with a game-clustered 95% CI."""
    b, a, y = (np.asarray(v, float) for v in (before, after, y))
    ok = np.isfinite(b) & np.isfinite(a) & np.isfinite(y)
    b, a, y, g = b[ok], a[ok], y[ok], np.asarray(game_ids)[ok]
    if kind == "prob":
        lb, la = (b - y) ** 2, (a - y) ** 2
        res = {"brier_before": float(lb.mean()), "brier_after": float(la.mean()), "mean_pred_before": float(b.mean()), "mean_pred_after": float(a.mean()),
               "base_rate": float(y.mean())}
        d = la - lb
        res["brier_diff"] = float(d.mean())
        res["brier_diff_ci95"] = _boot(g, d)
    else:
        eb, ea = b - y, a - y
        res = {"mae_before": float(np.abs(eb).mean()), "mae_after": float(np.abs(ea).mean()), "rmse_before": float(np.sqrt((eb**2).mean())),
               "rmse_after": float(np.sqrt((ea**2).mean())), "bias_before": float(eb.mean()), "bias_after": float(ea.mean())}
        d = np.abs(ea) - np.abs(eb)
        res["mae_diff"] = float(d.mean())
        res["mae_diff_ci95"] = _boot(g, d)
        d2 = ea**2 - eb**2
        res["mse_diff"] = float(d2.mean())
        res["mse_diff_ci95"] = _boot(g, d2)
    res["n"] = int(ok.sum())
    res["n_games"] = int(len(np.unique(g)))
    return res


def score_production(b: pd.DataFrame, a: pd.DataFrame, ts_new: pd.DataFrame) -> dict[str, Any]:
    m = b.merge(a, on=["game_id", "team_id", "player_id"], suffixes=("_b", "_a"))
    m = m[m["shifts_ok_b"].fillna(False).astype(bool)]
    # actual PP share against the CORRECTED team seconds (the fixed timeline is the truth for both arms)
    sec = ts_new.set_index(["game_id", "team_id"])["sec_pp"]
    m["y_share_pp"] = m["toi_pp_s_b"] / m.set_index(["game_id", "team_id"]).index.map(sec).to_numpy().astype(float)
    g = m["game_id"].to_numpy()
    out: dict[str, Any] = {}
    for name, col, y in (("toi_total_min", "e_toi", m["toi_s_b"] / 60.0), ("toi_ev_min", "e_toi_ev", m["toi_ev_s_b"] / 60.0),
                         ("toi_pp_min", "e_toi_pp", m["toi_pp_s_b"] / 60.0), ("toi_sh_min", "e_toi_sh", m["toi_sh_s_b"] / 60.0),
                         ("sog", "e_sog", m["sog_b"].astype(float))):
        out[name] = paired(g, m[f"{col}_b"], m[f"{col}_a"], y, "num")
    pp = m[np.isfinite(m["y_share_pp"]) & (m["team_sec_pp_a"] > 0)]
    out["pp_share"] = paired(pp["game_id"].to_numpy(), pp["e_share_pp_b"], pp["e_share_pp_a"], pp["y_share_pp"], "num")
    for flag in (True, False):
        k = m["ot_game_b"] == flag
        out["ot_games" if flag else "regulation_games"] = {nm: paired(g[k.to_numpy()], m.loc[k, f"{c}_b"], m.loc[k, f"{c}_a"], yy[k], "num")
                                                            for nm, c, yy in (("toi_total_min", "e_toi", m["toi_s_b"] / 60.0), ("toi_pp_min", "e_toi_pp", m["toi_pp_s_b"] / 60.0),
                                                                              ("sog", "e_sog", m["sog_b"].astype(float)))}
    return out


def score_walk_forward(skb: pd.DataFrame, ska: pd.DataFrame, glb: pd.DataFrame, gla: pd.DataFrame) -> dict[str, Any]:
    m = skb.merge(ska, on=["game_id", "player_id"], suffixes=("_b", "_a"))
    g = m["game_id"].to_numpy()
    out: dict[str, Any] = {}
    for p, y in (("p_g1", m["y_g_b"] >= 1), ("p_a1", m["y_a_b"] >= 1), ("p_p1", m["y_p_b"] >= 1), ("p_p2", m["y_p_b"] >= 2)):
        out[p] = paired(g, m[f"{p}_b"], m[f"{p}_a"], y.astype(float), "prob")
    out["exp_toi_walk_forward_template"] = paired(g, m["exp_toi_b"], m["exp_toi_a"], m["toi_s_b"] / 60.0, "num")
    gm = glb.merge(gla, on=["game_id", "player_id"], suffixes=("_b", "_a"))
    out["saves_mean"] = paired(gm["game_id"].to_numpy(), gm["e_saves_b"], gm["e_saves_a"], gm["y_saves_b"], "num")
    out["saves_identical"] = bool(np.allclose(gm["e_saves_b"], gm["e_saves_a"]))
    lad = [f"p_s{t}" for t in range(14, 41)]
    yb = np.column_stack([(gm["y_saves_b"] >= t).astype(float) for t in range(14, 41)])
    lb = ((gm[[c + "_b" for c in lad]].to_numpy() - yb) ** 2).mean(axis=1)
    la = ((gm[[c + "_a" for c in lad]].to_numpy() - yb) ** 2).mean(axis=1)
    out["saves_ladder_brier"] = {"before": float(lb.mean()), "after": float(la.mean()), "diff": float((la - lb).mean()),
                                 "diff_ci95": _boot(gm["game_id"].to_numpy(), la - lb), "n": int(len(gm))}
    return out


# ---------------------------------------------------------------------------------------------------------------------
# 3. deployed parameters
# ---------------------------------------------------------------------------------------------------------------------
def _flat(d: Any, pre: str = "") -> dict[str, Any]:
    if isinstance(d, dict):
        out: dict[str, Any] = {}
        for k, v in d.items():
            out |= _flat(v, f"{pre}.{k}" if pre else str(k))
        return out
    if isinstance(d, list):
        return {pre: json.dumps(d)}
    return {pre: d}


def params_diff(old: Path, new: Path) -> dict[str, Any]:
    """Refit ``players.fit.fit_all`` on both histories (in memory) and list every parameter that moves."""
    from nhl_edge.players.fit import fit_all

    a, b = _flat(fit_all(old)), _flat(fit_all(new))
    changed = {}
    for k in sorted(set(a) | set(b)):
        va, vb = a.get(k), b.get(k)
        if isinstance(va, float) and isinstance(vb, float):
            if abs(va - vb) > 1e-12 * max(1.0, abs(va)):
                changed[k] = {"old": va, "new": vb, "rel_change": (vb - va) / va if va else None}
        elif va != vb:
            changed[k] = {"old": va, "new": vb}
    return {"n_parameters": len(a), "n_changed": len(changed), "changed": changed,
            "note": "computed in memory; data/params/player-sim-1.0.json is NOT regenerated (needs an explicit owner decision)"}


def _round(o: Any) -> Any:
    if isinstance(o, float):
        return round(o, 6)
    if isinstance(o, dict):
        return {str(k): _round(v) for k, v in o.items()}
    if isinstance(o, list | tuple):
        return [_round(v) for v in o]
    if isinstance(o, np.generic):
        return _round(o.item())
    return o


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.ot_timeline_effect")
    ap.add_argument("--old", default="data/history")
    ap.add_argument("--new", default=None)
    ap.add_argument("--wf-games", default=WF_GAMES)
    ap.add_argument("--seasons", default="2024,2025")
    ap.add_argument("--n-sims", type=int, default=4000)
    ap.add_argument("--part", choices=["tables", "production", "walk_forward", "params", "all"], default="all")
    ap.add_argument("--out", default="docs/research/ot_timeline_fix")
    ap.add_argument("--cache", default="out/ot_timeline_cache", help="per-arm walk-forward outputs (parquet), reused when present")
    ap.add_argument("--only-old", action="store_true", help="only build the cached BEFORE walk-forward (no --new needed yet)")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    seasons = [int(s) for s in a.seasons.split(",")]
    wf = pd.read_csv(a.wf_games)
    t0 = time.time()
    cache = Path(a.cache)
    cache.mkdir(parents=True, exist_ok=True)

    def wf_cached(tag: str, data: Data, season: int) -> tuple[pd.DataFrame, pd.DataFrame]:
        fs, fg = cache / f"{tag}_sk_{season}.parquet", cache / f"{tag}_gl_{season}.parquet"
        if not (fs.exists() and fg.exists()):
            sk, gl = simulate(data, wf, season, a.n_sims, progress_every=0)
            sk.to_parquet(fs, index=False)
            gl.to_parquet(fg, index=False)
        return pd.read_parquet(fs), pd.read_parquet(fg)

    if a.only_old:
        d_old = Data(Path(a.old), SEASONS_ALL)
        for s in seasons:
            wf_cached("old", d_old, s)
            print(f"old walk-forward {s} cached {time.time() - t0:.0f}s", flush=True)
        return 0
    if a.new is None:
        raise SystemExit("--new is required")
    old, new = Path(a.old), Path(a.new)
    if a.part in ("tables", "all"):
        (out / "tables.json").write_text(json.dumps(_round(compare_tables(old, new, SEASONS_ALL)), indent=1))
    if a.part in ("production", "walk_forward", "all"):
        d_old, d_new = Data(old, SEASONS_ALL), Data(new, SEASONS_ALL)
        for s in seasons:
            if a.part in ("production", "all"):
                rep = score_production(production_rows(d_old, wf, s), production_rows(d_new, wf, s), d_new.team_states)
                (out / f"production_{s}.json").write_text(json.dumps(_round(rep), indent=1))
                print(f"production {s} done {time.time() - t0:.0f}s", flush=True)
            if a.part in ("walk_forward", "all"):
                skb, glb = wf_cached("old", d_old, s)
                ska, gla = wf_cached("new", d_new, s)
                (out / f"walk_forward_{s}.json").write_text(json.dumps(_round(score_walk_forward(skb, ska, glb, gla)), indent=1))
                print(f"walk-forward {s} done {time.time() - t0:.0f}s", flush=True)
    if a.part in ("params", "all"):
        (out / "params_diff.json").write_text(json.dumps(_round(params_diff(old, new)), indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
