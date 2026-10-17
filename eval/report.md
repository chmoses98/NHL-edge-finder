# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-17T22:12:43Z · rows 355198 · pregame 355198 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 63850 | 0.1627 | 0.4919 | 0.0162 | 0.4498 | 0.4626 |
| ALL | MARKET_BASELINE | 296011 | 0.1486 | 0.4573 | 0.0098 | 0.2909 | 0.2972 |
| ALL | MARKET_ANCHORED_V1 | 63833 | 0.1600 | 0.4848 | 0.0162 | 0.4538 | 0.4627 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13700 | 0.0400 | 0.1710 | 0.0041 | 0.0396 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10216 | 0.1808 | 0.5429 | 0.0296 | 0.2316 | 0.2567 |
| game_spread | MARKET_BASELINE | 10216 | 0.1768 | 0.5328 | 0.0211 | 0.2419 | 0.2567 |
| game_spread | MARKET_ANCHORED_V1 | 10216 | 0.1773 | 0.5338 | 0.0212 | 0.2394 | 0.2567 |
| game_total | DATA_ONLY_V1 | 22986 | 0.1264 | 0.3963 | 0.0224 | 0.5685 | 0.5821 |
| game_total | MARKET_BASELINE | 22986 | 0.1236 | 0.3885 | 0.0274 | 0.5733 | 0.5821 |
| game_total | MARKET_ANCHORED_V1 | 22986 | 0.1240 | 0.3897 | 0.0276 | 0.5724 | 0.5821 |
| game_winner | DATA_ONLY_V1 | 5108 | 0.2285 | 0.6495 | 0.1089 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5108 | 0.2258 | 0.6427 | 0.0364 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5108 | 0.2257 | 0.6429 | 0.0473 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1289 | 0.2439 | 0.6812 | 0.0860 | 0.4319 | 0.3894 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14723 | 0.1411 | 0.4570 | 0.0421 | 0.1296 | 0.1707 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 22797 | 0.1810 | 0.5389 | 0.0294 | 0.5960 | 0.6197 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 22815 | 0.2165 | 0.6236 | 0.0195 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 40527 | 0.1555 | 0.4767 | 0.0166 | 0.2342 | 0.2337 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 64510 | 0.1049 | 0.3487 | 0.0096 | 0.1273 | 0.1306 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 51817 | 0.1681 | 0.5054 | 0.0128 | 0.2952 | 0.2938 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 25540 | 0.1750 | 0.5260 | 0.0204 | 0.4202 | 0.4300 |
| team_total | MARKET_BASELINE | 25523 | 0.1720 | 0.5185 | 0.0161 | 0.4247 | 0.4302 |
| team_total | MARKET_ANCHORED_V1 | 25523 | 0.1724 | 0.5193 | 0.0178 | 0.4237 | 0.4302 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
