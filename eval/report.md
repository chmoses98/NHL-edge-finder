# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-05T01:50:21Z · rows 96793 · pregame 96793 · new 2737

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 18525 | 0.1731 | 0.5192 | 0.0176 | 0.4471 | 0.4568 |
| ALL | MARKET_BASELINE | 82738 | 0.1571 | 0.4803 | 0.0143 | 0.2981 | 0.3058 |
| ALL | MARKET_ANCHORED_V1 | 18525 | 0.1728 | 0.5186 | 0.0243 | 0.4528 | 0.4568 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 4795 | 0.0351 | 0.1562 | 0.0038 | 0.0355 | 0.0363 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 2964 | 0.1796 | 0.5396 | 0.0381 | 0.2304 | 0.2594 |
| game_spread | MARKET_BASELINE | 2964 | 0.1797 | 0.5419 | 0.0640 | 0.2411 | 0.2594 |
| game_spread | MARKET_ANCHORED_V1 | 2964 | 0.1793 | 0.5405 | 0.0531 | 0.2385 | 0.2594 |
| game_total | DATA_ONLY_V1 | 6669 | 0.1354 | 0.4221 | 0.0149 | 0.5649 | 0.5622 |
| game_total | MARKET_BASELINE | 6669 | 0.1328 | 0.4153 | 0.0257 | 0.5724 | 0.5622 |
| game_total | MARKET_ANCHORED_V1 | 6669 | 0.1332 | 0.4162 | 0.0245 | 0.5709 | 0.5622 |
| game_winner | DATA_ONLY_V1 | 1482 | 0.2288 | 0.6499 | 0.0904 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 1482 | 0.2372 | 0.6665 | 0.1362 | 0.4997 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 1482 | 0.2350 | 0.6621 | 0.1379 | 0.4998 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 323 | 0.2585 | 0.7110 | 0.1027 | 0.3914 | 0.4861 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 4253 | 0.1589 | 0.4997 | 0.0662 | 0.1316 | 0.1977 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 6644 | 0.1825 | 0.5418 | 0.0227 | 0.5936 | 0.6135 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 6657 | 0.2160 | 0.6225 | 0.0368 | 0.3280 | 0.3333 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 11446 | 0.1576 | 0.4819 | 0.0213 | 0.2325 | 0.2367 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 16878 | 0.1219 | 0.3997 | 0.0188 | 0.1458 | 0.1513 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 13217 | 0.1784 | 0.5305 | 0.0333 | 0.3132 | 0.3110 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 7410 | 0.1933 | 0.5723 | 0.0383 | 0.4172 | 0.4324 |
| team_total | MARKET_BASELINE | 7410 | 0.1936 | 0.5742 | 0.0675 | 0.4243 | 0.4324 |
| team_total | MARKET_ANCHORED_V1 | 7410 | 0.1934 | 0.5732 | 0.0598 | 0.4228 | 0.4324 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
