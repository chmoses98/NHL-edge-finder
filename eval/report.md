# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-27T01:33:24Z · rows 602812 · pregame 602812 · new 0

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 102325 | 0.1649 | 0.4970 | 0.0196 | 0.4490 | 0.4667 |
| ALL | MARKET_BASELINE | 503200 | 0.1473 | 0.4534 | 0.0098 | 0.2833 | 0.2918 |
| ALL | MARKET_ANCHORED_V1 | 102300 | 0.1627 | 0.4913 | 0.0146 | 0.4555 | 0.4668 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 26641 | 0.0376 | 0.1619 | 0.0022 | 0.0380 | 0.0393 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 16372 | 0.1851 | 0.5550 | 0.0290 | 0.2311 | 0.2588 |
| game_spread | MARKET_BASELINE | 16372 | 0.1809 | 0.5434 | 0.0207 | 0.2428 | 0.2588 |
| game_spread | MARKET_ANCHORED_V1 | 16372 | 0.1814 | 0.5447 | 0.0195 | 0.2400 | 0.2588 |
| game_total | DATA_ONLY_V1 | 36837 | 0.1274 | 0.3980 | 0.0283 | 0.5675 | 0.5873 |
| game_total | MARKET_BASELINE | 36837 | 0.1260 | 0.3940 | 0.0287 | 0.5764 | 0.5873 |
| game_total | MARKET_ANCHORED_V1 | 36837 | 0.1261 | 0.3944 | 0.0265 | 0.5746 | 0.5873 |
| game_winner | DATA_ONLY_V1 | 8186 | 0.2327 | 0.6581 | 0.0952 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 8186 | 0.2290 | 0.6497 | 0.0314 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 8186 | 0.2291 | 0.6502 | 0.0445 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2300 | 0.2531 | 0.7000 | 0.0486 | 0.4443 | 0.4583 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 23317 | 0.1369 | 0.4469 | 0.0362 | 0.1288 | 0.1644 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 36648 | 0.1816 | 0.5404 | 0.0263 | 0.5990 | 0.6236 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 36666 | 0.2174 | 0.6257 | 0.0189 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 71424 | 0.1572 | 0.4808 | 0.0136 | 0.2320 | 0.2348 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 110880 | 0.1025 | 0.3410 | 0.0077 | 0.1221 | 0.1283 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 93024 | 0.1668 | 0.5022 | 0.0092 | 0.2868 | 0.2908 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 40930 | 0.1768 | 0.5307 | 0.0183 | 0.4194 | 0.4346 |
| team_total | MARKET_BASELINE | 40905 | 0.1746 | 0.5250 | 0.0178 | 0.4273 | 0.4348 |
| team_total | MARKET_ANCHORED_V1 | 40905 | 0.1747 | 0.5254 | 0.0150 | 0.4257 | 0.4348 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
