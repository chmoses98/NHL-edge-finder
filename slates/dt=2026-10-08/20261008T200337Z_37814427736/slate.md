# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T20:03:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3984 · contracts joined: 1926 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 1676, 'OK': 161, 'NO_EDGE': 89}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 229, 'game_early_goal': 10, 'first_goal': 350, 'game_winner': 20, 'player_goals': 527, 'game_overtime': 10, 'player_points': 296, 'goalie_saves': 14, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-90m | 0.522 | 0.478 | 0.178 | 5.99 | 3.06 | 2.93 | 95 (25/70) | CONFIRMED/PROBABLE |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-90m | 0.563 | 0.437 | 0.179 | 6.03 | 3.21 | 2.81 | 176 (25/151) | PROBABLE/CONFIRMED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-90m | 0.590 | 0.410 | 0.168 | 6.54 | 3.56 | 2.97 | 170 (25/145) | CONFIRMED/PROBABLE |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-90m | 0.603 | 0.397 | 0.167 | 6.27 | 3.47 | 2.80 | 215 (25/190) | CONFIRMED/CONFIRMED |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-90m | 0.552 | 0.448 | 0.175 | 5.88 | 3.09 | 2.79 | 207 (25/182) | PROBABLE/CONFIRMED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-90m | 0.680 | 0.320 | 0.154 | 6.67 | 3.94 | 2.73 | 217 (25/192) | PROBABLE/PROBABLE |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-3h | 0.608 | 0.392 | 0.176 | 5.79 | 3.23 | 2.56 | 201 (25/176) | CONFIRMED/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-3h | 0.599 | 0.401 | 0.172 | 6.17 | 3.41 | 2.77 | 205 (25/180) | CONFIRMED/CONFIRMED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-3h | 0.435 | 0.565 | 0.183 | 5.61 | 2.61 | 3.00 | 211 (25/186) | CONFIRMED/PROBABLE |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-3h | 0.653 | 0.347 | 0.153 | 7.06 | 4.05 | 3.01 | 229 (25/204) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.362 | 0.545 | 0.508 | 55 | 46 | no | +0.160 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.586 | 0.745 | 0.716 | 75 | 26 | no | +0.141 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.184 | 0.330 | 0.297 | 34 | 68 | no | +0.120 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.326 | 0.465 | 0.436 | 47 | 54 | no | +0.116 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.195 | 0.325 | 0.296 | 33 | 68 | no | +0.109 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.435 | 0.315 | 0.338 | 32 | 69 | yes | +0.100 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.565 | 0.685 | 0.662 | 69 | 32 | no | +0.100 | OK |
| KXNHLTOTAL-26OCT08COLCGY-7 | game_total | 0.349 | 0.465 | 0.441 | 47 | 54 | no | +0.094 | OK |
| KXNHLTOTAL-26OCT08COLCGY-6 | game_total | 0.461 | 0.575 | 0.552 | 58 | 43 | no | +0.092 | OK |
| KXNHLTOTAL-26OCT08COLCGY-5 | game_total | 0.695 | 0.795 | 0.777 | 80 | 21 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.800 | 0.895 | 0.880 | 90 | 11 | no | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.389 | 0.295 | 0.313 | 30 | 71 | yes | +0.074 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.386 | 0.295 | 0.312 | 30 | 71 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.516 | 0.425 | 0.443 | 43 | 58 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.324 | 0.415 | 0.396 | 42 | 59 | no | +0.069 | OK |
| KXNHLTOTAL-26OCT08COLCGY-8 | game_total | 0.178 | 0.265 | 0.246 | 27 | 74 | no | +0.068 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.290 | 0.205 | 0.220 | 21 | 80 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.300 | 0.215 | 0.230 | 22 | 79 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.595 | 0.505 | 0.523 | 51 | 50 | yes | +0.067 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.320 | 0.235 | 0.251 | 24 | 77 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT08COLCGY-4 | game_total | 0.795 | 0.875 | 0.862 | 88 | 13 | no | +0.067 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.563 | 0.475 | 0.493 | 48 | 53 | yes | +0.065 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.437 | 0.525 | 0.507 | 53 | 48 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.747 | 0.665 | 0.682 | 67 | 34 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL6 | team_total | 0.080 | 0.160 | 0.140 | 17 | 85 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.463 | 0.545 | 0.529 | 55 | 46 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.696 | 0.615 | 0.632 | 62 | 39 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.218 | 0.140 | 0.153 | 15 | 87 | yes | +0.059 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.680 | 0.755 | 0.741 | 76 | 25 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.230 | 0.305 | 0.289 | 31 | 70 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.538 | 0.620 | 0.604 | 63 | 39 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.779 | 0.705 | 0.721 | 71 | 30 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.149 | 0.080 | 0.091 | 9 | 93 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.222 | 0.155 | 0.167 | 16 | 85 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.127 | 0.195 | 0.180 | 20 | 81 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT08COLCGY-9 | game_total | 0.120 | 0.190 | 0.174 | 20 | 82 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-8 | game_total | 0.271 | 0.205 | 0.217 | 21 | 80 | yes | +0.049 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.587 | 0.515 | 0.530 | 52 | 49 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB4 | team_total | 0.384 | 0.455 | 0.441 | 46 | 55 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-6 | game_total | 0.574 | 0.505 | 0.519 | 51 | 50 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.319 | 0.390 | 0.375 | 40 | 62 | no | +0.045 | OK |
| KXNHLGAME-26OCT08UTABOS-BOS | game_winner | 0.522 | 0.455 | 0.468 | 46 | 55 | yes | +0.044 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.478 | 0.545 | 0.532 | 55 | 46 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.765 | 0.825 | 0.814 | 83 | 18 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-7 | game_total | 0.459 | 0.395 | 0.408 | 40 | 61 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.336 | 0.275 | 0.287 | 28 | 73 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.158 | 0.105 | 0.114 | 11 | 90 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.157 | 0.100 | 0.110 | 11 | 91 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA3 | game_spread | 0.150 | 0.205 | 0.193 | 21 | 80 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT08UTABOS-UTA2 | team_total | 0.781 | 0.835 | 0.825 | 84 | 17 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.445 | 0.385 | 0.397 | 39 | 62 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-PHI3 | team_total | 0.534 | 0.475 | 0.487 | 48 | 53 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08UTABOS-UTA3 | team_total | 0.568 | 0.630 | 0.618 | 64 | 38 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.119 | 0.075 | 0.082 | 8 | 93 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT08MINTB-5 | game_total | 0.735 | 0.785 | 0.776 | 79 | 22 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.715 | 0.765 | 0.755 | 77 | 24 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT08MINTB-6 | game_total | 0.511 | 0.565 | 0.554 | 57 | 44 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.910 | 0.865 | 0.875 | 87 | 14 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-9 | game_total | 0.190 | 0.145 | 0.153 | 15 | 86 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL5 | team_total | 0.158 | 0.205 | 0.195 | 21 | 80 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA2 | game_spread | 0.265 | 0.315 | 0.305 | 32 | 69 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT08VANCAR-8 | game_total | 0.334 | 0.285 | 0.294 | 29 | 72 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT08VANCAR-9 | game_total | 0.240 | 0.195 | 0.203 | 20 | 81 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT08TORVGK-5 | game_total | 0.859 | 0.815 | 0.824 | 82 | 19 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.311 | 0.265 | 0.274 | 27 | 74 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT08UTABOS-BOS2 | game_spread | 0.300 | 0.255 | 0.264 | 26 | 75 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB3 | team_total | 0.607 | 0.660 | 0.650 | 67 | 35 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT08VANCAR-10 | game_total | 0.122 | 0.085 | 0.091 | 9 | 92 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT08MINTB-4 | game_total | 0.825 | 0.865 | 0.858 | 87 | 14 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08UTABOS-UTA4 | team_total | 0.348 | 0.395 | 0.385 | 40 | 61 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB5 | team_total | 0.202 | 0.250 | 0.240 | 26 | 76 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT08MINTB-8 | game_total | 0.212 | 0.255 | 0.246 | 26 | 75 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT08MINTB-7 | game_total | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-9 | game_total | 0.225 | 0.185 | 0.193 | 19 | 82 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT08MINTB-TB3 | game_spread | 0.194 | 0.235 | 0.226 | 24 | 77 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT08COLCGY-10 | game_total | 0.051 | 0.085 | 0.077 | 9 | 92 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT5 | team_total | 0.276 | 0.230 | 0.239 | 24 | 78 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-PHI5 | team_total | 0.160 | 0.125 | 0.131 | 13 | 88 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF5 | team_total | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.022 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 0.522 | 0.510 | 0.178 | 0.213 | 5.99 | 6.45 | 0.955/0.999 | KXNHLTOTAL-26OCT08UTABOS-7 +0.084 |
| DAL @ BUF | 0.563 | 0.530 | 0.179 | 0.225 | 6.03 | 6.20 | 1.000/0.993 | KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 +0.046 |
| NSH @ MTL | 0.590 | 0.566 | 0.168 | 0.210 | 6.54 | 6.60 | 0.983/1.002 | KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH4 +0.027 |
| PHI @ OTT | 0.603 | 0.597 | 0.167 | 0.222 | 6.27 | 5.86 | 0.968/0.990 | KXNHLTOTAL-26OCT08PHIOTT-6 -0.075 |
| MIN @ TBL | 0.552 | 0.521 | 0.175 | 0.223 | 5.88 | 6.32 | 0.979/0.991 | KXNHLTOTAL-26OCT08MINTB-7 +0.074 |
| VAN @ CAR | 0.680 | 0.615 | 0.154 | 0.205 | 6.67 | 6.59 | 1.000/1.026 | KXNHLSPREAD-26OCT08VANCAR-CAR2 -0.067 |
| CHI @ NYI | 0.608 | 0.619 | 0.176 | 0.210 | 5.79 | 6.23 | 0.947/1.003 | KXNHLTOTAL-26OCT08CHINYI-7 +0.080 |
| SJS @ STL | 0.599 | 0.565 | 0.172 | 0.215 | 6.17 | 6.36 | 0.976/1.021 | KXNHLTEAMTOTAL-26OCT08SJSTL-SJ3 +0.050 |
| COL @ CGY | 0.435 | 0.433 | 0.183 | 0.218 | 5.61 | 6.25 | 0.978/0.972 | KXNHLTOTAL-26OCT08COLCGY-7 +0.111 |
| TOR @ VGK | 0.653 | 0.658 | 0.153 | 0.201 | 7.06 | 6.35 | 1.003/0.983 | KXNHLTOTAL-26OCT08TORVGK-6 -0.115 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Boston over 4.5 goals scored YES @ 18c · p 0.2328 (adj 0.2039) · $1.1 · thesis BOS:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 14c · p 0.2157 (adj 0.1955) · $5.32 · thesis BUF:OFFENSE_4PLUS
- Justin Danforth: 1+ goals YES @ 8c · p 0.122 (adj 0.1103) · $2.53 · thesis BUF:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 12c · p 0.1604 (adj 0.1453) · $1.89 · thesis BUF:OFFENSE_4PLUS
- Zach Benson: 1+ goals YES @ 22c · p 0.2661 (adj 0.2533) · $2.93 · thesis BUF:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 24c · p 0.2955 (adj 0.2791) · $3.69 · thesis NSH:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 12c · p 0.1581 (adj 0.1473) · $2.27 · thesis MTL:WINS_BY_2PLUS
- Josh Anderson: 1+ goals YES @ 14c · p 0.18 (adj 0.1675) · $2.29 · thesis MTL:OFFENSE_4PLUS
- Alexandre Carrier: 1+ goals YES @ 5c · p 0.0697 (adj 0.0635) · $1.04 · thesis MTL:OFFENSE_4PLUS
- William Eklund: 1+ assists NO @ 61c · p 0.7854 (adj 0.6681) · $8.59 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1762 (adj 0.1634) · $2.97 · thesis OTT:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 13c · p 0.168 (adj 0.1573) · $2.33 · thesis PHI:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 8c · p 0.1091 (adj 0.1006) · $1.68 · thesis OTT:OFFENSE_4PLUS
- Ilya Mikheyev: 1+ goals YES @ 15c · p 0.1991 (adj 0.1856) · $3.35 · thesis TBL:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 18c · p 0.2304 (adj 0.2165) · $3.22 · thesis MIN:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 58c · p 0.7237 (adj 0.627) · $8.59 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 40c · p 0.4915 (adj 0.4433) · $4.28 · thesis TBL:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 15c · p 0.2155 (adj 0.1979) · $4.28 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 18c · p 0.2511 (adj 0.2321) · $4.75 · thesis VAN:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 63c · p 0.7053 (adj 0.6852) · $8.35 · thesis CAR:SUPPRESSED
- Carolina wins by over 2.5 goals NO @ 59c · p 0.7282 (adj 0.6351) · $4.09 · thesis GAME:TIGHT
- Ryan Greene: 1+ goals YES @ 10c · p 0.1545 (adj 0.1396) · $3.55 · thesis CHI:OFFENSE_4PLUS
- Wyatt Kaiser: 1+ goals YES @ 3c · p 0.0549 (adj 0.0474) · $1.37 · thesis CHI:OFFENSE_4PLUS
- Calum Ritchie: 1+ assists YES @ 26c · p 0.3499 (adj 0.3024) · $3.89 · thesis NYI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7266 (adj 0.6313) · $8.3 · thesis CHI:SUPPRESSED
- Philip Broberg: 1+ goals YES @ 7c · p 0.1005 (adj 0.0916) · $1.8 · thesis STL:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 70c · p 0.789 (adj 0.7395) · $8.59 · thesis SJS:SUPPRESSED
- Mason McTavish: 1+ assists NO @ 70c · p 0.7833 (adj 0.7391) · $8.59 · thesis STL:SUPPRESSED
- Pius Suter: 1+ goals YES @ 14c · p 0.1762 (adj 0.1659) · $2.13 · thesis STL:OFFENSE_4PLUS
- Martin Necas: 1+ goals NO @ 62c · p 0.7006 (adj 0.6792) · $6.45 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.644 (adj 0.6205) · $6.45 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6624 (adj 0.5796) · $3.18 · thesis GAME:TIGHT
- Scott Wedgewood: 22+ saves YES @ 51c · p 0.5877 (adj 0.5438) · $3.46 · thesis COL:NET_HIGH_VOLUME
- Teddy Blueger: 1+ goals YES @ 8c · p 0.1149 (adj 0.1049) · $2.09 · thesis TOR:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0882 (adj 0.0799) · $1.63 · thesis VGK:OFFENSE_4PLUS
- Braeden Bowman: 1+ goals YES @ 17c · p 0.2131 (adj 0.1998) · $2.44 · thesis VGK:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 66c · p 0.7021 (adj 0.6903) · $4.8 · thesis TOR:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 38/44 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.45, exp saves 24.61 (sd 6.85), pull risk 0.062
- UTA net: Sebastian Cossa (PROBABLE) exp shots 26.34, exp saves 22.54 (sd 6.33), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Cossa: 24+ saves | 0.433 | 0.470 | 48/54 | +0.009 |  |
| JJ Peterka: First Goalscorer | 0.035 | 0.050 | 5/ | -0.019 | STANDARD |
| Frederic Brunet: First Goalscorer | 0.009 | 0.020 | 2/ | -0.013 | PRIOR_HEAVY |
| Nate Schmidt: First Goalscorer | 0.010 | 0.020 | 2/ | -0.012 | STANDARD |
| Nick Schmaltz: First Goalscorer | 0.060 | 0.070 | 7/ | -0.014 | STANDARD |
| James Hagens: First Goalscorer | 0.031 | 0.040 | 4/ | -0.012 | PRIOR_HEAVY |

