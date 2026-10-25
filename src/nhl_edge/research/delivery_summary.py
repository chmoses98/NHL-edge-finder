"""Multi-slate summary of pregame forecast delivery (RESEARCH_ONLY, read-only).

For every regular-season game in a date range: the last projection run that *evaluated* the game before its puck drop (from ``projection-data`` ``runs/``), how many minutes before the drop
that was, how old the lineup capture it used was, whether any pregame forecast row exists, and the slate size. Slates are grouped by ET date, so "larger slates" can be read directly.
A forecast whose values did not change is not a failure; a game with no pregame evaluation, or one older than the stale limits of ``delivery_monitor``, is.

    python -m nhl_edge.research.delivery_summary --pf <projection-data checkout> --schedule <context/schedule files...> --from 2026-10-18 --to 2026-10-24 --out out/delivery_summary
"""

from __future__ import annotations

import argparse
import glob
import gzip
import json
import statistics as st
import sys
from pathlib import Path
from typing import Any

from nhl_edge.research.delivery_monitor import STALE_EVAL_MIN, STALE_LINEUP_MIN, _dt, load_games


def evaluations(pf: Path) -> dict[str, list[tuple[Any, float | None]]]:
    """game_id -> [(run archived_at, newest lineup capture age in minutes at that run)] over every run partition present."""
    out: dict[str, list[tuple[Any, float | None]]] = {}
    for p in sorted(glob.glob(str(Path(pf) / "runs" / "nhl" / "*" / "*_project.json"))):
        try:
            r = json.loads(Path(p).read_text())
        except (OSError, ValueError):
            continue
        at = _dt(r.get("archived_at"))
        if at is None:
            continue
        for gid, ev in ((r.get("coverage") or {}).get("events") or {}).items():
            age = ev.get("newest_age_minutes") if isinstance(ev, dict) else None
            out.setdefault(str(gid), []).append((at, None if age is None else float(age)))
    return out


def pregame_rows(pf: Path) -> dict[str, int]:
    n: dict[str, int] = {}
    for p in glob.glob(str(Path(pf) / "forecasts" / "nhl" / "*" / "*.jsonl.gz")):
        try:
            with gzip.open(p, "rt", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        r = json.loads(line)
                        a, s = _dt(r.get("archived_utc")), _dt(r.get("game_start_utc"))
                        if a and s and a <= s:
                            n[str(r.get("game_id"))] = n.get(str(r.get("game_id")), 0) + 1
        except (OSError, ValueError):
            continue
    return n


def summarize(games: list[dict[str, Any]], ev: dict[str, list[tuple[Any, float | None]]], rows: dict[str, int], d_from: str, d_to: str) -> dict[str, Any]:
    per_game, by_day = [], {}
    for g in games:
        if str(g.get("season_type", "regular")).lower() not in ("regular", "2") or not (d_from <= str(g.get("game_date_et")) <= d_to):
            continue
        start = _dt(g.get("start_time_utc"))
        if start is None:
            continue
        gid = str(g["game_id"])
        before = [(a, age) for a, age in ev.get(gid, []) if a <= start]
        last = max(before, default=None, key=lambda x: x[0])
        lead = None if last is None else round((start - last[0]).total_seconds() / 60, 1)
        lin = None if last is None else last[1]
        status = "MISSING" if not rows.get(gid) and last is None else ("NO_EVALUATION" if last is None else ("STALE_LINEUP" if lin is not None and lin > STALE_LINEUP_MIN else "OK"))
        rec = {"game_id": gid, "date_et": str(g["game_date_et"]), "start_utc": g["start_time_utc"], "n_evaluations_before_drop": len(before), "last_eval_lead_min": lead,
               "lineup_age_at_last_eval_min": lin, "n_pregame_forecast_rows": rows.get(gid, 0), "status": status}
        per_game.append(rec)
        by_day.setdefault(rec["date_et"], []).append(rec)
    days = []
    for d, rs in sorted(by_day.items()):
        leads = [r["last_eval_lead_min"] for r in rs if r["last_eval_lead_min"] is not None]
        ages = [r["lineup_age_at_last_eval_min"] for r in rs if r["lineup_age_at_last_eval_min"] is not None]
        days.append({"date_et": d, "games": len(rs), "ok": sum(1 for r in rs if r["status"] == "OK"), "problems": [r["game_id"] for r in rs if r["status"] != "OK"],
                     "min_last_eval_lead_min": min(leads) if leads else None, "median_last_eval_lead_min": st.median(leads) if leads else None,
                     "median_lineup_age_min": round(st.median(ages), 1) if ages else None, "max_lineup_age_min": max(ages) if ages else None})
    return {"from": d_from, "to": d_to, "stale_lineup_limit_min": STALE_LINEUP_MIN, "stale_eval_limit_min": STALE_EVAL_MIN, "days": days, "games": per_game}


def render(s: dict[str, Any]) -> str:
    L = [f"# Pregame forecast delivery across slates {s['from']} … {s['to']} (research only)", "",
         "| slate (ET) | games | ok | problems | earliest last-evaluation lead (min) | median lead | median lineup age at that evaluation | max lineup age |", "|---|---:|---:|---|---:|---:|---:|---:|"]
    for d in s["days"]:
        L.append(f"| {d['date_et']} | {d['games']} | {d['ok']} | {', '.join(d['problems']) or '—'} | {d['min_last_eval_lead_min']} | {d['median_last_eval_lead_min']} | {d['median_lineup_age_min']} | {d['max_lineup_age_min']} |")
    L.append("\nLead = minutes between the last projection run that evaluated the game and its puck drop; a forecast row exists only when values changed, so a long gap since the last *row* is not a failure.")
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.delivery_summary")
    ap.add_argument("--pf", required=True)
    ap.add_argument("--schedule", nargs="+", required=True)
    ap.add_argument("--from", dest="d_from", required=True)
    ap.add_argument("--to", dest="d_to", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    files = [Path(f) for pat in a.schedule for f in sorted(glob.glob(pat))]
    s = summarize(load_games(files), evaluations(Path(a.pf)), pregame_rows(Path(a.pf)), a.d_from, a.d_to)
    Path(a.out).with_suffix(".json").write_text(json.dumps(s, indent=1))
    md = render(s)
    Path(a.out).with_suffix(".md").write_text(md)
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
