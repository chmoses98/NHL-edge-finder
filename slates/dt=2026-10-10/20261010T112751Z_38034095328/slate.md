# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T11:27:51Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4308 · contracts joined: 2479 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2129, 'OK': 219, 'NO_EDGE': 131}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 303, 'game_early_goal': 14, 'first_goal': 389, 'game_winner': 28, 'player_goals': 682, 'game_overtime': 14, 'player_points': 391, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 2026-10-10T17:00:00Z | T-3h | 0.611 | 0.389 | 0.179 | 5.70 | 3.18 | 2.52 | 217 (25/192) | PROJECTED/PROJECTED |
| VAN @ NJD | 2026-10-10T19:30:00Z | T-6h | 0.616 | 0.385 | 0.167 | 6.49 | 3.62 | 2.87 | 213 (25/188) | PROJECTED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-6h | 0.484 | 0.516 | 0.168 | 6.85 | 3.37 | 3.48 | 217 (25/192) | PROJECTED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-6h | 0.468 | 0.532 | 0.165 | 6.26 | 3.03 | 3.23 | 207 (25/182) | PROJECTED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-6h | 0.535 | 0.465 | 0.173 | 6.35 | 3.29 | 3.06 | 211 (25/186) | PROJECTED/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-6h | 0.565 | 0.435 | 0.172 | 6.27 | 3.34 | 2.93 | 207 (25/182) | PROJECTED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-6h | 0.571 | 0.429 | 0.172 | 6.56 | 3.51 | 3.05 | 208 (25/183) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-6h | 0.515 | 0.485 | 0.174 | 6.44 | 3.27 | 3.17 | 208 (25/183) | PROJECTED/PROJECTED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-6h | 0.398 | 0.602 | 0.174 | 6.03 | 2.70 | 3.33 | 208 (25/183) | PROJECTED/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-6h | 0.535 | 0.465 | 0.181 | 5.81 | 3.01 | 2.80 | 212 (25/187) | PROJECTED/PROJECTED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-6h | 0.712 | 0.288 | 0.146 | 6.87 | 4.17 | 2.70 | 218 (25/193) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-12h | 0.486 | 0.514 | 0.180 | 5.67 | 2.80 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-12h | 0.466 | 0.534 | 0.175 | 6.33 | 3.06 | 3.27 | 51 (25/26) | PROJECTED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-12h | 0.620 | 0.380 | 0.173 | 6.11 | 3.44 | 2.67 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.486 | 0.375 | 0.396 | 38 | 63 | yes | +0.089 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ3 | game_spread | 0.260 | 0.365 | 0.343 | 37 | 64 | no | +0.084 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.234 | 0.335 | 0.313 | 34 | 67 | no | +0.080 | OK |
| KXNHLGAME-26OCT10VANNJ-VAN | game_winner | 0.385 | 0.285 | 0.304 | 29 | 72 | yes | +0.080 | OK |
| KXNHLGAME-26OCT10VANNJ-NJ | game_winner | 0.616 | 0.715 | 0.696 | 72 | 29 | no | +0.080 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.372 | 0.475 | 0.454 | 48 | 53 | no | +0.080 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.485 | 0.585 | 0.565 | 59 | 42 | no | +0.078 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.515 | 0.415 | 0.435 | 42 | 59 | yes | +0.078 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ2 | game_spread | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.602 | 0.695 | 0.677 | 70 | 31 | no | +0.073 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.398 | 0.305 | 0.323 | 31 | 70 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.213 | 0.305 | 0.285 | 31 | 70 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.333 | 0.245 | 0.261 | 25 | 76 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.415 | 0.320 | 0.338 | 33 | 69 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.334 | 0.435 | 0.414 | 45 | 58 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.285 | 0.375 | 0.356 | 38 | 63 | no | +0.069 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.514 | 0.605 | 0.587 | 61 | 40 | no | +0.069 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.468 | 0.555 | 0.538 | 56 | 45 | no | +0.065 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.532 | 0.445 | 0.462 | 45 | 56 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.163 | 0.250 | 0.230 | 26 | 76 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN3 | team_total | 0.550 | 0.460 | 0.478 | 47 | 55 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.305 | 0.225 | 0.240 | 23 | 78 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.342 | 0.425 | 0.408 | 43 | 58 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.314 | 0.235 | 0.250 | 24 | 77 | yes | +0.061 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.166 | 0.245 | 0.227 | 25 | 76 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.554 | 0.645 | 0.627 | 66 | 37 | no | +0.060 | OK |
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.435 | 0.355 | 0.371 | 36 | 65 | yes | +0.059 | OK |
| KXNHLGAME-26OCT10DETMTL-MTL | game_winner | 0.565 | 0.645 | 0.629 | 65 | 36 | no | +0.059 | OK |
| KXNHLGAME-26OCT10EDMSJ-SJ | game_winner | 0.484 | 0.405 | 0.421 | 41 | 60 | yes | +0.057 | OK |
| KXNHLGAME-26OCT10EDMSJ-EDM | game_winner | 0.516 | 0.595 | 0.579 | 60 | 41 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.318 | 0.245 | 0.259 | 25 | 76 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.438 | 0.520 | 0.503 | 53 | 49 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.622 | 0.545 | 0.561 | 55 | 46 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.632 | 0.545 | 0.563 | 56 | 47 | yes | +0.055 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.510 | 0.430 | 0.446 | 44 | 58 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.640 | 0.555 | 0.572 | 57 | 46 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.449 | 0.375 | 0.389 | 38 | 63 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.232 | 0.155 | 0.168 | 17 | 86 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.200 | 0.135 | 0.146 | 14 | 87 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.231 | 0.165 | 0.177 | 17 | 84 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.245 | 0.320 | 0.304 | 33 | 69 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.151 | 0.215 | 0.201 | 22 | 79 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.659 | 0.730 | 0.717 | 74 | 28 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.174 | 0.110 | 0.121 | 12 | 90 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL4 | team_total | 0.614 | 0.545 | 0.559 | 55 | 46 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 | team_total | 0.423 | 0.345 | 0.360 | 36 | 67 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.770 | 0.705 | 0.719 | 71 | 30 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 | team_total | 0.467 | 0.545 | 0.530 | 56 | 47 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM3 | game_spread | 0.192 | 0.255 | 0.241 | 26 | 75 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.261 | 0.325 | 0.311 | 33 | 68 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.591 | 0.520 | 0.534 | 53 | 49 | yes | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI4 | team_total | 0.252 | 0.320 | 0.306 | 33 | 69 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.440 | 0.515 | 0.500 | 53 | 50 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.378 | 0.305 | 0.319 | 32 | 71 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.778 | 0.840 | 0.829 | 85 | 17 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.166 | 0.230 | 0.216 | 24 | 78 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ3 | team_total | 0.659 | 0.590 | 0.604 | 60 | 42 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.201 | 0.140 | 0.151 | 15 | 87 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.508 | 0.445 | 0.458 | 45 | 56 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT10DETMTL-DET2 | game_spread | 0.231 | 0.175 | 0.185 | 18 | 83 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.262 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI2 | team_total | 0.707 | 0.775 | 0.762 | 79 | 24 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT3 | game_spread | 0.188 | 0.135 | 0.145 | 14 | 87 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN2 | team_total | 0.830 | 0.770 | 0.783 | 78 | 24 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-DET3 | team_total | 0.565 | 0.500 | 0.513 | 51 | 51 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.112 | 0.065 | 0.073 | 7 | 94 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM2 | game_spread | 0.306 | 0.365 | 0.353 | 37 | 64 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL6 | team_total | 0.238 | 0.175 | 0.186 | 19 | 84 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.515 | 0.450 | 0.463 | 46 | 56 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-SJ2 | game_spread | 0.279 | 0.225 | 0.235 | 23 | 78 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT5 | team_total | 0.237 | 0.180 | 0.191 | 19 | 83 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI4 | team_total | 0.300 | 0.240 | 0.251 | 25 | 77 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL3 | team_total | 0.659 | 0.720 | 0.708 | 73 | 29 | no | +0.036 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.712 | 0.655 | 0.667 | 66 | 35 | yes | +0.036 | OK |
| KXNHLGAME-26OCT10TORCOL-TOR | game_winner | 0.288 | 0.345 | 0.333 | 35 | 66 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL5 | team_total | 0.249 | 0.310 | 0.297 | 32 | 70 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.195 | 0.145 | 0.154 | 15 | 86 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT10TORCOL-8 | game_total | 0.359 | 0.305 | 0.316 | 31 | 70 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 | team_total | 0.410 | 0.345 | 0.358 | 36 | 67 | yes | +0.034 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 0.611 | 0.568 | 0.179 | 0.222 | 5.70 | 5.98 | 0.968/0.993 | KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 +0.068 |
| VAN @ NJD | 0.616 | 0.561 | 0.167 | 0.220 | 6.49 | 6.26 | 0.987/1.025 | KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 -0.064 |
| EDM @ SJS | 0.484 | 0.481 | 0.168 | 0.210 | 6.85 | 6.88 | 1.026/1.022 | KXNHLTEAMTOTAL-26OCT10EDMSJ-EDM4 +0.009 |
| MIN @ FLA | 0.468 | 0.469 | 0.165 | 0.218 | 6.26 | 6.42 | 1.008/0.995 | KXNHLTOTAL-26OCT10MINFLA-7 +0.031 |
| UTA @ BUF | 0.535 | 0.513 | 0.173 | 0.218 | 6.35 | 6.45 | 0.998/0.992 | KXNHLTEAMTOTAL-26OCT10UTABUF-UTA4 +0.032 |
| DET @ MTL | 0.565 | 0.588 | 0.172 | 0.217 | 6.27 | 6.34 | 0.953/1.023 | KXNHLSPREAD-26OCT10DETMTL-MTL3 +0.031 |
| NSH @ OTT | 0.571 | 0.595 | 0.172 | 0.213 | 6.56 | 6.39 | 0.998/1.000 | KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 -0.039 |
| DAL @ PIT | 0.515 | 0.539 | 0.174 | 0.222 | 6.44 | 6.49 | 1.033/0.986 | KXNHLSPREAD-26OCT10DALPIT-DAL2 -0.026 |
| CAR @ CHI | 0.398 | 0.421 | 0.174 | 0.214 | 6.03 | 6.41 | 1.003/0.989 | KXNHLTOTAL-26OCT10CARCHI-7 +0.067 |
| CBJ @ STL | 0.535 | 0.523 | 0.181 | 0.224 | 5.81 | 6.11 | 0.993/0.964 | KXNHLTOTAL-26OCT10CBJSTL-7 +0.057 |
| TOR @ COL | 0.712 | 0.678 | 0.146 | 0.196 | 6.87 | 6.58 | 0.976/0.965 | KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 -0.058 |
| TBL @ NYI | 0.486 | 0.510 | 0.180 | 0.224 | 5.67 | 5.98 | 0.956/0.957 | KXNHLTOTAL-26OCT10TBNYI-7 +0.057 |
| ANA @ CGY | 0.466 | 0.475 | 0.175 | 0.222 | 6.33 | 6.51 | 0.997/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.037 |
| LAK @ VGK | 0.620 | 0.593 | 0.173 | 0.211 | 6.11 | 5.95 | 1.003/0.992 | KXNHLTEAMTOTAL-26OCT10LAVGK-VGK4 -0.036 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 34 recommended · full analysis in card.md / packet.json `thesis_card`