**DAL @ BUF** · priced 119/125 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROBABLE) exp shots 25.45, exp saves 22.11 (sd 6.07), pull risk 0.054
- DAL net: Jake Oettinger (CONFIRMED) exp shots 27.04, exp saves 23.29 (sd 6.58), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Oettinger: 22+ saves | 0.612 | 0.525 | 54/49 | +0.055 |  |
| Owen Power: 1+ assists | 0.391 | 0.305 | 32/71 | +0.056 | STANDARD |
| Zach Benson: 1+ points | 0.536 | 0.455 | 46/55 | +0.059 | STANDARD |
| Jiri Kulich: 1+ goals | 0.216 | 0.135 | 14/87 | +0.067 | STANDARD |
| Zach Benson: 1+ assists | 0.372 | 0.300 | 31/71 | +0.047 | STANDARD |
| Tage Thompson: 1+ assists | 0.361 | 0.425 | 44/59 | +0.032 | STANDARD |

**NSH @ MTL** · priced 113/119 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.02, exp saves 24.28 (sd 6.54), pull risk 0.061
- NSH net: Juuse Saros (PROBABLE) exp shots 27.64, exp saves 23.6 (sd 6.64), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.205 | 0.320 | 33/69 | +0.090 | STANDARD |
| Chris Kreider: 1+ points | 0.411 | 0.525 | 53/48 | +0.092 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.480 | 0.370 | 39/65 | +0.073 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.352 | 0.260 | 27/75 | +0.068 | STANDARD |
| Juuse Saros: 27+ saves | 0.325 | 0.250 | 45/95 | -0.143 |  |
| Ryan O'Reilly: 1+ goals | 0.295 | 0.230 | 24/78 | +0.043 | STANDARD |

