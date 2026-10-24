"""Measured timeline of every projection refresh of one slate (RESEARCH_ONLY, read-only).

For each ``projection-foundation`` run in the slate window: when it was requested (``created_at``; for a dispatch this is the instant the request reached
GitHub), when a runner started its job (``started_at``), when the job completed, when its projection reached ``projection-data`` (the publishing commit) and how
many minutes before each puck drop that publication happened. Nothing here changes a model, price, timestamp or file; it reads the platform's run and commit
records through ``gh api`` (REST).

    python -m nhl_edge.research.delivery_timeline --date 2026-10-23 --games docs/research/slates/2026-10-23_snapshot_audit.json \\
        --out docs/research/slates/2026-10-23_delivery_timeline
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

REPO = "chmoses98/NHL-edge-finder"
WORKFLOW = "projection-foundation.yml"
PUBLISH_MESSAGE = re.compile(r"^NHL live shadow ")


def _dt(s: str | None) -> datetime | None:
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(UTC)


def _iso(t: datetime | None) -> str | None:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ") if t else None


def _minutes(a: datetime | None, b: datetime | None) -> float | None:
    return None if a is None or b is None else round((b - a).total_seconds() / 60, 1)


def gh_api(path: str) -> Any:
    out = subprocess.run(["gh", "api", path], capture_output=True, text=True, check=False, timeout=120)
    if out.returncode != 0:
        raise RuntimeError(f"gh api {path}: {out.stderr.strip()[:300]}")
    return json.loads(out.stdout)


def window(date: str) -> tuple[datetime, datetime]:
    """The slate's ET calendar date runs from ~04:00Z that day to ~08:00Z the next; use a generous, fixed window."""
    d0 = datetime.fromisoformat(date).replace(tzinfo=UTC)
    return d0 + timedelta(hours=8), d0 + timedelta(hours=32)


def collect(date: str, fetch: Callable[[str], Any] = gh_api) -> dict[str, Any]:
    lo, hi = window(date)
    runs: list[dict] = []
    for page in (1, 2, 3):
        got = fetch(f"repos/{REPO}/actions/workflows/{WORKFLOW}/runs?per_page=100&page={page}").get("workflow_runs", [])
        runs += got
        if len(got) < 100 or (_dt(got[-1]["created_at"]) or hi) < lo:
            break
    runs = [r for r in runs if lo <= _dt(r["created_at"]) < hi and r["event"] in ("schedule", "workflow_dispatch")]
    commits = fetch(f"repos/{REPO}/commits?sha=projection-data&since={_iso(lo)}&until={_iso(hi)}&per_page=100")
    pubs = sorted(
        (
            {
                "sha": c["sha"][:10],
                "at": _dt(c["commit"]["committer"]["date"]),
                "message": c["commit"]["message"].splitlines()[0],
            }
            for c in commits
            if PUBLISH_MESSAGE.match(c["commit"]["message"])
        ),
        key=lambda p: p["at"],
    )
    rows = []
    for r in sorted(runs, key=lambda r: r["created_at"]):
        jobs = fetch(f"repos/{REPO}/actions/runs/{r['id']}/jobs?per_page=100").get("jobs", [])
        live = next((j for j in jobs if j["name"] == "live"), None)
        steps = {s["name"]: s for s in (live or {}).get("steps", [])}
        chain = next((s for k, s in steps.items() if k.startswith("Run the chain")), None)
        commit_step = next((s for k, s in steps.items() if k.startswith("Commit to projection-data")), None)
        rows.append(
            {
                "run_id": r["id"],
                "event": r["event"],
                "title": r["display_title"],
                "conclusion": r.get("conclusion"),
                "requested": _dt(r["created_at"]),
                "runner_started": _dt((live or {}).get("started_at")),
                "job_created": _dt((live or {}).get("created_at")),
                "chain_started": _dt((chain or {}).get("started_at")),
                "chain_completed": _dt((chain or {}).get("completed_at")),
                "commit_step_conclusion": (commit_step or {}).get("conclusion"),
                "completed": _dt((live or {}).get("completed_at") or r["updated_at"]),
                "url": r["html_url"],
            }
        )
    used: set[str] = set()
    for row in rows:
        row["publication"] = None
        if row["conclusion"] == "success" and row["commit_step_conclusion"] == "success":
            nxt = next(
                (
                    p
                    for p in pubs
                    if p["sha"] not in used
                    and row["runner_started"]
                    and p["at"] >= row["runner_started"]
                    and p["at"] <= (row["completed"] or p["at"]) + timedelta(minutes=2)
                ),
                None,
            )
            if nxt:
                used.add(nxt["sha"])
                row["publication"] = nxt
    return {"date": date, "window": [_iso(lo), _iso(hi)], "runs": rows, "publications": pubs}


