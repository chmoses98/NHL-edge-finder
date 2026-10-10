# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T18:12:14Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 13 · markets on board: 4815 · contracts joined: 2782 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2457, 'OK': 199, 'NO_EDGE': 126}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 358, 'game_early_goal': 13, 'first_goal': 462, 'game_winner': 26, 'player_goals': 819, 'game_overtime': 13, 'player_points': 464, 'goalie_saves': 16, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ NJD | 2026-10-10T19:30:00Z | T-60m | 0.613 | 0.387 | 0.169 | 6.43 | 3.59 | 2.84 | 216 (25/191) | CONFIRMED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-90m | 0.439 | 0.561 | 0.162 | 7.11 | 3.34 | 3.77 | 216 (25/191) | CONFIRMED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-3h | 0.463 | 0.537 | 0.177 | 6.28 | 3.02 | 3.26 | 208 (25/183) | CONFIRMED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-3h | 0.536 | 0.464 | 0.173 | 6.31 | 3.27 | 3.04 | 221 (25/196) | PROBABLE/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-3h | 0.602 | 0.398 | 0.173 | 6.20 | 3.41 | 2.79 | 209 (25/184) | CONFIRMED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-3h | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 217 (25/192) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-3h | 0.466 | 0.534 | 0.172 | 6.34 | 3.06 | 3.28 | 209 (25/184) | PROJECTED/CONFIRMED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-3h | 0.401 | 0.599 | 0.176 | 5.97 | 2.68 | 3.29 | 210 (25/185) | PROBABLE/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-3h | 0.468 | 0.532 | 0.174 | 6.20 | 3.00 | 3.20 | 218 (25/193) | CONFIRMED/CONFIRMED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-3h | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 221 (25/196) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-3h | 0.498 | 0.501 | 0.190 | 5.49 | 2.74 | 2.75 | 208 (25/183) | CONFIRMED/PROBABLE |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-6h | 0.477 | 0.523 | 0.175 | 6.31 | 3.08 | 3.23 | 219 (25/194) | CONFIRMED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-6h | 0.617 | 0.383 | 0.169 | 6.07 | 3.41 | 2.65 | 210 (25/185) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.307 | 0.440 | 0.412 | 45 | 57 | no | +0.106 | OK |
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.498 | 0.375 | 0.399 | 38 | 63 | yes | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.527 | 0.655 | 0.630 | 67 | 36 | no | +0.097 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.270 | 0.385 | 0.360 | 39 | 62 | no | +0.093 | OK |
| KXNHLGAME-26OCT10VANNJ-VAN | game_winner | 0.387 | 0.275 | 0.296 | 28 | 73 | yes | +0.093 | OK |
| KXNHLGAME-26OCT10VANNJ-NJ | game_winner | 0.613 | 0.725 | 0.704 | 73 | 28 | no | +0.093 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.501 | 0.615 | 0.593 | 62 | 39 | no | +0.092 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.150 | 0.255 | 0.231 | 26 | 75 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.367 | 0.475 | 0.453 | 48 | 53 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ3 | game_spread | 0.259 | 0.365 | 0.342 | 37 | 64 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ2 | game_spread | 0.397 | 0.505 | 0.483 | 51 | 50 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.230 | 0.335 | 0.312 | 34 | 67 | no | +0.085 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.466 | 0.365 | 0.385 | 37 | 64 | yes | +0.080 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.599 | 0.695 | 0.677 | 70 | 31 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.401 | 0.305 | 0.323 | 31 | 70 | yes | +0.076 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.753 | 0.845 | 0.829 | 86 | 17 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.328 | 0.240 | 0.256 | 25 | 77 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.420 | 0.330 | 0.347 | 34 | 68 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.640 | 0.550 | 0.569 | 56 | 46 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.147 | 0.235 | 0.215 | 25 | 78 | no | +0.061 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.463 | 0.545 | 0.529 | 55 | 46 | no | +0.060 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.537 | 0.455 | 0.471 | 46 | 55 | yes | +0.060 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-8 | game_total | 0.395 | 0.315 | 0.330 | 32 | 69 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.238 | 0.160 | 0.174 | 17 | 85 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.321 | 0.245 | 0.259 | 25 | 76 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-9 | game_total | 0.300 | 0.225 | 0.239 | 23 | 78 | yes | +0.057 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN3 | team_total | 0.543 | 0.460 | 0.476 | 47 | 55 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.425 | 0.440 | 43 | 58 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.230 | 0.244 | 24 | 78 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.674 | 0.745 | 0.732 | 75 | 26 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.168 | 0.105 | 0.116 | 11 | 90 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.200 | 0.135 | 0.146 | 14 | 87 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.149 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.586 | 0.510 | 0.525 | 52 | 50 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-10 | game_total | 0.164 | 0.105 | 0.115 | 11 | 90 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.761 | 0.695 | 0.709 | 70 | 31 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.540 | 0.555 | 55 | 47 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.437 | 0.505 | 0.491 | 51 | 50 | no | +0.045 | OK |
| KXNHLGAME-26OCT10CBJSTL-CBJ | game_winner | 0.532 | 0.465 | 0.478 | 47 | 54 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-6 | game_total | 0.699 | 0.635 | 0.648 | 64 | 37 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.430 | 0.495 | 0.482 | 50 | 51 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.780 | 0.840 | 0.829 | 85 | 17 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.197 | 0.255 | 0.243 | 26 | 75 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.334 | 0.395 | 0.382 | 40 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.374 | 0.435 | 0.423 | 44 | 57 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.160 | 0.171 | 17 | 85 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2 | team_total | 0.831 | 0.770 | 0.783 | 78 | 24 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.260 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.305 | 0.318 | 32 | 71 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.111 | 0.065 | 0.072 | 7 | 94 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL2 | game_spread | 0.259 | 0.315 | 0.303 | 32 | 69 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT10EDMSJ-7 | game_total | 0.593 | 0.535 | 0.547 | 54 | 47 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.140 | 0.150 | 15 | 87 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL4 | team_total | 0.429 | 0.490 | 0.478 | 50 | 52 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ3 | team_total | 0.703 | 0.760 | 0.749 | 77 | 25 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.440 | 0.385 | 0.396 | 39 | 62 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL3 | team_total | 0.643 | 0.700 | 0.689 | 71 | 31 | no | +0.032 | OK |
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.398 | 0.345 | 0.355 | 35 | 66 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL3 | game_spread | 0.366 | 0.315 | 0.325 | 32 | 69 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.293 | 0.240 | 0.250 | 25 | 77 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ5 | team_total | 0.295 | 0.345 | 0.335 | 35 | 66 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 | team_total | 0.405 | 0.355 | 0.365 | 36 | 65 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-STL3 | game_spread | 0.150 | 0.200 | 0.189 | 21 | 81 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.450 | 0.461 | 46 | 56 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 | team_total | 0.374 | 0.320 | 0.331 | 33 | 69 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.506 | 0.450 | 0.461 | 46 | 56 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT10CBJSTL-CBJ2 | game_spread | 0.312 | 0.260 | 0.270 | 27 | 75 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.595 | 0.540 | 0.551 | 55 | 47 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT10MINFLA-8 | game_total | 0.269 | 0.225 | 0.233 | 23 | 78 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH2 | team_total | 0.799 | 0.750 | 0.760 | 76 | 26 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.457 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT10TORCOL-8 | game_total | 0.350 | 0.305 | 0.314 | 31 | 70 | yes | +0.025 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| VAN @ NJD | 0.613 | 0.560 | 0.169 | 0.219 | 6.43 | 6.25 | 0.984/1.025 | KXNHLSPREAD-26OCT10VANNJ-NJ2 -0.061 |
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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 51 recommended · full analysis in card.md / packet.json `thesis_card`

