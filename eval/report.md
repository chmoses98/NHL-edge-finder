# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-02T02:35:51Z · rows 30101 · pregame 30101 · new 8158

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 5025 | 0.2054 | 0.6052 | 0.0728 | 0.4387 | 0.4856 |
| ALL | MARKET_BASELINE | 25654 | 0.1538 | 0.4711 | 0.0256 | 0.2780 | 0.2777 |
| ALL | MARKET_ANCHORED_V1 | 5025 | 0.2020 | 0.5951 | 0.0613 | 0.4497 | 0.4856 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 2047 | 0.0232 | 0.1183 | 0.0085 | 0.0315 | 0.0230 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 804 | 0.2079 | 0.6054 | 0.1045 | 0.2289 | 0.2985 |
| game_spread | MARKET_BASELINE | 804 | 0.2090 | 0.6094 | 0.1532 | 0.2410 | 0.2985 |
| game_spread | MARKET_ANCHORED_V1 | 804 | 0.2083 | 0.6076 | 0.1437 | 0.2380 | 0.2985 |
| game_total | DATA_ONLY_V1 | 1809 | 0.1780 | 0.5423 | 0.0806 | 0.5534 | 0.5970 |
| game_total | MARKET_BASELINE | 1809 | 0.1708 | 0.5174 | 0.0622 | 0.5694 | 0.5970 |
| game_total | MARKET_ANCHORED_V1 | 1809 | 0.1721 | 0.5219 | 0.0628 | 0.5662 | 0.5970 |
| game_winner | DATA_ONLY_V1 | 402 | 0.2478 | 0.6890 | 0.0730 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 402 | 0.2476 | 0.6898 | 0.2839 | 0.4998 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 402 | 0.2471 | 0.6883 | 0.2127 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 136 | 0.2702 | 0.7359 | 0.1929 | 0.3856 | 0.4559 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 1136 | 0.1469 | 0.4797 | 0.0646 | 0.1292 | 0.1708 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 1794 | 0.1886 | 0.5599 | 0.0517 | 0.5912 | 0.6360 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 1797 | 0.2211 | 0.6334 | 0.0194 | 0.3293 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 3615 | 0.1493 | 0.4623 | 0.0432 | 0.2326 | 0.2008 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 5815 | 0.1106 | 0.3678 | 0.0359 | 0.1299 | 0.1317 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 4289 | 0.1781 | 0.5276 | 0.0664 | 0.3136 | 0.2677 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 2010 | 0.2206 | 0.6449 | 0.0957 | 0.4071 | 0.4572 |
| team_total | MARKET_BASELINE | 2010 | 0.2170 | 0.6365 | 0.1251 | 0.4226 | 0.4572 |
| team_total | MARKET_ANCHORED_V1 | 2010 | 0.2175 | 0.6374 | 0.1244 | 0.4194 | 0.4572 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
