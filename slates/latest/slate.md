# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T15:40:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4806 · contracts joined: 2977 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2627, 'OK': 222, 'NO_EDGE': 128}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 386, 'game_early_goal': 14, 'first_goal': 497, 'game_winner': 28, 'player_goals': 876, 'game_overtime': 14, 'player_points': 497, 'goalie_saves': 7, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 2026-10-10T17:00:00Z | T-60m | 0.600 | 0.400 | 0.179 | 5.61 | 3.11 | 2.50 | 218 (25/193) | PROJECTED/CONFIRMED |
| VAN @ NJD | 2026-10-10T19:30:00Z | T-3h | 0.612 | 0.388 | 0.168 | 6.46 | 3.60 | 2.86 | 215 (25/190) | PROJECTED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-3h | 0.487 | 0.513 | 0.175 | 6.82 | 3.35 | 3.47 | 214 (25/189) | PROJECTED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-6h | 0.463 | 0.537 | 0.177 | 6.28 | 3.02 | 3.26 | 208 (25/183) | CONFIRMED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-6h | 0.536 | 0.464 | 0.173 | 6.31 | 3.27 | 3.04 | 216 (25/191) | PROBABLE/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-6h | 0.598 | 0.402 | 0.170 | 6.21 | 3.41 | 2.80 | 208 (25/183) | PROBABLE/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-6h | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 209 (25/184) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-6h | 0.466 | 0.534 | 0.172 | 6.37 | 3.09 | 3.28 | 208 (25/183) | PROJECTED/PROJECTED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-6h | 0.401 | 0.599 | 0.176 | 5.97 | 2.68 | 3.29 | 210 (25/185) | PROBABLE/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-6h | 0.568 | 0.432 | 0.182 | 5.73 | 3.07 | 2.66 | 216 (25/191) | PROJECTED/PROJECTED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-6h | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 221 (25/196) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-6h | 0.504 | 0.496 | 0.187 | 5.54 | 2.79 | 2.75 | 207 (25/182) | CONFIRMED/PROJECTED |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-6h | 0.485 | 0.514 | 0.173 | 6.27 | 3.09 | 3.19 | 217 (25/192) | PROJECTED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-6h | 0.617 | 0.383 | 0.169 | 6.07 | 3.41 | 2.65 | 210 (25/185) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.504 | 0.375 | 0.400 | 38 | 63 | yes | +0.107 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.496 | 0.615 | 0.592 | 62 | 39 | no | +0.097 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.268 | 0.385 | 0.360 | 39 | 62 | no | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.528 | 0.655 | 0.631 | 67 | 36 | no | +0.096 | OK |
| KXNHLGAME-26OCT10VANNJ-VAN | game_winner | 0.388 | 0.275 | 0.296 | 28 | 73 | yes | +0.093 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.311 | 0.435 | 0.409 | 45 | 58 | no | +0.092 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.148 | 0.255 | 0.230 | 26 | 75 | no | +0.089 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.367 | 0.475 | 0.453 | 48 | 53 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.230 | 0.335 | 0.312 | 34 | 67 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ3 | game_spread | 0.259 | 0.365 | 0.342 | 37 | 64 | no | +0.084 | OK |
| KXNHLGAME-26OCT10VANNJ-NJ | game_winner | 0.612 | 0.715 | 0.696 | 72 | 29 | no | +0.083 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.466 | 0.365 | 0.385 | 37 | 64 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ2 | game_spread | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.599 | 0.695 | 0.677 | 70 | 31 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.401 | 0.305 | 0.323 | 31 | 70 | yes | +0.076 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.463 | 0.555 | 0.537 | 56 | 45 | no | +0.070 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.537 | 0.445 | 0.463 | 45 | 56 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.333 | 0.245 | 0.261 | 25 | 76 | yes | +0.070 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.752 | 0.845 | 0.829 | 86 | 17 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.277 | 0.195 | 0.210 | 20 | 81 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.420 | 0.330 | 0.347 | 34 | 68 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 | team_total | 0.461 | 0.545 | 0.528 | 55 | 46 | no | +0.062 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.147 | 0.230 | 0.211 | 24 | 78 | no | +0.061 | OK |
| KXNHLGAME-26OCT10EDMSJ-SJ | game_winner | 0.487 | 0.405 | 0.421 | 41 | 60 | yes | +0.060 | OK |
| KXNHLGAME-26OCT10EDMSJ-EDM | game_winner | 0.513 | 0.595 | 0.579 | 60 | 41 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.238 | 0.160 | 0.174 | 17 | 85 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.321 | 0.245 | 0.259 | 25 | 76 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN3 | team_total | 0.543 | 0.460 | 0.477 | 47 | 55 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI2 | team_total | 0.703 | 0.780 | 0.766 | 79 | 23 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.652 | 0.725 | 0.711 | 73 | 28 | no | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.425 | 0.440 | 43 | 58 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.202 | 0.135 | 0.147 | 14 | 87 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.640 | 0.555 | 0.573 | 57 | 46 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.430 | 0.505 | 0.490 | 51 | 50 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.766 | 0.695 | 0.710 | 70 | 31 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.235 | 0.305 | 0.290 | 31 | 70 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.314 | 0.385 | 0.370 | 39 | 62 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.149 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.545 | 0.559 | 55 | 46 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-7 | game_total | 0.367 | 0.435 | 0.421 | 44 | 57 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.681 | 0.745 | 0.733 | 75 | 26 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.172 | 0.110 | 0.121 | 12 | 90 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI4 | team_total | 0.251 | 0.325 | 0.309 | 34 | 69 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ5 | team_total | 0.255 | 0.195 | 0.206 | 20 | 81 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM3 | game_spread | 0.195 | 0.255 | 0.242 | 26 | 75 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-5 | game_total | 0.695 | 0.755 | 0.744 | 76 | 25 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ3 | team_total | 0.501 | 0.575 | 0.560 | 59 | 44 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-6 | game_total | 0.481 | 0.545 | 0.532 | 55 | 46 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.188 | 0.245 | 0.233 | 25 | 76 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.160 | 0.171 | 17 | 85 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.261 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.446 | 0.380 | 0.393 | 39 | 63 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.506 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.455 | 0.520 | 0.507 | 53 | 49 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 | team_total | 0.383 | 0.320 | 0.332 | 33 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.445 | 0.505 | 0.493 | 51 | 50 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.305 | 0.318 | 32 | 71 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.112 | 0.065 | 0.073 | 7 | 94 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-5 | game_total | 0.710 | 0.770 | 0.759 | 78 | 24 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.337 | 0.395 | 0.383 | 40 | 61 | no | +0.036 | OK |
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.402 | 0.345 | 0.356 | 35 | 66 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.785 | 0.840 | 0.830 | 85 | 17 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ4 | team_total | 0.289 | 0.350 | 0.337 | 36 | 66 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 | team_total | 0.497 | 0.555 | 0.544 | 56 | 45 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.140 | 0.150 | 15 | 87 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-SJ2 | game_spread | 0.277 | 0.225 | 0.235 | 23 | 78 | yes | +0.035 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.710 | 0.655 | 0.666 | 66 | 35 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-4 | game_total | 0.796 | 0.845 | 0.836 | 85 | 16 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM2 | game_spread | 0.310 | 0.365 | 0.354 | 37 | 64 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.601 | 0.540 | 0.552 | 55 | 47 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL4 | team_total | 0.429 | 0.490 | 0.478 | 50 | 52 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-7 | game_total | 0.350 | 0.405 | 0.394 | 41 | 60 | no | +0.033 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 0.600 | 0.567 | 0.179 | 0.219 | 5.61 | 5.97 | 0.968/0.994 | KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 +0.074 |
| VAN @ NJD | 0.612 | 0.558 | 0.168 | 0.214 | 6.46 | 6.25 | 0.987/1.025 | KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 -0.060 |
| EDM @ SJS | 0.487 | 0.484 | 0.175 | 0.211 | 6.82 | 6.88 | 1.026/1.022 | KXNHLTOTAL-26OCT10EDMSJ-7 +0.013 |
| MIN @ FLA | 0.463 | 0.467 | 0.177 | 0.218 | 6.28 | 6.44 | 1.014/0.995 | KXNHLTOTAL-26OCT10MINFLA-7 +0.034 |
| UTA @ BUF | 0.536 | 0.512 | 0.173 | 0.215 | 6.31 | 6.46 | 0.999/0.992 | KXNHLTEAMTOTAL-26OCT10UTABUF-UTA3 +0.034 |
| DET @ MTL | 0.598 | 0.612 | 0.170 | 0.209 | 6.21 | 6.37 | 0.980/1.023 | KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 +0.035 |
| NSH @ OTT | 0.567 | 0.597 | 0.170 | 0.206 | 6.52 | 6.38 | 0.998/1.000 | KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 -0.037 |
| DAL @ PIT | 0.466 | 0.505 | 0.172 | 0.220 | 6.37 | 6.42 | 1.033/0.986 | KXNHLGAME-26OCT10DALPIT-DAL -0.039 |
| CAR @ CHI | 0.401 | 0.415 | 0.176 | 0.214 | 5.97 | 6.38 | 0.995/0.989 | KXNHLTOTAL-26OCT10CARCHI-7 +0.068 |
| CBJ @ STL | 0.568 | 0.562 | 0.182 | 0.222 | 5.73 | 6.03 | 0.993/0.964 | KXNHLTOTAL-26OCT10CBJSTL-7 +0.054 |
| TOR @ COL | 0.710 | 0.674 | 0.145 | 0.194 | 6.82 | 6.58 | 0.976/0.965 | KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 -0.057 |
| TBL @ NYI | 0.504 | 0.514 | 0.187 | 0.223 | 5.54 | 5.95 | 0.947/0.957 | KXNHLTOTAL-26OCT10TBNYI-7 +0.076 |
| ANA @ CGY | 0.485 | 0.499 | 0.173 | 0.215 | 6.27 | 6.51 | 0.997/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.617 | 0.588 | 0.169 | 0.223 | 6.07 | 5.96 | 1.003/0.992 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 49 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 13c · p 0.1866 (adj 0.1712) · $2.31 · thesis PHI:OFFENSE_4PLUS
- Frederic Brunet: 1+ assists NO @ 64c · p 0.8111 (adj 0.6901) · $5.3 · thesis BOS:SUPPRESSED
- Travis Sanheim: 1+ goals YES @ 7c · p 0.0998 (adj 0.0911) · $1.03 · thesis PHI:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 21c · p 0.2516 (adj 0.2399) · $1.65 · thesis BOS:OFFENSE_4PLUS
- Nico Hischier: 1+ goals NO @ 66c · p 0.7368 (adj 0.7151) · $4.13 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 58c · p 0.6534 (adj 0.6325) · $3.82 · thesis NJD:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7847 (adj 0.6874) · $4.53 · thesis VAN:WINS
- Alex Formenton: 1+ goals YES @ 13c · p 0.2068 (adj 0.1864) · $3.39 · thesis EDM:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 18c · p 0.2366 (adj 0.2175) · $2.03 · thesis SJS:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1131 (adj 0.1023) · $1.25 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4732 (adj 0.3736) · $3.27 · thesis EDM:SUPPRESSED
- Michael McCarron: 1+ goals YES @ 8c · p 0.1272 (adj 0.1142) · $1.81 · thesis MIN:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.137 (adj 0.1253) · $1.92 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1499 (adj 0.1349) · $1.85 · thesis FLA:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 18c · p 0.2417 (adj 0.225) · $2.56 · thesis MIN:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8164 (adj 0.7245) · $5.3 · thesis UTA:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 61c · p 0.6662 (adj 0.6509) · $4.79 · thesis BUF:SUPPRESSED
- Jack McBain: 1+ goals YES @ 12c · p 0.1518 (adj 0.1413) · $1.01 · thesis UTA:OFFENSE_4PLUS
- Jacob Fowler: 23+ saves YES @ 52c · p 0.6607 (adj 0.5692) · $4.41 · thesis DET:SHOT_CONTROL
- Nick Suzuki: 2+ assists NO @ 78c · p 0.8379 (adj 0.8065) · $4.59 · thesis MTL:SUPPRESSED
- Chris Kreider: 1+ assists NO @ 69c · p 0.768 (adj 0.719) · $3.36 · thesis MTL:SUPPRESSED
- Ryan O'Reilly: 1+ goals YES @ 22c · p 0.282 (adj 0.264) · $2.55 · thesis NSH:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1593 (adj 0.1407) · $1.57 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2128 (adj 0.1971) · $2.03 · thesis OTT:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 14c · p 0.1927 (adj 0.1733) · $1.78 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1512 (adj 0.1384) · $2.13 · thesis PIT:WINS_BY_2PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3228 (adj 0.3058) · $2.83 · thesis PIT:OFFENSE_4PLUS
- Roope Hintz: 1+ assists NO @ 55c · p 0.7085 (adj 0.6022) · $5.3 · thesis DAL:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.326 (adj 0.3083) · $3.05 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 65c · p 0.7211 (adj 0.7021) · $5.3 · thesis CAR:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 15c · p 0.1987 (adj 0.184) · $1.83 · thesis CHI:OFFENSE_4PLUS
- Ryan Donato: 1+ goals YES @ 14c · p 0.177 (adj 0.1653) · $1.18 · thesis CHI:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 84c · p 0.8896 (adj 0.876) · $4.14 · thesis CBJ:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 65c · p 0.7374 (adj 0.6912) · $3.81 · thesis CBJ:SUPPRESSED
- Adam Jiricek: 1+ assists NO @ 68c · p 0.7712 (adj 0.7054) · $2.51 · thesis STL:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1654 (adj 0.1503) · $1.53 · thesis COL:WINS_BY_2PLUS
- Cale Makar: 1+ goals NO @ 76c · p 0.8061 (adj 0.7921) · $5.0 · thesis COL:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 62c · p 0.6996 (adj 0.6548) · $3.37 · thesis TOR:SUPPRESSED
- Martin Necas: 1+ goals NO @ 62c · p 0.6677 (adj 0.6545) · $2.96 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2626 (adj 0.2432) · $3.24 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 52c · p 0.7259 (adj 0.5823) · $5.3 · thesis TBL:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 10c · p 0.1447 (adj 0.1335) · $1.84 · thesis NYI:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 14c · p 0.1738 (adj 0.1653) · $1.18 · thesis NYI:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 9c · p 0.1353 (adj 0.1165) · $1.33 · thesis ANA:OFFENSE_4PLUS
- Leo Carlsson: 1+ assists NO @ 52c · p 0.6087 (adj 0.5594) · $2.83 · thesis ANA:SUPPRESSED
- Cutter Gauthier: 1+ goals NO @ 59c · p 0.6397 (adj 0.626) · $2.67 · thesis ANA:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 68c · p 0.7507 (adj 0.7318) · $5.13 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6416 (adj 0.5463) · $4.1 · thesis LAK:SUPPRESSED
- Tomas Hertl: 1+ goals NO @ 70c · p 0.7381 (adj 0.7273) · $2.82 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BOS** · priced 165/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.33, exp saves 23.02 (sd 6.34), pull risk 0.049
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.07, exp saves 23.38 (sd 6.51), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Frederic Brunet: 1+ points | 0.239 | 0.435 | 45/58 | +0.164 | PRIOR_HEAVY |
| Frederic Brunet: 1+ assists | 0.189 | 0.375 | 39/64 | +0.155 | PRIOR_HEAVY |
| JJ Peterka: 1+ assists | 0.180 | 0.305 | 31/70 | +0.106 | STANDARD |
| JJ Peterka: 1+ points | 0.351 | 0.465 | 48/55 | +0.082 | STANDARD |
| David Jiricek: 1+ points | 0.217 | 0.325 | 33/68 | +0.088 | STANDARD |
| David Pastrnak: 2+ points | 0.295 | 0.370 | 38/64 | +0.048 | STANDARD |

