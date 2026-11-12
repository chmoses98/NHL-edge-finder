# NHL slate 2026-11-12 — RESEARCH_ONLY

generated 2026-11-12T21:54:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 10 · markets on board: 3874 · contracts joined: 2165 (unjoined to any game: 1319)
gates: {'UNSUPPORTED': 1915, 'OK': 152, 'NO_EDGE': 98}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 289, 'game_early_goal': 10, 'first_goal': 355, 'game_winner': 20, 'player_goals': 612, 'game_overtime': 10, 'player_points': 382, 'goalie_saves': 17, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ BOS | 2026-11-13T00:00:00Z | T-90m | 0.583 | 0.417 | 0.179 | 5.91 | 3.21 | 2.70 | 216 (25/191) | CONFIRMED/CONFIRMED |
| MIN @ TOR | 2026-11-13T00:00:00Z | T-90m | 0.430 | 0.570 | 0.172 | 6.43 | 2.99 | 3.44 | 211 (25/186) | CONFIRMED/PROJECTED |
| COL @ OTT | 2026-11-13T00:00:00Z | T-90m | 0.457 | 0.543 | 0.175 | 6.40 | 3.06 | 3.34 | 234 (25/209) | CONFIRMED/PROJECTED |
| WSH @ NJD | 2026-11-13T00:00:00Z | T-90m | 0.557 | 0.443 | 0.175 | 6.17 | 3.27 | 2.91 | 218 (25/193) | PROJECTED/PROJECTED |
| TBL @ CBJ | 2026-11-13T00:00:00Z | T-90m | 0.457 | 0.543 | 0.179 | 5.88 | 2.81 | 3.07 | 216 (25/191) | CONFIRMED/PROJECTED |
| DET @ FLA | 2026-11-13T00:30:00Z | T-90m | 0.573 | 0.427 | 0.176 | 6.08 | 3.27 | 2.82 | 223 (25/198) | CONFIRMED/PROJECTED |
| BUF @ CHI | 2026-11-13T01:00:00Z | T-3h | 0.454 | 0.546 | 0.182 | 5.94 | 2.83 | 3.11 | 213 (25/188) | PROJECTED/PROJECTED |
| WPG @ DAL | 2026-11-13T01:00:00Z | T-3h | 0.600 | 0.400 | 0.184 | 5.77 | 3.19 | 2.57 | 213 (25/188) | CONFIRMED/PROJECTED |
| STL @ UTA | 2026-11-13T02:00:00Z | T-3h | 0.511 | 0.489 | 0.172 | 6.17 | 3.13 | 3.04 | 223 (25/198) | PROJECTED/PROJECTED |
| NYI @ LAK | 2026-11-13T03:00:00Z | T-3h | 0.554 | 0.446 | 0.185 | 5.66 | 3.00 | 2.66 | 198 (25/173) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV12TBCBJ-7 | game_total | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-6 | game_total | 0.507 | 0.605 | 0.586 | 61 | 40 | no | +0.076 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-7 | game_total | 0.407 | 0.505 | 0.485 | 51 | 50 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF4 | team_total | 0.390 | 0.490 | 0.470 | 50 | 52 | no | +0.072 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-5 | game_total | 0.732 | 0.815 | 0.800 | 82 | 19 | no | +0.068 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-6 | game_total | 0.518 | 0.605 | 0.588 | 61 | 40 | no | +0.065 | OK |
| KXNHLTOTAL-26NOV12NYILA-7 | game_total | 0.359 | 0.445 | 0.427 | 45 | 56 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV12NYILA-6 | game_total | 0.469 | 0.555 | 0.538 | 56 | 45 | no | +0.064 | OK |
| KXNHLTOTAL-26NOV12NYILA-5 | game_total | 0.695 | 0.775 | 0.760 | 78 | 23 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL3 | team_total | 0.513 | 0.595 | 0.579 | 60 | 41 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ4 | team_total | 0.324 | 0.405 | 0.388 | 41 | 60 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL4 | team_total | 0.298 | 0.375 | 0.359 | 38 | 63 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF3 | team_total | 0.609 | 0.690 | 0.675 | 70 | 32 | no | +0.056 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-5 | game_total | 0.735 | 0.810 | 0.796 | 82 | 20 | no | +0.054 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-4 | game_total | 0.825 | 0.885 | 0.875 | 89 | 12 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL2 | team_total | 0.741 | 0.810 | 0.797 | 82 | 20 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF5 | team_total | 0.209 | 0.275 | 0.261 | 28 | 73 | no | +0.048 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-5 | game_total | 0.733 | 0.795 | 0.784 | 80 | 21 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-4 | game_total | 0.829 | 0.885 | 0.875 | 89 | 12 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 | team_total | 0.541 | 0.610 | 0.597 | 62 | 40 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI3 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.042 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-8 | game_total | 0.224 | 0.285 | 0.272 | 29 | 72 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI2 | team_total | 0.737 | 0.800 | 0.788 | 81 | 21 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-8 | game_total | 0.216 | 0.275 | 0.262 | 28 | 73 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ5 | team_total | 0.158 | 0.220 | 0.206 | 23 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF2 | team_total | 0.812 | 0.870 | 0.860 | 88 | 14 | no | +0.040 | OK |
| KXNHLTOTAL-26NOV12NYILA-4 | game_total | 0.793 | 0.845 | 0.836 | 85 | 16 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ2 | team_total | 0.763 | 0.825 | 0.814 | 84 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-NYI4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.036 | OK |
| KXNHLGAME-26NOV12COLOTT-COL | game_winner | 0.543 | 0.485 | 0.497 | 49 | 52 | yes | +0.035 | OK |
| KXNHLGAME-26NOV12COLOTT-OTT | game_winner | 0.457 | 0.515 | 0.503 | 52 | 49 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV12BUFCHI-9 | game_total | 0.154 | 0.210 | 0.198 | 22 | 80 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV12COLOTT-OTT2 | game_spread | 0.250 | 0.305 | 0.294 | 31 | 70 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF3 | game_spread | 0.193 | 0.250 | 0.238 | 26 | 76 | no | +0.034 | OK |
| KXNHLGAME-26NOV12STLUTA-STL | game_winner | 0.489 | 0.545 | 0.534 | 55 | 46 | no | +0.034 | OK |
| KXNHLGAME-26NOV12STLUTA-UTA | game_winner | 0.511 | 0.455 | 0.466 | 46 | 55 | yes | +0.034 | OK |
| KXNHLSPREAD-26NOV12DETFLA-FLA3 | game_spread | 0.213 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-6 | game_total | 0.511 | 0.570 | 0.558 | 58 | 44 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV12NYILA-LA4 | team_total | 0.362 | 0.415 | 0.404 | 42 | 59 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV12TBCBJ-9 | game_total | 0.148 | 0.200 | 0.189 | 21 | 81 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ2 | game_spread | 0.246 | 0.295 | 0.285 | 30 | 71 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-7 | game_total | 0.404 | 0.455 | 0.445 | 46 | 55 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV12NYILA-8 | game_total | 0.189 | 0.235 | 0.225 | 24 | 77 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV12MTLBOS-MTL5 | team_total | 0.141 | 0.190 | 0.179 | 20 | 82 | no | +0.028 | OK |
| KXNHLGAME-26NOV12BUFCHI-BUF | game_winner | 0.546 | 0.595 | 0.585 | 60 | 41 | no | +0.027 | OK |
| KXNHLGAME-26NOV12BUFCHI-CHI | game_winner | 0.454 | 0.405 | 0.415 | 41 | 60 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-4 | game_total | 0.825 | 0.870 | 0.862 | 88 | 14 | no | +0.027 | OK |
| KXNHLGAME-26NOV12MTLBOS-MTL | game_winner | 0.417 | 0.465 | 0.455 | 47 | 54 | no | +0.026 | OK |
| KXNHLGAME-26NOV12TBCBJ-TB | game_winner | 0.543 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLSPREAD-26NOV12BUFCHI-BUF2 | game_spread | 0.319 | 0.365 | 0.356 | 37 | 64 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV12COLOTT-OTT3 | game_spread | 0.146 | 0.190 | 0.180 | 20 | 82 | no | +0.024 | OK |
| KXNHLSPREAD-26NOV12MTLBOS-MTL2 | game_spread | 0.213 | 0.260 | 0.250 | 27 | 75 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12STLUTA-STL2 | game_spread | 0.272 | 0.315 | 0.306 | 32 | 69 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-6 | game_total | 0.489 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLGAME-26NOV12MINTOR-TOR | game_winner | 0.430 | 0.385 | 0.394 | 39 | 62 | yes | +0.023 | OK |
| KXNHLGAME-26NOV12MINTOR-MIN | game_winner | 0.570 | 0.615 | 0.606 | 62 | 39 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12MTLBOS-MTL3 | game_spread | 0.118 | 0.155 | 0.147 | 16 | 85 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN3 | game_spread | 0.224 | 0.270 | 0.260 | 28 | 74 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV12COLOTT-COL2 | game_spread | 0.327 | 0.285 | 0.293 | 29 | 72 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV12TBCBJ-CBJ3 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV12NYILA-9 | game_total | 0.129 | 0.165 | 0.157 | 17 | 84 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV12MINTOR-MIN2 | game_spread | 0.352 | 0.395 | 0.386 | 40 | 61 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV12BUFCHI-BUF6 | team_total | 0.091 | 0.125 | 0.118 | 13 | 88 | no | +0.021 | OK |
| KXNHLGAME-26NOV12DETFLA-DET | game_winner | 0.427 | 0.385 | 0.393 | 39 | 62 | yes | +0.021 | OK |
| KXNHLGAME-26NOV12DETFLA-FLA | game_winner | 0.573 | 0.615 | 0.607 | 62 | 39 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-5 | game_total | 0.716 | 0.760 | 0.752 | 77 | 25 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV12MINTOR-TOR3 | team_total | 0.577 | 0.535 | 0.544 | 54 | 47 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-7 | game_total | 0.376 | 0.415 | 0.407 | 42 | 59 | no | +0.017 | OK |
| KXNHLGAME-26NOV12WSHNJ-NJ | game_winner | 0.557 | 0.595 | 0.587 | 60 | 41 | no | +0.016 | OK |
| KXNHLGAME-26NOV12WSHNJ-WSH | game_winner | 0.443 | 0.405 | 0.413 | 41 | 60 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV12WPGDAL-4 | game_total | 0.815 | 0.845 | 0.839 | 85 | 16 | no | +0.016 | OK |
| KXNHLGAME-26NOV12MTLBOS-BOS | game_winner | 0.583 | 0.545 | 0.553 | 55 | 46 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-8 | game_total | 0.221 | 0.255 | 0.248 | 26 | 75 | no | +0.016 | OK |
| KXNHLGAME-26NOV12TBCBJ-CBJ | game_winner | 0.457 | 0.495 | 0.487 | 50 | 51 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV12NYILA-NYI3 | game_spread | 0.126 | 0.160 | 0.153 | 17 | 85 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV12MTLBOS-3 | game_total | 0.953 | 0.975 | 0.972 | 98 | 3 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12TBCBJ-TB2 | team_total | 0.806 | 0.840 | 0.834 | 85 | 17 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV12COLOTT-COL6 | team_total | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV12MINTOR-TOR4 | team_total | 0.360 | 0.320 | 0.328 | 33 | 69 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV12STLUTA-UTA5 | team_total | 0.214 | 0.185 | 0.191 | 19 | 82 | yes | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ BOS | 0.583 | 0.590 | 0.179 | 0.209 | 5.91 | 6.65 | 0.956/0.983 | KXNHLTOTAL-26NOV12MTLBOS-7 +0.122 |
| MIN @ TOR | 0.430 | 0.505 | 0.172 | 0.217 | 6.43 | 6.46 | 0.956/0.995 | KXNHLGAME-26NOV12MINTOR-MIN -0.075 |
| COL @ OTT | 0.457 | 0.505 | 0.175 | 0.216 | 6.40 | 6.39 | 0.968/0.977 | KXNHLSPREAD-26NOV12COLOTT-COL2 -0.049 |
| WSH @ NJD | 0.557 | 0.556 | 0.175 | 0.216 | 6.17 | 6.31 | 0.959/0.961 | KXNHLTOTAL-26NOV12WSHNJ-7 +0.032 |
| TBL @ CBJ | 0.457 | 0.523 | 0.179 | 0.223 | 5.88 | 6.09 | 0.947/0.974 | KXNHLTEAMTOTAL-26NOV12TBCBJ-CBJ3 +0.071 |
| DET @ FLA | 0.573 | 0.576 | 0.176 | 0.220 | 6.08 | 6.26 | 0.992/1.015 | KXNHLTOTAL-26NOV12DETFLA-7 +0.035 |
| BUF @ CHI | 0.454 | 0.484 | 0.182 | 0.220 | 5.94 | 6.22 | 0.990/0.989 | KXNHLTEAMTOTAL-26NOV12BUFCHI-CHI3 +0.058 |
| WPG @ DAL | 0.600 | 0.586 | 0.184 | 0.209 | 5.77 | 6.12 | 0.994/1.001 | KXNHLTOTAL-26NOV12WPGDAL-7 +0.061 |
| STL @ UTA | 0.511 | 0.532 | 0.172 | 0.220 | 6.17 | 6.40 | 0.993/0.993 | KXNHLTEAMTOTAL-26NOV12STLUTA-UTA4 +0.044 |
| NYI @ LAK | 0.554 | 0.551 | 0.185 | 0.221 | 5.66 | 5.99 | 0.990/0.956 | KXNHLTOTAL-26NOV12NYILA-5 +0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- William Borgen: 1+ goals YES @ 5c · p 0.0884 (adj 0.0776) · $2.41 · thesis BOS:WINS_BY_2PLUS
- Nikita Zadorov: 1+ goals YES @ 4c · p 0.0665 (adj 0.0586) · $1.59 · thesis BOS:OFFENSE_4PLUS
- Tanner Jeannot: 1+ goals YES @ 8c · p 0.1141 (adj 0.1043) · $2.11 · thesis BOS:OFFENSE_4PLUS
- Cole Caufield: 1+ goals NO @ 61c · p 0.65 (adj 0.6388) · $3.54 · thesis MTL:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 9c · p 0.1764 (adj 0.1535) · $5.83 · thesis TOR:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6284 (adj 0.6038) · $8.98 · thesis MIN:SUPPRESSED
- Easton Cowan: 1+ goals YES @ 18c · p 0.2428 (adj 0.2258) · $4.36 · thesis TOR:OFFENSE_4PLUS
- Jordan Spence: 1+ goals YES @ 6c · p 0.0885 (adj 0.0801) · $1.73 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.2036 (adj 0.1902) · $2.65 · thesis OTT:OFFENSE_4PLUS
- Hayden Hodgson: 1+ goals YES @ 7c · p 0.0959 (adj 0.0869) · $1.36 · thesis OTT:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.169 (adj 0.1555) · $3.38 · thesis NJD:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2243 (adj 0.2082) · $3.69 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 17c · p 0.2112 (adj 0.1996) · $2.6 · thesis WSH:OFFENSE_4PLUS
- Anthony Beauvillier: 1+ goals YES @ 10c · p 0.1291 (adj 0.1206) · $1.65 · thesis WSH:OFFENSE_4PLUS
- Yanni Gourde: 1+ goals NO @ 86c · p 0.9002 (adj 0.8889) · $8.98 · thesis TBL:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 18c · p 0.2133 (adj 0.2037) · $2.02 · thesis CBJ:WINS_BY_2PLUS
- Cole Sillinger: 1+ goals YES @ 15c · p 0.1798 (adj 0.1711) · $1.7 · thesis CBJ:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 40c · p 0.4629 (adj 0.4289) · $2.95 · thesis GAME:LOW_EVENT
- Cole Schwindt: 1+ goals YES @ 8c · p 0.1066 (adj 0.0987) · $1.59 · thesis FLA:OFFENSE_4PLUS
- J.T. Compher: 1+ goals YES @ 13c · p 0.1605 (adj 0.1516) · $1.71 · thesis DET:OFFENSE_4PLUS
- Sam Bennett: 1+ goals YES @ 27c · p 0.3082 (adj 0.2974) · $2.2 · thesis FLA:OFFENSE_4PLUS
- Anton Lundell: 1+ assists NO @ 74c · p 0.8018 (adj 0.7659) · $6.74 · thesis FLA:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 24c · p 0.2868 (adj 0.2738) · $2.91 · thesis CHI:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 60c · p 0.6527 (adj 0.6383) · $5.57 · thesis BUF:SUPPRESSED
- Rasmus Dahlin: 1+ goals NO @ 80c · p 0.8362 (adj 0.8259) · $7.91 · thesis BUF:SUPPRESSED
- Buffalo wins by over 1.5 goals NO @ 64c · p 0.7081 (adj 0.6715) · $2.23 · thesis CHI:WINS
- Josh Morrissey: 1+ assists NO @ 60c · p 0.7432 (adj 0.6436) · $8.98 · thesis WPG:SUPPRESSED
- Arttu Hyry: 1+ goals YES @ 14c · p 0.1787 (adj 0.1678) · $2.33 · thesis DAL:OFFENSE_4PLUS
- Jamie Benn: 1+ goals YES @ 16c · p 0.1996 (adj 0.1885) · $2.48 · thesis DAL:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 27c · p 0.318 (adj 0.3048) · $3.17 · thesis DAL:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 18c · p 0.2462 (adj 0.2284) · $4.97 · thesis UTA:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 14c · p 0.1824 (adj 0.1693) · $2.58 · thesis UTA:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.162 (adj 0.1527) · $1.77 · thesis STL:OFFENSE_4PLUS
- Daniil But: 1+ goals NO @ 81c · p 0.8462 (adj 0.8359) · $8.98 · thesis UTA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 65c · p 0.8509 (adj 0.7171) · $8.98 · thesis LAK:SUPPRESSED
- Andre Lee: 1+ goals YES @ 9c · p 0.1318 (adj 0.1188) · $2.7 · thesis LAK:OFFENSE_4PLUS
- Mats Zuccarello: 2+ assists NO @ 94c · p 0.9887 (adj 0.9568) · $8.98 · thesis DIFFUSE
- Erik Haula: 1+ goals YES @ 15c · p 0.1784 (adj 0.1701) · $1.64 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ BOS** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 26.96, exp saves 23.58 (sd 6.49), pull risk 0.057
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.11, exp saves 23.81 (sd 6.8), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.352 | 0.495 | 51/52 | +0.111 | STANDARD |
| Nick Suzuki: 1+ points | 0.544 | 0.640 | 65/37 | +0.070 | STANDARD |
| Nick Suzuki: 2+ points | 0.186 | 0.275 | 29/74 | +0.061 | STANDARD |
| Fraser Minten: 1+ points | 0.464 | 0.375 | 38/63 | +0.067 | STANDARD |
| Nick Suzuki: 2+ assists | 0.069 | 0.155 | 17/86 | +0.063 | STANDARD |
| Fraser Minten: 1+ assists | 0.307 | 0.225 | 23/78 | +0.065 | STANDARD |

