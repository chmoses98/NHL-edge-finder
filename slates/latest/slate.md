# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T23:40:13Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4238 · contracts joined: 2437 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2162, 'OK': 139, 'NO_EDGE': 136}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 328, 'game_early_goal': 11, 'first_goal': 393, 'game_winner': 22, 'player_goals': 682, 'game_overtime': 11, 'player_points': 454, 'goalie_saves': 19, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-10m | 0.519 | 0.481 | 0.170 | 6.55 | 3.35 | 3.20 | 223 (25/198) | CONFIRMED/CONFIRMED |
| VGK @ DET | 2026-11-06T00:00:00Z | T-10m | 0.516 | 0.484 | 0.176 | 6.07 | 3.09 | 2.99 | 219 (25/194) | CONFIRMED/CONFIRMED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-10m | 0.761 | 0.239 | 0.140 | 6.33 | 4.06 | 2.27 | 212 (25/187) | CONFIRMED/CONFIRMED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-10m | 0.663 | 0.337 | 0.161 | 6.58 | 3.82 | 2.77 | 223 (25/198) | CONFIRMED/CONFIRMED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-10m | 0.449 | 0.551 | 0.179 | 6.06 | 2.87 | 3.19 | 217 (25/192) | CONFIRMED/CONFIRMED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-10m | 0.629 | 0.371 | 0.175 | 5.99 | 3.39 | 2.61 | 229 (25/204) | CONFIRMED/CONFIRMED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-10m | 0.466 | 0.534 | 0.168 | 6.63 | 3.21 | 3.42 | 239 (25/214) | CONFIRMED/CONFIRMED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-10m | 0.433 | 0.567 | 0.181 | 5.99 | 2.80 | 3.19 | 207 (25/182) | CONFIRMED/CONFIRMED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-10m | 0.620 | 0.381 | 0.167 | 6.51 | 3.64 | 2.87 | 209 (25/184) | CONFIRMED/CONFIRMED |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-60m | 0.642 | 0.358 | 0.156 | 6.99 | 4.00 | 3.00 | 236 (25/211) | CONFIRMED/PROBABLE |
| NSH @ COL | 2026-11-06T02:30:00Z | T-90m | 0.654 | 0.346 | 0.161 | 6.59 | 3.80 | 2.79 | 223 (25/198) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.551 | 0.645 | 0.627 | 65 | 36 | no | +0.073 | OK |
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.449 | 0.355 | 0.373 | 36 | 65 | yes | +0.073 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.324 | 0.415 | 0.396 | 42 | 59 | no | +0.070 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.516 | 0.425 | 0.443 | 43 | 58 | yes | +0.069 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.484 | 0.575 | 0.557 | 58 | 43 | no | +0.069 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.270 | 0.355 | 0.337 | 36 | 65 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV05STLNJ-8 | game_total | 0.315 | 0.235 | 0.250 | 24 | 77 | yes | +0.062 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.156 | 0.235 | 0.217 | 24 | 77 | no | +0.062 | OK |
| KXNHLTOTAL-26NOV05STLNJ-7 | game_total | 0.509 | 0.425 | 0.442 | 43 | 58 | yes | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.595 | 0.675 | 0.660 | 68 | 33 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.196 | 0.280 | 0.262 | 29 | 73 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.405 | 0.485 | 0.469 | 49 | 52 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.386 | 0.465 | 0.449 | 47 | 54 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV05STLNJ-6 | game_total | 0.623 | 0.545 | 0.561 | 55 | 46 | yes | +0.055 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.297 | 0.225 | 0.238 | 23 | 78 | yes | +0.054 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.404 | 0.475 | 0.461 | 48 | 53 | no | +0.048 | OK |
| KXNHLTOTAL-26NOV05STLNJ-9 | game_total | 0.228 | 0.160 | 0.172 | 17 | 85 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ6 | team_total | 0.183 | 0.125 | 0.135 | 13 | 88 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.362 | 0.430 | 0.416 | 44 | 58 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.624 | 0.695 | 0.681 | 71 | 32 | no | +0.041 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.239 | 0.185 | 0.195 | 19 | 82 | yes | +0.039 | OK |
| KXNHLGAME-26NOV05BOSPIT-BOS | game_winner | 0.534 | 0.475 | 0.487 | 48 | 53 | yes | +0.037 | OK |
| KXNHLGAME-26NOV05BOSPIT-PIT | game_winner | 0.466 | 0.525 | 0.513 | 53 | 48 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.795 | 0.850 | 0.840 | 86 | 16 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL3 | team_total | 0.523 | 0.460 | 0.473 | 47 | 55 | yes | +0.036 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.558 | 0.615 | 0.604 | 62 | 39 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL4 | team_total | 0.308 | 0.255 | 0.265 | 26 | 75 | yes | +0.034 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.629 | 0.575 | 0.586 | 58 | 43 | yes | +0.032 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.519 | 0.465 | 0.476 | 47 | 54 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV05CARNYI-NYI2 | game_spread | 0.243 | 0.195 | 0.204 | 20 | 81 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.345 | 0.290 | 0.301 | 30 | 72 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV05STLNJ-10 | game_total | 0.115 | 0.070 | 0.078 | 8 | 94 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.607 | 0.550 | 0.561 | 56 | 46 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.822 | 0.870 | 0.861 | 88 | 14 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.266 | 0.315 | 0.305 | 32 | 69 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.218 | 0.270 | 0.259 | 28 | 74 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.313 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.464 | 0.515 | 0.505 | 52 | 49 | no | +0.029 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.761 | 0.805 | 0.797 | 81 | 20 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 | team_total | 0.555 | 0.505 | 0.515 | 51 | 50 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.577 | 0.635 | 0.624 | 65 | 38 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.320 | 0.275 | 0.284 | 28 | 73 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI2 | game_spread | 0.183 | 0.225 | 0.216 | 23 | 78 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI3 | team_total | 0.487 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.381 | 0.335 | 0.344 | 34 | 67 | yes | +0.025 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.620 | 0.665 | 0.656 | 67 | 34 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.408 | 0.460 | 0.449 | 47 | 55 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET5 | team_total | 0.205 | 0.155 | 0.164 | 17 | 86 | yes | +0.025 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.098 | 0.135 | 0.127 | 14 | 87 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.380 | 0.330 | 0.340 | 34 | 68 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV05STLNJ-5 | game_total | 0.816 | 0.770 | 0.780 | 78 | 24 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-BOS4 | team_total | 0.461 | 0.415 | 0.424 | 42 | 59 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5 | team_total | 0.172 | 0.130 | 0.138 | 14 | 88 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.151 | 0.110 | 0.117 | 12 | 90 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.172 | 0.130 | 0.138 | 14 | 88 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.272 | 0.320 | 0.310 | 33 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.591 | 0.635 | 0.626 | 64 | 37 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL6 | team_total | 0.065 | 0.035 | 0.040 | 4 | 97 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI4 | team_total | 0.273 | 0.320 | 0.310 | 33 | 69 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 | team_total | 0.337 | 0.295 | 0.303 | 30 | 71 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.788 | 0.830 | 0.822 | 84 | 18 | no | +0.022 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.481 | 0.525 | 0.516 | 53 | 48 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.265 | 0.310 | 0.301 | 32 | 70 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.789 | 0.825 | 0.818 | 83 | 18 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL2 | team_total | 0.755 | 0.715 | 0.723 | 72 | 29 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK5 | team_total | 0.188 | 0.230 | 0.221 | 24 | 78 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV05STLNJ-4 | game_total | 0.888 | 0.855 | 0.862 | 86 | 15 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3 | team_total | 0.547 | 0.505 | 0.513 | 51 | 50 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-5 | game_total | 0.853 | 0.885 | 0.879 | 89 | 12 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2 | team_total | 0.771 | 0.730 | 0.739 | 74 | 28 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6 | team_total | 0.071 | 0.040 | 0.045 | 5 | 97 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.545 | 0.505 | 0.513 | 51 | 50 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET2 | team_total | 0.810 | 0.770 | 0.778 | 78 | 24 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET3 | game_spread | 0.176 | 0.140 | 0.147 | 15 | 87 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV05PHINYR-NYR2 | game_spread | 0.393 | 0.355 | 0.362 | 36 | 65 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-BOS6 | team_total | 0.133 | 0.100 | 0.106 | 11 | 91 | yes | +0.016 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.519 | 0.529 | 0.170 | 0.215 | 6.55 | 6.53 | 0.943/1.001 | KXNHLTOTAL-26NOV05UTAMTL-8 -0.011 |
| VGK @ DET | 0.516 | 0.450 | 0.176 | 0.217 | 6.07 | 6.30 | 1.024/1.003 | KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 +0.075 |
| CHI @ TBL | 0.761 | 0.727 | 0.140 | 0.185 | 6.33 | 6.41 | 0.947/1.042 | KXNHLTEAMTOTAL-26NOV05CHITB-CHI3 +0.050 |
| STL @ NJD | 0.663 | 0.577 | 0.161 | 0.217 | 6.58 | 6.28 | 0.950/1.032 | KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 -0.091 |
| CAR @ NYI | 0.449 | 0.474 | 0.179 | 0.221 | 6.06 | 6.39 | 0.978/0.984 | KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 +0.057 |
| PHI @ NYR | 0.629 | 0.540 | 0.175 | 0.224 | 5.99 | 5.98 | 0.988/0.991 | KXNHLGAME-26NOV05PHINYR-NYR -0.090 |
| BOS @ PIT | 0.466 | 0.531 | 0.168 | 0.215 | 6.63 | 6.80 | 1.042/0.999 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.068 |
| DAL @ CBJ | 0.433 | 0.509 | 0.181 | 0.223 | 5.99 | 6.13 | 1.008/0.969 | KXNHLGAME-26NOV05DALCBJ-DAL -0.076 |
| VAN @ WPG | 0.620 | 0.552 | 0.167 | 0.218 | 6.51 | 6.35 | 1.004/1.034 | KXNHLSPREAD-26NOV05VANWPG-WPG2 -0.076 |
| ANA @ EDM | 0.642 | 0.572 | 0.156 | 0.200 | 6.99 | 7.11 | 0.999/0.976 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3 +0.073 |
| NSH @ COL | 0.654 | 0.655 | 0.161 | 0.199 | 6.59 | 6.65 | 0.979/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Jake Evans: 1+ goals YES @ 12c · p 0.163 (adj 0.151) · $2.64 · thesis MTL:OFFENSE_4PLUS
- Cole Caufield: 1+ assists YES @ 33c · p 0.4036 (adj 0.3643) · $2.73 · thesis MTL:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 66c · p 0.707 (adj 0.694) · $5.93 · thesis UTA:SUPPRESSED
- Phillip Danault: 1+ goals YES @ 12c · p 0.1503 (adj 0.139) · $1.18 · thesis MTL:WINS_BY_2PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.076 (adj 0.0658) · $1.21 · thesis VGK:OFFENSE_4PLUS
- Justin Faulk: 1+ assists YES @ 25c · p 0.3136 (adj 0.2793) · $2.1 · thesis DET:OFFENSE_4PLUS
- Andrew Copp: 1+ goals YES @ 16c · p 0.1914 (adj 0.181) · $1.5 · thesis DET:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 58c · p 0.6442 (adj 0.6096) · $4.32 · thesis DET:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 18c · p 0.2341 (adj 0.2193) · $3.75 · thesis CHI:OFFENSE_4PLUS
- Tampa Bay over 3.5 goals scored NO @ 33c · p 0.4218 (adj 0.3734) · $5.43 · thesis TBL:SUPPRESSED
- Max Crozier: 1+ goals YES @ 5c · p 0.0751 (adj 0.0663) · $1.46 · thesis TBL:OFFENSE_4PLUS
- Arvid Soderblom: 28+ saves NO @ 53c · p 0.6181 (adj 0.5691) · $6.45 · thesis CHI:NET_LOW_VOLUME
- Robert Thomas: 1+ goals YES @ 19c · p 0.2671 (adj 0.2466) · $5.78 · thesis STL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 58c · p 0.6478 (adj 0.6296) · $8.8 · thesis NJD:SUPPRESSED
- Jimmy Snuggerud: 1+ goals YES @ 25c · p 0.3023 (adj 0.288) · $3.41 · thesis STL:OFFENSE_4PLUS
- Dougie Hamilton: 1+ assists YES @ 29c · p 0.3556 (adj 0.3178) · $2.53 · thesis NJD:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7332 (adj 0.7149) · $8.8 · thesis CAR:SUPPRESSED
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1697 (adj 0.1585) · $2.39 · thesis NYI:OFFENSE_4PLUS
- Anthony Duclair: 1+ goals YES @ 14c · p 0.1801 (adj 0.1688) · $2.43 · thesis NYI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 17c · p 0.2093 (adj 0.1982) · $2.82 · thesis PHI:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 67c · p 0.7434 (adj 0.7017) · $8.76 · thesis PHI:SUPPRESSED
- Travis Sanheim: 1+ assists YES @ 25c · p 0.3058 (adj 0.2754) · $1.56 · thesis PHI:OFFENSE_4PLUS
- Will Cuylle: 1+ goals NO @ 77c · p 0.8033 (adj 0.7925) · $5.31 · thesis NYR:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1887 (adj 0.1703) · $4.67 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1535 (adj 0.1364) · $3.11 · thesis PIT:WINS_BY_2PLUS
- Mark Kastelic: 1+ goals YES @ 9c · p 0.1193 (adj 0.1107) · $1.7 · thesis BOS:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 32c · p 0.3732 (adj 0.3586) · $3.66 · thesis PIT:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 16c · p 0.2104 (adj 0.1966) · $2.3 · thesis CBJ:WINS_BY_2PLUS
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2832 (adj 0.2686) · $3.66 · thesis CBJ:OFFENSE_4PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.1084 (adj 0.0988) · $1.47 · thesis CBJ:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.2204 (adj 0.2016) · $3.79 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2303 (adj 0.2115) · $3.88 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1526 (adj 0.1407) · $2.65 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 14c · p 0.1795 (adj 0.1684) · $2.35 · thesis VAN:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1223 (adj 0.113) · $1.92 · thesis ANA:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 29c · p 0.4096 (adj 0.3286) · $3.4 · thesis EDM:SUPPRESSED
- Sam Colangelo: 1+ goals YES @ 13c · p 0.1664 (adj 0.156) · $2.22 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.1988 (adj 0.1879) · $2.29 · thesis ANA:OFFENSE_4PLUS
- Mavrik Bourque: 1+ assists NO @ 72c · p 0.7959 (adj 0.7554) · $8.8 · thesis NSH:SUPPRESSED
- Adam Wilsby: 1+ goals YES @ 5c · p 0.0697 (adj 0.0635) · $1.1 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1561 (adj 0.1483) · $1.28 · thesis NSH:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ assists NO @ 40c · p 0.4729 (adj 0.4315) · $2.66 · thesis COL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.98, exp saves 25.14 (sd 6.77), pull risk 0.062
- UTA net: Sebastian Cossa (CONFIRMED) exp shots 25.81, exp saves 22.19 (sd 6.32), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ points | 0.386 | 0.475 | 49/54 | +0.056 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.247 | 0.335 | 35/68 | +0.057 | STANDARD |
| Lawson Crouse: 1+ points | 0.419 | 0.335 | 35/68 | +0.053 | STANDARD |
| Logan Cooley: 1+ points | 0.517 | 0.600 | 61/41 | +0.056 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.499 | 0.580 | 59/43 | +0.054 | STANDARD |
| Cole Caufield: 1+ assists | 0.404 | 0.325 | 33/68 | +0.058 | STANDARD |

