# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T09:37:50Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 2987 · contracts joined: 1158 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 808, 'OK': 221, 'NO_EDGE': 129}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 74, 'game_early_goal': 14, 'first_goal': 88, 'game_winner': 28, 'player_goals': 186, 'game_overtime': 14, 'player_points': 96, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 2026-10-10T17:00:00Z | T-6h | 0.611 | 0.389 | 0.179 | 5.70 | 3.18 | 2.52 | 217 (25/192) | PROJECTED/PROJECTED |
| VAN @ NJD | 2026-10-10T19:30:00Z | T-6h | 0.616 | 0.385 | 0.167 | 6.49 | 3.62 | 2.87 | 213 (25/188) | PROJECTED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-6h | 0.484 | 0.516 | 0.168 | 6.85 | 3.37 | 3.48 | 167 (25/142) | PROJECTED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-12h | 0.468 | 0.532 | 0.165 | 6.26 | 3.03 | 3.23 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-12h | 0.535 | 0.465 | 0.173 | 6.35 | 3.29 | 3.06 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-12h | 0.565 | 0.435 | 0.172 | 6.27 | 3.34 | 2.93 | 51 (25/26) | PROJECTED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-12h | 0.571 | 0.429 | 0.172 | 6.56 | 3.51 | 3.05 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-12h | 0.515 | 0.485 | 0.174 | 6.44 | 3.27 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-12h | 0.398 | 0.602 | 0.174 | 6.03 | 2.70 | 3.33 | 51 (25/26) | PROJECTED/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-12h | 0.535 | 0.465 | 0.181 | 5.81 | 3.01 | 2.80 | 51 (25/26) | PROJECTED/PROJECTED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-12h | 0.712 | 0.288 | 0.146 | 6.87 | 4.17 | 2.70 | 51 (25/26) | PROJECTED/PROJECTED |
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
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.398 | 0.300 | 0.319 | 31 | 71 | yes | +0.073 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.213 | 0.305 | 0.285 | 31 | 70 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.554 | 0.650 | 0.631 | 66 | 36 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.333 | 0.245 | 0.261 | 25 | 76 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.275 | 0.365 | 0.346 | 37 | 64 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.334 | 0.430 | 0.410 | 44 | 58 | no | +0.069 | OK |
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
| KXNHLGAME-26OCT10DETMTL-DET | game_winner | 0.435 | 0.355 | 0.371 | 36 | 65 | yes | +0.059 | OK |
| KXNHLGAME-26OCT10DETMTL-MTL | game_winner | 0.565 | 0.645 | 0.629 | 65 | 36 | no | +0.059 | OK |
| KXNHLGAME-26OCT10EDMSJ-EDM | game_winner | 0.516 | 0.595 | 0.579 | 60 | 41 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.318 | 0.245 | 0.259 | 25 | 76 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.438 | 0.525 | 0.507 | 54 | 49 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.622 | 0.540 | 0.557 | 55 | 47 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.632 | 0.550 | 0.567 | 56 | 46 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.440 | 0.520 | 0.504 | 53 | 49 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.510 | 0.430 | 0.446 | 44 | 58 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.232 | 0.165 | 0.177 | 17 | 84 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.200 | 0.135 | 0.146 | 14 | 87 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.231 | 0.165 | 0.177 | 17 | 84 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.245 | 0.320 | 0.304 | 33 | 69 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.415 | 0.335 | 0.350 | 35 | 68 | yes | +0.049 | OK |
| KXNHLGAME-26OCT10EDMSJ-SJ | game_winner | 0.484 | 0.415 | 0.429 | 42 | 59 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.174 | 0.110 | 0.121 | 12 | 90 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL4 | team_total | 0.614 | 0.545 | 0.559 | 55 | 46 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL5 | team_total | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 | team_total | 0.467 | 0.545 | 0.530 | 56 | 47 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.261 | 0.325 | 0.311 | 33 | 68 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI4 | team_total | 0.252 | 0.325 | 0.310 | 34 | 69 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.640 | 0.570 | 0.584 | 58 | 44 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.378 | 0.310 | 0.323 | 32 | 70 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.778 | 0.845 | 0.833 | 86 | 17 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.166 | 0.235 | 0.220 | 25 | 78 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.449 | 0.380 | 0.393 | 39 | 63 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.508 | 0.445 | 0.458 | 45 | 56 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT10DETMTL-DET2 | game_spread | 0.231 | 0.170 | 0.181 | 18 | 84 | yes | +0.041 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.262 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI2 | team_total | 0.707 | 0.775 | 0.762 | 79 | 24 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT3 | game_spread | 0.188 | 0.135 | 0.145 | 14 | 87 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 | team_total | 0.503 | 0.570 | 0.557 | 58 | 44 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.151 | 0.210 | 0.197 | 22 | 80 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.112 | 0.065 | 0.073 | 7 | 94 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM2 | game_spread | 0.306 | 0.365 | 0.353 | 37 | 64 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL6 | team_total | 0.238 | 0.175 | 0.186 | 19 | 84 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-SJ2 | game_spread | 0.279 | 0.225 | 0.235 | 23 | 78 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR3 | team_total | 0.659 | 0.725 | 0.712 | 74 | 29 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT5 | team_total | 0.237 | 0.180 | 0.191 | 19 | 83 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL3 | team_total | 0.659 | 0.720 | 0.708 | 73 | 29 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 | team_total | 0.423 | 0.355 | 0.368 | 37 | 66 | yes | +0.036 | OK |
| KXNHLGAME-26OCT10TORCOL-COL | game_winner | 0.712 | 0.655 | 0.667 | 66 | 35 | yes | +0.036 | OK |
| KXNHLGAME-26OCT10TORCOL-TOR | game_winner | 0.288 | 0.345 | 0.333 | 35 | 66 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.770 | 0.710 | 0.723 | 72 | 30 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM3 | game_spread | 0.192 | 0.250 | 0.238 | 26 | 76 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT10TORCOL-8 | game_total | 0.359 | 0.305 | 0.316 | 31 | 70 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 | team_total | 0.410 | 0.345 | 0.358 | 36 | 67 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.591 | 0.530 | 0.542 | 54 | 48 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-DET4 | team_total | 0.349 | 0.290 | 0.301 | 30 | 72 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL3 | team_total | 0.621 | 0.680 | 0.669 | 69 | 33 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ5 | team_total | 0.255 | 0.200 | 0.210 | 21 | 81 | yes | +0.034 | OK |
| KXNHLGAME-26OCT10PHIBOS-BOS | game_winner | 0.611 | 0.555 | 0.566 | 56 | 45 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT10PHIBOS-PHI3 | game_spread | 0.098 | 0.145 | 0.134 | 15 | 86 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ3 | team_total | 0.659 | 0.595 | 0.608 | 61 | 42 | yes | +0.032 | OK |

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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 26 recommended · full analysis in card.md / packet.json `thesis_card`

