# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T15:26:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4622 · contracts joined: 2401 (unjoined to any game: 1871)
gates: {'UNSUPPORTED': 2126, 'OK': 178, 'NO_EDGE': 97}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 316, 'game_early_goal': 11, 'first_goal': 397, 'game_winner': 22, 'player_goals': 692, 'game_overtime': 11, 'player_points': 433, 'goalie_saves': 2, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-6h | 0.451 | 0.549 | 0.166 | 6.70 | 3.18 | 3.51 | 226 (25/201) | PROBABLE/PROJECTED |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-6h | 0.538 | 0.462 | 0.180 | 6.03 | 3.12 | 2.91 | 231 (25/206) | PROBABLE/PROJECTED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-6h | 0.619 | 0.381 | 0.177 | 6.02 | 3.38 | 2.63 | 210 (25/185) | PROBABLE/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-6h | 0.604 | 0.396 | 0.163 | 6.69 | 3.70 | 2.99 | 203 (25/178) | CONFIRMED/PROJECTED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-6h | 0.470 | 0.530 | 0.178 | 6.08 | 2.95 | 3.13 | 215 (25/190) | PROBABLE/PROJECTED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-6h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 216 (25/191) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-6h | 0.494 | 0.505 | 0.180 | 5.87 | 2.91 | 2.96 | 211 (25/186) | PROJECTED/PROJECTED |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-6h | 0.536 | 0.464 | 0.172 | 6.38 | 3.30 | 3.08 | 233 (25/208) | PROJECTED/PROJECTED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-6h | 0.529 | 0.471 | 0.179 | 6.05 | 3.12 | 2.93 | 218 (25/193) | PROJECTED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-6h | 0.558 | 0.442 | 0.161 | 6.66 | 3.53 | 3.13 | 229 (25/204) | PROJECTED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-6h | 0.666 | 0.334 | 0.162 | 6.25 | 3.66 | 2.58 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.363 | 0.230 | 0.254 | 24 | 78 | yes | +0.110 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.575 | 0.440 | 0.467 | 45 | 57 | yes | +0.107 | OK |
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.604 | 0.725 | 0.703 | 73 | 28 | no | +0.102 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.396 | 0.275 | 0.297 | 28 | 73 | yes | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.785 | 0.675 | 0.699 | 68 | 33 | yes | +0.089 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.394 | 0.505 | 0.482 | 51 | 50 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.266 | 0.375 | 0.352 | 38 | 63 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.193 | 0.095 | 0.110 | 10 | 91 | yes | +0.086 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.389 | 0.495 | 0.473 | 50 | 51 | no | +0.084 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.299 | 0.395 | 0.375 | 40 | 61 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.250 | 0.345 | 0.325 | 35 | 66 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.550 | 0.530 | 56 | 46 | no | +0.073 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.530 | 0.435 | 0.454 | 44 | 57 | yes | +0.072 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.210 | 0.125 | 0.139 | 13 | 88 | yes | +0.072 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.147 | 0.235 | 0.215 | 24 | 77 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.564 | 0.475 | 0.493 | 48 | 53 | yes | +0.067 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.381 | 0.295 | 0.311 | 30 | 71 | yes | +0.066 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.619 | 0.705 | 0.689 | 71 | 30 | no | +0.066 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.470 | 0.555 | 0.538 | 56 | 45 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.441 | 0.525 | 0.508 | 53 | 48 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.335 | 0.318 | 34 | 67 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.666 | 0.745 | 0.730 | 75 | 26 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.334 | 0.255 | 0.270 | 26 | 75 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.354 | 0.435 | 0.418 | 44 | 57 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.257 | 0.335 | 0.319 | 34 | 67 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.670 | 0.745 | 0.731 | 75 | 26 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.569 | 0.650 | 0.634 | 66 | 36 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.306 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.346 | 0.275 | 0.288 | 28 | 73 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.352 | 0.430 | 0.414 | 44 | 58 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.730 | 0.795 | 0.783 | 80 | 21 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.330 | 0.265 | 0.277 | 27 | 74 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.340 | 0.275 | 0.287 | 28 | 73 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.120 | 0.065 | 0.074 | 7 | 94 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.087 | 0.030 | 0.037 | 4 | 98 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.311 | 0.380 | 0.366 | 39 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.788 | 0.845 | 0.835 | 85 | 16 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.243 | 0.185 | 0.196 | 19 | 82 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.575 | 0.562 | 58 | 43 | no | +0.042 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.549 | 0.485 | 0.498 | 49 | 52 | yes | +0.041 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.451 | 0.515 | 0.502 | 52 | 49 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT15SEATB-5 | game_total | 0.748 | 0.805 | 0.794 | 81 | 20 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.148 | 0.205 | 0.192 | 21 | 80 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.527 | 0.465 | 0.477 | 47 | 54 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.394 | 0.455 | 0.443 | 46 | 55 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.576 | 0.640 | 0.628 | 65 | 37 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.505 | 0.565 | 0.553 | 57 | 44 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.722 | 0.665 | 0.677 | 67 | 34 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.249 | 0.305 | 0.293 | 31 | 70 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.183 | 0.240 | 0.228 | 25 | 77 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15SEATB-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NYR3 | team_total | 0.621 | 0.565 | 0.576 | 57 | 44 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.714 | 0.765 | 0.755 | 77 | 24 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-SEA2 | team_total | 0.728 | 0.675 | 0.686 | 68 | 33 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-OTT3 | game_spread | 0.185 | 0.235 | 0.224 | 24 | 77 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.851 | 0.895 | 0.887 | 90 | 11 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.159 | 0.115 | 0.123 | 12 | 89 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-6 | game_total | 0.529 | 0.475 | 0.486 | 48 | 53 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-NYI2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 | team_total | 0.477 | 0.425 | 0.435 | 43 | 58 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.717 | 0.775 | 0.764 | 79 | 24 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.822 | 0.870 | 0.861 | 88 | 14 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.615 | 0.670 | 0.659 | 68 | 34 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.179 | 0.230 | 0.219 | 24 | 78 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15VANFLA-6 | game_total | 0.636 | 0.585 | 0.595 | 59 | 42 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.540 | 0.529 | 55 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NYR5 | team_total | 0.208 | 0.165 | 0.173 | 17 | 84 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.476 | 0.420 | 0.431 | 43 | 59 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.792 | 0.840 | 0.831 | 85 | 17 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN2 | game_spread | 0.307 | 0.355 | 0.345 | 36 | 65 | no | +0.028 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-CHI | game_winner | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.878 | 0.915 | 0.908 | 92 | 9 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR4 | team_total | 0.406 | 0.460 | 0.449 | 47 | 55 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-OTT2 | game_spread | 0.308 | 0.355 | 0.345 | 36 | 65 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR3 | game_spread | 0.185 | 0.145 | 0.152 | 15 | 86 | yes | +0.026 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 0.451 | 0.508 | 0.166 | 0.214 | 6.70 | 6.48 | 0.983/0.997 | KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 -0.065 |
| NYI @ OTT | 0.538 | 0.582 | 0.180 | 0.218 | 6.03 | 6.09 | 0.982/0.956 | KXNHLTEAMTOTAL-26OCT15NYIOTT-OTT3 +0.048 |
| SEA @ TBL | 0.619 | 0.582 | 0.177 | 0.218 | 6.02 | 6.08 | 0.952/1.005 | KXNHLTEAMTOTAL-26OCT15SEATB-SEA3 +0.043 |
| VAN @ FLA | 0.604 | 0.565 | 0.163 | 0.216 | 6.69 | 6.41 | 0.991/1.026 | KXNHLTEAMTOTAL-26OCT15VANFLA-FLA4 -0.060 |
| NYR @ NJD | 0.470 | 0.516 | 0.178 | 0.226 | 6.08 | 6.06 | 0.994/0.992 | KXNHLGAME-26OCT15NYRNJ-NJ +0.045 |
| PHI @ DET | 0.603 | 0.517 | 0.179 | 0.218 | 5.79 | 5.82 | 1.024/0.991 | KXNHLGAME-26OCT15PHIDET-DET -0.086 |
| WPG @ CHI | 0.494 | 0.481 | 0.180 | 0.218 | 5.87 | 6.19 | 1.003/0.988 | KXNHLTOTAL-26OCT15WPGCHI-7 +0.059 |
| SJS @ NSH | 0.536 | 0.536 | 0.172 | 0.213 | 6.38 | 6.51 | 1.000/1.026 | KXNHLTOTAL-26OCT15SJNSH-7 +0.022 |
| STL @ MIN | 0.529 | 0.552 | 0.179 | 0.218 | 6.05 | 6.40 | 0.995/0.993 | KXNHLTEAMTOTAL-26OCT15STLMIN-MIN4 +0.066 |
| UTA @ EDM | 0.558 | 0.579 | 0.161 | 0.208 | 6.66 | 6.78 | 0.994/0.992 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 +0.034 |
| CGY @ VGK | 0.666 | 0.660 | 0.162 | 0.198 | 6.25 | 6.17 | 1.003/0.997 | KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 -0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 39 recommended · full analysis in card.md / packet.json `thesis_card`

