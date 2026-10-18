"""Real-data replay smoke test of the whole live chain (runs the REAL frozen models, ~35-60 min on a shared box).

    cd research/projection_foundation
    python -m nhl.live.smoke --date 2026-10-15 --data-archive .cache/archive_wt --out .cache/smoke

Replays one past slate exactly as the scheduled runs would have seen it, using only recorded data (the capture worker's
DailyFaceoff / ESPN / PLAYER_SIM_V1 archive and the final box scores): three pregame runs (10:00, 16:00, 18:30 ET) with the
clock set by `--now`, a run after the first puck drop, the morning settle run, a rerun of every stage (idempotency), and a
simulated stat correction. Each step is committed to a scratch git repo (as the workflow does) and `archive_guard` must stay
clean. The assertions are the acceptance criteria of the brief; the report is written to <out>/smoke_report.json.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

PF = Path(__file__).resolve().parents[2]
if str(PF) not in sys.path:
    sys.path.insert(0, str(PF))


def sh(*a, cwd=None):
    subprocess.run(a, cwd=cwd, check=True, capture_output=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-15", help="ET slate date to replay (its games must be final in the archive), or 'auto'")
    ap.add_argument("--data-archive", default=str(PF / ".cache" / "archive_wt"))
    ap.add_argument("--out", default=str(PF / ".cache" / "smoke"))
    ap.add_argument("--keep-models", action="store_true", help="reuse an existing model table in <out>/models")
    a = ap.parse_args(argv)
    out = Path(a.out)
    arch = out / "projection_data"
    if arch.exists():
        shutil.rmtree(arch)
    if not a.keep_models and (out / "models").exists():
        shutil.rmtree(out / "models")
    for p in (arch, out / "work", out / "models", out / "frames"):
        p.mkdir(parents=True, exist_ok=True)
    os.environ["NHL_PF_ARCHIVE"] = a.data_archive
    os.environ["NHL_PF_CACHE"] = str(out / "frames")
    os.environ["NHL_PF_MODELS"] = str(out / "models")
    sh("git", "init", "-q", str(arch))

    import pandas as pd

    from nhl.live import common as C
    from nhl.live import run as RUN
    from pf_core import prospective as pr

    dar = a.data_archive
    if a.date == "auto":     # newest ET date at least two days old with at least one game the archive's own schedule shows as final by the morning settle
        s_all = C.schedule_asof(dar, C.now_utc(), back_days=10)
        s_all = s_all[s_all["game_id"].map(C.is_regular)]
        cutoff = C.et_date(C.now_utc() - pd.Timedelta(days=2))

        def settled_by_morning(d):
            g = s_all[s_all["game_date_et"] == d]
            seen = C.schedule_asof(dar, g["start"].max() + pd.Timedelta(hours=14), back_days=16)
            st = seen[seen["game_id"].isin(g["game_id"])].set_index("game_id")["status"]
            return bool((st == "final").any())   # a slate still "live" in the last schedule capture has nothing to settle

        a.date = max(d for d in s_all["game_date_et"].unique() if d <= cutoff and settled_by_morning(d))
    day = a.date
    sched = C.schedule_asof(dar, C.parse_ts(f"{day}T20:00:00Z") + pd.Timedelta(days=3), back_days=20)
    games = sched[(sched["game_date_et"] == day) & sched["game_id"].map(C.is_regular)].sort_values("start")
    assert len(games), f"no games on {day} in the archive"
    first = games["start"].iloc[0]
    t_pre = [first - pd.Timedelta(hours=9), first - pd.Timedelta(hours=3), first - pd.Timedelta(minutes=30)]   # ~10:00 / 16:00 / 18:30 ET
    t_after = first + pd.Timedelta(minutes=5)
    t_post = (games["start"].max() + pd.Timedelta(hours=14))
    iso = lambda t: t.strftime("%Y-%m-%dT%H:%M:%SZ")  # noqa: E731
    report: dict = {"date": day, "games": [int(g) for g in games["game_id"]], "steps": []}
    t0 = time.time()

    def step(name, stages, now, expect_fail=False):
        args = ["--stage", stages, "--archive", str(arch), "--data-archive", dar, "--now", iso(now), "--work", str(out / "work")]
        t = time.time()
        rc = RUN.main(args)
        sh("git", "add", "-A", cwd=arch)
        subprocess.run(["git", "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", name, "--allow-empty"], cwd=arch, check=True,
                       capture_output=True)
        nfiles = len(list(arch.rglob("*.jsonl.gz")))
        report["steps"].append({"name": name, "now": iso(now), "rc": rc, "seconds": round(time.time() - t, 1), "files": nfiles})
        assert (rc == 0) != expect_fail, f"{name}: rc={rc}"
        return nfiles

    # ---------------------------------------------------------------- pregame runs
    step("pregame 10:00 ET (first run of the day: computes the frozen-model table)", "capture,project,publish,results,settle,score,guard", t_pre[0])
    step("pregame 16:00 ET (table reused)", "capture,project,publish,results,settle,score,guard", t_pre[1])
    n_before = step("pregame 18:30 ET", "capture,project,publish,results,settle,score,guard", t_pre[2])
    n_again = step("18:30 ET rerun (idempotent)", "capture,project,publish,results,settle,score,guard", t_pre[2])
    report["idempotent_pregame_rerun_new_files"] = n_again - n_before
    assert n_again - n_before <= 2, "a pure rerun may only add the run-summary/scorecard views"

    f = pr.load_forecasts(str(arch), "NHL")
    ch, inc = f[f.model_role == "challenger"], f[f.model_role == "incumbent"]
    report["forecasts"] = {"challenger": int(len(ch)), "incumbent": int(len(inc)), "versions_per_key_max": int(
        ch.groupby(["game_id", "entity_id", "family"]).size().max())}
    assert len(ch) and len(inc)
    assert (pd.to_datetime(f["generated_utc"]) < pd.to_datetime(f["game_start_utc"])).all()
    assert (pd.to_datetime(f["archived_utc"]) < pd.to_datetime(f["game_start_utc"])).all()
    assert ch[ch.family != "team_goals"]["participation"].notna().all()
    report["gate_status"] = ch["gate_status"].value_counts().to_dict()
    report["participation"] = ch[ch.family != "team_goals"]["participation"].value_counts().to_dict()
    assert set(report["gate_status"]) <= {"PASS", "REVIEW", "BLOCK"}

    # ---------------------------------------------------------------- after the first puck drop: nothing for started games
    step("after first puck drop", "capture,project,publish", t_after)
    f2 = pr.load_forecasts(str(arch), "NHL")
    started = {str(int(g)) for g, s in zip(games["game_id"], games["start"]) if s <= t_after}
    late = f2[f2.game_id.isin(started) & (pd.to_datetime(f2["archived_utc"]) >= t_after - pd.Timedelta(seconds=1))]
    report["forecasts_for_started_games_after_puck_drop"] = int(len(late))
    assert len(late) == 0

    # ---------------------------------------------------------------- results / settle / score
    step("morning settle", "capture,results,settle,score,guard", t_post)
    st = pr.load_settlements(str(arch), "NHL")
    report["settlements"] = {"rows": int(len(st)), "void": int(st["void"].sum()), "by_role": st["model_role"].value_counts().to_dict()}
    assert len(st) > 0
    def n_results_files():       # a later clock legitimately captures newer availability; results/settlements must not change
        return sum(len(list((arch / d).rglob("*.jsonl.gz"))) for d in ("outcomes", "settlements", "corrections", "forecasts"))
    n1 = n_results_files()
    step("morning settle rerun (idempotent)", "capture,results,settle,score,guard", t_post + pd.Timedelta(hours=1))
    n2 = n_results_files()
    report["idempotent_settle_rerun_new_files"] = n2 - n1
    assert n2 == n1, "rerunning results/settle must add no outcome/settlement/forecast files"
    st2 = pr.load_settlements(str(arch), "NHL")
    assert len(st2) == len(st)

    # ---------------------------------------------------------------- simulated stat correction
    dar2 = out / "data_archive_corrected"
    if dar2.exists():
        shutil.rmtree(dar2)
    shutil.copytree(dar, dar2, symlinks=True)
    gid = int(games["game_id"].iloc[0])
    src = None
    for p in sorted((dar2 / "player_events" / "players").glob("dt=*/*.jsonl.gz")):
        rows = [json.loads(x) for x in gzip.open(p, "rt") if x.strip()]
        if any(r["game_id"] == gid for r in rows):
            src = (p, [r for r in rows if r["game_id"] == gid])
            break
    assert src, "game not found in player_events"
    # correct a player whose shots forecast was settled (an unforecast player has nothing to correct)
    settled_shots = set(pr.load_settlements(str(arch), "NHL").query("family == 'shots' and not void and model_role == 'challenger' "
                                                                     f"and game_id == '{gid}'")["entity_id"])
    scorer = next(r for r in src[1] if str(r["player_id"]) in settled_shots)
    new_rows = copy.deepcopy(src[1])
    for r in new_rows:
        r["_observed_at_utc"] = iso(t_post + pd.Timedelta(days=1))
        if r["player_id"] == scorer["player_id"]:
            r["sog"] += 1
    newp = src[0].with_name(src[0].name.replace(".jsonl.gz", "_corrected.jsonl.gz"))
    with gzip.open(newp, "wt") as fh:
        fh.write("\n".join(json.dumps(r) for r in new_rows))
    before = pr.load_settlements(str(arch), "NHL").copy()
    RUN_args = ["--stage", "results,settle,guard", "--archive", str(arch), "--data-archive", str(dar2),
                "--now", iso(t_post + pd.Timedelta(days=1, hours=1)), "--work", str(out / "work")]
    assert RUN.main(RUN_args) == 0
    corr = pd.DataFrame(pr._read(str(arch), "corrections", "NHL"))
    report["corrections"] = int(len(corr))
    assert len(corr) >= 1 and set(corr["family"]) == {"shots"}
    after = pr.load_settlements(str(arch), "NHL")
    pd.testing.assert_frame_equal(before.sort_values("forecast_id").reset_index(drop=True),
                                  after.sort_values("forecast_id").reset_index(drop=True))

    card = json.load(open(arch / "scorecards" / "nhl" / "season.json"))
    report["scorecard"] = {"settled": card["settlement"], "promotion": {p["family"]: [p["promotion_status"], p.get("n_paired")]
                                                                     for p in card["promotion"]},
                           "alerts": {a["family"]: a["status"] for a in card["alerts"]},
                           "capture_stats": card["capture_stats"]}
    runs = sorted((arch / "runs" / "nhl").rglob("*_project.json"))
    report["runs"] = [{"file": r.name, "model_reused": json.load(open(r))["model_reused"],
                       "coverage_mean": json.load(open(r))["coverage"]["mean_coverage"],
                       "archive": json.load(open(r))["archive"]} for r in runs]
    report["seconds"] = round(time.time() - t0, 1)
    report["ok"] = True
    (out / "smoke_report.json").write_text(json.dumps(report, indent=1, default=str))
    print(json.dumps(report, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
