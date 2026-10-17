# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T16:28:20Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4791 · contracts joined: 3004 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2654, 'OK': 260, 'NO_EDGE': 90}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 388, 'game_early_goal': 14, 'first_goal': 512, 'game_winner': 28, 'player_goals': 876, 'game_overtime': 14, 'player_points': 506, 'goalie_saves': 8, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 2026-10-17T17:00:00Z | T-30m | 0.579 | 0.421 | 0.175 | 5.96 | 3.22 | 2.74 | 228 (25/203) | CONFIRMED/CONFIRMED |
| CAR @ WPG | 2026-10-17T19:30:00Z | T-3h | 0.431 | 0.569 | 0.173 | 6.03 | 2.79 | 3.24 | 201 (25/176) | PROBABLE/PROJECTED |
| VAN @ TBL | 2026-10-17T20:00:00Z | T-3h | 0.691 | 0.309 | 0.152 | 6.26 | 3.75 | 2.50 | 200 (25/175) | PROJECTED/PROJECTED |
| SEA @ FLA | 2026-10-17T22:00:00Z | T-3h | 0.517 | 0.483 | 0.175 | 6.58 | 3.35 | 3.23 | 215 (25/190) | CONFIRMED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-6h | 0.470 | 0.530 | 0.173 | 6.33 | 3.07 | 3.26 | 222 (25/197) | CONFIRMED/PROBABLE |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-6h | 0.517 | 0.483 | 0.178 | 6.19 | 3.15 | 3.04 | 217 (25/192) | CONFIRMED/PROBABLE |
| SJS @ DET | 2026-10-17T23:00:00Z | T-6h | 0.550 | 0.450 | 0.182 | 5.96 | 3.15 | 2.82 | 221 (25/196) | CONFIRMED/PROJECTED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-6h | 0.489 | 0.511 | 0.183 | 5.58 | 2.76 | 2.82 | 228 (25/203) | CONFIRMED/CONFIRMED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-6h | 0.531 | 0.469 | 0.181 | 5.85 | 3.02 | 2.83 | 216 (25/191) | PROBABLE/PROBABLE |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-6h | 0.473 | 0.527 | 0.186 | 5.64 | 2.74 | 2.90 | 205 (25/180) | CONFIRMED/PROJECTED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-6h | 0.514 | 0.486 | 0.171 | 6.75 | 3.43 | 3.33 | 214 (25/189) | PROBABLE/PROJECTED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-6h | 0.507 | 0.493 | 0.189 | 5.62 | 2.83 | 2.78 | 204 (25/179) | PROJECTED/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-6h | 0.557 | 0.443 | 0.169 | 6.73 | 3.56 | 3.17 | 219 (25/194) | PROJECTED/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-6h | 0.615 | 0.385 | 0.163 | 6.77 | 3.78 | 2.99 | 214 (25/189) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.340 | 0.495 | 0.463 | 50 | 51 | no | +0.132 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.560 | 0.705 | 0.678 | 71 | 30 | no | +0.126 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.294 | 0.435 | 0.405 | 44 | 57 | no | +0.119 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.527 | 0.665 | 0.639 | 67 | 34 | no | +0.117 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB3 | game_spread | 0.328 | 0.465 | 0.436 | 47 | 54 | no | +0.115 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.473 | 0.345 | 0.369 | 35 | 66 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.416 | 0.295 | 0.318 | 30 | 71 | yes | +0.102 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.174 | 0.295 | 0.267 | 30 | 71 | no | +0.102 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.517 | 0.635 | 0.612 | 64 | 37 | no | +0.096 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.483 | 0.365 | 0.388 | 37 | 64 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.172 | 0.290 | 0.263 | 30 | 72 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.629 | 0.515 | 0.538 | 52 | 49 | yes | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.781 | 0.885 | 0.868 | 89 | 12 | no | +0.092 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB2 | game_spread | 0.473 | 0.585 | 0.563 | 59 | 42 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB4 | team_total | 0.536 | 0.645 | 0.624 | 65 | 36 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.233 | 0.135 | 0.151 | 14 | 87 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB5 | team_total | 0.333 | 0.440 | 0.418 | 45 | 57 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.276 | 0.185 | 0.201 | 19 | 82 | yes | +0.075 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.309 | 0.405 | 0.385 | 41 | 60 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.254 | 0.165 | 0.180 | 17 | 84 | yes | +0.074 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.336 | 0.240 | 0.258 | 25 | 77 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.194 | 0.285 | 0.265 | 29 | 72 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.322 | 0.415 | 0.396 | 42 | 59 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA4 | team_total | 0.323 | 0.415 | 0.396 | 42 | 59 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2 | team_total | 0.823 | 0.735 | 0.755 | 74 | 27 | yes | +0.070 | OK |
| KXNHLTOTAL-26OCT17STLNSH-7 | game_total | 0.537 | 0.440 | 0.459 | 45 | 57 | yes | +0.070 | OK |
| KXNHLGAME-26OCT17VANTB-TB | game_winner | 0.691 | 0.775 | 0.760 | 78 | 23 | no | +0.067 | OK |
| KXNHLGAME-26OCT17VANTB-VAN | game_winner | 0.309 | 0.225 | 0.240 | 23 | 78 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB6 | team_total | 0.172 | 0.255 | 0.236 | 26 | 75 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4 | team_total | 0.419 | 0.510 | 0.492 | 52 | 50 | no | +0.063 | OK |
| KXNHLGAME-26OCT17OTTPHI-PHI | game_winner | 0.489 | 0.405 | 0.422 | 41 | 60 | yes | +0.062 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.351 | 0.440 | 0.422 | 45 | 57 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT17STLNSH-6 | game_total | 0.648 | 0.565 | 0.582 | 57 | 44 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR3 | game_spread | 0.215 | 0.295 | 0.278 | 30 | 71 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.462 | 0.550 | 0.533 | 56 | 46 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.699 | 0.775 | 0.761 | 78 | 23 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT17STLNSH-9 | game_total | 0.249 | 0.170 | 0.184 | 18 | 84 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ4 | team_total | 0.306 | 0.385 | 0.369 | 39 | 62 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB3 | team_total | 0.732 | 0.815 | 0.800 | 83 | 20 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.267 | 0.195 | 0.208 | 20 | 81 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 | team_total | 0.518 | 0.595 | 0.580 | 60 | 41 | no | +0.055 | OK |
| KXNHLGAME-26OCT17CARWPG-CAR | game_winner | 0.569 | 0.645 | 0.630 | 65 | 36 | no | +0.055 | OK |
| KXNHLGAME-26OCT17CARWPG-WPG | game_winner | 0.431 | 0.355 | 0.370 | 36 | 65 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT17BOSLA-LA3 | team_total | 0.549 | 0.630 | 0.614 | 64 | 38 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT17BOSLA-6 | game_total | 0.459 | 0.535 | 0.520 | 54 | 47 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT17BOSLA-5 | game_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLGAME-26OCT17OTTPHI-OTT | game_winner | 0.511 | 0.585 | 0.570 | 59 | 42 | no | +0.052 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.530 | 0.455 | 0.470 | 46 | 55 | yes | +0.052 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.470 | 0.545 | 0.530 | 55 | 46 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.071 | 0.135 | 0.119 | 14 | 87 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.458 | 0.380 | 0.395 | 39 | 63 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT17BOSLA-7 | game_total | 0.352 | 0.425 | 0.410 | 43 | 58 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.392 | 0.465 | 0.450 | 47 | 54 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.729 | 0.795 | 0.783 | 80 | 21 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.313 | 0.245 | 0.258 | 25 | 76 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT17SJDET-DET4 | team_total | 0.393 | 0.470 | 0.454 | 48 | 54 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.504 | 0.580 | 0.565 | 59 | 43 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.545 | 0.615 | 0.601 | 62 | 39 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT17CARWPG-CAR2 | game_spread | 0.346 | 0.415 | 0.401 | 42 | 59 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT17VANTB-5 | game_total | 0.773 | 0.835 | 0.824 | 84 | 17 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.152 | 0.215 | 0.201 | 22 | 79 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT17NJWSH-NJ2 | game_spread | 0.219 | 0.285 | 0.271 | 29 | 72 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT2 | game_spread | 0.278 | 0.345 | 0.331 | 35 | 66 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.743 | 0.805 | 0.794 | 81 | 20 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT17SJDET-6 | game_total | 0.517 | 0.585 | 0.572 | 59 | 42 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA6 | team_total | 0.109 | 0.055 | 0.063 | 6 | 95 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 | team_total | 0.397 | 0.465 | 0.451 | 47 | 54 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT2 | team_total | 0.766 | 0.830 | 0.819 | 84 | 18 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT17NJWSH-WSH2 | game_spread | 0.347 | 0.285 | 0.297 | 29 | 72 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.410 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.263 | 0.325 | 0.312 | 33 | 68 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.185 | 0.245 | 0.232 | 25 | 76 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT17NJWSH-NJ3 | game_spread | 0.119 | 0.175 | 0.162 | 18 | 83 | no | +0.041 | OK |
| KXNHLGAME-26OCT17NJWSH-NJ | game_winner | 0.421 | 0.485 | 0.472 | 49 | 52 | no | +0.041 | OK |
| KXNHLGAME-26OCT17NJWSH-WSH | game_winner | 0.579 | 0.515 | 0.528 | 52 | 49 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA3 | game_spread | 0.168 | 0.115 | 0.124 | 12 | 89 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB2 | team_total | 0.885 | 0.935 | 0.927 | 94 | 7 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17CARWPG-CAR3 | team_total | 0.634 | 0.705 | 0.692 | 72 | 31 | no | +0.041 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 0.579 | 0.559 | 0.175 | 0.218 | 5.96 | 6.11 | 0.938/0.984 | KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 +0.036 |
| CAR @ WPG | 0.431 | 0.460 | 0.173 | 0.218 | 6.03 | 6.34 | 0.994/0.997 | KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3 +0.063 |
| VAN @ TBL | 0.691 | 0.624 | 0.152 | 0.216 | 6.26 | 6.27 | 0.974/1.026 | KXNHLSPREAD-26OCT17VANTB-TB2 -0.077 |
| SEA @ FLA | 0.517 | 0.516 | 0.175 | 0.218 | 6.58 | 6.31 | 1.015/1.005 | KXNHLTOTAL-26OCT17SEAFLA-6 -0.044 |
| NYI @ TOR | 0.470 | 0.507 | 0.173 | 0.218 | 6.33 | 6.31 | 0.988/0.952 | KXNHLSPREAD-26OCT17NYITOR-NYI2 -0.038 |
| BUF @ MTL | 0.517 | 0.519 | 0.178 | 0.222 | 6.19 | 6.44 | 0.983/1.000 | KXNHLTOTAL-26OCT17BUFMTL-7 +0.051 |
| SJS @ DET | 0.550 | 0.520 | 0.182 | 0.221 | 5.96 | 6.22 | 0.994/1.027 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ4 +0.052 |
| OTT @ PHI | 0.489 | 0.476 | 0.183 | 0.231 | 5.58 | 5.69 | 0.994/0.968 | KXNHLTOTAL-26OCT17OTTPHI-5 +0.024 |
| NYR @ CBJ | 0.531 | 0.554 | 0.181 | 0.220 | 5.85 | 6.06 | 0.955/0.990 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ4 +0.044 |
| DAL @ CHI | 0.473 | 0.465 | 0.186 | 0.220 | 5.64 | 6.15 | 0.988/0.986 | KXNHLTOTAL-26OCT17DALCHI-7 +0.092 |
| STL @ NSH | 0.514 | 0.498 | 0.171 | 0.210 | 6.75 | 6.42 | 1.002/1.016 | KXNHLTOTAL-26OCT17STLNSH-6 -0.054 |
| BOS @ LAK | 0.507 | 0.542 | 0.189 | 0.222 | 5.62 | 6.05 | 0.989/0.968 | KXNHLTOTAL-26OCT17BOSLA-7 +0.078 |
| EDM @ UTA | 0.557 | 0.522 | 0.169 | 0.210 | 6.73 | 6.89 | 0.993/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.046 |
| PIT @ VGK | 0.615 | 0.628 | 0.163 | 0.203 | 6.77 | 6.50 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-8 -0.049 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 47 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2438 (adj 0.2241) · $4.53 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 17c · p 0.2065 (adj 0.1949) · $1.6 · thesis WSH:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 76c · p 0.7985 (adj 0.7864) · $5.48 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 12c · p 0.1458 (adj 0.1381) · $1.11 · thesis NJD:OFFENSE_4PLUS
- Winnipeg wins by over 1.5 goals YES @ 18c · p 0.2602 (adj 0.2176) · $2.46 · thesis WPG:WINS_BY_2PLUS
- Mike Reilly: 1+ goals YES @ 4c · p 0.0568 (adj 0.0551) · $1.2 · thesis CAR:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7767 (adj 0.7638) · $6.08 · thesis CAR:SUPPRESSED
- Kyle Connor: 1+ goals YES @ 37c · p 0.4116 (adj 0.4) · $1.16 · thesis WPG:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 42c · p 0.6072 (adj 0.4823) · $2.66 · thesis GAME:TIGHT
- Tampa Bay wins by over 2.5 goals NO @ 54c · p 0.7256 (adj 0.6017) · $5.55 · thesis GAME:TIGHT
- Nikita Kucherov: 1+ goals NO @ 58c · p 0.6467 (adj 0.6275) · $4.94 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals NO @ 60c · p 0.6647 (adj 0.646) · $5.17 · thesis TBL:SUPPRESSED
- Ben Meyers: 1+ goals YES @ 10c · p 0.1478 (adj 0.1333) · $2.41 · thesis SEA:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 14c · p 0.1926 (adj 0.1769) · $2.76 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 11c · p 0.1554 (adj 0.1403) · $2.11 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 64c · p 0.7086 (adj 0.6902) · $7.33 · thesis FLA:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 11c · p 0.1405 (adj 0.1316) · $1.42 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2432 (adj 0.2336) · $1.34 · thesis NYI:OFFENSE_4PLUS
- Matias Maccelli: 1+ goals YES @ 18c · p 0.2173 (adj 0.2005) · $1.04 · thesis NYI:OFFENSE_4PLUS
- Alexandre Carrier: 1+ goals YES @ 4c · p 0.063 (adj 0.056) · $1.09 · thesis DIFFUSE
- Zach Benson: 1+ goals YES @ 23c · p 0.2849 (adj 0.2687) · $3.05 · thesis BUF:OFFENSE_4PLUS
- Noah Ostlund: 1+ goals YES @ 19c · p 0.2284 (adj 0.2175) · $1.86 · thesis BUF:OFFENSE_4PLUS
- Ryan McLeod: 1+ goals YES @ 15c · p 0.188 (adj 0.1735) · $1.46 · thesis BUF:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 13c · p 0.1657 (adj 0.1555) · $1.78 · thesis SJS:OFFENSE_4PLUS
- Luca Cagnoni: 1+ goals NO @ 91c · p 0.9392 (adj 0.9294) · $7.33 · thesis DIFFUSE
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2038 (adj 0.1929) · $1.54 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 71c · p 0.8102 (adj 0.7353) · $5.55 · thesis SJS:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8224 (adj 0.8093) · $7.33 · thesis PHI:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 18c · p 0.2167 (adj 0.2063) · $1.73 · thesis PHI:OFFENSE_4PLUS
- Tim Stutzle: 1+ assists NO @ 50c · p 0.626 (adj 0.5343) · $3.02 · thesis OTT:SUPPRESSED
- Ottawa over 3.5 goals scored NO @ 59c · p 0.6513 (adj 0.6181) · $1.74 · thesis OTT:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.7974 (adj 0.7512) · $6.63 · thesis NYR:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 24c · p 0.2745 (adj 0.2646) · $1.38 · thesis CBJ:OFFENSE_4PLUS
- Chicago wins by over 1.5 goals YES @ 17c · p 0.2503 (adj 0.2077) · $2.36 · thesis CHI:WINS_BY_2PLUS
- Tyler Bertuzzi: 1+ goals YES @ 25c · p 0.3043 (adj 0.2882) · $2.68 · thesis CHI:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 20c · p 0.2484 (adj 0.2326) · $2.07 · thesis CHI:OFFENSE_4PLUS
- Connor Bedard: 1+ assists NO @ 58c · p 0.6571 (adj 0.611) · $5.72 · thesis CHI:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 25c · p 0.2912 (adj 0.2784) · $1.84 · thesis STL:OFFENSE_4PLUS
- William Borgen: 1+ goals YES @ 3c · p 0.053 (adj 0.046) · $1.11 · thesis BOS:WINS_BY_2PLUS
- JJ Peterka: 1+ assists NO @ 71c · p 0.7878 (adj 0.7414) · $7.1 · thesis BOS:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 15c · p 0.209 (adj 0.1918) · $3.17 · thesis EDM:OFFENSE_4PLUS
- Mathieu Joseph: 1+ goals YES @ 7c · p 0.1034 (adj 0.0926) · $1.49 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 29c · p 0.3555 (adj 0.3341) · $3.69 · thesis EDM:OFFENSE_4PLUS
- Evan Bouchard: 1+ goals YES @ 18c · p 0.228 (adj 0.2147) · $2.6 · thesis EDM:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 23c · p 0.2838 (adj 0.2691) · $3.06 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1275 (adj 0.1194) · $1.21 · thesis PIT:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7341 (adj 0.7181) · $4.21 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ WSH** · priced 170/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 29.7, exp saves 26.02 (sd 6.93), pull risk 0.044
- NJD net: Jake Allen (CONFIRMED) exp shots 26.3, exp saves 22.67 (sd 6.31), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.354 | 0.485 | 50/53 | +0.099 | STANDARD |
| Jake Allen: 26+ saves | 0.315 | 0.440 | 45/57 | +0.098 |  |
| Jack Hughes: 1+ points | 0.542 | 0.660 | 67/35 | +0.092 | STANDARD |
| Ryan Leonard: 1+ assists | 0.377 | 0.265 | 28/75 | +0.083 | STANDARD |
| Jack Hughes: 2+ points | 0.185 | 0.295 | 31/72 | +0.081 | STANDARD |
| Nico Hischier: 1+ assists | 0.272 | 0.375 | 39/64 | +0.072 | STANDARD |

