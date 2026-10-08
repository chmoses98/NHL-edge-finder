# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T12:41:30Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3599 · contracts joined: 1577 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 1327, 'OK': 158, 'NO_EDGE': 92}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 166, 'game_early_goal': 10, 'first_goal': 281, 'game_winner': 20, 'player_goals': 405, 'game_overtime': 10, 'player_points': 215, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-6h | 0.508 | 0.492 | 0.181 | 6.12 | 3.08 | 3.04 | 93 (25/68) | PROJECTED/PROJECTED |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-6h | 0.556 | 0.444 | 0.176 | 6.13 | 3.24 | 2.89 | 174 (25/149) | PROJECTED/PROJECTED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-6h | 0.578 | 0.422 | 0.166 | 6.58 | 3.54 | 3.03 | 169 (25/144) | PROJECTED/PROJECTED |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-6h | 0.590 | 0.410 | 0.173 | 6.32 | 3.45 | 2.87 | 214 (25/189) | PROJECTED/PROJECTED |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-6h | 0.559 | 0.441 | 0.180 | 5.92 | 3.14 | 2.78 | 206 (25/181) | PROJECTED/PROJECTED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-6h | 0.672 | 0.328 | 0.154 | 6.61 | 3.88 | 2.73 | 216 (25/191) | PROJECTED/PROJECTED |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-6h | 0.604 | 0.397 | 0.175 | 5.83 | 3.24 | 2.60 | 200 (25/175) | PROBABLE/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-6h | 0.619 | 0.381 | 0.169 | 6.42 | 3.59 | 2.83 | 203 (25/178) | PROJECTED/PROJECTED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-12h | 0.409 | 0.591 | 0.173 | 6.26 | 2.84 | 3.42 | 51 (25/26) | PROJECTED/PROJECTED |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-12h | 0.681 | 0.319 | 0.152 | 6.74 | 3.97 | 2.77 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.234 | 0.335 | 0.313 | 34 | 67 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.364 | 0.465 | 0.444 | 47 | 54 | no | +0.079 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.591 | 0.685 | 0.667 | 69 | 32 | no | +0.074 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.409 | 0.315 | 0.333 | 32 | 69 | yes | +0.074 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.313 | 0.405 | 0.386 | 41 | 60 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.577 | 0.480 | 0.500 | 49 | 53 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.771 | 0.685 | 0.704 | 69 | 32 | yes | +0.066 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.672 | 0.755 | 0.740 | 76 | 25 | no | +0.065 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.328 | 0.245 | 0.260 | 25 | 76 | yes | +0.065 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.556 | 0.475 | 0.491 | 48 | 53 | yes | +0.059 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.444 | 0.525 | 0.509 | 53 | 48 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.455 | 0.540 | 0.523 | 55 | 47 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.372 | 0.285 | 0.301 | 30 | 73 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.300 | 0.220 | 0.235 | 23 | 79 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.464 | 0.385 | 0.400 | 39 | 62 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.457 | 0.535 | 0.519 | 54 | 47 | no | +0.055 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.681 | 0.605 | 0.621 | 61 | 40 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.202 | 0.135 | 0.147 | 14 | 87 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.515 | 0.430 | 0.447 | 45 | 59 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.132 | 0.195 | 0.181 | 20 | 81 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.260 | 0.330 | 0.315 | 34 | 68 | no | +0.045 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.319 | 0.385 | 0.371 | 39 | 62 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.673 | 0.735 | 0.723 | 74 | 27 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.337 | 0.275 | 0.287 | 28 | 73 | yes | +0.043 | OK |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.293 | 0.235 | 0.246 | 24 | 77 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.324 | 0.265 | 0.276 | 27 | 74 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.646 | 0.585 | 0.598 | 59 | 42 | yes | +0.040 | OK |
| KXNHLTOTAL-26OCT08SJSTL-6 | game_total | 0.597 | 0.535 | 0.548 | 54 | 47 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT08SJSTL-9 | game_total | 0.208 | 0.155 | 0.165 | 16 | 85 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.237 | 0.295 | 0.283 | 30 | 71 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT08SJSTL-7 | game_total | 0.484 | 0.425 | 0.437 | 43 | 58 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.331 | 0.275 | 0.286 | 28 | 73 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.557 | 0.625 | 0.612 | 64 | 39 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.122 | 0.075 | 0.083 | 8 | 93 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.299 | 0.240 | 0.251 | 25 | 77 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.750 | 0.685 | 0.699 | 70 | 33 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.338 | 0.405 | 0.391 | 42 | 61 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL3 | team_total | 0.700 | 0.645 | 0.656 | 65 | 36 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY3 | team_total | 0.541 | 0.475 | 0.488 | 49 | 54 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.161 | 0.115 | 0.123 | 12 | 89 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.244 | 0.195 | 0.204 | 20 | 81 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL6 | team_total | 0.150 | 0.100 | 0.109 | 11 | 91 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.149 | 0.100 | 0.109 | 11 | 91 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-6 | game_total | 0.580 | 0.525 | 0.536 | 53 | 48 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-8 | game_total | 0.275 | 0.225 | 0.234 | 23 | 78 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.316 | 0.265 | 0.275 | 27 | 74 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.157 | 0.205 | 0.195 | 21 | 80 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-7 | game_total | 0.469 | 0.415 | 0.426 | 42 | 59 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.081 | 0.125 | 0.115 | 13 | 88 | no | +0.031 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLGAME-26OCT08UTABOS-BOS | game_winner | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF3 | team_total | 0.637 | 0.585 | 0.596 | 59 | 42 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-9 | game_total | 0.230 | 0.185 | 0.193 | 19 | 82 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL4 | team_total | 0.496 | 0.440 | 0.451 | 45 | 57 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT08SJSTL-10 | game_total | 0.102 | 0.065 | 0.071 | 7 | 94 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY5 | team_total | 0.166 | 0.125 | 0.132 | 13 | 88 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.905 | 0.860 | 0.870 | 87 | 15 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH3 | team_total | 0.584 | 0.535 | 0.545 | 54 | 47 | yes | +0.027 | OK |
| KXNHLGAME-26OCT08NSHMTL-NSH | game_winner | 0.422 | 0.375 | 0.384 | 38 | 63 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.532 | 0.485 | 0.495 | 49 | 52 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT6 | team_total | 0.131 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-CAR4 | team_total | 0.559 | 0.610 | 0.600 | 62 | 40 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT08PHIOTT-9 | game_total | 0.194 | 0.155 | 0.162 | 16 | 85 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH4 | team_total | 0.370 | 0.315 | 0.326 | 33 | 70 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT3 | team_total | 0.680 | 0.635 | 0.644 | 64 | 37 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN3 | game_spread | 0.087 | 0.055 | 0.060 | 6 | 95 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL2 | team_total | 0.872 | 0.835 | 0.843 | 84 | 17 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-CGY4 | team_total | 0.327 | 0.275 | 0.285 | 29 | 74 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT08NSHMTL-MTL3 | game_spread | 0.234 | 0.275 | 0.266 | 28 | 73 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.129 | 0.085 | 0.092 | 10 | 93 | yes | +0.022 | OK |
| KXNHLGAME-26OCT08SJSTL-STL | game_winner | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-6 | game_total | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.726 | 0.765 | 0.757 | 77 | 24 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI2 | game_spread | 0.372 | 0.415 | 0.406 | 42 | 59 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.778 | 0.820 | 0.812 | 83 | 19 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-7 | game_total | 0.508 | 0.465 | 0.474 | 47 | 54 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT08SJSTL-STL2 | game_spread | 0.396 | 0.355 | 0.363 | 36 | 65 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT08MINTB-TB3 | game_spread | 0.198 | 0.235 | 0.227 | 24 | 77 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.854 | 0.890 | 0.883 | 90 | 12 | no | +0.019 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 27 recommended · full analysis in card.md / packet.json `thesis_card`

- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4969 (adj 0.4609) · $4.07 · thesis GAME:HIGH_EVENT
- Justin Danforth: 1+ goals YES @ 8c · p 0.1207 (adj 0.1043) · $2.86 · thesis BUF:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 16c · p 0.2086 (adj 0.189) · $3.43 · thesis BUF:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 12c · p 0.1604 (adj 0.144) · $2.68 · thesis BUF:OFFENSE_4PLUS
- Owen Power: 1+ assists YES @ 31c · p 0.3758 (adj 0.3379) · $1.82 · thesis BUF:OFFENSE_4PLUS
- Nils Hoglander: 1+ goals NO @ 81c · p 0.8422 (adj 0.8329) · $11.5 · thesis NSH:SUPPRESSED
- Jake Evans: 1+ goals YES @ 13c · p 0.1594 (adj 0.1483) · $1.89 · thesis MTL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.2902 (adj 0.2752) · $2.63 · thesis NSH:OFFENSE_4PLUS
- William Eklund: 1+ assists NO @ 63c · p 0.7865 (adj 0.6783) · $10.95 · thesis OTT:SUPPRESSED
- Carter Yakemchuk: 1+ assists NO @ 64c · p 0.7593 (adj 0.6785) · $8.83 · thesis OTT:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 13c · p 0.1622 (adj 0.1492) · $1.95 · thesis PHI:OFFENSE_4PLUS
- Jordan Spence: 1+ assists YES @ 27c · p 0.3431 (adj 0.2965) · $2.93 · thesis OTT:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 58c · p 0.7248 (adj 0.6242) · $6.93 · thesis TBL:SUPPRESSED
- Ilya Mikheyev: 1+ goals YES @ 16c · p 0.2042 (adj 0.1894) · $3.89 · thesis TBL:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 40c · p 0.4895 (adj 0.4423) · $3.99 · thesis TBL:SUPPRESSED
- John Carlson: 2+ assists NO @ 91c · p 0.9583 (adj 0.9266) · $8.86 · thesis TBL:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1869 (adj 0.1702) · $5.61 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2166 (adj 0.1962) · $4.88 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 20c · p 0.2489 (adj 0.2342) · $4.55 · thesis VAN:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 65c · p 0.705 (adj 0.69) · $11.84 · thesis CAR:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 11c · p 0.1637 (adj 0.1478) · $5.23 · thesis CHI:OFFENSE_4PLUS
- Calum Ritchie: 1+ assists YES @ 27c · p 0.3558 (adj 0.3079) · $5.34 · thesis NYI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7197 (adj 0.6321) · $12.09 · thesis CHI:SUPPRESSED
- Bo Horvat: 1+ goals NO @ 64c · p 0.6788 (adj 0.6666) · $5.34 · thesis NYI:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 70c · p 0.7731 (adj 0.729) · $11.22 · thesis SJS:SUPPRESSED
- Full Game: Over 8.5 goals scored YES @ 16c · p 0.2064 (adj 0.1807) · $1.72 · thesis GAME:HIGH_EVENT
- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4948 (adj 0.4599) · $2.96 · thesis GAME:HIGH_EVENT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 36/42 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.45, exp saves 24.51 (sd 6.77), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.34, exp saves 22.54 (sd 6.31), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| James Hagens: First Goalscorer | 0.031 | 0.040 | 4/ | -0.012 | PRIOR_HEAVY |
| David Pastrnak: 2+ goals | 0.061 | 0.060 | 8/96 | -0.024 | STANDARD |

