# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T17:13:22Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4682 · contracts joined: 2461 (unjoined to any game: 1871)
gates: {'UNSUPPORTED': 2186, 'OK': 188, 'NO_EDGE': 87}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 330, 'game_early_goal': 11, 'first_goal': 403, 'game_winner': 22, 'player_goals': 701, 'game_overtime': 11, 'player_points': 454, 'goalie_saves': 12, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-3h | 0.449 | 0.551 | 0.165 | 6.68 | 3.17 | 3.51 | 227 (25/202) | PROBABLE/PROBABLE |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-3h | 0.567 | 0.433 | 0.175 | 6.28 | 3.36 | 2.92 | 235 (25/210) | CONFIRMED/CONFIRMED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-3h | 0.619 | 0.381 | 0.177 | 6.02 | 3.38 | 2.63 | 216 (25/191) | PROBABLE/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-3h | 0.624 | 0.376 | 0.162 | 6.82 | 3.83 | 2.99 | 207 (25/182) | CONFIRMED/CONFIRMED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-3h | 0.456 | 0.544 | 0.175 | 6.00 | 2.87 | 3.13 | 219 (25/194) | PROBABLE/CONFIRMED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-6h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 216 (25/191) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-6h | 0.493 | 0.507 | 0.180 | 5.82 | 2.89 | 2.93 | 247 (25/222) | CONFIRMED/PROBABLE |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-6h | 0.532 | 0.468 | 0.175 | 6.40 | 3.30 | 3.10 | 235 (25/210) | PROBABLE/CONFIRMED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-6h | 0.540 | 0.460 | 0.181 | 5.99 | 3.12 | 2.87 | 221 (25/196) | CONFIRMED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-6h | 0.562 | 0.438 | 0.163 | 6.66 | 3.53 | 3.13 | 229 (25/204) | CONFIRMED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-6h | 0.666 | 0.334 | 0.162 | 6.25 | 3.66 | 2.58 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.360 | 0.225 | 0.249 | 23 | 78 | yes | +0.118 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.574 | 0.445 | 0.471 | 45 | 56 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.786 | 0.675 | 0.699 | 68 | 33 | yes | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.191 | 0.095 | 0.110 | 10 | 91 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.389 | 0.495 | 0.473 | 50 | 51 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.555 | 0.534 | 56 | 45 | no | +0.083 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.376 | 0.275 | 0.294 | 28 | 73 | yes | +0.082 | OK |
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.624 | 0.725 | 0.706 | 73 | 28 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.355 | 0.333 | 36 | 65 | no | +0.081 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.456 | 0.555 | 0.535 | 56 | 45 | no | +0.077 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.544 | 0.445 | 0.465 | 45 | 56 | yes | +0.077 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.381 | 0.285 | 0.303 | 29 | 72 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.299 | 0.395 | 0.375 | 40 | 61 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.250 | 0.345 | 0.325 | 35 | 66 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.412 | 0.505 | 0.486 | 51 | 50 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.283 | 0.375 | 0.356 | 38 | 63 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.333 | 0.425 | 0.406 | 43 | 58 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.139 | 0.225 | 0.205 | 23 | 78 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.352 | 0.265 | 0.281 | 27 | 74 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.247 | 0.335 | 0.316 | 34 | 67 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.544 | 0.450 | 0.469 | 46 | 56 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.346 | 0.435 | 0.417 | 44 | 57 | no | +0.067 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.619 | 0.705 | 0.689 | 71 | 30 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.562 | 0.475 | 0.492 | 48 | 53 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-6 | game_total | 0.570 | 0.485 | 0.502 | 49 | 52 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.441 | 0.525 | 0.508 | 53 | 48 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.666 | 0.745 | 0.730 | 75 | 26 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.334 | 0.255 | 0.270 | 26 | 75 | yes | +0.061 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-8 | game_total | 0.271 | 0.195 | 0.209 | 20 | 81 | yes | +0.060 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.197 | 0.125 | 0.137 | 13 | 88 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.555 | 0.640 | 0.624 | 65 | 37 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.257 | 0.185 | 0.198 | 19 | 82 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.670 | 0.750 | 0.735 | 76 | 26 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.610 | 0.685 | 0.671 | 69 | 32 | no | +0.054 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.317 | 0.245 | 0.258 | 25 | 76 | yes | +0.053 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.551 | 0.475 | 0.490 | 48 | 53 | yes | +0.053 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.449 | 0.525 | 0.510 | 53 | 48 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-7 | game_total | 0.458 | 0.385 | 0.399 | 39 | 62 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.167 | 0.240 | 0.224 | 25 | 77 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.719 | 0.790 | 0.777 | 80 | 22 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.494 | 0.565 | 0.551 | 57 | 44 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15VANFLA-6 | game_total | 0.654 | 0.585 | 0.599 | 59 | 42 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.774 | 0.840 | 0.828 | 85 | 17 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.350 | 0.280 | 0.293 | 29 | 73 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.569 | 0.640 | 0.626 | 65 | 37 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.087 | 0.030 | 0.037 | 4 | 98 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.251 | 0.315 | 0.302 | 32 | 69 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.311 | 0.380 | 0.366 | 39 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI5 | team_total | 0.180 | 0.125 | 0.135 | 13 | 88 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.575 | 0.562 | 58 | 43 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT15SEATB-5 | game_total | 0.748 | 0.805 | 0.794 | 81 | 20 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR4 | team_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.149 | 0.205 | 0.193 | 21 | 80 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.383 | 0.445 | 0.432 | 45 | 56 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-8 | game_total | 0.208 | 0.265 | 0.253 | 27 | 74 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.180 | 0.167 | 19 | 83 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.341 | 0.280 | 0.292 | 29 | 73 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.722 | 0.665 | 0.677 | 67 | 34 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI2 | team_total | 0.721 | 0.775 | 0.765 | 78 | 23 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.173 | 0.235 | 0.222 | 25 | 78 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-9 | game_total | 0.194 | 0.145 | 0.154 | 15 | 86 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT15SEATB-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.818 | 0.870 | 0.861 | 88 | 14 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.714 | 0.765 | 0.755 | 77 | 24 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.851 | 0.895 | 0.887 | 90 | 11 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.717 | 0.775 | 0.764 | 79 | 24 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6 | team_total | 0.160 | 0.205 | 0.195 | 21 | 80 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.540 | 0.529 | 55 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 | team_total | 0.476 | 0.425 | 0.435 | 43 | 58 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.476 | 0.420 | 0.431 | 43 | 59 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.113 | 0.070 | 0.077 | 8 | 94 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT15VANFLA-5 | game_total | 0.839 | 0.795 | 0.805 | 80 | 21 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT15VANFLA-10 | game_total | 0.134 | 0.085 | 0.093 | 10 | 93 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR2 | team_total | 0.814 | 0.855 | 0.847 | 86 | 15 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF6 | team_total | 0.144 | 0.100 | 0.108 | 11 | 91 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.878 | 0.915 | 0.908 | 92 | 9 | no | +0.027 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 0.449 | 0.510 | 0.165 | 0.214 | 6.68 | 6.48 | 0.983/1.000 | KXNHLSPREAD-26OCT15BUFTOR-BUF2 -0.066 |
| NYI @ OTT | 0.567 | 0.593 | 0.175 | 0.218 | 6.28 | 6.11 | 0.968/0.978 | KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 -0.038 |
| SEA @ TBL | 0.619 | 0.582 | 0.177 | 0.218 | 6.02 | 6.08 | 0.952/1.005 | KXNHLTEAMTOTAL-26OCT15SEATB-SEA3 +0.043 |
| VAN @ FLA | 0.624 | 0.574 | 0.162 | 0.214 | 6.82 | 6.43 | 0.991/1.034 | KXNHLTEAMTOTAL-26OCT15VANFLA-FLA5 -0.083 |
| NYR @ NJD | 0.456 | 0.511 | 0.175 | 0.222 | 6.00 | 6.05 | 0.994/0.988 | KXNHLGAME-26OCT15NYRNJ-NJ +0.055 |
| PHI @ DET | 0.603 | 0.517 | 0.179 | 0.218 | 5.79 | 5.82 | 1.024/0.991 | KXNHLGAME-26OCT15PHIDET-DET -0.086 |
| WPG @ CHI | 0.493 | 0.491 | 0.180 | 0.218 | 5.82 | 6.17 | 0.988/0.996 | KXNHLTOTAL-26OCT15WPGCHI-7 +0.063 |
| SJS @ NSH | 0.532 | 0.527 | 0.175 | 0.218 | 6.40 | 6.51 | 1.002/1.021 | KXNHLTOTAL-26OCT15SJNSH-7 +0.021 |
| STL @ MIN | 0.540 | 0.555 | 0.181 | 0.220 | 5.99 | 6.39 | 0.991/0.993 | KXNHLTOTAL-26OCT15STLMIN-7 +0.074 |
| UTA @ EDM | 0.562 | 0.580 | 0.163 | 0.207 | 6.66 | 6.78 | 0.994/0.992 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 +0.034 |
| CGY @ VGK | 0.666 | 0.660 | 0.162 | 0.198 | 6.25 | 6.17 | 1.003/0.997 | KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 -0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Owen Power: 1+ goals NO @ 88c · p 0.915 (adj 0.905) · $7.53 · thesis BUF:SUPPRESSED
- Gavin McKenna: 1+ assists NO @ 70c · p 0.7632 (adj 0.7291) · $5.17 · thesis TOR:SUPPRESSED
- Sergei Bobrovsky: 26+ saves YES @ 50c · p 0.5658 (adj 0.5304) · $2.43 · thesis TOR:NET_HIGH_VOLUME
- Tage Thompson: 1+ assists NO @ 58c · p 0.6455 (adj 0.6078) · $2.29 · thesis BUF:SUPPRESSED
- Andre Burakovsky: 1+ assists NO @ 75c · p 0.8277 (adj 0.7863) · $7.53 · thesis OTT:SUPPRESSED
- Warren Foegele: 1+ goals YES @ 14c · p 0.1763 (adj 0.166) · $1.92 · thesis OTT:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 10c · p 0.131 (adj 0.1207) · $1.45 · thesis NYI:OFFENSE_4PLUS
- Matias Maccelli: 1+ assists NO @ 66c · p 0.7312 (adj 0.6906) · $5.17 · thesis NYI:SUPPRESSED
- John Carlson: 1+ assists NO @ 51c · p 0.6801 (adj 0.5663) · $4.84 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals NO @ 61c · p 0.671 (adj 0.6545) · $4.07 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6404 (adj 0.6253) · $2.38 · thesis TBL:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 62c · p 0.7005 (adj 0.6779) · $5.65 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 62c · p 0.6965 (adj 0.6761) · $5.65 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 63c · p 0.7671 (adj 0.6747) · $4.49 · thesis VAN:WINS
- Jake DeBrusk: 1+ goals YES @ 27c · p 0.3212 (adj 0.3071) · $2.01 · thesis VAN:OFFENSE_4PLUS
- Matt Rempe: 1+ goals YES @ 6c · p 0.0903 (adj 0.0815) · $1.58 · thesis NYR:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 73c · p 0.7767 (adj 0.7625) · $6.4 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 62c · p 0.6712 (adj 0.6572) · $4.9 · thesis NJD:SUPPRESSED
- Amadeus Lombardi: 1+ goals YES @ 10c · p 0.129 (adj 0.1192) · $1.29 · thesis NJD:OFFENSE_4PLUS
- Nate Danielson: 1+ goals NO @ 84c · p 0.8871 (adj 0.8728) · $7.53 · thesis DET:SUPPRESSED
- Sheldon Dries: 1+ goals YES @ 9c · p 0.1206 (adj 0.1129) · $1.69 · thesis DET:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 19c · p 0.2329 (adj 0.2209) · $2.23 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 15c · p 0.1828 (adj 0.1721) · $1.4 · thesis PHI:OFFENSE_4PLUS
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7922 (adj 0.7767) · $7.45 · thesis CHI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 13c · p 0.1617 (adj 0.1525) · $1.49 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 27c · p 0.3135 (adj 0.3014) · $2.22 · thesis CHI:OFFENSE_4PLUS
- Connor Bedard: 1+ goals NO @ 66c · p 0.702 (adj 0.689) · $3.84 · thesis CHI:SUPPRESSED
- Collin Graf: 1+ goals YES @ 13c · p 0.1689 (adj 0.1579) · $2.11 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 20c · p 0.2442 (adj 0.2319) · $2.48 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2019 (adj 0.1927) · $1.5 · thesis SJS:OFFENSE_4PLUS
- Macklin Celebrini: 1+ assists NO @ 43c · p 0.5751 (adj 0.4588) · $2.84 · thesis SJS:SUPPRESSED
- Ross Johnston: 1+ goals YES @ 5c · p 0.0754 (adj 0.0716) · $1.69 · thesis STL:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 24c · p 0.3184 (adj 0.2742) · $2.28 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 19c · p 0.2323 (adj 0.2192) · $2.04 · thesis MIN:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.2168 (adj 0.2001) · $3.32 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1291 (adj 0.1193) · $2.41 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4519 (adj 0.3629) · $4.37 · thesis EDM:SUPPRESSED
- Filip Hallander: 1+ goals YES @ 14c · p 0.179 (adj 0.1693) · $2.15 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7416 (adj 0.7249) · $7.45 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6902 (adj 0.6476) · $3.32 · thesis GAME:TIGHT
- Vegas over 5.5 goals scored NO @ 80c · p 0.855 (adj 0.825) · $2.61 · thesis CGY:WINS
- Jack Eichel: 1+ goals NO @ 63c · p 0.6755 (adj 0.6629) · $3.84 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 30.87, exp saves 26.64 (sd 7.16), pull risk 0.068
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.02, exp saves 22.48 (sd 6.28), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 27+ saves | 0.256 | 0.405 | 42/61 | +0.117 |  |
| Tage Thompson: 1+ assists | 0.354 | 0.430 | 44/58 | +0.048 | STANDARD |
| Sergei Bobrovsky: 26+ saves | 0.566 | 0.495 | 50/51 | +0.048 |  |
| Tage Thompson: 2+ points | 0.225 | 0.295 | 31/72 | +0.041 | STANDARD |
| Gavin McKenna: 1+ assists | 0.237 | 0.305 | 31/70 | +0.049 | PRIOR_HEAVY |
| Darren Raddysh: 1+ assists | 0.354 | 0.420 | 43/59 | +0.039 | STANDARD |

