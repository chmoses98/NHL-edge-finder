# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T15:17:57Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4036 · contracts joined: 2384 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2109, 'OK': 125, 'NO_EDGE': 150}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 313, 'game_early_goal': 11, 'first_goal': 396, 'game_winner': 22, 'player_goals': 690, 'game_overtime': 11, 'player_points': 424, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-6h | 0.534 | 0.466 | 0.171 | 6.39 | 3.31 | 3.08 | 214 (25/189) | PROJECTED/PROJECTED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-6h | 0.507 | 0.493 | 0.185 | 6.08 | 3.06 | 3.02 | 213 (25/188) | PROJECTED/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-6h | 0.749 | 0.251 | 0.140 | 6.33 | 4.00 | 2.33 | 210 (25/185) | PROJECTED/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-6h | 0.560 | 0.440 | 0.180 | 5.97 | 3.17 | 2.80 | 223 (25/198) | PROJECTED/PROJECTED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-6h | 0.449 | 0.551 | 0.180 | 6.03 | 2.86 | 3.16 | 215 (25/190) | PROJECTED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-6h | 0.617 | 0.384 | 0.169 | 6.00 | 3.36 | 2.64 | 225 (25/200) | PROJECTED/PROJECTED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-6h | 0.464 | 0.536 | 0.170 | 6.47 | 3.10 | 3.37 | 222 (25/197) | PROJECTED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-6h | 0.458 | 0.542 | 0.177 | 5.98 | 2.85 | 3.13 | 202 (25/177) | PROJECTED/PROJECTED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-6h | 0.592 | 0.408 | 0.171 | 6.43 | 3.52 | 2.91 | 213 (25/188) | PROJECTED/PROJECTED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-6h | 0.608 | 0.392 | 0.162 | 7.02 | 3.87 | 3.15 | 231 (25/206) | PROJECTED/PROJECTED |
| NSH @ COL | 2026-11-06T02:30:00Z | T-6h | 0.652 | 0.348 | 0.160 | 6.61 | 3.80 | 2.81 | 216 (25/191) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV05STLNJ-STL | game_winner | 0.440 | 0.345 | 0.363 | 35 | 66 | yes | +0.074 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ3 | game_spread | 0.200 | 0.285 | 0.266 | 29 | 72 | no | +0.066 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.449 | 0.365 | 0.381 | 37 | 64 | yes | +0.062 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.158 | 0.235 | 0.218 | 24 | 77 | no | +0.060 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.493 | 0.575 | 0.559 | 58 | 43 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.270 | 0.345 | 0.329 | 35 | 66 | no | +0.055 | OK |
| KXNHLSPREAD-26NOV05STLNJ-NJ2 | game_spread | 0.330 | 0.410 | 0.393 | 42 | 60 | no | +0.054 | OK |
| KXNHLGAME-26NOV05STLNJ-NJ | game_winner | 0.560 | 0.635 | 0.620 | 64 | 37 | no | +0.053 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.551 | 0.625 | 0.611 | 63 | 38 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.195 | 0.265 | 0.250 | 27 | 74 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.402 | 0.480 | 0.464 | 49 | 53 | no | +0.050 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.507 | 0.435 | 0.449 | 44 | 57 | yes | +0.050 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.385 | 0.455 | 0.441 | 46 | 55 | no | +0.048 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.534 | 0.465 | 0.479 | 47 | 54 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.620 | 0.690 | 0.676 | 70 | 32 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.261 | 0.325 | 0.312 | 33 | 68 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 | team_total | 0.550 | 0.485 | 0.498 | 49 | 52 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL2 | game_spread | 0.233 | 0.175 | 0.186 | 18 | 83 | yes | +0.042 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.592 | 0.655 | 0.643 | 66 | 35 | no | +0.042 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.408 | 0.345 | 0.357 | 35 | 66 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.401 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.216 | 0.275 | 0.262 | 28 | 73 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.323 | 0.390 | 0.376 | 40 | 62 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.245 | 0.305 | 0.292 | 31 | 70 | no | +0.040 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.466 | 0.525 | 0.513 | 53 | 48 | no | +0.036 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.154 | 0.205 | 0.194 | 21 | 80 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.379 | 0.445 | 0.432 | 46 | 57 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ2 | team_total | 0.818 | 0.870 | 0.861 | 88 | 14 | no | +0.033 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.317 | 0.265 | 0.275 | 27 | 74 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.370 | 0.430 | 0.418 | 44 | 58 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.583 | 0.635 | 0.625 | 64 | 37 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.373 | 0.435 | 0.422 | 45 | 58 | no | +0.030 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.251 | 0.205 | 0.214 | 21 | 80 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV05CARNYI-NYI2 | game_spread | 0.240 | 0.195 | 0.204 | 20 | 81 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.281 | 0.235 | 0.244 | 24 | 77 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.376 | 0.425 | 0.415 | 43 | 58 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.536 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.216 | 0.170 | 0.179 | 18 | 84 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.602 | 0.550 | 0.561 | 56 | 46 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.620 | 0.670 | 0.660 | 68 | 34 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA5 | team_total | 0.203 | 0.250 | 0.240 | 26 | 76 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA3 | team_total | 0.599 | 0.650 | 0.640 | 66 | 36 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5 | team_total | 0.171 | 0.130 | 0.137 | 14 | 88 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.820 | 0.865 | 0.857 | 88 | 15 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.582 | 0.635 | 0.625 | 65 | 38 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.179 | 0.140 | 0.147 | 15 | 87 | yes | +0.020 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL3 | game_spread | 0.200 | 0.165 | 0.172 | 17 | 84 | yes | +0.020 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.617 | 0.575 | 0.583 | 58 | 43 | yes | +0.019 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.384 | 0.425 | 0.417 | 43 | 58 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.749 | 0.785 | 0.778 | 79 | 22 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.151 | 0.190 | 0.182 | 20 | 82 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.374 | 0.330 | 0.339 | 34 | 68 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.156 | 0.120 | 0.127 | 13 | 89 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN4 | team_total | 0.342 | 0.300 | 0.308 | 31 | 71 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-MTL4 | team_total | 0.434 | 0.395 | 0.403 | 40 | 61 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN3 | game_spread | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV05STLNJ-STL3 | game_spread | 0.132 | 0.105 | 0.110 | 11 | 90 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.911 | 0.940 | 0.935 | 95 | 7 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG2 | team_total | 0.859 | 0.890 | 0.884 | 90 | 12 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA2 | team_total | 0.806 | 0.845 | 0.838 | 86 | 17 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.328 | 0.295 | 0.301 | 30 | 71 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.786 | 0.815 | 0.809 | 82 | 19 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-MTL6 | team_total | 0.119 | 0.095 | 0.100 | 10 | 91 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 | team_total | 0.390 | 0.435 | 0.426 | 45 | 58 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.214 | 0.250 | 0.242 | 26 | 76 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5 | team_total | 0.224 | 0.190 | 0.196 | 20 | 82 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.591 | 0.625 | 0.618 | 63 | 38 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL4 | team_total | 0.317 | 0.280 | 0.287 | 29 | 73 | yes | +0.012 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI2 | game_spread | 0.196 | 0.225 | 0.219 | 23 | 78 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL6 | team_total | 0.065 | 0.045 | 0.048 | 5 | 96 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.206 | 0.240 | 0.233 | 25 | 77 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4 | team_total | 0.481 | 0.525 | 0.516 | 54 | 49 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.778 | 0.815 | 0.808 | 83 | 20 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.799 | 0.840 | 0.832 | 86 | 18 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.256 | 0.285 | 0.279 | 29 | 72 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 | team_total | 0.335 | 0.300 | 0.307 | 31 | 71 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT3 | team_total | 0.604 | 0.635 | 0.629 | 64 | 37 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG5 | team_total | 0.286 | 0.320 | 0.313 | 33 | 69 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV05CHITB-9 | game_total | 0.189 | 0.215 | 0.210 | 22 | 79 | no | +0.009 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.534 | 0.515 | 0.171 | 0.215 | 6.39 | 6.61 | 0.976/0.998 | KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 +0.048 |
| VGK @ DET | 0.507 | 0.453 | 0.185 | 0.219 | 6.08 | 6.28 | 1.015/1.004 | KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 +0.070 |
| CHI @ TBL | 0.749 | 0.718 | 0.140 | 0.189 | 6.33 | 6.39 | 0.958/1.026 | KXNHLTEAMTOTAL-26NOV05CHITB-CHI3 +0.043 |
| STL @ NJD | 0.560 | 0.549 | 0.180 | 0.220 | 5.97 | 6.23 | 0.974/0.993 | KXNHLTOTAL-26NOV05STLNJ-7 +0.053 |
| CAR @ NYI | 0.449 | 0.489 | 0.180 | 0.227 | 6.03 | 6.34 | 0.957/0.990 | KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 +0.062 |
| PHI @ NYR | 0.617 | 0.539 | 0.169 | 0.225 | 6.00 | 5.98 | 0.987/0.992 | KXNHLGAME-26NOV05PHINYR-NYR -0.078 |
| BOS @ PIT | 0.464 | 0.518 | 0.170 | 0.220 | 6.47 | 6.69 | 1.033/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.068 |
| DAL @ CBJ | 0.458 | 0.523 | 0.177 | 0.214 | 5.98 | 6.12 | 0.990/0.987 | KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ4 +0.069 |
| VAN @ WPG | 0.592 | 0.546 | 0.171 | 0.215 | 6.43 | 6.33 | 1.002/1.026 | KXNHLSPREAD-26NOV05VANWPG-WPG2 -0.052 |
| ANA @ EDM | 0.608 | 0.581 | 0.162 | 0.200 | 7.02 | 7.28 | 1.010/1.016 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA4 +0.047 |
| NSH @ COL | 0.652 | 0.661 | 0.160 | 0.204 | 6.61 | 6.65 | 0.977/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.021 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Lawson Crouse: 1+ goals YES @ 18c · p 0.2326 (adj 0.217) · $3.57 · thesis UTA:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 18c · p 0.2291 (adj 0.2143) · $2.84 · thesis MTL:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 14c · p 0.1726 (adj 0.1632) · $1.72 · thesis MTL:WINS_BY_2PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.7395 (adj 0.6998) · $6.69 · thesis UTA:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0779 (adj 0.0672) · $1.22 · thesis VGK:OFFENSE_4PLUS
- Ivan Barbashev: 1+ assists YES @ 28c · p 0.3489 (adj 0.312) · $2.23 · thesis VGK:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.2441 (adj 0.2293) · $3.29 · thesis CHI:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 55c · p 0.636 (adj 0.5905) · $3.66 · thesis GAME:TIGHT
- Victor Hedman: 1+ goals NO @ 90c · p 0.9259 (adj 0.9169) · $8.24 · thesis DIFFUSE
- Nikita Kucherov: 2+ assists NO @ 72c · p 0.7942 (adj 0.7496) · $5.23 · thesis TBL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 60c · p 0.6608 (adj 0.6443) · $7.01 · thesis NJD:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 22c · p 0.2698 (adj 0.2549) · $2.74 · thesis STL:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 72c · p 0.7892 (adj 0.7521) · $4.01 · thesis STL:WINS
- Dylan Holloway: 1+ goals YES @ 23c · p 0.2721 (adj 0.2591) · $2.03 · thesis STL:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 12c · p 0.1582 (adj 0.1449) · $1.87 · thesis NYI:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 21c · p 0.2567 (adj 0.2425) · $2.65 · thesis NYI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7348 (adj 0.7174) · $7.68 · thesis CAR:SUPPRESSED
- Victor Eklund: 1+ goals YES @ 16c · p 0.1991 (adj 0.1868) · $2.04 · thesis NYI:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 68c · p 0.7477 (adj 0.7114) · $5.89 · thesis PHI:SUPPRESSED
- Tye Kartye: 1+ assists YES @ 24c · p 0.3014 (adj 0.2657) · $1.65 · thesis NYR:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1887 (adj 0.1703) · $4.52 · thesis PIT:WINS_BY_2PLUS
- Rickard Rakell: 1+ goals YES @ 33c · p 0.3909 (adj 0.3719) · $4.02 · thesis PIT:OFFENSE_4PLUS
- Hendrix Lapierre: 1+ goals YES @ 12c · p 0.1525 (adj 0.1419) · $1.67 · thesis PIT:OFFENSE_4PLUS
- Ben Kindel: 1+ assists NO @ 69c · p 0.7601 (adj 0.7226) · $8.24 · thesis PIT:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2853 (adj 0.2702) · $3.67 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2134 (adj 0.1988) · $2.23 · thesis CBJ:OFFENSE_4PLUS
- Esa Lindell: 1+ goals NO @ 92c · p 0.9504 (adj 0.9378) · $8.24 · thesis DAL:SUPPRESSED
- Damon Severson: 1+ goals YES @ 8c · p 0.1105 (adj 0.0979) · $1.3 · thesis CBJ:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 15c · p 0.2151 (adj 0.1938) · $3.86 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2293 (adj 0.212) · $3.77 · thesis VAN:OFFENSE_4PLUS
- Nino Niederreiter: 1+ goals NO @ 84c · p 0.8868 (adj 0.8726) · $8.24 · thesis WPG:SUPPRESSED
- Brendan Gallagher: 1+ goals YES @ 12c · p 0.1574 (adj 0.1468) · $2.14 · thesis VAN:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1266 (adj 0.1137) · $1.8 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.2019 (adj 0.1902) · $2.43 · thesis ANA:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 14c · p 0.1765 (adj 0.1649) · $1.92 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 68c · p 0.7614 (adj 0.7157) · $7.62 · thesis EDM:SUPPRESSED
- Nathan MacKinnon: 1+ assists NO @ 39c · p 0.4689 (adj 0.4269) · $3.4 · thesis COL:SUPPRESSED
- Mavrik Bourque: 1+ assists NO @ 70c · p 0.7923 (adj 0.7258) · $4.65 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 162/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.98, exp saves 25.03 (sd 6.89), pull risk 0.067
- UTA net: Sebastian Cossa (PROJECTED) exp shots 25.81, exp saves 22.17 (sd 6.38), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Logan Cooley: 1+ points | 0.522 | 0.605 | 62/41 | +0.051 | STANDARD |
| Mikhail Sergachev: 2+ points | 0.155 | 0.235 | 25/78 | +0.053 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.261 | 0.340 | 35/67 | +0.054 | STANDARD |
| Vincent Trocheck: 1+ points | 0.408 | 0.485 | 49/52 | +0.054 | STANDARD |
| Noah Dobson: 1+ assists | 0.390 | 0.315 | 32/69 | +0.055 | STANDARD |
| Chris Kreider: 1+ points | 0.425 | 0.350 | 36/66 | +0.049 | STANDARD |

