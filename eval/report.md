# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-04T04:09:38Z · rows 86975 · pregame 86975 · new 2747

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 16425 | 0.1770 | 0.5295 | 0.0224 | 0.4469 | 0.4559 |
| ALL | MARKET_BASELINE | 74319 | 0.1577 | 0.4815 | 0.0149 | 0.2974 | 0.3045 |
| ALL | MARKET_ANCHORED_V1 | 16425 | 0.1770 | 0.5295 | 0.0283 | 0.4534 | 0.4559 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4376 | 0.0345 | 0.1538 | 0.0035 | 0.0352 | 0.0356 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 2628 | 0.1829 | 0.5473 | 0.0459 | 0.2307 | 0.2664 |
| game_spread | MARKET_BASELINE | 2628 | 0.1830 | 0.5495 | 0.0792 | 0.2421 | 0.2664 |
| game_spread | MARKET_ANCHORED_V1 | 2628 | 0.1826 | 0.5482 | 0.0677 | 0.2394 | 0.2664 |
| game_total | DATA_ONLY_V1 | 5913 | 0.1389 | 0.4320 | 0.0172 | 0.5645 | 0.5574 |
| game_total | MARKET_BASELINE | 5913 | 0.1363 | 0.4252 | 0.0267 | 0.5733 | 0.5574 |
| game_total | MARKET_ANCHORED_V1 | 5913 | 0.1367 | 0.4261 | 0.0264 | 0.5715 | 0.5574 |
| game_winner | DATA_ONLY_V1 | 1314 | 0.2273 | 0.6468 | 0.1012 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1314 | 0.2379 | 0.6678 | 0.2027 | 0.4996 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1314 | 0.2353 | 0.6625 | 0.1908 | 0.4997 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 294 | 0.2584 | 0.7113 | 0.0918 | 0.3925 | 0.4830 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 3778 | 0.1620 | 0.5080 | 0.0699 | 0.1320 | 0.2020 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 5898 | 0.1827 | 0.5422 | 0.0290 | 0.5947 | 0.6166 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 5901 | 0.2159 | 0.6224 | 0.0409 | 0.3278 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 10395 | 0.1562 | 0.4779 | 0.0241 | 0.2325 | 0.2321 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 15053 | 0.1208 | 0.3962 | 0.0223 | 0.1451 | 0.1492 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 12199 | 0.1785 | 0.5303 | 0.0358 | 0.3129 | 0.3130 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 6570 | 0.1990 | 0.5867 | 0.0511 | 0.4169 | 0.4315 |
| team_total | MARKET_BASELINE | 6570 | 0.1997 | 0.5898 | 0.0912 | 0.4251 | 0.4315 |
| team_total | MARKET_ANCHORED_V1 | 6570 | 0.1993 | 0.5885 | 0.0783 | 0.4234 | 0.4315 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
