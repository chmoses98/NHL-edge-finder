# NHL-edge-finder

**CURRENT AUTHORITY: RESEARCH_ONLY.** Every model family in this repository (`DATA_ONLY_V1`, `MARKET_ANCHORED_V1`) is a
research instrument, as is the SHADOW arm `DATA_ONLY_V2` (2026-09-29). Nothing here places, sizes, recommends or routes a wager, and the Kalshi bet router has NHL
explicitly out of scope. Promotion to any wagering authority requires prospective evidence and a separate explicit
decision (see `docs/AUTHORITY.md`).

NHL Kalshi market research workstation, built on the same infrastructure philosophy as `nba-edge-finder` and
`nfl-edge-finder` but with hockey-specific modelling:

```
data/context (schedule, team xG rates, goalie stats, starting-goalie observations, injuries)
  -> team / goalie state (point-in-time ratings, goalie status UNKNOWN/PROJECTED/PROBABLE/CONFIRMED)
  -> game environment (expected goals per side, home ice, rest, goalie mixture)
  -> coherent Monte Carlo game simulation (regulation + empty-net window + OT + shootout)
  -> Kalshi contract probabilities (winner, puck line, totals, team totals, ... from ONE joint draw)
  -> executable prices + fees (asks, not midpoints; quadratic Kalshi fee estimate)
  -> edge before / after fee (reported, never recommended)
  -> immutable append-only archive (data-archive branch)
  -> settlement (official NHL final, regulation vs OT/SO semantics)
  -> calibration, Brier, log loss, CLV
  -> future authority (explicit decision, prospective evidence only)
```

Season context: the 2026-27 regular season opens 2026-09-29 (five games). The system is schedule-driven; it reads
the official NHL feed and never hard-codes a slate.

## What runs automatically (GitHub Actions)

| workflow | trigger | what |
|---|---|---|
| `capture_worker.yml` | `*/5` cron bootstrap + self-dispatch | the cadence owner: one ~5h worker captures Kalshi markets/order books on a horizon-aware cadence (15/10/7/5 min), runs the conductor's due jobs (context, simulate, settle, evaluate, discover), pushes to `data-archive`, hands over to a successor |
| `conductor.yml` | manual dispatch (`force=` list) or `.trigger/conductor` push | one-shot decide-and-run; the "RUN NHL now" button and the recovery path |
| `ci.yml` | push / PR | ruff + pytest + CLI smoke |
| `probe.yml` | manual / `.trigger/probe` | source reachability + raw shape samples into `docs/probe/` |
| `history.yml` | manual / `.trigger/history` | MoneyPuck + NHL historical pull to Parquet, walk-forward evaluation |
| `rehearsal.yml` | manual / `.trigger/rehearsal` | full pipeline on a runner WITHOUT touching `data-archive`; summaries into `docs/rehearsal/` |

Schedules and `workflow_dispatch` only work on the default branch. Data lives on the `data-archive` branch (orphan,
append-only, `manifest.jsonl` with sha256 per file); code branches never accumulate snapshots.

## RUN NHL

```
nhl run --out data/archive --data data            # context + capture + simulate for today (ET)
nhl simulate --out data/archive --data data       # pricing only, from the latest archived snapshots
```
Outputs: `data/archive/slates/dt=YYYY-MM-DD/<ts>_<run>/{slate.json,slate.md,packet.json}` plus `slates/latest/`.
`packet.json` carries one comprehensive block per game (identity, context, goaltending, team state, model,
every Kalshi contract with executable prices and both edges, authority) for a downstream thesis builder.

On GitHub: Actions -> conductor -> Run workflow -> `force: context,capture,simulate`.

## Local use

```
python -m venv .venv && . .venv/bin/activate && pip install -e ".[dev]"
pytest -q -n auto                       # ~300 tests, no network
nhl discover --out data/catalog         # Kalshi NHL universe (network)
nhl context  --out data/archive         # schedule / stats / goalies / injuries snapshot
nhl capture  --out data/archive --orderbook
nhl simulate --out data/archive --data data --date 2026-09-29
nhl settle   --out data/archive --data data
nhl evaluate --out data/archive --data data
python -m nhl_edge.data.history --out data/history --seasons 2022,2023,2024,2025
python -m nhl_edge.research.walk_forward --history data/history --out docs/research
```
No credentials are needed for anything in this repository.

## Docs
- `docs/HANDOFF.md` overnight build handoff: verdict, SHAs, PRs, evidence, risks, next steps
- `docs/ARCHITECTURE.md` modules, data flow, storage, scheduling
- `docs/NHL_DATA_SOURCE_AUDIT.md` every source probed from a runner, with shapes and failure modes
- `docs/SIMULATION.md` exactly what the simulator does and what is crude
- `docs/KALSHI_MARKET_MAP.md` every discovered NHL market family and its support state
- `docs/POINT_IN_TIME.md` the cutoff discipline
- `docs/AUTHORITY.md` the authority ladder and why everything is RESEARCH_ONLY
- `docs/OPERATIONS.md` day-one checklist and runbook
- `docs/research/RESEARCH_NOTES.md` findings, negative results, roadmap
- `docs/research/V2_RESEARCH.md` DATA_ONLY_V2 shadow arm (sim 2.0, special teams, goalie true talent): evidence and limits
- `docs/research/MARKET_BENCHMARK.md` historical Kalshi benchmark (V1 vs V2 vs market)
