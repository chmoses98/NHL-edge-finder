# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T20:32:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4236 · contracts joined: 2544 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2269, 'CANNOT_TRUST_INPUTS': 275}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 384, 'game_early_goal': 11, 'first_goal': 391, 'game_winner': 22, 'player_goals': 678, 'game_overtime': 11, 'player_points': 515, 'goalie_saves': 15, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-3h | 0.481 | 0.519 | 0.167 | 7.09 | 3.48 | 3.61 | 237 (25/212) | CONFIRMED/PROBABLE |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-3h | 0.654 | 0.346 | 0.171 | 5.87 | 3.42 | 2.45 | 255 (25/230) | CONFIRMED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-3h | 0.641 | 0.359 | 0.172 | 6.03 | 3.45 | 2.57 | 219 (25/194) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-3h | 0.506 | 0.494 | 0.179 | 6.01 | 3.01 | 2.99 | 224 (25/199) | CONFIRMED/CONFIRMED |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-3h | 0.439 | 0.561 | 0.186 | 5.69 | 2.66 | 3.02 | 257 (25/232) | CONFIRMED/CONFIRMED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-3h | 0.539 | 0.461 | 0.167 | 6.81 | 3.53 | 3.27 | 216 (25/191) | CONFIRMED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-3h | 0.559 | 0.441 | 0.185 | 5.67 | 3.02 | 2.66 | 233 (25/208) | CONFIRMED/CONFIRMED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-3h | 0.362 | 0.638 | 0.167 | 6.16 | 2.64 | 3.52 | 224 (25/199) | CONFIRMED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-3h | 0.535 | 0.465 | 0.171 | 6.44 | 3.34 | 3.10 | 235 (25/210) | CONFIRMED/CONFIRMED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-3h | 0.370 | 0.630 | 0.167 | 6.31 | 2.74 | 3.56 | 235 (25/210) | CONFIRMED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-3h | 0.411 | 0.589 | 0.158 | 7.18 | 3.28 | 3.89 | 209 (25/184) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.638 | 0.515 | 0.540 | 52 | 49 |  | +0.101 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.362 | 0.475 | 0.452 | 48 | 53 |  | +0.091 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-COL2 | game_spread | 0.413 | 0.315 | 0.334 | 32 | 69 |  | +0.078 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.267 | 0.365 | 0.344 | 37 | 64 |  | +0.077 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.367 | 0.465 | 0.445 | 47 | 54 |  | +0.076 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.180 | 0.275 | 0.254 | 28 | 73 |  | +0.076 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.492 | 0.590 | 0.571 | 60 | 42 |  | +0.071 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.466 | 0.555 | 0.537 | 56 | 45 |  | +0.066 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.408 | 0.495 | 0.477 | 50 | 51 |  | +0.065 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.195 | 0.275 | 0.257 | 28 | 73 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.283 | 0.370 | 0.352 | 38 | 64 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03MINPHI-MIN2 | game_spread | 0.323 | 0.405 | 0.388 | 41 | 60 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.503 | 0.585 | 0.569 | 59 | 42 |  | +0.059 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.731 | 0.805 | 0.791 | 81 | 20 |  | +0.058 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.359 | 0.285 | 0.299 | 29 | 72 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.641 | 0.715 | 0.701 | 72 | 29 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.097 | 0.165 | 0.149 | 17 | 84 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.469 | 0.545 | 0.530 | 55 | 46 |  | +0.053 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.439 | 0.365 | 0.379 | 37 | 64 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN5 | team_total | 0.185 | 0.260 | 0.244 | 27 | 75 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.264 | 0.340 | 0.324 | 35 | 67 |  | +0.051 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.286 | 0.360 | 0.344 | 37 | 65 |  | +0.048 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN3 | team_total | 0.597 | 0.670 | 0.656 | 68 | 34 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.133 | 0.200 | 0.185 | 21 | 81 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG4 | team_total | 0.240 | 0.305 | 0.291 | 31 | 70 |  | +0.045 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.222 | 0.285 | 0.272 | 29 | 72 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.683 | 0.755 | 0.742 | 77 | 26 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-6 | game_total | 0.470 | 0.535 | 0.522 | 54 | 47 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.561 | 0.625 | 0.613 | 63 | 38 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR4 | team_total | 0.468 | 0.405 | 0.418 | 41 | 60 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.119 | 0.175 | 0.162 | 18 | 83 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.441 | 0.505 | 0.492 | 51 | 50 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.386 | 0.320 | 0.333 | 33 | 69 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-COL3 | game_spread | 0.272 | 0.210 | 0.221 | 22 | 80 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.209 | 0.150 | 0.161 | 16 | 86 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-5 | game_total | 0.708 | 0.770 | 0.758 | 78 | 24 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.535 | 0.595 | 0.583 | 60 | 41 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.465 | 0.405 | 0.417 | 41 | 60 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.741 | 0.800 | 0.789 | 81 | 21 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03WPGMTL-MTL | game_winner | 0.654 | 0.595 | 0.607 | 60 | 41 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL3 | team_total | 0.691 | 0.635 | 0.647 | 64 | 37 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-7 | game_total | 0.358 | 0.420 | 0.407 | 43 | 59 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR5 | team_total | 0.277 | 0.225 | 0.235 | 23 | 78 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6 | team_total | 0.141 | 0.090 | 0.099 | 10 | 92 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03UTATOR-TOR | game_winner | 0.481 | 0.425 | 0.436 | 43 | 58 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03UTATOR-UTA | game_winner | 0.519 | 0.575 | 0.564 | 58 | 43 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03EDMNJ-8 | game_total | 0.297 | 0.245 | 0.255 | 25 | 76 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.861 | 0.910 | 0.902 | 92 | 10 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-5 | game_total | 0.704 | 0.760 | 0.749 | 77 | 25 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 | team_total | 0.600 | 0.540 | 0.552 | 55 | 47 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.171 | 0.125 | 0.133 | 13 | 88 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-7 | game_total | 0.360 | 0.415 | 0.404 | 42 | 59 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 | team_total | 0.451 | 0.515 | 0.502 | 53 | 50 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.559 | 0.505 | 0.516 | 51 | 50 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03EDMNJ-10 | game_total | 0.105 | 0.065 | 0.072 | 7 | 94 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.130 | 0.180 | 0.169 | 19 | 83 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-4 | game_total | 0.800 | 0.850 | 0.841 | 86 | 16 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03EDMNJ-7 | game_total | 0.487 | 0.435 | 0.445 | 44 | 57 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR3 | team_total | 0.676 | 0.625 | 0.636 | 63 | 38 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL5 | team_total | 0.131 | 0.180 | 0.169 | 19 | 83 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03WPGMTL-6 | game_total | 0.505 | 0.555 | 0.545 | 56 | 45 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03WPGMTL-WPG | game_winner | 0.346 | 0.400 | 0.389 | 41 | 61 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-DET2 | game_spread | 0.175 | 0.135 | 0.142 | 14 | 87 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03WPGMTL-WPG2 | game_spread | 0.163 | 0.205 | 0.196 | 21 | 80 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.202 | 0.245 | 0.236 | 25 | 76 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.401 | 0.350 | 0.360 | 36 | 66 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03UTATOR-TOR2 | game_spread | 0.287 | 0.245 | 0.253 | 25 | 76 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.390 | 0.345 | 0.354 | 35 | 66 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.297 | 0.250 | 0.259 | 26 | 76 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03VGKPIT-8 | game_total | 0.349 | 0.305 | 0.313 | 31 | 70 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.439 | 0.485 | 0.476 | 49 | 52 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL4 | team_total | 0.481 | 0.430 | 0.440 | 44 | 58 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-10 | game_total | 0.160 | 0.120 | 0.127 | 13 | 89 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL6 | team_total | 0.139 | 0.100 | 0.107 | 11 | 91 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-7 | game_total | 0.589 | 0.545 | 0.554 | 55 | 46 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-8 | game_total | 0.186 | 0.225 | 0.217 | 23 | 78 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG2 | team_total | 0.695 | 0.745 | 0.735 | 76 | 27 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6 | team_total | 0.096 | 0.055 | 0.062 | 7 | 96 |  | +0.021 | CANNOT_TRUST_INPUTS |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 0.481 | 0.500 | 0.167 | 0.213 | 7.09 | 6.78 | 0.989/0.999 | KXNHLTOTAL-26NOV03UTATOR-8 -0.052 |
| WPG @ MTL | 0.654 | 0.584 | 0.171 | 0.213 | 5.87 | 6.29 | 0.983/1.002 | KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 +0.102 |
| DET @ TBL | 0.641 | 0.644 | 0.172 | 0.208 | 6.03 | 6.23 | 0.958/1.004 | KXNHLTOTAL-26NOV03DETTB-7 +0.038 |
| STL @ NYR | 0.506 | 0.517 | 0.179 | 0.222 | 6.01 | 6.25 | 0.988/0.977 | KXNHLTOTAL-26NOV03STLNYR-7 +0.041 |
| MIN @ PHI | 0.439 | 0.518 | 0.186 | 0.223 | 5.69 | 6.00 | 0.995/0.991 | KXNHLTEAMTOTAL-26NOV03MINPHI-PHI3 +0.095 |
| VGK @ PIT | 0.539 | 0.522 | 0.167 | 0.215 | 6.81 | 6.55 | 1.042/1.004 | KXNHLTOTAL-26NOV03VGKPIT-6 -0.047 |
| DAL @ WSH | 0.559 | 0.550 | 0.185 | 0.222 | 5.67 | 6.13 | 0.939/0.995 | KXNHLTOTAL-26NOV03DALWSH-7 +0.078 |
| COL @ CBJ | 0.362 | 0.463 | 0.167 | 0.220 | 6.16 | 6.40 | 1.008/0.971 | KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 +0.110 |
| EDM @ NJD | 0.535 | 0.510 | 0.171 | 0.212 | 6.44 | 6.62 | 0.950/1.023 | KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 +0.042 |
| CAR @ NSH | 0.370 | 0.455 | 0.167 | 0.214 | 6.31 | 6.56 | 1.005/0.998 | KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4 +0.095 |
| ANA @ VAN | 0.411 | 0.453 | 0.158 | 0.211 | 7.18 | 6.91 | 1.027/1.017 | KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4 -0.053 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ TOR** · priced 180/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.46 (sd 7.24), pull risk 0.077
- UTA net: Sebastian Cossa (PROBABLE) exp shots 26.79, exp saves 23.1 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Cossa: 23+ saves | 0.534 | 0.440 | 48/60 | +0.037 |  |
| Teddy Blueger: 1+ goals | 0.177 | 0.095 | 11/92 | +0.060 | STANDARD |
| Auston Matthews: 1+ assists | 0.408 | 0.490 | 50/52 | +0.054 | STANDARD |
| Morgan Rielly: 1+ assists | 0.340 | 0.265 | 27/74 | +0.056 | STANDARD |
| Lawson Crouse: 1+ assists | 0.285 | 0.210 | 22/80 | +0.053 | STANDARD |
| Lawson Crouse: 1+ points | 0.443 | 0.370 | 38/64 | +0.047 | STANDARD |

