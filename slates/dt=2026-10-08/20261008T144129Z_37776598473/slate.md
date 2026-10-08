# NHL slate 2026-10-08 — RESEARCH_ONLY

generated 2026-10-08T14:41:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 10 · simulated (not started): 10 · markets on board: 3934 · contracts joined: 1912 (unjoined to any game: 1560)
gates: {'UNSUPPORTED': 1662, 'OK': 171, 'NO_EDGE': 79}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 229, 'game_early_goal': 10, 'first_goal': 350, 'game_winner': 20, 'player_goals': 527, 'game_overtime': 10, 'player_points': 296, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 2026-10-08T23:00:00Z | T-6h | 0.508 | 0.492 | 0.181 | 6.12 | 3.08 | 3.04 | 93 (25/68) | PROJECTED/PROJECTED |
| DAL @ BUF | 2026-10-08T23:00:00Z | T-6h | 0.567 | 0.433 | 0.171 | 6.07 | 3.24 | 2.83 | 174 (25/149) | PROJECTED/PROJECTED |
| NSH @ MTL | 2026-10-08T23:00:00Z | T-6h | 0.578 | 0.422 | 0.166 | 6.58 | 3.54 | 3.03 | 169 (25/144) | PROJECTED/PROJECTED |
| PHI @ OTT | 2026-10-08T23:00:00Z | T-6h | 0.608 | 0.392 | 0.171 | 6.21 | 3.45 | 2.76 | 214 (25/189) | PROJECTED/PROJECTED |
| MIN @ TBL | 2026-10-08T23:00:00Z | T-6h | 0.559 | 0.441 | 0.180 | 5.92 | 3.14 | 2.78 | 206 (25/181) | PROJECTED/PROJECTED |
| VAN @ CAR | 2026-10-08T23:00:00Z | T-6h | 0.672 | 0.328 | 0.154 | 6.61 | 3.88 | 2.73 | 216 (25/191) | PROJECTED/PROJECTED |
| CHI @ NYI | 2026-10-08T23:30:00Z | T-6h | 0.604 | 0.397 | 0.175 | 5.83 | 3.24 | 2.60 | 200 (25/175) | PROBABLE/PROJECTED |
| SJS @ STL | 2026-10-09T00:00:00Z | T-6h | 0.619 | 0.381 | 0.169 | 6.42 | 3.59 | 2.83 | 203 (25/178) | PROJECTED/PROJECTED |
| COL @ CGY | 2026-10-09T01:00:00Z | T-6h | 0.432 | 0.568 | 0.183 | 5.76 | 2.66 | 3.10 | 209 (25/184) | PROJECTED/PROJECTED |
| TOR @ VGK | 2026-10-09T02:00:00Z | T-6h | 0.681 | 0.319 | 0.153 | 6.78 | 4.01 | 2.77 | 228 (25/203) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL4 | team_total | 0.385 | 0.535 | 0.505 | 54 | 47 | no | +0.127 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL3 | team_total | 0.610 | 0.745 | 0.721 | 75 | 26 | no | +0.117 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL3 | game_spread | 0.206 | 0.335 | 0.306 | 34 | 67 | no | +0.109 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL5 | team_total | 0.199 | 0.325 | 0.297 | 33 | 68 | no | +0.106 | OK |
| KXNHLSPREAD-26OCT08COLCGY-COL2 | game_spread | 0.338 | 0.465 | 0.439 | 47 | 54 | no | +0.104 | OK |
| KXNHLGAME-26OCT08COLCGY-CGY | game_winner | 0.432 | 0.315 | 0.337 | 32 | 69 | yes | +0.097 | OK |
| KXNHLGAME-26OCT08COLCGY-COL | game_winner | 0.568 | 0.675 | 0.655 | 68 | 33 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR3 | game_spread | 0.313 | 0.415 | 0.394 | 42 | 59 | no | +0.080 | OK |
| KXNHLTOTAL-26OCT08COLCGY-7 | game_total | 0.374 | 0.475 | 0.454 | 48 | 53 | no | +0.079 | OK |
| KXNHLGAME-26OCT08VANCAR-VAN | game_winner | 0.328 | 0.235 | 0.252 | 24 | 77 | yes | +0.075 | OK |
| KXNHLTOTAL-26OCT08COLCGY-5 | game_total | 0.718 | 0.805 | 0.789 | 81 | 20 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL2 | team_total | 0.813 | 0.895 | 0.882 | 90 | 11 | no | +0.070 | OK |
| KXNHLGAME-26OCT08DALBUF-BUF | game_winner | 0.567 | 0.475 | 0.493 | 48 | 53 | yes | +0.070 | OK |
| KXNHLTOTAL-26OCT08COLCGY-6 | game_total | 0.483 | 0.580 | 0.561 | 59 | 43 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK5 | team_total | 0.382 | 0.290 | 0.307 | 30 | 72 | yes | +0.068 | OK |
| KXNHLSPREAD-26OCT08VANCAR-CAR2 | game_spread | 0.457 | 0.545 | 0.527 | 55 | 46 | no | +0.065 | OK |
| KXNHLGAME-26OCT08VANCAR-CAR | game_winner | 0.672 | 0.755 | 0.740 | 76 | 25 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK6 | team_total | 0.213 | 0.130 | 0.144 | 14 | 88 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK2 | game_spread | 0.471 | 0.385 | 0.402 | 39 | 62 | yes | +0.064 | OK |
| KXNHLGAME-26OCT08DALBUF-DAL | game_winner | 0.433 | 0.515 | 0.499 | 52 | 49 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN3 | team_total | 0.515 | 0.435 | 0.451 | 44 | 57 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN4 | team_total | 0.300 | 0.225 | 0.239 | 23 | 78 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK4 | team_total | 0.583 | 0.505 | 0.521 | 51 | 50 | yes | +0.056 | OK |
| KXNHLGAME-26OCT08TORVGK-VGK | game_winner | 0.681 | 0.605 | 0.621 | 61 | 40 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08COLCGY-COL6 | team_total | 0.087 | 0.160 | 0.142 | 17 | 85 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL3 | team_total | 0.540 | 0.625 | 0.608 | 64 | 39 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF2 | game_spread | 0.346 | 0.275 | 0.289 | 28 | 73 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT08TORVGK-8 | game_total | 0.345 | 0.275 | 0.288 | 28 | 73 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT08SJSTL-8 | game_total | 0.293 | 0.225 | 0.238 | 23 | 78 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 | team_total | 0.323 | 0.400 | 0.384 | 41 | 61 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK3 | team_total | 0.774 | 0.700 | 0.716 | 71 | 31 | yes | +0.050 | OK |
| KXNHLTOTAL-26OCT08COLCGY-8 | game_total | 0.198 | 0.270 | 0.254 | 28 | 74 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL3 | game_spread | 0.131 | 0.195 | 0.180 | 20 | 81 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT08TORVGK-VGK3 | game_spread | 0.332 | 0.265 | 0.278 | 27 | 74 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT08COLCGY-4 | game_total | 0.815 | 0.875 | 0.865 | 88 | 13 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY2 | game_spread | 0.215 | 0.155 | 0.166 | 16 | 85 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT08DALBUF-DAL2 | game_spread | 0.230 | 0.295 | 0.281 | 30 | 71 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN2 | team_total | 0.750 | 0.685 | 0.699 | 69 | 32 | yes | +0.045 | OK |
| KXNHLGAME-26OCT08TORVGK-TOR | game_winner | 0.319 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL6 | team_total | 0.150 | 0.095 | 0.104 | 10 | 91 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-VAN5 | team_total | 0.149 | 0.095 | 0.104 | 10 | 91 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL2 | team_total | 0.768 | 0.830 | 0.819 | 84 | 18 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT08TORVGK-9 | game_total | 0.252 | 0.195 | 0.206 | 20 | 81 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT08SJSTL-9 | game_total | 0.208 | 0.155 | 0.165 | 16 | 85 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT08COLCGY-9 | game_total | 0.132 | 0.185 | 0.173 | 19 | 82 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT08TORVGK-6 | game_total | 0.653 | 0.595 | 0.607 | 60 | 41 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL5 | team_total | 0.299 | 0.235 | 0.247 | 25 | 78 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR2 | game_spread | 0.153 | 0.205 | 0.194 | 21 | 80 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT08TORVGK-VGK2 | team_total | 0.911 | 0.865 | 0.876 | 87 | 14 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08COLCGY-CGY3 | game_spread | 0.118 | 0.075 | 0.082 | 8 | 93 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-BUF3 | team_total | 0.640 | 0.585 | 0.596 | 59 | 42 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN2 | game_spread | 0.161 | 0.115 | 0.123 | 12 | 89 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT08TORVGK-TOR3 | game_spread | 0.081 | 0.125 | 0.115 | 13 | 88 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-8 | game_total | 0.316 | 0.265 | 0.275 | 27 | 74 | yes | +0.032 | OK |
| KXNHLGAME-26OCT08UTABOS-UTA | game_winner | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLGAME-26OCT08UTABOS-BOS | game_winner | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT08SJSTL-6 | game_total | 0.597 | 0.545 | 0.555 | 55 | 46 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH5 | team_total | 0.198 | 0.150 | 0.159 | 16 | 86 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-CAR3 | team_total | 0.750 | 0.795 | 0.786 | 80 | 21 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-9 | game_total | 0.230 | 0.185 | 0.193 | 19 | 82 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08SJSTL-STL4 | team_total | 0.496 | 0.445 | 0.455 | 45 | 56 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT08MINTB-TB4 | team_total | 0.395 | 0.445 | 0.435 | 45 | 56 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT08DALBUF-DAL5 | team_total | 0.161 | 0.205 | 0.196 | 21 | 80 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT08SJSTL-7 | game_total | 0.484 | 0.430 | 0.441 | 44 | 58 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH3 | team_total | 0.584 | 0.535 | 0.545 | 54 | 47 | yes | +0.027 | OK |
| KXNHLGAME-26OCT08NSHMTL-NSH | game_winner | 0.422 | 0.375 | 0.384 | 38 | 63 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH6 | team_total | 0.089 | 0.055 | 0.061 | 6 | 95 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT08DALBUF-BUF3 | game_spread | 0.215 | 0.175 | 0.182 | 18 | 83 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT08NSHMTL-NSH4 | team_total | 0.370 | 0.315 | 0.326 | 33 | 70 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT08TORVGK-7 | game_total | 0.541 | 0.495 | 0.504 | 50 | 51 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT08TORVGK-10 | game_total | 0.130 | 0.095 | 0.101 | 10 | 91 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT08VANCAR-VAN3 | game_spread | 0.087 | 0.055 | 0.060 | 6 | 95 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT08NSHMTL-MTL3 | game_spread | 0.234 | 0.275 | 0.266 | 28 | 73 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT08VANCAR-CAR2 | team_total | 0.893 | 0.925 | 0.919 | 93 | 8 | no | +0.022 | OK |
| KXNHLGAME-26OCT08SJSTL-STL | game_winner | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-6 | game_total | 0.619 | 0.575 | 0.584 | 58 | 43 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT08CHINYI-5 | game_total | 0.726 | 0.765 | 0.757 | 77 | 24 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-10 | game_total | 0.117 | 0.085 | 0.091 | 9 | 92 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT08CHINYI-NYI2 | game_spread | 0.372 | 0.415 | 0.406 | 42 | 59 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT08NSHMTL-7 | game_total | 0.508 | 0.465 | 0.474 | 47 | 54 | yes | +0.021 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ BOS | 0.508 | 0.499 | 0.181 | 0.215 | 6.12 | 6.47 | 0.968/0.992 | KXNHLTOTAL-26OCT08UTABOS-7 +0.060 |
| DAL @ BUF | 0.567 | 0.529 | 0.171 | 0.222 | 6.07 | 6.18 | 0.997/0.986 | KXNHLTEAMTOTAL-26OCT08DALBUF-DAL4 +0.041 |
| NSH @ MTL | 0.578 | 0.576 | 0.166 | 0.214 | 6.58 | 6.52 | 0.952/1.000 | KXNHLTOTAL-26OCT08NSHMTL-8 -0.016 |
| PHI @ OTT | 0.608 | 0.587 | 0.171 | 0.213 | 6.21 | 5.92 | 0.994/0.991 | KXNHLTEAMTOTAL-26OCT08PHIOTT-OTT4 -0.056 |
| MIN @ TBL | 0.559 | 0.539 | 0.180 | 0.219 | 5.92 | 6.30 | 0.957/1.003 | KXNHLTOTAL-26OCT08MINTB-7 +0.067 |
| VAN @ CAR | 0.672 | 0.613 | 0.154 | 0.207 | 6.61 | 6.57 | 0.997/1.020 | KXNHLSPREAD-26OCT08VANCAR-CAR2 -0.063 |
| CHI @ NYI | 0.604 | 0.611 | 0.175 | 0.213 | 5.83 | 6.24 | 0.951/1.003 | KXNHLTOTAL-26OCT08CHINYI-7 +0.075 |
| SJS @ STL | 0.619 | 0.565 | 0.169 | 0.215 | 6.42 | 6.43 | 0.993/1.034 | KXNHLGAME-26OCT08SJSTL-SJ +0.054 |
| COL @ CGY | 0.432 | 0.434 | 0.183 | 0.212 | 5.76 | 6.27 | 0.986/0.973 | KXNHLTOTAL-26OCT08COLCGY-7 +0.086 |
| TOR @ VGK | 0.681 | 0.649 | 0.153 | 0.203 | 6.78 | 6.34 | 1.003/0.978 | KXNHLTOTAL-26OCT08TORVGK-6 -0.074 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Boston over 4.5 goals scored YES @ 18c · p 0.2337 (adj 0.2043) · $1.29 · thesis BOS:OFFENSE_4PLUS
- Full Game: Over 6.5 goals scored YES @ 43c · p 0.4969 (adj 0.4609) · $1.45 · thesis GAME:HIGH_EVENT
- Jiri Kulich: 1+ goals YES @ 16c · p 0.2143 (adj 0.1957) · $2.87 · thesis BUF:OFFENSE_4PLUS
- Justin Danforth: 1+ goals YES @ 8c · p 0.1174 (adj 0.1031) · $1.72 · thesis BUF:OFFENSE_4PLUS
- Owen Power: 1+ assists YES @ 31c · p 0.3957 (adj 0.3478) · $2.64 · thesis BUF:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 71c · p 0.7509 (adj 0.7382) · $5.05 · thesis DAL:SUPPRESSED
- Jonathan Marchessault: 1+ assists YES @ 26c · p 0.3462 (adj 0.2981) · $3.11 · thesis NSH:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 13c · p 0.1594 (adj 0.1495) · $1.4 · thesis MTL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.2902 (adj 0.2777) · $1.8 · thesis NSH:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 69c · p 0.791 (adj 0.7156) · $4.66 · thesis MTL:SUPPRESSED
- William Eklund: 1+ assists NO @ 62c · p 0.7897 (adj 0.6729) · $6.85 · thesis OTT:SUPPRESSED
- Carter Yakemchuk: 1+ assists NO @ 64c · p 0.7589 (adj 0.6784) · $5.64 · thesis OTT:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 12c · p 0.1529 (adj 0.1422) · $1.68 · thesis PHI:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 14c · p 0.1738 (adj 0.1616) · $1.65 · thesis OTT:OFFENSE_4PLUS
- Ilya Mikheyev: 1+ goals YES @ 16c · p 0.2042 (adj 0.1906) · $2.71 · thesis TBL:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 58c · p 0.7248 (adj 0.6242) · $7.75 · thesis TBL:SUPPRESSED
- Nikita Kucherov: 1+ assists NO @ 40c · p 0.4895 (adj 0.4423) · $4.13 · thesis TBL:SUPPRESSED
- Ryan Hartman: 1+ goals YES @ 19c · p 0.2264 (adj 0.216) · $1.92 · thesis MIN:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 12c · p 0.1869 (adj 0.1689) · $3.69 · thesis VAN:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 64c · p 0.705 (adj 0.6875) · $7.35 · thesis CAR:SUPPRESSED
- Sebastian Aho: 1+ assists NO @ 49c · p 0.6465 (adj 0.5383) · $5.14 · thesis CAR:SUPPRESSED
- Carolina wins by over 2.5 goals NO @ 59c · p 0.7306 (adj 0.636) · $4.34 · thesis GAME:TIGHT
- Ryan Greene: 1+ goals YES @ 12c · p 0.1637 (adj 0.1503) · $2.51 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 2+ assists NO @ 90c · p 0.9559 (adj 0.9229) · $8.33 · thesis CHI:SUPPRESSED
- Calum Ritchie: 1+ assists YES @ 27c · p 0.3558 (adj 0.3079) · $3.43 · thesis NYI:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 63c · p 0.6788 (adj 0.6641) · $5.59 · thesis NYI:SUPPRESSED
- Ivar Stenberg: 1+ assists NO @ 72c · p 0.7987 (adj 0.7569) · $7.08 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 70c · p 0.7731 (adj 0.729) · $5.42 · thesis SJS:SUPPRESSED
- Full Game: Over 8.5 goals scored YES @ 16c · p 0.2064 (adj 0.1807) · $1.02 · thesis GAME:HIGH_EVENT
- Full Game: Over 7.5 goals scored YES @ 23c · p 0.2839 (adj 0.2545) · $1.03 · thesis GAME:HIGH_EVENT
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.6435 (adj 0.6201) · $8.22 · thesis COL:SUPPRESSED
- Cale Makar: 3+ assists NO @ 94c · p 0.9843 (adj 0.9571) · $8.22 · thesis DIFFUSE
- Colorado over 4.5 goals scored NO @ 68c · p 0.7558 (adj 0.7154) · $4.38 · thesis CGY:WINS
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0943 (adj 0.082) · $1.72 · thesis VGK:OFFENSE_4PLUS
- Kirill Marchenko: 2+ assists NO @ 92c · p 0.9644 (adj 0.9372) · $7.88 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 66c · p 0.7043 (adj 0.692) · $4.61 · thesis TOR:SUPPRESSED
- Mark Stone: 1+ goals YES @ 32c · p 0.3583 (adj 0.3462) · $1.72 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ BOS** · priced 36/42 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.45, exp saves 24.51 (sd 6.77), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.34, exp saves 22.54 (sd 6.31), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: First Goalscorer | 0.060 | 0.080 | 8/ | -0.025 | STANDARD |
| David Pastrnak: 2+ goals | 0.061 | 0.075 | 9/94 | -0.005 | STANDARD |
| Morgan Geekie: First Goalscorer | 0.062 | 0.050 | 6/ | -0.002 | STANDARD |
| Nick Schmaltz: First Goalscorer | 0.060 | 0.070 | 7/ | -0.014 | STANDARD |
| James Hagens: First Goalscorer | 0.031 | 0.040 | 4/ | -0.012 | PRIOR_HEAVY |
| Dylan Guenther: First Goalscorer | 0.061 | 0.070 | 7/ | -0.013 | STANDARD |

