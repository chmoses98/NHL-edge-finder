# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T11:32:39Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 3253 · contracts joined: 1332 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1057, 'OK': 180, 'NO_EDGE': 95}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 134, 'game_early_goal': 11, 'first_goal': 160, 'game_winner': 22, 'player_goals': 311, 'game_overtime': 11, 'player_points': 166, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-6h | 0.456 | 0.544 | 0.168 | 6.68 | 3.19 | 3.49 | 216 (25/191) | PROJECTED/PROJECTED |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-6h | 0.535 | 0.465 | 0.178 | 6.02 | 3.12 | 2.90 | 217 (25/192) | PROJECTED/PROJECTED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-6h | 0.613 | 0.388 | 0.172 | 6.06 | 3.38 | 2.68 | 182 (25/157) | PROJECTED/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-6h | 0.608 | 0.392 | 0.164 | 6.67 | 3.70 | 2.98 | 198 (25/173) | PROJECTED/PROJECTED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-6h | 0.496 | 0.504 | 0.179 | 5.93 | 2.95 | 2.98 | 213 (25/188) | PROJECTED/PROJECTED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-6h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 51 (25/26) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-12h | 0.494 | 0.505 | 0.180 | 5.87 | 2.91 | 2.96 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-12h | 0.536 | 0.464 | 0.172 | 6.38 | 3.30 | 3.08 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-12h | 0.529 | 0.471 | 0.179 | 6.05 | 3.12 | 2.93 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-12h | 0.558 | 0.442 | 0.161 | 6.66 | 3.53 | 3.13 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-12h | 0.666 | 0.334 | 0.162 | 6.25 | 3.66 | 2.58 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.608 | 0.735 | 0.712 | 74 | 27 | no | +0.108 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.392 | 0.265 | 0.288 | 27 | 74 | yes | +0.108 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.573 | 0.440 | 0.467 | 45 | 57 | yes | +0.106 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.356 | 0.230 | 0.252 | 24 | 78 | yes | +0.103 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.263 | 0.380 | 0.355 | 39 | 63 | no | +0.091 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.394 | 0.505 | 0.482 | 51 | 50 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.781 | 0.675 | 0.698 | 68 | 33 | yes | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.191 | 0.095 | 0.110 | 10 | 91 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.299 | 0.395 | 0.375 | 40 | 61 | no | +0.075 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.388 | 0.295 | 0.312 | 30 | 71 | yes | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.545 | 0.526 | 55 | 46 | no | +0.072 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.441 | 0.535 | 0.516 | 54 | 47 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.345 | 0.326 | 35 | 66 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.206 | 0.125 | 0.139 | 13 | 88 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.248 | 0.335 | 0.316 | 34 | 67 | no | +0.067 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.613 | 0.695 | 0.679 | 70 | 31 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.351 | 0.440 | 0.422 | 45 | 57 | no | +0.062 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.666 | 0.745 | 0.730 | 75 | 26 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.334 | 0.255 | 0.270 | 26 | 75 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.382 | 0.470 | 0.452 | 48 | 54 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.666 | 0.740 | 0.726 | 75 | 27 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.575 | 0.650 | 0.635 | 66 | 36 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.354 | 0.435 | 0.418 | 45 | 58 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.730 | 0.795 | 0.783 | 80 | 21 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.576 | 0.645 | 0.632 | 65 | 36 | no | +0.048 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.496 | 0.565 | 0.551 | 57 | 44 | no | +0.047 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.504 | 0.435 | 0.449 | 44 | 57 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.330 | 0.265 | 0.277 | 27 | 74 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.119 | 0.065 | 0.074 | 7 | 94 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.311 | 0.380 | 0.366 | 39 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.789 | 0.845 | 0.835 | 85 | 16 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.085 | 0.030 | 0.037 | 4 | 98 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.590 | 0.574 | 61 | 43 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.284 | 0.225 | 0.236 | 23 | 78 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.394 | 0.455 | 0.443 | 46 | 55 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.545 | 0.533 | 55 | 46 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.179 | 0.245 | 0.231 | 26 | 77 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.792 | 0.845 | 0.835 | 85 | 16 | no | +0.038 | OK |
| KXNHLGAME-26OCT15NYIOTT-NYI | game_winner | 0.465 | 0.405 | 0.417 | 41 | 60 | yes | +0.038 | OK |
| KXNHLGAME-26OCT15NYIOTT-OTT | game_winner | 0.535 | 0.595 | 0.583 | 60 | 41 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.505 | 0.565 | 0.553 | 57 | 44 | no | +0.038 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.544 | 0.485 | 0.497 | 49 | 52 | yes | +0.036 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.456 | 0.515 | 0.503 | 52 | 49 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.279 | 0.340 | 0.327 | 35 | 67 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.522 | 0.465 | 0.476 | 47 | 54 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-OTT3 | game_spread | 0.193 | 0.245 | 0.234 | 25 | 76 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN3 | game_spread | 0.183 | 0.235 | 0.224 | 24 | 77 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF6 | team_total | 0.141 | 0.095 | 0.103 | 10 | 91 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-NYI2 | game_spread | 0.256 | 0.205 | 0.215 | 21 | 80 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI4 | team_total | 0.271 | 0.330 | 0.318 | 34 | 68 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.244 | 0.190 | 0.200 | 20 | 82 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.850 | 0.895 | 0.887 | 90 | 11 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT15SEATB-SEA2 | game_spread | 0.192 | 0.145 | 0.154 | 15 | 86 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.714 | 0.765 | 0.755 | 77 | 24 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.560 | 0.500 | 0.512 | 51 | 51 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.253 | 0.310 | 0.298 | 32 | 70 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.159 | 0.115 | 0.123 | 12 | 89 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.717 | 0.775 | 0.764 | 79 | 24 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.822 | 0.870 | 0.861 | 88 | 14 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-7 | game_total | 0.403 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.179 | 0.230 | 0.219 | 24 | 78 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.170 | 0.159 | 18 | 84 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-5 | game_total | 0.740 | 0.790 | 0.781 | 80 | 22 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN2 | game_spread | 0.307 | 0.355 | 0.345 | 36 | 65 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.342 | 0.290 | 0.300 | 30 | 72 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.617 | 0.670 | 0.660 | 68 | 34 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-CHI | game_winner | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.722 | 0.675 | 0.685 | 68 | 33 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.878 | 0.920 | 0.913 | 93 | 9 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-6 | game_total | 0.516 | 0.565 | 0.555 | 57 | 44 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.269 | 0.220 | 0.229 | 23 | 79 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI2 | team_total | 0.721 | 0.770 | 0.761 | 78 | 24 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT15PHIDET-PHI3 | game_spread | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 0.456 | 0.512 | 0.168 | 0.215 | 6.68 | 6.47 | 0.978/0.997 | KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 -0.069 |
| NYI @ OTT | 0.535 | 0.572 | 0.178 | 0.221 | 6.02 | 6.13 | 0.998/0.956 | KXNHLTEAMTOTAL-26OCT15NYIOTT-OTT4 +0.048 |
| SEA @ TBL | 0.613 | 0.581 | 0.172 | 0.220 | 6.06 | 6.08 | 0.958/1.005 | KXNHLSPREAD-26OCT15SEATB-TB2 -0.035 |
| VAN @ FLA | 0.608 | 0.564 | 0.164 | 0.216 | 6.67 | 6.43 | 0.998/1.026 | KXNHLTEAMTOTAL-26OCT15VANFLA-FLA4 -0.060 |
| NYR @ NJD | 0.496 | 0.516 | 0.179 | 0.222 | 5.93 | 6.05 | 0.987/0.992 | KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 +0.029 |
| PHI @ DET | 0.603 | 0.517 | 0.179 | 0.218 | 5.79 | 5.82 | 1.024/0.991 | KXNHLGAME-26OCT15PHIDET-DET -0.086 |
| WPG @ CHI | 0.494 | 0.481 | 0.180 | 0.218 | 5.87 | 6.19 | 1.003/0.988 | KXNHLTOTAL-26OCT15WPGCHI-7 +0.059 |
| SJS @ NSH | 0.536 | 0.536 | 0.172 | 0.213 | 6.38 | 6.51 | 1.000/1.026 | KXNHLTOTAL-26OCT15SJNSH-7 +0.022 |
| STL @ MIN | 0.529 | 0.552 | 0.179 | 0.218 | 6.05 | 6.40 | 0.995/0.993 | KXNHLTEAMTOTAL-26OCT15STLMIN-MIN4 +0.066 |
| UTA @ EDM | 0.558 | 0.579 | 0.161 | 0.208 | 6.66 | 6.78 | 0.994/0.992 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM4 +0.034 |
| CGY @ VGK | 0.666 | 0.660 | 0.162 | 0.198 | 6.25 | 6.17 | 1.003/0.997 | KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 -0.020 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 17 recommended · full analysis in card.md / packet.json `thesis_card`

