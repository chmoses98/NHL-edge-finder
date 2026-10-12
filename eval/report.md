# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-12T01:04:18Z · rows 246109 · pregame 246109 · new 3001

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 44675 | 0.1688 | 0.5076 | 0.0110 | 0.4510 | 0.4534 |
| ALL | MARKET_BASELINE | 205305 | 0.1497 | 0.4603 | 0.0088 | 0.2915 | 0.2925 |
| ALL | MARKET_ANCHORED_V1 | 44661 | 0.1656 | 0.4993 | 0.0106 | 0.4537 | 0.4535 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10048 | 0.0394 | 0.1694 | 0.0050 | 0.0383 | 0.0411 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7148 | 0.1869 | 0.5574 | 0.0416 | 0.2318 | 0.2690 |
| game_spread | MARKET_BASELINE | 7148 | 0.1804 | 0.5408 | 0.0372 | 0.2420 | 0.2690 |
| game_spread | MARKET_ANCHORED_V1 | 7148 | 0.1813 | 0.5431 | 0.0328 | 0.2394 | 0.2690 |
| game_total | DATA_ONLY_V1 | 16083 | 0.1311 | 0.4099 | 0.0205 | 0.5701 | 0.5632 |
| game_total | MARKET_BASELINE | 16083 | 0.1284 | 0.4025 | 0.0249 | 0.5726 | 0.5632 |
| game_total | MARKET_ANCHORED_V1 | 16083 | 0.1288 | 0.4036 | 0.0252 | 0.5721 | 0.5632 |
| game_winner | DATA_ONLY_V1 | 3574 | 0.2309 | 0.6544 | 0.1064 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3574 | 0.2263 | 0.6440 | 0.0443 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3574 | 0.2266 | 0.6449 | 0.0375 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 770 | 0.2531 | 0.7006 | 0.0932 | 0.4222 | 0.4221 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10212 | 0.1484 | 0.4765 | 0.0505 | 0.1306 | 0.1798 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 15894 | 0.1847 | 0.5493 | 0.0258 | 0.5950 | 0.6044 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 15912 | 0.2172 | 0.6251 | 0.0214 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 27747 | 0.1532 | 0.4709 | 0.0196 | 0.2360 | 0.2289 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 45570 | 0.1058 | 0.3514 | 0.0093 | 0.1292 | 0.1311 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 34491 | 0.1677 | 0.5042 | 0.0159 | 0.3011 | 0.2897 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 17870 | 0.1831 | 0.5462 | 0.0344 | 0.4216 | 0.4190 |
| team_total | MARKET_BASELINE | 17856 | 0.1798 | 0.5378 | 0.0299 | 0.4242 | 0.4192 |
| team_total | MARKET_ANCHORED_V1 | 17856 | 0.1802 | 0.5388 | 0.0297 | 0.4236 | 0.4192 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