- Travis Sanheim: 1+ goals YES @ 6c · p 0.098 (adj 0.0872) · $3.39 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 13c · p 0.1827 (adj 0.167) · $4.81 · thesis PHI:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 61c · p 0.6727 (adj 0.6545) · $8.86 · thesis BOS:SUPPRESSED
- JJ Peterka: 1+ goals NO @ 74c · p 0.7897 (adj 0.7748) · $10.32 · thesis BOS:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 57c · p 0.7625 (adj 0.6309) · $12.79 · thesis NJD:SUPPRESSED
- Marco Rossi: 1+ goals YES @ 19c · p 0.2568 (adj 0.2351) · $5.66 · thesis VAN:OFFENSE_4PLUS
- New Jersey wins by over 1.5 goals NO @ 51c · p 0.6631 (adj 0.5603) · $3.72 · thesis VAN:WINS
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7812 (adj 0.6862) · $8.14 · thesis VAN:WINS
- Alex Formenton: 1+ goals YES @ 14c · p 0.1985 (adj 0.1801) · $5.55 · thesis EDM:OFFENSE_4PLUS
- Collin Graf: 1+ goals YES @ 18c · p 0.2391 (adj 0.2168) · $4.36 · thesis SJS:OFFENSE_4PLUS
- Kasperi Kapanen: 1+ goals NO @ 77c · p 0.8226 (adj 0.8082) · $12.79 · thesis EDM:SUPPRESSED
- Edmonton wins NO @ 41c · p 0.478 (adj 0.4415) · $3.34 · thesis SJS:WINS
- Minnesota over 4.5 goals scored YES @ 17c · p 0.2311 (adj 0.1981) · $1.68 · thesis MIN:OFFENSE_4PLUS
- Minnesota wins YES @ 45c · p 0.5265 (adj 0.4858) · $2.46 · thesis MIN:WINS
- Florida wins by over 1.5 goals NO @ 68c · p 0.745 (adj 0.71) · $4.29 · thesis MIN:WINS
- Full Game: Over 6.5 goals scored YES @ 42c · p 0.4846 (adj 0.4498) · $1.6 · thesis GAME:HIGH_EVENT
- Montreal wins by over 2.5 goals NO @ 70c · p 0.762 (adj 0.7285) · $8.37 · thesis GAME:TIGHT
- Dallas wins by over 2.5 goals NO @ 76c · p 0.8498 (adj 0.8024) · $12.79 · thesis PIT:WINS
- Pittsburgh wins by over 1.5 goals YES @ 23c · p 0.3185 (adj 0.2717) · $3.32 · thesis PIT:WINS_BY_2PLUS
- Pittsburgh wins by over 2.5 goals YES @ 14c · p 0.2049 (adj 0.1699) · $1.01 · thesis PIT:WINS_BY_2PLUS
- Pittsburgh over 2.5 goals scored YES @ 58c · p 0.6661 (adj 0.618) · $1.09 · thesis PIT:OFFENSE_4PLUS
- Chicago over 3.5 goals scored YES @ 26c · p 0.3463 (adj 0.2982) · $3.76 · thesis CHI:OFFENSE_4PLUS
- Carolina wins by over 2.5 goals NO @ 67c · p 0.7503 (adj 0.7077) · $8.74 · thesis GAME:TIGHT
- New York I wins by over 1.5 goals YES @ 21c · p 0.2868 (adj 0.2459) · $2.5 · thesis NYI:WINS_BY_2PLUS
- New York I wins YES @ 38c · p 0.5144 (adj 0.4238) · $1.9 · thesis NYI:WINS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8403 (adj 0.7952) · $12.79 · thesis NYI:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BOS** · priced 164/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (PROJECTED) exp shots 26.33, exp saves 23.05 (sd 6.3), pull risk 0.051
- PHI net: Dan Vladar (PROJECTED) exp shots 27.07, exp saves 23.36 (sd 6.54), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Frederic Brunet: 1+ points | 0.241 | 0.440 | 46/58 | +0.162 | PRIOR_HEAVY |
| Frederic Brunet: 1+ assists | 0.188 | 0.375 | 40/65 | +0.146 | PRIOR_HEAVY |
| JJ Peterka: 1+ assists | 0.176 | 0.305 | 31/70 | +0.110 | STANDARD |
| JJ Peterka: 1+ points | 0.348 | 0.470 | 48/54 | +0.094 | STANDARD |
| David Jiricek: 1+ points | 0.219 | 0.335 | 36/69 | +0.076 | STANDARD |
| Frederic Brunet: 2+ points | 0.030 | 0.130 | 15/89 | +0.073 | PRIOR_HEAVY |

