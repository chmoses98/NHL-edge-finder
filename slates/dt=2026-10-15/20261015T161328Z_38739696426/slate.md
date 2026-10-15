# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T16:13:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4629 · contracts joined: 2408 (unjoined to any game: 1871)
gates: {'UNSUPPORTED': 2133, 'OK': 190, 'NO_EDGE': 85}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 316, 'game_early_goal': 11, 'first_goal': 398, 'game_winner': 22, 'player_goals': 694, 'game_overtime': 11, 'player_points': 433, 'goalie_saves': 6, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-6h | 0.449 | 0.551 | 0.165 | 6.68 | 3.17 | 3.51 | 227 (25/202) | PROBABLE/PROBABLE |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-6h | 0.571 | 0.429 | 0.175 | 6.27 | 3.36 | 2.91 | 234 (25/209) | PROBABLE/CONFIRMED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-6h | 0.619 | 0.381 | 0.177 | 6.02 | 3.38 | 2.63 | 210 (25/185) | PROBABLE/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-6h | 0.611 | 0.389 | 0.158 | 6.75 | 3.76 | 2.99 | 204 (25/179) | CONFIRMED/PROBABLE |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-6h | 0.456 | 0.544 | 0.175 | 6.00 | 2.87 | 3.13 | 215 (25/190) | PROBABLE/CONFIRMED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-6h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 216 (25/191) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-6h | 0.493 | 0.507 | 0.179 | 5.85 | 2.91 | 2.94 | 211 (25/186) | PROBABLE/PROJECTED |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-6h | 0.532 | 0.468 | 0.175 | 6.40 | 3.30 | 3.10 | 233 (25/208) | PROBABLE/PROJECTED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-6h | 0.540 | 0.460 | 0.181 | 5.99 | 3.12 | 2.87 | 220 (25/195) | CONFIRMED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-6h | 0.558 | 0.442 | 0.161 | 6.66 | 3.53 | 3.13 | 229 (25/204) | PROJECTED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-6h | 0.666 | 0.334 | 0.162 | 6.25 | 3.66 | 2.58 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.574 | 0.445 | 0.471 | 45 | 56 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.359 | 0.230 | 0.253 | 24 | 78 | yes | +0.106 | OK |
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.611 | 0.725 | 0.704 | 73 | 28 | no | +0.095 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.389 | 0.275 | 0.296 | 28 | 73 | yes | +0.095 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.784 | 0.675 | 0.699 | 68 | 33 | yes | +0.089 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.194 | 0.095 | 0.110 | 10 | 91 | yes | +0.088 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.389 | 0.495 | 0.473 | 50 | 51 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.555 | 0.534 | 56 | 45 | no | +0.083 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.401 | 0.505 | 0.484 | 51 | 50 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.139 | 0.235 | 0.213 | 24 | 77 | no | +0.079 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.276 | 0.375 | 0.354 | 38 | 63 | no | +0.078 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.456 | 0.555 | 0.535 | 56 | 45 | no | +0.077 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.544 | 0.445 | 0.465 | 45 | 56 | yes | +0.077 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.381 | 0.285 | 0.303 | 29 | 72 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.299 | 0.395 | 0.375 | 40 | 61 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.250 | 0.345 | 0.325 | 35 | 66 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.333 | 0.425 | 0.406 | 43 | 58 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.555 | 0.650 | 0.632 | 66 | 36 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.206 | 0.125 | 0.139 | 13 | 88 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.247 | 0.335 | 0.316 | 34 | 67 | no | +0.068 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.619 | 0.705 | 0.689 | 71 | 30 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.348 | 0.435 | 0.417 | 44 | 57 | no | +0.065 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-6 | game_total | 0.572 | 0.485 | 0.503 | 49 | 52 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-8 | game_total | 0.274 | 0.195 | 0.209 | 20 | 81 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.560 | 0.475 | 0.492 | 48 | 53 | yes | +0.062 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.441 | 0.525 | 0.508 | 53 | 48 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.335 | 0.318 | 34 | 67 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.666 | 0.745 | 0.730 | 75 | 26 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.334 | 0.255 | 0.270 | 26 | 75 | yes | +0.061 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.534 | 0.450 | 0.467 | 46 | 56 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.670 | 0.745 | 0.731 | 75 | 26 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.774 | 0.845 | 0.832 | 85 | 16 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.610 | 0.685 | 0.671 | 69 | 32 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.338 | 0.265 | 0.279 | 27 | 74 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.317 | 0.245 | 0.258 | 25 | 76 | yes | +0.053 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.551 | 0.475 | 0.490 | 48 | 53 | yes | +0.053 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.449 | 0.525 | 0.510 | 53 | 48 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.346 | 0.275 | 0.288 | 28 | 73 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-7 | game_total | 0.458 | 0.385 | 0.399 | 39 | 62 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.167 | 0.240 | 0.224 | 25 | 77 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.250 | 0.185 | 0.197 | 19 | 82 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.341 | 0.275 | 0.288 | 28 | 73 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.087 | 0.030 | 0.037 | 4 | 98 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.251 | 0.315 | 0.302 | 32 | 69 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.725 | 0.790 | 0.778 | 80 | 22 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.311 | 0.375 | 0.362 | 38 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.572 | 0.640 | 0.627 | 65 | 37 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.575 | 0.562 | 58 | 43 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.149 | 0.205 | 0.193 | 21 | 80 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.114 | 0.065 | 0.073 | 7 | 94 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.180 | 0.167 | 19 | 83 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.722 | 0.665 | 0.677 | 67 | 34 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT15VANFLA-6 | game_total | 0.643 | 0.585 | 0.597 | 59 | 42 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.508 | 0.565 | 0.554 | 57 | 44 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-9 | game_total | 0.194 | 0.145 | 0.154 | 15 | 86 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT15SEATB-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.818 | 0.870 | 0.861 | 88 | 14 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.714 | 0.765 | 0.755 | 77 | 24 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.851 | 0.895 | 0.887 | 90 | 11 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.159 | 0.115 | 0.123 | 12 | 89 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI5 | team_total | 0.179 | 0.130 | 0.139 | 14 | 88 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.177 | 0.230 | 0.219 | 24 | 78 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT15SEATB-5 | game_total | 0.748 | 0.800 | 0.790 | 81 | 21 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR4 | team_total | 0.402 | 0.460 | 0.448 | 47 | 55 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.717 | 0.775 | 0.764 | 79 | 24 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.790 | 0.840 | 0.831 | 85 | 17 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.540 | 0.529 | 55 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 | team_total | 0.476 | 0.425 | 0.435 | 43 | 58 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.476 | 0.420 | 0.431 | 43 | 59 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR2 | team_total | 0.814 | 0.855 | 0.847 | 86 | 15 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.878 | 0.915 | 0.908 | 92 | 9 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-8 | game_total | 0.211 | 0.255 | 0.246 | 26 | 75 | no | +0.026 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.507 | 0.555 | 0.545 | 56 | 45 | no | +0.026 | OK |
| KXNHLGAME-26OCT15WPGCHI-CHI | game_winner | 0.493 | 0.445 | 0.455 | 45 | 56 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.269 | 0.220 | 0.229 | 23 | 79 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-9 | game_total | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.397 | 0.445 | 0.435 | 45 | 56 | no | +0.026 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 0.449 | 0.510 | 0.165 | 0.214 | 6.68 | 6.48 | 0.983/1.000 | KXNHLSPREAD-26OCT15BUFTOR-BUF2 -0.066 |
| NYI @ OTT | 0.571 | 0.586 | 0.175 | 0.215 | 6.27 | 6.14 | 0.982/0.978 | KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 -0.027 |
| SEA @ TBL | 0.619 | 0.582 | 0.177 | 0.218 | 6.02 | 6.08 | 0.952/1.005 | KXNHLTEAMTOTAL-26OCT15SEATB-SEA3 +0.043 |
| VAN @ FLA | 0.611 | 0.564 | 0.158 | 0.214 | 6.75 | 6.43 | 0.991/1.030 | KXNHLTEAMTOTAL-26OCT15VANFLA-FLA5 -0.067 |
| NYR @ NJD | 0.456 | 0.511 | 0.175 | 0.222 | 6.00 | 6.05 | 0.994/0.988 | KXNHLGAME-26OCT15NYRNJ-NJ +0.055 |
| PHI @ DET | 0.603 | 0.517 | 0.179 | 0.218 | 5.79 | 5.82 | 1.024/0.991 | KXNHLGAME-26OCT15PHIDET-DET -0.086 |
| WPG @ CHI | 0.493 | 0.489 | 0.179 | 0.220 | 5.85 | 6.17 | 0.995/0.988 | KXNHLTOTAL-26OCT15WPGCHI-7 +0.049 |
| SJS @ NSH | 0.532 | 0.536 | 0.175 | 0.212 | 6.40 | 6.52 | 1.002/1.026 | KXNHLTOTAL-26OCT15SJNSH-5 +0.022 |
| STL @ MIN | 0.540 | 0.555 | 0.181 | 0.220 | 5.99 | 6.39 | 0.991/0.993 | KXNHLTOTAL-26OCT15STLMIN-7 +0.074 |
| UTA @ EDM | 0.558 | 0.579 | 0.161 | 0.208 | 6.66 | 6.78 | 0.994/0.992 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 +0.034 |
| CGY @ VGK | 0.666 | 0.660 | 0.162 | 0.198 | 6.25 | 6.17 | 1.003/0.997 | KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 -0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Owen Power: 1+ goals NO @ 88c · p 0.915 (adj 0.9025) · $7.27 · thesis BUF:SUPPRESSED
- Sergei Bobrovsky: 26+ saves YES @ 49c · p 0.5658 (adj 0.5254) · $3.31 · thesis TOR:NET_HIGH_VOLUME
- Gavin McKenna: 1+ assists NO @ 70c · p 0.7632 (adj 0.7291) · $5.01 · thesis TOR:SUPPRESSED
- Andre Burakovsky: 1+ assists NO @ 75c · p 0.8287 (adj 0.7843) · $7.27 · thesis OTT:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 10c · p 0.1339 (adj 0.1217) · $1.42 · thesis OTT:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 14c · p 0.1764 (adj 0.1648) · $1.67 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 15c · p 0.1838 (adj 0.1741) · $1.64 · thesis OTT:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 51c · p 0.6801 (adj 0.5663) · $4.67 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals NO @ 61c · p 0.671 (adj 0.6545) · $3.93 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6404 (adj 0.6253) · $2.3 · thesis TBL:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 11c · p 0.1842 (adj 0.1632) · $3.49 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2452 (adj 0.2252) · $3.95 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2285 (adj 0.2101) · $3.46 · thesis VAN:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 62c · p 0.6948 (adj 0.6736) · $6.79 · thesis FLA:SUPPRESSED
- Matt Rempe: 1+ goals YES @ 6c · p 0.0903 (adj 0.0815) · $1.49 · thesis NYR:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 73c · p 0.7767 (adj 0.7638) · $6.36 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 62c · p 0.6712 (adj 0.6572) · $4.54 · thesis NJD:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 77c · p 0.8232 (adj 0.7941) · $2.73 · thesis NYR:WINS
- Nate Danielson: 1+ goals NO @ 84c · p 0.8871 (adj 0.8728) · $7.27 · thesis DET:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 19c · p 0.2329 (adj 0.2209) · $2.2 · thesis PHI:OFFENSE_4PLUS
- Sheldon Dries: 1+ goals YES @ 9c · p 0.1206 (adj 0.1092) · $1.22 · thesis DET:OFFENSE_4PLUS
- Porter Martone: 1+ goals NO @ 78c · p 0.8216 (adj 0.8099) · $7.27 · thesis PHI:SUPPRESSED
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7989 (adj 0.7829) · $6.48 · thesis CHI:SUPPRESSED
- Connor Bedard: 1+ assists NO @ 51c · p 0.6682 (adj 0.5556) · $4.42 · thesis CHI:SUPPRESSED
- Collin Graf: 1+ goals YES @ 13c · p 0.1676 (adj 0.1557) · $1.92 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 68c · p 0.8073 (adj 0.7181) · $7.27 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 21c · p 0.2451 (adj 0.2338) · $1.61 · thesis SJS:OFFENSE_4PLUS
- Macklin Celebrini: 1+ assists NO @ 43c · p 0.5761 (adj 0.459) · $2.46 · thesis SJS:SUPPRESSED
- Ross Johnston: 1+ goals YES @ 5c · p 0.0754 (adj 0.0678) · $1.23 · thesis STL:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 19c · p 0.2323 (adj 0.2192) · $1.96 · thesis MIN:OFFENSE_4PLUS
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1383 (adj 0.12) · $1.22 · thesis MIN:OFFENSE_4PLUS
- Adam Jiricek: 1+ assists NO @ 72c · p 0.7837 (adj 0.7469) · $5.12 · thesis STL:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 16c · p 0.2168 (adj 0.1926) · $2.45 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4519 (adj 0.3629) · $4.7 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1291 (adj 0.1106) · $1.48 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 30c · p 0.338 (adj 0.3273) · $2.83 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7416 (adj 0.7249) · $7.04 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6902 (adj 0.6476) · $3.36 · thesis GAME:TIGHT
- Aydar Suniev: 1+ goals YES @ 15c · p 0.1898 (adj 0.1736) · $1.34 · thesis CGY:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 63c · p 0.6755 (adj 0.6629) · $3.86 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 30.87, exp saves 26.64 (sd 7.16), pull risk 0.068
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.02, exp saves 22.48 (sd 6.28), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 27+ saves | 0.256 | 0.370 | 51/77 | -0.039 |  |
| Sergei Bobrovsky: 26+ saves | 0.566 | 0.485 | 49/52 | +0.058 |  |
| Tage Thompson: 1+ assists | 0.354 | 0.425 | 44/59 | +0.039 | STANDARD |
| Tage Thompson: 2+ points | 0.225 | 0.295 | 32/73 | +0.031 | STANDARD |
| Gavin McKenna: 1+ assists | 0.237 | 0.305 | 31/70 | +0.049 | PRIOR_HEAVY |
| Auston Matthews: 2+ points | 0.259 | 0.320 | 33/69 | +0.036 | STANDARD |

