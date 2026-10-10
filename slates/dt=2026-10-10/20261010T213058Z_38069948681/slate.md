# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T21:30:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 11 · markets on board: 4722 · contracts joined: 2499 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2224, 'OK': 166, 'NO_EDGE': 109}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 370, 'game_early_goal': 11, 'first_goal': 394, 'game_winner': 22, 'player_goals': 697, 'game_overtime': 11, 'player_points': 461, 'goalie_saves': 16, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ FLA | 2026-10-10T22:00:00Z | T-10m | 0.459 | 0.541 | 0.175 | 6.28 | 3.02 | 3.26 | 221 (25/196) | CONFIRMED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-60m | 0.539 | 0.461 | 0.174 | 6.31 | 3.27 | 3.04 | 222 (25/197) | PROBABLE/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-60m | 0.603 | 0.398 | 0.174 | 6.20 | 3.41 | 2.78 | 265 (25/240) | CONFIRMED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-60m | 0.572 | 0.428 | 0.166 | 6.51 | 3.49 | 3.03 | 220 (25/195) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-60m | 0.456 | 0.544 | 0.174 | 6.41 | 3.06 | 3.35 | 209 (25/184) | CONFIRMED/CONFIRMED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-60m | 0.401 | 0.599 | 0.176 | 5.97 | 2.68 | 3.29 | 214 (25/189) | PROBABLE/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-60m | 0.470 | 0.530 | 0.175 | 6.20 | 3.00 | 3.20 | 218 (25/193) | CONFIRMED/CONFIRMED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-60m | 0.716 | 0.284 | 0.146 | 6.79 | 4.14 | 2.65 | 228 (25/203) | CONFIRMED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-90m | 0.493 | 0.507 | 0.188 | 5.49 | 2.74 | 2.75 | 208 (25/183) | CONFIRMED/PROBABLE |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-3h | 0.477 | 0.523 | 0.179 | 6.32 | 3.09 | 3.23 | 237 (25/212) | CONFIRMED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-3h | 0.621 | 0.379 | 0.171 | 6.09 | 3.44 | 2.65 | 257 (25/232) | PROJECTED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.309 | 0.445 | 0.416 | 45 | 56 | no | +0.114 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.527 | 0.655 | 0.631 | 66 | 35 | no | +0.107 | OK |
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.493 | 0.375 | 0.398 | 38 | 63 | yes | +0.097 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.270 | 0.385 | 0.360 | 39 | 62 | no | +0.094 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.507 | 0.615 | 0.594 | 62 | 39 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.150 | 0.255 | 0.231 | 26 | 75 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.367 | 0.475 | 0.453 | 48 | 53 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.230 | 0.335 | 0.312 | 34 | 67 | no | +0.085 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.599 | 0.695 | 0.677 | 70 | 31 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.401 | 0.305 | 0.323 | 31 | 70 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.756 | 0.850 | 0.834 | 86 | 16 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.430 | 0.525 | 0.506 | 53 | 48 | no | +0.072 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.456 | 0.365 | 0.383 | 37 | 64 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.236 | 0.155 | 0.169 | 16 | 85 | yes | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.420 | 0.335 | 0.351 | 34 | 67 | yes | +0.064 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.459 | 0.545 | 0.528 | 55 | 46 | no | +0.064 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.541 | 0.455 | 0.472 | 46 | 55 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.641 | 0.555 | 0.573 | 56 | 45 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.148 | 0.235 | 0.215 | 25 | 78 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.270 | 0.195 | 0.209 | 20 | 81 | yes | +0.059 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.544 | 0.625 | 0.609 | 63 | 38 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.613 | 0.535 | 0.551 | 54 | 47 | yes | +0.055 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.316 | 0.245 | 0.258 | 25 | 76 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.674 | 0.745 | 0.732 | 75 | 26 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.305 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.499 | 0.425 | 0.440 | 43 | 58 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.235 | 0.310 | 0.294 | 32 | 70 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.149 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.370 | 0.300 | 0.313 | 31 | 71 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.240 | 0.305 | 0.291 | 31 | 70 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.438 | 0.505 | 0.491 | 51 | 50 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.651 | 0.715 | 0.703 | 72 | 29 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.777 | 0.835 | 0.824 | 84 | 17 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.332 | 0.395 | 0.382 | 40 | 61 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.221 | 0.165 | 0.175 | 17 | 84 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.588 | 0.520 | 0.534 | 53 | 49 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL2 | game_spread | 0.255 | 0.315 | 0.302 | 32 | 69 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.374 | 0.435 | 0.423 | 44 | 57 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.506 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.326 | 0.385 | 0.373 | 39 | 62 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.196 | 0.140 | 0.150 | 15 | 87 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB6 | team_total | 0.057 | 0.105 | 0.093 | 11 | 90 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.195 | 0.145 | 0.154 | 15 | 86 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN6 | team_total | 0.110 | 0.065 | 0.072 | 7 | 94 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.511 | 0.455 | 0.466 | 46 | 55 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.204 | 0.255 | 0.244 | 26 | 75 | no | +0.033 | OK |
| KXNHLGAME-26OCT10CBJSTL-CBJ | game_winner | 0.530 | 0.475 | 0.486 | 48 | 53 | yes | +0.033 | OK |
| KXNHLGAME-26OCT10CBJSTL-STL | game_winner | 0.470 | 0.525 | 0.514 | 53 | 48 | no | +0.033 | OK |
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.398 | 0.345 | 0.355 | 35 | 66 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL3 | game_spread | 0.148 | 0.195 | 0.185 | 20 | 81 | no | +0.031 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.716 | 0.665 | 0.675 | 67 | 34 | yes | +0.030 | OK |
| KXNHLGAME-26OCT10TORCOL-TOR | game_winner | 0.284 | 0.335 | 0.325 | 34 | 67 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2 | team_total | 0.832 | 0.780 | 0.791 | 79 | 23 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.293 | 0.240 | 0.250 | 25 | 77 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT10TBNYI-8 | game_total | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT10MINFLA-8 | game_total | 0.271 | 0.225 | 0.234 | 23 | 78 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.595 | 0.545 | 0.555 | 55 | 46 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.248 | 0.205 | 0.213 | 21 | 80 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI3 | game_spread | 0.154 | 0.115 | 0.122 | 12 | 89 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-CBJ2 | game_spread | 0.310 | 0.265 | 0.274 | 27 | 74 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT10TORCOL-TOR2 | game_spread | 0.134 | 0.175 | 0.166 | 18 | 83 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT10MINFLA-9 | game_total | 0.194 | 0.155 | 0.162 | 16 | 85 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL5 | team_total | 0.262 | 0.310 | 0.300 | 32 | 70 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-5 | game_total | 0.805 | 0.765 | 0.773 | 77 | 24 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-10 | game_total | 0.107 | 0.075 | 0.081 | 8 | 93 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5 | team_total | 0.139 | 0.105 | 0.111 | 11 | 90 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ4 | team_total | 0.408 | 0.365 | 0.374 | 37 | 64 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH6 | team_total | 0.086 | 0.055 | 0.060 | 6 | 95 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT10MINFLA-7 | game_total | 0.459 | 0.415 | 0.424 | 42 | 59 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT5 | team_total | 0.202 | 0.160 | 0.168 | 17 | 85 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR2 | team_total | 0.840 | 0.880 | 0.873 | 89 | 13 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL3 | team_total | 0.674 | 0.715 | 0.707 | 72 | 29 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR6 | team_total | 0.110 | 0.150 | 0.141 | 16 | 86 | no | +0.021 | OK |
| KXNHLGAME-26OCT10DETMTL-MTL | game_winner | 0.603 | 0.645 | 0.637 | 65 | 36 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2 | team_total | 0.736 | 0.695 | 0.703 | 70 | 31 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT10UTABUF-UTA2 | game_spread | 0.254 | 0.295 | 0.287 | 30 | 71 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL3 | game_spread | 0.367 | 0.325 | 0.333 | 33 | 68 | yes | +0.021 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ FLA | 0.459 | 0.467 | 0.175 | 0.218 | 6.28 | 6.44 | 1.014/0.995 | KXNHLTOTAL-26OCT10MINFLA-7 +0.034 |
| UTA @ BUF | 0.539 | 0.512 | 0.174 | 0.215 | 6.31 | 6.46 | 0.999/0.992 | KXNHLTEAMTOTAL-26OCT10UTABUF-UTA3 +0.036 |
| DET @ MTL | 0.603 | 0.608 | 0.174 | 0.217 | 6.20 | 6.39 | 0.983/1.023 | KXNHLTOTAL-26OCT10DETMTL-7 +0.032 |
| NSH @ OTT | 0.572 | 0.597 | 0.166 | 0.206 | 6.51 | 6.38 | 0.998/1.000 | KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 -0.034 |
| DAL @ PIT | 0.456 | 0.506 | 0.174 | 0.217 | 6.41 | 6.47 | 1.042/0.994 | KXNHLGAME-26OCT10DALPIT-DAL -0.050 |
| CAR @ CHI | 0.401 | 0.415 | 0.176 | 0.214 | 5.97 | 6.38 | 0.995/0.989 | KXNHLTOTAL-26OCT10CARCHI-7 +0.068 |
| CBJ @ STL | 0.470 | 0.540 | 0.175 | 0.221 | 6.20 | 6.08 | 1.032/0.946 | KXNHLGAME-26OCT10CBJSTL-CBJ -0.070 |
| TOR @ COL | 0.716 | 0.677 | 0.146 | 0.195 | 6.79 | 6.58 | 0.978/0.965 | KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 -0.054 |
| TBL @ NYI | 0.493 | 0.509 | 0.188 | 0.225 | 5.49 | 5.95 | 0.947/0.951 | KXNHLTOTAL-26OCT10TBNYI-6 +0.081 |
| ANA @ CGY | 0.477 | 0.496 | 0.179 | 0.219 | 6.32 | 6.53 | 1.005/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.621 | 0.597 | 0.171 | 0.226 | 6.09 | 5.96 | 1.003/0.993 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.034 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 42 recommended · full analysis in card.md / packet.json `thesis_card`

