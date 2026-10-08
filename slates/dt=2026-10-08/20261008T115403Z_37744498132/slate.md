# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T11:54:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3447 · contracts joined: 1425 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 1175, 'OK': 157, 'NO_EDGE': 93}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 142, 'game_early_goal': 10, 'first_goal': 245, 'game_winner': 20, 'player_goals': 345, 'game_overtime': 10, 'player_points': 183, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-6h | 0.508 | 0.492 | 0.181 | 6.12 | 3.08 | 3.04 | 93 (25/68) | PROJECTED/PROJECTED |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-6h | 0.556 | 0.444 | 0.176 | 6.13 | 3.24 | 2.89 | 174 (25/149) | PROJECTED/PROJECTED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-6h | 0.578 | 0.422 | 0.166 | 6.58 | 3.54 | 3.03 | 169 (25/144) | PROJECTED/PROJECTED |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-6h | 0.590 | 0.410 | 0.173 | 6.32 | 3.45 | 2.87 | 214 (25/189) | PROJECTED/PROJECTED |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-6h | 0.559 | 0.441 | 0.180 | 5.92 | 3.14 | 2.78 | 206 (25/181) | PROJECTED/PROJECTED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-6h | 0.672 | 0.328 | 0.154 | 6.61 | 3.88 | 2.73 | 216 (25/191) | PROJECTED/PROJECTED |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-6h | 0.604 | 0.397 | 0.175 | 5.83 | 3.24 | 2.60 | 200 (25/175) | PROBABLE/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-12h | 0.619 | 0.381 | 0.169 | 6.42 | 3.59 | 2.83 | 51 (25/26) | PROJECTED/PROJECTED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-12h | 0.409 | 0.591 | 0.173 | 6.26 | 2.84 | 3.42 | 51 (25/26) | PROJECTED/PROJECTED |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-12h | 0.681 | 0.319 | 0.152 | 6.74 | 3.97 | 2.77 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.234 | 0.335 | 0.313 | 34 | 67 | no | +0.081 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.577 | 0.475 | 0.496 | 48 | 53 | yes | +0.080 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.364 | 0.465 | 0.444 | 47 | 54 | no | +0.079 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.591 | 0.685 | 0.667 | 69 | 32 | no | +0.074 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.409 | 0.315 | 0.333 | 32 | 69 | yes | +0.074 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.313 | 0.405 | 0.386 | 41 | 60 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.372 | 0.280 | 0.297 | 29 | 73 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.771 | 0.680 | 0.700 | 69 | 33 | yes | +0.066 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.328 | 0.245 | 0.260 | 25 | 76 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.515 | 0.430 | 0.447 | 44 | 58 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.300 | 0.225 | 0.239 | 23 | 78 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.464 | 0.385 | 0.400 | 39 | 62 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.457 | 0.535 | 0.519 | 54 | 47 | no | +0.055 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.672 | 0.745 | 0.731 | 75 | 26 | no | +0.055 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.681 | 0.605 | 0.621 | 61 | 40 | yes | +0.054 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.556 | 0.480 | 0.495 | 49 | 53 | yes | +0.049 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.444 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.455 | 0.530 | 0.515 | 54 | 48 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.132 | 0.195 | 0.181 | 20 | 81 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.299 | 0.230 | 0.243 | 24 | 78 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.319 | 0.385 | 0.371 | 39 | 62 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.149 | 0.090 | 0.100 | 10 | 92 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.202 | 0.140 | 0.151 | 15 | 87 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.293 | 0.230 | 0.242 | 24 | 78 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.324 | 0.265 | 0.276 | 27 | 74 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.646 | 0.585 | 0.598 | 59 | 42 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT08SJSTL-6 | game_total | 0.597 | 0.535 | 0.548 | 54 | 47 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL4 | team_total | 0.496 | 0.435 | 0.447 | 44 | 57 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT08SJSTL-9 | game_total | 0.208 | 0.155 | 0.165 | 16 | 85 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT08SJSTL-7 | game_total | 0.484 | 0.425 | 0.437 | 43 | 58 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.331 | 0.275 | 0.286 | 28 | 73 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.557 | 0.625 | 0.612 | 64 | 39 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.122 | 0.075 | 0.083 | 8 | 93 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.750 | 0.690 | 0.703 | 70 | 32 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.260 | 0.325 | 0.311 | 34 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL3 | team_total | 0.700 | 0.640 | 0.653 | 65 | 37 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 | team_total | 0.541 | 0.475 | 0.488 | 49 | 54 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.161 | 0.115 | 0.123 | 12 | 89 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.673 | 0.730 | 0.719 | 74 | 28 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.244 | 0.195 | 0.204 | 20 | 81 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY4 | team_total | 0.327 | 0.270 | 0.281 | 28 | 74 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL6 | team_total | 0.150 | 0.095 | 0.104 | 11 | 92 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-6 | game_total | 0.580 | 0.525 | 0.536 | 53 | 48 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-8 | game_total | 0.275 | 0.225 | 0.234 | 23 | 78 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.316 | 0.265 | 0.275 | 27 | 74 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-7 | game_total | 0.469 | 0.415 | 0.426 | 42 | 59 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.081 | 0.125 | 0.115 | 13 | 88 | no | +0.031 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLGAME-26OCT08UTABOS-BOS | game_winner | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF3 | team_total | 0.637 | 0.585 | 0.596 | 59 | 42 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH5 | team_total | 0.198 | 0.150 | 0.159 | 16 | 86 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-9 | game_total | 0.230 | 0.185 | 0.193 | 19 | 82 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT5 | team_total | 0.270 | 0.225 | 0.234 | 23 | 78 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.905 | 0.855 | 0.866 | 87 | 16 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH3 | team_total | 0.584 | 0.535 | 0.545 | 54 | 47 | yes | +0.027 | OK |
| KXNHLGAME-26OCT08NSHMTL-NSH | game_winner | 0.422 | 0.375 | 0.384 | 38 | 63 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.338 | 0.395 | 0.383 | 41 | 62 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.532 | 0.485 | 0.495 | 49 | 52 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-9 | game_total | 0.194 | 0.155 | 0.162 | 16 | 85 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH4 | team_total | 0.370 | 0.315 | 0.326 | 33 | 70 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT3 | team_total | 0.680 | 0.630 | 0.640 | 64 | 38 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN3 | game_spread | 0.087 | 0.055 | 0.060 | 6 | 95 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL2 | team_total | 0.872 | 0.835 | 0.843 | 84 | 17 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT08NSHMTL-MTL3 | game_spread | 0.234 | 0.275 | 0.266 | 28 | 73 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.129 | 0.085 | 0.092 | 10 | 93 | yes | +0.022 | OK |
| KXNHLGAME-26OCT08SJSTL-STL | game_winner | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-6 | game_total | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.726 | 0.765 | 0.757 | 77 | 24 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI2 | game_spread | 0.372 | 0.415 | 0.406 | 42 | 59 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.778 | 0.820 | 0.812 | 83 | 19 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT08SJSTL-STL2 | game_spread | 0.396 | 0.355 | 0.363 | 36 | 65 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT08CHINYI-4 | game_total | 0.821 | 0.855 | 0.849 | 86 | 15 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT08MINTB-TB3 | game_spread | 0.198 | 0.235 | 0.227 | 24 | 77 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-10 | game_total | 0.093 | 0.065 | 0.070 | 7 | 94 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-CAR3 | team_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT08UTABOS-UTA2 | game_spread | 0.277 | 0.315 | 0.307 | 32 | 69 | no | +0.018 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 0.508 | 0.499 | 0.181 | 0.215 | 6.12 | 6.47 | 0.968/0.992 | KXNHLTOTAL-26OCT08UTABOS-7 +0.060 |
| DAL @ BUF | 0.556 | 0.531 | 0.176 | 0.220 | 6.13 | 6.17 | 0.998/0.986 | KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 +0.028 |
| NSH @ MTL | 0.578 | 0.576 | 0.166 | 0.214 | 6.58 | 6.52 | 0.952/1.000 | KXNHLTOTAL-26OCT08NSHMTL-8 -0.016 |
| PHI @ OTT | 0.590 | 0.562 | 0.173 | 0.219 | 6.32 | 6.04 | 1.050/0.991 | KXNHLTOTAL-26OCT08PHIOTT-6 -0.053 |
| MIN @ TBL | 0.559 | 0.539 | 0.180 | 0.219 | 5.92 | 6.30 | 0.957/1.003 | KXNHLTOTAL-26OCT08MINTB-7 +0.067 |
| VAN @ CAR | 0.672 | 0.613 | 0.154 | 0.207 | 6.61 | 6.57 | 0.997/1.020 | KXNHLSPREAD-26OCT08VANCAR-CAR2 -0.063 |
| CHI @ NYI | 0.604 | 0.611 | 0.175 | 0.213 | 5.83 | 6.24 | 0.951/1.003 | KXNHLTOTAL-26OCT08CHINYI-7 +0.075 |
| SJS @ STL | 0.619 | 0.565 | 0.169 | 0.215 | 6.42 | 6.43 | 0.993/1.034 | KXNHLGAME-26OCT08SJSTL-SJ +0.054 |
| COL @ CGY | 0.409 | 0.429 | 0.173 | 0.222 | 6.26 | 6.31 | 0.997/0.976 | KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 +0.024 |
| TOR @ VGK | 0.681 | 0.650 | 0.152 | 0.202 | 6.74 | 6.31 | 1.003/0.965 | KXNHLTOTAL-26OCT08TORVGK-6 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4969 (adj 0.4609) · $4.96 · thesis GAME:HIGH_EVENT
- Boston over 3.5 goals scored YES @ 36c · p 0.4189 (adj 0.387) · $2.28 · thesis BOS:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 16c · p 0.2086 (adj 0.184) · $3.79 · thesis BUF:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 12c · p 0.1604 (adj 0.1378) · $2.48 · thesis BUF:OFFENSE_4PLUS
- Owen Power: 1+ assists YES @ 31c · p 0.3758 (adj 0.3354) · $2.69 · thesis BUF:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.2902 (adj 0.2764) · $4.36 · thesis NSH:OFFENSE_4PLUS
- William Eklund: 1+ assists NO @ 65c · p 0.7865 (adj 0.6815) · $15.11 · thesis OTT:SUPPRESSED
- Jordan Spence: 1+ assists YES @ 27c · p 0.3431 (adj 0.2941) · $3.53 · thesis OTT:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 59c · p 0.7248 (adj 0.6274) · $14.52 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 41c · p 0.4895 (adj 0.4423) · $5.92 · thesis TBL:SUPPRESSED
- Ilya Mikheyev: 1+ goals YES @ 16c · p 0.2042 (adj 0.1806) · $3.41 · thesis TBL:OFFENSE_4PLUS
- Vancouver wins by over 1.5 goals YES @ 12c · p 0.2009 (adj 0.1579) · $5.42 · thesis VAN:WINS_BY_2PLUS
- Vancouver over 3.5 goals scored YES @ 23c · p 0.3488 (adj 0.2683) · $1.68 · thesis VAN:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 60c · p 0.7306 (adj 0.6425) · $9.98 · thesis GAME:TIGHT
- Sebastian Aho: 2+ assists NO @ 86c · p 0.9274 (adj 0.8812) · $20.0 · thesis CAR:SUPPRESSED
- Calum Ritchie: 1+ assists YES @ 27c · p 0.3558 (adj 0.3079) · $8.06 · thesis NYI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.1637 (adj 0.1453) · $4.61 · thesis CHI:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 64c · p 0.6788 (adj 0.6666) · $8.5 · thesis NYI:SUPPRESSED
- Full Game: Over 8.5 goals scored YES @ 16c · p 0.2064 (adj 0.1807) · $2.24 · thesis GAME:HIGH_EVENT
- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4948 (adj 0.4599) · $3.32 · thesis GAME:HIGH_EVENT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 36/42 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.45, exp saves 24.51 (sd 6.77), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.34, exp saves 22.54 (sd 6.31), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 2+ goals | 0.061 | 0.050 | 8/98 | -0.024 | STANDARD |