- Travis Sanheim: 1+ goals YES @ 6c · p 0.098 (adj 0.0872) · $2.3 · thesis PHI:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.6727 (adj 0.6558) · $6.1 · thesis BOS:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 14c · p 0.1827 (adj 0.1683) · $2.24 · thesis PHI:OFFENSE_4PLUS
- JJ Peterka: 1+ goals NO @ 74c · p 0.7897 (adj 0.7748) · $6.8 · thesis BOS:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1893 (adj 0.1745) · $3.89 · thesis VAN:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 57c · p 0.7625 (adj 0.6309) · $8.61 · thesis NJD:SUPPRESSED
- New Jersey wins by over 1.5 goals NO @ 51c · p 0.6631 (adj 0.5603) · $2.23 · thesis VAN:WINS
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7812 (adj 0.6862) · $5.73 · thesis VAN:WINS
- Alex Formenton: 1+ goals YES @ 13c · p 0.1985 (adj 0.1789) · $4.71 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1175 (adj 0.1081) · $2.71 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 31c · p 0.4706 (adj 0.3597) · $6.09 · thesis EDM:SUPPRESSED
- Collin Graf: 1+ goals YES @ 18c · p 0.2391 (adj 0.2156) · $2.91 · thesis SJS:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1412 (adj 0.1197) · $2.17 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1507 (adj 0.128) · $2.39 · thesis FLA:OFFENSE_4PLUS
- Anton Lundell: 1+ goals YES @ 17c · p 0.2196 (adj 0.2022) · $3.09 · thesis FLA:OFFENSE_4PLUS
- Minnesota wins YES @ 45c · p 0.5265 (adj 0.4858) · $4.85 · thesis MIN:WINS
- Montreal wins by over 2.5 goals NO @ 70c · p 0.762 (adj 0.7285) · $5.63 · thesis GAME:TIGHT
- Michael Amadio: 1+ goals YES @ 16c · p 0.216 (adj 0.1983) · $3.45 · thesis OTT:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 23c · p 0.2778 (adj 0.2621) · $2.75 · thesis NSH:OFFENSE_4PLUS
- Claude Giroux: 1+ goals YES @ 19c · p 0.2291 (adj 0.2181) · $2.2 · thesis OTT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3368 (adj 0.3138) · $4.44 · thesis PIT:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 76c · p 0.8498 (adj 0.8024) · $7.83 · thesis PIT:WINS
- Roope Hintz: 1+ assists NO @ 56c · p 0.7157 (adj 0.6112) · $7.45 · thesis DAL:SUPPRESSED
- Pittsburgh wins by over 1.5 goals YES @ 23c · p 0.3185 (adj 0.2717) · $1.79 · thesis PIT:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 67c · p 0.7503 (adj 0.7077) · $4.79 · thesis GAME:TIGHT
- Chicago over 1.5 goals scored YES @ 71c · p 0.7813 (adj 0.7431) · $5.85 · thesis CHI:WINS
- Sebastian Aho: 1+ goals NO @ 67c · p 0.7167 (adj 0.7) · $4.38 · thesis CAR:SUPPRESSED
- Andrei Svechnikov: 1+ goals NO @ 65c · p 0.6954 (adj 0.6791) · $3.71 · thesis CAR:SUPPRESSED
- Conor Garland: 1+ goals NO @ 84c · p 0.8836 (adj 0.869) · $8.61 · thesis CBJ:SUPPRESSED
- Zachary L'Heureux: 1+ goals YES @ 11c · p 0.1667 (adj 0.1438) · $2.79 · thesis COL:OFFENSE_4PLUS
- Martin Necas: 1+ goals NO @ 62c · p 0.674 (adj 0.6568) · $5.94 · thesis COL:SUPPRESSED
- New York I wins by over 1.5 goals YES @ 21c · p 0.2868 (adj 0.2459) · $1.68 · thesis NYI:WINS_BY_2PLUS
- New York I wins YES @ 38c · p 0.5144 (adj 0.4238) · $1.28 · thesis NYI:WINS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8403 (adj 0.7952) · $8.61 · thesis NYI:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BOS** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.33, exp saves 23.05 (sd 6.3), pull risk 0.051
- PHI net: Dan Vladar (PROJECTED) exp shots 27.07, exp saves 23.36 (sd 6.54), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Frederic Brunet: 1+ points | 0.241 | 0.445 | 47/58 | +0.162 | PRIOR_HEAVY |
| Frederic Brunet: 1+ assists | 0.188 | 0.365 | 39/66 | +0.136 | PRIOR_HEAVY |
| JJ Peterka: 1+ assists | 0.176 | 0.305 | 31/70 | +0.110 | STANDARD |
| JJ Peterka: 1+ points | 0.348 | 0.465 | 48/55 | +0.084 | STANDARD |
| David Jiricek: 1+ points | 0.219 | 0.325 | 35/70 | +0.067 | STANDARD |
| Morgan Geekie: 2+ points | 0.197 | 0.105 | 20/99 | -0.014 | STANDARD |

