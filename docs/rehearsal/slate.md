# NHL slate 2026-09-29 — RESEARCH_ONLY

generated 2026-09-29T12:20:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.0 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2529 · contracts joined: 750 (unjoined to any game: 1452)
gates: {'UNSUPPORTED': 625, 'OK': 91, 'NO_EDGE': 34}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 104, 'unknown': 5, 'game_winner': 10, 'player_goals': 186, 'game_overtime': 5, 'player_points': 143, 'player_unknown': 62, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CAR | 2026-09-29T21:00:00Z | T-6h | 0.652 | 0.348 | 0.156 | 6.85 | 3.96 | 2.89 | 249 (25/224) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-09-29T23:00:00Z | T-6h | 0.457 | 0.543 | 0.162 | 6.90 | 3.32 | 3.58 | 195 (25/170) | PROJECTED/PROJECTED |
| NYR @ BOS | 2026-09-30T00:00:00Z | T-6h | 0.538 | 0.462 | 0.172 | 6.24 | 3.24 | 3.00 | 204 (25/179) | PROJECTED/PROJECTED |
| VAN @ EDM | 2026-09-30T02:00:00Z | T-12h | 0.654 | 0.346 | 0.153 | 6.96 | 4.01 | 2.94 | 51 (25/26) | CONFIRMED/PROJECTED |
| CHI @ VGK | 2026-09-30T02:30:00Z | T-12h | 0.628 | 0.372 | 0.165 | 6.36 | 3.61 | 2.75 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26SEP29FLACAR-CAR2 | game_spread | 0.460 | 0.325 | 0.350 | 33 | 68 | yes | +0.114 | OK |
| KXNHLSPREAD-26SEP29FLACAR-CAR3 | game_spread | 0.328 | 0.205 | 0.227 | 21 | 80 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR4 | team_total | 0.576 | 0.445 | 0.471 | 46 | 57 | yes | +0.099 | OK |
| KXNHLGAME-26SEP29FLACAR-CAR | game_winner | 0.652 | 0.535 | 0.559 | 54 | 47 | yes | +0.094 | OK |
| KXNHLGAME-26SEP29FLACAR-FLA | game_winner | 0.348 | 0.465 | 0.441 | 47 | 54 | no | +0.094 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR3 | team_total | 0.764 | 0.645 | 0.671 | 66 | 37 | yes | +0.089 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR5 | team_total | 0.370 | 0.250 | 0.272 | 27 | 77 | yes | +0.087 | OK |
| KXNHLTOTAL-26SEP29FLACAR-8 | game_total | 0.354 | 0.265 | 0.282 | 27 | 74 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR6 | team_total | 0.206 | 0.115 | 0.130 | 13 | 90 | yes | +0.068 | OK |
| KXNHLTOTAL-26SEP29FLACAR-6 | game_total | 0.663 | 0.575 | 0.593 | 58 | 43 | yes | +0.066 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-8 | game_total | 0.365 | 0.280 | 0.296 | 29 | 73 | yes | +0.061 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-9 | game_total | 0.269 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA2 | game_spread | 0.180 | 0.255 | 0.239 | 26 | 75 | no | +0.057 | OK |
| KXNHLTOTAL-26SEP29FLACAR-9 | game_total | 0.257 | 0.185 | 0.198 | 19 | 82 | yes | +0.056 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI2 | game_spread | 0.194 | 0.125 | 0.137 | 13 | 88 | yes | +0.056 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-6 | game_total | 0.671 | 0.595 | 0.611 | 60 | 41 | yes | +0.054 | OK |
| KXNHLTOTAL-26SEP29FLACAR-7 | game_total | 0.550 | 0.475 | 0.490 | 48 | 53 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN3 | team_total | 0.560 | 0.475 | 0.492 | 49 | 54 | yes | +0.052 | OK |
| KXNHLGAME-26SEP29VANEDM-VAN | game_winner | 0.346 | 0.275 | 0.288 | 28 | 73 | yes | +0.052 | OK |
| KXNHLGAME-26SEP29VANEDM-EDM | game_winner | 0.654 | 0.725 | 0.712 | 73 | 28 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL5 | team_total | 0.304 | 0.225 | 0.240 | 24 | 79 | yes | +0.051 | OK |
| KXNHLGAME-26SEP29CHIVGK-VGK | game_winner | 0.628 | 0.695 | 0.682 | 70 | 31 | no | +0.047 | OK |
| KXNHLGAME-26SEP29CHIVGK-CHI | game_winner | 0.372 | 0.305 | 0.318 | 31 | 70 | yes | +0.047 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-7 | game_total | 0.564 | 0.495 | 0.509 | 50 | 51 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL4 | team_total | 0.493 | 0.415 | 0.430 | 43 | 60 | yes | +0.046 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN2 | game_spread | 0.182 | 0.125 | 0.135 | 13 | 88 | yes | +0.044 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM2 | game_spread | 0.459 | 0.525 | 0.512 | 53 | 48 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN4 | team_total | 0.348 | 0.270 | 0.285 | 29 | 75 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI3 | team_total | 0.520 | 0.450 | 0.464 | 46 | 56 | yes | +0.043 | OK |
| KXNHLTOTAL-26SEP29VANEDM-7 | game_total | 0.568 | 0.505 | 0.518 | 51 | 50 | yes | +0.040 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL2 | game_spread | 0.344 | 0.285 | 0.296 | 29 | 72 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN5 | team_total | 0.186 | 0.125 | 0.136 | 14 | 89 | yes | +0.038 | OK |
| KXNHLSPREAD-26SEP29FLACAR-FLA3 | game_spread | 0.103 | 0.155 | 0.143 | 16 | 85 | no | +0.038 | OK |
| KXNHLSPREAD-26SEP29VANEDM-EDM3 | game_spread | 0.326 | 0.385 | 0.373 | 39 | 62 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-CAR2 | team_total | 0.902 | 0.840 | 0.855 | 86 | 18 | yes | +0.034 | OK |
| KXNHLSPREAD-26SEP29VANEDM-VAN3 | game_spread | 0.108 | 0.065 | 0.072 | 7 | 94 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI4 | team_total | 0.307 | 0.250 | 0.261 | 26 | 76 | yes | +0.033 | OK |
| KXNHLTOTAL-26SEP29VANEDM-9 | game_total | 0.274 | 0.220 | 0.230 | 23 | 79 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL6 | team_total | 0.158 | 0.105 | 0.114 | 12 | 91 | yes | +0.031 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-5 | game_total | 0.841 | 0.790 | 0.801 | 80 | 22 | yes | +0.030 | OK |
| KXNHLTOTAL-26SEP29VANEDM-8 | game_total | 0.375 | 0.315 | 0.327 | 33 | 70 | yes | +0.029 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK2 | game_spread | 0.423 | 0.475 | 0.465 | 48 | 53 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN2 | team_total | 0.782 | 0.720 | 0.733 | 74 | 30 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI5 | team_total | 0.155 | 0.105 | 0.114 | 12 | 91 | yes | +0.028 | OK |
| KXNHLTOTAL-26SEP29FLACAR-5 | game_total | 0.839 | 0.795 | 0.804 | 80 | 21 | yes | +0.028 | OK |
| KXNHLTOTAL-26SEP29FLACAR-10 | game_total | 0.134 | 0.085 | 0.093 | 10 | 93 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL3 | team_total | 0.693 | 0.630 | 0.643 | 65 | 39 | yes | +0.027 | OK |
| KXNHLSPREAD-26SEP29MTLTOR-MTL3 | game_spread | 0.226 | 0.185 | 0.193 | 19 | 82 | yes | +0.026 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-BOS3 | game_spread | 0.215 | 0.175 | 0.183 | 18 | 83 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA3 | team_total | 0.548 | 0.595 | 0.586 | 60 | 41 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS4 | team_total | 0.421 | 0.370 | 0.380 | 38 | 64 | yes | +0.024 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-10 | game_total | 0.141 | 0.090 | 0.099 | 11 | 93 | yes | +0.024 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-VGK3 | game_spread | 0.292 | 0.340 | 0.330 | 35 | 67 | no | +0.022 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-8 | game_total | 0.264 | 0.225 | 0.233 | 23 | 78 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26SEP29CHIVGK-CHI2 | team_total | 0.746 | 0.695 | 0.706 | 71 | 32 | yes | +0.021 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-8 | game_total | 0.284 | 0.240 | 0.248 | 25 | 77 | yes | +0.021 | OK |
| KXNHLTOTAL-26SEP29VANEDM-10 | game_total | 0.148 | 0.110 | 0.117 | 12 | 90 | yes | +0.020 | OK |
| KXNHLGAME-26SEP29NYRBOS-NYR | game_winner | 0.462 | 0.505 | 0.496 | 51 | 50 | no | +0.020 | OK |
| KXNHLGAME-26SEP29NYRBOS-BOS | game_winner | 0.538 | 0.495 | 0.504 | 50 | 51 | yes | +0.020 | OK |
| KXNHLTOTAL-26SEP29VANEDM-6 | game_total | 0.675 | 0.635 | 0.643 | 64 | 37 | yes | +0.019 | OK |
| KXNHLTOTAL-26SEP29FLACAR-4 | game_total | 0.906 | 0.865 | 0.874 | 88 | 15 | yes | +0.019 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-9 | game_total | 0.198 | 0.160 | 0.167 | 17 | 85 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS3 | team_total | 0.633 | 0.595 | 0.603 | 60 | 41 | yes | +0.016 | OK |
| KXNHLSPREAD-26SEP29NYRBOS-BOS2 | game_spread | 0.331 | 0.295 | 0.302 | 30 | 71 | yes | +0.016 | OK |
| KXNHLTOTAL-26SEP29NYRBOS-9 | game_total | 0.185 | 0.155 | 0.161 | 16 | 85 | yes | +0.016 | OK |
| KXNHLSPREAD-26SEP29CHIVGK-CHI3 | game_spread | 0.111 | 0.080 | 0.086 | 9 | 93 | yes | +0.016 | OK |
| KXNHLGAME-26SEP29MTLTOR-TOR | game_winner | 0.457 | 0.495 | 0.487 | 50 | 51 | no | +0.015 | OK |
| KXNHLGAME-26SEP29MTLTOR-MTL | game_winner | 0.543 | 0.505 | 0.513 | 51 | 50 | yes | +0.015 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-7 | game_total | 0.471 | 0.435 | 0.442 | 44 | 57 | yes | +0.014 | OK |
| KXNHLTOTAL-26SEP29VANEDM-5 | game_total | 0.852 | 0.815 | 0.823 | 83 | 20 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26SEP29MTLTOR-MTL2 | team_total | 0.861 | 0.825 | 0.833 | 84 | 19 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP29FLACAR-FLA2 | team_total | 0.767 | 0.805 | 0.798 | 82 | 21 | no | +0.011 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-4 | game_total | 0.906 | 0.870 | 0.878 | 89 | 15 | yes | +0.009 | OK |
| KXNHLTOTAL-26SEP29FLACAR-3 | game_total | 0.981 | 0.955 | 0.962 | 97 | 6 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-VAN6 | team_total | 0.083 | 0.055 | 0.060 | 7 | 96 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26SEP29VANEDM-EDM5 | team_total | 0.385 | 0.425 | 0.417 | 44 | 59 | no | +0.008 | OK |
| KXNHLTOTAL-26SEP29MTLTOR-3 | game_total | 0.980 | 0.965 | 0.969 | 97 | 4 | yes | +0.008 | OK |
| KXNHLTOTAL-26SEP29CHIVGK-6 | game_total | 0.583 | 0.555 | 0.561 | 56 | 45 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-NYR4 | team_total | 0.368 | 0.395 | 0.390 | 40 | 61 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26SEP29NYRBOS-BOS5 | team_total | 0.236 | 0.205 | 0.211 | 22 | 81 | yes | +0.004 | OK |

_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
