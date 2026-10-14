# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-14T03:06:08Z · rows 280771 · pregame 280771 · new 10955

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 51350 | 0.1670 | 0.5032 | 0.0150 | 0.4491 | 0.4587 |
| ALL | MARKET_BASELINE | 234933 | 0.1496 | 0.4600 | 0.0095 | 0.2913 | 0.2947 |
| ALL | MARKET_ANCHORED_V1 | 51336 | 0.1644 | 0.4964 | 0.0131 | 0.4528 | 0.4588 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 11017 | 0.0399 | 0.1708 | 0.0050 | 0.0388 | 0.0418 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 8216 | 0.1875 | 0.5591 | 0.0418 | 0.2313 | 0.2692 |
| game_spread | MARKET_BASELINE | 8216 | 0.1829 | 0.5474 | 0.0353 | 0.2415 | 0.2692 |
| game_spread | MARKET_ANCHORED_V1 | 8216 | 0.1834 | 0.5487 | 0.0336 | 0.2389 | 0.2692 |
| game_total | DATA_ONLY_V1 | 18486 | 0.1295 | 0.4055 | 0.0202 | 0.5676 | 0.5726 |
| game_total | MARKET_BASELINE | 18486 | 0.1268 | 0.3980 | 0.0257 | 0.5718 | 0.5726 |
| game_total | MARKET_ANCHORED_V1 | 18486 | 0.1272 | 0.3991 | 0.0243 | 0.5710 | 0.5726 |
| game_winner | DATA_ONLY_V1 | 4108 | 0.2304 | 0.6534 | 0.1049 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 4108 | 0.2282 | 0.6478 | 0.0680 | 0.4991 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 4108 | 0.2280 | 0.6477 | 0.0470 | 0.4993 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 937 | 0.2475 | 0.6891 | 0.0889 | 0.4248 | 0.4013 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 11813 | 0.1458 | 0.4696 | 0.0474 | 0.1301 | 0.1762 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 18297 | 0.1826 | 0.5435 | 0.0277 | 0.5944 | 0.6107 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 18315 | 0.2171 | 0.6251 | 0.0209 | 0.3281 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 31899 | 0.1523 | 0.4682 | 0.0196 | 0.2333 | 0.2274 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 51336 | 0.1057 | 0.3511 | 0.0114 | 0.1280 | 0.1309 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 39983 | 0.1680 | 0.5053 | 0.0147 | 0.2971 | 0.2876 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 20540 | 0.1799 | 0.5387 | 0.0262 | 0.4194 | 0.4238 |
| team_total | MARKET_BASELINE | 20526 | 0.1772 | 0.5322 | 0.0284 | 0.4235 | 0.4240 |
| team_total | MARKET_ANCHORED_V1 | 20526 | 0.1775 | 0.5328 | 0.0318 | 0.4226 | 0.4240 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
