# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T17:11:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 4126 · contracts joined: 2235 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 1910, 'NO_EDGE': 153, 'OK': 172}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 297, 'game_early_goal': 13, 'first_goal': 454, 'game_winner': 26, 'player_goals': 453, 'game_overtime': 13, 'player_points': 357, 'goalie_saves': 11, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-3h | 0.658 | 0.342 | 0.164 | 6.08 | 3.54 | 2.54 | 160 (25/135) | PROBABLE/PROBABLE |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-3h | 0.462 | 0.538 | 0.170 | 6.70 | 3.22 | 3.48 | 184 (25/159) | PROBABLE/PROBABLE |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-3h | 0.631 | 0.369 | 0.176 | 6.19 | 3.50 | 2.68 | 182 (25/157) | PROBABLE/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-3h | 0.473 | 0.527 | 0.182 | 5.84 | 2.83 | 3.00 | 189 (25/164) | CONFIRMED/PROJECTED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-3h | 0.545 | 0.455 | 0.168 | 6.53 | 3.40 | 3.13 | 169 (25/144) | CONFIRMED/CONFIRMED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-3h | 0.540 | 0.460 | 0.182 | 6.10 | 3.16 | 2.94 | 173 (25/148) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-3h | 0.616 | 0.384 | 0.169 | 6.65 | 3.72 | 2.94 | 180 (25/155) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-6h | 0.537 | 0.463 | 0.190 | 5.65 | 2.94 | 2.70 | 172 (25/147) | CONFIRMED/CONFIRMED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-6h | 0.500 | 0.500 | 0.179 | 6.01 | 3.01 | 3.00 | 165 (25/140) | PROBABLE/PROJECTED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-6h | 0.638 | 0.362 | 0.165 | 6.31 | 3.59 | 2.72 | 170 (25/145) | CONFIRMED/PROJECTED |
| STL @ COL | 2026-10-04T01:00:00Z | T-6h | 0.665 | 0.335 | 0.153 | 6.73 | 3.93 | 2.80 | 171 (25/146) | PROBABLE/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-6h | 0.493 | 0.507 | 0.174 | 6.33 | 3.15 | 3.19 | 159 (25/134) | PROJECTED/PROJECTED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-6h | 0.550 | 0.450 | 0.176 | 6.32 | 3.31 | 3.02 | 161 (25/136) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.630 | 0.607 | 64 | 38 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.295 | 0.405 | 0.382 | 41 | 60 | no | +0.089 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.463 | 0.565 | 0.545 | 57 | 44 | no | +0.079 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.537 | 0.435 | 0.455 | 44 | 57 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.233 | 0.325 | 0.305 | 33 | 68 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.130 | 0.215 | 0.195 | 22 | 79 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.140 | 0.225 | 0.205 | 23 | 78 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.465 | 0.555 | 0.537 | 56 | 45 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.473 | 0.385 | 0.402 | 39 | 62 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.746 | 0.835 | 0.820 | 85 | 18 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.529 | 0.445 | 0.462 | 45 | 56 | yes | +0.061 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-8 | game_total | 0.331 | 0.255 | 0.269 | 26 | 75 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.277 | 0.205 | 0.218 | 21 | 80 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.318 | 0.245 | 0.259 | 25 | 76 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.359 | 0.435 | 0.419 | 44 | 57 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.680 | 0.605 | 0.621 | 61 | 40 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.639 | 0.565 | 0.580 | 57 | 44 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.697 | 0.770 | 0.756 | 78 | 24 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.525 | 0.450 | 0.465 | 46 | 56 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.341 | 0.275 | 0.288 | 28 | 73 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.329 | 0.265 | 0.277 | 27 | 74 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-9 | game_total | 0.245 | 0.180 | 0.192 | 19 | 83 | yes | +0.044 | OK |
| KXNHLGAME-26OCT03DALNSH-DAL | game_winner | 0.500 | 0.565 | 0.552 | 57 | 44 | no | +0.043 | OK |
| KXNHLGAME-26OCT03DALNSH-NSH | game_winner | 0.500 | 0.435 | 0.448 | 44 | 57 | yes | +0.043 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.540 | 0.475 | 0.488 | 48 | 53 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.305 | 0.245 | 0.256 | 25 | 76 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-10 | game_total | 0.126 | 0.075 | 0.083 | 8 | 93 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL3 | game_spread | 0.161 | 0.215 | 0.203 | 22 | 79 | no | +0.038 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.455 | 0.515 | 0.503 | 52 | 49 | no | +0.037 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.545 | 0.485 | 0.497 | 49 | 52 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL4 | team_total | 0.366 | 0.430 | 0.417 | 44 | 58 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-7 | game_total | 0.426 | 0.485 | 0.473 | 49 | 52 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.247 | 0.190 | 0.201 | 20 | 82 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.643 | 0.585 | 0.597 | 59 | 42 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.533 | 0.475 | 0.487 | 48 | 53 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.162 | 0.110 | 0.119 | 12 | 90 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.797 | 0.850 | 0.840 | 86 | 16 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.328 | 0.275 | 0.285 | 28 | 73 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.185 | 0.240 | 0.228 | 25 | 77 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.757 | 0.700 | 0.712 | 71 | 31 | yes | +0.033 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.460 | 0.515 | 0.504 | 52 | 49 | no | +0.032 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.665 | 0.715 | 0.705 | 72 | 29 | no | +0.031 | OK |
| KXNHLGAME-26OCT03STLCOL-STL | game_winner | 0.335 | 0.285 | 0.295 | 29 | 72 | yes | +0.031 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.538 | 0.485 | 0.496 | 49 | 52 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.095 | 0.085 | 10 | 91 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-6 | game_total | 0.544 | 0.600 | 0.589 | 61 | 41 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT03DALNSH-DAL2 | game_spread | 0.276 | 0.325 | 0.315 | 33 | 68 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.456 | 0.405 | 0.415 | 41 | 60 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.167 | 0.125 | 0.133 | 13 | 88 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF3 | team_total | 0.698 | 0.745 | 0.736 | 75 | 26 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.152 | 0.195 | 0.186 | 20 | 81 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL3 | team_total | 0.587 | 0.640 | 0.630 | 65 | 37 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.206 | 0.165 | 0.173 | 17 | 84 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.125 | 0.165 | 0.156 | 17 | 84 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.458 | 0.505 | 0.495 | 51 | 50 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF4 | team_total | 0.488 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL3 | game_spread | 0.320 | 0.365 | 0.356 | 37 | 64 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT6 | team_total | 0.141 | 0.090 | 0.099 | 11 | 93 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-5 | game_total | 0.825 | 0.785 | 0.794 | 79 | 22 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT2 | team_total | 0.853 | 0.815 | 0.823 | 82 | 19 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.500 | 0.545 | 0.536 | 55 | 46 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL2 | team_total | 0.808 | 0.845 | 0.838 | 85 | 16 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03DALNSH-DAL5 | team_total | 0.186 | 0.235 | 0.225 | 25 | 78 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-5 | game_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.021 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.462 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-UTA3 | game_spread | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.727 | 0.765 | 0.758 | 77 | 24 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03CHIBUF-BUF5 | team_total | 0.284 | 0.335 | 0.325 | 35 | 68 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.667 | 0.625 | 0.634 | 63 | 38 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT3 | game_spread | 0.211 | 0.175 | 0.182 | 18 | 83 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT03CARPHI-CAR3 | game_spread | 0.178 | 0.215 | 0.207 | 22 | 79 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.262 | 0.225 | 0.232 | 23 | 78 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT03CHIBUF-BUF3 | game_spread | 0.286 | 0.325 | 0.317 | 33 | 68 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT03UTACBJ-UTA3 | team_total | 0.565 | 0.605 | 0.597 | 61 | 40 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT03UTACBJ-CBJ2 | game_spread | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR2 | game_spread | 0.259 | 0.295 | 0.288 | 30 | 71 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT03DALNSH-5 | game_total | 0.752 | 0.785 | 0.779 | 79 | 22 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-4 | game_total | 0.894 | 0.865 | 0.871 | 87 | 14 | yes | +0.016 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 0.658 | 0.638 | 0.164 | 0.206 | 6.08 | 6.34 | 1.000/0.995 | KXNHLTEAMTOTAL-26OCT03CHIBUF-CHI3 +0.053 |
| OTT @ TOR | 0.462 | 0.451 | 0.170 | 0.217 | 6.70 | 6.11 | 0.983/0.982 | KXNHLTOTAL-26OCT03OTTTOR-6 -0.099 |
| WSH @ TBL | 0.631 | 0.606 | 0.176 | 0.209 | 6.19 | 6.25 | 0.951/1.015 | KXNHLTEAMTOTAL-26OCT03WSHTB-WSH3 +0.032 |
| CAR @ PHI | 0.473 | 0.538 | 0.182 | 0.226 | 5.84 | 5.93 | 0.990/0.997 | KXNHLGAME-26OCT03CARPHI-PHI +0.065 |
| MTL @ PIT | 0.545 | 0.559 | 0.168 | 0.213 | 6.53 | 6.60 | 1.042/0.942 | KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 +0.022 |
| UTA @ CBJ | 0.540 | 0.544 | 0.182 | 0.219 | 6.10 | 6.32 | 0.964/0.992 | KXNHLTOTAL-26OCT03UTACBJ-7 +0.040 |
| SEA @ EDM | 0.616 | 0.620 | 0.169 | 0.202 | 6.65 | 6.55 | 1.009/1.005 | KXNHLTOTAL-26OCT03SEAEDM-8 -0.020 |
| NJD @ NYI | 0.537 | 0.535 | 0.190 | 0.223 | 5.65 | 5.87 | 0.947/0.995 | KXNHLTOTAL-26OCT03NJNYI-5 +0.040 |
| DAL @ NSH | 0.500 | 0.529 | 0.179 | 0.225 | 6.01 | 6.10 | 1.002/0.976 | KXNHLGAME-26OCT03DALNSH-DAL -0.028 |
| BOS @ MIN | 0.638 | 0.624 | 0.165 | 0.208 | 6.31 | 6.40 | 0.991/0.986 | KXNHLTEAMTOTAL-26OCT03BOSMIN-BOS4 +0.021 |
| STL @ COL | 0.665 | 0.634 | 0.153 | 0.200 | 6.73 | 6.42 | 0.977/1.024 | KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 -0.062 |
| CGY @ VAN | 0.493 | 0.561 | 0.174 | 0.217 | 6.33 | 6.34 | 1.025/0.986 | KXNHLGAME-26OCT03CGYVAN-VAN +0.068 |
| LAK @ SJS | 0.550 | 0.521 | 0.176 | 0.222 | 6.32 | 6.12 | 1.034/0.992 | KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Ryan Greene: 1+ goals YES @ 12c · p 0.1727 (adj 0.1583) · $2.26 · thesis CHI:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 59c · p 0.6492 (adj 0.6331) · $4.65 · thesis BUF:SUPPRESSED
- Patrick Kane: 1+ assists NO @ 62c · p 0.7488 (adj 0.6553) · $4.46 · thesis CHI:SUPPRESSED
- Tage Thompson: 1+ assists NO @ 57c · p 0.6458 (adj 0.6054) · $3.08 · thesis BUF:SUPPRESSED
- Stephen Halliday: 1+ goals YES @ 9c · p 0.1341 (adj 0.1218) · $1.88 · thesis OTT:OFFENSE_4PLUS
- Easton Cowan: 1+ assists YES @ 26c · p 0.3289 (adj 0.2894) · $1.52 · thesis TOR:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 65c · p 0.6911 (adj 0.6796) · $3.12 · thesis TOR:SUPPRESSED
- Tim Stutzle: 1+ assists NO @ 53c · p 0.6082 (adj 0.5616) · $2.57 · thesis OTT:SUPPRESSED
- John Carlson: 1+ assists NO @ 48c · p 0.7462 (adj 0.5667) · $5.78 · thesis TBL:SUPPRESSED
- John Carlson: 1+ points NO @ 40c · p 0.6572 (adj 0.4568) · $1.34 · thesis TBL:SUPPRESSED
- Anthony Beauvillier: 1+ goals YES @ 10c · p 0.1349 (adj 0.1249) · $1.41 · thesis WSH:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2112 (adj 0.1996) · $1.59 · thesis WSH:OFFENSE_4PLUS
- Noel Acciari: 1+ goals YES @ 9c · p 0.1354 (adj 0.1215) · $1.75 · thesis PHI:OFFENSE_4PLUS
- Mark Jankowski: 1+ goals NO @ 84c · p 0.8839 (adj 0.8717) · $5.78 · thesis CAR:SUPPRESSED
- Carolina wins by over 2.5 goals NO @ 79c · p 0.856 (adj 0.8205) · $5.78 · thesis PHI:WINS
- Connor Dewar: 1+ goals YES @ 12c · p 0.2013 (adj 0.1797) · $3.69 · thesis PIT:WINS_BY_2PLUS
- Filip Hallander: 1+ goals YES @ 13c · p 0.2022 (adj 0.1816) · $3.17 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 29c · p 0.3739 (adj 0.3492) · $4.21 · thesis PIT:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8619 (adj 0.7339) · $5.78 · thesis UTA:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2706 (adj 0.253) · $2.74 · thesis CBJ:OFFENSE_4PLUS
- Danton Heinen: 1+ goals YES @ 10c · p 0.1317 (adj 0.1213) · $1.11 · thesis CBJ:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2202 (adj 0.2089) · $1.6 · thesis UTA:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 17c · p 0.2346 (adj 0.2147) · $3.13 · thesis EDM:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 10c · p 0.141 (adj 0.1295) · $1.66 · thesis SEA:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 68c · p 0.8259 (adj 0.7278) · $5.78 · thesis EDM:SUPPRESSED
- Connor McDavid: 1+ assists NO @ 33c · p 0.4807 (adj 0.3762) · $2.55 · thesis EDM:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 66c · p 0.8394 (adj 0.713) · $4.93 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 64c · p 0.695 (adj 0.6787) · $3.74 · thesis NJD:SUPPRESSED
- Kyle Palmieri: 1+ assists NO @ 70c · p 0.8241 (adj 0.7304) · $4.84 · thesis NYI:SUPPRESSED
- Dallas wins NO @ 44c · p 0.5305 (adj 0.4875) · $3.18 · thesis NSH:WINS
- Dallas wins by over 2.5 goals NO @ 79c · p 0.8463 (adj 0.8156) · $1.26 · thesis NSH:WINS
- Mikko Rantanen: 1+ goals NO @ 71c · p 0.7537 (adj 0.739) · $2.93 · thesis DAL:SUPPRESSED
- Mikko Rantanen: 2+ assists NO @ 86c · p 0.9178 (adj 0.8789) · $5.73 · thesis DAL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 52c · p 0.6063 (adj 0.5835) · $5.78 · thesis COL:SUPPRESSED
- Colorado wins NO @ 29c · p 0.3688 (adj 0.3311) · $1.47 · thesis STL:WINS
- Zayne Parekh: 1+ goals NO @ 85c · p 0.903 (adj 0.886) · $4.48 · thesis CGY:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 17c · p 0.2199 (adj 0.1974) · $1.0 · thesis VAN:OFFENSE_4PLUS
- Zeev Buium: 1+ goals NO @ 89c · p 0.9226 (adj 0.9094) · $4.33 · thesis VAN:SUPPRESSED
- Paul Cotter: 1+ goals NO @ 84c · p 0.8736 (adj 0.8639) · $4.33 · thesis VAN:SUPPRESSED
- Kiefer Sherwood: 1+ goals YES @ 13c · p 0.1991 (adj 0.1793) · $3.07 · thesis SJS:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 58c · p 0.8257 (adj 0.653) · $5.69 · thesis LAK:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 67c · p 0.8121 (adj 0.7132) · $5.69 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 101/109 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 24.71, exp saves 21.76 (sd 6.09), pull risk 0.05
- CHI net: Spencer Knight (PROBABLE) exp shots 30.42, exp saves 25.66 (sd 7.16), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 21+ saves | 0.578 | 0.275 | 53/98 | +0.031 |  |
| Patrick Kane: 1+ assists | 0.251 | 0.395 | 41/62 | +0.112 | STANDARD |
| Tage Thompson: 2+ points | 0.218 | 0.325 | 33/68 | +0.087 | STANDARD |
| Patrick Kane: 1+ points | 0.440 | 0.545 | 55/46 | +0.083 | STANDARD |
| Tage Thompson: 1+ points | 0.582 | 0.675 | 68/33 | +0.073 | STANDARD |
| Tage Thompson: 1+ assists | 0.354 | 0.435 | 44/57 | +0.059 | STANDARD |

