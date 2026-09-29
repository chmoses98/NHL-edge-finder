# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-29T16:23:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2735 · contracts joined: 924 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 799, 'OK': 82, 'NO_EDGE': 43}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 155, 'game_early_goal': 5, 'game_winner': 10, 'player_goals': 297, 'game_overtime': 5, 'player_points': 207, 'goalie_saves': 10, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 2026-09-29T21:00:00Z | T-3h | 0.651 | 0.349 | 0.163 | 6.52 | 3.76 | 2.77 | 230 (25/205) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-09-29T23:00:00Z | T-6h | 0.462 | 0.538 | 0.171 | 6.58 | 3.17 | 3.41 | 175 (25/150) | PROJECTED/PROJECTED |
| NYR @ BOS | 2026-09-30T00:00:00Z | T-6h | 0.545 | 0.455 | 0.179 | 5.83 | 3.06 | 2.77 | 187 (25/162) | CONFIRMED/PROJECTED |
| VAN @ EDM | 2026-09-30T02:00:00Z | T-6h | 0.645 | 0.355 | 0.157 | 6.63 | 3.79 | 2.83 | 169 (25/144) | CONFIRMED/PROJECTED |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-6h | 0.626 | 0.374 | 0.168 | 6.04 | 3.41 | 2.63 | 163 (25/138) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP29FLACAR-CAR | game_winner | 0.651 | 0.545 | 0.567 | 55 | 46 | yes | +0.084 | OK |
| KXNHLGAME-26SEP29FLACAR-FLA | game_winner | 0.349 | 0.455 | 0.433 | 46 | 55 | no | +0.084 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR2 | game_spread | 0.427 | 0.325 | 0.345 | 33 | 68 | yes | +0.082 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.289 | 0.385 | 0.365 | 39 | 62 | no | +0.074 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR4 | team_total | 0.535 | 0.435 | 0.455 | 45 | 58 | yes | +0.068 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA2 | game_spread | 0.173 | 0.255 | 0.237 | 26 | 75 | no | +0.064 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR3 | game_spread | 0.295 | 0.215 | 0.230 | 22 | 79 | yes | +0.063 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.355 | 0.275 | 0.290 | 28 | 73 | yes | +0.061 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.645 | 0.725 | 0.710 | 73 | 28 | no | +0.061 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.374 | 0.295 | 0.310 | 30 | 71 | yes | +0.060 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.626 | 0.705 | 0.690 | 71 | 30 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR4 | team_total | 0.314 | 0.395 | 0.378 | 40 | 61 | no | +0.059 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.255 | 0.340 | 0.322 | 35 | 67 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR3 | team_total | 0.734 | 0.645 | 0.664 | 66 | 37 | yes | +0.058 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR5 | team_total | 0.325 | 0.245 | 0.260 | 26 | 77 | yes | +0.052 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA3 | game_spread | 0.093 | 0.155 | 0.140 | 16 | 85 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.455 | 0.530 | 0.515 | 54 | 48 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM4 | team_total | 0.542 | 0.610 | 0.597 | 62 | 40 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA3 | team_total | 0.523 | 0.585 | 0.573 | 59 | 42 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.538 | 0.475 | 0.488 | 48 | 53 | yes | +0.040 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.177 | 0.125 | 0.134 | 13 | 88 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.335 | 0.410 | 0.394 | 43 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.185 | 0.135 | 0.144 | 14 | 87 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.673 | 0.735 | 0.723 | 75 | 28 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR6 | team_total | 0.170 | 0.115 | 0.125 | 13 | 90 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.324 | 0.260 | 0.272 | 28 | 76 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR3 | team_total | 0.533 | 0.590 | 0.579 | 60 | 42 | no | +0.030 | OK |
| KXNHLGAME-26SEP29NYRBOS-BOS | game_winner | 0.545 | 0.495 | 0.505 | 50 | 51 | yes | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-NYR | game_winner | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA2 | team_total | 0.751 | 0.805 | 0.795 | 82 | 21 | no | +0.027 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR3 | game_spread | 0.134 | 0.175 | 0.166 | 18 | 83 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA4 | team_total | 0.309 | 0.370 | 0.357 | 39 | 65 | no | +0.025 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-6 | game_total | 0.499 | 0.545 | 0.536 | 55 | 46 | no | +0.024 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.098 | 0.065 | 0.071 | 7 | 94 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR2 | team_total | 0.755 | 0.805 | 0.796 | 82 | 21 | no | +0.023 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-5 | game_total | 0.725 | 0.775 | 0.765 | 79 | 24 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.263 | 0.315 | 0.304 | 33 | 70 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM6 | team_total | 0.176 | 0.220 | 0.211 | 23 | 79 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.766 | 0.715 | 0.726 | 73 | 30 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29FLACAR-9 | game_total | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29FLACAR-8 | game_total | 0.305 | 0.260 | 0.269 | 27 | 75 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR2 | team_total | 0.889 | 0.840 | 0.851 | 86 | 18 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR5 | team_total | 0.149 | 0.195 | 0.185 | 21 | 82 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 | team_total | 0.456 | 0.415 | 0.423 | 42 | 59 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.281 | 0.235 | 0.244 | 25 | 78 | yes | +0.017 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-9 | game_total | 0.228 | 0.190 | 0.197 | 20 | 82 | yes | +0.017 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR2 | game_spread | 0.239 | 0.275 | 0.268 | 28 | 73 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.165 | 0.120 | 0.128 | 14 | 90 | yes | +0.017 | OK |
| KXNHLTOTAL-26SEP29FLACAR-6 | game_total | 0.613 | 0.575 | 0.583 | 58 | 43 | yes | +0.016 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-7 | game_total | 0.388 | 0.425 | 0.417 | 43 | 58 | no | +0.015 | OK |
| KXNHLTOTAL-26SEP29FLACAR-7 | game_total | 0.503 | 0.465 | 0.473 | 47 | 54 | yes | +0.015 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-BOS2 | game_spread | 0.319 | 0.285 | 0.292 | 29 | 72 | yes | +0.015 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR3 | game_spread | 0.158 | 0.185 | 0.179 | 19 | 82 | no | +0.012 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-4 | game_total | 0.819 | 0.855 | 0.848 | 87 | 16 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.489 | 0.455 | 0.462 | 46 | 55 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA5 | team_total | 0.158 | 0.200 | 0.191 | 22 | 82 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL5 | team_total | 0.264 | 0.225 | 0.232 | 24 | 79 | yes | +0.011 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-8 | game_total | 0.316 | 0.280 | 0.287 | 29 | 73 | yes | +0.011 | OK |
| KXNHLGAME-26SEP29MTLTOR-MTL | game_winner | 0.538 | 0.505 | 0.512 | 51 | 50 | yes | +0.011 | OK |
| KXNHLGAME-26SEP29MTLTOR-TOR | game_winner | 0.462 | 0.495 | 0.488 | 50 | 51 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL3 | team_total | 0.666 | 0.625 | 0.633 | 64 | 39 | yes | +0.010 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL2 | game_spread | 0.324 | 0.295 | 0.301 | 30 | 71 | yes | +0.009 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-3 | game_total | 0.950 | 0.965 | 0.962 | 97 | 4 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM3 | team_total | 0.740 | 0.785 | 0.777 | 81 | 24 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK2 | team_total | 0.856 | 0.890 | 0.884 | 91 | 13 | no | +0.007 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR2 | game_spread | 0.260 | 0.290 | 0.284 | 30 | 72 | no | +0.006 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.753 | 0.775 | 0.771 | 78 | 23 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI2 | team_total | 0.729 | 0.695 | 0.702 | 71 | 32 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.132 | 0.095 | 0.102 | 12 | 93 | yes | +0.004 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI3 | game_spread | 0.099 | 0.080 | 0.084 | 9 | 93 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM2 | team_total | 0.891 | 0.920 | 0.915 | 94 | 10 | no | +0.003 | OK |
| KXNHLTOTAL-26SEP29FLACAR-10 | game_total | 0.109 | 0.090 | 0.093 | 10 | 92 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-6 | game_total | 0.619 | 0.595 | 0.600 | 60 | 41 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29FLACAR-4 | game_total | 0.880 | 0.865 | 0.868 | 87 | 14 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL6 | team_total | 0.129 | 0.105 | 0.109 | 12 | 91 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-2 | game_total | 0.977 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-4 | game_total | 0.841 | 0.865 | 0.860 | 88 | 15 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP29FLACAR-3 | game_total | 0.973 | 0.965 | 0.967 | 97 | 4 | yes | +0.001 | OK |

_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
