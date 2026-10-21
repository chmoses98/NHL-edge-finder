# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-21T02:07:36Z · rows 435121 · pregame 435121 · new 16656

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 76975 | 0.1616 | 0.4896 | 0.0167 | 0.4495 | 0.4596 |
| ALL | MARKET_BASELINE | 357133 | 0.1486 | 0.4572 | 0.0086 | 0.2924 | 0.2966 |
| ALL | MARKET_ANCHORED_V1 | 76957 | 0.1596 | 0.4844 | 0.0175 | 0.4548 | 0.4597 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 15811 | 0.0390 | 0.1677 | 0.0024 | 0.0403 | 0.0407 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 12316 | 0.1819 | 0.5467 | 0.0253 | 0.2315 | 0.2551 |
| game_spread | MARKET_BASELINE | 12316 | 0.1783 | 0.5367 | 0.0280 | 0.2427 | 0.2551 |
| game_spread | MARKET_ANCHORED_V1 | 12316 | 0.1787 | 0.5377 | 0.0193 | 0.2400 | 0.2551 |
| game_total | DATA_ONLY_V1 | 27711 | 0.1245 | 0.3923 | 0.0271 | 0.5680 | 0.5785 |
| game_total | MARKET_BASELINE | 27711 | 0.1230 | 0.3886 | 0.0318 | 0.5751 | 0.5785 |
| game_total | MARKET_ANCHORED_V1 | 27711 | 0.1231 | 0.3889 | 0.0298 | 0.5737 | 0.5785 |
| game_winner | DATA_ONLY_V1 | 6158 | 0.2313 | 0.6550 | 0.0980 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6158 | 0.2285 | 0.6484 | 0.0422 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6158 | 0.2284 | 0.6485 | 0.0386 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1607 | 0.2493 | 0.6920 | 0.0440 | 0.4401 | 0.4306 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 17616 | 0.1354 | 0.4415 | 0.0346 | 0.1292 | 0.1630 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 27522 | 0.1826 | 0.5426 | 0.0287 | 0.5975 | 0.6202 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 27540 | 0.2170 | 0.6246 | 0.0232 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 48665 | 0.1567 | 0.4799 | 0.0191 | 0.2382 | 0.2346 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 78446 | 0.1043 | 0.3470 | 0.0104 | 0.1263 | 0.1301 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 62969 | 0.1681 | 0.5050 | 0.0134 | 0.2972 | 0.2932 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 30790 | 0.1731 | 0.5212 | 0.0178 | 0.4198 | 0.4264 |
| team_total | MARKET_BASELINE | 30772 | 0.1710 | 0.5157 | 0.0193 | 0.4260 | 0.4266 |
| team_total | MARKET_ANCHORED_V1 | 30772 | 0.1711 | 0.5161 | 0.0205 | 0.4247 | 0.4266 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