**DAL @ BUF** · priced 115/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 25.45, exp saves 22.08 (sd 6.14), pull risk 0.056
- DAL net: Jake Oettinger (PROJECTED) exp shots 27.04, exp saves 23.28 (sd 6.48), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jiri Kulich: 1+ goals | 0.209 | 0.130 | 16/90 | +0.039 | STANDARD |
| Owen Power: 1+ assists | 0.376 | 0.300 | 31/71 | +0.051 | STANDARD |
| Zach Benson: 1+ assists | 0.366 | 0.295 | 31/72 | +0.041 | STANDARD |
| Zach Benson: 1+ points | 0.527 | 0.460 | 48/56 | +0.030 | STANDARD |
| Justin Danforth: 1+ goals | 0.121 | 0.055 | 8/97 | +0.036 | STANDARD |
| Peyton Krebs: 1+ goals | 0.160 | 0.095 | 12/93 | +0.033 | STANDARD |

**NSH @ MTL** · priced 114/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.02, exp saves 24.37 (sd 6.62), pull risk 0.054
- NSH net: Juuse Saros (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.63), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.209 | 0.330 | 35/69 | +0.086 | STANDARD |
| Chris Kreider: 1+ points | 0.408 | 0.525 | 53/48 | +0.095 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.346 | 0.260 | 28/76 | +0.052 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.465 | 0.380 | 40/64 | +0.049 | STANDARD |
| Nick Suzuki: 1+ assists | 0.511 | 0.575 | 59/44 | +0.032 | STANDARD |
| Chris Kreider: 2+ points | 0.099 | 0.160 | 18/86 | +0.033 | STANDARD |

