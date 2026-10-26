"""When does the NHL actually publish lineup information before a puck drop? (RESEARCH_ONLY, read-only, identifying User-Agent)

For each regular-season game of a day, poll the same public NHL endpoints the pipeline already reads (``gamecenter/{id}/landing`` and ``/right-rail``) at fixed offsets before the drop
(T-120 ... T-5 minutes) and record, per poll, what is present: HTTP status, size, content hash, game state, and every structure whose key names look like a lineup, scratch list, roster, starter or
goalie (with item counts and player ids). Raw bodies are stored whenever the hash changes, so the schema can be re-read offline. Nothing is inferred or back-filled: a poll that does not
happen is a missing observation. Optionally (``--sheets``, off by default, only after the access audit allows it) the official HTML game roster sheet is probed the same way.

Output: write-once ``obs/`` and ``raw/`` files with an append-only manifest, intended for the orphan branch ``lineup-probe-data``.

    python -m nhl_edge.research.nhl_lineup_probe watch --date 2026-10-25 --out /tmp/probe --tag A --from-utc 2026-10-25T19:00:00Z --to-utc 2026-10-25T21:00:00Z
    python -m nhl_edge.research.nhl_lineup_probe summarize --out /tmp/probe
"""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
import re
import sys
import time
from collections.abc import Callable
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import httpx

from nhl_edge.config import settings
from nhl_edge.timeutil import iso, parse_iso

OFFSETS_MIN = (120, 90, 75, 60, 45, 30, 20, 12, 8, 5)
LATE_GRACE_MIN = 2.0          # smaller than the smallest gap between offsets (3 min): a late poll can never be labelled as the next offset's
ENDPOINTS = ("landing", "right-rail")
KEY_RE = re.compile(r"scratch|lineup|roster|starting|starter|probable|goalie|depth|injur|healthy|dressed", re.I)
API = "https://api-web.nhle.com/v1"
SHEET = "https://www.nhl.com/scores/htmlreports/{season}/RO{num}.HTM"
Getter = Callable[[str], tuple[int, bytes]]


def http_get(url: str, timeout: float = 25.0) -> tuple[int, bytes]:
    try:
        r = httpx.get(url, headers={"User-Agent": settings().user_agent, "Accept": "*/*"}, timeout=timeout, follow_redirects=True)
        return r.status_code, r.content
    except httpx.HTTPError as e:
        return 0, f"{type(e).__name__}: {e}".encode()[:200]


def _ids(v: Any, limit: int = 40) -> list[Any]:
    out: list[Any] = []
    stack = [v]
    while stack and len(out) < limit:
        x = stack.pop()
        if isinstance(x, dict):
            for k in ("playerId", "id"):
                if isinstance(x.get(k), int):
                    out.append(x[k])
                    break
            else:
                stack.extend(x.values())
        elif isinstance(x, list):
            stack.extend(x)
    return sorted(set(out))


def interesting(obj: Any, path: str = "", depth: int = 0) -> dict[str, dict[str, Any]]:
    """{path: {n, ids}} for every key whose name looks lineup-related and whose value is non-trivial (a list/dict, counted)."""
    out: dict[str, dict[str, Any]] = {}
    if depth > 8:
        return out
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}" if path else str(k)
            if KEY_RE.search(str(k)) and isinstance(v, (list, dict)):
                out[p] = {"n": len(v), "ids": _ids(v)}
            out.update(interesting(v, p, depth + 1))
    elif isinstance(obj, list):
        for i, v in enumerate(obj[:3]):
            out.update(interesting(v, f"{path}[{i}]", depth + 1))
    return out


def features(status: int, body: bytes) -> dict[str, Any]:
    f: dict[str, Any] = {"status": status, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    if status == 200:
        try:
            j = json.loads(body)
        except ValueError:
            f["note"] = "not json"
            return f
        f["game_state"] = j.get("gameState") if isinstance(j, dict) else None
        f["top_keys"] = sorted(j)[:40] if isinstance(j, dict) else None
        f["interesting"] = interesting(j)
    return f


def sheet_features(status: int, body: bytes) -> dict[str, Any]:
    f: dict[str, Any] = {"status": status, "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    if status == 200:
        t = body.decode("utf-8", "replace")
        f["mentions_scratches"] = "scratch" in t.lower()
        f["n_player_rows"] = len(re.findall(r"<td[^>]*>\s*\d{1,2}\s*</td>", t))
    return f


def write_once(out: Path, tag: str, rel: str, rows: list[dict[str, Any]]) -> None:
    """Write-once gz file plus one line in this run's own manifest ``MANIFEST.<tag>.jsonl`` (parallel runs never touch the same manifest)."""
    p = out / rel
    if p.exists():
        raise FileExistsError(f"refusing to overwrite {rel}")
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, separators=(",", ":")) + "\n")
    tmp.replace(p)
    entry = {"path": rel, "rows": len(rows), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "written_at_utc": iso(datetime.now(UTC))}
    with (out / f"MANIFEST.{tag}.jsonl").open("a") as m:
        m.write(json.dumps(entry) + "\n")


