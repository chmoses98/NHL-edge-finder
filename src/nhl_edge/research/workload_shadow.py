"""WORKLOAD_V1_LC forward predictor for the prospective shadow test (RESEARCH_ONLY; docs/research/workload_v1/LC_PROSPECTIVE_REGISTRATION.md).

Builds the same skater/team tables as the retrospective harness from the repository's pinned history plus the settled player events in the archive, appends
OUTCOME-FREE stub rows for the games about to be played, and runs the unchanged ``workload_v1.skater_predictions`` on the whole table. Because every quantity in
that function is "strictly before this row" (``ew_prior_sums`` never includes the row itself; league windows are strictly earlier dates), a stub row gets exactly the
prediction the retrospective harness would have given the same player-game with the same earlier games present -- ``tests/test_workload_shadow.py`` proves this on
real data. The level factor (``workload_level_cal.level_factors``) and the NegBin dispersion (fitted on the previous season's residuals of the corrected means)
follow the frozen definitions.

Nothing here reads the market, the betting engine or the app contract, and nothing is published: records go to their own data branch.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.data.history import pinned_seasons
from nhl_edge.data.player_history import load_player_tables
from nhl_edge.research import workload_eval as E
from nhl_edge.research import workload_level_cal as LC
from nhl_edge.research import workload_v1 as W

TABLES = ("players", "goalies", "goals", "shots", "team_states")
TRAIN_SEASONS = [2021, 2022, 2023, 2024, 2025]            # constants for the 2026 season: every completed season, as in the retrospective protocol
DISPERSION_SEASON = 2025
CANDIDATE_GAMES = 5                                       # a candidate dressed in any of the team's last five settled games
MODEL_ID = "WORKLOAD_V1_LC"
PMF_K = 12                                                # stored probabilities P(0)..P(11) and P(>=12)
PARAMS_FILE = "docs/research/workload_v1/preregistration.json"
INTERNAL_COLS = ("_observed_at_utc", "_run_id")


@contextlib.contextmanager
def stable_sorts() -> Iterator[None]:
    """Make ``DataFrame.sort_values`` stable by default while the unchanged ``workload_v1`` functions run.

    ``workload_v1`` sorts by date with numpy's unstable default, so which rows of the boundary DATE fall inside a rolling league window depends on the input
    row order (documented in WORKLOAD_V1_REPLICATION.md: a wobble of a few 1e-3 in the mean shot prediction, all rows dated strictly before the game). A prospective
    record must be reproducible from its inputs, so the predictor fixes the tie order to the input order; the numbers therefore differ from the retrospective
    harness only within that documented wobble.
    """
    orig = pd.DataFrame.sort_values

    def stable(self, *a, **k):
        k.setdefault("kind", "stable")
        return orig(self, *a, **k)

    pd.DataFrame.sort_values = stable  # type: ignore[method-assign]
    try:
        yield
    finally:
        pd.DataFrame.sort_values = orig  # type: ignore[method-assign]


def load_tables(history_root: Path, live: dict[str, list[dict[str, Any]]] | None = None) -> dict[str, pd.DataFrame]:
    """Pinned history (skater tables >= 2021) plus the settled live events of the archive (rows for games not already in history)."""
    hist = Path(history_root)
    seasons = pinned_seasons(hist, "players")
    t = {k: load_player_tables(hist, k, seasons) for k in TABLES}
    for k in TABLES:
        rows = (live or {}).get(k) or []
        if rows:
            df = pd.DataFrame(rows).drop(columns=[c for c in INTERNAL_COLS if c in rows[0]], errors="ignore")
            known = set(t[k]["game_id"].unique()) if len(t[k]) else set()
            df = df[~df["game_id"].isin(known)]
            t[k] = pd.concat([t[k], df], ignore_index=True) if len(t[k]) else df
    for k in TABLES:                                       # live rows may carry strings; make the keys numeric like the history files
        for col in ("game_id", "team_id", "player_id", "season", "game_type"):
            if col in t[k].columns:
                t[k][col] = pd.to_numeric(t[k][col], errors="coerce")
    if len(t["goals"]) and "game_type" in t["goals"].columns:
        t["goals"] = t["goals"][t["goals"]["game_type"] == 2]
    return t


def build_tables(t: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    tg = W.team_games(t["players"], t["team_states"], t["shots"], t["goals"])
    sk = W.skater_table(t["players"], tg, t["shots"])
    return sk, tg


def candidates(players: pd.DataFrame, team_id: int, before_date_int: int, k: int = CANDIDATE_GAMES) -> list[int]:
    """Skaters who dressed for ``team_id`` in any of its last ``k`` regular-season games dated before ``before_date_int`` (point in time, outcome free)."""
    p = players[(players["team_id"] == team_id) & (players["game_type"] == 2)].copy()
    p["date_int"] = p["game_date"].astype(str).str.replace("-", "").str[:8].astype(int)
    p = p[p["date_int"] < before_date_int]
    last = sorted(p[["date_int", "game_id"]].drop_duplicates().itertuples(index=False))[-k:]
    keep = {g for _, g in last}
    return sorted(int(x) for x in p.loc[p["game_id"].isin(keep), "player_id"].unique())


def _stubs(sk: pd.DataFrame, tg: pd.DataFrame, games: list[dict[str, Any]], cand: dict[int, list[int]], season: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    dates = {int(str(g["game_date_et"]).replace("-", "")) for g in games}
    if len(dates) != 1:
        raise ValueError("stub rows are built for ONE game day at a time (a stub must never precede another stub)")
    di = dates.pop()
    last = sk.sort_values(["player_id", "date_int", "game_id"]).groupby("player_id").tail(1).set_index("player_id")
    sk_rows, tg_rows = [], []
    for g in games:
        gid, hid, aid = int(g["game_id"]), int(g["home_team_id"]), int(g["away_team_id"])
        for tid, oid, home in ((hid, aid, True), (aid, hid, False)):
            base = {c: np.nan for c in tg.columns}
            base.update({"game_id": gid, "team_id": tid, "opp_id": oid, "is_home": home, "date_int": di, "season": season, "game_type": 2, "game_date": str(g["game_date_et"]),
                         "clean": False, "repaired": False, "ot_game": False, "ot_len": 0.0, "home_team_id": hid, "away_team_id": aid})
            tg_rows.append(base)
            for pid in cand.get(tid, []):
                if pid not in last.index:
                    continue
                r = {c: np.nan for c in sk.columns}
                r["player_id"] = pid
                r.update({c: last.loc[pid, c] for c in ("name", "position", "pos") if c in last.columns})
                r.update({"game_id": gid, "team_id": tid, "opp_id": oid, "is_home": home, "date_int": di, "season": season, "game_type": 2, "game_date": str(g["game_date_et"]),
                          "home_team_id": hid, "away_team_id": aid, "share_ok": False, "shifts_ok": False, "clean": False, "repaired": False, "ot_game": False})
                sk_rows.append(r)
    return pd.DataFrame(sk_rows, columns=sk.columns), pd.DataFrame(tg_rows, columns=tg.columns)


@dataclass
class Fit:
    constants: W.TrainedConstants
    params: W.WorkloadParams
    alpha: float
    prediction_inputs_sha: str


def predict_day(sk: pd.DataFrame, tg: pd.DataFrame, games: list[dict[str, Any]], players: pd.DataFrame, goalies: pd.DataFrame, params_path: Path,
                season: int = 2026, cand: dict[int, list[int]] | None = None, constants: W.TrainedConstants | None = None,
                dispersion_season: int = DISPERSION_SEASON) -> tuple[pd.DataFrame, Fit]:
    """Predictions for the candidate skaters of ``games`` (one game day). ``sk``/``tg`` hold only settled games.

    ``constants`` / ``dispersion_season`` exist for the equivalence test only; production uses the registered defaults (constants on 2021-2025, dispersion on 2025)."""
    pre = json.loads(Path(params_path).read_text())
    prm = W.WorkloadParams.from_dict(pre["frozen_params"])
    c = constants or W.fit_constants(sk, tg, goalies, TRAIN_SEASONS)
    di = int(str(games[0]["game_date_et"]).replace("-", ""))
    if cand is None:
        tids = {int(g[k]) for g in games for k in ("home_team_id", "away_team_id")}
        cand = {t: candidates(players, t, di) for t in tids}
    ssk, stg = _stubs(sk, tg, games, cand, season)
    sk_all = pd.concat([sk, ssk], ignore_index=True).sort_values(["player_id", "date_int", "game_id"]).reset_index(drop=True)
    tg_all = pd.concat([tg, stg], ignore_index=True).sort_values(["date_int", "game_id", "team_id"]).reset_index(drop=True)
    with stable_sorts():
        d = W.skater_predictions(sk_all, tg_all, c, prm)
    d["y_sog"] = pd.to_numeric(d["sog"], errors="coerce")
    stub_ids = {int(g["game_id"]) for g in games}
    prev = d[(d["season"] == dispersion_season) & (d["game_type"] == 2) & d["y_sog"].notna()]
    cur = d[(d["season"] == season) & (d["game_type"] == 2)]
    both = pd.concat([prev.assign(_s=0), cur.assign(_s=1)], ignore_index=True)
    known = both["y_sog"].notna().to_numpy()
    days = LC._days(both["date_int"])
    y_k, p_k, d_k = both.loc[known, "y_sog"].to_numpy(float), both.loc[known, "wl_sog"].to_numpy(float), days[known]
    f = np.ones(len(both))
    f[known] = LC.level_factors(d_k, y_k, p_k)                      # settled rows: exactly the retrospective harness's factor
    stub_day = int(LC._days(pd.Series([di]))[0])
    stub_factor = float(LC.level_factors(np.r_[d_k, stub_day], np.r_[y_k, 0.0], np.r_[p_k, 0.0])[-1])   # strictly earlier settled days only
    f[~known] = stub_factor
    both["lc_mean"] = both["wl_sog"].to_numpy(float) * f
    prev_lc = both[both["_s"] == 0]
    alpha = E.fit_nb_alpha(prev_lc["y_sog"].to_numpy(float), prev_lc["lc_mean"].to_numpy(float))
    out = both[(both["_s"] == 1) & both["game_id"].isin(stub_ids) & both["y_sog"].isna()].copy()
    out["level_factor"] = stub_factor
    pmf = E.nb_pmf(out["lc_mean"].to_numpy(float), alpha, PMF_K)
    out["pmf"] = list(pmf)
    out["raw_mean"] = out["wl_sog"].to_numpy(float)
    sha = hashlib.sha256(json.dumps({"constants": c.to_dict(), "params": pre["frozen_params"], "alpha": round(alpha, 10)}, sort_keys=True, default=float).encode()).hexdigest()
    return out, Fit(c, prm, float(alpha), sha)


def records(pred: pd.DataFrame, games: list[dict[str, Any]], fit: Fit, predicted_at_utc: str, code_commit: str) -> list[dict[str, Any]]:
    start = {int(g["game_id"]): g["start_time_utc"] for g in games}
    out = []
    for r in pred.itertuples(index=False):
        out.append({"schema": "workload-shadow-1", "model_id": MODEL_ID, "game_id": int(r.game_id), "game_start_utc": start[int(r.game_id)], "predicted_at_utc": predicted_at_utc,
                    "pregame": predicted_at_utc < start[int(r.game_id)], "player_id": int(r.player_id), "name": str(r.name), "pos": str(r.pos), "team_id": int(r.team_id),
                    "opp_id": int(r.opp_id), "is_home": bool(r.is_home), "raw_mean": round(float(r.raw_mean), 6), "level_factor": round(float(r.level_factor), 6),
                    "mean": round(float(r.lc_mean), 6), "alpha": round(fit.alpha, 8), "pmf": [round(float(x), 7) for x in r.pmf], "inputs_sha256": fit.prediction_inputs_sha,
                    "code_commit": code_commit, "conditional_on": "dressing", "authority": "research_only", "role": "shadow"})
    return out
