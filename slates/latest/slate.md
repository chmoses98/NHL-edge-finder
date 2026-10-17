# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T15:39:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4753 · contracts joined: 2966 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2616, 'OK': 251, 'NO_EDGE': 99}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 378, 'game_early_goal': 14, 'first_goal': 508, 'game_winner': 28, 'player_goals': 870, 'game_overtime': 14, 'player_points': 490, 'goalie_saves': 6, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 2026-10-17T17:00:00Z | T-60m | 0.579 | 0.421 | 0.175 | 5.96 | 3.22 | 2.74 | 225 (25/200) | CONFIRMED/CONFIRMED |
| CAR @ WPG | 2026-10-17T19:30:00Z | T-3h | 0.431 | 0.569 | 0.173 | 6.03 | 2.79 | 3.24 | 201 (25/176) | PROBABLE/PROJECTED |
| VAN @ TBL | 2026-10-17T20:00:00Z | T-3h | 0.691 | 0.309 | 0.152 | 6.26 | 3.75 | 2.50 | 200 (25/175) | PROJECTED/PROJECTED |
| SEA @ FLA | 2026-10-17T22:00:00Z | T-6h | 0.517 | 0.483 | 0.175 | 6.58 | 3.35 | 3.23 | 215 (25/190) | CONFIRMED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-6h | 0.474 | 0.526 | 0.175 | 6.40 | 3.13 | 3.27 | 222 (25/197) | CONFIRMED/PROJECTED |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-6h | 0.520 | 0.479 | 0.177 | 6.20 | 3.16 | 3.04 | 215 (25/190) | CONFIRMED/PROJECTED |
| SJS @ DET | 2026-10-17T23:00:00Z | T-6h | 0.549 | 0.451 | 0.179 | 5.97 | 3.15 | 2.82 | 221 (25/196) | PROBABLE/PROJECTED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-6h | 0.482 | 0.518 | 0.187 | 5.58 | 2.74 | 2.84 | 201 (25/176) | PROBABLE/PROJECTED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-6h | 0.535 | 0.465 | 0.181 | 5.87 | 3.05 | 2.82 | 210 (25/185) | PROBABLE/PROJECTED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-6h | 0.473 | 0.527 | 0.186 | 5.64 | 2.74 | 2.90 | 205 (25/180) | CONFIRMED/PROJECTED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-6h | 0.554 | 0.446 | 0.171 | 6.53 | 3.43 | 3.09 | 214 (25/189) | PROJECTED/PROJECTED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-6h | 0.507 | 0.493 | 0.189 | 5.62 | 2.83 | 2.78 | 204 (25/179) | PROJECTED/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-6h | 0.557 | 0.443 | 0.169 | 6.73 | 3.56 | 3.17 | 219 (25/194) | PROJECTED/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-6h | 0.615 | 0.385 | 0.163 | 6.77 | 3.78 | 2.99 | 214 (25/189) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.340 | 0.495 | 0.463 | 50 | 51 | no | +0.132 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.294 | 0.435 | 0.405 | 44 | 57 | no | +0.119 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.527 | 0.665 | 0.639 | 67 | 34 | no | +0.117 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.560 | 0.700 | 0.674 | 71 | 31 | no | +0.115 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB3 | game_spread | 0.328 | 0.465 | 0.436 | 47 | 54 | no | +0.115 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.473 | 0.345 | 0.369 | 35 | 66 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.416 | 0.290 | 0.314 | 30 | 72 | yes | +0.102 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.174 | 0.300 | 0.271 | 31 | 71 | no | +0.102 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.517 | 0.635 | 0.612 | 64 | 37 | no | +0.096 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.483 | 0.365 | 0.388 | 37 | 64 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.172 | 0.285 | 0.259 | 29 | 72 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.781 | 0.890 | 0.873 | 90 | 12 | no | +0.092 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB2 | game_spread | 0.473 | 0.585 | 0.563 | 59 | 42 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB4 | team_total | 0.536 | 0.650 | 0.628 | 66 | 36 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.233 | 0.135 | 0.151 | 14 | 87 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB5 | team_total | 0.333 | 0.445 | 0.422 | 46 | 57 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.276 | 0.185 | 0.201 | 19 | 82 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.309 | 0.405 | 0.385 | 41 | 60 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.254 | 0.165 | 0.180 | 17 | 84 | yes | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4 | team_total | 0.419 | 0.515 | 0.496 | 52 | 49 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.194 | 0.285 | 0.265 | 29 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.629 | 0.525 | 0.546 | 54 | 49 | yes | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.323 | 0.415 | 0.396 | 42 | 59 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2 | team_total | 0.823 | 0.735 | 0.755 | 74 | 27 | yes | +0.070 | OK |
| KXNHLGAME-26OCT17VANTB-TB | game_winner | 0.691 | 0.775 | 0.760 | 78 | 23 | no | +0.067 | OK |
| KXNHLGAME-26OCT17VANTB-VAN | game_winner | 0.309 | 0.225 | 0.240 | 23 | 78 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 | team_total | 0.518 | 0.605 | 0.588 | 61 | 40 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.328 | 0.415 | 0.397 | 42 | 59 | no | +0.066 | OK |
| KXNHLGAME-26OCT17CARWPG-CAR | game_winner | 0.569 | 0.655 | 0.638 | 66 | 35 | no | +0.065 | OK |
| KXNHLGAME-26OCT17CARWPG-WPG | game_winner | 0.431 | 0.345 | 0.362 | 35 | 66 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.351 | 0.440 | 0.422 | 45 | 57 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR3 | game_spread | 0.215 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.462 | 0.550 | 0.533 | 56 | 46 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.699 | 0.780 | 0.765 | 79 | 23 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ4 | team_total | 0.306 | 0.390 | 0.373 | 40 | 62 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB3 | team_total | 0.732 | 0.810 | 0.796 | 82 | 20 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB6 | team_total | 0.172 | 0.255 | 0.236 | 27 | 76 | no | +0.056 | OK |
| KXNHLGAME-26OCT17OTTPHI-PHI | game_winner | 0.482 | 0.405 | 0.420 | 41 | 60 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.549 | 0.630 | 0.614 | 64 | 38 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.459 | 0.535 | 0.520 | 54 | 47 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.458 | 0.380 | 0.395 | 39 | 63 | yes | +0.051 | OK |
| KXNHLGAME-26OCT17NJWSH-WSH | game_winner | 0.579 | 0.505 | 0.520 | 51 | 50 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.352 | 0.425 | 0.410 | 43 | 58 | no | +0.051 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.526 | 0.455 | 0.469 | 46 | 55 | yes | +0.049 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.474 | 0.545 | 0.531 | 55 | 46 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.504 | 0.580 | 0.565 | 59 | 43 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.395 | 0.465 | 0.451 | 47 | 54 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.731 | 0.800 | 0.787 | 81 | 21 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR2 | game_spread | 0.346 | 0.415 | 0.401 | 42 | 59 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA2 | team_total | 0.773 | 0.835 | 0.824 | 84 | 17 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.268 | 0.200 | 0.213 | 21 | 81 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT17NJWSH-NJ2 | game_spread | 0.219 | 0.285 | 0.271 | 29 | 72 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.268 | 0.335 | 0.321 | 34 | 67 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.162 | 0.225 | 0.211 | 23 | 78 | no | +0.046 | OK |
| KXNHLGAME-26OCT17OTTPHI-OTT | game_winner | 0.518 | 0.585 | 0.572 | 59 | 42 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA6 | team_total | 0.109 | 0.050 | 0.059 | 6 | 96 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.408 | 0.475 | 0.461 | 48 | 53 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.745 | 0.810 | 0.798 | 82 | 20 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.797 | 0.865 | 0.853 | 88 | 15 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR5 | team_total | 0.232 | 0.300 | 0.286 | 31 | 71 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT17NJWSH-WSH2 | game_spread | 0.347 | 0.285 | 0.297 | 29 | 72 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.306 | 0.245 | 0.257 | 25 | 76 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.669 | 0.600 | 0.614 | 61 | 41 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.071 | 0.130 | 0.115 | 14 | 88 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 | team_total | 0.401 | 0.470 | 0.456 | 48 | 54 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.185 | 0.250 | 0.236 | 26 | 76 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT17NJWSH-NJ3 | game_spread | 0.119 | 0.175 | 0.162 | 18 | 83 | no | +0.041 | OK |
| KXNHLGAME-26OCT17NJWSH-NJ | game_winner | 0.421 | 0.485 | 0.472 | 49 | 52 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA3 | game_spread | 0.168 | 0.115 | 0.124 | 12 | 89 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB2 | team_total | 0.885 | 0.955 | 0.945 | 98 | 7 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR3 | team_total | 0.634 | 0.695 | 0.683 | 70 | 31 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT17NJWSH-6 | game_total | 0.523 | 0.585 | 0.573 | 59 | 42 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ2 | team_total | 0.749 | 0.805 | 0.795 | 81 | 20 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET4 | team_total | 0.393 | 0.455 | 0.442 | 46 | 55 | no | +0.039 | OK |
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.385 | 0.325 | 0.337 | 33 | 68 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.302 | 0.245 | 0.256 | 25 | 76 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA3 | game_spread | 0.160 | 0.215 | 0.203 | 22 | 79 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT17BOSLA-LA2 | game_spread | 0.276 | 0.335 | 0.323 | 34 | 67 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA5 | team_total | 0.160 | 0.220 | 0.207 | 23 | 79 | no | +0.039 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 0.579 | 0.559 | 0.175 | 0.218 | 5.96 | 6.11 | 0.938/0.984 | KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 +0.036 |
| CAR @ WPG | 0.431 | 0.460 | 0.173 | 0.218 | 6.03 | 6.34 | 0.994/0.997 | KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3 +0.063 |
| VAN @ TBL | 0.691 | 0.624 | 0.152 | 0.216 | 6.26 | 6.27 | 0.974/1.026 | KXNHLSPREAD-26OCT17VANTB-TB2 -0.077 |
| SEA @ FLA | 0.517 | 0.516 | 0.175 | 0.218 | 6.58 | 6.31 | 1.015/1.005 | KXNHLTOTAL-26OCT17SEAFLA-6 -0.044 |
| NYI @ TOR | 0.474 | 0.515 | 0.175 | 0.216 | 6.40 | 6.33 | 0.988/0.956 | KXNHLGAME-26OCT17NYITOR-NYI -0.041 |
| BUF @ MTL | 0.520 | 0.524 | 0.177 | 0.219 | 6.20 | 6.44 | 0.983/0.998 | KXNHLTOTAL-26OCT17BUFMTL-7 +0.041 |
| SJS @ DET | 0.549 | 0.519 | 0.179 | 0.221 | 5.97 | 6.23 | 0.998/1.027 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ4 +0.053 |
| OTT @ PHI | 0.482 | 0.490 | 0.187 | 0.230 | 5.58 | 5.75 | 0.994/0.998 | KXNHLTOTAL-26OCT17OTTPHI-7 +0.033 |
| NYR @ CBJ | 0.535 | 0.558 | 0.181 | 0.222 | 5.87 | 6.07 | 0.955/0.992 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ4 +0.039 |
| DAL @ CHI | 0.473 | 0.465 | 0.186 | 0.220 | 5.64 | 6.15 | 0.988/0.986 | KXNHLTOTAL-26OCT17DALCHI-7 +0.092 |
| STL @ NSH | 0.554 | 0.506 | 0.171 | 0.220 | 6.53 | 6.42 | 0.994/1.016 | KXNHLSPREAD-26OCT17STLNSH-NSH2 -0.049 |
| BOS @ LAK | 0.507 | 0.542 | 0.189 | 0.222 | 5.62 | 6.05 | 0.989/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.557 | 0.522 | 0.169 | 0.210 | 6.73 | 6.89 | 0.993/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.046 |
| PIT @ VGK | 0.615 | 0.628 | 0.163 | 0.203 | 6.77 | 6.50 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-8 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 44 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2438 (adj 0.2253) · $3.8 · thesis WSH:OFFENSE_4PLUS
- Ethen Frank: 1+ goals YES @ 11c · p 0.1441 (adj 0.1331) · $1.59 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 17c · p 0.2065 (adj 0.1949) · $1.65 · thesis WSH:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 76c · p 0.7985 (adj 0.7864) · $5.79 · thesis NJD:SUPPRESSED
- Winnipeg wins by over 1.5 goals YES @ 18c · p 0.2602 (adj 0.2176) · $2.3 · thesis WPG:WINS_BY_2PLUS
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7767 (adj 0.7638) · $6.57 · thesis CAR:SUPPRESSED
- Kyle Connor: 1+ goals YES @ 37c · p 0.4116 (adj 0.4) · $1.3 · thesis WPG:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.6072 (adj 0.4823) · $2.96 · thesis GAME:TIGHT
- Tampa Bay wins by over 2.5 goals NO @ 54c · p 0.7256 (adj 0.6017) · $6.49 · thesis GAME:TIGHT
- John Carlson: 1+ goals NO @ 82c · p 0.8782 (adj 0.8599) · $7.59 · thesis TBL:SUPPRESSED
- Filip Chytil: 1+ goals YES @ 16c · p 0.2101 (adj 0.1951) · $2.15 · thesis VAN:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 13c · p 0.1926 (adj 0.1732) · $3.45 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 10c · p 0.1478 (adj 0.1333) · $2.52 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7086 (adj 0.6902) · $7.67 · thesis FLA:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1554 (adj 0.1391) · $2.06 · thesis SEA:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 11c · p 0.1427 (adj 0.132) · $1.53 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2436 (adj 0.234) · $1.48 · thesis NYI:OFFENSE_4PLUS
- Ryan McLeod: 1+ goals YES @ 13c · p 0.1816 (adj 0.1675) · $2.96 · thesis BUF:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 23c · p 0.2844 (adj 0.2683) · $3.1 · thesis BUF:OFFENSE_4PLUS
- Noah Ostlund: 1+ goals YES @ 19c · p 0.2344 (adj 0.2208) · $2.27 · thesis BUF:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 13c · p 0.1667 (adj 0.1563) · $1.97 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2045 (adj 0.1946) · $1.76 · thesis SJS:OFFENSE_4PLUS
- Luca Cagnoni: 1+ assists NO @ 70c · p 0.7677 (adj 0.7288) · $5.4 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 72c · p 0.7772 (adj 0.7461) · $5.3 · thesis SJS:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8201 (adj 0.8076) · $7.67 · thesis PHI:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 18c · p 0.2198 (adj 0.2036) · $1.36 · thesis PHI:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 78c · p 0.8349 (adj 0.805) · $5.53 · thesis PHI:WINS
- Ottawa over 3.5 goals scored NO @ 59c · p 0.6568 (adj 0.6209) · $1.79 · thesis OTT:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2045 (adj 0.1909) · $1.22 · thesis CBJ:OFFENSE_4PLUS
- Chicago wins by over 1.5 goals YES @ 17c · p 0.2503 (adj 0.2077) · $1.77 · thesis CHI:WINS_BY_2PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1502 (adj 0.1351) · $1.58 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 25c · p 0.3043 (adj 0.287) · $2.53 · thesis CHI:OFFENSE_4PLUS
- Frank Nazar: 1+ goals YES @ 19c · p 0.2359 (adj 0.2219) · $2.12 · thesis CHI:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 27c · p 0.3083 (adj 0.2962) · $1.64 · thesis NSH:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 25c · p 0.2861 (adj 0.2746) · $1.43 · thesis STL:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.8261 (adj 0.7441) · $7.67 · thesis BOS:SUPPRESSED
- Charlie McAvoy: 1+ assists NO @ 62c · p 0.6938 (adj 0.6469) · $2.77 · thesis BOS:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 15c · p 0.209 (adj 0.1918) · $3.37 · thesis EDM:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.241 (adj 0.222) · $3.5 · thesis UTA:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 29c · p 0.3555 (adj 0.3366) · $4.31 · thesis EDM:OFFENSE_4PLUS
- Evan Bouchard: 1+ goals YES @ 18c · p 0.228 (adj 0.2147) · $2.73 · thesis EDM:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 23c · p 0.2838 (adj 0.2691) · $3.21 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 24c · p 0.28 (adj 0.2688) · $1.97 · thesis PIT:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7341 (adj 0.7181) · $4.4 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ WSH** · priced 167/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 29.7, exp saves 26.02 (sd 6.93), pull risk 0.044
- NJD net: Jake Allen (CONFIRMED) exp shots 26.3, exp saves 22.67 (sd 6.31), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Beauvillier: 1+ assists | 0.225 | 0.500 | 97/97 | -0.197 | STANDARD |
| Jake Allen: 26+ saves | 0.315 | 0.480 | 49/53 | +0.138 |  |
| Jack Hughes: 1+ assists | 0.354 | 0.485 | 50/53 | +0.099 | STANDARD |
| Jack Hughes: 1+ points | 0.542 | 0.655 | 66/35 | +0.092 | STANDARD |
| Nico Hischier: 1+ assists | 0.272 | 0.375 | 39/64 | +0.072 | STANDARD |
| Ryan Leonard: 1+ assists | 0.377 | 0.275 | 29/74 | +0.073 | STANDARD |