**MIN @ TOR** · priced 154/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.08, exp saves 26.9 (sd 7.18), pull risk 0.063
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 27.87, exp saves 23.93 (sd 6.63), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Easton Cowan: 1+ points | 0.546 | 0.405 | 41/60 | +0.119 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.263 | 0.400 | 41/61 | +0.110 | STANDARD |
| Easton Cowan: 1+ assists | 0.403 | 0.275 | 28/73 | +0.109 | STANDARD |
| Quinn Hughes: 1+ assists | 0.551 | 0.655 | 66/35 | +0.083 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.633 | 0.735 | 74/27 | +0.083 | STANDARD |
| Matt Boldy: 2+ points | 0.235 | 0.335 | 34/67 | +0.079 | STANDARD |

**COL @ OTT** · priced 176/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (CONFIRMED) exp shots 28.4, exp saves 24.61 (sd 6.7), pull risk 0.062
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 27.05, exp saves 23.47 (sd 6.36), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 1+ assists | 0.464 | 0.555 | 57/46 | +0.059 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.287 | 0.205 | 21/80 | +0.065 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.444 | 0.365 | 38/65 | +0.047 | STANDARD |
| Martin Necas: 1+ assists | 0.412 | 0.490 | 50/52 | +0.050 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.298 | 0.370 | 38/64 | +0.046 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.659 | 0.730 | 74/28 | +0.047 | STANDARD |

