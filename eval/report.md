# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-10T20:25:37Z · rows 197783 · pregame 197783 · new 2394

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 36875 | 0.1672 | 0.5029 | 0.0138 | 0.4501 | 0.4609 |
| ALL | MARKET_BASELINE | 168473 | 0.1496 | 0.4603 | 0.0106 | 0.2906 | 0.2959 |
| ALL | MARKET_ANCHORED_V1 | 36861 | 0.1646 | 0.4960 | 0.0118 | 0.4532 | 0.4610 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9185 | 0.0397 | 0.1708 | 0.0061 | 0.0375 | 0.0414 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5900 | 0.1857 | 0.5539 | 0.0432 | 0.2314 | 0.2676 |
| game_spread | MARKET_BASELINE | 5900 | 0.1804 | 0.5409 | 0.0400 | 0.2412 | 0.2676 |
| game_spread | MARKET_ANCHORED_V1 | 5900 | 0.1811 | 0.5425 | 0.0350 | 0.2387 | 0.2676 |
| game_total | DATA_ONLY_V1 | 13275 | 0.1266 | 0.3969 | 0.0241 | 0.5689 | 0.5733 |
| game_total | MARKET_BASELINE | 13275 | 0.1242 | 0.3894 | 0.0264 | 0.5721 | 0.5733 |
| game_total | MARKET_ANCHORED_V1 | 13275 | 0.1245 | 0.3905 | 0.0254 | 0.5715 | 0.5733 |
| game_winner | DATA_ONLY_V1 | 2950 | 0.2310 | 0.6542 | 0.0747 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2950 | 0.2287 | 0.6488 | 0.0621 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2950 | 0.2285 | 0.6487 | 0.0366 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 638 | 0.2524 | 0.6989 | 0.0668 | 0.4172 | 0.4451 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 8411 | 0.1508 | 0.4815 | 0.0547 | 0.1308 | 0.1838 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 13086 | 0.1805 | 0.5380 | 0.0315 | 0.5947 | 0.6126 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 13104 | 0.2165 | 0.6238 | 0.0272 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 22295 | 0.1543 | 0.4744 | 0.0188 | 0.2350 | 0.2311 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 37381 | 0.1083 | 0.3595 | 0.0102 | 0.1298 | 0.1345 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 27512 | 0.1696 | 0.5091 | 0.0197 | 0.3030 | 0.2938 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 14750 | 0.1837 | 0.5478 | 0.0283 | 0.4207 | 0.4292 |
| team_total | MARKET_BASELINE | 14736 | 0.1810 | 0.5411 | 0.0308 | 0.4239 | 0.4295 |
| team_total | MARKET_ANCHORED_V1 | 14736 | 0.1813 | 0.5418 | 0.0293 | 0.4232 | 0.4295 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