- New Jersey wins by over 1.5 goals NO @ 50c · p 0.669 (adj 0.5559) · $3.4 · thesis VAN:WINS
- Nico Hischier: 1+ goals NO @ 66c · p 0.7305 (adj 0.7104) · $5.17 · thesis NJD:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7816 (adj 0.6863) · $2.07 · thesis VAN:WINS
- Jack Hughes: 1+ goals NO @ 59c · p 0.6498 (adj 0.6336) · $3.43 · thesis NJD:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 13c · p 0.2013 (adj 0.1822) · $3.45 · thesis EDM:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 17c · p 0.2301 (adj 0.2138) · $2.76 · thesis SJS:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1161 (adj 0.1058) · $1.65 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4687 (adj 0.3753) · $3.82 · thesis EDM:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 8c · p 0.137 (adj 0.1215) · $2.42 · thesis MIN:OFFENSE_4PLUS
- Nico Sturm: 1+ goals YES @ 6c · p 0.1042 (adj 0.0919) · $1.8 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 8c · p 0.1272 (adj 0.1142) · $1.96 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1499 (adj 0.1362) · $2.13 · thesis FLA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 17c · p 0.223 (adj 0.2085) · $2.43 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8164 (adj 0.7212) · $5.74 · thesis UTA:SUPPRESSED
- Justin Danforth: 1+ goals YES @ 10c · p 0.1305 (adj 0.1216) · $1.15 · thesis BUF:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 12c · p 0.1518 (adj 0.1426) · $1.22 · thesis UTA:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 7c · p 0.1067 (adj 0.0963) · $1.52 · thesis DET:OFFENSE_4PLUS
- Andrew Copp: 1+ goals YES @ 14c · p 0.1848 (adj 0.1661) · $1.39 · thesis DET:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 17c · p 0.2078 (adj 0.1971) · $1.61 · thesis MTL:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 69c · p 0.7642 (adj 0.7221) · $5.25 · thesis MTL:SUPPRESSED
- Warren Foegele: 1+ goals YES @ 13c · p 0.1865 (adj 0.1686) · $2.32 · thesis OTT:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 22c · p 0.2793 (adj 0.262) · $2.69 · thesis NSH:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.212 (adj 0.1953) · $2.09 · thesis OTT:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1498 (adj 0.1386) · $1.64 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1532 (adj 0.1386) · $2.2 · thesis PIT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3304 (adj 0.3115) · $3.02 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ assists YES @ 30c · p 0.3936 (adj 0.3443) · $1.82 · thesis PIT:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8297 (adj 0.7873) · $4.98 · thesis PIT:WINS
- Ryan Greene: 1+ goals YES @ 14c · p 0.1987 (adj 0.1828) · $2.62 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.326 (adj 0.3083) · $3.28 · thesis CHI:OFFENSE_4PLUS
- Ryan Donato: 1+ goals YES @ 13c · p 0.177 (adj 0.164) · $1.93 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7211 (adj 0.7033) · $5.74 · thesis CAR:SUPPRESSED
- Conor Garland: 1+ goals NO @ 84c · p 0.8875 (adj 0.8744) · $4.49 · thesis CBJ:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 65c · p 0.7336 (adj 0.6893) · $4.11 · thesis CBJ:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1851 (adj 0.1751) · $1.35 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2427 (adj 0.232) · $1.04 · thesis CBJ:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1694 (adj 0.1545) · $1.92 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 76c · p 0.8057 (adj 0.7918) · $5.38 · thesis COL:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 62c · p 0.6996 (adj 0.6548) · $3.62 · thesis TOR:SUPPRESSED
- Martin Necas: 1+ goals NO @ 62c · p 0.6674 (adj 0.6543) · $3.22 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2676 (adj 0.2457) · $3.68 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 54c · p 0.727 (adj 0.5989) · $5.63 · thesis TBL:SUPPRESSED
- Matias Maccelli: 1+ goals YES @ 15c · p 0.1963 (adj 0.1835) · $1.9 · thesis NYI:OFFENSE_4PLUS
- Jake Guentzel: 1+ goals NO @ 67c · p 0.7164 (adj 0.7036) · $2.98 · thesis TBL:SUPPRESSED
- Aydar Suniev: 1+ goals YES @ 12c · p 0.1953 (adj 0.1715) · $3.08 · thesis CGY:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1312 (adj 0.1172) · $2.14 · thesis ANA:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 17c · p 0.2241 (adj 0.2068) · $2.19 · thesis ANA:OFFENSE_4PLUS
- Cutter Gauthier: 1+ goals NO @ 59c · p 0.6342 (adj 0.6219) · $2.63 · thesis ANA:SUPPRESSED
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0809 (adj 0.0707) · $1.1 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 69c · p 0.7507 (adj 0.7343) · $5.74 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6416 (adj 0.5463) · $4.37 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**VAN @ NJD** · priced 160/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 24.83, exp saves 21.69 (sd 6.01), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.91 (sd 7.17), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.408 | 0.615 | 63/40 | +0.176 | STANDARD |
| Luke Evangelista: 1+ assists | 0.242 | 0.440 | 45/57 | +0.171 | STANDARD |
| Jack Hughes: 2+ points | 0.249 | 0.430 | 44/58 | +0.153 | STANDARD |
| Luke Evangelista: 1+ points | 0.400 | 0.565 | 57/44 | +0.142 | STANDARD |
| Jack Hughes: 1+ points | 0.616 | 0.780 | 79/23 | +0.142 | STANDARD |
| Luke Evangelista: 2+ points | 0.096 | 0.220 | 23/79 | +0.102 | STANDARD |

