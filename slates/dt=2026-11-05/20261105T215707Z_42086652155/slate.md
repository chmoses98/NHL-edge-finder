# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T21:57:07Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4161 · contracts joined: 2422 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2147, 'OK': 132, 'NO_EDGE': 143}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 322, 'game_early_goal': 11, 'first_goal': 394, 'game_winner': 22, 'player_goals': 684, 'game_overtime': 11, 'player_points': 444, 'goalie_saves': 17, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-90m | 0.518 | 0.482 | 0.166 | 6.53 | 3.33 | 3.20 | 223 (25/198) | CONFIRMED/PROBABLE |
| VGK @ DET | 2026-11-06T00:00:00Z | T-90m | 0.513 | 0.487 | 0.179 | 6.06 | 3.06 | 3.00 | 217 (25/192) | PROBABLE/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-90m | 0.755 | 0.245 | 0.139 | 6.32 | 4.03 | 2.29 | 212 (25/187) | PROBABLE/PROBABLE |
| STL @ NJD | 2026-11-06T00:00:00Z | T-90m | 0.658 | 0.342 | 0.157 | 6.58 | 3.81 | 2.77 | 223 (25/198) | PROBABLE/CONFIRMED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-90m | 0.447 | 0.553 | 0.178 | 6.05 | 2.86 | 3.19 | 216 (25/191) | CONFIRMED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-90m | 0.629 | 0.371 | 0.175 | 5.99 | 3.39 | 2.61 | 229 (25/204) | CONFIRMED/CONFIRMED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-90m | 0.452 | 0.548 | 0.176 | 6.53 | 3.10 | 3.43 | 223 (25/198) | CONFIRMED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-90m | 0.433 | 0.567 | 0.181 | 5.99 | 2.80 | 3.19 | 207 (25/182) | CONFIRMED/CONFIRMED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-90m | 0.609 | 0.391 | 0.167 | 6.46 | 3.58 | 2.88 | 213 (25/188) | CONFIRMED/PROBABLE |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-3h | 0.642 | 0.358 | 0.156 | 6.99 | 4.00 | 3.00 | 236 (25/211) | CONFIRMED/PROBABLE |
| NSH @ COL | 2026-11-06T02:30:00Z | T-3h | 0.654 | 0.346 | 0.161 | 6.59 | 3.80 | 2.79 | 223 (25/198) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.447 | 0.345 | 0.365 | 35 | 66 | yes | +0.081 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.553 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.513 | 0.425 | 0.442 | 43 | 58 | yes | +0.066 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.487 | 0.575 | 0.558 | 58 | 43 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV05STLNJ-8 | game_total | 0.317 | 0.235 | 0.250 | 24 | 77 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.382 | 0.465 | 0.448 | 47 | 54 | no | +0.061 | OK |
| KXNHLTOTAL-26NOV05STLNJ-7 | game_total | 0.507 | 0.425 | 0.441 | 43 | 58 | yes | +0.060 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.325 | 0.405 | 0.388 | 41 | 60 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.586 | 0.670 | 0.654 | 68 | 34 | no | +0.058 | OK |
| KXNHLTOTAL-26NOV05STLNJ-9 | game_total | 0.227 | 0.155 | 0.168 | 16 | 85 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.406 | 0.485 | 0.469 | 49 | 52 | no | +0.057 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.201 | 0.280 | 0.263 | 29 | 73 | no | +0.055 | OK |
| KXNHLTOTAL-26NOV05STLNJ-6 | game_total | 0.621 | 0.545 | 0.561 | 55 | 46 | yes | +0.054 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.273 | 0.345 | 0.330 | 35 | 66 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.397 | 0.465 | 0.451 | 47 | 54 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ6 | team_total | 0.183 | 0.120 | 0.131 | 13 | 89 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL3 | team_total | 0.522 | 0.455 | 0.468 | 46 | 55 | yes | +0.045 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.287 | 0.225 | 0.237 | 23 | 78 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.363 | 0.430 | 0.416 | 44 | 58 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.625 | 0.695 | 0.682 | 71 | 32 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.547 | 0.605 | 0.594 | 61 | 40 | no | +0.036 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.391 | 0.335 | 0.346 | 34 | 67 | yes | +0.035 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.609 | 0.665 | 0.654 | 67 | 34 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.796 | 0.850 | 0.840 | 86 | 16 | no | +0.035 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.755 | 0.805 | 0.796 | 81 | 20 | no | +0.033 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.245 | 0.195 | 0.204 | 20 | 81 | yes | +0.033 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.629 | 0.575 | 0.586 | 58 | 43 | yes | +0.032 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI4 | team_total | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.582 | 0.635 | 0.625 | 64 | 37 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.167 | 0.215 | 0.205 | 22 | 79 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.345 | 0.290 | 0.301 | 30 | 72 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.255 | 0.310 | 0.299 | 32 | 70 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.584 | 0.635 | 0.625 | 64 | 37 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.313 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV05STLNJ-10 | game_total | 0.113 | 0.070 | 0.077 | 8 | 94 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.825 | 0.870 | 0.862 | 88 | 14 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.220 | 0.270 | 0.260 | 28 | 74 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.279 | 0.325 | 0.315 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.407 | 0.460 | 0.449 | 47 | 55 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI3 | team_total | 0.487 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.098 | 0.135 | 0.127 | 14 | 87 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.151 | 0.115 | 0.122 | 12 | 89 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV05STLNJ-5 | game_total | 0.815 | 0.770 | 0.780 | 78 | 24 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 | team_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA3 | team_total | 0.622 | 0.670 | 0.661 | 68 | 34 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL6 | team_total | 0.064 | 0.035 | 0.040 | 4 | 97 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET6 | team_total | 0.085 | 0.055 | 0.060 | 6 | 95 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLGAME-26NOV05BOSPIT-BOS | game_winner | 0.548 | 0.505 | 0.514 | 51 | 50 | yes | +0.021 | OK |
| KXNHLGAME-26NOV05BOSPIT-PIT | game_winner | 0.452 | 0.495 | 0.486 | 50 | 51 | no | +0.021 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.518 | 0.475 | 0.484 | 48 | 53 | yes | +0.021 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.482 | 0.525 | 0.516 | 53 | 48 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.376 | 0.330 | 0.339 | 34 | 68 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.597 | 0.550 | 0.560 | 56 | 46 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV05STLNJ-4 | game_total | 0.888 | 0.855 | 0.862 | 86 | 15 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV05ANAEDM-5 | game_total | 0.853 | 0.885 | 0.879 | 89 | 12 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 | team_total | 0.334 | 0.295 | 0.303 | 30 | 71 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.247 | 0.285 | 0.277 | 29 | 72 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK5 | team_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.781 | 0.820 | 0.813 | 83 | 19 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV05CARNYI-5 | game_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLSPREAD-26NOV05CARNYI-NYI2 | game_spread | 0.239 | 0.205 | 0.212 | 21 | 80 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB6 | team_total | 0.210 | 0.245 | 0.238 | 25 | 76 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV05CARNYI-6 | game_total | 0.536 | 0.575 | 0.567 | 58 | 43 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.741 | 0.700 | 0.709 | 71 | 31 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV05PHINYR-NYR2 | game_spread | 0.393 | 0.355 | 0.362 | 36 | 65 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4 | team_total | 0.496 | 0.535 | 0.527 | 54 | 47 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-WPG2 | team_total | 0.867 | 0.895 | 0.890 | 90 | 11 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI2 | game_spread | 0.183 | 0.220 | 0.212 | 23 | 79 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.543 | 0.500 | 0.509 | 51 | 51 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL4 | team_total | 0.309 | 0.265 | 0.274 | 28 | 75 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-BOS3 | team_total | 0.671 | 0.635 | 0.642 | 64 | 37 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV05CHITB-8 | game_total | 0.280 | 0.315 | 0.308 | 32 | 69 | no | +0.015 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.388 | 0.425 | 0.418 | 43 | 58 | no | +0.015 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.329 | 0.295 | 0.302 | 30 | 71 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL3 | game_spread | 0.194 | 0.165 | 0.171 | 17 | 84 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.173 | 0.135 | 0.142 | 15 | 88 | yes | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.518 | 0.522 | 0.166 | 0.211 | 6.53 | 6.52 | 0.943/0.999 | KXNHLSPREAD-26NOV05UTAMTL-UTA2 -0.013 |
| VGK @ DET | 0.513 | 0.451 | 0.179 | 0.215 | 6.06 | 6.28 | 1.020/1.004 | KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 +0.068 |
| CHI @ TBL | 0.755 | 0.720 | 0.139 | 0.185 | 6.32 | 6.39 | 0.952/1.034 | KXNHLTEAMTOTAL-26NOV05CHITB-CHI3 +0.052 |
| STL @ NJD | 0.658 | 0.582 | 0.157 | 0.216 | 6.58 | 6.28 | 0.954/1.032 | KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 -0.093 |
| CAR @ NYI | 0.447 | 0.470 | 0.178 | 0.221 | 6.05 | 6.40 | 0.978/0.990 | KXNHLTOTAL-26NOV05CARNYI-7 +0.061 |
| PHI @ NYR | 0.629 | 0.540 | 0.175 | 0.224 | 5.99 | 5.98 | 0.988/0.991 | KXNHLGAME-26NOV05PHINYR-NYR -0.090 |
| BOS @ PIT | 0.452 | 0.517 | 0.176 | 0.212 | 6.53 | 6.71 | 1.042/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.072 |
| DAL @ CBJ | 0.433 | 0.509 | 0.181 | 0.223 | 5.99 | 6.13 | 1.008/0.969 | KXNHLGAME-26NOV05DALCBJ-DAL -0.076 |
| VAN @ WPG | 0.609 | 0.547 | 0.167 | 0.214 | 6.46 | 6.33 | 1.004/1.030 | KXNHLSPREAD-26NOV05VANWPG-WPG2 -0.064 |
| ANA @ EDM | 0.642 | 0.572 | 0.156 | 0.200 | 6.99 | 7.11 | 0.999/0.976 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3 +0.073 |
| NSH @ COL | 0.654 | 0.655 | 0.161 | 0.199 | 6.59 | 6.65 | 0.979/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Lawson Crouse: 1+ goals YES @ 18c · p 0.2254 (adj 0.2103) · $2.58 · thesis UTA:OFFENSE_4PLUS
- Cole Caufield: 1+ assists YES @ 33c · p 0.4133 (adj 0.3691) · $3.71 · thesis MTL:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 67c · p 0.7191 (adj 0.7056) · $7.23 · thesis UTA:SUPPRESSED
- Anders Lee: 1+ goals YES @ 20c · p 0.2352 (adj 0.2239) · $1.66 · thesis UTA:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.078 (adj 0.0698) · $1.67 · thesis VGK:OFFENSE_4PLUS
- Tampa Bay wins by over 1.5 goals NO @ 40c · p 0.4943 (adj 0.4446) · $5.54 · thesis GAME:TIGHT
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.2359 (adj 0.2219) · $2.75 · thesis CHI:OFFENSE_4PLUS
- Andrei Vasilevskiy: 19+ saves YES @ 51c · p 0.6441 (adj 0.5439) · $4.58 · thesis CHI:SHOT_CONTROL
- Connor Bedard: 1+ assists NO @ 58c · p 0.6452 (adj 0.6101) · $6.24 · thesis CHI:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 20c · p 0.2633 (adj 0.2462) · $4.57 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 25c · p 0.304 (adj 0.2893) · $3.75 · thesis STL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 59c · p 0.6516 (adj 0.6337) · $7.72 · thesis NJD:SUPPRESSED
- Dougie Hamilton: 1+ assists YES @ 29c · p 0.3446 (adj 0.3148) · $2.17 · thesis NJD:OFFENSE_4PLUS
- Brayden Schenn: 1+ goals YES @ 20c · p 0.2562 (adj 0.2409) · $3.96 · thesis NYI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7342 (adj 0.7169) · $8.81 · thesis CAR:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 12c · p 0.1581 (adj 0.1473) · $2.38 · thesis NYI:OFFENSE_4PLUS
- Anthony Duclair: 1+ goals YES @ 14c · p 0.1794 (adj 0.1683) · $2.47 · thesis NYI:OFFENSE_4PLUS
- Tye Kartye: 1+ assists YES @ 23c · p 0.306 (adj 0.2655) · $3.02 · thesis NYR:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 17c · p 0.2093 (adj 0.1982) · $2.92 · thesis PHI:OFFENSE_4PLUS
- Cole Knuble: 1+ goals YES @ 12c · p 0.1501 (adj 0.1413) · $1.73 · thesis PHI:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 67c · p 0.7434 (adj 0.7017) · $8.81 · thesis PHI:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1775 (adj 0.1619) · $3.91 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 10c · p 0.1401 (adj 0.1251) · $2.0 · thesis PIT:WINS_BY_2PLUS
- Ben Kindel: 1+ assists NO @ 69c · p 0.7562 (adj 0.7206) · $7.24 · thesis PIT:SUPPRESSED
- David Pastrnak: 1+ goals NO @ 61c · p 0.6528 (adj 0.6409) · $3.71 · thesis BOS:SUPPRESSED
- Cole Sillinger: 1+ goals YES @ 13c · p 0.1783 (adj 0.1625) · $2.8 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2832 (adj 0.2674) · $3.42 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2104 (adj 0.1978) · $2.2 · thesis CBJ:WINS_BY_2PLUS
- Damon Severson: 1+ goals YES @ 8c · p 0.1084 (adj 0.0975) · $1.34 · thesis CBJ:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2311 (adj 0.2121) · $5.15 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.218 (adj 0.2022) · $3.95 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1516 (adj 0.14) · $2.51 · thesis VAN:OFFENSE_4PLUS
- Winnipeg over 3.5 goals scored NO @ 47c · p 0.5626 (adj 0.5138) · $5.14 · thesis WPG:SUPPRESSED
- Jeff Malott: 1+ goals YES @ 9c · p 0.1223 (adj 0.113) · $1.93 · thesis ANA:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 13c · p 0.1664 (adj 0.1548) · $2.05 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.1988 (adj 0.1866) · $2.15 · thesis ANA:OFFENSE_4PLUS
- Beckett Sennecke: 1+ goals YES @ 30c · p 0.3494 (adj 0.3358) · $3.31 · thesis ANA:OFFENSE_4PLUS
- Nathan MacKinnon: 2+ assists NO @ 76c · p 0.8282 (adj 0.7866) · $6.13 · thesis COL:SUPPRESSED
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1561 (adj 0.1483) · $1.25 · thesis NSH:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ assists NO @ 40c · p 0.4729 (adj 0.4315) · $1.54 · thesis COL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.98, exp saves 25.12 (sd 6.84), pull risk 0.062
- UTA net: Sebastian Cossa (PROBABLE) exp shots 25.81, exp saves 22.17 (sd 6.29), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikhail Sergachev: 1+ points | 0.500 | 0.590 | 60/42 | +0.063 | STANDARD |
| Lawson Crouse: 1+ points | 0.429 | 0.340 | 36/68 | +0.053 | STANDARD |
| Cole Caufield: 1+ assists | 0.413 | 0.325 | 33/68 | +0.068 | STANDARD |
| Logan Cooley: 1+ points | 0.520 | 0.600 | 61/41 | +0.053 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.261 | 0.335 | 35/68 | +0.044 | STANDARD |
| Noah Dobson: 1+ assists | 0.370 | 0.300 | 32/72 | +0.035 | STANDARD |

