"""Pre-puck-drop audit of the archived projections for one ET game day (RESEARCH_ONLY; read-only).

For every game on the day it answers, from the append-only ``predictions`` (and optional ``predictions_v2`` / ``predictions_oa``) partitions
only:

* which forecast was the **last one available before puck drop** (``predicted_at_utc`` < start) and how far ahead of the start it was made;
* how many runs produced a forecast before the start, and how many rows arrived **late** (at or after the start: they exist in the archive
  but were never usable as pregame forecasts and are excluded from any pregame score);
* the goalie status the last pregame forecast carried;
* that every partition file used still matches the sha256 recorded in ``manifest.jsonl`` when it was written (nothing was rewritten).

Nothing here changes or re-scores history: it only reads. ``python -m nhl_edge.research.pregame_audit --archive DIR --date 2026-10-22 --out OUT``
"""

from __future__ import annotations

import gzip
import hashlib
import json
import sys
from datetime import timedelta
from pathlib import Path
from typing import Any

from nhl_edge.timeutil import iso, parse_iso

KINDS = ("predictions", "predictions_v2", "predictions_oa")
LATE_GAME_FAMILY = "game_winner"


def _partition_files(archive: Path, kind: str, dates: list[str]) -> list[Path]:
    out: list[Path] = []
    for d in dates:
        out += sorted((archive / kind / f"dt={d}").glob("*.jsonl.gz"))
    return out


def _rows(path: Path):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def manifest_hashes(archive: Path, paths: set[str]) -> dict[str, str]:
    """sha256 recorded at write time for the given archive-relative paths (streamed; the manifest is large)."""
    out: dict[str, str] = {}
    mp = archive / "manifest.jsonl"
    if not mp.exists():
        return out
    with mp.open() as f:
        for line in f:
            if not any(p in line for p in paths):
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if e.get("path") in paths:
                out[e["path"]] = e.get("sha256", "")
    return out


