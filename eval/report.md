# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-09T02:07:35Z · rows 169861 · pregame 169861 · new 15918

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 32200 | 0.1678 | 0.5039 | 0.0108 | 0.4503 | 0.4590 |
| ALL | MARKET_BASELINE | 144642 | 0.1530 | 0.4691 | 0.0100 | 0.2941 | 0.3022 |
| ALL | MARKET_ANCHORED_V1 | 32193 | 0.1658 | 0.4988 | 0.0107 | 0.4534 | 0.4591 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 8222 | 0.0409 | 0.1752 | 0.0077 | 0.0371 | 0.0427 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5152 | 0.1828 | 0.5474 | 0.0395 | 0.2312 | 0.2638 |
| game_spread | MARKET_BASELINE | 5152 | 0.1793 | 0.5385 | 0.0378 | 0.2413 | 0.2638 |
| game_spread | MARKET_ANCHORED_V1 | 5152 | 0.1796 | 0.5393 | 0.0312 | 0.2388 | 0.2638 |
| game_total | DATA_ONLY_V1 | 11592 | 0.1271 | 0.3977 | 0.0236 | 0.5693 | 0.5695 |
| game_total | MARKET_BASELINE | 11592 | 0.1253 | 0.3923 | 0.0264 | 0.5725 | 0.5695 |
| game_total | MARKET_ANCHORED_V1 | 11592 | 0.1255 | 0.3930 | 0.0256 | 0.5718 | 0.5695 |
| game_winner | DATA_ONLY_V1 | 2576 | 0.2321 | 0.6567 | 0.0818 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2576 | 0.2307 | 0.6531 | 0.0431 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2576 | 0.2304 | 0.6525 | 0.0234 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 556 | 0.2557 | 0.7057 | 0.0825 | 0.4118 | 0.4622 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 7337 | 0.1541 | 0.4906 | 0.0591 | 0.1309 | 0.1881 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 11456 | 0.1841 | 0.5462 | 0.0294 | 0.5946 | 0.6163 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 11482 | 0.2164 | 0.6235 | 0.0301 | 0.3284 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 18960 | 0.1601 | 0.4892 | 0.0186 | 0.2373 | 0.2405 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 31219 | 0.1113 | 0.3672 | 0.0089 | 0.1344 | 0.1395 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 23217 | 0.1762 | 0.5264 | 0.0218 | 0.3078 | 0.3075 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 12880 | 0.1855 | 0.5516 | 0.0282 | 0.4210 | 0.4295 |
| team_total | MARKET_BASELINE | 12873 | 0.1834 | 0.5467 | 0.0321 | 0.4241 | 0.4297 |
| team_total | MARKET_ANCHORED_V1 | 12873 | 0.1836 | 0.5470 | 0.0324 | 0.4234 | 0.4297 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
