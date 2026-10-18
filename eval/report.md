# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-18T02:05:26Z · rows 383935 · pregame 383935 · new 19869

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 68575 | 0.1619 | 0.4905 | 0.0158 | 0.4490 | 0.4579 |
| ALL | MARKET_BASELINE | 317286 | 0.1482 | 0.4564 | 0.0089 | 0.2915 | 0.2950 |
| ALL | MARKET_ANCHORED_V1 | 68557 | 0.1595 | 0.4845 | 0.0154 | 0.4537 | 0.4580 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14363 | 0.0394 | 0.1691 | 0.0032 | 0.0399 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10972 | 0.1793 | 0.5395 | 0.0277 | 0.2313 | 0.2545 |
| game_spread | MARKET_BASELINE | 10972 | 0.1753 | 0.5290 | 0.0249 | 0.2422 | 0.2545 |
| game_spread | MARKET_ANCHORED_V1 | 10972 | 0.1757 | 0.5301 | 0.0187 | 0.2395 | 0.2545 |
| game_total | DATA_ONLY_V1 | 24687 | 0.1273 | 0.4002 | 0.0226 | 0.5674 | 0.5758 |
| game_total | MARKET_BASELINE | 24687 | 0.1255 | 0.3958 | 0.0265 | 0.5735 | 0.5758 |
| game_total | MARKET_ANCHORED_V1 | 24687 | 0.1257 | 0.3962 | 0.0254 | 0.5723 | 0.5758 |
| game_winner | DATA_ONLY_V1 | 5486 | 0.2274 | 0.6471 | 0.1243 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5486 | 0.2232 | 0.6374 | 0.0430 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5486 | 0.2234 | 0.6381 | 0.0560 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1377 | 0.2458 | 0.6851 | 0.0698 | 0.4345 | 0.4074 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 15764 | 0.1371 | 0.4455 | 0.0375 | 0.1294 | 0.1660 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 24498 | 0.1832 | 0.5442 | 0.0265 | 0.5963 | 0.6142 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 24516 | 0.2160 | 0.6225 | 0.0221 | 0.3282 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 43130 | 0.1555 | 0.4769 | 0.0187 | 0.2364 | 0.2325 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 69719 | 0.1037 | 0.3457 | 0.0099 | 0.1265 | 0.1291 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 55362 | 0.1680 | 0.5055 | 0.0136 | 0.2968 | 0.2922 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 27430 | 0.1730 | 0.5210 | 0.0126 | 0.4193 | 0.4247 |
| team_total | MARKET_BASELINE | 27412 | 0.1704 | 0.5145 | 0.0145 | 0.4247 | 0.4250 |
| team_total | MARKET_ANCHORED_V1 | 27412 | 0.1706 | 0.5151 | 0.0153 | 0.4236 | 0.4250 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