**NYI @ OTT** · priced 176/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (CONFIRMED) exp shots 25.99, exp saves 22.66 (sd 6.14), pull risk 0.047
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 27.57, exp saves 23.45 (sd 6.64), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Semyon Varlamov: 26+ saves | 0.369 | 0.485 | 50/53 | +0.083 |  |
| Andre Burakovsky: 1+ assists | 0.172 | 0.255 | 26/75 | +0.065 | STANDARD |
| Matias Maccelli: 1+ assists | 0.269 | 0.350 | 36/66 | +0.055 | STANDARD |
| Jordan Spence: 1+ points | 0.382 | 0.305 | 32/71 | +0.047 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.384 | 0.310 | 33/71 | +0.038 | STANDARD |
| Jordan Spence: 1+ assists | 0.327 | 0.255 | 27/76 | +0.043 | STANDARD |

**SEA @ TBL** · priced 154/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.41, exp saves 21.35 (sd 5.88), pull risk 0.048
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.4 (sd 6.94), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.401 | 0.590 | 60/42 | +0.162 | STANDARD |
| John Carlson: 1+ assists | 0.320 | 0.495 | 50/51 | +0.153 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.512 | 0.665 | 67/34 | +0.132 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.235 | 25/78 | +0.113 | STANDARD |
| Nikita Kucherov: 2+ points | 0.327 | 0.460 | 47/55 | +0.106 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.162 | 0.285 | 29/72 | +0.104 | STANDARD |