**CAR @ WPG** · priced 149/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.7, exp saves 25.52 (sd 6.9), pull risk 0.066
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.96, exp saves 20.7 (sd 5.96), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.370 | 0.465 | 48/55 | +0.062 | STANDARD |
| Sebastian Aho: 1+ points | 0.549 | 0.640 | 65/37 | +0.065 | STANDARD |
| Sebastian Aho: 2+ points | 0.195 | 0.285 | 31/74 | +0.052 | STANDARD |
| Cole Perfetti: 1+ points | 0.573 | 0.505 | 52/51 | +0.035 | STANDARD |
| Kyle Connor: 1+ points | 0.667 | 0.605 | 62/41 | +0.030 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.440 | 0.500 | 51/51 | +0.032 | STANDARD |

**VAN @ TBL** · priced 142/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROJECTED) exp shots 23.47, exp saves 20.67 (sd 5.82), pull risk 0.046
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.69, exp saves 26.08 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.415 | 0.615 | 63/40 | +0.168 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.510 | 53/51 | +0.152 | STANDARD |
| John Carlson: 1+ assists | 0.332 | 0.520 | 54/50 | +0.151 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.497 | 0.655 | 67/36 | +0.126 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.250 | 28/78 | +0.113 | STANDARD |
| Nikita Kucherov: 3+ points | 0.109 | 0.230 | 26/80 | +0.080 | STANDARD |

