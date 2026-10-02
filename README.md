# NHL-edge-finder

**CURRENT AUTHORITY: RESEARCH_ONLY.** Every model family in this repository (`DATA_ONLY_V1`, `MARKET_ANCHORED_V1`) is a
research instrument, as are the SHADOW arms `DATA_ONLY_V2` (2026-09-29) and `PLAYER_SIM_V1` / `MARKET_ANCHORED_PLAYER_V1`
(2026-09-30, player goals / assists / points / saves / first goal), and the thesis / portfolio card layer (2026-10-01; its stakes are
research suggestions for a nominal bankroll). Nothing here places or routes a wager, and the Kalshi bet router has NHL
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
every Kalshi contract with executable prices and both edges, authority) for a downstream thesis builder, plus
`v2_shadow` and `player_shadow` (every Kalshi player contract with PLAYER_SIM_V1 and market-anchored probabilities,
executable asks, fee-adjusted edges, expected TOI / PP TOI / shots / goals / assists / points, projection quality,
role confidence, uncertainty flags; per-net goalie saves distributions; per-game contract correlation matrix), plus
`thesis_card` (RESEARCH_ONLY): game-script distribution, thesis events, every contract mapped to the scripts it wins in,
best expression per thesis, same-game joint outcome matrix, portfolio A/B/C on the simulated P/L, and the card that passed
the 18-field completion gate (`card.md` next to `slate.md`), with each bet's expression fidelity and its research status
(FUNDED_RESEARCH / SHADOW_ONLY / REJECTED) and whole-dollar research stake ($250 research bankroll, $5 max; research
governance, never placed). See `docs/research/THESIS_ENGINE.md` (section 16 for the 2026-10-02 repair pass).

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
python -m nhl_edge.data.player_history --out data/history --seasons 2024,2025      # official player events (network)
python -m nhl_edge.players.fit --history data/history                             # data/params/player-sim-1.0.json
python -m nhl_edge.research.player_walk_forward --mode simulate --seasons 2024,2025 # PLAYER_SIM_V1 walk-forward
python -m nhl_edge.research.thesis_replay --archive <ARCHIVE COPY> --now <cutoff> --date <ET date> \
       --propose "<ticker>|yes:<stake>:<price cents>" --model-audit --out <dir>                # replay the thesis card / audit a proposed card
python -m nhl_edge.research.rules_replay --archive <ARCHIVE COPY> --date <ET date> --work <scratch> \
       --old-src <old checkout>/src --out <dir>                                               # DIAGNOSTIC old-vs-new-rules replay at the final production cutoffs
```
No credentials are needed for anything in this repository.

## Docs
- `docs/HANDOFF_REPAIR_PASS.md` thesis-card repair pass (2026-10-02): snapshot-unique postmortem, settlement completeness, expression fidelity, research governance / staking, replays
- `docs/research/PREREGISTERED_HYPOTHESES.md` model-defect leads registered with their tests BEFORE the evidence exists
- `docs/HANDOFF_THESIS.md` thesis / portfolio card handoff (2026-10-01): verdict, PRs, architecture, sample, limits
- `docs/research/THESIS_ENGINE.md` game scripts, thesis mapping, expressions, joint matrix, portfolio, completion gate, model audit
- `docs/CROSS_SPORT_THESIS.md` the portable card-construction abstraction for other sports
- `docs/ACCOUNTING.md` routed-wager ACCOUNTING ledger (manually placed Kalshi bets, via kalshi-bet-router; `accounting-data` branch; no model involvement)
- `docs/HANDOFF_ROUTER.md` NHL router handoff (2026-09-29): verdict, production runs, owner action
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
- `docs/research/PLAYER_SIM_V1.md` player/event simulation: architecture, data, walk-forward evidence, calibration, limits
- `docs/HANDOFF_PLAYER_SIM.md` PLAYER_SIM_V1 overnight build handoff (A-Z)
