# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-11T04:41:34Z · rows 232488 · pregame 232488 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 42475 | 0.1697 | 0.5101 | 0.0120 | 0.4509 | 0.4541 |
| ALL | MARKET_BASELINE | 194079 | 0.1500 | 0.4615 | 0.0098 | 0.2924 | 0.2933 |
| ALL | MARKET_ANCHORED_V1 | 42461 | 0.1661 | 0.5010 | 0.0097 | 0.4535 | 0.4543 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 9723 | 0.0401 | 0.1716 | 0.0060 | 0.0382 | 0.0419 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 6796 | 0.1888 | 0.5625 | 0.0425 | 0.2317 | 0.2707 |
| game_spread | MARKET_BASELINE | 6796 | 0.1818 | 0.5445 | 0.0355 | 0.2417 | 0.2707 |
| game_spread | MARKET_ANCHORED_V1 | 6796 | 0.1828 | 0.5471 | 0.0341 | 0.2392 | 0.2707 |
| game_total | DATA_ONLY_V1 | 15291 | 0.1311 | 0.4104 | 0.0225 | 0.5700 | 0.5635 |
| game_total | MARKET_BASELINE | 15291 | 0.1282 | 0.4023 | 0.0272 | 0.5724 | 0.5635 |
| game_total | MARKET_ANCHORED_V1 | 15291 | 0.1286 | 0.4035 | 0.0271 | 0.5719 | 0.5635 |
| game_winner | DATA_ONLY_V1 | 3398 | 0.2325 | 0.6577 | 0.1017 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3398 | 0.2269 | 0.6451 | 0.0526 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3398 | 0.2273 | 0.6463 | 0.0341 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 734 | 0.2529 | 0.7002 | 0.0786 | 0.4207 | 0.4332 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 9690 | 0.1525 | 0.4880 | 0.0555 | 0.1307 | 0.1848 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 15102 | 0.1835 | 0.5463 | 0.0279 | 0.5948 | 0.6039 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 15120 | 0.2170 | 0.6248 | 0.0228 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 25893 | 0.1525 | 0.4694 | 0.0211 | 0.2382 | 0.2282 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 43110 | 0.1065 | 0.3540 | 0.0099 | 0.1299 | 0.1319 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 32246 | 0.1684 | 0.5062 | 0.0189 | 0.3038 | 0.2904 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 16990 | 0.1843 | 0.5493 | 0.0322 | 0.4216 | 0.4199 |
| team_total | MARKET_BASELINE | 16976 | 0.1805 | 0.5400 | 0.0294 | 0.4240 | 0.4202 |
| team_total | MARKET_ANCHORED_V1 | 16976 | 0.1810 | 0.5412 | 0.0293 | 0.4235 | 0.4202 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