**SEA @ FLA** · priced 160/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 25.35, exp saves 22.01 (sd 6.12), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.19 (sd 6.88), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ assists | 0.293 | 0.415 | 43/60 | +0.090 | STANDARD |
| Kaapo Kakko: 1+ points | 0.470 | 0.355 | 37/66 | +0.084 | STANDARD |
| Brady Tkachuk: 1+ points | 0.512 | 0.625 | 64/39 | +0.081 | STANDARD |
| Sam Reinhart: 1+ assists | 0.311 | 0.420 | 44/60 | +0.072 | STANDARD |
| Sam Reinhart: 1+ points | 0.513 | 0.620 | 64/40 | +0.070 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.344 | 0.240 | 26/78 | +0.071 | STANDARD |

**NYI @ TOR** · priced 165/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.61, exp saves 26.56 (sd 7.07), pull risk 0.06
- NYI net: Ilya Sorokin (PROBABLE) exp shots 26.0, exp saves 22.41 (sd 6.3), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Bobrovsky: 26+ saves | 0.558 | 0.470 | 49/55 | +0.050 |  |
| Darren Raddysh: 1+ assists | 0.373 | 0.440 | 45/57 | +0.040 | STANDARD |
| Matias Maccelli: 1+ goals | 0.217 | 0.150 | 18/88 | +0.027 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.329 | 0.395 | 41/62 | +0.034 | STANDARD |
| Darren Raddysh: 2+ points | 0.133 | 0.195 | 20/81 | +0.046 | STANDARD |
| Easton Cowan: 1+ assists | 0.315 | 0.260 | 28/76 | +0.020 | STANDARD |

