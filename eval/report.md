# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-12T16:58:01Z · rows 249379 · pregame 249379 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 45200 | 0.1684 | 0.5064 | 0.0107 | 0.4507 | 0.4528 |
| ALL | MARKET_BASELINE | 207992 | 0.1495 | 0.4597 | 0.0088 | 0.2912 | 0.2918 |
| ALL | MARKET_ANCHORED_V1 | 45186 | 0.1651 | 0.4981 | 0.0105 | 0.4534 | 0.4529 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10132 | 0.0397 | 0.1701 | 0.0053 | 0.0383 | 0.0415 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7232 | 0.1876 | 0.5588 | 0.0446 | 0.2318 | 0.2717 |
| game_spread | MARKET_BASELINE | 7232 | 0.1810 | 0.5418 | 0.0365 | 0.2420 | 0.2717 |
| game_spread | MARKET_ANCHORED_V1 | 7232 | 0.1819 | 0.5442 | 0.0354 | 0.2395 | 0.2717 |
| game_total | DATA_ONLY_V1 | 16272 | 0.1303 | 0.4080 | 0.0226 | 0.5697 | 0.5618 |
| game_total | MARKET_BASELINE | 16272 | 0.1277 | 0.4008 | 0.0270 | 0.5723 | 0.5618 |
| game_total | MARKET_ANCHORED_V1 | 16272 | 0.1281 | 0.4018 | 0.0267 | 0.5718 | 0.5618 |
| game_winner | DATA_ONLY_V1 | 3616 | 0.2299 | 0.6525 | 0.1096 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3616 | 0.2252 | 0.6417 | 0.0480 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3616 | 0.2255 | 0.6426 | 0.0413 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 785 | 0.2521 | 0.6987 | 0.0966 | 0.4227 | 0.4140 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10337 | 0.1481 | 0.4756 | 0.0504 | 0.1306 | 0.1796 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 16083 | 0.1854 | 0.5508 | 0.0249 | 0.5948 | 0.6025 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 16101 | 0.2167 | 0.6242 | 0.0239 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 28159 | 0.1527 | 0.4698 | 0.0208 | 0.2356 | 0.2276 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 46141 | 0.1056 | 0.3509 | 0.0095 | 0.1291 | 0.1310 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 35068 | 0.1675 | 0.5035 | 0.0169 | 0.3004 | 0.2882 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 18080 | 0.1826 | 0.5448 | 0.0344 | 0.4212 | 0.4176 |
| team_total | MARKET_BASELINE | 18066 | 0.1792 | 0.5365 | 0.0301 | 0.4239 | 0.4179 |
| team_total | MARKET_ANCHORED_V1 | 18066 | 0.1797 | 0.5375 | 0.0298 | 0.4233 | 0.4179 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
