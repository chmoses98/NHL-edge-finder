# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T13:11:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4458 · contracts joined: 2629 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2279, 'OK': 227, 'NO_EDGE': 123}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 324, 'game_early_goal': 14, 'first_goal': 425, 'game_winner': 28, 'player_goals': 744, 'game_overtime': 14, 'player_points': 422, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 2026-10-10T17:00:00Z | T-3h | 0.608 | 0.392 | 0.186 | 5.67 | 3.16 | 2.50 | 217 (25/192) | PROJECTED/PROJECTED |
| VAN @ NJD | 2026-10-10T19:30:00Z | T-6h | 0.612 | 0.388 | 0.168 | 6.46 | 3.60 | 2.86 | 213 (25/188) | PROJECTED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-6h | 0.487 | 0.513 | 0.175 | 6.82 | 3.35 | 3.47 | 217 (25/192) | PROJECTED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-6h | 0.468 | 0.532 | 0.176 | 6.23 | 3.02 | 3.21 | 207 (25/182) | PROJECTED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-6h | 0.536 | 0.464 | 0.174 | 6.31 | 3.27 | 3.04 | 211 (25/186) | PROJECTED/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-6h | 0.599 | 0.401 | 0.173 | 6.22 | 3.41 | 2.81 | 207 (25/182) | PROJECTED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-6h | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 208 (25/183) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-6h | 0.466 | 0.534 | 0.172 | 6.37 | 3.09 | 3.28 | 208 (25/183) | PROJECTED/PROJECTED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-6h | 0.400 | 0.600 | 0.178 | 6.00 | 2.68 | 3.31 | 208 (25/183) | PROJECTED/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-6h | 0.568 | 0.432 | 0.182 | 5.73 | 3.07 | 2.66 | 212 (25/187) | PROJECTED/PROJECTED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-6h | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 218 (25/193) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-6h | 0.488 | 0.512 | 0.184 | 5.63 | 2.78 | 2.85 | 201 (25/176) | PROJECTED/PROJECTED |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-12h | 0.485 | 0.514 | 0.173 | 6.27 | 3.09 | 3.19 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-12h | 0.617 | 0.383 | 0.169 | 6.07 | 3.41 | 2.65 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.488 | 0.375 | 0.397 | 38 | 63 | yes | +0.091 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ3 | game_spread | 0.259 | 0.365 | 0.342 | 37 | 64 | no | +0.084 | OK |
| KXNHLGAME-26OCT10VANNJ-VAN | game_winner | 0.388 | 0.285 | 0.304 | 29 | 72 | yes | +0.083 | OK |
| KXNHLGAME-26OCT10VANNJ-NJ | game_winner | 0.612 | 0.715 | 0.696 | 72 | 29 | no | +0.083 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.512 | 0.615 | 0.595 | 62 | 39 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.372 | 0.475 | 0.454 | 48 | 53 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ2 | game_spread | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.237 | 0.335 | 0.314 | 34 | 67 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.161 | 0.255 | 0.234 | 26 | 75 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.600 | 0.695 | 0.677 | 70 | 31 | no | +0.075 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.400 | 0.305 | 0.323 | 31 | 70 | yes | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.551 | 0.655 | 0.635 | 67 | 36 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.330 | 0.435 | 0.413 | 45 | 58 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.283 | 0.375 | 0.356 | 38 | 63 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.333 | 0.240 | 0.257 | 25 | 77 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN3 | team_total | 0.543 | 0.455 | 0.473 | 46 | 55 | yes | +0.066 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.065 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.532 | 0.445 | 0.462 | 45 | 56 | yes | +0.065 | OK |
| KXNHLGAME-26OCT10EDMSJ-SJ | game_winner | 0.487 | 0.405 | 0.421 | 41 | 60 | yes | +0.060 | OK |
| KXNHLGAME-26OCT10EDMSJ-EDM | game_winner | 0.513 | 0.595 | 0.579 | 60 | 41 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.434 | 0.520 | 0.503 | 53 | 49 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.202 | 0.135 | 0.147 | 14 | 87 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.409 | 0.330 | 0.345 | 34 | 68 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.265 | 0.195 | 0.208 | 20 | 81 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.234 | 0.305 | 0.290 | 31 | 70 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.628 | 0.550 | 0.566 | 56 | 46 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.230 | 0.165 | 0.177 | 17 | 84 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 | team_total | 0.463 | 0.540 | 0.525 | 55 | 47 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.446 | 0.375 | 0.389 | 38 | 63 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.771 | 0.840 | 0.828 | 85 | 17 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.657 | 0.730 | 0.716 | 74 | 28 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ5 | team_total | 0.296 | 0.365 | 0.351 | 37 | 64 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.545 | 0.559 | 55 | 46 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.309 | 0.245 | 0.257 | 25 | 76 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-7 | game_total | 0.367 | 0.435 | 0.421 | 44 | 57 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 | team_total | 0.497 | 0.575 | 0.560 | 59 | 44 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.260 | 0.325 | 0.311 | 33 | 68 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.172 | 0.110 | 0.121 | 12 | 90 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.154 | 0.215 | 0.202 | 22 | 79 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.430 | 0.444 | 44 | 58 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ5 | team_total | 0.255 | 0.195 | 0.206 | 20 | 81 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.164 | 0.230 | 0.216 | 24 | 78 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI2 | team_total | 0.704 | 0.770 | 0.758 | 78 | 24 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM3 | game_spread | 0.195 | 0.255 | 0.242 | 26 | 75 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.243 | 0.315 | 0.300 | 33 | 70 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ3 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.766 | 0.705 | 0.718 | 71 | 30 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI4 | team_total | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.188 | 0.245 | 0.233 | 25 | 76 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.165 | 0.175 | 17 | 84 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.305 | 0.318 | 32 | 71 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.112 | 0.065 | 0.073 | 7 | 94 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-5 | game_total | 0.710 | 0.765 | 0.755 | 77 | 24 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10CBJSTL-CBJ4 | team_total | 0.289 | 0.345 | 0.333 | 35 | 66 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.140 | 0.150 | 15 | 87 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-SJ2 | game_spread | 0.277 | 0.225 | 0.235 | 23 | 78 | yes | +0.035 | OK |
| KXNHLGAME-26OCT10TORCOL-TOR | game_winner | 0.290 | 0.345 | 0.334 | 35 | 66 | no | +0.034 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.710 | 0.655 | 0.666 | 66 | 35 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM2 | game_spread | 0.310 | 0.365 | 0.354 | 37 | 64 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-5 | game_total | 0.703 | 0.755 | 0.745 | 76 | 25 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ3 | team_total | 0.703 | 0.760 | 0.749 | 77 | 25 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.370 | 0.425 | 0.414 | 43 | 58 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.296 | 0.240 | 0.251 | 25 | 77 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT10PHIBOS-PHI3 | game_spread | 0.099 | 0.145 | 0.134 | 15 | 86 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.695 | 0.745 | 0.735 | 75 | 26 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-4 | game_total | 0.809 | 0.855 | 0.847 | 86 | 15 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.461 | 0.520 | 0.508 | 53 | 49 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT10CBJSTL-6 | game_total | 0.481 | 0.535 | 0.524 | 54 | 47 | no | +0.031 | OK |
| KXNHLGAME-26OCT10PHIBOS-BOS | game_winner | 0.608 | 0.555 | 0.566 | 56 | 45 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL3 | game_spread | 0.366 | 0.315 | 0.325 | 32 | 69 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.314 | 0.365 | 0.354 | 37 | 64 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.507 | 0.450 | 0.461 | 46 | 56 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ3 | team_total | 0.656 | 0.595 | 0.608 | 61 | 42 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 | team_total | 0.405 | 0.345 | 0.357 | 36 | 67 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.188 | 0.145 | 0.153 | 15 | 86 | yes | +0.029 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.585 | 0.575 | 59 | 42 | no | +0.029 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.466 | 0.415 | 0.425 | 42 | 59 | yes | +0.029 | OK |

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
| TBL @ NYI | 0.488 | 0.509 | 0.184 | 0.219 | 5.63 | 5.98 | 0.956/0.957 | KXNHLTOTAL-26OCT10TBNYI-7 +0.066 |
| ANA @ CGY | 0.485 | 0.499 | 0.173 | 0.215 | 6.27 | 6.51 | 0.997/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.617 | 0.588 | 0.169 | 0.223 | 6.07 | 5.96 | 1.003/0.992 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 43 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 13c · p 0.1788 (adj 0.1641) · $2.18 · thesis PHI:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.6675 (adj 0.6519) · $5.33 · thesis BOS:SUPPRESSED
- Travis Sanheim: 1+ goals YES @ 7c · p 0.0959 (adj 0.0882) · $1.01 · thesis PHI:OFFENSE_4PLUS
- David Jiricek: 1+ assists NO @ 75c · p 0.8189 (adj 0.777) · $6.14 · thesis PHI:SUPPRESSED
- Nico Hischier: 1+ goals NO @ 66c · p 0.7368 (adj 0.7151) · $4.88 · thesis NJD:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 58c · p 0.6534 (adj 0.6325) · $4.4 · thesis NJD:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 51c · p 0.6658 (adj 0.5613) · $2.12 · thesis VAN:WINS
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7847 (adj 0.6874) · $3.59 · thesis VAN:WINS
- Alex Formenton: 1+ goals YES @ 13c · p 0.2068 (adj 0.1864) · $3.93 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1131 (adj 0.1048) · $1.61 · thesis EDM:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 18c · p 0.2366 (adj 0.2162) · $2.28 · thesis SJS:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 68c · p 0.8302 (adj 0.7196) · $6.19 · thesis EDM:SUPPRESSED
- Michael McCarron: 1+ goals YES @ 8c · p 0.1288 (adj 0.1166) · $2.38 · thesis MIN:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1394 (adj 0.127) · $2.44 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 18c · p 0.2443 (adj 0.2282) · $3.39 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1479 (adj 0.1334) · $2.08 · thesis FLA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 69c · p 0.8167 (adj 0.7213) · $5.67 · thesis UTA:SUPPRESSED
- Tage Thompson: 1+ goals NO @ 62c · p 0.6671 (adj 0.6516) · $3.57 · thesis BUF:SUPPRESSED
- Owen Power: 1+ assists YES @ 32c · p 0.387 (adj 0.346) · $1.4 · thesis BUF:OFFENSE_4PLUS
- Nick Suzuki: 2+ assists NO @ 78c · p 0.8434 (adj 0.8092) · $5.18 · thesis MTL:SUPPRESSED
- Chris Kreider: 1+ assists NO @ 69c · p 0.7702 (adj 0.7226) · $4.1 · thesis MTL:SUPPRESSED
- Josh Anderson: 1+ goals YES @ 17c · p 0.201 (adj 0.192) · $1.23 · thesis MTL:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 23c · p 0.282 (adj 0.2677) · $2.53 · thesis NSH:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 17c · p 0.2116 (adj 0.1975) · $1.6 · thesis OTT:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 19c · p 0.2296 (adj 0.2185) · $1.8 · thesis OTT:OFFENSE_4PLUS
- Carter Yakemchuk: 1+ assists NO @ 69c · p 0.7633 (adj 0.7167) · $4.15 · thesis OTT:SUPPRESSED
- Roope Hintz: 1+ assists NO @ 56c · p 0.7085 (adj 0.6055) · $4.99 · thesis DAL:SUPPRESSED
- Dallas wins by over 1.5 goals NO @ 64c · p 0.7223 (adj 0.6786) · $4.49 · thesis PIT:WINS
- Evgeni Malkin: 1+ assists NO @ 59c · p 0.6581 (adj 0.6191) · $3.03 · thesis PIT:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 13c · p 0.1704 (adj 0.1578) · $1.5 · thesis CHI:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 67c · p 0.7553 (adj 0.7102) · $6.19 · thesis GAME:TIGHT
- Patrick Kane: 1+ assists NO @ 59c · p 0.7018 (adj 0.6259) · $5.5 · thesis CHI:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 27c · p 0.3131 (adj 0.2998) · $1.65 · thesis CHI:OFFENSE_4PLUS
- Conor Garland: 1+ goals NO @ 83c · p 0.8896 (adj 0.8722) · $4.0 · thesis CBJ:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 65c · p 0.7374 (adj 0.6887) · $3.08 · thesis CBJ:SUPPRESSED
- Adam Fantilli: 1+ assists NO @ 61c · p 0.6872 (adj 0.6461) · $2.2 · thesis CBJ:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1654 (adj 0.1503) · $1.82 · thesis COL:WINS_BY_2PLUS
- Martin Necas: 1+ goals NO @ 62c · p 0.6677 (adj 0.6545) · $3.78 · thesis COL:SUPPRESSED
- Cale Makar: 1+ goals NO @ 77c · p 0.8061 (adj 0.7933) · $3.97 · thesis COL:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 63c · p 0.6996 (adj 0.6573) · $2.41 · thesis TOR:SUPPRESSED
- John Carlson: 1+ assists NO @ 51c · p 0.7367 (adj 0.5828) · $5.72 · thesis TBL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2634 (adj 0.2426) · $3.03 · thesis NYI:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 75c · p 0.8415 (adj 0.7933) · $5.72 · thesis NYI:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BOS** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.33, exp saves 23.04 (sd 6.29), pull risk 0.051
- PHI net: Dan Vladar (PROJECTED) exp shots 27.07, exp saves 23.38 (sd 6.46), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Frederic Brunet: 1+ points | 0.239 | 0.445 | 46/57 | +0.174 | PRIOR_HEAVY |
| Frederic Brunet: 1+ assists | 0.188 | 0.380 | 40/64 | +0.156 | PRIOR_HEAVY |
| JJ Peterka: 1+ assists | 0.177 | 0.310 | 32/70 | +0.108 | STANDARD |
| David Jiricek: 1+ points | 0.217 | 0.330 | 34/68 | +0.088 | STANDARD |
| JJ Peterka: 1+ points | 0.354 | 0.465 | 48/55 | +0.079 | STANDARD |
| David Jiricek: 1+ assists | 0.181 | 0.265 | 28/75 | +0.056 | STANDARD |

