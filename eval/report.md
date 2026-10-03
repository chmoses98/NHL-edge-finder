# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-03T02:34:30Z · rows 49891 · pregame 49891 · new 2758

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 8975 | 0.2002 | 0.5899 | 0.0667 | 0.4452 | 0.4896 |
| ALL | MARKET_BASELINE | 42939 | 0.1596 | 0.4853 | 0.0214 | 0.2878 | 0.3003 |
| ALL | MARKET_ANCHORED_V1 | 8975 | 0.1974 | 0.5825 | 0.0575 | 0.4520 | 0.4896 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 2984 | 0.0296 | 0.1352 | 0.0029 | 0.0334 | 0.0305 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 1436 | 0.2076 | 0.6044 | 0.0908 | 0.2296 | 0.3078 |
| game_spread | MARKET_BASELINE | 1436 | 0.2044 | 0.5970 | 0.1282 | 0.2417 | 0.3078 |
| game_spread | MARKET_ANCHORED_V1 | 1436 | 0.2046 | 0.5975 | 0.1268 | 0.2388 | 0.3078 |
| game_total | DATA_ONLY_V1 | 3231 | 0.1614 | 0.4957 | 0.0580 | 0.5624 | 0.5911 |
| game_total | MARKET_BASELINE | 3231 | 0.1563 | 0.4809 | 0.0530 | 0.5715 | 0.5911 |
| game_total | MARKET_ANCHORED_V1 | 3231 | 0.1572 | 0.4834 | 0.0559 | 0.5697 | 0.5911 |
| game_winner | DATA_ONLY_V1 | 718 | 0.2390 | 0.6710 | 0.0592 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 718 | 0.2391 | 0.6710 | 0.3127 | 0.4999 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 718 | 0.2385 | 0.6698 | 0.2723 | 0.4999 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 187 | 0.2574 | 0.7086 | 0.1195 | 0.3849 | 0.4599 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 2050 | 0.1614 | 0.5122 | 0.0873 | 0.1295 | 0.1941 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 3216 | 0.1925 | 0.5652 | 0.0465 | 0.5934 | 0.6399 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 3219 | 0.2146 | 0.6192 | 0.0552 | 0.3286 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 6077 | 0.1548 | 0.4744 | 0.0410 | 0.2299 | 0.2210 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 8922 | 0.1185 | 0.3880 | 0.0224 | 0.1382 | 0.1462 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 7309 | 0.1792 | 0.5307 | 0.0538 | 0.3080 | 0.2940 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 3590 | 0.2244 | 0.6527 | 0.0927 | 0.4151 | 0.4688 |
| team_total | MARKET_BASELINE | 3590 | 0.2223 | 0.6480 | 0.1413 | 0.4236 | 0.4688 |
| team_total | MARKET_ANCHORED_V1 | 3590 | 0.2225 | 0.6483 | 0.1242 | 0.4218 | 0.4688 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
