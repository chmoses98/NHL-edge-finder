"""The self-renewing capture worker: one long-lived run that captures on a cadence and hands over.

Architecture, and why it is this shape rather than the obvious one:

GitHub's scheduler does not deliver. Measured on this repository over six days, ``*/10`` cron
produced 34 conductor runs against 864 expected (~3.9%), with observed gaps of 2h18m and 3h09m
between consecutive "ten-minute" wakes. The dominant failure is OMISSION, not lateness, so no
amount of cron tuning fixes it. The fix is to stop asking cron for cadence: one long-lived run
owns the cadence internally, and cron is demoted to a bootstrap of last resort.

Every structural decision below is backed by a chainlab experiment run against this repository:

  E0  A workflow file that exists only on a non-default branch is NOT dispatchable (404), while
      the same token dispatches a file present on the default branch (204). => The worker workflow
      must be merged to main before it can renew itself at all.
  E1  A run CAN dispatch its own successor with GITHUB_TOKEN (``actions: write``), and the
      successor really runs. GitHub's recursion suppression does not extend to workflow_dispatch.
      Handover measured at ~7s from parent dispatch to successor job start.
  E2  Within one concurrency group GitHub keeps at most one run IN PROGRESS and at most one run
      PENDING; queueing a third cancels the previously pending one. Three queued runs collapsed to
      exactly one, and two writers never coexisted.

E2 is the load-bearing one. It means a successor queued early can be cancelled by a watchdog that
fires later -- which would be fatal if the watchdog were a different workflow. So the watchdog
dispatches THIS SAME workflow: the single pending slot then always holds a worker, and it does not
matter who put it there. Cancellation becomes a substitution rather than a break.

Ownership is therefore enforced in two layers. The concurrency group is the real guarantee (E2:
never two in progress). The lease is the evidence, the cross-workflow reach, and the fail-closed
check -- see ``worker/lease.py``.
"""

from __future__ import annotations

import json
import os
import secrets
import subprocess
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from nhl_edge.timeutil import iso, parse_iso, utcnow
from nhl_edge.worker import lease as lease_mod
from nhl_edge.worker.health import assess as assess_health
from nhl_edge.worker.plan import (
    plan_cycle,
    planned_exit,
    should_retire,
    tip_times,
)

# The branch the worker pushes to. Read from the environment, with the production branch as the
# default, because the workflow declares `env: ARCHIVE_BRANCH` and a reader reasonably assumes that
# is what takes effect. It was previously a bare constant, so the env var was decorative and the
# worker silently pushed to `data-archive` whatever the workflow said -- which is exactly how a
# rehearsal intended for a throwaway branch ended up writing to the real archive.
DEFAULT_ARCHIVE_BRANCH = "data-archive"


def archive_branch() -> str:
    return os.environ.get("ARCHIVE_BRANCH") or DEFAULT_ARCHIVE_BRANCH


@dataclass
class CycleRecord:
    """What one iteration actually did -- the raw material for the Phase 4 cadence report."""

    started_at: str
    jobs_run: list[str]
    captured: bool
    capture_ok: bool
    push_ok: bool
    duration_s: float
    cadence_s: float
    hours_to_next_tip: float | None
    reason: str
    # Recorded so a failed job is visible in STATUS_worker.json and to the health verdict. Before 2026-10-02 only
    # successes were kept, so a settle job that crashed every attempt left no trace outside the run log.
    jobs_failed: list[str] = field(default_factory=list)
    # False when the conductor decision could not be computed this cycle: "nothing was due" is then unproven.
    decision_ok: bool = True
    # Compact view of the STATUS_settle.json the settle job wrote in THIS cycle (None when settle did not run OK here).
    # `nhl settle` exits 0 even when results or player events could not be fetched (it records them instead), so the
    # exit code alone cannot show a settlement that has stopped progressing; this can.
    settle: dict | None = None


