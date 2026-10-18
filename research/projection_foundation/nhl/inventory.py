"""Data-availability matrix and the point-in-time status of lineups / starting goalies.

pit_class
  archived        captured before puck drop and stored immutably (data-archive branch)
  reconstructable a post-game fact that is legitimately usable as HISTORY for later games, or a
                  pregame-knowable fact (schedule, rest, travel) rebuilt after the fact
  retrospective   only known after the game; using it for the same game conditions on the outcome
                  (dressed lineup, actual starting goalie, actual line deployment)
  missing         not available
"""
from __future__ import annotations

import glob
import json
import unicodedata

import numpy as np
import pandas as pd

from . import data

ARCH = data.ARCHIVE


def _season_counts(kind):
    out = {}
    for s in data.SEASONS:
        m = data.HIST / f"MANIFEST_{s}.json"
        if m.exists():
            out[s] = json.load(open(m))
    return out


def matrix(sk: pd.DataFrame | None = None) -> list[dict]:
    rows = []
    man = _season_counts("players")
    p = data.load_kind("players")
    games = p.groupby("season")["game_id"].nunique().to_dict()
    shifts = p.groupby("season").apply(lambda g: g.groupby("game_id")["shifts_ok"].all().mean(), include_groups=False).to_dict()
    arch_games = 0
    if data.archive_available():
        arch_games = int(p.loc[p["season"] == 2026, "game_id"].nunique())

    def seas(d):
        return ", ".join(f"{k}-{str(k + 1)[2:]}: {v}" for k, v in sorted(d.items()))

    rows.append({"dataset": "skater/goalie box scores (official boxscore)", "seasons": "2021-22..2026-27",
                 "rows": int(len(p)), "pit_class": "reconstructable",
                 "notes": f"regular-season games by season {seas(games)}; 2026-27 = {arch_games} games from the data-archive "
                          "player_events (through 2026-10-16) superseding 3 committed games. Post-game facts used only as history."})
    rows.append({"dataset": "TOI by strength (EV / PP / SH / EA / EN / OT from shift charts)", "seasons": "2021-22..2026-27",
                 "rows": int(p["shifts_ok"].sum()), "pit_class": "reconstructable",
                 "notes": "share of games with shift charts: " + ", ".join(f"{k}: {v:.3f}" for k, v in sorted(shifts.items()))
                          + ". 2024-25 lacks shift charts for 57 games (strength split NaN there)."})
    c = sum(v["files"]["coice"]["rows"] for v in man.values())
    rows.append({"dataset": "line combinations (pairwise shared ice, coice)", "seasons": "2021-22..2026-27", "rows": int(c),
                 "pit_class": "reconstructable",
                 "notes": "post-game deployment; the PIT role used for game g is the previous game's lines / PP unit. "
                          "Tonight's lines are NOT known historically."})
    nl = len(glob.glob(str(ARCH / "context" / "lines" / "dt=*" / "*")))
    rows.append({"dataset": "pregame projected lines / PP units (DailyFaceoff)", "seasons": "2026-27 only (from 2026-09-30)",
                 "rows": nl, "pit_class": "archived" if nl else "missing",
                 "notes": "archived hourly snapshots (context/lines); none for 2021-22..2025-26, so the value of confirmed lines "
                          "cannot be backtested. See lineup_accuracy."})
    gl = data.load_kind("goalies")
    rows.append({"dataset": "starting goalie (actual, boxscore starter flag)", "seasons": "2021-22..2026-27",
                 "rows": int(gl["starter"].sum()), "pit_class": "retrospective",
                 "notes": "saves projections are CONDITIONAL_ON_ACTUAL_STARTER; no PIT starter source exists before 2026-27."})
    ng = len(glob.glob(str(ARCH / "context" / "goalie_observations" / "dt=*" / "*")))
    rows.append({"dataset": "pregame starting-goalie observations (DailyFaceoff status)", "seasons": "2026-27 only",
                 "rows": ng, "pit_class": "archived" if ng else "missing",
                 "notes": "PROJECTED / PROBABLE / CONFIRMED with observation time; see starter_accuracy."})
    sh = data.load_kind("shots")
    rows.append({"dataset": "shot events with x/y, type, strength (xG possible)", "seasons": "2021-22..2026-27",
                 "rows": int(len(sh)), "pit_class": "reconstructable",
                 "notes": "own logistic xG fitted on development seasons; used as lagged player/team shot quality."})
    rows.append({"dataset": "schedule, rest days, back-to-backs", "seasons": "2021-22..2026-27", "rows": int(sum(games.values())),
                 "pit_class": "reconstructable", "notes": "game dates are known in advance; derived from the game list."})
    rows.append({"dataset": "travel distance / time zones", "seasons": "2021-22..2026-27", "rows": int(sum(games.values())),
                 "pit_class": "reconstructable", "notes": "previous venue -> current venue haversine on approximate arena coordinates."})
    ni = len(glob.glob(str(ARCH / "context" / "injuries" / "dt=*" / "*")))
    rows.append({"dataset": "injury reports (ESPN)", "seasons": "2026-27 only", "rows": ni,
                 "pit_class": "archived" if ni else "missing", "notes": "historical injury status missing; scratches are inferred post hoc."})
    pp = CACHE_PP()
    rows.append({"dataset": "archived prospective forecasts PLAYER_SIM_V1 (predictions_player)", "seasons": "2026-27 only",
                 "rows": int(len(pp)) if pp is not None else 0, "pit_class": "archived",
                 "notes": "goals / assists / points / first-goal / saves ladders + expected TOI, PP TOI, SOG, G, A, P per player "
                          "snapshot; incumbent on the 2026-27 overlap (last pregame snapshot per player-game)."})
    rows.append({"dataset": "PLAYER_SIM_V1 walk-forward predictions (docs/research/player_sim_v1)",
                 "seasons": "skaters 2025-26; goalies 2024-25, 2025-26", "rows": 47231 + 2624 * 2,
                 "pit_class": "reconstructable",
                 "notes": "historical walk-forward (deployment from recent shifts, actual dressed lineup and starters); "
                          "incumbent on holdout."})
    rows.append({"dataset": "DATA_ONLY_V2 walk-forward game lambdas (docs/research/walk_forward_v2_*_games.csv)",
                 "seasons": "2024-25, 2025-26", "rows": 2624, "pit_class": "reconstructable",
                 "notes": "SIM2_ST expected home/away goals = team-goals incumbent on holdout (valid pregame arm)."})
    rows.append({"dataset": "dressed lineup / scratches", "seasons": "2021-22..2026-27", "rows": int(len(p)),
                 "pit_class": "retrospective",
                 "notes": "evaluation is conditional on playing (Kalshi settles a non-entering player at fair price)."})
    return rows