class Probe:
    def __init__(self, out: Path, get: Getter = http_get, sheets: bool = False, tag: str = "run", clock: Callable[[], datetime] | None = None, store_raw: bool = False) -> None:
        self.out, self.get, self.sheets, self.tag, self.store_raw = out, get, sheets, tag, store_raw
        self.clock = clock or (lambda: datetime.now(UTC))
        self.buf: list[dict[str, Any]] = []
        self.raw: list[dict[str, Any]] = []
        self.last_sha: dict[tuple[int, str], str] = {}

    def poll_game(self, g: dict[str, Any], offset: int, now: datetime | None = None) -> None:
        gid, start = int(g["id"]), parse_iso(g["startTimeUTC"])
        targets = [(e, f"{API}/gamecenter/{gid}/{e}", features) for e in ENDPOINTS]
        if self.sheets:
            season = str(g.get("season") or "")
            targets.append(("game-sheet-RO", SHEET.format(season=season, num=f"{gid % 1_000_000:06d}"), sheet_features))
        for name, url, feat in targets:
            status, body = self.get(url)
            at = self.clock()                                   # stamped when the response is in hand, not at the start of the tick
            row = {"game_id": gid, "endpoint": name, "offset_min": offset, "polled_at_utc": iso(at), "game_start_utc": g["startTimeUTC"],
                   "lead_min": round((start - at).total_seconds() / 60, 1), **feat(status, body)}
            self.buf.append(row)
            sha = row["sha256"]
            if status == 200 and self.store_raw and self.last_sha.get((gid, name)) != sha:
                self.last_sha[(gid, name)] = sha
                self.raw.append({"game_id": gid, "endpoint": name, "polled_at_utc": row["polled_at_utc"], "sha256": sha, "body_b64": base64.b64encode(gzip.compress(body)).decode()})

    def flush(self, now: datetime) -> None:
        stamp = now.strftime("%Y%m%dT%H%M%S%fZ")
        if self.buf:
            write_once(self.out, self.tag, f"obs/dt={now:%Y-%m-%d}/probe_{self.tag}_{stamp}.jsonl.gz", self.buf)
            self.buf = []
        if self.raw:
            write_once(self.out, self.tag, f"raw/dt={now:%Y-%m-%d}/raw_{self.tag}_{stamp}.jsonl.gz", self.raw)
            self.raw = []


def schedule_games(get: Getter, date_et: str, attempts: int = 3, sleep_fn: Callable[[float], None] = time.sleep) -> list[dict[str, Any]]:
    status, body = 0, b""
    for i in range(attempts):
        status, body = get(f"{API}/schedule/{date_et}")
        if status == 200:
            break
        sleep_fn(5.0 * (i + 1))
    if status != 200:
        raise RuntimeError(f"schedule for {date_et}: HTTP {status}")
    try:
        j = json.loads(body)
    except ValueError as e:
        raise RuntimeError(f"schedule for {date_et}: not json ({e})") from e
    for day in j.get("gameWeek") or []:
        if day.get("date") == date_et:
            return [g for g in day.get("games") or [] if g.get("gameType") == 2 and g.get("startTimeUTC")]
    return []


def watch(out: Path, date_et: str, get: Getter = http_get, sheets: bool = False, now_fn: Callable[[], datetime] | None = None, sleep_fn: Callable[[float], None] = time.sleep,
          max_minutes: float = 320.0, tick_s: float = 30.0, tag: str = "run", start_from: datetime | None = None, start_to: datetime | None = None,
          store_raw: bool = False) -> dict[str, Any]:
    """Poll the games of ``date_et`` (optionally only those starting in [start_from, start_to)) at the registered offsets until the last drop has passed (or ``max_minutes``).
    One poll per (game, offset). An offset that is already more than ``LATE_GRACE_MIN`` late when first seen is not polled: a ``skipped_late`` row is written instead, so a missing
    observation is visible in the data. Raises if the schedule cannot be read or the selection holds no game (a green run must mean something was watched)."""
    now_fn = now_fn or (lambda: datetime.now(UTC))
    games = [g for g in schedule_games(get, date_et, sleep_fn=sleep_fn)
             if (start_from is None or parse_iso(g["startTimeUTC"]) >= start_from) and (start_to is None or parse_iso(g["startTimeUTC"]) < start_to)]
    if not games:
        raise RuntimeError(f"no regular-season game on {date_et} in the selected window")
    p = Probe(out, get, sheets, tag, clock=now_fn, store_raw=store_raw)
    done: set[tuple[int, int]] = set()
    skipped: list[tuple[int, int]] = []
    t0 = now_fn()
    while True:
        now = now_fn()
        if (now - t0) > timedelta(minutes=max_minutes) or all(now > parse_iso(g["startTimeUTC"]) + timedelta(minutes=5) for g in games):
            break
        polled = False
        for g in games:
            start = parse_iso(g["startTimeUTC"])
            for off in OFFSETS_MIN:
                key = (int(g["id"]), off)
                now = now_fn()                                   # requests are sequential and can be slow: re-read the clock before every decision
                if key in done or now >= start:
                    continue
                due = start - timedelta(minutes=off)
                if now >= due:
                    done.add(key)
                    if now - due > timedelta(minutes=LATE_GRACE_MIN):
                        skipped.append(key)
                        p.buf.append({"game_id": key[0], "endpoint": "skipped_late", "offset_min": off, "polled_at_utc": iso(now), "game_start_utc": g["startTimeUTC"],
                                      "lead_min": round((start - now).total_seconds() / 60, 1), "status": None})
                    else:
                        p.poll_game(g, off)
                        polled = True
        if polled:
            p.flush(now_fn())
        sleep_fn(tick_s)
    p.flush(now_fn())
    return {"games": len(games), "polls": len(done) - len(skipped), "skipped_late": len(skipped), "date_et": date_et, "tag": tag}


