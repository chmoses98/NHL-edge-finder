# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-01T03:35:01Z · rows 18929 · pregame 18929 · new 5674

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 2825 | 0.2072 | 0.6133 | 0.0882 | 0.4536 | 0.4042 |
| ALL | MARKET_BASELINE | 15703 | 0.1446 | 0.4493 | 0.0553 | 0.2692 | 0.2234 |
| ALL | MARKET_ANCHORED_V1 | 2825 | 0.2036 | 0.6038 | 0.0819 | 0.4560 | 0.4042 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 1263 | 0.0301 | 0.1453 | 0.0024 | 0.0325 | 0.0301 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 452 | 0.1855 | 0.5591 | 0.0806 | 0.2338 | 0.2345 |
| game_spread | MARKET_BASELINE | 452 | 0.1783 | 0.5382 | 0.1097 | 0.2437 | 0.2345 |
| game_spread | MARKET_ANCHORED_V1 | 452 | 0.1791 | 0.5410 | 0.0873 | 0.2411 | 0.2345 |
| game_total | DATA_ONLY_V1 | 1017 | 0.1780 | 0.5486 | 0.0952 | 0.5735 | 0.4897 |
| game_total | MARKET_BASELINE | 1017 | 0.1783 | 0.5450 | 0.1125 | 0.5739 | 0.4897 |
| game_total | MARKET_ANCHORED_V1 | 1017 | 0.1782 | 0.5455 | 0.1124 | 0.5738 | 0.4897 |
| game_winner | DATA_ONLY_V1 | 226 | 0.2914 | 0.7784 | 0.2079 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 226 | 0.2761 | 0.7499 | 0.1627 | 0.4998 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 226 | 0.2785 | 0.7537 | 0.1935 | 0.4999 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 101 | 0.2684 | 0.7320 | 0.2261 | 0.3931 | 0.4158 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 638 | 0.1517 | 0.4941 | 0.0793 | 0.1303 | 0.1740 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 1002 | 0.1991 | 0.5931 | 0.1192 | 0.5934 | 0.5369 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 1005 | 0.2284 | 0.6492 | 0.0328 | 0.3302 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 2231 | 0.1278 | 0.4106 | 0.0860 | 0.2346 | 0.1560 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 3986 | 0.0934 | 0.3211 | 0.0404 | 0.1199 | 0.1026 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 2652 | 0.1689 | 0.5048 | 0.1146 | 0.3185 | 0.2055 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 1130 | 0.2252 | 0.6601 | 0.1276 | 0.4243 | 0.3761 |
| team_total | MARKET_BASELINE | 1130 | 0.2207 | 0.6502 | 0.1349 | 0.4280 | 0.3761 |
| team_total | MARKET_ANCHORED_V1 | 1130 | 0.2214 | 0.6513 | 0.1435 | 0.4272 | 0.3761 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
