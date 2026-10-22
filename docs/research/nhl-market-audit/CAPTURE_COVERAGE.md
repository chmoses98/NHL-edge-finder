# Capture coverage

> RESEARCH ONLY. No wager was placed, no stake/cap/model/production contract changed. Snapshot of archive manifest `385fda9c45633413`.

## Cadence

* 2,870 ticks from 2026-09-29T12:42:10+00:00 to 2026-10-21T15:51:18+00:00.
* Gap between ticks (minutes): p10 5.0, median 10.0, p90 15.0, p99 20.1, max 55.4;
  2 gaps over 30 min, 0 over 60 min.
* Timing semantics (important): a tick is stamped with the capture **start**. The market board is fully written ~30-40 s later and the order books ~91-100 s later (manifest
  `written_at_utc - observed_at_utc`). Point-in-time logic uses `stamp + 45 s` (markets) and `stamp + 105 s` (books) as the instant a quote became knowable.

## Per final game (151 games)

| measure | value |
|---|---|
| games with at least one usable pregame quote | 151 |
| last pregame tick, minutes before scheduled start (p10 / p50 / p90 / max) | 1.1 / 3.4 / 5.0 / 16.7 |
| pregame ticks within the last 60 min (min / median / max) | 6 / 10 / 13 |
| markets first listed, hours before start (p10 / p50 / p90) | 61.3 / 165.9 / 167.1 |

## Coverage by market family (final games only)

| family | scope | contracts | with usable pregame quote | settled YES/NO | void / unscored | settled with pregame quote | order-book sampled |
|---|---|---|---|---|---|---|---|
| first_goal | player | 5376 | 563 | 5067 | 309 | 505 | 0.0% |
| game_early_goal | game | 151 | 151 | 151 | 0 | 151 | 0.0% |
| game_overtime | game | 151 | 151 | 151 | 0 | 151 | 0.0% |
| game_spread | game | 1163 | 604 | 1163 | 0 | 604 | 100.0% |
| game_total | game | 1520 | 1359 | 1520 | 0 | 1359 | 99.5% |
| game_winner | game | 302 | 302 | 302 | 0 | 302 | 100.0% |
| goalie_saves | player | 391 | 255 | 390 | 1 | 254 | 0.0% |
| period_spread | game | 1122 | 906 | 1122 | 0 | 906 | 0.0% |
| period_total | game | 2149 | 1359 | 2149 | 0 | 1359 | 0.0% |
| period_winner | game | 1359 | 1359 | 1359 | 0 | 1359 | 0.0% |
| player_assists | player | 4938 | 4717 | 4868 | 70 | 4647 | 0.0% |
| player_goals | player | 8382 | 7977 | 8101 | 281 | 7706 | 0.0% |
| player_points | player | 6308 | 6146 | 6215 | 93 | 6055 | 0.0% |
| team_total | game | 1510 | 1510 | 1510 | 0 | 1510 | 100.0% |


## Order-book depth is sampled, and only for four families

3,775 of 27,359 usable contracts (13.8%) ever received a pregame book. The cause is the capture rule, not an outage:
`snapshot_orderbooks()` ranks live markets by (support rank, has-quote, earliest expiry) and takes 300 per tick. Only winner / spread / total / team total are `MODELABLE`, so they
fill the 300 slots and **period markets, overtime, first-10-minutes, goalie saves, assists, points, goals and first-goal never have depth**. Executability can therefore be
measured for four families only; everything else is reported as quote-only (DEPTH-UNOBSERVED).

## Not claimed

Every number above is for the 151 games that finished by the snapshot. 62 scheduled games are not final and are excluded.
