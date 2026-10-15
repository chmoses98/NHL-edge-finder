# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T13:24:38Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4107 · contracts joined: 2186 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 1911, 'OK': 180, 'NO_EDGE': 95}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 281, 'game_early_goal': 11, 'first_goal': 351, 'game_winner': 22, 'player_goals': 618, 'game_overtime': 11, 'player_points': 375, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-6h | 0.456 | 0.544 | 0.168 | 6.68 | 3.19 | 3.49 | 216 (25/191) | PROJECTED/PROJECTED |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-6h | 0.535 | 0.465 | 0.178 | 6.02 | 3.12 | 2.90 | 217 (25/192) | PROJECTED/PROJECTED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-6h | 0.613 | 0.388 | 0.172 | 6.06 | 3.38 | 2.68 | 210 (25/185) | PROJECTED/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-6h | 0.608 | 0.392 | 0.164 | 6.67 | 3.70 | 2.98 | 198 (25/173) | PROJECTED/PROJECTED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-6h | 0.496 | 0.504 | 0.179 | 5.93 | 2.95 | 2.98 | 213 (25/188) | PROJECTED/PROJECTED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-6h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 211 (25/186) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-6h | 0.494 | 0.505 | 0.180 | 5.87 | 2.91 | 2.96 | 208 (25/183) | PROJECTED/PROJECTED |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-6h | 0.536 | 0.464 | 0.172 | 6.38 | 3.30 | 3.08 | 228 (25/203) | PROJECTED/PROJECTED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-6h | 0.529 | 0.471 | 0.179 | 6.05 | 3.12 | 2.93 | 213 (25/188) | PROJECTED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-6h | 0.558 | 0.442 | 0.161 | 6.66 | 3.53 | 3.13 | 221 (25/196) | PROJECTED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-12h | 0.666 | 0.334 | 0.162 | 6.25 | 3.66 | 2.58 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.573 | 0.435 | 0.463 | 44 | 57 | yes | +0.116 | OK |
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.608 | 0.735 | 0.712 | 74 | 27 | no | +0.108 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.356 | 0.230 | 0.252 | 24 | 78 | yes | +0.103 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.392 | 0.275 | 0.297 | 28 | 73 | yes | +0.098 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.263 | 0.375 | 0.351 | 38 | 63 | no | +0.091 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.394 | 0.505 | 0.482 | 51 | 50 | no | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.781 | 0.675 | 0.698 | 68 | 33 | yes | +0.085 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.191 | 0.095 | 0.110 | 10 | 91 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.299 | 0.395 | 0.375 | 40 | 61 | no | +0.075 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.388 | 0.295 | 0.312 | 30 | 71 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.441 | 0.535 | 0.516 | 54 | 47 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.382 | 0.475 | 0.456 | 48 | 53 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.206 | 0.125 | 0.139 | 13 | 88 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.248 | 0.335 | 0.316 | 34 | 67 | no | +0.067 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.613 | 0.695 | 0.679 | 70 | 31 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.540 | 0.522 | 55 | 47 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.351 | 0.435 | 0.418 | 44 | 57 | no | +0.062 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.666 | 0.745 | 0.730 | 75 | 26 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.334 | 0.255 | 0.270 | 26 | 75 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.335 | 0.318 | 34 | 67 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.354 | 0.435 | 0.418 | 44 | 57 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.666 | 0.740 | 0.726 | 75 | 27 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.575 | 0.650 | 0.635 | 66 | 36 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.730 | 0.795 | 0.783 | 80 | 21 | no | +0.048 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.496 | 0.565 | 0.551 | 57 | 44 | no | +0.047 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.504 | 0.435 | 0.449 | 44 | 57 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.330 | 0.265 | 0.277 | 27 | 74 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.279 | 0.345 | 0.331 | 35 | 66 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.244 | 0.185 | 0.196 | 19 | 82 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.311 | 0.380 | 0.366 | 39 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.560 | 0.495 | 0.508 | 50 | 51 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.789 | 0.845 | 0.835 | 85 | 16 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.085 | 0.030 | 0.037 | 4 | 98 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.575 | 0.562 | 58 | 43 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.284 | 0.225 | 0.236 | 23 | 78 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.394 | 0.455 | 0.443 | 46 | 55 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-5 | game_total | 0.740 | 0.795 | 0.785 | 80 | 21 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.179 | 0.245 | 0.231 | 26 | 77 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.792 | 0.845 | 0.835 | 85 | 16 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.342 | 0.280 | 0.292 | 29 | 73 | yes | +0.038 | OK |
| KXNHLGAME-26OCT15NYIOTT-NYI | game_winner | 0.465 | 0.405 | 0.417 | 41 | 60 | yes | +0.038 | OK |
| KXNHLGAME-26OCT15NYIOTT-OTT | game_winner | 0.535 | 0.595 | 0.583 | 60 | 41 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.576 | 0.640 | 0.628 | 65 | 37 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.505 | 0.565 | 0.553 | 57 | 44 | no | +0.038 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.544 | 0.485 | 0.497 | 49 | 52 | yes | +0.036 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.456 | 0.515 | 0.503 | 52 | 49 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.522 | 0.465 | 0.476 | 47 | 54 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-OTT3 | game_spread | 0.193 | 0.245 | 0.234 | 25 | 76 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-NYI2 | game_spread | 0.256 | 0.205 | 0.215 | 21 | 80 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.119 | 0.070 | 0.078 | 8 | 94 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI4 | team_total | 0.271 | 0.325 | 0.314 | 33 | 68 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.850 | 0.895 | 0.887 | 90 | 11 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT15SEATB-SEA2 | game_spread | 0.192 | 0.145 | 0.154 | 15 | 86 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.714 | 0.765 | 0.755 | 77 | 24 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.253 | 0.310 | 0.298 | 32 | 70 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.159 | 0.115 | 0.123 | 12 | 89 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.127 | 0.085 | 0.092 | 9 | 92 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.717 | 0.775 | 0.764 | 79 | 24 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.822 | 0.870 | 0.861 | 88 | 14 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-7 | game_total | 0.403 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.179 | 0.230 | 0.219 | 24 | 78 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.540 | 0.529 | 55 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.170 | 0.159 | 18 | 84 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.476 | 0.420 | 0.431 | 43 | 59 | yes | +0.028 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN2 | game_spread | 0.307 | 0.355 | 0.345 | 36 | 65 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.617 | 0.670 | 0.660 | 68 | 34 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-CHI | game_winner | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.722 | 0.675 | 0.685 | 68 | 33 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.878 | 0.920 | 0.913 | 93 | 9 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-6 | game_total | 0.534 | 0.485 | 0.495 | 49 | 52 | yes | +0.027 | OK |
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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Tage Thompson: 1+ goals NO @ 60c · p 0.6455 (adj 0.6329) · $5.45 · thesis BUF:SUPPRESSED
- Adam Pelech: 1+ goals YES @ 4c · p 0.062 (adj 0.0527) · $1.11 · thesis NYI:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 10c · p 0.1306 (adj 0.1205) · $1.86 · thesis NYI:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 16c · p 0.1954 (adj 0.1828) · $1.98 · thesis OTT:OFFENSE_4PLUS
- Carter Yakemchuk: 1+ assists NO @ 67c · p 0.7371 (adj 0.6986) · $5.93 · thesis OTT:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 9c · p 0.1263 (adj 0.116) · $2.39 · thesis SEA:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 67c · p 0.7628 (adj 0.7139) · $9.37 · thesis GAME:TIGHT
- Ben Meyers: 1+ goals YES @ 9c · p 0.1197 (adj 0.111) · $1.87 · thesis SEA:OFFENSE_4PLUS
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6452 (adj 0.6289) · $5.44 · thesis TBL:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 15c · p 0.2187 (adj 0.1965) · $5.06 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 17c · p 0.2368 (adj 0.2176) · $5.39 · thesis VAN:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 62c · p 0.7029 (adj 0.6797) · $10.25 · thesis FLA:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1873 (adj 0.1692) · $4.21 · thesis VAN:OFFENSE_4PLUS
- Jack Hughes: 2+ assists NO @ 85c · p 0.9098 (adj 0.8749) · $10.25 · thesis NJD:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 77c · p 0.8246 (adj 0.7948) · $6.28 · thesis NYR:WINS
- New Jersey wins by over 1.5 goals NO @ 66c · p 0.7208 (adj 0.6879) · $1.54 · thesis NYR:WINS
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.7854 (adj 0.7452) · $6.91 · thesis NYR:SUPPRESSED
- Christian Dvorak: 1+ goals YES @ 19c · p 0.2329 (adj 0.2197) · $2.87 · thesis PHI:OFFENSE_4PLUS
- Denver Barkey: 1+ goals YES @ 14c · p 0.1734 (adj 0.1613) · $1.77 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 15c · p 0.1828 (adj 0.1709) · $1.6 · thesis PHI:OFFENSE_4PLUS
- Viktor Arvidsson: 1+ assists NO @ 66c · p 0.729 (adj 0.6895) · $5.75 · thesis DET:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 13c · p 0.1764 (adj 0.1623) · $3.33 · thesis CHI:OFFENSE_4PLUS
- Viggo Bjorck: 1+ goals NO @ 83c · p 0.8621 (adj 0.8528) · $10.25 · thesis WPG:SUPPRESSED
- Connor Bedard: 1+ goals NO @ 65c · p 0.6938 (adj 0.6816) · $6.1 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 28c · p 0.3205 (adj 0.3066) · $2.16 · thesis CHI:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 13c · p 0.1729 (adj 0.1597) · $3.11 · thesis SJS:OFFENSE_4PLUS
- Macklin Celebrini: 1+ assists NO @ 43c · p 0.5709 (adj 0.4577) · $3.1 · thesis SJS:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 19c · p 0.2297 (adj 0.216) · $2.34 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 24c · p 0.3086 (adj 0.2668) · $2.27 · thesis MIN:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 23c · p 0.2689 (adj 0.2529) · $1.72 · thesis STL:OFFENSE_4PLUS
- Vasily Podkolzin: 2+ assists YES @ 7c · p 0.1257 (adj 0.0979) · $2.33 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1291 (adj 0.1106) · $1.61 · thesis EDM:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.7985 (adj 0.7182) · $7.08 · thesis UTA:SUPPRESSED
- Vegas wins by over 1.5 goals NO @ 47c · p 0.5586 (adj 0.5118) · $4.37 · thesis GAME:TIGHT
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6902 (adj 0.6476) · $2.95 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.87, exp saves 26.74 (sd 7.08), pull risk 0.063
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.46 (sd 6.27), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ assists | 0.344 | 0.260 | 28/76 | +0.049 | STANDARD |
| Tage Thompson: 1+ assists | 0.347 | 0.425 | 44/59 | +0.046 | STANDARD |
| Owen Power: 1+ assists | 0.440 | 0.365 | 38/65 | +0.044 | STANDARD |
| Gavin McKenna: 1+ goals | 0.184 | 0.110 | 20/98 | -0.027 | PRIOR_HEAVY |
| Easton Cowan: 1+ points | 0.468 | 0.400 | 42/62 | +0.031 | STANDARD |
| Tage Thompson: 1+ points | 0.578 | 0.645 | 66/37 | +0.036 | STANDARD |

