# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-04T11:52:26Z · rows 92313 · pregame 92313 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 17625 | 0.1767 | 0.5281 | 0.0237 | 0.4477 | 0.4603 |
| ALL | MARKET_BASELINE | 78799 | 0.1583 | 0.4829 | 0.0149 | 0.2986 | 0.3068 |
| ALL | MARKET_ANCHORED_V1 | 17625 | 0.1764 | 0.5275 | 0.0265 | 0.4536 | 0.4603 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4533 | 0.0338 | 0.1512 | 0.0027 | 0.0354 | 0.0349 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 2820 | 0.1833 | 0.5486 | 0.0440 | 0.2307 | 0.2652 |
| game_spread | MARKET_BASELINE | 2820 | 0.1833 | 0.5504 | 0.0757 | 0.2416 | 0.2652 |
| game_spread | MARKET_ANCHORED_V1 | 2820 | 0.1829 | 0.5491 | 0.0639 | 0.2390 | 0.2652 |
| game_total | DATA_ONLY_V1 | 6345 | 0.1390 | 0.4311 | 0.0164 | 0.5656 | 0.5649 |
| game_total | MARKET_BASELINE | 6345 | 0.1363 | 0.4239 | 0.0244 | 0.5735 | 0.5649 |
| game_total | MARKET_ANCHORED_V1 | 6345 | 0.1367 | 0.4249 | 0.0228 | 0.5720 | 0.5649 |
| game_winner | DATA_ONLY_V1 | 1410 | 0.2278 | 0.6478 | 0.0935 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1410 | 0.2375 | 0.6671 | 0.1562 | 0.4998 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1410 | 0.2351 | 0.6621 | 0.1479 | 0.4999 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 310 | 0.2595 | 0.7133 | 0.1051 | 0.3933 | 0.4871 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 4064 | 0.1602 | 0.5031 | 0.0674 | 0.1321 | 0.1996 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 6330 | 0.1842 | 0.5460 | 0.0215 | 0.5948 | 0.6163 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 6333 | 0.2160 | 0.6225 | 0.0377 | 0.3278 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 10981 | 0.1575 | 0.4817 | 0.0231 | 0.2321 | 0.2350 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 15958 | 0.1220 | 0.3996 | 0.0215 | 0.1455 | 0.1513 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 12665 | 0.1787 | 0.5309 | 0.0347 | 0.3137 | 0.3109 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 7050 | 0.1978 | 0.5832 | 0.0475 | 0.4178 | 0.4362 |
| team_total | MARKET_BASELINE | 7050 | 0.1982 | 0.5855 | 0.0786 | 0.4253 | 0.4362 |
| team_total | MARKET_ANCHORED_V1 | 7050 | 0.1979 | 0.5844 | 0.0700 | 0.4237 | 0.4362 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
