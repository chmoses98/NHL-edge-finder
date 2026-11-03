# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T16:50:22Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4039 · contracts joined: 2347 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2072, 'CANNOT_TRUST_INPUTS': 275}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 306, 'game_early_goal': 11, 'first_goal': 393, 'game_winner': 22, 'player_goals': 672, 'game_overtime': 11, 'player_points': 408, 'goalie_saves': 7, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-6h | 0.479 | 0.521 | 0.171 | 7.06 | 3.45 | 3.61 | 236 (25/211) | CONFIRMED/PROJECTED |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-6h | 0.669 | 0.331 | 0.167 | 6.00 | 3.54 | 2.46 | 196 (25/171) | CONFIRMED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-6h | 0.641 | 0.359 | 0.172 | 6.03 | 3.45 | 2.57 | 215 (25/190) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-6h | 0.509 | 0.491 | 0.175 | 6.03 | 3.04 | 2.99 | 204 (25/179) | CONFIRMED/PROBABLE |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-6h | 0.439 | 0.561 | 0.186 | 5.69 | 2.66 | 3.02 | 213 (25/188) | CONFIRMED/CONFIRMED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-6h | 0.539 | 0.461 | 0.167 | 6.81 | 3.53 | 3.27 | 216 (25/191) | CONFIRMED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-6h | 0.568 | 0.432 | 0.187 | 5.72 | 3.06 | 2.66 | 219 (25/194) | CONFIRMED/PROJECTED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-6h | 0.362 | 0.638 | 0.167 | 6.16 | 2.64 | 3.52 | 212 (25/187) | CONFIRMED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-6h | 0.532 | 0.468 | 0.173 | 6.40 | 3.30 | 3.10 | 217 (25/192) | CONFIRMED/PROJECTED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-6h | 0.370 | 0.630 | 0.167 | 6.31 | 2.74 | 3.56 | 211 (25/186) | CONFIRMED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-6h | 0.421 | 0.579 | 0.162 | 7.11 | 3.29 | 3.82 | 208 (25/183) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.362 | 0.475 | 0.452 | 48 | 53 |  | +0.091 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.638 | 0.525 | 0.548 | 53 | 48 |  | +0.091 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.180 | 0.275 | 0.254 | 28 | 73 |  | +0.076 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.492 | 0.590 | 0.571 | 60 | 42 |  | +0.071 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-COL2 | game_spread | 0.413 | 0.325 | 0.342 | 33 | 68 |  | +0.068 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.267 | 0.355 | 0.336 | 36 | 65 |  | +0.068 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.466 | 0.560 | 0.541 | 57 | 45 |  | +0.066 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.367 | 0.460 | 0.441 | 47 | 55 |  | +0.066 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.195 | 0.275 | 0.257 | 28 | 73 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.283 | 0.370 | 0.352 | 38 | 64 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03MINPHI-MIN2 | game_spread | 0.323 | 0.405 | 0.388 | 41 | 60 |  | +0.061 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.264 | 0.350 | 0.332 | 36 | 66 |  | +0.060 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.731 | 0.805 | 0.791 | 81 | 20 |  | +0.058 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.506 | 0.585 | 0.569 | 59 | 42 |  | +0.057 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.288 | 0.370 | 0.353 | 38 | 64 |  | +0.055 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.408 | 0.485 | 0.469 | 49 | 52 |  | +0.055 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.359 | 0.285 | 0.299 | 29 | 72 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.641 | 0.715 | 0.701 | 72 | 29 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.097 | 0.165 | 0.149 | 17 | 84 |  | +0.054 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-6 | game_total | 0.470 | 0.545 | 0.530 | 55 | 46 |  | +0.053 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.439 | 0.365 | 0.379 | 37 | 64 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.737 | 0.805 | 0.793 | 81 | 20 |  | +0.052 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.432 | 0.505 | 0.490 | 51 | 50 |  | +0.050 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03COLCBJ-COL3 | game_spread | 0.272 | 0.205 | 0.217 | 21 | 80 |  | +0.050 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-5 | game_total | 0.708 | 0.775 | 0.763 | 78 | 23 |  | +0.049 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN3 | team_total | 0.597 | 0.670 | 0.656 | 68 | 34 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.219 | 0.285 | 0.271 | 29 | 72 |  | +0.047 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-7 | game_total | 0.358 | 0.425 | 0.411 | 43 | 58 |  | +0.045 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.683 | 0.750 | 0.737 | 76 | 26 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG4 | team_total | 0.243 | 0.305 | 0.292 | 31 | 70 |  | +0.043 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.480 | 0.545 | 0.532 | 55 | 46 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.118 | 0.175 | 0.162 | 18 | 83 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.561 | 0.625 | 0.613 | 63 | 38 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 | team_total | 0.450 | 0.515 | 0.502 | 52 | 49 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN5 | team_total | 0.185 | 0.255 | 0.240 | 27 | 76 |  | +0.042 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.387 | 0.325 | 0.337 | 33 | 68 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.532 | 0.595 | 0.583 | 60 | 41 |  | +0.041 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.568 | 0.505 | 0.518 | 51 | 50 |  | +0.040 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.133 | 0.195 | 0.181 | 21 | 82 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03WPGMTL-WPG2 | game_spread | 0.152 | 0.205 | 0.193 | 21 | 80 |  | +0.037 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 | team_total | 0.602 | 0.545 | 0.557 | 55 | 46 |  | +0.035 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03WPGMTL-WPG | game_winner | 0.331 | 0.385 | 0.374 | 39 | 62 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03WPGMTL-MTL | game_winner | 0.669 | 0.615 | 0.626 | 62 | 39 |  | +0.032 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.196 | 0.245 | 0.235 | 25 | 76 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6 | team_total | 0.138 | 0.095 | 0.102 | 10 | 91 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-8 | game_total | 0.186 | 0.240 | 0.228 | 25 | 77 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.468 | 0.415 | 0.425 | 42 | 59 |  | +0.031 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03WPGMTL-WPG3 | game_spread | 0.074 | 0.115 | 0.106 | 12 | 89 |  | +0.029 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL5 | team_total | 0.132 | 0.185 | 0.173 | 20 | 83 |  | +0.028 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.207 | 0.155 | 0.164 | 17 | 86 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.393 | 0.345 | 0.354 | 35 | 66 |  | +0.027 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2 | team_total | 0.804 | 0.855 | 0.846 | 87 | 16 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03EDMNJ-NJ2 | game_spread | 0.318 | 0.365 | 0.355 | 37 | 64 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03MINPHI-9 | game_total | 0.125 | 0.165 | 0.156 | 17 | 84 |  | +0.026 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL3 | team_total | 0.691 | 0.640 | 0.651 | 65 | 37 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-5 | game_total | 0.712 | 0.755 | 0.747 | 76 | 25 |  | +0.025 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR4 | team_total | 0.462 | 0.410 | 0.420 | 42 | 60 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-10 | game_total | 0.162 | 0.120 | 0.128 | 13 | 89 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-9 | game_total | 0.298 | 0.255 | 0.263 | 26 | 75 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.162 | 0.125 | 0.132 | 13 | 88 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.439 | 0.485 | 0.476 | 49 | 52 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL4 | team_total | 0.481 | 0.430 | 0.440 | 44 | 58 |  | +0.024 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.861 | 0.905 | 0.897 | 92 | 11 |  | +0.023 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL6 | team_total | 0.139 | 0.100 | 0.107 | 11 | 91 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-4 | game_total | 0.808 | 0.850 | 0.842 | 86 | 16 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DALWSH-7 | game_total | 0.372 | 0.415 | 0.406 | 42 | 59 |  | +0.022 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG2 | team_total | 0.695 | 0.740 | 0.731 | 75 | 27 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.294 | 0.250 | 0.259 | 26 | 76 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03EDMNJ-EDM2 | game_spread | 0.263 | 0.225 | 0.232 | 23 | 78 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.130 | 0.170 | 0.161 | 18 | 84 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03DALWSH-WSH2 | game_spread | 0.325 | 0.285 | 0.293 | 29 | 72 |  | +0.021 | CANNOT_TRUST_INPUTS |
| KXNHLSPREAD-26NOV03VGKPIT-PIT2 | game_spread | 0.335 | 0.295 | 0.303 | 30 | 71 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DETTB-6 | game_total | 0.533 | 0.575 | 0.567 | 58 | 43 |  | +0.020 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.385 | 0.340 | 0.349 | 35 | 67 |  | +0.019 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-COL5 | team_total | 0.282 | 0.240 | 0.248 | 25 | 77 |  | +0.018 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03COLCBJ-6 | game_total | 0.556 | 0.595 | 0.587 | 60 | 41 |  | +0.017 | CANNOT_TRUST_INPUTS |
| KXNHLTEAMTOTAL-26NOV03VGKPIT-PIT4 | team_total | 0.484 | 0.440 | 0.449 | 45 | 57 |  | +0.017 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03EDMNJ-8 | game_total | 0.290 | 0.250 | 0.258 | 26 | 76 |  | +0.016 | CANNOT_TRUST_INPUTS |
| KXNHLTOTAL-26NOV03DETTB-7 | game_total | 0.417 | 0.455 | 0.447 | 46 | 55 |  | +0.016 | CANNOT_TRUST_INPUTS |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 0.479 | 0.497 | 0.171 | 0.214 | 7.06 | 6.77 | 0.989/0.998 | KXNHLTOTAL-26NOV03UTATOR-8 -0.047 |
| WPG @ MTL | 0.669 | 0.586 | 0.167 | 0.215 | 6.00 | 6.28 | 0.983/0.998 | KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 +0.102 |
| DET @ TBL | 0.641 | 0.644 | 0.172 | 0.208 | 6.03 | 6.23 | 0.958/1.004 | KXNHLTOTAL-26NOV03DETTB-7 +0.038 |
| STL @ NYR | 0.509 | 0.518 | 0.175 | 0.220 | 6.03 | 6.27 | 0.988/0.985 | KXNHLTOTAL-26NOV03STLNYR-7 +0.040 |
| MIN @ PHI | 0.439 | 0.518 | 0.186 | 0.223 | 5.69 | 6.00 | 0.995/0.991 | KXNHLTEAMTOTAL-26NOV03MINPHI-PHI3 +0.095 |
| VGK @ PIT | 0.539 | 0.522 | 0.167 | 0.215 | 6.81 | 6.55 | 1.042/1.004 | KXNHLTOTAL-26NOV03VGKPIT-6 -0.047 |
| DAL @ WSH | 0.568 | 0.544 | 0.187 | 0.228 | 5.72 | 6.12 | 0.939/0.987 | KXNHLTOTAL-26NOV03DALWSH-7 +0.068 |
| COL @ CBJ | 0.362 | 0.463 | 0.167 | 0.220 | 6.16 | 6.40 | 1.008/0.971 | KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 +0.110 |
| EDM @ NJD | 0.532 | 0.506 | 0.173 | 0.216 | 6.40 | 6.58 | 0.950/1.010 | KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 +0.042 |
| CAR @ NSH | 0.370 | 0.455 | 0.167 | 0.214 | 6.31 | 6.56 | 1.005/0.998 | KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4 +0.095 |
| ANA @ VAN | 0.421 | 0.457 | 0.162 | 0.213 | 7.11 | 6.88 | 1.022/1.017 | KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4 -0.050 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status NO_BETS · gate PASS · 0 recommended · full analysis in card.md / packet.json `thesis_card`


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ TOR** · priced 179/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.47 (sd 7.23), pull risk 0.077
- UTA net: Sebastian Cossa (PROJECTED) exp shots 26.79, exp saves 23.14 (sd 6.52), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Rielly: 1+ assists | 0.349 | 0.255 | 27/76 | +0.066 | STANDARD |
| Auston Matthews: 1+ assists | 0.402 | 0.490 | 50/52 | +0.060 | STANDARD |
| Lawson Crouse: 1+ points | 0.443 | 0.355 | 38/67 | +0.046 | STANDARD |
| Sergei Bobrovsky: 29+ saves | 0.382 | 0.460 | 48/56 | +0.040 |  |
| Easton Cowan: 1+ assists | 0.353 | 0.280 | 29/73 | +0.049 | STANDARD |
| Jake McCabe: 1+ assists | 0.281 | 0.210 | 23/81 | +0.039 | STANDARD |