**BUF @ MTL** · priced 157/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.31, exp saves 24.62 (sd 6.73), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.14, exp saves 22.47 (sd 6.39), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.628 | 0.445 | 53/64 | +0.081 |  |
| Ukko-Pekka Luukkonen: 26+ saves | 0.308 | 0.450 | 53/63 | +0.045 |  |
| Zach Benson: 1+ points | 0.574 | 0.455 | 47/56 | +0.087 | STANDARD |
| Nick Suzuki: 1+ assists | 0.461 | 0.555 | 57/46 | +0.061 | STANDARD |
| Zach Benson: 1+ assists | 0.407 | 0.325 | 34/69 | +0.052 | STANDARD |
| Nick Suzuki: 2+ points | 0.266 | 0.345 | 36/67 | +0.048 | STANDARD |

**SJS @ DET** · priced 163/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (CONFIRMED) exp shots 25.93, exp saves 22.5 (sd 6.3), pull risk 0.057
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 29.07, exp saves 25.1 (sd 6.74), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.318 | 0.440 | 45/57 | +0.095 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.190 | 0.305 | 32/71 | +0.086 | PRIOR_HEAVY |
| Luca Cagnoni: 1+ points | 0.287 | 0.385 | 40/63 | +0.067 | STANDARD |
| Nate Danielson: 1+ points | 0.248 | 0.340 | 35/67 | +0.067 | STANDARD |
| Luca Cagnoni: 1+ assists | 0.239 | 0.310 | 32/70 | +0.046 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.291 | 0.360 | 37/65 | +0.043 | STANDARD |