**VAN @ NJD** · priced 159/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.83, exp saves 21.68 (sd 5.96), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.9 (sd 7.21), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.235 | 0.440 | 45/57 | +0.178 | STANDARD |
| Jack Hughes: 2+ points | 0.244 | 0.440 | 46/58 | +0.159 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.605 | 62/41 | +0.161 | STANDARD |
| Luke Evangelista: 1+ points | 0.398 | 0.575 | 59/44 | +0.145 | STANDARD |
| Jack Hughes: 1+ points | 0.615 | 0.760 | 78/26 | +0.112 | STANDARD |
| Luke Evangelista: 2+ points | 0.091 | 0.220 | 23/79 | +0.108 | STANDARD |

**EDM @ SJS** · priced 163/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 28.97, exp saves 24.77 (sd 6.93), pull risk 0.081
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.61 (sd 6.41), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.170 | 0.325 | 34/69 | +0.125 | STANDARD |
| Connor McDavid: 1+ assists | 0.527 | 0.680 | 69/33 | +0.128 | STANDARD |
| Connor McDavid: 2+ points | 0.389 | 0.520 | 53/49 | +0.104 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.379 | 0.250 | 27/77 | +0.096 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.476 | 0.605 | 61/40 | +0.107 | STANDARD |
| Tyler Toffoli: 1+ points | 0.544 | 0.420 | 44/60 | +0.087 | STANDARD |