**DAL @ BUF** · priced 115/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 25.45, exp saves 22.1 (sd 6.09), pull risk 0.056
- DAL net: Jake Oettinger (PROJECTED) exp shots 27.04, exp saves 23.28 (sd 6.43), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Owen Power: 1+ assists | 0.396 | 0.300 | 31/71 | +0.071 | STANDARD |
| Jiri Kulich: 1+ goals | 0.214 | 0.140 | 16/88 | +0.045 | STANDARD |
| Zach Benson: 1+ assists | 0.368 | 0.295 | 31/72 | +0.043 | STANDARD |
| Zach Benson: 1+ points | 0.529 | 0.460 | 48/56 | +0.031 | STANDARD |
| Tage Thompson: 1+ assists | 0.352 | 0.415 | 42/59 | +0.041 | STANDARD |
| Konsta Helenius: 1+ goals | 0.188 | 0.125 | 17/92 | +0.008 | STANDARD |

**NSH @ MTL** · priced 114/118 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.02, exp saves 24.37 (sd 6.62), pull risk 0.054
- NSH net: Juuse Saros (PROJECTED) exp shots 27.64, exp saves 23.6 (sd 6.63), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ points | 0.408 | 0.525 | 53/48 | +0.095 | STANDARD |
| Chris Kreider: 1+ assists | 0.209 | 0.325 | 34/69 | +0.086 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.346 | 0.250 | 26/76 | +0.073 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.465 | 0.380 | 40/64 | +0.049 | STANDARD |
| Nick Suzuki: 1+ assists | 0.511 | 0.595 | 61/42 | +0.052 | STANDARD |
| Chris Kreider: 2+ points | 0.099 | 0.170 | 19/85 | +0.042 | STANDARD |