def _sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def audit_kind(archive: Path, kind: str, dates: list[str], game_filter: set[str] | None = None) -> dict[str, Any]:
    files = _partition_files(archive, kind, dates)
    rel = {str(p.relative_to(archive)): p for p in files}
    recorded = manifest_hashes(archive, set(rel))
    integrity = {"files": len(files), "verified": 0, "mismatch": [], "not_in_manifest": []}
    for r, p in rel.items():
        if r not in recorded:
            integrity["not_in_manifest"].append(r)
        elif recorded[r] == _sha(p):
            integrity["verified"] += 1
        else:
            integrity["mismatch"].append(r)
    games: dict[str, dict[str, Any]] = {}
    for p in files:
        for r in _rows(p):
            gid = str(r.get("game_id"))
            if game_filter is not None and gid not in game_filter:
                continue
            at = r.get("predicted_at_utc")
            mts = r.get("minutes_to_start")
            if not at or mts is None:
                continue
            g = games.setdefault(gid, {"home": r.get("home"), "away": r.get("away"), "runs": {}, "starts": []})
            t = parse_iso(at)
            g["starts"].append(t + timedelta(minutes=float(mts)))
            run = g["runs"].setdefault(at, {"predicted_at_utc": at, "minutes_to_start": float(mts), "rows": 0, "pregame": bool(r.get("pregame")),
                                            "home_goalie_status": r.get("home_goalie_status"), "away_goalie_status": r.get("away_goalie_status")})
            run["rows"] += 1
    out_games: dict[str, Any] = {}
    for gid, g in games.items():
        starts = sorted(g["starts"])
        start = starts[len(starts) // 2]                                     # predicted_at + minutes_to_start, median over rows (rounded minutes)
        runs = sorted(g["runs"].values(), key=lambda x: x["predicted_at_utc"])
        pre = [x for x in runs if x["pregame"]]
        late = [x for x in runs if not x["pregame"]]
        last = pre[-1] if pre else None
        out_games[gid] = {"start_utc_derived": iso(start).replace(":00Z", ":00Z"), "runs_pregame": len(pre), "runs_late": len(late), "rows_late": sum(x["rows"] for x in late),
                          "last_pregame_at_utc": last["predicted_at_utc"] if last else None, "last_pregame_minutes_to_start": last["minutes_to_start"] if last else None,
                          "goalies_at_last_pregame": [last["home_goalie_status"], last["away_goalie_status"]] if last else None,
                          "first_late_at_utc": late[0]["predicted_at_utc"] if late else None, "pregame_run_times": [x["predicted_at_utc"] for x in pre]}
    return {"kind": kind, "integrity": integrity, "games": out_games}


def audit_day(archive: Path, date_et: str, utc_dates: list[str] | None = None, kinds: tuple[str, ...] = KINDS) -> dict[str, Any]:
    """``utc_dates`` are the ``dt=`` partitions to read: the ET game day spans two UTC dates (default: that date and the next)."""
    from datetime import date

    d0 = date.fromisoformat(date_et)
    dates = utc_dates or [d0.isoformat(), (d0 + timedelta(days=1)).isoformat()]
    res: dict[str, Any] = {"date_et": date_et, "partitions": dates, "kinds": {}}
    v1 = audit_kind(archive, "predictions", dates)
    # keep only games whose derived start falls on the ET date (EDT = UTC-4, EST = UTC-5; the ET day ends by 05:00 UTC the next day)
    day = {gid: g for gid, g in v1["games"].items() if iso(parse_iso(g["start_utc_derived"]) - timedelta(hours=5))[:10] == date_et}
    res["kinds"]["predictions"] = {**v1, "games": day}
    for k in kinds:
        if k == "predictions" or not (archive / k).exists():
            continue
        res["kinds"][k] = audit_kind(archive, k, dates, set(day))
    return res


def render(res: dict[str, Any]) -> str:
    v1 = res["kinds"]["predictions"]
    L = [f"# Pre-puck-drop projection audit — {res['date_et']} (ET)", "",
         "RESEARCH_ONLY · read-only audit of the append-only archive · start times are derived as `predicted_at + minutes_to_start` (rounded to 0.1 min)", "",
         "| game_id | start (UTC) | last pregame forecast | min before start | pregame runs | goalies H/A at last pregame | late runs (rows) after start |", "|---|---|---|---:|---:|---|---|"]
    for gid, g in sorted(v1["games"].items(), key=lambda kv: kv[1]["start_utc_derived"]):
        gl = "/".join(str(x)[:4] for x in g["goalies_at_last_pregame"]) if g["goalies_at_last_pregame"] else "-"
        mts = "-" if g["last_pregame_minutes_to_start"] is None else f"{g['last_pregame_minutes_to_start']:.1f}"
        L.append(f"| {gid} | {g['start_utc_derived']} | {g['last_pregame_at_utc'] or 'NONE'} | {mts} | {g['runs_pregame']} | {gl} | {g['runs_late']} ({g['rows_late']}) |")
    L += ["", "## Archive integrity (sha256 recorded in manifest.jsonl at write time vs file now)", "", "| kind | files | verified | mismatch | not in manifest |", "|---|---:|---:|---:|---:|"]
    for k, d in res["kinds"].items():
        i = d["integrity"]
        L.append(f"| {k} | {i['files']} | {i['verified']} | {len(i['mismatch'])} | {len(i['not_in_manifest'])} |")
    L += ["", "Late rows are forecasts written at or after the puck drop (the simulator keeps running while a game is live). They are retained unchanged in the archive but are **not** pregame forecasts and must be excluded from every pregame score."]
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.pregame_audit")
    ap.add_argument("--archive", required=True, help="data-archive checkout (predictions*/, manifest.jsonl)")
    ap.add_argument("--date", required=True, help="ET game day, YYYY-MM-DD")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    res = audit_day(Path(a.archive), a.date)
    md = render(res)
    print(md)
    if a.out:
        out = Path(a.out)
        out.mkdir(parents=True, exist_ok=True)
        (out / f"{a.date}_pregame_audit.json").write_text(json.dumps(res, indent=1, default=str))
        (out / f"{a.date}_pregame_audit.md").write_text(md)
    bad = sum(len(d["integrity"]["mismatch"]) for d in res["kinds"].values())
    return 2 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
