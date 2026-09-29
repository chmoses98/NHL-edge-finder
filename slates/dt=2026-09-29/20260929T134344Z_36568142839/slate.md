# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-29T13:43:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2529 · contracts joined: 750 (unjoined to any game: 1452)
gates: {'UNSUPPORTED': 625, 'OK': 76, 'NO_EDGE': 49}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 104, 'game_early_goal': 5, 'game_winner': 10, 'player_goals': 186, 'game_overtime': 5, 'player_points': 143, 'goalie_saves': 62, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 2026-09-29T21:00:00Z | T-6h | 0.651 | 0.349 | 0.163 | 6.52 | 3.76 | 2.77 | 249 (25/224) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-09-29T23:00:00Z | T-6h | 0.462 | 0.538 | 0.171 | 6.58 | 3.17 | 3.41 | 195 (25/170) | PROJECTED/PROJECTED |
| NYR @ BOS | 2026-09-30T00:00:00Z | T-6h | 0.530 | 0.470 | 0.185 | 5.94 | 3.06 | 2.88 | 204 (25/179) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-09-30T02:00:00Z | T-12h | 0.645 | 0.355 | 0.157 | 6.63 | 3.79 | 2.83 | 51 (25/26) | CONFIRMED/PROJECTED |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-12h | 0.626 | 0.374 | 0.168 | 6.04 | 3.41 | 2.63 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP29FLACAR-CAR | game_winner | 0.651 | 0.535 | 0.559 | 54 | 47 | yes | +0.094 | OK |
| KXNHLGAME-26SEP29FLACAR-FLA | game_winner | 0.349 | 0.465 | 0.441 | 47 | 54 | no | +0.094 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR2 | game_spread | 0.427 | 0.320 | 0.340 | 33 | 69 | yes | +0.082 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.289 | 0.385 | 0.365 | 39 | 62 | no | +0.074 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR3 | game_spread | 0.295 | 0.205 | 0.221 | 21 | 80 | yes | +0.073 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.068 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA2 | game_spread | 0.173 | 0.255 | 0.237 | 26 | 75 | no | +0.064 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.355 | 0.275 | 0.290 | 28 | 73 | yes | +0.061 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.645 | 0.725 | 0.710 | 73 | 28 | no | +0.061 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.255 | 0.340 | 0.322 | 35 | 67 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.335 | 0.420 | 0.402 | 43 | 59 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR4 | team_total | 0.535 | 0.440 | 0.459 | 46 | 58 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR3 | team_total | 0.734 | 0.645 | 0.664 | 66 | 37 | yes | +0.058 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR5 | team_total | 0.325 | 0.245 | 0.260 | 26 | 77 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA3 | team_total | 0.523 | 0.595 | 0.581 | 60 | 41 | no | +0.050 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.374 | 0.305 | 0.318 | 31 | 70 | yes | +0.049 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.626 | 0.695 | 0.682 | 70 | 31 | no | +0.049 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA3 | game_spread | 0.093 | 0.155 | 0.140 | 16 | 85 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.455 | 0.535 | 0.519 | 55 | 48 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA4 | team_total | 0.309 | 0.385 | 0.369 | 40 | 63 | no | +0.045 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.177 | 0.125 | 0.134 | 13 | 88 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR4 | team_total | 0.335 | 0.395 | 0.383 | 40 | 61 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA2 | team_total | 0.751 | 0.810 | 0.799 | 82 | 20 | no | +0.038 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.185 | 0.135 | 0.144 | 14 | 87 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR6 | team_total | 0.170 | 0.115 | 0.125 | 13 | 90 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM4 | team_total | 0.542 | 0.600 | 0.589 | 61 | 41 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.324 | 0.265 | 0.276 | 28 | 75 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.538 | 0.475 | 0.488 | 49 | 54 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR2 | team_total | 0.889 | 0.835 | 0.847 | 85 | 18 | yes | +0.030 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.098 | 0.065 | 0.071 | 7 | 94 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.263 | 0.315 | 0.304 | 33 | 70 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.673 | 0.725 | 0.715 | 74 | 29 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM6 | team_total | 0.176 | 0.225 | 0.215 | 24 | 79 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.766 | 0.715 | 0.726 | 73 | 30 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29FLACAR-9 | game_total | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29FLACAR-8 | game_total | 0.305 | 0.265 | 0.273 | 27 | 74 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA5 | team_total | 0.158 | 0.205 | 0.195 | 22 | 81 | no | +0.021 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL2 | game_spread | 0.324 | 0.285 | 0.293 | 29 | 72 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 | team_total | 0.456 | 0.415 | 0.423 | 42 | 59 | yes | +0.019 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-9 | game_total | 0.228 | 0.195 | 0.201 | 20 | 81 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.165 | 0.125 | 0.132 | 14 | 89 | yes | +0.017 | OK |
| KXNHLTOTAL-26SEP29FLACAR-6 | game_total | 0.613 | 0.575 | 0.583 | 58 | 43 | yes | +0.016 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR3 | game_spread | 0.146 | 0.175 | 0.169 | 18 | 83 | no | +0.014 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-4 | game_total | 0.828 | 0.860 | 0.854 | 87 | 15 | no | +0.013 | OK |
| KXNHLGAME-26SEP29NYRBOS-BOS | game_winner | 0.530 | 0.495 | 0.502 | 50 | 51 | yes | +0.013 | OK |
| KXNHLGAME-26SEP29NYRBOS-NYR | game_winner | 0.470 | 0.505 | 0.498 | 51 | 50 | no | +0.013 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR3 | game_spread | 0.158 | 0.185 | 0.179 | 19 | 82 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.489 | 0.450 | 0.458 | 46 | 56 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL5 | team_total | 0.264 | 0.225 | 0.232 | 24 | 79 | yes | +0.011 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-8 | game_total | 0.316 | 0.285 | 0.291 | 29 | 72 | yes | +0.011 | OK |
| KXNHLGAME-26SEP29MTLTOR-MTL | game_winner | 0.538 | 0.505 | 0.512 | 51 | 50 | yes | +0.011 | OK |
| KXNHLGAME-26SEP29MTLTOR-TOR | game_winner | 0.462 | 0.495 | 0.488 | 50 | 51 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL3 | team_total | 0.666 | 0.625 | 0.633 | 64 | 39 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA6 | team_total | 0.065 | 0.090 | 0.084 | 10 | 92 | no | +0.010 | OK |
| KXNHLTOTAL-26SEP29FLACAR-3 | game_total | 0.973 | 0.955 | 0.959 | 96 | 5 | yes | +0.010 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-3 | game_total | 0.972 | 0.955 | 0.959 | 96 | 5 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.281 | 0.250 | 0.256 | 26 | 76 | yes | +0.007 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-6 | game_total | 0.516 | 0.545 | 0.539 | 55 | 46 | no | +0.007 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR2 | game_spread | 0.260 | 0.290 | 0.284 | 30 | 72 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK6 | team_total | 0.125 | 0.155 | 0.149 | 17 | 86 | no | +0.006 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-5 | game_total | 0.742 | 0.770 | 0.764 | 78 | 24 | no | +0.006 | OK |
| KXNHLTOTAL-26SEP29FLACAR-7 | game_total | 0.503 | 0.475 | 0.481 | 48 | 53 | yes | +0.005 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.753 | 0.775 | 0.771 | 78 | 23 | no | +0.005 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR2 | game_spread | 0.251 | 0.275 | 0.270 | 28 | 73 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI2 | team_total | 0.729 | 0.695 | 0.702 | 71 | 32 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.132 | 0.105 | 0.110 | 12 | 91 | yes | +0.004 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI3 | game_spread | 0.099 | 0.080 | 0.084 | 9 | 93 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR5 | team_total | 0.167 | 0.195 | 0.189 | 21 | 82 | no | +0.002 | OK |
| KXNHLTOTAL-26SEP29FLACAR-10 | game_total | 0.109 | 0.085 | 0.089 | 10 | 93 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-5 | game_total | 0.814 | 0.790 | 0.795 | 80 | 22 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-6 | game_total | 0.619 | 0.595 | 0.600 | 60 | 41 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL6 | team_total | 0.129 | 0.105 | 0.109 | 12 | 91 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-7 | game_total | 0.508 | 0.485 | 0.490 | 49 | 52 | yes | +0.001 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-4 | game_total | 0.841 | 0.865 | 0.860 | 88 | 15 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-3 | game_total | 0.957 | 0.965 | 0.964 | 97 | 4 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26SEP29NYRBOS-7 | game_total | 0.403 | 0.430 | 0.425 | 44 | 58 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR2 | team_total | 0.779 | 0.805 | 0.800 | 82 | 21 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI6 | team_total | 0.053 | 0.035 | 0.038 | 5 | 98 |  | -0.001 | NO_EDGE |

_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