@dataclass
class WorkerResult:
    worker_id: str
    generation: int
    exit_reason: str
    cycles: list[CycleRecord] = field(default_factory=list)
    successor_dispatched: bool = False
    fail_closed: bool = False
    # Whether a dispatcher was configured at all (no token / --no-successor => no successor is expected).
    successor_expected: bool = False
    # Outcome of the push made AFTER STATUS_worker.json is written; None inside that file (not yet known).
    final_push_ok: bool | None = None
    # Coverage alarms of the shift's last capture (STATUS_capture.json), surfaced as DEGRADED, never as red.
    capture_alarms: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        d = {
            "worker_id": self.worker_id,
            "generation": self.generation,
            "exit_reason": self.exit_reason,
            "successor_dispatched": self.successor_dispatched,
            "successor_expected": self.successor_expected,
            "fail_closed": self.fail_closed,
            "final_push_ok": self.final_push_ok,
            "capture_alarms": list(self.capture_alarms),
            "n_cycles": len(self.cycles),
            "n_captured": sum(1 for c in self.cycles if c.captured),
            "n_capture_failed": sum(1 for c in self.cycles if c.captured and not c.capture_ok),
            "n_jobs_failed": sum(len(c.jobs_failed) for c in self.cycles),
            "cycles": [vars(c) for c in self.cycles],
        }
        d["health"] = assess_health(d)
        return d

    def to_json(self) -> str:
        return json.dumps(self.as_dict(), indent=2, sort_keys=True) + "\n"


def _default_run(cmd: list[str], timeout: float) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout or "")[-4000:] + (p.stderr or "")[-4000:]
    except subprocess.TimeoutExpired:
        return 124, f"timeout after {timeout}s: {' '.join(cmd)}"
    except OSError as e:  # noqa: BLE001 - a missing binary must not kill the worker
        return 127, f"{e}"


def dispatch_successor_via_api(repo: str, ref: str, token: str, workflow: str, successor_token: str) -> bool:
    """Queue the next worker. Returns True only on GitHub's 204 (accepted).

    204 means ACCEPTED, not "a run exists" -- E2 showed an accepted dispatch can still lose its
    pending slot to a later one. The caller must verify, not trust this boolean alone.
    """
    import urllib.error
    import urllib.request

    body = json.dumps({"ref": ref, "inputs": {"successor_token": successor_token}}).encode()
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/actions/workflows/{workflow}/dispatches",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status == 204
    except urllib.error.HTTPError as e:
        print(f"worker: successor dispatch failed HTTP {e.code}: {e.read()[:300]!r}")
        return False
    except OSError as e:
        print(f"worker: successor dispatch failed: {e}")
        return False


