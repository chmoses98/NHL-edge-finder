# NHL evaluation report — RESEARCH_ONLY

evaluated 2026-10-09T04:54:43Z · rows 179206 · pregame 179206 · new 3132

| scope | view | n | Brier | log loss | ECE | mean p | hit rate |
|---|---|---:|---:|---:|---:|---:|---:|
| ALL | DATA_ONLY_V1 | 33875 | 0.1680 | 0.5048 | 0.0130 | 0.4496 | 0.4609 |
| ALL | MARKET_BASELINE | 152771 | 0.1517 | 0.4658 | 0.0105 | 0.2928 | 0.3005 |
| ALL | MARKET_ANCHORED_V1 | 33863 | 0.1653 | 0.4975 | 0.0106 | 0.4530 | 0.4611 |
| first_goal | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| first_goal | MARKET_BASELINE | 8479 | 0.0407 | 0.1742 | 0.0075 | 0.0372 | 0.0425 |
| first_goal | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| game_spread | DATA_ONLY_V1 | 5420 | 0.1836 | 0.5483 | 0.0428 | 0.2311 | 0.2673 |
| game_spread | MARKET_BASELINE | 5420 | 0.1784 | 0.5355 | 0.0382 | 0.2415 | 0.2673 |
| game_spread | MARKET_ANCHORED_V1 | 5420 | 0.1791 | 0.5371 | 0.0355 | 0.2390 | 0.2673 |
| game_total | DATA_ONLY_V1 | 12195 | 0.1286 | 0.4021 | 0.0212 | 0.5683 | 0.5728 |
| game_total | MARKET_BASELINE | 12195 | 0.1262 | 0.3947 | 0.0250 | 0.5720 | 0.5728 |
| game_total | MARKET_ANCHORED_V1 | 12195 | 0.1265 | 0.3958 | 0.0248 | 0.5712 | 0.5728 |
| game_winner | DATA_ONLY_V1 | 2710 | 0.2321 | 0.6566 | 0.0812 | 0.5000 | 0.5000 |
| game_winner | MARKET_BASELINE | 2710 | 0.2288 | 0.6490 | 0.0619 | 0.4993 | 0.5000 |
| game_winner | MARKET_ANCHORED_V1 | 2710 | 0.2288 | 0.6492 | 0.0342 | 0.4994 | 0.5000 |
| goalie_saves | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| goalie_saves | MARKET_BASELINE | 593 | 0.2544 | 0.7029 | 0.0651 | 0.4157 | 0.4570 |
| goalie_saves | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_spread | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_spread | MARKET_BASELINE | 7709 | 0.1514 | 0.4828 | 0.0556 | 0.1310 | 0.1848 |
| period_spread | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_total | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_total | MARKET_BASELINE | 12024 | 0.1814 | 0.5400 | 0.0329 | 0.5943 | 0.6178 |
| period_total | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| period_winner | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| period_winner | MARKET_BASELINE | 12042 | 0.2160 | 0.6227 | 0.0325 | 0.3284 | 0.3334 |
| period_winner | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_assists | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_assists | MARKET_BASELINE | 20013 | 0.1576 | 0.4825 | 0.0173 | 0.2365 | 0.2364 |
| player_assists | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_goals | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_goals | MARKET_BASELINE | 33552 | 0.1103 | 0.3656 | 0.0096 | 0.1319 | 0.1377 |
| player_goals | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| player_points | DATA_ONLY_V1 | 0 |  |  |  |  |  |
| player_points | MARKET_BASELINE | 24496 | 0.1750 | 0.5231 | 0.0202 | 0.3070 | 0.3039 |
| player_points | MARKET_ANCHORED_V1 | 0 |  |  |  |  |  |
| team_total | DATA_ONLY_V1 | 13550 | 0.1845 | 0.5493 | 0.0267 | 0.4202 | 0.4299 |
| team_total | MARKET_BASELINE | 13538 | 0.1817 | 0.5421 | 0.0306 | 0.4238 | 0.4302 |
| team_total | MARKET_ANCHORED_V1 | 13538 | 0.1820 | 0.5429 | 0.0286 | 0.4230 | 0.4302 |

The market is the benchmark. If MARKET_BASELINE scores better than DATA_ONLY_V1, that is the finding. Small samples prove nothing.