**VAN @ NJD** · priced 157/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.83, exp saves 21.7 (sd 5.96), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.86 (sd 7.24), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.237 | 0.440 | 45/57 | +0.175 | STANDARD |
| Jack Hughes: 1+ assists | 0.413 | 0.615 | 63/40 | +0.170 | STANDARD |
| Jack Hughes: 2+ points | 0.255 | 0.435 | 46/59 | +0.138 | STANDARD |
| Luke Evangelista: 1+ points | 0.395 | 0.565 | 59/46 | +0.128 | STANDARD |
| Marco Rossi: 1+ goals | 0.257 | 0.125 | 19/94 | +0.056 | STANDARD |
| Evan Rodrigues: 1+ points | 0.304 | 0.420 | 44/60 | +0.079 | STANDARD |

**EDM @ SJS** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 28.97, exp saves 24.81 (sd 6.94), pull risk 0.081
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.62 (sd 6.38), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.529 | 0.700 | 71/31 | +0.146 | STANDARD |
| Connor McDavid: 2+ assists | 0.166 | 0.330 | 36/70 | +0.119 | STANDARD |
| Tyler Toffoli: 1+ points | 0.547 | 0.400 | 44/64 | +0.090 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.464 | 0.610 | 62/40 | +0.119 | STANDARD |
| Connor McDavid: 2+ points | 0.383 | 0.515 | 54/51 | +0.089 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.376 | 0.250 | 28/78 | +0.082 | STANDARD |

