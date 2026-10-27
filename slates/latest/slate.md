# NHL slate 2026-10-27 — RESEARCH_ONLY

generated 2026-10-27T22:53:36Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4671 · contracts joined: 2707 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 2432, 'OK': 165, 'NO_EDGE': 110}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 431, 'game_early_goal': 11, 'first_goal': 404, 'game_winner': 22, 'player_goals': 702, 'game_overtime': 11, 'player_points': 589, 'goalie_saves': 20, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 2026-10-27T23:00:00Z | T-<10m | 0.574 | 0.426 | 0.189 | 5.72 | 3.09 | 2.63 | 244 (25/219) | CONFIRMED/CONFIRMED |
| BOS @ CAR | 2026-10-28T00:00:00Z | T-60m | 0.569 | 0.431 | 0.181 | 6.07 | 3.26 | 2.82 | 239 (25/214) | PROBABLE/CONFIRMED |
| LAK @ CHI | 2026-10-28T00:00:00Z | T-60m | 0.501 | 0.499 | 0.195 | 5.55 | 2.78 | 2.76 | 221 (25/196) | CONFIRMED/PROBABLE |
| MTL @ STL | 2026-10-28T00:00:00Z | T-60m | 0.465 | 0.535 | 0.172 | 6.57 | 3.17 | 3.39 | 249 (25/224) | CONFIRMED/CONFIRMED |
| NYI @ NSH | 2026-10-28T00:00:00Z | T-60m | 0.519 | 0.481 | 0.177 | 6.15 | 3.14 | 3.01 | 231 (25/206) | PROBABLE/CONFIRMED |
| NJD @ DAL | 2026-10-28T00:00:00Z | T-60m | 0.561 | 0.439 | 0.187 | 5.58 | 2.97 | 2.61 | 257 (25/232) | CONFIRMED/CONFIRMED |
| FLA @ WPG | 2026-10-28T00:00:00Z | T-60m | 0.525 | 0.475 | 0.184 | 5.99 | 3.08 | 2.92 | 267 (25/242) | CONFIRMED/CONFIRMED |
| MIN @ UTA | 2026-10-28T01:00:00Z | T-90m | 0.535 | 0.465 | 0.173 | 6.21 | 3.21 | 3.00 | 238 (25/213) | CONFIRMED/CONFIRMED |
| OTT @ VGK | 2026-10-28T02:00:00Z | T-3h | 0.572 | 0.428 | 0.163 | 6.68 | 3.57 | 3.11 | 239 (25/214) | CONFIRMED/CONFIRMED |
| VAN @ ANA | 2026-10-28T02:00:00Z | T-3h | 0.632 | 0.368 | 0.159 | 6.81 | 3.85 | 2.96 | 250 (25/225) | CONFIRMED/PROJECTED |
| BUF @ SJS | 2026-10-28T02:30:00Z | T-3h | 0.463 | 0.537 | 0.171 | 6.74 | 3.25 | 3.50 | 272 (25/247) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT27LACHI-6 | game_total | 0.446 | 0.555 | 0.533 | 56 | 45 | no | +0.087 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ3 | team_total | 0.496 | 0.595 | 0.576 | 60 | 41 | no | +0.077 | OK |
| KXNHLGAME-26OCT27CBJPHI-CBJ | game_winner | 0.426 | 0.525 | 0.505 | 53 | 48 | no | +0.077 | OK |
| KXNHLGAME-26OCT27CBJPHI-PHI | game_winner | 0.574 | 0.475 | 0.495 | 48 | 53 | yes | +0.077 | OK |
| KXNHLTOTAL-26OCT27LACHI-5 | game_total | 0.683 | 0.775 | 0.758 | 78 | 23 | no | +0.075 | OK |
| KXNHLTOTAL-26OCT27LACHI-7 | game_total | 0.340 | 0.435 | 0.415 | 44 | 57 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ4 | team_total | 0.281 | 0.375 | 0.355 | 38 | 63 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ2 | game_spread | 0.213 | 0.305 | 0.285 | 31 | 70 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA4 | team_total | 0.339 | 0.430 | 0.411 | 44 | 58 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-CBJ3 | game_spread | 0.116 | 0.195 | 0.176 | 20 | 81 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ2 | team_total | 0.731 | 0.805 | 0.792 | 81 | 20 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-PHI2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT27LACHI-4 | game_total | 0.788 | 0.855 | 0.843 | 86 | 15 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR3 | game_spread | 0.214 | 0.285 | 0.270 | 29 | 72 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ5 | team_total | 0.128 | 0.195 | 0.180 | 20 | 81 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR4 | team_total | 0.422 | 0.500 | 0.484 | 51 | 51 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA3 | team_total | 0.564 | 0.640 | 0.625 | 65 | 37 | no | +0.050 | OK |
| KXNHLGAME-26OCT27FLAWPG-WPG | game_winner | 0.525 | 0.455 | 0.469 | 46 | 55 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR3 | team_total | 0.638 | 0.710 | 0.696 | 72 | 30 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA3 | team_total | 0.537 | 0.610 | 0.596 | 62 | 40 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ3 | team_total | 0.497 | 0.570 | 0.555 | 58 | 44 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT27LACHI-8 | game_total | 0.172 | 0.235 | 0.221 | 24 | 77 | no | +0.046 | OK |
| KXNHLGAME-26OCT27BOSCAR-BOS | game_winner | 0.431 | 0.365 | 0.378 | 37 | 64 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA3 | game_spread | 0.144 | 0.210 | 0.195 | 22 | 80 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT27NJDAL-5 | game_total | 0.693 | 0.755 | 0.743 | 76 | 25 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR5 | team_total | 0.233 | 0.300 | 0.286 | 31 | 71 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA4 | team_total | 0.311 | 0.380 | 0.366 | 39 | 63 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ4 | team_total | 0.273 | 0.345 | 0.330 | 36 | 67 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI4 | team_total | 0.312 | 0.375 | 0.362 | 38 | 63 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ3 | game_spread | 0.120 | 0.175 | 0.163 | 18 | 83 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR2 | team_total | 0.833 | 0.885 | 0.876 | 89 | 12 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA2 | team_total | 0.759 | 0.815 | 0.805 | 82 | 19 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT27FLAWPG-FLA2 | game_spread | 0.256 | 0.315 | 0.303 | 32 | 69 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-CAR2 | game_spread | 0.344 | 0.405 | 0.392 | 41 | 60 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA2 | team_total | 0.782 | 0.840 | 0.829 | 85 | 17 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI3 | team_total | 0.535 | 0.595 | 0.583 | 60 | 41 | no | +0.038 | OK |
| KXNHLGAME-26OCT27FLAWPG-FLA | game_winner | 0.475 | 0.535 | 0.523 | 54 | 47 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ2 | team_total | 0.731 | 0.785 | 0.775 | 79 | 22 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT27LACHI-9 | game_total | 0.115 | 0.165 | 0.154 | 17 | 84 | no | +0.036 | OK |
| KXNHLGAME-26OCT27BOSCAR-CAR | game_winner | 0.569 | 0.625 | 0.614 | 63 | 38 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT27FLAWPG-FLA5 | team_total | 0.174 | 0.230 | 0.218 | 24 | 78 | no | +0.034 | OK |
| KXNHLGAME-26OCT27NJDAL-NJ | game_winner | 0.439 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT27NJDAL-NJ2 | game_spread | 0.223 | 0.275 | 0.264 | 28 | 73 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI5 | team_total | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-10 | game_total | 0.114 | 0.075 | 0.082 | 8 | 93 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT27MTLSTL-8 | game_total | 0.312 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT27CBJPHI-PHI3 | game_spread | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-CHI2 | team_total | 0.762 | 0.805 | 0.797 | 81 | 20 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-5 | game_total | 0.711 | 0.755 | 0.747 | 76 | 25 | no | +0.026 | OK |
| KXNHLGAME-26OCT27BUFSJ-SJ | game_winner | 0.463 | 0.415 | 0.425 | 42 | 59 | yes | +0.026 | OK |
| KXNHLGAME-26OCT27BUFSJ-BUF | game_winner | 0.537 | 0.585 | 0.575 | 59 | 42 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-7 | game_total | 0.417 | 0.465 | 0.455 | 47 | 54 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT27LACHI-LA5 | team_total | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT27NJDAL-NJ5 | team_total | 0.126 | 0.170 | 0.160 | 18 | 84 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF3 | game_spread | 0.203 | 0.245 | 0.236 | 25 | 76 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27NJDAL-4 | game_total | 0.796 | 0.840 | 0.832 | 85 | 17 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT27BOSCAR-BOS2 | game_spread | 0.225 | 0.185 | 0.192 | 19 | 82 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT27CBJPHI-4 | game_total | 0.807 | 0.845 | 0.838 | 85 | 16 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLGAME-26OCT27NJDAL-DAL | game_winner | 0.561 | 0.515 | 0.524 | 52 | 49 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT27BOSCAR-CAR6 | team_total | 0.109 | 0.145 | 0.137 | 15 | 86 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-6 | game_total | 0.541 | 0.585 | 0.576 | 59 | 42 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT27BUFSJ-BUF2 | game_spread | 0.322 | 0.365 | 0.356 | 37 | 64 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT27OTTVGK-OTT5 | team_total | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT27LACHI-LA3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-5 | game_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL6 | team_total | 0.127 | 0.090 | 0.096 | 10 | 92 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT27NJDAL-7 | game_total | 0.344 | 0.385 | 0.377 | 39 | 62 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT27VANANA-ANA3 | game_spread | 0.285 | 0.325 | 0.317 | 33 | 68 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT27BOSCAR-8 | game_total | 0.237 | 0.275 | 0.267 | 28 | 73 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT27OTTVGK-6 | game_total | 0.635 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT27NJDAL-6 | game_total | 0.454 | 0.495 | 0.487 | 50 | 51 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT27MINUTA-5 | game_total | 0.771 | 0.810 | 0.803 | 82 | 20 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-4 | game_total | 0.834 | 0.870 | 0.863 | 88 | 14 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT27MTLSTL-MTL5 | team_total | 0.260 | 0.220 | 0.228 | 23 | 79 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27VANANA-VAN5 | team_total | 0.186 | 0.155 | 0.161 | 16 | 85 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT27MINUTA-6 | game_total | 0.556 | 0.600 | 0.591 | 61 | 41 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27MINUTA-4 | game_total | 0.856 | 0.885 | 0.880 | 89 | 12 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT27FLAWPG-6 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ6 | team_total | 0.049 | 0.080 | 0.073 | 9 | 93 | no | +0.016 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ PHI | 0.574 | 0.543 | 0.189 | 0.222 | 5.72 | 5.85 | 0.994/1.008 | KXNHLTEAMTOTAL-26OCT27CBJPHI-CBJ3 +0.043 |
| BOS @ CAR | 0.569 | 0.563 | 0.181 | 0.214 | 6.07 | 6.66 | 1.000/0.956 | KXNHLTOTAL-26OCT27BOSCAR-7 +0.101 |
| LAK @ CHI | 0.501 | 0.477 | 0.195 | 0.226 | 5.55 | 5.99 | 0.988/0.988 | KXNHLTOTAL-26OCT27LACHI-7 +0.078 |
| MTL @ STL | 0.465 | 0.567 | 0.172 | 0.213 | 6.57 | 6.54 | 1.032/0.983 | KXNHLGAME-26OCT27MTLSTL-MTL -0.103 |
| NYI @ NSH | 0.519 | 0.528 | 0.177 | 0.219 | 6.15 | 6.37 | 1.002/0.978 | KXNHLTOTAL-26OCT27NYINSH-7 +0.039 |
| NJD @ DAL | 0.561 | 0.553 | 0.187 | 0.229 | 5.58 | 5.89 | 0.968/0.949 | KXNHLTOTAL-26OCT27NJDAL-7 +0.059 |
| FLA @ WPG | 0.525 | 0.530 | 0.184 | 0.224 | 5.99 | 6.11 | 0.997/0.991 | KXNHLTOTAL-26OCT27FLAWPG-5 +0.022 |
| MIN @ UTA | 0.535 | 0.566 | 0.173 | 0.213 | 6.21 | 6.40 | 0.989/0.991 | KXNHLTEAMTOTAL-26OCT27MINUTA-UTA4 +0.049 |
| OTT @ VGK | 0.572 | 0.581 | 0.163 | 0.213 | 6.68 | 6.30 | 1.004/1.040 | KXNHLTOTAL-26OCT27OTTVGK-6 -0.062 |
| VAN @ ANA | 0.632 | 0.602 | 0.159 | 0.204 | 6.81 | 6.78 | 1.016/1.026 | KXNHLSPREAD-26OCT27VANANA-ANA2 -0.039 |
| BUF @ SJS | 0.463 | 0.524 | 0.171 | 0.214 | 6.74 | 6.52 | 1.039/0.999 | KXNHLTEAMTOTAL-26OCT27BUFSJ-BUF4 -0.069 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Cole Knuble: 1+ goals YES @ 13c · p 0.1907 (adj 0.1743) · $3.28 · thesis PHI:OFFENSE_4PLUS
- Travis Sanheim: 1+ goals YES @ 8c · p 0.1182 (adj 0.1074) · $1.89 · thesis PHI:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.1152 (adj 0.1051) · $1.68 · thesis CBJ:OFFENSE_4PLUS
- Adam Fantilli: 1+ goals NO @ 70c · p 0.7417 (adj 0.73) · $4.42 · thesis CBJ:SUPPRESSED
- Casey Mittelstadt: 1+ goals YES @ 12c · p 0.1827 (adj 0.1658) · $3.47 · thesis BOS:OFFENSE_4PLUS
- Pavel Zacha: 1+ goals YES @ 21c · p 0.2758 (adj 0.2581) · $3.89 · thesis BOS:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 8c · p 0.1093 (adj 0.1007) · $1.35 · thesis BOS:OFFENSE_4PLUS
- Jeremy Swayman: 30+ saves NO @ 52c · p 0.6058 (adj 0.5604) · $4.81 · thesis BOS:NET_LOW_VOLUME
- Patrick Kane: 1+ assists NO @ 54c · p 0.7069 (adj 0.5952) · $5.39 · thesis CHI:SUPPRESSED
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7923 (adj 0.778) · $5.03 · thesis CHI:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 52c · p 0.6066 (adj 0.5583) · $2.85 · thesis LAK:SUPPRESSED
- Erik Gustafsson: 1+ assists NO @ 63c · p 0.7365 (adj 0.664) · $3.57 · thesis LAK:SUPPRESSED
- Pius Suter: 1+ goals YES @ 13c · p 0.1867 (adj 0.1713) · $3.0 · thesis STL:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 24c · p 0.3059 (adj 0.2882) · $3.88 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 30c · p 0.3566 (adj 0.3412) · $3.26 · thesis STL:OFFENSE_4PLUS
- Jordan Binnington: 25+ saves NO @ 54c · p 0.6081 (adj 0.5716) · $3.08 · thesis STL:NET_LOW_VOLUME
- Victor Eklund: 1+ assists NO @ 72c · p 0.7922 (adj 0.7536) · $6.94 · thesis NYI:SUPPRESSED
- Victor Eklund: 1+ goals YES @ 17c · p 0.2036 (adj 0.194) · $1.42 · thesis NYI:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 28c · p 0.322 (adj 0.3103) · $1.94 · thesis NSH:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 13c · p 0.1581 (adj 0.1498) · $1.21 · thesis NYI:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1232 (adj 0.1137) · $1.61 · thesis NJD:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 75c · p 0.7951 (adj 0.7826) · $6.94 · thesis NJD:SUPPRESSED
- Roope Hintz: 1+ goals YES @ 26c · p 0.3052 (adj 0.2927) · $2.32 · thesis DAL:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 11c · p 0.1373 (adj 0.1292) · $1.16 · thesis NJD:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 65c · p 0.7201 (adj 0.7001) · $5.21 · thesis FLA:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1716 (adj 0.16) · $1.52 · thesis WPG:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 67c · p 0.7302 (adj 0.7139) · $5.21 · thesis FLA:SUPPRESSED
- Viggo Bjorck: 1+ assists NO @ 79c · p 0.8469 (adj 0.8159) · $5.28 · thesis WPG:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 56c · p 0.6421 (adj 0.6203) · $6.94 · thesis MIN:SUPPRESSED
- Anders Lee: 1+ goals YES @ 20c · p 0.2453 (adj 0.2327) · $2.24 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1562 (adj 0.1447) · $1.56 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 19c · p 0.235 (adj 0.2213) · $2.13 · thesis UTA:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 46c · p 0.6073 (adj 0.5083) · $5.38 · thesis VGK:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0859 (adj 0.0782) · $1.17 · thesis VGK:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 59c · p 0.7115 (adj 0.6293) · $4.95 · thesis OTT:SUPPRESSED
- Jonas Johansson: 28+ saves NO @ 61c · p 0.773 (adj 0.647) · $5.87 · thesis OTT:NET_LOW_VOLUME
- Filip Chytil: 1+ goals YES @ 18c · p 0.2344 (adj 0.2195) · $2.93 · thesis VAN:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2693 (adj 0.195) · $1.42 · thesis ANA:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2116 (adj 0.1987) · $1.9 · thesis VAN:OFFENSE_4PLUS
- Adam Gaudette: 1+ goals YES @ 13c · p 0.1747 (adj 0.1623) · $2.14 · thesis SJS:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 61c · p 0.6756 (adj 0.658) · $6.82 · thesis BUF:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 22c · p 0.2695 (adj 0.2559) · $2.47 · thesis SJS:OFFENSE_4PLUS
- Buffalo wins by over 2.5 goals NO @ 76c · p 0.834 (adj 0.7945) · $5.78 · thesis SJS:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ PHI** · priced 185/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.63, exp saves 24.07 (sd 6.4), pull risk 0.049
- CBJ net: Cam Talbot (CONFIRMED) exp shots 25.48, exp saves 22.01 (sd 6.26), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Werenski: 2+ points | 0.196 | 0.315 | 32/69 | +0.099 | STANDARD |
| Zach Werenski: 1+ points | 0.550 | 0.660 | 67/35 | +0.084 | STANDARD |
| Zach Werenski: 1+ assists | 0.445 | 0.545 | 55/46 | +0.078 | STANDARD |
| Valeri Nichushkin: 1+ points | 0.381 | 0.475 | 48/53 | +0.072 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.229 | 0.315 | 32/69 | +0.066 | STANDARD |
| Travis Sanheim: 1+ points | 0.399 | 0.315 | 33/70 | +0.054 | STANDARD |