**VAN @ FLA** · priced 145/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.7, exp saves 21.59 (sd 6.08), pull risk 0.058
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.21, exp saves 24.98 (sd 6.84), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Marco Rossi: 1+ points | 0.492 | 0.365 | 38/65 | +0.096 | STANDARD |
| Sam Reinhart: 1+ points | 0.525 | 0.645 | 65/36 | +0.099 | STANDARD |
| Linus Karlsson: 1+ points | 0.450 | 0.330 | 34/68 | +0.094 | STANDARD |
| Brady Tkachuk: 1+ points | 0.518 | 0.635 | 64/37 | +0.096 | STANDARD |
| Brady Tkachuk: 2+ points | 0.162 | 0.275 | 28/73 | +0.094 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.265 | 0.375 | 39/64 | +0.079 | STANDARD |

**NYR @ NJD** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROBABLE) exp shots 24.13, exp saves 21.03 (sd 5.99), pull risk 0.053
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.99, exp saves 25.89 (sd 6.92), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 29+ saves | 0.344 | 0.500 | 52/52 | +0.118 |  |
| Jack Hughes: 1+ assists | 0.384 | 0.525 | 53/48 | +0.119 | STANDARD |
| Jack Hughes: 2+ points | 0.222 | 0.355 | 37/66 | +0.102 | STANDARD |
| Jack Hughes: 1+ points | 0.589 | 0.700 | 71/31 | +0.086 | STANDARD |
| Nico Hischier: 1+ points | 0.484 | 0.590 | 60/42 | +0.079 | STANDARD |
| Jack Hughes: 3+ points | 0.057 | 0.150 | 16/86 | +0.075 | STANDARD |