**CAR @ WPG** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.7, exp saves 25.52 (sd 6.9), pull risk 0.066
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.96, exp saves 20.7 (sd 5.96), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.549 | 0.635 | 65/38 | +0.055 | STANDARD |
| Sebastian Aho: 1+ assists | 0.370 | 0.450 | 47/57 | +0.043 | STANDARD |
| Sebastian Aho: 2+ points | 0.195 | 0.270 | 29/75 | +0.042 | STANDARD |
| Cole Perfetti: 1+ points | 0.573 | 0.500 | 52/52 | +0.035 | STANDARD |
| Gabriel Vilardi: 1+ points | 0.542 | 0.475 | 49/54 | +0.034 | STANDARD |
| Kyle Connor: 2+ points | 0.304 | 0.240 | 27/79 | +0.020 | STANDARD |

**VAN @ TBL** · priced 142/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROJECTED) exp shots 23.47, exp saves 20.67 (sd 5.82), pull risk 0.046
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.69, exp saves 26.08 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.415 | 0.605 | 63/42 | +0.148 | STANDARD |
| John Carlson: 1+ assists | 0.332 | 0.505 | 54/53 | +0.121 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.485 | 49/52 | +0.142 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.497 | 0.635 | 66/39 | +0.096 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.160 | 0.295 | 32/73 | +0.097 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.230 | 27/81 | +0.084 | STANDARD |