**PHI @ OTT** · priced 160/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (CONFIRMED) exp shots 23.58, exp saves 20.65 (sd 5.77), pull risk 0.041
- PHI net: Joseph Woll (CONFIRMED) exp shots 28.92, exp saves 24.87 (sd 6.81), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.215 | 0.395 | 40/61 | +0.159 | STANDARD |
| William Eklund: 1+ points | 0.395 | 0.550 | 56/46 | +0.128 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.231 | 0.375 | 38/63 | +0.122 | PRIOR_HEAVY |
| Carter Yakemchuk: 1+ points | 0.289 | 0.430 | 44/58 | +0.114 | PRIOR_HEAVY |
| Tim Stutzle: 1+ assists | 0.419 | 0.525 | 53/48 | +0.084 | STANDARD |
| Jordan Spence: 1+ assists | 0.335 | 0.230 | 24/78 | +0.083 | STANDARD |

**MIN @ TBL** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Dennis Hildeby (PROBABLE) exp shots 26.09, exp saves 22.6 (sd 6.27), pull risk 0.06
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.6, exp saves 25.56 (sd 6.93), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.276 | 0.425 | 43/58 | +0.127 | STANDARD |
| John Carlson: 1+ points | 0.361 | 0.500 | 51/51 | +0.112 | STANDARD |
| Nikita Kucherov: 2+ points | 0.318 | 0.425 | 44/59 | +0.075 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.508 | 0.605 | 61/40 | +0.075 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.154 | 0.245 | 26/77 | +0.064 | STANDARD |
| John Carlson: 2+ points | 0.075 | 0.160 | 18/86 | +0.056 | STANDARD |

