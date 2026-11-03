# NHL slate 2026-11-03 — RESEARCH_ONLY

generated 2026-11-03T05:34:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 2253 · contracts joined: 561 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 286, 'NO_EDGE': 160, 'OK': 115}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'game_early_goal': 11, 'game_winner': 22, 'game_overtime': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 2026-11-04T00:00:00Z | T-12h | 0.467 | 0.533 | 0.164 | 6.98 | 3.37 | 3.61 | 51 (25/26) | CONFIRMED/PROJECTED |
| WPG @ MTL | 2026-11-04T00:00:00Z | T-12h | 0.638 | 0.362 | 0.174 | 5.97 | 3.42 | 2.55 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ TBL | 2026-11-04T00:00:00Z | T-12h | 0.623 | 0.377 | 0.171 | 5.99 | 3.38 | 2.62 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ NYR | 2026-11-04T00:00:00Z | T-12h | 0.507 | 0.493 | 0.183 | 6.10 | 3.08 | 3.02 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ PHI | 2026-11-04T00:00:00Z | T-12h | 0.440 | 0.560 | 0.180 | 5.79 | 2.72 | 3.07 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ PIT | 2026-11-04T00:00:00Z | T-12h | 0.484 | 0.516 | 0.163 | 6.63 | 3.27 | 3.36 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ WSH | 2026-11-04T00:00:00Z | T-12h | 0.552 | 0.448 | 0.184 | 5.81 | 3.06 | 2.75 | 51 (25/26) | PROJECTED/PROJECTED |
| COL @ CBJ | 2026-11-04T00:00:00Z | T-12h | 0.398 | 0.602 | 0.178 | 5.84 | 2.60 | 3.24 | 51 (25/26) | PROJECTED/CONFIRMED |
| EDM @ NJD | 2026-11-04T00:30:00Z | T-12h | 0.507 | 0.493 | 0.177 | 6.30 | 3.17 | 3.13 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ NSH | 2026-11-04T01:00:00Z | T-12h | 0.376 | 0.624 | 0.164 | 6.27 | 2.74 | 3.53 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ VAN | 2026-11-04T02:00:00Z | T-12h | 0.434 | 0.566 | 0.161 | 7.10 | 3.33 | 3.77 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV03DETTB-TB4 | team_total | 0.452 | 0.550 | 0.530 | 56 | 46 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 | team_total | 0.485 | 0.585 | 0.565 | 60 | 43 | no | +0.068 | OK |
| KXNHLGAME-26NOV03EDMNJ-NJ | game_winner | 0.507 | 0.595 | 0.578 | 60 | 41 | no | +0.066 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB3 | game_spread | 0.250 | 0.345 | 0.325 | 36 | 67 | no | +0.064 | OK |
| KXNHLGAME-26NOV03DETTB-TB | game_winner | 0.623 | 0.705 | 0.689 | 71 | 30 | no | +0.062 | OK |
| KXNHLSPREAD-26NOV03DETTB-TB2 | game_spread | 0.391 | 0.475 | 0.458 | 48 | 53 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ4 | team_total | 0.277 | 0.370 | 0.350 | 39 | 65 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB3 | team_total | 0.670 | 0.755 | 0.739 | 77 | 26 | no | +0.057 | OK |
| KXNHLGAME-26NOV03EDMNJ-EDM | game_winner | 0.493 | 0.415 | 0.430 | 42 | 59 | yes | +0.056 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-7 | game_total | 0.388 | 0.465 | 0.449 | 47 | 54 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB5 | team_total | 0.251 | 0.335 | 0.317 | 35 | 68 | no | +0.053 | OK |
| KXNHLGAME-26NOV03DETTB-DET | game_winner | 0.377 | 0.305 | 0.319 | 31 | 70 | yes | +0.052 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-6 | game_total | 0.501 | 0.585 | 0.569 | 60 | 43 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB2 | team_total | 0.848 | 0.905 | 0.895 | 91 | 10 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ2 | team_total | 0.723 | 0.800 | 0.786 | 82 | 22 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-8 | game_total | 0.212 | 0.280 | 0.265 | 29 | 73 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ5 | team_total | 0.127 | 0.195 | 0.180 | 21 | 82 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN4 | team_total | 0.380 | 0.460 | 0.444 | 48 | 56 | no | +0.042 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-EDM2 | game_spread | 0.284 | 0.225 | 0.236 | 23 | 78 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-TB6 | team_total | 0.119 | 0.175 | 0.162 | 18 | 83 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN5 | team_total | 0.196 | 0.265 | 0.250 | 28 | 75 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN3 | team_total | 0.604 | 0.675 | 0.661 | 69 | 34 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN3 | game_spread | 0.197 | 0.255 | 0.243 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV03MINPHI-MIN2 | game_spread | 0.324 | 0.385 | 0.372 | 39 | 62 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ2 | game_spread | 0.295 | 0.355 | 0.343 | 36 | 65 | no | +0.039 | OK |
| KXNHLSPREAD-26NOV03DETTB-DET2 | game_spread | 0.187 | 0.135 | 0.144 | 14 | 87 | yes | +0.039 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-NJ3 | game_spread | 0.179 | 0.240 | 0.227 | 25 | 77 | no | +0.038 | OK |
| KXNHLGAME-26NOV03COLCBJ-CBJ | game_winner | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLGAME-26NOV03COLCBJ-COL | game_winner | 0.602 | 0.545 | 0.557 | 55 | 46 | yes | +0.035 | OK |
| KXNHLGAME-26NOV03DALWSH-DAL | game_winner | 0.448 | 0.505 | 0.494 | 51 | 50 | no | +0.034 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-9 | game_total | 0.297 | 0.245 | 0.255 | 25 | 76 | yes | +0.034 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-5 | game_total | 0.724 | 0.780 | 0.770 | 79 | 23 | no | +0.033 | OK |
| KXNHLGAME-26NOV03MINPHI-MIN | game_winner | 0.560 | 0.615 | 0.604 | 62 | 39 | no | +0.033 | OK |
| KXNHLGAME-26NOV03MINPHI-PHI | game_winner | 0.440 | 0.385 | 0.396 | 39 | 62 | yes | +0.033 | OK |
| KXNHLTOTAL-26NOV03MINPHI-6 | game_total | 0.490 | 0.545 | 0.534 | 55 | 46 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-4 | game_total | 0.819 | 0.870 | 0.861 | 88 | 14 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN2 | team_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL2 | game_spread | 0.234 | 0.285 | 0.274 | 29 | 72 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ2 | game_spread | 0.196 | 0.245 | 0.235 | 25 | 76 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV03DALWSH-DAL3 | game_spread | 0.130 | 0.175 | 0.165 | 18 | 83 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM4 | team_total | 0.395 | 0.335 | 0.347 | 35 | 68 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL3 | team_total | 0.525 | 0.580 | 0.569 | 59 | 43 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-CBJ3 | game_spread | 0.104 | 0.150 | 0.140 | 16 | 86 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV03DETTB-8 | game_total | 0.229 | 0.280 | 0.269 | 29 | 73 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-9 | game_total | 0.145 | 0.185 | 0.176 | 19 | 82 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL2 | team_total | 0.754 | 0.800 | 0.791 | 81 | 21 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5 | team_total | 0.215 | 0.165 | 0.174 | 18 | 85 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL4 | team_total | 0.310 | 0.365 | 0.354 | 38 | 65 | no | +0.024 | OK |
| KXNHLGAME-26NOV03DALWSH-WSH | game_winner | 0.552 | 0.500 | 0.510 | 51 | 51 | yes | +0.024 | OK |
| KXNHLSPREAD-26NOV03DALWSH-WSH2 | game_spread | 0.318 | 0.275 | 0.283 | 28 | 73 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV03MINPHI-7 | game_total | 0.379 | 0.425 | 0.416 | 43 | 58 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV03MINPHI-8 | game_total | 0.204 | 0.250 | 0.240 | 26 | 76 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-NJ2 | team_total | 0.818 | 0.860 | 0.852 | 87 | 15 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV03EDMNJ-EDM3 | game_spread | 0.171 | 0.130 | 0.137 | 14 | 88 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV03DALWSH-DAL5 | team_total | 0.147 | 0.190 | 0.181 | 20 | 82 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV03MINPHI-9 | game_total | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV03DETTB-7 | game_total | 0.412 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3 | team_total | 0.608 | 0.555 | 0.566 | 57 | 46 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM6 | team_total | 0.095 | 0.065 | 0.070 | 7 | 94 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV03DALWSH-6 | game_total | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV03UTATOR-8 | game_total | 0.375 | 0.330 | 0.339 | 34 | 68 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV03MINPHI-5 | game_total | 0.719 | 0.755 | 0.748 | 76 | 25 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-8 | game_total | 0.394 | 0.350 | 0.359 | 36 | 66 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV03MINPHI-MIN6 | team_total | 0.086 | 0.115 | 0.109 | 12 | 89 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-NJ4 | team_total | 0.406 | 0.455 | 0.445 | 47 | 56 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV03UTATOR-9 | game_total | 0.280 | 0.240 | 0.248 | 25 | 77 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ6 | team_total | 0.049 | 0.080 | 0.073 | 9 | 93 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV03UTATOR-7 | game_total | 0.574 | 0.535 | 0.543 | 54 | 47 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV03EDMNJ-NJ3 | team_total | 0.618 | 0.665 | 0.656 | 68 | 35 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV03DETTB-6 | game_total | 0.528 | 0.575 | 0.566 | 59 | 44 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV03DETTB-DET5 | team_total | 0.131 | 0.105 | 0.110 | 11 | 90 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV03MINPHI-4 | game_total | 0.817 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV03COLCBJ-COL2 | game_spread | 0.369 | 0.335 | 0.342 | 34 | 67 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-10 | game_total | 0.161 | 0.130 | 0.136 | 14 | 88 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV03COLCBJ-10 | game_total | 0.062 | 0.090 | 0.084 | 10 | 92 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-5 | game_total | 0.862 | 0.835 | 0.841 | 84 | 17 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV03DETTB-9 | game_total | 0.157 | 0.185 | 0.179 | 19 | 82 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-6 | game_total | 0.697 | 0.655 | 0.664 | 67 | 36 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV03ANAVAN-7 | game_total | 0.589 | 0.550 | 0.558 | 56 | 46 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV03DETTB-5 | game_total | 0.747 | 0.780 | 0.774 | 79 | 23 | no | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ TOR | 0.467 | 0.498 | 0.164 | 0.213 | 6.98 | 6.78 | 0.989/0.993 | KXNHLTEAMTOTAL-26NOV03UTATOR-UTA5 -0.041 |
| WPG @ MTL | 0.638 | 0.589 | 0.174 | 0.214 | 5.97 | 6.28 | 0.976/1.002 | KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG4 +0.075 |
| DET @ TBL | 0.623 | 0.626 | 0.171 | 0.209 | 5.99 | 6.26 | 0.958/1.016 | KXNHLTOTAL-26NOV03DETTB-7 +0.051 |
| STL @ NYR | 0.507 | 0.523 | 0.183 | 0.218 | 6.10 | 6.30 | 0.987/0.994 | KXNHLTOTAL-26NOV03STLNYR-7 +0.036 |
| MIN @ PHI | 0.440 | 0.520 | 0.180 | 0.218 | 5.79 | 6.01 | 0.994/0.996 | KXNHLTEAMTOTAL-26NOV03MINPHI-PHI3 +0.088 |
| VGK @ PIT | 0.484 | 0.490 | 0.163 | 0.219 | 6.63 | 6.59 | 1.034/1.004 | KXNHLSPREAD-26NOV03VGKPIT-VGK2 -0.017 |
| DAL @ WSH | 0.552 | 0.534 | 0.184 | 0.217 | 5.81 | 6.18 | 0.961/0.987 | KXNHLTOTAL-26NOV03DALWSH-7 +0.066 |
| COL @ CBJ | 0.398 | 0.457 | 0.178 | 0.218 | 5.84 | 6.32 | 0.965/0.971 | KXNHLTEAMTOTAL-26NOV03COLCBJ-CBJ3 +0.105 |
| EDM @ NJD | 0.507 | 0.493 | 0.177 | 0.213 | 6.30 | 6.58 | 0.960/0.998 | KXNHLTOTAL-26NOV03EDMNJ-7 +0.052 |
| CAR @ NSH | 0.376 | 0.456 | 0.164 | 0.211 | 6.27 | 6.56 | 1.001/0.998 | KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3 +0.095 |
| ANA @ VAN | 0.434 | 0.439 | 0.161 | 0.209 | 7.10 | 6.83 | 1.026/0.986 | KXNHLTOTAL-26NOV03ANAVAN-8 -0.048 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Detroit wins by over 1.5 goals YES @ 14c · p 0.1906 (adj 0.1628) · $2.08 · thesis DET:WINS_BY_2PLUS
- Tampa Bay wins by over 1.5 goals NO @ 53c · p 0.6056 (adj 0.5653) · $6.46 · thesis GAME:TIGHT
- Detroit over 4.5 goals scored YES @ 11c · p 0.1515 (adj 0.1283) · $1.32 · thesis DET:OFFENSE_4PLUS
- Philadelphia wins by over 1.5 goals YES @ 21c · p 0.2894 (adj 0.2447) · $3.64 · thesis PHI:WINS_BY_2PLUS
- Minnesota wins by over 1.5 goals NO @ 62c · p 0.7477 (adj 0.6614) · $11.19 · thesis PHI:WINS
- Philadelphia over 4.5 goals scored YES @ 14c · p 0.1938 (adj 0.1644) · $1.71 · thesis PHI:OFFENSE_4PLUS
- Minnesota wins by over 2.5 goals NO @ 75c · p 0.8468 (adj 0.7806) · $6.08 · thesis PHI:WINS
- Edmonton over 5.5 goals scored YES @ 7c · p 0.1126 (adj 0.0888) · $2.16 · thesis GAME:HIGH_EVENT
- Edmonton wins by over 1.5 goals YES @ 23c · p 0.2921 (adj 0.2586) · $2.01 · thesis EDM:WINS_BY_2PLUS
- New Jersey wins by over 1.5 goals NO @ 65c · p 0.7168 (adj 0.6809) · $7.21 · thesis EDM:WINS
- Full Game: Over 6.5 goals scored YES @ 46c · p 0.5212 (adj 0.4881) · $2.67 · thesis GAME:HIGH_EVENT
- Nashville wins by over 1.5 goals YES @ 19c · p 0.2441 (adj 0.2146) · $2.49 · thesis NSH:WINS_BY_2PLUS
- Carolina wins by over 1.5 goals NO @ 59c · p 0.6649 (adj 0.6225) · $6.78 · thesis NSH:WINS
- Nashville over 3.5 goals scored YES @ 32c · p 0.3909 (adj 0.3479) · $1.12 · thesis NSH:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ TOR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.7, exp saves 26.53 (sd 7.32), pull risk 0.072
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.79, exp saves 23.19 (sd 6.45), pull risk 0.071