**WPG @ MTL** · priced 195/204 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.0, exp saves 23.62 (sd 6.23), pull risk 0.049
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.07, exp saves 22.98 (sd 6.51), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Barron: 1+ points | 0.281 | 0.115 | 21/98 | +0.059 | STANDARD |
| Isak Rosen: 1+ points | 0.268 | 0.125 | 23/98 | +0.025 | STANDARD |
| Alexandre Texier: 1+ assists | 0.273 | 0.135 | 25/98 | +0.010 | STANDARD |
| Alexandre Carrier: 1+ assists | 0.260 | 0.125 | 23/98 | +0.017 | STANDARD |
| Oliver Kapanen: 1+ assists | 0.244 | 0.125 | 23/98 | +0.002 | STANDARD |
| Dylan Samberg: 1+ assists | 0.251 | 0.135 | 20/93 | +0.039 | STANDARD |

**DET @ TBL** · priced 157/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.08 (sd 6.22), pull risk 0.044
- DET net: John Gibson (PROJECTED) exp shots 27.95, exp saves 23.68 (sd 6.8), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.524 | 0.645 | 65/36 | +0.100 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.169 | 0.285 | 30/73 | +0.088 | STANDARD |
| Nikita Kucherov: 2+ points | 0.338 | 0.445 | 45/56 | +0.085 | STANDARD |
| Nikita Kucherov: 3+ points | 0.122 | 0.205 | 22/81 | +0.057 | STANDARD |
| Lucas Raymond: 1+ assists | 0.332 | 0.410 | 43/61 | +0.042 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.329 | 0.255 | 26/75 | +0.056 | STANDARD |

