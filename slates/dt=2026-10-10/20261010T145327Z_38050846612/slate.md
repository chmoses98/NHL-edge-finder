# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T14:53:27Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4790 · contracts joined: 2961 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2611, 'OK': 220, 'NO_EDGE': 130}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 383, 'game_early_goal': 14, 'first_goal': 496, 'game_winner': 28, 'player_goals': 875, 'game_overtime': 14, 'player_points': 492, 'game_spread': 56, 'team_total': 140, 'game_total': 126, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 2026-10-10T17:00:00Z | T-90m | 0.608 | 0.392 | 0.186 | 5.67 | 3.16 | 2.50 | 217 (25/192) | PROJECTED/PROJECTED |
| VAN @ NJD | 2026-10-10T19:30:00Z | T-3h | 0.612 | 0.388 | 0.168 | 6.46 | 3.60 | 2.86 | 215 (25/190) | PROJECTED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-3h | 0.487 | 0.513 | 0.175 | 6.82 | 3.35 | 3.47 | 217 (25/192) | PROJECTED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-6h | 0.468 | 0.532 | 0.176 | 6.23 | 3.02 | 3.21 | 207 (25/182) | PROJECTED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-6h | 0.536 | 0.464 | 0.174 | 6.31 | 3.27 | 3.04 | 211 (25/186) | PROJECTED/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-6h | 0.599 | 0.401 | 0.173 | 6.22 | 3.41 | 2.81 | 207 (25/182) | PROJECTED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-6h | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 208 (25/183) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-6h | 0.466 | 0.534 | 0.172 | 6.37 | 3.09 | 3.28 | 208 (25/183) | PROJECTED/PROJECTED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-6h | 0.400 | 0.600 | 0.178 | 6.00 | 2.68 | 3.31 | 208 (25/183) | PROJECTED/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-6h | 0.568 | 0.432 | 0.182 | 5.73 | 3.07 | 2.66 | 216 (25/191) | PROJECTED/PROJECTED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-6h | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 221 (25/196) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-6h | 0.496 | 0.504 | 0.187 | 5.58 | 2.78 | 2.80 | 202 (25/177) | PROBABLE/PROJECTED |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-6h | 0.485 | 0.514 | 0.173 | 6.27 | 3.09 | 3.19 | 214 (25/189) | PROJECTED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-6h | 0.617 | 0.383 | 0.169 | 6.07 | 3.41 | 2.65 | 210 (25/185) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.496 | 0.375 | 0.399 | 38 | 63 | yes | +0.100 | OK |
| KXNHLGAME-26OCT10VANNJ-VAN | game_winner | 0.388 | 0.275 | 0.296 | 28 | 73 | yes | +0.093 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.504 | 0.615 | 0.593 | 62 | 39 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.539 | 0.655 | 0.633 | 67 | 36 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ3 | game_spread | 0.259 | 0.365 | 0.342 | 37 | 64 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.319 | 0.435 | 0.411 | 45 | 58 | no | +0.084 | OK |
| KXNHLGAME-26OCT10VANNJ-NJ | game_winner | 0.612 | 0.715 | 0.696 | 72 | 29 | no | +0.083 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.154 | 0.255 | 0.232 | 26 | 75 | no | +0.083 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.372 | 0.475 | 0.454 | 48 | 53 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.274 | 0.375 | 0.353 | 38 | 63 | no | +0.080 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.466 | 0.365 | 0.385 | 37 | 64 | yes | +0.079 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ2 | game_spread | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.237 | 0.335 | 0.314 | 34 | 67 | no | +0.078 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.600 | 0.695 | 0.677 | 70 | 31 | no | +0.075 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.400 | 0.305 | 0.323 | 31 | 70 | yes | +0.075 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.065 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.532 | 0.445 | 0.462 | 45 | 56 | yes | +0.065 | OK |
| KXNHLGAME-26OCT10EDMSJ-SJ | game_winner | 0.487 | 0.405 | 0.421 | 41 | 60 | yes | +0.060 | OK |
| KXNHLGAME-26OCT10EDMSJ-EDM | game_winner | 0.513 | 0.595 | 0.579 | 60 | 41 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.333 | 0.250 | 0.265 | 26 | 76 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 | team_total | 0.463 | 0.550 | 0.533 | 56 | 46 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.761 | 0.845 | 0.830 | 86 | 17 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.425 | 0.440 | 43 | 58 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.202 | 0.135 | 0.147 | 14 | 87 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.409 | 0.330 | 0.345 | 34 | 68 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.230 | 0.244 | 24 | 78 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.234 | 0.305 | 0.290 | 31 | 70 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.766 | 0.695 | 0.710 | 70 | 31 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.314 | 0.385 | 0.370 | 39 | 62 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.230 | 0.160 | 0.172 | 17 | 85 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.434 | 0.505 | 0.491 | 51 | 50 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.657 | 0.725 | 0.712 | 73 | 28 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.545 | 0.559 | 55 | 46 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.309 | 0.245 | 0.257 | 25 | 76 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN3 | team_total | 0.543 | 0.465 | 0.481 | 48 | 55 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-7 | game_total | 0.367 | 0.435 | 0.421 | 44 | 57 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.260 | 0.325 | 0.311 | 33 | 68 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.172 | 0.110 | 0.121 | 12 | 90 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.154 | 0.215 | 0.202 | 22 | 79 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ5 | team_total | 0.255 | 0.190 | 0.202 | 20 | 82 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI2 | team_total | 0.704 | 0.775 | 0.762 | 79 | 24 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM3 | game_spread | 0.195 | 0.255 | 0.242 | 26 | 75 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ3 | team_total | 0.501 | 0.575 | 0.560 | 59 | 44 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-6 | game_total | 0.481 | 0.545 | 0.532 | 55 | 46 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.628 | 0.555 | 0.570 | 57 | 46 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI4 | team_total | 0.254 | 0.325 | 0.310 | 34 | 69 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.158 | 0.225 | 0.210 | 24 | 79 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.188 | 0.245 | 0.233 | 25 | 76 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.160 | 0.171 | 17 | 85 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.261 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.446 | 0.380 | 0.393 | 39 | 63 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 | team_total | 0.383 | 0.320 | 0.332 | 33 | 69 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ5 | team_total | 0.296 | 0.355 | 0.343 | 36 | 65 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.305 | 0.318 | 32 | 71 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.112 | 0.065 | 0.073 | 7 | 94 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-5 | game_total | 0.710 | 0.770 | 0.759 | 78 | 24 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ4 | team_total | 0.289 | 0.355 | 0.341 | 37 | 66 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 | team_total | 0.497 | 0.555 | 0.544 | 56 | 45 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.140 | 0.150 | 15 | 87 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-SJ2 | game_spread | 0.277 | 0.225 | 0.235 | 23 | 78 | yes | +0.035 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.710 | 0.655 | 0.666 | 66 | 35 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM2 | game_spread | 0.310 | 0.365 | 0.354 | 37 | 64 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-5 | game_total | 0.703 | 0.755 | 0.745 | 76 | 25 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.601 | 0.540 | 0.552 | 55 | 47 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL4 | team_total | 0.429 | 0.490 | 0.478 | 50 | 52 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.296 | 0.240 | 0.251 | 25 | 77 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT10PHIBOS-PHI3 | game_spread | 0.099 | 0.145 | 0.134 | 15 | 86 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI2 | team_total | 0.737 | 0.680 | 0.692 | 69 | 33 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-4 | game_total | 0.809 | 0.860 | 0.851 | 87 | 15 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.461 | 0.520 | 0.508 | 53 | 49 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLGAME-26OCT10PHIBOS-BOS | game_winner | 0.608 | 0.555 | 0.566 | 56 | 45 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL3 | game_spread | 0.366 | 0.315 | 0.325 | 32 | 69 | yes | +0.031 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 0.608 | 0.565 | 0.186 | 0.222 | 5.67 | 5.98 | 0.968/0.993 | KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 +0.073 |
| VAN @ NJD | 0.612 | 0.558 | 0.168 | 0.214 | 6.46 | 6.25 | 0.987/1.025 | KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 -0.060 |
| EDM @ SJS | 0.487 | 0.484 | 0.175 | 0.211 | 6.82 | 6.88 | 1.026/1.022 | KXNHLTOTAL-26OCT10EDMSJ-7 +0.013 |
| MIN @ FLA | 0.468 | 0.471 | 0.176 | 0.221 | 6.23 | 6.42 | 1.008/0.995 | KXNHLTOTAL-26OCT10MINFLA-7 +0.038 |
| UTA @ BUF | 0.536 | 0.513 | 0.174 | 0.219 | 6.31 | 6.45 | 0.998/0.992 | KXNHLTEAMTOTAL-26OCT10UTABUF-UTA3 +0.035 |
| DET @ MTL | 0.599 | 0.622 | 0.173 | 0.207 | 6.22 | 6.31 | 0.953/1.023 | KXNHLSPREAD-26OCT10DETMTL-MTL3 +0.037 |
| NSH @ OTT | 0.567 | 0.597 | 0.170 | 0.206 | 6.52 | 6.38 | 0.998/1.000 | KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 -0.037 |
| DAL @ PIT | 0.466 | 0.505 | 0.172 | 0.220 | 6.37 | 6.42 | 1.033/0.986 | KXNHLGAME-26OCT10DALPIT-DAL -0.039 |
| CAR @ CHI | 0.400 | 0.413 | 0.178 | 0.215 | 6.00 | 6.40 | 1.003/0.989 | KXNHLTOTAL-26OCT10CARCHI-7 +0.073 |
| CBJ @ STL | 0.568 | 0.562 | 0.182 | 0.222 | 5.73 | 6.03 | 0.993/0.964 | KXNHLTOTAL-26OCT10CBJSTL-7 +0.054 |
| TOR @ COL | 0.710 | 0.674 | 0.145 | 0.194 | 6.82 | 6.58 | 0.976/0.965 | KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 -0.057 |
| TBL @ NYI | 0.496 | 0.506 | 0.187 | 0.220 | 5.58 | 5.97 | 0.951/0.957 | KXNHLTOTAL-26OCT10TBNYI-7 +0.068 |
| ANA @ CGY | 0.485 | 0.499 | 0.173 | 0.215 | 6.27 | 6.51 | 0.997/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.617 | 0.588 | 0.169 | 0.223 | 6.07 | 5.96 | 1.003/0.992 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 48 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 13c · p 0.1788 (adj 0.1641) · $1.95 · thesis PHI:OFFENSE_4PLUS
- JJ Peterka: 1+ goals NO @ 73c · p 0.7865 (adj 0.7711) · $5.56 · thesis BOS:SUPPRESSED
- David Jiricek: 1+ assists NO @ 76c · p 0.8189 (adj 0.7844) · $4.86 · thesis PHI:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 66c · p 0.7368 (adj 0.7151) · $4.39 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 58c · p 0.6534 (adj 0.6325) · $3.96 · thesis NJD:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 51c · p 0.6658 (adj 0.5613) · $1.91 · thesis VAN:WINS
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7847 (adj 0.6874) · $3.23 · thesis VAN:WINS
- Alex Formenton: 1+ goals YES @ 14c · p 0.2068 (adj 0.1876) · $2.98 · thesis EDM:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 18c · p 0.2366 (adj 0.2225) · $2.58 · thesis SJS:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4732 (adj 0.3736) · $3.34 · thesis EDM:SUPPRESSED
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1131 (adj 0.1011) · $1.22 · thesis EDM:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1394 (adj 0.127) · $2.2 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 8c · p 0.1288 (adj 0.1141) · $1.93 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 18c · p 0.2443 (adj 0.2257) · $2.83 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1479 (adj 0.1334) · $1.87 · thesis FLA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.8167 (adj 0.7246) · $5.56 · thesis UTA:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 62c · p 0.6671 (adj 0.6528) · $3.45 · thesis BUF:SUPPRESSED
- Owen Power: 1+ assists YES @ 32c · p 0.387 (adj 0.346) · $1.28 · thesis BUF:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 69c · p 0.7702 (adj 0.7226) · $3.91 · thesis MTL:SUPPRESSED
- Nick Suzuki: 2+ assists NO @ 78c · p 0.8434 (adj 0.8067) · $4.44 · thesis MTL:SUPPRESSED
- Josh Anderson: 1+ goals YES @ 17c · p 0.201 (adj 0.192) · $1.11 · thesis MTL:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 12c · p 0.1764 (adj 0.1723) · $3.5 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2116 (adj 0.1962) · $2.05 · thesis OTT:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 15c · p 0.1926 (adj 0.182) · $1.84 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1512 (adj 0.1384) · $2.18 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 8c · p 0.1137 (adj 0.1053) · $1.33 · thesis PIT:OFFENSE_4PLUS
- Nick Robertson: 1+ goals YES @ 12c · p 0.1567 (adj 0.1475) · $1.49 · thesis PIT:OFFENSE_4PLUS
- Roope Hintz: 1+ assists NO @ 56c · p 0.7085 (adj 0.6055) · $4.87 · thesis DAL:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 65c · p 0.7216 (adj 0.7025) · $5.45 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.3131 (adj 0.2986) · $2.33 · thesis CHI:OFFENSE_4PLUS
- Chicago wins by over 1.5 goals YES @ 15c · p 0.2117 (adj 0.1784) · $1.17 · thesis CHI:WINS_BY_2PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7018 (adj 0.6259) · $4.96 · thesis CHI:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 14c · p 0.1752 (adj 0.1664) · $1.43 · thesis CBJ:OFFENSE_4PLUS
- Matthew Knies: 1+ assists NO @ 65c · p 0.7374 (adj 0.6887) · $5.29 · thesis CBJ:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1654 (adj 0.1503) · $1.64 · thesis COL:WINS_BY_2PLUS
- Nathan MacKinnon: 2+ assists NO @ 75c · p 0.8374 (adj 0.7912) · $5.56 · thesis COL:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 62c · p 0.6996 (adj 0.6548) · $3.67 · thesis TOR:SUPPRESSED
- Martin Necas: 1+ goals NO @ 62c · p 0.6677 (adj 0.6545) · $2.63 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2694 (adj 0.2483) · $3.73 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 52c · p 0.7398 (adj 0.5872) · $5.56 · thesis TBL:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 10c · p 0.1436 (adj 0.1327) · $1.81 · thesis NYI:OFFENSE_4PLUS
- Casey Cizikas: 1+ goals YES @ 10c · p 0.1426 (adj 0.132) · $1.77 · thesis NYI:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 9c · p 0.1353 (adj 0.1152) · $1.29 · thesis ANA:OFFENSE_4PLUS
- Cutter Gauthier: 1+ goals NO @ 59c · p 0.6397 (adj 0.626) · $3.11 · thesis ANA:SUPPRESSED
- Leo Carlsson: 1+ assists NO @ 51c · p 0.6087 (adj 0.5413) · $1.64 · thesis ANA:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 69c · p 0.7507 (adj 0.733) · $5.39 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6416 (adj 0.5463) · $4.3 · thesis LAK:SUPPRESSED
- Tomas Hertl: 1+ goals NO @ 70c · p 0.7381 (adj 0.7273) · $2.96 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BOS** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.33, exp saves 23.04 (sd 6.29), pull risk 0.051
- PHI net: Dan Vladar (PROJECTED) exp shots 27.07, exp saves 23.38 (sd 6.46), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Frederic Brunet: 1+ points | 0.239 | 0.435 | 45/58 | +0.164 | PRIOR_HEAVY |
| Frederic Brunet: 1+ assists | 0.188 | 0.375 | 39/64 | +0.156 | PRIOR_HEAVY |
| JJ Peterka: 1+ assists | 0.177 | 0.305 | 31/70 | +0.108 | STANDARD |
| JJ Peterka: 1+ points | 0.354 | 0.465 | 48/55 | +0.079 | STANDARD |
| David Jiricek: 1+ points | 0.217 | 0.325 | 34/69 | +0.078 | STANDARD |
| David Pastrnak: 2+ points | 0.287 | 0.375 | 39/64 | +0.056 | STANDARD |

