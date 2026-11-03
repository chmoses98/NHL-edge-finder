# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T15:40:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3963 · contracts joined: 2271 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1996, 'OK': 146, 'NO_EDGE': 129}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 282, 'game_early_goal': 11, 'first_goal': 393, 'game_winner': 22, 'player_goals': 672, 'game_overtime': 11, 'player_points': 363, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-6h | 0.479 | 0.521 | 0.171 | 7.06 | 3.45 | 3.61 | 223 (25/198) | CONFIRMED/PROJECTED |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-6h | 0.657 | 0.343 | 0.166 | 6.10 | 3.54 | 2.55 | 191 (25/166) | PROJECTED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-6h | 0.641 | 0.359 | 0.172 | 6.03 | 3.45 | 2.57 | 215 (25/190) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-6h | 0.506 | 0.494 | 0.178 | 6.09 | 3.07 | 3.02 | 196 (25/171) | PROJECTED/PROJECTED |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-6h | 0.416 | 0.584 | 0.173 | 5.96 | 2.72 | 3.24 | 209 (25/184) | PROJECTED/PROJECTED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-6h | 0.548 | 0.452 | 0.168 | 6.76 | 3.53 | 3.22 | 206 (25/181) | PROJECTED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-6h | 0.551 | 0.449 | 0.185 | 5.82 | 3.06 | 2.75 | 209 (25/184) | PROJECTED/PROJECTED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-6h | 0.417 | 0.583 | 0.177 | 5.80 | 2.64 | 3.16 | 207 (25/182) | PROJECTED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-6h | 0.527 | 0.473 | 0.177 | 6.43 | 3.31 | 3.12 | 208 (25/183) | PROJECTED/PROJECTED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-6h | 0.380 | 0.620 | 0.172 | 6.28 | 2.75 | 3.53 | 199 (25/174) | PROJECTED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-6h | 0.421 | 0.579 | 0.162 | 7.11 | 3.29 | 3.82 | 208 (25/183) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.379 | 0.485 | 0.463 | 49 | 52 | no | +0.084 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-6 | game_total | 0.492 | 0.595 | 0.575 | 60 | 41 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.496 | 0.605 | 0.584 | 62 | 41 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.282 | 0.375 | 0.355 | 38 | 63 | no | +0.072 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.267 | 0.355 | 0.336 | 36 | 65 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.466 | 0.560 | 0.541 | 57 | 45 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.264 | 0.350 | 0.332 | 36 | 66 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.408 | 0.485 | 0.469 | 49 | 52 | no | +0.055 | OK |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.359 | 0.285 | 0.299 | 29 | 72 | yes | +0.054 | OK |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.641 | 0.715 | 0.701 | 72 | 29 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.734 | 0.810 | 0.796 | 82 | 20 | no | +0.054 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-8 | game_total | 0.205 | 0.275 | 0.260 | 28 | 73 | no | +0.051 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-5 | game_total | 0.720 | 0.785 | 0.773 | 79 | 22 | no | +0.048 | OK |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.527 | 0.595 | 0.582 | 60 | 41 | no | +0.046 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.210 | 0.275 | 0.261 | 28 | 73 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.389 | 0.325 | 0.337 | 33 | 68 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.683 | 0.750 | 0.737 | 76 | 26 | no | +0.043 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-4 | game_total | 0.820 | 0.880 | 0.870 | 89 | 13 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-9 | game_total | 0.138 | 0.195 | 0.182 | 20 | 81 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.523 | 0.590 | 0.577 | 60 | 42 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.111 | 0.165 | 0.153 | 17 | 84 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 | team_total | 0.607 | 0.545 | 0.557 | 55 | 46 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.133 | 0.195 | 0.181 | 21 | 82 | no | +0.037 | OK |
| KXNHLSPREAD-26NOV03VGKPIT-PIT2 | game_spread | 0.341 | 0.285 | 0.296 | 29 | 72 | yes | +0.036 | OK |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.473 | 0.415 | 0.426 | 42 | 59 | yes | +0.036 | OK |
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.417 | 0.475 | 0.463 | 48 | 53 | no | +0.036 | OK |
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.583 | 0.525 | 0.537 | 53 | 48 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.309 | 0.370 | 0.357 | 38 | 64 | no | +0.035 | OK |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.449 | 0.505 | 0.494 | 51 | 50 | no | +0.034 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.223 | 0.275 | 0.264 | 28 | 73 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6 | team_total | 0.138 | 0.090 | 0.098 | 10 | 92 | yes | +0.031 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.196 | 0.245 | 0.235 | 25 | 76 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ2 | game_spread | 0.313 | 0.365 | 0.354 | 37 | 64 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.210 | 0.160 | 0.169 | 17 | 85 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.130 | 0.180 | 0.169 | 19 | 83 | no | +0.030 | OK |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.131 | 0.175 | 0.165 | 18 | 83 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV03VGKPIT-PIT4 | team_total | 0.486 | 0.430 | 0.441 | 44 | 58 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.393 | 0.345 | 0.354 | 35 | 66 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.496 | 0.545 | 0.535 | 55 | 46 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV03VGKPIT-PIT3 | team_total | 0.692 | 0.640 | 0.651 | 65 | 37 | yes | +0.026 | OK |
| KXNHLTOTAL-26NOV03DETTB-5 | game_total | 0.753 | 0.795 | 0.787 | 80 | 21 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR4 | team_total | 0.462 | 0.410 | 0.420 | 42 | 60 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03UTATOR-10 | game_total | 0.162 | 0.120 | 0.128 | 13 | 89 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-9 | game_total | 0.298 | 0.255 | 0.263 | 26 | 75 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.162 | 0.125 | 0.132 | 13 | 88 | yes | +0.024 | OK |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.551 | 0.505 | 0.514 | 51 | 50 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.861 | 0.905 | 0.897 | 92 | 11 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV03WPGMTL-WPG2 | game_spread | 0.167 | 0.205 | 0.197 | 21 | 80 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6 | team_total | 0.096 | 0.055 | 0.062 | 7 | 96 | yes | +0.021 | OK |
| KXNHLGAME-26NOV03VGKPIT-PIT | game_winner | 0.548 | 0.505 | 0.514 | 51 | 50 | yes | +0.021 | OK |
| KXNHLGAME-26NOV03VGKPIT-VGK | game_winner | 0.452 | 0.495 | 0.486 | 50 | 51 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.294 | 0.250 | 0.259 | 26 | 76 | yes | +0.021 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN2 | game_spread | 0.353 | 0.395 | 0.386 | 40 | 61 | no | +0.021 | OK |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.584 | 0.625 | 0.617 | 63 | 38 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV03EDMNJ-7 | game_total | 0.487 | 0.445 | 0.453 | 45 | 56 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV03DETTB-6 | game_total | 0.533 | 0.575 | 0.567 | 58 | 43 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.385 | 0.340 | 0.349 | 35 | 67 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-EDM2 | game_spread | 0.261 | 0.225 | 0.232 | 23 | 78 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR3 | team_total | 0.674 | 0.635 | 0.643 | 64 | 37 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV03EDMNJ-8 | game_total | 0.291 | 0.250 | 0.258 | 26 | 76 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV03VGKPIT-PIT6 | team_total | 0.144 | 0.110 | 0.116 | 12 | 90 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 | team_total | 0.476 | 0.515 | 0.507 | 52 | 49 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-3 | game_total | 0.951 | 0.980 | 0.976 | 99 | 3 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV03CARNSH-CAR3 | game_spread | 0.259 | 0.295 | 0.288 | 30 | 71 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV03DETTB-7 | game_total | 0.417 | 0.455 | 0.447 | 46 | 55 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV03DETTB-DET2 | game_spread | 0.175 | 0.145 | 0.151 | 15 | 86 | yes | +0.016 | OK |
| KXNHLSPREAD-26NOV03DALWSH-WSH2 | game_spread | 0.320 | 0.285 | 0.292 | 29 | 72 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV03VGKPIT-VGK2 | team_total | 0.826 | 0.855 | 0.849 | 86 | 15 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-7 | game_total | 0.592 | 0.555 | 0.563 | 56 | 45 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV03DALWSH-5 | game_total | 0.722 | 0.755 | 0.749 | 76 | 25 | no | +0.015 | OK |
| KXNHLSPREAD-26NOV03VGKPIT-VGK3 | game_spread | 0.155 | 0.190 | 0.183 | 20 | 82 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-6 | game_total | 0.700 | 0.665 | 0.672 | 67 | 34 | yes | +0.014 | OK |
| KXNHLGAME-26NOV03CARNSH-NSH | game_winner | 0.380 | 0.345 | 0.352 | 35 | 66 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.419 | 0.460 | 0.452 | 47 | 55 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-10 | game_total | 0.061 | 0.090 | 0.083 | 10 | 92 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG4 | team_total | 0.262 | 0.295 | 0.288 | 30 | 71 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-5 | game_total | 0.863 | 0.835 | 0.841 | 84 | 17 | yes | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 0.479 | 0.497 | 0.171 | 0.214 | 7.06 | 6.77 | 0.989/0.998 | KXNHLTOTAL-26NOV03UTATOR-8 -0.047 |
| WPG @ MTL | 0.657 | 0.587 | 0.166 | 0.217 | 6.10 | 6.26 | 0.976/0.998 | KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 +0.072 |
| DET @ TBL | 0.641 | 0.644 | 0.172 | 0.208 | 6.03 | 6.23 | 0.958/1.004 | KXNHLTOTAL-26NOV03DETTB-7 +0.038 |
| STL @ NYR | 0.506 | 0.521 | 0.178 | 0.219 | 6.09 | 6.29 | 0.987/0.994 | KXNHLTOTAL-26NOV03STLNYR-7 +0.039 |
| MIN @ PHI | 0.416 | 0.523 | 0.173 | 0.221 | 5.96 | 6.01 | 0.992/0.996 | KXNHLGAME-26NOV03MINPHI-MIN -0.106 |
| VGK @ PIT | 0.548 | 0.526 | 0.168 | 0.214 | 6.76 | 6.53 | 1.034/1.004 | KXNHLTEAMTOTAL-26NOV03VGKPIT-PIT4 -0.043 |
| DAL @ WSH | 0.551 | 0.542 | 0.185 | 0.222 | 5.82 | 6.17 | 0.961/0.987 | KXNHLTOTAL-26NOV03DALWSH-7 +0.064 |
| COL @ CBJ | 0.417 | 0.484 | 0.177 | 0.214 | 5.80 | 6.28 | 0.965/0.971 | KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 +0.109 |
| EDM @ NJD | 0.527 | 0.498 | 0.177 | 0.214 | 6.43 | 6.61 | 0.960/1.010 | KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 +0.047 |
| CAR @ NSH | 0.380 | 0.455 | 0.172 | 0.214 | 6.28 | 6.55 | 1.001/0.998 | KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3 +0.094 |
| ANA @ VAN | 0.421 | 0.457 | 0.162 | 0.213 | 7.11 | 6.88 | 1.022/1.017 | KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4 -0.050 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 11c · p 0.1774 (adj 0.1593) · $4.56 · thesis TOR:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 11c · p 0.151 (adj 0.1382) · $2.33 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2205 (adj 0.2079) · $2.21 · thesis UTA:OFFENSE_4PLUS
- Anders Lee: 1+ goals YES @ 20c · p 0.2431 (adj 0.2273) · $2.09 · thesis UTA:OFFENSE_4PLUS
- Oliver Kapanen: 1+ goals YES @ 15c · p 0.1923 (adj 0.1805) · $2.59 · thesis MTL:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 4c · p 0.0645 (adj 0.0546) · $1.1 · thesis WPG:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 14c · p 0.1738 (adj 0.1628) · $1.69 · thesis MTL:WINS_BY_2PLUS
- Josh Anderson: 1+ goals YES @ 20c · p 0.2384 (adj 0.2276) · $2.16 · thesis MTL:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 88c · p 0.9217 (adj 0.9075) · $8.54 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 35c · p 0.4763 (adj 0.3877) · $2.99 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 65c · p 0.7157 (adj 0.6804) · $2.67 · thesis GAME:TIGHT
- Emmitt Finnie: 1+ assists YES @ 27c · p 0.3293 (adj 0.2972) · $1.68 · thesis DET:OFFENSE_4PLUS
- Tye Kartye: 1+ goals YES @ 16c · p 0.1987 (adj 0.1865) · $2.08 · thesis NYR:OFFENSE_4PLUS
- Alexis Lafreniere: 1+ goals YES @ 31c · p 0.3548 (adj 0.3411) · $2.49 · thesis NYR:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2199 (adj 0.2024) · $4.04 · thesis PHI:OFFENSE_4PLUS
- Philadelphia wins by over 1.5 goals YES @ 20c · p 0.2927 (adj 0.2439) · $3.15 · thesis PHI:WINS_BY_2PLUS
- Matt Boldy: 1+ goals NO @ 63c · p 0.6874 (adj 0.6705) · $5.66 · thesis MIN:SUPPRESSED
- Travis Konecny: 1+ assists NO @ 68c · p 0.7538 (adj 0.7094) · $8.5 · thesis PHI:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1668 (adj 0.1551) · $2.02 · thesis PIT:WINS_BY_2PLUS
- Sidney Crosby: 1+ assists NO @ 53c · p 0.6156 (adj 0.5678) · $4.81 · thesis PIT:SUPPRESSED
- Ville Koivunen: 1+ goals NO @ 82c · p 0.8542 (adj 0.8431) · $7.89 · thesis PIT:SUPPRESSED
- Mark Stone: 1+ assists NO @ 56c · p 0.6261 (adj 0.588) · $2.73 · thesis VGK:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2317 (adj 0.2138) · $4.15 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 16c · p 0.2113 (adj 0.1972) · $3.37 · thesis WSH:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 87c · p 0.9037 (adj 0.894) · $8.54 · thesis DAL:SUPPRESSED
- Arttu Hyry: 1+ goals YES @ 12c · p 0.151 (adj 0.142) · $1.81 · thesis DAL:OFFENSE_4PLUS
- Cole Sillinger: 1+ goals YES @ 13c · p 0.1639 (adj 0.1529) · $1.73 · thesis CBJ:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 15c · p 0.1844 (adj 0.1746) · $1.89 · thesis CBJ:OFFENSE_4PLUS
- Brock Nelson: 1+ goals NO @ 77c · p 0.811 (adj 0.7995) · $8.54 · thesis COL:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1771 (adj 0.1691) · $1.13 · thesis CBJ:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 10c · p 0.1577 (adj 0.142) · $3.71 · thesis EDM:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 9c · p 0.1282 (adj 0.1149) · $1.96 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 23c · p 0.2842 (adj 0.2681) · $3.34 · thesis EDM:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 65c · p 0.7336 (adj 0.6893) · $7.6 · thesis NJD:SUPPRESSED
- Jack Drury: 1+ goals YES @ 9c · p 0.1298 (adj 0.1186) · $2.34 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1728 (adj 0.1596) · $2.36 · thesis NSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7197 (adj 0.7048) · $5.98 · thesis CAR:SUPPRESSED
- Carolina wins by over 2.5 goals NO @ 71c · p 0.7807 (adj 0.7429) · $4.61 · thesis NSH:WINS
- Tim Washe: 1+ goals YES @ 12c · p 0.1591 (adj 0.1468) · $2.21 · thesis ANA:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 20c · p 0.244 (adj 0.2305) · $2.48 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 21c · p 0.2557 (adj 0.2405) · $2.41 · thesis VAN:OFFENSE_4PLUS
- Liam Ohgren: 1+ goals YES @ 17c · p 0.2067 (adj 0.195) · $1.85 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ TOR** · priced 166/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.47 (sd 7.23), pull risk 0.077
- UTA net: Sebastian Cossa (PROJECTED) exp shots 26.79, exp saves 23.14 (sd 6.52), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Morgan Rielly: 1+ assists | 0.349 | 0.255 | 27/76 | +0.066 | STANDARD |
| Auston Matthews: 1+ assists | 0.402 | 0.495 | 51/52 | +0.060 | STANDARD |
| Teddy Blueger: 1+ goals | 0.177 | 0.105 | 11/90 | +0.061 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.533 | 0.605 | 62/41 | +0.040 | STANDARD |
| Easton Cowan: 1+ assists | 0.353 | 0.285 | 30/73 | +0.039 | STANDARD |
| Morgan Rielly: 1+ points | 0.402 | 0.335 | 35/68 | +0.036 | STANDARD |

