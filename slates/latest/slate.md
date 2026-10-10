# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T19:49:00Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 12 · markets on board: 4818 · contracts joined: 2682 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2382, 'OK': 184, 'NO_EDGE': 116}
families: {'period_winner': 108, 'period_spread': 72, 'period_total': 108, 'player_assists': 403, 'game_early_goal': 12, 'first_goal': 428, 'game_winner': 24, 'player_goals': 759, 'game_overtime': 12, 'player_points': 464, 'goalie_saves': 16, 'game_spread': 48, 'team_total': 120, 'game_total': 108}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ SJS | 2026-10-10T20:00:00Z | T-10m | 0.439 | 0.561 | 0.162 | 7.11 | 3.34 | 3.77 | 221 (25/196) | CONFIRMED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-90m | 0.463 | 0.537 | 0.177 | 6.28 | 3.02 | 3.26 | 221 (25/196) | CONFIRMED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-3h | 0.536 | 0.464 | 0.173 | 6.31 | 3.27 | 3.04 | 222 (25/197) | PROBABLE/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-3h | 0.602 | 0.398 | 0.173 | 6.20 | 3.41 | 2.79 | 232 (25/207) | CONFIRMED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-3h | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 220 (25/195) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-3h | 0.466 | 0.534 | 0.172 | 6.34 | 3.06 | 3.28 | 209 (25/184) | PROJECTED/CONFIRMED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-3h | 0.401 | 0.599 | 0.176 | 5.97 | 2.68 | 3.29 | 214 (25/189) | PROBABLE/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-3h | 0.468 | 0.532 | 0.174 | 6.20 | 3.00 | 3.20 | 218 (25/193) | CONFIRMED/CONFIRMED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-3h | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 227 (25/202) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-3h | 0.498 | 0.501 | 0.190 | 5.49 | 2.74 | 2.75 | 208 (25/183) | CONFIRMED/PROBABLE |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-6h | 0.477 | 0.523 | 0.175 | 6.31 | 3.08 | 3.23 | 237 (25/212) | CONFIRMED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-6h | 0.617 | 0.383 | 0.169 | 6.07 | 3.41 | 2.65 | 253 (25/228) | PROJECTED/PROJECTED |

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
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.599 | 0.695 | 0.677 | 70 | 31 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.401 | 0.305 | 0.323 | 31 | 70 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.430 | 0.530 | 0.510 | 54 | 48 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.147 | 0.240 | 0.219 | 25 | 77 | no | +0.070 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.753 | 0.845 | 0.829 | 86 | 17 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.420 | 0.330 | 0.347 | 34 | 68 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.640 | 0.550 | 0.569 | 56 | 46 | yes | +0.063 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.463 | 0.545 | 0.529 | 55 | 46 | no | +0.060 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.537 | 0.455 | 0.471 | 46 | 55 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.238 | 0.160 | 0.174 | 17 | 85 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.321 | 0.245 | 0.259 | 25 | 76 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-9 | game_total | 0.300 | 0.225 | 0.239 | 23 | 78 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.535 | 0.551 | 54 | 47 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.425 | 0.440 | 43 | 58 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.674 | 0.745 | 0.732 | 75 | 26 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.149 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.586 | 0.515 | 0.529 | 52 | 49 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.300 | 0.314 | 31 | 71 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-10 | game_total | 0.164 | 0.105 | 0.115 | 11 | 90 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.437 | 0.505 | 0.491 | 51 | 50 | no | +0.045 | OK |
| KXNHLGAME-26OCT10CBJSTL-CBJ | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.652 | 0.715 | 0.703 | 72 | 29 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.780 | 0.835 | 0.825 | 84 | 17 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.197 | 0.255 | 0.243 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.334 | 0.395 | 0.382 | 40 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.374 | 0.435 | 0.423 | 44 | 57 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.165 | 0.175 | 17 | 84 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-8 | game_total | 0.395 | 0.335 | 0.347 | 34 | 67 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2 | team_total | 0.831 | 0.770 | 0.783 | 78 | 24 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.506 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.260 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB6 | team_total | 0.057 | 0.110 | 0.097 | 12 | 90 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL2 | game_spread | 0.259 | 0.315 | 0.303 | 32 | 69 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.145 | 0.154 | 15 | 86 | yes | +0.035 | OK |
| KXNHLGAME-26OCT10CBJSTL-STL | game_winner | 0.468 | 0.525 | 0.514 | 53 | 48 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN6 | team_total | 0.109 | 0.065 | 0.072 | 7 | 94 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL4 | team_total | 0.429 | 0.490 | 0.478 | 50 | 52 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL3 | team_total | 0.643 | 0.700 | 0.689 | 71 | 31 | no | +0.032 | OK |
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.398 | 0.345 | 0.355 | 35 | 66 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT10TBNYI-8 | game_total | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.293 | 0.240 | 0.250 | 25 | 77 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 | team_total | 0.405 | 0.355 | 0.365 | 36 | 65 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL3 | game_spread | 0.150 | 0.195 | 0.185 | 20 | 81 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-CBJ2 | game_spread | 0.312 | 0.265 | 0.274 | 27 | 74 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.595 | 0.540 | 0.551 | 55 | 47 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT10MINFLA-8 | game_total | 0.269 | 0.225 | 0.233 | 23 | 78 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH2 | team_total | 0.799 | 0.750 | 0.760 | 76 | 26 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.457 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI3 | game_spread | 0.153 | 0.115 | 0.122 | 12 | 89 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL5 | team_total | 0.260 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLGAME-26OCT10TORCOL-TOR | game_winner | 0.290 | 0.335 | 0.326 | 34 | 67 | no | +0.025 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.710 | 0.665 | 0.674 | 67 | 34 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-10 | game_total | 0.109 | 0.075 | 0.081 | 8 | 93 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ3 | team_total | 0.650 | 0.605 | 0.614 | 61 | 40 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-5 | game_total | 0.806 | 0.765 | 0.774 | 77 | 24 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-6 | game_total | 0.699 | 0.655 | 0.664 | 66 | 35 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.440 | 0.395 | 0.404 | 40 | 61 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ5 | team_total | 0.255 | 0.215 | 0.223 | 22 | 79 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT10MINFLA-7 | game_total | 0.459 | 0.415 | 0.424 | 42 | 59 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT10TORCOL-TOR2 | game_spread | 0.138 | 0.175 | 0.167 | 18 | 83 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT10TBNYI-9 | game_total | 0.110 | 0.145 | 0.137 | 15 | 86 | no | +0.022 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ SJS | 0.439 | 0.478 | 0.162 | 0.211 | 7.11 | 6.91 | 1.039/1.022 | KXNHLTEAMTOTAL-26OCT10EDMSJ-EDM4 -0.049 |
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
| LAK @ VGK | 0.617 | 0.588 | 0.169 | 0.223 | 6.07 | 5.96 | 1.003/0.992 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 46 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Formenton: 1+ goals YES @ 13c · p 0.2044 (adj 0.1845) · $3.94 · thesis EDM:OFFENSE_4PLUS
- Igor Chernyshov: 1+ goals YES @ 21c · p 0.2947 (adj 0.2723) · $4.7 · thesis SJS:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 17c · p 0.2301 (adj 0.2138) · $2.99 · thesis SJS:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 32c · p 0.4643 (adj 0.3673) · $3.82 · thesis EDM:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 7c · p 0.137 (adj 0.119) · $3.09 · thesis MIN:OFFENSE_4PLUS
- Nico Sturm: 1+ goals YES @ 6c · p 0.1042 (adj 0.0919) · $1.99 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 8c · p 0.1272 (adj 0.1142) · $2.15 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1499 (adj 0.1362) · $2.35 · thesis FLA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 17c · p 0.223 (adj 0.2085) · $2.69 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8164 (adj 0.7245) · $6.34 · thesis UTA:SUPPRESSED
- Justin Danforth: 1+ goals YES @ 10c · p 0.1305 (adj 0.1216) · $1.27 · thesis BUF:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1518 (adj 0.1426) · $1.34 · thesis UTA:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 7c · p 0.1067 (adj 0.0963) · $1.65 · thesis DET:OFFENSE_4PLUS
- Andrew Copp: 1+ goals YES @ 14c · p 0.1848 (adj 0.1724) · $2.12 · thesis DET:OFFENSE_4PLUS
- Emmitt Finnie: 1+ goals YES @ 16c · p 0.2008 (adj 0.1881) · $1.63 · thesis DET:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 69c · p 0.7642 (adj 0.7246) · $5.83 · thesis MTL:SUPPRESSED
- Warren Foegele: 1+ goals YES @ 12c · p 0.1865 (adj 0.1674) · $3.23 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 15c · p 0.212 (adj 0.1928) · $2.91 · thesis OTT:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 22c · p 0.2793 (adj 0.262) · $2.97 · thesis NSH:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1498 (adj 0.1386) · $1.81 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1532 (adj 0.1386) · $1.7 · thesis PIT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3304 (adj 0.3115) · $2.6 · thesis PIT:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8297 (adj 0.7873) · $4.82 · thesis PIT:WINS
- Ryan Greene: 1+ goals YES @ 14c · p 0.1987 (adj 0.1828) · $2.89 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.326 (adj 0.3083) · $3.63 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 65c · p 0.7211 (adj 0.7021) · $6.34 · thesis CAR:SUPPRESSED
- Ryan Donato: 1+ goals YES @ 13c · p 0.177 (adj 0.164) · $2.14 · thesis CHI:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 84c · p 0.8875 (adj 0.8744) · $4.9 · thesis CBJ:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 65c · p 0.7336 (adj 0.6893) · $4.61 · thesis CBJ:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 20c · p 0.2427 (adj 0.2308) · $2.01 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1851 (adj 0.1738) · $1.36 · thesis CBJ:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1694 (adj 0.1545) · $2.23 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 76c · p 0.8057 (adj 0.7918) · $5.93 · thesis COL:SUPPRESSED
- Martin Necas: 1+ goals NO @ 62c · p 0.6674 (adj 0.6543) · $3.57 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2676 (adj 0.2457) · $4.07 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 53c · p 0.727 (adj 0.5957) · $6.23 · thesis TBL:SUPPRESSED
- Matias Maccelli: 1+ goals YES @ 15c · p 0.1963 (adj 0.1835) · $2.1 · thesis NYI:OFFENSE_4PLUS
- Jake Guentzel: 1+ goals NO @ 67c · p 0.7164 (adj 0.7036) · $3.28 · thesis TBL:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 12c · p 0.1953 (adj 0.1715) · $3.4 · thesis CGY:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 15c · p 0.2241 (adj 0.2043) · $3.83 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1312 (adj 0.1172) · $2.34 · thesis ANA:OFFENSE_4PLUS
- Morgan Frost: 1+ goals YES @ 26c · p 0.301 (adj 0.2895) · $1.62 · thesis CGY:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0809 (adj 0.0719) · $1.32 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7507 (adj 0.7343) · $6.34 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6416 (adj 0.5463) · $4.97 · thesis LAK:SUPPRESSED
- Trevor Moore: 1+ assists YES @ 23c · p 0.3031 (adj 0.2591) · $1.61 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**EDM @ SJS** · priced 164/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.97, exp saves 24.77 (sd 7.03), pull risk 0.082
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.62 (sd 6.47), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.171 | 0.345 | 36/67 | +0.144 | STANDARD |
| Connor McDavid: 1+ assists | 0.536 | 0.685 | 69/32 | +0.129 | STANDARD |
| Tyler Toffoli: 1+ points | 0.551 | 0.405 | 42/61 | +0.114 | STANDARD |
| Mattias Ekholm: 1+ points | 0.455 | 0.310 | 32/70 | +0.120 | STANDARD |
| Connor McDavid: 2+ points | 0.397 | 0.535 | 55/48 | +0.105 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.381 | 0.245 | 26/77 | +0.107 | STANDARD |

