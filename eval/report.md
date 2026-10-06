# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-06T06:56:50Z · rows 116606 · pregame 116606 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 22450 | 0.1685 | 0.5070 | 0.0115 | 0.4492 | 0.4458 |
| ALL | MARKET_BASELINE | 99561 | 0.1544 | 0.4735 | 0.0150 | 0.3002 | 0.2994 |
| ALL | MARKET_ANCHORED_V1 | 22450 | 0.1669 | 0.5030 | 0.0178 | 0.4532 | 0.4458 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 5531 | 0.0376 | 0.1643 | 0.0059 | 0.0360 | 0.0391 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 3592 | 0.1818 | 0.5444 | 0.0404 | 0.2311 | 0.2631 |
| game_spread | MARKET_BASELINE | 3592 | 0.1795 | 0.5391 | 0.0542 | 0.2415 | 0.2631 |
| game_spread | MARKET_ANCHORED_V1 | 3592 | 0.1795 | 0.5392 | 0.0482 | 0.2389 | 0.2631 |
| game_total | DATA_ONLY_V1 | 8082 | 0.1268 | 0.3995 | 0.0381 | 0.5676 | 0.5473 |
| game_total | MARKET_BASELINE | 8082 | 0.1238 | 0.3919 | 0.0419 | 0.5726 | 0.5473 |
| game_total | MARKET_ANCHORED_V1 | 8082 | 0.1243 | 0.3930 | 0.0408 | 0.5716 | 0.5473 |
| game_winner | DATA_ONLY_V1 | 1796 | 0.2275 | 0.6474 | 0.0981 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1796 | 0.2316 | 0.6547 | 0.1109 | 0.4997 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1796 | 0.2301 | 0.6520 | 0.1127 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 391 | 0.2544 | 0.7026 | 0.0935 | 0.3923 | 0.4604 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 5070 | 0.1599 | 0.5046 | 0.0675 | 0.1323 | 0.1970 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 8027 | 0.1815 | 0.5400 | 0.0246 | 0.5939 | 0.6002 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 8070 | 0.2149 | 0.6202 | 0.0393 | 0.3279 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 13739 | 0.1532 | 0.4711 | 0.0177 | 0.2348 | 0.2267 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 19957 | 0.1200 | 0.3937 | 0.0161 | 0.1476 | 0.1490 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 16326 | 0.1724 | 0.5172 | 0.0275 | 0.3109 | 0.2946 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 8980 | 0.1889 | 0.5607 | 0.0342 | 0.4196 | 0.4168 |
| team_total | MARKET_BASELINE | 8980 | 0.1875 | 0.5580 | 0.0515 | 0.4241 | 0.4168 |
| team_total | MARKET_ANCHORED_V1 | 8980 | 0.1875 | 0.5579 | 0.0452 | 0.4231 | 0.4168 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