**PHI @ OTT** · priced 161/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 23.58, exp saves 20.6 (sd 5.77), pull risk 0.046
- PHI net: Joseph Woll (PROJECTED) exp shots 28.92, exp saves 24.85 (sd 6.78), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.210 | 0.390 | 40/62 | +0.153 | STANDARD |
| William Eklund: 1+ points | 0.383 | 0.540 | 56/48 | +0.120 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.294 | 0.445 | 47/58 | +0.109 | PRIOR_HEAVY |
| Carter Yakemchuk: 1+ assists | 0.241 | 0.365 | 37/64 | +0.103 | PRIOR_HEAVY |
| William Eklund: 2+ points | 0.087 | 0.195 | 21/82 | +0.083 | STANDARD |
| Jordan Spence: 1+ assists | 0.340 | 0.260 | 28/76 | +0.046 | STANDARD |

**MIN @ TBL** · priced 153/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.09, exp saves 22.63 (sd 6.24), pull risk 0.058
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.6, exp saves 25.5 (sd 6.88), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.275 | 0.430 | 44/58 | +0.128 | STANDARD |
| John Carlson: 1+ points | 0.364 | 0.500 | 52/52 | +0.099 | STANDARD |
| Nikita Kucherov: 2+ points | 0.321 | 0.425 | 44/59 | +0.072 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.510 | 0.605 | 61/40 | +0.073 | STANDARD |
| John Carlson: 2+ points | 0.076 | 0.170 | 18/84 | +0.074 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.161 | 0.245 | 26/77 | +0.057 | STANDARD |

