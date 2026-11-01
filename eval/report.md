# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-01T03:15:37Z · rows 772641 · pregame 772641 · new 5603

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 127475 | 0.1659 | 0.4996 | 0.0194 | 0.4495 | 0.4689 |
| ALL | MARKET_BASELINE | 662277 | 0.1439 | 0.4443 | 0.0107 | 0.2740 | 0.2832 |
| ALL | MARKET_ANCHORED_V1 | 127442 | 0.1635 | 0.4935 | 0.0141 | 0.4564 | 0.4691 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 46223 | 0.0344 | 0.1497 | 0.0021 | 0.0346 | 0.0359 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 20396 | 0.1825 | 0.5488 | 0.0235 | 0.2311 | 0.2535 |
| game_spread | MARKET_BASELINE | 20396 | 0.1779 | 0.5361 | 0.0152 | 0.2431 | 0.2535 |
| game_spread | MARKET_ANCHORED_V1 | 20396 | 0.1785 | 0.5377 | 0.0149 | 0.2402 | 0.2535 |
| game_total | DATA_ONLY_V1 | 45891 | 0.1303 | 0.4058 | 0.0273 | 0.5681 | 0.5900 |
| game_total | MARKET_BASELINE | 45891 | 0.1288 | 0.4018 | 0.0226 | 0.5776 | 0.5900 |
| game_total | MARKET_ANCHORED_V1 | 45891 | 0.1290 | 0.4021 | 0.0220 | 0.5757 | 0.5900 |
| game_winner | DATA_ONLY_V1 | 10198 | 0.2332 | 0.6591 | 0.0793 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10198 | 0.2287 | 0.6492 | 0.0275 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10198 | 0.2290 | 0.6500 | 0.0422 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2971 | 0.2487 | 0.6910 | 0.0370 | 0.4459 | 0.4396 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 29172 | 0.1324 | 0.4352 | 0.0301 | 0.1284 | 0.1581 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 45681 | 0.1796 | 0.5347 | 0.0253 | 0.5993 | 0.6245 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 45720 | 0.2168 | 0.6243 | 0.0250 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 94550 | 0.1569 | 0.4800 | 0.0165 | 0.2293 | 0.2350 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 146563 | 0.1009 | 0.3367 | 0.0081 | 0.1191 | 0.1260 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 123955 | 0.1661 | 0.5009 | 0.0123 | 0.2815 | 0.2887 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 50990 | 0.1778 | 0.5326 | 0.0215 | 0.4200 | 0.4399 |
| team_total | MARKET_BASELINE | 50957 | 0.1751 | 0.5261 | 0.0177 | 0.4285 | 0.4402 |
| team_total | MARKET_ANCHORED_V1 | 50957 | 0.1754 | 0.5267 | 0.0158 | 0.4268 | 0.4402 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
