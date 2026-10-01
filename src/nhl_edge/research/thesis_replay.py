"""Replay RUN NHL's thesis card at a past cutoff on a COPY of the archive, and optionally audit a proposed card.

    python -m nhl_edge.research.thesis_replay --archive <archive copy> --now 2026-09-30T23:20:00Z --date 2026-09-30 \
        --propose "KXNHLGAME-26SEP30NYITOR-NYI|yes:50:44" --out docs/research/thesis_sample

Point-in-time: ``nhl simulate`` itself only reads archive partitions observed at or before ``--now`` (and the repository
history / params, which end before the 2026-27 season's games). The replay WRITES slates / ledger rows into the archive
it is given, so always pass a copy, never the production checkout. Diagnostic only: a replayed card says nothing about
whether it would have won, and nothing here is tuned to make it look better.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import time
from pathlib import Path
from typing import Any

from nhl_edge.timeutil import parse_iso


def replay(archive: Path, data_root: Path, now_iso: str, date: str, proposals: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    from nhl_edge.archive.ledger import Ledger
    from nhl_edge.thesis.engine import analyze_game, audit_card
    from nhl_edge.thesis.reliability import reliability_table
    from nhl_edge.workflows import simulate, thesis_card

    captured: dict[str, Any] = {}
    orig = thesis_card.run_thesis_card

    def capture(dists, ledger, now, odds, run_id, cfg=None):
        captured.update(dists=dists, ledger=ledger, now=now, odds=odds)
        return orig(dists, ledger, now, odds, run_id, cfg)

    thesis_card.run_thesis_card = capture
    t0 = time.perf_counter()
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            rc = simulate.run_simulate(archive, data_root, date=date, now=parse_iso(now_iso))
    finally:
        thesis_card.run_thesis_card = orig
    out: dict[str, Any] = {"rc": rc, "seconds_total_simulate": round(time.perf_counter() - t0, 2), "now": now_iso}
    slates = sorted((archive / "slates" / f"dt={date}").glob(f"{parse_iso(now_iso).strftime('%Y%m%dT%H%M%SZ')}_*"))
    out["slate_dir"] = str(slates[-1]) if slates else None
    if proposals and captured.get("dists"):
        from nhl_edge.thesis.benchmark import consensus_moneyline
        from nhl_edge.workflows.thesis_card import _jsonable, portfolio_config

        cfg = portfolio_config()
        fams = sorted({b.family for d in captured["dists"] for b in d.bets})
        rel = reliability_table(Ledger(archive), captured["now"], fams)
        analyses = [analyze_game(d, rel, consensus_moneyline(captured["odds"] or [], d.game_id, d.home_team_id, d.away_team_id), cfg) for d in captured["dists"]]
        out["audit"] = _jsonable(audit_card(analyses, proposals, cfg, rel))
    return out


def parse_proposals(specs: list[str]) -> list[dict[str, Any]]:
    out = []
    for s in specs:
        bet, *rest = s.split(":")
        out.append({"bet_id": bet, "stake_dollars": float(rest[0]) if rest else 0.0, "price_cents": float(rest[1]) if len(rest) > 1 else None})
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--data", default="data")
    ap.add_argument("--now", required=True)
    ap.add_argument("--date", required=True)
    ap.add_argument("--propose", action="append", default=[], help="'<ticker>|<yes|no>:<stake dollars>:<price cents>' (repeatable)")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    res = replay(Path(a.archive), Path(a.data), a.now, a.date, parse_proposals(a.propose))
    if a.out:
        d = Path(a.out)
        d.mkdir(parents=True, exist_ok=True)
        (d / "replay.json").write_text(json.dumps(res, indent=1, default=str))
    print(json.dumps({k: v for k, v in res.items() if k != "audit"} | {"audit_verdict": (res.get("audit") or {}).get("verdict")}, indent=1, default=str))
    return 0 if res["rc"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