**VAN @ NJD** · priced 157/162 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.83, exp saves 21.7 (sd 5.96), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.86 (sd 7.24), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.237 | 0.440 | 45/57 | +0.175 | STANDARD |
| Jack Hughes: 1+ assists | 0.413 | 0.615 | 63/40 | +0.170 | STANDARD |
| Jack Hughes: 2+ points | 0.255 | 0.440 | 46/58 | +0.148 | STANDARD |
| Luke Evangelista: 1+ points | 0.395 | 0.570 | 59/45 | +0.138 | STANDARD |
| Jack Hughes: 2+ assists | 0.104 | 0.235 | 25/78 | +0.104 | STANDARD |
| Evan Rodrigues: 1+ points | 0.304 | 0.425 | 44/59 | +0.089 | STANDARD |

**EDM @ SJS** · priced 113/116 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 28.97, exp saves 24.81 (sd 6.94), pull risk 0.081
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.62 (sd 6.38), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tyler Toffoli: 1+ points | 0.547 | 0.415 | 44/61 | +0.090 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.376 | 0.250 | 28/78 | +0.082 | STANDARD |
| Michael Misa: 1+ assists | 0.347 | 0.240 | 27/79 | +0.064 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.223 | 0.325 | 35/70 | +0.062 | PRIOR_HEAVY |
| Tyler Toffoli: 2+ points | 0.180 | 0.080 | 14/98 | +0.032 | STANDARD |
| Michael Misa: 1+ points | 0.487 | 0.390 | 41/63 | +0.060 | STANDARD |

**MIN @ FLA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.41, exp saves 23.61 (sd 6.57), pull risk 0.069
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.94 (sd 6.73), pull risk 0.06

**UTA @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROJECTED) exp shots 26.66, exp saves 22.98 (sd 6.37), pull risk 0.065
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 23.98 (sd 6.66), pull risk 0.067

**DET @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 28.75, exp saves 25.18 (sd 6.63), pull risk 0.051
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 22.03 (sd 6.31), pull risk 0.08

**NSH @ OTT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.1), pull risk 0.055
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.07 (sd 7.16), pull risk 0.077

**DAL @ PIT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.15 (sd 6.27), pull risk 0.061
- DAL net: Jake Oettinger (PROJECTED) exp shots 26.81, exp saves 23.09 (sd 6.52), pull risk 0.071

**CAR @ CHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 31.13, exp saves 26.68 (sd 7.33), pull risk 0.075
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.54), pull risk 0.053

**CBJ @ STL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (PROJECTED) exp shots 27.71, exp saves 24.03 (sd 6.58), pull risk 0.057
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.17, exp saves 22.48 (sd 6.22), pull risk 0.061

**TOR @ COL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.71 (sd 5.96), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.66 (sd 8.1), pull risk 0.091

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