**WSH @ NJD** · priced 158/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 25.32, exp saves 22.03 (sd 6.08), pull risk 0.058
- WSH net: Logan Thompson (PROJECTED) exp shots 30.42, exp saves 26.06 (sd 7.15), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.297 | 0.370 | 38/64 | +0.047 | STANDARD |
| Jack Hughes: 1+ assists | 0.458 | 0.530 | 54/48 | +0.044 | STANDARD |
| Luke Evangelista: 1+ assists | 0.272 | 0.340 | 35/67 | +0.043 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.309 | 0.375 | 38/63 | +0.045 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.224 | 0.160 | 17/85 | +0.044 | STANDARD |
| Arseny Gritsyuk: 1+ points | 0.496 | 0.435 | 44/57 | +0.039 | STANDARD |

**TBL @ CBJ** · priced 164/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (CONFIRMED) exp shots 27.7, exp saves 24.15 (sd 6.58), pull risk 0.054
- TBL net: Dennis Hildeby (PROJECTED) exp shots 26.39, exp saves 22.76 (sd 6.33), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.433 | 0.590 | 60/42 | +0.130 | STANDARD |
| Nikita Kucherov: 2+ points | 0.257 | 0.390 | 40/62 | +0.107 | STANDARD |
| Nikita Kucherov: 1+ points | 0.622 | 0.740 | 75/27 | +0.094 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.111 | 0.220 | 23/79 | +0.087 | STANDARD |
| Nikita Kucherov: 3+ points | 0.078 | 0.155 | 17/86 | +0.053 | STANDARD |
| Yanni Gourde: 1+ points | 0.253 | 0.330 | 35/69 | +0.042 | STANDARD |