**BOS @ CAR** · priced 181/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 23.29, exp saves 20.32 (sd 5.85), pull risk 0.064
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 32.38, exp saves 27.54 (sd 7.68), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sean Walker: 1+ points | 0.400 | 0.305 | 31/70 | +0.075 | STANDARD |
| Jeremy Swayman: 30+ saves | 0.394 | 0.485 | 49/52 | +0.068 |  |
| William Carrier: 1+ points | 0.411 | 0.325 | 33/68 | +0.066 | STANDARD |
| Sean Walker: 1+ assists | 0.333 | 0.250 | 26/76 | +0.060 | STANDARD |
| K'Andre Miller: 1+ points | 0.415 | 0.335 | 34/67 | +0.059 | STANDARD |
| K'Andre Miller: 1+ assists | 0.354 | 0.275 | 28/73 | +0.060 | STANDARD |

**LAK @ CHI** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 28.78, exp saves 24.89 (sd 6.73), pull risk 0.055
- LAK net: Anton Forsberg (PROBABLE) exp shots 25.18, exp saves 21.88 (sd 6.1), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.293 | 0.465 | 47/54 | +0.150 | STANDARD |
| Patrick Kane: 1+ points | 0.465 | 0.590 | 60/42 | +0.098 | STANDARD |
| Connor Bedard: 1+ assists | 0.365 | 0.485 | 49/52 | +0.097 | STANDARD |
| Erik Gustafsson: 1+ assists | 0.264 | 0.375 | 38/63 | +0.090 | STANDARD |
| Artemi Panarin: 1+ assists | 0.393 | 0.490 | 50/52 | +0.069 | STANDARD |
| Connor Bedard: 1+ points | 0.546 | 0.640 | 65/37 | +0.067 | STANDARD |

