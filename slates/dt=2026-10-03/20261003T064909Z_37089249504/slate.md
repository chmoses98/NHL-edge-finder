# NHL slate 2026-10-03 — RESEARCH_ONLY

generated 2026-10-03T06:49:09Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 13 · simulated (not started): 13 · markets on board: 2554 · contracts joined: 663 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 338, 'NO_EDGE': 156, 'OK': 169}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'game_early_goal': 13, 'game_winner': 26, 'game_overtime': 13, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 2026-10-03T23:00:00Z | T-12h | 0.660 | 0.340 | 0.166 | 6.12 | 3.57 | 2.56 | 51 (25/26) | PROJECTED/PROJECTED |
| OTT @ TOR | 2026-10-03T23:00:00Z | T-12h | 0.470 | 0.530 | 0.170 | 6.58 | 3.18 | 3.39 | 51 (25/26) | PROJECTED/PROJECTED |
| WSH @ TBL | 2026-10-03T23:00:00Z | T-12h | 0.597 | 0.403 | 0.172 | 6.17 | 3.40 | 2.78 | 51 (25/26) | PROJECTED/CONFIRMED |
| CAR @ PHI | 2026-10-03T23:00:00Z | T-12h | 0.441 | 0.559 | 0.176 | 5.84 | 2.73 | 3.11 | 51 (25/26) | PROJECTED/PROJECTED |
| MTL @ PIT | 2026-10-03T23:00:00Z | T-12h | 0.565 | 0.435 | 0.169 | 6.56 | 3.49 | 3.07 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ CBJ | 2026-10-03T23:00:00Z | T-12h | 0.537 | 0.463 | 0.181 | 6.10 | 3.15 | 2.94 | 51 (25/26) | PROJECTED/PROJECTED |
| SEA @ EDM | 2026-10-03T23:00:00Z | T-12h | 0.611 | 0.389 | 0.160 | 6.66 | 3.71 | 2.95 | 51 (25/26) | PROJECTED/PROJECTED |
| NJD @ NYI | 2026-10-03T23:30:00Z | T-12h | 0.530 | 0.470 | 0.188 | 5.59 | 2.90 | 2.70 | 51 (25/26) | CONFIRMED/PROJECTED |
| DAL @ NSH | 2026-10-04T00:00:00Z | T-12h | 0.473 | 0.526 | 0.176 | 6.19 | 3.02 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ MIN | 2026-10-04T00:00:00Z | T-12h | 0.555 | 0.445 | 0.176 | 6.04 | 3.20 | 2.84 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ COL | 2026-10-04T01:00:00Z | T-12h | 0.643 | 0.357 | 0.161 | 6.75 | 3.85 | 2.90 | 51 (25/26) | PROJECTED/PROBABLE |
| CGY @ VAN | 2026-10-04T02:00:00Z | T-12h | 0.554 | 0.446 | 0.165 | 6.55 | 3.44 | 3.11 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ SJS | 2026-10-04T02:00:00Z | T-12h | 0.545 | 0.455 | 0.172 | 6.32 | 3.30 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ4 | team_total | 0.293 | 0.410 | 0.385 | 42 | 60 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL3 | team_total | 0.551 | 0.440 | 0.462 | 45 | 57 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ3 | team_total | 0.514 | 0.620 | 0.599 | 63 | 39 | no | +0.080 | OK |
| KXNHLTOTAL-26OCT03NJNYI-6 | game_total | 0.453 | 0.555 | 0.535 | 56 | 45 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL4 | team_total | 0.341 | 0.240 | 0.258 | 25 | 77 | yes | +0.078 | OK |
| KXNHLGAME-26OCT03MTLPIT-MTL | game_winner | 0.435 | 0.535 | 0.515 | 54 | 47 | no | +0.077 | OK |
| KXNHLGAME-26OCT03MTLPIT-PIT | game_winner | 0.565 | 0.465 | 0.485 | 47 | 54 | yes | +0.077 | OK |
| KXNHLGAME-26OCT03BOSMIN-BOS | game_winner | 0.445 | 0.355 | 0.372 | 36 | 65 | yes | +0.069 | OK |
| KXNHLGAME-26OCT03BOSMIN-MIN | game_winner | 0.555 | 0.645 | 0.628 | 65 | 36 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT2 | game_spread | 0.352 | 0.265 | 0.281 | 27 | 74 | yes | +0.068 | OK |
| KXNHLTOTAL-26OCT03NJNYI-7 | game_total | 0.347 | 0.435 | 0.417 | 44 | 57 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT03NJNYI-5 | game_total | 0.693 | 0.775 | 0.760 | 78 | 23 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ2 | team_total | 0.747 | 0.825 | 0.811 | 83 | 18 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN2 | game_spread | 0.331 | 0.415 | 0.398 | 42 | 59 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ2 | game_spread | 0.243 | 0.325 | 0.308 | 33 | 68 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL5 | team_total | 0.178 | 0.100 | 0.113 | 11 | 91 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ5 | team_total | 0.137 | 0.225 | 0.205 | 24 | 79 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL2 | game_spread | 0.237 | 0.315 | 0.298 | 32 | 69 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL2 | team_total | 0.772 | 0.690 | 0.708 | 70 | 32 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT03STLCOL-7 | game_total | 0.534 | 0.455 | 0.471 | 46 | 55 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT3 | team_total | 0.679 | 0.600 | 0.616 | 61 | 41 | yes | +0.053 | OK |
| KXNHLGAME-26OCT03STLCOL-COL | game_winner | 0.643 | 0.720 | 0.705 | 73 | 29 | no | +0.053 | OK |
| KXNHLGAME-26OCT03STLCOL-STL | game_winner | 0.357 | 0.285 | 0.299 | 29 | 72 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL2 | game_spread | 0.430 | 0.505 | 0.490 | 51 | 50 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NJ3 | game_spread | 0.136 | 0.205 | 0.189 | 21 | 80 | no | +0.052 | OK |
| KXNHLGAME-26OCT03NJNYI-NYI | game_winner | 0.530 | 0.455 | 0.470 | 46 | 55 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN4 | team_total | 0.411 | 0.495 | 0.478 | 51 | 52 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-MIN3 | game_spread | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT03STLCOL-6 | game_total | 0.647 | 0.575 | 0.590 | 58 | 43 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT03STLCOL-COL3 | game_spread | 0.295 | 0.370 | 0.354 | 38 | 64 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-MTL3 | game_spread | 0.140 | 0.205 | 0.191 | 21 | 80 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN3 | team_total | 0.628 | 0.695 | 0.682 | 70 | 31 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT03STLCOL-8 | game_total | 0.341 | 0.270 | 0.283 | 28 | 74 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT4 | team_total | 0.473 | 0.390 | 0.406 | 41 | 63 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL2 | game_spread | 0.184 | 0.125 | 0.135 | 13 | 88 | yes | +0.046 | OK |
| KXNHLGAME-26OCT03NJNYI-NJ | game_winner | 0.470 | 0.540 | 0.526 | 55 | 47 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT03MTLPIT-PIT3 | game_spread | 0.222 | 0.165 | 0.175 | 17 | 84 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN5 | team_total | 0.225 | 0.290 | 0.276 | 30 | 72 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT03NJNYI-8 | game_total | 0.178 | 0.240 | 0.227 | 25 | 77 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT03NJNYI-4 | game_total | 0.792 | 0.850 | 0.840 | 86 | 16 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT03STLCOL-9 | game_total | 0.249 | 0.185 | 0.197 | 20 | 83 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT5 | team_total | 0.279 | 0.215 | 0.227 | 23 | 80 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT03STLCOL-STL6 | team_total | 0.078 | 0.035 | 0.041 | 4 | 97 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL3 | team_total | 0.589 | 0.650 | 0.638 | 66 | 36 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-PIT6 | team_total | 0.140 | 0.085 | 0.094 | 10 | 93 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT03CARPHI-5 | game_total | 0.724 | 0.775 | 0.765 | 78 | 23 | no | +0.033 | OK |
| KXNHLGAME-26OCT03OTTTOR-TOR | game_winner | 0.470 | 0.525 | 0.514 | 53 | 48 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT03NJNYI-9 | game_total | 0.118 | 0.165 | 0.155 | 17 | 84 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN5 | team_total | 0.273 | 0.220 | 0.230 | 23 | 79 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL4 | team_total | 0.382 | 0.440 | 0.428 | 45 | 57 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT03CGYVAN-8 | game_total | 0.314 | 0.265 | 0.274 | 27 | 74 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT03STLCOL-STL3 | game_spread | 0.104 | 0.065 | 0.072 | 7 | 94 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03NJNYI-NJ6 | team_total | 0.055 | 0.095 | 0.085 | 10 | 91 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT03BOSMIN-MIN2 | team_total | 0.822 | 0.865 | 0.857 | 87 | 14 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT03NJNYI-NYI2 | game_spread | 0.303 | 0.255 | 0.264 | 26 | 75 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT03SEAEDM-SEA5 | team_total | 0.187 | 0.145 | 0.153 | 15 | 86 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT3 | team_total | 0.662 | 0.605 | 0.617 | 62 | 41 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT03CGYVAN-VAN4 | team_total | 0.463 | 0.405 | 0.416 | 42 | 61 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT03SEAEDM-SEA2 | game_spread | 0.205 | 0.165 | 0.172 | 17 | 84 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-PHI3 | team_total | 0.518 | 0.565 | 0.556 | 57 | 44 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT03STLCOL-10 | game_total | 0.131 | 0.085 | 0.093 | 10 | 93 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT03BOSMIN-BOS2 | game_spread | 0.235 | 0.190 | 0.198 | 20 | 82 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT03CARPHI-6 | game_total | 0.499 | 0.545 | 0.536 | 55 | 46 | no | +0.023 | OK |
| KXNHLGAME-26OCT03SEAEDM-EDM | game_winner | 0.611 | 0.655 | 0.646 | 66 | 35 | no | +0.023 | OK |
| KXNHLGAME-26OCT03SEAEDM-SEA | game_winner | 0.389 | 0.345 | 0.354 | 35 | 66 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-OTT2 | game_spread | 0.317 | 0.275 | 0.283 | 28 | 73 | yes | +0.023 | OK |
| KXNHLGAME-26OCT03OTTTOR-OTT | game_winner | 0.530 | 0.485 | 0.494 | 49 | 52 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT03OTTTOR-TOR3 | game_spread | 0.157 | 0.200 | 0.191 | 21 | 81 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT03CGYVAN-VAN2 | game_spread | 0.337 | 0.295 | 0.303 | 30 | 71 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT4 | team_total | 0.449 | 0.390 | 0.402 | 41 | 63 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT03CHIBUF-7 | game_total | 0.431 | 0.475 | 0.466 | 48 | 53 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-PHI2 | team_total | 0.747 | 0.790 | 0.782 | 80 | 22 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT03CARPHI-PHI4 | team_total | 0.304 | 0.350 | 0.340 | 36 | 66 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT03STLCOL-5 | game_total | 0.832 | 0.795 | 0.803 | 80 | 21 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-6 | game_total | 0.617 | 0.575 | 0.584 | 58 | 43 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT03OTTTOR-OTT5 | team_total | 0.263 | 0.215 | 0.224 | 23 | 80 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT03OTTTOR-7 | game_total | 0.507 | 0.460 | 0.469 | 47 | 55 | yes | +0.020 | OK |
| KXNHLGAME-26OCT03UTACBJ-CBJ | game_winner | 0.537 | 0.495 | 0.503 | 50 | 51 | yes | +0.020 | OK |
| KXNHLGAME-26OCT03UTACBJ-UTA | game_winner | 0.463 | 0.505 | 0.497 | 51 | 50 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL2 | team_total | 0.801 | 0.840 | 0.833 | 85 | 17 | no | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CHI @ BUF | 0.660 | 0.639 | 0.166 | 0.204 | 6.12 | 6.35 | 0.997/1.003 | KXNHLTEAMTOTAL-26OCT03CHIBUF-CHI3 +0.046 |
| OTT @ TOR | 0.470 | 0.460 | 0.170 | 0.215 | 6.58 | 6.08 | 0.965/0.998 | KXNHLTOTAL-26OCT03OTTTOR-6 -0.081 |
| WSH @ TBL | 0.597 | 0.588 | 0.172 | 0.214 | 6.17 | 6.26 | 0.957/1.015 | KXNHLTEAMTOTAL-26OCT03WSHTB-WSH3 +0.024 |
| CAR @ PHI | 0.441 | 0.500 | 0.176 | 0.223 | 5.84 | 5.97 | 0.991/0.989 | KXNHLTEAMTOTAL-26OCT03CARPHI-PHI3 +0.065 |
| MTL @ PIT | 0.565 | 0.568 | 0.169 | 0.209 | 6.56 | 6.61 | 1.033/0.952 | KXNHLTEAMTOTAL-26OCT03MTLPIT-MTL3 +0.017 |
| UTA @ CBJ | 0.537 | 0.544 | 0.181 | 0.217 | 6.10 | 6.31 | 0.964/0.992 | KXNHLTOTAL-26OCT03UTACBJ-7 +0.040 |
| SEA @ EDM | 0.611 | 0.630 | 0.160 | 0.206 | 6.66 | 6.52 | 0.994/1.005 | KXNHLTOTAL-26OCT03SEAEDM-8 -0.032 |
| NJD @ NYI | 0.530 | 0.534 | 0.188 | 0.220 | 5.59 | 5.85 | 0.947/0.987 | KXNHLTOTAL-26OCT03NJNYI-6 +0.049 |
| DAL @ NSH | 0.473 | 0.491 | 0.176 | 0.225 | 6.19 | 6.20 | 1.000/0.986 | KXNHLSPREAD-26OCT03DALNSH-DAL2 -0.020 |
| BOS @ MIN | 0.555 | 0.583 | 0.176 | 0.213 | 6.04 | 6.38 | 1.003/0.968 | KXNHLTOTAL-26OCT03BOSMIN-7 +0.062 |
| STL @ COL | 0.643 | 0.603 | 0.161 | 0.206 | 6.75 | 6.43 | 0.976/1.024 | KXNHLTEAMTOTAL-26OCT03STLCOL-COL5 -0.062 |
| CGY @ VAN | 0.554 | 0.570 | 0.165 | 0.210 | 6.55 | 6.35 | 1.021/0.997 | KXNHLTOTAL-26OCT03CGYVAN-8 -0.037 |
| LAK @ SJS | 0.545 | 0.523 | 0.172 | 0.222 | 6.32 | 6.12 | 1.034/0.992 | KXNHLTEAMTOTAL-26OCT03LASJ-SJ4 -0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 5 recommended · full analysis in card.md / packet.json `thesis_card`