**NYI @ OTT** · priced 159/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.99, exp saves 22.64 (sd 6.16), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.57, exp saves 23.58 (sd 6.56), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ assists | 0.350 | 0.245 | 27/78 | +0.066 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.319 | 0.415 | 43/60 | +0.064 | STANDARD |
| Andre Burakovsky: 1+ points | 0.302 | 0.390 | 41/63 | +0.052 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.173 | 0.260 | 29/77 | +0.045 | STANDARD |
| Jordan Spence: 1+ points | 0.410 | 0.330 | 35/69 | +0.044 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.263 | 0.340 | 35/67 | +0.052 | STANDARD |

**SEA @ TBL** · priced 155/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.41, exp saves 21.37 (sd 5.94), pull risk 0.047
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.47 (sd 6.92), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.399 | 0.575 | 59/44 | +0.144 | STANDARD |
| John Carlson: 1+ assists | 0.316 | 0.485 | 50/53 | +0.136 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.502 | 0.650 | 66/36 | +0.122 | STANDARD |
| John Carlson: 2+ points | 0.091 | 0.230 | 25/79 | +0.107 | STANDARD |
| Nikita Kucherov: 2+ points | 0.314 | 0.430 | 44/58 | +0.089 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.150 | 0.260 | 29/77 | +0.067 | STANDARD |