**VGK @ DET** · priced 159/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 26.45, exp saves 22.65 (sd 6.43), pull risk 0.072
- VGK net: Carter Hart (CONFIRMED) exp shots 27.41, exp saves 23.79 (sd 6.48), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.417 | 0.535 | 55/48 | +0.085 | STANDARD |
| Mitch Marner: 1+ points | 0.550 | 0.645 | 67/38 | +0.053 | STANDARD |
| Jack Eichel: 1+ assists | 0.439 | 0.530 | 54/48 | +0.064 | STANDARD |
| Rasmus Andersson: 1+ assists | 0.304 | 0.220 | 25/81 | +0.041 | STANDARD |
| Ivan Barbashev: 1+ points | 0.501 | 0.425 | 43/58 | +0.054 | STANDARD |
| Lucas Raymond: 1+ assists | 0.356 | 0.425 | 43/58 | +0.047 | STANDARD |

**CHI @ TBL** · priced 150/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (CONFIRMED) exp shots 23.1, exp saves 20.7 (sd 5.74), pull risk 0.037
- CHI net: Arvid Soderblom (CONFIRMED) exp shots 30.41, exp saves 25.22 (sd 7.41), pull risk 0.108

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 19+ saves | 0.642 | 0.515 | 52/49 | +0.105 |  |
| Arvid Soderblom: 28+ saves | 0.382 | 0.480 | 49/53 | +0.071 |  |
| Nikita Kucherov: 2+ points | 0.395 | 0.490 | 50/52 | +0.068 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.206 | 0.285 | 29/72 | +0.060 | STANDARD |
| Nikita Kucherov: 3+ points | 0.157 | 0.225 | 23/78 | +0.051 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.573 | 0.640 | 66/38 | +0.031 | STANDARD |