**SEA @ FLA** · priced 160/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 25.35, exp saves 22.01 (sd 6.12), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.19 (sd 6.88), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ assists | 0.293 | 0.415 | 43/60 | +0.090 | STANDARD |
| Kaapo Kakko: 1+ points | 0.470 | 0.355 | 37/66 | +0.084 | STANDARD |
| Brady Tkachuk: 1+ points | 0.512 | 0.625 | 65/40 | +0.071 | STANDARD |
| Brady Tkachuk: 2+ points | 0.160 | 0.270 | 30/76 | +0.068 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.344 | 0.235 | 26/79 | +0.071 | STANDARD |
| Sam Reinhart: 1+ assists | 0.311 | 0.415 | 44/61 | +0.063 | STANDARD |

**NYI @ TOR** · priced 165/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.61, exp saves 26.54 (sd 7.11), pull risk 0.063
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.0, exp saves 22.4 (sd 6.34), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Bobrovsky: 26+ saves | 0.555 | 0.480 | 51/55 | +0.028 |  |
| Matias Maccelli: 1+ goals | 0.213 | 0.145 | 18/89 | +0.023 | STANDARD |
| Easton Cowan: 1+ assists | 0.316 | 0.255 | 27/76 | +0.033 | STANDARD |
| Easton Cowan: 1+ points | 0.454 | 0.395 | 41/62 | +0.027 | STANDARD |
| Darren Raddysh: 1+ assists | 0.378 | 0.435 | 44/57 | +0.035 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.320 | 0.375 | 41/66 | +0.004 | STANDARD |

