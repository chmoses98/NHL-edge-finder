# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-01T12:39:07Z · rows 778783 · pregame 778783 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 128350 | 0.1655 | 0.4987 | 0.0200 | 0.4496 | 0.4696 |
| ALL | MARKET_BASELINE | 667690 | 0.1437 | 0.4439 | 0.0111 | 0.2739 | 0.2835 |
| ALL | MARKET_ANCHORED_V1 | 128317 | 0.1629 | 0.4921 | 0.0140 | 0.4565 | 0.4697 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 46804 | 0.0344 | 0.1496 | 0.0021 | 0.0346 | 0.0360 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 20536 | 0.1825 | 0.5486 | 0.0250 | 0.2313 | 0.2552 |
| game_spread | MARKET_BASELINE | 20536 | 0.1774 | 0.5349 | 0.0168 | 0.2435 | 0.2552 |
| game_spread | MARKET_ANCHORED_V1 | 20536 | 0.1781 | 0.5367 | 0.0164 | 0.2406 | 0.2552 |
| game_total | DATA_ONLY_V1 | 46206 | 0.1299 | 0.4048 | 0.0281 | 0.5682 | 0.5905 |
| game_total | MARKET_BASELINE | 46206 | 0.1284 | 0.4007 | 0.0224 | 0.5777 | 0.5905 |
| game_total | MARKET_ANCHORED_V1 | 46206 | 0.1285 | 0.4011 | 0.0224 | 0.5759 | 0.5905 |
| game_winner | DATA_ONLY_V1 | 10268 | 0.2323 | 0.6571 | 0.0794 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10268 | 0.2275 | 0.6464 | 0.0288 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10268 | 0.2278 | 0.6474 | 0.0435 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2989 | 0.2488 | 0.6912 | 0.0346 | 0.4462 | 0.4430 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 29368 | 0.1323 | 0.4346 | 0.0300 | 0.1286 | 0.1581 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 45990 | 0.1793 | 0.5342 | 0.0256 | 0.5994 | 0.6247 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 46035 | 0.2166 | 0.6239 | 0.0250 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 95352 | 0.1570 | 0.4806 | 0.0173 | 0.2294 | 0.2356 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 147809 | 0.1008 | 0.3365 | 0.0080 | 0.1192 | 0.1261 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 125026 | 0.1661 | 0.5009 | 0.0130 | 0.2816 | 0.2894 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 51340 | 0.1773 | 0.5315 | 0.0219 | 0.4201 | 0.4404 |
| team_total | MARKET_BASELINE | 51307 | 0.1745 | 0.5246 | 0.0179 | 0.4286 | 0.4406 |
| team_total | MARKET_ANCHORED_V1 | 51307 | 0.1748 | 0.5253 | 0.0158 | 0.4269 | 0.4406 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
