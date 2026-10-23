"""Audit of the pregame projection snapshots of one slate date (RESEARCH_ONLY, read-only).

Question answered: for every game of ``date``, which forecasts were GENUINELY available before puck drop, how old was the input
data when they were made, and which later artefacts are post-puck-drop or late-arriving? It reads immutable records only
(``predictions`` in data-archive; ``forecasts`` / ``runs`` in projection-data) and writes nothing back; no prediction, timestamp or
file is changed. "Available before puck drop" means ``archived_utc`` (the instant the record was written to its append-only ledger)
is at or before the scheduled start; ``generated_utc`` / ``predicted_at_utc`` is when the model ran, ``data_asof_utc`` /
``data_cutoff_utc`` the cut of its inputs. A record whose archive time is after the start is "late-arriving" even if it claims an
earlier model time.

Sources are either a directory checkout or a git ref in a (partial) clone: ``git:<repo>:<ref>``.
"""

from __future__ import annotations

import argparse
import gzip
import json
import subprocess
import sys
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from datetime import date as _date
from pathlib import Path


def _dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


def _iso(t: datetime | None) -> str | None:
    return t.strftime("%Y-%m-%dT%H:%M:%SZ") if t else None


class Tree:
    """A read-only file tree: a directory or a git ref. ``ls(prefix)`` -> paths, ``read(path)`` -> bytes."""

    def __init__(self, spec: str) -> None:
        self.git: tuple[str, str] | None = None
        self.root: Path | None = None
        if spec.startswith("git:"):
            _, repo, ref = spec.split(":", 2)
            self.git = (repo, ref)
        else:
            self.root = Path(spec)

    def ls(self, prefix: str) -> list[str]:
        if self.git:
            repo, ref = self.git
            out = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", ref, "--", prefix], capture_output=True, text=True, check=False)
            return sorted(x for x in out.stdout.splitlines() if x)
        base = self.root / prefix if self.root else None
        if base is None or not base.exists():
            return []
        return sorted(str(p.relative_to(self.root)) for p in base.rglob("*") if p.is_file())

    def read(self, path: str) -> bytes:
        if self.git:
            repo, ref = self.git
            return subprocess.run(["git", "-C", repo, "show", f"{ref}:{path}"], capture_output=True, check=True).stdout
        return (self.root / path).read_bytes()

    def rows(self, path: str) -> Iterable[dict]:
        raw = self.read(path)
        if path.endswith(".gz"):
            raw = gzip.decompress(raw)
        for line in raw.decode().splitlines():
            if line.strip():
                try:
                    yield json.loads(line)
                except ValueError:
                    continue


@dataclass
class Snap:
    """One distinct (model, model run) of a game: all rows sharing it were produced and archived together."""

    kind: str                 # v1 | v2 | pf_challenger | pf_incumbent
    generated: datetime | None
    archived: datetime | None
    data_asof: datetime | None
    n_rows: int = 0
    detail: dict | None = None


def _pregame(s: Snap, start: datetime) -> bool:
    return s.archived is not None and s.archived <= start


