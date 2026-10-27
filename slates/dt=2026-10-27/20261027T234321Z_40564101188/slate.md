# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-27T23:43:21Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 10 · markets on board: 4645 · contracts joined: 2463 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2213, 'OK': 140, 'NO_EDGE': 110}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 391, 'game_early_goal': 10, 'first_goal': 368, 'game_winner': 20, 'player_goals': 640, 'game_overtime': 10, 'player_points': 536, 'goalie_saves': 18, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ CAR | 2026-10-28T00:00:00Z | T-10m | 0.572 | 0.428 | 0.179 | 6.06 | 3.26 | 2.80 | 239 (25/214) | CONFIRMED/CONFIRMED |
| LAK @ CHI | 2026-10-28T00:00:00Z | T-10m | 0.501 | 0.499 | 0.191 | 5.53 | 2.77 | 2.76 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MTL @ STL | 2026-10-28T00:00:00Z | T-10m | 0.465 | 0.535 | 0.172 | 6.57 | 3.17 | 3.39 | 249 (25/224) | CONFIRMED/CONFIRMED |
| NYI @ NSH | 2026-10-28T00:00:00Z | T-10m | 0.519 | 0.481 | 0.178 | 6.16 | 3.14 | 3.03 | 231 (25/206) | CONFIRMED/CONFIRMED |
| NJD @ DAL | 2026-10-28T00:00:00Z | T-10m | 0.561 | 0.439 | 0.187 | 5.58 | 2.97 | 2.61 | 257 (25/232) | CONFIRMED/CONFIRMED |
| FLA @ WPG | 2026-10-28T00:00:00Z | T-10m | 0.525 | 0.475 | 0.184 | 5.99 | 3.08 | 2.92 | 267 (25/242) | CONFIRMED/CONFIRMED |
| MIN @ UTA | 2026-10-28T01:00:00Z | T-60m | 0.535 | 0.465 | 0.173 | 6.21 | 3.21 | 3.00 | 238 (25/213) | CONFIRMED/CONFIRMED |
| OTT @ VGK | 2026-10-28T02:00:00Z | T-90m | 0.572 | 0.428 | 0.163 | 6.68 | 3.57 | 3.11 | 239 (25/214) | CONFIRMED/CONFIRMED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-90m | 0.632 | 0.368 | 0.159 | 6.81 | 3.85 | 2.96 | 250 (25/225) | CONFIRMED/PROJECTED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-90m | 0.463 | 0.537 | 0.171 | 6.74 | 3.25 | 3.50 | 272 (25/247) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT27LACHI-6 | game_total | 0.446 | 0.555 | 0.533 | 56 | 45 | no | +0.087 | OK |
| KXNHLTOTAL-26OCT27LACHI-5 | game_total | 0.679 | 0.775 | 0.758 | 78 | 23 | no | +0.079 | OK |
| KXNHLTOTAL-26OCT27LACHI-7 | game_total | 0.335 | 0.435 | 0.414 | 44 | 57 | no | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA4 | team_total | 0.339 | 0.430 | 0.411 | 44 | 58 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT27LACHI-4 | game_total | 0.783 | 0.860 | 0.847 | 87 | 15 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR4 | team_total | 0.422 | 0.505 | 0.488 | 52 | 51 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA3 | team_total | 0.534 | 0.610 | 0.595 | 62 | 40 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT27LACHI-8 | game_total | 0.169 | 0.235 | 0.221 | 24 | 77 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR3 | game_spread | 0.218 | 0.285 | 0.271 | 29 | 72 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI4 | team_total | 0.306 | 0.375 | 0.361 | 38 | 63 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR3 | team_total | 0.639 | 0.710 | 0.696 | 72 | 30 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA3 | game_spread | 0.144 | 0.210 | 0.195 | 22 | 80 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI3 | team_total | 0.531 | 0.595 | 0.582 | 60 | 41 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA4 | team_total | 0.311 | 0.375 | 0.362 | 38 | 63 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ4 | team_total | 0.273 | 0.340 | 0.326 | 35 | 67 | no | +0.042 | OK |
| KXNHLGAME-26OCT27BOSCAR-BOS | game_winner | 0.428 | 0.365 | 0.377 | 37 | 64 | yes | +0.042 | OK |
| KXNHLGAME-26OCT27BOSCAR-CAR | game_winner | 0.572 | 0.635 | 0.623 | 64 | 37 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR5 | team_total | 0.234 | 0.300 | 0.286 | 31 | 71 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA2 | team_total | 0.758 | 0.815 | 0.805 | 82 | 19 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR2 | game_spread | 0.342 | 0.405 | 0.392 | 41 | 60 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA3 | team_total | 0.564 | 0.630 | 0.617 | 64 | 38 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA2 | game_spread | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA2 | team_total | 0.782 | 0.835 | 0.825 | 84 | 17 | no | +0.039 | OK |
| KXNHLGAME-26OCT27FLAWPG-FLA | game_winner | 0.475 | 0.535 | 0.523 | 54 | 47 | no | +0.038 | OK |
| KXNHLGAME-26OCT27FLAWPG-WPG | game_winner | 0.525 | 0.465 | 0.477 | 47 | 54 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT27LACHI-9 | game_total | 0.114 | 0.165 | 0.153 | 17 | 84 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ3 | team_total | 0.497 | 0.560 | 0.547 | 57 | 45 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA5 | team_total | 0.174 | 0.230 | 0.218 | 24 | 78 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-5 | game_total | 0.755 | 0.805 | 0.796 | 81 | 20 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT27NJDAL-5 | game_total | 0.693 | 0.750 | 0.739 | 76 | 26 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ3 | game_spread | 0.120 | 0.165 | 0.155 | 17 | 84 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI5 | team_total | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR2 | team_total | 0.833 | 0.885 | 0.876 | 90 | 13 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-10 | game_total | 0.114 | 0.075 | 0.082 | 8 | 93 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-8 | game_total | 0.312 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI2 | team_total | 0.761 | 0.805 | 0.797 | 81 | 20 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-6 | game_total | 0.535 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-7 | game_total | 0.524 | 0.475 | 0.485 | 48 | 53 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-9 | game_total | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.026 | OK |
| KXNHLGAME-26OCT27BUFSJ-SJ | game_winner | 0.463 | 0.415 | 0.425 | 42 | 59 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-7 | game_total | 0.427 | 0.475 | 0.465 | 48 | 53 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA5 | team_total | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR6 | team_total | 0.107 | 0.145 | 0.137 | 15 | 86 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ2 | game_spread | 0.223 | 0.265 | 0.256 | 27 | 74 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27NJDAL-8 | game_total | 0.176 | 0.215 | 0.207 | 22 | 79 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-9 | game_total | 0.243 | 0.200 | 0.208 | 21 | 81 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.322 | 0.365 | 0.356 | 37 | 64 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT5 | team_total | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-BOS2 | game_spread | 0.221 | 0.185 | 0.192 | 19 | 82 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-4 | game_total | 0.842 | 0.880 | 0.873 | 89 | 13 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT27NJDAL-7 | game_total | 0.344 | 0.385 | 0.377 | 39 | 62 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT27VANANA-ANA3 | game_spread | 0.285 | 0.325 | 0.317 | 33 | 68 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-6 | game_total | 0.635 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT27NJDAL-6 | game_total | 0.454 | 0.495 | 0.487 | 50 | 51 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT27LACHI-CHI3 | game_spread | 0.151 | 0.185 | 0.178 | 19 | 82 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT27MINUTA-5 | game_total | 0.771 | 0.810 | 0.803 | 82 | 20 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-4 | game_total | 0.834 | 0.870 | 0.863 | 88 | 14 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL5 | team_total | 0.260 | 0.220 | 0.228 | 23 | 79 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT27LACHI-3 | game_total | 0.940 | 0.965 | 0.961 | 97 | 4 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN5 | team_total | 0.186 | 0.150 | 0.157 | 16 | 86 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT27MINUTA-6 | game_total | 0.556 | 0.600 | 0.591 | 61 | 41 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-6 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL3 | team_total | 0.662 | 0.625 | 0.633 | 63 | 38 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL4 | team_total | 0.453 | 0.410 | 0.419 | 42 | 60 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT3 | team_total | 0.603 | 0.560 | 0.569 | 57 | 45 | yes | +0.016 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ2 | team_total | 0.731 | 0.775 | 0.767 | 79 | 24 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-7 | game_total | 0.417 | 0.455 | 0.447 | 46 | 55 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27NJDAL-9 | game_total | 0.116 | 0.145 | 0.139 | 15 | 86 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT27MINUTA-7 | game_total | 0.447 | 0.485 | 0.477 | 49 | 52 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ5 | team_total | 0.126 | 0.160 | 0.153 | 17 | 85 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-WPG2 | game_spread | 0.299 | 0.265 | 0.272 | 27 | 74 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-8 | game_total | 0.329 | 0.295 | 0.302 | 30 | 71 | yes | +0.015 | OK |
| KXNHLGAME-26OCT27NJDAL-DAL | game_winner | 0.561 | 0.525 | 0.532 | 53 | 48 | yes | +0.014 | OK |
| KXNHLGAME-26OCT27NJDAL-NJ | game_winner | 0.439 | 0.475 | 0.468 | 48 | 53 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT27NJDAL-4 | game_total | 0.796 | 0.830 | 0.824 | 84 | 18 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF3 | team_total | 0.682 | 0.715 | 0.709 | 72 | 29 | no | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ CAR | 0.572 | 0.562 | 0.179 | 0.208 | 6.06 | 6.66 | 1.003/0.956 | KXNHLTOTAL-26OCT27BOSCAR-7 +0.101 |
| LAK @ CHI | 0.501 | 0.477 | 0.191 | 0.223 | 5.53 | 5.97 | 0.988/0.987 | KXNHLTOTAL-26OCT27LACHI-7 +0.078 |
| MTL @ STL | 0.465 | 0.567 | 0.172 | 0.213 | 6.57 | 6.54 | 1.032/0.983 | KXNHLGAME-26OCT27MTLSTL-MTL -0.103 |
| NYI @ NSH | 0.519 | 0.529 | 0.178 | 0.218 | 6.16 | 6.38 | 1.004/0.978 | KXNHLTOTAL-26OCT27NYINSH-7 +0.037 |
| NJD @ DAL | 0.561 | 0.553 | 0.187 | 0.229 | 5.58 | 5.89 | 0.968/0.949 | KXNHLTOTAL-26OCT27NJDAL-7 +0.059 |
| FLA @ WPG | 0.525 | 0.530 | 0.184 | 0.224 | 5.99 | 6.11 | 0.997/0.991 | KXNHLTOTAL-26OCT27FLAWPG-5 +0.022 |
| MIN @ UTA | 0.535 | 0.566 | 0.173 | 0.213 | 6.21 | 6.40 | 0.989/0.991 | KXNHLTEAMTOTAL-26OCT27MINUTA-UTA4 +0.049 |
| OTT @ VGK | 0.572 | 0.581 | 0.163 | 0.213 | 6.68 | 6.30 | 1.004/1.040 | KXNHLTOTAL-26OCT27OTTVGK-6 -0.062 |
| VAN @ ANA | 0.632 | 0.602 | 0.159 | 0.204 | 6.81 | 6.78 | 1.016/1.026 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.039 |
| BUF @ SJS | 0.463 | 0.524 | 0.171 | 0.214 | 6.74 | 6.52 | 1.039/0.999 | KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 -0.069 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 39 recommended · full analysis in card.md / packet.json `thesis_card`

