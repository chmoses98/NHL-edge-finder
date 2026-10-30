# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-30T04:45:53Z · rows 710621 · pregame 710621 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 118650 | 0.1653 | 0.4985 | 0.0164 | 0.4488 | 0.4642 |
| ALL | MARKET_BASELINE | 606554 | 0.1440 | 0.4446 | 0.0087 | 0.2763 | 0.2825 |
| ALL | MARKET_ANCHORED_V1 | 118617 | 0.1633 | 0.4933 | 0.0117 | 0.4560 | 0.4643 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 39903 | 0.0348 | 0.1515 | 0.0018 | 0.0353 | 0.0364 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 18984 | 0.1845 | 0.5536 | 0.0276 | 0.2310 | 0.2575 |
| game_spread | MARKET_BASELINE | 18984 | 0.1803 | 0.5419 | 0.0194 | 0.2431 | 0.2575 |
| game_spread | MARKET_ANCHORED_V1 | 18984 | 0.1808 | 0.5433 | 0.0187 | 0.2402 | 0.2575 |
| game_total | DATA_ONLY_V1 | 42714 | 0.1290 | 0.4032 | 0.0246 | 0.5671 | 0.5833 |
| game_total | MARKET_BASELINE | 42714 | 0.1279 | 0.4001 | 0.0234 | 0.5771 | 0.5833 |
| game_total | MARKET_ANCHORED_V1 | 42714 | 0.1280 | 0.4002 | 0.0204 | 0.5752 | 0.5833 |
| game_winner | DATA_ONLY_V1 | 9492 | 0.2345 | 0.6617 | 0.0802 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 9492 | 0.2308 | 0.6534 | 0.0214 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 9492 | 0.2310 | 0.6539 | 0.0327 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2801 | 0.2493 | 0.6922 | 0.0415 | 0.4471 | 0.4373 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 27138 | 0.1327 | 0.4365 | 0.0303 | 0.1286 | 0.1584 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 42525 | 0.1806 | 0.5374 | 0.0227 | 0.5995 | 0.6190 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 42543 | 0.2168 | 0.6243 | 0.0240 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 86097 | 0.1561 | 0.4785 | 0.0137 | 0.2300 | 0.2323 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 134130 | 0.0995 | 0.3329 | 0.0068 | 0.1192 | 0.1238 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 112800 | 0.1648 | 0.4976 | 0.0089 | 0.2827 | 0.2855 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 47460 | 0.1765 | 0.5295 | 0.0151 | 0.4191 | 0.4326 |
| team_total | MARKET_BASELINE | 47427 | 0.1745 | 0.5246 | 0.0161 | 0.4281 | 0.4328 |
| team_total | MARKET_ANCHORED_V1 | 47427 | 0.1746 | 0.5249 | 0.0141 | 0.4263 | 0.4328 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
