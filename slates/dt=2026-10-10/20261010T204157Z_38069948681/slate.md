# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T20:41:57Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 11 · markets on board: 4741 · contracts joined: 2498 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2223, 'OK': 173, 'NO_EDGE': 102}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 370, 'game_early_goal': 11, 'first_goal': 394, 'game_winner': 22, 'player_goals': 697, 'game_overtime': 11, 'player_points': 461, 'goalie_saves': 15, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ FLA | 2026-10-10T22:00:00Z | T-60m | 0.463 | 0.537 | 0.177 | 6.28 | 3.02 | 3.26 | 221 (25/196) | CONFIRMED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-90m | 0.536 | 0.464 | 0.173 | 6.31 | 3.27 | 3.04 | 222 (25/197) | PROBABLE/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-90m | 0.602 | 0.398 | 0.173 | 6.20 | 3.41 | 2.79 | 265 (25/240) | CONFIRMED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-90m | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 220 (25/195) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-90m | 0.466 | 0.534 | 0.172 | 6.34 | 3.06 | 3.28 | 209 (25/184) | PROJECTED/CONFIRMED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-90m | 0.401 | 0.599 | 0.176 | 5.97 | 2.68 | 3.29 | 214 (25/189) | PROBABLE/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-90m | 0.468 | 0.532 | 0.174 | 6.20 | 3.00 | 3.20 | 218 (25/193) | CONFIRMED/CONFIRMED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-90m | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 227 (25/202) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-90m | 0.498 | 0.501 | 0.190 | 5.49 | 2.74 | 2.75 | 208 (25/183) | CONFIRMED/PROBABLE |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-3h | 0.477 | 0.523 | 0.175 | 6.31 | 3.08 | 3.23 | 237 (25/212) | CONFIRMED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-3h | 0.622 | 0.378 | 0.171 | 6.09 | 3.44 | 2.65 | 257 (25/232) | PROJECTED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.307 | 0.445 | 0.416 | 45 | 56 | no | +0.115 | OK |
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.498 | 0.375 | 0.399 | 38 | 63 | yes | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.527 | 0.650 | 0.626 | 66 | 36 | no | +0.097 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.270 | 0.385 | 0.360 | 39 | 62 | no | +0.093 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.501 | 0.615 | 0.593 | 62 | 39 | no | +0.092 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.150 | 0.255 | 0.231 | 26 | 75 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.367 | 0.475 | 0.453 | 48 | 53 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.230 | 0.335 | 0.312 | 34 | 67 | no | +0.085 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.466 | 0.365 | 0.385 | 37 | 64 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.753 | 0.850 | 0.834 | 86 | 16 | no | +0.077 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.599 | 0.695 | 0.677 | 70 | 31 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.401 | 0.305 | 0.323 | 31 | 70 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.430 | 0.530 | 0.510 | 54 | 48 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.147 | 0.240 | 0.219 | 25 | 77 | no | +0.070 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.420 | 0.335 | 0.351 | 34 | 67 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.640 | 0.555 | 0.573 | 56 | 45 | yes | +0.063 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.463 | 0.545 | 0.529 | 55 | 46 | no | +0.060 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.537 | 0.455 | 0.471 | 46 | 55 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.238 | 0.160 | 0.174 | 17 | 85 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.321 | 0.245 | 0.259 | 25 | 76 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.535 | 0.551 | 54 | 47 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.425 | 0.440 | 43 | 58 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.674 | 0.745 | 0.732 | 75 | 26 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.149 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.300 | 0.314 | 31 | 71 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.437 | 0.505 | 0.491 | 51 | 50 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.652 | 0.715 | 0.703 | 72 | 29 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.780 | 0.835 | 0.825 | 84 | 17 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.197 | 0.255 | 0.243 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.334 | 0.395 | 0.382 | 40 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.374 | 0.435 | 0.423 | 44 | 57 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.165 | 0.175 | 17 | 84 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.506 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.260 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.586 | 0.520 | 0.533 | 53 | 49 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB6 | team_total | 0.057 | 0.105 | 0.093 | 11 | 90 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL2 | game_spread | 0.259 | 0.315 | 0.303 | 32 | 69 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.140 | 0.150 | 15 | 87 | yes | +0.035 | OK |
| KXNHLGAME-26OCT10CBJSTL-CBJ | game_winner | 0.532 | 0.475 | 0.486 | 48 | 53 | yes | +0.035 | OK |
| KXNHLGAME-26OCT10CBJSTL-STL | game_winner | 0.468 | 0.525 | 0.514 | 53 | 48 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN6 | team_total | 0.109 | 0.065 | 0.072 | 7 | 94 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL4 | team_total | 0.429 | 0.490 | 0.478 | 50 | 52 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL3 | team_total | 0.643 | 0.700 | 0.689 | 71 | 31 | no | +0.032 | OK |
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.398 | 0.345 | 0.355 | 35 | 66 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT10TBNYI-8 | game_total | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.293 | 0.240 | 0.250 | 25 | 77 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 | team_total | 0.405 | 0.355 | 0.365 | 36 | 65 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2 | team_total | 0.831 | 0.780 | 0.791 | 79 | 23 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL3 | game_spread | 0.150 | 0.195 | 0.185 | 20 | 81 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-CBJ2 | game_spread | 0.312 | 0.265 | 0.274 | 27 | 74 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.595 | 0.545 | 0.555 | 55 | 46 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT10MINFLA-8 | game_total | 0.269 | 0.225 | 0.233 | 23 | 78 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH2 | team_total | 0.799 | 0.750 | 0.760 | 76 | 26 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.457 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT10MINFLA-6 | game_total | 0.573 | 0.525 | 0.535 | 53 | 48 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI3 | game_spread | 0.153 | 0.115 | 0.122 | 12 | 89 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL5 | team_total | 0.260 | 0.310 | 0.300 | 32 | 70 | no | +0.025 | OK |
| KXNHLGAME-26OCT10TORCOL-TOR | game_winner | 0.290 | 0.335 | 0.326 | 34 | 67 | no | +0.025 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.710 | 0.665 | 0.674 | 67 | 34 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-10 | game_total | 0.109 | 0.075 | 0.081 | 8 | 93 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-5 | game_total | 0.806 | 0.765 | 0.774 | 77 | 24 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH6 | team_total | 0.086 | 0.055 | 0.060 | 6 | 95 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT10MINFLA-7 | game_total | 0.459 | 0.415 | 0.424 | 42 | 59 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT10TORCOL-TOR2 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT10TBNYI-9 | game_total | 0.110 | 0.145 | 0.137 | 15 | 86 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR2 | team_total | 0.840 | 0.880 | 0.873 | 89 | 13 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2 | team_total | 0.736 | 0.695 | 0.704 | 70 | 31 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI5 | team_total | 0.139 | 0.105 | 0.111 | 11 | 90 | yes | +0.022 | OK |
| KXNHLGAME-26OCT10DETMTL-MTL | game_winner | 0.602 | 0.645 | 0.637 | 65 | 36 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-OTT6 | team_total | 0.139 | 0.105 | 0.111 | 11 | 90 | yes | +0.022 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ FLA | 0.463 | 0.467 | 0.177 | 0.218 | 6.28 | 6.44 | 1.014/0.995 | KXNHLTOTAL-26OCT10MINFLA-7 +0.034 |
| UTA @ BUF | 0.536 | 0.512 | 0.173 | 0.215 | 6.31 | 6.46 | 0.999/0.992 | KXNHLTEAMTOTAL-26OCT10UTABUF-UTA3 +0.034 |
| DET @ MTL | 0.602 | 0.608 | 0.173 | 0.217 | 6.20 | 6.39 | 0.983/1.023 | KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 +0.032 |
| NSH @ OTT | 0.567 | 0.597 | 0.170 | 0.206 | 6.52 | 6.38 | 0.998/1.000 | KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 -0.037 |
| DAL @ PIT | 0.466 | 0.507 | 0.172 | 0.218 | 6.34 | 6.45 | 1.033/0.994 | KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 +0.048 |
| CAR @ CHI | 0.401 | 0.415 | 0.176 | 0.214 | 5.97 | 6.38 | 0.995/0.989 | KXNHLTOTAL-26OCT10CARCHI-7 +0.068 |
| CBJ @ STL | 0.468 | 0.540 | 0.174 | 0.221 | 6.20 | 6.08 | 1.032/0.946 | KXNHLGAME-26OCT10CBJSTL-CBJ -0.072 |
| TOR @ COL | 0.710 | 0.674 | 0.145 | 0.194 | 6.82 | 6.58 | 0.976/0.965 | KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 -0.057 |
| TBL @ NYI | 0.498 | 0.509 | 0.190 | 0.225 | 5.49 | 5.95 | 0.947/0.951 | KXNHLTOTAL-26OCT10TBNYI-6 +0.081 |
| ANA @ CGY | 0.477 | 0.496 | 0.175 | 0.219 | 6.31 | 6.53 | 1.005/1.035 | KXNHLTEAMTOTAL-26OCT10ANACGY-CGY3 +0.043 |
| LAK @ VGK | 0.622 | 0.597 | 0.171 | 0.226 | 6.09 | 5.96 | 1.003/0.993 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Yakov Trenin: 1+ goals YES @ 7c · p 0.137 (adj 0.119) · $3.28 · thesis MIN:OFFENSE_4PLUS
- Nico Sturm: 1+ goals YES @ 6c · p 0.1042 (adj 0.0919) · $2.11 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 8c · p 0.1272 (adj 0.1142) · $2.29 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1499 (adj 0.1362) · $2.5 · thesis FLA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8164 (adj 0.7245) · $6.74 · thesis UTA:SUPPRESSED
- Justin Danforth: 1+ goals YES @ 10c · p 0.1305 (adj 0.1216) · $1.33 · thesis BUF:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1518 (adj 0.1426) · $1.42 · thesis UTA:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 14c · p 0.1703 (adj 0.1615) · $1.19 · thesis BUF:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 7c · p 0.1067 (adj 0.0963) · $1.76 · thesis DET:OFFENSE_4PLUS
- Emmitt Finnie: 1+ goals YES @ 16c · p 0.2008 (adj 0.1881) · $1.73 · thesis DET:OFFENSE_4PLUS
- Andrew Copp: 1+ goals YES @ 15c · p 0.1848 (adj 0.1749) · $1.57 · thesis DET:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 69c · p 0.7642 (adj 0.7246) · $6.18 · thesis MTL:SUPPRESSED
- Warren Foegele: 1+ goals YES @ 12c · p 0.1865 (adj 0.1674) · $3.43 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.212 (adj 0.194) · $3.22 · thesis OTT:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 22c · p 0.2793 (adj 0.262) · $3.16 · thesis NSH:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1498 (adj 0.1386) · $1.92 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1532 (adj 0.1386) · $2.54 · thesis PIT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3304 (adj 0.3115) · $3.89 · thesis PIT:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8297 (adj 0.7873) · $6.56 · thesis PIT:WINS
- Evgeni Malkin: 1+ assists NO @ 60c · p 0.6662 (adj 0.6281) · $3.86 · thesis PIT:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 14c · p 0.1987 (adj 0.1828) · $3.08 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.326 (adj 0.3083) · $3.86 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 65c · p 0.7211 (adj 0.7021) · $6.74 · thesis CAR:SUPPRESSED
- Ryan Donato: 1+ goals YES @ 13c · p 0.177 (adj 0.164) · $2.27 · thesis CHI:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 84c · p 0.8875 (adj 0.8744) · $5.29 · thesis CBJ:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 65c · p 0.7336 (adj 0.6893) · $4.82 · thesis CBJ:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2427 (adj 0.2308) · $1.77 · thesis CBJ:OFFENSE_4PLUS
- Adam Jiricek: 1+ assists NO @ 68c · p 0.7825 (adj 0.7094) · $3.8 · thesis STL:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1694 (adj 0.1545) · $2.23 · thesis COL:OFFENSE_4PLUS
- Nathan MacKinnon: 2+ assists NO @ 75c · p 0.8379 (adj 0.7914) · $6.36 · thesis COL:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 61c · p 0.6996 (adj 0.6498) · $5.22 · thesis TOR:SUPPRESSED
- Martin Necas: 1+ goals NO @ 62c · p 0.6674 (adj 0.6543) · $3.04 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2676 (adj 0.2457) · $3.93 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 53c · p 0.727 (adj 0.5957) · $6.46 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 75c · p 0.8425 (adj 0.7937) · $6.46 · thesis NYI:WINS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2241 (adj 0.2056) · $3.37 · thesis ANA:OFFENSE_4PLUS
- Aydar Suniev: 1+ goals YES @ 15c · p 0.1953 (adj 0.179) · $1.86 · thesis CGY:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 10c · p 0.1312 (adj 0.1197) · $1.12 · thesis ANA:OFFENSE_4PLUS
- Morgan Frost: 1+ goals YES @ 26c · p 0.301 (adj 0.2895) · $1.78 · thesis CGY:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0806 (adj 0.0717) · $1.39 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7523 (adj 0.7355) · $6.74 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6473 (adj 0.5483) · $5.74 · thesis LAK:SUPPRESSED
- Trevor Moore: 1+ assists YES @ 23c · p 0.3076 (adj 0.2613) · $1.98 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ FLA** · priced 165/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.41, exp saves 23.53 (sd 6.55), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.74), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.510 | 0.365 | 38/65 | +0.114 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.234 | 0.370 | 38/64 | +0.109 | STANDARD |
| Ryan Hartman: 1+ assists | 0.352 | 0.220 | 23/79 | +0.110 | STANDARD |
| Brady Tkachuk: 1+ points | 0.438 | 0.565 | 58/45 | +0.095 | STANDARD |
| Brady Tkachuk: 2+ points | 0.118 | 0.215 | 23/80 | +0.071 | STANDARD |
| Sam Reinhart: 1+ points | 0.506 | 0.600 | 61/41 | +0.067 | STANDARD |