**WPG @ MTL** · priced 134/140 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.0, exp saves 23.57 (sd 6.38), pull risk 0.05
- WPG net: Nico Daws (PROJECTED) exp shots 27.07, exp saves 23.05 (sd 6.44), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Perfetti: 1+ assists | 0.374 | 0.295 | 30/71 | +0.059 | STANDARD |
| Cole Perfetti: 1+ points | 0.535 | 0.465 | 47/54 | +0.048 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.305 | 0.240 | 25/77 | +0.042 | STANDARD |
| Cole Caufield: 1+ assists | 0.367 | 0.430 | 44/58 | +0.036 | STANDARD |
| Mark Scheifele: 1+ goals | 0.312 | 0.265 | 28/75 | +0.018 | STANDARD |
| Oliver Kapanen: 1+ goals | 0.192 | 0.145 | 15/86 | +0.033 | STANDARD |

**DET @ TBL** · priced 153/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.08 (sd 6.22), pull risk 0.044
- DET net: John Gibson (PROJECTED) exp shots 27.95, exp saves 23.68 (sd 6.8), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.524 | 0.660 | 67/35 | +0.110 | STANDARD |
| Nikita Kucherov: 2+ points | 0.338 | 0.460 | 48/56 | +0.085 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.169 | 0.280 | 30/74 | +0.078 | STANDARD |
| Nikita Kucherov: 3+ points | 0.122 | 0.215 | 23/80 | +0.067 | STANDARD |
| Nikita Kucherov: 1+ points | 0.705 | 0.770 | 81/27 | +0.011 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.329 | 0.265 | 27/74 | +0.046 | STANDARD |