**MIN @ FLA** · priced 165/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.41, exp saves 23.53 (sd 6.55), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.74), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jared Spurgeon: 1+ points | 0.392 | 0.180 | 32/96 | +0.056 | STANDARD |
| Jared Spurgeon: 1+ assists | 0.342 | 0.140 | 27/99 | +0.059 | STANDARD |
| Gustav Forsling: 1+ assists | 0.313 | 0.160 | 28/96 | +0.019 | STANDARD |
| Ryan Hartman: 1+ points | 0.510 | 0.365 | 38/65 | +0.114 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.234 | 0.370 | 38/64 | +0.109 | STANDARD |
| Brady Tkachuk: 1+ points | 0.438 | 0.570 | 59/45 | +0.095 | STANDARD |

**UTA @ BUF** · priced 162/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 26.66, exp saves 23.02 (sd 6.38), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.03 (sd 6.6), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Karel Vejmelka: 25+ saves | 0.466 | 0.280 | 50/94 | -0.052 |  |
| Vincent Trocheck: 1+ assists | 0.184 | 0.325 | 33/68 | +0.121 | STANDARD |
| Vincent Trocheck: 1+ points | 0.348 | 0.455 | 46/55 | +0.084 | STANDARD |
| Colten Ellis: 26+ saves | 0.345 | 0.240 | 43/95 | -0.102 |  |
| Josh Doan: 1+ assists | 0.324 | 0.240 | 26/78 | +0.051 | STANDARD |
| Josh Doan: 1+ points | 0.491 | 0.415 | 42/59 | +0.054 | STANDARD |