**MIN @ FLA** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.41, exp saves 23.61 (sd 6.57), pull risk 0.069
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.94 (sd 6.73), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Max Shabanov: 1+ points | 0.385 | 0.225 | 44/99 | -0.072 | STANDARD |
| Ryan Hartman: 1+ goals | 0.243 | 0.095 | 18/99 | +0.053 | STANDARD |
| Ryan Hartman: 1+ points | 0.507 | 0.360 | 38/66 | +0.111 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.244 | 0.375 | 39/64 | +0.100 | STANDARD |
| Ryan Hartman: 1+ assists | 0.344 | 0.220 | 25/81 | +0.081 | STANDARD |
| Brady Tkachuk: 1+ points | 0.446 | 0.565 | 59/46 | +0.077 | STANDARD |

**UTA @ BUF** · priced 157/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 26.66, exp saves 22.98 (sd 6.37), pull risk 0.065
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 23.98 (sd 6.66), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.181 | 0.330 | 36/70 | +0.104 | STANDARD |
| Zach Benson: 1+ goals | 0.251 | 0.130 | 24/98 | -0.002 | STANDARD |
| Lawson Crouse: 1+ goals | 0.221 | 0.105 | 19/98 | +0.021 | STANDARD |
| Anders Lee: 1+ goals | 0.230 | 0.115 | 22/99 | -0.002 | STANDARD |
| Jack Quinn: 1+ goals | 0.269 | 0.155 | 29/98 | -0.036 | STANDARD |
| Vincent Trocheck: 1+ points | 0.352 | 0.465 | 49/56 | +0.071 | STANDARD |

