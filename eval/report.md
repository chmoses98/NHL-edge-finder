# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-01T00:14:20Z · rows 13255 · pregame 13255 · new 12355

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 1725 | 0.1953 | 0.5888 | 0.0810 | 0.4566 | 0.4325 |
| ALL | MARKET_BASELINE | 10467 | 0.1421 | 0.4436 | 0.0471 | 0.2653 | 0.2240 |
| ALL | MARKET_ANCHORED_V1 | 1725 | 0.1947 | 0.5871 | 0.0555 | 0.4599 | 0.4325 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 641 | 0.0298 | 0.1449 | 0.0058 | 0.0354 | 0.0296 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 276 | 0.1629 | 0.4923 | 0.1004 | 0.2370 | 0.2246 |
| game_spread | MARKET_BASELINE | 276 | 0.1553 | 0.4727 | 0.1031 | 0.2497 | 0.2246 |
| game_spread | MARKET_ANCHORED_V1 | 276 | 0.1561 | 0.4750 | 0.0861 | 0.2465 | 0.2246 |
| game_total | DATA_ONLY_V1 | 621 | 0.1973 | 0.6160 | 0.1017 | 0.5772 | 0.5185 |
| game_total | MARKET_BASELINE | 621 | 0.1986 | 0.6114 | 0.1225 | 0.5782 | 0.5185 |
| game_total | MARKET_ANCHORED_V1 | 621 | 0.1983 | 0.6121 | 0.1263 | 0.5780 | 0.5185 |
| game_winner | DATA_ONLY_V1 | 138 | 0.2729 | 0.7422 | 0.3231 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 138 | 0.2817 | 0.7636 | 0.2317 | 0.5003 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 138 | 0.2793 | 0.7574 | 0.3457 | 0.5002 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 69 | 0.2942 | 0.7855 | 0.3266 | 0.4240 | 0.4928 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 382 | 0.0780 | 0.2887 | 0.0553 | 0.1364 | 0.0812 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 606 | 0.2060 | 0.6107 | 0.1300 | 0.5933 | 0.5248 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 609 | 0.2281 | 0.6482 | 0.0413 | 0.3318 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 1559 | 0.1374 | 0.4389 | 0.0803 | 0.2390 | 0.1693 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 3037 | 0.0847 | 0.2972 | 0.0309 | 0.1109 | 0.0932 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 1839 | 0.1885 | 0.5547 | 0.1087 | 0.3301 | 0.2431 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 690 | 0.1910 | 0.5723 | 0.0672 | 0.4273 | 0.4246 |
| team_total | MARKET_BASELINE | 690 | 0.1901 | 0.5774 | 0.0911 | 0.4320 | 0.4246 |
| team_total | MARKET_ANCHORED_V1 | 690 | 0.1900 | 0.5754 | 0.0709 | 0.4309 | 0.4246 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