**VAN @ CAR** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 22.48, exp saves 19.72 (sd 5.67), pull risk 0.055
- VAN net: Kevin Lankinen (PROBABLE) exp shots 32.08, exp saves 27.11 (sd 7.43), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.347 | 0.530 | 54/48 | +0.155 | STANDARD |
| Sebastian Aho: 2+ points | 0.186 | 0.340 | 36/68 | +0.118 | STANDARD |
| Sebastian Aho: 1+ points | 0.537 | 0.680 | 69/33 | +0.117 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.429 | 0.540 | 55/47 | +0.083 | STANDARD |
| Sebastian Aho: 2+ assists | 0.072 | 0.180 | 20/84 | +0.079 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.535 | 0.640 | 65/37 | +0.079 | STANDARD |

**CHI @ NYI** · priced 150/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.34, exp saves 21.45 (sd 5.96), pull risk 0.047
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.51 (sd 7.12), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.273 | 0.420 | 43/59 | +0.120 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.223 | 0.340 | 35/67 | +0.092 | STANDARD |
| Kyle Palmieri: 1+ points | 0.424 | 0.525 | 54/49 | +0.068 | STANDARD |
| Calum Ritchie: 1+ assists | 0.350 | 0.255 | 26/75 | +0.076 | STANDARD |
| Patrick Kane: 1+ points | 0.456 | 0.550 | 56/46 | +0.067 | STANDARD |
| Ilya Sorokin: 24+ saves | 0.351 | 0.445 | 45/56 | +0.072 |  |

