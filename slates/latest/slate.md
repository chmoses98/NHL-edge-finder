# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T14:26:28Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4313 · contracts joined: 2392 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 2117, 'OK': 180, 'NO_EDGE': 95}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 314, 'game_early_goal': 11, 'first_goal': 397, 'game_winner': 22, 'player_goals': 692, 'game_overtime': 11, 'player_points': 428, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-6h | 0.456 | 0.544 | 0.168 | 6.68 | 3.19 | 3.49 | 223 (25/198) | PROJECTED/PROJECTED |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-6h | 0.535 | 0.465 | 0.178 | 6.02 | 3.12 | 2.90 | 226 (25/201) | PROJECTED/PROJECTED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-6h | 0.613 | 0.388 | 0.172 | 6.06 | 3.38 | 2.68 | 210 (25/185) | PROJECTED/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-6h | 0.608 | 0.392 | 0.164 | 6.67 | 3.70 | 2.98 | 203 (25/178) | PROJECTED/PROJECTED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-6h | 0.496 | 0.504 | 0.179 | 5.93 | 2.95 | 2.98 | 215 (25/190) | PROJECTED/PROJECTED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-6h | 0.603 | 0.397 | 0.179 | 5.79 | 3.20 | 2.58 | 215 (25/190) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-6h | 0.494 | 0.505 | 0.180 | 5.87 | 2.91 | 2.96 | 211 (25/186) | PROJECTED/PROJECTED |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-6h | 0.536 | 0.464 | 0.172 | 6.38 | 3.30 | 3.08 | 233 (25/208) | PROJECTED/PROJECTED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-6h | 0.529 | 0.471 | 0.179 | 6.05 | 3.12 | 2.93 | 218 (25/193) | PROJECTED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-6h | 0.558 | 0.442 | 0.161 | 6.66 | 3.53 | 3.13 | 229 (25/204) | PROJECTED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-6h | 0.666 | 0.334 | 0.162 | 6.25 | 3.66 | 2.58 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.573 | 0.435 | 0.463 | 44 | 57 | yes | +0.116 | OK |
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.608 | 0.735 | 0.712 | 74 | 27 | no | +0.108 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.356 | 0.230 | 0.252 | 24 | 78 | yes | +0.103 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.392 | 0.275 | 0.297 | 28 | 73 | yes | +0.098 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.263 | 0.375 | 0.351 | 38 | 63 | no | +0.091 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.394 | 0.510 | 0.486 | 52 | 50 | no | +0.088 | OK |
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
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.666 | 0.745 | 0.730 | 75 | 26 | no | +0.061 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.334 | 0.255 | 0.270 | 26 | 75 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.254 | 0.335 | 0.318 | 34 | 67 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.354 | 0.435 | 0.418 | 44 | 57 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.351 | 0.430 | 0.414 | 44 | 58 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.666 | 0.740 | 0.726 | 75 | 27 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.575 | 0.650 | 0.635 | 66 | 36 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.730 | 0.795 | 0.783 | 80 | 21 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.342 | 0.275 | 0.288 | 28 | 73 | yes | +0.048 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.496 | 0.565 | 0.551 | 57 | 44 | no | +0.047 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.504 | 0.435 | 0.449 | 44 | 57 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.330 | 0.265 | 0.277 | 27 | 74 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.244 | 0.185 | 0.196 | 19 | 82 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.311 | 0.375 | 0.362 | 38 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.560 | 0.490 | 0.504 | 50 | 52 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.789 | 0.845 | 0.835 | 85 | 16 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.085 | 0.030 | 0.037 | 4 | 98 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.575 | 0.562 | 58 | 43 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.394 | 0.455 | 0.443 | 46 | 55 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.179 | 0.245 | 0.231 | 26 | 77 | no | +0.039 | OK |
| KXNHLGAME-26OCT15NYIOTT-NYI | game_winner | 0.465 | 0.405 | 0.417 | 41 | 60 | yes | +0.038 | OK |
| KXNHLGAME-26OCT15NYIOTT-OTT | game_winner | 0.535 | 0.595 | 0.583 | 60 | 41 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.576 | 0.640 | 0.628 | 65 | 37 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.505 | 0.565 | 0.553 | 57 | 44 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT15NYIOTT-6 | game_total | 0.534 | 0.475 | 0.487 | 48 | 53 | yes | +0.037 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.544 | 0.485 | 0.497 | 49 | 52 | yes | +0.036 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.456 | 0.515 | 0.503 | 52 | 49 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.152 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.279 | 0.340 | 0.327 | 35 | 67 | no | +0.036 | OK |
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
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.284 | 0.235 | 0.244 | 24 | 77 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.717 | 0.775 | 0.764 | 79 | 24 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.822 | 0.870 | 0.861 | 88 | 14 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15PHIDET-4 | game_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-7 | game_total | 0.403 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.179 | 0.230 | 0.219 | 24 | 78 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.484 | 0.540 | 0.529 | 55 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.122 | 0.170 | 0.159 | 18 | 84 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.476 | 0.420 | 0.431 | 43 | 59 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-5 | game_total | 0.740 | 0.790 | 0.781 | 80 | 22 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF4 | team_total | 0.475 | 0.425 | 0.435 | 43 | 58 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.792 | 0.840 | 0.831 | 85 | 17 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN2 | game_spread | 0.307 | 0.355 | 0.345 | 36 | 65 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-TOR3 | team_total | 0.617 | 0.670 | 0.660 | 68 | 34 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.027 | OK |
| KXNHLGAME-26OCT15WPGCHI-CHI | game_winner | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-FLA5 | team_total | 0.317 | 0.370 | 0.359 | 38 | 64 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY2 | team_total | 0.722 | 0.675 | 0.685 | 68 | 33 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK2 | team_total | 0.878 | 0.915 | 0.908 | 92 | 9 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-6 | game_total | 0.516 | 0.565 | 0.555 | 57 | 44 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.269 | 0.220 | 0.229 | 23 | 79 | yes | +0.026 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Owen Power: 1+ goals NO @ 87c · p 0.9134 (adj 0.8988) · $8.12 · thesis BUF:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 9c · p 0.1306 (adj 0.1192) · $2.35 · thesis NYI:OFFENSE_4PLUS
- Jordan Spence: 1+ assists YES @ 28c · p 0.3497 (adj 0.3049) · $1.31 · thesis OTT:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 9c · p 0.1263 (adj 0.116) · $1.89 · thesis SEA:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 67c · p 0.7628 (adj 0.7139) · $7.26 · thesis GAME:TIGHT
- Ben Meyers: 1+ goals YES @ 8c · p 0.1197 (adj 0.1023) · $1.52 · thesis SEA:OFFENSE_4PLUS
- Nikita Kucherov: 1+ goals NO @ 59c · p 0.6452 (adj 0.6301) · $4.65 · thesis TBL:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 12c · p 0.1873 (adj 0.1692) · $4.34 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 15c · p 0.2187 (adj 0.199) · $4.32 · thesis VAN:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 62c · p 0.7029 (adj 0.6797) · $8.12 · thesis FLA:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 18c · p 0.2368 (adj 0.2188) · $3.3 · thesis VAN:OFFENSE_4PLUS
- Matt Rempe: 1+ goals YES @ 6c · p 0.0899 (adj 0.0812) · $1.62 · thesis NYR:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.6728 (adj 0.6558) · $7.58 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 13c · p 0.1637 (adj 0.1528) · $1.7 · thesis NJD:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 77c · p 0.8246 (adj 0.7948) · $4.75 · thesis NYR:WINS
- Christian Dvorak: 1+ goals YES @ 19c · p 0.2329 (adj 0.2209) · $2.46 · thesis PHI:OFFENSE_4PLUS
- Nate Danielson: 1+ goals NO @ 85c · p 0.8839 (adj 0.8704) · $8.12 · thesis DET:SUPPRESSED
- Denver Barkey: 1+ goals YES @ 14c · p 0.1734 (adj 0.16) · $1.3 · thesis PHI:OFFENSE_4PLUS
- Viktor Arvidsson: 1+ assists NO @ 66c · p 0.729 (adj 0.6895) · $4.07 · thesis DET:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 12c · p 0.1764 (adj 0.1573) · $3.28 · thesis CHI:OFFENSE_4PLUS
- Connor Bedard: 1+ assists NO @ 52c · p 0.6605 (adj 0.5627) · $7.56 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 28c · p 0.3205 (adj 0.3079) · $2.51 · thesis CHI:OFFENSE_4PLUS
- Anton Frondell: 1+ goals YES @ 22c · p 0.2528 (adj 0.2421) · $1.42 · thesis CHI:OFFENSE_4PLUS
- Ivar Stenberg: 2+ assists NO @ 93c · p 0.9795 (adj 0.9523) · $7.46 · thesis DIFFUSE
- Collin Graf: 1+ goals YES @ 13c · p 0.1729 (adj 0.1597) · $2.16 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 80c · p 0.8336 (adj 0.8227) · $5.85 · thesis SJS:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 69c · p 0.7982 (adj 0.7181) · $4.83 · thesis SJS:SUPPRESSED
- Ryan Hartman: 1+ assists YES @ 24c · p 0.3086 (adj 0.2693) · $2.09 · thesis MIN:OFFENSE_4PLUS
- Robert Thomas: 1+ goals YES @ 23c · p 0.2689 (adj 0.2554) · $1.73 · thesis STL:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4519 (adj 0.3629) · $4.49 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 9c · p 0.1291 (adj 0.1131) · $1.88 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 17c · p 0.2168 (adj 0.2014) · $2.65 · thesis EDM:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.7985 (adj 0.7182) · $5.67 · thesis UTA:SUPPRESSED
- Trevor Connelly: 1+ goals NO @ 73c · p 0.7814 (adj 0.7661) · $7.23 · thesis VGK:SUPPRESSED
- Vegas wins by over 1.5 goals NO @ 47c · p 0.5586 (adj 0.5118) · $2.72 · thesis GAME:TIGHT
- Jack Eichel: 1+ goals NO @ 62c · p 0.6755 (adj 0.6591) · $4.95 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6902 (adj 0.6476) · $1.75 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.87, exp saves 26.74 (sd 7.08), pull risk 0.063
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.46 (sd 6.27), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tage Thompson: 1+ assists | 0.347 | 0.425 | 44/59 | +0.046 | STANDARD |
| Owen Power: 1+ assists | 0.440 | 0.365 | 38/65 | +0.044 | STANDARD |
| Easton Cowan: 1+ assists | 0.344 | 0.275 | 29/74 | +0.039 | STANDARD |
| Tage Thompson: 1+ points | 0.578 | 0.645 | 66/37 | +0.036 | STANDARD |
| Auston Matthews: 2+ points | 0.259 | 0.325 | 34/69 | +0.036 | STANDARD |
| Darren Raddysh: 1+ assists | 0.352 | 0.415 | 43/60 | +0.031 | STANDARD |