**VGK @ DET** · priced 156/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROJECTED) exp shots 26.45, exp saves 22.65 (sd 6.47), pull risk 0.072
- VGK net: Carter Hart (PROJECTED) exp shots 27.41, exp saves 23.73 (sd 6.53), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.418 | 0.515 | 52/49 | +0.075 | STANDARD |
| Lucas Raymond: 1+ assists | 0.348 | 0.425 | 44/59 | +0.045 | STANDARD |
| Jack Eichel: 1+ assists | 0.443 | 0.520 | 53/49 | +0.049 | STANDARD |
| Mitch Marner: 1+ points | 0.560 | 0.635 | 65/38 | +0.043 | STANDARD |
| Ivan Barbashev: 1+ assists | 0.349 | 0.275 | 28/73 | +0.055 | STANDARD |
| Ivan Barbashev: 1+ points | 0.492 | 0.425 | 43/58 | +0.045 | STANDARD |

**CHI @ TBL** · priced 148/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.1, exp saves 20.67 (sd 5.73), pull risk 0.041
- CHI net: Arvid Soderblom (PROJECTED) exp shots 30.41, exp saves 25.28 (sd 7.26), pull risk 0.104

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 2+ points | 0.395 | 0.485 | 50/53 | +0.058 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.206 | 0.295 | 31/72 | +0.060 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.583 | 0.660 | 67/35 | +0.052 | STANDARD |
| Nikita Kucherov: 3+ points | 0.155 | 0.220 | 23/79 | +0.044 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.446 | 0.385 | 40/63 | +0.029 | STANDARD |
| Connor Bedard: 2+ points | 0.195 | 0.255 | 27/76 | +0.032 | STANDARD |

