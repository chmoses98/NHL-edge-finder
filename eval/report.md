# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-05T03:06:32Z · rows 102440 · pregame 102440 · new 5647

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 19675 | 0.1720 | 0.5163 | 0.0152 | 0.4478 | 0.4559 |
| ALL | MARKET_BASELINE | 87561 | 0.1572 | 0.4804 | 0.0150 | 0.2987 | 0.3074 |
| ALL | MARKET_ANCHORED_V1 | 19675 | 0.1718 | 0.5160 | 0.0228 | 0.4529 | 0.4559 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4973 | 0.0362 | 0.1595 | 0.0047 | 0.0359 | 0.0376 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 3148 | 0.1792 | 0.5385 | 0.0368 | 0.2306 | 0.2589 |
| game_spread | MARKET_BASELINE | 3148 | 0.1789 | 0.5396 | 0.0552 | 0.2408 | 0.2589 |
| game_spread | MARKET_ANCHORED_V1 | 3148 | 0.1785 | 0.5384 | 0.0441 | 0.2383 | 0.2589 |
| game_total | DATA_ONLY_V1 | 7083 | 0.1326 | 0.4149 | 0.0200 | 0.5659 | 0.5618 |
| game_total | MARKET_BASELINE | 7083 | 0.1302 | 0.4082 | 0.0231 | 0.5726 | 0.5618 |
| game_total | MARKET_ANCHORED_V1 | 7083 | 0.1305 | 0.4091 | 0.0205 | 0.5713 | 0.5618 |
| game_winner | DATA_ONLY_V1 | 1574 | 0.2263 | 0.6448 | 0.1102 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1574 | 0.2375 | 0.6671 | 0.1321 | 0.4997 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1574 | 0.2347 | 0.6615 | 0.1329 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 340 | 0.2618 | 0.7182 | 0.1170 | 0.3916 | 0.4824 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 4496 | 0.1584 | 0.4989 | 0.0655 | 0.1311 | 0.1966 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 7043 | 0.1814 | 0.5391 | 0.0222 | 0.5935 | 0.6132 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 7071 | 0.2160 | 0.6226 | 0.0334 | 0.3280 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 12105 | 0.1591 | 0.4853 | 0.0191 | 0.2323 | 0.2411 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 17756 | 0.1207 | 0.3960 | 0.0150 | 0.1466 | 0.1501 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 14102 | 0.1789 | 0.5328 | 0.0283 | 0.3119 | 0.3153 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 7870 | 0.1936 | 0.5731 | 0.0427 | 0.4181 | 0.4305 |
| team_total | MARKET_BASELINE | 7870 | 0.1941 | 0.5753 | 0.0580 | 0.4243 | 0.4305 |
| team_total | MARKET_ANCHORED_V1 | 7870 | 0.1937 | 0.5742 | 0.0535 | 0.4230 | 0.4305 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