**VAN @ NJD** · priced 157/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.83, exp saves 21.68 (sd 5.96), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.9 (sd 7.21), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.235 | 0.440 | 45/57 | +0.178 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.615 | 63/40 | +0.171 | STANDARD |
| Jack Hughes: 2+ points | 0.244 | 0.430 | 45/59 | +0.149 | STANDARD |
| Luke Evangelista: 1+ points | 0.398 | 0.570 | 59/45 | +0.135 | STANDARD |
| Jack Hughes: 2+ assists | 0.097 | 0.235 | 25/78 | +0.111 | STANDARD |
| Jack Hughes: 1+ points | 0.615 | 0.745 | 78/29 | +0.081 | STANDARD |

**EDM @ SJS** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 28.97, exp saves 24.77 (sd 6.93), pull risk 0.081
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.61 (sd 6.41), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.170 | 0.340 | 36/68 | +0.135 | STANDARD |
| Connor McDavid: 2+ points | 0.389 | 0.535 | 55/48 | +0.114 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.476 | 0.610 | 62/40 | +0.107 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.379 | 0.250 | 28/78 | +0.085 | STANDARD |
| Tyler Toffoli: 1+ points | 0.544 | 0.415 | 44/61 | +0.087 | STANDARD |
| Leon Draisaitl: 2+ points | 0.335 | 0.460 | 48/56 | +0.088 | STANDARD |