**VAN @ FLA** · priced 143/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 24.7, exp saves 21.65 (sd 6.11), pull risk 0.055
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.21, exp saves 24.99 (sd 6.84), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Marco Rossi: 1+ points | 0.483 | 0.355 | 37/66 | +0.097 | STANDARD |
| Brady Tkachuk: 2+ points | 0.165 | 0.280 | 30/74 | +0.081 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.306 | 0.415 | 43/60 | +0.077 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.267 | 0.375 | 39/64 | +0.077 | STANDARD |
| Brady Tkachuk: 1+ points | 0.519 | 0.625 | 64/39 | +0.075 | STANDARD |
| Marco Rossi: 1+ assists | 0.323 | 0.230 | 24/78 | +0.071 | STANDARD |

**NYR @ NJD** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.13, exp saves 20.98 (sd 5.99), pull risk 0.054
- NYR net: Dylan Garand (PROJECTED) exp shots 29.99, exp saves 25.82 (sd 6.94), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.222 | 0.345 | 36/67 | +0.093 | STANDARD |
| Jack Hughes: 1+ assists | 0.386 | 0.500 | 52/52 | +0.076 | STANDARD |
| Gabe Perreault: 1+ assists | 0.324 | 0.230 | 25/79 | +0.061 | STANDARD |
| Nico Hischier: 1+ points | 0.494 | 0.585 | 60/43 | +0.059 | STANDARD |
| Jack Hughes: 3+ points | 0.059 | 0.145 | 16/87 | +0.063 | STANDARD |
| Gabe Perreault: 1+ points | 0.459 | 0.375 | 40/65 | +0.042 | STANDARD |

