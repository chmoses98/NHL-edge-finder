# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-28T09:17:33Z · rows 665984 · pregame 665984 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 111675 | 0.1665 | 0.5015 | 0.0152 | 0.4491 | 0.4618 |
| ALL | MARKET_BASELINE | 564574 | 0.1450 | 0.4473 | 0.0079 | 0.2784 | 0.2836 |
| ALL | MARKET_ANCHORED_V1 | 111650 | 0.1646 | 0.4965 | 0.0113 | 0.4558 | 0.4619 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 34581 | 0.0355 | 0.1545 | 0.0017 | 0.0361 | 0.0370 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 17868 | 0.1846 | 0.5542 | 0.0266 | 0.2309 | 0.2564 |
| game_spread | MARKET_BASELINE | 17868 | 0.1806 | 0.5429 | 0.0190 | 0.2428 | 0.2564 |
| game_spread | MARKET_ANCHORED_V1 | 17868 | 0.1811 | 0.5442 | 0.0171 | 0.2399 | 0.2564 |
| game_total | DATA_ONLY_V1 | 40203 | 0.1302 | 0.4060 | 0.0224 | 0.5676 | 0.5803 |
| game_total | MARKET_BASELINE | 40203 | 0.1292 | 0.4035 | 0.0225 | 0.5769 | 0.5803 |
| game_total | MARKET_ANCHORED_V1 | 40203 | 0.1293 | 0.4036 | 0.0201 | 0.5750 | 0.5803 |
| game_winner | DATA_ONLY_V1 | 8934 | 0.2363 | 0.6654 | 0.0741 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8934 | 0.2321 | 0.6560 | 0.0201 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8934 | 0.2323 | 0.6567 | 0.0276 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2599 | 0.2504 | 0.6946 | 0.0334 | 0.4456 | 0.4506 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 25561 | 0.1342 | 0.4403 | 0.0322 | 0.1287 | 0.1603 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 40014 | 0.1827 | 0.5424 | 0.0223 | 0.5994 | 0.6160 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 40032 | 0.2174 | 0.6256 | 0.0209 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 80294 | 0.1557 | 0.4772 | 0.0125 | 0.2307 | 0.2318 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 124772 | 0.0996 | 0.3327 | 0.0062 | 0.1200 | 0.1240 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 105071 | 0.1644 | 0.4962 | 0.0071 | 0.2836 | 0.2847 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 44670 | 0.1780 | 0.5336 | 0.0166 | 0.4195 | 0.4297 |
| team_total | MARKET_BASELINE | 44645 | 0.1761 | 0.5288 | 0.0174 | 0.4279 | 0.4299 |
| team_total | MARKET_ANCHORED_V1 | 44645 | 0.1762 | 0.5291 | 0.0144 | 0.4261 | 0.4299 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