**MIN @ FLA** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.41, exp saves 23.59 (sd 6.55), pull risk 0.069
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.73), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 1+ points | 0.390 | 0.215 | 42/99 | -0.047 | STANDARD |
| Ryan Hartman: 1+ points | 0.509 | 0.360 | 38/66 | +0.113 | STANDARD |
| Brady Tkachuk: 1+ points | 0.441 | 0.580 | 60/44 | +0.102 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.242 | 0.375 | 39/64 | +0.102 | STANDARD |
| Quinn Hughes: 2+ points | 0.263 | 0.135 | 25/98 | -0.000 | STANDARD |
| Ryan Hartman: 1+ assists | 0.348 | 0.230 | 25/79 | +0.085 | STANDARD |

**UTA @ BUF** · priced 157/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 26.66, exp saves 22.95 (sd 6.35), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.01 (sd 6.59), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.183 | 0.330 | 35/69 | +0.112 | STANDARD |
| Vincent Trocheck: 1+ points | 0.347 | 0.465 | 48/55 | +0.085 | STANDARD |
| Anders Lee: 1+ goals | 0.233 | 0.120 | 22/98 | +0.001 | STANDARD |
| Jiri Kulich: 1+ goals | 0.211 | 0.105 | 19/98 | +0.011 | STANDARD |
| Josh Norris: 1+ goals | 0.225 | 0.120 | 22/98 | -0.007 | STANDARD |
| Owen Power: 1+ assists | 0.387 | 0.305 | 32/71 | +0.052 | STANDARD |

