# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-29T18:05:53Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2900 · contracts joined: 1089 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 964, 'OK': 85, 'NO_EDGE': 40}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 155, 'game_early_goal': 5, 'first_goal': 165, 'game_winner': 10, 'player_goals': 297, 'game_overtime': 5, 'player_points': 207, 'goalie_saves': 10, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 2026-09-29T21:00:00Z | T-90m | 0.651 | 0.349 | 0.163 | 6.52 | 3.76 | 2.77 | 265 (25/240) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-09-29T23:00:00Z | T-3h | 0.447 | 0.553 | 0.169 | 6.52 | 3.09 | 3.44 | 209 (25/184) | PROBABLE/CONFIRMED |
| NYR @ BOS | 2026-09-30T00:00:00Z | T-3h | 0.545 | 0.455 | 0.181 | 5.78 | 3.02 | 2.77 | 221 (25/196) | CONFIRMED/PROBABLE |
| VAN @ EDM | 2026-09-30T02:00:00Z | T-6h | 0.645 | 0.355 | 0.157 | 6.63 | 3.79 | 2.83 | 199 (25/174) | CONFIRMED/PROJECTED |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-6h | 0.626 | 0.374 | 0.168 | 6.04 | 3.41 | 2.63 | 195 (25/170) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26SEP29FLACAR-CAR | game_winner | 0.651 | 0.545 | 0.567 | 55 | 46 | yes | +0.084 | OK |
| KXNHLGAME-26SEP29FLACAR-FLA | game_winner | 0.349 | 0.455 | 0.433 | 46 | 55 | no | +0.084 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR2 | game_spread | 0.427 | 0.325 | 0.345 | 33 | 68 | yes | +0.082 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR3 | team_total | 0.734 | 0.635 | 0.656 | 64 | 37 | yes | +0.077 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.289 | 0.385 | 0.365 | 39 | 62 | no | +0.074 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.434 | 0.525 | 0.507 | 53 | 48 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR4 | team_total | 0.535 | 0.445 | 0.463 | 45 | 56 | yes | +0.068 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA2 | game_spread | 0.173 | 0.255 | 0.237 | 26 | 75 | no | +0.064 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR3 | game_spread | 0.295 | 0.215 | 0.230 | 22 | 79 | yes | +0.063 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.355 | 0.275 | 0.290 | 28 | 73 | yes | +0.061 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.645 | 0.725 | 0.710 | 73 | 28 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR4 | team_total | 0.312 | 0.395 | 0.378 | 40 | 61 | no | +0.061 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.374 | 0.295 | 0.310 | 30 | 71 | yes | +0.060 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.626 | 0.705 | 0.690 | 71 | 30 | no | +0.060 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.255 | 0.340 | 0.322 | 35 | 67 | no | +0.059 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA4 | team_total | 0.309 | 0.385 | 0.369 | 39 | 62 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR5 | team_total | 0.325 | 0.255 | 0.268 | 26 | 75 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM4 | team_total | 0.542 | 0.615 | 0.601 | 62 | 39 | no | +0.052 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA3 | game_spread | 0.093 | 0.155 | 0.140 | 16 | 85 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.455 | 0.530 | 0.515 | 54 | 48 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR3 | team_total | 0.528 | 0.600 | 0.586 | 61 | 41 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.324 | 0.255 | 0.268 | 27 | 76 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.538 | 0.475 | 0.488 | 48 | 53 | yes | +0.040 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.177 | 0.125 | 0.134 | 13 | 88 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.335 | 0.410 | 0.394 | 43 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.185 | 0.135 | 0.144 | 14 | 87 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.673 | 0.735 | 0.723 | 75 | 28 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR6 | team_total | 0.170 | 0.125 | 0.133 | 13 | 88 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA5 | team_total | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-5 | game_total | 0.717 | 0.770 | 0.760 | 78 | 24 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA3 | team_total | 0.523 | 0.575 | 0.565 | 58 | 43 | no | +0.030 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-6 | game_total | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR2 | team_total | 0.889 | 0.840 | 0.851 | 85 | 17 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR5 | team_total | 0.150 | 0.200 | 0.189 | 21 | 81 | no | +0.029 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-4 | game_total | 0.813 | 0.860 | 0.851 | 87 | 15 | no | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-BOS | game_winner | 0.545 | 0.495 | 0.505 | 50 | 51 | yes | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-NYR | game_winner | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA2 | team_total | 0.751 | 0.795 | 0.787 | 80 | 21 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.165 | 0.115 | 0.124 | 13 | 90 | yes | +0.027 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL2 | game_spread | 0.342 | 0.295 | 0.304 | 30 | 71 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 | team_total | 0.464 | 0.415 | 0.425 | 42 | 59 | yes | +0.027 | OK |
| KXNHLGAME-26SEP29MTLTOR-MTL | game_winner | 0.553 | 0.505 | 0.515 | 51 | 50 | yes | +0.025 | OK |
| KXNHLGAME-26SEP29MTLTOR-TOR | game_winner | 0.447 | 0.495 | 0.485 | 50 | 51 | no | +0.025 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR3 | game_spread | 0.146 | 0.185 | 0.177 | 19 | 82 | no | +0.024 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.098 | 0.065 | 0.071 | 7 | 94 | yes | +0.023 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.263 | 0.315 | 0.304 | 33 | 70 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM6 | team_total | 0.176 | 0.220 | 0.211 | 23 | 79 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.766 | 0.715 | 0.726 | 73 | 30 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29FLACAR-9 | game_total | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29FLACAR-8 | game_total | 0.305 | 0.265 | 0.273 | 27 | 74 | yes | +0.022 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-7 | game_total | 0.382 | 0.425 | 0.416 | 43 | 58 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR2 | team_total | 0.757 | 0.805 | 0.796 | 82 | 21 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL5 | team_total | 0.272 | 0.230 | 0.238 | 24 | 78 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM3 | team_total | 0.740 | 0.780 | 0.772 | 79 | 23 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL6 | team_total | 0.134 | 0.100 | 0.106 | 11 | 91 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK2 | team_total | 0.856 | 0.890 | 0.884 | 90 | 12 | no | +0.017 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-TOR2 | game_spread | 0.250 | 0.285 | 0.278 | 29 | 72 | no | +0.016 | OK |
| KXNHLTOTAL-26SEP29FLACAR-6 | game_total | 0.613 | 0.575 | 0.583 | 58 | 43 | yes | +0.016 | OK |
| KXNHLTOTAL-26SEP29FLACAR-7 | game_total | 0.503 | 0.465 | 0.473 | 47 | 54 | yes | +0.015 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-8 | game_total | 0.205 | 0.235 | 0.229 | 24 | 77 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.489 | 0.455 | 0.462 | 46 | 55 | yes | +0.012 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR2 | game_spread | 0.245 | 0.275 | 0.269 | 28 | 73 | no | +0.011 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-9 | game_total | 0.219 | 0.190 | 0.195 | 20 | 82 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.281 | 0.245 | 0.252 | 26 | 77 | yes | +0.007 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-10 | game_total | 0.113 | 0.085 | 0.090 | 10 | 93 | yes | +0.007 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL3 | game_spread | 0.217 | 0.195 | 0.199 | 20 | 81 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK6 | team_total | 0.125 | 0.155 | 0.149 | 17 | 86 | no | +0.006 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-BOS2 | game_spread | 0.309 | 0.285 | 0.290 | 29 | 72 | yes | +0.005 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.753 | 0.775 | 0.771 | 78 | 23 | no | +0.005 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-9 | game_total | 0.136 | 0.155 | 0.151 | 16 | 85 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.132 | 0.105 | 0.110 | 12 | 91 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL3 | team_total | 0.670 | 0.630 | 0.638 | 65 | 39 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM2 | team_total | 0.891 | 0.915 | 0.911 | 93 | 10 | no | +0.003 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-2 | game_total | 0.976 | 0.985 | 0.984 | 99 | 2 | no | +0.003 | OK |
| KXNHLTOTAL-26SEP29FLACAR-10 | game_total | 0.109 | 0.095 | 0.098 | 10 | 91 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29FLACAR-4 | game_total | 0.880 | 0.860 | 0.864 | 87 | 15 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-8 | game_total | 0.305 | 0.280 | 0.285 | 29 | 73 | yes | +0.001 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 0.651 | 0.611 | 0.163 | 0.208 | 6.52 | 6.49 | 0.993/1.008 | KXNHLGAME-26SEP29FLACAR-CAR -0.040 |
| MTL @ TOR | 0.447 | 0.489 | 0.169 | 0.220 | 6.52 | 6.30 | 0.983/0.942 | KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 -0.058 |
| NYR @ BOS | 0.545 | 0.524 | 0.181 | 0.226 | 5.78 | 6.14 | 0.955/0.945 | KXNHLTOTAL-26SEP29NYRBOS-7 +0.063 |
| VAN @ EDM | 0.645 | 0.631 | 0.157 | 0.204 | 6.63 | 6.53 | 1.022/1.021 | KXNHLTOTAL-26SEP29VANEDM-8 -0.023 |
| CHI @ VGK | 0.626 | 0.672 | 0.168 | 0.201 | 6.04 | 6.25 | 1.003/1.003 | KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 +0.065 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