**STL @ NYR** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.61, exp saves 23.04 (sd 6.32), pull risk 0.055
- STL net: Joel Hofer (CONFIRMED) exp shots 26.51, exp saves 22.95 (sd 6.34), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ assists | 0.273 | 0.340 | 35/67 | +0.042 | STANDARD |
| Philip Broberg: 1+ points | 0.486 | 0.420 | 43/59 | +0.038 | STANDARD |
| Robert Thomas: 1+ assists | 0.429 | 0.490 | 50/52 | +0.034 | STANDARD |
| Tye Kartye: 1+ points | 0.416 | 0.360 | 38/66 | +0.020 | STANDARD |
| Dylan Garand: 23+ saves | 0.530 | 0.475 | 50/55 | +0.013 |  |
| Pavel Dorofeyev: 1+ points | 0.492 | 0.545 | 56/47 | +0.020 | STANDARD |

**MIN @ PHI** · priced 205/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.47, exp saves 24.7 (sd 6.68), pull risk 0.058
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 25.89, exp saves 22.45 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.245 | 0.410 | 42/60 | +0.138 | STANDARD |
| Yakov Trenin: 1+ points | 0.273 | 0.110 | 20/98 | +0.061 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.601 | 0.760 | 77/25 | +0.136 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.389 | 0.535 | 54/47 | +0.123 | STANDARD |
| Olli Maatta: 1+ points | 0.239 | 0.095 | 17/98 | +0.059 | STANDARD |
| Matt Boldy: 1+ assists | 0.374 | 0.510 | 52/50 | +0.108 | STANDARD |