**MIN @ FLA** · priced 152/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.41, exp saves 23.53 (sd 6.55), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.74), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Markstrom: 24+ saves | 0.499 | 0.295 | 53/94 | -0.048 |  |
| Ryan Hartman: 1+ points | 0.510 | 0.365 | 38/65 | +0.114 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.234 | 0.375 | 39/64 | +0.109 | STANDARD |
| Brady Tkachuk: 1+ points | 0.438 | 0.570 | 59/45 | +0.095 | STANDARD |
| Ryan Hartman: 1+ assists | 0.352 | 0.225 | 23/78 | +0.110 | STANDARD |
| Sam Reinhart: 1+ points | 0.506 | 0.605 | 62/41 | +0.067 | STANDARD |

**UTA @ BUF** · priced 158/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 26.66, exp saves 23.02 (sd 6.38), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.03 (sd 6.6), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.184 | 0.325 | 33/68 | +0.121 | STANDARD |
| Vincent Trocheck: 1+ points | 0.348 | 0.460 | 47/55 | +0.084 | STANDARD |
| Tage Thompson: 1+ points | 0.581 | 0.660 | 68/36 | +0.043 | STANDARD |
| Owen Power: 1+ assists | 0.374 | 0.300 | 32/72 | +0.039 | STANDARD |
| Tage Thompson: 2+ points | 0.213 | 0.285 | 31/74 | +0.033 | STANDARD |
| Owen Power: 1+ points | 0.424 | 0.355 | 36/65 | +0.048 | STANDARD |