**STL @ NJD** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (CONFIRMED) exp shots 24.87, exp saves 21.61 (sd 6.04), pull risk 0.052
- STL net: Jordan Binnington (CONFIRMED) exp shots 30.21, exp saves 25.9 (sd 7.15), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Binnington: 28+ saves | 0.404 | 0.515 | 52/49 | +0.089 |  |
| Dylan Holloway: 1+ points | 0.537 | 0.435 | 45/58 | +0.070 | STANDARD |
| Jack Hughes: 2+ points | 0.258 | 0.355 | 37/66 | +0.066 | STANDARD |
| Jack Hughes: 1+ assists | 0.430 | 0.525 | 53/48 | +0.072 | STANDARD |
| Dylan Holloway: 1+ assists | 0.371 | 0.280 | 29/73 | +0.066 | STANDARD |
| Luke Evangelista: 1+ assists | 0.261 | 0.350 | 37/67 | +0.054 | STANDARD |

**CAR @ NYI** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 29.43, exp saves 25.25 (sd 6.86), pull risk 0.066
- CAR net: Brandon Bussi (CONFIRMED) exp shots 24.49, exp saves 21.19 (sd 6.05), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.330 | 0.445 | 46/57 | +0.083 | STANDARD |
| Sebastian Aho: 1+ points | 0.508 | 0.615 | 63/40 | +0.075 | STANDARD |
| Sebastian Aho: 2+ points | 0.159 | 0.255 | 28/77 | +0.058 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.308 | 0.400 | 41/61 | +0.065 | STANDARD |
| Brayden Schenn: 1+ points | 0.501 | 0.420 | 43/59 | +0.054 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.496 | 0.575 | 59/44 | +0.047 | STANDARD |