**PHI @ OTT** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (PROJECTED) exp shots 23.58, exp saves 20.56 (sd 5.83), pull risk 0.049
- PHI net: Joseph Woll (PROJECTED) exp shots 28.92, exp saves 24.88 (sd 6.84), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.213 | 0.380 | 39/63 | +0.140 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.295 | 0.445 | 47/58 | +0.108 | PRIOR_HEAVY |
| William Eklund: 1+ points | 0.385 | 0.530 | 55/49 | +0.107 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.241 | 0.365 | 37/64 | +0.103 | PRIOR_HEAVY |
| Jordan Spence: 1+ assists | 0.343 | 0.250 | 27/77 | +0.059 | STANDARD |
| Jordan Spence: 1+ points | 0.402 | 0.325 | 34/69 | +0.046 | STANDARD |

**MIN @ TBL** · priced 153/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.09, exp saves 22.63 (sd 6.24), pull risk 0.058
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.6, exp saves 25.5 (sd 6.88), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.275 | 0.430 | 44/58 | +0.128 | STANDARD |
| John Carlson: 1+ points | 0.364 | 0.490 | 51/53 | +0.089 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.510 | 0.605 | 61/40 | +0.073 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.405 | 42/61 | +0.052 | STANDARD |
| John Carlson: 2+ points | 0.076 | 0.155 | 18/87 | +0.046 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.161 | 0.225 | 24/79 | +0.038 | STANDARD |

**VAN @ CAR** · priced 165/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.48, exp saves 19.78 (sd 5.62), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 32.08, exp saves 27.13 (sd 7.47), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 3+ points | 0.030 | 0.490 | 97/99 | -0.020 | STANDARD |
| Sebastian Aho: 1+ assists | 0.353 | 0.515 | 53/50 | +0.129 | STANDARD |
| Sebastian Aho: 1+ points | 0.544 | 0.670 | 68/34 | +0.100 | STANDARD |
| Sebastian Aho: 2+ points | 0.190 | 0.305 | 32/71 | +0.085 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.425 | 0.530 | 54/48 | +0.078 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.348 | 0.445 | 46/57 | +0.065 | STANDARD |

**CHI @ NYI** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 24.34, exp saves 21.41 (sd 5.94), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.5 (sd 7.18), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.280 | 0.415 | 42/59 | +0.113 | STANDARD |
| Patrick Kane: 1+ points | 0.451 | 0.570 | 59/45 | +0.081 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.231 | 0.335 | 35/68 | +0.073 | STANDARD |
| Calum Ritchie: 1+ points | 0.501 | 0.405 | 43/62 | +0.054 | STANDARD |
| Calum Ritchie: 1+ assists | 0.356 | 0.260 | 27/75 | +0.072 | STANDARD |
| Kyle Palmieri: 1+ points | 0.432 | 0.525 | 54/49 | +0.061 | STANDARD |

**SJS @ STL** · priced 152/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 25.77, exp saves 22.28 (sd 6.19), pull risk 0.06
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.07, exp saves 23.04 (sd 6.56), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dmitry Orlov: 1+ assists | 0.354 | 0.260 | 29/77 | +0.049 | STANDARD |
| Mason Marchment: 1+ assists | 0.227 | 0.315 | 33/70 | +0.058 | STANDARD |
| Adam Jiricek: 1+ points | 0.312 | 0.395 | 42/63 | +0.041 | PRIOR_HEAVY |
| Dmitry Orlov: 1+ points | 0.397 | 0.315 | 33/70 | +0.052 | STANDARD |
| Luca Cagnoni: 1+ points | 0.334 | 0.415 | 44/61 | +0.040 | STANDARD |
| Mason McTavish: 1+ assists | 0.229 | 0.310 | 33/71 | +0.047 | STANDARD |

**COL @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 32.7, exp saves 27.83 (sd 7.58), pull risk 0.073
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.32, exp saves 22.94 (sd 6.3), pull risk 0.056

**TOR @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 24.89, exp saves 21.95 (sd 6.05), pull risk 0.043
- TOR net: Anthony Stolarz (PROJECTED) exp shots 31.39, exp saves 26.48 (sd 7.37), pull risk 0.088

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
