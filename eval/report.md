# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-02T07:41:00Z · rows 800656 · pregame 800656 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 131500 | 0.1663 | 0.5007 | 0.0224 | 0.4498 | 0.4722 |
| ALL | MARKET_BASELINE | 687609 | 0.1441 | 0.4448 | 0.0123 | 0.2734 | 0.2842 |
| ALL | MARKET_ANCHORED_V1 | 131467 | 0.1640 | 0.4947 | 0.0156 | 0.4567 | 0.4723 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 49188 | 0.0342 | 0.1487 | 0.0020 | 0.0345 | 0.0357 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 21040 | 0.1855 | 0.5556 | 0.0309 | 0.2314 | 0.2611 |
| game_spread | MARKET_BASELINE | 21040 | 0.1810 | 0.5433 | 0.0242 | 0.2436 | 0.2611 |
| game_spread | MARKET_ANCHORED_V1 | 21040 | 0.1815 | 0.5448 | 0.0223 | 0.2407 | 0.2611 |
| game_total | DATA_ONLY_V1 | 47340 | 0.1297 | 0.4042 | 0.0297 | 0.5685 | 0.5930 |
| game_total | MARKET_BASELINE | 47340 | 0.1282 | 0.4001 | 0.0238 | 0.5780 | 0.5930 |
| game_total | MARKET_ANCHORED_V1 | 47340 | 0.1284 | 0.4004 | 0.0244 | 0.5762 | 0.5930 |
| game_winner | DATA_ONLY_V1 | 10520 | 0.2322 | 0.6569 | 0.0738 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10520 | 0.2283 | 0.6481 | 0.0260 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10520 | 0.2285 | 0.6487 | 0.0334 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3085 | 0.2487 | 0.6911 | 0.0325 | 0.4462 | 0.4441 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 30116 | 0.1350 | 0.4418 | 0.0336 | 0.1287 | 0.1618 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 47121 | 0.1786 | 0.5324 | 0.0294 | 0.5996 | 0.6276 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 47169 | 0.2165 | 0.6236 | 0.0257 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 98186 | 0.1583 | 0.4840 | 0.0195 | 0.2297 | 0.2380 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 152296 | 0.1008 | 0.3365 | 0.0083 | 0.1191 | 0.1260 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 128981 | 0.1667 | 0.5027 | 0.0136 | 0.2814 | 0.2905 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 52600 | 0.1784 | 0.5343 | 0.0241 | 0.4203 | 0.4424 |
| team_total | MARKET_BASELINE | 52567 | 0.1759 | 0.5283 | 0.0184 | 0.4289 | 0.4426 |
| team_total | MARKET_ANCHORED_V1 | 52567 | 0.1762 | 0.5288 | 0.0170 | 0.4271 | 0.4426 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