- Casey Mittelstadt: 1+ goals YES @ 12c · p 0.1835 (adj 0.1664) · $4.23 · thesis BOS:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 21c · p 0.2764 (adj 0.256) · $4.34 · thesis BOS:OFFENSE_4PLUS
- William Borgen: 1+ goals YES @ 4c · p 0.0627 (adj 0.0558) · $1.22 · thesis BOS:WINS_BY_2PLUS
- Mark Kastelic: 1+ goals YES @ 8c · p 0.1106 (adj 0.1017) · $1.77 · thesis BOS:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0755 (adj 0.0679) · $1.49 · thesis LAK:WINS_BY_2PLUS
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7958 (adj 0.7806) · $7.62 · thesis CHI:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 55c · p 0.6938 (adj 0.5938) · $5.07 · thesis CHI:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 52c · p 0.6059 (adj 0.5579) · $5.42 · thesis LAK:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 28c · p 0.3566 (adj 0.3362) · $5.75 · thesis STL:OFFENSE_4PLUS
- Robert Thomas: 2+ goals YES @ 3c · p 0.0556 (adj 0.0479) · $1.03 · thesis STL:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.3059 (adj 0.2882) · $3.37 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 14c · p 0.1867 (adj 0.1725) · $2.55 · thesis STL:OFFENSE_4PLUS
- Adam Wilsby: 1+ assists YES @ 22c · p 0.3084 (adj 0.2617) · $3.64 · thesis NSH:OFFENSE_4PLUS
- Victor Eklund: 1+ assists NO @ 72c · p 0.7969 (adj 0.756) · $8.46 · thesis NYI:SUPPRESSED
- Victor Eklund: 1+ goals YES @ 17c · p 0.2069 (adj 0.1964) · $2.03 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 22c · p 0.2612 (adj 0.2496) · $3.01 · thesis NYI:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1232 (adj 0.1137) · $1.94 · thesis NJD:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 26c · p 0.3058 (adj 0.2931) · $2.86 · thesis DAL:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1373 (adj 0.1292) · $1.41 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 68c · p 0.7228 (adj 0.7108) · $5.5 · thesis NJD:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 65c · p 0.7201 (adj 0.7013) · $8.46 · thesis FLA:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1716 (adj 0.16) · $2.57 · thesis WPG:OFFENSE_4PLUS
- Adam Lowry: 1+ goals YES @ 11c · p 0.145 (adj 0.135) · $2.01 · thesis WPG:OFFENSE_4PLUS
- Cole Schwindt: 1+ goals YES @ 9c · p 0.1179 (adj 0.1097) · $1.54 · thesis FLA:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 56c · p 0.6421 (adj 0.6203) · $8.46 · thesis MIN:SUPPRESSED
- Anders Lee: 1+ goals YES @ 20c · p 0.2453 (adj 0.2327) · $2.73 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1562 (adj 0.1447) · $1.9 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 19c · p 0.235 (adj 0.2213) · $2.6 · thesis UTA:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 46c · p 0.6073 (adj 0.5083) · $6.86 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0859 (adj 0.0782) · $1.48 · thesis VGK:OFFENSE_4PLUS
- Jonas Johansson: 28+ saves NO @ 61c · p 0.773 (adj 0.647) · $7.74 · thesis OTT:NET_LOW_VOLUME
- Michael Amadio: 1+ goals YES @ 13c · p 0.1607 (adj 0.1518) · $1.62 · thesis OTT:OFFENSE_4PLUS
- Filip Chytil: 1+ goals YES @ 18c · p 0.2344 (adj 0.2195) · $3.58 · thesis VAN:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 17c · p 0.2693 (adj 0.2015) · $1.38 · thesis ANA:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2116 (adj 0.1987) · $2.31 · thesis VAN:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1747 (adj 0.1623) · $2.66 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 61c · p 0.6756 (adj 0.658) · $8.24 · thesis BUF:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 22c · p 0.2695 (adj 0.2559) · $3.33 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 65c · p 0.7344 (adj 0.6847) · $6.92 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BOS @ CAR** · priced 181/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 23.29, exp saves 20.31 (sd 5.89), pull risk 0.067
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 32.38, exp saves 27.61 (sd 7.59), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.381 | 0.475 | 48/53 | +0.072 | STANDARD |
| Jeremy Swayman: 30+ saves | 0.398 | 0.480 | 51/55 | +0.035 |  |
| Seth Jarvis: 1+ assists | 0.263 | 0.345 | 36/67 | +0.051 | STANDARD |
| Pavel Zacha: 1+ goals | 0.276 | 0.195 | 21/82 | +0.055 | STANDARD |
| Casey Mittelstadt: 1+ points | 0.400 | 0.325 | 33/68 | +0.055 | STANDARD |
| Sean Walker: 1+ points | 0.378 | 0.305 | 31/70 | +0.053 | STANDARD |

