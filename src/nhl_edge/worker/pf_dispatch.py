"""Worker-driven dispatch of the projection-foundation workflow (RESEARCH_ONLY; changes no model, price, stake, cap or contract).

Why this exists (measured on 2026-10-22, see docs/research/PROJECTION_DELIVERY.md): the player-layer chain
(``projection-foundation.yml``) was driven by cron slots that GitHub delivered 2.2-4.4 hours late, each slot needed two runner
requests (a ``gate`` job, then the ``live`` job) that waited 51-78 and 22 minutes for a runner, and the DST duplicates of every slot
(an EDT and an EST entry) produced no-op runs that could take the single pending concurrency slot from a real run. The capture
worker is the only component that is already running at the right moments, so it asks for the chain instead of waiting for cron.

The module is stdlib-only, like ``worker/plan.py`` and ``worker/lease.py``: the watchdog workflows import it without an install.

Policy, in one paragraph. Look at the next puck drop. Far away (> ``WINDOW_HOURS``) nothing is wanted. Closer, a run is wanted when
the newest successful run is older than a horizon-dependent interval. Never dispatch while a run is queued or in progress (a second
pending run in a concurrency group *cancels the first*, which throws away its place in the runner queue -- the opposite of what a
late slate needs). Dispatch at most every ``MIN_SPACING_MINUTES`` and ``MAX_DISPATCHES_PER_DAY`` times. A run requested too close
to a puck drop to finish in time is not requested (it could not be pregame data); the previous run is the final one. After the last
game of a slate has had time to finish, one settle-oriented run is requested. Every decision is returned with its reason, so a
skipped dispatch is as visible as a made one.
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import statistics
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime, timedelta
from pathlib import Path

PF_WORKFLOW = "projection-foundation.yml"
IN_FLIGHT = frozenset({"queued", "in_progress", "waiting", "pending", "requested"})

#: Nothing is wanted earlier than this before the next puck drop (the slate is not formed yet and goalies are unknown).
WINDOW_HOURS = 9.0
#: (hours-to-next-tip upper bound, wanted refresh interval in minutes). First matching row wins.
INTERVALS = ((1.5, 25.0), (3.0, 45.0), (6.0, 90.0), (WINDOW_HOURS, 180.0))
#: A run needs this long to run (install + chain) once it has a runner; used to decide that a request is too late to be pregame.
NOMINAL_RUNTIME_MINUTES = 8.0
#: Never request a run that cannot possibly finish before the next puck drop (queue latency taken at its observed median).
MIN_LEAD_MINUTES = 15.0
MIN_SPACING_MINUTES = 12.0
#: "Late delivery" threshold for the watchdog: a puck drop within STALE_WITHIN_HOURS and no successful run for this long.
STALE_MINUTES = 240.0
STALE_WITHIN_HOURS = 1.5
MAX_DISPATCHES_PER_DAY = 18
#: A queued/in-progress run older than this is treated as lost (the platform cancels at 24 h; the chain's own timeout is 150 min).
STUCK_HOURS = 6.0
#: One settle-oriented run this long after a slate's last scheduled start (regulation + OT/SO + box score availability).
SETTLE_AFTER_LAST_TIP_HOURS = 3.75
SETTLE_STAGES = "capture,results,settle,score,guard"
PREGAME_STAGES = "all"


@dataclass(frozen=True)
class RunInfo:
    id: int
    status: str
    conclusion: str | None
    event: str
    created_at: datetime
    updated_at: datetime | None
    title: str = ""        # the workflow's ``run-name``: "projection-foundation <event> [stages] [dry-run]"

    @property
    def dry_run(self) -> bool:
        return "dry-run" in self.title

    @property
    def projects(self) -> bool:
        """Whether the run refreshed projections (stages ``all`` or including ``project``). A title with no ``[stages]`` is a cron/default run: ``all``."""
        if "[" not in self.title:
            return True
        stages = self.title.split("[", 1)[1].split("]", 1)[0]
        return stages.strip() in ("", "all") or "project" in [x.strip() for x in stages.split(",")]

    @property
    def in_flight(self) -> bool:
        return self.status in IN_FLIGHT

    @property
    def succeeded(self) -> bool:
        return self.status == "completed" and self.conclusion == "success"

    def e2e_minutes(self) -> float | None:
        """Request-to-completion time of a finished run (queue wait + runtime): what a dispatch really costs in latency."""
        if self.status != "completed" or self.updated_at is None:
            return None
        return max(0.0, (self.updated_at - self.created_at).total_seconds() / 60.0)

    def data_asof(self) -> datetime | None:
        """Best estimate of the instant the run read its inputs: completion minus the nominal runtime (never before creation)."""
        if self.updated_at is None:
            return None
        return max(self.created_at, self.updated_at - timedelta(minutes=NOMINAL_RUNTIME_MINUTES))


@dataclass(frozen=True)
class Decision:
    action: str          # "dispatch" | "wait" | "idle"
    code: str            # stable machine-readable reason
    reason: str          # human sentence
    stages: str = PREGAME_STAGES
    hours_to_next_tip: float | None = None
    wanted_interval_min: float | None = None
    last_success_age_min: float | None = None
    median_e2e_min: float | None = None
    #: True when a puck drop is close, nothing is in flight and the newest successful run is older than STALE_MINUTES (or absent):
    #: the delivery is late and a human-visible alert is warranted. Independent of ``action``.
    stale: bool = False
    #: True when a projection-refreshing run succeeded within STALE_MINUTES: the only condition under which a "late delivery" alert may close.
    recovered: bool = False
    details: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return asdict(self)


def _dt(s: str | None) -> datetime | None:
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(UTC)


def parse_runs(payload: dict) -> list[RunInfo]:
    """GitHub ``workflow runs`` JSON -> RunInfo, newest first. Malformed rows, pull-request runs and dry runs are dropped, never raised on."""
    out: list[RunInfo] = []
    for r in payload.get("workflow_runs") or []:
        try:
            created = _dt(r["created_at"])
            if created is None:
                continue
            ri = RunInfo(int(r["id"]), str(r.get("status") or ""), r.get("conclusion"), str(r.get("event") or ""), created, _dt(r.get("updated_at")),
                         str(r.get("display_title") or r.get("name") or ""))
            # pull-request dry runs and human dry runs write nothing: they are neither "in flight" work nor a fresh projection, and they must
            # not count against the dispatch cap
            if ri.event in ("schedule", "workflow_dispatch") and not ri.dry_run:
                out.append(ri)
        except (KeyError, TypeError, ValueError):
            continue
    out.sort(key=lambda x: x.created_at, reverse=True)
    return out


def median_e2e_minutes(runs: list[RunInfo], n: int = 6) -> float | None:
    """Median request-to-completion of the last ``n`` successful runs (None when there is no history)."""
    vals = [m for m in (r.e2e_minutes() for r in runs if r.succeeded and r.projects) if m is not None][:n]
    return statistics.median(vals) if vals else None


def wanted_interval_minutes(hours_to_tip: float) -> float | None:
    for upper, minutes in INTERVALS:
        if hours_to_tip <= upper:
            return minutes
    return None


def _next_tip(now: datetime, tips: list[datetime]) -> datetime | None:
    up = sorted(t for t in tips if t > now)
    return up[0] if up else None


def decide(
    now: datetime,
    tips: list[datetime],
    runs: list[RunInfo],
    *,
    dispatched_today: int = 0,
    last_dispatch_at: datetime | None = None,
) -> Decision:
    """Pure decision: should the projection chain be requested now? ``tips`` are all start times of the current and next slate."""
    d = _decide(now, tips, runs, dispatched_today=dispatched_today, last_dispatch_at=last_dispatch_at)
    now = now.astimezone(UTC)
    ok = next((r for r in runs if r.succeeded and r.projects), None)
    asof = ok.data_asof() if ok else None
    recovered = asof is not None and (now - asof) <= timedelta(minutes=STALE_MINUTES)
    nxt = _next_tip(now, tips)
    stale = bool(nxt is not None and (nxt - now) <= timedelta(hours=STALE_WITHIN_HOURS) and not any(r.in_flight and (now - r.created_at) < timedelta(hours=STUCK_HOURS) for r in runs)
                 and not recovered)
    return Decision(**{**d.__dict__, "stale": stale, "recovered": recovered})


def _decide(
    now: datetime,
    tips: list[datetime],
    runs: list[RunInfo],
    *,
    dispatched_today: int = 0,
    last_dispatch_at: datetime | None = None,
) -> Decision:
    now = now.astimezone(UTC)
    med = median_e2e_minutes(runs)
    in_flight = [r for r in runs if r.in_flight and (now - r.created_at) < timedelta(hours=STUCK_HOURS)]
    last_any = next((r for r in runs if r.succeeded), None)                       # any stages: covers "was the slate settled"
    last_any_asof = last_any.data_asof() if last_any else None
    last_ok = next((r for r in runs if r.succeeded and r.projects), None)         # refreshed projections: drives pregame freshness
    last_ok_asof = last_ok.data_asof() if last_ok else None
    age = (now - last_ok_asof).total_seconds() / 60.0 if last_ok_asof else None
    nxt = _next_tip(now, tips)
    h = (nxt - now).total_seconds() / 3600.0 if nxt else None
    base = dict(hours_to_next_tip=h, last_success_age_min=age, median_e2e_min=med)

    # settle-oriented run once the slate has had time to finish; only if no successful run has started since that moment
    past = sorted(t for t in tips if t <= now)
    if past and (nxt is None or h is None or h > 0.25):
        settle_due_at = past[-1] + timedelta(hours=SETTLE_AFTER_LAST_TIP_HOURS)
        if now >= settle_due_at and (last_any_asof is None or last_any_asof < settle_due_at):
            if in_flight:
                return Decision("wait", "SETTLE_WAIT_IN_FLIGHT", f"settle run is due but run #{in_flight[0].id} ({in_flight[0].status}) is already in flight", SETTLE_STAGES, **base)
            gate = _backoff(runs, now) or _throttle(now, dispatched_today, last_dispatch_at)
            if gate:
                return Decision("wait", gate[0], gate[1], SETTLE_STAGES, **base)
            return Decision("dispatch", "SETTLE_DUE", f"slate finished (last start {past[-1].isoformat()}) and no successful run since {settle_due_at.isoformat()}", SETTLE_STAGES, **base)

    if nxt is None or h is None:
        return Decision("idle", "NO_UPCOMING_GAME", "no upcoming puck drop", **base)
    want = wanted_interval_minutes(h)
    if want is None:
        return Decision("idle", "OUTSIDE_WINDOW", f"next puck drop is {h:.1f} h away (window {WINDOW_HOURS:.0f} h)", **base, wanted_interval_min=None)
    base["wanted_interval_min"] = want
    if in_flight:
        r = in_flight[0]
        return Decision("wait", "IN_FLIGHT", f"run #{r.id} is {r.status} since {r.created_at.isoformat()}; a second request would replace it in the queue", **base)
    lead = max(MIN_LEAD_MINUTES, NOMINAL_RUNTIME_MINUTES + min(med or 0.0, 20.0))
    if h * 60.0 < lead and last_ok is not None:
        return Decision("idle", "TOO_LATE_FOR_PREGAME", f"puck drop in {h * 60:.0f} min; a run requested now would not finish first (lead {lead:.0f} min); the previous run is the final one", **base)
    if age is not None and age < want:
        return Decision("idle", "FRESH_ENOUGH", f"newest successful run is {age:.0f} min old (< {want:.0f} min wanted at T-{h:.1f} h)", **base)
    gate = _backoff(runs, now) or _throttle(now, dispatched_today, last_dispatch_at)
    if gate:
        return Decision("wait", gate[0], gate[1], **base)
    why = "no successful run on record" if age is None else f"newest successful run is {age:.0f} min old (>= {want:.0f} min wanted at T-{h:.1f} h)"
    return Decision("dispatch", "REFRESH_DUE", why, PREGAME_STAGES, **base)


FAILURE_BACKOFF_RUNS = 3
FAILURE_BACKOFF_MINUTES = 90.0


def _backoff(runs: list[RunInfo], now: datetime) -> tuple[str, str] | None:
    """A chain that keeps failing is not re-requested every few minutes (each attempt can hold a runner for up to 150 min and the daily cap would
    be spent on a bug): after ``FAILURE_BACKOFF_RUNS`` consecutive failed runs, wait ``FAILURE_BACKOFF_MINUTES`` from the newest failure.
    Cancelled runs (the gate's own no-op marker, a replaced pending run) are not failures."""
    done = [r for r in runs if r.status == "completed" and r.conclusion in ("success", "failure", "timed_out")]
    last = done[:FAILURE_BACKOFF_RUNS]
    if len(last) == FAILURE_BACKOFF_RUNS and all(r.conclusion != "success" for r in last) and last[0].updated_at is not None:
        since = (now - last[0].updated_at).total_seconds() / 60.0
        if since < FAILURE_BACKOFF_MINUTES:
            return "FAILURE_BACKOFF", f"the last {FAILURE_BACKOFF_RUNS} runs failed; waiting {FAILURE_BACKOFF_MINUTES - since:.0f} more min before another request"
    return None


def _throttle(now: datetime, dispatched_today: int, last_dispatch_at: datetime | None) -> tuple[str, str] | None:
    if dispatched_today >= MAX_DISPATCHES_PER_DAY:
        return "DAILY_CAP", f"already {dispatched_today} dispatches in the last 24 h (cap {MAX_DISPATCHES_PER_DAY})"
    if last_dispatch_at is not None and (now - last_dispatch_at) < timedelta(minutes=MIN_SPACING_MINUTES):
        return "SPACING", f"last dispatch {(now - last_dispatch_at).total_seconds() / 60:.0f} min ago (< {MIN_SPACING_MINUTES:.0f})"
    return None


def count_recent_dispatches(runs: list[RunInfo], now: datetime) -> tuple[int, datetime | None]:
    """Dispatch-event runs created in the last 24 h and the newest creation time (the platform's record of what we requested)."""
    recent = [r for r in runs if r.event == "workflow_dispatch" and (now - r.created_at) < timedelta(hours=24)]
    return len(recent), (max(r.created_at for r in recent) if recent else None)


# ----------------------------------------------------------------------------------------------------- GitHub API (stdlib)
def _headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}


