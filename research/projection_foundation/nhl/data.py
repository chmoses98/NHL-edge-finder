"""Load official NHL player-event history into tidy skater / goalie / team game tables.

Sources (all official NHL boxscore + play-by-play + shift charts, pulled by the repo's own
`player_research_data` job; schema `nhl-player-events-1.0`):
  * data/history/players/<kind>_<season>.parquet  seasons 2021-22 .. 2025-26 (+3 games of 2026-27)
  * data-archive branch player_events/<kind>/dt=*/*.jsonl.gz  2026-27 games as they go final
    (read from a sparse worktree; default research/projection_foundation/.cache/archive_wt,
    override with NHL_PF_ARCHIVE)

Only regular-season games (game_type 2) are used. Every quantity here is a POST-game fact; the
point-in-time discipline lives in features.py (everything there is shifted one game).
"""
from __future__ import annotations

import glob
import math
import os
from functools import cache
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[3]
HIST = ROOT / "data" / "history" / "players"
PF = ROOT / "research" / "projection_foundation"
CACHE = Path(os.environ.get("NHL_PF_CACHE", str(PF / ".cache")))
ARCHIVE = Path(os.environ.get("NHL_PF_ARCHIVE", str(PF / ".cache" / "archive_wt")))
# Forward projection hook: placeholder rows for not-yet-played games (outcomes are dummies; every
# feature is lagged, so a game's own placeholder outcome can only feed games after it - none exist).
EXTRA: dict[str, pd.DataFrame] = {}


def set_future(extra: dict[str, pd.DataFrame]) -> None:
    EXTRA.clear()
    EXTRA.update(extra)
    load_kind.cache_clear()
SEASONS = [2021, 2022, 2023, 2024, 2025, 2026]

# Arizona (53) -> Utah Hockey Club (59) -> Utah Mammoth (68): one franchise for ratings.
FRANCHISE = {53: 68, 59: 68}

# Approximate arena coordinates (lat, lon) by home team id, for travel distance.
ARENA = {
    1: (40.733, -74.171), 2: (40.722, -73.590), 3: (40.750, -73.993), 4: (39.901, -75.172),
    5: (40.439, -79.989), 6: (42.366, -71.062), 7: (42.875, -78.876), 8: (45.496, -73.569),
    9: (45.297, -75.927), 10: (43.643, -79.379), 12: (35.803, -78.722), 13: (26.158, -80.326),
    14: (27.943, -82.452), 15: (38.898, -77.021), 16: (41.881, -87.674), 17: (42.341, -83.055),
    18: (36.159, -86.779), 19: (38.627, -90.203), 20: (51.037, -114.052), 21: (39.749, -105.008),
    22: (53.547, -113.498), 23: (49.278, -123.109), 24: (33.808, -117.877), 25: (32.790, -96.810),
    26: (34.043, -118.267), 28: (37.333, -121.901), 29: (39.969, -83.006), 30: (44.945, -93.101),
    52: (49.893, -97.144), 53: (33.532, -112.261), 54: (36.103, -115.178), 55: (47.622, -122.354),
    59: (40.768, -111.901), 68: (40.768, -111.901),
}

KEYS = {
    "players": ["game_id", "player_id"],
    "goalies": ["game_id", "player_id"],
    "goals": ["game_id", "period", "t_s", "team_id", "scorer_id"],
    "shots": ["game_id", "period", "t_s", "shooter_id", "kind", "x", "y"],
    "coice": ["game_id", "team_id", "p1", "p2"],
    "team_states": ["game_id", "team_id"],
}


def _read_archive(kind: str) -> pd.DataFrame:
    files = sorted(glob.glob(str(ARCHIVE / "player_events" / kind / "dt=*" / "*.jsonl.gz")))
    if not files:
        return pd.DataFrame()
    parts = [pd.read_json(f, lines=True, dtype=False) for f in files]
    d = pd.concat([p for p in parts if len(p)], ignore_index=True)
    if d.empty:
        return d
    # a game can be re-ingested (stat corrections): keep only its newest complete snapshot
    last = d.groupby("game_id")["_observed_at_utc"].transform("max")
    d = d[d["_observed_at_utc"] == last]
    return d


