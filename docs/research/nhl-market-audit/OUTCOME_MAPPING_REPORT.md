# Outcome-mapping report

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

`market_audit/outcomes.py` is a pure function (`resolve(spec, facts)`), written independently of `nhl_edge.settlement`. It returns YES / NO, or an explicit non-decision:
`VOID_FAIR_PRICE`, `NOT_FINAL`, `DATA_INCONSISTENT`, `PLAYER_UNMATCHED`, `PLAYER_NOT_IN_BOXSCORE`, `RULE_SILENT`, `UNRESOLVED_SPEC`. It never guesses.

## Three independent checks

1. **Three-source reconciliation per game** (official final = play-by-play goals = boxscore lines, goalie scorers included): 151/151 games clean.
2. **Against production settlement**: 31,478 contracts decided by both, **0 disagreements**.
3. **Against Kalshi's own settlement (2025-26 history)**: 15,892 finalized winner / spread / total markets, **0 disagreements**, split by how the game ended:

| series | game ended | markets | agree | rate |
|---|---|---|---|---|
| KXNHLGAME | OT | 494 | 494 | 1.0 |
| KXNHLGAME | REG | 2218 | 2218 | 1.0 |
| KXNHLGAME | SO | 238 | 238 | 1.0 |
| KXNHLSPREAD | OT | 844 | 844 | 1.0 |
| KXNHLSPREAD | REG | 3838 | 3838 | 1.0 |
| KXNHLSPREAD | SO | 452 | 452 | 1.0 |
| KXNHLTOTAL | OT | 1277 | 1277 | 1.0 |
| KXNHLTOTAL | REG | 5861 | 5861 | 1.0 |
| KXNHLTOTAL | SO | 670 | 670 | 1.0 |

The shootout rows (the discriminating cases for the "shootout = one goal" rule on totals and spreads) agree 100%. The 11 `scalar` (fair-price) results are one postponed game; the resolver
correctly refuses to settle them (135 markets did not join to a final).

## Outcomes by family (live archive, all captured games)

| family | YES | NO | void | not on boxscore | rule silent | not final |
|---|---|---|---|---|---|---|
| first_goal | 149 | 4,918 | 1 | 275 | 33 | 74 |
| game_early_goal | 83 | 68 | 0 | 0 | 0 | 14 |
| game_overtime | 35 | 116 | 0 | 0 | 0 | 14 |
| game_spread | 189 | 974 | 0 | 0 | 0 | 64 |
| game_total | 789 | 731 | 0 | 0 | 0 | 144 |
| game_winner | 151 | 151 | 0 | 0 | 0 | 94 |
| goalie_saves | 176 | 214 | 1 | 0 | 0 | 0 |
| period_spread | 175 | 947 | 0 | 0 | 0 | 84 |
| period_total | 887 | 1,262 | 0 | 0 | 0 | 126 |
| period_winner | 453 | 906 | 0 | 0 | 0 | 126 |
| player_assists | 1,041 | 3,827 | 0 | 70 | 0 | 76 |
| player_goals | 872 | 7,229 | 1 | 280 | 0 | 128 |
| player_points | 1,664 | 4,551 | 0 | 93 | 0 | 86 |
| team_total | 640 | 870 | 0 | 0 | 0 | 140 |

`NOT_FINAL` rows are games not yet played at the snapshot. Player contracts for a player on neither club's boxscore are held out (the text does not say a scratch voids) and never scored.

Regression tests: `tests/test_market_audit_outcomes.py` (16 cases: shootout totals/spreads, overtime, P3 excludes OT, the 10:00 boundary, name matching, goalie scorer, scratch vs zero-TOI, first-goal rule gap, not-final).
