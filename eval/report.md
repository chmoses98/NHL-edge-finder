# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-15T15:59:03Z · rows 310656 · pregame 310656 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 56600 | 0.1656 | 0.4992 | 0.0195 | 0.4492 | 0.4637 |
| ALL | MARKET_BASELINE | 260378 | 0.1493 | 0.4591 | 0.0099 | 0.2907 | 0.2967 |
| ALL | MARKET_ANCHORED_V1 | 56586 | 0.1634 | 0.4934 | 0.0154 | 0.4532 | 0.4638 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 12355 | 0.0405 | 0.1727 | 0.0051 | 0.0393 | 0.0423 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 9056 | 0.1878 | 0.5596 | 0.0414 | 0.2313 | 0.2683 |
| game_spread | MARKET_BASELINE | 9056 | 0.1839 | 0.5499 | 0.0329 | 0.2414 | 0.2683 |
| game_spread | MARKET_ANCHORED_V1 | 9056 | 0.1843 | 0.5509 | 0.0325 | 0.2389 | 0.2683 |
| game_total | DATA_ONLY_V1 | 20376 | 0.1274 | 0.3998 | 0.0207 | 0.5677 | 0.5801 |
| game_total | MARKET_BASELINE | 20376 | 0.1250 | 0.3928 | 0.0287 | 0.5725 | 0.5801 |
| game_total | MARKET_ANCHORED_V1 | 20376 | 0.1254 | 0.3937 | 0.0271 | 0.5715 | 0.5801 |
| game_winner | DATA_ONLY_V1 | 4528 | 0.2314 | 0.6553 | 0.1081 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4528 | 0.2301 | 0.6519 | 0.0340 | 0.4990 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4528 | 0.2298 | 0.6514 | 0.0372 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1100 | 0.2455 | 0.6849 | 0.0945 | 0.4253 | 0.3900 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 13073 | 0.1425 | 0.4608 | 0.0432 | 0.1296 | 0.1718 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 20187 | 0.1815 | 0.5403 | 0.0276 | 0.5951 | 0.6185 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 20205 | 0.2172 | 0.6252 | 0.0203 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 35573 | 0.1531 | 0.4706 | 0.0179 | 0.2321 | 0.2291 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 56357 | 0.1057 | 0.3510 | 0.0107 | 0.1275 | 0.1315 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 44942 | 0.1678 | 0.5047 | 0.0130 | 0.2949 | 0.2897 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 22640 | 0.1780 | 0.5334 | 0.0177 | 0.4196 | 0.4298 |
| team_total | MARKET_BASELINE | 22626 | 0.1757 | 0.5281 | 0.0172 | 0.4240 | 0.4300 |
| team_total | MARKET_ANCHORED_V1 | 22626 | 0.1759 | 0.5285 | 0.0201 | 0.4231 | 0.4300 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
