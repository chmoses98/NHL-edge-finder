# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-28T02:33:00Z · rows 619274 · pregame 619274 · new 4047

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 104825 | 0.1648 | 0.4970 | 0.0206 | 0.4489 | 0.4688 |
| ALL | MARKET_BASELINE | 519447 | 0.1469 | 0.4523 | 0.0101 | 0.2819 | 0.2915 |
| ALL | MARKET_ANCHORED_V1 | 104800 | 0.1627 | 0.4914 | 0.0159 | 0.4556 | 0.4689 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 28797 | 0.0365 | 0.1577 | 0.0016 | 0.0374 | 0.0382 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16772 | 0.1854 | 0.5561 | 0.0286 | 0.2310 | 0.2583 |
| game_spread | MARKET_BASELINE | 16772 | 0.1816 | 0.5455 | 0.0230 | 0.2428 | 0.2583 |
| game_spread | MARKET_ANCHORED_V1 | 16772 | 0.1820 | 0.5466 | 0.0191 | 0.2400 | 0.2583 |
| game_total | DATA_ONLY_V1 | 37737 | 0.1271 | 0.3969 | 0.0307 | 0.5673 | 0.5904 |
| game_total | MARKET_BASELINE | 37737 | 0.1254 | 0.3926 | 0.0293 | 0.5765 | 0.5904 |
| game_total | MARKET_ANCHORED_V1 | 37737 | 0.1256 | 0.3930 | 0.0275 | 0.5747 | 0.5904 |
| game_winner | DATA_ONLY_V1 | 8386 | 0.2345 | 0.6617 | 0.0852 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8386 | 0.2309 | 0.6536 | 0.0228 | 0.4992 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8386 | 0.2310 | 0.6540 | 0.0357 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2381 | 0.2518 | 0.6973 | 0.0417 | 0.4446 | 0.4553 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 23917 | 0.1371 | 0.4479 | 0.0366 | 0.1288 | 0.1643 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 37548 | 0.1811 | 0.5391 | 0.0271 | 0.5991 | 0.6258 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 37566 | 0.2179 | 0.6267 | 0.0161 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 73752 | 0.1578 | 0.4821 | 0.0138 | 0.2316 | 0.2366 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 114594 | 0.1023 | 0.3404 | 0.0086 | 0.1214 | 0.1279 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 96092 | 0.1666 | 0.5017 | 0.0094 | 0.2862 | 0.2919 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 41930 | 0.1766 | 0.5305 | 0.0199 | 0.4193 | 0.4373 |
| team_total | MARKET_BASELINE | 41905 | 0.1745 | 0.5250 | 0.0189 | 0.4275 | 0.4375 |
| team_total | MARKET_ANCHORED_V1 | 41905 | 0.1746 | 0.5254 | 0.0163 | 0.4258 | 0.4375 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