- Ondrej Palat: 1+ goals YES @ 9c · p 0.1256 (adj 0.1154) · $1.97 · thesis NYI:OFFENSE_4PLUS
- Carter Yakemchuk: 1+ assists NO @ 68c · p 0.7537 (adj 0.7118) · $6.06 · thesis OTT:SUPPRESSED
- Ridly Greig: 1+ goals YES @ 15c · p 0.1787 (adj 0.169) · $1.2 · thesis OTT:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 35c · p 0.4875 (adj 0.3949) · $3.39 · thesis TBL:SUPPRESSED
- Tampa Bay over 5.5 goals scored NO @ 83c · p 0.8891 (adj 0.857) · $7.51 · thesis SEA:WINS
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6404 (adj 0.6265) · $4.18 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals NO @ 62c · p 0.671 (adj 0.6558) · $3.73 · thesis TBL:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 61c · p 0.7002 (adj 0.6764) · $5.98 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 62c · p 0.6959 (adj 0.6744) · $5.98 · thesis FLA:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 50c · p 0.6473 (adj 0.5483) · $2.07 · thesis VAN:WINS
- Florida wins by over 2.5 goals NO @ 63c · p 0.7693 (adj 0.6755) · $4.29 · thesis VAN:WINS
- Matt Rempe: 1+ goals YES @ 6c · p 0.0873 (adj 0.078) · $1.35 · thesis NYR:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 62c · p 0.6741 (adj 0.6593) · $6.39 · thesis NJD:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.7935 (adj 0.7517) · $7.76 · thesis NYR:SUPPRESSED
- Cody Glass: 1+ goals YES @ 13c · p 0.1615 (adj 0.1511) · $1.46 · thesis NJD:OFFENSE_4PLUS
- Sheldon Dries: 1+ goals YES @ 9c · p 0.1206 (adj 0.1129) · $1.8 · thesis DET:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 19c · p 0.2329 (adj 0.2209) · $2.39 · thesis PHI:OFFENSE_4PLUS
- Viktor Arvidsson: 1+ assists NO @ 66c · p 0.7336 (adj 0.6943) · $6.46 · thesis DET:SUPPRESSED
- Denver Barkey: 1+ goals YES @ 14c · p 0.1734 (adj 0.1626) · $1.56 · thesis PHI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1764 (adj 0.1585) · $2.97 · thesis CHI:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 89c · p 0.9271 (adj 0.9141) · $7.64 · thesis WPG:SUPPRESSED
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7892 (adj 0.7756) · $7.64 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 28c · p 0.3205 (adj 0.3079) · $1.7 · thesis CHI:OFFENSE_4PLUS
- Ivar Stenberg: 2+ assists NO @ 93c · p 0.9795 (adj 0.9523) · $7.98 · thesis DIFFUSE
- Collin Graf: 1+ goals YES @ 13c · p 0.1729 (adj 0.1597) · $2.36 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 20c · p 0.242 (adj 0.2265) · $1.88 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8336 (adj 0.8239) · $7.12 · thesis SJS:SUPPRESSED
- Ross Johnston: 1+ goals YES @ 5c · p 0.0777 (adj 0.0695) · $1.49 · thesis STL:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 19c · p 0.2297 (adj 0.2173) · $2.04 · thesis MIN:OFFENSE_4PLUS
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1351 (adj 0.1188) · $1.05 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 24c · p 0.3086 (adj 0.2693) · $1.81 · thesis MIN:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.2168 (adj 0.1951) · $2.85 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4519 (adj 0.3629) · $4.65 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1291 (adj 0.1131) · $1.86 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ assists YES @ 29c · p 0.3939 (adj 0.3199) · $2.11 · thesis EDM:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7416 (adj 0.7212) · $6.8 · thesis VGK:SUPPRESSED
- Jack Eichel: 1+ goals NO @ 62c · p 0.6755 (adj 0.6604) · $5.16 · thesis VGK:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 15c · p 0.1898 (adj 0.1761) · $1.77 · thesis CGY:OFFENSE_4PLUS
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6902 (adj 0.6476) · $3.54 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 172/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 30.87, exp saves 26.61 (sd 7.14), pull risk 0.067
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.48 (sd 6.3), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Bobrovsky: 26+ saves | 0.564 | 0.470 | 50/56 | +0.046 |  |
| Owen Power: 1+ assists | 0.442 | 0.365 | 38/65 | +0.046 | STANDARD |
| Tage Thompson: 2+ points | 0.218 | 0.290 | 32/74 | +0.029 | STANDARD |
| Tage Thompson: 1+ assists | 0.355 | 0.425 | 44/59 | +0.038 | STANDARD |
| Gavin McKenna: 1+ assists | 0.233 | 0.300 | 31/71 | +0.042 | PRIOR_HEAVY |
| Kirill Marchenko: 2+ points | 0.162 | 0.225 | 24/79 | +0.037 | STANDARD |