- Yakov Trenin: 1+ goals YES @ 7c · p 0.137 (adj 0.119) · $3.23 · thesis MIN:OFFENSE_4PLUS
- Nico Sturm: 1+ goals YES @ 6c · p 0.1042 (adj 0.0919) · $2.08 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 8c · p 0.1272 (adj 0.1142) · $2.25 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1499 (adj 0.1362) · $2.46 · thesis FLA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 17c · p 0.223 (adj 0.2085) · $2.81 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8164 (adj 0.7245) · $6.62 · thesis UTA:SUPPRESSED
- Justin Danforth: 1+ goals YES @ 10c · p 0.1305 (adj 0.1216) · $1.33 · thesis BUF:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1518 (adj 0.1426) · $1.41 · thesis UTA:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 7c · p 0.1067 (adj 0.0963) · $1.73 · thesis DET:OFFENSE_4PLUS
- Emmitt Finnie: 1+ goals YES @ 16c · p 0.2008 (adj 0.1881) · $1.7 · thesis DET:OFFENSE_4PLUS
- Andrew Copp: 1+ goals YES @ 15c · p 0.1848 (adj 0.1749) · $1.55 · thesis DET:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 69c · p 0.7642 (adj 0.7246) · $6.07 · thesis MTL:SUPPRESSED
- Warren Foegele: 1+ goals YES @ 11c · p 0.1865 (adj 0.1661) · $4.02 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.212 (adj 0.194) · $3.15 · thesis OTT:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 22c · p 0.2793 (adj 0.2632) · $3.23 · thesis NSH:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1498 (adj 0.1386) · $1.89 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1539 (adj 0.1392) · $2.6 · thesis PIT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3264 (adj 0.3085) · $3.58 · thesis PIT:OFFENSE_4PLUS
- Roope Hintz: 1+ assists NO @ 56c · p 0.7075 (adj 0.6084) · $6.13 · thesis DAL:SUPPRESSED
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8261 (adj 0.7855) · $4.26 · thesis PIT:WINS
- Ryan Greene: 1+ goals YES @ 14c · p 0.1987 (adj 0.1828) · $3.03 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.326 (adj 0.3083) · $3.8 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 65c · p 0.7211 (adj 0.7021) · $6.62 · thesis CAR:SUPPRESSED
- Ryan Donato: 1+ goals YES @ 13c · p 0.177 (adj 0.164) · $2.23 · thesis CHI:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 83c · p 0.8875 (adj 0.8719) · $6.62 · thesis CBJ:SUPPRESSED
- Ross Johnston: 1+ goals YES @ 6c · p 0.0832 (adj 0.0774) · $1.13 · thesis STL:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2427 (adj 0.2308) · $1.98 · thesis CBJ:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 76c · p 0.8085 (adj 0.7951) · $6.01 · thesis COL:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1554 (adj 0.1441) · $1.26 · thesis COL:OFFENSE_4PLUS
- Nick Paul: 1+ goals NO @ 83c · p 0.8646 (adj 0.8547) · $6.01 · thesis TOR:SUPPRESSED
- Martin Necas: 1+ goals NO @ 63c · p 0.6748 (adj 0.6623) · $3.29 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 18c · p 0.2676 (adj 0.2445) · $5.06 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 53c · p 0.727 (adj 0.5957) · $6.43 · thesis TBL:SUPPRESSED
- Jake Guentzel: 1+ goals NO @ 67c · p 0.7164 (adj 0.7036) · $3.5 · thesis TBL:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 16c · p 0.2241 (adj 0.2056) · $3.31 · thesis ANA:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 14c · p 0.1953 (adj 0.1777) · $2.58 · thesis CGY:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 9c · p 0.1312 (adj 0.1197) · $1.93 · thesis ANA:OFFENSE_4PLUS
- Zayne Parekh: 1+ goals NO @ 85c · p 0.8813 (adj 0.8722) · $6.62 · thesis CGY:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0806 (adj 0.0717) · $1.36 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7523 (adj 0.7355) · $6.62 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6473 (adj 0.5483) · $5.64 · thesis LAK:SUPPRESSED
- Trevor Moore: 1+ assists YES @ 23c · p 0.3076 (adj 0.2613) · $1.94 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ FLA** · priced 165/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.41, exp saves 23.53 (sd 6.55), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.74), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.510 | 0.365 | 37/64 | +0.124 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.234 | 0.370 | 38/64 | +0.109 | STANDARD |
| Ryan Hartman: 1+ assists | 0.352 | 0.220 | 23/79 | +0.110 | STANDARD |
| Brady Tkachuk: 1+ points | 0.438 | 0.570 | 58/44 | +0.105 | STANDARD |
| Jared Spurgeon: 1+ assists | 0.342 | 0.210 | 26/84 | +0.069 | STANDARD |
| Brady Tkachuk: 2+ points | 0.118 | 0.220 | 24/80 | +0.071 | STANDARD |