**STL @ NJD** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.87, exp saves 21.61 (sd 6.05), pull risk 0.048
- STL net: Joel Hofer (PROJECTED) exp shots 30.21, exp saves 25.96 (sd 7.12), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.241 | 0.365 | 37/64 | +0.103 | STANDARD |
| Luke Evangelista: 1+ assists | 0.247 | 0.365 | 37/64 | +0.097 | STANDARD |
| Jack Hughes: 1+ assists | 0.414 | 0.525 | 53/48 | +0.089 | STANDARD |
| Jack Hughes: 1+ points | 0.616 | 0.725 | 74/29 | +0.079 | STANDARD |
| Luke Evangelista: 1+ points | 0.402 | 0.495 | 50/51 | +0.071 | STANDARD |
| Jesper Bratt: 1+ assists | 0.400 | 0.480 | 49/53 | +0.053 | STANDARD |

**CAR @ NYI** · priced 161/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 29.43, exp saves 25.33 (sd 6.81), pull risk 0.063
- CAR net: Brandon Bussi (PROJECTED) exp shots 24.49, exp saves 21.13 (sd 6.06), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.501 | 0.610 | 62/40 | +0.082 | STANDARD |
| Sebastian Aho: 1+ assists | 0.323 | 0.430 | 44/58 | +0.080 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.485 | 0.570 | 58/44 | +0.058 | STANDARD |
| Sebastian Aho: 2+ points | 0.155 | 0.240 | 26/78 | +0.053 | STANDARD |
| Seth Jarvis: 1+ assists | 0.280 | 0.360 | 37/65 | +0.054 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.312 | 0.390 | 40/62 | +0.052 | STANDARD |

