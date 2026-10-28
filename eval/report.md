# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-28T04:13:16Z · rows 650592 · pregame 650592 · new 4553

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 109400 | 0.1654 | 0.4985 | 0.0153 | 0.4483 | 0.4623 |
| ALL | MARKET_BASELINE | 549533 | 0.1453 | 0.4480 | 0.0080 | 0.2794 | 0.2854 |
| ALL | MARKET_ANCHORED_V1 | 109375 | 0.1634 | 0.4932 | 0.0115 | 0.4552 | 0.4624 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 32789 | 0.0357 | 0.1548 | 0.0017 | 0.0365 | 0.0373 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 17504 | 0.1851 | 0.5556 | 0.0270 | 0.2307 | 0.2565 |
| game_spread | MARKET_BASELINE | 17504 | 0.1811 | 0.5442 | 0.0228 | 0.2426 | 0.2565 |
| game_spread | MARKET_ANCHORED_V1 | 17504 | 0.1815 | 0.5455 | 0.0174 | 0.2398 | 0.2565 |
| game_total | DATA_ONLY_V1 | 39384 | 0.1280 | 0.3998 | 0.0260 | 0.5665 | 0.5816 |
| game_total | MARKET_BASELINE | 39384 | 0.1270 | 0.3970 | 0.0255 | 0.5761 | 0.5816 |
| game_total | MARKET_ANCHORED_V1 | 39384 | 0.1270 | 0.3971 | 0.0232 | 0.5742 | 0.5816 |
| game_winner | DATA_ONLY_V1 | 8752 | 0.2357 | 0.6642 | 0.0739 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8752 | 0.2314 | 0.6547 | 0.0304 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8752 | 0.2317 | 0.6554 | 0.0268 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2527 | 0.2512 | 0.6962 | 0.0409 | 0.4452 | 0.4464 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 25015 | 0.1343 | 0.4407 | 0.0332 | 0.1285 | 0.1602 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 39195 | 0.1819 | 0.5407 | 0.0229 | 0.5988 | 0.6189 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 39213 | 0.2178 | 0.6266 | 0.0186 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 77975 | 0.1563 | 0.4784 | 0.0126 | 0.2312 | 0.2331 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 121446 | 0.1004 | 0.3348 | 0.0070 | 0.1205 | 0.1252 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 101998 | 0.1648 | 0.4971 | 0.0081 | 0.2844 | 0.2865 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 43760 | 0.1771 | 0.5313 | 0.0156 | 0.4186 | 0.4297 |
| team_total | MARKET_BASELINE | 43735 | 0.1751 | 0.5261 | 0.0173 | 0.4272 | 0.4299 |
| team_total | MARKET_ANCHORED_V1 | 43735 | 0.1752 | 0.5264 | 0.0138 | 0.4254 | 0.4299 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