**UTA @ BUF** · priced 162/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 26.66, exp saves 23.02 (sd 6.38), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.03 (sd 6.6), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 25+ saves | 0.466 | 0.295 | 50/91 | -0.052 |  |
| Vincent Trocheck: 1+ assists | 0.184 | 0.325 | 33/68 | +0.121 | STANDARD |
| Vincent Trocheck: 1+ points | 0.348 | 0.455 | 46/55 | +0.084 | STANDARD |
| Colten Ellis: 26+ saves | 0.345 | 0.250 | 44/94 | -0.112 |  |
| Josh Doan: 1+ assists | 0.324 | 0.230 | 25/79 | +0.061 | STANDARD |
| Zach Benson: 1+ points | 0.537 | 0.460 | 47/55 | +0.050 | STANDARD |

**DET @ MTL** · priced 194/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.75, exp saves 25.24 (sd 6.6), pull risk 0.048
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.95 (sd 6.31), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Josh Anderson: 1+ points | 0.384 | 0.175 | 33/98 | +0.038 | STANDARD |
| Jacob Fowler: 23+ saves | 0.663 | 0.475 | 51/56 | +0.136 |  |
| Ben Chiarot: 1+ points | 0.256 | 0.100 | 17/97 | +0.076 | STANDARD |
| Albert Johansson: 1+ assists | 0.205 | 0.060 | 11/99 | +0.089 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.270 | 0.125 | 23/98 | +0.027 | STANDARD |
| Albert Johansson: 1+ points | 0.242 | 0.100 | 16/96 | +0.072 | STANDARD |