def audit(date: str, da: Tree, pd: Tree) -> dict:
    games: dict[str, dict] = {}

    def game(gid: str, start: datetime | None = None, exact: bool = False) -> dict:
        g = games.setdefault(gid, {"game_id": gid, "start": start, "snaps": defaultdict(dict), "home": None, "away": None, "exact": False})
        if start and (not g["start"] or (exact and not g["exact"])):
            g["start"], g["exact"] = start, exact
        return g

    # ---- V1 / V2 (data-archive 'predictions', 'predictions_v2'): one snapshot per (run, predicted_at)
    for kind, base, key in (("v1", "predictions", "predicted_at_utc"), ("v2", "predictions_v2", "predicted_at_utc")):
        # partitions are by UTC date: an evening slate spills into the next one
        for path in da.ls(f"{base}/dt={date}/") + da.ls(f"{base}/dt={_next_day(date)}/"):
            seen: set[tuple[str, str]] = set()
            for r in da.rows(path):
                gid, pa = str(r.get("game_id") or ""), r.get(key)
                if not gid or not pa or (gid, pa) in seen:
                    continue
                seen.add((gid, pa))
                pred = _dt(pa)
                m = r.get("minutes_to_start")
                start = None
                if pred is not None and isinstance(m, (int, float)):
                    start = pred + timedelta(minutes=float(m))
                g = game(gid, start)
                snap = Snap(kind, pred, _dt(r.get("_observed_at_utc")), _dt(r.get("data_cutoff_utc")), 0,
                            {"home_goalie": r.get("home_goalie_status"), "away_goalie": r.get("away_goalie_status"), "minutes_to_start": m, "horizon": r.get("horizon_label"),
                             "market_observed": r.get("market_observed_at_utc")})
                g["snaps"][kind][(path, pa)] = snap

    # ---- projection-foundation (projection-data 'forecasts'): dated by game date and by archive date
    for d in {date, _next_day(date)}:
        for path in pd.ls(f"forecasts/nhl/{d}/"):
            per: dict[tuple[str, str, str], Snap] = {}
            for r in pd.rows(path):
                gid = str(r.get("game_id") or "")
                if not gid:
                    continue
                start = _dt(r.get("game_start_utc"))
                if start is None or start.astimezone(UTC).strftime("%Y-%m-%d") not in (date, _next_day(date)):
                    continue
                role = r.get("model_role") or "?"
                k = (gid, role, r.get("generated_utc") or "")
                if k not in per:
                    per[k] = Snap("pf_" + role, _dt(r.get("generated_utc")), _dt(r.get("archived_utc")), _dt(r.get("data_asof_utc")), 0, {"path": path})
                per[k].n_rows += 1
                game(gid, start, exact=True)           # the forecast record carries the scheduled start verbatim
            for (gid, role, gen), s in per.items():
                games[gid]["snaps"]["pf_" + role][(s.detail["path"], gen)] = s

    # ---- PF run reports (inputs of the project stage: capture ages)
    runs = []
    for path in pd.ls(f"runs/nhl/{date}/") + pd.ls(f"runs/nhl/{_next_day(date)}/"):
        try:
            rep = json.loads(pd.read(path))
        except (ValueError, subprocess.CalledProcessError):
            continue
        runs.append({"path": path, "archived_at": rep.get("archived_at"), "assemble": rep.get("assemble"),
                     "newest_capture_age_min": {gid: ev.get("newest_age_minutes") for gid, ev in ((rep.get("coverage") or {}).get("events") or {}).items()}})
    run_times = [(_dt(r["archived_at"]), r) for r in runs if _dt(r["archived_at"])]

    out_games = []
    for gid, g in sorted(games.items(), key=lambda kv: (kv[1]["start"] or datetime.max.replace(tzinfo=UTC), kv[0])):
        start = g["start"]
        if start is None or start.strftime("%Y-%m-%d") not in (date, _next_day(date)):
            continue
        row = {"game_id": gid, "start_utc": _iso(start), "kinds": {}}
        for kind, snaps in g["snaps"].items():
            ordered = sorted(snaps.values(), key=lambda s: (s.archived or datetime.min.replace(tzinfo=UTC), s.generated or datetime.min.replace(tzinfo=UTC)))
            pre = [s for s in ordered if _pregame(s, start)]
            post = [s for s in ordered if not _pregame(s, start)]
            last = pre[-1] if pre else None
            row["kinds"][kind] = {
                "n_pregame": len(pre), "n_post_start": len(post),
                "last_pregame_archived_utc": _iso(last.archived) if last else None,
                "last_pregame_generated_utc": _iso(last.generated) if last else None,
                "last_pregame_minutes_before_start": round((start - last.archived).total_seconds() / 60, 1) if last else None,
                "last_pregame_input_asof_utc": _iso(last.data_asof) if last else None,
                "last_pregame_input_age_min": round((last.generated - last.data_asof).total_seconds() / 60, 1) if last and last.generated and last.data_asof else None,
                "pregame_archive_times_utc": [_iso(s.archived) for s in pre][-8:],
                "first_post_start_archived_utc": _iso(post[0].archived) if post else None,
                "last_pregame_detail": last.detail if last and kind in ("v1", "v2") else None,
            }
        ev = [(t, r) for t, r in run_times if t <= start and gid in (r.get("newest_capture_age_min") or {})]
        if ev:
            t, r = ev[-1]
            row["pf_last_evaluation_before_start"] = {"archived_utc": _iso(t), "minutes_before_start": round((start - t).total_seconds() / 60, 1),
                                                     "newest_capture_age_min": r["newest_capture_age_min"].get(gid)}
        else:
            row["pf_last_evaluation_before_start"] = None
        out_games.append(row)
    return {"date": date, "n_games": len(out_games), "games": out_games, "pf_runs": runs, "definition": __doc__.split("\n\n")[1].strip()}