**STL @ NYR** · priced 142/145 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 26.61, exp saves 23.01 (sd 6.37), pull risk 0.057
- STL net: Joel Hofer (PROJECTED) exp shots 26.51, exp saves 22.94 (sd 6.39), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ assists | 0.382 | 0.305 | 32/71 | +0.047 | STANDARD |
| Alexis Lafreniere: 1+ points | 0.608 | 0.550 | 57/47 | +0.021 | STANDARD |
| Alexis Lafreniere: 1+ goals | 0.355 | 0.300 | 31/71 | +0.030 | STANDARD |
| Dylan Holloway: 1+ points | 0.549 | 0.495 | 50/51 | +0.031 | STANDARD |
| Robert Thomas: 1+ assists | 0.416 | 0.470 | 49/55 | +0.016 | STANDARD |
| Robert Thomas: 2+ assists | 0.103 | 0.155 | 17/86 | +0.028 | STANDARD |

**MIN @ PHI** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 28.47, exp saves 24.74 (sd 6.67), pull risk 0.054
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 25.89, exp saves 22.47 (sd 6.23), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.245 | 0.400 | 42/62 | +0.118 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.611 | 0.765 | 78/25 | +0.126 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.389 | 0.530 | 55/49 | +0.104 | STANDARD |
| Matt Boldy: 1+ assists | 0.379 | 0.500 | 52/52 | +0.084 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.366 | 0.475 | 48/53 | +0.087 | STANDARD |
| Kirill Kaprizov: 3+ points | 0.069 | 0.175 | 19/84 | +0.081 | STANDARD |

