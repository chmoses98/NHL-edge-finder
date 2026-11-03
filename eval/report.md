# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-03T03:18:42Z · rows 808028 · pregame 808028 · new 7372

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 132650 | 0.1660 | 0.4998 | 0.0223 | 0.4498 | 0.4721 |
| ALL | MARKET_BASELINE | 694398 | 0.1439 | 0.4442 | 0.0123 | 0.2732 | 0.2840 |
| ALL | MARKET_ANCHORED_V1 | 132617 | 0.1638 | 0.4943 | 0.0155 | 0.4567 | 0.4722 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 49973 | 0.0341 | 0.1484 | 0.0019 | 0.0345 | 0.0356 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 21224 | 0.1849 | 0.5542 | 0.0297 | 0.2314 | 0.2599 |
| game_spread | MARKET_BASELINE | 21224 | 0.1806 | 0.5425 | 0.0239 | 0.2435 | 0.2599 |
| game_spread | MARKET_ANCHORED_V1 | 21224 | 0.1811 | 0.5439 | 0.0211 | 0.2406 | 0.2599 |
| game_total | DATA_ONLY_V1 | 47754 | 0.1295 | 0.4035 | 0.0304 | 0.5685 | 0.5932 |
| game_total | MARKET_BASELINE | 47754 | 0.1281 | 0.3996 | 0.0243 | 0.5779 | 0.5932 |
| game_total | MARKET_ANCHORED_V1 | 47754 | 0.1282 | 0.3999 | 0.0251 | 0.5761 | 0.5932 |
| game_winner | DATA_ONLY_V1 | 10612 | 0.2322 | 0.6569 | 0.0726 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10612 | 0.2291 | 0.6497 | 0.0253 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10612 | 0.2291 | 0.6500 | 0.0326 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3106 | 0.2483 | 0.6903 | 0.0337 | 0.4461 | 0.4411 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 30352 | 0.1346 | 0.4407 | 0.0330 | 0.1286 | 0.1611 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 47535 | 0.1782 | 0.5315 | 0.0298 | 0.5995 | 0.6275 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 47583 | 0.2166 | 0.6238 | 0.0253 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 99192 | 0.1583 | 0.4838 | 0.0194 | 0.2297 | 0.2381 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 153698 | 0.1007 | 0.3362 | 0.0080 | 0.1191 | 0.1259 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 130342 | 0.1664 | 0.5021 | 0.0134 | 0.2814 | 0.2907 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 53060 | 0.1780 | 0.5334 | 0.0235 | 0.4203 | 0.4424 |
| team_total | MARKET_BASELINE | 53027 | 0.1757 | 0.5278 | 0.0185 | 0.4288 | 0.4427 |
| team_total | MARKET_ANCHORED_V1 | 53027 | 0.1759 | 0.5283 | 0.0177 | 0.4270 | 0.4427 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