def list_runs_via_api(repo: str, token: str, workflow: str = PF_WORKFLOW, per_page: int = 100) -> list[RunInfo] | None:
    """Recent runs of the workflow, newest first; None when the API could not be read (the caller must then not dispatch blindly)."""
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/runs?per_page={per_page}", headers=_headers(token))
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return parse_runs(json.loads(r.read().decode()))
    except (urllib.error.URLError, OSError, ValueError) as e:
        print(f"pf_dispatch: could not list runs: {e}")
        return None


def dispatch_via_api(repo: str, ref: str, token: str, stages: str, workflow: str = PF_WORKFLOW) -> bool:
    body = json.dumps({"ref": ref, "inputs": {"stages": stages, "dry_run": "false"}}).encode()
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/dispatches", data=body, method="POST",
                                 headers={**_headers(token), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 204
    except urllib.error.HTTPError as e:
        print(f"pf_dispatch: dispatch failed HTTP {e.code}: {e.read()[:300]!r}")
        return False
    except OSError as e:
        print(f"pf_dispatch: dispatch failed: {e}")
        return False


def tips_from_schedule_files(paths: list[Path]) -> list[datetime]:
    """Start times from archived ``context/schedule`` snapshots (jsonl or jsonl.gz); unparseable rows are skipped."""
    out: set[datetime] = set()
    for p in paths:
        try:
            opener = gzip.open if str(p).endswith(".gz") else open
            with opener(p, "rt") as f:
                for line in f:
                    if not line.strip():
                        continue
                    try:
                        row = json.loads(line)
                        if str(row.get("season_type", "regular")).lower() not in ("regular", "playoffs", "playoff", "post", "2", "3"):
                            continue
                        t = _dt(row.get("start_time_utc"))
                        if t is not None:
                            out.add(t)
                    except (ValueError, TypeError, AttributeError):
                        continue
        except OSError:
            continue
    return sorted(out)


class PfDispatcher:
    """Per-worker state around ``decide``: reads the platform's own record of runs, dispatches at most what the policy allows.

    Never raises into the caller. ``list_fn`` / ``dispatch_fn`` are injectable so the whole policy can be driven in tests.
    """

    def __init__(self, repo: str, ref: str, token: str, *, list_fn=None, dispatch_fn=None) -> None:
        self.repo, self.ref, self.token = repo, ref, token
        self.list_fn = list_fn or (lambda: list_runs_via_api(repo, token))
        self.dispatch_fn = dispatch_fn or (lambda stages: dispatch_via_api(repo, ref, token, stages))
        self._last_dispatch: datetime | None = None
        self._dispatched: list[datetime] = []

    def step(self, now: datetime, tips: list[datetime]) -> dict:
        try:
            runs = self.list_fn()
            if runs is None:
                return {"action": "wait", "code": "API_UNREADABLE", "reason": "could not read the run list; not dispatching blind"}
            n_api, last_api = count_recent_dispatches(runs, now)
            self._dispatched = [t for t in self._dispatched if (now - t) < timedelta(hours=24)]
            n = max(n_api, len(self._dispatched))
            last = max([t for t in (last_api, self._last_dispatch) if t is not None], default=None)
            d = decide(now, tips, runs, dispatched_today=n, last_dispatch_at=last)
            out = d.as_dict()
            if d.action == "dispatch":
                ok = bool(self.dispatch_fn(d.stages))
                out["dispatched"] = ok
                if ok:
                    self._last_dispatch = now
                    self._dispatched.append(now)
                else:
                    out["action"], out["code"], out["reason"] = "wait", "DISPATCH_REFUSED", "the dispatch API did not accept the request: " + d.reason
            return out
        except Exception as e:  # noqa: BLE001 - the dispatcher must never take the capture worker down
            return {"action": "wait", "code": "DISPATCHER_ERROR", "reason": f"{type(e).__name__}: {str(e)[:200]}"}


def main(argv: list[str] | None = None) -> int:
    """``python -m nhl_edge.worker.pf_dispatch decide|dispatch --schedule FILE...`` for the watchdog / fallback workflows."""
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.worker.pf_dispatch")
    ap.add_argument("mode", choices=("decide", "dispatch", "gate"))
    ap.add_argument("--schedule", nargs="+", required=True, help="context/schedule snapshot file(s)")
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", ""))
    ap.add_argument("--ref", default=os.environ.get("GITHUB_REF_NAME", "main"))
    ap.add_argument("--now", default=None)
    ap.add_argument("--github-output", default=None)
    ap.add_argument("--event", default=os.environ.get("EVENT_NAME", ""), help="gate: the triggering event (schedule / workflow_dispatch / pull_request)")
    ap.add_argument("--stages-input", default="", help="gate: the dispatch input 'stages' (empty = default)")
    ap.add_argument("--exclude-run", type=int, default=None, help="ignore this run id (the run asking), so it does not count as 'in flight'")
    a = ap.parse_args(argv)
    token = os.environ.get("GITHUB_TOKEN", "")
    if not a.repo or not token:
        print("pf_dispatch: GITHUB_REPOSITORY and GITHUB_TOKEN are required", file=sys.stderr)
        return 2
    now = _dt(a.now) if a.now else datetime.now(UTC)
    tips = tips_from_schedule_files([Path(p) for p in a.schedule])
    disp = PfDispatcher(a.repo, a.ref, token)
    run = False
    if a.mode == "gate" and a.event in ("workflow_dispatch", "pull_request"):
        # an explicit request (the worker's, a human's or a PR dry run) always runs; only cron is policy-gated
        out = {"action": "dispatch", "code": "EXPLICIT_REQUEST", "reason": f"{a.event} runs unconditionally", "stages": a.stages_input or PREGAME_STAGES}
        run = True
    elif a.mode in ("decide", "gate"):
        runs = disp.list_fn()
        if runs is None:
            out = {"action": "wait", "code": "API_UNREADABLE", "reason": "could not read the run list"}
            # cron is the fallback of last resort: when the platform record is unreadable, run (the chain is idempotent) rather than skip
            run = a.mode == "gate"
        else:
            if a.exclude_run is not None:
                runs = [r for r in runs if r.id != a.exclude_run]
            if a.mode == "gate":
                out = decide(now, tips, runs).as_dict()
                run = out["action"] == "dispatch"
                out["stages"] = PREGAME_STAGES          # a cron run is never a partial run: it must also count as a fresh projection
            else:
                n, last = count_recent_dispatches(runs, now)
                out = decide(now, tips, runs, dispatched_today=n, last_dispatch_at=last).as_dict()
    else:
        out = disp.step(now, tips)
    print(json.dumps(out, indent=1, default=str))
    if a.github_output:
        with open(a.github_output, "a") as f:
            f.write(f"action={out['action']}\ncode={out['code']}\nstages={out.get('stages', PREGAME_STAGES)}\nrun={'true' if run else 'false'}\nstale={'true' if out.get('stale') else 'false'}\nrecovered={'true' if out.get('recovered') else 'false'}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
