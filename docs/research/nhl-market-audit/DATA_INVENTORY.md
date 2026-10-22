# Historical data inventory

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

## What exists (verified, not assumed)

| item | exact count | note |
|---|---:|---|
| files on the `data-archive` branch | 16,769 | the "~18,000 indexed files" in the brief is not accurate for this branch snapshot |
| ledger (manifest-indexed) files | 14,214 | every one exists, none duplicated, every SHA-256 matches |
| files NOT in the ledger | 2,555 | derived outputs and pointers: .gitattributes: 1, LEASE_capture.json: 1, README.md: 1, STATUS_capture.json: 1, STATUS_context.json: 1, STATUS_evaluate.json: 1, STATUS_settle.json: 1, STATUS_simulate.json: 1, STATUS_worker.json: 1, app: 287, catalog: 2, eval: 10, manifest.jsonl: 1, slates: 2246 |
| Kalshi board ticks (market) | 2,870 | 128 full checkpoints + 2,742 hash-chained deltas |
| order-book ticks | 2,870 | 300 books per tick (sampled), 0 fetch errors |
| calendar span of captures | 2026-09-29 to 2026-10-21 | about 23 days of one season |
| scheduled games seen | 213 | |
| **independent games with an official final** | **151** | **the only unit that is an independent observation** |
| unique game-scoped contracts | 35,992 | all have a PROVEN semantic spec |
| contracts on final games | 34,822 | |
| contracts on final games with a usable pregame quote | 27,359 | two-sided, active, fully captured before scheduled start |
| contracts reliably settled (YES/NO) on final games | 34,068 | independent resolver, reconciled with production |
| settled AND with a usable pregame quote | 26,868 | the analysable set |
| usable pregame change-events | 1,504,374 | repeated snapshots of the same contracts, NOT independent |
| routed wagers in the accounting ledger | 34 | separate group, never mixed with research selections |

**Honest scale statement.** Thousands of captures and tens of thousands of contracts are 151 independent games. Every contract of a game shares one
outcome path, every snapshot of a contract shares one outcome, and a V1 prediction table of 475,882 rows is
3151.5 rows per game. All statistics in this audit resample whole games.

## Ledger kinds

| kind | files | rows | first day | last day |
|---|---|---|---|---|
| context/dailyfaceoff_raw | 400 | 400 | 2026-09-29 | 2026-10-21 |
| context/goalie_observations | 451 | 11,040 | 2026-09-29 | 2026-10-21 |
| context/goalie_stats | 400 | 357,706 | 2026-09-29 | 2026-10-21 |
| context/injuries | 400 | 48,517 | 2026-09-29 | 2026-10-21 |
| context/lines | 382 | 213,748 | 2026-09-30 | 2026-10-21 |
| context/rosters | 400 | 311,348 | 2026-09-29 | 2026-10-21 |
| context/schedule | 400 | 24,886 | 2026-09-29 | 2026-10-21 |
| context/sportsbook_odds | 216 | 14,130 | 2026-09-29 | 2026-10-21 |
| context/team_games | 399 | 1,168,098 | 2026-09-29 | 2026-10-21 |
| context/team_games_st | 23 | 269,904 | 2026-09-29 | 2026-10-21 |
| context/team_summary | 400 | 24,247 | 2026-09-29 | 2026-10-21 |
| contracts | 529 | 475,882 | 2026-09-29 | 2026-10-21 |
| evaluations | 80 | 456,082 | 2026-09-30 | 2026-10-21 |
| evaluations_player | 78 | 288,477 | 2026-10-01 | 2026-10-21 |
| kalshi/markets | 128 | 408,853 | 2026-09-29 | 2026-10-21 |
| kalshi/markets_delta | 2742 | 2,742 | 2026-09-29 | 2026-10-21 |
| kalshi/orderbooks | 128 | 38,400 | 2026-09-29 | 2026-10-21 |
| kalshi/orderbooks_delta | 2742 | 2,742 | 2026-09-29 | 2026-10-21 |
| player_events/coice | 151 | 32,664 | 2026-09-30 | 2026-10-21 |
| player_events/goalies | 151 | 604 | 2026-09-30 | 2026-10-21 |
| player_events/goals | 150 | 932 | 2026-09-30 | 2026-10-21 |
| player_events/players | 151 | 5,436 | 2026-09-30 | 2026-10-21 |
| player_events/shots | 151 | 17,363 | 2026-09-30 | 2026-10-21 |
| player_events/team_states | 151 | 302 | 2026-09-30 | 2026-10-21 |
| predictions | 529 | 475,882 | 2026-09-29 | 2026-10-21 |
| predictions_player | 366 | 300,401 | 2026-09-30 | 2026-10-21 |
| predictions_v2 | 523 | 470,594 | 2026-09-29 | 2026-10-21 |
| results | 81 | 151 | 2026-09-30 | 2026-10-21 |
| script_forecasts | 343 | 2,149 | 2026-10-07 | 2026-10-21 |
| script_postmortems | 54 | 2,123 | 2026-10-08 | 2026-10-21 |
| settlements | 81 | 33,324 | 2026-09-30 | 2026-10-21 |
| thesis_decisions | 474 | 22,929 | 2026-10-01 | 2026-10-21 |
| thesis_games | 484 | 3,083 | 2026-10-01 | 2026-10-21 |
| thesis_postmortems | 76 | 22,642 | 2026-10-02 | 2026-10-21 |


## A second dataset: 2025-26 history on `main`

`data/history/kalshi/` holds finalized KXNHLGAME / KXNHLTOTAL / KXNHLSPREAD markets and hourly/1-minute candle closes for the 2025-26 season. It is a
**different instrument of evidence**: best bid/ask at candle close, no depth, no model inputs of its own, no period/team-total/prop markets. It is used only as a
separate tier ("HIST") and is never pooled with the live archive. 15,892 of its settled markets were used to validate the outcome resolver.

## Season-level markets (separated from single-game markets)

1,571 of 2,377 markets on the last checkpoint board are season futures, awards or player-season statistics. They have different
horizons (months), settlement rules (e.g. the Ted Lindsay market pays $1/N on ties) and statistics, and are excluded from every game-level number here.

| family | support | markets |
|---|---|---|
| non_hockey_or_office | UNMODELABLE | 1 |
| season_awards | UNMODELABLE | 547 |
| season_champion | RESEARCH | 481 |
| season_player_stats | RESEARCH | 497 |
| season_unknown | UNRESOLVED | 45 |

Series on the board with no ontology entry ("unresolved"): the rules are quoted verbatim and **no mapping is invented**.

| series | markets | example | rules |
|---|---|---|---|
| KXNHLLINDSAY | 28 | Ted Lindsay Award: William Nylander wins | If William Nylander wins the NHL Ted Lindsay Award in the 2026-27 NHL season, then the market resolves to Yes. |
| KXNHLPSEASONGOALS | 17 | Macklin Celebrini: 60+ goals in 2026-27 NHL regular season? | If Macklin Celebrini scores at least 60 goals during the 2026-27 NHL regular season, then the market resolves to Yes. |


## What cannot be claimed

* Full historical coverage of Kalshi NHL. The live archive starts 2026-09-29; nothing before it exists on this branch.
* Kalshi's own settlement for live-archive contracts. The capture requests only live statuses, so `result` is empty on all 35,992 contracts;
  settlement truth is the NHL official final, validated separately against Kalshi's own results on the 2025-26 history.
* Depth for anything except winner / spread / total / team total (see CAPTURE_COVERAGE.md).