**PHI @ NYR** · priced 173/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 25.8, exp saves 22.54 (sd 6.17), pull risk 0.05
- PHI net: Joseph Woll (PROJECTED) exp shots 26.19, exp saves 22.64 (sd 6.26), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ points | 0.418 | 0.495 | 51/52 | +0.045 | STANDARD |
| Travis Konecny: 1+ assists | 0.252 | 0.325 | 33/68 | +0.052 | STANDARD |
| Tye Kartye: 1+ assists | 0.301 | 0.230 | 24/78 | +0.049 | STANDARD |
| Christian Dvorak: 1+ points | 0.451 | 0.385 | 40/63 | +0.034 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.476 | 0.540 | 55/47 | +0.037 | STANDARD |
| Tye Kartye: 1+ points | 0.435 | 0.380 | 39/63 | +0.028 | STANDARD |

**BOS @ PIT** · priced 163/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.87, exp saves 22.2 (sd 6.33), pull risk 0.071
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.09 (sd 6.88), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 1+ assists | 0.462 | 0.545 | 55/46 | +0.061 | STANDARD |
| David Pastrnak: 1+ points | 0.645 | 0.725 | 74/29 | +0.051 | STANDARD |
| David Pastrnak: 2+ points | 0.277 | 0.355 | 36/65 | +0.057 | STANDARD |
| Rickard Rakell: 1+ goals | 0.391 | 0.315 | 33/70 | +0.045 | STANDARD |
| Ben Kindel: 1+ assists | 0.240 | 0.315 | 32/69 | +0.055 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.400 | 0.475 | 48/53 | +0.052 | STANDARD |