**NSH @ OTT** · priced 163/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.09), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Juuse Saros: 27+ saves | 0.474 | 0.315 | 53/90 | -0.073 |  |
| Andre Burakovsky: 1+ points | 0.371 | 0.520 | 53/49 | +0.122 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.234 | 0.365 | 38/65 | +0.100 | STANDARD |
| Tim Stutzle: 1+ assists | 0.437 | 0.545 | 55/46 | +0.085 | STANDARD |
| Jordan Spence: 1+ points | 0.411 | 0.315 | 33/70 | +0.065 | STANDARD |
| Jordan Spence: 1+ assists | 0.349 | 0.265 | 27/74 | +0.065 | STANDARD |

**DAL @ PIT** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.55, exp saves 22.05 (sd 6.27), pull risk 0.066
- DAL net: Jake Oettinger (CONFIRMED) exp shots 26.81, exp saves 23.18 (sd 6.47), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.292 | 0.445 | 45/56 | +0.130 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.333 | 0.200 | 22/82 | +0.101 | STANDARD |
| Tyler Seguin: 1+ assists | 0.139 | 0.260 | 27/75 | +0.098 | STANDARD |
| Tyler Seguin: 1+ points | 0.326 | 0.435 | 45/58 | +0.077 | STANDARD |
| Jason Robertson: 2+ points | 0.248 | 0.355 | 37/66 | +0.076 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.419 | 0.525 | 53/48 | +0.084 | STANDARD |

