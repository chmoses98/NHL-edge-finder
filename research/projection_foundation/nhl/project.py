"""Forward projections in `sift.projections.v1` for the next NHL slate (research only).

    cd research/projection_foundation && python -m nhl.project [--date YYYY-MM-DD] [--out PATH] [--now ISO]

How it stays point-in-time
  * history = every FINAL game in data/history + the data-archive player_events (newest final game
    defines data_asof_utc);
  * the slate = the archived NHL schedule; lineups = the newest archived DailyFaceoff lines observed
    before generation (fallback: the team's last dressed lineup); starters = newest archived goalie
    observation (fallback: the team's most recent starter); injuries = newest ESPN snapshot;
  * the slate's games enter the exact walk-forward code path as placeholder rows (their dummy outcomes
    can only feed later games, and none exist), so a forward projection is computed by the same
    functions, frozen development parameters and season-blocked LightGBM as the backtest.

Every projection carries authority = research_only; BLOCK rows are written but must not be displayed.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time
import unicodedata
from pathlib import Path

PF = Path(__file__).resolve().parents[1]
if str(PF) not in sys.path:
    sys.path.insert(0, str(PF))
os.environ.setdefault("NHL_PF_CACHE", str(PF / ".cache" / "forward"))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from pf_core import gate  # noqa: E402

from nhl import VERSION, data  # noqa: E402

ARCH = data.ARCHIVE
FAMS = {"sog": ("shots", [2, 3, 4, 5]), "goals": ("goals", [1, 2]), "assists": ("assists", [1, 2]),
        "points": ("points", [1, 2, 3])}
DEFAULT_BEST = {"sog": "D", "goals": "D", "assists": "D", "points": "D", "saves": "D", "team_goals": "D"}


def _norm(n) -> str:
    t = unicodedata.normalize("NFKD", str(n)).encode("ascii", "ignore").decode().lower()
    return t.split()[-1] if t.split() else ""


def _read(kind: str) -> pd.DataFrame:
    files = sorted(glob.glob(str(ARCH / kind / "dt=*" / "*.jsonl.gz")))
    if not files:
        return pd.DataFrame()
    return pd.concat([pd.read_json(f, lines=True, dtype=False) for f in files[-400:]], ignore_index=True)


def schedule() -> pd.DataFrame:
    s = _read("context/schedule")
    for c in ("game_id", "home_team_id", "away_team_id"):
        s[c] = pd.to_numeric(s[c], errors="coerce")
    s = s.dropna(subset=["game_id"]).sort_values("_observed_at_utc").drop_duplicates("game_id", keep="last")
    s["start"] = pd.to_datetime(s["start_time_utc"], utc=True)
    s["game_id"] = s["game_id"].astype("int64")
    return s


def pick_slate(s: pd.DataFrame, last_final: pd.Timestamp, date: str | None):
    s = s[(s["season_type"] == "regular") & (s["game_id"] // 10000 % 100 == 2)]
    if date:
        g = s[s["game_date_et"] == date]
    else:
        fut = s[(pd.to_datetime(s["game_date_et"]) > last_final) & (s["status"] != "final")]
        if fut.empty:
            return s.iloc[0:0], None
        date = fut["game_date_et"].min()
        g = fut[fut["game_date_et"] == date]
    return g.sort_values("start"), date


def lineups(games: pd.DataFrame, now: pd.Timestamp, hist: pd.DataFrame) -> pd.DataFrame:
    L = _read("context/lines")
    rows = []
    if not L.empty:
        L["obs"] = pd.to_datetime(L["observed_at_utc"], utc=True)
        L["team_id"] = pd.to_numeric(L["team_id"], errors="coerce")
        L["player_id"] = pd.to_numeric(L["player_id"], errors="coerce")
    for g in games.itertuples():
        for tid, home in ((int(g.home_team_id), True), (int(g.away_team_id), False)):
            src = None
            if not L.empty:
                x = L[(L["team_id"] == tid) & (L["obs"] <= min(now, g.start)) & (L["obs"] > g.start - pd.Timedelta(hours=36))]
                if len(x):
                    x = x[x["obs"] == x["obs"].max()]
                    ev = x[(x["category"] == "ev") & (x["unit"] != "g") & x["player_id"].notna()]
                    if len(ev) >= 15:
                        pp = x[x["unit"].isin(["pp1", "pp2"]) & x["player_id"].notna()]
                        ppu = dict(zip(pp["player_id"].astype(int), pp["unit"]))
                        for r in ev.itertuples():
                            conf = 1.0 if r.resolution == "jersey+name" else 0.95
                            rows.append({"game_id": g.game_id, "team_id": tid, "is_home": home, "player_id": int(r.player_id),
                                         "name": r.name, "slot": r.slot, "unit": r.unit, "pp_unit_proj": ppu.get(int(r.player_id)),
                                         "lineup_source": f"DailyFaceoff lines ({r.lines_source}) observed {x['obs'].max():%Y-%m-%dT%H:%MZ}",
                                         "identity_confidence": conf, "lines_injury": r.injury_status})
                        src = "lines"
            if src is None:  # fallback: last dressed lineup of this team
                h = hist[hist["team_id"] == tid]
                last = h[h["game_date"] == h["game_date"].max()]
                for r in last.itertuples():
                    rows.append({"game_id": g.game_id, "team_id": tid, "is_home": home, "player_id": int(r.player_id),
                                 "name": r.name, "slot": None, "unit": None, "pp_unit_proj": None,
                                 "lineup_source": f"team's last dressed lineup ({r.game_date:%Y-%m-%d}); no lines archived",
                                 "identity_confidence": 1.0, "lines_injury": None})
    return pd.DataFrame(rows)


def starters(games: pd.DataFrame, now: pd.Timestamp, ghist: pd.DataFrame) -> pd.DataFrame:
    G = _read("context/goalie_observations")
    out = []
    if not G.empty:
        G = G[G["source"] == "dailyfaceoff"].copy()
        G["game_id"] = pd.to_numeric(G["game_id"], errors="coerce")
        G["team_id"] = pd.to_numeric(G["team_id"], errors="coerce")
        G["obs"] = pd.to_datetime(G["observed_at_utc"], utc=True)
    for g in games.itertuples():
        for tid, home in ((int(g.home_team_id), True), (int(g.away_team_id), False)):
            th = ghist[ghist["team_id"] == tid].sort_values("game_date")
            pick = None
            if not G.empty:
                x = G[(G["game_id"] == g.game_id) & (G["team_id"] == tid) & (G["obs"] <= min(now, g.start))]
                if len(x):
                    x = x.sort_values("obs").iloc[-1]
                    cand = th[th["name"].map(_norm) == _norm(x["player_name"])]
                    if len(cand):
                        pick = (int(cand["player_id"].iloc[-1]), cand["name"].iloc[-1], f"DailyFaceoff {x['status']} "
                                f"observed {x['obs']:%Y-%m-%dT%H:%MZ}", x["status"])
            if pick is None:
                st = th[th["starter"]]
                if len(st):
                    pick = (int(st["player_id"].iloc[-1]), st["name"].iloc[-1], "team's most recent starter (no observation)",
                            "ASSUMED")
            if pick:
                out.append({"game_id": g.game_id, "team_id": tid, "is_home": home, "player_id": pick[0], "name": pick[1],
                            "starter_source": pick[2], "starter_status": pick[3]})
    return pd.DataFrame(out)


def injuries() -> dict:
    I = _read("context/injuries")
    if I.empty:
        return {}
    I = I[I["_observed_at_utc"] == I["_observed_at_utc"].max()]
    return {(int(r.team_id), _norm(r.player_name)): str(r.status) for r in I.itertuples() if pd.notna(r.team_id)}


def placeholder_rows(games, lu, gs, hist, ghist):
    pos = hist.sort_values("game_date").drop_duplicates("player_id", keep="last").set_index("player_id")["position"]
    gmap = games.set_index("game_id")
    P = []
    for r in lu.itertuples():
        g = gmap.loc[r.game_id]
        p = pos.get(r.player_id)
        if p is None:
            p = "D" if str(r.slot) in ("ld", "rd") else "C"
        P.append({"game_id": r.game_id, "home_team_id": int(g.home_team_id), "away_team_id": int(g.away_team_id),
                  "season": 2026, "game_date": g.game_date_et, "game_type": 2, "player_id": r.player_id,
                  "team_id": r.team_id, "is_home": bool(r.is_home), "name": r.name, "position": p, "toi_s": 1,
                  "shifts_ok": True})
    P = pd.DataFrame(P)
    num = [c for c in data.load_kind("players").columns if c not in P.columns and c not in ("schema_version",)]
    for c in num:
        P[c] = 0
    Gr = []
    for r in gs.itertuples():
        g = gmap.loc[r.game_id]
        Gr.append({"game_id": r.game_id, "home_team_id": int(g.home_team_id), "away_team_id": int(g.away_team_id),
                   "season": 2026, "game_date": g.game_date_et, "game_type": 2, "player_id": r.player_id,
                   "team_id": r.team_id, "is_home": bool(r.is_home), "name": r.name, "starter": True, "toi_s": 1,
                   "saves": 0, "shots_against": 0, "goals_against": 0})
    Gr = pd.DataFrame(Gr)
    for c in [c for c in data.load_kind("goalies").columns if c not in Gr.columns and c not in ("schema_version", "decision")]:
        Gr[c] = 0
    return P, Gr


def _best(summary_path: Path) -> dict:
    best = dict(DEFAULT_BEST)
    readiness = {}
    if summary_path.exists():
        s = json.load(open(summary_path))
        inv = {"A_season_avg_shrunk": "A", "B_ewma_shrunk": "B", "C_toi_x_rate": "C", "D_opp_adjusted": "D",
               "E_lightgbm": "E", "F_stack": "F"}
        keymap = {"shots": "sog", "goals": "goals", "assists": "assists", "points": "points", "saves": "saves",
                  "team_goals": "team_goals"}
        for f in s.get("families", []):
            k = keymap.get(f["family"])
            if k and f.get("best_model") in inv:
                best[k] = inv[f["best_model"]]
                readiness[k] = (f.get("readiness"), f.get("readiness_reason"))
    return best, readiness


def run(date=None, now=None, out=None) -> dict:
    t0 = time.time()
    from nhl import evaluate as ev
    from nhl import pipeline

    now = pd.Timestamp(now or pd.Timestamp.utcnow().isoformat()).tz_convert("UTC") if now else pd.Timestamp.now(tz="UTC")
    hist = data.load_kind("players")
    ghist = data.load_kind("goalies")
    last_final = hist["game_date"].max()
    pe = sorted(glob.glob(str(ARCH / "player_events" / "players" / "dt=*" / "*.jsonl.gz")))
    asof = pd.read_json(pe[-1], lines=True, dtype=False)["_observed_at_utc"].max() if pe else f"{last_final:%Y-%m-%d}T12:00:00Z"
    s = schedule()
    games, date = pick_slate(s, last_final, date)
    if games.empty:
        raise SystemExit("no upcoming regular-season games in the archived schedule")
    lu = lineups(games, now, hist)
    gs = starters(games, now, ghist)
    inj = injuries()
    P, Gr = placeholder_rows(games, lu, gs, hist, ghist)
    data.set_future({"players": P, "goalies": Gr})
    best, readiness = _best(PF / "results" / "summary.json")
    rebuild = True
    pipeline.stage1(rebuild=rebuild)
    sk, p2 = pipeline.stage2(rebuild=rebuild)
    gf, tg, p3 = pipeline.stage3(rebuild=rebuild)
    gids = set(games["game_id"])
    fut = sk[sk["game_id"].isin(gids)].copy()
    dev = sk["season"].isin([2021, 2022]) & (sk["toi_n"] >= 1)
    # residual quantiles of the selected TOI model on development (opportunity range)
    rq = np.nanquantile((sk.loc[dev, "toi"] - sk.loc[dev, "toi_E"]).to_numpy(float), [0.1, 0.9])
    teams = pd.read_csv(data.ROOT / "data" / "identity" / "teams.csv")
    ab = dict(zip(teams["team_id"], teams["abbrev"]))
    gmap = games.set_index("game_id")
    lu_i = lu.set_index(["game_id", "player_id"])
    players = []
    tg_f = tg[tg["game_id"].isin(gids)]
    tcol = f"mu_tg_{best['team_goals']}"
    tdev = tg["season"].isin([2021, 2022]) & (tg["goals_for_n"].fillna(0) >= 1) & tg[tcol].notna()
    tdp = ev.fit_dist("nb_binned", tg.loc[tdev, "tg"], tg.loc[tdev, tcol], "team_goals")
    team_mu = dict(zip(zip(tg_f["game_id"], tg_f["team_id"]), tg_f[tcol]))
    recon = {}
    for stat, (fam, rungs) in FAMS.items():
        col = f"mu_{stat}_{best[stat]}"
        ok = dev & sk[col].notna()
        dp = ev.fit_dist("nb_binned", sk.loc[ok, stat], sk.loc[ok, col], stat)
        mu = fut[col].fillna(fut[f"mu_{stat}_D"]).to_numpy(float)
        dist = ev.make(dp, mu)
        for i, r in enumerate(fut.itertuples()):
            g = gmap.loc[r.game_id]
            li = lu_i.loc[(r.game_id, r.player_id)] if (r.game_id, r.player_id) in lu_i.index else None
            th = {str(k): round(float(dist.prob_ge(k)[i]), 4) for k in rungs}
            oppf = float(getattr(r, f"oppadj_{stat}")) if np.isfinite(getattr(r, f"oppadj_{stat}")) else 1.0
            adj = []
            if abs(oppf - 1) >= 0.03:
                adj.append(f"opponent {ab.get(int(r.opp_id), r.opp_id)} {'allows more' if oppf > 1 else 'suppresses'} "
                           f"{'shots' if stat == 'sog' else 'scoring'}: x{oppf:.2f} (schedule-adjusted ridge rating)")
            if r.b2b == 1:
                adj.append("team on the second night of a back-to-back")
            if r.toi_n < 10:
                adj.append(f"only {int(r.toi_n)} prior NHL games since 2021-22: rates lean on the role prior")
            if li is not None and isinstance(li, pd.Series) and li.get("pp_unit_proj"):
                adj.append(f"projected {li['pp_unit_proj'].upper()} by DailyFaceoff (role uses the previous game's PP unit)")
            st = inj.get((int(r.team_id), _norm(r.name)))
            hist_toi = sk[(sk["player_id"] == r.player_id) & (sk["game_date"] < r.game_date)].tail(10)
            gi = gate.GateInput(
                sport="NHL", family=fam, entity_id=str(r.player_id), entity_name=r.name, team=ab.get(int(r.team_id)),
                game_id=str(r.game_id), game_start_utc=g.start.strftime("%Y-%m-%dT%H:%M:%SZ"), mean=float(mu[i]),
                identity_confidence=float(li["identity_confidence"]) if li is not None else 1.0, team_verified=True,
                data_asof_utc=asof, injury_status=st, expected_opportunity=float(r.toi_E),
                opportunity_history=hist_toi["toi"].tolist(), stat_history=hist_toi[stat].tolist(),
                opponent_sample_games=None, opponent_factor=oppf, support_lo=0, probs=dist.P[i].tolist(),
                thresholds={k: v for k, v in th.items()}, sd=float(np.sqrt(dist.var[i])), model_n_obs=int(r.toi_n))
            gr = gate.evaluate(gi, now_utc=now.strftime("%Y-%m-%dT%H:%M:%SZ"))
            rd = readiness.get(stat, ("SHADOW VALIDATION", ""))[0]
            players.append({
                "player_id": str(r.player_id), "name": r.name, "team": ab.get(int(r.team_id)),
                "opponent": ab.get(int(r.opp_id)), "game_id": str(r.game_id), "family": fam,
                "mean": round(float(mu[i]), 4), "median": int(dist.median[i]),
                "p10": int(dist.quantile(0.1)[i]), "p90": int(dist.quantile(0.9)[i]), "thresholds": th,
                "opportunity": {"family": "toi_minutes", "mean": round(float(r.toi_E), 2),
                                "p10": round(max(0.0, float(r.toi_E + rq[0])), 2), "p90": round(float(r.toi_E + rq[1]), 2),
                                "pp_mean": round(float(r.toi_pp_E), 2)},
                "opponent_adjustment": {"factor": round(oppf, 4), "sample_games": None},
                "adjustments": adj, "readiness": rd,
                "gate": {"status": gr["status"], "findings": [{k: f[k] for k in ("check", "severity", "what", "category", "action")}
                                                              for f in gr["findings"]]},
                "lineup_source": li["lineup_source"] if li is not None else None,
                "data_asof_utc": asof})
            if stat == "goals":
                recon[(r.game_id, int(r.team_id))] = recon.get((r.game_id, int(r.team_id)), 0.0) + float(mu[i])
    # goalies
    gcol = f"mu_saves_{best['saves']}"
    gdev = gf["season"].isin([2021, 2022]) & (gf["saves_n"].fillna(0) >= 1) & gf[gcol].notna()
    gdp = ev.fit_dist("nb_binned", gf.loc[gdev, "saves"], gf.loc[gdev, gcol], "saves")
    gfut = gf[gf["game_id"].isin(gids)]
    gd = ev.make(gdp, gfut[gcol].fillna(gfut["mu_saves_D"]))
    gsi = gs.set_index(["game_id", "player_id"])
    for i, r in enumerate(gfut.itertuples()):
        g = gmap.loc[r.game_id]
        mu = float(gd.mean[i])
        src = gsi.loc[(r.game_id, r.player_id)] if (r.game_id, r.player_id) in gsi.index else None
        th = {str(k): round(float(gd.prob_ge(k)[i]), 4) for k in (20, 25, 30)}
        gi = gate.GateInput(sport="NHL", family="saves", entity_id=str(r.player_id), entity_name=r.name,
                            team=ab.get(int(r.team_id)), game_id=str(r.game_id),
                            game_start_utc=g.start.strftime("%Y-%m-%dT%H:%M:%SZ"), mean=mu, data_asof_utc=asof,
                            expected_opportunity=float(r.sa_D) if np.isfinite(r.sa_D) else None,
                            support_lo=0, probs=gd.P[i].tolist(), thresholds=th,
                            model_n_obs=int(r.saves_n) if np.isfinite(r.saves_n) else 0)
        gr = gate.evaluate(gi, now_utc=now.strftime("%Y-%m-%dT%H:%M:%SZ"))
        adj = ["conditional on starting: " + (src["starter_source"] if src is not None else "unknown")]
        if src is not None and src["starter_status"] not in ("CONFIRMED",):
            gr["findings"].append({"check": "starter", "severity": "REVIEW", "what": f"starter status {src['starter_status']}",
                                   "category": "uncertainty", "action": "Re-run after the starter is confirmed."})
            if gr["status"] == "PASS":
                gr["status"] = "REVIEW"
        players.append({
            "player_id": str(r.player_id), "name": r.name, "team": ab.get(int(r.team_id)), "opponent": ab.get(int(r.opp_id)),
            "game_id": str(r.game_id), "family": "saves", "mean": round(mu, 3), "median": int(gd.median[i]),
            "p10": int(gd.quantile(0.1)[i]), "p90": int(gd.quantile(0.9)[i]), "thresholds": th,
            "opportunity": {"family": "shots_against", "mean": round(float(r.sa_D), 2) if np.isfinite(r.sa_D) else None,
                            "p10": None, "p90": None},
            "opponent_adjustment": {"factor": None, "sample_games": None}, "adjustments": adj,
            "readiness": readiness.get("saves", ("SHADOW VALIDATION", ""))[0],
            "gate": {"status": gr["status"], "findings": [{k: f[k] for k in ("check", "severity", "what", "category", "action")}
                                                          for f in gr["findings"]]},
            "data_asof_utc": asof})
    games_out = []
    for g in games.itertuples():
        tl = []
        for tid in (int(g.home_team_id), int(g.away_team_id)):
            m = team_mu.get((g.game_id, tid))
            if m is None or not np.isfinite(m):
                continue
            d = ev.make(tdp, [m])
            rec = gate.team_reconciliation(recon.get((g.game_id, tid), 0.0), m, "team goals")
            tl.append({"team": ab.get(tid), "family": "team_goals", "mean": round(float(m), 3),
                       "p10": int(d.quantile(0.1)[0]), "p90": int(d.quantile(0.9)[0]),
                       "player_goal_sum": round(recon.get((g.game_id, tid), 0.0), 3),
                       "reconciliation": {"status": rec["status"], "ratio": rec.get("ratio")}})
        games_out.append({"game_id": str(g.game_id), "start_utc": g.start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                          "home": ab.get(int(g.home_team_id)), "away": ab.get(int(g.away_team_id)), "teams": tl})
    fam_meta = {}
    for k, (fam, _) in list(FAMS.items()) + [("saves", ("saves", None)), ("team_goals", ("team_goals", None))]:
        rd = readiness.get(k, ("SHADOW VALIDATION", "no research summary found"))
        fam_meta[fam] = {"readiness": rd[0], "model": {"A": "A_season_avg_shrunk", "B": "B_ewma_shrunk", "C": "C_toi_x_rate",
                                                       "D": "D_opp_adjusted", "E": "E_lightgbm", "F": "F_stack"}[best[k]],
                         "reason": rd[1]}
    payload = {
        "schema": "sift.projections.v1", "sport": "NHL",
        "generated_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "data_asof_utc": asof,
        "model": {"id": "pf-nhl", "version": f"{VERSION}+{_sha()}", "authority": "research_only"},
        "slate": {"date": date, "label": f"{date} regular-season slate projected from final games through "
                                         f"{last_final:%Y-%m-%d}; lineups/starters from the newest archived pregame "
                                         f"observation at or before {now:%Y-%m-%dT%H:%MZ}",
                  "conditioning": "skater projections are conditional on the player dressing; saves conditional on the "
                                  "listed goalie starting"},
        "families": fam_meta, "games": games_out, "players": players,
        "gate_summary": gate.summarize([{"status": p["gate"]["status"], "findings": p["gate"]["findings"]} for p in players]),
        "runtime_s": round(time.time() - t0, 1),
    }
    if out:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        json.dump(payload, open(out, "w"), indent=1, default=str)
    return payload


def _sha() -> str:
    import subprocess
    try:
        return subprocess.check_output(["git", "-C", str(PF), "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--now")
    ap.add_argument("--out", default=str(PF / "results" / "projections_latest.json"))
    a = ap.parse_args()
    p = run(a.date, a.now, a.out)
    print(json.dumps({"games": len(p["games"]), "players": len(p["players"]), "gate": p["gate_summary"]["status_counts"],
                      "runtime_s": p["runtime_s"]}))