**LAK @ CHI** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 28.78, exp saves 24.88 (sd 6.74), pull risk 0.057
- LAK net: Anton Forsberg (CONFIRMED) exp shots 25.18, exp saves 21.94 (sd 6.13), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.306 | 0.460 | 47/55 | +0.126 | STANDARD |
| Patrick Kane: 1+ points | 0.470 | 0.590 | 60/42 | +0.093 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.260 | 0.375 | 38/63 | +0.094 | STANDARD |
| Connor Bedard: 1+ assists | 0.372 | 0.475 | 48/53 | +0.080 | STANDARD |
| Artemi Panarin: 1+ assists | 0.394 | 0.490 | 50/52 | +0.068 | STANDARD |
| Connor Bedard: 1+ points | 0.548 | 0.640 | 65/37 | +0.065 | STANDARD |

**MTL @ STL** · priced 193/198 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 26.31, exp saves 22.93 (sd 6.47), pull risk 0.058
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.26, exp saves 23.12 (sd 6.58), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ points | 0.440 | 0.305 | 33/72 | +0.095 | STANDARD |
| Justin Barron: 1+ points | 0.281 | 0.160 | 25/93 | +0.017 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.325 | 0.220 | 23/79 | +0.082 | STANDARD |
| Justin Barron: 1+ assists | 0.226 | 0.130 | 19/93 | +0.025 | STANDARD |
| Jake Neighbours: 1+ assists | 0.333 | 0.240 | 25/77 | +0.070 | STANDARD |
| Brandon Carlo: 1+ points | 0.200 | 0.110 | 15/93 | +0.041 | STANDARD |