**EDM @ SJS** · priced 165/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 28.97, exp saves 24.77 (sd 7.03), pull risk 0.082
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.62 (sd 6.47), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.168 | 0.320 | 33/69 | +0.127 | STANDARD |
| Yaroslav Askarov: 26+ saves | 0.456 | 0.310 | 56/94 | -0.121 |  |
| Connor McDavid: 1+ assists | 0.531 | 0.675 | 68/33 | +0.123 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.381 | 0.245 | 26/77 | +0.107 | STANDARD |
| Mattias Ekholm: 1+ points | 0.423 | 0.290 | 30/72 | +0.108 | STANDARD |
| Connor McDavid: 2+ points | 0.393 | 0.525 | 54/49 | +0.100 | STANDARD |

**MIN @ FLA** · priced 152/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.41, exp saves 23.53 (sd 6.55), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.74), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.510 | 0.365 | 38/65 | +0.114 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.234 | 0.370 | 38/64 | +0.109 | STANDARD |
| Ryan Hartman: 1+ assists | 0.352 | 0.220 | 23/79 | +0.110 | STANDARD |
| Brady Tkachuk: 1+ points | 0.438 | 0.570 | 59/45 | +0.095 | STANDARD |
| Bobby Brink: 1+ goals | 0.173 | 0.065 | 12/99 | +0.046 | STANDARD |
| Sam Reinhart: 1+ points | 0.506 | 0.600 | 61/41 | +0.067 | STANDARD |

