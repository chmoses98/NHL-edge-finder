# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-25T03:07:10Z · rows 562448 · pregame 562448 · new 38651

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 96400 | 0.1639 | 0.4948 | 0.0176 | 0.4498 | 0.4658 |
| ALL | MARKET_BASELINE | 466022 | 0.1483 | 0.4561 | 0.0089 | 0.2865 | 0.2942 |
| ALL | MARKET_ANCHORED_V1 | 96375 | 0.1620 | 0.4898 | 0.0146 | 0.4556 | 0.4659 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 22825 | 0.0390 | 0.1676 | 0.0033 | 0.0390 | 0.0407 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 15424 | 0.1831 | 0.5498 | 0.0268 | 0.2315 | 0.2564 |
| game_spread | MARKET_BASELINE | 15424 | 0.1789 | 0.5382 | 0.0202 | 0.2427 | 0.2564 |
| game_spread | MARKET_ANCHORED_V1 | 15424 | 0.1794 | 0.5395 | 0.0202 | 0.2400 | 0.2564 |
| game_total | DATA_ONLY_V1 | 34704 | 0.1273 | 0.3979 | 0.0277 | 0.5685 | 0.5864 |
| game_total | MARKET_BASELINE | 34704 | 0.1263 | 0.3951 | 0.0260 | 0.5763 | 0.5864 |
| game_total | MARKET_ANCHORED_V1 | 34704 | 0.1263 | 0.3952 | 0.0257 | 0.5748 | 0.5864 |
| game_winner | DATA_ONLY_V1 | 7712 | 0.2323 | 0.6571 | 0.0870 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7712 | 0.2295 | 0.6505 | 0.0257 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7712 | 0.2294 | 0.6506 | 0.0387 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2148 | 0.2530 | 0.6996 | 0.0556 | 0.4440 | 0.4507 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 22034 | 0.1372 | 0.4469 | 0.0370 | 0.1288 | 0.1651 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 34515 | 0.1801 | 0.5366 | 0.0257 | 0.5987 | 0.6230 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 34533 | 0.2171 | 0.6249 | 0.0217 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 66027 | 0.1575 | 0.4814 | 0.0143 | 0.2329 | 0.2342 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 101766 | 0.1035 | 0.3442 | 0.0071 | 0.1241 | 0.1295 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 85799 | 0.1678 | 0.5045 | 0.0094 | 0.2889 | 0.2914 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 38560 | 0.1756 | 0.5275 | 0.0157 | 0.4203 | 0.4342 |
| team_total | MARKET_BASELINE | 38535 | 0.1736 | 0.5226 | 0.0204 | 0.4272 | 0.4344 |
| team_total | MARKET_ANCHORED_V1 | 38535 | 0.1737 | 0.5229 | 0.0187 | 0.4258 | 0.4344 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