**DET @ MTL** · priced 147/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROBABLE) exp shots 28.75, exp saves 25.25 (sd 6.68), pull risk 0.05
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.99 (sd 6.29), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.232 | 0.330 | 35/69 | +0.063 | STANDARD |
| Andrew Copp: 1+ points | 0.420 | 0.330 | 35/69 | +0.054 | STANDARD |
| Andrew Copp: 1+ assists | 0.297 | 0.210 | 23/81 | +0.055 | STANDARD |
| Chris Kreider: 1+ points | 0.430 | 0.515 | 53/50 | +0.053 | STANDARD |
| Viktor Arvidsson: 1+ goals | 0.293 | 0.220 | 28/84 | -0.001 | STANDARD |
| Alex DeBrincat: 2+ points | 0.248 | 0.180 | 25/89 | -0.015 | STANDARD |

**NSH @ OTT** · priced 152/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.1), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ points | 0.432 | 0.320 | 34/70 | +0.076 | STANDARD |
| Tim Stutzle: 1+ assists | 0.434 | 0.545 | 55/46 | +0.089 | STANDARD |
| Jordan Spence: 1+ assists | 0.373 | 0.265 | 28/75 | +0.079 | STANDARD |
| Claude Giroux: 1+ points | 0.513 | 0.415 | 42/59 | +0.076 | STANDARD |
| Claude Giroux: 1+ assists | 0.372 | 0.285 | 30/73 | +0.058 | STANDARD |
| Drake Batherson: 1+ assists | 0.366 | 0.445 | 46/57 | +0.047 | STANDARD |

