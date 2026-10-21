"""M-INFO-1: do Kalshi moneyline prices move around Daily Faceoff goalie confirmations, and is our capture early enough to matter? (LIVE tier, descriptive)

Event = first pregame CONFIRMED observation of a team's goalie that carries the SOURCE's own report time (``source_reported_at_utc``).
CHANGE events: the confirmed goalie differs from the one named in the preceding observation. The source time is the best available lower bound on when the
fact became public; it is not proof of when the market learned it. Kalshi quotes are the 15-minute board ticks (+45 s availability lag), so any reaction faster than ~15 min is invisible.
    python -m nhl_edge.model_research.exp_info --archive <data-archive> --derived <work dir> --repo . --out docs/research/nhl-model-improvement/data
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from nhl_edge.market_audit.games import read_kind
from nhl_edge.model_research import registry
from nhl_edge.model_research import scoring as S
from nhl_edge.model_research.live_dataset import dev_games

HORIZONS_MIN = (15, 30, 60, 120)


def confirmation_events(archive: Path, games: pd.DataFrame) -> pd.DataFrame:
    go = read_kind(archive, "context/goalie_observations")
    go = go[go["source"] == "dailyfaceoff"].copy()
    go["game_id"] = go["game_id"].astype(str)
    go["obs"] = pd.to_datetime(go["observed_at_utc"], utc=True)
    go["rep"] = pd.to_datetime(go["source_reported_at_utc"], utc=True)
    go = go.merge(games[["game_id", "start_time_utc", "home_team_id", "away_team_id"]], on="game_id")
    go = go[go["obs"] < go["start_time_utc"]]
    rows = []
    for (gid, tid), x in go.sort_values("obs").groupby(["game_id", "team_id"]):
        conf = x[x["status"] == "CONFIRMED"]
        if conf.empty or pd.isna(conf.iloc[0]["rep"]):
            continue
        c = conf.iloc[0]
        before = x[x["obs"] < c["obs"]]
        prior = before.iloc[-1]["player_name"] if len(before) else None
        rows.append({"game_id": gid, "team_id": int(tid), "t0": c["rep"], "first_obs": c["obs"], "start": c["start_time_utc"], "home": int(tid) == int(c["home_team_id"]),
                     "confirmed": c["player_name"], "prior": prior, "change": prior is not None and prior != c["player_name"], "has_prior": prior is not None,
                     "capture_lag_min": (c["obs"] - c["rep"]).total_seconds() / 60, "report_min_before_start": (c["start_time_utc"] - c["rep"]).total_seconds() / 60})
    return pd.DataFrame(rows)


def mid_asof(q: pd.DataFrame, t: pd.Timestamp) -> float:
    s = q[q["available_at"] <= t]
    if s.empty:
        return np.nan
    r = s.iloc[-1]
    if not (r["yes_bid"] > 0 and r["yes_ask"] > r["yes_bid"] and r["status"] == "active"):
        return np.nan
    return float((r["yes_bid"] + r["yes_ask"]) / 200)


def run(archive: Path, derived: Path) -> dict[str, Any]:
    games = dev_games(archive)
    ev = confirmation_events(archive, games)
    cm = pd.read_parquet(derived / "contract_master.parquet")
    cm = cm[(cm["kind"] == "winner") & cm["game_id"].notna()]
    home_leg = {}
    for r in cm.itertuples():
        g = games[games["game_id"] == str(r.game_id)]
        if len(g) and r.subject_team_id == g.iloc[0]["home_team_id"]:
            home_leg[str(r.game_id)] = r.ticker
    qe = pd.read_parquet(derived / "quote_events.parquet")
    qe = qe[qe["ticker"].isin(set(home_leg.values()))].sort_values("available_at")
    by_t = {t: g.reset_index(drop=True) for t, g in qe.groupby("ticker")}
    rows = []
    for e in ev.itertuples():
        tk = home_leg.get(e.game_id)
        if tk is None or tk not in by_t or e.report_min_before_start < 20:
            continue
        q = by_t[tk]
        sign = 1.0 if e.home else -1.0  # a better goalie for THIS team raises ITS win probability
        pre = mid_asof(q, e.t0 - pd.Timedelta(minutes=1))
        plc = mid_asof(q, e.t0 - pd.Timedelta(hours=3, minutes=1))  # placebo window: same horizon, 3h earlier
        r = {"game_id": e.game_id, "team_id": e.team_id, "change": e.change, "has_prior": e.has_prior, "capture_lag_min": e.capture_lag_min, "mid_before": pre}
        for h in HORIZONS_MIN:
            # the post window must end at least 5 minutes before puck drop: later quotes are in-play and would contaminate the move
            post = mid_asof(q, e.t0 + pd.Timedelta(minutes=h)) if e.t0 + pd.Timedelta(minutes=h) <= e.start - pd.Timedelta(minutes=5) else np.nan
            r[f"d{h}"] = sign * (post - pre) if not (np.isnan(post) or np.isnan(pre)) else np.nan
            plc_post = mid_asof(q, e.t0 - pd.Timedelta(hours=3) + pd.Timedelta(minutes=h))
            r[f"placebo_abs{h}"] = abs(plc_post - plc) if not (np.isnan(plc_post) or np.isnan(plc)) else np.nan
        rows.append(r)
    d = pd.DataFrame(rows)
    out: dict[str, Any] = {"n_confirmation_events_with_source_time": int(len(ev)), "n_with_kalshi_quotes": int(len(d)),
                           "capture_lag_min": {"median": float(ev["capture_lag_min"].median()), "p25": float(ev["capture_lag_min"].quantile(0.25)), "p75": float(ev["capture_lag_min"].quantile(0.75)),
                                               "share_under_15min": float((ev["capture_lag_min"] < 15).mean())},
                           "n_change_events": int(ev["change"].sum()), "n_same_events": int((~ev["change"] & ev["has_prior"]).sum()), "groups": {}}
    for name, m in (("CHANGE", d["change"] & d["has_prior"]), ("SAME", ~d["change"] & d["has_prior"])):
        s = d[m]
        g: dict[str, Any] = {"n": int(len(s))}
        for h in HORIZONS_MIN:
            v = s[f"d{h}"].dropna().to_numpy()
            pl = s[f"placebo_abs{h}"].dropna().to_numpy()
            g[f"h{h}"] = {"n": int(len(v)), "mean_abs_move_pts": float(np.abs(v).mean() * 100) if len(v) else None, "mean_signed_move_pts": S.boot_mean_ci(v)[0] * 100 if len(v) else None,
                          "mean_abs_move_placebo_pts": float(pl.mean() * 100) if len(pl) else None}
        out["groups"][name] = g
    ch, sm = d[d["change"] & d["has_prior"]], d[~d["change"] & d["has_prior"]]
    out["change_minus_same_abs_move_pts"] = {}
    for h in HORIZONS_MIN:
        a, b = np.abs(ch[f"d{h}"].dropna().to_numpy()) * 100, np.abs(sm[f"d{h}"].dropna().to_numpy()) * 100
        if len(a) > 3 and len(b) > 3:
            rng = np.random.default_rng(0)
            boots = [rng.choice(a, len(a)).mean() - rng.choice(b, len(b)).mean() for _ in range(4000)]
            out["change_minus_same_abs_move_pts"][f"h{h}"] = {"diff": float(a.mean() - b.mean()), "lo95": float(np.quantile(boots, 0.025)), "hi95": float(np.quantile(boots, 0.975)), "n_change": len(a), "n_same": len(b)}
    return out


def record(res: dict[str, Any], repo: Path, reg: Path) -> None:
    ents = registry.read(reg)
    if any(e["type"] == "RESULT" and e["id"] == "M-INFO-1" and e.get("revision") == 2 for e in ents):
        return
    if any(e["type"] == "RESULT" and e["id"] == "M-INFO-1" for e in ents) and not any(e["type"] == "NOTE" and e["id"] == "M-INFO-1" for e in ents):
        registry.append(reg, "NOTE", "M-INFO-1", {"note": "The first M-INFO-1 RESULT let the post-event window run past puck drop for late confirmations (in-play prices inflated the SAME-group moves at "
                                                          "60/120 minutes). It is retained as history and SUPERSEDED by revision 2, which requires the window to end at least 5 minutes before the start. "
                                                          "Lesson applied to every later runner: results are written to the registry only with an explicit --record after the printed output has been checked."}, repo)
    if not any(e["id"] == "M-INFO-1" for e in ents):
        registry.append(reg, "PREREG", "M-INFO-1", {
            "hypothesis": "Kalshi moneylines reprice around goalie confirmations that change the expected starter, and our archive captures confirmations before the market has absorbed them.",
            "motivation": "Information timing is the only plausible source of a pregame edge; the prior audit declared it untestable for lack of source timestamps.",
            "method": "Confirmation events with source_reported_at_utc (Daily Faceoff); Kalshi home-leg mid as-of t0-1min vs t0+15/30/60/120 min (15-minute board ticks); abs and signed moves, "
                      "CHANGE vs SAME vs 3-hour-earlier placebo; our capture lag = first_observed - source_reported.",
            "baseline": "placebo drift and SAME events", "decision_rule": "MARKET_REACTS if CHANGE abs move exceeds SAME with 95% CI > 0 at any horizon; CAPTURE_TOO_SLOW if the median capture lag exceeds 15 minutes. Descriptive; n small.",
            "tier": "LIVE_DESCRIPTIVE", "disclosure": "registered after the first execution of this script (code written before executing; not edited after)."}, repo)
    if not any(e["id"] == "M-INFO-1" and e["type"] == "RESULT" for e in registry.read(reg)):
        react = [h for h, v in res["change_minus_same_abs_move_pts"].items() if v["lo95"] > 0]
        registry.append(reg, "RESULT", "M-INFO-1", {"revision": 2, "supersedes": "first M-INFO-1 RESULT (window crossed puck drop)", "metrics": res, "decision": ("MARKET_REACTS@" + ",".join(react) if react else "NO_DETECTABLE_REACTION_DIFFERENCE")
                                                    + ("; CAPTURE_TOO_SLOW" if res["capture_lag_min"]["median"] > 15 else ""),
                                                    "interpretation": "see docs/research/nhl-model-improvement/INFORMATION_EVENT_ASSESSMENT.md",
                                                    "reproduction": "python -m nhl_edge.model_research.exp_info --archive <data-archive> --derived <work dir> --repo . --out docs/research/nhl-model-improvement/data",
                                                    "results_file": "docs/research/nhl-model-improvement/data/info_events.json"}, repo)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--archive", type=Path, required=True)
    ap.add_argument("--derived", type=Path, required=True)
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--record", action="store_true", help="append the RESULT to the experiment registry (only after the output has been checked)")
    a = ap.parse_args()
    r = run(a.archive, a.derived)
    (a.out / "info_events.json").write_text(json.dumps(r, indent=1, default=float))
    if a.record:
        record(r, a.repo, a.repo / "docs/research/nhl-model-improvement/experiment_registry.jsonl")
    print(json.dumps(r, indent=1, default=float))
