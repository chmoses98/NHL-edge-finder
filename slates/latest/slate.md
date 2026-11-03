# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T13:52:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3806 · contracts joined: 2114 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1839, 'OK': 134, 'NO_EDGE': 141}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 254, 'game_early_goal': 11, 'first_goal': 360, 'game_winner': 22, 'player_goals': 611, 'game_overtime': 11, 'player_points': 328, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-6h | 0.478 | 0.522 | 0.167 | 7.06 | 3.45 | 3.61 | 223 (25/198) | CONFIRMED/PROJECTED |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-6h | 0.657 | 0.343 | 0.165 | 6.10 | 3.55 | 2.55 | 191 (25/166) | PROJECTED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-6h | 0.620 | 0.380 | 0.172 | 5.98 | 3.36 | 2.62 | 215 (25/190) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-6h | 0.509 | 0.491 | 0.184 | 6.10 | 3.07 | 3.02 | 196 (25/171) | PROJECTED/PROJECTED |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-6h | 0.419 | 0.581 | 0.179 | 5.97 | 2.73 | 3.24 | 209 (25/184) | PROJECTED/PROJECTED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-6h | 0.515 | 0.485 | 0.164 | 6.81 | 3.44 | 3.37 | 206 (25/181) | PROJECTED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-6h | 0.554 | 0.446 | 0.184 | 5.82 | 3.07 | 2.75 | 209 (25/184) | PROJECTED/PROJECTED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-6h | 0.395 | 0.605 | 0.176 | 5.84 | 2.59 | 3.24 | 207 (25/182) | PROJECTED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-6h | 0.530 | 0.470 | 0.174 | 6.43 | 3.31 | 3.12 | 208 (25/183) | PROJECTED/PROJECTED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-6h | 0.378 | 0.622 | 0.170 | 6.28 | 2.75 | 3.53 | 199 (25/174) | PROJECTED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-12h | 0.423 | 0.577 | 0.162 | 7.11 | 3.29 | 3.83 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.484 | 0.590 | 0.569 | 60 | 42 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.447 | 0.550 | 0.529 | 56 | 46 | no | +0.076 | OK |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.380 | 0.285 | 0.303 | 29 | 72 | yes | +0.076 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.251 | 0.350 | 0.329 | 36 | 66 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.274 | 0.370 | 0.350 | 38 | 64 | no | +0.070 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.393 | 0.485 | 0.466 | 49 | 52 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.720 | 0.805 | 0.790 | 81 | 20 | no | +0.068 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.387 | 0.475 | 0.457 | 48 | 53 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-6 | game_total | 0.497 | 0.590 | 0.572 | 60 | 42 | no | +0.066 | OK |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.620 | 0.705 | 0.689 | 71 | 30 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.250 | 0.345 | 0.325 | 36 | 67 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.668 | 0.750 | 0.735 | 76 | 26 | no | +0.059 | OK |
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.395 | 0.465 | 0.451 | 47 | 54 | no | +0.048 | OK |
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.605 | 0.535 | 0.549 | 54 | 47 | yes | +0.048 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-5 | game_total | 0.722 | 0.785 | 0.773 | 79 | 22 | no | +0.046 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-8 | game_total | 0.211 | 0.275 | 0.261 | 28 | 73 | no | +0.046 | OK |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.530 | 0.595 | 0.582 | 60 | 41 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.127 | 0.190 | 0.176 | 20 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.118 | 0.180 | 0.166 | 19 | 83 | no | +0.042 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.197 | 0.255 | 0.243 | 26 | 75 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.526 | 0.590 | 0.577 | 60 | 42 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV03DETTB-6 | game_total | 0.527 | 0.585 | 0.573 | 59 | 42 | no | +0.036 | OK |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.446 | 0.505 | 0.493 | 51 | 50 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.848 | 0.905 | 0.895 | 92 | 11 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.107 | 0.155 | 0.144 | 16 | 85 | no | +0.034 | OK |
| KXNHLTOTAL-26NOV03DETTB-5 | game_total | 0.744 | 0.795 | 0.785 | 80 | 21 | no | +0.034 | OK |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.470 | 0.415 | 0.426 | 42 | 59 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.213 | 0.150 | 0.161 | 17 | 87 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.311 | 0.365 | 0.354 | 37 | 64 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.388 | 0.330 | 0.341 | 34 | 68 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV03DETTB-DET2 | game_spread | 0.190 | 0.145 | 0.153 | 15 | 86 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-4 | game_total | 0.821 | 0.870 | 0.861 | 88 | 14 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6 | team_total | 0.137 | 0.090 | 0.098 | 10 | 92 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.197 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.132 | 0.175 | 0.165 | 18 | 83 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ2 | game_spread | 0.316 | 0.365 | 0.355 | 37 | 64 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-9 | game_total | 0.301 | 0.250 | 0.260 | 26 | 76 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 | team_total | 0.605 | 0.550 | 0.561 | 56 | 46 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.394 | 0.340 | 0.350 | 35 | 67 | yes | +0.028 | OK |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.554 | 0.505 | 0.515 | 51 | 50 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.221 | 0.265 | 0.256 | 27 | 74 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-9 | game_total | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.753 | 0.800 | 0.791 | 81 | 21 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR4 | team_total | 0.462 | 0.410 | 0.420 | 42 | 60 | yes | +0.025 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.233 | 0.275 | 0.266 | 28 | 73 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV03UTATOR-10 | game_total | 0.161 | 0.120 | 0.127 | 13 | 89 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-7 | game_total | 0.590 | 0.545 | 0.554 | 55 | 46 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6 | team_total | 0.097 | 0.065 | 0.071 | 7 | 94 | yes | +0.023 | OK |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.419 | 0.375 | 0.384 | 38 | 63 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.421 | 0.470 | 0.460 | 48 | 54 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.293 | 0.250 | 0.258 | 26 | 76 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV03DETTB-7 | game_total | 0.413 | 0.455 | 0.447 | 46 | 55 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV03UTATOR-7 | game_total | 0.587 | 0.545 | 0.553 | 55 | 46 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-EDM2 | game_spread | 0.261 | 0.225 | 0.232 | 23 | 78 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.384 | 0.340 | 0.349 | 35 | 67 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.495 | 0.535 | 0.527 | 54 | 47 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-DET4 | team_total | 0.281 | 0.240 | 0.248 | 25 | 77 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV03DETTB-DET3 | game_spread | 0.102 | 0.075 | 0.080 | 8 | 93 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV03UTATOR-TOR3 | team_total | 0.673 | 0.630 | 0.639 | 64 | 38 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV03DETTB-8 | game_total | 0.230 | 0.270 | 0.262 | 28 | 74 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-COL2 | game_spread | 0.372 | 0.335 | 0.342 | 34 | 67 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV03DETTB-4 | game_total | 0.836 | 0.870 | 0.864 | 88 | 14 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ6 | team_total | 0.050 | 0.075 | 0.069 | 8 | 93 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV03VGKPIT-8 | game_total | 0.350 | 0.315 | 0.322 | 32 | 69 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.163 | 0.130 | 0.136 | 14 | 88 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV03DALWSH-WSH2 | game_spread | 0.318 | 0.285 | 0.292 | 29 | 72 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV03CARNSH-CAR3 | game_spread | 0.262 | 0.295 | 0.288 | 30 | 71 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV03DETTB-9 | game_total | 0.156 | 0.185 | 0.179 | 19 | 82 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-DET5 | team_total | 0.130 | 0.105 | 0.110 | 11 | 90 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV03DALWSH-5 | game_total | 0.724 | 0.755 | 0.749 | 76 | 25 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-10 | game_total | 0.063 | 0.090 | 0.084 | 10 | 92 | no | +0.012 | OK |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.581 | 0.615 | 0.608 | 62 | 39 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL5 | team_total | 0.148 | 0.185 | 0.177 | 20 | 83 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-5 | game_total | 0.861 | 0.835 | 0.841 | 84 | 17 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-DET2 | team_total | 0.726 | 0.685 | 0.694 | 70 | 33 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV03ANAVAN-VAN6 | team_total | 0.118 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-6 | game_total | 0.696 | 0.660 | 0.667 | 67 | 35 | yes | +0.011 | OK |
| KXNHLGAME-26NOV03UTATOR-TOR | game_winner | 0.478 | 0.445 | 0.452 | 45 | 56 | yes | +0.011 | OK |
| KXNHLGAME-26NOV03UTATOR-UTA | game_winner | 0.522 | 0.555 | 0.548 | 56 | 45 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV03UTATOR-6 | game_total | 0.686 | 0.655 | 0.661 | 66 | 35 | yes | +0.010 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 0.478 | 0.497 | 0.167 | 0.214 | 7.06 | 6.78 | 0.989/0.998 | KXNHLTOTAL-26NOV03UTATOR-8 -0.047 |
| WPG @ MTL | 0.657 | 0.585 | 0.165 | 0.212 | 6.10 | 6.28 | 0.976/0.998 | KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG3 +0.078 |
| DET @ TBL | 0.620 | 0.621 | 0.172 | 0.209 | 5.98 | 6.22 | 0.958/1.004 | KXNHLTOTAL-26NOV03DETTB-7 +0.046 |
| STL @ NYR | 0.509 | 0.523 | 0.184 | 0.218 | 6.10 | 6.30 | 0.987/0.994 | KXNHLTOTAL-26NOV03STLNYR-7 +0.040 |
| MIN @ PHI | 0.419 | 0.521 | 0.179 | 0.222 | 5.97 | 6.01 | 0.992/0.996 | KXNHLGAME-26NOV03MINPHI-MIN -0.103 |
| VGK @ PIT | 0.515 | 0.493 | 0.164 | 0.218 | 6.81 | 6.59 | 1.034/1.004 | KXNHLTOTAL-26NOV03VGKPIT-8 -0.042 |
| DAL @ WSH | 0.554 | 0.534 | 0.184 | 0.217 | 5.82 | 6.18 | 0.961/0.987 | KXNHLTOTAL-26NOV03DALWSH-7 +0.065 |
| COL @ CBJ | 0.395 | 0.457 | 0.176 | 0.218 | 5.84 | 6.32 | 0.965/0.971 | KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 +0.106 |
| EDM @ NJD | 0.530 | 0.501 | 0.174 | 0.209 | 6.43 | 6.62 | 0.960/1.010 | KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 +0.045 |
| CAR @ NSH | 0.378 | 0.456 | 0.170 | 0.211 | 6.28 | 6.56 | 1.001/0.998 | KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3 +0.094 |
| ANA @ VAN | 0.423 | 0.457 | 0.162 | 0.210 | 7.11 | 6.91 | 1.022/1.017 | KXNHLTEAMTOTAL-26NOV03ANAVAN-ANA4 -0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 29 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 11c · p 0.1834 (adj 0.1613) · $7.69 · thesis TOR:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2234 (adj 0.2063) · $5.57 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 11c · p 0.1479 (adj 0.1347) · $3.17 · thesis UTA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 64c · p 0.6878 (adj 0.6734) · $9.37 · thesis UTA:SUPPRESSED
- Winnipeg over 5.5 goals scored YES @ 4c · p 0.0729 (adj 0.054) · $1.48 · thesis GAME:HIGH_EVENT
- Jake Evans: 1+ goals YES @ 15c · p 0.1884 (adj 0.1751) · $3.2 · thesis MTL:OFFENSE_4PLUS
- Charle-Edouard D'Astous: 1+ goals NO @ 88c · p 0.9248 (adj 0.9098) · $14.03 · thesis TBL:SUPPRESSED
- Alex DeBrincat: 1+ goals YES @ 31c · p 0.361 (adj 0.347) · $4.67 · thesis DET:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 66c · p 0.7381 (adj 0.6941) · $7.69 · thesis GAME:TIGHT
- Tye Kartye: 1+ goals YES @ 16c · p 0.1969 (adj 0.1839) · $2.89 · thesis NYR:OFFENSE_4PLUS
- Philadelphia wins by over 1.5 goals YES @ 20c · p 0.289 (adj 0.242) · $4.32 · thesis PHI:WINS_BY_2PLUS
- Nick Seeler: 1+ goals YES @ 3c · p 0.0468 (adj 0.0451) · $2.07 · thesis PHI:OFFENSE_4PLUS
- Matt Boldy: 1+ goals NO @ 63c · p 0.6866 (adj 0.67) · $9.68 · thesis MIN:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 17c · p 0.2136 (adj 0.199) · $3.27 · thesis PHI:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 13c · p 0.165 (adj 0.1537) · $3.05 · thesis PIT:OFFENSE_4PLUS
- Sidney Crosby: 1+ assists NO @ 54c · p 0.6175 (adj 0.5713) · $5.82 · thesis PIT:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2353 (adj 0.219) · $5.89 · thesis WSH:OFFENSE_4PLUS
- Miro Heiskanen: 1+ goals NO @ 87c · p 0.9042 (adj 0.8931) · $14.03 · thesis DAL:SUPPRESSED
- Arttu Hyry: 1+ goals YES @ 12c · p 0.151 (adj 0.142) · $2.92 · thesis DAL:OFFENSE_4PLUS
- Alex Ovechkin: 1+ goals YES @ 22c · p 0.2573 (adj 0.2467) · $3.26 · thesis WSH:OFFENSE_4PLUS
- Sean Monahan: 1+ goals YES @ 15c · p 0.1804 (adj 0.1716) · $2.52 · thesis CBJ:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 11c · p 0.1563 (adj 0.1422) · $4.58 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 23c · p 0.2885 (adj 0.2689) · $5.56 · thesis EDM:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 9c · p 0.1291 (adj 0.1118) · $2.66 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1138 (adj 0.0991) · $2.22 · thesis EDM:OFFENSE_4PLUS
- Jack Drury: 1+ goals YES @ 9c · p 0.1314 (adj 0.116) · $3.15 · thesis NSH:OFFENSE_4PLUS
- Adam Edstrom: 1+ goals YES @ 13c · p 0.1711 (adj 0.1583) · $3.36 · thesis NSH:OFFENSE_4PLUS
- Nashville over 4.5 goals scored YES @ 15c · p 0.2115 (adj 0.1758) · $1.53 · thesis NSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7172 (adj 0.7029) · $9.5 · thesis CAR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ TOR** · priced 166/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.45 (sd 7.17), pull risk 0.079
- UTA net: Sebastian Cossa (PROJECTED) exp shots 26.79, exp saves 23.13 (sd 6.47), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.403 | 0.500 | 52/52 | +0.059 | STANDARD |
| Teddy Blueger: 1+ goals | 0.183 | 0.095 | 11/92 | +0.067 | STANDARD |
| Morgan Rielly: 1+ assists | 0.344 | 0.260 | 28/76 | +0.050 | STANDARD |
| Morgan Rielly: 1+ points | 0.400 | 0.320 | 35/71 | +0.034 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.526 | 0.605 | 62/41 | +0.047 | STANDARD |
| Logan Cooley: 1+ points | 0.545 | 0.620 | 64/40 | +0.038 | STANDARD |

