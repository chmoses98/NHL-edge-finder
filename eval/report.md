# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-25T02:06:18Z · rows 523797 · pregame 523797 · new 7322

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 91150 | 0.1621 | 0.4901 | 0.0186 | 0.4486 | 0.4634 |
| ALL | MARKET_BASELINE | 431122 | 0.1484 | 0.4565 | 0.0083 | 0.2894 | 0.2956 |
| ALL | MARKET_ANCHORED_V1 | 91125 | 0.1605 | 0.4861 | 0.0151 | 0.4547 | 0.4635 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 19364 | 0.0400 | 0.1708 | 0.0032 | 0.0405 | 0.0419 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 14584 | 0.1821 | 0.5465 | 0.0273 | 0.2311 | 0.2567 |
| game_spread | MARKET_BASELINE | 14584 | 0.1788 | 0.5375 | 0.0221 | 0.2427 | 0.2567 |
| game_spread | MARKET_ANCHORED_V1 | 14584 | 0.1791 | 0.5384 | 0.0209 | 0.2399 | 0.2567 |
| game_total | DATA_ONLY_V1 | 32814 | 0.1245 | 0.3912 | 0.0308 | 0.5669 | 0.5827 |
| game_total | MARKET_BASELINE | 32814 | 0.1236 | 0.3886 | 0.0269 | 0.5753 | 0.5827 |
| game_total | MARKET_ANCHORED_V1 | 32814 | 0.1236 | 0.3887 | 0.0271 | 0.5736 | 0.5827 |
| game_winner | DATA_ONLY_V1 | 7292 | 0.2307 | 0.6540 | 0.1047 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7292 | 0.2294 | 0.6502 | 0.0344 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7292 | 0.2290 | 0.6498 | 0.0326 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1970 | 0.2509 | 0.6953 | 0.0582 | 0.4439 | 0.4396 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 20835 | 0.1381 | 0.4497 | 0.0383 | 0.1286 | 0.1663 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 32625 | 0.1794 | 0.5349 | 0.0295 | 0.5978 | 0.6242 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 32643 | 0.2169 | 0.6246 | 0.0225 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 60445 | 0.1560 | 0.4775 | 0.0177 | 0.2337 | 0.2319 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 93702 | 0.1035 | 0.3444 | 0.0080 | 0.1250 | 0.1292 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 78413 | 0.1675 | 0.5038 | 0.0111 | 0.2908 | 0.2893 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 36460 | 0.1741 | 0.5237 | 0.0133 | 0.4189 | 0.4312 |
| team_total | MARKET_BASELINE | 36435 | 0.1726 | 0.5201 | 0.0174 | 0.4262 | 0.4315 |
| team_total | MARKET_ANCHORED_V1 | 36435 | 0.1727 | 0.5201 | 0.0177 | 0.4247 | 0.4315 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