**DET @ MTL** · priced 148/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.75, exp saves 25.29 (sd 6.65), pull risk 0.047
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.93 (sd 6.36), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex DeBrincat: 1+ goals | 0.349 | 0.190 | 34/96 | -0.006 | STANDARD |
| Nick Suzuki: 1+ points | 0.679 | 0.530 | 74/68 | -0.075 | STANDARD |
| Viktor Arvidsson: 1+ goals | 0.277 | 0.150 | 28/98 | -0.017 | STANDARD |
| Dylan Larkin: 1+ goals | 0.289 | 0.170 | 32/98 | -0.046 | STANDARD |
| Emmitt Finnie: 1+ goals | 0.197 | 0.095 | 17/98 | +0.017 | STANDARD |
| Chris Kreider: 1+ assists | 0.230 | 0.325 | 34/69 | +0.065 | STANDARD |

**NSH @ OTT** · priced 151/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.1), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ points | 0.627 | 0.345 | 67/98 | -0.059 | STANDARD |
| Jordan Spence: 1+ assists | 0.373 | 0.255 | 28/77 | +0.079 | STANDARD |
| Tim Stutzle: 1+ assists | 0.434 | 0.550 | 56/46 | +0.089 | STANDARD |
| Jordan Spence: 1+ points | 0.432 | 0.320 | 34/70 | +0.076 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.305 | 0.400 | 42/62 | +0.059 | PRIOR_HEAVY |
| Fabian Zetterlund: 1+ goals | 0.200 | 0.105 | 19/98 | -0.000 | STANDARD |