**PHI @ NYR** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 25.8, exp saves 22.51 (sd 6.14), pull risk 0.049
- PHI net: Joseph Woll (CONFIRMED) exp shots 26.19, exp saves 22.68 (sd 6.17), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.257 | 0.340 | 35/67 | +0.058 | STANDARD |
| Travis Konecny: 1+ points | 0.420 | 0.495 | 51/52 | +0.043 | STANDARD |
| Tye Kartye: 1+ assists | 0.306 | 0.240 | 25/77 | +0.043 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.470 | 0.535 | 54/47 | +0.042 | STANDARD |
| Travis Sanheim: 1+ assists | 0.306 | 0.245 | 25/76 | +0.043 | STANDARD |
| Travis Sanheim: 1+ points | 0.374 | 0.320 | 33/69 | +0.029 | STANDARD |

**BOS @ PIT** · priced 187/188 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.87, exp saves 22.22 (sd 6.43), pull risk 0.073
- BOS net: Michael DiPietro (CONFIRMED) exp shots 29.12, exp saves 24.96 (sd 6.83), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ville Koivunen: 1+ assists | 0.279 | 0.175 | 26/91 | +0.006 | STANDARD |
| Hampus Lindholm: 1+ points | 0.342 | 0.250 | 31/81 | +0.017 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.400 | 0.490 | 50/52 | +0.063 | STANDARD |
| David Pastrnak: 1+ assists | 0.464 | 0.545 | 55/46 | +0.059 | STANDARD |
| Charlie McAvoy: 1+ points | 0.478 | 0.555 | 57/46 | +0.045 | STANDARD |
| Connor Dewar: 1+ goals | 0.189 | 0.115 | 12/89 | +0.061 | STANDARD |

