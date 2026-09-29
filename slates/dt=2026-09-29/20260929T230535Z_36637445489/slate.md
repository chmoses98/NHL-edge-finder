# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-29T23:05:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 3 · markets on board: 2889 · contracts joined: 615 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 540, 'OK': 54, 'NO_EDGE': 21}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 82, 'game_early_goal': 3, 'first_goal': 96, 'game_winner': 6, 'player_goals': 169, 'game_overtime': 3, 'player_points': 109, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ BOS | 2026-09-30T00:00:00Z | T-30m | 0.545 | 0.455 | 0.181 | 5.78 | 3.02 | 2.77 | 221 (25/196) | CONFIRMED/PROBABLE |
| VAN @ EDM | 2026-09-30T02:00:00Z | T-90m | 0.652 | 0.348 | 0.159 | 6.69 | 3.85 | 2.84 | 199 (25/174) | CONFIRMED/PROBABLE |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-3h | 0.618 | 0.382 | 0.173 | 6.03 | 3.38 | 2.66 | 195 (25/170) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.382 | 0.475 | 0.456 | 48 | 53 | no | +0.071 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.244 | 0.335 | 0.316 | 34 | 67 | no | +0.070 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.382 | 0.295 | 0.312 | 30 | 71 | yes | +0.067 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.618 | 0.705 | 0.688 | 71 | 30 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.065 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.652 | 0.735 | 0.719 | 74 | 27 | no | +0.064 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.348 | 0.265 | 0.281 | 27 | 74 | yes | +0.064 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.300 | 0.385 | 0.367 | 39 | 62 | no | +0.063 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.440 | 0.525 | 0.508 | 53 | 48 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR3 | team_total | 0.528 | 0.600 | 0.586 | 61 | 41 | no | +0.045 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.191 | 0.135 | 0.145 | 14 | 87 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM4 | team_total | 0.551 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.253 | 0.320 | 0.306 | 33 | 69 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR4 | team_total | 0.312 | 0.380 | 0.366 | 39 | 63 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.539 | 0.475 | 0.488 | 48 | 53 | yes | +0.041 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-5 | game_total | 0.717 | 0.775 | 0.764 | 78 | 23 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.666 | 0.725 | 0.714 | 73 | 28 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.346 | 0.405 | 0.393 | 41 | 60 | no | +0.037 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.175 | 0.125 | 0.134 | 13 | 88 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.326 | 0.265 | 0.277 | 28 | 75 | yes | +0.032 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-6 | game_total | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR5 | team_total | 0.150 | 0.205 | 0.193 | 22 | 81 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM2 | team_total | 0.897 | 0.935 | 0.929 | 94 | 7 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.166 | 0.115 | 0.124 | 13 | 90 | yes | +0.028 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-4 | game_total | 0.813 | 0.855 | 0.847 | 86 | 15 | no | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-BOS | game_winner | 0.545 | 0.495 | 0.505 | 50 | 51 | yes | +0.028 | OK |
| KXNHLGAME-26SEP29NYRBOS-NYR | game_winner | 0.455 | 0.505 | 0.495 | 51 | 50 | no | +0.028 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK2 | team_total | 0.851 | 0.885 | 0.879 | 89 | 12 | no | +0.022 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-NYR2 | game_spread | 0.245 | 0.285 | 0.277 | 29 | 72 | no | +0.021 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-7 | game_total | 0.382 | 0.425 | 0.416 | 43 | 58 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR2 | team_total | 0.757 | 0.805 | 0.796 | 82 | 21 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.764 | 0.720 | 0.729 | 73 | 29 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM3 | team_total | 0.748 | 0.790 | 0.782 | 80 | 22 | no | +0.020 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI3 | game_spread | 0.100 | 0.075 | 0.080 | 8 | 93 | yes | +0.015 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-4 | game_total | 0.837 | 0.865 | 0.860 | 87 | 14 | no | +0.015 | OK |
| KXNHLTOTAL-26SEP29VANEDM-9 | game_total | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI6 | team_total | 0.056 | 0.030 | 0.034 | 4 | 98 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.286 | 0.245 | 0.253 | 26 | 77 | yes | +0.012 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-8 | game_total | 0.205 | 0.235 | 0.229 | 24 | 77 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK6 | team_total | 0.120 | 0.155 | 0.148 | 17 | 86 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.498 | 0.465 | 0.472 | 47 | 54 | yes | +0.011 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.096 | 0.070 | 0.075 | 8 | 94 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.137 | 0.110 | 0.115 | 12 | 90 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI2 | team_total | 0.734 | 0.695 | 0.703 | 71 | 32 | yes | +0.009 | OK |
| KXNHLTOTAL-26SEP29VANEDM-10 | game_total | 0.125 | 0.105 | 0.109 | 11 | 90 | yes | +0.008 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-BOS2 | game_spread | 0.309 | 0.285 | 0.290 | 29 | 72 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN6 | team_total | 0.069 | 0.050 | 0.053 | 6 | 96 | yes | +0.005 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-9 | game_total | 0.136 | 0.155 | 0.151 | 16 | 85 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR6 | team_total | 0.061 | 0.085 | 0.080 | 10 | 93 | no | +0.004 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-2 | game_total | 0.976 | 0.985 | 0.984 | 99 | 2 | no | +0.003 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-6 | game_total | 0.532 | 0.555 | 0.550 | 56 | 45 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM6 | team_total | 0.188 | 0.215 | 0.209 | 23 | 80 | no | +0.001 | OK |
| KXNHLTOTAL-26SEP29VANEDM-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26SEP29NYRBOS-10 | game_total | 0.057 | 0.065 | 0.063 | 7 | 94 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-8 | game_total | 0.332 | 0.315 | 0.318 | 32 | 69 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP29NYRBOS-3 | game_total | 0.948 | 0.945 | 0.946 | 95 | 6 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-7 | game_total | 0.420 | 0.435 | 0.432 | 44 | 57 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-2 | game_total | 0.982 | 0.980 | 0.981 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-10 | game_total | 0.077 | 0.075 | 0.075 | 8 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-8 | game_total | 0.239 | 0.245 | 0.244 | 25 | 76 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-4 | game_total | 0.895 | 0.900 | 0.899 | 91 | 11 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS2 | team_total | 0.798 | 0.795 | 0.796 | 80 | 21 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS4 | team_total | 0.367 | 0.375 | 0.373 | 38 | 63 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-9 | game_total | 0.164 | 0.170 | 0.169 | 18 | 84 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-5 | game_total | 0.824 | 0.825 | 0.825 | 83 | 18 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26SEP29NYRBOS-BOS3 | game_spread | 0.184 | 0.185 | 0.185 | 19 | 82 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS3 | team_total | 0.588 | 0.595 | 0.594 | 60 | 41 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-7 | game_total | 0.521 | 0.515 | 0.516 | 52 | 49 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS6 | team_total | 0.082 | 0.085 | 0.084 | 10 | 93 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS5 | team_total | 0.192 | 0.190 | 0.190 | 20 | 82 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-6 | game_total | 0.634 | 0.635 | 0.635 | 64 | 37 |  | -0.020 | NO_EDGE |
| KXNHL1P-26SEP29NYRBOS-BOS | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP29NYRBOS-NYR | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP29NYRBOS-TIE | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP29NYRBOS-BOS2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP29NYRBOS-NYR2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ BOS | 0.545 | 0.524 | 0.181 | 0.226 | 5.78 | 6.14 | 0.955/0.945 | KXNHLTOTAL-26SEP29NYRBOS-7 +0.063 |
| VAN @ EDM | 0.652 | 0.638 | 0.159 | 0.200 | 6.69 | 6.54 | 1.022/1.026 | KXNHLTOTAL-26SEP29VANEDM-8 -0.030 |
| CHI @ VGK | 0.618 | 0.662 | 0.173 | 0.206 | 6.03 | 6.20 | 1.003/0.987 | KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
