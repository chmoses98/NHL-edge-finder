# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-07T02:51:19Z · rows 134662 · pregame 134662 · new 3229

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 25625 | 0.1678 | 0.5050 | 0.0133 | 0.4491 | 0.4624 |
| ALL | MARKET_BASELINE | 114689 | 0.1548 | 0.4745 | 0.0139 | 0.2974 | 0.3075 |
| ALL | MARKET_ANCHORED_V1 | 25625 | 0.1665 | 0.5016 | 0.0132 | 0.4527 | 0.4624 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 6423 | 0.0404 | 0.1737 | 0.0084 | 0.0363 | 0.0422 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 4100 | 0.1767 | 0.5319 | 0.0335 | 0.2309 | 0.2566 |
| game_spread | MARKET_BASELINE | 4100 | 0.1758 | 0.5301 | 0.0384 | 0.2409 | 0.2566 |
| game_spread | MARKET_ANCHORED_V1 | 4100 | 0.1756 | 0.5295 | 0.0288 | 0.2384 | 0.2566 |
| game_total | DATA_ONLY_V1 | 9225 | 0.1300 | 0.4064 | 0.0278 | 0.5676 | 0.5734 |
| game_total | MARKET_BASELINE | 9225 | 0.1273 | 0.3991 | 0.0265 | 0.5718 | 0.5734 |
| game_total | MARKET_ANCHORED_V1 | 9225 | 0.1277 | 0.4002 | 0.0262 | 0.5710 | 0.5734 |
| game_winner | DATA_ONLY_V1 | 2050 | 0.2274 | 0.6473 | 0.1069 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2050 | 0.2308 | 0.6533 | 0.0926 | 0.4996 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2050 | 0.2295 | 0.6508 | 0.0702 | 0.4997 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 446 | 0.2531 | 0.6998 | 0.0864 | 0.3989 | 0.4731 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 5832 | 0.1572 | 0.4982 | 0.0646 | 0.1308 | 0.1931 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 9170 | 0.1797 | 0.5355 | 0.0260 | 0.5936 | 0.6154 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 9213 | 0.2152 | 0.6208 | 0.0356 | 0.3282 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 15511 | 0.1589 | 0.4852 | 0.0157 | 0.2362 | 0.2431 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 23725 | 0.1180 | 0.3869 | 0.0113 | 0.1427 | 0.1483 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 18744 | 0.1763 | 0.5278 | 0.0231 | 0.3089 | 0.3100 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 10250 | 0.1863 | 0.5544 | 0.0305 | 0.4195 | 0.4374 |
| team_total | MARKET_BASELINE | 10250 | 0.1853 | 0.5522 | 0.0390 | 0.4234 | 0.4374 |
| team_total | MARKET_ANCHORED_V1 | 10250 | 0.1852 | 0.5519 | 0.0347 | 0.4225 | 0.4374 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
