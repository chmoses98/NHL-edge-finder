# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-21T05:16:51Z · rows 452292 · pregame 452292 · new 6716

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 79850 | 0.1601 | 0.4859 | 0.0172 | 0.4492 | 0.4589 |
| ALL | MARKET_BASELINE | 371027 | 0.1481 | 0.4561 | 0.0086 | 0.2922 | 0.2963 |
| ALL | MARKET_ANCHORED_V1 | 79832 | 0.1581 | 0.4807 | 0.0196 | 0.4547 | 0.4590 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 16230 | 0.0394 | 0.1691 | 0.0026 | 0.0404 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 12776 | 0.1786 | 0.5388 | 0.0198 | 0.2315 | 0.2497 |
| game_spread | MARKET_BASELINE | 12776 | 0.1748 | 0.5287 | 0.0244 | 0.2428 | 0.2497 |
| game_spread | MARKET_ANCHORED_V1 | 12776 | 0.1752 | 0.5297 | 0.0139 | 0.2401 | 0.2497 |
| game_total | DATA_ONLY_V1 | 28746 | 0.1242 | 0.3913 | 0.0280 | 0.5676 | 0.5788 |
| game_total | MARKET_BASELINE | 28746 | 0.1227 | 0.3877 | 0.0311 | 0.5751 | 0.5788 |
| game_total | MARKET_ANCHORED_V1 | 28746 | 0.1229 | 0.3880 | 0.0289 | 0.5736 | 0.5788 |
| game_winner | DATA_ONLY_V1 | 6388 | 0.2292 | 0.6509 | 0.1095 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 6388 | 0.2266 | 0.6445 | 0.0381 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 6388 | 0.2265 | 0.6445 | 0.0499 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1683 | 0.2487 | 0.6909 | 0.0436 | 0.4405 | 0.4290 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 18293 | 0.1354 | 0.4410 | 0.0351 | 0.1291 | 0.1634 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 28557 | 0.1812 | 0.5394 | 0.0273 | 0.5976 | 0.6197 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 28575 | 0.2170 | 0.6247 | 0.0229 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 50762 | 0.1566 | 0.4794 | 0.0197 | 0.2378 | 0.2345 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 81385 | 0.1039 | 0.3457 | 0.0100 | 0.1261 | 0.1295 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 65710 | 0.1681 | 0.5049 | 0.0144 | 0.2963 | 0.2933 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 31940 | 0.1713 | 0.5169 | 0.0186 | 0.4195 | 0.4264 |
| team_total | MARKET_BASELINE | 31922 | 0.1692 | 0.5114 | 0.0187 | 0.4259 | 0.4266 |
| team_total | MARKET_ANCHORED_V1 | 31922 | 0.1694 | 0.5118 | 0.0197 | 0.4246 | 0.4266 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