**MTL @ STL** · priced 193/198 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 26.31, exp saves 22.93 (sd 6.47), pull risk 0.058
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.26, exp saves 23.12 (sd 6.58), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Barron: 1+ points | 0.281 | 0.135 | 25/98 | +0.017 | STANDARD |
| Jonatan Berggren: 1+ points | 0.440 | 0.310 | 34/72 | +0.084 | STANDARD |
| Jimmy Snuggerud: 2+ points | 0.253 | 0.135 | 21/94 | +0.031 | STANDARD |
| Justin Barron: 1+ assists | 0.226 | 0.115 | 21/98 | +0.004 | STANDARD |
| Alexandre Texier: 1+ assists | 0.219 | 0.120 | 23/99 | -0.023 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.325 | 0.230 | 24/78 | +0.072 | STANDARD |

**NYI @ NSH** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 28.8, exp saves 24.82 (sd 6.91), pull risk 0.065
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 27.04, exp saves 23.32 (sd 6.57), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Wilsby: 1+ points | 0.362 | 0.260 | 27/75 | +0.078 | STANDARD |
| Adam Wilsby: 1+ assists | 0.306 | 0.220 | 23/79 | +0.063 | STANDARD |
| Emil Heineman: 1+ assists | 0.285 | 0.205 | 22/81 | +0.053 | STANDARD |
| Emil Heineman: 1+ points | 0.423 | 0.345 | 35/66 | +0.057 | STANDARD |
| Victor Eklund: 1+ assists | 0.208 | 0.285 | 29/72 | +0.058 | STANDARD |
| Matthew Wood: 1+ points | 0.396 | 0.330 | 34/68 | +0.040 | STANDARD |