def load_obs(out: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for f in sorted((out / "obs").rglob("*.jsonl.gz")) if (out / "obs").exists() else []:
        with gzip.open(f, "rt", encoding="utf-8") as fh:
            rows += [json.loads(line) for line in fh if line.strip()]
    return rows


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Per game and endpoint: the first poll (largest lead) at which a lineup-like structure was non-empty, and whether it changed afterwards."""
    by: dict[tuple[int, str], list[dict[str, Any]]] = {}
    for r in rows:
        if r["endpoint"] == "skipped_late":
            continue
        by.setdefault((r["game_id"], r["endpoint"]), []).append(r)
    out = []
    for (gid, ep), rs in sorted(by.items()):
        rs.sort(key=lambda r: -r["lead_min"])
        first: dict[str, float] = {}
        for r in rs:
            for path, v in (r.get("interesting") or {}).items():
                if v["n"] > 0 and path not in first:
                    first[path] = r["lead_min"]
        shas = [r["sha256"] for r in rs if r["status"] == 200]
        out.append({"game_id": gid, "endpoint": ep, "polls": len(rs), "ok": sum(1 for r in rs if r["status"] == 200), "statuses": sorted({r["status"] for r in rs}),
                    "first_nonempty_lead_min": first, "n_distinct_bodies": len(set(shas)), "changed_after_first_nonempty": len(set(shas)) > 1})
    return {"games": sorted({r["game_id"] for r in rows}), "per_game_endpoint": out}


def render(s: dict[str, Any]) -> str:
    L = ["# NHL lineup-publication timing probe (research only)", "", f"Games observed: {len(s['games'])}", "",
         "| game | endpoint | polls (ok) | statuses | first non-empty lineup-like structure (minutes before drop) | bodies |", "|---|---|---|---|---|---|"]
    for r in s["per_game_endpoint"]:
        fn = "; ".join(f"`{p}` @ T-{m:.0f}" for p, m in sorted(r["first_nonempty_lead_min"].items(), key=lambda kv: -kv[1])[:4]) or "none"
        L.append(f"| {r['game_id']} | {r['endpoint']} | {r['polls']} ({r['ok']}) | {r['statuses']} | {fn} | {r['n_distinct_bodies']} |")
    L.append("\nPublication is the first poll showing the structure, not the true publication instant: the error is at most the gap between polls. NHL does not label confirmed vs projected; a structure that appears only after warmups is treated as confirmed.")
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m nhl_edge.research.nhl_lineup_probe")
    sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("watch")
    w.add_argument("--date", required=True)
    w.add_argument("--out", required=True)
    w.add_argument("--sheets", action="store_true")
    w.add_argument("--max-minutes", type=float, default=320.0)
    w.add_argument("--tag", default="run")
    w.add_argument("--store-raw", action="store_true", help="also store raw response bodies (off by default: verbatim NHL responses are not republished while rights are unresolved)")
    w.add_argument("--from-utc", default=None, help="only games starting at or after this UTC instant")
    w.add_argument("--to-utc", default=None, help="only games starting before this UTC instant")
    s = sub.add_parser("summarize")
    s.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    if a.cmd == "watch":
        Path(a.out).mkdir(parents=True, exist_ok=True)
        try:
            rep = watch(Path(a.out), a.date, sheets=a.sheets, max_minutes=a.max_minutes, tag=a.tag, store_raw=a.store_raw, start_from=parse_iso(a.from_utc) if a.from_utc else None,
                        start_to=parse_iso(a.to_utc) if a.to_utc else None)
        except RuntimeError as e:
            print(json.dumps({"error": str(e)}))
            return 3
        print(json.dumps(rep))
        return 0
    md = render(summarize(load_obs(Path(a.out))))
    print(md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