**OTT @ TOR** · priced 131/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.35, exp saves 27.01 (sd 7.12), pull risk 0.066
- OTT net: Linus Ullmark (PROBABLE) exp shots 24.74, exp saves 21.69 (sd 5.97), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Bobrovsky: 26+ saves | 0.589 | 0.270 | 53/99 | +0.041 |  |
| Darren Raddysh: 1+ points | 0.383 | 0.520 | 53/49 | +0.109 | STANDARD |
| Darren Raddysh: 1+ assists | 0.290 | 0.415 | 44/61 | +0.084 | STANDARD |
| Kirill Marchenko: 1+ points | 0.461 | 0.575 | 59/44 | +0.082 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.272 | 0.385 | 39/62 | +0.091 | STANDARD |
| Auston Matthews: 1+ assists | 0.304 | 0.410 | 43/61 | +0.069 | STANDARD |

**WSH @ TBL** · priced 129/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 25.03, exp saves 21.89 (sd 6.08), pull risk 0.05
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.45 (sd 6.85), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.254 | 0.530 | 54/48 | +0.249 | STANDARD |
| John Carlson: 1+ points | 0.343 | 0.610 | 62/40 | +0.240 | STANDARD |
| John Carlson: 2+ points | 0.069 | 0.235 | 26/79 | +0.129 | STANDARD |
| John Carlson: 2+ assists | 0.035 | 0.175 | 18/83 | +0.126 | STANDARD |
| Andrei Vasilevskiy: 24+ saves | 0.389 | 0.265 | 51/98 | -0.138 |  |
| Anthony Cirelli: 1+ points | 0.494 | 0.415 | 44/61 | +0.037 | STANDARD |

