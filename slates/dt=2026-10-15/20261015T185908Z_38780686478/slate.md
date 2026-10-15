# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T18:59:08Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4732 · contracts joined: 2511 (unjoined to any game: 1871)
gates: {'UNSUPPORTED': 2236, 'OK': 191, 'NO_EDGE': 84}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 348, 'game_early_goal': 11, 'first_goal': 404, 'game_winner': 22, 'player_goals': 702, 'game_overtime': 11, 'player_points': 478, 'goalie_saves': 18, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-3h | 0.449 | 0.551 | 0.165 | 6.68 | 3.17 | 3.51 | 227 (25/202) | PROBABLE/PROBABLE |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-3h | 0.567 | 0.433 | 0.175 | 6.28 | 3.36 | 2.92 | 235 (25/210) | CONFIRMED/CONFIRMED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-3h | 0.619 | 0.381 | 0.177 | 6.02 | 3.38 | 2.63 | 216 (25/191) | PROBABLE/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-3h | 0.624 | 0.376 | 0.162 | 6.82 | 3.83 | 2.99 | 222 (25/197) | CONFIRMED/CONFIRMED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-3h | 0.456 | 0.544 | 0.175 | 6.00 | 2.87 | 3.13 | 220 (25/195) | PROBABLE/CONFIRMED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-3h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 217 (25/192) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-3h | 0.493 | 0.507 | 0.180 | 5.82 | 2.89 | 2.93 | 255 (25/230) | CONFIRMED/PROBABLE |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-3h | 0.532 | 0.468 | 0.175 | 6.40 | 3.30 | 3.10 | 237 (25/212) | PROBABLE/CONFIRMED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-3h | 0.540 | 0.460 | 0.181 | 5.99 | 3.12 | 2.87 | 242 (25/217) | CONFIRMED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-6h | 0.562 | 0.438 | 0.163 | 6.66 | 3.53 | 3.13 | 230 (25/205) | CONFIRMED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-6h | 0.672 | 0.328 | 0.161 | 6.28 | 3.70 | 2.58 | 210 (25/185) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.360 | 0.230 | 0.253 | 24 | 78 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.574 | 0.445 | 0.471 | 45 | 56 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.786 | 0.675 | 0.699 | 68 | 33 | yes | +0.090 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.250 | 0.355 | 0.332 | 36 | 65 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.191 | 0.095 | 0.110 | 10 | 91 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.389 | 0.495 | 0.473 | 50 | 51 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.560 | 0.538 | 57 | 45 | no | +0.083 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.376 | 0.275 | 0.294 | 28 | 73 | yes | +0.082 | OK |
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.624 | 0.725 | 0.706 | 73 | 28 | no | +0.082 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.456 | 0.555 | 0.535 | 56 | 45 | no | +0.077 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.544 | 0.445 | 0.465 | 45 | 56 | yes | +0.077 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.381 | 0.285 | 0.303 | 29 | 72 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.412 | 0.505 | 0.486 | 51 | 50 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.350 | 0.329 | 36 | 66 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.283 | 0.375 | 0.356 | 38 | 63 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.333 | 0.425 | 0.406 | 43 | 58 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.139 | 0.225 | 0.205 | 23 | 78 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.305 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.352 | 0.265 | 0.281 | 27 | 74 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.247 | 0.335 | 0.316 | 34 | 67 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.544 | 0.455 | 0.473 | 46 | 55 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.346 | 0.435 | 0.417 | 44 | 57 | no | +0.067 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.619 | 0.705 | 0.689 | 71 | 30 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.562 | 0.475 | 0.492 | 48 | 53 | yes | +0.065 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-6 | game_total | 0.570 | 0.485 | 0.502 | 49 | 52 | yes | +0.063 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-8 | game_total | 0.271 | 0.195 | 0.209 | 20 | 81 | yes | +0.060 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.197 | 0.125 | 0.137 | 13 | 88 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.555 | 0.640 | 0.624 | 65 | 37 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT15VANFLA-6 | game_total | 0.654 | 0.575 | 0.591 | 58 | 43 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.257 | 0.185 | 0.198 | 19 | 82 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.670 | 0.750 | 0.735 | 76 | 26 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.774 | 0.845 | 0.832 | 85 | 16 | no | +0.056 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.328 | 0.255 | 0.269 | 26 | 75 | yes | +0.055 | OK |
| KXNHLGAME-26OCT15UTAEDM-UTA | game_winner | 0.438 | 0.515 | 0.500 | 52 | 49 | no | +0.054 | OK |
| KXNHLGAME-26OCT15UTAEDM-EDM | game_winner | 0.562 | 0.485 | 0.500 | 49 | 52 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.317 | 0.245 | 0.258 | 25 | 76 | yes | +0.053 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.551 | 0.475 | 0.490 | 48 | 53 | yes | +0.053 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.449 | 0.525 | 0.510 | 53 | 48 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.450 | 0.525 | 0.510 | 53 | 48 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-7 | game_total | 0.458 | 0.385 | 0.399 | 39 | 62 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.167 | 0.240 | 0.224 | 25 | 77 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.719 | 0.790 | 0.777 | 80 | 22 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.494 | 0.565 | 0.551 | 57 | 44 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.341 | 0.275 | 0.288 | 28 | 73 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.350 | 0.280 | 0.293 | 29 | 73 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.569 | 0.640 | 0.626 | 65 | 37 | no | +0.045 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.672 | 0.735 | 0.723 | 74 | 27 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.087 | 0.030 | 0.037 | 4 | 98 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.610 | 0.680 | 0.667 | 69 | 33 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.251 | 0.315 | 0.302 | 32 | 69 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.321 | 0.385 | 0.372 | 39 | 62 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI5 | team_total | 0.180 | 0.125 | 0.135 | 13 | 88 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-UTA2 | game_spread | 0.244 | 0.305 | 0.292 | 31 | 70 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR4 | team_total | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.149 | 0.205 | 0.193 | 21 | 80 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.383 | 0.445 | 0.432 | 45 | 56 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.113 | 0.065 | 0.073 | 7 | 94 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.180 | 0.167 | 19 | 83 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-EDM2 | game_spread | 0.352 | 0.295 | 0.306 | 30 | 71 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI2 | team_total | 0.721 | 0.775 | 0.765 | 78 | 23 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI2 | team_total | 0.779 | 0.725 | 0.736 | 73 | 28 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.720 | 0.665 | 0.677 | 67 | 34 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.173 | 0.230 | 0.218 | 24 | 78 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-9 | game_total | 0.194 | 0.145 | 0.154 | 15 | 86 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.518 | 0.575 | 0.564 | 58 | 43 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.818 | 0.870 | 0.861 | 88 | 14 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT15UTAEDM-UTA3 | game_spread | 0.146 | 0.195 | 0.184 | 20 | 81 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.714 | 0.765 | 0.755 | 77 | 24 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.851 | 0.895 | 0.887 | 90 | 11 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT15SEATB-5 | game_total | 0.748 | 0.795 | 0.786 | 80 | 21 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.273 | 0.220 | 0.230 | 23 | 79 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-8 | game_total | 0.208 | 0.255 | 0.245 | 26 | 75 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.540 | 0.529 | 55 | 47 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-9 | game_total | 0.141 | 0.185 | 0.175 | 19 | 82 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 | team_total | 0.476 | 0.425 | 0.435 | 43 | 58 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT15VANFLA-5 | game_total | 0.839 | 0.795 | 0.805 | 80 | 21 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT15VANFLA-10 | game_total | 0.134 | 0.085 | 0.093 | 10 | 93 | yes | +0.028 | OK |

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
| CGY @ VGK | 0.672 | 0.662 | 0.161 | 0.200 | 6.28 | 6.20 | 1.003/1.006 | KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6 -0.021 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 41 recommended · full analysis in card.md / packet.json `thesis_card`

