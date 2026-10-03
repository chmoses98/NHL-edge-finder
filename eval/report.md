# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-03T01:42:03Z · rows 47133 · pregame 47133 · new 2500

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 8450 | 0.2007 | 0.5920 | 0.0658 | 0.4468 | 0.4852 |
| ALL | MARKET_BASELINE | 40448 | 0.1587 | 0.4835 | 0.0216 | 0.2879 | 0.2962 |
| ALL | MARKET_ANCHORED_V1 | 8450 | 0.1976 | 0.5838 | 0.0581 | 0.4524 | 0.4852 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 2741 | 0.0292 | 0.1358 | 0.0038 | 0.0337 | 0.0299 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 1352 | 0.1983 | 0.5813 | 0.0789 | 0.2303 | 0.2959 |
| game_spread | MARKET_BASELINE | 1352 | 0.1939 | 0.5708 | 0.1092 | 0.2418 | 0.2959 |
| game_spread | MARKET_ANCHORED_V1 | 1352 | 0.1943 | 0.5718 | 0.1077 | 0.2390 | 0.2959 |
| game_total | DATA_ONLY_V1 | 3042 | 0.1658 | 0.5078 | 0.0577 | 0.5645 | 0.5865 |
| game_total | MARKET_BASELINE | 3042 | 0.1615 | 0.4944 | 0.0562 | 0.5715 | 0.5865 |
| game_total | MARKET_ANCHORED_V1 | 3042 | 0.1623 | 0.4967 | 0.0564 | 0.5701 | 0.5865 |
| game_winner | DATA_ONLY_V1 | 676 | 0.2363 | 0.6656 | 0.0959 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 676 | 0.2330 | 0.6588 | 0.2961 | 0.4999 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 676 | 0.2331 | 0.6590 | 0.2538 | 0.4999 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 179 | 0.2588 | 0.7115 | 0.1418 | 0.3786 | 0.4358 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 1925 | 0.1623 | 0.5130 | 0.0910 | 0.1294 | 0.1964 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 3027 | 0.1906 | 0.5619 | 0.0404 | 0.5933 | 0.6313 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 3030 | 0.2145 | 0.6189 | 0.0553 | 0.3290 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 5727 | 0.1512 | 0.4647 | 0.0498 | 0.2306 | 0.2144 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 8474 | 0.1178 | 0.3865 | 0.0249 | 0.1371 | 0.1447 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 6895 | 0.1776 | 0.5267 | 0.0577 | 0.3085 | 0.2853 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 3380 | 0.2259 | 0.6574 | 0.0953 | 0.4168 | 0.4669 |
| team_total | MARKET_BASELINE | 3380 | 0.2232 | 0.6516 | 0.1306 | 0.4237 | 0.4669 |
| team_total | MARKET_ANCHORED_V1 | 3380 | 0.2235 | 0.6520 | 0.1182 | 0.4222 | 0.4669 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
