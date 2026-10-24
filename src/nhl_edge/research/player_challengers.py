"""Simple, incremental skater-workload challengers: ice time, power-play time and the shots level (RESEARCH_ONLY, development evidence only).

Every challenger is the incumbent's own expectation times ``exp(X b)``: a level term and, one at a time, point-in-time signals found in the diagnosis
(``docs/research/player_diagnosis/RESULTS.md``). Coefficients are fitted on **earlier seasons only** and scored on the later one (2023, 2024, 2025); each stage is
compared with the stage before it and with the incumbent under a game-clustered paired bootstrap, so a signal is only credited for what it adds.

Stages (cumulative):

* ``toi``     (minutes, squared error):  LEVEL -> +ROLL (rolling league level) -> +USAGE (last 3 games vs expectation) -> +ROLE (last 3 vs the 12 before)
* ``toi_pp``  (minutes, squared error):  LEVEL -> +ROLL -> +USAGE (last 5 vs expectation) -> +ROLE (last 3 vs the 12 before) -> +TEAM_ENV (penalty environment)
* ``sog``     (Poisson deviance):        LEVEL -> +ROLL -> +USAGE (recent TOI vs expectation) -> +OPP (opponent shots allowed) -> +LINEMATES (lagged co-ice quality)

**Evidence label.** Every season used here (2022-2025) was already exposed to the earlier workload work, so this is *development* evidence. It selects a frozen
specification; it validates nothing. Validation is the write-once prospective record described in ``docs/research/player_minutes/PREREGISTRATION.md``.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.research import player_diagnosis as PD

TEST_SEASONS = (2023, 2024, 2025)
ROLL_DAYS = 90
ROLL_PRIOR = 2000.0           # pseudo-rows of "the incumbent is right" shrinking the rolling level toward zero

TARGETS: dict[str, dict[str, Any]] = {
    "toi": {"pred": "ch_toi", "act": "y_toi", "loss": "sq", "stages": [("LEVEL", []), ("+ROLL", ["x_roll"]), ("+USAGE", ["x_roll", "x_recent_toi"]), ("+ROLE", ["x_roll", "x_recent_toi", "x_role_toi"])]},
    "toi_pp": {"pred": "ch_toi_pp", "act": "y_toi_pp", "loss": "sq", "needs_shifts": True,
               "stages": [("LEVEL", []), ("+ROLL", ["x_roll"]), ("+USAGE", ["x_roll", "x_recent_pp"]), ("+ROLE", ["x_roll", "x_recent_pp", "x_role_pp"]),
                          ("+TEAM_ENV", ["x_roll", "x_recent_pp", "x_role_pp", "x_drawn", "x_opp_taken"])]},
    "sog": {"pred": "ch_sog", "act": "y_sog", "loss": "poisson",
            "stages": [("LEVEL", []), ("+ROLL", ["x_roll"]), ("+USAGE", ["x_roll", "x_recent_toi"]), ("+OPP", ["x_roll", "x_recent_toi", "x_opp_sa"]),
                       ("+LINEMATES", ["x_roll", "x_recent_toi", "x_opp_sa", "x_linemates"])]},
}


def _day_index(d: pd.DataFrame) -> np.ndarray:
    return (pd.to_datetime(d["date_int"].astype(str), format="%Y%m%d") - pd.Timestamp("2000-01-01")).dt.days.to_numpy()


def rolling_level(d: pd.DataFrame, pred: str, act: str, mask: np.ndarray | None = None) -> np.ndarray:
    """log((actual + shrink) / (expected + shrink)) over ALL skater-games of the previous ``ROLL_DAYS`` days (strictly before the row's date): the league-wide level
    drift a pregame system can see. Rows with no history get 0."""
    m = np.ones(len(d), bool) if mask is None else mask
    day = _day_index(d)
    n_days = int(day.max()) + 2
    a = np.bincount(day[m], weights=d[act].to_numpy(float)[m], minlength=n_days)
    p = np.bincount(day[m], weights=d[pred].to_numpy(float)[m], minlength=n_days)
    ca, cp = np.concatenate([[0], np.cumsum(a)]), np.concatenate([[0], np.cumsum(p)])
    lo = np.clip(day - ROLL_DAYS, 0, n_days)
    hi = np.clip(day, 0, n_days)                              # days [day-90, day-1]
    sa, sp = ca[hi] - ca[lo], cp[hi] - cp[lo]
    mean_p = float(d[pred].to_numpy(float)[m].mean())
    return np.log((sa + ROLL_PRIOR * mean_p) / (sp + ROLL_PRIOR * mean_p))


def role_features(d: pd.DataFrame) -> dict[str, np.ndarray]:
    """Change of role: the last 3 dressed games against the 12 before them (player-level, strictly earlier games)."""
    g = d.groupby("player_id", sort=False)

    def trend(col: str, k0: float) -> np.ndarray:
        last3 = g[col].transform(lambda x: x.shift(1).rolling(3, min_periods=3).mean())
        prev12 = g[col].transform(lambda x: x.shift(4).rolling(12, min_periods=6).mean())
        return np.log((last3 + k0) / (prev12 + k0)).to_numpy(float)
    return {"x_role_toi": trend("y_toi", 1.0), "x_role_pp": trend("y_toi_pp", 0.25)}


def build_features(d: pd.DataFrame, history: Path | None) -> pd.DataFrame:
    d = d.reset_index(drop=True)
    env = PD.shot_environment_features(d)
    use = PD.usage_features(d)
    pen = PD.penalty_features(d)[["game_id", "team_id", "drawn", "opp_taken"]]
    lg = float(pen["drawn"].mean())
    pen = pen.assign(x_drawn=np.log(pen["drawn"] / lg), x_opp_taken=np.log(pen["opp_taken"] / lg))
    f = pd.DataFrame({"x_opp_sa": env["x_opp_sa"], "x_recent_toi": use["x_recent_toi"], "x_recent_pp": use["x_recent_pp"], **role_features(d)})
    f = pd.concat([d[["game_id", "team_id"]], f], axis=1).merge(pen[["game_id", "team_id", "x_drawn", "x_opp_taken"]], on=["game_id", "team_id"], how="left")
    if history is not None:
        f["x_linemates"] = PD.lagged_linemate_feature(d, history)
    else:
        f["x_linemates"] = np.nan
    return f.drop(columns=["game_id", "team_id"])


def fit_predict(d: pd.DataFrame, F: pd.DataFrame, target: str, stage_cols: list[str], test_season: int, roll: np.ndarray, with_train: bool = False) -> Any:
    """Predictions for the rows of ``test_season`` from a model fitted on earlier seasons only (missing signals count as 'no information', i.e. 0)."""
    spec = TARGETS[target]
    season = d["season"].to_numpy()
    pred, y = d[spec["pred"]].to_numpy(float), d[spec["act"]].to_numpy(float)
    ok = d["shifts_ok"].astype(bool).to_numpy() if spec.get("needs_shifts") else np.ones(len(d), bool)
    tr, te = (season < test_season) & ok, (season == test_season) & ok
    cols = [roll if c == "x_roll" else np.nan_to_num(F[c].to_numpy(float)) for c in stage_cols]
    X = np.column_stack([np.ones(len(d)), *cols]) if cols else np.ones((len(d), 1))
    b = PD.fit_scale(pred[tr], X[tr], y[tr], spec["loss"])
    out = np.full(len(d), np.nan)
    out[te] = pred[te] * np.exp(np.clip(X[te] @ b, -3, 3))
    if with_train:
        return out, pred * np.exp(np.clip(X @ b, -3, 3)), tr
    return out


def evaluate_target(d: pd.DataFrame, F: pd.DataFrame, target: str, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    spec = TARGETS[target]
    ok = d["shifts_ok"].astype(bool).to_numpy() if spec.get("needs_shifts") else np.ones(len(d), bool)
    y = d[spec["act"]].to_numpy(float)
    game = d["game_id"].to_numpy()
    season = d["season"].to_numpy()
    roll = np.nan_to_num(rolling_level(d, spec["pred"], spec["act"], mask=ok))          # league-wide level of the previous 90 days: point-in-time by construction
    preds: dict[str, np.ndarray] = {"INCUMBENT": np.where(np.isin(season, TEST_SEASONS) & ok, d[spec["pred"]].to_numpy(float), np.nan)}
    for s in TEST_SEASONS:
        for name, cols in spec["stages"]:
            p = fit_predict(d, F, target, cols, s, roll)
            preds.setdefault(name, np.full(len(d), np.nan))
            preds[name] = np.where(np.isnan(preds[name]), p, preds[name])
    loss = {k: PD.row_loss(np.where(np.isnan(v), 1.0, v), y, spec["loss"]) for k, v in preds.items()}
    names = ["INCUMBENT"] + [n for n, _ in spec["stages"]]
    out: dict[str, Any] = {"loss": spec["loss"], "stages": [n for n, _ in spec["stages"]], "by_season": {}, "pooled": {}}
    for scope, mask_fn in [(str(s), (lambda s=s: (season == s) & ok)) for s in TEST_SEASONS] + [("pooled", lambda: np.isin(season, TEST_SEASONS) & ok)]:
        m = mask_fn()
        row: dict[str, Any] = {"n": int(m.sum()), "loss": {k: float(loss[k][m].mean()) for k in names}, "bias": {k: float(np.nanmean(preds[k][m] - y[m])) for k in names}}
        if spec["loss"] == "sq":
            row["rmse"] = {k: float(np.sqrt(loss[k][m].mean())) for k in names}
        row["vs_previous"] = {names[i]: PD.paired_game_ci(loss[names[i]][m] - loss[names[i - 1]][m], game[m], n_boot=n_boot) for i in range(2, len(names))}
        row["vs_incumbent"] = {k: PD.paired_game_ci(loss[k][m] - loss["INCUMBENT"][m], game[m], n_boot=n_boot) for k in names[1:]}
        (out["pooled"] if scope == "pooled" else out["by_season"]).update({scope: row} if scope != "pooled" else row)
    return out


def shots_crps(d: pd.DataFrame, F: pd.DataFrame, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    """Distributional check on the shots stages with the project's own scorer (negative binomial, dispersion fitted on the TRAINING seasons' in-sample residuals) against the
    incumbent as Poisson (CHAMPION) and as NB (CHAMPION_NB), 2023-25, game-clustered paired bootstrap. In-sample dispersion for the challenger is a stated approximation."""
    from nhl_edge.research import workload_eval as E
    from nhl_edge.research import workload_v1 as W

    spec = TARGETS["sog"]
    y = d["y_sog"].to_numpy(float)
    game, season = d["game_id"].to_numpy(), d["season"].to_numpy()
    roll = np.nan_to_num(rolling_level(d, spec["pred"], spec["act"]))
    names = ["CHAMPION", "CHAMPION_NB"] + [n for n, _ in spec["stages"]]
    pieces: dict[str, list[dict[str, np.ndarray]]] = {k: [] for k in names}
    for s in TEST_SEASONS:
        te = season == s
        inc = d[spec["pred"]].to_numpy(float)
        tr = season < s
        pieces["CHAMPION"].append(E.score_arm(E.poisson_pmf(inc[te], W.SOG_K), y[te], [1, 2, 3, 4, 5]))
        a_nb = E.fit_nb_alpha(y[tr], inc[tr])
        pieces["CHAMPION_NB"].append(E.score_arm(E.nb_pmf(inc[te], a_nb, W.SOG_K), y[te], [1, 2, 3, 4, 5]))
        for name, cols in spec["stages"]:
            te_pred, all_pred, trm = fit_predict(d, F, "sog", cols, s, roll, with_train=True)
            a = E.fit_nb_alpha(y[trm], all_pred[trm])
            pieces[name].append(E.score_arm(E.nb_pmf(te_pred[te], a, W.SOG_K), y[te], [1, 2, 3, 4, 5]))
    cat = {k: {m: np.concatenate([p[m] for p in v]) for m in v[0]} for k, v in pieces.items()}
    g = np.concatenate([game[season == s] for s in TEST_SEASONS])
    out = {"summary": {k: E.summarize(v) for k, v in cat.items()}, "vs_champion_nb": {}, "vs_champion": {}}
    for k in cat:
        if k not in ("CHAMPION", "CHAMPION_NB"):
            out["vs_champion_nb"][k] = E.bootstrap_diff(g, cat[k], cat["CHAMPION_NB"], n_boot)
            out["vs_champion"][k] = E.bootstrap_diff(g, cat[k], cat["CHAMPION"], n_boot)
    return out


def lc_stack(history: Path, cache: Path, prereg: Path, seasons: tuple[int, ...] = (2023, 2024, 2025), n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    """Do the signals add anything on top of WORKLOAD_V1_LC itself? LC's own predictive mean per skater-game (frozen parameters, level factor, as in the registered test)
    times ``exp(b0 + b1 usage + b2 opponent)``; walk-forward on LC's own seasons, so only 2024 (fitted on 2023) and 2025 (fitted on 2023-24) can be scored. Exploratory."""
    from nhl_edge.research import workload_eval as E
    from nhl_edge.research import workload_experiment as X
    from nhl_edge.research import workload_level_cal as LC
    from nhl_edge.research import workload_replication as R
    from nhl_edge.research import workload_v1 as W

    pre = json.loads(Path(prereg).read_text())
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    ctx = R.ReplicationCtx(history, cache, "derived", R.derive_wf(history, [2022, *seasons]))
    frames = []
    for s in seasons:
        stash: dict[int, pd.DataFrame] = {}
        m, _, _ = X.skater_arms(ctx, s, prm, frames_hook=LC.make_hook(stash))
        frames.append(m[["game_id", "player_id", "season", "date_int", "team_id", "opp_id", "wl_sog", "ch_sog", "y_sog", "ch_toi", "y_toi"]])
    lc = pd.concat(frames, ignore_index=True)
    champ = PD.load_champion(cache)
    d = lc.merge(champ[["game_id", "player_id", "ch_toi_pp", "y_toi_pp", "y_toi_ev", "shifts_ok"]], on=["game_id", "player_id"], how="left").sort_values(["date_int", "game_id"]).reset_index(drop=True)
    F = build_features(champ.reset_index(drop=True), None).assign(game_id=champ.reset_index(drop=True)["game_id"], player_id=champ.reset_index(drop=True)["player_id"])
    d = d.merge(F[["game_id", "player_id", "x_recent_toi", "x_opp_sa"]], on=["game_id", "player_id"], how="left")
    y, pred, game, season = d["y_sog"].to_numpy(float), d["wl_sog"].to_numpy(float), d["game_id"].to_numpy(), d["season"].to_numpy()
    out: dict[str, Any] = {"seasons_scored": [], "stages": {}}
    stage_cols = {"LC": [], "LC+USAGE": ["x_recent_toi"], "LC+USAGE+OPP": ["x_recent_toi", "x_opp_sa"]}
    rows: dict[str, list[dict[str, np.ndarray]]] = {k: [] for k in stage_cols}
    gids = []
    for s in seasons[1:]:
        tr, te = season < s, season == s
        alpha = {}
        mu_te = {}
        for name, cols in stage_cols.items():
            X_ = np.column_stack([np.ones(len(d)), *[np.nan_to_num(d[c].to_numpy(float)) for c in cols]]) if cols else np.ones((len(d), 1))
            b = PD.fit_scale(pred[tr], X_[tr], y[tr], "poisson") if cols else np.zeros(1)
            mu = pred * np.exp(np.clip(X_ @ b, -3, 3))
            alpha[name] = E.fit_nb_alpha(y[tr], mu[tr])
            mu_te[name] = mu[te]
            rows[name].append(E.score_arm(E.nb_pmf(mu[te], alpha[name], W.SOG_K), y[te], [1, 2, 3, 4, 5]))
        gids.append(game[te])
        out["seasons_scored"].append(int(s))
    cat = {k: {m: np.concatenate([p[m] for p in v]) for m in v[0]} for k, v in rows.items()}
    g = np.concatenate(gids)
    out["summary"] = {k: E.summarize(v) for k, v in cat.items()}
    out["vs_lc"] = {k: E.bootstrap_diff(g, cat[k], cat["LC"], n_boot) for k in cat if k != "LC"}
    return out