**OTT @ PHI** · priced 172/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.39, exp saves 23.79 (sd 6.48), pull risk 0.052
- OTT net: Linus Ullmark (CONFIRMED) exp shots 24.0, exp saves 21.01 (sd 5.93), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Cates: 1+ points | 0.340 | 0.195 | 36/97 | -0.036 | STANDARD |
| Tim Stutzle: 1+ assists | 0.374 | 0.515 | 53/50 | +0.108 | STANDARD |
| Sean Couturier: 1+ points | 0.336 | 0.200 | 38/98 | -0.060 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.149 | 0.275 | 29/74 | +0.098 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.269 | 0.390 | 41/63 | +0.084 | STANDARD |
| Andre Burakovsky: 1+ points | 0.261 | 0.370 | 38/64 | +0.083 | STANDARD |

**NYR @ CBJ** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROBABLE) exp shots 24.38, exp saves 21.4 (sd 5.92), pull risk 0.046
- NYR net: Dylan Garand (PROBABLE) exp shots 28.58, exp saves 24.5 (sd 6.75), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Fox: 1+ assists | 0.416 | 0.510 | 52/50 | +0.067 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.203 | 0.295 | 31/72 | +0.063 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.419 | 0.510 | 53/51 | +0.054 | STANDARD |
| Valeri Nichushkin: 1+ assists | 0.244 | 0.320 | 34/70 | +0.041 | STANDARD |
| Adam Fox: 1+ points | 0.473 | 0.545 | 56/47 | +0.040 | STANDARD |
| Sean Monahan: 1+ points | 0.462 | 0.395 | 40/61 | +0.045 | STANDARD |

