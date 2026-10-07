# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-07T02:03:42Z · rows 131433 · pregame 131433 · new 14827

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 25075 | 0.1683 | 0.5063 | 0.0108 | 0.4496 | 0.4603 |
| ALL | MARKET_BASELINE | 111938 | 0.1551 | 0.4752 | 0.0140 | 0.2983 | 0.3069 |
| ALL | MARKET_ANCHORED_V1 | 25075 | 0.1669 | 0.5028 | 0.0138 | 0.4532 | 0.4603 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 6241 | 0.0400 | 0.1720 | 0.0081 | 0.0363 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4012 | 0.1748 | 0.5282 | 0.0279 | 0.2310 | 0.2512 |
| game_spread | MARKET_BASELINE | 4012 | 0.1737 | 0.5256 | 0.0406 | 0.2411 | 0.2512 |
| game_spread | MARKET_ANCHORED_V1 | 4012 | 0.1735 | 0.5251 | 0.0307 | 0.2386 | 0.2512 |
| game_total | DATA_ONLY_V1 | 9027 | 0.1310 | 0.4089 | 0.0270 | 0.5683 | 0.5714 |
| game_total | MARKET_BASELINE | 9027 | 0.1283 | 0.4016 | 0.0260 | 0.5725 | 0.5714 |
| game_total | MARKET_ANCHORED_V1 | 9027 | 0.1287 | 0.4027 | 0.0257 | 0.5717 | 0.5714 |
| game_winner | DATA_ONLY_V1 | 2006 | 0.2288 | 0.6501 | 0.1004 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2006 | 0.2319 | 0.6556 | 0.1039 | 0.4995 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2006 | 0.2307 | 0.6532 | 0.0789 | 0.4996 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 437 | 0.2536 | 0.7007 | 0.0981 | 0.3972 | 0.4828 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 5700 | 0.1580 | 0.5007 | 0.0650 | 0.1311 | 0.1937 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 8972 | 0.1804 | 0.5373 | 0.0245 | 0.5940 | 0.6142 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 9015 | 0.2154 | 0.6213 | 0.0346 | 0.3282 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 15205 | 0.1575 | 0.4820 | 0.0165 | 0.2359 | 0.2397 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 23029 | 0.1193 | 0.3904 | 0.0123 | 0.1438 | 0.1499 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 18264 | 0.1757 | 0.5261 | 0.0234 | 0.3101 | 0.3081 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 10030 | 0.1871 | 0.5565 | 0.0295 | 0.4201 | 0.4360 |
| team_total | MARKET_BASELINE | 10030 | 0.1860 | 0.5541 | 0.0427 | 0.4240 | 0.4360 |
| team_total | MARKET_ANCHORED_V1 | 10030 | 0.1859 | 0.5538 | 0.0360 | 0.4231 | 0.4360 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