**CAR @ PHI** · priced 136/138 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 29.07, exp saves 25.27 (sd 6.78), pull risk 0.052
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.27, exp saves 20.0 (sd 5.71), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sean Couturier: 1+ goals | 0.176 | 0.075 | 11/96 | +0.059 | STANDARD |
| Sebastian Aho: 1+ points | 0.465 | 0.565 | 58/45 | +0.067 | STANDARD |
| Sebastian Aho: 1+ assists | 0.297 | 0.395 | 41/62 | +0.066 | STANDARD |
| Sebastian Aho: 2+ points | 0.126 | 0.200 | 21/81 | +0.053 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.363 | 0.430 | 45/59 | +0.030 | STANDARD |
| Porter Martone: 1+ points | 0.391 | 0.455 | 47/56 | +0.032 | STANDARD |

**MTL @ PIT** · priced 116/118 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- PIT net: Arturs Silovs (CONFIRMED) exp shots 24.51, exp saves 21.32 (sd 6.07), pull risk 0.061
- MTL net: Jakub Dobes (CONFIRMED) exp shots 29.53, exp saves 25.27 (sd 7.0), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 26+ saves | 0.235 | 0.435 | 53/66 | +0.089 |  |
| Jakub Dobes: 24+ saves | 0.606 | 0.425 | 52/67 | +0.068 |  |
| Rickard Rakell: 1+ points | 0.640 | 0.530 | 55/49 | +0.073 | STANDARD |
| Rickard Rakell: 1+ goals | 0.374 | 0.275 | 29/74 | +0.069 | STANDARD |
| Andrei Kuzmenko: 1+ goals | 0.190 | 0.100 | 19/99 | -0.011 | STANDARD |
| Connor Dewar: 1+ goals | 0.201 | 0.115 | 12/89 | +0.074 | STANDARD |