**VGK @ DET** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROBABLE) exp shots 26.45, exp saves 22.72 (sd 6.46), pull risk 0.069
- VGK net: Carter Hart (PROJECTED) exp shots 27.41, exp saves 23.76 (sd 6.48), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.426 | 0.525 | 54/49 | +0.067 | STANDARD |
| Jack Eichel: 1+ assists | 0.445 | 0.530 | 55/49 | +0.047 | STANDARD |
| Ivan Barbashev: 1+ points | 0.500 | 0.425 | 43/58 | +0.053 | STANDARD |
| Mark Stone: 1+ assists | 0.376 | 0.450 | 46/56 | +0.047 | STANDARD |
| Mitch Marner: 2+ points | 0.201 | 0.275 | 28/73 | +0.055 | STANDARD |
| Mitch Marner: 1+ points | 0.563 | 0.635 | 64/37 | +0.051 | STANDARD |

**CHI @ TBL** · priced 150/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 23.1, exp saves 20.68 (sd 5.73), pull risk 0.039
- CHI net: Arvid Soderblom (PROBABLE) exp shots 30.41, exp saves 25.28 (sd 7.37), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 19+ saves | 0.644 | 0.490 | 51/53 | +0.117 |  |
| Nikita Kucherov: 2+ points | 0.387 | 0.495 | 50/51 | +0.086 | STANDARD |
| Arvid Soderblom: 28+ saves | 0.379 | 0.485 | 50/53 | +0.074 |  |
| Nikita Kucherov: 1+ assists | 0.562 | 0.665 | 67/34 | +0.082 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.205 | 0.295 | 31/72 | +0.061 | STANDARD |
| Nikita Kucherov: 3+ points | 0.149 | 0.225 | 23/78 | +0.059 | STANDARD |

