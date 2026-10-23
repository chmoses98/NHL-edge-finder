"""NHL live shadow operation: availability capture, point-in-time projection archive, results, settlement, scoring.

The data-archive fixture under tests/fixtures/nhl_live is a slice of REAL recorded capture-worker output (two games of
2026-10-15: DailyFaceoff lines and goalie observations, ESPN injuries, PLAYER_SIM_V1 predictions, the final box scores).
The frozen walk-forward models (30-40 min) are replaced by a stub that returns well-formed pmfs, so these tests exercise
everything AROUND the model; the model path itself is run for real by nhl/live/smoke.py and by the workflow.
"""
import copy
import gzip
import json
import shutil
import subprocess
import sys
from datetime import timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

PF = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PF))

from pf_core import archive_guard, availability as av, dists, prospective as pr  # noqa: E402

from nhl import data  # noqa: E402
from nhl.live import availability as A, common as C, forecast as FC, model as M, results as R, scoring as S  # noqa: E402

FIX = PF / "tests" / "fixtures" / "nhl_live" / "data_archive"
GAMES = (2026020108, 2026020109)
START = "2026-10-15T23:00:00Z"
PRE = "2026-10-15T20:00:00Z"        # a run at 16:00 ET
POST = "2026-10-16T09:00:00Z"        # the morning settle run
ROOT = PF.parents[1]


@pytest.fixture()
def env(tmp_path, monkeypatch):
    dar = tmp_path / "data_archive"
    shutil.copytree(FIX, dar)
    monkeypatch.setattr(data, "ARCHIVE", dar)
    monkeypatch.setattr(M, "TABLES", tmp_path / "tables")
    data.set_repair_starters(True)
    data.set_cutoff(None)
    arch = tmp_path / "projection_data"
    arch.mkdir()
    subprocess.run(["git", "init", "-q", str(arch)], check=True)
    yield {"dar": str(dar), "arch": str(arch), "work": str(tmp_path / "work"), "tmp": tmp_path}
    data.set_cutoff(None)
    data.set_repair_starters(False)
    data.set_future({})


def stub_compute(games, lu, gs, slate_date, asof, key, log=print):
    """Stand-in for the 30-40 minute model run: same table schema, deterministic Poisson/NB pmfs."""
    rng = np.random.default_rng(1)
    sk = {}
    for r in lu.itertuples():
        e = {"game_id": int(r.game_id), "player_id": int(r.player_id), "team_id": int(r.team_id), "is_home": bool(r.is_home),
             "opp_id": int(games.loc[games.game_id == r.game_id, "away_team_id" if r.is_home else "home_team_id"].iloc[0]),
             "name": r.name, "toi_E": 17.0, "toi_pp_E": 2.0, "toi_n": 40.0, "b2b": 0, "hist_toi": [17.0] * 10, "hist": {}, "stats": {}}
        for stat, (fam, rungs) in {"sog": ("shots", [2, 3]), "goals": ("goals", [1, 2]), "assists": ("assists", [1, 2]),
                                   "points": ("points", [1, 2])}.items():
            mu = {"sog": 2.4, "goals": 0.3, "assists": 0.4, "points": 0.7}[stat] * rng.uniform(0.8, 1.2)
            d = dists.poisson(np.array([mu]), K=20)
            e["hist"][stat] = [mu] * 10
            e["stats"][stat] = {"family": fam, "model": "F_stack", "mu": float(d.mean[0]), "probs": d.P[0].tolist(),
                                "median": int(d.median[0]), "p10": int(d.quantile(0.1)[0]), "p90": int(d.quantile(0.9)[0]),
                                "sd": float(np.sqrt(d.var[0])), "thresholds": {str(k): round(float(d.prob_ge(k)[0]), 4) for k in rungs},
                                "oppf": 1.0}
        sk[(int(r.game_id), int(r.player_id))] = e
    gl = {}
    for r in gs.itertuples():
        d = dists.poisson(np.array([26.0]), K=70)
        gl[(int(r.game_id), int(r.player_id))] = {
            "game_id": int(r.game_id), "player_id": int(r.player_id), "team_id": int(r.team_id), "name": r.name, "family": "saves",
            "opp_id": int(games.loc[games.game_id == r.game_id, "away_team_id" if r.is_home else "home_team_id"].iloc[0]),
            "model": "F_stack", "mu": 26.0, "probs": d.P[0].tolist(), "median": 26, "p10": 20, "p90": 32,
            "thresholds": {"20": 0.9, "25": 0.6, "30": 0.2}, "sa_D": 28.0, "saves_n": 30}
    tm = {}
    for g in games.itertuples():
        for tid in (int(g.home_team_id), int(g.away_team_id)):
            d = dists.poisson(np.array([3.0]), K=16)
            tm[(int(g.game_id), tid)] = {"game_id": int(g.game_id), "team_id": tid, "model": "F_stack", "mu": 3.0,
                                         "probs": d.P[0].tolist(), "p10": 1, "p90": 5, "median": 3}
    fam = {f: {"readiness": "SHADOW VALIDATION", "model": "F_stack", "reason": "stub"} for f in
           ("shots", "goals", "assists", "points", "team_goals")}
    fam["saves"] = {"readiness": "NEEDS IMPROVEMENT", "model": "F_stack", "reason": "stub"}
    return {"key": key, "slate_date": slate_date, "asof": asof, "last_final": "2026-10-14", "rq": [-3.0, 3.0], "families": fam,
            "skaters": sk, "goalies": gl, "teams": tm, "skater_keys": sorted(sk), "goalie_keys": sorted(gl), "code": "stub",
            "pf_core": "1.2.0", "version": "stub", "runtime_s": 0.0}