**DAL @ CBJ** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 25.44, exp saves 22.08 (sd 6.18), pull risk 0.055
- DAL net: Casey DeSmith (CONFIRMED) exp shots 25.62, exp saves 22.16 (sd 6.17), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.427 | 0.495 | 51/52 | +0.036 | STANDARD |
| Charlie Coyle: 1+ goals | 0.283 | 0.225 | 23/78 | +0.041 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.210 | 0.155 | 16/85 | +0.041 | STANDARD |
| Cole Sillinger: 1+ goals | 0.178 | 0.125 | 14/89 | +0.030 | STANDARD |
| Charlie Coyle: 1+ points | 0.561 | 0.510 | 52/50 | +0.024 | STANDARD |
| Sean Monahan: 1+ goals | 0.197 | 0.150 | 16/86 | +0.027 | STANDARD |

**VAN @ WPG** · priced 150/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 24.76, exp saves 21.49 (sd 6.04), pull risk 0.055
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.31, exp saves 25.01 (sd 6.94), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 1+ goals | 0.232 | 0.125 | 24/99 | -0.021 | STANDARD |
| Kyle Connor: 1+ assists | 0.428 | 0.515 | 52/49 | +0.065 | STANDARD |
| Kyle Connor: 2+ points | 0.302 | 0.385 | 41/64 | +0.042 | STANDARD |
| Neal Pionk: 1+ points | 0.464 | 0.540 | 55/47 | +0.048 | STANDARD |
| Marco Rossi: 1+ goals | 0.220 | 0.145 | 16/87 | +0.051 | STANDARD |
| Linus Karlsson: 1+ goals | 0.230 | 0.155 | 17/86 | +0.050 | STANDARD |

