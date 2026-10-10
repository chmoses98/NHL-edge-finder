# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-10T02:02:50Z · rows 192280 · pregame 192280 · new 9404

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 36000 | 0.1667 | 0.5019 | 0.0134 | 0.4505 | 0.4604 |
| ALL | MARKET_BASELINE | 163950 | 0.1498 | 0.4607 | 0.0107 | 0.2912 | 0.2968 |
| ALL | MARKET_ANCHORED_V1 | 35986 | 0.1640 | 0.4947 | 0.0122 | 0.4534 | 0.4605 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 8981 | 0.0394 | 0.1696 | 0.0059 | 0.0373 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5760 | 0.1825 | 0.5463 | 0.0372 | 0.2315 | 0.2620 |
| game_spread | MARKET_BASELINE | 5760 | 0.1771 | 0.5330 | 0.0355 | 0.2414 | 0.2620 |
| game_spread | MARKET_ANCHORED_V1 | 5760 | 0.1778 | 0.5347 | 0.0293 | 0.2389 | 0.2620 |
| game_total | DATA_ONLY_V1 | 12960 | 0.1281 | 0.4005 | 0.0213 | 0.5695 | 0.5737 |
| game_total | MARKET_BASELINE | 12960 | 0.1257 | 0.3930 | 0.0252 | 0.5722 | 0.5737 |
| game_total | MARKET_ANCHORED_V1 | 12960 | 0.1260 | 0.3941 | 0.0243 | 0.5717 | 0.5737 |
| game_winner | DATA_ONLY_V1 | 2880 | 0.2308 | 0.6538 | 0.0806 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2880 | 0.2283 | 0.6480 | 0.0602 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2880 | 0.2282 | 0.6479 | 0.0355 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 636 | 0.2525 | 0.6990 | 0.0670 | 0.4170 | 0.4450 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 8206 | 0.1511 | 0.4827 | 0.0549 | 0.1309 | 0.1841 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 12771 | 0.1810 | 0.5396 | 0.0319 | 0.5948 | 0.6140 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 12789 | 0.2167 | 0.6242 | 0.0251 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 21659 | 0.1547 | 0.4750 | 0.0172 | 0.2354 | 0.2320 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 36270 | 0.1083 | 0.3593 | 0.0092 | 0.1302 | 0.1347 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 26652 | 0.1708 | 0.5121 | 0.0186 | 0.3042 | 0.2966 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 14400 | 0.1824 | 0.5451 | 0.0239 | 0.4211 | 0.4299 |
| team_total | MARKET_BASELINE | 14386 | 0.1796 | 0.5380 | 0.0335 | 0.4240 | 0.4302 |
| team_total | MARKET_ANCHORED_V1 | 14386 | 0.1799 | 0.5388 | 0.0276 | 0.4234 | 0.4302 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