**DET @ FLA** · priced 161/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (CONFIRMED) exp shots 27.02, exp saves 23.58 (sd 6.37), pull risk 0.052
- DET net: Daniil Tarasov (PROJECTED) exp shots 27.83, exp saves 23.78 (sd 6.68), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matthew Tkachuk: 1+ assists | 0.480 | 0.560 | 57/45 | +0.053 | STANDARD |
| Lucas Raymond: 1+ assists | 0.351 | 0.430 | 44/58 | +0.052 | STANDARD |
| Anton Lundell: 1+ assists | 0.198 | 0.270 | 28/74 | +0.048 | STANDARD |
| Aaron Ekblad: 1+ assists | 0.331 | 0.260 | 27/75 | +0.047 | STANDARD |
| Moritz Seider: 1+ assists | 0.367 | 0.435 | 45/58 | +0.035 | STANDARD |
| Aaron Ekblad: 1+ points | 0.392 | 0.325 | 34/69 | +0.036 | STANDARD |

**BUF @ CHI** · priced 161/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 29.67, exp saves 25.66 (sd 6.84), pull risk 0.063
- BUF net: Alex Lyon (PROJECTED) exp shots 25.13, exp saves 21.69 (sd 6.06), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ points | 0.518 | 0.630 | 64/38 | +0.086 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.422 | 0.530 | 54/48 | +0.081 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.169 | 0.265 | 28/75 | +0.068 | STANDARD |
| Tage Thompson: 1+ points | 0.564 | 0.655 | 66/35 | +0.070 | STANDARD |
| Ryan Donato: 1+ assists | 0.270 | 0.185 | 19/82 | +0.069 | STANDARD |
| Tage Thompson: 2+ points | 0.209 | 0.290 | 30/72 | +0.057 | STANDARD |