**DAL @ CBJ** · priced 147/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (PROJECTED) exp shots 25.44, exp saves 22.13 (sd 6.13), pull risk 0.055
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.62, exp saves 22.08 (sd 6.26), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ points | 0.566 | 0.495 | 52/53 | +0.028 | STANDARD |
| Charlie Coyle: 2+ points | 0.209 | 0.140 | 17/89 | +0.029 | STANDARD |
| Charlie Coyle: 1+ goals | 0.285 | 0.225 | 23/78 | +0.043 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.213 | 0.155 | 17/86 | +0.034 | STANDARD |
| Cole Sillinger: 1+ goals | 0.177 | 0.120 | 15/91 | +0.018 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.436 | 0.490 | 51/53 | +0.017 | STANDARD |

**VAN @ WPG** · priced 155/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 24.76, exp saves 21.52 (sd 6.11), pull risk 0.057
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.31, exp saves 25.02 (sd 6.89), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#25): 1+ goals | 0.060 | 0.265 | 52/99 | -0.051 | STANDARD |
| Kyle Connor: 1+ assists | 0.434 | 0.525 | 54/49 | +0.059 | STANDARD |
| Neal Pionk: 1+ points | 0.460 | 0.550 | 56/46 | +0.063 | STANDARD |
| Marco Rossi: 1+ goals | 0.215 | 0.130 | 15/89 | +0.056 | STANDARD |
| Kyle Connor: 2+ points | 0.307 | 0.390 | 40/62 | +0.057 | STANDARD |
| Elias Pettersson (#40): 1+ goals | 0.237 | 0.160 | 31/99 | -0.088 | STANDARD |

**ANA @ EDM** · priced 179/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.9, exp saves 24.11 (sd 6.81), pull risk 0.079
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.83, exp saves 23.49 (sd 6.9), pull risk 0.103

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.383 | 0.530 | 54/48 | +0.119 | STANDARD |
| Leon Draisaitl: 3+ points | 0.150 | 0.280 | 30/74 | +0.097 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.510 | 0.630 | 64/38 | +0.093 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.157 | 0.270 | 29/75 | +0.080 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.373 | 0.265 | 28/75 | +0.079 | STANDARD |
| Connor McDavid: 1+ assists | 0.603 | 0.705 | 71/30 | +0.083 | STANDARD |

**NSH @ COL** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 25.73, exp saves 22.66 (sd 6.18), pull risk 0.047
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.24 (sd 7.61), pull risk 0.096

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.208 | 0.310 | 32/70 | +0.078 | STANDARD |
| Mavrik Bourque: 1+ points | 0.352 | 0.440 | 45/57 | +0.061 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.531 | 0.615 | 62/39 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.240 | 26/78 | +0.035 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.383 | 0.450 | 46/56 | +0.040 | STANDARD |
| Cale Makar: 1+ assists | 0.504 | 0.570 | 58/44 | +0.039 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