**ANA @ EDM** · priced 184/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Matt Tomkins (CONFIRMED) exp shots 27.9, exp saves 24.13 (sd 6.74), pull risk 0.075
- ANA net: Laurent Brossoit (PROBABLE) exp shots 27.83, exp saves 23.61 (sd 6.86), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leon Draisaitl: 2+ points | 0.379 | 0.525 | 53/48 | +0.123 | STANDARD |
| Connor McDavid: 2+ points | 0.446 | 0.585 | 59/42 | +0.117 | STANDARD |
| Connor McDavid: 2+ assists | 0.221 | 0.350 | 37/67 | +0.093 | STANDARD |
| Connor McDavid: 1+ assists | 0.590 | 0.715 | 72/29 | +0.105 | STANDARD |
| Leon Draisaitl: 3+ points | 0.138 | 0.255 | 26/75 | +0.099 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.500 | 0.615 | 62/39 | +0.094 | STANDARD |

**NSH @ COL** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.73, exp saves 22.64 (sd 6.23), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.26 (sd 7.57), pull risk 0.094

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.381 | 0.465 | 48/55 | +0.052 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.527 | 0.610 | 62/40 | +0.056 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.204 | 0.285 | 29/72 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.250 | 27/77 | +0.046 | STANDARD |
| Mavrik Bourque: 1+ points | 0.353 | 0.420 | 43/59 | +0.040 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.145 | 0.205 | 22/81 | +0.035 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