**VAN @ CAR** · priced 165/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.48, exp saves 19.78 (sd 5.62), pull risk 0.05
- VAN net: Kevin Lankinen (PROJECTED) exp shots 32.08, exp saves 27.13 (sd 7.47), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 3+ points | 0.030 | 0.490 | 97/99 | -0.020 | STANDARD |
| Sebastian Aho: 1+ assists | 0.353 | 0.520 | 53/49 | +0.139 | STANDARD |
| Sebastian Aho: 1+ points | 0.544 | 0.675 | 68/33 | +0.111 | STANDARD |
| Sebastian Aho: 2+ points | 0.190 | 0.315 | 32/69 | +0.105 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.425 | 0.535 | 55/48 | +0.078 | STANDARD |
| Elias Pettersson (#40): 1+ goals | 0.220 | 0.125 | 22/97 | -0.012 | STANDARD |

**CHI @ NYI** · priced 149/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 24.34, exp saves 21.41 (sd 5.94), pull risk 0.05
- CHI net: Spencer Knight (PROJECTED) exp shots 30.03, exp saves 25.5 (sd 7.18), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.280 | 0.415 | 43/60 | +0.103 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.231 | 0.340 | 35/67 | +0.083 | STANDARD |
| Kyle Palmieri: 1+ points | 0.432 | 0.530 | 54/48 | +0.071 | STANDARD |
| Calum Ritchie: 1+ assists | 0.356 | 0.260 | 27/75 | +0.072 | STANDARD |
| Patrick Kane: 1+ points | 0.451 | 0.545 | 56/47 | +0.061 | STANDARD |
| Patrick Kane: 2+ points | 0.124 | 0.210 | 22/80 | +0.065 | STANDARD |

**SJS @ STL** · priced 152/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 25.77, exp saves 22.28 (sd 6.19), pull risk 0.06
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.07, exp saves 23.04 (sd 6.56), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason Marchment: 1+ assists | 0.227 | 0.315 | 33/70 | +0.058 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.201 | 0.285 | 29/72 | +0.065 | PRIOR_HEAVY |
| Dmitry Orlov: 1+ assists | 0.354 | 0.270 | 29/75 | +0.049 | STANDARD |
| Adam Jiricek: 1+ points | 0.312 | 0.395 | 42/63 | +0.041 | PRIOR_HEAVY |
| Dmitry Orlov: 1+ points | 0.397 | 0.320 | 34/70 | +0.041 | STANDARD |
| Luca Cagnoni: 1+ points | 0.334 | 0.410 | 43/61 | +0.040 | STANDARD |

**COL @ CGY** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 32.7, exp saves 27.87 (sd 7.48), pull risk 0.073
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.32, exp saves 22.97 (sd 6.27), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.282 | 0.510 | 53/51 | +0.191 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.454 | 0.660 | 67/35 | +0.180 | STANDARD |
| Cale Makar: 1+ assists | 0.401 | 0.580 | 59/43 | +0.152 | STANDARD |
| Martin Necas: 2+ points | 0.236 | 0.400 | 42/62 | +0.128 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.646 | 0.810 | 83/21 | +0.132 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.122 | 0.285 | 29/72 | +0.144 | STANDARD |

**TOR @ VGK** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 24.89, exp saves 21.95 (sd 6.02), pull risk 0.043
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.39, exp saves 26.52 (sd 7.32), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ points | 0.302 | 0.420 | 44/60 | +0.081 | PRIOR_HEAVY |
| Gavin McKenna: 1+ assists | 0.182 | 0.295 | 31/72 | +0.084 | PRIOR_HEAVY |
| Darren Raddysh: 1+ assists | 0.282 | 0.395 | 41/62 | +0.082 | STANDARD |
| Darren Raddysh: 1+ points | 0.374 | 0.480 | 50/54 | +0.069 | STANDARD |
| Kirill Marchenko: 1+ points | 0.441 | 0.545 | 57/48 | +0.061 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.262 | 0.365 | 38/65 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