- Owen Power: 1+ goals NO @ 86c · p 0.915 (adj 0.9) · $7.05 · thesis BUF:SUPPRESSED
- Gavin McKenna: 1+ assists NO @ 70c · p 0.7613 (adj 0.7282) · $4.63 · thesis TOR:SUPPRESSED
- Ukko-Pekka Luukkonen: 27+ saves NO @ 61c · p 0.7436 (adj 0.6397) · $3.66 · thesis BUF:NET_LOW_VOLUME
- Sergei Bobrovsky: 26+ saves YES @ 50c · p 0.5658 (adj 0.5304) · $2.21 · thesis TOR:NET_HIGH_VOLUME
- Andre Burakovsky: 1+ assists NO @ 75c · p 0.841 (adj 0.793) · $7.05 · thesis OTT:SUPPRESSED
- Jean-Gabriel Pageau: 1+ goals YES @ 12c · p 0.1521 (adj 0.1416) · $1.34 · thesis NYI:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 14c · p 0.1718 (adj 0.1626) · $1.42 · thesis OTT:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 51c · p 0.6801 (adj 0.5663) · $4.13 · thesis TBL:SUPPRESSED
- John Carlson: 1+ goals NO @ 83c · p 0.8809 (adj 0.8669) · $4.4 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6404 (adj 0.6265) · $2.04 · thesis TBL:SUPPRESSED
- Sam Reinhart: 1+ goals NO @ 61c · p 0.7005 (adj 0.6766) · $5.28 · thesis FLA:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 62c · p 0.6965 (adj 0.6761) · $5.28 · thesis FLA:SUPPRESSED
- Florida wins by over 2.5 goals NO @ 63c · p 0.7671 (adj 0.6747) · $4.2 · thesis VAN:WINS
- Jake DeBrusk: 1+ goals YES @ 27c · p 0.3212 (adj 0.3071) · $1.89 · thesis VAN:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 73c · p 0.7767 (adj 0.7638) · $6.17 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 13c · p 0.1629 (adj 0.1534) · $1.51 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 62c · p 0.6712 (adj 0.6572) · $4.4 · thesis NJD:SUPPRESSED
- Gabe Perreault: 1+ assists YES @ 26c · p 0.3267 (adj 0.2908) · $1.99 · thesis NYR:OFFENSE_4PLUS
- Nate Danielson: 1+ goals NO @ 83c · p 0.8871 (adj 0.8716) · $6.55 · thesis DET:SUPPRESSED
- Porter Martone: 1+ goals NO @ 78c · p 0.8216 (adj 0.8099) · $6.55 · thesis PHI:SUPPRESSED
- Denver Barkey: 1+ goals YES @ 14c · p 0.1734 (adj 0.1613) · $1.1 · thesis PHI:OFFENSE_4PLUS
- Dylan Larkin: 1+ goals NO @ 67c · p 0.7115 (adj 0.6986) · $3.42 · thesis DET:SUPPRESSED
- Roman Kantserov: 1+ goals NO @ 74c · p 0.7922 (adj 0.7767) · $7.05 · thesis CHI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 13c · p 0.1617 (adj 0.1525) · $1.4 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 27c · p 0.3135 (adj 0.3014) · $2.08 · thesis CHI:OFFENSE_4PLUS
- Connor Bedard: 1+ goals NO @ 66c · p 0.702 (adj 0.6877) · $3.32 · thesis CHI:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 68c · p 0.797 (adj 0.7144) · $7.05 · thesis SJS:SUPPRESSED
- Juuse Saros: 26+ saves NO @ 52c · p 0.6059 (adj 0.5579) · $3.92 · thesis NSH:NET_LOW_VOLUME
- Collin Graf: 1+ goals YES @ 14c · p 0.1689 (adj 0.1604) · $1.16 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2019 (adj 0.1927) · $1.53 · thesis SJS:OFFENSE_4PLUS
- Ross Johnston: 1+ goals YES @ 5c · p 0.0774 (adj 0.0693) · $1.3 · thesis STL:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1356 (adj 0.123) · $1.5 · thesis MIN:OFFENSE_4PLUS
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1383 (adj 0.1225) · $1.43 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 19c · p 0.2323 (adj 0.2205) · $2.07 · thesis MIN:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.2256 (adj 0.2067) · $3.51 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1321 (adj 0.1203) · $2.21 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.4994 (adj 0.4522) · $4.92 · thesis EDM:SUPPRESSED
- Utah wins by over 2.5 goals NO @ 81c · p 0.8643 (adj 0.8346) · $6.97 · thesis EDM:WINS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7363 (adj 0.721) · $6.84 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 61c · p 0.688 (adj 0.6465) · $3.03 · thesis GAME:TIGHT
- Vegas over 4.5 goals scored NO @ 62c · p 0.6924 (adj 0.6537) · $1.14 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 30.87, exp saves 26.64 (sd 7.16), pull risk 0.068
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 26.02, exp saves 22.48 (sd 6.28), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ukko-Pekka Luukkonen: 27+ saves | 0.256 | 0.395 | 40/61 | +0.117 |  |
| Tage Thompson: 1+ assists | 0.354 | 0.430 | 44/58 | +0.048 | STANDARD |
| Kirill Marchenko: 1+ points | 0.507 | 0.580 | 59/43 | +0.045 | STANDARD |
| Sergei Bobrovsky: 26+ saves | 0.566 | 0.495 | 50/51 | +0.048 |  |
| Tage Thompson: 2+ points | 0.225 | 0.295 | 32/73 | +0.031 | STANDARD |
| Auston Matthews: 2+ points | 0.257 | 0.325 | 33/68 | +0.048 | STANDARD |