**NYI @ OTT** · priced 173/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROBABLE) exp shots 25.99, exp saves 22.62 (sd 6.18), pull risk 0.049
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.57, exp saves 23.53 (sd 6.62), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Yakemchuk: 1+ points | 0.302 | 0.395 | 41/62 | +0.061 | STANDARD |
| Jordan Spence: 1+ points | 0.393 | 0.305 | 32/71 | +0.058 | STANDARD |
| Jordan Spence: 1+ assists | 0.337 | 0.250 | 27/77 | +0.053 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.166 | 0.250 | 27/77 | +0.052 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.246 | 0.330 | 34/68 | +0.058 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.246 | 0.165 | 19/86 | +0.045 | STANDARD |

**SEA @ TBL** · priced 150/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.41, exp saves 21.35 (sd 5.88), pull risk 0.048
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.4 (sd 6.94), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.401 | 0.570 | 59/45 | +0.132 | STANDARD |
| John Carlson: 1+ assists | 0.320 | 0.485 | 50/53 | +0.133 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.512 | 0.655 | 66/35 | +0.122 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.162 | 0.275 | 31/76 | +0.065 | STANDARD |
| Nikita Kucherov: 3+ points | 0.111 | 0.220 | 23/79 | +0.087 | STANDARD |
| Nikita Kucherov: 2+ points | 0.327 | 0.435 | 44/57 | +0.086 | STANDARD |