**WPG @ MTL** · priced 134/140 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.0, exp saves 23.59 (sd 6.4), pull risk 0.052
- WPG net: Nico Daws (PROJECTED) exp shots 27.07, exp saves 23.04 (sd 6.5), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cole Perfetti: 1+ points | 0.526 | 0.450 | 47/57 | +0.038 | STANDARD |
| Cole Perfetti: 1+ assists | 0.358 | 0.290 | 30/72 | +0.043 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.302 | 0.240 | 25/77 | +0.039 | STANDARD |
| Cole Caufield: 1+ assists | 0.366 | 0.425 | 44/59 | +0.027 | STANDARD |
| Jake Evans: 1+ goals | 0.188 | 0.135 | 15/88 | +0.029 | STANDARD |
| Adam Lowry: 1+ goals | 0.125 | 0.075 | 11/96 | +0.009 | STANDARD |

**DET @ TBL** · priced 153/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.01 (sd 6.21), pull risk 0.044
- DET net: John Gibson (PROJECTED) exp shots 27.95, exp saves 23.8 (sd 6.71), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 2+ points | 0.329 | 0.475 | 49/54 | +0.113 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.519 | 0.650 | 66/36 | +0.105 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.161 | 0.285 | 30/73 | +0.095 | STANDARD |
| Lucas Raymond: 1+ assists | 0.326 | 0.405 | 42/61 | +0.048 | STANDARD |
| John Carlson: 1+ assists | 0.312 | 0.375 | 39/64 | +0.032 | STANDARD |
| Emmitt Finnie: 1+ points | 0.491 | 0.430 | 44/58 | +0.034 | STANDARD |