**VAN @ NJD** · priced 159/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.83, exp saves 21.68 (sd 5.96), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.9 (sd 7.21), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.235 | 0.440 | 45/57 | +0.178 | STANDARD |
| Jack Hughes: 2+ points | 0.244 | 0.440 | 46/58 | +0.159 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.600 | 62/42 | +0.151 | STANDARD |
| Luke Evangelista: 1+ points | 0.398 | 0.575 | 59/44 | +0.145 | STANDARD |
| Jack Hughes: 1+ points | 0.615 | 0.785 | 80/23 | +0.143 | STANDARD |
| Luke Evangelista: 2+ points | 0.091 | 0.215 | 23/80 | +0.098 | STANDARD |

**EDM @ SJS** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 28.97, exp saves 24.77 (sd 6.93), pull risk 0.081
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.61 (sd 6.41), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.170 | 0.330 | 35/69 | +0.125 | STANDARD |
| Connor McDavid: 1+ assists | 0.527 | 0.680 | 69/33 | +0.128 | STANDARD |
| Connor McDavid: 2+ points | 0.389 | 0.525 | 54/49 | +0.104 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.379 | 0.250 | 27/77 | +0.096 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.476 | 0.605 | 61/40 | +0.107 | STANDARD |
| Leon Draisaitl: 2+ points | 0.335 | 0.460 | 48/56 | +0.088 | STANDARD |