**UTA @ BUF** · priced 161/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 26.66, exp saves 23.02 (sd 6.38), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.03 (sd 6.6), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.184 | 0.330 | 34/68 | +0.121 | STANDARD |
| Vincent Trocheck: 1+ points | 0.348 | 0.455 | 46/55 | +0.084 | STANDARD |
| Josh Doan: 1+ assists | 0.324 | 0.220 | 26/82 | +0.051 | STANDARD |
| Colten Ellis: 26+ saves | 0.345 | 0.245 | 44/95 | -0.112 |  |
| Josh Doan: 2+ points | 0.153 | 0.075 | 12/97 | +0.026 | STANDARD |
| Zach Benson: 1+ points | 0.537 | 0.465 | 48/55 | +0.040 | STANDARD |

**DET @ MTL** · priced 146/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.75, exp saves 25.24 (sd 6.6), pull risk 0.048
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.95 (sd 6.31), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.663 | 0.470 | 51/57 | +0.136 |  |
| Andrew Copp: 1+ points | 0.422 | 0.325 | 34/69 | +0.067 | STANDARD |
| Andrew Copp: 1+ assists | 0.291 | 0.205 | 22/81 | +0.059 | STANDARD |
| Chris Kreider: 1+ assists | 0.236 | 0.320 | 33/69 | +0.059 | STANDARD |
| Andrew Copp: 1+ goals | 0.185 | 0.110 | 14/92 | +0.036 | STANDARD |
| Chris Kreider: 1+ points | 0.438 | 0.510 | 52/50 | +0.044 | STANDARD |

**NSH @ OTT** · priced 160/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.09), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.437 | 0.545 | 55/46 | +0.085 | STANDARD |
| Jordan Spence: 1+ points | 0.411 | 0.320 | 34/70 | +0.055 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.230 | 0.315 | 33/70 | +0.055 | PRIOR_HEAVY |
| Jordan Spence: 1+ assists | 0.349 | 0.265 | 28/75 | +0.055 | STANDARD |
| Andre Burakovsky: 1+ points | 0.371 | 0.290 | 56/98 | -0.207 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.290 | 0.370 | 38/64 | +0.054 | PRIOR_HEAVY |

**DAL @ PIT** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.04 (sd 6.24), pull risk 0.065
- DAL net: Jake Oettinger (CONFIRMED) exp shots 26.81, exp saves 23.14 (sd 6.46), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.294 | 0.455 | 46/55 | +0.139 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.335 | 0.200 | 23/83 | +0.092 | STANDARD |
| Tyler Seguin: 1+ assists | 0.140 | 0.270 | 29/75 | +0.097 | STANDARD |
| Tyler Seguin: 1+ points | 0.328 | 0.440 | 46/58 | +0.075 | STANDARD |
| Jason Robertson: 2+ points | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Jason Robertson: 1+ assists | 0.386 | 0.495 | 51/52 | +0.077 | STANDARD |

