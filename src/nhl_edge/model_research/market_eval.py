"""Model-vs-market comparison on game-scoped contracts: contract probabilities from a predictive pmf, and rolling-origin tests of whether
the model carries information beyond the market mid. The independent unit is the GAME: contract-level losses are averaged within a game
and a game family before any interval is computed (a game's ladder of totals is one observation, not seven)."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd
import statsmodels.api as sm

from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.wf_data import MARGIN_LO

FAMILIES = ("winner", "total", "spread")


def contract_p(kind: str, thr: float, subj_home: bool, pm_total: np.ndarray, pm_margin: np.ndarray, p_home_win: float) -> float:
    """P(YES) of a full-game contract from a per-game pmf. Totals: Over thr. Spread: subject wins by MORE than thr (regulation + OT/SO final)."""
    if kind == "winner":
        return p_home_win if subj_home else 1.0 - p_home_win
    if kind == "total":
        return float(pm_total[int(np.floor(thr)) + 1 :].sum())
    if kind == "spread":
        k = int(np.floor(thr)) + 1  # margin >= k
        off = -MARGIN_LO
        return float(pm_margin[off + k :].sum()) if subj_home else float(pm_margin[: off - k + 1].sum())
    raise ValueError(kind)


def attach_model_p(panel: pd.DataFrame, pmf_by_game: dict[Any, dict[str, Any]], col: str) -> pd.DataFrame:
    p = panel[panel["kind"].isin(FAMILIES)].copy()
    vals = []
    for r in p.itertuples():
        g = pmf_by_game.get(r.game_id)
        if g is None:
            vals.append(np.nan)
            continue
        vals.append(contract_p(r.kind, float(r.threshold) if r.threshold == r.threshold else 0.0, bool(r.subject_team_id == r.home_team_id), g["total"], g["margin"], g["p_home_win"]))
    p[col] = vals
    return p


def _fit_offset(y: np.ndarray, off: np.ndarray, x: np.ndarray) -> float:
    try:
        m = sm.GLM(y, x.reshape(-1, 1), family=sm.families.Binomial(), offset=off).fit()
        return float(m.params[0])
    except Exception:  # noqa: BLE001 - separation / too few rows: no adjustment
        return 0.0


def _fit_cal(y: np.ndarray, lm: np.ndarray) -> tuple[float, float]:
    try:
        m = sm.GLM(y, sm.add_constant(lm), family=sm.families.Binomial()).fit()
        return float(m.params[0]), float(m.params[1])
    except Exception:  # noqa: BLE001
        return 0.0, 1.0


def rolling_incremental(df: pd.DataFrame, pcol: str, start_date: str, min_prior: int = 300) -> pd.DataFrame:
    """Per-contract predictions of three forecasters using ONLY contracts from strictly earlier dates, refit once per date:
    mid (raw market), cal (a + b logit mid), inc (offset logit mid + c (logit p_model - logit mid))."""
    df = df.sort_values(["game_date", "game_id", "ticker"]).reset_index(drop=True)
    df["lm"] = S.logit(df["mid"].to_numpy())
    df["lp"] = S.logit(df[pcol].to_numpy())
    df["gap"] = df["lp"] - df["lm"]
    out_cal = np.full(len(df), np.nan)
    out_inc = np.full(len(df), np.nan)
    out_c = np.full(len(df), np.nan)
    ok_model = df[pcol].notna().to_numpy()
    for date, idx in df.groupby("game_date", sort=True).indices.items():
        if str(date) < start_date:
            continue
        prior = df[(df["game_date"] < date) & ok_model]
        if len(prior) < min_prior:
            continue
        y, lm, gap = prior["y"].to_numpy(float), prior["lm"].to_numpy(), prior["gap"].to_numpy()
        a, b = _fit_cal(y, lm)
        c = _fit_offset(y, lm, gap)
        sub = df.iloc[idx]
        out_cal[idx] = S.expit(a + b * sub["lm"].to_numpy())
        out_inc[idx] = S.expit(sub["lm"].to_numpy() + c * np.nan_to_num(sub["gap"].to_numpy()))
        out_c[idx] = c
    df["p_cal"], df["p_inc"], df["c_prior"] = out_cal, out_inc, out_c
    return df


def game_level_losses(df: pd.DataFrame, family: str, pcols: dict[str, str]) -> pd.DataFrame:
    d = df[(df["kind"] == family) & df["p_cal"].notna() & df["p_inc"].notna()]
    rows = {}
    for name, col in pcols.items():
        rows[name] = (S.brier(d[col].to_numpy(), d["y"].to_numpy()))
    t = pd.DataFrame(rows, index=d.index)
    t["game_id"] = d["game_id"].to_numpy()
    return t.groupby("game_id").mean()