def attach_drops(tl: dict[str, Any], starts: list[datetime]) -> None:
    starts = sorted(starts)
    tl["puck_drops"] = [_iso(s) for s in starts]
    for row in tl["runs"]:
        row["minutes"] = {
            "request_to_runner_start": _minutes(row["requested"], row["runner_started"]),
            "runner_start_to_complete": _minutes(row["runner_started"], row["completed"]),
            "request_to_publication": _minutes(row["requested"], row["publication"]["at"])
            if row["publication"]
            else None,
        }
        pub = row["publication"]["at"] if row["publication"] else None
        nxt = next((s for s in starts if pub and s > pub), None)
        row["games_already_started_at_publication"] = sum(1 for s in starts if pub and s <= pub) if pub else None
        row["publication_to_next_drop_min"] = _minutes(pub, nxt) if pub else None
        row["publication_to_first_drop_min"] = _minutes(pub, starts[0]) if pub and starts else None


def slate_starts(games: list[dict[str, Any]], date: str) -> list[datetime]:
    """Puck drops of this slate only (the audit reads two UTC partitions, so it also lists the previous evening's tail and the next day's games)."""
    lo, hi = window(date)
    return [d for g in games if (d := _dt(g.get("start_utc"))) and lo <= d < hi]


def schedule_games(paths: list[Path]) -> list[dict[str, Any]]:
    """Regular-season rows of archived ``context/schedule`` snapshots as ``{"start_utc": ...}`` (the same shape ``slate_starts`` takes), latest snapshot wins per game."""
    import gzip

    by: dict[str, dict[str, Any]] = {}
    for p in paths:
        try:
            with (gzip.open(p, "rt") if str(p).endswith(".gz") else open(p)) as f:
                for line in f:
                    if line.strip():
                        try:
                            r = json.loads(line)
                        except ValueError:
                            continue
                        if str(r.get("season_type", "regular")).lower() in ("regular", "2") and r.get("game_id") is not None:
                            by[str(r["game_id"])] = {"start_utc": r.get("start_time_utc")}
        except OSError:
            continue
    return list(by.values())


def markdown(tl: dict[str, Any]) -> str:
    t = lambda x: x.strftime("%H:%M:%S") if x else "—"  # noqa: E731
    L = [
        f"# Projection refresh timeline — slate {tl['date']}",
        "",
        "RESEARCH_ONLY · UTC · source: GitHub Actions run/job records and `projection-data` commits (read-only).",
        "",
    ]
    if tl.get("puck_drops"):
        L += [
            f"Puck drops: first {tl['puck_drops'][0]}, last {tl['puck_drops'][-1]} ({len(tl['puck_drops'])} games).",
            "",
        ]
    L += [
        "| run | event | requested | runner start | complete | publication | req→runner | req→pub | pub→next drop | games started at pub | result |",
        "|---|---|---|---|---|---|---:|---:|---:|---:|---|",
    ]
    for r in tl["runs"]:
        m = r.get("minutes", {})
        f = lambda v: "—" if v is None else f"{v:.1f}"  # noqa: E731
        L.append(
            f"| [{r['run_id']}]({r['url']}) | {r['event']} {('[' + r['title'].split('[')[-1]) if '[' in r['title'] else ''} | {t(r['requested'])} | {t(r['runner_started'])} | {t(r['completed'])} | "
            f"{t(r['publication']['at']) if r['publication'] else '—'} | {f(m.get('request_to_runner_start'))} | {f(m.get('request_to_publication'))} | "
            f"{f(r.get('publication_to_next_drop_min'))} | {r.get('games_already_started_at_publication') if r.get('games_already_started_at_publication') is not None else '—'} | "
            f"{r['conclusion'] or 'in progress'}{'' if r['publication'] or r['conclusion'] != 'success' else ' (no publication: gated out or nothing to commit)'} |"
        )
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.delivery_timeline")
    ap.add_argument("--date", required=True)
    ap.add_argument("--games", help="snapshot_audit JSON of the same slate (puck drops are read from it)")
    ap.add_argument("--schedule", nargs="+", help="context/schedule snapshot file(s) (puck drops are read from them when no audit JSON is given)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    tl = collect(a.date)
    if a.games:
        starts = slate_starts(json.loads(Path(a.games).read_text())["games"], a.date)
    elif a.schedule:
        starts = slate_starts(schedule_games([Path(p) for p in a.schedule]), a.date)
    else:
        starts = []
    attach_drops(tl, starts)
    Path(a.out + ".json").write_text(
        json.dumps(tl, indent=1, default=lambda o: _iso(o) if isinstance(o, datetime) else str(o))
    )
    Path(a.out + ".md").write_text(markdown(tl))
    print(f"{len(tl['runs'])} runs, {len(tl['publications'])} publications")
    return 0


if __name__ == "__main__":
    sys.exit(main())