**DAL @ PIT** · priced 157/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.05 (sd 6.21), pull risk 0.064
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.81, exp saves 23.15 (sd 6.41), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.291 | 0.455 | 46/55 | +0.141 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.330 | 0.190 | 22/84 | +0.098 | STANDARD |
| Tyler Seguin: 1+ assists | 0.139 | 0.270 | 29/75 | +0.098 | STANDARD |
| Tyler Seguin: 1+ points | 0.322 | 0.440 | 46/58 | +0.081 | STANDARD |
| Jason Robertson: 2+ points | 0.240 | 0.350 | 36/66 | +0.084 | STANDARD |
| Jason Robertson: 1+ assists | 0.390 | 0.495 | 51/52 | +0.072 | STANDARD |

**CAR @ CHI** · priced 155/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.13, exp saves 26.71 (sd 7.37), pull risk 0.078
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.55), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.485 | 49/52 | +0.122 | STANDARD |
| Sebastian Aho: 2+ points | 0.170 | 0.300 | 32/72 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.522 | 0.640 | 65/37 | +0.092 | STANDARD |
| Patrick Kane: 1+ assists | 0.292 | 0.410 | 42/60 | +0.091 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.573 | 0.475 | 49/54 | +0.065 | STANDARD |
| Nikolaj Ehlers: 1+ points | 0.491 | 0.585 | 60/43 | +0.062 | STANDARD |

