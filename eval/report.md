# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-18T03:11:47Z · rows 387280 · pregame 387280 · new 3345

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 69150 | 0.1618 | 0.4902 | 0.0165 | 0.4492 | 0.4588 |
| ALL | MARKET_BASELINE | 319785 | 0.1483 | 0.4567 | 0.0089 | 0.2916 | 0.2956 |
| ALL | MARKET_ANCHORED_V1 | 69132 | 0.1596 | 0.4846 | 0.0153 | 0.4537 | 0.4589 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14371 | 0.0394 | 0.1690 | 0.0032 | 0.0399 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11064 | 0.1803 | 0.5415 | 0.0296 | 0.2313 | 0.2565 |
| game_spread | MARKET_BASELINE | 11064 | 0.1765 | 0.5319 | 0.0269 | 0.2421 | 0.2565 |
| game_spread | MARKET_ANCHORED_V1 | 11064 | 0.1769 | 0.5328 | 0.0207 | 0.2395 | 0.2565 |
| game_total | DATA_ONLY_V1 | 24894 | 0.1268 | 0.3989 | 0.0233 | 0.5678 | 0.5766 |
| game_total | MARKET_BASELINE | 24894 | 0.1251 | 0.3947 | 0.0262 | 0.5735 | 0.5766 |
| game_total | MARKET_ANCHORED_V1 | 24894 | 0.1253 | 0.3951 | 0.0251 | 0.5723 | 0.5766 |
| game_winner | DATA_ONLY_V1 | 5532 | 0.2272 | 0.6468 | 0.1270 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5532 | 0.2235 | 0.6379 | 0.0457 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5532 | 0.2236 | 0.6385 | 0.0592 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1383 | 0.2459 | 0.6853 | 0.0717 | 0.4349 | 0.4056 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 15893 | 0.1371 | 0.4455 | 0.0377 | 0.1293 | 0.1661 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 24705 | 0.1830 | 0.5437 | 0.0278 | 0.5962 | 0.6155 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 24723 | 0.2160 | 0.6226 | 0.0223 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 43444 | 0.1560 | 0.4780 | 0.0186 | 0.2365 | 0.2333 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 70315 | 0.1039 | 0.3462 | 0.0098 | 0.1264 | 0.1294 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 55819 | 0.1679 | 0.5051 | 0.0144 | 0.2967 | 0.2927 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 27660 | 0.1729 | 0.5206 | 0.0119 | 0.4196 | 0.4253 |
| team_total | MARKET_BASELINE | 27642 | 0.1705 | 0.5146 | 0.0144 | 0.4247 | 0.4256 |
| team_total | MARKET_ANCHORED_V1 | 27642 | 0.1707 | 0.5151 | 0.0145 | 0.4236 | 0.4256 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
