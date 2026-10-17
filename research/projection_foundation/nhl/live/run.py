"""NHL Projection Foundation live runner (research only).

    cd research/projection_foundation
    python -m nhl.live.run --stage all --archive /path/to/projection-data-checkout --data-archive /path/to/data-archive-sparse \\
        [--now 2026-10-17T14:00:00Z] [--dry-run] [--live-fetch] [--work DIR]

Stages, each idempotent and runnable on its own (`--stage all` runs them in order):
  capture  data-archive DailyFaceoff / ESPN captures (+ optional live fetch) -> immutable availability snapshots
  project  next slate: frozen models (cached per slate) + participation + gate -> challenger forecasts, incumbent forecasts
  publish  projections/nhl/latest.json (+ timestamped copy) and summary/nhl/latest.json
  results  FINAL box scores -> outcome records for every archived forecast key
  settle   pf_core settle-once (+ appended corrections); void for scratches
  score    daily (7d) / weekly (28d) / season scorecards with promotion_status per family
  guard    pf_core.archive_guard: only additions to the immutable directories

`--dry-run` copies the archive to a temp directory first and writes only there. Exit status is non-zero when a stage fails.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PF = Path(__file__).resolve().parents[2]
if str(PF) not in sys.path:
    sys.path.insert(0, str(PF))
STAGES = ["capture", "project", "publish", "results", "settle", "score", "guard"]


def _args(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", default="all", help="all or a comma list of: " + ",".join(STAGES))
    ap.add_argument("--archive", required=True, help="projection-data checkout (created if missing)")
    ap.add_argument("--data-archive", default=os.environ.get("NHL_PF_ARCHIVE"), help="sparse data-archive checkout")
    ap.add_argument("--now", help="ISO UTC 'now' (tests / replay); default the real clock")
    ap.add_argument("--date", help="force the slate ET date (replay)")
    ap.add_argument("--dry-run", action="store_true", help="write only to a temp copy of the archive")
    ap.add_argument("--live-fetch", action="store_true", help="also fetch DailyFaceoff / ESPN / NHL pregame roster directly")
    ap.add_argument("--work", help="scratch dir passed between stages (default <tmp>/nhl_live_work)")
    ap.add_argument("--lookback-h", type=float, default=48.0)
    return ap.parse_args(argv)


def _emit(stage: str, d: dict) -> None:
    print(f"[{stage}] " + json.dumps(d, default=str, sort_keys=True), flush=True)
    sm = os.environ.get("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(f"**NHL live / {stage}**\n\n```json\n{json.dumps(d, indent=1, default=str, sort_keys=True)}\n```\n\n")


def main(argv=None) -> int:
    a = _args(argv)
    if a.data_archive:
        os.environ["NHL_PF_ARCHIVE"] = a.data_archive
    os.environ.setdefault("NHL_PF_CACHE", str(PF / ".cache" / "live"))
    os.environ.setdefault("NHL_PF_MODELS", str(Path(os.environ["NHL_PF_CACHE"]).parent / "model_tables"))
    from pf_core import archive_guard

    from nhl import data
    from nhl.live import availability as A
    from nhl.live import common as C
    from nhl.live import fetch as F
    from nhl.live import forecast as FC
    from nhl.live import results as R
    from nhl.live import scoring as S
    from pf_core import prospective as pr

    data.set_repair_starters(True)   # 2026-27 archive loses the starter flag for ~half the team-games (see nhl.data)
    stages = STAGES if a.stage == "all" else [s.strip() for s in a.stage.split(",")]
    bad = [s for s in stages if s not in STAGES]
    if bad:
        print(f"unknown stage(s): {bad}", file=sys.stderr)
        return 2
    now = C.now_utc(a.now)
    arch = os.path.abspath(a.archive)
    os.makedirs(arch, exist_ok=True)
    if not os.path.isdir(os.path.join(arch, ".git")):
        subprocess.run(["git", "init", "-q", arch], check=True)
    if a.dry_run:
        tmp = tempfile.mkdtemp(prefix="nhl_live_dry_")
        shutil.copytree(arch, tmp, dirs_exist_ok=True, symlinks=True)
        arch = tmp
        print(f"[dry-run] writing only to a temp copy: {arch}", flush=True)
    work = Path(a.work or os.path.join(tempfile.gettempdir(), "nhl_live_work"))
    work.mkdir(parents=True, exist_ok=True)
    dar = a.data_archive
    if not dar or not os.path.isdir(dar):
        print("--data-archive (sparse data-archive checkout) is required", file=sys.stderr)
        return 2
    summary = Path(PF / "results" / "summary.json")
    rc = 0
    t_all = time.time()
    for stage in stages:
        t0 = time.time()
        try:
            if stage == "capture":
                st = A.ingest_archive(dar, arch, now, a.lookback_h)
                if a.live_fetch:
                    st["live"] = F.fetch_and_write(arch, now, dar)
                    if st["live"].get("errors"):
                        for e in st["live"]["errors"]:
                            print(f"::warning::live fetch: {e}", flush=True)
                if st.get("error"):
                    raise RuntimeError(st["error"])
            elif stage == "project":
                def refresh(t):
                    A.ingest_archive(dar, arch, t, a.lookback_h)
                    if a.live_fetch:
                        F.fetch_and_write(arch, t, dar)
                st = FC.run_project(dar, arch, now, work, a.date, log=lambda m: print(m, flush=True),
                                    clock=None if a.now else (lambda: C.now_utc()), refresh=refresh)
            elif stage == "publish":
                st = publish_stage(arch, work, now, summary)
            elif stage == "results":
                st = R.run(dar, arch, now)
            elif stage == "settle":
                st = pr.settle(arch, C.SPORT, now_utc=C.iso(now))
            elif stage == "score":
                st = S.score(arch, str(summary), now, os.environ.get("GITHUB_STEP_SUMMARY"))
            elif stage == "guard":
                v = archive_guard.violations(arch)
                st = {"violations": v}
                if v:
                    raise RuntimeError("archive_guard: immutable files changed: " + ", ".join(v[:5]))
            st["seconds"] = round(time.time() - t0, 1)
            _emit(stage, st)
        except Exception as e:  # noqa: BLE001 - a failed stage fails the run; nothing is committed afterwards
            import traceback
            traceback.print_exc()
            print(f"::error::NHL live stage {stage} failed: {type(e).__name__}: {e}", flush=True)
            rc = 1
            break
    print(f"[done] stages={stages} rc={rc} seconds={time.time() - t_all:.0f} archive={arch}", flush=True)
    return rc


# --------------------------------------------------------------------------- publish
def publish_stage(arch: str, work: Path, now, summary: Path) -> dict:
    out = {"projection": "none this run"}
    pj = work / "projection.json"
    new = json.loads(pj.read_text()) if pj.exists() else None
    strip = lambda d: {k: v for k, v in d.items() if k not in ("generated_utc", "runtime_s")}  # noqa: E731
    if new is not None:
        dst = Path(arch) / "projections" / "nhl" / "latest.json"
        dst.parent.mkdir(parents=True, exist_ok=True)
        old = json.loads(dst.read_text()) if dst.exists() else None
        if old is None or strip(old) != strip(new):
            ts = new["generated_utc"].replace(":", "").replace("-", "")[:13] + "Z"
            for p in (dst, dst.parent / f"{ts}.json"):
                p.write_text(json.dumps(new, indent=1, default=str))
            out["projection"] = f"published {len(new['players'])} player rows / {len(new['games'])} games"
        else:
            out["projection"] = "unchanged (content identical ignoring timestamps)"
    sd = Path(arch) / "summary" / "nhl"
    sd.mkdir(parents=True, exist_ok=True)
    shutil.copy(summary, sd / "latest.json")
    out["summary"] = "summary/nhl/latest.json refreshed"
    return out


if __name__ == "__main__":
    sys.exit(main())