def CACHE_PP():
    f = data.CACHE / "pp_archive.parquet"
    if f.exists():
        return pd.read_parquet(f)
    files = sorted(glob.glob(str(ARCH / "predictions_player" / "dt=*" / "*.jsonl.gz")))
    if not files:
        return None
    d = pd.concat([pd.read_json(x, lines=True, dtype=False) for x in files], ignore_index=True)
    d.to_parquet(f)
    return d


def _last(n) -> str:
    t = unicodedata.normalize("NFKD", str(n)).encode("ascii", "ignore").decode()
    return t.split()[-1].lower() if t.split() else ""


def _schedule() -> pd.DataFrame:
    files = sorted(glob.glob(str(ARCH / "context" / "schedule" / "dt=*" / "*.jsonl.gz")))
    s = pd.concat([pd.read_json(f, lines=True, dtype=False) for f in files], ignore_index=True)
    for c in ("game_id", "home_team_id", "away_team_id"):
        s[c] = pd.to_numeric(s[c], errors="coerce")
    s = s.dropna(subset=["game_id"]).astype({"game_id": "int64"})
    s = s.sort_values("_observed_at_utc").drop_duplicates("game_id", keep="last")
    s["start"] = pd.to_datetime(s["start_time_utc"], utc=True)
    return s


