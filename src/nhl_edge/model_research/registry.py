"""Append-only, hash-chained experiment registry (JSON lines).

Entry types: ``PREREG`` (hypothesis + protocol + decision rule, written BEFORE the result is computed), ``RESULT``
(metrics, uncertainty, interpretation, decision, code commit, reproduction command) and ``NOTE``. Every line carries the
SHA-256 of the previous line, so any edit or deletion of history is detected by ``verify``. Unsuccessful experiments are
recorded exactly like successful ones; nothing here is ever rewritten. The frozen v1.0 hypothesis registry of the prior market
audit lives in ``nhl_edge.market_audit.hypotheses`` and is not touched by this module.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

GENESIS = "0" * 64


def _h(prev: str, body: dict[str, Any]) -> str:
    return hashlib.sha256((prev + json.dumps(body, sort_keys=True, default=str)).encode()).hexdigest()


def read(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def verify(path: Path) -> list[str]:
    problems: list[str] = []
    prev = GENESIS
    for i, e in enumerate(read(path)):
        body = {k: v for k, v in e.items() if k != "entry_hash"}
        if e.get("prev_hash") != prev:
            problems.append(f"line {i}: prev_hash mismatch")
        if _h(prev, body) != e.get("entry_hash"):
            problems.append(f"line {i}: entry_hash mismatch")
        if e.get("seq") != i:
            problems.append(f"line {i}: seq {e.get('seq')}")
        prev = e.get("entry_hash", "")
    return problems


def git_commit(repo: Path) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
    except OSError:
        return ""


def append(path: Path, entry_type: str, exp_id: str, fields: dict[str, Any], repo: Path | None = None, now: datetime | None = None) -> dict[str, Any]:
    if entry_type not in ("PREREG", "RESULT", "NOTE"):
        raise ValueError(entry_type)
    existing = read(path)
    if entry_type == "RESULT" and not any(e["type"] == "PREREG" and e["id"] == exp_id for e in existing):
        raise ValueError(f"RESULT for {exp_id} without a preceding PREREG")
    if entry_type == "PREREG" and any(e["type"] == "PREREG" and e["id"] == exp_id for e in existing):
        raise ValueError(f"{exp_id} already preregistered; a changed idea is a new id")
    prev = existing[-1]["entry_hash"] if existing else GENESIS
    body = {"seq": len(existing), "ts": (now or datetime.now(UTC)).strftime("%Y-%m-%dT%H:%M:%SZ"), "type": entry_type, "id": exp_id, "prev_hash": prev,
            "code_commit": git_commit(repo) if repo else "", **fields}
    body["entry_hash"] = _h(prev, {k: v for k, v in body.items()})
    with path.open("a") as fh:
        fh.write(json.dumps(body, sort_keys=True, default=str) + "\n")
    return body