**WPG @ MTL** · priced 139/145 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 27.0, exp saves 23.57 (sd 6.38), pull risk 0.053
- WPG net: Nico Daws (PROJECTED) exp shots 27.07, exp saves 23.09 (sd 6.46), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Perfetti: 1+ assists | 0.372 | 0.280 | 30/74 | +0.057 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.311 | 0.240 | 25/77 | +0.048 | STANDARD |
| Cole Caufield: 1+ assists | 0.360 | 0.430 | 44/58 | +0.043 | STANDARD |
| Cole Perfetti: 1+ points | 0.528 | 0.460 | 48/56 | +0.030 | STANDARD |
| Oliver Kapanen: 1+ goals | 0.196 | 0.135 | 16/89 | +0.026 | STANDARD |
| Phillip Danault: 1+ points | 0.357 | 0.300 | 33/73 | +0.012 | STANDARD |

**DET @ TBL** · priced 153/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.08 (sd 6.22), pull risk 0.044
- DET net: John Gibson (PROJECTED) exp shots 27.95, exp saves 23.68 (sd 6.8), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.524 | 0.655 | 66/35 | +0.110 | STANDARD |
| Nikita Kucherov: 2+ points | 0.338 | 0.460 | 47/55 | +0.095 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.169 | 0.280 | 30/74 | +0.078 | STANDARD |
| Nikita Kucherov: 3+ points | 0.122 | 0.210 | 23/81 | +0.057 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.329 | 0.255 | 26/75 | +0.056 | STANDARD |
| Lucas Raymond: 1+ assists | 0.332 | 0.400 | 41/61 | +0.042 | STANDARD |