**UTA @ BUF** · priced 162/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 26.66, exp saves 23.02 (sd 6.38), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.03 (sd 6.6), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 25+ saves | 0.466 | 0.280 | 49/93 | -0.042 |  |
| Vincent Trocheck: 1+ assists | 0.184 | 0.325 | 33/68 | +0.121 | STANDARD |
| Vincent Trocheck: 1+ points | 0.348 | 0.455 | 46/55 | +0.084 | STANDARD |
| Colten Ellis: 26+ saves | 0.345 | 0.250 | 44/94 | -0.112 |  |
| Josh Doan: 1+ assists | 0.324 | 0.240 | 26/78 | +0.051 | STANDARD |
| Josh Doan: 1+ points | 0.491 | 0.415 | 42/59 | +0.054 | STANDARD |

**DET @ MTL** · priced 194/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.75, exp saves 25.24 (sd 6.6), pull risk 0.048
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.95 (sd 6.31), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.663 | 0.465 | 50/57 | +0.146 |  |
| Zachary Bolduc: 1+ points | 0.398 | 0.200 | 38/98 | +0.002 | STANDARD |
| Albert Johansson: 1+ points | 0.242 | 0.090 | 16/98 | +0.072 | STANDARD |
| Ben Chiarot: 1+ points | 0.256 | 0.105 | 17/96 | +0.076 | STANDARD |
| Emmitt Finnie: 1+ assists | 0.286 | 0.140 | 22/94 | +0.054 | STANDARD |
| Albert Johansson: 1+ assists | 0.205 | 0.060 | 11/99 | +0.089 | STANDARD |

