# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-24T08:58:21Z · rows 516475 · pregame 516475 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 90150 | 0.1622 | 0.4904 | 0.0182 | 0.4488 | 0.4637 |
| ALL | MARKET_BASELINE | 424540 | 0.1486 | 0.4571 | 0.0082 | 0.2903 | 0.2962 |
| ALL | MARKET_ANCHORED_V1 | 90125 | 0.1606 | 0.4864 | 0.0151 | 0.4549 | 0.4638 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 18604 | 0.0400 | 0.1706 | 0.0029 | 0.0409 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 14424 | 0.1831 | 0.5489 | 0.0284 | 0.2311 | 0.2580 |
| game_spread | MARKET_BASELINE | 14424 | 0.1797 | 0.5397 | 0.0242 | 0.2428 | 0.2580 |
| game_spread | MARKET_ANCHORED_V1 | 14424 | 0.1800 | 0.5406 | 0.0221 | 0.2400 | 0.2580 |
| game_total | DATA_ONLY_V1 | 32454 | 0.1241 | 0.3903 | 0.0307 | 0.5672 | 0.5829 |
| game_total | MARKET_BASELINE | 32454 | 0.1231 | 0.3876 | 0.0273 | 0.5755 | 0.5829 |
| game_total | MARKET_ANCHORED_V1 | 32454 | 0.1232 | 0.3877 | 0.0277 | 0.5739 | 0.5829 |
| game_winner | DATA_ONLY_V1 | 7212 | 0.2312 | 0.6549 | 0.1010 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7212 | 0.2297 | 0.6510 | 0.0300 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7212 | 0.2294 | 0.6505 | 0.0330 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1964 | 0.2510 | 0.6955 | 0.0588 | 0.4439 | 0.4409 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 20613 | 0.1377 | 0.4486 | 0.0388 | 0.1286 | 0.1656 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 32265 | 0.1795 | 0.5351 | 0.0290 | 0.5980 | 0.6241 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 32283 | 0.2170 | 0.6247 | 0.0211 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 59428 | 0.1560 | 0.4779 | 0.0180 | 0.2341 | 0.2315 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 92151 | 0.1034 | 0.3442 | 0.0080 | 0.1254 | 0.1292 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 77107 | 0.1678 | 0.5045 | 0.0107 | 0.2914 | 0.2894 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 36060 | 0.1743 | 0.5242 | 0.0137 | 0.4192 | 0.4314 |
| team_total | MARKET_BASELINE | 36035 | 0.1728 | 0.5206 | 0.0153 | 0.4264 | 0.4317 |
| team_total | MARKET_ANCHORED_V1 | 36035 | 0.1728 | 0.5206 | 0.0161 | 0.4249 | 0.4317 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