def do_capture(env, now=PRE):
    return A.ingest_archive(env["dar"], env["arch"], C.parse_ts(now), 48)


def do_project(env, monkeypatch, now=PRE, date=None):
    monkeypatch.setattr(M, "compute", stub_compute)
    return FC.run_project(env["dar"], env["arch"], C.parse_ts(now), env["work"], date, log=lambda m: None)


# --------------------------------------------------------------------------- availability capture
def test_capture_maps_real_rows_with_certainty_and_never_upgrades(env):
    st = do_capture(env)
    assert st["lines"]["written"] > 0 and st["goalies"]["written"] > 0 and st["injuries"]["written"] > 0
    rows = pd.DataFrame(av.load_snapshots(env["arch"], "NHL"))
    assert set(rows["sport"]) == {"NHL"}
    kinds = rows.groupby(["source", "kind", "status", "certainty"]).size()
    # lines are PROJECTED, ESPN REPORTED, DailyFaceoff goalie "Confirmed" CONFIRMED, everything else PROJECTED; nothing official
    assert set(rows[rows.source == "dailyfaceoff_lines"]["certainty"]) == {"PROJECTED"}
    assert set(rows[rows.source == "espn_injuries"]["certainty"]) == {"REPORTED"}
    g = rows[rows.source == "dailyfaceoff_goalies"]
    assert set(g[g.certainty == "CONFIRMED"]["status"]) == {"STARTING"}
    assert set(g[g.certainty == "PROJECTED"]["status"]) == {"PROBABLE"}
    assert (g[g.certainty == "CONFIRMED"]["detail"].map(lambda d: d["dfo_status"]) == "CONFIRMED").all()
    assert not (rows["certainty"] == "CONFIRMED").loc[rows.source != "dailyfaceoff_goalies"].any()
    # every observation: provenance, event, entity, team; fetched before the event start; the stated source time never after our fetch
    assert rows[["source_url", "captured_utc", "event_id", "event_start_utc", "entity_id", "entity_name", "team"]].notna().all().all()
    assert (pd.to_datetime(rows["captured_utc"]) < pd.to_datetime(rows["event_start_utc"])).all()
    su = rows.dropna(subset=["source_updated_utc"])
    assert (pd.to_datetime(su["source_updated_utc"]) <= pd.to_datetime(su["captured_utc"])).all()
    assert set(rows["event_id"]) <= {str(g) for g in GAMES}
    assert len(kinds) >= 5


def test_capture_is_idempotent_and_files_are_write_once(env):
    do_capture(env)
    files = sorted(Path(env["arch"]).rglob("*.jsonl.gz"))
    again = do_capture(env)
    assert again["written"] == 0
    assert sorted(Path(env["arch"]).rglob("*.jsonl.gz")) == files