**BUF @ MTL** · priced 155/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.31, exp saves 24.59 (sd 6.7), pull risk 0.064
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.14, exp saves 22.52 (sd 6.31), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.628 | 0.435 | 52/65 | +0.090 |  |
| Zach Benson: 1+ points | 0.579 | 0.455 | 47/56 | +0.091 | STANDARD |
| Nick Suzuki: 1+ assists | 0.468 | 0.560 | 58/46 | +0.055 | STANDARD |
| Zach Benson: 2+ points | 0.222 | 0.130 | 15/89 | +0.063 | STANDARD |
| Zach Benson: 1+ assists | 0.410 | 0.330 | 34/68 | +0.054 | STANDARD |
| Nick Suzuki: 2+ points | 0.261 | 0.340 | 36/68 | +0.044 | STANDARD |

**SJS @ DET** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 25.93, exp saves 22.52 (sd 6.3), pull risk 0.054
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 29.07, exp saves 25.14 (sd 6.82), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.317 | 0.440 | 46/58 | +0.086 | PRIOR_HEAVY |
| Nate Danielson: 1+ points | 0.250 | 0.365 | 38/65 | +0.084 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.188 | 0.300 | 32/72 | +0.078 | PRIOR_HEAVY |
| Luca Cagnoni: 1+ points | 0.281 | 0.370 | 40/66 | +0.044 | STANDARD |
| Luca Cagnoni: 1+ assists | 0.232 | 0.310 | 32/70 | +0.053 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.292 | 0.355 | 37/66 | +0.032 | STANDARD |