**NYI @ OTT** · priced 168/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.99, exp saves 22.64 (sd 6.16), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.57, exp saves 23.58 (sd 6.56), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ridly Greig: 1+ points | 0.404 | 0.185 | 35/98 | +0.038 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.385 | 0.175 | 33/98 | +0.039 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.253 | 0.105 | 20/99 | +0.042 | STANDARD |
| Ridly Greig: 1+ assists | 0.260 | 0.115 | 22/99 | +0.028 | STANDARD |
| Stephen Halliday: 1+ points | 0.327 | 0.190 | 36/98 | -0.049 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.319 | 0.415 | 43/60 | +0.064 | STANDARD |

**SEA @ TBL** · priced 155/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.41, exp saves 21.37 (sd 5.94), pull risk 0.047
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.47 (sd 6.92), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.399 | 0.575 | 59/44 | +0.144 | STANDARD |
| John Carlson: 1+ assists | 0.316 | 0.485 | 50/53 | +0.136 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.502 | 0.645 | 66/37 | +0.111 | STANDARD |
| John Carlson: 2+ points | 0.091 | 0.230 | 25/79 | +0.107 | STANDARD |
| Nikita Kucherov: 2+ points | 0.314 | 0.430 | 44/58 | +0.089 | STANDARD |
| Nikita Kucherov: 3+ points | 0.103 | 0.215 | 24/81 | +0.076 | STANDARD |