**NYI @ OTT** · priced 177/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (CONFIRMED) exp shots 25.99, exp saves 22.66 (sd 6.14), pull risk 0.047
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 27.57, exp saves 23.45 (sd 6.64), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ assists | 0.159 | 0.255 | 26/75 | +0.078 | STANDARD |
| Semyon Varlamov: 26+ saves | 0.369 | 0.460 | 47/55 | +0.063 |  |
| Andre Burakovsky: 1+ points | 0.288 | 0.375 | 38/63 | +0.065 | STANDARD |
| Matias Maccelli: 1+ assists | 0.269 | 0.350 | 36/66 | +0.055 | STANDARD |
| Tim Stutzle: 1+ assists | 0.415 | 0.495 | 50/51 | +0.057 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.249 | 0.325 | 33/68 | +0.055 | STANDARD |

**SEA @ TBL** · priced 154/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.41, exp saves 21.35 (sd 5.88), pull risk 0.048
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.4 (sd 6.94), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.401 | 0.590 | 60/42 | +0.162 | STANDARD |
| John Carlson: 1+ assists | 0.320 | 0.495 | 50/51 | +0.153 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.512 | 0.665 | 67/34 | +0.132 | STANDARD |
| John Carlson: 2+ points | 0.095 | 0.235 | 25/78 | +0.113 | STANDARD |
| Nikita Kucherov: 2+ points | 0.327 | 0.465 | 47/54 | +0.116 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.162 | 0.285 | 29/72 | +0.104 | STANDARD |