**SJS @ STL** · priced 152/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 25.77, exp saves 22.39 (sd 6.07), pull risk 0.051
- SJS net: Alex Nedeljkovic (CONFIRMED) exp shots 27.07, exp saves 23.1 (sd 6.65), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.300 | 0.405 | 41/60 | +0.083 | PRIOR_HEAVY |
| Mason Marchment: 1+ assists | 0.211 | 0.310 | 32/70 | +0.074 | STANDARD |
| Alex Nedeljkovic: 26+ saves | 0.351 | 0.445 | 51/62 | +0.012 |  |
| Mason McTavish: 1+ assists | 0.217 | 0.305 | 31/70 | +0.069 | STANDARD |
| Dmitry Orlov: 1+ assists | 0.339 | 0.255 | 27/76 | +0.055 | STANDARD |
| Dmitry Orlov: 1+ points | 0.378 | 0.300 | 31/71 | +0.053 | STANDARD |

**COL @ CGY** · priced 160/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 32.7, exp saves 27.85 (sd 7.5), pull risk 0.072
- COL net: Scott Wedgewood (PROBABLE) exp shots 26.32, exp saves 22.94 (sd 6.27), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.279 | 0.535 | 55/48 | +0.224 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.451 | 0.655 | 66/35 | +0.183 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.119 | 0.315 | 34/71 | +0.157 | STANDARD |
| Cale Makar: 1+ assists | 0.409 | 0.580 | 59/43 | +0.144 | STANDARD |
| Cale Makar: 1+ points | 0.500 | 0.665 | 68/35 | +0.134 | STANDARD |
| Cale Makar: 2+ points | 0.149 | 0.310 | 34/72 | +0.116 | STANDARD |

**TOR @ VGK** · priced 175/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (CONFIRMED) exp shots 24.89, exp saves 21.96 (sd 6.01), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.39, exp saves 26.49 (sd 7.38), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sergei Bobrovsky: 28+ saves | 0.444 | 0.270 | 47/93 | -0.043 |  |
| Kirill Marchenko: 1+ assists | 0.254 | 0.370 | 38/64 | +0.090 | STANDARD |
| Kirill Marchenko: 1+ points | 0.441 | 0.550 | 57/47 | +0.071 | STANDARD |
| Shea Theodore: 1+ assists | 0.455 | 0.350 | 37/67 | +0.068 | STANDARD |
| Darren Raddysh: 1+ points | 0.375 | 0.475 | 48/53 | +0.077 | STANDARD |
| Mitch Marner: 2+ points | 0.252 | 0.345 | 35/66 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