**PHI @ DET** · priced 154/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Viktor Arvidsson: 1+ assists | 0.266 | 0.345 | 35/66 | +0.058 | STANDARD |
| Viktor Arvidsson: 1+ points | 0.467 | 0.545 | 56/47 | +0.045 | STANDARD |
| Dylan Larkin: 1+ points | 0.528 | 0.605 | 62/41 | +0.045 | STANDARD |
| Dylan Larkin: 1+ assists | 0.337 | 0.410 | 42/60 | +0.046 | STANDARD |
| Daniil Tarasov: 23+ saves | 0.425 | 0.495 | 55/56 | -0.002 |  |
| Dylan Larkin: 2+ points | 0.176 | 0.245 | 26/77 | +0.042 | STANDARD |

**WPG @ CHI** · priced 184/196 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.63, exp saves 23.95 (sd 6.63), pull risk 0.064
- WPG net: Stuart Skinner (PROBABLE) exp shots 25.12, exp saves 21.75 (sd 6.06), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ian Cole: 1+ points | 0.214 | 0.540 | 91/83 | -0.054 | STANDARD |
| Ian Cole: 1+ assists | 0.169 | 0.495 | 98/99 | -0.160 | STANDARD |
| Alex Vlasic: 1+ assists | 0.266 | 0.490 | 97/99 | -0.257 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.271 | 0.490 | 97/99 | -0.261 | STANDARD |
| Alex Vlasic: 1+ points | 0.302 | 0.465 | 91/98 | -0.283 | STANDARD |
| Connor Bedard: 1+ assists | 0.351 | 0.500 | 52/52 | +0.112 | STANDARD |