**NYI @ OTT** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROBABLE) exp shots 25.99, exp saves 22.67 (sd 6.16), pull risk 0.047
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 27.57, exp saves 23.51 (sd 6.61), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Ullmark: 23+ saves | 0.504 | 0.285 | 50/93 | -0.013 |  |
| Andre Burakovsky: 1+ assists | 0.171 | 0.260 | 27/75 | +0.066 | STANDARD |
| Jordan Spence: 1+ points | 0.386 | 0.305 | 32/71 | +0.050 | STANDARD |
| Claude Giroux: 1+ points | 0.484 | 0.405 | 42/61 | +0.047 | STANDARD |
| Jordan Spence: 1+ assists | 0.328 | 0.250 | 27/77 | +0.045 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.379 | 0.305 | 32/71 | +0.044 | STANDARD |

**SEA @ TBL** · priced 150/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.41, exp saves 21.35 (sd 5.88), pull risk 0.048
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.4 (sd 6.94), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.401 | 0.580 | 59/43 | +0.152 | STANDARD |
| John Carlson: 1+ assists | 0.320 | 0.495 | 50/51 | +0.153 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.512 | 0.665 | 67/34 | +0.132 | STANDARD |
| Nikita Kucherov: 2+ points | 0.327 | 0.470 | 48/54 | +0.116 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.230 | 25/79 | +0.103 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.162 | 0.290 | 31/73 | +0.094 | STANDARD |

