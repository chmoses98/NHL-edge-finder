# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-09-30T23:43:52Z · rows 900 · pregame 900 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 900 | 0.1957 | 0.6062 | 0.2269 | 0.4536 | 0.2267 |
| ALL | MARKET_BASELINE | 900 | 0.1977 | 0.6045 | 0.2280 | 0.4547 | 0.2267 |
| ALL | MARKET_ANCHORED_V1 | 900 | 0.1970 | 0.6041 | 0.2277 | 0.4543 | 0.2267 |
| game_spread | DATA_ONLY_V1 | 144 | 0.1607 | 0.4953 | 0.1704 | 0.2334 | 0.1944 |
| game_spread | MARKET_BASELINE | 144 | 0.1609 | 0.5032 | 0.0809 | 0.2348 | 0.1944 |
| game_spread | MARKET_ANCHORED_V1 | 144 | 0.1602 | 0.5004 | 0.0841 | 0.2339 | 0.1944 |
| game_total | DATA_ONLY_V1 | 324 | 0.2304 | 0.7451 | 0.3390 | 0.5735 | 0.2346 |
| game_total | MARKET_BASELINE | 324 | 0.2321 | 0.7314 | 0.3373 | 0.5718 | 0.2346 |
| game_total | MARKET_ANCHORED_V1 | 324 | 0.2317 | 0.7338 | 0.3376 | 0.5722 | 0.2346 |
| game_winner | DATA_ONLY_V1 | 72 | 0.2682 | 0.7328 | 0.5103 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 72 | 0.2629 | 0.7190 | 0.2099 | 0.5004 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 72 | 0.2634 | 0.7201 | 0.1982 | 0.5003 | 0.5000 |
| team_total | DATA_ONLY_V1 | 360 | 0.1641 | 0.5003 | 0.2484 | 0.4245 | 0.1778 |
| team_total | MARKET_BASELINE | 360 | 0.1683 | 0.5080 | 0.2502 | 0.4280 | 0.1778 |
| team_total | MARKET_ANCHORED_V1 | 360 | 0.1672 | 0.5056 | 0.2494 | 0.4272 | 0.1778 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
