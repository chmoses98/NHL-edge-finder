# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-17T23:00:16Z · rows 358222 · pregame 358222 · new 3024

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 64300 | 0.1622 | 0.4906 | 0.0160 | 0.4497 | 0.4616 |
| ALL | MARKET_BASELINE | 298014 | 0.1484 | 0.4569 | 0.0096 | 0.2910 | 0.2967 |
| ALL | MARKET_ANCHORED_V1 | 64283 | 0.1595 | 0.4836 | 0.0168 | 0.4538 | 0.4617 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13781 | 0.0400 | 0.1710 | 0.0041 | 0.0396 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10288 | 0.1799 | 0.5410 | 0.0278 | 0.2316 | 0.2549 |
| game_spread | MARKET_BASELINE | 10288 | 0.1761 | 0.5311 | 0.0193 | 0.2419 | 0.2549 |
| game_spread | MARKET_ANCHORED_V1 | 10288 | 0.1765 | 0.5321 | 0.0198 | 0.2394 | 0.2549 |
| game_total | DATA_ONLY_V1 | 23148 | 0.1260 | 0.3953 | 0.0228 | 0.5684 | 0.5812 |
| game_total | MARKET_BASELINE | 23148 | 0.1233 | 0.3878 | 0.0287 | 0.5733 | 0.5812 |
| game_total | MARKET_ANCHORED_V1 | 23148 | 0.1237 | 0.3889 | 0.0279 | 0.5724 | 0.5812 |
| game_winner | DATA_ONLY_V1 | 5144 | 0.2282 | 0.6489 | 0.1111 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5144 | 0.2251 | 0.6414 | 0.0387 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5144 | 0.2251 | 0.6417 | 0.0496 | 0.4992 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1289 | 0.2439 | 0.6812 | 0.0860 | 0.4319 | 0.3894 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14821 | 0.1403 | 0.4549 | 0.0409 | 0.1296 | 0.1696 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 22959 | 0.1815 | 0.5400 | 0.0279 | 0.5960 | 0.6185 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 22977 | 0.2164 | 0.6234 | 0.0200 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 40771 | 0.1555 | 0.4769 | 0.0173 | 0.2345 | 0.2332 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 65020 | 0.1048 | 0.3483 | 0.0097 | 0.1271 | 0.1304 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 52113 | 0.1682 | 0.5057 | 0.0125 | 0.2957 | 0.2934 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 25720 | 0.1744 | 0.5245 | 0.0199 | 0.4201 | 0.4290 |
| team_total | MARKET_BASELINE | 25703 | 0.1714 | 0.5171 | 0.0152 | 0.4247 | 0.4293 |
| team_total | MARKET_ANCHORED_V1 | 25703 | 0.1718 | 0.5180 | 0.0177 | 0.4237 | 0.4293 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
