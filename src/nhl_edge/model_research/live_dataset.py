"""Point-in-time pregame reconstruction of the LIVE tier (2026-09-29 .. 2026-10-20): what SIFT knew at T-``cut_minutes``.

Every pregame column is stamped with the archive instant it was observed; nothing observed after the cut enters a pregame
column. Final results and the actual starting goalie are LABELS (``y_*`` / ``actual_*``), never inputs. Columns are grouped
by provenance in ``DATA_DICTIONARY`` so a reader can tell observed, model-derived and inferred values apart.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.market_audit.games import build_games, read_kind
from nhl_edge.model_research import DEV_LAST_GAME_DATE_ET, PROSPECTIVE_FREEZE_UTC
from nhl_edge.model_research.slates import build_slate_table

DATA_DICTIONARY: dict[str, tuple[str, str]] = {
    "game_id": ("OBSERVED", "NHL game id from the archived schedule snapshots"),
    "start_time_utc": ("OBSERVED", "latest scheduled puck drop in any pre-start schedule snapshot"),
    "cut_utc": ("DERIVED", "start - cut_minutes; the instant the pregame state is frozen"),
    "slate_run_id / slate_generated_at": ("OBSERVED", "the last production slate run generated at or before the cut"),
    "slate_age_min": ("DERIVED", "cut - slate_generated_at: staleness of the model forecast at the cut"),
    "v1_lam_home, v1_lam_away, v1_seed": ("MODEL-DERIVED", "exact inputs of nhl-sim-1.1; the predictive distribution regenerates bit-for-bit"),
    "v2_lam_*": ("MODEL-DERIVED", "DATA_ONLY_V2 shadow expected goals for the same run"),
    "{home,away}_goalie_*": ("OBSERVED", "goalie named by the slate at the cut (status ladder PROJECTED<PROBABLE<CONFIRMED)"),
    "gobs_{home,away}_*": ("OBSERVED", "goalie_observations: last Daily Faceoff observation at or before the cut; source_reported_at_utc is the "
                                       "SOURCE's own timestamp when the site supplied one (33% of rows) - a lower bound on when the fact was public"),
    "sb_p_home, sb_n_providers": ("OBSERVED", "de-vigged median NHL-API sportsbook moneyline (decimal odds) from the last snapshot at or before the cut"),
    "actual_{home,away}_starter_id": ("LABEL", "goalie with starter=True in the archived boxscore; known only after the game"),
    "y_*, home_final, away_final": ("LABEL", "official final from the archived results kind"),
}


def _utc(s: pd.Series) -> pd.Series:
    return pd.to_datetime(s, utc=True)


def dev_games(archive: Path) -> pd.DataFrame:
    g = build_games(archive)
    g = g[g["is_final"] & (g["season_type"] == "regular") & (g["game_date_et"] <= DEV_LAST_GAME_DATE_ET)
          & (g["start_time_utc"] < pd.Timestamp(PROSPECTIVE_FREEZE_UTC))].copy()
    g["game_id"] = g["game_id"].astype(str)
    return g.sort_values("start_time_utc").reset_index(drop=True)


def goalie_obs_at_cut(obs: pd.DataFrame, game: str, team: int, cut: pd.Timestamp) -> dict[str, Any]:
    o = obs[(obs["game_id"] == game) & (obs["team_id"] == team)].sort_values("obs_ts")
    pre = o[o["obs_ts"] <= cut]
    conf = o[o["status"] == "CONFIRMED"]
    out: dict[str, Any] = {"n_obs_pre_cut": int(len(pre))}
    if len(pre):
        last = pre.iloc[-1]
        out.update(name=last["player_name"], status=last["status"], obs_utc=last["obs_ts"], source_reported_utc=last["rep_ts"])
    first_conf = conf.iloc[0] if len(conf) else None
    out["first_confirmed_obs_utc"] = first_conf["obs_ts"] if first_conf is not None else pd.NaT
    rep = conf["rep_ts"].dropna()
    out["first_confirmed_reported_utc"] = rep.min() if len(rep) else pd.NaT
    out["confirmed_name"] = first_conf["player_name"] if first_conf is not None else None
    return out


def to_decimal_odds(v: Any) -> float:
    """The feed mixes decimal ("1.68") and American ("-125", "+104") quotes by provider; normalise to decimal odds."""
    try:
        x = float(str(v).strip())
    except ValueError:
        return float("nan")
    if abs(x) >= 100:
        return 1 + x / 100 if x > 0 else 1 + 100 / -x
    return x if x > 1 else float("nan")


def sportsbook_at_cut(sb: pd.DataFrame, cut: pd.Timestamp) -> tuple[float, int, float]:
    s = sb[sb["obs_ts"] <= cut]
    if s.empty:
        return np.nan, 0, np.nan
    last = s.sort_values("obs_ts").groupby(["provider", "side"]).tail(1)
    piv = last.pivot_table(index="provider", columns="side", values="dec", aggfunc="first").dropna()
    if piv.empty:
        return np.nan, 0, np.nan
    ph = (1 / piv["home"]) / ((1 / piv["home"]) + (1 / piv["away"]))
    overround = float(((1 / piv["home"]) + (1 / piv["away"])).median())
    return float(ph.median()), int(len(ph)), overround


def build_live_dataset(archive: Path, cut_minutes: float = 60.0, slate_table: pd.DataFrame | None = None, games: pd.DataFrame | None = None) -> pd.DataFrame:
    """Pregame table at T-``cut_minutes``. ``games`` defaults to the DEVELOPMENT window; only ``daily.py`` passes post-freeze games (the prospective ledger)."""
    games = dev_games(archive) if games is None else games
    slates = slate_table if slate_table is not None else build_slate_table(archive, DEV_LAST_GAME_DATE_ET)
    obs = read_kind(archive, "context/goalie_observations")
    obs["game_id"] = obs["game_id"].astype(str)
    box_obs = obs[obs["source"] == "nhl_api_boxscore"]  # post-start starter flags: LABEL material, never a pregame observation
    obs = obs[obs["source"] == "dailyfaceoff"].copy()
    obs["obs_ts"] = _utc(obs["observed_at_utc"])
    obs["rep_ts"] = _utc(obs["source_reported_at_utc"])
    sb = read_kind(archive, "context/sportsbook_odds")
    sb["game_id"] = sb["game_id"].astype(str)
    sb["obs_ts"] = _utc(sb["_observed_at_utc"])
    sb["dec"] = sb["value"].map(to_decimal_odds)
    sb = sb.dropna(subset=["dec"])
    ge = read_kind(archive, "player_events/goalies")
    ge["game_id"] = ge["game_id"].astype(str)
    # The archived ``starter`` flag is unreliable (False for 76/151 games' goalies who played the whole game), so the
    # goalie of record is the one with the most ice time; ``n_goalies_used`` flags relief appearances.
    ge = ge.sort_values(["game_id", "team_id", "toi_s"], ascending=[True, True, False])
    used = ge[ge["toi_s"] > 0].groupby(["game_id", "team_id"]).size().rename("n_used")
    top = ge.groupby(["game_id", "team_id"]).head(1).set_index(["game_id", "team_id"])
    starters = top.join(used)
    del box_obs
    rows: list[dict[str, Any]] = []
    for g in games.itertuples():
        cut = g.start_time_utc - pd.Timedelta(minutes=cut_minutes)
        sl = slates[(slates["game_id"] == g.game_id) & (slates["generated_at_utc"] <= cut)]
        r: dict[str, Any] = {"game_id": g.game_id, "game_date_et": g.game_date_et, "start_time_utc": g.start_time_utc, "cut_utc": cut,
                             "home": g.home_abbrev, "away": g.away_abbrev, "home_team_id": int(g.home_team_id), "away_team_id": int(g.away_team_id),
                             "start_changed": bool(g.start_changed), "home_final": int(g.home_final), "away_final": int(g.away_final), "home_reg": g.home_reg,
                             "away_reg": g.away_reg, "last_period_type": g.last_period_type}
        r["y_home_win"] = int(g.home_final > g.away_final)
        r["y_total"] = int(g.home_final + g.away_final)
        r["y_ot"] = int(g.last_period_type in ("OT", "SO"))
        r["y_so"] = int(g.last_period_type == "SO")
        if len(sl):
            s = sl.iloc[-1]
            r.update({"slate_run_id": s["run_id"], "slate_generated_at": s["generated_at_utc"], "slate_age_min": (cut - s["generated_at_utc"]).total_seconds() / 60})
            r.update({k: s[k] for k in sl.columns if k.startswith(("v1_", "v2_", "home_goalie", "away_goalie"))})
        for side, tid in (("home", g.home_team_id), ("away", g.away_team_id)):
            o = goalie_obs_at_cut(obs, g.game_id, int(tid), cut)
            r.update({f"gobs_{side}_{k}": v for k, v in o.items()})
            if (g.game_id, int(tid)) in starters.index:
                st = starters.loc[(g.game_id, int(tid))]
                r.update({f"actual_{side}_starter_id": int(st["player_id"]), f"actual_{side}_starter_name": st["name"], f"actual_{side}_n_goalies_used": int(st["n_used"]),
                          f"actual_{side}_saves": int(st["saves"]),
                          f"actual_{side}_shots_against": int(st["shots_against"]), f"actual_{side}_goals_against": int(st["goals_against"]),
                          f"actual_{side}_goalie_toi_s": int(st["toi_s"])})
        p, n, ov = sportsbook_at_cut(sb[sb["game_id"] == g.game_id], cut)
        r.update({"sb_p_home": p, "sb_n_providers": n, "sb_overround": ov})
        rows.append(r)
    return pd.DataFrame(rows)
