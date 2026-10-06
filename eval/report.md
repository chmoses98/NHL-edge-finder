# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-06T02:35:22Z · rows 113811 · pregame 113811 · new 8525

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 21900 | 0.1685 | 0.5075 | 0.0126 | 0.4489 | 0.4460 |
| ALL | MARKET_BASELINE | 97184 | 0.1548 | 0.4745 | 0.0147 | 0.2998 | 0.3003 |
| ALL | MARKET_ANCHORED_V1 | 21900 | 0.1671 | 0.5039 | 0.0189 | 0.4530 | 0.4460 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 5399 | 0.0369 | 0.1613 | 0.0055 | 0.0359 | 0.0383 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 3504 | 0.1797 | 0.5404 | 0.0348 | 0.2310 | 0.2571 |
| game_spread | MARKET_BASELINE | 3504 | 0.1781 | 0.5365 | 0.0534 | 0.2413 | 0.2571 |
| game_spread | MARKET_ANCHORED_V1 | 3504 | 0.1780 | 0.5363 | 0.0473 | 0.2388 | 0.2571 |
| game_total | DATA_ONLY_V1 | 7884 | 0.1278 | 0.4023 | 0.0334 | 0.5673 | 0.5498 |
| game_total | MARKET_BASELINE | 7884 | 0.1248 | 0.3944 | 0.0374 | 0.5723 | 0.5498 |
| game_total | MARKET_ANCHORED_V1 | 7884 | 0.1253 | 0.3956 | 0.0362 | 0.5713 | 0.5498 |
| game_winner | DATA_ONLY_V1 | 1752 | 0.2289 | 0.6503 | 0.0902 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1752 | 0.2338 | 0.6594 | 0.1052 | 0.4997 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1752 | 0.2322 | 0.6563 | 0.1087 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 383 | 0.2549 | 0.7037 | 0.1028 | 0.3905 | 0.4700 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 4948 | 0.1589 | 0.4998 | 0.0665 | 0.1309 | 0.1975 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 7829 | 0.1816 | 0.5406 | 0.0256 | 0.5934 | 0.6014 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 7872 | 0.2160 | 0.6226 | 0.0332 | 0.3280 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 13441 | 0.1536 | 0.4718 | 0.0172 | 0.2341 | 0.2286 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 19539 | 0.1205 | 0.3952 | 0.0159 | 0.1474 | 0.1493 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 15873 | 0.1739 | 0.5209 | 0.0261 | 0.3114 | 0.2977 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 8760 | 0.1886 | 0.5604 | 0.0376 | 0.4192 | 0.4172 |
| team_total | MARKET_BASELINE | 8760 | 0.1874 | 0.5584 | 0.0537 | 0.4238 | 0.4172 |
| team_total | MARKET_ANCHORED_V1 | 8760 | 0.1874 | 0.5581 | 0.0490 | 0.4228 | 0.4172 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
