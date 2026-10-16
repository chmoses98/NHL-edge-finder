# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-16T02:24:11Z · rows 326055 · pregame 326055 · new 15399

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 59100 | 0.1651 | 0.4981 | 0.0167 | 0.4495 | 0.4627 |
| ALL | MARKET_BASELINE | 272778 | 0.1491 | 0.4587 | 0.0097 | 0.2907 | 0.2961 |
| ALL | MARKET_ANCHORED_V1 | 59086 | 0.1625 | 0.4911 | 0.0140 | 0.4533 | 0.4628 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 12742 | 0.0407 | 0.1732 | 0.0051 | 0.0394 | 0.0425 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 9456 | 0.1850 | 0.5533 | 0.0341 | 0.2314 | 0.2612 |
| game_spread | MARKET_BASELINE | 9456 | 0.1812 | 0.5433 | 0.0267 | 0.2417 | 0.2612 |
| game_spread | MARKET_ANCHORED_V1 | 9456 | 0.1816 | 0.5443 | 0.0257 | 0.2392 | 0.2612 |
| game_total | DATA_ONLY_V1 | 21276 | 0.1279 | 0.4004 | 0.0212 | 0.5681 | 0.5810 |
| game_total | MARKET_BASELINE | 21276 | 0.1251 | 0.3924 | 0.0278 | 0.5726 | 0.5810 |
| game_total | MARKET_ANCHORED_V1 | 21276 | 0.1255 | 0.3936 | 0.0275 | 0.5717 | 0.5810 |
| game_winner | DATA_ONLY_V1 | 4728 | 0.2298 | 0.6522 | 0.1132 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4728 | 0.2271 | 0.6455 | 0.0369 | 0.4990 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4728 | 0.2270 | 0.6456 | 0.0439 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1160 | 0.2443 | 0.6824 | 0.0953 | 0.4272 | 0.3836 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 13622 | 0.1414 | 0.4583 | 0.0418 | 0.1297 | 0.1705 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 21087 | 0.1816 | 0.5407 | 0.0274 | 0.5953 | 0.6177 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 21105 | 0.2172 | 0.6252 | 0.0184 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 37312 | 0.1537 | 0.4723 | 0.0175 | 0.2328 | 0.2295 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 59279 | 0.1053 | 0.3499 | 0.0114 | 0.1273 | 0.1306 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 47385 | 0.1681 | 0.5057 | 0.0121 | 0.2948 | 0.2900 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 23640 | 0.1777 | 0.5331 | 0.0140 | 0.4199 | 0.4294 |
| team_total | MARKET_BASELINE | 23626 | 0.1749 | 0.5260 | 0.0155 | 0.4241 | 0.4296 |
| team_total | MARKET_ANCHORED_V1 | 23626 | 0.1752 | 0.5267 | 0.0156 | 0.4232 | 0.4296 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