**VAN @ FLA** · priced 158/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.7, exp saves 21.59 (sd 6.08), pull risk 0.058
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 29.21, exp saves 24.98 (sd 6.84), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Marco Rossi: 1+ points | 0.492 | 0.365 | 38/65 | +0.096 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.309 | 0.430 | 44/58 | +0.094 | STANDARD |
| Sam Reinhart: 1+ points | 0.525 | 0.645 | 65/36 | +0.099 | STANDARD |
| Brady Tkachuk: 2+ points | 0.162 | 0.280 | 29/73 | +0.094 | STANDARD |
| Brady Tkachuk: 1+ points | 0.518 | 0.635 | 64/37 | +0.096 | STANDARD |
| Linus Karlsson: 1+ points | 0.450 | 0.335 | 34/67 | +0.094 | STANDARD |

**NYR @ NJD** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROBABLE) exp shots 24.13, exp saves 21.03 (sd 5.99), pull risk 0.053
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.99, exp saves 25.89 (sd 6.92), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.384 | 0.525 | 53/48 | +0.119 | STANDARD |
| Jack Hughes: 2+ points | 0.222 | 0.355 | 36/65 | +0.112 | STANDARD |
| Dylan Garand: 29+ saves | 0.344 | 0.460 | 48/56 | +0.078 |  |
| Jack Hughes: 1+ points | 0.589 | 0.700 | 71/31 | +0.086 | STANDARD |
| Nico Hischier: 1+ points | 0.484 | 0.580 | 59/43 | +0.069 | STANDARD |
| Jack Hughes: 2+ assists | 0.085 | 0.170 | 18/84 | +0.065 | STANDARD |