**NJD @ DAL** · priced 194/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Casey DeSmith (CONFIRMED) exp shots 26.96, exp saves 23.52 (sd 6.41), pull risk 0.052
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.01, exp saves 22.56 (sd 6.28), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cody Glass: 1+ points | 0.279 | 0.110 | 20/98 | +0.068 | STANDARD |
| Nils Lundkvist: 1+ assists | 0.249 | 0.105 | 19/98 | +0.048 | STANDARD |
| Justin Hryckowian: 1+ assists | 0.256 | 0.115 | 21/98 | +0.034 | STANDARD |
| Lian Bichsel: 1+ points | 0.213 | 0.090 | 16/98 | +0.044 | STANDARD |
| Colin Blackwell: 1+ points | 0.218 | 0.100 | 18/98 | +0.028 | STANDARD |
| Luke Evangelista: 1+ assists | 0.206 | 0.320 | 33/69 | +0.089 | STANDARD |

**FLA @ WPG** · priced 207/216 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (CONFIRMED) exp shots 27.13, exp saves 23.59 (sd 6.44), pull risk 0.056
- FLA net: Akira Schmid (CONFIRMED) exp shots 26.32, exp saves 22.64 (sd 6.37), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Barron: 1+ points | 0.269 | 0.115 | 21/98 | +0.047 | STANDARD |
| Mario Ferraro: 1+ points | 0.207 | 0.075 | 13/98 | +0.069 | STANDARD |
| Seth Jones: 1+ points | 0.413 | 0.525 | 53/48 | +0.089 | STANDARD |
| Sam Reinhart: 1+ points | 0.485 | 0.595 | 60/41 | +0.088 | STANDARD |
| Dmitry Kulikov: 1+ points | 0.194 | 0.085 | 15/98 | +0.035 | STANDARD |
| Matthew Tkachuk: 1+ assists | 0.436 | 0.535 | 54/47 | +0.077 | STANDARD |