**VGK @ PIT** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.98, exp saves 23.37 (sd 6.5), pull risk 0.066
- VGK net: Adin Hill (PROJECTED) exp shots 27.28, exp saves 23.52 (sd 6.54), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.439 | 0.540 | 55/47 | +0.074 | STANDARD |
| Mitch Marner: 1+ assists | 0.422 | 0.520 | 53/49 | +0.070 | STANDARD |
| Mitch Marner: 1+ points | 0.557 | 0.655 | 66/35 | +0.077 | STANDARD |
| Mitch Marner: 2+ points | 0.199 | 0.280 | 30/74 | +0.047 | STANDARD |
| Jack Eichel: 2+ points | 0.241 | 0.320 | 33/69 | +0.054 | STANDARD |
| Sidney Crosby: 1+ assists | 0.412 | 0.480 | 49/53 | +0.040 | STANDARD |

**DAL @ WSH** · priced 178/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 26.25, exp saves 22.86 (sd 6.28), pull risk 0.053
- DAL net: Jake Oettinger (CONFIRMED) exp shots 25.46, exp saves 21.82 (sd 6.17), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Hryckowian: 2+ points | 0.047 | 0.150 | 29/99 | -0.038 | STANDARD |
| Miro Heiskanen: 1+ points | 0.447 | 0.550 | 56/46 | +0.075 | STANDARD |
| Aliaksei Protas: 1+ points | 0.443 | 0.350 | 36/66 | +0.066 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.345 | 0.430 | 44/58 | +0.058 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.410 | 0.495 | 51/52 | +0.052 | STANDARD |
| Mikko Rantanen: 2+ points | 0.202 | 0.285 | 30/73 | +0.055 | STANDARD |

**COL @ CBJ** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 29.48, exp saves 25.52 (sd 6.84), pull risk 0.064
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.34 (sd 6.32), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Sillinger: 1+ assists | 0.274 | 0.135 | 25/98 | +0.011 | STANDARD |
| Scott Wedgewood: 26+ saves | 0.356 | 0.475 | 49/54 | +0.087 |  |
| Damon Severson: 1+ points | 0.417 | 0.320 | 34/70 | +0.061 | STANDARD |
| Damon Severson: 1+ assists | 0.337 | 0.255 | 27/76 | +0.053 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.301 | 0.375 | 38/63 | +0.053 | STANDARD |
| Zach Werenski: 1+ assists | 0.484 | 0.555 | 57/46 | +0.039 | STANDARD |

**EDM @ NJD** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.46, exp saves 22.85 (sd 6.47), pull risk 0.067
- EDM net: Tristan Jarry (CONFIRMED) exp shots 29.41, exp saves 25.29 (sd 6.96), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.370 | 0.495 | 50/51 | +0.102 | STANDARD |
| Connor McDavid: 2+ assists | 0.168 | 0.285 | 30/73 | +0.088 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.525 | 53/48 | +0.090 | STANDARD |
| Connor McDavid: 1+ assists | 0.533 | 0.645 | 65/36 | +0.091 | STANDARD |
| Mathieu Joseph: 1+ points | 0.261 | 0.155 | 29/98 | -0.043 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.519 | 0.415 | 43/60 | +0.072 | STANDARD |

**CAR @ NSH** · priced 180/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 31.84, exp saves 27.15 (sd 7.47), pull risk 0.082
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.29 (sd 6.07), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Sebastian Aho: 2+ points | 0.179 | 0.290 | 31/73 | +0.077 | STANDARD |
| Sebastian Aho: 1+ points | 0.543 | 0.650 | 66/36 | +0.080 | STANDARD |
| Jaccob Slavin: 1+ assists | 0.233 | 0.140 | 26/98 | -0.041 | STANDARD |
| Sebastian Aho: 2+ assists | 0.071 | 0.155 | 17/86 | +0.060 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.347 | 0.425 | 44/59 | +0.046 | STANDARD |

**ANA @ VAN** · priced 147/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.41, exp saves 26.03 (sd 7.2), pull risk 0.081
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.99, exp saves 21.59 (sd 6.16), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ assists | 0.414 | 0.520 | 53/49 | +0.079 | STANDARD |
| Leo Carlsson: 2+ points | 0.230 | 0.315 | 33/70 | +0.056 | STANDARD |
| Linus Karlsson: 1+ goals | 0.245 | 0.170 | 19/85 | +0.044 | STANDARD |
| Marco Rossi: 1+ goals | 0.249 | 0.175 | 19/84 | +0.048 | STANDARD |
| Marco Rossi: 1+ points | 0.480 | 0.420 | 43/59 | +0.033 | STANDARD |
| Liam Ohgren: 1+ goals | 0.203 | 0.145 | 16/87 | +0.034 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
