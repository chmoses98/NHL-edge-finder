# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-03T04:34:30Z · rows 55235 · pregame 55235 · new 2658

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 10100 | 0.1951 | 0.5760 | 0.0607 | 0.4426 | 0.4817 |
| ALL | MARKET_BASELINE | 47615 | 0.1591 | 0.4842 | 0.0199 | 0.2892 | 0.2981 |
| ALL | MARKET_ANCHORED_V1 | 10100 | 0.1943 | 0.5738 | 0.0515 | 0.4506 | 0.4817 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 3277 | 0.0286 | 0.1326 | 0.0041 | 0.0334 | 0.0293 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 1616 | 0.2075 | 0.6060 | 0.0846 | 0.2285 | 0.3020 |
| game_spread | MARKET_BASELINE | 1616 | 0.2089 | 0.6128 | 0.1297 | 0.2412 | 0.3020 |
| game_spread | MARKET_ANCHORED_V1 | 1616 | 0.2082 | 0.6104 | 0.1260 | 0.2382 | 0.3020 |
| game_total | DATA_ONLY_V1 | 3636 | 0.1555 | 0.4784 | 0.0435 | 0.5589 | 0.5806 |
| game_total | MARKET_BASELINE | 3636 | 0.1509 | 0.4652 | 0.0495 | 0.5700 | 0.5806 |
| game_total | MARKET_ANCHORED_V1 | 3636 | 0.1516 | 0.4674 | 0.0520 | 0.5679 | 0.5806 |
| game_winner | DATA_ONLY_V1 | 808 | 0.2418 | 0.6765 | 0.0487 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 808 | 0.2501 | 0.6936 | 0.2707 | 0.5000 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 808 | 0.2479 | 0.6889 | 0.2355 | 0.5000 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 205 | 0.2595 | 0.7136 | 0.1404 | 0.3872 | 0.4585 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 2318 | 0.1594 | 0.5078 | 0.0844 | 0.1296 | 0.1907 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 3621 | 0.1880 | 0.5547 | 0.0383 | 0.5919 | 0.6302 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 3624 | 0.2173 | 0.6252 | 0.0393 | 0.3282 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 6704 | 0.1529 | 0.4688 | 0.0379 | 0.2305 | 0.2157 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 9775 | 0.1205 | 0.3953 | 0.0259 | 0.1391 | 0.1477 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 7991 | 0.1784 | 0.5280 | 0.0545 | 0.3093 | 0.2900 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 4040 | 0.2165 | 0.6317 | 0.0969 | 0.4121 | 0.4609 |
| team_total | MARKET_BASELINE | 4040 | 0.2166 | 0.6329 | 0.1414 | 0.4223 | 0.4609 |
| team_total | MARKET_ANCHORED_V1 | 4040 | 0.2163 | 0.6319 | 0.1307 | 0.4202 | 0.4609 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