def test_unresolvable_names_are_dropped_not_guessed(env):
    ref = A.player_ref()
    assert ref.resolve("Nobody Atall", 7)[0] is None
    pid, how = ref.resolve("Auston Matthews", 10)
    assert pid == 8479318 and how in ("name_team", "name_only")


def obs(**kw):
    base = dict(sport="NHL", event_id="1", event_start_utc="2026-10-15T23:00:00Z", entity_id="9", entity_name="X", team="TOR",
                kind="line", status="ACTIVE", certainty="PROJECTED", source="dailyfaceoff_lines",
                captured_utc="2026-10-15T18:00:00Z", detail={})
    base.update(kw)
    return av.Observation(**base)


def resolve(rows, cutoff="2026-10-15T20:00:00Z", **kw):
    rows = [o.__dict__ for o in rows]
    lat = av.asof(rows, cutoff)
    return A.participation(lat, "1", "9", cutoff, idx=A.capture_index(rows), **kw)


def test_participation_rules():
    assert resolve([]).status == av.UNVERIFIED
    assert resolve([obs()]).status == av.LIKELY_ACTIVE
    assert resolve([obs(detail={"game_time_decision": True})]).status == av.UNCERTAIN
    out = obs(kind="injury", status="OUT", certainty="REPORTED", source="espn_injuries", captured_utc="2026-10-15T19:00:00Z")
    assert resolve([out]).status == av.CONFIRMED_OUT
    # a later ESPN capture that no longer lists him clears the designation
    other = obs(entity_id="77", kind="injury", status="OUT", certainty="REPORTED", source="espn_injuries",
                captured_utc="2026-10-15T19:30:00Z")
    assert resolve([out, other]).status == av.UNVERIFIED
    assert resolve([obs(captured_utc="2026-10-15T17:00:00Z"), out, other]).status == av.LIKELY_ACTIVE
    # a lineup slot captured after an unofficial OUT contradicts it: uncertain, never confirmed out, never confirmed active
    p = resolve([out, obs(captured_utc="2026-10-15T19:30:00Z")])
    assert p.status == av.UNCERTAIN and any("contradicts" in r for r in p.reasons)
    # official scratch is final
    scratch = obs(kind="lineup", status="INACTIVE", certainty="CONFIRMED", source="nhl_api_pbp_rosterspots",
                  captured_utc="2026-10-15T21:30:00Z")
    assert resolve([obs(captured_utc="2026-10-15T21:00:00Z"), scratch], cutoff="2026-10-15T22:00:00Z").status == av.CONFIRMED_OUT
    # nothing captured at/after the start is ever used
    late = obs(kind="lineup", status="INACTIVE", certainty="CONFIRMED", captured_utc="2026-10-15T23:30:00Z")
    assert resolve([obs(), late], cutoff="2026-10-16T01:00:00Z").status != av.CONFIRMED_OUT
    # DailyFaceoff injured list caps a projected-active skater
    dfo = obs(kind="injury", status="QUESTIONABLE", source="dailyfaceoff_lines", captured_utc="2026-10-15T18:30:00Z",
              detail={"dfo_injury_status": "dtd"})
    assert resolve([obs(), dfo]).status == av.UNCERTAIN


