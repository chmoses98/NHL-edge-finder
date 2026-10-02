"""Operational health of one capture-worker shift: HEALTHY / DEGRADED / FAILED / NOT_APPLICABLE.

Why this exists: until 2026-10-02 ``nhl worker`` returned 0 unconditionally, so the only recurring
scheduled workflow in this repository could not go red. Run 36955011158 (2026-10-02 02:18-07:05Z) was
a green check while ``nhl settle`` crashed twice with ``ImmutabilityError`` and settlement silently
stopped; the failure was visible only by reading a five-hour log by hand. The opposite mistake -- a red
run for every transient API error -- would teach the owner to ignore the workflow. This module is the
single place that decides which of the two a shift was.

The verdict is computed from what the worker RECORDED (per-cycle capture / job / push outcomes and the
conductor decision), never from the absence of a file or an empty directory:

* NOT_APPLICABLE  the conductor decision was available on every cycle and said nothing was due (off-day,
                  off-season outside the daily slot), or another worker legitimately owns the archive
                  (fail-closed stand-down). Maps to a green run.
* HEALTHY         every due capture/job ended the shift succeeding. Transient failures that a later
                  attempt in the same shift recovered are recorded as ``RECOVERED_AFTER_RETRY``.
* DEGRADED        the primary responsibility was met but something nonfatal is worth recording: a failed
                  research/context job, capture holes followed by recovery, a single not-yet-retried
                  failure, coverage alarms from the last capture, a successor that was not dispatched
                  (the cron bootstrap restarts the chain). Green run + warning annotation + step summary.
* FAILED          actionable after bounded in-shift recovery: captures that kept failing to the end of
                  the shift, a production job (simulate / settle) that failed repeatedly and was still
                  failing at retirement, an archive that could not be pushed, or a conductor decision that
                  was never available (so "nothing due" cannot be claimed). Red run.

Stdlib only, like ``archive/status.py``: the workflow's report step must not need an install to run.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

HEALTHY = "HEALTHY"
DEGRADED = "DEGRADED"
FAILED = "FAILED"
NOT_APPLICABLE = "NOT_APPLICABLE"

# Jobs whose sustained failure means a required production output is not being produced: simulate builds
# the slate, settle resolves it. context / evaluate / discover feed research quality and are retried by the
# conductor's age gates, so their failure is recorded as DEGRADED rather than paged.
CRITICAL_JOBS = ("simulate", "settle")

# Bounded recovery, expressed as attempts inside one shift. Captures run every 5-15 minutes, so three
# consecutive failures at the END of a shift is a current outage of 15-45 minutes, not a blip. A critical
# job is re-run by the conductor gate until its breadcrumb moves; two failed attempts with the last one still
# failing means the in-shift retry did not recover it.
CAPTURE_TRAILING_FAILURES_FOR_FAILED = 3
CRITICAL_JOB_FAILURES_FOR_FAILED = 2


def _trailing_failures(outcomes: list[bool]) -> int:
    n = 0
    for ok in reversed(outcomes):
        if ok:
            break
        n += 1
    return n


def _disposition(outcomes: list[bool]) -> str:
    if not outcomes:
        return "NOT_DUE"
    if all(outcomes):
        return "OK"
    if outcomes[-1]:
        return "RECOVERED_AFTER_RETRY"
    if not any(outcomes):
        return "FAILED_EVERY_ATTEMPT"
    return "FAILING_AT_RETIREMENT"


def assess(status: dict[str, Any]) -> dict[str, Any]:
    """Classify one worker shift from its STATUS_worker.json payload (``WorkerResult`` as a dict).

    Pure and deterministic: no clock, no filesystem, no network.
    """
    failures: list[str] = []
    warnings: list[str] = []
    notes: list[str] = []

    if status.get("fail_closed"):
        return {
            "state": NOT_APPLICABLE,
            "reason": f"stood down: {status.get('exit_reason', 'another worker owns the archive lease')}",
            "failures": [],
            "warnings": [],
            "notes": [],
            "components": {},
        }

    cycles = list(status.get("cycles") or [])
    components: dict[str, Any] = {}

    # -- capture ---------------------------------------------------------------------------------------
    cap = [bool(c.get("capture_ok")) for c in cycles if c.get("captured")]
    components["capture"] = {
        "attempts": len(cap),
        "ok": sum(cap),
        "failed": len(cap) - sum(cap),
        "trailing_failures": _trailing_failures(cap),
        "disposition": _disposition(cap),
    }
    if cap and not cap[-1] and _trailing_failures(cap) >= CAPTURE_TRAILING_FAILURES_FOR_FAILED:
        failures.append(
            f"capture: the last {_trailing_failures(cap)} capture attempts failed "
            f"({len(cap) - sum(cap)}/{len(cap)} this shift) -- current capture outage"
        )
    elif cap and not all(cap):
        warnings.append(
            f"capture: {len(cap) - sum(cap)}/{len(cap)} capture attempts failed this shift "
            f"({_disposition(cap)}); the archive has holes at those ticks"
        )

    # -- slow jobs -------------------------------------------------------------------------------------
    job_outcomes: dict[str, list[bool]] = {}
    for c in cycles:
        for name in c.get("jobs_run") or []:
            job_outcomes.setdefault(name, []).append(True)
        for name in c.get("jobs_failed") or []:
            job_outcomes.setdefault(name, []).append(False)
    # Order within one cycle does not matter for the verdict: the conductor runs each job at most once per
    # cycle, so a job's outcome list is already in cycle (time) order.
    jobs: dict[str, Any] = {}
    for name, outs in sorted(job_outcomes.items()):
        n_fail = len(outs) - sum(outs)
        disp = _disposition(outs)
        jobs[name] = {"attempts": len(outs), "ok": sum(outs), "failed": n_fail, "disposition": disp}
        if disp == "RECOVERED_AFTER_RETRY":
            notes.append(f"{name}: {n_fail} failed attempt(s) recovered by a later run in the same shift")
        elif not outs[-1]:
            if name in CRITICAL_JOBS and n_fail >= CRITICAL_JOB_FAILURES_FOR_FAILED:
                failures.append(f"{name}: failed {n_fail}/{len(outs)} attempts and was still failing at retirement")
            else:
                why = "retry pending" if name in CRITICAL_JOBS else "research/context job; retried by the conductor gate"
                warnings.append(f"{name}: last attempt failed ({n_fail}/{len(outs)} failed; {why})")
    components["jobs"] = jobs

    # -- conductor decision (the evidence for "nothing was due") --------------------------------------
    n_dec_err = sum(1 for c in cycles if c.get("decision_ok") is False)
    components["decision"] = {"cycles": len(cycles), "unavailable": n_dec_err}
    if cycles and n_dec_err == len(cycles):
        failures.append(
            f"conductor decision unavailable on all {len(cycles)} cycles: cannot tell whether simulate/settle "
            "were due (fail closed)"
        )
    elif n_dec_err:
        warnings.append(f"conductor decision unavailable on {n_dec_err}/{len(cycles)} cycles")

    # -- archive push ----------------------------------------------------------------------------------
    pushes = [bool(c.get("push_ok")) for c in cycles]
    final_push = status.get("final_push_ok")
    components["push"] = {
        "cycle_pushes": len(pushes),
        "cycle_push_failures": len(pushes) - sum(pushes),
        "final_push_ok": final_push,
    }
    if final_push is False:
        failures.append("archive push failed at retirement: this shift's captures are not on the archive branch")
    elif pushes and not all(pushes):
        if final_push is True:
            notes.append(f"archive: {len(pushes) - sum(pushes)} cycle push(es) failed; the final push delivered them")
        else:
            warnings.append(f"archive: {len(pushes) - sum(pushes)}/{len(pushes)} cycle pushes failed (final push pending)")

    # -- chain renewal ---------------------------------------------------------------------------------
    if status.get("successor_expected") and not status.get("successor_dispatched"):
        warnings.append("successor not dispatched: the chain now depends on the cron bootstrap to restart")

    # -- coverage alarms from the shift's last capture ------------------------------------------------
    for a in status.get("capture_alarms") or []:
        warnings.append(f"coverage alarm: {a}")

    if failures:
        state = FAILED
    elif warnings:
        state = DEGRADED
    elif not cap and not job_outcomes:
        state = NOT_APPLICABLE
    else:
        state = HEALTHY
    reason = {
        FAILED: "; ".join(failures),
        DEGRADED: "; ".join(warnings),
        NOT_APPLICABLE: "the conductor decision said no capture or job was due this shift",
        HEALTHY: "every due capture and job succeeded by the end of the shift",
    }[state]
    return {"state": state, "reason": reason, "failures": failures, "warnings": warnings, "notes": notes, "components": components}


# -- workflow report step ------------------------------------------------------------------------------


def summary_markdown(status: dict[str, Any], health: dict[str, Any]) -> str:
    cap = health.get("components", {}).get("capture", {})
    lines = [
        f"## capture-worker shift: **{health['state']}**",
        "",
        f"- worker `{status.get('worker_id')}` generation {status.get('generation')}: {status.get('exit_reason')}",
        f"- cycles {status.get('n_cycles', len(status.get('cycles') or []))}; captures {cap.get('ok', 0)}/{cap.get('attempts', 0)} ok",
        f"- reason: {health['reason']}",
    ]
    for name, j in sorted((health.get("components", {}).get("jobs") or {}).items()):
        lines.append(f"- job `{name}`: {j['ok']}/{j['attempts']} ok ({j['disposition']})")
    for n in health.get("notes") or []:
        lines.append(f"- note: {n}")
    return "\n".join(lines) + "\n"


def _escape(msg: str) -> str:
    return msg.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def report(report_path: Path, summary_path: str | None, output_path: str | None) -> dict[str, Any]:
    """Read the worker's final report, emit annotations + step summary + step outputs. Never exits non-zero:
    the workflow's single enforcement step decides red/green from the ``state`` output."""
    try:
        status = json.loads(report_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        status = {}
        health = {
            "state": FAILED,
            "reason": f"no readable worker report at {report_path} ({e.__class__.__name__}); the worker did not finish",
            "failures": ["worker report missing"],
            "warnings": [],
            "notes": [],
            "components": {},
        }
    else:
        health = status.get("health") or assess(status)
    state = health["state"]
    if state == FAILED:
        for f in health["failures"]:
            print(f"::error title=capture-worker FAILED::{_escape(f)}")
    elif state == DEGRADED:
        for w in health["warnings"]:
            print(f"::warning title=capture-worker DEGRADED::{_escape(w)}")
    else:
        print(f"capture-worker {state}: {health['reason']}")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write(summary_markdown(status, health) if status else f"## capture-worker shift: **{state}**\n\n{health['reason']}\n")
    if output_path:
        final_push = (status.get("health") or {}).get("components", {}).get("push", {}).get("final_push_ok")
        with open(output_path, "a") as f:
            f.write(f"state={state}\n")
            f.write(f"final_push_ok={'false' if final_push is False else 'true'}\n")
    return health


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="nhl-worker-health", description=__doc__)
    ap.add_argument("--report", required=True, type=Path)
    ap.add_argument("--summary", default=os.environ.get("GITHUB_STEP_SUMMARY"))
    ap.add_argument("--github-output", default=os.environ.get("GITHUB_OUTPUT"))
    a = ap.parse_args(argv)
    report(a.report, a.summary, a.github_output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