**OTT @ PHI** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROBABLE) exp shots 27.39, exp saves 23.84 (sd 6.46), pull risk 0.054
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.0, exp saves 21.03 (sd 5.89), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ assists | 0.150 | 0.270 | 29/75 | +0.086 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.275 | 0.390 | 41/63 | +0.079 | STANDARD |
| Tim Stutzle: 1+ assists | 0.381 | 0.495 | 53/54 | +0.061 | STANDARD |
| Andre Burakovsky: 1+ points | 0.262 | 0.365 | 38/65 | +0.072 | STANDARD |
| Tim Stutzle: 2+ points | 0.198 | 0.300 | 33/73 | +0.059 | STANDARD |
| Tim Stutzle: 2+ assists | 0.081 | 0.170 | 19/85 | +0.060 | STANDARD |

**NYR @ CBJ** · priced 153/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 24.38, exp saves 21.32 (sd 5.94), pull risk 0.05
- NYR net: Dylan Garand (PROJECTED) exp shots 28.58, exp saves 24.55 (sd 6.68), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| J.T. Miller: 1+ goals | 0.241 | 0.160 | 24/92 | -0.011 | STANDARD |
| Sean Monahan: 1+ points | 0.466 | 0.395 | 40/61 | +0.049 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.225 | 0.295 | 31/72 | +0.041 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.442 | 0.510 | 53/51 | +0.031 | STANDARD |
| Adam Fox: 1+ assists | 0.437 | 0.505 | 51/50 | +0.045 | STANDARD |
| J.T. Miller: 1+ assists | 0.351 | 0.415 | 43/60 | +0.033 | STANDARD |