**CAR @ CHI** · priced 155/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.13, exp saves 26.71 (sd 7.37), pull risk 0.078
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.55), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.485 | 49/52 | +0.122 | STANDARD |
| Sebastian Aho: 2+ points | 0.170 | 0.300 | 32/72 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.522 | 0.640 | 65/37 | +0.092 | STANDARD |
| Patrick Kane: 1+ assists | 0.292 | 0.405 | 42/61 | +0.081 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.573 | 0.470 | 48/54 | +0.075 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.325 | 0.425 | 44/59 | +0.069 | STANDARD |

**CBJ @ STL** · priced 165/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.71, exp saves 24.07 (sd 6.6), pull risk 0.054
- CBJ net: Jet Greaves (CONFIRMED) exp shots 26.17, exp saves 22.42 (sd 6.22), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.272 | 0.400 | 41/61 | +0.102 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.421 | 0.530 | 54/48 | +0.081 | STANDARD |
| Adam Jiricek: 1+ assists | 0.217 | 0.325 | 34/69 | +0.078 | PRIOR_HEAVY |
| Matthew Knies: 1+ assists | 0.266 | 0.355 | 36/65 | +0.068 | STANDARD |
| Charlie Coyle: 1+ points | 0.505 | 0.425 | 44/59 | +0.048 | STANDARD |
| Zach Werenski: 1+ assists | 0.478 | 0.555 | 56/45 | +0.054 | STANDARD |

**TOR @ COL** · priced 166/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.483 | 0.595 | 60/41 | +0.090 | STANDARD |
| Cale Makar: 1+ points | 0.584 | 0.690 | 71/33 | +0.070 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.265 | 28/75 | +0.075 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.365 | 0.465 | 47/54 | +0.078 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.521 | 0.620 | 63/39 | +0.072 | STANDARD |
| Cale Makar: 2+ points | 0.217 | 0.315 | 32/69 | +0.078 | STANDARD |

**TBL @ NYI** · priced 147/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.71 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.5, exp saves 22.83 (sd 6.25), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.352 | 0.565 | 58/45 | +0.180 | STANDARD |
| John Carlson: 1+ assists | 0.273 | 0.470 | 48/54 | +0.170 | STANDARD |
| Brayden Schenn: 1+ points | 0.508 | 0.385 | 40/63 | +0.091 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.191 | 0.310 | 32/70 | +0.094 | STANDARD |
| Nikita Kucherov: 2+ points | 0.277 | 0.380 | 39/63 | +0.077 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.129 | 0.225 | 23/78 | +0.079 | STANDARD |

**ANA @ CGY** · priced 164/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (CONFIRMED) exp shots 30.92, exp saves 26.73 (sd 7.25), pull risk 0.067
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.27 (sd 6.52), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Leo Carlsson: 1+ assists | 0.389 | 0.495 | 50/51 | +0.083 | STANDARD |
| Aydar Suniev: 1+ goals | 0.195 | 0.100 | 12/92 | +0.068 | PRIOR_HEAVY |
| Dustin Wolf: 26+ saves | 0.568 | 0.480 | 51/55 | +0.041 |  |
| Alex Killorn: 1+ assists | 0.314 | 0.230 | 25/79 | +0.051 | STANDARD |
| Leo Carlsson: 1+ points | 0.574 | 0.645 | 65/36 | +0.050 | STANDARD |
| Cutter Gauthier: 1+ points | 0.590 | 0.660 | 67/35 | +0.044 | STANDARD |

**LAK @ VGK** · priced 157/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.01 (sd 6.25), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.27 (sd 6.63), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Mitch Marner: 1+ assists | 0.405 | 0.540 | 56/48 | +0.098 | STANDARD |
| Mitch Marner: 2+ points | 0.190 | 0.325 | 33/68 | +0.115 | STANDARD |
| Jack Eichel: 2+ points | 0.244 | 0.355 | 37/66 | +0.080 | STANDARD |
| Jack Eichel: 1+ assists | 0.443 | 0.545 | 55/46 | +0.080 | STANDARD |
| Artemi Panarin: 1+ points | 0.541 | 0.635 | 64/37 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