**DET @ MTL** · priced 148/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.75, exp saves 25.18 (sd 6.63), pull risk 0.051
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 22.03 (sd 6.31), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ points | 0.668 | 0.385 | 76/99 | -0.104 | STANDARD |
| Alex DeBrincat: 1+ goals | 0.365 | 0.180 | 35/99 | -0.001 | STANDARD |
| Viktor Arvidsson: 1+ goals | 0.288 | 0.155 | 30/99 | -0.027 | STANDARD |
| Dylan Larkin: 1+ goals | 0.301 | 0.170 | 33/99 | -0.045 | STANDARD |
| Lucas Raymond: 1+ goals | 0.246 | 0.130 | 25/99 | -0.017 | STANDARD |
| Emmitt Finnie: 1+ goals | 0.205 | 0.090 | 17/99 | +0.025 | STANDARD |

**NSH @ OTT** · priced 151/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.1), pull risk 0.055
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.07 (sd 7.16), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ points | 0.625 | 0.365 | 72/99 | -0.109 | STANDARD |
| Jordan Spence: 1+ points | 0.433 | 0.310 | 33/71 | +0.088 | STANDARD |
| Jordan Spence: 1+ assists | 0.371 | 0.250 | 27/77 | +0.087 | STANDARD |
| Tim Stutzle: 1+ assists | 0.435 | 0.555 | 57/46 | +0.087 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.237 | 0.340 | 37/69 | +0.058 | PRIOR_HEAVY |
| Fabian Zetterlund: 1+ goals | 0.198 | 0.100 | 19/99 | -0.003 | STANDARD |