def test_official_roster_parser_on_real_pbp_payload():
    d = json.load(open(ROOT / "docs" / "probe" / "samples" / "player_game" / "nhl_pbp_2025020001.json"))
    cand = {13: {"1": "Scratch Candidate"}}
    # the recorded payload is a FINAL game: rejected as not pregame
    o, st = A.roster_spots_observations(d, C.parse_ts("2026-10-15T21:00:00Z"), cand, C.abbrev_by_id(), START)
    assert o == [] and "not pregame" in st["rejected_reason"]
    d["gameState"] = "FUT"   # same real structure, pregame state
    o, st = A.roster_spots_observations(d, C.parse_ts("2026-10-15T21:00:00Z"), cand, C.abbrev_by_id(), START)
    assert st["teams_accepted"] == 2 and st["dressed_obs"] == 36
    assert {x.certainty for x in o} == {"CONFIRMED"}
    assert [x.status for x in o if x.entity_id == "1"] == ["INACTIVE"]
    assert not any(x.entity_name == "" for x in o)
    # goalies are never confirmed from "dressed"
    assert all(x.entity_id not in {str(s["playerId"]) for s in d["rosterSpots"] if s["positionCode"] == "G"} for x in o)
    # a half-posted or full-roster payload is rejected, never turned into scratches
    short = copy.deepcopy(d)
    short["rosterSpots"] = [s for s in short["rosterSpots"] if not (s["teamId"] == 13 and s["positionCode"] != "G")][:-3]
    o, st = A.roster_spots_observations(short, C.parse_ts("2026-10-15T21:00:00Z"), cand, C.abbrev_by_id(), START)
    assert st["teams_rejected"] >= 1 and not any(x.entity_id == "1" for x in o)


def test_start_probability_is_a_shrunk_empirical_rate():
    tab = {"PROJECTED": {"0-3h": {"n": 10, "hits": 10, "p": 0.95}, "3-8h": {"n": 19, "hits": 17, "p": 0.8966}}}
    p, why = A.p_start(tab, "PROJECTED", 2.0)
    assert p == 0.95 and "10/10" in why
    assert A.p_start(tab, None, 2.0)[0] is None
    p, why = A.p_start(tab, "CONFIRMED", 2.0)          # nothing observed for this status yet: the prior, and it says so
    assert p == 0.9 and "prior only" in why


def test_live_fetch_paths_on_recorded_pages_and_a_failing_source_does_not_abort_the_rest(env):
    from nhl.live import fetch as F
    samples = ROOT / "docs" / "probe" / "samples"
    fetched = "2026-10-15T20:00:05Z"

    def get(url, headers=None):
        if "starting-goalies" in url:
            return (samples / "dailyfaceoff_goalies_date.html").read_bytes(), fetched
        if "espn.com" in url:
            raise RuntimeError("simulated outage")
        if "line-combinations" in url:
            return (samples / "player_sources" / "dfo_lines_boston-bruins.html").read_bytes(), fetched
        if "play-by-play" in url:
            d = json.load(open(samples / "player_game" / "nhl_pbp_2025020001.json"))
            d["gameState"] = "FUT"
            return json.dumps(d).encode(), fetched
        raise AssertionError(url)

    st = F.fetch_and_write(env["arch"], C.parse_ts(PRE), env["dar"], get=get)
    assert len(st["errors"]) == 1 and st["errors"][0].startswith("injuries")
    assert st["lines"]["line_obs"] > 0 and st["lines"]["page_errors"] == 0       # recorded DailyFaceoff team page parsed
    assert st["official"]["teams_accepted"] == 4 and st["official"]["states"] == {"FUT": 2}
    rows = pd.DataFrame(av.load_snapshots(env["arch"], "NHL"))
    live = rows[rows.captured_utc == fetched]
    assert set(live.source) >= {"dailyfaceoff_lines", "nhl_api_pbp_rosterspots"}       # our own fetch time is the capture time
    assert (live[live.source == "nhl_api_pbp_rosterspots"]["certainty"] == "CONFIRMED").all()