**STL @ NJD** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROBABLE) exp shots 24.87, exp saves 21.6 (sd 6.06), pull risk 0.055
- STL net: Jordan Binnington (CONFIRMED) exp shots 30.21, exp saves 25.9 (sd 7.1), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ points | 0.622 | 0.735 | 75/28 | +0.084 | STANDARD |
| Luke Evangelista: 1+ assists | 0.247 | 0.360 | 37/65 | +0.087 | STANDARD |
| Dylan Holloway: 1+ points | 0.542 | 0.435 | 45/58 | +0.074 | STANDARD |
| Jack Hughes: 2+ points | 0.259 | 0.365 | 38/65 | +0.075 | STANDARD |
| Jack Hughes: 1+ assists | 0.420 | 0.525 | 54/49 | +0.072 | STANDARD |
| Jordan Binnington: 28+ saves | 0.406 | 0.505 | 52/51 | +0.067 |  |

**CAR @ NYI** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 29.43, exp saves 25.26 (sd 6.94), pull risk 0.067
- CAR net: Brandon Bussi (PROJECTED) exp shots 24.49, exp saves 21.24 (sd 6.06), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.329 | 0.445 | 46/57 | +0.084 | STANDARD |
| Sebastian Aho: 1+ points | 0.506 | 0.620 | 63/39 | +0.087 | STANDARD |
| Sebastian Aho: 2+ points | 0.157 | 0.270 | 28/74 | +0.090 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.494 | 0.585 | 60/43 | +0.059 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.309 | 0.395 | 41/62 | +0.055 | STANDARD |
| Simon Holmstrom: 1+ points | 0.515 | 0.435 | 44/57 | +0.057 | STANDARD |