**DAL @ CHI** · priced 149/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.33, exp saves 23.56 (sd 6.55), pull risk 0.067
- DAL net: Jake Oettinger (PROJECTED) exp shots 23.84, exp saves 20.7 (sd 5.89), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 26+ saves | 0.375 | 0.485 | 51/54 | +0.068 |  |
| Jason Robertson: 2+ points | 0.265 | 0.365 | 39/66 | +0.060 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.543 | 0.450 | 47/57 | +0.056 | STANDARD |
| Connor Bedard: 1+ assists | 0.343 | 0.430 | 45/59 | +0.050 | STANDARD |
| Mikko Rantanen: 2+ points | 0.255 | 0.340 | 38/70 | +0.031 | STANDARD |
| Mikko Rantanen: 2+ assists | 0.125 | 0.205 | 22/81 | +0.054 | STANDARD |

**STL @ NSH** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 27.32, exp saves 23.57 (sd 6.56), pull risk 0.069
- STL net: Jordan Binnington (PROJECTED) exp shots 27.33, exp saves 23.53 (sd 6.6), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.260 | 0.335 | 35/68 | +0.045 | STANDARD |
| Robert Thomas: 1+ assists | 0.423 | 0.490 | 51/53 | +0.029 | STANDARD |
| Cam Fowler: 1+ assists | 0.333 | 0.275 | 30/75 | +0.018 | STANDARD |
| Adam Jiricek: 1+ points | 0.309 | 0.365 | 40/67 | +0.006 | PRIOR_HEAVY |
| Matthew Wood: 1+ goals | 0.214 | 0.160 | 21/89 | -0.008 | STANDARD |
| Jake Neighbours: 1+ assists | 0.287 | 0.235 | 26/79 | +0.014 | STANDARD |