**STL @ NYR** · priced 150/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 26.61, exp saves 23.04 (sd 6.42), pull risk 0.057
- STL net: Joel Hofer (PROBABLE) exp shots 26.51, exp saves 22.91 (sd 6.36), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ assists | 0.388 | 0.305 | 32/71 | +0.053 | STANDARD |
| Dylan Garand: 23+ saves | 0.530 | 0.455 | 51/60 | +0.003 |  |
| Dylan Holloway: 1+ points | 0.559 | 0.485 | 50/53 | +0.041 | STANDARD |
| Philip Broberg: 1+ points | 0.483 | 0.425 | 44/59 | +0.026 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.278 | 0.335 | 35/68 | +0.027 | STANDARD |
| Dylan Holloway: 2+ points | 0.207 | 0.150 | 17/87 | +0.027 | STANDARD |

**MIN @ PHI** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.47, exp saves 24.7 (sd 6.68), pull risk 0.058
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 25.89, exp saves 22.45 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.245 | 0.405 | 42/61 | +0.128 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.389 | 0.535 | 55/48 | +0.113 | STANDARD |
| Matt Boldy: 1+ assists | 0.374 | 0.505 | 52/51 | +0.099 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.357 | 0.485 | 49/52 | +0.106 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.601 | 0.715 | 74/31 | +0.074 | STANDARD |
| Matt Boldy: 2+ points | 0.211 | 0.320 | 33/69 | +0.084 | STANDARD |

