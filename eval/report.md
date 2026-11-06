# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-06T08:17:31Z · rows 899436 · pregame 899436 · new 36601

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 147350 | 0.1660 | 0.4997 | 0.0197 | 0.4507 | 0.4704 |
| ALL | MARKET_BASELINE | 777593 | 0.1432 | 0.4425 | 0.0115 | 0.2719 | 0.2819 |
| ALL | MARKET_ANCHORED_V1 | 147317 | 0.1635 | 0.4932 | 0.0133 | 0.4572 | 0.4705 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 59365 | 0.0337 | 0.1475 | 0.0022 | 0.0337 | 0.0352 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 23576 | 0.1797 | 0.5421 | 0.0195 | 0.2318 | 0.2510 |
| game_spread | MARKET_BASELINE | 23576 | 0.1751 | 0.5298 | 0.0178 | 0.2438 | 0.2510 |
| game_spread | MARKET_ANCHORED_V1 | 23576 | 0.1757 | 0.5313 | 0.0132 | 0.2410 | 0.2510 |
| game_total | DATA_ONLY_V1 | 53046 | 0.1319 | 0.4087 | 0.0289 | 0.5697 | 0.5935 |
| game_total | MARKET_BASELINE | 53046 | 0.1303 | 0.4043 | 0.0222 | 0.5784 | 0.5935 |
| game_total | MARKET_ANCHORED_V1 | 53046 | 0.1305 | 0.4047 | 0.0238 | 0.5767 | 0.5935 |
| game_winner | DATA_ONLY_V1 | 11788 | 0.2330 | 0.6584 | 0.0681 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 11788 | 0.2280 | 0.6473 | 0.0244 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 11788 | 0.2284 | 0.6483 | 0.0310 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3508 | 0.2479 | 0.6894 | 0.0180 | 0.4486 | 0.4518 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 33730 | 0.1329 | 0.4362 | 0.0302 | 0.1289 | 0.1587 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 52825 | 0.1793 | 0.5343 | 0.0270 | 0.6002 | 0.6263 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 52875 | 0.2167 | 0.6240 | 0.0220 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 110710 | 0.1581 | 0.4832 | 0.0194 | 0.2297 | 0.2383 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 171490 | 0.1009 | 0.3373 | 0.0091 | 0.1189 | 0.1257 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 145773 | 0.1662 | 0.5016 | 0.0141 | 0.2811 | 0.2895 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 58940 | 0.1777 | 0.5328 | 0.0219 | 0.4213 | 0.4414 |
| team_total | MARKET_BASELINE | 58907 | 0.1750 | 0.5259 | 0.0159 | 0.4292 | 0.4416 |
| team_total | MARKET_ANCHORED_V1 | 58907 | 0.1753 | 0.5266 | 0.0162 | 0.4275 | 0.4416 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