**MIN @ FLA** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.41, exp saves 23.59 (sd 6.55), pull risk 0.069
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.73), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.509 | 0.370 | 39/65 | +0.102 | STANDARD |
| Brady Tkachuk: 1+ points | 0.441 | 0.575 | 60/45 | +0.092 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.242 | 0.375 | 39/64 | +0.102 | STANDARD |
| Ryan Hartman: 1+ assists | 0.348 | 0.225 | 24/79 | +0.096 | STANDARD |
| Sam Reinhart: 1+ points | 0.505 | 0.610 | 63/41 | +0.068 | STANDARD |
| Carter Verhaeghe: 2+ points | 0.188 | 0.095 | 17/98 | +0.008 | STANDARD |

**UTA @ BUF** · priced 157/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 26.66, exp saves 22.95 (sd 6.35), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.01 (sd 6.59), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.183 | 0.325 | 34/69 | +0.112 | STANDARD |
| Vincent Trocheck: 1+ points | 0.347 | 0.465 | 48/55 | +0.085 | STANDARD |
| Owen Power: 1+ assists | 0.387 | 0.305 | 32/71 | +0.052 | STANDARD |
| Owen Power: 1+ points | 0.437 | 0.365 | 38/65 | +0.040 | STANDARD |
| Josh Norris: 1+ assists | 0.317 | 0.245 | 26/77 | +0.043 | STANDARD |
| Josh Norris: 1+ points | 0.470 | 0.400 | 42/62 | +0.033 | STANDARD |

