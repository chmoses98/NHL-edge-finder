# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-27T03:55:34Z · rows 610591 · pregame 610591 · new 4072

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 103525 | 0.1655 | 0.4985 | 0.0209 | 0.4490 | 0.4686 |
| ALL | MARKET_BASELINE | 510846 | 0.1473 | 0.4534 | 0.0100 | 0.2826 | 0.2919 |
| ALL | MARKET_ANCHORED_V1 | 103500 | 0.1634 | 0.4931 | 0.0156 | 0.4556 | 0.4687 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 27699 | 0.0368 | 0.1590 | 0.0016 | 0.0377 | 0.0384 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16564 | 0.1870 | 0.5597 | 0.0318 | 0.2311 | 0.2616 |
| game_spread | MARKET_BASELINE | 16564 | 0.1831 | 0.5488 | 0.0255 | 0.2428 | 0.2616 |
| game_spread | MARKET_ANCHORED_V1 | 16564 | 0.1835 | 0.5499 | 0.0223 | 0.2400 | 0.2616 |
| game_total | DATA_ONLY_V1 | 37269 | 0.1276 | 0.3983 | 0.0296 | 0.5675 | 0.5894 |
| game_total | MARKET_BASELINE | 37269 | 0.1261 | 0.3942 | 0.0284 | 0.5765 | 0.5894 |
| game_total | MARKET_ANCHORED_V1 | 37269 | 0.1262 | 0.3946 | 0.0268 | 0.5747 | 0.5894 |
| game_winner | DATA_ONLY_V1 | 8282 | 0.2333 | 0.6592 | 0.0935 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8282 | 0.2300 | 0.6517 | 0.0269 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8282 | 0.2300 | 0.6520 | 0.0375 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2333 | 0.2529 | 0.6996 | 0.0489 | 0.4446 | 0.4604 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 23605 | 0.1371 | 0.4479 | 0.0362 | 0.1288 | 0.1644 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 37080 | 0.1813 | 0.5396 | 0.0278 | 0.5990 | 0.6261 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 37098 | 0.2177 | 0.6264 | 0.0169 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 72421 | 0.1577 | 0.4823 | 0.0131 | 0.2319 | 0.2356 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 112704 | 0.1025 | 0.3411 | 0.0083 | 0.1217 | 0.1282 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 94406 | 0.1668 | 0.5023 | 0.0091 | 0.2864 | 0.2912 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 41410 | 0.1773 | 0.5322 | 0.0193 | 0.4194 | 0.4365 |
| team_total | MARKET_BASELINE | 41385 | 0.1752 | 0.5269 | 0.0198 | 0.4274 | 0.4367 |
| team_total | MARKET_ANCHORED_V1 | 41385 | 0.1754 | 0.5273 | 0.0166 | 0.4258 | 0.4367 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
