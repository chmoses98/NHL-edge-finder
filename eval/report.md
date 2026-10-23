# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-23T03:15:40Z · rows 491247 · pregame 491247 · new 11733

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 86100 | 0.1612 | 0.4881 | 0.0163 | 0.4489 | 0.4602 |
| ALL | MARKET_BASELINE | 403542 | 0.1481 | 0.4557 | 0.0083 | 0.2908 | 0.2952 |
| ALL | MARKET_ANCHORED_V1 | 86077 | 0.1594 | 0.4837 | 0.0155 | 0.4545 | 0.4603 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 17597 | 0.0399 | 0.1701 | 0.0030 | 0.0406 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 13776 | 0.1823 | 0.5473 | 0.0266 | 0.2313 | 0.2562 |
| game_spread | MARKET_BASELINE | 13776 | 0.1790 | 0.5385 | 0.0273 | 0.2427 | 0.2562 |
| game_spread | MARKET_ANCHORED_V1 | 13776 | 0.1793 | 0.5393 | 0.0206 | 0.2399 | 0.2562 |
| game_total | DATA_ONLY_V1 | 30996 | 0.1229 | 0.3876 | 0.0300 | 0.5672 | 0.5787 |
| game_total | MARKET_BASELINE | 30996 | 0.1218 | 0.3848 | 0.0287 | 0.5749 | 0.5787 |
| game_total | MARKET_ANCHORED_V1 | 30996 | 0.1219 | 0.3849 | 0.0277 | 0.5734 | 0.5787 |
| game_winner | DATA_ONLY_V1 | 6888 | 0.2308 | 0.6541 | 0.0999 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6888 | 0.2278 | 0.6469 | 0.0401 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6888 | 0.2278 | 0.6472 | 0.0382 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1871 | 0.2508 | 0.6950 | 0.0580 | 0.4430 | 0.4495 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 19687 | 0.1373 | 0.4467 | 0.0375 | 0.1287 | 0.1655 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 30807 | 0.1799 | 0.5363 | 0.0275 | 0.5975 | 0.6210 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 30825 | 0.2168 | 0.6243 | 0.0234 | 0.3278 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 56131 | 0.1552 | 0.4757 | 0.0192 | 0.2351 | 0.2302 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 87758 | 0.1032 | 0.3434 | 0.0087 | 0.1256 | 0.1289 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 72789 | 0.1671 | 0.5029 | 0.0128 | 0.2925 | 0.2891 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 34440 | 0.1732 | 0.5217 | 0.0169 | 0.4192 | 0.4273 |
| team_total | MARKET_BASELINE | 34417 | 0.1716 | 0.5176 | 0.0189 | 0.4258 | 0.4275 |
| team_total | MARKET_ANCHORED_V1 | 34417 | 0.1716 | 0.5177 | 0.0199 | 0.4244 | 0.4275 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