**DAL @ PIT** · priced 157/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.15 (sd 6.27), pull risk 0.061
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.81, exp saves 23.09 (sd 6.52), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jason Robertson: 1+ points | 0.608 | 0.370 | 73/99 | -0.136 | STANDARD |
| Kris Letang: 1+ points | 0.348 | 0.175 | 34/99 | -0.008 | STANDARD |
| Roope Hintz: 1+ assists | 0.284 | 0.445 | 45/56 | +0.138 | STANDARD |
| Rickard Rakell: 1+ goals | 0.316 | 0.165 | 29/96 | +0.012 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.346 | 0.195 | 23/84 | +0.103 | STANDARD |
| Evgeni Malkin: 1+ goals | 0.261 | 0.135 | 26/99 | -0.013 | STANDARD |

**CAR @ CHI** · priced 153/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 31.13, exp saves 26.68 (sd 7.33), pull risk 0.075
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.54), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.287 | 0.435 | 47/60 | +0.096 | STANDARD |
| Sebastian Aho: 1+ assists | 0.338 | 0.480 | 51/55 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.527 | 0.655 | 68/37 | +0.087 | STANDARD |
| Sebastian Aho: 2+ points | 0.173 | 0.300 | 33/73 | +0.083 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.315 | 0.410 | 44/62 | +0.049 | STANDARD |
| Jordan Staal: 1+ goals | 0.207 | 0.115 | 21/98 | -0.014 | STANDARD |

**CBJ @ STL** · priced 159/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.71, exp saves 24.03 (sd 6.58), pull risk 0.057
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.17, exp saves 22.48 (sd 6.22), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.255 | 0.110 | 21/99 | +0.033 | STANDARD |
| Adam Jiricek: 1+ assists | 0.220 | 0.350 | 38/68 | +0.084 | PRIOR_HEAVY |
| Adam Jiricek: 1+ points | 0.277 | 0.405 | 45/64 | +0.067 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.419 | 0.535 | 55/48 | +0.084 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.188 | 0.075 | 14/99 | +0.040 | STANDARD |
| Sean Monahan: 1+ goals | 0.208 | 0.105 | 20/99 | -0.003 | STANDARD |

**TOR @ COL** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.71 (sd 5.96), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.66 (sd 8.1), pull risk 0.091

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 1+ points | 0.721 | 0.410 | 81/99 | -0.100 | STANDARD |
| Martin Necas: 1+ points | 0.649 | 0.365 | 72/99 | -0.085 | STANDARD |
| Cale Makar: 1+ points | 0.579 | 0.360 | 71/99 | -0.145 | STANDARD |
| William Nylander: 1+ goals | 0.319 | 0.165 | 32/99 | -0.016 | STANDARD |
| Gabriel Landeskog: 1+ goals | 0.273 | 0.135 | 25/98 | +0.010 | STANDARD |
| Auston Matthews: 1+ goals | 0.331 | 0.195 | 37/98 | -0.055 | STANDARD |

**TBL @ NYI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.33, exp saves 23.7 (sd 6.45), pull risk 0.053
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 26.5, exp saves 22.82 (sd 6.19), pull risk 0.056

**ANA @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.92, exp saves 26.58 (sd 7.23), pull risk 0.073
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.3 (sd 6.51), pull risk 0.064

**LAK @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.03 (sd 6.22), pull risk 0.044
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.25 (sd 6.62), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