**DET @ MTL** · priced 148/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.75, exp saves 25.29 (sd 6.65), pull risk 0.047
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.93 (sd 6.36), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Viktor Arvidsson: 1+ goals | 0.277 | 0.180 | 29/93 | -0.027 | STANDARD |
| Chris Kreider: 1+ assists | 0.230 | 0.325 | 34/69 | +0.065 | STANDARD |
| Chris Kreider: 1+ points | 0.425 | 0.515 | 53/50 | +0.057 | STANDARD |
| Andrew Copp: 1+ points | 0.409 | 0.330 | 35/69 | +0.043 | STANDARD |
| Nick Suzuki: 2+ assists | 0.157 | 0.230 | 24/78 | +0.051 | STANDARD |
| Andrew Copp: 1+ assists | 0.282 | 0.210 | 23/81 | +0.039 | STANDARD |

**NSH @ OTT** · priced 151/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.1), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.434 | 0.550 | 56/46 | +0.089 | STANDARD |
| Jordan Spence: 1+ points | 0.432 | 0.325 | 35/70 | +0.066 | STANDARD |
| Jordan Spence: 1+ assists | 0.373 | 0.270 | 29/75 | +0.068 | STANDARD |
| Claude Giroux: 1+ assists | 0.368 | 0.285 | 30/73 | +0.053 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.305 | 0.385 | 40/63 | +0.049 | PRIOR_HEAVY |
| Claude Giroux: 1+ points | 0.510 | 0.430 | 45/59 | +0.043 | STANDARD |