**DAL @ CHI** · priced 149/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.33, exp saves 23.56 (sd 6.55), pull risk 0.067
- DAL net: Jake Oettinger (PROJECTED) exp shots 23.84, exp saves 20.7 (sd 5.89), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jason Robertson: 2+ points | 0.265 | 0.365 | 39/66 | +0.060 | STANDARD |
| Spencer Knight: 26+ saves | 0.375 | 0.475 | 50/55 | +0.058 |  |
| Mikko Rantanen: 2+ points | 0.255 | 0.355 | 38/67 | +0.060 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.543 | 0.450 | 47/57 | +0.056 | STANDARD |
| Connor Bedard: 1+ assists | 0.343 | 0.435 | 45/58 | +0.060 | STANDARD |
| Patrick Kane: 1+ assists | 0.305 | 0.395 | 41/62 | +0.059 | STANDARD |

**STL @ NSH** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.32, exp saves 23.6 (sd 6.51), pull risk 0.066
- STL net: Jordan Binnington (PROJECTED) exp shots 27.33, exp saves 23.58 (sd 6.67), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.259 | 0.340 | 36/68 | +0.046 | STANDARD |
| Robert Thomas: 1+ assists | 0.430 | 0.500 | 52/52 | +0.032 | STANDARD |
| Jake Neighbours: 1+ assists | 0.290 | 0.235 | 26/79 | +0.017 | STANDARD |
| Jake Neighbours: 1+ points | 0.444 | 0.390 | 41/63 | +0.017 | STANDARD |
| Cam Fowler: 1+ assists | 0.331 | 0.280 | 30/74 | +0.017 | STANDARD |
| Robert Thomas: 1+ goals | 0.291 | 0.240 | 25/77 | +0.028 | STANDARD |