**STL @ NYR** · priced 142/145 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 26.61, exp saves 23.05 (sd 6.33), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 26.51, exp saves 22.98 (sd 6.32), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Holloway: 1+ assists | 0.381 | 0.305 | 32/71 | +0.046 | STANDARD |
| Robert Thomas: 1+ assists | 0.418 | 0.475 | 50/55 | +0.015 | STANDARD |
| Alexis Lafreniere: 1+ points | 0.607 | 0.550 | 57/47 | +0.020 | STANDARD |
| Dylan Holloway: 1+ points | 0.545 | 0.490 | 50/52 | +0.028 | STANDARD |
| Tye Kartye: 1+ goals | 0.197 | 0.145 | 16/87 | +0.027 | STANDARD |
| Alexis Lafreniere: 1+ goals | 0.350 | 0.305 | 32/71 | +0.015 | STANDARD |

**MIN @ PHI** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 28.47, exp saves 24.77 (sd 6.67), pull risk 0.052
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 25.89, exp saves 22.45 (sd 6.21), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.243 | 0.405 | 42/61 | +0.131 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.385 | 0.530 | 55/49 | +0.108 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.360 | 0.490 | 50/52 | +0.102 | STANDARD |
| Matt Boldy: 1+ assists | 0.381 | 0.500 | 52/52 | +0.082 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.602 | 0.715 | 78/35 | +0.032 | STANDARD |
| Travis Sanheim: 1+ points | 0.399 | 0.290 | 30/72 | +0.084 | STANDARD |