**DAL @ PIT** · priced 157/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.05 (sd 6.21), pull risk 0.064
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.81, exp saves 23.15 (sd 6.41), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.291 | 0.450 | 46/56 | +0.131 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.330 | 0.190 | 22/84 | +0.098 | STANDARD |
| Tyler Seguin: 1+ assists | 0.139 | 0.270 | 29/75 | +0.098 | STANDARD |
| Tyler Seguin: 1+ points | 0.322 | 0.435 | 46/59 | +0.071 | STANDARD |
| Jason Robertson: 2+ points | 0.240 | 0.350 | 36/66 | +0.084 | STANDARD |
| Jason Robertson: 1+ assists | 0.390 | 0.495 | 51/52 | +0.072 | STANDARD |

**CAR @ CHI** · priced 153/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 31.13, exp saves 26.7 (sd 7.37), pull risk 0.077
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.52), pull risk 0.049

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.485 | 49/52 | +0.122 | STANDARD |
| Sebastian Aho: 2+ points | 0.172 | 0.310 | 33/71 | +0.104 | STANDARD |
| Patrick Kane: 1+ assists | 0.298 | 0.415 | 42/59 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.525 | 0.640 | 65/37 | +0.088 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.318 | 0.415 | 43/60 | +0.065 | STANDARD |
| Patrick Kane: 1+ points | 0.477 | 0.570 | 59/45 | +0.056 | STANDARD |