**DAL @ BUF** · priced 115/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 25.45, exp saves 22.08 (sd 6.14), pull risk 0.056
- DAL net: Jake Oettinger (PROJECTED) exp shots 27.04, exp saves 23.28 (sd 6.48), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jiri Kulich: 1+ goals | 0.209 | 0.110 | 16/94 | +0.039 | STANDARD |
| Peyton Krebs: 1+ goals | 0.160 | 0.070 | 12/98 | +0.033 | STANDARD |
| Owen Power: 1+ assists | 0.376 | 0.295 | 31/72 | +0.051 | STANDARD |
| Zach Benson: 1+ assists | 0.366 | 0.295 | 31/72 | +0.041 | STANDARD |
| Justin Danforth: 1+ goals | 0.121 | 0.050 | 9/99 | +0.025 | STANDARD |
| Tage Thompson: 1+ assists | 0.352 | 0.420 | 44/60 | +0.032 | STANDARD |

**NSH @ MTL** · priced 114/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.02, exp saves 24.37 (sd 6.62), pull risk 0.054
- NSH net: Juuse Saros (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.63), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.209 | 0.310 | 34/72 | +0.057 | STANDARD |
| Chris Kreider: 1+ points | 0.408 | 0.505 | 53/52 | +0.055 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.346 | 0.255 | 29/78 | +0.042 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.465 | 0.375 | 40/65 | +0.049 | STANDARD |
| Mavrik Bourque: 1+ goals | 0.209 | 0.130 | 18/92 | +0.019 | STANDARD |
| Josh Anderson: 1+ goals | 0.174 | 0.100 | 15/95 | +0.015 | STANDARD |