**PHI @ DET** · priced 155/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Larkin: 1+ points | 0.528 | 0.610 | 62/40 | +0.055 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.266 | 0.345 | 35/66 | +0.058 | STANDARD |
| Viktor Arvidsson: 1+ points | 0.467 | 0.545 | 55/46 | +0.055 | STANDARD |
| Dylan Larkin: 1+ assists | 0.337 | 0.410 | 42/60 | +0.046 | STANDARD |
| Dylan Larkin: 2+ points | 0.176 | 0.245 | 26/77 | +0.042 | STANDARD |
| Nate Danielson: 1+ goals | 0.113 | 0.175 | 18/83 | +0.047 | STANDARD |

**WPG @ CHI** · priced 187/204 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 27.63, exp saves 23.95 (sd 6.63), pull risk 0.064
- WPG net: Stuart Skinner (PROBABLE) exp shots 25.12, exp saves 21.75 (sd 6.06), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Vlasic: 1+ assists | 0.266 | 0.080 | 14/98 | +0.118 | STANDARD |
| Connor Bedard: 1+ assists | 0.351 | 0.495 | 51/52 | +0.112 | STANDARD |
| Alex Vlasic: 1+ points | 0.302 | 0.160 | 18/86 | +0.111 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.271 | 0.130 | 24/98 | +0.018 | STANDARD |
| Connor Bedard: 1+ points | 0.540 | 0.660 | 67/35 | +0.094 | STANDARD |
| Connor Bedard: 2+ points | 0.187 | 0.305 | 32/71 | +0.089 | STANDARD |

**SJS @ NSH** · priced 183/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 27.54, exp saves 23.87 (sd 6.58), pull risk 0.066
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.64, exp saves 23.73 (sd 6.59), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.425 | 0.575 | 59/44 | +0.118 | STANDARD |
| Ivar Stenberg: 1+ points | 0.341 | 0.470 | 48/54 | +0.102 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.203 | 0.330 | 34/68 | +0.102 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.274 | 0.400 | 42/62 | +0.089 | STANDARD |
| Macklin Celebrini: 2+ assists | 0.105 | 0.215 | 23/80 | +0.083 | STANDARD |
| Juuse Saros: 26+ saves | 0.394 | 0.490 | 50/52 | +0.068 |  |

**STL @ MIN** · priced 181/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.75, exp saves 23.23 (sd 6.4), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.78), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ assists | 0.264 | 0.120 | 22/98 | +0.031 | STANDARD |
| Ryan Hartman: 1+ points | 0.479 | 0.365 | 38/65 | +0.082 | STANDARD |
| Philip Broberg: 1+ points | 0.428 | 0.325 | 34/69 | +0.072 | STANDARD |
| Philip Broberg: 1+ assists | 0.372 | 0.280 | 30/74 | +0.057 | STANDARD |
| Dalibor Dvorsky: 1+ assists | 0.206 | 0.115 | 21/98 | -0.016 | STANDARD |
| Zach Bogosian: 1+ assists | 0.205 | 0.120 | 13/89 | +0.067 | STANDARD |

**UTA @ EDM** · priced 175/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 27.2, exp saves 23.65 (sd 6.47), pull risk 0.061
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.198 | 0.330 | 34/68 | +0.107 | STANDARD |
| Connor McDavid: 2+ assists | 0.199 | 0.325 | 34/69 | +0.096 | STANDARD |
| Connor McDavid: 1+ assists | 0.559 | 0.680 | 69/33 | +0.095 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.395 | 0.280 | 29/73 | +0.090 | STANDARD |
| Connor McDavid: 2+ points | 0.426 | 0.535 | 54/47 | +0.087 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.658 | 0.550 | 56/46 | +0.080 | STANDARD |

**CGY @ VGK** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.27 (sd 6.19), pull risk 0.039
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.19, exp saves 25.44 (sd 7.13), pull risk 0.087

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.464 | 0.605 | 61/40 | +0.120 | STANDARD |
| Trevor Connelly: 1+ assists | 0.232 | 0.365 | 37/64 | +0.112 | PRIOR_HEAVY |
| Trevor Connelly: 1+ points | 0.395 | 0.520 | 53/49 | +0.098 | PRIOR_HEAVY |
| Jack Eichel: 2+ points | 0.269 | 0.390 | 40/62 | +0.095 | STANDARD |
| Mitch Marner: 2+ points | 0.228 | 0.340 | 35/67 | +0.086 | STANDARD |
| Mitch Marner: 1+ assists | 0.445 | 0.555 | 56/45 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
