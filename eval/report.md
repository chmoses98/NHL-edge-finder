# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-24T03:10:41Z · rows 512186 · pregame 512186 · new 4030

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 89475 | 0.1616 | 0.4890 | 0.0177 | 0.4489 | 0.4618 |
| ALL | MARKET_BASELINE | 420797 | 0.1481 | 0.4559 | 0.0079 | 0.2904 | 0.2950 |
| ALL | MARKET_ANCHORED_V1 | 89450 | 0.1602 | 0.4852 | 0.0147 | 0.4549 | 0.4619 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 18349 | 0.0397 | 0.1691 | 0.0027 | 0.0408 | 0.0416 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 14316 | 0.1821 | 0.5468 | 0.0266 | 0.2312 | 0.2561 |
| game_spread | MARKET_BASELINE | 14316 | 0.1789 | 0.5378 | 0.0250 | 0.2428 | 0.2561 |
| game_spread | MARKET_ANCHORED_V1 | 14316 | 0.1792 | 0.5386 | 0.0203 | 0.2400 | 0.2561 |
| game_total | DATA_ONLY_V1 | 32211 | 0.1234 | 0.3887 | 0.0297 | 0.5673 | 0.5806 |
| game_total | MARKET_BASELINE | 32211 | 0.1227 | 0.3867 | 0.0288 | 0.5754 | 0.5806 |
| game_total | MARKET_ANCHORED_V1 | 32211 | 0.1226 | 0.3866 | 0.0277 | 0.5738 | 0.5806 |
| game_winner | DATA_ONLY_V1 | 7158 | 0.2313 | 0.6551 | 0.0983 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7158 | 0.2298 | 0.6511 | 0.0337 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7158 | 0.2295 | 0.6507 | 0.0297 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1939 | 0.2506 | 0.6946 | 0.0572 | 0.4442 | 0.4399 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 20453 | 0.1376 | 0.4483 | 0.0387 | 0.1286 | 0.1656 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 32022 | 0.1797 | 0.5356 | 0.0271 | 0.5979 | 0.6220 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 32040 | 0.2170 | 0.6248 | 0.0216 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 58824 | 0.1550 | 0.4753 | 0.0199 | 0.2342 | 0.2296 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 91366 | 0.1032 | 0.3437 | 0.0081 | 0.1254 | 0.1288 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 76354 | 0.1667 | 0.5017 | 0.0118 | 0.2914 | 0.2872 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 35790 | 0.1738 | 0.5228 | 0.0119 | 0.4193 | 0.4294 |
| team_total | MARKET_BASELINE | 35765 | 0.1724 | 0.5196 | 0.0151 | 0.4263 | 0.4297 |
| team_total | MARKET_ANCHORED_V1 | 35765 | 0.1724 | 0.5195 | 0.0168 | 0.4248 | 0.4297 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