**VGK @ PIT** · priced 151/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.98, exp saves 23.4 (sd 6.55), pull risk 0.061
- VGK net: Adin Hill (PROJECTED) exp shots 27.28, exp saves 23.46 (sd 6.65), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.436 | 0.535 | 54/47 | +0.077 | STANDARD |
| Sidney Crosby: 1+ assists | 0.384 | 0.480 | 49/53 | +0.068 | STANDARD |
| Mitch Marner: 1+ assists | 0.412 | 0.505 | 51/50 | +0.071 | STANDARD |
| Jack Eichel: 2+ points | 0.239 | 0.330 | 34/68 | +0.066 | STANDARD |
| Mitch Marner: 1+ points | 0.552 | 0.640 | 65/37 | +0.061 | STANDARD |
| Sidney Crosby: 1+ points | 0.574 | 0.660 | 67/35 | +0.060 | STANDARD |

**DAL @ WSH** · priced 152/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 26.25, exp saves 22.85 (sd 6.26), pull risk 0.055
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.46, exp saves 21.84 (sd 6.18), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.456 | 0.555 | 57/46 | +0.066 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.346 | 0.425 | 44/59 | +0.047 | STANDARD |
| Miro Heiskanen: 2+ points | 0.129 | 0.205 | 22/81 | +0.050 | STANDARD |
| Mikko Rantanen: 2+ points | 0.207 | 0.280 | 29/73 | +0.049 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.232 | 0.160 | 17/85 | +0.052 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.400 | 0.470 | 48/54 | +0.043 | STANDARD |