**NYI @ NSH** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.8, exp saves 24.82 (sd 6.84), pull risk 0.064
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 27.04, exp saves 23.32 (sd 6.56), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ points | 0.362 | 0.260 | 27/75 | +0.078 | STANDARD |
| Adam Wilsby: 1+ assists | 0.308 | 0.215 | 22/79 | +0.076 | STANDARD |
| Emil Heineman: 1+ assists | 0.282 | 0.200 | 21/81 | +0.060 | STANDARD |
| Victor Eklund: 1+ assists | 0.203 | 0.285 | 29/72 | +0.063 | STANDARD |
| Simon Holmstrom: 1+ assists | 0.351 | 0.280 | 29/73 | +0.046 | STANDARD |
| Matthew Wood: 1+ points | 0.394 | 0.330 | 34/68 | +0.038 | STANDARD |

**NJD @ DAL** · priced 194/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Casey DeSmith (CONFIRMED) exp shots 26.96, exp saves 23.52 (sd 6.41), pull risk 0.052
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.01, exp saves 22.56 (sd 6.28), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cody Glass: 1+ points | 0.279 | 0.145 | 20/91 | +0.068 | STANDARD |
| Justin Hryckowian: 1+ assists | 0.257 | 0.125 | 18/93 | +0.066 | STANDARD |
| Luke Evangelista: 1+ assists | 0.206 | 0.320 | 33/69 | +0.089 | STANDARD |
| Justin Hryckowian: 1+ points | 0.363 | 0.255 | 28/77 | +0.069 | STANDARD |
| Colin Blackwell: 1+ points | 0.216 | 0.115 | 16/93 | +0.047 | STANDARD |
| Luke Evangelista: 1+ points | 0.360 | 0.455 | 47/56 | +0.063 | STANDARD |

