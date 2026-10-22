"""Weekly / monthly research summary and integrity alerts, built only from outputs the pipeline already writes (RESEARCH_ONLY).

Inputs (read-only): the archive's ``eval/report.json`` (V1 / market / market-anchored scores per contract family),
``eval/report_player.json`` (PLAYER_SIM_V1), ``eval/report_learning.json`` (settled counts, stage) and the ``STATUS_*.json``
heartbeat files; optionally the projection-foundation scorecard (``scorecards/nhl/weekly.json``).

Two products, deliberately separate:

* ``summary`` -- the narrative scoreboard (always produced; goes to the job summary / an artifact, never to an issue).
* ``alerts`` -- integrity problems only (stale or failing jobs, missing reports, calibration collapse on a large sample,
  a projection scorecard in ALERT). Model *performance* is never an alert: the market beating V1 is a finding, not an outage.

Contract rows are not independent games (a game spawns many contracts and snapshots); the per-family ``n`` printed here is a
contract count and must not be read as a game count. Independent-game counts come from the learning report.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from nhl_edge.timeutil import iso, parse_iso, utcnow

KEY_FAMILIES = ("game_winner", "game_spread", "game_total", "team_total", "period_winner", "period_total", "game_overtime")
STALE_HOURS = {"STATUS_capture.json": ("last_capture_utc", 1.0), "STATUS_simulate.json": ("simulated_at_utc", 8.0), "STATUS_settle.json": ("settled_at_utc", 12.0),
               "STATUS_evaluate.json": ("evaluated_at_utc", 30.0), "STATUS_context.json": ("refreshed_at_utc", 8.0)}
ECE_ALERT = 0.15            # on a family with at least ECE_MIN_N contracts
ECE_MIN_N = 5000


def _load(p: Path) -> Any | None:
    try:
        return json.loads(p.read_text())
    except (OSError, json.JSONDecodeError):
        return None


def _age_h(ts: str | None, now: datetime) -> float | None:
    try:
        return (now - parse_iso(ts)).total_seconds() / 3600.0 if ts else None
    except ValueError:
        return None


def integrity_alerts(archive: Path, now: datetime, in_game_season: bool = True) -> list[dict[str, str]]:
    out: list[dict[str, str]] = []
    for fname, (key, limit_h) in STALE_HOURS.items():
        d = _load(archive / fname)
        if d is None:
            out.append({"code": "STATUS_MISSING", "message": f"{fname} missing or unreadable"})
            continue
        age = _age_h(d.get(key), now)
        if in_game_season and (age is None or age > limit_h):
            out.append({"code": "STATUS_STALE", "message": f"{fname}: {key} is {'missing' if age is None else f'{age:.1f} h old'} (limit {limit_h:.0f} h)"})
    sett = _load(archive / "STATUS_settle.json") or {}
    if sett.get("errors") or sett.get("disagreements"):
        out.append({"code": "SETTLE_PROBLEM", "message": f"settle errors={len(sett.get('errors') or [])} disagreements={len(sett.get('disagreements') or [])}"})
    ev = _load(archive / "eval" / "report.json")
    if ev is None:
        out.append({"code": "EVAL_REPORT_MISSING", "message": "eval/report.json missing"})
    else:
        for fam, f in (ev.get("families") or {}).items():
            for view, m in (f.get("views") or {}).items():
                if m.get("n", 0) >= ECE_MIN_N and (m.get("ece") or 0) > ECE_ALERT:
                    out.append({"code": "CALIBRATION_COLLAPSE", "message": f"{fam}/{view}: ECE {m['ece']:.3f} on {m['n']} contracts"})
    ev_status = _load(archive / "STATUS_evaluate.json") or {}
    for step, val in (ev_status.get("steps") or {}).items():
        if str(val).startswith("FAILED"):
            out.append({"code": "EVAL_STEP_FAILED", "message": f"evaluate step {step}: {val}"})
    return out


def _fmt(x: Any, nd: int = 4) -> str:
    return "-" if x is None else f"{x:.{nd}f}" if isinstance(x, float) else str(x)


def render_summary(archive: Path, now: datetime, alerts: list[dict[str, str]], pf_scorecard: dict[str, Any] | None = None) -> str:
    ev = _load(archive / "eval" / "report.json") or {}
    pl = _load(archive / "eval" / "report_player.json") or {}
    lr = _load(archive / "eval" / "report_learning.json") or {}
    cnt = lr.get("counts") or {}
    lines = [f"# NHL research summary — {iso(now)}", "",
             f"RESEARCH_ONLY · evaluated {ev.get('evaluated_at_utc', '?')} · games settled {cnt.get('games_settled', '?')} of {cnt.get('games_projected', '?')} projected · learning stage "
             f"`{(lr.get('stage') or {}).get('stage', '?')}`", ""]
    lines += ["## Integrity", ""] + ([f"- **{a['code']}** {a['message']}" for a in alerts] or ["- all heartbeats fresh; no settlement problems; no calibration collapse"]) + [""]
    lines += ["## Live pregame scores by family (contract rows, NOT independent games)", "",
              "| family | view | contracts | Brier | log loss | ECE |", "|---|---|---:|---:|---:|---:|"]
    for fam in KEY_FAMILIES:
        for view, m in ((ev.get("families") or {}).get(fam, {}).get("views") or {}).items():
            if m.get("n"):
                lines.append(f"| {fam} | {view} | {m['n']} | {_fmt(m.get('brier'))} | {_fmt(m.get('log_loss'))} | {_fmt(m.get('ece'))} |")
    lines += ["", "The market is the benchmark. A model scoring worse than `MARKET_BASELINE` is the finding, not an outage; differences below ~0.004 Brier are below what ~150 independent games can resolve.", ""]
    if pl.get("overall"):
        lines += ["## Player layer (PLAYER_SIM_V1, shadow)", "", "| view | n | Brier | ECE |", "|---|---:|---:|---:|"]
        for v, m in pl["overall"].items():
            if m.get("n"):
                lines.append(f"| {v} | {m['n']} | {_fmt(m.get('brier'))} | {_fmt(m.get('ece'))} |")
        lines.append("")
    if pf_scorecard:
        lines += ["## Projection foundation scorecard", "", f"alerts: `{json.dumps(pf_scorecard.get('alerts', {}), sort_keys=True)}`", f"promotion: `{json.dumps(pf_scorecard.get('promotion', {}), sort_keys=True)}`", ""]
    return "\n".join(lines) + "\n"


def run(archive: Path, out: Path | None, pf_dir: Path | None = None, now: datetime | None = None) -> int:
    now = now or utcnow()
    alerts = integrity_alerts(archive, now)
    pf = _load(pf_dir / "scorecards" / "nhl" / "weekly.json") if pf_dir else None
    if pf and any(str(v).upper() == "ALERT" for v in (pf.get("alerts") or {}).values()):
        alerts.append({"code": "PF_SCORECARD_ALERT", "message": f"projection-foundation weekly alerts: {pf.get('alerts')}"})
    md = render_summary(archive, now, alerts, pf)
    print(md)
    if out:
        out.mkdir(parents=True, exist_ok=True)
        (out / "summary.md").write_text(md)
        (out / "alerts.json").write_text(json.dumps({"generated_at_utc": iso(now), "alerts": alerts}, indent=1))
    return 2 if alerts else 0


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.weekly_summary")
    ap.add_argument("--archive", required=True, help="data-archive checkout (needs STATUS_*.json and eval/)")
    ap.add_argument("--pf", help="projection-data checkout (optional)")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    return run(Path(a.archive), Path(a.out) if a.out else None, Path(a.pf) if a.pf else None)


if __name__ == "__main__":
    sys.exit(main())