class Worker:
    """One long-lived capture run.

    Every side effect is injected so the race and rollover tests can drive a whole simulated
    lifetime -- takeovers, crashes, fail-closed refusals -- without a runner or a network.
    """

    def __init__(
        self,
        *,
        data_root: Path,
        archive_root: Path,
        worker_id: str,
        successor_token: str | None = None,
        now_fn: Callable[[], datetime] = utcnow,
        sleep_fn: Callable[[float], None] = time.sleep,
        run_fn: Callable[[list[str], float], tuple[int, str]] = _default_run,
        dispatch_fn: Callable[[str], bool] | None = None,
        schedule_fn: Callable[[], list[dict]] | None = None,
        decide_fn: Callable[[], dict] | None = None,
        lifetime_minutes: float | None = None,
    ) -> None:
        self.data_root = Path(data_root)
        self.archive_root = Path(archive_root)
        self.worker_id = worker_id
        self.successor_token = successor_token
        self.now = now_fn
        self.sleep = sleep_fn
        self.run_cmd = run_fn
        self.dispatch_fn = dispatch_fn
        self.schedule_fn = schedule_fn or self._read_schedule
        self.decide_fn = decide_fn or self._decide
        self.lifetime_minutes = lifetime_minutes
        self.result: WorkerResult | None = None
        self._decision_error: str | None = None

    # -- archive I/O -------------------------------------------------------------------------
    def _read_schedule(self) -> list[dict]:
        from nhl_edge.archive.ledger import Ledger

        try:
            from nhl_edge.workflows.conductor import _latest_schedule

            return _latest_schedule(Ledger(self.archive_root))
        except Exception as e:  # noqa: BLE001 - a bad snapshot must degrade, not crash the worker
            print(f"worker: could not read schedule ({e}); treating slate as unknown")
            return []

    def _decide(self) -> dict:
        """The conductor's own decision, reused rather than reimplemented."""
        try:
            from nhl_edge.workflows.conductor import decide_now

            # the worker's clock, not the wall clock: in production they are the same (utcnow), and under an
            # injected clock the conductor gate must see the same instant the cadence does
            return decide_now(self.data_root, now=self.now())
        except Exception as e:  # noqa: BLE001 - a bad breadcrumb must not stop capture
            print(f"worker: could not read the conductor decision ({e}); capture-only this cycle")
            # Recorded, not swallowed: the health verdict must not read "nothing due" into a missing decision.
            self._decision_error = str(e) or e.__class__.__name__
            return {}

    def _push(self, message: str) -> bool:
        script = Path(__file__).resolve().parents[3] / "scripts" / "archive_push.sh"
        if not script.exists():
            print(f"worker: push script missing at {script}")
            return False
        rc, out = self.run_cmd(
            ["bash", str(script), str(self.archive_root), archive_branch(), message], 300
        )
        if rc != 0:
            print(f"worker: archive push failed rc={rc}: {out[-600:]}")
        return rc == 0

    # -- lifecycle ---------------------------------------------------------------------------
    def acquire(self) -> tuple[bool, str, int]:
        """Take the lease, or refuse to run. Returns (ok, reason, generation)."""
        now = self.now()
        current = lease_mod.read_lease(self.archive_root)
        ok, why = lease_mod.may_write(current, self.worker_id, now, successor_token=self.successor_token)
        if not ok:
            return False, why, current.generation if current else 0
        new = lease_mod.takeover(current, self.worker_id, now)
        exit_at = planned_exit(now, self.lifetime_minutes) if self.lifetime_minutes else planned_exit(now)
        new = lease_mod.heartbeat(new, now, planned_exit_at=exit_at, note=why)
        lease_mod.write_lease(self.archive_root, new)
        return True, why, new.generation

    def run(self) -> WorkerResult:
        started = self.now()
        exit_at = (
            planned_exit(started, self.lifetime_minutes) if self.lifetime_minutes else planned_exit(started)
        )

        ok, why, gen = self.acquire()
        res = WorkerResult(
            worker_id=self.worker_id, generation=gen, exit_reason="", successor_expected=self.dispatch_fn is not None
        )
        self.result = res
        if not ok:
            # Fail closed. Exit 0, not an error: another worker legitimately owns the archive and
            # the correct behaviour is to stand down quietly rather than to race it.
            res.exit_reason = f"fail-closed: {why}"
            res.fail_closed = True
            print(f"worker: {res.exit_reason}")
            return res
        print(f"worker {self.worker_id} generation {gen} acquired lease ({why}); planned exit {iso(exit_at)}")
        self._push(f"worker: {self.worker_id} gen {gen} acquired lease")

        # Queue the successor NOW rather than at retirement. A crash at any later point then still
        # leaves a worker in the pending slot, which starts the instant this run leaves the group.
        # E2 says a later dispatch can cancel it -- that is why retirement re-verifies below.
        self._dispatch_successor(res, "early (crash insurance)")

        last_cost = 0.0
        while True:
            now = self.now()
            if should_retire(now, exit_at, last_cost):
                res.exit_reason = f"planned retirement at {iso(now)} (exit_at {iso(exit_at)})"
                break
            rec = self._one_cycle(now)
            res.cycles.append(rec)
            last_cost = rec.duration_s
            now2 = self.now()
            sleep_s = max(0.0, rec.cadence_s - (now2 - now).total_seconds())
            if should_retire(now2, exit_at, sleep_s):
                res.exit_reason = "planned retirement before next cadence tick"
                break
            if sleep_s:
                self.sleep(sleep_s)

        self._retire(res, exit_at)
        return res

    def _one_cycle(self, now: datetime) -> CycleRecord:
        starts = tip_times(self.schedule_fn())
        cyc = plan_cycle(now, starts)
        self._decision_error = None
        decision = self.decide_fn() or {}
        decision_ok = self._decision_error is None
        # The UNION of both gates, because the worker replaced the conductor's schedule and has to
        # be a genuine superset of it.
        #
        # `plan_cycle` only opens inside the 8h active window, but `decide()` also captured within
        # 36h of a tip AND on a daily off-season slot. Taking only the worker's gate silently ended
        # off-season market capture the moment the conductor's cron was removed -- no futures
        # snapshots at all between seasons, which is exactly the sort of quiet evidence loss that is
        # invisible until someone goes looking for data that was never collected.
        should_capture = bool(cyc.should_capture or decision.get("capture"))
        captured = capture_ok = push_ok = False
        if should_capture:
            captured = True
            rc, out = self.run_cmd(
                [p.replace("ARCHIVE", str(self.archive_root)) for p in self.CAPTURE_CMD],
                self.CAPTURE_BUDGET_S,
            )
            capture_ok = rc == 0
            if not capture_ok:
                # One bad capture must never end the worker. The archive is append-only and the
                # next tick is minutes away; dying here would convert a transient API error into a
                # multi-hour hole, which is precisely the failure this design exists to remove.
                print(f"worker: capture failed rc={rc}: {out[-600:]}")

        # The worker owns the archive's concurrency group for hours, so every scheduled conductor
        # run queues behind it and is cancelled (E2). Whatever the conductor would have decided to
        # do, the worker must therefore do itself -- otherwise simulate/settle/evaluate/discover
        # silently stop for as long as a worker is alive. Each is age-gated by decide(), so this is
        # the same cadence they had before, not extra work.
        jobs_run, jobs_failed = self._run_jobs(decision, capture_ok=capture_ok)
        self._run_research_export(jobs_run, jobs_failed)
        settle_snapshot = self._settle_snapshot(now) if "settle" in jobs_run else None

        cur = lease_mod.read_lease(self.archive_root)
        if cur is not None:
            ok, why = lease_mod.may_write(
                cur, self.worker_id, self.now(), successor_token=self.successor_token
            )
            if not ok:
                print(f"worker: lost the lease mid-flight ({why}); not writing mutable state")
            else:
                lease_mod.write_lease(
                    self.archive_root,
                    lease_mod.heartbeat(
                        cur,
                        self.now(),
                        last_capture_at=self.now() if capture_ok else None,
                        expected_next_capture_at=cyc.next_cycle_at,
                    ),
                )
        push_ok = self._push(f"capture: {self.worker_id} at {iso(now)}")
        return CycleRecord(
            started_at=iso(now),
            jobs_run=jobs_run,
            captured=captured,
            capture_ok=capture_ok,
            push_ok=push_ok,
            duration_s=(self.now() - now).total_seconds(),
            cadence_s=cyc.cadence_seconds,
            hours_to_next_tip=cyc.hours_to_next_tip,
            reason=cyc.reason if cyc.should_capture or not should_capture else "conductor gate: off-window capture due",
            jobs_failed=jobs_failed,
            decision_ok=decision_ok,
            settle=settle_snapshot,
        )

    def _settle_snapshot(self, cycle_started: datetime) -> dict:
        """Read (never modify) the STATUS_settle.json that this cycle's settle run wrote.

        Fresh only if its ``settled_at_utc`` is not older than the start of this cycle: a breadcrumb left by an
        earlier run or another workflow must never be attributed to this shift (same rule as coverage alarms).
        """
        path = self.archive_root / "STATUS_settle.json"
        try:
            d = json.loads(path.read_text())
            fresh = parse_iso(d["settled_at_utc"]) >= cycle_started
        except (OSError, ValueError, KeyError, TypeError, AttributeError):
            return {"fresh": False}
        if not fresh:
            return {"fresh": False}
        player = d.get("player") if isinstance(d.get("player"), dict) else {}
        return {
            "fresh": True,
            "games_pending": sorted(str(g) for g in (d.get("games_pending") or [])),
            "n_result_errors": len(d.get("errors") or []),
            "n_player_errors": len(player.get("errors") or []),
        }

    # The capture command, as a constant rather than inline, so a test can compare it against
    # conductor.yml's production-proven invocation instead of against a copy of itself.
    CAPTURE_CMD = ("nhl", "capture", "--out", "ARCHIVE", "--orderbook", "--max-orderbooks", "300")
    CAPTURE_BUDGET_S = 600.0

    # The slow jobs, in dependency order: context before simulate (a simulation wants the freshest goalie
    # observation), settle before evaluate (evaluation scores what settlement just resolved).
    SLOW_JOBS = (
        ("context", ["nhl", "context", "--out", "ARCHIVE"], 900.0),
        ("simulate", ["nhl", "simulate", "--data", "DATA", "--out", "ARCHIVE"], 1500.0),
        ("settle", ["nhl", "settle", "--data", "DATA", "--out", "ARCHIVE"], 900.0),
        # the evaluation ledger IS the archive (predictions + settlements live there); reports go to ARCHIVE/eval/. The
        # original "ARCHIVE/eval" root read an empty sub-ledger, so production evaluation scored 0 rows (fixed 2026-09-30).
        ("evaluate", ["nhl", "evaluate", "--data", "DATA", "--out", "ARCHIVE"], 900.0),
        # The Edge Finder app export (edge_finder.app.v1) reads what the jobs above wrote and publishes ARCHIVE/app/latest,
        # which archive_push.sh carries to the data-archive branch. Not conductor-gated: it is due whenever this cycle
        # changed the archive (a capture or any slow job), so the app never shows a board older than the archive. A failed
        # export rewrites only app/latest/health.json (export_failed=true) and, like every job here, never ends the cycle.
        ("app_export", ["nhl", "app-export", "--data-root", "ARCHIVE", "--out", "ARCHIVE/app/latest", "--accounting-dir", "DATA/accounting"], 300.0),
        ("discover", ["nhl", "discover", "--out", "ARCHIVE/catalog", "--statuses", "open,unopened", "--max-pages", "10"], 1200.0),
    )
    #: Jobs that are due by what happened in the cycle rather than by the conductor's decision.
    DERIVED_JOBS = ("app_export",)

    # The research explorer (contract 1.1.0) lives inside app/latest, and publishing app/latest removes every file its
    # manifest does not list -- explorer/ included. So it is re-published right after every successful app export, as its
    # own command: a failure is recorded on the cycle (non-critical job) and never touches the v1 payload.
    RESEARCH_EXPORT_JOB = ("research_export", ["nhl", "research-export", "--data-root", "ARCHIVE", "--out", "ARCHIVE/app/latest"], 600.0)

    def _run_research_export(self, jobs_run: list[str], jobs_failed: list[str]) -> None:
        if "app_export" not in jobs_run:
            return
        name, template, budget = self.RESEARCH_EXPORT_JOB
        cmd = [part.replace("ARCHIVE", str(self.archive_root)).replace("DATA", str(self.data_root)) for part in template]
        rc, out = self.run_cmd(cmd, budget)
        if rc == 0:
            jobs_run.append(name)
        else:
            jobs_failed.append(name)
            print(f"worker: job {name} failed rc={rc}: {out[-400:]}")

    def _run_due_jobs(self, decision: dict | None = None, *, capture_ok: bool = False) -> list[str]:
        return self._run_jobs(decision, capture_ok=capture_ok)[0]

    def _run_jobs(self, decision: dict | None = None, *, capture_ok: bool = False) -> tuple[list[str], list[str]]:
        """Run every due slow job; returns (succeeded, failed) job names in run order.

        ``capture_ok`` feeds the DERIVED_JOBS rule: app_export is due after a good capture or after any
        other slow job ran, whatever the conductor decided."""
        decision = decision if decision is not None else (self.decide_fn() or {})
        done: list[str] = []
        failed: list[str] = []
        for name, template, budget in self.SLOW_JOBS:
            due = decision.get(name)
            if name in self.DERIVED_JOBS and due is None:
                due = capture_ok or bool(done)
            if not due:
                continue
            cmd = [
                part.replace("ARCHIVE", str(self.archive_root)).replace("DATA", str(self.data_root))
                for part in template
            ]
            rc, out = self.run_cmd(cmd, budget)
            if rc == 0:
                done.append(name)
            else:
                # Same reasoning as a failed capture: one bad job must never end the worker. The failure is
                # recorded on the cycle so the shift's health verdict (worker/health.py) can see it.
                failed.append(name)
                print(f"worker: job {name} failed rc={rc}: {out[-400:]}")
        return done, failed

    def _dispatch_successor(self, res: WorkerResult, label: str) -> None:
        if self.dispatch_fn is None:
            print(f"worker: no dispatcher configured; skipping successor ({label})")
            return
        now = self.now()
        cur = lease_mod.read_lease(self.archive_root)
        thrash, why = lease_mod.thrashing(cur, now)
        if thrash and res.successor_dispatched:
            # Only re-dispatches are throttled: the early "crash insurance" dispatch happens seconds after
            # this worker's own lease was acquired, so the age test would always refuse it. Storms are
            # bounded by the platform concurrency group (one pending slot) regardless.
            print(f"worker: refusing successor -- {why}")
            return
        token = secrets.token_hex(16)
        if not self.dispatch_fn(token):
            print(f"worker: successor dispatch NOT accepted ({label})")
            return
        res.successor_dispatched = True
        if cur is not None:
            lease_mod.write_lease(
                self.archive_root,
                lease_mod.heartbeat(cur, now, successor_token=token, successor_dispatched_at=now),
            )
        print(f"worker: successor dispatched {label}, token {token[:8]}...")

    def _retire(self, res: WorkerResult, exit_at: datetime) -> None:
        """Hand over. Re-dispatch, because E2 says the early successor may have been cancelled.

        Re-dispatching unconditionally is correct rather than wasteful: a duplicate dispatch
        collapses into the single pending slot (E2), so the cost of being wrong in this direction
        is nothing, while the cost of being wrong in the other direction is a broken chain.
        """
        self._dispatch_successor(res, "at retirement (re-verify)")
        cur = lease_mod.read_lease(self.archive_root)
        if cur is not None and cur.worker_id == self.worker_id:
            lease_mod.write_lease(
                self.archive_root,
                lease_mod.heartbeat(
                    cur, self.now(), released_at=self.now(), note=f"retired: {res.exit_reason}"
                ),
            )
        if any(c.captured for c in res.cycles):
            res.capture_alarms = self._capture_alarms()
        (self.archive_root / "STATUS_worker.json").write_text(res.to_json())
        # The Phase 12 dashboard, refreshed on every handover (~5x/day, comfortably "daily").
        # Retirement is the right moment: the worker has just finished a full shift, so the counts
        # describe a completed period rather than a half-finished one.
        res.final_push_ok = self._push(f"worker: {self.worker_id} retired after {len(res.cycles)} cycles")
        print(f"worker: {res.exit_reason}")
        print(f"worker: health {res.as_dict()['health']['state']}")

    def _capture_alarms(self) -> list[str]:
        """Coverage alarms of the latest capture. Unreadable status is reported as an alarm, never ignored."""
        path = self.archive_root / "STATUS_capture.json"
        if not path.exists():
            return []
        try:
            return [str(a) for a in (json.loads(path.read_text()).get("alarms") or [])]
        except (OSError, ValueError, AttributeError) as e:
            return [f"STATUS_capture.json unreadable ({e.__class__.__name__})"]