**NSH @ OTT** · priced 163/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.09), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Juuse Saros: 27+ saves | 0.474 | 0.305 | 54/93 | -0.083 |  |
| Andre Burakovsky: 1+ points | 0.371 | 0.525 | 54/49 | +0.122 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.234 | 0.370 | 38/64 | +0.109 | STANDARD |
| Linus Ullmark: 23+ saves | 0.474 | 0.355 | 44/73 | +0.016 |  |
| Tim Stutzle: 1+ assists | 0.437 | 0.545 | 55/46 | +0.085 | STANDARD |
| Andre Burakovsky: 2+ points | 0.078 | 0.170 | 19/85 | +0.063 | STANDARD |

**DAL @ PIT** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.04 (sd 6.24), pull risk 0.065
- DAL net: Jake Oettinger (CONFIRMED) exp shots 26.81, exp saves 23.14 (sd 6.46), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.294 | 0.445 | 45/56 | +0.129 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.335 | 0.200 | 22/82 | +0.102 | STANDARD |
| Tyler Seguin: 1+ assists | 0.140 | 0.270 | 29/75 | +0.097 | STANDARD |
| Tyler Seguin: 1+ points | 0.328 | 0.440 | 46/58 | +0.075 | STANDARD |
| Jason Robertson: 2+ points | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Jason Robertson: 1+ assists | 0.386 | 0.495 | 51/52 | +0.077 | STANDARD |

