# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-30T01:29:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 2 · markets on board: 2821 · contracts joined: 394 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 344, 'OK': 36, 'NO_EDGE': 14}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 51, 'game_early_goal': 2, 'first_goal': 62, 'game_winner': 4, 'player_goals': 111, 'game_overtime': 2, 'player_points': 64, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ EDM | 2026-09-30T02:00:00Z | T-30m | 0.652 | 0.348 | 0.159 | 6.69 | 3.85 | 2.84 | 199 (25/174) | CONFIRMED/PROBABLE |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-60m | 0.618 | 0.382 | 0.173 | 6.03 | 3.38 | 2.66 | 195 (25/170) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.300 | 0.395 | 0.375 | 40 | 61 | no | +0.073 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.382 | 0.475 | 0.456 | 48 | 53 | no | +0.071 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.244 | 0.335 | 0.316 | 34 | 67 | no | +0.070 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.382 | 0.295 | 0.312 | 30 | 71 | yes | +0.067 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.618 | 0.705 | 0.688 | 71 | 30 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 | team_total | 0.448 | 0.535 | 0.518 | 54 | 47 | no | +0.065 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.652 | 0.735 | 0.719 | 74 | 27 | no | +0.064 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.348 | 0.265 | 0.281 | 27 | 74 | yes | +0.064 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.440 | 0.525 | 0.508 | 53 | 48 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM4 | team_total | 0.551 | 0.615 | 0.602 | 62 | 39 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.326 | 0.260 | 0.273 | 27 | 75 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK5 | team_total | 0.253 | 0.320 | 0.306 | 33 | 69 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.539 | 0.475 | 0.488 | 48 | 53 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK3 | team_total | 0.666 | 0.730 | 0.718 | 74 | 28 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.346 | 0.410 | 0.397 | 42 | 60 | no | +0.037 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.175 | 0.125 | 0.134 | 13 | 88 | yes | +0.037 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.191 | 0.145 | 0.153 | 15 | 86 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.166 | 0.115 | 0.124 | 13 | 90 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK2 | team_total | 0.851 | 0.890 | 0.883 | 90 | 12 | no | +0.022 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.096 | 0.065 | 0.070 | 7 | 94 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.498 | 0.455 | 0.464 | 46 | 55 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.764 | 0.720 | 0.729 | 73 | 29 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM3 | team_total | 0.748 | 0.790 | 0.782 | 80 | 22 | no | +0.020 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-5 | game_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM2 | team_total | 0.897 | 0.925 | 0.920 | 93 | 8 | no | +0.018 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI3 | game_spread | 0.100 | 0.075 | 0.080 | 8 | 93 | yes | +0.015 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-4 | game_total | 0.837 | 0.865 | 0.860 | 87 | 14 | no | +0.015 | OK |
| KXNHLTOTAL-26SEP29VANEDM-9 | game_total | 0.245 | 0.215 | 0.221 | 22 | 79 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.286 | 0.245 | 0.253 | 26 | 77 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK6 | team_total | 0.120 | 0.155 | 0.148 | 17 | 86 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM6 | team_total | 0.188 | 0.220 | 0.213 | 23 | 79 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.137 | 0.110 | 0.115 | 12 | 90 | yes | +0.010 | OK |
| KXNHLTOTAL-26SEP29VANEDM-10 | game_total | 0.125 | 0.105 | 0.109 | 11 | 90 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN6 | team_total | 0.069 | 0.050 | 0.053 | 6 | 96 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI6 | team_total | 0.056 | 0.040 | 0.043 | 5 | 97 | yes | +0.002 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-6 | game_total | 0.532 | 0.555 | 0.550 | 56 | 45 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI2 | team_total | 0.734 | 0.700 | 0.707 | 72 | 32 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-4 | game_total | 0.895 | 0.905 | 0.903 | 91 | 10 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-8 | game_total | 0.332 | 0.315 | 0.318 | 32 | 69 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-5 | game_total | 0.824 | 0.835 | 0.833 | 84 | 17 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-2 | game_total | 0.982 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-7 | game_total | 0.420 | 0.435 | 0.432 | 44 | 57 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-10 | game_total | 0.077 | 0.070 | 0.071 | 8 | 94 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-8 | game_total | 0.239 | 0.245 | 0.244 | 25 | 76 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26SEP29CHIVGK-9 | game_total | 0.164 | 0.170 | 0.169 | 18 | 84 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-7 | game_total | 0.521 | 0.515 | 0.516 | 52 | 49 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26SEP29VANEDM-6 | game_total | 0.634 | 0.635 | 0.635 | 64 | 37 |  | -0.020 | NO_EDGE |
| KXNHL1P-26SEP29VANEDM-EDM | period_winner |  | 0.450 |  | 46 | 56 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP29VANEDM-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP29VANEDM-VAN | period_winner |  | 0.225 |  | 23 | 78 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP29VANEDM-EDM2 | period_spread |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP29VANEDM-VAN2 | period_spread |  | 0.060 |  | 9 | 97 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26SEP29VANEDM-1 | period_total |  | 0.845 |  | 86 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26SEP29VANEDM-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26SEP29VANEDM-3 | period_total |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26SEP29VANEDM-EDM | period_winner |  | 0.475 |  | 49 | 54 |  |  | UNSUPPORTED |
| KXNHL2P-26SEP29VANEDM-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26SEP29VANEDM-VAN | period_winner |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26SEP29VANEDM-EDM2 | period_spread |  | 0.215 |  | 24 | 81 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26SEP29VANEDM-VAN2 | period_spread |  | 0.070 |  | 10 | 96 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26SEP29VANEDM-1 | period_total |  | 0.900 |  | 93 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26SEP29VANEDM-2 | period_total |  | 0.650 |  | 68 | 38 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26SEP29VANEDM-3 | period_total |  | 0.375 |  | 40 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26SEP29VANEDM-EDM | period_winner |  | 0.505 |  | 53 | 52 |  |  | UNSUPPORTED |
| KXNHL3P-26SEP29VANEDM-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3P-26SEP29VANEDM-VAN | period_winner |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26SEP29VANEDM-EDM2 | period_spread |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26SEP29VANEDM-VAN2 | period_spread |  | 0.080 |  | 11 | 95 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26SEP29VANEDM-1 | period_total |  | 0.905 |  | 92 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26SEP29VANEDM-2 | period_total |  | 0.685 |  | 71 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26SEP29VANEDM-3 | period_total |  | 0.410 |  | 43 | 61 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29VANEDM-EDMCMCDAVID97-1 | player_assists |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29VANEDM-EDMCMCDAVID97-2 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29VANEDM-EDMCMCDAVID97-3 | player_assists |  | 0.095 |  | 12 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29VANEDM-EDMEBOUCHARD2-1 | player_assists |  | 0.615 |  | 63 | 40 |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29VANEDM-EDMEBOUCHARD2-2 | player_assists |  |  |  | 26 |  |  |  | UNSUPPORTED |
| KXNHLAST-26SEP29VANEDM-EDMEBOUCHARD2-3 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ EDM | 0.652 | 0.638 | 0.159 | 0.200 | 6.69 | 6.54 | 1.022/1.026 | KXNHLTOTAL-26SEP29VANEDM-8 -0.030 |
| CHI @ VGK | 0.618 | 0.662 | 0.173 | 0.206 | 6.03 | 6.20 | 1.003/0.987 | KXNHLTEAMTOTAL-26SEP29CHIVGK-VGK4 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