**DAL @ PIT** · priced 157/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.05 (sd 6.21), pull risk 0.064
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.81, exp saves 23.15 (sd 6.41), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kris Letang: 1+ points | 0.339 | 0.180 | 34/98 | -0.017 | STANDARD |
| Roope Hintz: 1+ assists | 0.291 | 0.450 | 46/56 | +0.131 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.330 | 0.190 | 22/84 | +0.098 | STANDARD |
| Tyler Seguin: 1+ assists | 0.139 | 0.265 | 29/76 | +0.088 | STANDARD |
| Jason Robertson: 1+ points | 0.610 | 0.485 | 69/72 | -0.095 | STANDARD |
| Tyler Seguin: 1+ points | 0.322 | 0.430 | 45/59 | +0.071 | STANDARD |

**CAR @ CHI** · priced 153/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 31.13, exp saves 26.7 (sd 7.37), pull risk 0.077
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.52), pull risk 0.049

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.480 | 49/53 | +0.112 | STANDARD |
| Sebastian Aho: 2+ points | 0.172 | 0.310 | 33/71 | +0.104 | STANDARD |
| Sebastian Aho: 1+ points | 0.525 | 0.645 | 65/36 | +0.099 | STANDARD |
| Patrick Kane: 1+ assists | 0.298 | 0.415 | 42/59 | +0.095 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.318 | 0.415 | 43/60 | +0.065 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.521 | 0.610 | 63/41 | +0.052 | STANDARD |

**CBJ @ STL** · priced 159/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.71, exp saves 24.19 (sd 6.51), pull risk 0.048
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.17, exp saves 22.36 (sd 6.26), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonatan Berggren: 1+ assists | 0.273 | 0.140 | 27/99 | -0.011 | STANDARD |
| Adam Jiricek: 1+ points | 0.286 | 0.415 | 44/61 | +0.087 | PRIOR_HEAVY |
| Charlie Coyle: 1+ goals | 0.241 | 0.115 | 21/98 | +0.020 | STANDARD |
| Adam Jiricek: 1+ assists | 0.229 | 0.335 | 35/68 | +0.076 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.436 | 0.535 | 55/48 | +0.066 | STANDARD |
| Matthew Knies: 1+ assists | 0.263 | 0.360 | 37/65 | +0.071 | STANDARD |

**TOR @ COL** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Martin Necas: 1+ points | 0.646 | 0.350 | 68/98 | -0.050 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.518 | 0.635 | 65/38 | +0.085 | STANDARD |
| Cale Makar: 1+ assists | 0.484 | 0.600 | 61/41 | +0.089 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.364 | 0.480 | 50/54 | +0.079 | STANDARD |
| Cale Makar: 1+ points | 0.585 | 0.470 | 68/74 | -0.110 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.163 | 0.270 | 29/75 | +0.074 | STANDARD |

**TBL @ NYI** · priced 145/150 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.33, exp saves 23.67 (sd 6.45), pull risk 0.054
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.5, exp saves 22.81 (sd 6.21), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ points | 0.645 | 0.360 | 70/98 | -0.070 | STANDARD |
| John Carlson: 1+ assists | 0.263 | 0.500 | 51/51 | +0.209 | STANDARD |
| John Carlson: 1+ points | 0.346 | 0.555 | 57/46 | +0.177 | STANDARD |
| Brayden Schenn: 1+ points | 0.511 | 0.375 | 39/64 | +0.104 | STANDARD |
| Victor Eklund: 1+ goals | 0.221 | 0.105 | 19/98 | +0.020 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ assists | 0.189 | 0.300 | 33/73 | +0.068 | STANDARD |

**ANA @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.92, exp saves 26.72 (sd 7.17), pull risk 0.066
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.24 (sd 6.53), pull risk 0.067

**LAK @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.01 (sd 6.25), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.27 (sd 6.63), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