**PHI @ NYR** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 25.8, exp saves 22.51 (sd 6.14), pull risk 0.049
- PHI net: Joseph Woll (CONFIRMED) exp shots 26.19, exp saves 22.68 (sd 6.17), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.257 | 0.340 | 35/67 | +0.058 | STANDARD |
| Tye Kartye: 1+ assists | 0.306 | 0.225 | 23/78 | +0.064 | STANDARD |
| Travis Konecny: 1+ points | 0.420 | 0.495 | 51/52 | +0.043 | STANDARD |
| Dylan Garand: 22+ saves | 0.562 | 0.495 | 51/52 | +0.034 |  |
| Travis Sanheim: 1+ assists | 0.306 | 0.245 | 25/76 | +0.043 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.470 | 0.530 | 54/48 | +0.032 | STANDARD |

**BOS @ PIT** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.87, exp saves 22.21 (sd 6.39), pull risk 0.073
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.04 (sd 6.84), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.399 | 0.485 | 50/53 | +0.053 | STANDARD |
| David Pastrnak: 1+ assists | 0.461 | 0.545 | 55/46 | +0.062 | STANDARD |
| David Pastrnak: 2+ points | 0.280 | 0.360 | 37/65 | +0.054 | STANDARD |
| Ben Kindel: 1+ assists | 0.244 | 0.315 | 32/69 | +0.051 | STANDARD |
| Pavel Zacha: 1+ assists | 0.359 | 0.430 | 44/58 | +0.044 | STANDARD |
| Charlie McAvoy: 2+ points | 0.138 | 0.205 | 22/81 | +0.041 | STANDARD |