**PHI @ OTT** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 23.58, exp saves 20.56 (sd 5.83), pull risk 0.049
- PHI net: Joseph Woll (PROJECTED) exp shots 28.92, exp saves 24.88 (sd 6.84), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.213 | 0.375 | 40/65 | +0.121 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.295 | 0.445 | 47/58 | +0.108 | PRIOR_HEAVY |
| William Eklund: 1+ points | 0.385 | 0.520 | 55/51 | +0.087 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.241 | 0.375 | 40/65 | +0.093 | PRIOR_HEAVY |
| Jordan Spence: 1+ assists | 0.343 | 0.245 | 27/78 | +0.059 | STANDARD |
| Jordan Spence: 1+ points | 0.402 | 0.315 | 33/70 | +0.056 | STANDARD |

**MIN @ TBL** · priced 153/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.09, exp saves 22.63 (sd 6.24), pull risk 0.058
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.6, exp saves 25.5 (sd 6.88), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.275 | 0.425 | 44/59 | +0.118 | STANDARD |
| John Carlson: 1+ points | 0.364 | 0.490 | 51/53 | +0.089 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.510 | 0.605 | 62/41 | +0.063 | STANDARD |
| Ilya Mikheyev: 1+ goals | 0.204 | 0.110 | 16/94 | +0.035 | STANDARD |
| Brayden Point: 2+ points | 0.221 | 0.130 | 24/98 | -0.032 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.400 | 42/62 | +0.043 | STANDARD |