**WPG @ DAL** · priced 159/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.62, exp saves 21.66 (sd 6.03), pull risk 0.048
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.72, exp saves 22.89 (sd 6.34), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Morrissey: 1+ assists | 0.257 | 0.410 | 42/60 | +0.126 | STANDARD |
| Josh Morrissey: 1+ points | 0.337 | 0.470 | 48/54 | +0.106 | STANDARD |
| Josh Morrissey: 2+ points | 0.062 | 0.145 | 15/86 | +0.070 | STANDARD |
| Mikko Rantanen: 2+ points | 0.243 | 0.320 | 33/69 | +0.052 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.453 | 0.530 | 54/48 | +0.050 | STANDARD |
| Josh Morrissey: 2+ assists | 0.036 | 0.105 | 12/91 | +0.049 | STANDARD |

**STL @ UTA** · priced 169/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.26), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.65, exp saves 24.64 (sd 6.73), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ points | 0.450 | 0.335 | 34/67 | +0.094 | STANDARD |
| Jack McBain: 1+ points | 0.387 | 0.275 | 29/74 | +0.083 | STANDARD |
| Robert Thomas: 1+ assists | 0.431 | 0.535 | 54/47 | +0.082 | STANDARD |
| Nick Schmaltz: 1+ goals | 0.325 | 0.225 | 29/84 | +0.021 | STANDARD |
| Clayton Keller: 1+ assists | 0.478 | 0.575 | 58/43 | +0.075 | STANDARD |
| MacKenzie Weegar: 1+ assists | 0.367 | 0.285 | 29/72 | +0.062 | STANDARD |

**NYI @ LAK** · priced 136/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 26.98, exp saves 23.62 (sd 6.37), pull risk 0.047
- NYI net: Ilya Sorokin (PROJECTED) exp shots 28.46, exp saves 24.61 (sd 6.69), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.149 | 0.355 | 36/65 | +0.185 | STANDARD |
| Mats Zuccarello: 1+ points | 0.313 | 0.470 | 48/54 | +0.130 | STANDARD |
| Mats Zuccarello: 2+ points | 0.058 | 0.150 | 17/87 | +0.064 | STANDARD |
| Alex Laferriere: 1+ points | 0.608 | 0.530 | 54/48 | +0.050 | STANDARD |
| Alex Laferriere: 1+ assists | 0.431 | 0.365 | 37/64 | +0.045 | STANDARD |
| Mats Zuccarello: 2+ assists | 0.011 | 0.075 | 9/94 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
