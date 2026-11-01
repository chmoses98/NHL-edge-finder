# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-11-01T02:10:22Z · rows 767038 · pregame 767038 · new 32590

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 126700 | 0.1662 | 0.5004 | 0.0203 | 0.4498 | 0.4701 |
| ALL | MARKET_BASELINE | 657340 | 0.1441 | 0.4447 | 0.0107 | 0.2743 | 0.2838 |
| ALL | MARKET_ANCHORED_V1 | 126667 | 0.1637 | 0.4942 | 0.0140 | 0.4566 | 0.4702 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 45682 | 0.0344 | 0.1497 | 0.0020 | 0.0347 | 0.0359 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 20272 | 0.1828 | 0.5497 | 0.0234 | 0.2312 | 0.2536 |
| game_spread | MARKET_BASELINE | 20272 | 0.1782 | 0.5370 | 0.0170 | 0.2431 | 0.2536 |
| game_spread | MARKET_ANCHORED_V1 | 20272 | 0.1788 | 0.5386 | 0.0149 | 0.2403 | 0.2536 |
| game_total | DATA_ONLY_V1 | 45612 | 0.1305 | 0.4063 | 0.0278 | 0.5686 | 0.5916 |
| game_total | MARKET_BASELINE | 45612 | 0.1289 | 0.4021 | 0.0229 | 0.5779 | 0.5916 |
| game_total | MARKET_ANCHORED_V1 | 45612 | 0.1291 | 0.4025 | 0.0228 | 0.5760 | 0.5916 |
| game_winner | DATA_ONLY_V1 | 10136 | 0.2336 | 0.6598 | 0.0773 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 10136 | 0.2293 | 0.6503 | 0.0254 | 0.4994 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 10136 | 0.2296 | 0.6510 | 0.0401 | 0.4995 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2946 | 0.2484 | 0.6905 | 0.0400 | 0.4463 | 0.4375 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 28996 | 0.1323 | 0.4350 | 0.0300 | 0.1285 | 0.1580 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 45406 | 0.1795 | 0.5344 | 0.0260 | 0.5996 | 0.6256 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 45441 | 0.2167 | 0.6241 | 0.0250 | 0.3283 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 93747 | 0.1570 | 0.4804 | 0.0165 | 0.2293 | 0.2351 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 145504 | 0.1010 | 0.3369 | 0.0083 | 0.1192 | 0.1263 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 122951 | 0.1663 | 0.5014 | 0.0121 | 0.2816 | 0.2890 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 50680 | 0.1781 | 0.5335 | 0.0226 | 0.4204 | 0.4414 |
| team_total | MARKET_BASELINE | 50647 | 0.1754 | 0.5269 | 0.0180 | 0.4288 | 0.4417 |
| team_total | MARKET_ANCHORED_V1 | 50647 | 0.1757 | 0.5276 | 0.0155 | 0.4271 | 0.4417 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