**BOS @ LAK** · priced 145/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.88, exp saves 22.55 (sd 6.28), pull risk 0.054
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.68, exp saves 25.61 (sd 6.83), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.384 | 0.505 | 52/51 | +0.089 | STANDARD |
| Fraser Minten: 1+ assists | 0.297 | 0.195 | 22/83 | +0.065 | STANDARD |
| Fraser Minten: 1+ points | 0.440 | 0.340 | 35/67 | +0.074 | STANDARD |
| JJ Peterka: 1+ assists | 0.212 | 0.305 | 32/71 | +0.063 | STANDARD |
| Artemi Panarin: 2+ points | 0.212 | 0.300 | 33/73 | +0.045 | STANDARD |
| Hampus Lindholm: 1+ points | 0.368 | 0.285 | 29/72 | +0.063 | STANDARD |

**EDM @ UTA** · priced 155/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.03, exp saves 23.36 (sd 6.56), pull risk 0.07
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.77 (sd 6.81), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vasily Podkolzin: 1+ points | 0.645 | 0.475 | 48/53 | +0.147 | STANDARD |
| Mattias Ekholm: 1+ points | 0.469 | 0.320 | 34/70 | +0.114 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.454 | 0.310 | 32/70 | +0.118 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.226 | 0.355 | 37/66 | +0.098 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.393 | 0.270 | 28/74 | +0.099 | STANDARD |
| Vasily Podkolzin: 1+ goals | 0.355 | 0.270 | 29/75 | +0.051 | STANDARD |

**PIT @ VGK** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.53, exp saves 23.36 (sd 6.36), pull risk 0.049
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.73 (sd 6.79), pull risk 0.09

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.280 | 0.425 | 44/59 | +0.113 | STANDARD |
| Jack Eichel: 1+ assists | 0.481 | 0.615 | 64/41 | +0.092 | STANDARD |
| Mitch Marner: 2+ points | 0.230 | 0.350 | 37/67 | +0.085 | STANDARD |
| Jack Eichel: 2+ assists | 0.136 | 0.250 | 28/78 | +0.072 | STANDARD |
| Evgeni Malkin: 1+ assists | 0.284 | 0.385 | 40/63 | +0.069 | STANDARD |
| Trevor Connelly: 1+ points | 0.390 | 0.490 | 50/52 | +0.072 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