**BOS @ LAK** · priced 152/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.88, exp saves 22.55 (sd 6.28), pull risk 0.054
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.61 (sd 6.83), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ assists | 0.174 | 0.300 | 31/71 | +0.102 | STANDARD |
| Artemi Panarin: 1+ assists | 0.384 | 0.500 | 52/52 | +0.079 | STANDARD |
| JJ Peterka: 1+ points | 0.330 | 0.425 | 43/58 | +0.073 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.306 | 0.400 | 42/62 | +0.057 | STANDARD |
| Artemi Panarin: 2+ points | 0.212 | 0.295 | 33/74 | +0.035 | STANDARD |
| Charlie McAvoy: 1+ points | 0.394 | 0.475 | 49/54 | +0.049 | STANDARD |

**EDM @ UTA** · priced 155/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.03, exp saves 23.36 (sd 6.56), pull risk 0.07
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vasily Podkolzin: 1+ points | 0.645 | 0.490 | 51/53 | +0.117 | STANDARD |
| Mattias Ekholm: 1+ points | 0.469 | 0.320 | 34/70 | +0.114 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.454 | 0.305 | 32/71 | +0.118 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.283 | 0.140 | 17/89 | +0.103 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.393 | 0.265 | 28/75 | +0.099 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.226 | 0.330 | 37/71 | +0.050 | STANDARD |

**PIT @ VGK** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.53, exp saves 23.36 (sd 6.36), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.280 | 0.420 | 44/60 | +0.103 | STANDARD |
| Jack Eichel: 1+ assists | 0.481 | 0.615 | 64/41 | +0.092 | STANDARD |
| Mitch Marner: 2+ points | 0.230 | 0.350 | 37/67 | +0.085 | STANDARD |
| Ben Kindel: 1+ assists | 0.231 | 0.125 | 24/99 | -0.022 | STANDARD |
| Trevor Connelly: 1+ points | 0.390 | 0.490 | 52/54 | +0.053 | PRIOR_HEAVY |
| Jack Eichel: 2+ assists | 0.136 | 0.235 | 28/81 | +0.044 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