**UTA @ CBJ** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.33 (sd 6.36), pull risk 0.055
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.96 (sd 6.66), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.138 | 0.335 | 35/68 | +0.167 | STANDARD |
| Vincent Trocheck: 1+ points | 0.315 | 0.460 | 47/55 | +0.118 | STANDARD |
| Matthew Knies: 1+ assists | 0.245 | 0.360 | 38/66 | +0.079 | STANDARD |
| Charlie Coyle: 1+ points | 0.557 | 0.465 | 48/55 | +0.059 | STANDARD |
| Matthew Knies: 1+ points | 0.460 | 0.550 | 57/47 | +0.053 | STANDARD |
| Matthew Knies: 2+ points | 0.134 | 0.205 | 21/80 | +0.054 | STANDARD |

**SEA @ EDM** · priced 129/129 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 25.57, exp saves 22.4 (sd 6.15), pull risk 0.054
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.05 (sd 7.23), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.519 | 0.680 | 69/33 | +0.135 | STANDARD |
| Leon Draisaitl: 2+ points | 0.320 | 0.480 | 49/53 | +0.132 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.441 | 0.595 | 60/41 | +0.132 | STANDARD |
| Connor McDavid: 2+ assists | 0.174 | 0.325 | 33/68 | +0.131 | STANDARD |
| Connor McDavid: 2+ points | 0.401 | 0.535 | 55/48 | +0.101 | STANDARD |
| Mattias Ekholm: 1+ points | 0.447 | 0.315 | 33/70 | +0.102 | STANDARD |