**MIN @ UTA** · priced 183/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (CONFIRMED) exp shots 27.66, exp saves 24.14 (sd 6.55), pull risk 0.053
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.67, exp saves 24.59 (sd 6.81), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.252 | 0.405 | 41/60 | +0.131 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.397 | 0.515 | 52/49 | +0.095 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.609 | 0.715 | 73/30 | +0.076 | STANDARD |
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
| Jake Sanderson: 1+ points | 0.370 | 0.505 | 52/51 | +0.103 | STANDARD |
| Jake Sanderson: 1+ assists | 0.288 | 0.415 | 42/59 | +0.105 | STANDARD |
| Adin Hill: 21+ saves | 0.651 | 0.530 | 56/50 | +0.074 |  |
| Mitch Marner: 1+ points | 0.541 | 0.660 | 67/35 | +0.093 | STANDARD |

**VAN @ ANA** · priced 180/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 23.87, exp saves 20.92 (sd 5.92), pull risk 0.058
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.6, exp saves 26.72 (sd 7.46), pull risk 0.091

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tom Willander: 1+ assists | 0.278 | 0.130 | 24/98 | +0.025 | STANDARD |
| Arshdeep Bains: 1+ points | 0.260 | 0.120 | 22/98 | +0.027 | STANDARD |
| Tim Washe: 1+ points | 0.412 | 0.275 | 30/75 | +0.097 | STANDARD |
| A.J. Greer: 1+ points | 0.435 | 0.320 | 33/69 | +0.089 | STANDARD |
| A.J. Greer: 1+ goals | 0.269 | 0.155 | 16/85 | +0.100 | STANDARD |
| Tim Washe: 1+ assists | 0.303 | 0.200 | 21/81 | +0.082 | STANDARD |

**BUF @ SJS** · priced 218/221 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.51, exp saves 24.68 (sd 6.72), pull risk 0.063
- BUF net: Colten Ellis (PROBABLE) exp shots 27.09, exp saves 23.35 (sd 6.5), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.298 | 0.100 | 17/97 | +0.118 | STANDARD |
| Ivar Stenberg: 1+ points | 0.407 | 0.575 | 59/44 | +0.135 | STANDARD |
| Sam Dickinson: 1+ assists | 0.246 | 0.085 | 15/98 | +0.087 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.447 | 0.580 | 59/43 | +0.106 | STANDARD |
| Peyton Krebs: 1+ assists | 0.221 | 0.090 | 16/98 | +0.051 | STANDARD |
| Barclay Goodrow: 1+ points | 0.230 | 0.100 | 18/98 | +0.039 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