**CAR @ CHI** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.13, exp saves 26.71 (sd 7.37), pull risk 0.078
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.55), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.485 | 49/52 | +0.122 | STANDARD |
| Sebastian Aho: 1+ points | 0.522 | 0.645 | 66/37 | +0.092 | STANDARD |
| Patrick Kane: 1+ assists | 0.292 | 0.415 | 42/59 | +0.101 | STANDARD |
| Sebastian Aho: 2+ points | 0.170 | 0.290 | 30/72 | +0.095 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.325 | 0.430 | 44/58 | +0.078 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.573 | 0.470 | 48/54 | +0.075 | STANDARD |

**CBJ @ STL** · priced 165/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.71, exp saves 24.07 (sd 6.6), pull risk 0.054
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.17, exp saves 22.42 (sd 6.22), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.272 | 0.400 | 41/61 | +0.102 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.217 | 0.330 | 34/68 | +0.087 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.421 | 0.525 | 53/48 | +0.081 | STANDARD |
| Jet Greaves: 24+ saves | 0.422 | 0.520 | 54/50 | +0.060 |  |
| Matthew Knies: 1+ assists | 0.266 | 0.355 | 36/65 | +0.068 | STANDARD |
| Charlie Coyle: 1+ points | 0.505 | 0.425 | 44/59 | +0.048 | STANDARD |

**TOR @ COL** · priced 175/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 24.57, exp saves 21.7 (sd 5.96), pull risk 0.048
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.64 (sd 8.14), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.349 | 0.470 | 48/54 | +0.093 | STANDARD |
| Cale Makar: 1+ assists | 0.477 | 0.595 | 60/41 | +0.096 | STANDARD |
| Cale Makar: 2+ points | 0.216 | 0.330 | 34/68 | +0.089 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.287 | 0.400 | 41/61 | +0.086 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.157 | 0.270 | 29/75 | +0.079 | STANDARD |
| Cale Makar: 1+ points | 0.578 | 0.690 | 70/32 | +0.087 | STANDARD |

**TBL @ NYI** · priced 147/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.71 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.5, exp saves 22.83 (sd 6.25), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.352 | 0.560 | 57/45 | +0.180 | STANDARD |
| John Carlson: 1+ assists | 0.273 | 0.475 | 48/53 | +0.180 | STANDARD |
| John Carlson: 2+ points | 0.069 | 0.210 | 22/80 | +0.120 | STANDARD |
| Brayden Schenn: 1+ points | 0.508 | 0.380 | 40/64 | +0.091 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.191 | 0.310 | 33/71 | +0.084 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.470 | 0.580 | 59/43 | +0.083 | STANDARD |

**ANA @ CGY** · priced 182/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.92, exp saves 26.73 (sd 7.25), pull risk 0.067
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.27 (sd 6.52), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.268 | 0.100 | 18/98 | +0.078 | STANDARD |
| Kevin Bahl: 1+ assists | 0.268 | 0.110 | 20/98 | +0.057 | STANDARD |
| Adam Klapka: 1+ assists | 0.247 | 0.110 | 20/98 | +0.036 | STANDARD |
| Noah Warren: 1+ assists | 0.202 | 0.080 | 14/98 | +0.053 | PRIOR_HEAVY |
| Yegor Sharangovich: 1+ assists | 0.330 | 0.210 | 23/81 | +0.088 | STANDARD |
| Leo Carlsson: 1+ assists | 0.389 | 0.500 | 51/51 | +0.083 | STANDARD |

**LAK @ VGK** · priced 202/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.03 (sd 6.3), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 28.34, exp saves 24.25 (sd 6.62), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.270 | 0.105 | 18/97 | +0.079 | STANDARD |
| Artemi Panarin: 1+ assists | 0.353 | 0.505 | 51/50 | +0.130 | STANDARD |
| Drew Doughty: 1+ points | 0.314 | 0.170 | 32/98 | -0.022 | STANDARD |
| Brayden McNabb: 1+ assists | 0.263 | 0.125 | 21/96 | +0.042 | STANDARD |
| Drew Doughty: 1+ assists | 0.272 | 0.140 | 24/96 | +0.019 | STANDARD |
| Joel Armia: 1+ points | 0.276 | 0.145 | 26/97 | +0.003 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