# --------------------------------------------------------------------------- project
def test_project_archives_pregame_forecasts_for_both_roles_with_participation(env, monkeypatch):
    do_capture(env)
    st = do_project(env, monkeypatch)
    assert st["slate_date"] == "2026-10-15" and st["late_rejected"] == 0
    assert st["archive"]["challenger"]["written"] > 0 and st["archive"]["incumbent"]["written"] > 0
    f = pr.load_forecasts(env["arch"], "NHL")
    assert set(f["model_role"]) == {"challenger", "incumbent"}
    assert set(f[f.model_role == "challenger"]["family"]) == {"shots", "goals", "assists", "points", "saves", "team_goals", "toi_minutes"}
    # nothing generated or archived at/after the start
    assert (pd.to_datetime(f["generated_utc"]) < pd.to_datetime(f["game_start_utc"])).all()
    assert (pd.to_datetime(f["archived_utc"]) < pd.to_datetime(f["game_start_utc"])).all()
    ch = f[f.model_role == "challenger"]
    assert ch["participation"].notna().sum() == len(ch[ch.family != "team_goals"])
    assert set(ch[ch.family != "team_goals"]["participation"]) <= set(av.PARTICIPATION)
    assert ch["gate_status"].isin(["PASS", "REVIEW", "BLOCK"]).all()
    assert (ch["role"] == "shadow").all() and (ch["authority"] == "research_only").all()
    # incumbent is archived unchanged: mean as published, ladder kept, no pmf invented
    inc = f[f.model_role == "incumbent"]
    assert (inc["model_id"] == "PLAYER_SIM_V1").all() and (inc["probs"].map(len) == 0).all()
    assert inc[inc.family == "goals"]["ladder"].map(bool).any()
    raw = C.read_kind(env["dar"], "predictions_player")
    t = raw[(raw.player_id == 8479318) & (raw.game_id.astype(str) == "2026020108") & (raw.predicted_at_utc <= PRE)]
    if len(t):
        last = t[t.predicted_at_utc == t.predicted_at_utc.max()].iloc[0]
        row = inc[(inc.entity_id == "8479318") & (inc.family == "goals")]
        assert abs(float(row["mean"].iloc[0]) - float(last["meta_expected_goals"])) < 1e-9
    # goalies: conditional on starting, published with P(start), CONFIRMED vs PROJECTED visible
    sv = ch[ch.family == "saves"]
    assert (sv["conditional_on"] == "starting").all() and sv["p_start"].notna().any()
    pj = json.load(open(Path(env["work"]) / "projection.json"))
    g = [p for p in pj["players"] if p["family"] == "saves"]
    assert all("p_start" in p and p["participation"]["status"] in av.PARTICIPATION for p in g)
    assert all(p["role"] == "shadow" and p["participation"]["captured_utc"] < START for p in pj["players"])
    assert pj["model"]["authority"] == "research_only"
    # coverage + freshness are measured
    runs = list((Path(env["arch"]) / "runs" / "nhl").rglob("*_project.json"))
    summ = json.load(open(runs[0]))
    assert summ["coverage"]["mean_coverage"] is not None and summ["coverage"]["n_events"] == 2


def test_unverified_when_no_observation_and_review_gate(env, monkeypatch):
    # capture only the goalie feed: skaters have no availability observation at all -> UNVERIFIED -> REVIEW, never "active"
    do_capture(env)
    keep = [p for p in Path(env["arch"]).rglob("*.jsonl.gz") if "dailyfaceoff_lines" in gzip.open(p, "rt").read()
            or "espn_injuries" in gzip.open(p, "rt").read()]
    for p in keep:
        p.unlink()
    st = do_project(env, monkeypatch)
    pj = json.load(open(Path(env["work"]) / "projection.json"))
    sk = [p for p in pj["players"] if p["family"] == "shots"]
    assert sk and all(p["participation"]["status"] == "UNVERIFIED" for p in sk)
    assert all(p["gate"]["status"] == "REVIEW" for p in sk)
    assert all("unverified" in " ".join(f["what"] for f in p["gate"]["findings"]).lower() for p in sk)
    assert st["lineup_info"]["teams_last_dressed"] == 4


def test_project_is_idempotent_and_never_projects_started_games(env, monkeypatch):
    do_capture(env)
    do_project(env, monkeypatch)
    n_files = len(list(Path(env["arch"]).rglob("*.jsonl.gz")))
    st2 = do_project(env, monkeypatch, now="2026-10-15T20:30:00Z")
    assert st2["archive"]["challenger"]["written"] == 0 and st2["archive"]["incumbent"]["written"] <= st2["archive"]["incumbent"]["offered"]
    assert st2["model_reused"] is True
    # incumbent snapshots are only re-archived when the incumbent itself produced a new one
    assert len(list(Path(env["arch"]).rglob("*.jsonl.gz"))) - n_files <= 1
    # after the start: no slate at all, nothing written
    before = len(list(Path(env["arch"]).rglob("*.jsonl.gz")))
    late = do_project(env, monkeypatch, now="2026-10-15T23:05:00Z")
    assert late["slate_date"] is None or late["slate_date"] > "2026-10-15"
    assert len(list(Path(env["arch"]).rglob("*.jsonl.gz"))) == before
    f = pr.load_forecasts(env["arch"], "NHL")
    assert (pd.to_datetime(f["archived_utc"]) < pd.to_datetime(f["game_start_utc"])).all()


