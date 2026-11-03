# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T23:41:46Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4291 · contracts joined: 2599 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2324, 'CANNOT_TRUST_INPUTS': 275}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 401, 'game_early_goal': 11, 'first_goal': 392, 'game_winner': 22, 'player_goals': 679, 'game_overtime': 11, 'player_points': 547, 'goalie_saves': 19, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-10m | 0.481 | 0.519 | 0.167 | 7.09 | 3.48 | 3.61 | 246 (25/221) | CONFIRMED/PROBABLE |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-10m | 0.654 | 0.346 | 0.171 | 5.87 | 3.42 | 2.45 | 255 (25/230) | CONFIRMED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-10m | 0.641 | 0.359 | 0.172 | 6.03 | 3.45 | 2.57 | 223 (25/198) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-10m | 0.506 | 0.494 | 0.179 | 6.01 | 3.01 | 2.99 | 224 (25/199) | CONFIRMED/CONFIRMED |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-10m | 0.439 | 0.561 | 0.186 | 5.69 | 2.66 | 3.02 | 261 (25/236) | CONFIRMED/CONFIRMED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-10m | 0.539 | 0.461 | 0.167 | 6.81 | 3.53 | 3.27 | 245 (25/220) | CONFIRMED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-10m | 0.559 | 0.441 | 0.185 | 5.67 | 3.02 | 2.66 | 233 (25/208) | CONFIRMED/CONFIRMED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-10m | 0.362 | 0.638 | 0.167 | 6.16 | 2.64 | 3.52 | 226 (25/201) | CONFIRMED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-30m | 0.535 | 0.465 | 0.171 | 6.44 | 3.34 | 3.10 | 235 (25/210) | CONFIRMED/CONFIRMED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-60m | 0.370 | 0.630 | 0.167 | 6.31 | 2.74 | 3.56 | 236 (25/211) | CONFIRMED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-90m | 0.411 | 0.589 | 0.158 | 7.18 | 3.28 | 3.89 | 215 (25/190) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.362 | 0.475 | 0.452 | 48 | 53 |  | +0.091 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.638 | 0.525 | 0.548 | 53 | 48 |  | +0.091 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.367 | 0.475 | 0.453 | 48 | 53 |  | +0.086 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-COL2 | game_spread | 0.413 | 0.315 | 0.334 | 32 | 69 |  | +0.078 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.267 | 0.365 | 0.344 | 37 | 64 |  | +0.077 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.180 | 0.275 | 0.254 | 28 | 73 |  | +0.076 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.408 | 0.505 | 0.485 | 51 | 50 |  | +0.075 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.492 | 0.585 | 0.567 | 59 | 42 |  | +0.071 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.283 | 0.375 | 0.356 | 38 | 63 |  | +0.071 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.466 | 0.560 | 0.541 | 57 | 45 |  | +0.066 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.359 | 0.275 | 0.291 | 28 | 73 |  | +0.065 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.641 | 0.725 | 0.709 | 73 | 28 |  | +0.065 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.195 | 0.275 | 0.257 | 28 | 73 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.264 | 0.345 | 0.328 | 35 | 66 |  | +0.060 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.503 | 0.585 | 0.569 | 59 | 42 |  | +0.059 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.731 | 0.805 | 0.791 | 81 | 20 |  | +0.058 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN3 | team_total | 0.597 | 0.675 | 0.660 | 68 | 33 |  | +0.058 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.097 | 0.165 | 0.149 | 17 | 84 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.439 | 0.365 | 0.379 | 37 | 64 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN5 | team_total | 0.185 | 0.255 | 0.240 | 26 | 75 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.386 | 0.315 | 0.329 | 32 | 69 |  | +0.051 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03MINPHI-MIN2 | game_spread | 0.323 | 0.400 | 0.384 | 41 | 61 |  | +0.051 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.286 | 0.355 | 0.341 | 36 | 65 |  | +0.048 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.222 | 0.285 | 0.272 | 29 | 72 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.683 | 0.750 | 0.737 | 76 | 26 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-5 | game_total | 0.704 | 0.765 | 0.754 | 77 | 24 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.469 | 0.535 | 0.522 | 54 | 47 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-6 | game_total | 0.470 | 0.535 | 0.522 | 54 | 47 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.561 | 0.625 | 0.613 | 63 | 38 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 | team_total | 0.451 | 0.515 | 0.502 | 52 | 49 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR4 | team_total | 0.468 | 0.405 | 0.418 | 41 | 60 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.119 | 0.175 | 0.162 | 18 | 83 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.441 | 0.505 | 0.492 | 51 | 50 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-4 | game_total | 0.800 | 0.855 | 0.845 | 86 | 15 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-COL3 | game_spread | 0.272 | 0.215 | 0.226 | 22 | 79 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-5 | game_total | 0.708 | 0.770 | 0.758 | 78 | 24 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.535 | 0.595 | 0.583 | 60 | 41 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.465 | 0.405 | 0.417 | 41 | 60 |  | +0.039 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.741 | 0.800 | 0.789 | 81 | 21 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03WPGMTL-MTL | game_winner | 0.654 | 0.595 | 0.607 | 60 | 41 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03WPGMTL-WPG | game_winner | 0.346 | 0.405 | 0.393 | 41 | 60 |  | +0.038 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.133 | 0.195 | 0.181 | 21 | 82 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2 | team_total | 0.804 | 0.860 | 0.850 | 87 | 15 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG4 | team_total | 0.240 | 0.295 | 0.283 | 30 | 71 |  | +0.036 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-7 | game_total | 0.358 | 0.415 | 0.403 | 42 | 59 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR5 | team_total | 0.277 | 0.225 | 0.235 | 23 | 78 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.202 | 0.255 | 0.244 | 26 | 75 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.390 | 0.335 | 0.346 | 34 | 67 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03UTATOR-TOR | game_winner | 0.481 | 0.425 | 0.436 | 43 | 58 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03UTATOR-UTA | game_winner | 0.519 | 0.575 | 0.564 | 58 | 43 |  | +0.034 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.861 | 0.910 | 0.902 | 92 | 10 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.171 | 0.125 | 0.133 | 13 | 88 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-7 | game_total | 0.360 | 0.415 | 0.404 | 42 | 59 |  | +0.033 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.559 | 0.505 | 0.516 | 51 | 50 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN5 | team_total | 0.242 | 0.195 | 0.204 | 20 | 81 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.130 | 0.180 | 0.169 | 19 | 83 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR3 | team_total | 0.676 | 0.625 | 0.636 | 63 | 38 |  | +0.030 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.209 | 0.160 | 0.169 | 17 | 85 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03WPGMTL-6 | game_total | 0.505 | 0.555 | 0.545 | 56 | 45 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03EDMNJ-EDM2 | game_spread | 0.260 | 0.215 | 0.223 | 22 | 79 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-DET2 | game_spread | 0.175 | 0.135 | 0.142 | 14 | 87 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN4 | team_total | 0.423 | 0.375 | 0.384 | 38 | 63 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03WPGMTL-WPG2 | game_spread | 0.163 | 0.205 | 0.196 | 21 | 80 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DETTB-5 | game_total | 0.753 | 0.795 | 0.787 | 80 | 21 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL3 | team_total | 0.691 | 0.640 | 0.651 | 65 | 37 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03ANAVAN-ANA | game_winner | 0.589 | 0.635 | 0.626 | 64 | 37 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.401 | 0.355 | 0.364 | 36 | 65 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03UTATOR-TOR2 | game_spread | 0.287 | 0.245 | 0.253 | 25 | 76 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.297 | 0.255 | 0.263 | 26 | 75 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6 | team_total | 0.141 | 0.095 | 0.103 | 11 | 92 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.439 | 0.485 | 0.476 | 49 | 52 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03EDMNJ-8 | game_total | 0.297 | 0.255 | 0.263 | 26 | 75 |  | +0.023 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-10 | game_total | 0.160 | 0.120 | 0.127 | 13 | 89 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL6 | team_total | 0.139 | 0.100 | 0.107 | 11 | 91 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ6 | team_total | 0.053 | 0.085 | 0.077 | 9 | 92 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03COLCBJ-5 | game_total | 0.767 | 0.805 | 0.798 | 81 | 20 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-8 | game_total | 0.186 | 0.225 | 0.217 | 23 | 78 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG2 | team_total | 0.695 | 0.740 | 0.731 | 75 | 27 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03WPGMTL-7 | game_total | 0.392 | 0.435 | 0.426 | 44 | 57 |  | +0.021 | CANNOT_TRUST_INPUTS |

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

