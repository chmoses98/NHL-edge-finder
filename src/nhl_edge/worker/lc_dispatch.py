"""Unattended dispatch and coverage alerts for the WORKLOAD_V1_LC prospective collection (RESEARCH_ONLY).

``workload_shadow.yml`` writes a game's write-once pregame record on the first run that starts after the game enters its 14-hour horizon and at least 20 minutes
before the drop. GitHub's scheduled runs arrive hours late, so this module asks for a run the same way ``pf_dispatch`` asks for a projection refresh: from the capture
worker and from ``slate-watch``, off the platform's own record of runs. Nothing is back-filled: a game that starts without a record is reported, never repaired.

Policy (pure; see ``decide``):
* a game is *covered* when a run that created at or after ``game start - 14 h`` (and, if finished, at least ``MIN_LEAD`` before the drop) is queued, running or succeeded;
* a run is requested when an uncovered game starts within ``DISPATCH_WINDOW_H`` and at least ``MIN_LEAD`` ahead, nothing is in flight, the spacing and daily cap allow;
* ``gap`` (the only alert condition) = an uncovered game starts within ``GAP_WITHIN_MIN`` and nothing is in flight: a record is actually missing or about to be;
  an unchanged prediction is never an alert.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime, timedelta
from pathlib import Path

from nhl_edge.worker.pf_dispatch import RunInfo, _headers, list_runs_via_api

WORKFLOW = "workload_shadow.yml"
MINUTES_WORKFLOW = "player_minutes.yml"       # requested together with the LC run (best effort); never read by the decision logic
HORIZON_H = 14.0                    # keep equal to research/workload_shadow_run.HORIZON_H
DISPATCH_WINDOW_H = 4.0
MIN_LEAD_MINUTES = 20.0             # 10-minute pregame margin + runtime; a request closer than this cannot produce a countable record
GAP_WITHIN_MIN = 90.0
MIN_SPACING_MINUTES = 12.0
MAX_DISPATCHES_PER_DAY = 24
STUCK_HOURS = 3.0                   # an in-flight run older than this is treated as lost
FAILURE_BACKOFF_RUNS = 3
FAILURE_BACKOFF_MINUTES = 60.0


@dataclass(frozen=True)
class Decision:
    action: str                     # "dispatch" | "wait" | "idle"
    code: str
    reason: str
    uncovered: int = 0
    next_uncovered_in_min: float | None = None
    gap: bool = False
    recovered: bool = False
    details: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return asdict(self)


def _covered(tip: datetime, now: datetime, runs: list[RunInfo]) -> bool:
    for r in runs:
        if r.event not in ("schedule", "workflow_dispatch") or r.created_at < tip - timedelta(hours=HORIZON_H):
            continue
        if r.in_flight and (now - r.created_at) < timedelta(hours=STUCK_HOURS):
            return True
        if r.succeeded and (r.updated_at or r.created_at) <= tip - timedelta(minutes=10) and r.created_at <= tip - timedelta(minutes=10):
            return True
    return False


def decide(now: datetime, tips: list[datetime], runs: list[RunInfo], *, dispatched_today: int = 0, last_dispatch_at: datetime | None = None) -> Decision:
    ahead = sorted(t for t in tips if t > now)
    uncovered = [t for t in ahead if not _covered(t, now, runs)]
    nxt = (uncovered[0] - now).total_seconds() / 60 if uncovered else None
    in_flight = [r for r in runs if r.in_flight and (now - r.created_at) < timedelta(hours=STUCK_HOURS)]
    gap = bool(uncovered and nxt is not None and nxt <= GAP_WITHIN_MIN and not in_flight)
    recovered = not any((t - now).total_seconds() / 60 <= GAP_WITHIN_MIN for t in uncovered)
    base = dict(uncovered=len(uncovered), next_uncovered_in_min=None if nxt is None else round(nxt, 1), gap=gap, recovered=recovered)
    due = [t for t in uncovered if MIN_LEAD_MINUTES <= (t - now).total_seconds() / 60 <= DISPATCH_WINDOW_H * 60]
    if not uncovered:
        return Decision("idle", "COVERED", "every upcoming game is covered by a run that started inside its horizon", **base)
    if not due:
        too_close = [t for t in uncovered if (t - now).total_seconds() / 60 < MIN_LEAD_MINUTES]
        if too_close:
            return Decision("wait", "TOO_CLOSE", f"{len(too_close)} uncovered game(s) start in under {MIN_LEAD_MINUTES:.0f} min: a run could not produce a countable record", **base)
        return Decision("idle", "OUTSIDE_WINDOW", f"the next uncovered game starts in {nxt / 60:.1f} h (dispatch window {DISPATCH_WINDOW_H:.0f} h)", **base)
    if in_flight:
        return Decision("wait", "IN_FLIGHT", f"run #{in_flight[0].id} ({in_flight[0].status}) is already queued or running", **base)
    fails = [r for r in runs if r.status == "completed" and r.conclusion in ("failure", "timed_out")][:FAILURE_BACKOFF_RUNS]
    if len(fails) >= FAILURE_BACKOFF_RUNS and all(r.created_at > now - timedelta(hours=6) for r in fails):
        newest = max(r.updated_at or r.created_at for r in fails)
        if (now - newest) < timedelta(minutes=FAILURE_BACKOFF_MINUTES):
            return Decision("wait", "BACKOFF", f"{FAILURE_BACKOFF_RUNS} consecutive failed runs; backing off {FAILURE_BACKOFF_MINUTES:.0f} min", **base)
    if last_dispatch_at is not None and (now - last_dispatch_at) < timedelta(minutes=MIN_SPACING_MINUTES):
        return Decision("wait", "SPACING", f"last request {(now - last_dispatch_at).total_seconds() / 60:.0f} min ago", **base)
    if dispatched_today >= MAX_DISPATCHES_PER_DAY:
        return Decision("wait", "DAILY_CAP", f"{dispatched_today} requests in 24 h", **base)
    return Decision("dispatch", "DUE", f"{len(due)} game(s) in the next {DISPATCH_WINDOW_H:.0f} h have no covering run", **base)


def count_recent(runs: list[RunInfo], now: datetime) -> tuple[int, datetime | None]:
    recent = [r for r in runs if r.event == "workflow_dispatch" and (now - r.created_at) < timedelta(hours=24)]
    return len(recent), (max(r.created_at for r in recent) if recent else None)


def regular_tips_from_schedule(paths: list[Path]) -> list[datetime]:
    import gzip

    out: set[datetime] = set()
    for p in paths:
        try:
            with (gzip.open(p, "rt") if str(p).endswith(".gz") else open(p)) as f:
                for line in f:
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                        if str(row.get("season_type", "regular")).lower() in ("regular", "2") and row.get("status") in ("not_started", None):
                            out.add(datetime.fromisoformat(str(row["start_time_utc"]).replace("Z", "+00:00")).astimezone(UTC))
                    except (ValueError, TypeError, KeyError, AttributeError):
                        continue
        except OSError:
            continue
    return sorted(out)


def dispatch_via_api(repo: str, ref: str, token: str, workflow: str = WORKFLOW) -> bool:
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/dispatches", data=json.dumps({"ref": ref}).encode(), method="POST",
                                 headers={**_headers(token), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 204
    except urllib.error.HTTPError as e:
        print(f"lc_dispatch: dispatch failed HTTP {e.code}: {e.read()[:300]!r}")
    except OSError as e:
        print(f"lc_dispatch: dispatch failed: {e}")
    return False


def _dispatch_both(repo: str, ref: str, token: str) -> bool:
    """Ask for the LC run (the result that matters) and, best effort, for the player-minutes run on the same occasion; the second one's outcome never changes the first's."""
    ok = dispatch_via_api(repo, ref, token)
    if ok:
        dispatch_via_api(repo, ref, token, MINUTES_WORKFLOW)
    return ok


class LcDispatcher:
    """Per-process state around ``decide``; never raises into the caller; ``list_fn`` / ``dispatch_fn`` are injectable."""

    def __init__(self, repo: str, ref: str, token: str, *, list_fn=None, dispatch_fn=None) -> None:
        self.list_fn = list_fn or (lambda: list_runs_via_api(repo, token, workflow=WORKFLOW))
        self.dispatch_fn = dispatch_fn or (lambda: _dispatch_both(repo, ref, token))
        self._last: datetime | None = None
        self._n: list[datetime] = []

    def step(self, now: datetime, tips: list[datetime]) -> dict:
        try:
            runs = self.list_fn()
            if runs is None:
                return {"action": "wait", "code": "API_UNREADABLE", "reason": "could not read the run list; not dispatching blind"}
            n_api, last_api = count_recent(runs, now)
            self._n = [t for t in self._n if (now - t) < timedelta(hours=24)]
            last = max([t for t in (last_api, self._last) if t is not None], default=None)
            d = decide(now, tips, runs, dispatched_today=max(n_api, len(self._n)), last_dispatch_at=last)
            out = d.as_dict()
            if d.action == "dispatch":
                ok = bool(self.dispatch_fn())
                out["dispatched"] = ok
                if ok:
                    self._last = now
                    self._n.append(now)
                else:
                    out["action"], out["code"] = "wait", "DISPATCH_REFUSED"
            return out
        except Exception as e:  # noqa: BLE001 - research plumbing must never take the capture worker down
            return {"action": "wait", "code": "DISPATCHER_ERROR", "reason": f"{type(e).__name__}: {str(e)[:200]}"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.worker.lc_dispatch")
    ap.add_argument("mode", choices=("decide", "dispatch"))
    ap.add_argument("--schedule", nargs="+", required=True)
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    ap.add_argument("--ref", default=os.environ.get("GITHUB_REF_NAME", "main"))
    ap.add_argument("--now", default=None)
    ap.add_argument("--github-output", default=None)
    ap.add_argument("--drill", action="store_true", help="production drill: pretend no run covers the supplied (synthetic) game, so the REAL dispatch path (token, endpoint, workflows) is exercised")
    a = ap.parse_args(argv)
    token = os.environ.get("GITHUB_TOKEN", "")
    if not a.repo or not token:
        print("lc_dispatch: GITHUB_REPOSITORY and GITHUB_TOKEN are required", file=sys.stderr)
        return 2
    now = datetime.fromisoformat(a.now.replace("Z", "+00:00")).astimezone(UTC) if a.now else datetime.now(UTC)
    tips = regular_tips_from_schedule([Path(p) for p in a.schedule])
    disp = LcDispatcher(a.repo, a.ref, token, list_fn=(lambda: []) if a.drill else None)
    if a.drill and a.mode != "dispatch":
        print("lc_dispatch: --drill needs mode 'dispatch'", file=sys.stderr)
        return 2
    if a.mode == "dispatch":
        out = disp.step(now, tips)
    else:
        runs = disp.list_fn()
        if runs is None:
            out = {"action": "wait", "code": "API_UNREADABLE", "reason": "could not read the run list"}
        else:
            n, last = count_recent(runs, now)
            out = decide(now, tips, runs, dispatched_today=n, last_dispatch_at=last).as_dict()
    if a.drill:
        out["drill"] = True
    print(json.dumps(out, indent=1, default=str))
    if a.github_output:
        with open(a.github_output, "a") as f:
            f.write(f"lc_action={out['action']}\nlc_code={out['code']}\nlc_gap={'true' if out.get('gap') else 'false'}\nlc_recovered={'true' if out.get('recovered') else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