**DAL @ CBJ** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 25.44, exp saves 22.08 (sd 6.18), pull risk 0.055
- DAL net: Casey DeSmith (CONFIRMED) exp shots 25.62, exp saves 22.16 (sd 6.17), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikko Rantanen: 1+ assists | 0.427 | 0.495 | 51/52 | +0.036 | STANDARD |
| Mikko Rantanen: 2+ points | 0.220 | 0.285 | 30/73 | +0.036 | STANDARD |
| Cole Sillinger: 1+ goals | 0.178 | 0.115 | 13/90 | +0.040 | STANDARD |
| Charlie Coyle: 1+ goals | 0.283 | 0.220 | 23/79 | +0.041 | STANDARD |
| Charlie Coyle: 1+ points | 0.561 | 0.510 | 52/50 | +0.024 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.210 | 0.160 | 17/85 | +0.031 | STANDARD |

**VAN @ WPG** · priced 154/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 24.76, exp saves 21.54 (sd 6.0), pull risk 0.056
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.31, exp saves 25.02 (sd 6.89), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 1+ goals | 0.229 | 0.125 | 24/99 | -0.023 | STANDARD |
| Kyle Connor: 2+ points | 0.304 | 0.390 | 41/63 | +0.050 | STANDARD |
| Mark Scheifele: 1+ assists | 0.506 | 0.590 | 60/42 | +0.057 | STANDARD |
| Elias Pettersson (#25): 1+ goals | 0.061 | 0.145 | 25/96 | -0.024 | STANDARD |
| Neal Pionk: 1+ points | 0.463 | 0.545 | 55/46 | +0.060 | STANDARD |
| Linus Karlsson: 1+ goals | 0.231 | 0.155 | 16/85 | +0.062 | STANDARD |

**ANA @ EDM** · priced 184/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Matt Tomkins (CONFIRMED) exp shots 27.9, exp saves 24.13 (sd 6.74), pull risk 0.075
- ANA net: Laurent Brossoit (PROBABLE) exp shots 27.83, exp saves 23.61 (sd 6.86), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.446 | 0.590 | 60/42 | +0.117 | STANDARD |
| Leon Draisaitl: 2+ points | 0.379 | 0.520 | 53/49 | +0.113 | STANDARD |
| Connor McDavid: 1+ assists | 0.590 | 0.715 | 73/30 | +0.095 | STANDARD |
| Connor McDavid: 2+ assists | 0.221 | 0.345 | 36/67 | +0.093 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.500 | 0.615 | 62/39 | +0.094 | STANDARD |
| Connor McDavid: 3+ points | 0.188 | 0.300 | 31/71 | +0.087 | STANDARD |

**NSH @ COL** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.73, exp saves 22.64 (sd 6.23), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.26 (sd 7.57), pull risk 0.094

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.204 | 0.290 | 31/73 | +0.052 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.255 | 27/76 | +0.055 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.527 | 0.610 | 62/40 | +0.056 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.381 | 0.455 | 47/56 | +0.042 | STANDARD |
| Cale Makar: 1+ assists | 0.503 | 0.575 | 59/44 | +0.040 | STANDARD |
| Cale Makar: 1+ points | 0.600 | 0.670 | 68/34 | +0.044 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