**UTA @ TOR** · priced 189/195 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.46 (sd 7.24), pull risk 0.077
- UTA net: Sebastian Cossa (PROBABLE) exp shots 26.79, exp saves 23.1 (sd 6.49), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.408 | 0.495 | 50/51 | +0.064 | STANDARD |
| Lawson Crouse: 1+ assists | 0.285 | 0.200 | 22/82 | +0.053 | STANDARD |
| Lawson Crouse: 1+ points | 0.443 | 0.365 | 37/64 | +0.057 | STANDARD |
| Teddy Blueger: 1+ goals | 0.177 | 0.105 | 11/90 | +0.060 | STANDARD |
| Clayton Keller: 1+ assists | 0.455 | 0.525 | 53/48 | +0.048 | STANDARD |
| Logan Cooley: 2+ points | 0.187 | 0.255 | 26/75 | +0.050 | STANDARD |

**WPG @ MTL** · priced 195/204 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.0, exp saves 23.62 (sd 6.23), pull risk 0.049
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.07, exp saves 22.98 (sd 6.51), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brad Lambert: 1+ points | 0.167 | 0.450 | 73/83 | -0.006 | STANDARD |
| Morgan Barron: 1+ points | 0.281 | 0.160 | 21/89 | +0.059 | STANDARD |
| Dylan Samberg: 1+ points | 0.300 | 0.205 | 22/81 | +0.068 | STANDARD |
| Dylan DeMelo: 1+ points | 0.224 | 0.130 | 19/93 | +0.023 | STANDARD |
| Oliver Kapanen: 1+ assists | 0.244 | 0.155 | 19/88 | +0.044 | STANDARD |
| Cole Perfetti: 1+ assists | 0.374 | 0.285 | 30/73 | +0.059 | STANDARD |

