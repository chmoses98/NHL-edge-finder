"""Command-line entry: ``nhl <command>``. Each command wraps a module function so the same code runs locally, in
tests and in GitHub Actions. RESEARCH_ONLY: there is no command that places, sizes or routes a wager."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from nhl_edge.log import get_logger

log = get_logger("nhl")


def cmd_discover(args: argparse.Namespace) -> int:
    from nhl_edge.config import settings
    from nhl_edge.kalshi.client import KalshiClient
    from nhl_edge.kalshi.discovery import discover, summary_markdown
    from nhl_edge.kalshi.ontology import Ontology

    onto = Ontology.load()
    client = KalshiClient(settings())
    statuses = tuple(args.statuses.split(",")) if args.statuses else ("unopened", "open", "closed", "settled")
    summary = discover(client, onto, raw_dir=Path(args.raw_dir) if args.raw_dir else None, statuses=statuses, max_pages_per_status=args.max_pages,
                       include_series=args.include.split(",") if args.include else None)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "discovery_summary.json").write_text(summary.to_json())
    (out / "discovery_summary.md").write_text(summary_markdown(summary))
    print(summary_markdown(summary))
    return 0


def cmd_capture(args: argparse.Namespace) -> int:
    from nhl_edge.archive.capture import run_capture
    from nhl_edge.archive.reconstruct import DEFAULT_CHECKPOINT_EVERY

    return run_capture(out_root=Path(args.out), statuses=args.statuses.split(","), with_orderbook=args.orderbook, max_orderbooks=args.max_orderbooks,
                       series_filter=args.series.split(",") if args.series else None, delta_encode=not args.full_snapshots,
                       checkpoint_every=args.checkpoint_every or DEFAULT_CHECKPOINT_EVERY)


def cmd_context(args: argparse.Namespace) -> int:
    from nhl_edge.data.context import run_context_refresh

    return run_context_refresh(out_root=Path(args.out), date_et=args.date, with_dfo=not args.no_dfo, with_injuries=not args.no_injuries, with_moneypuck=not args.no_moneypuck)


def cmd_simulate(args: argparse.Namespace) -> int:
    from nhl_edge.workflows.simulate import run_simulate

    return run_simulate(out_root=Path(args.out), data_root=Path(args.data), date=args.date, n_sims=args.sims, seed=args.seed)


def cmd_settle(args: argparse.Namespace) -> int:
    from nhl_edge.workflows.settle import run_settle

    return run_settle(out_root=Path(args.out), data_root=Path(args.data))


def cmd_evaluate(args: argparse.Namespace) -> int:
    from nhl_edge.workflows.evaluate import run_evaluate

    return run_evaluate(out_root=Path(args.out), data_root=Path(args.data))


def cmd_conductor(args: argparse.Namespace) -> int:
    from nhl_edge.workflows.conductor import run_conductor

    return run_conductor(Path(args.data), args.github_output)


def cmd_worker(args: argparse.Namespace) -> int:
    import os

    from nhl_edge.worker.run import Worker, dispatch_successor_via_api

    repo = os.environ.get("GITHUB_REPOSITORY", "")
    token = os.environ.get("GITHUB_TOKEN", "")
    ref = os.environ.get("GITHUB_REF_NAME", "main")
    worker_id = os.environ.get("GITHUB_RUN_ID") or f"local-{os.getpid()}"
    dispatch = None
    if repo and token and not args.no_successor:
        def dispatch(nonce: str) -> bool:
            return dispatch_successor_via_api(repo, ref, token, args.workflow, nonce)
    w = Worker(data_root=Path(args.data), archive_root=Path(args.out), worker_id=str(worker_id), successor_token=args.successor_token or None,
               dispatch_fn=dispatch, lifetime_minutes=args.lifetime_minutes)
    result = w.run()
    payload = result.to_json()
    print(payload)
    if args.report:
        # The workflow's report/enforcement steps read this; it carries final_push_ok, which STATUS_worker.json
        # (written before that push) cannot. Exit 0 for every classified outcome: the single enforcement step
        # turns a FAILED verdict red, so the archive-preservation step still runs first.
        Path(args.report).write_text(payload)
    return 0


def cmd_app_export(args: argparse.Namespace) -> int:
    """Publish the Edge Finder app documents (edge_finder.app.v1) from the archive. RESEARCH_ONLY throughout."""
    from nhl_edge.app_export import run_from_args

    return run_from_args(args)


def cmd_run(args: argparse.Namespace) -> int:
    """RUN NHL: context -> capture -> simulate for the target date, in one command."""
    from nhl_edge.archive.capture import run_capture
    from nhl_edge.data.context import run_context_refresh
    from nhl_edge.workflows.simulate import run_simulate

    out = Path(args.out)
    rc = run_context_refresh(out_root=out, date_et=args.date)
    if not args.skip_capture:
        try:
            run_capture(out_root=out, statuses=["open", "unopened"], with_orderbook=True, max_orderbooks=args.max_orderbooks)
        except Exception as e:  # noqa: BLE001 - a market outage must not stop the hockey-side snapshot
            log.error(f"capture failed: {e}")
    rc2 = run_simulate(out_root=out, data_root=Path(args.data), date=args.date, n_sims=args.sims)
    return rc or rc2


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="nhl", description="NHL Edge Finder (RESEARCH_ONLY)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("discover", help="enumerate the Kalshi NHL universe")
    p.add_argument("--out", default="data/catalog")
    p.add_argument("--raw-dir", default=None)
    p.add_argument("--statuses", default=None)
    p.add_argument("--max-pages", type=int, default=40)
    p.add_argument("--include", default=None)
    p.set_defaults(fn=cmd_discover)
    p = sub.add_parser("capture", help="snapshot Kalshi NHL markets (+order books) into the archive")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--statuses", default="open,unopened")
    p.add_argument("--orderbook", action="store_true")
    p.add_argument("--max-orderbooks", type=int, default=300)
    p.add_argument("--series", default=None)
    p.add_argument("--full-snapshots", action="store_true")
    p.add_argument("--checkpoint-every", type=int, default=None)
    p.set_defaults(fn=cmd_capture)
    p = sub.add_parser("context", help="snapshot schedule, team/goalie stats, rosters, goalie observations, injuries")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--date", default=None)
    p.add_argument("--no-dfo", action="store_true")
    p.add_argument("--no-injuries", action="store_true")
    p.add_argument("--no-moneypuck", action="store_true")
    p.set_defaults(fn=cmd_context)
    p = sub.add_parser("simulate", help="RUN NHL pricing: slate.json / slate.md / packet.json")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--data", default="data")
    p.add_argument("--date", default=None)
    p.add_argument("--sims", type=int, default=0)
    p.add_argument("--seed", type=int, default=None)
    p.set_defaults(fn=cmd_simulate)
    p = sub.add_parser("run", help="RUN NHL end to end: context + capture + simulate")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--data", default="data")
    p.add_argument("--date", default=None)
    p.add_argument("--sims", type=int, default=0)
    p.add_argument("--skip-capture", action="store_true")
    p.add_argument("--max-orderbooks", type=int, default=300)
    p.set_defaults(fn=cmd_run)
    p = sub.add_parser("settle", help="settle captured contracts against official final results")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--data", default="data")
    p.set_defaults(fn=cmd_settle)
    p = sub.add_parser("evaluate", help="calibration / Brier / CLV report")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--data", default="data")
    p.set_defaults(fn=cmd_evaluate)
    p = sub.add_parser("conductor", help="decide which jobs are due")
    p.add_argument("--data", default="data")
    p.add_argument("--github-output", default=None)
    p.set_defaults(fn=cmd_conductor)
    p = sub.add_parser("app-export", help="publish the Edge Finder app documents (app/latest) from the archive")
    from nhl_edge.app_export import add_arguments

    add_arguments(p)
    p.set_defaults(fn=cmd_app_export)
    p = sub.add_parser("worker", help="long-lived capture worker (GitHub Actions)")
    p.add_argument("--data", default="data")
    p.add_argument("--out", default="data/archive")
    p.add_argument("--workflow", default="capture_worker.yml")
    p.add_argument("--successor-token", default=None)
    p.add_argument("--lifetime-minutes", type=float, default=None)
    p.add_argument("--no-successor", action="store_true")
    p.add_argument("--report", default=None, help="write the final shift report (with health verdict) here")
    p.set_defaults(fn=cmd_worker)
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