**VGK @ PIT** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.98, exp saves 23.37 (sd 6.5), pull risk 0.066
- VGK net: Adin Hill (PROJECTED) exp shots 27.28, exp saves 23.52 (sd 6.54), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.422 | 0.510 | 52/50 | +0.060 | STANDARD |
| Mitch Marner: 1+ points | 0.557 | 0.645 | 66/37 | +0.056 | STANDARD |
| Jack Eichel: 1+ assists | 0.439 | 0.520 | 54/50 | +0.044 | STANDARD |
| Jack Eichel: 2+ points | 0.241 | 0.320 | 33/69 | +0.054 | STANDARD |
| Sidney Crosby: 1+ assists | 0.412 | 0.475 | 49/54 | +0.030 | STANDARD |
| Mark Stone: 1+ assists | 0.384 | 0.445 | 46/57 | +0.029 | STANDARD |

**DAL @ WSH** · priced 162/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 26.25, exp saves 22.85 (sd 6.2), pull risk 0.056
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.46, exp saves 21.83 (sd 6.24), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.450 | 0.560 | 57/45 | +0.082 | STANDARD |
| Aliaksei Protas: 1+ points | 0.453 | 0.355 | 37/66 | +0.067 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.238 | 0.155 | 16/85 | +0.069 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.393 | 0.475 | 49/54 | +0.049 | STANDARD |
| Mikko Rantanen: 1+ points | 0.559 | 0.640 | 65/37 | +0.055 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.345 | 0.425 | 44/59 | +0.048 | STANDARD |