**FLA @ WPG** · priced 207/216 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (CONFIRMED) exp shots 27.13, exp saves 23.59 (sd 6.44), pull risk 0.056
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.32, exp saves 22.64 (sd 6.37), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Barron: 1+ points | 0.269 | 0.140 | 21/93 | +0.047 | STANDARD |
| Seth Jones: 1+ points | 0.413 | 0.525 | 53/48 | +0.089 | STANDARD |
| Dmitry Kulikov: 1+ points | 0.194 | 0.090 | 15/97 | +0.035 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.436 | 0.535 | 54/47 | +0.077 | STANDARD |
| Morgan Barron: 1+ assists | 0.173 | 0.075 | 12/97 | +0.045 | STANDARD |
| Brady Tkachuk: 2+ points | 0.159 | 0.255 | 26/75 | +0.078 | STANDARD |

**MIN @ UTA** · priced 183/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (CONFIRMED) exp shots 27.66, exp saves 24.14 (sd 6.55), pull risk 0.053
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.67, exp saves 24.59 (sd 6.81), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.252 | 0.405 | 41/60 | +0.131 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.397 | 0.515 | 52/49 | +0.095 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.609 | 0.710 | 73/31 | +0.066 | STANDARD |
| Kailer Yamamoto: 1+ points | 0.434 | 0.340 | 35/67 | +0.068 | STANDARD |
| Quinn Hughes: 1+ assists | 0.512 | 0.605 | 61/40 | +0.071 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.358 | 0.445 | 45/56 | +0.065 | STANDARD |