**VAN @ FLA** · priced 148/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.7, exp saves 21.58 (sd 6.14), pull risk 0.06
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.21, exp saves 24.95 (sd 6.9), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Marco Rossi: 1+ points | 0.473 | 0.355 | 37/66 | +0.087 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.305 | 0.420 | 43/59 | +0.088 | STANDARD |
| Brady Tkachuk: 1+ points | 0.517 | 0.630 | 65/39 | +0.076 | STANDARD |
| Brady Tkachuk: 2+ points | 0.158 | 0.265 | 30/77 | +0.059 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.269 | 0.375 | 39/64 | +0.075 | STANDARD |
| Sam Reinhart: 1+ points | 0.525 | 0.625 | 64/39 | +0.068 | STANDARD |

**NYR @ NJD** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROBABLE) exp shots 24.13, exp saves 21.01 (sd 5.98), pull risk 0.053
- NYR net: Dylan Garand (PROJECTED) exp shots 29.99, exp saves 25.83 (sd 6.95), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.225 | 0.345 | 36/67 | +0.090 | STANDARD |
| Jack Hughes: 1+ assists | 0.393 | 0.505 | 52/51 | +0.079 | STANDARD |
| Nico Hischier: 1+ points | 0.489 | 0.585 | 60/43 | +0.064 | STANDARD |
| Pavel Dorofeyev: 1+ assists | 0.206 | 0.290 | 30/72 | +0.059 | STANDARD |
| Gabe Perreault: 1+ points | 0.461 | 0.380 | 40/64 | +0.044 | STANDARD |
| Jack Hughes: 1+ points | 0.591 | 0.670 | 71/37 | +0.022 | STANDARD |