**VAN @ FLA** · priced 148/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 24.7, exp saves 21.65 (sd 6.11), pull risk 0.055
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.21, exp saves 24.99 (sd 6.84), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Eetu Luostarinen: 1+ points | 0.410 | 0.210 | 40/98 | -0.007 | STANDARD |
| Eetu Luostarinen: 1+ assists | 0.269 | 0.130 | 25/99 | +0.006 | STANDARD |
| Marco Rossi: 1+ points | 0.483 | 0.355 | 37/66 | +0.097 | STANDARD |
| Brady Tkachuk: 1+ points | 0.519 | 0.630 | 65/39 | +0.075 | STANDARD |
| Matthew Tkachuk: 2+ points | 0.267 | 0.375 | 39/64 | +0.077 | STANDARD |
| Sam Reinhart: 2+ points | 0.176 | 0.280 | 31/75 | +0.061 | STANDARD |

**NYR @ NJD** · priced 163/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.13, exp saves 20.98 (sd 5.99), pull risk 0.054
- NYR net: Dylan Garand (PROJECTED) exp shots 29.99, exp saves 25.82 (sd 6.94), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.222 | 0.350 | 37/67 | +0.093 | STANDARD |
| Jack Hughes: 1+ assists | 0.386 | 0.500 | 52/52 | +0.076 | STANDARD |
| Nico Hischier: 1+ points | 0.494 | 0.585 | 60/43 | +0.059 | STANDARD |
| Jack Hughes: 3+ points | 0.059 | 0.145 | 16/87 | +0.063 | STANDARD |
| Nico Hischier: 2+ points | 0.151 | 0.235 | 26/79 | +0.048 | STANDARD |
| Jack Hughes: 1+ points | 0.589 | 0.670 | 70/36 | +0.035 | STANDARD |

