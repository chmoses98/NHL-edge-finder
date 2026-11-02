# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-02T03:47:06Z · rows 795303 · pregame 795303 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 130700 | 0.1662 | 0.5004 | 0.0211 | 0.4495 | 0.4707 |
| ALL | MARKET_BASELINE | 682794 | 0.1438 | 0.4440 | 0.0117 | 0.2734 | 0.2835 |
| ALL | MARKET_ANCHORED_V1 | 130667 | 0.1637 | 0.4940 | 0.0143 | 0.4565 | 0.4708 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 48653 | 0.0346 | 0.1499 | 0.0024 | 0.0345 | 0.0361 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 20912 | 0.1850 | 0.5544 | 0.0295 | 0.2313 | 0.2596 |
| game_spread | MARKET_BASELINE | 20912 | 0.1800 | 0.5411 | 0.0218 | 0.2435 | 0.2596 |
| game_spread | MARKET_ANCHORED_V1 | 20912 | 0.1807 | 0.5428 | 0.0209 | 0.2406 | 0.2596 |
| game_total | DATA_ONLY_V1 | 47052 | 0.1296 | 0.4041 | 0.0282 | 0.5681 | 0.5912 |
| game_total | MARKET_BASELINE | 47052 | 0.1281 | 0.3998 | 0.0221 | 0.5777 | 0.5912 |
| game_total | MARKET_ANCHORED_V1 | 47052 | 0.1282 | 0.4002 | 0.0228 | 0.5759 | 0.5912 |
| game_winner | DATA_ONLY_V1 | 10456 | 0.2325 | 0.6574 | 0.0715 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10456 | 0.2280 | 0.6475 | 0.0256 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10456 | 0.2283 | 0.6483 | 0.0362 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 3054 | 0.2487 | 0.6911 | 0.0335 | 0.4463 | 0.4434 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 29925 | 0.1334 | 0.4376 | 0.0315 | 0.1286 | 0.1597 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 46836 | 0.1786 | 0.5325 | 0.0273 | 0.5994 | 0.6254 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 46881 | 0.2165 | 0.6237 | 0.0251 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 97496 | 0.1578 | 0.4826 | 0.0187 | 0.2296 | 0.2368 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 151288 | 0.1008 | 0.3363 | 0.0081 | 0.1191 | 0.1260 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 127994 | 0.1661 | 0.5009 | 0.0130 | 0.2815 | 0.2896 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 52280 | 0.1783 | 0.5341 | 0.0233 | 0.4200 | 0.4408 |
| team_total | MARKET_BASELINE | 52247 | 0.1756 | 0.5274 | 0.0171 | 0.4286 | 0.4410 |
| team_total | MARKET_ANCHORED_V1 | 52247 | 0.1759 | 0.5281 | 0.0158 | 0.4269 | 0.4410 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