**VAN @ FLA** · priced 145/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.7, exp saves 21.61 (sd 6.14), pull risk 0.058
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.21, exp saves 24.98 (sd 6.82), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Marco Rossi: 1+ points | 0.494 | 0.365 | 38/65 | +0.097 | STANDARD |
| Brady Tkachuk: 1+ points | 0.518 | 0.635 | 64/37 | +0.095 | STANDARD |
| Linus Karlsson: 1+ points | 0.444 | 0.330 | 34/68 | +0.088 | STANDARD |
| Sam Reinhart: 1+ points | 0.534 | 0.645 | 65/36 | +0.090 | STANDARD |
| Brady Tkachuk: 2+ points | 0.166 | 0.275 | 29/74 | +0.081 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.307 | 0.415 | 42/59 | +0.086 | STANDARD |

**NYR @ NJD** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROBABLE) exp shots 24.13, exp saves 21.03 (sd 5.99), pull risk 0.053
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.99, exp saves 25.89 (sd 6.92), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.222 | 0.350 | 36/66 | +0.102 | STANDARD |
| Jack Hughes: 1+ assists | 0.384 | 0.505 | 51/50 | +0.098 | STANDARD |
| Jack Hughes: 1+ points | 0.589 | 0.695 | 71/32 | +0.076 | STANDARD |
| Nico Hischier: 1+ points | 0.484 | 0.585 | 60/43 | +0.069 | STANDARD |
| Jack Hughes: 3+ points | 0.057 | 0.140 | 15/87 | +0.065 | STANDARD |
| Nico Hischier: 2+ points | 0.149 | 0.230 | 24/78 | +0.059 | STANDARD |