**CAR @ CHI** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.13, exp saves 26.71 (sd 7.37), pull risk 0.078
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.55), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.485 | 49/52 | +0.122 | STANDARD |
| Sebastian Aho: 2+ points | 0.170 | 0.295 | 31/72 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.522 | 0.645 | 66/37 | +0.092 | STANDARD |
| Patrick Kane: 1+ assists | 0.292 | 0.415 | 42/59 | +0.101 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.573 | 0.465 | 47/54 | +0.085 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.325 | 0.430 | 44/58 | +0.078 | STANDARD |

**CBJ @ STL** · priced 165/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.71, exp saves 24.07 (sd 6.6), pull risk 0.054
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.17, exp saves 22.42 (sd 6.22), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.272 | 0.395 | 40/61 | +0.102 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.217 | 0.330 | 34/68 | +0.087 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.421 | 0.525 | 53/48 | +0.081 | STANDARD |
| Jet Greaves: 24+ saves | 0.422 | 0.525 | 55/50 | +0.060 |  |
| Matthew Knies: 1+ assists | 0.266 | 0.355 | 36/65 | +0.068 | STANDARD |
| Charlie Coyle: 1+ points | 0.505 | 0.425 | 44/59 | +0.048 | STANDARD |

**TOR @ COL** · priced 172/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.217 | 0.335 | 35/68 | +0.087 | STANDARD |
| Cale Makar: 1+ assists | 0.483 | 0.595 | 60/41 | +0.090 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.365 | 0.470 | 48/54 | +0.078 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.300 | 0.400 | 41/61 | +0.073 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.521 | 0.615 | 62/39 | +0.072 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.255 | 26/75 | +0.075 | STANDARD |