**VGK @ PIT** · priced 151/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.98, exp saves 23.33 (sd 6.56), pull risk 0.065
- VGK net: Adin Hill (PROJECTED) exp shots 27.28, exp saves 23.58 (sd 6.54), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sidney Crosby: 1+ assists | 0.383 | 0.475 | 49/54 | +0.060 | STANDARD |
| Mitch Marner: 1+ assists | 0.428 | 0.520 | 54/50 | +0.055 | STANDARD |
| Jack Eichel: 1+ assists | 0.444 | 0.530 | 55/49 | +0.049 | STANDARD |
| Sidney Crosby: 1+ points | 0.574 | 0.645 | 66/37 | +0.040 | STANDARD |
| Erik Karlsson: 1+ assists | 0.449 | 0.520 | 54/50 | +0.033 | STANDARD |
| Sidney Crosby: 2+ assists | 0.082 | 0.145 | 17/88 | +0.031 | STANDARD |

**DAL @ WSH** · priced 152/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 26.25, exp saves 22.85 (sd 6.2), pull risk 0.053
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.46, exp saves 21.79 (sd 6.19), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Miro Heiskanen: 1+ points | 0.450 | 0.555 | 57/46 | +0.073 | STANDARD |
| Miro Heiskanen: 2+ points | 0.121 | 0.210 | 23/81 | +0.059 | STANDARD |
| Wyatt Johnston: 1+ assists | 0.347 | 0.425 | 44/59 | +0.046 | STANDARD |
| Miro Heiskanen: 1+ assists | 0.393 | 0.470 | 48/54 | +0.050 | STANDARD |
| Mikko Rantanen: 2+ points | 0.206 | 0.280 | 29/73 | +0.051 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.424 | 0.490 | 50/52 | +0.038 | STANDARD |