**WPG @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.0, exp saves 23.57 (sd 6.35), pull risk 0.051
- WPG net: Stuart Skinner (PROJECTED) exp shots 27.07, exp saves 23.05 (sd 6.5), pull risk 0.073

**DET @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.15, exp saves 23.0 (sd 6.12), pull risk 0.046
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.95, exp saves 23.77 (sd 6.71), pull risk 0.081

**STL @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 26.61, exp saves 23.05 (sd 6.33), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 26.51, exp saves 22.98 (sd 6.32), pull risk 0.061

**MIN @ PHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 28.47, exp saves 24.77 (sd 6.7), pull risk 0.053
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 25.89, exp saves 22.45 (sd 6.19), pull risk 0.054

**VGK @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 26.98, exp saves 23.29 (sd 6.51), pull risk 0.069
- VGK net: Carter Hart (PROJECTED) exp shots 27.28, exp saves 23.6 (sd 6.56), pull risk 0.068

**DAL @ WSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 26.25, exp saves 22.85 (sd 6.2), pull risk 0.053
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.46, exp saves 21.79 (sd 6.19), pull risk 0.068

**COL @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 29.48, exp saves 25.57 (sd 6.93), pull risk 0.056
- COL net: Scott Wedgewood (CONFIRMED) exp shots 26.96, exp saves 23.38 (sd 6.4), pull risk 0.057

**EDM @ NJD** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.46, exp saves 22.87 (sd 6.45), pull risk 0.067
- EDM net: Matt Tomkins (PROJECTED) exp shots 29.41, exp saves 25.37 (sd 6.94), pull risk 0.071

**CAR @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 31.84, exp saves 27.16 (sd 7.45), pull risk 0.083
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.43, exp saves 21.26 (sd 6.07), pull risk 0.062

**ANA @ VAN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.41, exp saves 25.97 (sd 7.28), pull risk 0.084
- ANA net: Laurent Brossoit (PROJECTED) exp shots 24.99, exp saves 21.61 (sd 6.19), pull risk 0.072

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
