# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-19T02:42:25Z · rows 401109 · pregame 401109 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 71550 | 0.1626 | 0.4920 | 0.0159 | 0.4496 | 0.4596 |
| ALL | MARKET_BASELINE | 330672 | 0.1485 | 0.4570 | 0.0086 | 0.2920 | 0.2962 |
| ALL | MARKET_ANCHORED_V1 | 71532 | 0.1605 | 0.4867 | 0.0143 | 0.4542 | 0.4597 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 14734 | 0.0388 | 0.1669 | 0.0023 | 0.0400 | 0.0405 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11448 | 0.1833 | 0.5488 | 0.0344 | 0.2314 | 0.2614 |
| game_spread | MARKET_BASELINE | 11448 | 0.1794 | 0.5386 | 0.0313 | 0.2423 | 0.2614 |
| game_spread | MARKET_ANCHORED_V1 | 11448 | 0.1798 | 0.5397 | 0.0255 | 0.2397 | 0.2614 |
| game_total | DATA_ONLY_V1 | 25758 | 0.1263 | 0.3973 | 0.0249 | 0.5682 | 0.5768 |
| game_total | MARKET_BASELINE | 25758 | 0.1250 | 0.3940 | 0.0296 | 0.5741 | 0.5768 |
| game_total | MARKET_ANCHORED_V1 | 25758 | 0.1251 | 0.3943 | 0.0285 | 0.5729 | 0.5768 |
| game_winner | DATA_ONLY_V1 | 5724 | 0.2271 | 0.6466 | 0.1193 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5724 | 0.2235 | 0.6379 | 0.0596 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5724 | 0.2236 | 0.6384 | 0.0530 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1436 | 0.2465 | 0.6864 | 0.0644 | 0.4361 | 0.4116 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 16422 | 0.1377 | 0.4474 | 0.0380 | 0.1293 | 0.1665 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 25569 | 0.1828 | 0.5432 | 0.0296 | 0.5967 | 0.6181 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 25587 | 0.2160 | 0.6226 | 0.0249 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 44822 | 0.1562 | 0.4786 | 0.0191 | 0.2374 | 0.2338 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 72868 | 0.1038 | 0.3454 | 0.0095 | 0.1262 | 0.1295 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 57702 | 0.1676 | 0.5041 | 0.0145 | 0.2973 | 0.2929 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 28620 | 0.1742 | 0.5236 | 0.0137 | 0.4200 | 0.4253 |
| team_total | MARKET_BASELINE | 28602 | 0.1719 | 0.5181 | 0.0168 | 0.4251 | 0.4255 |
| team_total | MARKET_ANCHORED_V1 | 28602 | 0.1721 | 0.5185 | 0.0165 | 0.4240 | 0.4255 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