**PHI @ DET** · priced 149/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Larkin: 1+ points | 0.522 | 0.615 | 64/41 | +0.051 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.300 | 0.210 | 25/83 | +0.037 | STANDARD |
| Tyson Foerster: 1+ assists | 0.271 | 0.185 | 23/86 | +0.028 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.271 | 0.350 | 36/66 | +0.053 | STANDARD |
| Viktor Arvidsson: 1+ points | 0.479 | 0.550 | 57/47 | +0.033 | STANDARD |
| Dylan Larkin: 1+ assists | 0.337 | 0.405 | 42/61 | +0.037 | STANDARD |

**WPG @ CHI** · priced 156/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.63, exp saves 23.86 (sd 6.62), pull risk 0.067
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.12, exp saves 21.77 (sd 6.08), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor Bedard: 1+ assists | 0.340 | 0.480 | 50/54 | +0.103 | STANDARD |
| Connor Bedard: 2+ points | 0.182 | 0.315 | 34/71 | +0.093 | STANDARD |
| Connor Bedard: 1+ points | 0.544 | 0.660 | 68/36 | +0.080 | STANDARD |
| Patrick Kane: 1+ assists | 0.317 | 0.415 | 43/60 | +0.066 | STANDARD |
| Viggo Bjorck: 1+ points | 0.277 | 0.360 | 38/66 | +0.048 | PRIOR_HEAVY |
| Patrick Kane: 1+ points | 0.490 | 0.565 | 59/46 | +0.033 | STANDARD |

**SJS @ NSH** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.54, exp saves 23.88 (sd 6.63), pull risk 0.066
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.73), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.429 | 0.580 | 59/43 | +0.124 | STANDARD |
| Ivar Stenberg: 1+ points | 0.336 | 0.460 | 48/56 | +0.087 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.202 | 0.320 | 34/70 | +0.084 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.287 | 0.385 | 40/63 | +0.066 | STANDARD |
| Ivar Stenberg: 2+ points | 0.061 | 0.145 | 17/88 | +0.051 | PRIOR_HEAVY |
| Tyler Toffoli: 1+ assists | 0.321 | 0.240 | 27/79 | +0.037 | STANDARD |

**STL @ MIN** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 26.75, exp saves 23.2 (sd 6.33), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.77), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.471 | 0.365 | 38/65 | +0.075 | STANDARD |
| Adam Jiricek: 1+ points | 0.288 | 0.385 | 40/63 | +0.065 | PRIOR_HEAVY |
| Ryan Hartman: 1+ assists | 0.309 | 0.225 | 24/79 | +0.056 | STANDARD |
| Max Shabanov: 1+ goals | 0.193 | 0.120 | 22/98 | -0.039 | STANDARD |
| Robert Thomas: 1+ goals | 0.269 | 0.205 | 23/82 | +0.027 | STANDARD |
| Jimmy Snuggerud: 1+ assists | 0.363 | 0.300 | 31/71 | +0.038 | STANDARD |

**UTA @ EDM** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.2, exp saves 23.7 (sd 6.46), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mattias Ekholm: 1+ assists | 0.394 | 0.215 | 31/88 | +0.069 | STANDARD |
| John Marino: 1+ assists | 0.330 | 0.170 | 32/98 | -0.005 | STANDARD |
| Evan Bouchard: 1+ points | 0.684 | 0.555 | 72/61 | -0.050 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.202 | 0.325 | 34/69 | +0.094 | STANDARD |
| Alex Formenton: 1+ goals | 0.217 | 0.095 | 17/98 | +0.037 | STANDARD |
| Connor McDavid: 1+ assists | 0.548 | 0.665 | 69/36 | +0.076 | STANDARD |

**CGY @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.19 (sd 6.2), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.46 (sd 7.16), pull risk 0.089

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
