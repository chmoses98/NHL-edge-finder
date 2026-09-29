# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-29T20:31:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2900 · contracts joined: 1089 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 964, 'OK': 90, 'NO_EDGE': 35}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 155, 'game_early_goal': 5, 'first_goal': 165, 'game_winner': 10, 'player_goals': 297, 'game_overtime': 5, 'player_points': 207, 'goalie_saves': 10, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 2026-09-29T21:00:00Z | T-10m | 0.655 | 0.345 | 0.161 | 6.51 | 3.76 | 2.75 | 265 (25/240) | CONFIRMED/PROJECTED |
| MTL @ TOR | 2026-09-29T23:00:00Z | T-90m | 0.442 | 0.558 | 0.166 | 6.55 | 3.09 | 3.47 | 209 (25/184) | CONFIRMED/CONFIRMED |
| NYR @ BOS | 2026-09-30T00:00:00Z | T-3h | 0.545 | 0.455 | 0.181 | 5.78 | 3.02 | 2.77 | 221 (25/196) | CONFIRMED/PROBABLE |
| VAN @ EDM | 2026-09-30T02:00:00Z | T-3h | 0.652 | 0.348 | 0.159 | 6.69 | 3.85 | 2.84 | 199 (25/174) | CONFIRMED/PROBABLE |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-3h | 0.618 | 0.382 | 0.173 | 6.03 | 3.38 | 2.66 | 195 (25/170) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26SEP29FLACAR-CAR2 | game_spread | 0.435 | 0.325 | 0.346 | 33 | 68 | yes | +0.089 | OK |
| KXNHLGAME-26SEP29FLACAR-CAR | game_winner | 0.655 | 0.545 | 0.568 | 55 | 46 | yes | +0.087 | OK |
| KXNHLGAME-26SEP29FLACAR-FLA | game_winner | 0.345 | 0.455 | 0.432 | 46 | 55 | no | +0.087 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.382 | 0.475 | 0.456 | 48 | 53 | no | +0.071 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.244 | 0.335 | 0.316 | 34 | 67 | no | +0.070 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.382 | 0.295 | 0.312 | 30 | 71 | yes | +0.067 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.618 | 0.705 | 0.688 | 71 | 30 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR4 | team_total | 0.534 | 0.445 | 0.463 | 45 | 56 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.065 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA2 | game_spread | 0.173 | 0.255 | 0.237 | 26 | 75 | no | +0.064 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.300 | 0.385 | 0.367 | 39 | 62 | no | +0.063 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.440 | 0.525 | 0.508 | 53 | 48 | no | +0.063 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR3 | game_spread | 0.293 | 0.215 | 0.229 | 22 | 79 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR3 | team_total | 0.734 | 0.655 | 0.672 | 66 | 35 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA4 | team_total | 0.307 | 0.385 | 0.369 | 39 | 62 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR5 | team_total | 0.329 | 0.255 | 0.269 | 26 | 75 | yes | +0.056 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.652 | 0.725 | 0.711 | 73 | 28 | no | +0.054 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.348 | 0.275 | 0.289 | 28 | 73 | yes | +0.054 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA3 | game_spread | 0.093 | 0.155 | 0.140 | 16 | 85 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR3 | team_total | 0.528 | 0.600 | 0.586 | 61 | 41 | no | +0.045 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.191 | 0.135 | 0.145 | 14 | 87 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM4 | team_total | 0.551 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR4 | team_total | 0.312 | 0.380 | 0.366 | 39 | 63 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.539 | 0.475 | 0.488 | 48 | 53 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.666 | 0.730 | 0.718 | 74 | 28 | no | +0.040 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.175 | 0.125 | 0.134 | 13 | 88 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA5 | team_total | 0.154 | 0.205 | 0.194 | 21 | 80 | no | +0.035 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL2 | game_spread | 0.349 | 0.295 | 0.305 | 30 | 71 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA3 | team_total | 0.519 | 0.575 | 0.564 | 58 | 43 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.253 | 0.315 | 0.302 | 33 | 70 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.326 | 0.265 | 0.277 | 28 | 75 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR6 | team_total | 0.170 | 0.125 | 0.133 | 13 | 88 | yes | +0.032 | OK |
| KXNHLGAME-26SEP29MTLTOR-MTL | game_winner | 0.558 | 0.505 | 0.516 | 51 | 50 | yes | +0.031 | OK |
| KXNHLGAME-26SEP29MTLTOR-TOR | game_winner | 0.442 | 0.495 | 0.484 | 50 | 51 | no | +0.031 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-5 | game_total | 0.717 | 0.770 | 0.760 | 78 | 24 | no | +0.030 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-6 | game_total | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR5 | team_total | 0.150 | 0.205 | 0.193 | 22 | 81 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM2 | team_total | 0.897 | 0.935 | 0.929 | 94 | 7 | no | +0.028 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-4 | game_total | 0.813 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-BOS | game_winner | 0.545 | 0.495 | 0.505 | 50 | 51 | yes | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-NYR | game_winner | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.346 | 0.405 | 0.393 | 42 | 61 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA2 | team_total | 0.752 | 0.795 | 0.787 | 80 | 21 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR2 | team_total | 0.884 | 0.840 | 0.850 | 85 | 17 | yes | +0.026 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR3 | game_spread | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL5 | team_total | 0.278 | 0.230 | 0.239 | 24 | 78 | yes | +0.025 | OK |
| KXNHLTOTAL-26SEP29FLACAR-7 | game_total | 0.500 | 0.455 | 0.464 | 46 | 55 | yes | +0.023 | OK |
| KXNHLTOTAL-26SEP29FLACAR-8 | game_total | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK2 | team_total | 0.851 | 0.890 | 0.883 | 90 | 12 | no | +0.022 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.096 | 0.065 | 0.070 | 7 | 94 | yes | +0.021 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-7 | game_total | 0.382 | 0.425 | 0.416 | 43 | 58 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR2 | team_total | 0.757 | 0.805 | 0.796 | 82 | 21 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.498 | 0.455 | 0.464 | 46 | 55 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.764 | 0.720 | 0.729 | 73 | 29 | yes | +0.021 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL3 | game_spread | 0.221 | 0.185 | 0.192 | 19 | 82 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM3 | team_total | 0.748 | 0.790 | 0.782 | 80 | 22 | no | +0.020 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.166 | 0.120 | 0.128 | 14 | 90 | yes | +0.018 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR2 | game_spread | 0.248 | 0.285 | 0.277 | 29 | 72 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-TOR2 | team_total | 0.803 | 0.840 | 0.833 | 85 | 17 | no | +0.017 | OK |
| KXNHLTOTAL-26SEP29FLACAR-9 | game_total | 0.218 | 0.185 | 0.191 | 19 | 82 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL3 | team_total | 0.672 | 0.630 | 0.639 | 64 | 38 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 | team_total | 0.471 | 0.430 | 0.438 | 44 | 58 | yes | +0.014 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-9 | game_total | 0.225 | 0.195 | 0.201 | 20 | 81 | yes | +0.014 | OK |
| KXNHLTOTAL-26SEP29VANEDM-9 | game_total | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-8 | game_total | 0.205 | 0.235 | 0.229 | 24 | 77 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-TOR4 | team_total | 0.382 | 0.420 | 0.412 | 43 | 59 | no | +0.012 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR2 | game_spread | 0.245 | 0.275 | 0.269 | 28 | 73 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK6 | team_total | 0.120 | 0.155 | 0.148 | 17 | 86 | no | +0.011 | OK |
| KXNHLTOTAL-26SEP29FLACAR-10 | game_total | 0.107 | 0.085 | 0.089 | 9 | 92 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM6 | team_total | 0.188 | 0.220 | 0.213 | 23 | 79 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL6 | team_total | 0.137 | 0.105 | 0.111 | 12 | 91 | yes | +0.009 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-8 | game_total | 0.313 | 0.285 | 0.290 | 29 | 72 | yes | +0.008 | OK |
| KXNHLTOTAL-26SEP29FLACAR-3 | game_total | 0.970 | 0.955 | 0.958 | 96 | 5 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-TOR3 | team_total | 0.596 | 0.635 | 0.627 | 65 | 38 | no | +0.007 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-10 | game_total | 0.113 | 0.095 | 0.098 | 10 | 91 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL2 | team_total | 0.855 | 0.830 | 0.835 | 84 | 18 | yes | +0.005 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-BOS2 | game_spread | 0.309 | 0.285 | 0.290 | 29 | 72 | yes | +0.005 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 0.655 | 0.613 | 0.161 | 0.201 | 6.51 | 6.46 | 0.984/1.008 | KXNHLGAME-26SEP29FLACAR-CAR -0.041 |
| MTL @ TOR | 0.442 | 0.487 | 0.166 | 0.217 | 6.55 | 6.30 | 0.988/0.942 | KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 -0.061 |
| NYR @ BOS | 0.545 | 0.524 | 0.181 | 0.226 | 5.78 | 6.14 | 0.955/0.945 | KXNHLTOTAL-26SEP29NYRBOS-7 +0.063 |
| VAN @ EDM | 0.652 | 0.638 | 0.159 | 0.200 | 6.69 | 6.54 | 1.022/1.026 | KXNHLTOTAL-26SEP29VANEDM-8 -0.030 |
| CHI @ VGK | 0.618 | 0.662 | 0.173 | 0.206 | 6.03 | 6.20 | 1.003/0.987 | KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