**COL @ CBJ** · priced 155/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 29.48, exp saves 25.61 (sd 6.84), pull risk 0.059
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.26 (sd 6.36), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ points | 0.532 | 0.615 | 63/40 | +0.051 | STANDARD |
| Zach Werenski: 1+ assists | 0.479 | 0.560 | 57/45 | +0.053 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.290 | 0.370 | 38/64 | +0.054 | STANDARD |
| Cale Makar: 2+ points | 0.173 | 0.245 | 26/77 | +0.045 | STANDARD |
| Cale Makar: 1+ assists | 0.443 | 0.510 | 52/50 | +0.039 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.449 | 0.515 | 53/50 | +0.034 | STANDARD |

**EDM @ NJD** · priced 156/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.46, exp saves 22.89 (sd 6.43), pull risk 0.066
- EDM net: Tristan Jarry (PROJECTED) exp shots 29.41, exp saves 25.35 (sd 6.96), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.406 | 0.530 | 54/48 | +0.096 | STANDARD |
| Connor McDavid: 2+ points | 0.379 | 0.500 | 51/51 | +0.094 | STANDARD |
| Connor McDavid: 1+ assists | 0.534 | 0.650 | 66/36 | +0.090 | STANDARD |
| Connor McDavid: 2+ assists | 0.177 | 0.290 | 31/73 | +0.080 | STANDARD |
| Jack Hughes: 1+ points | 0.604 | 0.695 | 71/32 | +0.061 | STANDARD |
| Luke Evangelista: 1+ assists | 0.266 | 0.355 | 36/65 | +0.068 | STANDARD |

