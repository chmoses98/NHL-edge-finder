# Data-quality audit

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

## Integrity (ledger)

| check | result |
|---|---|
| manifest entries / entries whose file exists and hashes correctly / duplicated paths | 14,214 / 14,214 / 0 |
| SHA-256 mismatches | 0 |
| market delta chains verified (ok / broken) | 128 / 0 |
| order-book delta chains verified (ok / broken) | 128 / 0 |

## Outcome integrity

| check | result |
|---|---|
| final games reconciled across official final, play-by-play goals and boxscore lines | 151 / 151 |
| contracts decided by BOTH my resolver and production settlement | 31,478 |
| **disagreements** between them | **0** |
| decided by my resolver, not by production | 2,590 |
| decided by production, not by my resolver | 0 |
| resolver vs Kalshi's own settlement, 2025-26 history (15,892 markets incl. shootout games) | 0 disagreements |

Why production leaves ~2,600 contracts unsettled that the resolver decides: overtime and first-10-minutes markets are labelled "semantics not proven" by production (their
contract text is unambiguous and is parsed here), and alternate-line ladders that did not exist at production's settlement candidate cut have no settlement record at all.

## Findings register

| # | finding | evidence | consequence | status |
|---|---|---|---|---|
| F1 | Kalshi `result` is never captured for live contracts | no non-empty `result` in any archived quote event; the capture requests only `open/active` statuses | settlement relies on NHL finals; validated against Kalshi's own results on 2025-26 history | documented; recommend a periodic `finalized` capture (research PR, not applied) |
| F2 | Tick stamp is the capture START | written-at minus observed-at: ~33 s markets, ~94 s books | a quote stamped before puck drop can finish after it | handled: point-in-time uses stamp + lag; 9 games' last market tick and 37 games' last book tick would have leaked under a stamp-only filter |
| F3 | Order books exist for 4 of 14 families only | table below | no executability evidence for props/periods | documented |
| F4 | Registry lacks Kalshi display names "New York I", "New York R", "Utah" | `resolve_name()` returns None; production survives via ticker-tricode fallback | silent dependence on a fallback; fragile to a new alias | verified 1:1 with ticker codes on all 32 clubs; local alias layer; recommend adding aliases to `teams.csv` |
| F5 | Goalie goals break skater-only goal reconciliation | game 2026020010: Shesterkin empty-net goal | a skater-only check flags a clean game | fixed in the resolver (goalie scorers counted); production unaffected |
| F6 | Player contracts for players NOT on the boxscore | 279 distinct (game, player) pairs absent from both clubs' boxscores | the contract text voids only a player "active but never enters"; a scratch is not addressed | held out of all return statistics, never scored; counted separately |
| F7 | One-sided boards for long-tail props | table Q1 below | no executable price on one side | quotes with a missing side are treated as missing, never filled from an older state |
| F8 | Capture family classification vs independent taxonomy | 0 mismatches of 35,992 | none | clean |
| F9 | Production prediction inputs vs archived board | bid match 100.0%, ask match 100.0% on 15,553 sampled rows | none | clean: no look-ahead or board mismatch in the frozen V1 inputs |
| F10 | Prediction repeated evidence | 475,882 V1 rows over 151 games (3151.5 per game; ~5 decision runs per game) | row counts overstate evidence by ~3 orders of magnitude | all inference clusters by game |
| F11 | Tip-time schedule | no scheduled start moved for any archived game | none | clean |
| F12 | Unresolved season series | see DATA_INVENTORY.md | outside game scope | documented, no mapping invented |
| F13 | The routed ledger carries no provenance and cannot distinguish a manual bet from a model-driven one | `kalshi-bet-router` `routed_ledger.py:47-58, 111` actively REFUSES recommendation / model / thesis fields; `entry_method` is the constant `IMPORTED_RECEIPT` | "independent handicapping" vs "model recommendation" cannot be separated for real wagers; only "a thesis-card decision exists / does not exist" is available as a proxy | documented; scorecard marks the group NOT_MEASURABLE |
| F14 | Cash-outs and hedges are recorded as purchases of the contract traded | `production.py:575-590` (`EXPOSURE_SIDE_DESTINATIONS` is empty; documented NFL cash-out evidence) | a late-placed row (e.g. a 0.99 YES placed 67 min after puck drop, a NO placed after the final) may be an exit, not new risk; the ledger cannot say | flagged in the wager audit; all 34 rows are analysed as recorded |
| F15 | Router docs contradict router code on NHL auto-merge | `destinations.py:466` `auto_merge=True`; `docs/DESTINATIONS.md:247, 286-292` still say False; `docs/EDGE_FINDER_APP_CONTRACT.md:161` says the NHL ledger is empty | none for this audit (ledger content verified directly); stale documentation | reported to the owner, not edited here |

### Q1. Quote completeness at the last pregame tick

| family | contracts | two-sided % | no bid % | median spread (c) |
|---|---|---|---|---|
| first_goal | 5376 | 8.5 | 91.5 | 1.0 |
| game_early_goal | 151 | 100.0 | 0.0 | 2.0 |
| game_overtime | 151 | 100.0 | 0.0 | 1.0 |
| game_spread | 604 | 100.0 | 0.0 | 1.0 |
| game_total | 1359 | 98.5 | 0.0 | 1.0 |
| game_winner | 302 | 100.0 | 0.0 | 1.0 |
| goalie_saves | 348 | 72.7 | 27.3 | 4.0 |
| period_spread | 906 | 100.0 | 0.0 | 3.0 |
| period_total | 1359 | 100.0 | 0.0 | 3.0 |
| period_winner | 1359 | 100.0 | 0.0 | 3.0 |
| player_assists | 4754 | 93.5 | 6.5 | 3.0 |
| player_goals | 8327 | 69.1 | 30.9 | 1.0 |
| player_points | 6212 | 90.4 | 9.6 | 3.0 |
| team_total | 1510 | 100.0 | 0.0 | 1.0 |

### Q3. Order-book sampling by family

| family | contracts | with any book | % |
|---|---|---|---|
| first_goal | 5376 | 0 | 0.0 |
| game_early_goal | 151 | 0 | 0.0 |
| game_overtime | 151 | 0 | 0.0 |
| game_spread | 1163 | 1163 | 100.0 |
| game_total | 1520 | 1512 | 99.5 |
| game_winner | 302 | 302 | 100.0 |
| goalie_saves | 391 | 0 | 0.0 |
| period_spread | 1122 | 0 | 0.0 |
| period_total | 2149 | 0 | 0.0 |
| period_winner | 1359 | 0 | 0.0 |
| player_assists | 4938 | 0 | 0.0 |
| player_goals | 8382 | 0 | 0.0 |
| player_points | 6308 | 0 | 0.0 |
| team_total | 1510 | 1510 | 100.0 |

### Q4. Board vs book at the same tick

{
 "n_event_pairs_compared": 467434,
 "bid_exact_pct": 90.69,
 "ask_exact_pct": 91.31,
 "bid_abs_diff_cents_p50_p90_p99": [
  0.0,
  0.0,
  10.0
 ],
 "note": "pairs exist only where BOTH the board row and the book row changed at that tick, so this OVERSTATES disagreement; quiet-market agreement is not observable from a change log."
}

### Q2. Tip-straddle contamination

stamp = capture START; fully written ~45s (markets) / ~105s (books) later. Point-in-time logic uses stamp+lag, so these ticks are EXCLUDED from pregame use; a naive stamp-only filter would have admitted them.