**PHI @ DET** · priced 154/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Viktor Arvidsson: 1+ points | 0.467 | 0.550 | 57/47 | +0.045 | STANDARD |
| Dylan Larkin: 1+ points | 0.528 | 0.610 | 63/41 | +0.045 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.266 | 0.345 | 35/66 | +0.058 | STANDARD |
| Dylan Larkin: 1+ assists | 0.337 | 0.410 | 42/60 | +0.046 | STANDARD |
| Dylan Larkin: 2+ points | 0.176 | 0.245 | 26/77 | +0.042 | STANDARD |
| Denver Barkey: 1+ goals | 0.173 | 0.105 | 14/93 | +0.025 | STANDARD |

**WPG @ CHI** · priced 157/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.63, exp saves 23.93 (sd 6.64), pull risk 0.061
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.12, exp saves 21.73 (sd 6.05), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Bedard: 1+ assists | 0.332 | 0.505 | 52/51 | +0.141 | STANDARD |
| Connor Bedard: 2+ points | 0.172 | 0.305 | 32/71 | +0.103 | STANDARD |
| Connor Bedard: 1+ points | 0.527 | 0.660 | 67/35 | +0.107 | STANDARD |
| Patrick Kane: 1+ assists | 0.316 | 0.415 | 43/60 | +0.067 | STANDARD |
| Connor Bedard: 2+ assists | 0.060 | 0.155 | 17/86 | +0.071 | STANDARD |
| Patrick Kane: 2+ points | 0.139 | 0.225 | 24/79 | +0.059 | STANDARD |

