# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-21T04:19:41Z · rows 445576 · pregame 445576 · new 3540

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 78650 | 0.1605 | 0.4869 | 0.0161 | 0.4491 | 0.4567 |
| ALL | MARKET_BASELINE | 365501 | 0.1481 | 0.4558 | 0.0083 | 0.2921 | 0.2954 |
| ALL | MARKET_ANCHORED_V1 | 78632 | 0.1586 | 0.4818 | 0.0186 | 0.4545 | 0.4568 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 16126 | 0.0389 | 0.1672 | 0.0020 | 0.0404 | 0.0405 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 12584 | 0.1792 | 0.5406 | 0.0200 | 0.2314 | 0.2497 |
| game_spread | MARKET_BASELINE | 12584 | 0.1758 | 0.5311 | 0.0260 | 0.2426 | 0.2497 |
| game_spread | MARKET_ANCHORED_V1 | 12584 | 0.1761 | 0.5320 | 0.0139 | 0.2399 | 0.2497 |
| game_total | DATA_ONLY_V1 | 28314 | 0.1241 | 0.3913 | 0.0268 | 0.5675 | 0.5757 |
| game_total | MARKET_BASELINE | 28314 | 0.1227 | 0.3880 | 0.0321 | 0.5748 | 0.5757 |
| game_total | MARKET_ANCHORED_V1 | 28314 | 0.1228 | 0.3882 | 0.0300 | 0.5734 | 0.5757 |
| game_winner | DATA_ONLY_V1 | 6292 | 0.2305 | 0.6535 | 0.1053 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6292 | 0.2276 | 0.6465 | 0.0367 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6292 | 0.2275 | 0.6467 | 0.0470 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1654 | 0.2491 | 0.6916 | 0.0426 | 0.4399 | 0.4365 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 18018 | 0.1346 | 0.4393 | 0.0337 | 0.1290 | 0.1619 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 28125 | 0.1817 | 0.5407 | 0.0260 | 0.5973 | 0.6173 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 28143 | 0.2171 | 0.6250 | 0.0223 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 49926 | 0.1564 | 0.4791 | 0.0200 | 0.2379 | 0.2343 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 80264 | 0.1039 | 0.3457 | 0.0104 | 0.1262 | 0.1295 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 64613 | 0.1676 | 0.5036 | 0.0146 | 0.2968 | 0.2929 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 31460 | 0.1718 | 0.5180 | 0.0169 | 0.4194 | 0.4238 |
| team_total | MARKET_BASELINE | 31442 | 0.1698 | 0.5128 | 0.0192 | 0.4257 | 0.4240 |
| team_total | MARKET_ANCHORED_V1 | 31442 | 0.1699 | 0.5131 | 0.0202 | 0.4244 | 0.4240 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
