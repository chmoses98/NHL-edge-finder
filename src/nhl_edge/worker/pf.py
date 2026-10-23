"""Worker-driven refresh of the projection foundation (PF) pregame run (RESEARCH_ONLY; no betting authority).

Why: ``projection-foundation.yml`` is driven by three cron slots a day (10:07, 16:07, 18:07 ET). GitHub's scheduler delivered those slots
up to several hours late and the runner queue added 10-40 min on top, so a slate's published projections could be older than the games
they cover (2026-10-22: the refresh requested at 21:27Z had not started by 22:29Z). The capture worker already runs every 5-15 minutes
for hours around the games and holds ``actions: write``; it therefore asks "is the published PF projection fresh enough for the next
puck drop?" each cycle and, if not, dispatches the SAME workflow (all stages, live, never dry-run). The cron slots stay as the backstop.

Properties (tested without a network):

* **Idempotent.** Nothing is dispatched while any PF run is executing or a dispatched run is queued, within 15 min of the last PF run created, or
  after the daily cap; a dispatch is never stacked on a pending run (the workflow's concurrency group keeps ONE pending run, so a second
  dispatch would cancel the first).
* **Freshness is read from what was published**, i.e. the commit time of ``projection-data``'s tip, not from run metadata: a skipped cron
  run (the gate job exits early for non-slot entries) and a failed run both look "successful" or "recent" in the runs list but publish nothing.
* **Only useful runs.** A refresh must be able to land before some unstarted puck drop (>= 20 min away) and the first such game must be
  inside 6 h (earlier, the morning slot is enough).
* **Fails soft.** Any API error is recorded and the worker carries on; capture and the other jobs never depend on this.
* **Watchdog.** A run queued > 45 min, a run in progress > 90 min, or a publication older than 2 h inside the last hour before a puck drop
  is returned as an alert string (surfaced in the worker's cycle record and STATUS_worker.json).

Kill-switch: ``NHL_EDGE_PF_DISPATCH=0``.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from collections.abc import Callable
from datetime import datetime
from typing import Any

from nhl_edge.timeutil import iso, parse_iso

PF_WORKFLOW = "projection-foundation.yml"
PF_BRANCH = "projection-data"
HORIZON_H = 6.0
MIN_LEAD_MIN = 20.0
#: (lead minutes to the first reachable puck drop is <=, maximum acceptable age of the published projection in minutes)
MAX_AGE_BY_LEAD: tuple[tuple[float, float], ...] = ((90.0, 40.0), (180.0, 75.0), (360.0, 150.0))
THROTTLE_MIN = 15.0
STUCK_QUEUE_MIN = 45.0
STUCK_RUN_MIN = 90.0
STALE_NEAR_TIPOFF_MIN = 120.0
MAX_DISPATCHES_PER_DAY = 8
IN_FLIGHT = ("queued", "waiting", "in_progress", "requested", "pending")
OUR_EVENTS = ("schedule", "workflow_dispatch")   # pull_request runs of this workflow are CI dry-runs of a PR, never refreshes
CALL_TIMEOUT_S = 10
FAILURE_BACKOFF_MIN = 60.0
NO_PUBLISH_BACKOFF = 2                           # dispatched runs that completed OK since the tip last moved

Http = Callable[[str, str, bytes | None], tuple[int, Any]]


def enabled() -> bool:
    return os.environ.get("NHL_EDGE_PF_DISPATCH", "1") not in ("0", "false", "False", "")


def _max_age_for(lead_min: float) -> float | None:
    for bound, age in MAX_AGE_BY_LEAD:
        if lead_min <= bound:
            return age
    return None


def _parse(ts: Any) -> datetime | None:
    try:
        return parse_iso(ts) if ts else None
    except (ValueError, TypeError):
        return None


def decide_pf(now: datetime, schedule_rows: list[dict[str, Any]], runs: list[dict[str, Any]], last_pub_at: datetime | None) -> dict[str, Any]:
    """Pure policy. ``runs`` are the workflow-runs API objects of projection-foundation.yml (newest first)."""
    starts = []
    for g in schedule_rows:
        if g.get("status") not in ("not_started", None):
            continue
        t = _parse(g.get("start_time_utc"))
        if t is not None and t > now:
            starts.append(t)
    reachable = sorted(t for t in starts if (t - now).total_seconds() / 60 >= MIN_LEAD_MIN)
    next_start = min(starts) if starts else None
    age_min = None if last_pub_at is None else (now - last_pub_at).total_seconds() / 60
    out: dict[str, Any] = {"now_utc": iso(now), "action": "skip", "reason": "", "alerts": [], "published_age_min": None if age_min is None else round(age_min, 1),
                           "lead_min": None, "max_age_min": None}
    runs = [r for r in runs if r.get("event") in OUR_EVENTS]

    # A queued *scheduled* run may be one of the cron entries the gate job skips (4 of the 8 daily entries are no-ops), so it is not evidence that
    # a real refresh is on its way and must not block one. Any run that is executing, and any queued run we or a person dispatched, does.
    inflight = [r for r in runs if r.get("status") == "in_progress" or (r.get("status") in IN_FLIGHT and r.get("event") != "schedule")]
    for r in inflight:
        created = _parse(r.get("created_at"))
        started = _parse(r.get("run_started_at")) or created          # a run waiting on the job-level concurrency group is already "in progress"
        if created is None or started is None:
            continue
        if r.get("status") in ("queued", "waiting", "requested", "pending"):
            waited = (now - created).total_seconds() / 60
            if waited > STUCK_QUEUE_MIN:
                out["alerts"].append(f"PF_RUN_QUEUED_{waited:.0f}MIN (run {r.get('id')}): GitHub runner capacity")
        elif r.get("status") == "in_progress":
            ran = (now - started).total_seconds() / 60
            if ran > STUCK_RUN_MIN:
                out["alerts"].append(f"PF_RUN_IN_PROGRESS_{ran:.0f}MIN (run {r.get('id')})")
    if next_start is not None and (next_start - now).total_seconds() / 60 <= 60 and (age_min is None or age_min > STALE_NEAR_TIPOFF_MIN):
        out["alerts"].append(f"PF_PUBLICATION_STALE_NEAR_TIPOFF age={'unknown' if age_min is None else f'{age_min:.0f}min'} next_tip_in={(next_start - now).total_seconds() / 60:.0f}min")

    if not reachable:
        out["reason"] = "no unstarted game at least 20 min away" if starts else "no unstarted game"
        return out
    lead = (reachable[0] - now).total_seconds() / 60
    out["lead_min"] = round(lead, 1)
    max_age = _max_age_for(lead)
    out["max_age_min"] = max_age
    if max_age is None:
        out["reason"] = f"first reachable game is {lead / 60:.1f} h away (> {HORIZON_H:.0f} h): the cron slot covers it"
        return out
    if age_min is not None and age_min <= max_age:
        out["reason"] = f"published projection is {age_min:.0f} min old (<= {max_age:.0f} min allowed at T-{lead:.0f}min)"
        return out
    if inflight:
        out["reason"] = f"{len(inflight)} PF run(s) already queued or running; not stacking a dispatch on it"
        return out
    # Back off when our own dispatches are not producing a publication: a failed run recently, or runs that "succeeded" while the tip never moved
    # (no-op / partial runs). Without this a broken pipeline would be re-dispatched every 15 minutes up to the daily cap.
    dispatched = [r for r in runs if r.get("event") == "workflow_dispatch"]
    for r in dispatched:
        c = _parse(r.get("created_at"))
        if r.get("status") == "completed" and r.get("conclusion") in ("failure", "timed_out", "startup_failure") and c is not None and (now - c).total_seconds() / 60 < FAILURE_BACKOFF_MIN:
            out["reason"] = f"dispatched run {r.get('id')} ended {r.get('conclusion')} < {FAILURE_BACKOFF_MIN:.0f} min ago; backing off"
            out["alerts"].append(f"PF_DISPATCHED_RUN_{str(r.get('conclusion')).upper()} (run {r.get('id')})")
            return out
    no_publish = [r for r in dispatched if r.get("status") == "completed" and r.get("conclusion") == "success" and last_pub_at is not None
                  and (_parse(r.get("created_at")) or now) > last_pub_at and (now - (_parse(r.get("created_at")) or now)).total_seconds() / 60 < 180]
    if len(no_publish) >= NO_PUBLISH_BACKOFF:
        out["reason"] = f"{len(no_publish)} dispatched runs completed since the last publication without publishing; backing off"
        out["alerts"].append("PF_DISPATCHED_BUT_NOT_PUBLISHED")
        return out
    created_times = [t for t in (_parse(r.get("created_at")) for r in runs) if t is not None]
    if created_times and (now - max(created_times)).total_seconds() / 60 < THROTTLE_MIN:
        out["reason"] = f"a PF run was created < {THROTTLE_MIN:.0f} min ago"
        return out
    today = now.date().isoformat()
    n_today = sum(1 for r in runs if r.get("event") == "workflow_dispatch" and str(r.get("created_at", ""))[:10] == today)
    if n_today >= MAX_DISPATCHES_PER_DAY:
        out["reason"] = f"daily dispatch cap ({MAX_DISPATCHES_PER_DAY}) reached"
        out["alerts"].append("PF_DISPATCH_CAP_REACHED")
        return out
    out["action"] = "dispatch"
    out["reason"] = f"published projection is {'missing' if age_min is None else f'{age_min:.0f} min old'} > {max_age:.0f} min allowed at T-{lead:.0f}min"
    return out


def _urllib_http(token: str) -> Http:
    def call(method: str, url: str, body: bytes | None = None) -> tuple[int, Any]:
        req = urllib.request.Request(url, data=body, method=method, headers={
            "Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=CALL_TIMEOUT_S) as r:
                raw = r.read()
                return r.status, (json.loads(raw) if raw else None)
        except urllib.error.HTTPError as e:
            return e.code, e.read()[:300].decode("utf-8", "replace")
        except OSError as e:
            return 0, str(e)
    return call


def run_pf_refresh(now: datetime, schedule_rows: list[dict[str, Any]], repo: str, token: str, ref: str = "main", http: Http | None = None) -> dict[str, Any]:
    """One worker-cycle check. Never raises; the returned dict goes into the cycle record."""
    call = http or _urllib_http(token)
    base = f"https://api.github.com/repos/{repo}"
    near = [t for t in (_parse(g.get("start_time_utc")) for g in schedule_rows if g.get("status") in ("not_started", None)) if t is not None
            and 0 < (t - now).total_seconds() / 3600 <= HORIZON_H + 1.0]
    if not near:       # off-season or nothing within reach: no network call, nothing to decide
        return {"action": "skip", "reason": "no unstarted game within the refresh horizon", "alerts": []}
    try:
        sc, runs_doc = call("GET", f"{base}/actions/workflows/{PF_WORKFLOW}/runs?per_page=50", None)
        if sc != 200 or not isinstance(runs_doc, dict):
            return {"action": "error", "reason": f"runs list HTTP {sc}: {str(runs_doc)[:120]}", "alerts": []}
        runs = runs_doc.get("workflow_runs") or []
        sc, commits = call("GET", f"{base}/commits?sha={PF_BRANCH}&per_page=1", None)
        last_pub = None
        if sc == 200 and isinstance(commits, list) and commits:
            last_pub = _parse(((commits[0].get("commit") or {}).get("committer") or {}).get("date"))
        elif sc != 404:      # 404 == the branch does not exist yet (first season run); anything else is an error worth recording
            return {"action": "error", "reason": f"projection-data tip HTTP {sc}: {str(commits)[:120]}", "alerts": []}
        d = decide_pf(now, schedule_rows, runs, last_pub)
        if d["action"] == "dispatch":
            body = json.dumps({"ref": ref, "inputs": {"stages": "all", "dry_run": "false"}}).encode()
            sc, resp = call("POST", f"{base}/actions/workflows/{PF_WORKFLOW}/dispatches", body)
            d["dispatch_http"] = sc
            if sc != 204:
                d["action"] = "error"
                d["reason"] += f" -- dispatch rejected HTTP {sc}: {str(resp)[:120]}"
        return d
    except Exception as e:  # noqa: BLE001 - a PF check must never take the capture worker down
        return {"action": "error", "reason": f"{type(e).__name__}: {str(e)[:160]}", "alerts": []}


def make_pf_fn(repo: str, token: str, ref: str = "main") -> Callable[[datetime, list[dict[str, Any]]], dict[str, Any]] | None:
    if not (repo and token) or not enabled():
        return None
    if ref != "main":      # a worker started from a feature branch is an experiment: it must not launch live (publishing) PF runs
        return None
    return lambda now, rows: run_pf_refresh(now, rows, repo, token, "main")