# --------------------------------------------------------------------------- results, settle, score
def chain(env, monkeypatch):
    do_capture(env)
    do_project(env, monkeypatch)
    return R.run(env["dar"], env["arch"], C.parse_ts(POST), back_days=7)


def test_results_only_from_final_games_and_scratches_are_void(env, monkeypatch):
    do_capture(env)
    do_project(env, monkeypatch)
    # in-progress game: the schedule snapshot says not final at PRE -> nothing archived
    assert R.run(env["dar"], env["arch"], C.parse_ts(PRE), back_days=7)["written"] == 0
    st = R.run(env["dar"], env["arch"], C.parse_ts(POST), back_days=7)
    assert st["written"] > 0 and st["final_games"] == 2
    o = pd.DataFrame(pr._read(env["arch"], "outcomes", "NHL"))
    assert set(o["family"]) >= {"shots", "goals", "assists", "points", "saves", "team_goals", "toi_minutes"}
    assert o["final"].all() and set(o["participated"]) == {True, False}
    # participated False exactly for forecast keys without a box-score row with ice time
    p = data.load_kind("players")
    dressed = set(zip(p.game_id.astype(str), p.player_id.astype(str)))
    sk = o[o.family == "shots"]
    assert all(((g, e) in dressed) == bool(x) for g, e, x in zip(sk.game_id, sk.entity_id, sk.participated))
    # saves: participated == the starter
    s = o[o.family == "saves"]
    assert s[s.participated].shape[0] > 0
    # team goals equals the goals scored (box score), both teams
    tg = o[o.family == "team_goals"]
    assert len(tg) == 4 and (tg["actual"] >= 0).all()


def test_settle_once_correction_appended_original_untouched(env, monkeypatch):
    chain(env, monkeypatch)
    s1 = pr.settle(env["arch"], "NHL", now_utc=C.iso(C.parse_ts(POST)))
    assert s1["settled"] > 0 and s1["void"] > 0
    s2 = pr.settle(env["arch"], "NHL", now_utc=C.iso(C.parse_ts(POST) + timedelta(hours=1)))
    assert s2["settled"] == 0 and s2["corrections"] == 0
    # a second results run with unchanged box scores archives nothing
    assert R.run(env["dar"], env["arch"], C.parse_ts(POST) + timedelta(hours=2), back_days=7)["written"] == 0
    st = pr.load_settlements(env["arch"], "NHL")
    before = st.copy()
    # stat correction: a newer final snapshot of game 2026020108 changes one skater's goals
    src = next(Path(env["dar"], "player_events", "players").rglob("*2026020108.jsonl.gz"))
    rows = [json.loads(x) for x in gzip.open(src, "rt")]
    scorer = next(r for r in rows if r["goals"] > 0)
    for r in rows:
        r["_observed_at_utc"] = "2026-10-17T10:00:00Z"
        if r["player_id"] == scorer["player_id"]:
            r["goals"] += 1
            r["points"] += 1
    newf = src.with_name(src.name.replace("20261016T022135Z", "20261017T100000Z"))
    with gzip.open(newf, "wt") as f:
        f.write("\n".join(json.dumps(r) for r in rows))
    data.load_kind.cache_clear()
    later = C.parse_ts("2026-10-17T11:00:00Z")
    r3 = R.run(env["dar"], env["arch"], later, back_days=7)
    assert r3["changed_or_new"] == 2          # goals + points of that one skater
    s3 = pr.settle(env["arch"], "NHL", now_utc=C.iso(later))
    hit = before[(before.entity_id == str(scorer["player_id"])) & before.family.isin(["goals", "points"]) & (before.game_id == "2026020108")]
    assert len(hit) >= 2 and set(hit.family) == {"goals", "points"}
    assert s3["corrections"] == len(hit) and s3["settled"] == 0      # one correction per settled forecast (challenger and incumbent)
    after = pr.load_settlements(env["arch"], "NHL")
    pd.testing.assert_frame_equal(before.sort_values("forecast_id").reset_index(drop=True),
                                  after.sort_values("forecast_id").reset_index(drop=True))
    assert pr.settle(env["arch"], "NHL", now_utc=C.iso(later + timedelta(hours=1)))["corrections"] == 0