**PHI @ DET** · priced 153/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.58 (sd 5.97), pull risk 0.052
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.76), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Larkin: 1+ points | 0.522 | 0.605 | 63/42 | +0.041 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.271 | 0.350 | 36/66 | +0.053 | STANDARD |
| Viktor Arvidsson: 1+ points | 0.479 | 0.550 | 57/47 | +0.033 | STANDARD |
| Dylan Larkin: 1+ assists | 0.337 | 0.405 | 42/61 | +0.037 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.300 | 0.235 | 25/78 | +0.037 | STANDARD |
| Viktor Arvidsson: 2+ points | 0.133 | 0.195 | 22/83 | +0.027 | STANDARD |

**WPG @ CHI** · priced 159/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.63, exp saves 23.86 (sd 6.62), pull risk 0.067
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.12, exp saves 21.77 (sd 6.08), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Teuvo Teravainen: 1+ points | 0.371 | 0.200 | 38/98 | -0.026 | STANDARD |
| Connor Bedard: 1+ assists | 0.340 | 0.490 | 50/52 | +0.123 | STANDARD |
| Connor Bedard: 1+ points | 0.544 | 0.660 | 68/36 | +0.080 | STANDARD |
| Connor Bedard: 2+ points | 0.182 | 0.295 | 33/74 | +0.064 | STANDARD |
| Teuvo Teravainen: 1+ assists | 0.267 | 0.160 | 31/99 | -0.058 | STANDARD |
| Patrick Kane: 1+ assists | 0.317 | 0.410 | 43/61 | +0.056 | STANDARD |

**SJS @ NSH** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.54, exp saves 23.88 (sd 6.63), pull risk 0.066
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.73), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kiefer Sherwood: 1+ points | 0.374 | 0.185 | 35/98 | +0.008 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.429 | 0.575 | 59/44 | +0.114 | STANDARD |
| Ivar Stenberg: 1+ points | 0.336 | 0.460 | 48/56 | +0.087 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.202 | 0.325 | 34/69 | +0.093 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ assists | 0.112 | 0.210 | 23/81 | +0.067 | STANDARD |
| Macklin Celebrini: 2+ points | 0.287 | 0.385 | 40/63 | +0.066 | STANDARD |

**STL @ MIN** · priced 166/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 26.75, exp saves 23.2 (sd 6.33), pull risk 0.06
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.34 (sd 6.77), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Danila Yurov: 1+ points | 0.390 | 0.195 | 37/98 | +0.004 | STANDARD |
| Danila Yurov: 1+ assists | 0.254 | 0.140 | 27/99 | -0.030 | STANDARD |
| Ryan Hartman: 1+ points | 0.471 | 0.365 | 38/65 | +0.075 | STANDARD |
| Adam Jiricek: 1+ points | 0.288 | 0.385 | 40/63 | +0.065 | PRIOR_HEAVY |
| Ryan Hartman: 1+ assists | 0.309 | 0.230 | 24/78 | +0.056 | STANDARD |
| Adam Jiricek: 1+ assists | 0.223 | 0.295 | 31/72 | +0.043 | PRIOR_HEAVY |

**UTA @ EDM** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.2, exp saves 23.7 (sd 6.46), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.78 (sd 6.77), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Barrett Hayton: 1+ points | 0.363 | 0.190 | 36/98 | -0.013 | STANDARD |
| Connor McDavid: 1+ assists | 0.548 | 0.685 | 69/32 | +0.117 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.202 | 0.325 | 34/69 | +0.094 | STANDARD |
| Mattias Ekholm: 1+ assists | 0.394 | 0.275 | 29/74 | +0.089 | STANDARD |
| Connor Murphy: 1+ points | 0.278 | 0.165 | 31/98 | -0.047 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.445 | 0.335 | 35/68 | +0.079 | STANDARD |

**CGY @ VGK** · priced 157/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.19 (sd 6.2), pull risk 0.042
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.46 (sd 7.16), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brett Howden: 1+ assists | 0.265 | 0.500 | 97/97 | -0.237 | STANDARD |
| Brett Howden: 1+ points | 0.440 | 0.235 | 43/96 | -0.008 | STANDARD |
| Trevor Connelly: 1+ points | 0.395 | 0.530 | 55/49 | +0.097 | PRIOR_HEAVY |
| Trevor Connelly: 1+ assists | 0.228 | 0.360 | 38/66 | +0.097 | PRIOR_HEAVY |
| Mitch Marner: 2+ points | 0.210 | 0.340 | 36/68 | +0.094 | STANDARD |
| Jack Eichel: 2+ points | 0.271 | 0.395 | 41/62 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