@cache
def load_kind(kind: str, seasons: tuple[int, ...] = tuple(SEASONS)) -> pd.DataFrame:
    parts = []
    for s in seasons:
        f = HIST / f"{kind}_{s}.parquet"
        if f.exists():
            parts.append(pd.read_parquet(f))
    d = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    if 2026 in seasons:
        a = _read_archive(kind)
        if len(a):
            a = a[[c for c in a.columns if not c.startswith("_")]]
            # archive supersedes the committed parquet for the same game
            d = d[~d["game_id"].isin(a["game_id"].unique())] if len(d) else d
            d = pd.concat([d, a], ignore_index=True)
    if kind in EXTRA and len(EXTRA[kind]):
        d = pd.concat([d, EXTRA[kind]], ignore_index=True)
    if len(d):
        d = d[d["game_type"] == 2].copy()
        d["game_date"] = pd.to_datetime(d["game_date"])
        d = d.drop_duplicates(subset=[c for c in KEYS[kind] if c in d.columns], keep="last")
    return d.reset_index(drop=True)


def archive_available() -> bool:
    return (ARCHIVE / "player_events" / "players").exists()


def haversine_km(a, b) -> float:
    (la1, lo1), (la2, lo2) = a, b
    p1, p2 = math.radians(la1), math.radians(la2)
    dphi, dl = p2 - p1, math.radians(lo2 - lo1)
    h = math.sin(dphi / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


# --------------------------------------------------------------------------- xG
def shot_frame(seasons=tuple(SEASONS)) -> pd.DataFrame:
    """Unblocked attempts (SOG, GOAL, MISS) with geometry for the xG model."""
    s = load_kind("shots", seasons)
    s = s[s["kind"].isin(["SOG", "GOAL", "MISS"])].copy()
    ax = s["x"].abs().clip(upper=99)
    dx = (89 - ax).astype(float)
    dy = s["y"].astype(float)
    s["dist"] = np.sqrt(dx ** 2 + dy ** 2)
    s["angle"] = np.degrees(np.arctan2(dy.abs(), dx.clip(lower=0.5)))
    s["behind"] = (ax > 89).astype(int)
    s["rebound"] = (s["since_prev_s"].fillna(99) <= 3).astype(int)
    s["is_goal"] = (s["kind"] == "GOAL").astype(int)
    s["shot_type"] = s["shot_type"].fillna("unknown")
    return s


# --------------------------------------------------------------------------- team games
def team_games(seasons=tuple(SEASONS)) -> pd.DataFrame:
    p = load_kind("players", seasons)
    g = load_kind("goals", seasons)
    ts = load_kind("team_states", seasons)
    gl = load_kind("goalies", seasons)
    base = p.groupby(["game_id", "team_id"], as_index=False).agg(
        season=("season", "first"), game_date=("game_date", "first"), is_home=("is_home", "first"),
        home_team_id=("home_team_id", "first"), away_team_id=("away_team_id", "first"),
        sog_for=("sog", "sum"), goals_box=("goals", "sum"), att_for=("att_ev", "sum"),
        ot_s=("toi_ot_s", "max"))
    gf = g.groupby(["game_id", "team_id"]).size().rename("goals_for")
    base = base.merge(gf, on=["game_id", "team_id"], how="left")
    base["goals_for"] = base["goals_for"].fillna(0).astype(int)
    base["opp_id"] = np.where(base["is_home"], base["away_team_id"], base["home_team_id"])
    opp = base[["game_id", "team_id", "sog_for", "goals_for"]].rename(
        columns={"team_id": "opp_id", "sog_for": "sog_against", "goals_for": "goals_against"})
    base = base.merge(opp, on=["game_id", "opp_id"], how="left")
    ts2 = ts[["game_id", "team_id", "sec_pp", "sec_sh", "sec_ev", "n_seconds"]]
    base = base.merge(ts2, on=["game_id", "team_id"], how="left")
    base["pp_min"] = base["sec_pp"] / 60.0
    base["sh_min"] = base["sec_sh"] / 60.0
    # OT: any goal scored in OT, or skaters logged OT time
    otg = g[g["period_type"] == "OT"].groupby("game_id").size()
    base["ot"] = (base["game_id"].map(otg).fillna(0) > 0) | (base["ot_s"].fillna(0) > 0)
    # saves allowed context: starting goalie
    st = gl[gl["starter"]][["game_id", "team_id", "player_id"]].rename(columns={"player_id": "starter_id"})
    base = base.merge(st, on=["game_id", "team_id"], how="left")
    base["franchise"] = base["team_id"].replace(FRANCHISE)
    base["opp_franchise"] = base["opp_id"].replace(FRANCHISE)
    base = base.sort_values(["team_id", "game_date", "game_id"]).reset_index(drop=True)
    # schedule: rest, back-to-back, travel (venue = home team's arena)
    base["venue"] = np.where(base["is_home"], base["team_id"], base["opp_id"])
    prev_date = base.groupby("team_id")["game_date"].shift(1)
    base["rest_days"] = (base["game_date"] - prev_date).dt.days
    base.loc[base["season"] != base.groupby("team_id")["season"].shift(1), "rest_days"] = np.nan
    base["b2b"] = (base["rest_days"] == 1).astype(int)
    prev_venue = base.groupby("team_id")["venue"].shift(1)
    base["travel_km"] = [haversine_km(ARENA[int(a)], ARENA[int(b)]) if pd.notna(a) and int(a) in ARENA and int(b) in ARENA else 0.0
                         for a, b in zip(prev_venue, base["venue"])]
    base.loc[base["rest_days"].isna(), "travel_km"] = 0.0
    o = base[["game_id", "team_id", "b2b", "rest_days", "travel_km"]].rename(
        columns={"team_id": "opp_id", "b2b": "opp_b2b", "rest_days": "opp_rest_days", "travel_km": "opp_travel_km"})
    base = base.merge(o, on=["game_id", "opp_id"], how="left")
    base["total_goals"] = base["goals_for"] + base["goals_against"]
    return base


# --------------------------------------------------------------------------- skaters
def skater_games(seasons=tuple(SEASONS), xg: pd.DataFrame | None = None) -> pd.DataFrame:
    p = load_kind("players", seasons).copy()
    p = p[p["toi_s"] > 0]
    p["opp_id"] = np.where(p["is_home"], p["away_team_id"], p["home_team_id"])
    p["pos"] = np.where(p["position"] == "D", "D", "F")
    ok = p["shifts_ok"].astype(bool)
    p["toi"] = p["toi_s"] / 60.0
    p["toi_pp"] = np.where(ok, p["toi_pp_s"].fillna(0) / 60.0, np.nan)
    p["toi_sh"] = np.where(ok, p["toi_sh_s"].fillna(0) / 60.0, np.nan)
    p["toi_ev"] = np.where(ok, p["toi_ev_s"].fillna(0) / 60.0, np.nan)
    p["toi_np"] = p["toi"] - p["toi_pp"]
    p["sog_pp"] = np.where(ok, p["sog_pp"], np.nan)
    p["sog_np"] = p["sog"] - p["sog_pp"]
    p["att"] = p[["att_ev", "att_pp", "att_sh", "att_ea", "att_en"]].sum(axis=1)
    # points by strength from the official goal events
    g = load_kind("goals", seasons)
    rows = []
    for col in ("scorer_id", "a1_id", "a2_id"):
        x = g[["game_id", col, "strength"]].dropna(subset=[col]).rename(columns={col: "player_id"})
        x["player_id"] = x["player_id"].astype("int64")
        x["kind"] = "g" if col == "scorer_id" else "a"
        rows.append(x)
    ev = pd.concat(rows, ignore_index=True)
    ev["pp"] = (ev["strength"] == "PP").astype(int)
    ev["pp_a"] = ev["pp"] * (ev["kind"] == "a").astype(int)
    agg = ev.groupby(["game_id", "player_id"]).agg(points_pp=("pp", "sum"), assists_pp=("pp_a", "sum"))
    p = p.merge(agg, on=["game_id", "player_id"], how="left")
    p["points_pp"] = p["points_pp"].fillna(0)
    p["assists_pp"] = p["assists_pp"].fillna(0)
    p.loc[~ok.to_numpy(), ["points_pp", "assists_pp"]] = np.nan
    p["points_np"] = p["points"] - p["points_pp"]
    p["assists_np"] = p["assists"] - p["assists_pp"]
    p["goals_pp"] = np.where(ok, p["pp_goals"], np.nan)
    p["goals_np"] = p["goals"] - p["goals_pp"]
    # on-ice team goals while on the ice (involvement denominators)
    p["gf_on"] = p[["gf_ev", "gf_pp", "gf_sh", "gf_ea", "gf_en"]].sum(axis=1)
    if xg is not None:
        p = p.merge(xg, on=["game_id", "player_id"], how="left")
        for c in ("ixg", "ixg_pp"):
            p[c] = p[c].fillna(0.0)
    p["franchise"] = p["team_id"].replace(FRANCHISE)
    p["opp_franchise"] = p["opp_id"].replace(FRANCHISE)
    p = p.sort_values(["player_id", "game_date", "game_id"]).reset_index(drop=True)
    return p


def goalie_games(seasons=tuple(SEASONS)) -> pd.DataFrame:
    g = load_kind("goalies", seasons).copy()
    g["opp_id"] = np.where(g["is_home"], g["away_team_id"], g["home_team_id"])
    g["toi"] = g["toi_s"] / 60.0
    g["franchise"] = g["team_id"].replace(FRANCHISE)
    g["opp_franchise"] = g["opp_id"].replace(FRANCHISE)
    g = g.sort_values(["player_id", "game_date", "game_id"]).reset_index(drop=True)
    return g