def test_score_promotion_status_and_segments(env, monkeypatch):
    chain(env, monkeypatch)
    pr.settle(env["arch"], "NHL", now_utc=C.iso(C.parse_ts(POST)))
    out = S.score(env["arch"], str(PF / "results" / "summary.json"), C.parse_ts(POST))
    card = json.load(open(Path(env["arch"]) / "scorecards" / "nhl" / "season.json"))
    assert card["authority"] == "research_only" and card["settlement"]["settled"] > 0
    promo = {p["family"]: p for p in card["promotion"]}
    assert set(promo) == set(S.FAM_ORDER)
    # tiny live sample -> never "better" no matter how the point estimate looks
    assert all(p["promotion_status"] in ("not yet distinguishable", "no incumbent") for p in promo.values())
    assert promo["team_goals"]["promotion_status"] == "no incumbent"
    assert "goalie_start" in card["segments"] and card["segments"]["goalie_start"]["n"] > 0
    assert (Path(env["arch"]) / "scorecards" / "nhl" / "daily.md").exists()
    md = (Path(env["arch"]) / "scorecards" / "nhl" / "weekly.md").read_text()
    assert "promotion_status" in md and "betting signal" in md
    assert set(out) == {"daily", "weekly", "season"}


def test_promotion_status_thresholds():
    assert S.status_from_ci(1000, [-0.02, -0.001]) == "better"
    assert S.status_from_ci(999, [-0.02, -0.001]) == "not yet distinguishable"
    assert S.status_from_ci(5000, [-0.02, 0.001]) == "not yet distinguishable"
    assert S.status_from_ci(1000, [0.001, 0.02]) == "worse"
    assert S.status_from_ci(0, None) == "no incumbent"


def test_promotion_better_needs_n_and_ci_on_synthetic_pairs():
    rng = np.random.default_rng(3)
    rows = []
    for g in range(400):
        for p in range(4):
            y = int(rng.poisson(0.35))
            mu_c = 0.35
            for role, mu in (("challenger", mu_c), ("incumbent", 0.5)):
                d = dists.poisson(np.array([mu]), K=8)
                rows.append({"forecast_id": f"{role}{g}{p}", "model_role": role, "family": "goals", "game_id": f"g{g}",
                             "entity_id": f"p{p}", "mean": mu, "actual": y, "void": False, "lo": 0,
                             "probs": d.P[0].tolist() if role == "challenger" else []})
    s = pd.DataFrame(rows)
    f = pd.DataFrame([{"forecast_id": r["forecast_id"], "ladder": {"1": 1 - np.exp(-0.5), "2": 1 - np.exp(-0.5) * 1.5}}
                      for r in rows if r["model_role"] == "incumbent"])
    pm = {p["family"]: p for p in S.promotion(s, f)}["goals"]
    assert pm["n_paired"] == 1600 and pm["promotion_status"] == "better" and pm["ci95"][1] < 0
    small = s[s.game_id.isin([f"g{i}" for i in range(100)])]
    ps = {p["family"]: p for p in S.promotion(small, f)}["goals"]
    assert ps["n_paired"] == 400 and ps["promotion_status"] == "not yet distinguishable"


def test_archive_guard_clean_after_full_chain_and_catches_tampering(env, monkeypatch):
    chain(env, monkeypatch)
    pr.settle(env["arch"], "NHL", now_utc=C.iso(C.parse_ts(POST)))
    S.score(env["arch"], str(PF / "results" / "summary.json"), C.parse_ts(POST))
    assert archive_guard.violations(env["arch"]) == []
    subprocess.run(["git", "-C", env["arch"], "add", "-A"], check=True)
    subprocess.run(["git", "-C", env["arch"], "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"], check=True)
    # a rerun of every stage adds nothing
    pr.settle(env["arch"], "NHL", now_utc=C.iso(C.parse_ts(POST) + timedelta(hours=3)))
    assert archive_guard.violations(env["arch"]) == []
    victim = next(Path(env["arch"], "forecasts").rglob("*.jsonl.gz"))
    victim.write_bytes(b"tampered")
    assert archive_guard.violations(env["arch"])


