# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-04T03:09:26Z · rows 84228 · pregame 84228 · new 8047

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 15850 | 0.1778 | 0.5318 | 0.0217 | 0.4454 | 0.4521 |
| ALL | MARKET_BASELINE | 72023 | 0.1575 | 0.4810 | 0.0151 | 0.2963 | 0.3023 |
| ALL | MARKET_ANCHORED_V1 | 15850 | 0.1781 | 0.5328 | 0.0285 | 0.4529 | 0.4521 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4312 | 0.0333 | 0.1497 | 0.0020 | 0.0348 | 0.0343 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 2536 | 0.1823 | 0.5469 | 0.0376 | 0.2297 | 0.2579 |
| game_spread | MARKET_BASELINE | 2536 | 0.1836 | 0.5524 | 0.0904 | 0.2412 | 0.2579 |
| game_spread | MARKET_ANCHORED_V1 | 2536 | 0.1830 | 0.5504 | 0.0750 | 0.2384 | 0.2579 |
| game_total | DATA_ONLY_V1 | 5706 | 0.1415 | 0.4386 | 0.0221 | 0.5626 | 0.5535 |
| game_total | MARKET_BASELINE | 5706 | 0.1387 | 0.4311 | 0.0305 | 0.5731 | 0.5535 |
| game_total | MARKET_ANCHORED_V1 | 5706 | 0.1391 | 0.4321 | 0.0273 | 0.5710 | 0.5535 |
| game_winner | DATA_ONLY_V1 | 1268 | 0.2315 | 0.6554 | 0.0927 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1268 | 0.2437 | 0.6801 | 0.2203 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1268 | 0.2408 | 0.6740 | 0.2083 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 289 | 0.2551 | 0.7042 | 0.0853 | 0.3935 | 0.4740 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 3669 | 0.1582 | 0.4999 | 0.0643 | 0.1312 | 0.1954 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 5691 | 0.1833 | 0.5440 | 0.0298 | 0.5944 | 0.6148 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 5694 | 0.2165 | 0.6237 | 0.0351 | 0.3278 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 10007 | 0.1569 | 0.4795 | 0.0256 | 0.2322 | 0.2327 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 14638 | 0.1196 | 0.3928 | 0.0223 | 0.1444 | 0.1477 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 11873 | 0.1788 | 0.5311 | 0.0360 | 0.3114 | 0.3127 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 6340 | 0.1979 | 0.5849 | 0.0478 | 0.4153 | 0.4290 |
| team_total | MARKET_BASELINE | 6340 | 0.1993 | 0.5898 | 0.0841 | 0.4250 | 0.4290 |
| team_total | MARKET_ANCHORED_V1 | 6340 | 0.1988 | 0.5882 | 0.0740 | 0.4230 | 0.4290 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