**DET @ MTL** · priced 166/181 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.75, exp saves 25.24 (sd 6.6), pull risk 0.048
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.95 (sd 6.31), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.663 | 0.465 | 51/58 | +0.136 |  |
| Emmitt Finnie: 1+ assists | 0.286 | 0.130 | 22/96 | +0.054 | STANDARD |
| Albert Johansson: 1+ assists | 0.205 | 0.060 | 11/99 | +0.089 | STANDARD |
| Zachary Bolduc: 1+ assists | 0.270 | 0.125 | 23/98 | +0.027 | STANDARD |
| Justin Faulk: 1+ assists | 0.278 | 0.135 | 23/96 | +0.035 | STANDARD |
| Ben Chiarot: 1+ assists | 0.220 | 0.085 | 15/98 | +0.061 | STANDARD |

**NSH @ OTT** · priced 163/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.09), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Juuse Saros: 27+ saves | 0.474 | 0.305 | 54/93 | -0.083 |  |
| Andre Burakovsky: 1+ assists | 0.234 | 0.365 | 38/65 | +0.100 | STANDARD |
| Tim Stutzle: 1+ assists | 0.437 | 0.545 | 55/46 | +0.085 | STANDARD |
| Ridly Greig: 1+ assists | 0.262 | 0.155 | 23/92 | +0.020 | STANDARD |
| Jordan Spence: 1+ points | 0.411 | 0.310 | 32/70 | +0.076 | STANDARD |
| Andre Burakovsky: 1+ points | 0.371 | 0.465 | 54/61 | +0.003 | STANDARD |