- Adam Pelech: 1+ goals YES @ 4c · p 0.062 (adj 0.0527) · $2.19 · thesis NYI:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 10c · p 0.1306 (adj 0.1205) · $3.65 · thesis NYI:OFFENSE_4PLUS
- Carter Yakemchuk: 1+ assists NO @ 67c · p 0.7371 (adj 0.6961) · $8.92 · thesis OTT:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 8c · p 0.1263 (adj 0.1135) · $6.44 · thesis SEA:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 67c · p 0.7628 (adj 0.7139) · $17.22 · thesis GAME:TIGHT
- Ben Meyers: 1+ goals YES @ 9c · p 0.1197 (adj 0.1098) · $3.32 · thesis SEA:OFFENSE_4PLUS
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6452 (adj 0.6289) · $10.61 · thesis TBL:SUPPRESSED
- Vancouver over 4.5 goals scored YES @ 10c · p 0.1858 (adj 0.1404) · $5.76 · thesis VAN:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1873 (adj 0.1705) · $7.16 · thesis VAN:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 63c · p 0.6948 (adj 0.6736) · $19.75 · thesis FLA:SUPPRESSED
- Marco Rossi: 1+ assists YES @ 24c · p 0.3233 (adj 0.2766) · $4.16 · thesis VAN:OFFENSE_4PLUS
- Matt Rempe: 1+ goals YES @ 6c · p 0.0899 (adj 0.0799) · $3.59 · thesis NYR:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 77c · p 0.8246 (adj 0.7948) · $14.46 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.7854 (adj 0.7452) · $13.8 · thesis NYR:SUPPRESSED
- Gabe Perreault: 1+ assists YES @ 23c · p 0.3241 (adj 0.2532) · $2.64 · thesis NYR:OFFENSE_4PLUS
- Vegas wins by over 1.5 goals NO @ 47c · p 0.5586 (adj 0.5118) · $8.53 · thesis GAME:TIGHT
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6902 (adj 0.6476) · $5.75 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.87, exp saves 26.74 (sd 7.08), pull risk 0.063
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.46 (sd 6.27), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ assists | 0.344 | 0.260 | 28/76 | +0.049 | STANDARD |
| Tage Thompson: 1+ assists | 0.347 | 0.425 | 44/59 | +0.046 | STANDARD |
| Tage Thompson: 1+ points | 0.578 | 0.650 | 67/37 | +0.036 | STANDARD |
| Tage Thompson: 2+ points | 0.218 | 0.290 | 32/74 | +0.029 | STANDARD |
| Owen Power: 1+ assists | 0.440 | 0.370 | 39/65 | +0.034 | STANDARD |
| Easton Cowan: 1+ points | 0.468 | 0.400 | 42/62 | +0.031 | STANDARD |