**CBJ @ STL** · priced 163/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.71, exp saves 24.19 (sd 6.51), pull risk 0.048
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.17, exp saves 22.36 (sd 6.26), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.286 | 0.415 | 44/61 | +0.087 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.229 | 0.335 | 35/68 | +0.076 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.436 | 0.535 | 55/48 | +0.066 | STANDARD |
| Matthew Knies: 1+ assists | 0.263 | 0.360 | 37/65 | +0.071 | STANDARD |
| Zach Werenski: 1+ assists | 0.478 | 0.565 | 58/45 | +0.054 | STANDARD |
| Matthew Knies: 1+ points | 0.445 | 0.530 | 55/49 | +0.047 | STANDARD |

**TOR @ COL** · priced 166/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.484 | 0.600 | 61/41 | +0.089 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.518 | 0.630 | 64/38 | +0.085 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.364 | 0.465 | 48/55 | +0.069 | STANDARD |
| Cale Makar: 2+ points | 0.217 | 0.315 | 32/69 | +0.078 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.163 | 0.255 | 26/75 | +0.074 | STANDARD |
| Cale Makar: 2+ assists | 0.144 | 0.235 | 24/77 | +0.074 | STANDARD |

**TBL @ NYI** · priced 146/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 27.33, exp saves 23.71 (sd 6.44), pull risk 0.05
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.5, exp saves 22.82 (sd 6.21), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ assists | 0.260 | 0.495 | 51/52 | +0.202 | STANDARD |
| John Carlson: 1+ points | 0.343 | 0.560 | 57/45 | +0.190 | STANDARD |
| Brayden Schenn: 1+ points | 0.509 | 0.380 | 40/64 | +0.093 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.188 | 0.310 | 33/71 | +0.087 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.471 | 0.570 | 58/44 | +0.072 | STANDARD |
| Brayden Schenn: 2+ points | 0.163 | 0.065 | 11/98 | +0.046 | STANDARD |

**ANA @ CGY** · priced 160/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.92, exp saves 26.72 (sd 7.17), pull risk 0.066
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.24 (sd 6.53), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.220 | 0.090 | 16/98 | +0.050 | STANDARD |
| Aydar Suniev: 1+ goals | 0.194 | 0.085 | 15/98 | +0.035 | PRIOR_HEAVY |
| Leo Carlsson: 1+ assists | 0.391 | 0.495 | 50/51 | +0.081 | STANDARD |
| Jackson LaCombe: 2+ points | 0.217 | 0.115 | 21/98 | -0.005 | STANDARD |
| Beckett Sennecke: 2+ points | 0.235 | 0.135 | 25/98 | -0.028 | STANDARD |
| Mikael Backlund: 1+ goals | 0.212 | 0.120 | 22/98 | -0.020 | STANDARD |

**LAK @ VGK** · priced 157/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.01 (sd 6.25), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.27 (sd 6.63), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.405 | 0.555 | 57/46 | +0.118 | STANDARD |
| Artemi Panarin: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Mitch Marner: 2+ points | 0.190 | 0.325 | 34/69 | +0.105 | STANDARD |
| Jack Eichel: 2+ points | 0.244 | 0.360 | 38/66 | +0.080 | STANDARD |
| Jack Eichel: 1+ assists | 0.443 | 0.545 | 55/46 | +0.080 | STANDARD |
| Artemi Panarin: 1+ points | 0.541 | 0.635 | 64/37 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