**COL @ CBJ** · priced 160/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 29.48, exp saves 25.52 (sd 6.84), pull risk 0.064
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.34 (sd 6.32), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Scott Wedgewood: 26+ saves | 0.356 | 0.450 | 48/58 | +0.047 |  |
| Zach Werenski: 1+ assists | 0.484 | 0.550 | 57/47 | +0.029 | STANDARD |
| Cale Makar: 2+ points | 0.184 | 0.245 | 26/77 | +0.034 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.301 | 0.360 | 37/65 | +0.033 | STANDARD |
| Matthew Knies: 1+ assists | 0.298 | 0.355 | 37/66 | +0.027 | STANDARD |
| Cale Makar: 1+ points | 0.548 | 0.600 | 61/41 | +0.025 | STANDARD |

**EDM @ NJD** · priced 161/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 26.46, exp saves 22.85 (sd 6.49), pull risk 0.069
- EDM net: Tristan Jarry (PROJECTED) exp shots 29.41, exp saves 25.35 (sd 6.93), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.400 | 0.530 | 54/48 | +0.103 | STANDARD |
| Connor McDavid: 1+ assists | 0.529 | 0.655 | 67/36 | +0.095 | STANDARD |
| Connor McDavid: 2+ points | 0.371 | 0.495 | 50/51 | +0.101 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.521 | 0.415 | 43/60 | +0.074 | STANDARD |
| Connor McDavid: 2+ assists | 0.175 | 0.270 | 29/75 | +0.062 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.299 | 0.215 | 24/81 | +0.046 | STANDARD |

**CAR @ NSH** · priced 159/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (CONFIRMED) exp shots 31.84, exp saves 27.15 (sd 7.47), pull risk 0.082
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.29 (sd 6.07), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Sebastian Aho: 1+ points | 0.543 | 0.650 | 66/36 | +0.080 | STANDARD |
| Sebastian Aho: 2+ points | 0.179 | 0.285 | 30/73 | +0.077 | STANDARD |
| Ryan O'Reilly: 2+ points | 0.225 | 0.130 | 22/96 | -0.008 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.387 | 0.470 | 48/54 | +0.055 | STANDARD |
| Sebastian Aho: 2+ assists | 0.071 | 0.150 | 17/87 | +0.051 | STANDARD |

**ANA @ VAN** · priced 146/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.41, exp saves 26.04 (sd 7.19), pull risk 0.079
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.99, exp saves 21.54 (sd 6.17), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ assists | 0.417 | 0.520 | 53/49 | +0.076 | STANDARD |
| Leo Carlsson: 2+ points | 0.229 | 0.305 | 31/70 | +0.056 | STANDARD |
| Leo Carlsson: 2+ assists | 0.101 | 0.175 | 19/84 | +0.049 | STANDARD |
| Marco Rossi: 1+ goals | 0.244 | 0.175 | 18/83 | +0.054 | STANDARD |
| Mikael Granlund: 1+ points | 0.538 | 0.605 | 61/40 | +0.045 | STANDARD |
| Alex Killorn: 1+ assists | 0.305 | 0.240 | 26/78 | +0.032 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