**PHI @ DET** · priced 154/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Daniil Tarasov: 23+ saves | 0.425 | 0.295 | 56/97 | -0.152 |  |
| Viktor Arvidsson: 1+ assists | 0.266 | 0.345 | 35/66 | +0.058 | STANDARD |
| Viktor Arvidsson: 1+ points | 0.467 | 0.540 | 56/48 | +0.035 | STANDARD |
| Dylan Larkin: 1+ points | 0.528 | 0.600 | 62/42 | +0.035 | STANDARD |
| Dylan Larkin: 1+ assists | 0.337 | 0.405 | 42/61 | +0.036 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.297 | 0.230 | 25/79 | +0.034 | STANDARD |

**WPG @ CHI** · priced 159/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.63, exp saves 23.86 (sd 6.62), pull risk 0.067
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.12, exp saves 21.77 (sd 6.08), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Bedard: 1+ assists | 0.340 | 0.485 | 50/53 | +0.113 | STANDARD |
| Connor Bedard: 1+ points | 0.544 | 0.655 | 67/36 | +0.080 | STANDARD |
| Patrick Kane: 1+ assists | 0.317 | 0.410 | 42/60 | +0.066 | STANDARD |
| Connor Bedard: 2+ assists | 0.064 | 0.150 | 16/86 | +0.068 | STANDARD |
| Viggo Bjorck: 1+ points | 0.277 | 0.360 | 37/65 | +0.057 | PRIOR_HEAVY |
| Ryan Greene: 1+ goals | 0.176 | 0.105 | 12/91 | +0.049 | STANDARD |

**SJS @ NSH** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.54, exp saves 23.88 (sd 6.63), pull risk 0.066
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.73), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.429 | 0.575 | 59/44 | +0.114 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.202 | 0.325 | 34/69 | +0.093 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ points | 0.336 | 0.455 | 47/56 | +0.087 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.287 | 0.385 | 41/64 | +0.056 | STANDARD |
| Macklin Celebrini: 3+ points | 0.092 | 0.170 | 18/84 | +0.059 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.112 | 0.185 | 23/86 | +0.019 | STANDARD |

**STL @ MIN** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 26.75, exp saves 23.2 (sd 6.33), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.77), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.471 | 0.365 | 38/65 | +0.075 | STANDARD |
| Adam Jiricek: 1+ points | 0.288 | 0.375 | 39/64 | +0.056 | PRIOR_HEAVY |
| Ryan Hartman: 1+ assists | 0.309 | 0.230 | 24/78 | +0.056 | STANDARD |
| Rieger Lorenz: 1+ goals | 0.135 | 0.070 | 10/96 | +0.029 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.223 | 0.285 | 30/73 | +0.034 | PRIOR_HEAVY |
| Matt Boldy: 1+ assists | 0.408 | 0.470 | 49/55 | +0.025 | STANDARD |

**UTA @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.2, exp saves 23.7 (sd 6.46), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.548 | 0.685 | 69/32 | +0.117 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.202 | 0.325 | 34/69 | +0.094 | STANDARD |
| Connor McDavid: 2+ points | 0.410 | 0.530 | 54/48 | +0.092 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.488 | 0.605 | 61/40 | +0.095 | STANDARD |
| Connor McDavid: 2+ assists | 0.189 | 0.305 | 31/70 | +0.096 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.394 | 0.280 | 29/73 | +0.089 | STANDARD |

**CGY @ VGK** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.19 (sd 6.2), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.46 (sd 7.16), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 2+ points | 0.210 | 0.350 | 37/67 | +0.104 | STANDARD |
| Trevor Connelly: 1+ assists | 0.228 | 0.365 | 38/65 | +0.106 | PRIOR_HEAVY |
| Trevor Connelly: 1+ points | 0.395 | 0.520 | 53/49 | +0.097 | PRIOR_HEAVY |
| Jack Eichel: 2+ points | 0.271 | 0.390 | 40/62 | +0.092 | STANDARD |
| Jack Eichel: 1+ assists | 0.467 | 0.585 | 60/43 | +0.086 | STANDARD |
| Jack Eichel: 2+ assists | 0.129 | 0.235 | 24/77 | +0.089 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
