# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-20T03:11:14Z · rows 414685 · pregame 414685 · new 3421

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 73750 | 0.1618 | 0.4898 | 0.0153 | 0.4496 | 0.4569 |
| ALL | MARKET_BASELINE | 341213 | 0.1483 | 0.4566 | 0.0079 | 0.2923 | 0.2952 |
| ALL | MARKET_ANCHORED_V1 | 73732 | 0.1600 | 0.4853 | 0.0151 | 0.4544 | 0.4570 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 15235 | 0.0389 | 0.1672 | 0.0024 | 0.0402 | 0.0406 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 11800 | 0.1819 | 0.5453 | 0.0323 | 0.2315 | 0.2592 |
| game_spread | MARKET_BASELINE | 11800 | 0.1784 | 0.5361 | 0.0266 | 0.2425 | 0.2592 |
| game_spread | MARKET_ANCHORED_V1 | 11800 | 0.1787 | 0.5370 | 0.0234 | 0.2398 | 0.2592 |
| game_total | DATA_ONLY_V1 | 26550 | 0.1254 | 0.3951 | 0.0257 | 0.5682 | 0.5736 |
| game_total | MARKET_BASELINE | 26550 | 0.1243 | 0.3922 | 0.0315 | 0.5745 | 0.5736 |
| game_total | MARKET_ANCHORED_V1 | 26550 | 0.1243 | 0.3923 | 0.0302 | 0.5733 | 0.5736 |
| game_winner | DATA_ONLY_V1 | 5900 | 0.2287 | 0.6499 | 0.1134 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5900 | 0.2264 | 0.6439 | 0.0413 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5900 | 0.2262 | 0.6439 | 0.0481 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1506 | 0.2485 | 0.6904 | 0.0475 | 0.4379 | 0.4270 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 16898 | 0.1362 | 0.4431 | 0.0359 | 0.1293 | 0.1644 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 26361 | 0.1824 | 0.5420 | 0.0268 | 0.5971 | 0.6163 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 26379 | 0.2165 | 0.6237 | 0.0227 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 46250 | 0.1565 | 0.4795 | 0.0191 | 0.2381 | 0.2337 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 75132 | 0.1037 | 0.3455 | 0.0101 | 0.1262 | 0.1291 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 59720 | 0.1676 | 0.5040 | 0.0136 | 0.2977 | 0.2920 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 29500 | 0.1731 | 0.5209 | 0.0125 | 0.4200 | 0.4223 |
| team_total | MARKET_BASELINE | 29482 | 0.1713 | 0.5164 | 0.0158 | 0.4255 | 0.4225 |
| team_total | MARKET_ANCHORED_V1 | 29482 | 0.1714 | 0.5166 | 0.0148 | 0.4243 | 0.4225 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
