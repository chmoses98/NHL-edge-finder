# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-21T14:16:52Z · rows 456082 · pregame 456082 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 80475 | 0.1608 | 0.4876 | 0.0167 | 0.4491 | 0.4603 |
| ALL | MARKET_BASELINE | 374193 | 0.1482 | 0.4561 | 0.0085 | 0.2922 | 0.2965 |
| ALL | MARKET_ANCHORED_V1 | 80457 | 0.1587 | 0.4820 | 0.0185 | 0.4547 | 0.4604 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 16314 | 0.0395 | 0.1694 | 0.0027 | 0.0405 | 0.0413 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 12876 | 0.1799 | 0.5422 | 0.0218 | 0.2314 | 0.2516 |
| game_spread | MARKET_BASELINE | 12876 | 0.1760 | 0.5314 | 0.0262 | 0.2428 | 0.2516 |
| game_spread | MARKET_ANCHORED_V1 | 12876 | 0.1764 | 0.5326 | 0.0158 | 0.2400 | 0.2516 |
| game_total | DATA_ONLY_V1 | 28971 | 0.1243 | 0.3915 | 0.0286 | 0.5674 | 0.5803 |
| game_total | MARKET_BASELINE | 28971 | 0.1227 | 0.3876 | 0.0299 | 0.5751 | 0.5803 |
| game_total | MARKET_ANCHORED_V1 | 28971 | 0.1229 | 0.3880 | 0.0285 | 0.5736 | 0.5803 |
| game_winner | DATA_ONLY_V1 | 6438 | 0.2297 | 0.6518 | 0.1045 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6438 | 0.2268 | 0.6449 | 0.0385 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6438 | 0.2268 | 0.6451 | 0.0455 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1701 | 0.2496 | 0.6926 | 0.0487 | 0.4409 | 0.4297 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 18435 | 0.1354 | 0.4410 | 0.0350 | 0.1290 | 0.1633 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 28782 | 0.1815 | 0.5400 | 0.0284 | 0.5976 | 0.6210 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 28800 | 0.2170 | 0.6246 | 0.0234 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 51285 | 0.1558 | 0.4776 | 0.0197 | 0.2376 | 0.2329 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 82049 | 0.1039 | 0.3458 | 0.0098 | 0.1261 | 0.1297 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 66370 | 0.1678 | 0.5043 | 0.0142 | 0.2961 | 0.2926 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 32190 | 0.1722 | 0.5193 | 0.0212 | 0.4194 | 0.4278 |
| team_total | MARKET_BASELINE | 32172 | 0.1699 | 0.5133 | 0.0191 | 0.4260 | 0.4280 |
| team_total | MARKET_ANCHORED_V1 | 32172 | 0.1701 | 0.5138 | 0.0209 | 0.4246 | 0.4280 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