**NYI @ OTT** · priced 159/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.99, exp saves 22.64 (sd 6.16), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.57, exp saves 23.58 (sd 6.56), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Bo Horvat: 1+ goals | 0.295 | 0.190 | 36/98 | -0.081 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.319 | 0.415 | 44/61 | +0.054 | STANDARD |
| Jordan Spence: 1+ assists | 0.350 | 0.260 | 29/77 | +0.045 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.173 | 0.260 | 29/77 | +0.045 | STANDARD |
| Andre Burakovsky: 1+ points | 0.302 | 0.385 | 41/64 | +0.042 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.263 | 0.345 | 36/67 | +0.052 | STANDARD |

**SEA @ TBL** · priced 127/131 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.41, exp saves 21.37 (sd 5.94), pull risk 0.047
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.47 (sd 6.92), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.316 | 0.495 | 51/52 | +0.146 | STANDARD |
| John Carlson: 1+ points | 0.399 | 0.575 | 60/45 | +0.134 | STANDARD |
| Nikita Kucherov: 2+ points | 0.314 | 0.470 | 49/55 | +0.119 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.502 | 0.645 | 67/38 | +0.101 | STANDARD |
| John Carlson: 2+ points | 0.091 | 0.220 | 25/81 | +0.088 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.150 | 0.275 | 30/75 | +0.086 | STANDARD |

