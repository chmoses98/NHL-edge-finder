# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-14T01:24:54Z · rows 261926 · pregame 261926 · new 4412

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 47625 | 0.1695 | 0.5094 | 0.0135 | 0.4498 | 0.4583 |
| ALL | MARKET_BASELINE | 218829 | 0.1499 | 0.4608 | 0.0084 | 0.2910 | 0.2940 |
| ALL | MARKET_ANCHORED_V1 | 47611 | 0.1662 | 0.5007 | 0.0114 | 0.4529 | 0.4584 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 10637 | 0.0394 | 0.1693 | 0.0046 | 0.0387 | 0.0412 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 7620 | 0.1893 | 0.5636 | 0.0456 | 0.2315 | 0.2734 |
| game_spread | MARKET_BASELINE | 7620 | 0.1830 | 0.5469 | 0.0382 | 0.2416 | 0.2734 |
| game_spread | MARKET_ANCHORED_V1 | 7620 | 0.1839 | 0.5492 | 0.0373 | 0.2391 | 0.2734 |
| game_total | DATA_ONLY_V1 | 17145 | 0.1320 | 0.4122 | 0.0188 | 0.5685 | 0.5701 |
| game_total | MARKET_BASELINE | 17145 | 0.1290 | 0.4038 | 0.0220 | 0.5718 | 0.5701 |
| game_total | MARKET_ANCHORED_V1 | 17145 | 0.1295 | 0.4051 | 0.0218 | 0.5711 | 0.5701 |
| game_winner | DATA_ONLY_V1 | 3810 | 0.2317 | 0.6560 | 0.0944 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 3810 | 0.2274 | 0.6461 | 0.0610 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 3810 | 0.2276 | 0.6468 | 0.0369 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 844 | 0.2510 | 0.6964 | 0.0930 | 0.4229 | 0.4135 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 10919 | 0.1465 | 0.4718 | 0.0481 | 0.1303 | 0.1771 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 16956 | 0.1852 | 0.5499 | 0.0275 | 0.5943 | 0.6074 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 16974 | 0.2170 | 0.6247 | 0.0238 | 0.3280 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 29614 | 0.1531 | 0.4705 | 0.0195 | 0.2349 | 0.2287 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 48352 | 0.1059 | 0.3512 | 0.0101 | 0.1285 | 0.1316 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 36922 | 0.1683 | 0.5057 | 0.0152 | 0.2995 | 0.2897 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 19050 | 0.1830 | 0.5460 | 0.0331 | 0.4203 | 0.4234 |
| team_total | MARKET_BASELINE | 19036 | 0.1794 | 0.5371 | 0.0295 | 0.4235 | 0.4236 |
| team_total | MARKET_ANCHORED_V1 | 19036 | 0.1799 | 0.5382 | 0.0315 | 0.4228 | 0.4236 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