**NJD @ NYI** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.54 (sd 6.48), pull risk 0.046
- NJD net: Nico Daws (CONFIRMED) exp shots 27.75, exp saves 24.0 (sd 6.52), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.161 | 0.355 | 37/66 | +0.164 | STANDARD |
| Luke Evangelista: 1+ points | 0.300 | 0.480 | 50/54 | +0.143 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.176 | 0.320 | 34/70 | +0.109 | STANDARD |
| Anthony Mantha: 1+ points | 0.329 | 0.460 | 48/56 | +0.094 | STANDARD |
| Anthony Mantha: 1+ assists | 0.154 | 0.280 | 30/74 | +0.093 | STANDARD |
| Jack Hughes: 1+ assists | 0.377 | 0.500 | 51/51 | +0.096 | STANDARD |

**DAL @ NSH** · priced 114/114 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.51, exp saves 23.91 (sd 6.48), pull risk 0.054
- DAL net: Casey DeSmith (PROJECTED) exp shots 26.36, exp saves 22.76 (sd 6.38), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ goals | 0.211 | 0.090 | 17/99 | +0.031 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.374 | 0.490 | 51/53 | +0.079 | STANDARD |
| Mikko Rantanen: 1+ points | 0.527 | 0.640 | 65/37 | +0.087 | STANDARD |
| Roope Hintz: 1+ assists | 0.240 | 0.350 | 36/66 | +0.084 | STANDARD |
| Miro Heiskanen: 1+ points | 0.470 | 0.565 | 58/45 | +0.062 | STANDARD |
| Ryan O'Reilly: 1+ goals | 0.303 | 0.210 | 29/87 | -0.001 | STANDARD |

