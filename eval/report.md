# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-08T18:34:47Z · rows 153943 · pregame 153943 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 29050 | 0.1667 | 0.5017 | 0.0122 | 0.4501 | 0.4611 |
| ALL | MARKET_BASELINE | 130847 | 0.1534 | 0.4702 | 0.0106 | 0.2958 | 0.3044 |
| ALL | MARKET_ANCHORED_V1 | 29050 | 0.1648 | 0.4967 | 0.0097 | 0.4535 | 0.4611 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 7448 | 0.0406 | 0.1736 | 0.0081 | 0.0366 | 0.0424 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4648 | 0.1773 | 0.5335 | 0.0322 | 0.2310 | 0.2562 |
| game_spread | MARKET_BASELINE | 4648 | 0.1746 | 0.5265 | 0.0229 | 0.2411 | 0.2562 |
| game_spread | MARKET_ANCHORED_V1 | 4648 | 0.1747 | 0.5269 | 0.0369 | 0.2386 | 0.2562 |
| game_total | DATA_ONLY_V1 | 10458 | 0.1277 | 0.4001 | 0.0273 | 0.5690 | 0.5731 |
| game_total | MARKET_BASELINE | 10458 | 0.1255 | 0.3938 | 0.0258 | 0.5730 | 0.5731 |
| game_total | MARKET_ANCHORED_V1 | 10458 | 0.1258 | 0.3947 | 0.0263 | 0.5722 | 0.5731 |
| game_winner | DATA_ONLY_V1 | 2324 | 0.2326 | 0.6577 | 0.0812 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2324 | 0.2322 | 0.6564 | 0.0619 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2324 | 0.2316 | 0.6553 | 0.0332 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 499 | 0.2546 | 0.7030 | 0.0904 | 0.4042 | 0.4569 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 6641 | 0.1535 | 0.4890 | 0.0589 | 0.1306 | 0.1873 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 10403 | 0.1807 | 0.5379 | 0.0310 | 0.5946 | 0.6166 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 10446 | 0.2160 | 0.6227 | 0.0322 | 0.3283 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 17452 | 0.1591 | 0.4857 | 0.0152 | 0.2374 | 0.2404 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 27667 | 0.1148 | 0.3770 | 0.0079 | 0.1387 | 0.1447 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 21241 | 0.1768 | 0.5280 | 0.0188 | 0.3092 | 0.3086 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 11620 | 0.1843 | 0.5492 | 0.0239 | 0.4208 | 0.4345 |
| team_total | MARKET_BASELINE | 11620 | 0.1824 | 0.5443 | 0.0291 | 0.4244 | 0.4345 |
| team_total | MARKET_ANCHORED_V1 | 11620 | 0.1825 | 0.5446 | 0.0257 | 0.4236 | 0.4345 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