**DET @ TBL** · priced 161/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.08 (sd 6.22), pull risk 0.044
- DET net: John Gibson (PROJECTED) exp shots 27.95, exp saves 23.68 (sd 6.8), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Gibson: 27+ saves | 0.328 | 0.485 | 49/52 | +0.135 |  |
| Nikita Kucherov: 2+ points | 0.338 | 0.475 | 49/54 | +0.105 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.524 | 0.655 | 66/35 | +0.110 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.169 | 0.265 | 28/75 | +0.068 | STANDARD |
| Nikita Kucherov: 3+ points | 0.122 | 0.210 | 22/80 | +0.067 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.329 | 0.255 | 26/75 | +0.056 | STANDARD |

**STL @ NYR** · priced 172/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.61, exp saves 23.04 (sd 6.32), pull risk 0.055
- STL net: Joel Hofer (CONFIRMED) exp shots 26.51, exp saves 22.95 (sd 6.34), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.327 | 0.230 | 25/79 | +0.064 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.384 | 0.300 | 31/71 | +0.059 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.273 | 0.345 | 35/66 | +0.052 | STANDARD |
| Pavel Buchnevich: 1+ assists | 0.210 | 0.280 | 29/73 | +0.046 | STANDARD |
| Dylan Garand: 23+ saves | 0.530 | 0.465 | 48/55 | +0.033 |  |
| Philip Broberg: 1+ points | 0.486 | 0.425 | 43/58 | +0.038 | STANDARD |

**MIN @ PHI** · priced 209/210 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.47, exp saves 24.7 (sd 6.68), pull risk 0.058
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 25.89, exp saves 22.45 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.245 | 0.425 | 43/58 | +0.158 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.389 | 0.545 | 55/46 | +0.133 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.601 | 0.755 | 76/25 | +0.136 | STANDARD |
| Matt Boldy: 2+ points | 0.211 | 0.350 | 36/66 | +0.113 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.357 | 0.495 | 50/51 | +0.116 | STANDARD |
| Matt Boldy: 1+ assists | 0.374 | 0.505 | 51/50 | +0.108 | STANDARD |