- Montreal wins NO @ 47c · p 0.5639 (adj 0.5144) · $8.01 · thesis PIT:WINS
- Pittsburgh wins by over 1.5 goals YES @ 27c · p 0.3482 (adj 0.3066) · $3.56 · thesis PIT:WINS_BY_2PLUS
- Montreal wins by over 2.5 goals NO @ 80c · p 0.8536 (adj 0.8243) · $7.36 · thesis PIT:WINS
- New Jersey wins by over 1.5 goals NO @ 68c · p 0.754 (adj 0.7145) · $6.61 · thesis NYI:WINS
- Colorado wins by over 1.5 goals NO @ 50c · p 0.624 (adj 0.5402) · $12.22 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CHI @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 24.71, exp saves 21.79 (sd 6.06), pull risk 0.047
- CHI net: Spencer Knight (PROJECTED) exp shots 30.42, exp saves 25.71 (sd 7.11), pull risk 0.083

**OTT @ TOR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.35, exp saves 27.06 (sd 7.17), pull risk 0.063
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.74, exp saves 21.64 (sd 6.02), pull risk 0.053

**WSH @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.03, exp saves 21.89 (sd 6.05), pull risk 0.049
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 28.7, exp saves 24.53 (sd 6.83), pull risk 0.072

**CAR @ PHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.18 (sd 6.79), pull risk 0.054
- CAR net: Brandon Bussi (PROJECTED) exp shots 23.27, exp saves 20.13 (sd 5.78), pull risk 0.057