def stack_on(M: pd.DataFrame, pred: str, act: str, feats: list[str], loss: str, test_seasons: tuple[int, ...], mask_col: str | None = None, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    """Generic walk-forward stack: ``M[pred] * exp(b0 + b.feats)`` fitted on rows of earlier seasons present in ``M``, scored on each test season; returns pooled losses and the
    paired game-clustered differences (stack vs base, stack vs level-only)."""
    y, p, game, season = M[act].to_numpy(float), M[pred].to_numpy(float), M["game_id"].to_numpy(), M["season"].to_numpy()
    ok = np.ones(len(M), bool) if mask_col is None else M[mask_col].astype(bool).to_numpy()
    X_full = np.column_stack([np.ones(len(M)), *[np.nan_to_num(M[c].to_numpy(float)) for c in feats]]) if feats else np.ones((len(M), 1))
    X_lvl = np.ones((len(M), 1))
    base, lvl, stk, gids, coefs = [], [], [], [], {}
    for s in test_seasons:
        tr, te = (season < s) & ok, (season == s) & ok
        if tr.sum() < 1000 or te.sum() < 1000:
            continue
        b0 = PD.fit_scale(p[tr], X_lvl[tr], y[tr], loss)
        b1 = PD.fit_scale(p[tr], X_full[tr], y[tr], loss)
        base.append(PD.row_loss(p[te], y[te], loss))
        lvl.append(PD.row_loss(p[te] * np.exp(X_lvl[te] @ b0), y[te], loss))
        stk.append(PD.row_loss(p[te] * np.exp(np.clip(X_full[te] @ b1, -3, 3)), y[te], loss))
        gids.append(game[te])
        coefs[str(s)] = [float(x) for x in b1]
    B, L, S, G = (np.concatenate(x) for x in (base, lvl, stk, gids))
    return {"seasons": list(coefs), "n": int(len(B)), "loss_base": float(B.mean()), "loss_level": float(L.mean()), "loss_stack": float(S.mean()), "coef": coefs,
            "stack_vs_base": PD.paired_game_ci(S - B, G, n_boot=n_boot), "stack_vs_level": PD.paired_game_ci(S - L, G, n_boot=n_boot)}


def workload_frames(history: Path, cache: Path, prereg: Path, seasons: tuple[int, ...] = TEST_SEASONS) -> pd.DataFrame:
    """WORKLOAD_V1's own per-skater-game predictions (frozen parameters, constants fitted on earlier seasons) for the walk-forward seasons, with the incumbent's, joined to outcomes."""
    from nhl_edge.research import workload_experiment as X
    from nhl_edge.research import workload_level_cal as LC
    from nhl_edge.research import workload_replication as R
    from nhl_edge.research import workload_v1 as W

    pre = json.loads(Path(prereg).read_text())
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    ctx = R.ReplicationCtx(history, cache, "derived", R.derive_wf(history, [2022, *seasons]))
    fr = []
    for s in seasons:
        m, _, _ = X.skater_arms(ctx, s, prm, frames_hook=LC.make_hook({}))
        fr.append(m[["game_id", "player_id", "season", "wl_toi", "wl_toi_pp", "wl_sog", "y_toi", "y_toi_pp", "ch_toi", "ch_toi_pp"]])
    return pd.concat(fr, ignore_index=True)


def minutes_vs_workload(history: Path, cache: Path, prereg: Path, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    """Is there anything left to add on top of WORKLOAD_V1's own ice-time forecasts? WORKLOAD_V1 vs the incumbent over 2023-25, then recent usage (and role) stacked on
    WORKLOAD_V1 and fitted on earlier seasons (so only 2024 and 2025 can be scored)."""
    wl = workload_frames(history, cache, prereg)
    champ = PD.load_champion(cache).reset_index(drop=True)
    g = champ.groupby("player_id", sort=False)
    champ["last3_toi"] = g["y_toi"].transform(lambda x: x.shift(1).rolling(3, min_periods=3).mean())
    champ["last5_pp"] = g["y_toi_pp"].transform(lambda x: x.shift(1).rolling(5, min_periods=5).mean())
    champ["last3_pp"] = g["y_toi_pp"].transform(lambda x: x.shift(1).rolling(3, min_periods=3).mean())
    champ["last12_pp"] = g["y_toi_pp"].transform(lambda x: x.shift(4).rolling(12, min_periods=6).mean())
    M = wl.merge(champ[["game_id", "player_id", "date_int", "shifts_ok", "last3_toi", "last5_pp", "last3_pp", "last12_pp"]], on=["game_id", "player_id"], how="left")
    M = M.sort_values(["date_int", "game_id"]).reset_index(drop=True)
    M["x_use_toi"] = np.log((M["last3_toi"] + 1.0) / (M["wl_toi"] + 1.0))
    M["x_use_pp"] = np.log((M["last5_pp"] + 0.25) / (M["wl_toi_pp"] + 0.25))
    M["x_role_pp"] = np.log((M["last3_pp"] + 0.25) / (M["last12_pp"] + 0.25))
    out: dict[str, Any] = {"seasons_workload": list(TEST_SEASONS), "vs_incumbent": {}}
    for tgt, base, inc, act, needs in (("toi", "wl_toi", "ch_toi", "y_toi", False), ("toi_pp", "wl_toi_pp", "ch_toi_pp", "y_toi_pp", True)):
        m = M[M["shifts_ok"].astype(bool)] if needs else M
        y = m[act].to_numpy(float)
        a, b = (m[base].to_numpy(float) - y) ** 2, (m[inc].to_numpy(float) - y) ** 2
        out["vs_incumbent"][tgt] = {"n": int(len(m)), "mse_incumbent": float(b.mean()), "mse_workload_v1": float(a.mean()), "bias_workload_v1": float((m[base] - m[act]).mean()),
                                    "bias_incumbent": float((m[inc] - m[act]).mean()), "workload_minus_incumbent": PD.paired_game_ci(a - b, m["game_id"].to_numpy(), n_boot=n_boot)}
    out["stack_on_workload"] = {"toi": stack_on(M, "wl_toi", "y_toi", ["x_use_toi"], "sq", (2024, 2025), n_boot=n_boot),
                                "toi_pp": stack_on(M, "wl_toi_pp", "y_toi_pp", ["x_use_pp", "x_role_pp"], "sq", (2024, 2025), mask_col="shifts_ok", n_boot=n_boot)}
    return out


def run(cache: Path, history: Path | None, n_boot: int = PD.N_BOOT) -> dict[str, Any]:
    d = PD.load_champion(cache).reset_index(drop=True)
    F = build_features(d, history)
    return {"test_seasons": list(TEST_SEASONS), "evidence": "development (all seasons exposed to earlier workload work); selects a frozen specification, validates nothing",
            "n_rows": int(len(d)), "targets": {t: evaluate_target(d, F, t, n_boot) for t in TARGETS}, "shots_distribution": shots_crps(d, F, n_boot)}


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.player_challengers")
    ap.add_argument("--cache", default="out/workload_v1_replication_cache/derived")
    ap.add_argument("--prereg", default="docs/research/workload_v1/preregistration.json")
    ap.add_argument("--with-workload", action="store_true", help="also compare with WORKLOAD_V1/LC themselves (needs the replication context; a few minutes)")
    ap.add_argument("--history", default="data/history")
    ap.add_argument("--out", required=True)
    ap.add_argument("--no-lines", action="store_true")
    a = ap.parse_args(argv)
    res = run(Path(a.cache), None if a.no_lines else Path(a.history))
    if a.with_workload:
        res["minutes_vs_workload"] = minutes_vs_workload(Path(a.history), Path(a.cache), Path(a.prereg))
        res["lc_stack"] = lc_stack(Path(a.history), Path(a.cache), Path(a.prereg))
    Path(a.out).write_text(json.dumps(res, indent=1, default=float))
    print(f"wrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
