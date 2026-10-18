# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-17T23:47:23Z · rows 360802 · pregame 360802 · new 2580

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 64750 | 0.1616 | 0.4892 | 0.0164 | 0.4498 | 0.4615 |
| ALL | MARKET_BASELINE | 299853 | 0.1482 | 0.4564 | 0.0098 | 0.2912 | 0.2968 |
| ALL | MARKET_ANCHORED_V1 | 64732 | 0.1589 | 0.4822 | 0.0181 | 0.4539 | 0.4616 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 13843 | 0.0399 | 0.1707 | 0.0039 | 0.0396 | 0.0417 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 10360 | 0.1794 | 0.5396 | 0.0279 | 0.2317 | 0.2548 |
| game_spread | MARKET_BASELINE | 10360 | 0.1756 | 0.5297 | 0.0191 | 0.2423 | 0.2548 |
| game_spread | MARKET_ANCHORED_V1 | 10360 | 0.1760 | 0.5307 | 0.0195 | 0.2397 | 0.2548 |
| game_total | DATA_ONLY_V1 | 23310 | 0.1256 | 0.3943 | 0.0241 | 0.5684 | 0.5810 |
| game_total | MARKET_BASELINE | 23310 | 0.1229 | 0.3868 | 0.0296 | 0.5735 | 0.5810 |
| game_total | MARKET_ANCHORED_V1 | 23310 | 0.1233 | 0.3879 | 0.0283 | 0.5725 | 0.5810 |
| game_winner | DATA_ONLY_V1 | 5180 | 0.2273 | 0.6469 | 0.1122 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 5180 | 0.2239 | 0.6387 | 0.0400 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 5180 | 0.2240 | 0.6392 | 0.0510 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 1289 | 0.2439 | 0.6812 | 0.0860 | 0.4319 | 0.3894 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 14918 | 0.1401 | 0.4541 | 0.0408 | 0.1298 | 0.1697 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 23121 | 0.1812 | 0.5393 | 0.0283 | 0.5962 | 0.6188 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 23139 | 0.2161 | 0.6228 | 0.0188 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 40973 | 0.1557 | 0.4773 | 0.0167 | 0.2348 | 0.2334 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 65457 | 0.1047 | 0.3480 | 0.0099 | 0.1270 | 0.1304 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 52381 | 0.1681 | 0.5054 | 0.0128 | 0.2960 | 0.2936 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 25900 | 0.1737 | 0.5230 | 0.0203 | 0.4201 | 0.4288 |
| team_total | MARKET_BASELINE | 25882 | 0.1708 | 0.5155 | 0.0165 | 0.4248 | 0.4291 |
| team_total | MARKET_ANCHORED_V1 | 25882 | 0.1711 | 0.5164 | 0.0188 | 0.4238 | 0.4291 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