**COL @ CBJ** · priced 155/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 29.48, exp saves 25.57 (sd 6.93), pull risk 0.056
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.38 (sd 6.4), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Werenski: 1+ assists | 0.473 | 0.560 | 57/45 | +0.059 | STANDARD |
| Cale Makar: 1+ points | 0.537 | 0.620 | 63/39 | +0.056 | STANDARD |
| Matthew Knies: 1+ assists | 0.289 | 0.360 | 37/65 | +0.045 | STANDARD |
| Zach Werenski: 2+ points | 0.211 | 0.280 | 29/73 | +0.045 | STANDARD |
| Cale Makar: 2+ points | 0.181 | 0.250 | 26/76 | +0.046 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.308 | 0.375 | 39/64 | +0.035 | STANDARD |

**EDM @ NJD** · priced 156/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.46, exp saves 22.84 (sd 6.45), pull risk 0.069
- EDM net: Tristan Jarry (PROJECTED) exp shots 29.41, exp saves 25.32 (sd 7.0), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.535 | 0.650 | 66/36 | +0.088 | STANDARD |
| Jack Hughes: 1+ assists | 0.408 | 0.520 | 53/49 | +0.084 | STANDARD |
| Connor McDavid: 2+ points | 0.373 | 0.480 | 50/54 | +0.070 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.530 | 0.440 | 46/58 | +0.053 | STANDARD |
| Connor McDavid: 2+ assists | 0.176 | 0.260 | 31/79 | +0.022 | STANDARD |
| Vasily Podkolzin: 1+ goals | 0.288 | 0.210 | 23/81 | +0.046 | STANDARD |

**CAR @ NSH** · priced 147/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 31.84, exp saves 27.16 (sd 7.45), pull risk 0.083
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.26 (sd 6.07), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.354 | 0.495 | 51/52 | +0.109 | STANDARD |
| Sebastian Aho: 1+ points | 0.533 | 0.655 | 67/36 | +0.090 | STANDARD |
| Sebastian Aho: 2+ points | 0.180 | 0.300 | 32/72 | +0.086 | STANDARD |
| Sebastian Aho: 2+ assists | 0.070 | 0.150 | 17/87 | +0.052 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.345 | 0.420 | 43/59 | +0.048 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.527 | 0.600 | 61/41 | +0.046 | STANDARD |

**ANA @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Kevin Lankinen (PROJECTED) exp shots 30.41, exp saves 25.98 (sd 7.22), pull risk 0.083
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.99, exp saves 21.59 (sd 6.19), pull risk 0.072

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