**DAL @ PIT** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.04 (sd 6.24), pull risk 0.065
- DAL net: Jake Oettinger (CONFIRMED) exp shots 26.81, exp saves 23.14 (sd 6.46), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.294 | 0.445 | 45/56 | +0.129 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.335 | 0.200 | 23/83 | +0.092 | STANDARD |
| Tyler Seguin: 1+ assists | 0.140 | 0.270 | 29/75 | +0.097 | STANDARD |
| Tyler Seguin: 1+ points | 0.328 | 0.440 | 46/58 | +0.075 | STANDARD |
| Jason Robertson: 2+ points | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Jason Robertson: 1+ assists | 0.386 | 0.495 | 51/52 | +0.077 | STANDARD |

**CAR @ CHI** · priced 159/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.13, exp saves 26.71 (sd 7.37), pull risk 0.078
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.55), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| K'Andre Miller: 1+ assists | 0.351 | 0.190 | 29/91 | +0.046 | STANDARD |
| Sebastian Aho: 1+ assists | 0.341 | 0.485 | 49/52 | +0.122 | STANDARD |
| Sebastian Aho: 2+ points | 0.170 | 0.295 | 31/72 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.522 | 0.640 | 65/37 | +0.092 | STANDARD |
| Patrick Kane: 1+ assists | 0.292 | 0.410 | 42/60 | +0.091 | STANDARD |
| K'Andre Miller: 1+ points | 0.399 | 0.285 | 36/79 | +0.023 | STANDARD |