**BOS @ MIN** · priced 117/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.46, exp saves 24.14 (sd 6.54), pull risk 0.051
- BOS net: Michael DiPietro (PROJECTED) exp shots 30.36, exp saves 25.64 (sd 7.16), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ goals | 0.279 | 0.155 | 24/93 | +0.026 | STANDARD |
| Elias Lindholm: 1+ goals | 0.223 | 0.110 | 20/98 | +0.012 | STANDARD |
| JJ Peterka: 1+ points | 0.349 | 0.460 | 47/55 | +0.084 | STANDARD |
| JJ Peterka: 1+ assists | 0.170 | 0.280 | 30/74 | +0.077 | STANDARD |
| Max Shabanov: 1+ assists | 0.206 | 0.315 | 34/71 | +0.069 | STANDARD |
| Max Shabanov: 1+ points | 0.359 | 0.460 | 49/57 | +0.054 | STANDARD |

**STL @ COL** · priced 120/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 24.45, exp saves 21.42 (sd 5.99), pull risk 0.051
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.45 (sd 7.4), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.343 | 0.525 | 54/49 | +0.150 | STANDARD |
| Cale Makar: 1+ assists | 0.444 | 0.615 | 63/40 | +0.139 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.118 | 0.275 | 29/74 | +0.128 | STANDARD |
| Cale Makar: 2+ points | 0.186 | 0.335 | 34/67 | +0.129 | STANDARD |
| Cale Makar: 1+ points | 0.548 | 0.695 | 70/31 | +0.127 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.502 | 0.645 | 65/36 | +0.122 | STANDARD |