**CBJ @ STL** · priced 163/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.71, exp saves 24.19 (sd 6.51), pull risk 0.048
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.17, exp saves 22.36 (sd 6.26), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.286 | 0.410 | 43/61 | +0.087 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.229 | 0.330 | 34/68 | +0.076 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.436 | 0.530 | 54/48 | +0.066 | STANDARD |
| Matthew Knies: 1+ assists | 0.263 | 0.355 | 36/65 | +0.071 | STANDARD |
| Zach Werenski: 1+ assists | 0.478 | 0.560 | 57/45 | +0.054 | STANDARD |
| Matthew Knies: 1+ points | 0.445 | 0.525 | 54/49 | +0.047 | STANDARD |

**TOR @ COL** · priced 166/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 1+ assists | 0.518 | 0.630 | 64/38 | +0.085 | STANDARD |
| Cale Makar: 1+ assists | 0.484 | 0.595 | 60/41 | +0.089 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.163 | 0.265 | 28/75 | +0.074 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.364 | 0.465 | 48/55 | +0.069 | STANDARD |
| Cale Makar: 2+ points | 0.217 | 0.315 | 32/69 | +0.078 | STANDARD |
| Cale Makar: 2+ assists | 0.144 | 0.235 | 24/77 | +0.074 | STANDARD |

**TBL @ NYI** · priced 146/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.76 (sd 6.42), pull risk 0.049
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.5, exp saves 22.78 (sd 6.23), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ilya Sorokin: 24+ saves | 0.510 | 0.275 | 53/98 | -0.038 |  |
| John Carlson: 1+ assists | 0.274 | 0.495 | 51/52 | +0.188 | STANDARD |
| John Carlson: 1+ points | 0.354 | 0.560 | 57/45 | +0.178 | STANDARD |
| Brayden Schenn: 1+ points | 0.514 | 0.380 | 40/64 | +0.097 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.188 | 0.315 | 33/70 | +0.097 | STANDARD |
| Nikita Kucherov: 2+ points | 0.274 | 0.380 | 40/64 | +0.070 | STANDARD |

**ANA @ CGY** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.92, exp saves 26.72 (sd 7.17), pull risk 0.066
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.24 (sd 6.53), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aydar Suniev: 1+ points | 0.326 | 0.170 | 32/98 | -0.009 | PRIOR_HEAVY |
| A.J. Greer: 1+ goals | 0.220 | 0.095 | 16/97 | +0.050 | STANDARD |
| Aydar Suniev: 1+ goals | 0.194 | 0.085 | 14/97 | +0.046 | PRIOR_HEAVY |
| Jackson LaCombe: 2+ points | 0.217 | 0.115 | 21/98 | -0.005 | STANDARD |
| Beckett Sennecke: 2+ points | 0.235 | 0.135 | 25/98 | -0.028 | STANDARD |
| Leo Carlsson: 1+ assists | 0.391 | 0.490 | 50/52 | +0.071 | STANDARD |

**LAK @ VGK** · priced 157/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.01 (sd 6.25), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.27 (sd 6.63), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Mitch Marner: 1+ assists | 0.405 | 0.545 | 56/47 | +0.108 | STANDARD |
| Mitch Marner: 2+ points | 0.190 | 0.325 | 34/69 | +0.105 | STANDARD |
| Jack Eichel: 2+ points | 0.244 | 0.355 | 37/66 | +0.080 | STANDARD |
| Jack Eichel: 1+ assists | 0.443 | 0.545 | 55/46 | +0.080 | STANDARD |
| Artemi Panarin: 1+ points | 0.541 | 0.635 | 64/37 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