**CBJ @ STL** · priced 165/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.71, exp saves 24.07 (sd 6.6), pull risk 0.054
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.17, exp saves 22.42 (sd 6.22), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.272 | 0.390 | 40/62 | +0.092 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.217 | 0.330 | 34/68 | +0.087 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.421 | 0.525 | 53/48 | +0.081 | STANDARD |
| Matthew Knies: 1+ assists | 0.266 | 0.355 | 36/65 | +0.068 | STANDARD |
| Jet Greaves: 24+ saves | 0.422 | 0.510 | 54/52 | +0.040 |  |
| Charlie Coyle: 1+ points | 0.505 | 0.425 | 44/59 | +0.048 | STANDARD |

**TOR @ COL** · priced 172/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.217 | 0.335 | 35/68 | +0.087 | STANDARD |
| Cale Makar: 1+ assists | 0.483 | 0.600 | 61/41 | +0.090 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.365 | 0.470 | 48/54 | +0.078 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.265 | 28/75 | +0.075 | STANDARD |
| Kirill Marchenko: 1+ assists | 0.300 | 0.400 | 42/62 | +0.063 | STANDARD |
| Nick Paul: 1+ assists | 0.215 | 0.120 | 22/98 | -0.017 | STANDARD |

**TBL @ NYI** · priced 147/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.71 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.5, exp saves 22.83 (sd 6.25), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.352 | 0.555 | 57/46 | +0.170 | STANDARD |
| John Carlson: 1+ assists | 0.273 | 0.475 | 48/53 | +0.180 | STANDARD |
| Brayden Schenn: 1+ points | 0.508 | 0.385 | 40/63 | +0.091 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.191 | 0.310 | 32/70 | +0.094 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.470 | 0.575 | 58/43 | +0.083 | STANDARD |
| Nikita Kucherov: 2+ points | 0.277 | 0.380 | 39/63 | +0.077 | STANDARD |

**ANA @ CGY** · priced 182/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.92, exp saves 26.73 (sd 7.25), pull risk 0.067
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.27 (sd 6.52), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Yegor Sharangovich: 1+ assists | 0.330 | 0.125 | 23/98 | +0.088 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.268 | 0.095 | 17/98 | +0.088 | STANDARD |
| Kevin Bahl: 1+ assists | 0.268 | 0.105 | 19/98 | +0.067 | STANDARD |
| Pavel Mintyukov: 1+ assists | 0.256 | 0.120 | 22/98 | +0.024 | STANDARD |
| Adam Klapka: 1+ assists | 0.247 | 0.115 | 21/98 | +0.026 | STANDARD |
| Noah Warren: 1+ assists | 0.202 | 0.080 | 15/99 | +0.043 | PRIOR_HEAVY |

**LAK @ VGK** · priced 198/202 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.01 (sd 6.25), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.27 (sd 6.63), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Andersson: 1+ assists | 0.303 | 0.155 | 29/98 | -0.001 | STANDARD |
| Artemi Panarin: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Mitch Marner: 1+ assists | 0.405 | 0.545 | 55/46 | +0.118 | STANDARD |
| Drew Doughty: 1+ assists | 0.269 | 0.130 | 24/98 | +0.016 | STANDARD |
| Brayden McNabb: 1+ assists | 0.269 | 0.130 | 24/98 | +0.016 | STANDARD |
| Joel Edmundson: 1+ assists | 0.214 | 0.085 | 16/99 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