def starter_accuracy() -> dict:
    """How often the last pregame DailyFaceoff starter (by status) was the actual starter (2026-27)."""
    files = sorted(glob.glob(str(ARCH / "context" / "goalie_observations" / "dt=*" / "*.jsonl.gz")))
    if not files:
        return {"available": False}
    g = pd.concat([pd.read_json(f, lines=True, dtype=False) for f in files], ignore_index=True)
    g = g[g["source"] == "dailyfaceoff"].copy()
    g["game_id"] = pd.to_numeric(g["game_id"], errors="coerce")
    g["team_id"] = pd.to_numeric(g["team_id"], errors="coerce")
    g = g.dropna(subset=["game_id", "team_id"]).astype({"game_id": "int64", "team_id": "int64"})
    s = _schedule()[["game_id", "start"]]
    g = g.merge(s, on="game_id")
    g["obs"] = pd.to_datetime(g["observed_at_utc"], utc=True)
    g = g[g["obs"] < g["start"]]
    g["mins_before"] = (g["start"] - g["obs"]).dt.total_seconds() / 60
    last = g.sort_values("obs").groupby(["game_id", "team_id"]).tail(1)
    act = data.load_kind("goalies")
    act = act[(act["season"] == 2026) & act["starter"]][["game_id", "team_id", "name"]]
    last = last.merge(act, on=["game_id", "team_id"], how="inner")
    last["ok"] = [_last(a) == _last(b) for a, b in zip(last["player_name"], last["name"])]
    by = last.groupby("status")["ok"].agg(["mean", "size"]).reset_index().to_dict("records")
    # accuracy at fixed horizons before puck drop
    hz = []
    for h in (60, 180, 360):
        x = g[g["mins_before"] >= h].sort_values("obs").groupby(["game_id", "team_id"]).tail(1)
        x = x.merge(act, on=["game_id", "team_id"], how="inner")
        ok = [_last(a) == _last(b) for a, b in zip(x["player_name"], x["name"])]
        hz.append({"horizon_min_before": h, "n": int(len(x)), "accuracy": float(np.mean(ok)) if len(x) else None,
                   "share_confirmed": float((x["status"] == "CONFIRMED").mean()) if len(x) else None})
    return {"available": True, "n_team_games": int(len(last)), "accuracy_last_pregame": float(last["ok"].mean()),
            "by_status": by, "by_horizon": hz,
            "wrong": last.loc[~last["ok"], ["game_id", "team_id", "player_name", "name", "status"]].to_dict("records")}


def lineup_accuracy() -> dict:
    """Last pregame DailyFaceoff lines vs who actually dressed, PP1 membership and forward-line slot (2026-27)."""
    files = sorted(glob.glob(str(ARCH / "context" / "lines" / "dt=*" / "*.jsonl.gz")))
    if not files:
        return {"available": False}
    L = pd.concat([pd.read_json(f, lines=True, dtype=False) for f in files], ignore_index=True)
    L["obs"] = pd.to_datetime(L["observed_at_utc"], utc=True)
    L["team_id"] = pd.to_numeric(L["team_id"], errors="coerce")
    L["player_id"] = pd.to_numeric(L["player_id"], errors="coerce")
    s = _schedule()
    s = s[s["season"] == "2026-27"] if "season" in s else s
    sk = data.load_kind("players")
    sk = sk[sk["season"] == 2026]
    tm = pd.concat([s[["game_id", "start", "home_team_id"]].rename(columns={"home_team_id": "team_id"}),
                    s[["game_id", "start", "away_team_id"]].rename(columns={"away_team_id": "team_id"})])
    tm = tm[tm["game_id"].isin(sk["game_id"].unique())]
    res = []
    for r in tm.itertuples():
        x = L[(L["team_id"] == r.team_id) & (L["obs"] < r.start) & (L["obs"] > r.start - pd.Timedelta(hours=30))]
        if x.empty:
            continue
        x = x[x["obs"] == x["obs"].max()]
        act = sk[(sk["game_id"] == r.game_id) & (sk["team_id"] == r.team_id) & (sk["toi_s"] > 0)].copy()
        if act.empty:
            continue
        proj = x[(x["category"] == "ev") & (x["unit"] != "g") & x["player_id"].notna()]
        pset, aset = set(proj["player_id"].astype(int)), set(act["player_id"].astype(int))
        pp1 = set(x[(x["unit"] == "pp1") & x["player_id"].notna()]["player_id"].astype(int))
        act["pp_rank"] = act["toi_pp_s"].rank(ascending=False, method="first")
        app1 = set(act[(act["pp_rank"] <= 5) & (act["toi_pp_s"] > 15)]["player_id"].astype(int))
        res.append({"game_id": r.game_id, "team_id": r.team_id, "n_proj": len(pset), "n_act": len(aset),
                    "proj_dressed": len(pset & aset), "act_in_proj": len(aset & pset),
                    "pp1_proj": len(pp1), "pp1_hit": len(pp1 & app1), "pp1_act": len(app1),
                    "mins_before": (r.start - x["obs"].max()).total_seconds() / 60})
    d = pd.DataFrame(res)
    if d.empty:
        return {"available": True, "n_team_games": 0}
    return {"available": True, "n_team_games": int(len(d)),
            "projected_skaters_who_dressed": float(d["proj_dressed"].sum() / d["n_proj"].sum()),
            "dressed_skaters_in_projection": float(d["act_in_proj"].sum() / d["n_act"].sum()),
            "pp1_precision": float(d["pp1_hit"].sum() / max(d["pp1_proj"].sum(), 1)),
            "pp1_recall": float(d["pp1_hit"].sum() / max(d["pp1_act"].sum(), 1)),
            "median_minutes_before_start": float(d["mins_before"].median())}