**MTL @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 24.51, exp saves 21.3 (sd 5.98), pull risk 0.059
- MTL net: Jakub Dobes (PROJECTED) exp shots 29.53, exp saves 25.21 (sd 7.05), pull risk 0.084

**UTA @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.84, exp saves 23.27 (sd 6.35), pull risk 0.061
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.0, exp saves 23.93 (sd 6.7), pull risk 0.069

**SEA @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 25.57, exp saves 22.42 (sd 6.14), pull risk 0.052
- SEA net: Joey Daccord (PROJECTED) exp shots 30.84, exp saves 26.03 (sd 7.24), pull risk 0.089

**NJD @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 28.14, exp saves 24.51 (sd 6.49), pull risk 0.045
- NJD net: Jake Allen (PROJECTED) exp shots 27.75, exp saves 24.05 (sd 6.57), pull risk 0.052

**DAL @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.51, exp saves 23.79 (sd 6.49), pull risk 0.059
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.36, exp saves 22.84 (sd 6.39), pull risk 0.058

**BOS @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.46, exp saves 24.03 (sd 6.5), pull risk 0.054
- BOS net: Jeremy Swayman (PROJECTED) exp shots 30.36, exp saves 25.78 (sd 7.11), pull risk 0.081

**STL @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.45, exp saves 21.39 (sd 5.93), pull risk 0.052
- STL net: Jordan Binnington (PROBABLE) exp shots 31.38, exp saves 26.57 (sd 7.28), pull risk 0.08

**CGY @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 28.38, exp saves 24.7 (sd 6.66), pull risk 0.057
- CGY net: Dustin Wolf (PROJECTED) exp shots 28.2, exp saves 24.18 (sd 6.72), pull risk 0.071

**LAK @ SJS** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.98, exp saves 24.32 (sd 6.6), pull risk 0.057
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.75, exp saves 23.24 (sd 6.38), pull risk 0.06

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