**SJS @ NSH** · priced 181/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.54, exp saves 23.87 (sd 6.58), pull risk 0.066
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.64, exp saves 23.73 (sd 6.59), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.425 | 0.580 | 59/43 | +0.128 | STANDARD |
| Ivar Stenberg: 1+ points | 0.341 | 0.470 | 48/54 | +0.102 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.203 | 0.330 | 35/69 | +0.092 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.274 | 0.390 | 41/63 | +0.079 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.105 | 0.215 | 24/81 | +0.074 | STANDARD |
| Ivar Stenberg: 2+ points | 0.068 | 0.155 | 17/86 | +0.064 | PRIOR_HEAVY |

**STL @ MIN** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.75, exp saves 23.23 (sd 6.4), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.78), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.479 | 0.360 | 37/65 | +0.092 | STANDARD |
| Adam Jiricek: 1+ points | 0.286 | 0.380 | 39/63 | +0.068 | PRIOR_HEAVY |
| Ryan Hartman: 1+ assists | 0.318 | 0.230 | 24/78 | +0.066 | STANDARD |
| Adam Jiricek: 1+ assists | 0.216 | 0.300 | 32/72 | +0.050 | PRIOR_HEAVY |
| Rieger Lorenz: 1+ goals | 0.138 | 0.060 | 10/98 | +0.032 | PRIOR_HEAVY |
| Yakov Trenin: 1+ goals | 0.136 | 0.070 | 11/97 | +0.019 | STANDARD |

**UTA @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 27.2, exp saves 23.7 (sd 6.46), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.548 | 0.685 | 69/32 | +0.117 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.202 | 0.330 | 34/68 | +0.103 | STANDARD |
| Connor McDavid: 2+ points | 0.410 | 0.535 | 54/47 | +0.102 | STANDARD |
| Connor McDavid: 2+ assists | 0.189 | 0.305 | 31/70 | +0.096 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.394 | 0.280 | 29/73 | +0.089 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.488 | 0.595 | 60/41 | +0.085 | STANDARD |

**CGY @ VGK** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.19 (sd 6.2), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.46 (sd 7.16), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Trevor Connelly: 1+ assists | 0.228 | 0.375 | 39/64 | +0.116 | PRIOR_HEAVY |
| Jack Eichel: 1+ assists | 0.467 | 0.605 | 61/40 | +0.116 | STANDARD |
| Mitch Marner: 2+ points | 0.210 | 0.340 | 35/67 | +0.104 | STANDARD |
| Trevor Connelly: 1+ points | 0.395 | 0.520 | 53/49 | +0.097 | PRIOR_HEAVY |
| Mitch Marner: 1+ assists | 0.436 | 0.555 | 56/45 | +0.097 | STANDARD |
| Jack Eichel: 2+ points | 0.271 | 0.390 | 40/62 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
