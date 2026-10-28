# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-28T03:14:01Z · rows 646039 · pregame 646039 · new 26765

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 108725 | 0.1654 | 0.4984 | 0.0162 | 0.4483 | 0.4634 |
| ALL | MARKET_BASELINE | 545094 | 0.1457 | 0.4490 | 0.0085 | 0.2797 | 0.2864 |
| ALL | MARKET_ANCHORED_V1 | 108700 | 0.1633 | 0.4930 | 0.0122 | 0.4552 | 0.4635 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 32222 | 0.0358 | 0.1552 | 0.0017 | 0.0366 | 0.0374 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 17396 | 0.1851 | 0.5558 | 0.0271 | 0.2307 | 0.2566 |
| game_spread | MARKET_BASELINE | 17396 | 0.1811 | 0.5443 | 0.0219 | 0.2427 | 0.2566 |
| game_spread | MARKET_ANCHORED_V1 | 17396 | 0.1816 | 0.5456 | 0.0174 | 0.2398 | 0.2566 |
| game_total | DATA_ONLY_V1 | 39141 | 0.1280 | 0.3997 | 0.0273 | 0.5665 | 0.5832 |
| game_total | MARKET_BASELINE | 39141 | 0.1268 | 0.3966 | 0.0255 | 0.5760 | 0.5832 |
| game_total | MARKET_ANCHORED_V1 | 39141 | 0.1269 | 0.3968 | 0.0237 | 0.5741 | 0.5832 |
| game_winner | DATA_ONLY_V1 | 8698 | 0.2354 | 0.6635 | 0.0777 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8698 | 0.2311 | 0.6541 | 0.0273 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8698 | 0.2314 | 0.6547 | 0.0302 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2503 | 0.2514 | 0.6966 | 0.0419 | 0.4453 | 0.4459 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 24853 | 0.1350 | 0.4427 | 0.0343 | 0.1285 | 0.1612 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 38952 | 0.1816 | 0.5400 | 0.0238 | 0.5988 | 0.6199 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 38970 | 0.2178 | 0.6265 | 0.0183 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 77413 | 0.1566 | 0.4793 | 0.0121 | 0.2311 | 0.2334 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 120319 | 0.1009 | 0.3363 | 0.0073 | 0.1207 | 0.1257 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 101162 | 0.1654 | 0.4984 | 0.0078 | 0.2846 | 0.2871 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 43490 | 0.1772 | 0.5314 | 0.0163 | 0.4186 | 0.4311 |
| team_total | MARKET_BASELINE | 43465 | 0.1750 | 0.5260 | 0.0179 | 0.4271 | 0.4313 |
| team_total | MARKET_ANCHORED_V1 | 43465 | 0.1752 | 0.5264 | 0.0144 | 0.4254 | 0.4313 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
