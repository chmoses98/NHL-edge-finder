# HANDOFF: NHL Edge Finder overnight foundation build (2026-09-28/29)

## A. Executive verdict

**READY FOR PROSPECTIVE COLLECTION.**

`main` carries a tested NHL research platform. The self-renewing capture worker is running on `main` and writing
point-in-time snapshots to the `data-archive` branch ahead of opening night (first puck drop 2026-09-29 21:00 UTC).
The context snapshot (schedule, team xG game log, goalie stats, starting-goalie observations, rosters, injuries)
landed at 12:27 UTC with zero source errors; the market capture, RUN NHL simulation and discovery jobs follow on the
worker's cadence (see section L for the verified production runs). Every model family is RESEARCH_ONLY.

Why not "fully proven": the first prospective evaluation rows only exist after tonight's games settle, the
walk-forward shows measured weaknesses (OT under-prediction), and the worker chain's multi-day continuity is
proven on the NBA repository, not yet on this one.

## B. Start / end SHAs

| repo | start | end |
|---|---|---|
| chmoses98/NHL-edge-finder `main` | `30463e739f34bad8b90d9469e84a99ab891dabb6` (empty README) | `a3b439023849bd70fe78febe2ca9ffa1842bf2cc` (PR #1 merge) + the handoff PR |
| chmoses98/NHL-edge-finder `data-archive` | (did not exist) | growing; first commits `937f646` (init), `3474ff4` (first context snapshot) |
| nba-edge-finder, nfl-edge-finder, edge-finder-api, kalshi-bet-router | read only, untouched | untouched |

## C. PRs

| # | title | status |
|---|---|---|
| 1 | NHL Edge Finder foundation: RESEARCH_ONLY simulation, Kalshi pricing and prospective capture | merged (CI green, 300 tests) |
| 2 | Handoff document | see PR list |

## D. What was built

`src/nhl_edge/` (see `docs/ARCHITECTURE.md`): canonical identity; NHL API / stats / MoneyPuck / DailyFaceoff / ESPN
readers; append-only ledger with delta-encoded Kalshi boards; point-in-time context snapshots; goalie status as
first-class observations; DATA_ONLY_V1 ratings; coherent Monte Carlo simulator (`nhl-sim-1.1`); Kalshi discovery
(no caps), ontology (YAML), contract semantics with OT/SO settlement basis, executable-ask economics with the
quadratic fee estimate; RUN NHL slate/packet; deterministic idempotent settlement; evaluation (Brier, log loss,
ECE, CLV); informational authority eligibility; stdlib-only conductor; self-renewing capture worker; historical
dataset + walk-forward. Workflows: `ci`, `probe`, `history`, `rehearsal`, `conductor`, `capture_worker`.

## E. Data sources (all verified from GitHub runners; the build container itself reached none of them)

| source | status | supplies | role | limitations |
|---|---|---|---|---|
| api-web.nhle.com | working | schedule (5 games 2026-09-29), scores, boxscore (final, REG/OT/SO, goalie starter flag), rosters | production | schedule feed embeds sportsbook odds (quarantined) |
| api.nhle.com/stats/rest | working | team + goalie season summaries, official game list with period (OT/SO) | production | new season empty until games exist |
| MoneyPuck | working | team game-by-game xG since 2008, goalie xG vs goals | production (ratings), history | teams.csv for 2026 404s until games exist; all_teams.csv ~40 MB per fetch (cached 1h) |
| Kalshi (api.elections + external-api) | working | 75 NHL series, 3,355 markets (2,529 active), order books | production | short tricodes; big series list |
| DailyFaceoff | working | starting goalies with Confirmed/Likely/Unconfirmed and news timestamps | optional enrichment | HTML `__NEXT_DATA__` (shape may drift; raw page archived) |
| ESPN injuries | working | injury list | optional enrichment | shown in packet, not modelled |
| MoneyPuck shots (peter-tanner host), ESPN scoreboard, Rotowire | reachable | | research / fallback | not ingested |

## F. Historical data (`data/history`, 6.4 MB Parquet, `MANIFEST.json`)

MoneyPuck team-game rows 2022, 2023, 2024, 2025 (NHL 2022-23 .. 2025-26): 11,200 / 11,200 / 11,184 / 11,200 rows
(4 situations), 1,400 / 1,400 / 1,398 / 1,400 games, 32 teams each, 0 unresolved abbreviations. NHL official results:
1,417 rows per season (1,312 regular + ~105 playoff), REG/OT/SO labelled (2022-23: 1,074 / 231 / 95). No shots,
skater or line data ingested. No errors.

## G. Kalshi discovery (live, 2026-09-29 12:17 UTC, run 36567059802)

14,468 series scanned; 75 NHL series; 3,355 markets across all statuses; 2,529 active captured in the rehearsal.
Families: game_winner (KXNHLGAME), game_spread (KXNHLSPREAD), game_total (KXNHLTOTAL), team_total (KXNHLTEAMTOTAL)
SUPPORTED (MODELABLE); game_overtime (KXNHLOT) PARTIAL; period winner/spread/total, first goal, early goal, player
goals/assists/points/saves, playoff series, season points/goals, futures (Stanley Cup, conferences, divisions,
Presidents', win streaks) and awards RESEARCH/UNMODELABLE. Every live series maps to a family (test enforced);
1,452 season-scope contracts are recorded but not joined to any game by design.

## H. Opening-night slate (2026-09-29, from the live rehearsal at T-6h..T-12h)

| game | start UTC | goalies (home / away) at 12:20 UTC | simulation | Kalshi contracts joined | snapshot |
|---|---|---|---|---|---|
| FLA @ CAR (2026020001) | 21:00 | PROJECTED Bussi / PROJECTED Markstrom | done, 20k draws, ladders clean | 249 (25 supported, 224 research/unsupported) | archived |
| MTL @ TOR (2026020002) | 23:00 | PROJECTED Bobrovsky / PROJECTED Dobes | done | 195 (25 / 170) | archived |
| NYR @ BOS (2026020003) | 00:00 | PROJECTED Swayman / PROJECTED Shesterkin | done | 204 (25 / 179) | archived |
| VAN @ EDM (2026020004) | 02:00 | CONFIRMED Jarry / PROJECTED Lankinen | done | 51 (25 / 26) | archived |
| CHI @ VGK (2026020005) | 02:30 | PROJECTED Hart / PROJECTED Knight | done | 51 (25 / 26) | archived |

## I. Model V1

Inputs: MoneyPuck all-situation xG for/against per game (EW half-life 20, 20-game prior, previous season x0.6),
regressed finishing and team stopping, goalie factor (regressed GA/xGA, confidence-weighted mixture over plausible
starters; UNKNOWN = league average), home ice x1.045, back-to-back adjustments. Simulation: 57-minute Poisson
window, 3-minute goalie-pull window (leader x4.0, trailer x1.8, normalised so E[goals] is preserved), OT (66% decided
before a shootout), OT/SO winner from a shrunk strength ratio, winner credited +1 goal. Goalie handling: status
ladder with 0.985 / 0.85 / 0.70 / 0 confidences. Known crude assumptions in `docs/SIMULATION.md`.

## J. Historical evaluation (walk-forward, regular season 2024-25 and 2025-26, n = 2,624; `docs/research/WALK_FORWARD_V1.md`)

Moneyline: DATA_ONLY_V1 Brier 0.2420 / log loss 0.6768 / ECE 0.026 vs league-Poisson 0.2483 / 0.6897 and
constant-home 0.2483 / 0.6898. Overtime: model P(OT) 0.168 vs observed 0.2275 (Brier 0.1792, essentially tied with
the baseline): the Poisson tie deficit. Totals: over 5.5 / 6.5 Brier 0.2496 / 0.2498 (baseline 0.2501 / 0.2503);
expected total 6.51 vs actual 6.17 (+0.35 bias, structurally corrected in sim 1.1 by normalising the pull window;
not re-run tonight). No market benchmark exists for these games (no historical Kalshi NHL prices ingested), so no
model-vs-market claim is made. Goalie factor was 1.0 throughout. This is historical, not prospective.

## K. Authority

**ALL NHL MODEL FAMILIES REMAIN RESEARCH_ONLY. NO BETTING AUTHORITY WAS CREATED. NO BETS WERE PLACED.** The router
has NHL out of scope and this repository ships no importer, ledger branch or payload handling.

## L. Automation (see the end of this section for the verified production runs)

- `capture_worker.yml`: `*/5` cron bootstrap + self-dispatch; ~300-minute lifetime; cadence 15/10/7/5 min by
  time to start; runs context / simulate / settle / evaluate / discover when the conductor says they are due; pushes
  to `data-archive` after every cycle.
- `conductor.yml`: manual (`force=` list) or `.trigger/conductor` push; shares the concurrency group.
- `ci.yml` on push/PR; `probe.yml`, `history.yml`, `rehearsal.yml` manual or trigger-file.
- What happens next automatically: the worker captures every 15 min until T-6h, then 10 / 7 / 5 min; simulates
  every 45+ min and after each context refresh (every 55 min near games); settles ~3h after each start; evaluates
  after settlement; discovers daily; hands over to a successor every ~5h; the `*/5` cron restarts a dead chain.

### Verified production runs on `main` (2026-09-29 UTC)

| run | workflow | result |
|---|---|---|
| 36568131132 | ci (merge commit) | success |
| 36568139041 | conductor (forced) | cancelled by design: the worker took the shared concurrency group first and ran the same jobs |
| 36568142839 | capture_worker gen 1 | in progress (planned exit 17:27 UTC); successor 36568193942 queued in the pending slot |
| 36567059802 | rehearsal (branch) | success: full pipeline against live sources |
| 36567064829 | history-pull (branch) | success: dataset + walk-forward |

Archive evidence (`data-archive`, commits `1ebf50f`, `3474ff4`, `08ce532`):
1. NHL schedule fetch: `STATUS_context.json` n_games 55, five games today, errors [] .
2. NHL context: team summary, goalie summary (98 goalies), rosters, ESPN injuries, DailyFaceoff 16 observations, all archived.
3. MoneyPuck: `context/team_games` snapshot (2,788 rows, 0 unresolved teams), goalies 2025 (490 rows).
4. Kalshi discovery: 75 NHL series / 3,355 markets (rehearsal); the worker re-scans series on every capture.
5. Market capture: `kalshi/markets` 2,529 active markets + 300 order books at 12:42:10 UTC, coverage alarms [] .
6. Identity: every game and contract resolved to official team ids (750 contracts joined by date + team set).
7. Simulation: five games, 20,000 draws each, `nhl-sim-1.1`, ladder violations [] on every game.
8. Slate: `slates/dt=2026-09-29/20260929T124343Z_36568142839/{slate.json,slate.md,packet.json}` + `slates/latest/`.
9. Archive persists: `manifest.jsonl` 13 entries with sha256, `Ledger.verify()` clean before each push.
10. Idempotency: the rehearsal ran simulate twice (second instant appended, archive verified); every worker cycle appends.
11. Automation continues: successor queued, `*/5` bootstrap cron enabled on `main`, lease heartbeat every cycle.

First production slate (12:43 UTC, T-6h): FLA @ CAR P(home) 0.651 (market mid 0.535), MTL @ TOR 0.462, NYR @ BOS 0.530,
VAN @ EDM 0.645, CHI @ VGK 0.626; gates OK 76 / NO_EDGE 49 / UNSUPPORTED 625 (player props and periods, preserved).
Settlement and evaluation have not yet had a final game to act on; they are exercised by tests and the rehearsal
(0 candidates) and run automatically ~3h after each start.

## M. Testing

`ruff check src tests scripts`: clean. `pytest -q -n auto`: **300 passed** (identity incl. Utah history and alias
codes; contracts on real Kalshi payloads; simulator invariants incl. a hypothesis property test over strengths and
seeds; goalie point-in-time discipline; 30 settlement tests over REG/OT/SO/postponed/canceled/idempotency; conductor
decisions and stdlib-only import chain; worker lease races and rollover; delta archive reconstruction; ledger
immutability; fees and economics; workflow YAML/bash/heredoc validity; end-to-end slate on a fixture archive built
from real samples incl. a later goalie confirmation that must stay invisible; history parsers; walk-forward cutoff).

## N. Risks / known limitations

1. Worker-chain continuity on this repository is unproven beyond the first handover; the `*/5` cron bootstrap is
   the safety net and GitHub cron delivery is unreliable. Check the Actions tab tomorrow morning.
2. Model: OT under-predicted (~17% vs ~23%); special teams folded into all-situation rates; goalie factor from
   season aggregates; injuries and lines not modelled; sim 1.1's totals correction is unvalidated on history.
3. Start-of-season ratings are last season regressed; early slates lean on the prior (the FLA @ CAR 65% home
   probability vs a 53% market is the model's prior opinion, not evidence).
4. Kalshi rule text for regulation-winner, win-margin and overtime families has not been reviewed on live markets
   (none observed yet); they stay BUILDABLE/NEEDS_RULE_REVIEW.
5. DailyFaceoff HTML may drift; the raw page is archived every refresh so observations can be re-parsed.
6. Archive growth: each context refresh writes ~0.9 MB (team game log); ~20 MB/day in season. Compaction is a
   follow-up.
7. Order books are sampled by priority (cap 300 per capture) as a documented note, not an alarm.
8. Series list pagination (14k series) makes discovery ~70 s; fine daily.

## O. Owner action required

**NONE** for prospective collection. Optional: glance at Actions to confirm the worker chain is alive tomorrow.

## P. Tomorrow's run command

RUN NHL, opening night: GitHub Actions -> `conductor` -> Run workflow (branch `main`) -> `force: context,capture,simulate`.
Output: `data-archive` branch -> `slates/latest/slate.md` and `packet.json`. Locally:
`nhl run --out data/archive --data data --date 2026-09-29` on a checkout of `data-archive` at `data/archive`.

## Q. Next research priorities (evidence-ranked)

1. Ingest historical Kalshi NHL settled markets/candles (2025-26 exists on the exchange) to benchmark the market on
   the same games as the walk-forward.
2. Tie/OT calibration: score effects or a Dixon-Coles style correction, judged on P(OT) Brier/ECE walk-forward.
3. Goalie true talent and workload from goalie game logs; measure DailyFaceoff status confidences against boxscore
   starters from the prospective archive.
4. Explicit special teams from MoneyPuck 5on4/4on5 situation rows.
5. Empty-net multipliers estimated from play-by-play (landing feed), then period-level simulation for period markets.