**CAR @ NSH** · priced 147/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 31.84, exp saves 27.19 (sd 7.41), pull risk 0.081
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.28 (sd 6.02), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.354 | 0.500 | 51/51 | +0.119 | STANDARD |
| Sebastian Aho: 2+ points | 0.181 | 0.305 | 32/71 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.536 | 0.650 | 66/36 | +0.088 | STANDARD |
| Andrei Svechnikov: 2+ points | 0.168 | 0.255 | 27/76 | +0.059 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.345 | 0.425 | 44/59 | +0.048 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.532 | 0.610 | 62/40 | +0.051 | STANDARD |

**ANA @ VAN** · priced 146/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.41, exp saves 26.04 (sd 7.19), pull risk 0.079
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.99, exp saves 21.54 (sd 6.17), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ assists | 0.417 | 0.525 | 54/49 | +0.076 | STANDARD |
| Leo Carlsson: 2+ points | 0.229 | 0.330 | 34/68 | +0.076 | STANDARD |
| Leo Carlsson: 2+ assists | 0.101 | 0.180 | 20/84 | +0.049 | STANDARD |
| Mikael Granlund: 1+ assists | 0.385 | 0.455 | 47/56 | +0.037 | STANDARD |
| Leo Carlsson: 1+ points | 0.596 | 0.660 | 68/36 | +0.028 | STANDARD |
| Mikael Granlund: 2+ points | 0.183 | 0.245 | 26/77 | +0.034 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