**TBL @ NYI** · priced 147/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.71 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.5, exp saves 22.83 (sd 6.25), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.352 | 0.560 | 57/45 | +0.180 | STANDARD |
| John Carlson: 1+ assists | 0.273 | 0.475 | 48/53 | +0.180 | STANDARD |
| John Carlson: 2+ points | 0.069 | 0.210 | 22/80 | +0.120 | STANDARD |
| Brayden Schenn: 1+ points | 0.508 | 0.385 | 40/63 | +0.091 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.191 | 0.305 | 32/71 | +0.084 | STANDARD |
| John Carlson: 2+ assists | 0.039 | 0.145 | 16/87 | +0.083 | STANDARD |

**ANA @ CGY** · priced 182/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.92, exp saves 26.73 (sd 7.25), pull risk 0.067
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.27 (sd 6.52), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Zach Whitecloud: 1+ assists | 0.268 | 0.100 | 18/98 | +0.078 | STANDARD |
| Kevin Bahl: 1+ assists | 0.268 | 0.105 | 19/98 | +0.067 | STANDARD |
| Adam Klapka: 1+ assists | 0.247 | 0.110 | 20/98 | +0.036 | STANDARD |
| Pavel Mintyukov: 1+ assists | 0.256 | 0.120 | 22/98 | +0.024 | STANDARD |
| Noah Warren: 1+ assists | 0.202 | 0.075 | 14/99 | +0.053 | PRIOR_HEAVY |
| Leo Carlsson: 1+ assists | 0.389 | 0.505 | 52/51 | +0.083 | STANDARD |

**LAK @ VGK** · priced 202/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.03 (sd 6.3), pull risk 0.046
- LAK net: Darcy Kuemper (PROBABLE) exp shots 28.34, exp saves 24.25 (sd 6.62), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.270 | 0.105 | 19/98 | +0.069 | STANDARD |
| Artemi Panarin: 1+ assists | 0.353 | 0.505 | 51/50 | +0.130 | STANDARD |
| Noah Hanifin: 1+ assists | 0.253 | 0.115 | 21/98 | +0.031 | STANDARD |
| Joel Armia: 1+ points | 0.276 | 0.140 | 26/98 | +0.003 | STANDARD |
| Joel Edmundson: 1+ assists | 0.220 | 0.085 | 16/99 | +0.051 | STANDARD |
| Mitch Marner: 1+ assists | 0.411 | 0.540 | 55/47 | +0.102 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