**VGK @ PIT** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.98, exp saves 23.37 (sd 6.5), pull risk 0.066
- VGK net: Adin Hill (PROJECTED) exp shots 27.28, exp saves 23.52 (sd 6.54), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.422 | 0.520 | 53/49 | +0.070 | STANDARD |
| Mitch Marner: 1+ points | 0.557 | 0.655 | 66/35 | +0.077 | STANDARD |
| Jack Eichel: 1+ assists | 0.439 | 0.525 | 53/48 | +0.064 | STANDARD |
| Brayden McNabb: 1+ points | 0.335 | 0.260 | 27/75 | +0.051 | STANDARD |
| Jack Eichel: 2+ points | 0.241 | 0.315 | 32/69 | +0.054 | STANDARD |
| Sidney Crosby: 1+ assists | 0.412 | 0.480 | 49/53 | +0.040 | STANDARD |

**DAL @ WSH** · priced 178/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 26.25, exp saves 22.86 (sd 6.28), pull risk 0.053
- DAL net: Jake Oettinger (CONFIRMED) exp shots 25.46, exp saves 21.82 (sd 6.17), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.447 | 0.560 | 57/45 | +0.085 | STANDARD |
| Jake Oettinger: 23+ saves | 0.452 | 0.540 | 56/48 | +0.050 |  |
| Aliaksei Protas: 1+ points | 0.443 | 0.355 | 36/65 | +0.066 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.389 | 0.470 | 48/54 | +0.054 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.345 | 0.425 | 43/58 | +0.058 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.410 | 0.490 | 50/52 | +0.052 | STANDARD |

**COL @ CBJ** · priced 174/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 29.48, exp saves 25.52 (sd 6.84), pull risk 0.064
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.34 (sd 6.32), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Scott Wedgewood: 26+ saves | 0.356 | 0.465 | 48/55 | +0.077 |  |
| Nathan MacKinnon: 2+ points | 0.301 | 0.395 | 41/62 | +0.063 | STANDARD |
| Damon Severson: 1+ points | 0.417 | 0.330 | 34/68 | +0.061 | STANDARD |
| Damon Severson: 1+ assists | 0.337 | 0.265 | 27/74 | +0.053 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.458 | 0.525 | 54/49 | +0.035 | STANDARD |
| Zach Werenski: 1+ assists | 0.484 | 0.550 | 56/46 | +0.039 | STANDARD |

**EDM @ NJD** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.46, exp saves 22.85 (sd 6.47), pull risk 0.067
- EDM net: Tristan Jarry (CONFIRMED) exp shots 29.41, exp saves 25.29 (sd 6.96), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.370 | 0.500 | 51/51 | +0.102 | STANDARD |
| Connor McDavid: 1+ assists | 0.533 | 0.655 | 66/35 | +0.101 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.525 | 53/48 | +0.090 | STANDARD |
| Connor McDavid: 2+ assists | 0.168 | 0.280 | 29/73 | +0.088 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.519 | 0.420 | 43/59 | +0.072 | STANDARD |
| Brett Pesce: 1+ points | 0.323 | 0.230 | 26/80 | +0.049 | STANDARD |

**CAR @ NSH** · priced 181/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 31.84, exp saves 27.15 (sd 7.47), pull risk 0.082
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.29 (sd 6.07), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Sebastian Aho: 2+ points | 0.179 | 0.295 | 31/72 | +0.087 | STANDARD |
| Sebastian Aho: 1+ points | 0.543 | 0.655 | 66/35 | +0.091 | STANDARD |
| Sebastian Aho: 2+ assists | 0.071 | 0.150 | 17/87 | +0.051 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.347 | 0.420 | 43/59 | +0.046 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.387 | 0.460 | 47/55 | +0.045 | STANDARD |

**ANA @ VAN** · priced 156/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROBABLE) exp shots 30.41, exp saves 26.03 (sd 7.2), pull risk 0.081
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.99, exp saves 21.59 (sd 6.16), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ assists | 0.414 | 0.535 | 54/47 | +0.099 | STANDARD |
| Leo Carlsson: 2+ points | 0.230 | 0.335 | 34/67 | +0.085 | STANDARD |
| Liam Ohgren: 1+ points | 0.434 | 0.340 | 35/67 | +0.068 | STANDARD |
| Cutter Gauthier: 2+ points | 0.222 | 0.310 | 33/71 | +0.053 | STANDARD |
| Liam Ohgren: 1+ assists | 0.292 | 0.205 | 21/80 | +0.070 | STANDARD |
| Linus Karlsson: 1+ goals | 0.245 | 0.165 | 17/84 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