**CGY @ VAN** · priced 106/108 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 28.38, exp saves 24.72 (sd 6.61), pull risk 0.056
- CGY net: Devin Cooley (PROJECTED) exp shots 28.2, exp saves 24.24 (sd 6.68), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Karlsson: 1+ goals | 0.254 | 0.140 | 22/94 | +0.021 | STANDARD |
| Drew O'Connor: 1+ goals | 0.220 | 0.130 | 17/91 | +0.040 | STANDARD |
| Filip Hronek: 2+ points | 0.174 | 0.095 | 18/99 | -0.016 | STANDARD |
| Liam Ohgren: 1+ goals | 0.192 | 0.115 | 20/97 | -0.019 | STANDARD |
| Connor Zary: 1+ goals | 0.207 | 0.130 | 21/95 | -0.014 | STANDARD |
| Brendan Gallagher: 1+ goals | 0.162 | 0.085 | 14/97 | +0.013 | STANDARD |

**LAK @ SJS** · priced 107/110 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.98, exp saves 24.34 (sd 6.56), pull risk 0.055
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.75, exp saves 23.27 (sd 6.38), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.174 | 0.440 | 46/58 | +0.229 | STANDARD |
| Mason Marchment: 1+ assists | 0.188 | 0.340 | 35/67 | +0.127 | STANDARD |
| Artemi Panarin: 1+ assists | 0.359 | 0.510 | 52/50 | +0.123 | STANDARD |
| Luca Cagnoni: 1+ points | 0.310 | 0.425 | 44/59 | +0.083 | PRIOR_HEAVY |
| Mats Zuccarello: 2+ assists | 0.017 | 0.115 | 14/91 | +0.067 | STANDARD |
| Mason Marchment: 1+ points | 0.394 | 0.490 | 50/52 | +0.068 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
