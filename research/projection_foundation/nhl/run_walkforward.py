"""NHL Projection Foundation walk-forward evaluation.

    cd research/projection_foundation && python -m nhl.run_walkforward [--rebuild]

Writes
  results/summary.json            sift.projection_foundation.sport_summary.v1 (CONTRACT.md)
  results/nhl_full_results.json   every table behind RESULTS_NHL.md
  results/experiments/*.json      immutable experiment records (pf_core.registry)

Split discipline: parameters fitted on development (2021-22, 2022-23); model / distribution
selection on validation (2023-24); holdout (2024-25, 2025-26) scored once for frozen candidates;
2026-27-to-date is a prospective check against the archived PLAYER_SIM_V1 forecasts.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

PF = Path(__file__).resolve().parents[1]
if str(PF) not in sys.path:
    sys.path.insert(0, str(PF))

from pf_core import VERSION as PF_VERSION  # noqa: E402
from pf_core import gate, metrics, registry  # noqa: E402

from nhl import SPLIT_LABELS, SPLITS, VERSION, data, incumbent, inventory, opportunity, pipeline, xg  # noqa: E402
from nhl import evaluate as ev  # noqa: E402

RES = PF / "results"
EXP = RES / "experiments"
MODELS = ["A", "B", "C", "D", "E", "F"]
MODEL_NAMES = {"A": "A_season_avg_shrunk", "B": "B_ewma_shrunk", "C": "C_toi_x_rate", "D": "D_opp_adjusted",
               "E": "E_lightgbm", "F": "F_stack"}
SKATER_FAMS = {"sog": "shots", "goals": "goals", "assists": "assists", "points": "points"}
SPLIT_SEASONS = {"development": [2022], "validation": [2023], "holdout": [2024, 2025], "prospective": [2026]}
INC_RUNGS = {"goals": [1, 2, 3], "assists": [1, 2], "points": [1, 2, 3]}
T0 = time.time()


def sha() -> str:
    try:
        return subprocess.check_output(["git", "-C", str(PF), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items() if not str(k).startswith("_")}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else round(float(o), 6)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


# =========================================================================== generic family evaluation
def eval_family(df: pd.DataFrame, fam: str, stat: str, pop: pd.Series, dev_fit: pd.Series, family_key: str,
                inc_frames: dict | None = None, rung_fn=None, records=None) -> dict:
    """df has columns stat, mu_<stat>_<M>; pop = evaluation population mask; dev_fit = rows for fitting
    dispersion. Returns dict with model rows by split, dist comparison, calibration, chosen model."""
    out = {"family": family_key, "models": [], "dist": {}, "calibration": {}, "zero_mass": {}, "incumbent": {}}
    cols = {m: f"mu_{stat}_{m}" for m in MODELS if f"mu_{stat}_{m}" in df}
    dparams = {}
    for m, c in cols.items():
        ok = dev_fit & df[c].notna()
        dparams[m] = ev.fit_dist("nb_binned", df.loc[ok, stat], df.loc[ok, c], fam)
    out["dist_params"] = {m: {k: v for k, v in p.items() if k != "samples"} for m, p in dparams.items()}
    crps_store = {}
    for split, seasons in SPLIT_SEASONS.items():
        mask = pop & df["season"].isin(seasons) & df[list(cols.values())].notna().all(axis=1)
        d = df[mask]
        if len(d) < 50:
            continue
        y = d[stat].to_numpy(float)
        cl = d["game_id"].to_numpy()
        _, crps_a = ev.score(y, d[cols["A"]], dparams["A"], fam)
        for m, c in cols.items():
            row, crps = ev.model_row(MODEL_NAMES[m], split, y, d[c], dparams[m], fam, cl,
                                     crps_base=None if m == "A" else crps_a)
            row["thresholds"] = row.pop("_thresholds")
            row["zero_mass_pred_obs"] = row.pop("_zero")
            out["models"].append(row)
            crps_store[(split, m)] = (d.index, crps)
    # choose on validation by CRPS
    val = [r for r in out["models"] if r["split"] == "validation"]
    best = min(val, key=lambda r: r["crps"])["model"]
    bm = [k for k, v in MODEL_NAMES.items() if v == best][0]
    out["best_model"] = best
    out["best_key"] = bm
    for r in out["models"]:
        r["verdict"] = ("baseline" if r["model"] == MODEL_NAMES["A"] else
                        "best" if r["model"] == best else
                        "competitive" if (r["split"] == "validation" and r["crps"] <= min(v["crps"] for v in val) * 1.002)
                        else "rejected")
    # distributions for the selected mean (validation + holdout)
    c = cols[bm]
    ok = dev_fit & df[c].notna()
    kinds = ["poisson", "nb", "nb_binned"] + (["normal_binned"] if fam in ("saves",) else [])
    for split in ("validation", "holdout"):
        mask = pop & df["season"].isin(SPLIT_SEASONS[split]) & df[c].notna()
        d = df[mask]
        y = d[stat].to_numpy(float)
        res = {}
        for k in kinds:
            p = ev.fit_dist(k, df.loc[ok, stat], df.loc[ok, c], fam) if k != "normal_binned" else \
                {**__import__("pf_core").models.fit_dist_params("normal_binned", df.loc[ok, stat], df.loc[ok, c],
                                                                 K=ev.SUPPORT_K[fam], lo=0, floor_at=0), "K": ev.SUPPORT_K[fam]}
            m_, crps = ev.score(y, d[c], p, fam)
            res[k] = {"crps": m_["crps"], "log_score": m_["log_score"], "cover_50": m_["cover_50"],
                      "cover_80": m_["cover_80"], "cover_90": m_["cover_90"], "pit_var_ratio": m_["pit_var_ratio"],
                      "pit_deciles": m_["pit_deciles"], "zero_mass_pred": m_["zero_mass_pred"],
                      "zero_mass_obs": m_["zero_mass_obs"], "thresholds": m_.get("thresholds", {}),
                      "alpha": p.get("alpha")}
        out["dist"][split] = res
        # calibration of the rungs (selected nb_binned)
        dd = ev.make(dparams[bm], d[c])
        out["calibration"][split] = [ev.calib_threshold(dd, y, k) for k in ev.THRESHOLDS.get(fam, [])]
        # zero mass by predicted-mean decile
        if fam in ("goals", "assists", "points"):
            q = pd.qcut(d[c], 5, duplicates="drop")
            z = pd.DataFrame({"q": q, "p0": dd.P[:, 0], "o0": (y == 0)}).groupby("q", observed=True).agg(
                n=("p0", "size"), p0_pred=("p0", "mean"), p0_obs=("o0", "mean"))
            out["zero_mass"][split] = [{"mu_bin": str(i), **{k: float(v) for k, v in r.items()}} for i, r in z.iterrows()]
    out["_dparams"] = dparams
    out["_cols"] = cols
    return out


def incumbent_compare(df, stat, fam, mu_col, dparam, inc: pd.DataFrame, label: str, rungs) -> dict | None:
    if inc is None or inc.empty:
        return None
    d = df.merge(inc, on=["game_id", "player_id"] if "player_id" in inc else ["game_id", "team_id"], how="inner")
    inc_mu = f"inc_{stat}" if f"inc_{stat}" in d else None
    d = d[d[mu_col].notna()]
    if inc_mu:
        d = d[d[inc_mu].notna()]
    if len(d) < 30:
        return None
    y = d[stat].to_numpy(float)
    cl = d["game_id"].to_numpy()
    out = {"source": label, "n_obs": int(len(d)), "n_clusters": int(d["game_id"].nunique())}
    if inc_mu:
        out["ours"] = metrics.point_metrics(y, d[mu_col])
        out["incumbent"] = metrics.point_metrics(y, d[inc_mu])
        out["sq_error_diff"] = ev.compare(ev.sq(y, d[mu_col]), ev.sq(y, d[inc_mu]), cl)
        out["abs_error_diff"] = ev.compare(np.abs(d[mu_col] - y), np.abs(d[inc_mu] - y), cl)
    rk = [k for k in rungs if f"inc_p_{fam}_{k}" in d and d[f"inc_p_{fam}_{k}"].notna().mean() > 0.95]
    if rk:
        dd = d[d[[f"inc_p_{fam}_{k}" for k in rk]].notna().all(axis=1)]
        y2 = dd[stat].to_numpy(float)
        ours = ev.make(dparam, dd[mu_col])
        po = {k: ours.prob_ge(k) for k in rk}
        pi = {k: dd[f"inc_p_{fam}_{k}"].to_numpy(float) for k in rk}
        r_o, r_i = incumbent.rps(po, y2, rk), incumbent.rps(pi, y2, rk)
        out["rps_rungs"] = rk
        out["rps_ours"], out["rps_incumbent"] = float(r_o.mean()), float(r_i.mean())
        out["rps_diff"] = ev.compare(r_o, r_i, dd["game_id"].to_numpy())
        out["brier"] = {str(k): {"ours": float(np.mean((po[k] - (y2 >= k)) ** 2)),
                                 "incumbent": float(np.mean((pi[k] - (y2 >= k)) ** 2)),
                                 "diff": ev.compare((po[k] - (y2 >= k)) ** 2, (pi[k] - (y2 >= k)) ** 2,
                                                    dd["game_id"].to_numpy()),
                                 "hit_rate": float((y2 >= k).mean())} for k in rk}
    if fam == "sog" and inc_mu:
        # PLAYER_SIM_V1 publishes only the expected SOG; score it as Poisson (production champion convention)
        from pf_core import dists
        dp = dists.poisson(d[inc_mu].to_numpy(float), 20)
        do = ev.make(dparam, d[mu_col])
        out["crps_ours"], out["crps_incumbent_poisson"] = float(do.crps(y).mean()), float(dp.crps(y).mean())
        out["crps_diff"] = ev.compare(do.crps(y), dp.crps(y), cl)
    return out


# =========================================================================== gate
def run_gate(df, stat, gfam, mu_col, dparam, split_mask, opp_games, k_rungs) -> dict:
    d = df[split_mask & df[mu_col].notna()].copy()
    if d.empty:
        return {}
    dist = ev.make(dparam, d[mu_col])
    statuses, checks = [], []
    th_list = k_rungs
    toi_hist = d[[f"toi_lag{i}" for i in range(1, 11)]].to_numpy()
    st_hist = d[[f"{stat}_lag{i}" for i in range(1, 11)]].to_numpy()
    for i, r in enumerate(d.itertuples(index=False)):
        gd = pd.Timestamp(r.game_date)
        gi = gate.GateInput(
            sport="NHL", family=gfam, entity_id=str(r.player_id), entity_name=None, team=str(r.team_id),
            game_id=str(r.game_id), game_start_utc=(gd + pd.Timedelta(hours=23)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            mean=float(getattr(r, mu_col)),
            data_asof_utc=(gd - pd.Timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            expected_opportunity=float(r.toi_E),
            opportunity_history=[x for x in toi_hist[i][::-1] if np.isfinite(x)],
            stat_history=[x for x in st_hist[i][::-1] if np.isfinite(x)],
            opponent_sample_games=int(opp_games[i]) if np.isfinite(opp_games[i]) else None,
            opponent_factor=float(getattr(r, f"oppadj_{stat}")) if np.isfinite(getattr(r, f"oppadj_{stat}")) else None,
            support_lo=0, probs=dist.P[i].tolist(),
            thresholds={str(k): float(dist.prob_ge(k)[i]) if False else float(1 - dist.cdf_matrix[i, k - 1]) for k in th_list},
            model_n_obs=int(r.toi_n))
        res = gate.evaluate(gi, now_utc=(gd + pd.Timedelta(hours=22)).strftime("%Y-%m-%dT%H:%M:%SZ"))
        statuses.append(res["status"])
        checks.append(res)
    d["status"] = statuses
    y = d[stat].to_numpy(float)
    d["crps"] = dist.crps(y)
    d["ae"] = np.abs(d[mu_col] - d[stat])
    by = d.groupby("status").agg(n=("crps", "size"), crps=("crps", "mean"), mae=("ae", "mean"),
                                 bias=(mu_col, lambda s: float((s - d.loc[s.index, stat]).mean())))
    summ = gate.summarize(checks)
    summ["status_rates"] = {k: v / summ["n"] for k, v in summ["status_counts"].items()}
    return {"summary": summ, "error_by_status": by.reset_index().to_dict("records")}


def add_lags(df, cols, n=10):
    df = df.sort_values(["player_id", "game_date", "game_id"]).reset_index(drop=True)
    g = df.groupby("player_id", sort=False)
    new = {f"{c}_lag{i}": g[c].shift(i) for c in cols for i in range(1, n + 1)}
    return pd.concat([df, pd.DataFrame(new)], axis=1)


# =========================================================================== root cause
def root_cause(sk, stat, fam, mu_col, dparam, tg) -> dict:
    """Largest recurring errors: quantify on development + validation, test PIT fixes (dev fit, validation test)."""
    m = tg[["game_id", "team_id", "goals_for", "goals_against", "ot"]].copy()
    m["margin"] = m["goals_for"] - m["goals_against"]
    d = sk.merge(m[["game_id", "team_id", "margin", "ot"]], on=["game_id", "team_id"], how="left")
    d = d[(d["toi_n"] >= 1) & d[mu_col].notna() & d["season"].isin([2022, 2023])].copy()
    d["err"] = d[mu_col] - d[stat]
    d["toi_err"] = d["toi_E"] - d["toi"]
    segs = {
        "line_changed_vs_last_game (post-game)": d["line_changed_now"] == 1,
        "pp_unit_changed (post-game)": (d["pp_unit_now"] != d["pp_unit_last"]) & d["pp_unit_last"].notna(),
        "returning_from_absence>=1 team game (PIT)": d["missed_games"].fillna(0) >= 1,
        "new_team (PIT)": d["new_team"] == 1,
        "team_back_to_back (PIT)": d["b2b"] == 1,
        "blowout |margin|>=3 (post-game)": d["margin"].abs() >= 3,
        "overtime game (post-game)": d["ot"].astype(bool),
        "toi_miss>3min (post-game)": d["toi_err"].abs() > 3,
        "early season <=10 player games (PIT)": d["toi_n"] <= 10,
    }
    tot_se = float((d["err"] ** 2).sum())
    rows = []
    for k, s in segs.items():
        s = s.fillna(False).to_numpy(bool)
        if s.sum() < 50:
            continue
        rows.append({"pattern": k, "n": int(s.sum()), "share_rows": float(s.mean()), "bias": float(d.loc[s, "err"].mean()),
                     "mae": float(d.loc[s, "err"].abs().mean()), "mae_rest": float(d.loc[~s, "err"].abs().mean()),
                     "share_sq_error": float((d.loc[s, "err"] ** 2).sum() / tot_se),
                     "toi_bias": float(d.loc[s, "toi_err"].mean())})
    # oracle decomposition: replace projected TOI by the actual TOI (rates unchanged)
    v = d[d["season"] == 2023]
    oracle = v["toi_np"].fillna(v["toi"] - v["toi_pp_E"]) * v[f"rate_np_{stat}"] + v["toi_pp"].fillna(v["toi_pp_E"]) * v[f"rate_pp_{stat}"]
    base_c = v[f"mu_{stat}_C"]
    decomp = {"split": "validation", "mse_C": float(((base_c - v[stat]) ** 2).mean()),
              "mse_C_actual_toi": float(((oracle - v[stat]) ** 2).mean()),
              "mse_best": float(((v[mu_col] - v[stat]) ** 2).mean()),
              "poisson_floor_mse": float(v[stat].mean()),
              "note": "mse_C_actual_toi uses the realised TOI (retrospective oracle); the gap to mse_C is the share "
                      "of error attributable to opportunity misprojection; Poisson floor = irreducible count noise if "
                      "the mean were known exactly."}
    # PIT fixes: multiplicative factor fitted on development rows of the segment, tested on validation
    from pf_core import models as M
    fixes = []
    for name, s in (("b2b", d["b2b"] == 1), ("returning_from_absence", d["missed_games"].fillna(0) >= 1),
                    ("new_team", d["new_team"] == 1), ("early_season", d["toi_n"] <= 10),
                    ("line_changed_last_game_PIT", d["line_changed_pit"] == 1)):
        s = s.fillna(False).to_numpy(bool)
        dev = (d["season"] == 2022).to_numpy() & s
        val = (d["season"] == 2023).to_numpy()
        if dev.sum() < 200:
            continue
        f = M.fit_calibration_scale(d.loc[dev, stat], d.loc[dev, mu_col])
        mu_fix = np.where(s, d[mu_col] * f, d[mu_col])
        y = d.loc[val, stat].to_numpy(float)
        c0 = ev.make(dparam, d.loc[val, mu_col]).crps(y)
        c1 = ev.make(dparam, mu_fix[val]).crps(y)
        cmp = ev.compare(c1, c0, d.loc[val, "game_id"].to_numpy())
        segv = s[val]
        cmp_seg = ev.compare(c1[segv], c0[segv], d.loc[val, "game_id"].to_numpy()[segv]) if segv.sum() > 50 else None
        fixes.append({"fix": name, "factor_dev": f, "n_dev": int(dev.sum()), "n_val_segment": int(segv.sum()),
                      "val_crps_diff_all": cmp, "val_crps_diff_segment": cmp_seg,
                      "adopt": bool(cmp["ci95"][1] < 0)})
    return {"segments": rows, "toi_oracle_decomposition": decomp, "fixes": fixes}


# =========================================================================== main
def main(rebuild=False):
    RES.mkdir(parents=True, exist_ok=True)
    EXP.mkdir(parents=True, exist_ok=True)
    full = {"version": VERSION, "splits": SPLIT_LABELS}
    print("stage1..3", flush=True)
    sk, p1 = pipeline.stage1(rebuild=rebuild)
    del sk
    sk, p2 = pipeline.stage2(rebuild=rebuild)
    gf, tg, p3 = pipeline.stage3(rebuild=rebuild)
    full["params"] = {"stage1": p1, "stage2": p2, "stage3": p3}
    print(f"[{time.time()-T0:.0f}s] predictions loaded", flush=True)

    # ---------------------------------------------------------------- inventory
    full["inventory"] = inventory.matrix()
    full["starter_accuracy"] = inventory.starter_accuracy()
    full["lineup_accuracy"] = inventory.lineup_accuracy()
    _, full["xg"] = xg.fit_and_score()

    # ---------------------------------------------------------------- incumbents
    inc_sk_pro, inc_gl_pro = incumbent.prospective()
    inc_sk_wf = incumbent.walkforward_skaters()
    inc_gl_wf = incumbent.walkforward_goalies()
    inc_tg_wf = incumbent.walkforward_team()

    pop = sk["toi_n"] >= 1
    dev_fit = sk["season"].isin(SPLITS["development"]) & pop

    # ---------------------------------------------------------------- opportunity (TOI)
    opp = {"models": {}, "by_role": {}, "incumbent": {}}
    for split, seasons in SPLIT_SEASONS.items():
        opp["models"][split] = opportunity.toi_eval(sk, pop & sk["season"].isin(seasons))
    for split in ("validation", "holdout"):
        msk = pop & sk["season"].isin(SPLIT_SEASONS[split])
        opp["by_role"][split] = {
            "toi_E_by_role": opportunity.toi_by_role(sk, msk, "toi_E", "toi", "role"),
            "toi_B_by_role": opportunity.toi_by_role(sk, msk, "toi_B", "toi", "role"),
            "toi_pp_E_by_pp_role": opportunity.toi_by_role(sk, msk, "toi_pp_E", "toi_pp", "pp_role"),
        }
    for label, inc, seasons in (("PLAYER_SIM_V1 walk-forward 2025-26", inc_sk_wf, [2025]),
                                ("PLAYER_SIM_V1 prospective archive 2026-27", inc_sk_pro, [2026])):
        if inc.empty:
            continue
        d = sk[pop & sk["season"].isin(seasons)].merge(inc, on=["game_id", "player_id"])
        d = d[d["inc_toi"].notna()]
        r = {"n_obs": int(len(d)), "n_clusters": int(d["game_id"].nunique())}
        for tgt, ours, theirs in (("toi", "toi_E", "inc_toi"), ("toi_pp", "toi_pp_E", "inc_toi_pp")):
            dd = d[d[tgt].notna() & d[theirs].notna()]
            r[tgt] = {"ours": metrics.point_metrics(dd[tgt], dd[ours]), "incumbent": metrics.point_metrics(dd[tgt], dd[theirs]),
                      "abs_error_diff": ev.compare(np.abs(dd[ours] - dd[tgt]), np.abs(dd[theirs] - dd[tgt]), dd["game_id"])}
        opp["incumbent"][label] = r
    opp["workload_v1_published_2025"] = {"toi_mae": 1.875, "toi_rmse": 2.484, "toi_bias": -0.008,
                                         "pp_mae": 0.795, "pp_rmse": 1.168, "source": "docs/research/WORKLOAD_V1_RESULTS.md"}
    full["opportunity"] = opp
    print(f"[{time.time()-T0:.0f}s] opportunity done", flush=True)

    # ---------------------------------------------------------------- skater families
    tf = pd.read_parquet(data.CACHE / "stage3_team.parquet") if (data.CACHE / "stage3_team.parquet").exists() else tg
    fams = {}
    for stat, fam_key in SKATER_FAMS.items():
        r = eval_family(sk, stat, stat, pop, dev_fit, fam_key)
        bm = r["best_key"]
        col = r["_cols"][bm]
        dp = r["_dparams"][bm]
        # incumbent comparisons (paired, one row per player-game)
        r["incumbent"]["holdout"] = incumbent_compare(sk[pop & (sk["season"] == 2025)], stat, stat, col, dp, inc_sk_wf,
                                                      "PLAYER_SIM_V1 walk-forward 2025-26", INC_RUNGS.get(stat, []))
        r["incumbent"]["prospective"] = incumbent_compare(sk[pop & (sk["season"] == 2026)], stat, stat, col, dp, inc_sk_pro,
                                                          "PLAYER_SIM_V1 prospective archive 2026-27", INC_RUNGS.get(stat, []))
        # also baseline-vs-incumbent so the reader can see the incumbent against model A
        r["incumbent"]["holdout_A"] = incumbent_compare(sk[pop & (sk["season"] == 2025)], stat, stat, r["_cols"]["A"],
                                                        r["_dparams"]["A"], inc_sk_wf, "A vs PLAYER_SIM_V1 walk-forward",
                                                        INC_RUNGS.get(stat, []))
        r["root_cause"] = root_cause(sk, stat, stat, col, dp, tf)
        fams[stat] = r
        print(f"[{time.time()-T0:.0f}s] family {stat} best={r['best_model']}", flush=True)

    # ---------------------------------------------------------------- goalie saves
    gpop = gf["saves_n"].fillna(0) >= 1
    gdev = gf["season"].isin(SPLITS["development"]) & gpop
    gr = eval_family(gf, "saves", "saves", gpop, gdev, "saves")
    gcol, gdp = gr["_cols"][gr["best_key"]], gr["_dparams"][gr["best_key"]]
    gr["incumbent"]["holdout"] = incumbent_compare(gf[gpop & gf["season"].isin([2024, 2025])], "saves", "saves", gcol, gdp,
                                                   inc_gl_wf, "PLAYER_SIM_V1 walk-forward 2024-25 + 2025-26",
                                                   list(range(14, 41)))
    gr["incumbent"]["prospective"] = incumbent_compare(gf[gpop & (gf["season"] == 2026)], "saves", "saves", gcol, gdp,
                                                       inc_gl_pro, "PLAYER_SIM_V1 prospective archive 2026-27", [])
    # pulled starters and starter conditioning
    d = gf[gpop & gf["season"].isin([2023])]
    e = (d[gcol] - d["saves"])
    pulled = d["toi"] < 55
    gr["pulled_starters"] = {"split": "validation", "share": float(pulled.mean()), "bias_pulled": float(e[pulled].mean()),
                             "bias_full": float(e[~pulled].mean()),
                             "share_sq_error": float((e[pulled] ** 2).sum() / (e ** 2).sum())}
    full["saves_sa_decomposition"] = {
        "validation_mse_saves": float((e ** 2).mean()),
        "mse_if_shots_known": float(((d["shots_against"] * d["sv_hat"] - d["saves"]) ** 2).mean()),
        "note": "replacing projected shots-against by the realised number (oracle) shows how much saves error is volume"}
    fams["saves"] = gr
    print(f"[{time.time()-T0:.0f}s] saves best={gr['best_model']}", flush=True)

    # ---------------------------------------------------------------- team goals
    tpop = tg["goals_for_n"].fillna(0) >= 1
    tdev = tg["season"].isin(SPLITS["development"]) & tpop
    tr = eval_family(tg, "team_goals", "tg", tpop, tdev, "team_goals")
    tcol, tdp = tr["_cols"][tr["best_key"]], tr["_dparams"][tr["best_key"]]
    inc_t = inc_tg_wf.rename(columns={"inc_tg": "inc_tg"})
    tr["incumbent"]["holdout"] = incumbent_compare(tg[tpop & tg["season"].isin([2024, 2025])].assign(player_id=0),
                                                   "tg", "tg", tcol, tdp, inc_t.assign(player_id=0),
                                                   "DATA_ONLY_V2 SIM2_ST walk-forward 2024-25 + 2025-26", [3, 4])
    # game total from the two team means (independent NB convolution) vs actual
    gt = []
    for split, seasons in SPLIT_SEASONS.items():
        x = tg[tpop & tg["season"].isin(seasons) & tg[tcol].notna()]
        h = x[x["is_home"]].merge(x[~x["is_home"]][["game_id", tcol, "tg"]], on="game_id", suffixes=("", "_a"))
        if len(h) < 30:
            continue
        dh, da = ev.make(tdp, h[tcol]), ev.make(tdp, h[f"{tcol}_a"])
        K = dh.P.shape[1] + da.P.shape[1] - 1
        P = np.zeros((len(h), K))
        for j in range(da.P.shape[1]):
            P[:, j:j + dh.P.shape[1]] += dh.P * da.P[:, [j]]
        from pf_core.dists import DistBatch
        dt = DistBatch(0, P)
        yt = (h["tg"] + h["tg_a"]).to_numpy(float)
        mt = metrics.dist_metrics(yt, dt, thresholds=[5, 6, 7])
        pmx = metrics.point_metrics(yt, dt.mean)
        row = {"split": split, "n_games": int(len(h)), "mae": pmx["mae"], "rmse": pmx["rmse"], "bias": pmx["bias"],
               "crps": mt["crps"], "cover_80": mt["cover_80"], "pit_var_ratio": mt["pit_var_ratio"],
               "thresholds": mt.get("thresholds")}
        if split == "holdout" and not inc_tg_wf.empty:
            hi = h.merge(inc_tg_wf.rename(columns={"team_id": "_t"}), left_on=["game_id", "team_id"], right_on=["game_id", "_t"])
            hi = hi.merge(inc_tg_wf.rename(columns={"team_id": "_t2", "inc_tg": "inc_tg_a"})[["game_id", "_t2", "inc_tg_a"]],
                          on="game_id")
            hi = hi[hi["_t2"] != hi["_t"]]
            y2 = (hi["tg"] + hi["tg_a"]).to_numpy(float)
            ours = hi[tcol] + hi[f"{tcol}_a"]
            theirs = hi["inc_tg"] + hi["inc_tg_a"]
            row["vs_incumbent_total_sq_error"] = ev.compare(ev.sq(y2, ours), ev.sq(y2, theirs), hi["game_id"])
            row["incumbent_total"] = metrics.point_metrics(y2, theirs)
        gt.append(row)
    tr["game_total"] = gt
    # coherence: sum of player goal means vs team goal mean
    gcol_sk = fams["goals"]["_cols"][fams["goals"]["best_key"]]
    ps = sk.groupby(["game_id", "team_id"]).agg(player_sum=(gcol_sk, "sum"), season=("season", "first"),
                                                 actual=("goals", "sum")).reset_index()
    ps = ps.merge(tg[["game_id", "team_id", tcol, "tg"]], on=["game_id", "team_id"])
    coh = []
    for split, seasons in SPLIT_SEASONS.items():
        x = ps[ps["season"].isin(seasons) & ps[tcol].notna()]
        recs = [gate.team_reconciliation(a, b, "team goals") for a, b in zip(x["player_sum"], x[tcol])]
        st = pd.Series([r["status"] for r in recs]).value_counts(normalize=True).to_dict()
        coh.append({"split": split, "n_team_games": int(len(x)), "mean_player_sum": float(x["player_sum"].mean()),
                    "mean_team_model": float(x[tcol].mean()), "mean_actual_team_goals": float(x["tg"].mean()),
                    "mean_actual_player_goal_sum": float(x["actual"].mean()),
                    "ratio_mean": float((x["player_sum"] / x[tcol]).mean()),
                    "ratio_p10_p90": [float(np.quantile(x["player_sum"] / x[tcol], 0.1)),
                                      float(np.quantile(x["player_sum"] / x[tcol], 0.9))],
                    "corr_player_sum_vs_team_model": float(np.corrcoef(x["player_sum"], x[tcol])[0, 1]),
                    "reconciliation_status_rates": st})
    tr["coherence"] = coh
    fams["team_goals"] = tr
    print(f"[{time.time()-T0:.0f}s] team goals best={tr['best_model']}", flush=True)

    # ---------------------------------------------------------------- gate on validation / holdout
    lag = add_lags(sk[["player_id", "game_date", "game_id", "toi", "sog", "goals", "assists", "points"]].copy(),
                   ["toi", "sog", "goals", "assists", "points"])
    skg = sk.merge(lag.drop(columns=["game_date", "toi", "sog", "goals", "assists", "points"]), on=["player_id", "game_id"])
    og = tg[["game_id", "team_id", "team_gno"]].rename(columns={"team_id": "opp_id", "team_gno": "opp_gno"})
    skg = skg.merge(og, on=["game_id", "opp_id"], how="left")
    gate_res = {}
    for stat, gfam in (("sog", "shots"), ("points", "points"), ("goals", "goals"), ("assists", "assists")):
        r = fams[stat]
        col, dp = r["_cols"][r["best_key"]], r["_dparams"][r["best_key"]]
        for split, seasons in (("validation", [2023]), ("holdout", [2025])):
            msk = (skg["toi_n"] >= 1) & skg["season"].isin(seasons)
            gate_res[f"{stat}|{split}"] = run_gate(skg, stat, gfam, col, dp, msk, skg.loc[msk, "opp_gno"].to_numpy(float),
                                                   ev.THRESHOLDS[stat])
        print(f"[{time.time()-T0:.0f}s] gate {stat}", flush=True)
    full["gate"] = gate_res
    full["families"] = {k: {kk: vv for kk, vv in v.items() if not kk.startswith("_")} for k, v in fams.items()}
    full["runtime_s"] = time.time() - T0
    json.dump(_clean(full), open(RES / "nhl_full_results.json", "w"), indent=1, default=str)
    print(f"[{time.time()-T0:.0f}s] wrote nhl_full_results.json", flush=True)
    write_records(full)
    return full


def write_records(full):
    """One immutable experiment record per family x model x split (validation, holdout)."""
    n = 0
    for fam, r in full["families"].items():
        feats = full["params"]["stage2"].get(fam, {}).get("features_E", []) if fam in SKATER_FAMS else []
        for row in r["models"]:
            if row["split"] not in ("validation", "holdout"):
                continue
            rec = registry.ExperimentRecord(
                experiment_id=f"nhl_{fam}_{row['model']}_{row['split']}", sport="NHL", family=fam, model=row["model"],
                model_version=VERSION, question=f"How accurate is {row['model']} for NHL {fam}?",
                hypothesis="Each rung of the ladder (A..F) should improve CRPS over the shrunk season average.",
                split=row["split"], train_period="2021-22..2022-23 (scalars); LightGBM refit on all seasons before the scored one",
                eval_period=SPLIT_LABELS[row["split"]], features=feats if row["model"].startswith("E") else [],
                hyperparameters={}, data_provenance=["data/history/players/*.parquet", "data-archive player_events (2026-27)"],
                n_obs=row["n_obs"], n_independent=row["n_obs"], n_clusters=row["n_clusters"],
                point={k: row[k] for k in ("mae", "rmse", "bias")},
                distribution={k: row[k] for k in ("crps", "log_score", "cover_50", "cover_80", "cover_90", "pit_var_ratio")},
                vs_baseline=row.get("vs_baseline") or {}, verdict=row.get("verdict", ""),
                limitations=["conditional on the player dressing / the actual starting goalie"])
            registry.write_record(rec, str(EXP))
            n += 1
    return n


if __name__ == "__main__":
    main(rebuild="--rebuild" in sys.argv)