**OTT @ VGK** · priced 185/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 26.26, exp saves 22.87 (sd 6.3), pull risk 0.054
- OTT net: Jonas Johansson (CONFIRMED) exp shots 26.79, exp saves 22.82 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonas Johansson: 28+ saves | 0.227 | 0.395 | 40/61 | +0.146 |  |
| Mitch Marner: 1+ assists | 0.393 | 0.545 | 55/46 | +0.130 | STANDARD |
| Jake Sanderson: 1+ points | 0.370 | 0.495 | 52/53 | +0.083 | STANDARD |
| Jake Sanderson: 1+ assists | 0.288 | 0.410 | 42/60 | +0.095 | STANDARD |
| Adin Hill: 21+ saves | 0.651 | 0.530 | 56/50 | +0.074 |  |
| Mitch Marner: 1+ points | 0.541 | 0.650 | 66/36 | +0.083 | STANDARD |

**VAN @ ANA** · priced 180/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 23.87, exp saves 20.92 (sd 5.92), pull risk 0.058
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.6, exp saves 26.72 (sd 7.46), pull risk 0.091

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tom Willander: 1+ assists | 0.278 | 0.130 | 24/98 | +0.025 | STANDARD |
| Arshdeep Bains: 1+ points | 0.260 | 0.120 | 22/98 | +0.027 | STANDARD |
| Tim Washe: 1+ points | 0.412 | 0.290 | 30/72 | +0.097 | STANDARD |
| A.J. Greer: 1+ points | 0.435 | 0.320 | 33/69 | +0.089 | STANDARD |
| A.J. Greer: 1+ goals | 0.269 | 0.165 | 17/84 | +0.089 | STANDARD |
| Tim Washe: 1+ assists | 0.303 | 0.200 | 21/81 | +0.082 | STANDARD |

**BUF @ SJS** · priced 218/221 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.51, exp saves 24.68 (sd 6.72), pull risk 0.063
- BUF net: Colten Ellis (PROBABLE) exp shots 27.09, exp saves 23.35 (sd 6.5), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.298 | 0.090 | 17/99 | +0.118 | STANDARD |
| Ivar Stenberg: 1+ points | 0.407 | 0.570 | 58/44 | +0.135 | STANDARD |
| Sam Dickinson: 1+ assists | 0.246 | 0.085 | 15/98 | +0.087 | STANDARD |
| Zack Ostapchuk: 1+ points | 0.236 | 0.090 | 16/98 | +0.067 | STANDARD |
| Barclay Goodrow: 1+ points | 0.230 | 0.100 | 18/98 | +0.039 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.447 | 0.575 | 59/44 | +0.096 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
