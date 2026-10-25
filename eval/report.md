# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-25T04:14:13Z · rows 568211 · pregame 568211 · new 5763

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 97250 | 0.1641 | 0.4949 | 0.0189 | 0.4497 | 0.4673 |
| ALL | MARKET_BASELINE | 471195 | 0.1481 | 0.4556 | 0.0090 | 0.2862 | 0.2942 |
| ALL | MARKET_ANCHORED_V1 | 97225 | 0.1620 | 0.4896 | 0.0159 | 0.4557 | 0.4674 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 23262 | 0.0387 | 0.1663 | 0.0030 | 0.0389 | 0.0404 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 15560 | 0.1820 | 0.5473 | 0.0246 | 0.2314 | 0.2541 |
| game_spread | MARKET_BASELINE | 15560 | 0.1779 | 0.5359 | 0.0195 | 0.2427 | 0.2541 |
| game_spread | MARKET_ANCHORED_V1 | 15560 | 0.1784 | 0.5372 | 0.0180 | 0.2400 | 0.2541 |
| game_total | DATA_ONLY_V1 | 35010 | 0.1280 | 0.3995 | 0.0289 | 0.5684 | 0.5891 |
| game_total | MARKET_BASELINE | 35010 | 0.1267 | 0.3958 | 0.0284 | 0.5765 | 0.5891 |
| game_total | MARKET_ANCHORED_V1 | 35010 | 0.1268 | 0.3961 | 0.0272 | 0.5749 | 0.5891 |
| game_winner | DATA_ONLY_V1 | 7780 | 0.2321 | 0.6567 | 0.0902 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 7780 | 0.2291 | 0.6497 | 0.0292 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 7780 | 0.2291 | 0.6499 | 0.0422 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 2162 | 0.2531 | 0.6998 | 0.0532 | 0.4443 | 0.4542 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 22226 | 0.1362 | 0.4443 | 0.0355 | 0.1288 | 0.1637 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 34821 | 0.1811 | 0.5393 | 0.0265 | 0.5989 | 0.6234 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 34839 | 0.2173 | 0.6253 | 0.0203 | 0.3279 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 66804 | 0.1573 | 0.4808 | 0.0149 | 0.2328 | 0.2341 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 103031 | 0.1037 | 0.3445 | 0.0075 | 0.1238 | 0.1298 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 86825 | 0.1673 | 0.5032 | 0.0093 | 0.2886 | 0.2910 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 38900 | 0.1757 | 0.5276 | 0.0174 | 0.4202 | 0.4365 |
| team_total | MARKET_BASELINE | 38875 | 0.1734 | 0.5221 | 0.0199 | 0.4274 | 0.4368 |
| team_total | MARKET_ANCHORED_V1 | 38875 | 0.1736 | 0.5225 | 0.0187 | 0.4259 | 0.4368 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