def test_runner_cli_dry_run_writes_nothing_to_the_archive_and_reports_stages(env, monkeypatch, capsys):
    from nhl.live import run as RUN
    monkeypatch.setattr(M, "compute", stub_compute)
    args = ["--stage", "all", "--archive", env["arch"], "--data-archive", env["dar"], "--now", PRE, "--dry-run", "--work", env["work"]]
    assert RUN.main(args) == 0
    out = capsys.readouterr().out
    for st in ("capture", "project", "publish", "results", "settle", "score", "guard"):
        assert f"[{st}]" in out
    assert [p for p in Path(env["arch"]).rglob("*") if ".git" not in p.parts and p.is_file()] == []   # temp copy only
    assert RUN.main(["--stage", "nonsense", "--archive", env["arch"], "--data-archive", env["dar"]]) == 2
    # a failing stage fails the run (and stops it): results before anything exists
    def boom(*a, **k):
        raise RuntimeError("boom")
    monkeypatch.setattr(A, "ingest_archive", boom)
    assert RUN.main(["--stage", "capture,project", "--archive", env["arch"], "--data-archive", env["dar"], "--now", PRE,
                     "--work", env["work"]]) == 1


# --------------------------------------------------------------------------- 2026-27 starter-flag repair
def test_starter_repair_matches_flag_where_present_and_fills_the_rest(env):
    data.set_repair_starters(False)
    raw = data.load_kind("goalies")
    raw = raw[raw.game_id.isin(GAMES)]
    data.set_repair_starters(True)
    fixed = data.load_kind("goalies")
    fixed = fixed[fixed.game_id.isin(GAMES)]
    flagged_before = raw[raw.starter][["game_id", "player_id"]]
    assert set(map(tuple, flagged_before.values)) <= set(map(tuple, fixed[fixed.starter][["game_id", "player_id"]].values))
    assert (fixed.groupby(["game_id", "team_id"])["starter"].sum() == 1).all()


# --------------------------------------------------------------------------- workflow
def test_workflow_contract():
    d = yaml.safe_load((ROOT / ".github" / "workflows" / "projection-foundation.yml").read_text())
    on = d.get("on", d.get(True))
    assert {"schedule", "workflow_dispatch", "pull_request"} <= set(on)
    assert on["pull_request"]["paths"] == ["research/projection_foundation/**", ".github/workflows/projection-foundation.yml"]
    assert "dry_run" in on["workflow_dispatch"]["inputs"]
    text = (ROOT / ".github" / "workflows" / "projection-foundation.yml").read_text()
    assert "secrets." not in text
    jobs = d["jobs"]
    assert all("timeout-minutes" in j for j in jobs.values())
    pr_job, live = jobs["pr-dry-run"], jobs["live"]
    assert pr_job["permissions"] == {"contents": "read"} and live["permissions"] == {"contents": "write"}
    pr_runs = " ".join(s.get("run", "") for s in pr_job["steps"])
    assert "--dry-run" in pr_runs and "git push" not in pr_runs and "ci_publish" not in pr_runs
    assert "ci_publish.sh" in " ".join(s.get("run", "") for s in live["steps"])
    assert "run_id" in d["concurrency"]["group"] and "pull_request" in d["concurrency"]["group"]
    assert "projection-foundation-nhl'" in live["concurrency"]["group"] and live["concurrency"]["cancel-in-progress"] is False
    # pregame slots 10:00 / 16:00 / 18:00 ET (EDT + EST variants) and a morning settle
    crons = [s["cron"] for s in on["schedule"]]
    hours = sorted({c.split()[1] for c in crons})
    assert hours == ["10", "11", "14", "15", "20", "21", "22", "23"]
    for sh in ("ci_data_archive.sh", "ci_projection_data.sh", "ci_publish.sh"):
        assert subprocess.run(["bash", "-n", str(PF / "nhl" / "live" / sh)]).returncode == 0