**VAN @ CAR** · priced 165/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.48, exp saves 19.78 (sd 5.62), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 32.08, exp saves 27.13 (sd 7.47), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 3+ points | 0.030 | 0.490 | 97/99 | -0.020 | STANDARD |
| Sebastian Aho: 1+ assists | 0.353 | 0.510 | 53/51 | +0.119 | STANDARD |
| Elias Pettersson (#40): 1+ assists | 0.352 | 0.200 | 39/99 | -0.054 | STANDARD |
| Sebastian Aho: 1+ points | 0.544 | 0.670 | 69/35 | +0.090 | STANDARD |
| Sebastian Aho: 2+ points | 0.190 | 0.315 | 34/71 | +0.085 | STANDARD |
| Marco Rossi: 1+ goals | 0.249 | 0.130 | 21/95 | +0.027 | STANDARD |

**CHI @ NYI** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 24.34, exp saves 21.41 (sd 5.94), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.5 (sd 7.18), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.280 | 0.425 | 45/60 | +0.103 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.231 | 0.335 | 36/69 | +0.064 | STANDARD |
| Patrick Kane: 1+ points | 0.451 | 0.550 | 57/47 | +0.061 | STANDARD |
| Calum Ritchie: 1+ points | 0.501 | 0.405 | 44/63 | +0.044 | STANDARD |
| Brayden Schenn: 1+ goals | 0.261 | 0.165 | 26/93 | -0.012 | STANDARD |
| Calum Ritchie: 1+ assists | 0.356 | 0.260 | 27/75 | +0.072 | STANDARD |

**SJS @ STL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 25.77, exp saves 22.28 (sd 6.19), pull risk 0.06
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.07, exp saves 23.04 (sd 6.56), pull risk 0.082

**COL @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 32.7, exp saves 27.83 (sd 7.58), pull risk 0.073
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.32, exp saves 22.94 (sd 6.3), pull risk 0.056

**TOR @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 24.89, exp saves 21.95 (sd 6.05), pull risk 0.043
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.39, exp saves 26.48 (sd 7.37), pull risk 0.088

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