def _next_day(date: str) -> str:
    return (_date.fromisoformat(date) + timedelta(days=1)).isoformat()


def markdown(rep: dict) -> str:
    lines = [f"# Pregame snapshot audit, slate {rep['date']}", "", "_Read-only audit of immutable records; no prediction or timestamp was changed._", "", rep["definition"], "",
             "A projection-foundation forecast row is written only when its content changed, so \"last write\" can be old while the last *evaluation* (a run that re-checked the game and found nothing new) is recent; both are shown.",
             "",
             "| game | start (UTC) | V1 last pregame (min before) | V1 goalies H/A | PF last write: challenger / incumbent (min before) | PF last evaluation (min before) | lineup capture age at that run (min) | rows archived after start |",
             "|---|---|---|---|---|---|---|---|"]
    for g in rep["games"]:
        k = g["kinds"]

        def mb(kind, k=k):
            x = k.get(kind) or {}
            return "-" if x.get("last_pregame_minutes_before_start") is None else f"{x['last_pregame_minutes_before_start']:.0f}"

        v1 = k.get("v1") or {}
        det = v1.get("last_pregame_detail") or {}
        gl = f"{det.get('home_goalie', '-')}/{det.get('away_goalie', '-')}"
        ev = g.get("pf_last_evaluation_before_start") or {}
        evm = "-" if not ev else f"{ev['minutes_before_start']:.0f}"
        age = "-" if not ev or ev.get("newest_capture_age_min") is None else f"{ev['newest_capture_age_min']:.0f}"
        post = sum((x or {}).get("n_post_start", 0) for x in k.values())
        lines.append(f"| {g['game_id']} | {g['start_utc']} | {mb('v1')} | {gl} | {mb('pf_challenger')} / {mb('pf_incumbent')} | {evm} | {age} | {post} |")
    lines += ["", "## Projection-foundation runs", "", "| archived | rows | confirmed active | newest capture age, min (min / max over games) |", "|---|---|---|---|"]
    for r in rep["pf_runs"]:
        a = (r.get("assemble") or {})
        ages = [v for v in (r.get("newest_capture_age_min") or {}).values() if v is not None]
        part = (a.get("participation") or {})
        lines.append(f"| {r['archived_at']} | {a.get('rows')} | {part.get('CONFIRMED_ACTIVE', 0)} | {min(ages):.0f} / {max(ages):.0f} |" if ages else f"| {r['archived_at']} | {a.get('rows')} | {part.get('CONFIRMED_ACTIVE', 0)} | - |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.snapshot_audit")
    ap.add_argument("--date", required=True, help="slate date, ET calendar date used by the archives (YYYY-MM-DD)")
    ap.add_argument("--data-archive", required=True, help="directory or git:<repo>:<ref> of data-archive")
    ap.add_argument("--projection-data", required=True, help="directory or git:<repo>:<ref> of projection-data")
    ap.add_argument("--out", required=True, help="output prefix; writes <out>.json and <out>.md")
    a = ap.parse_args(argv)
    rep = audit(a.date, Tree(a.data_archive), Tree(a.projection_data))
    Path(a.out + ".json").write_text(json.dumps(rep, indent=1, default=str))
    Path(a.out + ".md").write_text(markdown(rep))
    print(f"{rep['n_games']} games audited")
    return 0


if __name__ == "__main__":
    sys.exit(main())