**VAN @ FLA** · priced 143/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 24.7, exp saves 21.65 (sd 6.11), pull risk 0.055
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.21, exp saves 24.99 (sd 6.84), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Bennett: 1+ goals | 0.321 | 0.175 | 33/98 | -0.025 | STANDARD |
| Marco Rossi: 1+ goals | 0.237 | 0.095 | 17/98 | +0.057 | STANDARD |
| Linus Karlsson: 1+ goals | 0.219 | 0.085 | 15/98 | +0.060 | STANDARD |
| Brady Tkachuk: 2+ points | 0.165 | 0.295 | 32/73 | +0.091 | STANDARD |
| Marco Rossi: 1+ points | 0.483 | 0.360 | 38/66 | +0.087 | STANDARD |
| Brady Tkachuk: 1+ points | 0.519 | 0.635 | 66/39 | +0.075 | STANDARD |

**NYR @ NJD** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.13, exp saves 20.98 (sd 5.99), pull risk 0.054
- NYR net: Dylan Garand (PROJECTED) exp shots 29.99, exp saves 25.82 (sd 6.94), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.386 | 0.510 | 53/51 | +0.086 | STANDARD |
| Jack Hughes: 2+ points | 0.222 | 0.345 | 36/67 | +0.093 | STANDARD |
| Gabe Perreault: 1+ assists | 0.324 | 0.215 | 23/80 | +0.082 | STANDARD |
| Jack Hughes: 1+ points | 0.589 | 0.495 | 72/73 | -0.145 | STANDARD |
| Cody Glass: 1+ goals | 0.164 | 0.075 | 13/98 | +0.026 | STANDARD |
| Nico Hischier: 1+ points | 0.494 | 0.575 | 60/45 | +0.039 | STANDARD |

**PHI @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

**WPG @ CHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.63, exp saves 23.86 (sd 6.62), pull risk 0.067
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.12, exp saves 21.77 (sd 6.08), pull risk 0.06

**SJS @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.54, exp saves 23.88 (sd 6.63), pull risk 0.066
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.73), pull risk 0.079

**STL @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 26.75, exp saves 23.2 (sd 6.33), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.77), pull risk 0.071

**UTA @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.2, exp saves 23.7 (sd 6.46), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

**CGY @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.19 (sd 6.2), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.46 (sd 7.16), pull risk 0.089

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