**SJS @ NSH** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.54, exp saves 23.88 (sd 6.56), pull risk 0.064
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.64, exp saves 23.68 (sd 6.61), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.424 | 0.580 | 59/43 | +0.129 | STANDARD |
| Ivar Stenberg: 1+ points | 0.325 | 0.470 | 48/54 | +0.118 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.193 | 0.330 | 34/68 | +0.112 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.276 | 0.390 | 41/63 | +0.078 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.104 | 0.195 | 24/85 | +0.037 | STANDARD |
| Ivar Stenberg: 2+ points | 0.061 | 0.145 | 16/87 | +0.061 | PRIOR_HEAVY |

**STL @ MIN** · priced 166/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.75, exp saves 23.23 (sd 6.4), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.78), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.479 | 0.360 | 37/65 | +0.092 | STANDARD |
| Adam Jiricek: 1+ points | 0.286 | 0.380 | 39/63 | +0.068 | PRIOR_HEAVY |
| Ryan Hartman: 1+ assists | 0.318 | 0.235 | 25/78 | +0.055 | STANDARD |
| Adam Jiricek: 1+ assists | 0.216 | 0.290 | 30/72 | +0.050 | PRIOR_HEAVY |
| Rieger Lorenz: 1+ goals | 0.138 | 0.065 | 10/97 | +0.032 | PRIOR_HEAVY |
| Danila Yurov: 1+ points | 0.396 | 0.335 | 35/68 | +0.030 | STANDARD |

**UTA @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.2, exp saves 23.7 (sd 6.46), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.548 | 0.685 | 69/32 | +0.117 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.202 | 0.330 | 34/68 | +0.103 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.394 | 0.275 | 28/73 | +0.100 | STANDARD |
| Connor McDavid: 2+ assists | 0.189 | 0.305 | 31/70 | +0.096 | STANDARD |
| Connor McDavid: 2+ points | 0.410 | 0.525 | 53/48 | +0.092 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.488 | 0.595 | 60/41 | +0.085 | STANDARD |

**CGY @ VGK** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.19 (sd 6.2), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.46 (sd 7.16), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Trevor Connelly: 1+ assists | 0.228 | 0.370 | 38/64 | +0.116 | PRIOR_HEAVY |
| Jack Eichel: 1+ assists | 0.467 | 0.605 | 61/40 | +0.116 | STANDARD |
| Mitch Marner: 2+ points | 0.210 | 0.340 | 35/67 | +0.104 | STANDARD |
| Trevor Connelly: 1+ points | 0.395 | 0.520 | 53/49 | +0.097 | PRIOR_HEAVY |
| Mitch Marner: 1+ assists | 0.436 | 0.555 | 56/45 | +0.097 | STANDARD |
| Jack Eichel: 2+ points | 0.271 | 0.390 | 40/62 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
