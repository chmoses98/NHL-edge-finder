# NHL slate 2026-10-10 — RESEARCH_ONLY

generated 2026-10-10T16:33:32Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 4848 · contracts joined: 3019 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2669, 'OK': 220, 'NO_EDGE': 130}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'player_assists': 400, 'game_early_goal': 14, 'first_goal': 498, 'game_winner': 28, 'player_goals': 878, 'game_overtime': 14, 'player_points': 518, 'goalie_saves': 11, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 2026-10-10T17:00:00Z | T-10m | 0.621 | 0.380 | 0.182 | 5.51 | 3.12 | 2.40 | 251 (25/226) | CONFIRMED/CONFIRMED |
| VAN @ NJD | 2026-10-10T19:30:00Z | T-90m | 0.612 | 0.388 | 0.168 | 6.46 | 3.60 | 2.86 | 215 (25/190) | PROJECTED/PROJECTED |
| EDM @ SJS | 2026-10-10T20:00:00Z | T-3h | 0.487 | 0.513 | 0.175 | 6.82 | 3.35 | 3.47 | 215 (25/190) | PROJECTED/CONFIRMED |
| MIN @ FLA | 2026-10-10T22:00:00Z | T-3h | 0.463 | 0.537 | 0.177 | 6.28 | 3.02 | 3.26 | 208 (25/183) | CONFIRMED/PROJECTED |
| UTA @ BUF | 2026-10-10T23:00:00Z | T-6h | 0.536 | 0.464 | 0.173 | 6.31 | 3.27 | 3.04 | 219 (25/194) | PROBABLE/PROJECTED |
| DET @ MTL | 2026-10-10T23:00:00Z | T-6h | 0.602 | 0.398 | 0.173 | 6.20 | 3.41 | 2.79 | 209 (25/184) | CONFIRMED/CONFIRMED |
| NSH @ OTT | 2026-10-10T23:00:00Z | T-6h | 0.567 | 0.433 | 0.170 | 6.52 | 3.49 | 3.03 | 212 (25/187) | PROJECTED/PROJECTED |
| DAL @ PIT | 2026-10-10T23:00:00Z | T-6h | 0.466 | 0.534 | 0.172 | 6.34 | 3.06 | 3.28 | 209 (25/184) | PROJECTED/CONFIRMED |
| CAR @ CHI | 2026-10-10T23:00:00Z | T-6h | 0.401 | 0.599 | 0.176 | 5.97 | 2.68 | 3.29 | 210 (25/185) | PROBABLE/PROJECTED |
| CBJ @ STL | 2026-10-10T23:00:00Z | T-6h | 0.481 | 0.519 | 0.174 | 6.25 | 3.06 | 3.19 | 216 (25/191) | CONFIRMED/PROJECTED |
| TOR @ COL | 2026-10-10T23:00:00Z | T-6h | 0.710 | 0.290 | 0.145 | 6.82 | 4.14 | 2.68 | 221 (25/196) | PROJECTED/PROJECTED |
| TBL @ NYI | 2026-10-10T23:30:00Z | T-6h | 0.498 | 0.501 | 0.190 | 5.49 | 2.74 | 2.75 | 207 (25/182) | CONFIRMED/PROBABLE |
| ANA @ CGY | 2026-10-11T02:00:00Z | T-6h | 0.485 | 0.514 | 0.173 | 6.27 | 3.09 | 3.19 | 217 (25/192) | PROJECTED/PROJECTED |
| LAK @ VGK | 2026-10-11T02:00:00Z | T-6h | 0.617 | 0.383 | 0.169 | 6.07 | 3.41 | 2.65 | 210 (25/185) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT10TBNYI-NYI | game_winner | 0.498 | 0.375 | 0.399 | 38 | 63 | yes | +0.102 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB3 | team_total | 0.527 | 0.650 | 0.626 | 66 | 36 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB4 | team_total | 0.307 | 0.430 | 0.404 | 44 | 58 | no | +0.096 | OK |
| KXNHLGAME-26OCT10VANNJ-VAN | game_winner | 0.388 | 0.275 | 0.296 | 28 | 73 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB2 | game_spread | 0.270 | 0.385 | 0.360 | 39 | 62 | no | +0.093 | OK |
| KXNHLGAME-26OCT10TBNYI-TB | game_winner | 0.501 | 0.615 | 0.593 | 62 | 39 | no | +0.092 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 | team_total | 0.435 | 0.545 | 0.523 | 55 | 46 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT10TBNYI-TB3 | game_spread | 0.150 | 0.255 | 0.231 | 26 | 75 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR2 | game_spread | 0.367 | 0.475 | 0.453 | 48 | 53 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CAR3 | game_spread | 0.230 | 0.335 | 0.312 | 34 | 67 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ3 | game_spread | 0.259 | 0.365 | 0.342 | 37 | 64 | no | +0.084 | OK |
| KXNHLGAME-26OCT10VANNJ-NJ | game_winner | 0.612 | 0.715 | 0.696 | 72 | 29 | no | +0.083 | OK |
| KXNHLGAME-26OCT10DALPIT-PIT | game_winner | 0.466 | 0.365 | 0.385 | 37 | 64 | yes | +0.080 | OK |
| KXNHLSPREAD-26OCT10VANNJ-NJ2 | game_spread | 0.395 | 0.495 | 0.475 | 50 | 51 | no | +0.078 | OK |
| KXNHLGAME-26OCT10CARCHI-CAR | game_winner | 0.599 | 0.695 | 0.677 | 70 | 31 | no | +0.076 | OK |
| KXNHLGAME-26OCT10CARCHI-CHI | game_winner | 0.401 | 0.305 | 0.323 | 31 | 70 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN3 | team_total | 0.640 | 0.545 | 0.565 | 55 | 46 | yes | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI2 | team_total | 0.685 | 0.775 | 0.759 | 78 | 23 | no | +0.073 | OK |
| KXNHLGAME-26OCT10MINFLA-FLA | game_winner | 0.463 | 0.555 | 0.537 | 56 | 45 | no | +0.070 | OK |
| KXNHLGAME-26OCT10MINFLA-MIN | game_winner | 0.537 | 0.445 | 0.463 | 45 | 56 | yes | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN4 | team_total | 0.333 | 0.245 | 0.261 | 25 | 76 | yes | +0.070 | OK |
| KXNHLGAME-26OCT10DALPIT-DAL | game_winner | 0.534 | 0.625 | 0.607 | 63 | 38 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB2 | team_total | 0.753 | 0.845 | 0.829 | 86 | 17 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI4 | team_total | 0.229 | 0.320 | 0.300 | 33 | 69 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN4 | team_total | 0.420 | 0.330 | 0.347 | 34 | 68 | yes | +0.064 | OK |
| KXNHLGAME-26OCT10EDMSJ-SJ | game_winner | 0.487 | 0.405 | 0.421 | 41 | 60 | yes | +0.060 | OK |
| KXNHLGAME-26OCT10EDMSJ-EDM | game_winner | 0.513 | 0.595 | 0.579 | 60 | 41 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN5 | team_total | 0.238 | 0.160 | 0.174 | 17 | 85 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN2 | game_spread | 0.321 | 0.245 | 0.259 | 25 | 76 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT10TBNYI-NYI2 | game_spread | 0.268 | 0.195 | 0.208 | 20 | 81 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-5 | game_total | 0.681 | 0.755 | 0.741 | 76 | 25 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN3 | team_total | 0.543 | 0.460 | 0.477 | 47 | 55 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-7 | game_total | 0.501 | 0.425 | 0.440 | 43 | 58 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN2 | game_spread | 0.202 | 0.135 | 0.147 | 14 | 87 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-8 | game_total | 0.306 | 0.235 | 0.248 | 24 | 77 | yes | +0.053 | OK |
| KXNHLTOTAL-26OCT10TBNYI-5 | game_total | 0.674 | 0.745 | 0.732 | 75 | 26 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT10TBNYI-TB5 | team_total | 0.147 | 0.225 | 0.207 | 24 | 79 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN2 | team_total | 0.766 | 0.695 | 0.710 | 70 | 31 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA2 | game_spread | 0.254 | 0.325 | 0.310 | 33 | 68 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-7 | game_total | 0.333 | 0.405 | 0.390 | 41 | 60 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT10MINFLA-FLA3 | game_spread | 0.149 | 0.215 | 0.200 | 22 | 79 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-6 | game_total | 0.445 | 0.515 | 0.501 | 52 | 49 | no | +0.048 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-6 | game_total | 0.614 | 0.545 | 0.559 | 55 | 46 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL2 | game_spread | 0.318 | 0.385 | 0.371 | 39 | 62 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT10TBNYI-6 | game_total | 0.437 | 0.505 | 0.491 | 51 | 50 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-VAN5 | team_total | 0.172 | 0.110 | 0.121 | 12 | 90 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM3 | game_spread | 0.195 | 0.255 | 0.242 | 26 | 75 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR4 | team_total | 0.430 | 0.495 | 0.482 | 50 | 51 | no | +0.042 | OK |
| KXNHLGAME-26OCT10CBJSTL-STL | game_winner | 0.481 | 0.545 | 0.532 | 55 | 46 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT10CARCHI-CHI2 | game_spread | 0.200 | 0.145 | 0.155 | 15 | 86 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR5 | team_total | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT10TBNYI-4 | game_total | 0.780 | 0.840 | 0.829 | 85 | 17 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10DALPIT-DAL3 | game_spread | 0.197 | 0.255 | 0.243 | 26 | 75 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10PHIBOS-PHI2 | game_spread | 0.178 | 0.235 | 0.223 | 24 | 77 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT10TORCOL-COL2 | game_spread | 0.507 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT10TBNYI-7 | game_total | 0.334 | 0.395 | 0.382 | 40 | 61 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT10PHIBOS-PHI3 | game_spread | 0.092 | 0.145 | 0.133 | 15 | 86 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT10DETMTL-MTL2 | game_spread | 0.374 | 0.435 | 0.423 | 44 | 57 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT10NSHOTT-9 | game_total | 0.219 | 0.160 | 0.171 | 17 | 85 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ4 | team_total | 0.446 | 0.385 | 0.397 | 39 | 62 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CHI3 | team_total | 0.506 | 0.445 | 0.457 | 45 | 56 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT10DALPIT-PIT2 | game_spread | 0.260 | 0.205 | 0.215 | 21 | 80 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH3 | team_total | 0.586 | 0.520 | 0.533 | 53 | 49 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT10PHIBOS-4 | game_total | 0.782 | 0.840 | 0.829 | 85 | 17 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-PIT3 | team_total | 0.595 | 0.535 | 0.547 | 54 | 47 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 | team_total | 0.373 | 0.305 | 0.318 | 32 | 71 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10VANNJ-VAN3 | game_spread | 0.112 | 0.065 | 0.073 | 7 | 94 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT10MINFLA-MIN3 | game_spread | 0.196 | 0.145 | 0.154 | 15 | 86 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 | team_total | 0.457 | 0.515 | 0.503 | 52 | 49 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH5 | team_total | 0.194 | 0.140 | 0.150 | 15 | 87 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-SJ2 | game_spread | 0.277 | 0.225 | 0.235 | 23 | 78 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT10MINFLA-MIN6 | team_total | 0.109 | 0.060 | 0.068 | 7 | 95 | yes | +0.034 | OK |
| KXNHLSPREAD-26OCT10EDMSJ-EDM2 | game_spread | 0.310 | 0.365 | 0.354 | 37 | 64 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL4 | team_total | 0.429 | 0.490 | 0.478 | 50 | 52 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT10VANNJ-NJ3 | team_total | 0.703 | 0.755 | 0.745 | 76 | 25 | no | +0.034 | OK |
| KXNHLGAME-26OCT10PHIBOS-BOS | game_winner | 0.621 | 0.565 | 0.576 | 57 | 44 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10EDMSJ-SJ5 | team_total | 0.255 | 0.200 | 0.210 | 21 | 81 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT10CARCHI-CAR2 | team_total | 0.840 | 0.885 | 0.877 | 89 | 12 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT10DALPIT-DAL3 | team_total | 0.643 | 0.700 | 0.689 | 71 | 31 | no | +0.032 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BOS | 0.621 | 0.569 | 0.182 | 0.221 | 5.51 | 5.95 | 0.955/0.994 | KXNHLTEAMTOTAL-26OCT10PHIBOS-PHI3 +0.094 |
| VAN @ NJD | 0.612 | 0.558 | 0.168 | 0.214 | 6.46 | 6.25 | 0.987/1.025 | KXNHLTEAMTOTAL-26OCT10VANNJ-NJ4 -0.060 |
| EDM @ SJS | 0.487 | 0.484 | 0.175 | 0.211 | 6.82 | 6.88 | 1.026/1.022 | KXNHLTOTAL-26OCT10EDMSJ-7 +0.013 |
| MIN @ FLA | 0.463 | 0.467 | 0.177 | 0.218 | 6.28 | 6.44 | 1.014/0.995 | KXNHLTOTAL-26OCT10MINFLA-7 +0.034 |
| UTA @ BUF | 0.536 | 0.512 | 0.173 | 0.215 | 6.31 | 6.46 | 0.999/0.992 | KXNHLTEAMTOTAL-26OCT10UTABUF-UTA3 +0.034 |
| DET @ MTL | 0.602 | 0.608 | 0.173 | 0.217 | 6.20 | 6.39 | 0.983/1.023 | KXNHLTEAMTOTAL-26OCT10DETMTL-MTL4 +0.032 |
| NSH @ OTT | 0.567 | 0.597 | 0.170 | 0.206 | 6.52 | 6.38 | 0.998/1.000 | KXNHLTEAMTOTAL-26OCT10NSHOTT-NSH4 -0.037 |
| DAL @ PIT | 0.466 | 0.507 | 0.172 | 0.218 | 6.34 | 6.45 | 1.033/0.994 | KXNHLTEAMTOTAL-26OCT10DALPIT-PIT4 +0.048 |
| CAR @ CHI | 0.401 | 0.415 | 0.176 | 0.214 | 5.97 | 6.38 | 0.995/0.989 | KXNHLTOTAL-26OCT10CARCHI-7 +0.068 |
| CBJ @ STL | 0.481 | 0.551 | 0.174 | 0.220 | 6.25 | 6.12 | 1.032/0.964 | KXNHLGAME-26OCT10CBJSTL-CBJ -0.070 |
| TOR @ COL | 0.710 | 0.674 | 0.145 | 0.194 | 6.82 | 6.58 | 0.976/0.965 | KXNHLTEAMTOTAL-26OCT10TORCOL-COL5 -0.057 |
| TBL @ NYI | 0.498 | 0.509 | 0.190 | 0.225 | 5.49 | 5.95 | 0.947/0.951 | KXNHLTOTAL-26OCT10TBNYI-6 +0.081 |
| ANA @ CGY | 0.485 | 0.499 | 0.173 | 0.215 | 6.27 | 6.51 | 0.997/1.035 | KXNHLTOTAL-26OCT10ANACGY-7 +0.044 |
| LAK @ VGK | 0.617 | 0.588 | 0.169 | 0.223 | 6.07 | 5.96 | 1.003/0.992 | KXNHLSPREAD-26OCT10LAVGK-VGK2 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 50 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 13c · p 0.1819 (adj 0.1664) · $1.96 · thesis PHI:OFFENSE_4PLUS
- Frederic Brunet: 1+ goals NO @ 90c · p 0.9365 (adj 0.9249) · $5.32 · thesis DIFFUSE
- JJ Peterka: 1+ goals NO @ 74c · p 0.7897 (adj 0.776) · $5.32 · thesis BOS:SUPPRESSED
- Vancouver wins YES @ 28c · p 0.4412 (adj 0.3332) · $1.58 · thesis VAN:WINS
- Nico Hischier: 1+ goals NO @ 66c · p 0.7368 (adj 0.7151) · $4.05 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 67c · p 0.7406 (adj 0.7217) · $4.05 · thesis NJD:SUPPRESSED
- New Jersey wins by over 2.5 goals NO @ 64c · p 0.7847 (adj 0.6874) · $3.18 · thesis VAN:WINS
- Alex Formenton: 1+ goals YES @ 13c · p 0.2068 (adj 0.1864) · $3.36 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ assists YES @ 25c · p 0.344 (adj 0.2945) · $2.42 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1131 (adj 0.1023) · $1.26 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 33c · p 0.4732 (adj 0.3736) · $3.61 · thesis EDM:SUPPRESSED
- Nico Sturm: 1+ goals YES @ 6c · p 0.1042 (adj 0.0907) · $1.58 · thesis MIN:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 8c · p 0.1272 (adj 0.1129) · $1.75 · thesis MIN:OFFENSE_4PLUS
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1499 (adj 0.1362) · $1.98 · thesis FLA:OFFENSE_4PLUS
- Ryan Hartman: 1+ goals YES @ 18c · p 0.2417 (adj 0.225) · $2.59 · thesis MIN:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 68c · p 0.8164 (adj 0.7245) · $5.4 · thesis UTA:SUPPRESSED
- Ryan McLeod: 1+ goals YES @ 13c · p 0.1688 (adj 0.1529) · $1.09 · thesis BUF:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 7c · p 0.1034 (adj 0.0913) · $1.08 · thesis DET:OFFENSE_4PLUS
- Emmitt Finnie: 1+ goals YES @ 16c · p 0.2009 (adj 0.1907) · $1.67 · thesis DET:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 17c · p 0.208 (adj 0.1972) · $1.32 · thesis MTL:OFFENSE_4PLUS
- Jacob Fowler: 23+ saves YES @ 48c · p 0.6641 (adj 0.5152) · $2.8 · thesis MTL:NET_HIGH_VOLUME
- Michael Amadio: 1+ goals YES @ 15c · p 0.212 (adj 0.1953) · $2.68 · thesis OTT:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 22c · p 0.2759 (adj 0.2607) · $2.42 · thesis NSH:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1498 (adj 0.1386) · $1.54 · thesis OTT:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 15c · p 0.1865 (adj 0.1761) · $1.32 · thesis OTT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 10c · p 0.1532 (adj 0.1399) · $2.19 · thesis PIT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 26c · p 0.3304 (adj 0.3115) · $3.16 · thesis PIT:OFFENSE_4PLUS
- Dallas wins by over 2.5 goals NO @ 75c · p 0.8297 (adj 0.7873) · $4.78 · thesis PIT:WINS
- Rickard Rakell: 1+ goals YES @ 27c · p 0.3111 (adj 0.2996) · $1.23 · thesis PIT:OFFENSE_4PLUS
- Teuvo Teravainen: 1+ goals YES @ 9c · p 0.1365 (adj 0.1224) · $1.73 · thesis CHI:OFFENSE_4PLUS
- Tyler Bertuzzi: 1+ goals YES @ 26c · p 0.326 (adj 0.3083) · $3.09 · thesis CHI:OFFENSE_4PLUS
- Ryan Donato: 1+ goals YES @ 13c · p 0.177 (adj 0.164) · $1.86 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7211 (adj 0.7033) · $5.4 · thesis CAR:SUPPRESSED
- Matthew Knies: 1+ assists NO @ 65c · p 0.7365 (adj 0.6907) · $5.37 · thesis CBJ:SUPPRESSED
- Adam Jiricek: 1+ assists NO @ 68c · p 0.7663 (adj 0.7181) · $5.36 · thesis STL:SUPPRESSED
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.1861 (adj 0.1771) · $1.37 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 21c · p 0.2489 (adj 0.2367) · $1.41 · thesis CBJ:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 12c · p 0.1694 (adj 0.152) · $1.65 · thesis COL:OFFENSE_4PLUS
- Cale Makar: 1+ goals NO @ 76c · p 0.8057 (adj 0.7918) · $5.07 · thesis COL:SUPPRESSED
- Kirill Marchenko: 1+ assists NO @ 62c · p 0.6996 (adj 0.6548) · $3.47 · thesis TOR:SUPPRESSED
- Martin Necas: 1+ goals NO @ 62c · p 0.6674 (adj 0.6543) · $3.03 · thesis COL:SUPPRESSED
- Brayden Schenn: 1+ goals YES @ 19c · p 0.2676 (adj 0.2457) · $3.15 · thesis NYI:OFFENSE_4PLUS
- John Carlson: 1+ assists NO @ 54c · p 0.727 (adj 0.5989) · $5.18 · thesis TBL:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 75c · p 0.8425 (adj 0.7937) · $5.18 · thesis NYI:WINS
- Judd Caulfield: 1+ goals YES @ 9c · p 0.1353 (adj 0.1165) · $1.34 · thesis ANA:OFFENSE_4PLUS
- Cutter Gauthier: 1+ goals NO @ 59c · p 0.6397 (adj 0.626) · $3.02 · thesis ANA:SUPPRESSED
- Leo Carlsson: 1+ assists NO @ 51c · p 0.6087 (adj 0.5413) · $1.6 · thesis ANA:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 68c · p 0.7507 (adj 0.7318) · $5.23 · thesis VGK:SUPPRESSED
- Artemi Panarin: 1+ assists NO @ 50c · p 0.6416 (adj 0.5463) · $4.18 · thesis LAK:SUPPRESSED
- Tomas Hertl: 1+ goals NO @ 70c · p 0.7381 (adj 0.7273) · $2.87 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BOS** · priced 198/200 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 26.33, exp saves 23.02 (sd 6.29), pull risk 0.053
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.07, exp saves 23.39 (sd 6.47), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Borgen: 1+ assists | 0.171 | 0.500 | 95/95 | -0.124 | STANDARD |
| William Borgen: 1+ points | 0.207 | 0.500 | 94/94 | -0.151 | STANDARD |
| Frederic Brunet: 1+ points | 0.246 | 0.435 | 45/58 | +0.157 | PRIOR_HEAVY |
| Travis Sanheim: 1+ assists | 0.303 | 0.120 | 23/99 | +0.061 | STANDARD |
| Frederic Brunet: 1+ assists | 0.193 | 0.375 | 39/64 | +0.151 | PRIOR_HEAVY |
| Fraser Minten: 1+ assists | 0.250 | 0.115 | 22/99 | +0.018 | STANDARD |

**VAN @ NJD** · priced 159/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.83, exp saves 21.68 (sd 5.96), pull risk 0.054
- VAN net: Leevi Merilainen (PROJECTED) exp shots 31.33, exp saves 26.9 (sd 7.21), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.235 | 0.440 | 45/57 | +0.178 | STANDARD |
| Jack Hughes: 1+ assists | 0.412 | 0.615 | 62/39 | +0.181 | STANDARD |
| Jack Hughes: 2+ points | 0.244 | 0.430 | 44/58 | +0.159 | STANDARD |
| Luke Evangelista: 1+ points | 0.398 | 0.575 | 59/44 | +0.145 | STANDARD |
| Jack Hughes: 1+ points | 0.615 | 0.765 | 79/26 | +0.112 | STANDARD |
| Luke Evangelista: 2+ points | 0.091 | 0.215 | 22/79 | +0.108 | STANDARD |

**EDM @ SJS** · priced 164/164 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 28.97, exp saves 24.77 (sd 6.93), pull risk 0.081
- EDM net: Tristan Jarry (CONFIRMED) exp shots 26.23, exp saves 22.61 (sd 6.41), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.527 | 0.680 | 69/33 | +0.128 | STANDARD |
| Connor McDavid: 2+ assists | 0.170 | 0.315 | 34/71 | +0.106 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.379 | 0.245 | 26/77 | +0.106 | STANDARD |
| Connor McDavid: 2+ points | 0.389 | 0.520 | 53/49 | +0.104 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.476 | 0.605 | 61/40 | +0.107 | STANDARD |
| Tyler Toffoli: 1+ points | 0.544 | 0.420 | 44/60 | +0.087 | STANDARD |

**MIN @ FLA** · priced 152/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.41, exp saves 23.53 (sd 6.55), pull risk 0.073
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 28.66, exp saves 24.91 (sd 6.74), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ points | 0.510 | 0.365 | 38/65 | +0.114 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.234 | 0.375 | 39/64 | +0.109 | STANDARD |
| Brady Tkachuk: 1+ points | 0.438 | 0.570 | 59/45 | +0.095 | STANDARD |
| Ryan Hartman: 1+ assists | 0.352 | 0.225 | 23/78 | +0.110 | STANDARD |
| Sam Reinhart: 1+ points | 0.506 | 0.605 | 62/41 | +0.067 | STANDARD |
| Carter Verhaeghe: 2+ points | 0.191 | 0.095 | 17/98 | +0.011 | STANDARD |

**UTA @ BUF** · priced 159/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 26.66, exp saves 23.02 (sd 6.38), pull risk 0.063
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.86, exp saves 24.03 (sd 6.6), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.184 | 0.325 | 33/68 | +0.121 | STANDARD |
| Josh Doan: 1+ assists | 0.324 | 0.190 | 26/88 | +0.051 | STANDARD |
| Vincent Trocheck: 1+ points | 0.348 | 0.460 | 47/55 | +0.084 | STANDARD |
| Josh Doan: 2+ points | 0.153 | 0.065 | 12/99 | +0.026 | STANDARD |
| Zach Benson: 2+ points | 0.184 | 0.105 | 16/95 | +0.014 | STANDARD |
| Zach Benson: 1+ points | 0.537 | 0.465 | 48/55 | +0.040 | STANDARD |

**DET @ MTL** · priced 146/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.75, exp saves 25.25 (sd 6.65), pull risk 0.048
- DET net: Daniil Tarasov (CONFIRMED) exp shots 25.85, exp saves 21.95 (sd 6.31), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jacob Fowler: 23+ saves | 0.664 | 0.435 | 48/61 | +0.167 |  |
| Andrew Copp: 1+ assists | 0.301 | 0.210 | 23/81 | +0.059 | STANDARD |
| Andrew Copp: 1+ points | 0.419 | 0.330 | 35/69 | +0.053 | STANDARD |
| Chris Kreider: 1+ assists | 0.237 | 0.325 | 34/69 | +0.058 | STANDARD |
| Chris Kreider: 1+ points | 0.437 | 0.510 | 52/50 | +0.046 | STANDARD |
| Viktor Arvidsson: 1+ goals | 0.292 | 0.225 | 28/83 | -0.002 | STANDARD |

**NSH @ OTT** · priced 155/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.23, exp saves 22.18 (sd 6.09), pull risk 0.052
- NSH net: Juuse Saros (PROJECTED) exp shots 30.65, exp saves 26.11 (sd 7.12), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Linus Ullmark: 23+ saves | 0.474 | 0.285 | 51/94 | -0.054 |  |
| Tim Stutzle: 1+ assists | 0.437 | 0.545 | 55/46 | +0.085 | STANDARD |
| Jordan Spence: 1+ points | 0.411 | 0.320 | 34/70 | +0.055 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.230 | 0.320 | 34/70 | +0.055 | PRIOR_HEAVY |
| Carter Yakemchuk: 1+ points | 0.290 | 0.375 | 39/64 | +0.054 | PRIOR_HEAVY |
| Jordan Spence: 1+ assists | 0.349 | 0.265 | 28/75 | +0.055 | STANDARD |

**DAL @ PIT** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.55, exp saves 22.04 (sd 6.24), pull risk 0.065
- DAL net: Jake Oettinger (CONFIRMED) exp shots 26.81, exp saves 23.14 (sd 6.46), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Roope Hintz: 1+ assists | 0.294 | 0.455 | 46/55 | +0.139 | STANDARD |
| Tyler Seguin: 1+ assists | 0.140 | 0.270 | 29/75 | +0.097 | STANDARD |
| Tyler Seguin: 1+ points | 0.328 | 0.440 | 46/58 | +0.075 | STANDARD |
| Jason Robertson: 2+ points | 0.243 | 0.355 | 37/66 | +0.081 | STANDARD |
| Jason Robertson: 1+ assists | 0.386 | 0.495 | 51/52 | +0.077 | STANDARD |
| Rickard Rakell: 2+ points | 0.218 | 0.115 | 17/94 | +0.038 | STANDARD |

**CAR @ CHI** · priced 155/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 31.13, exp saves 26.71 (sd 7.37), pull risk 0.078
- CAR net: Brandon Bussi (PROJECTED) exp shots 22.38, exp saves 19.61 (sd 5.55), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.490 | 50/52 | +0.122 | STANDARD |
| Sebastian Aho: 2+ points | 0.170 | 0.300 | 32/72 | +0.095 | STANDARD |
| Sebastian Aho: 1+ points | 0.522 | 0.640 | 65/37 | +0.092 | STANDARD |
| Patrick Kane: 1+ assists | 0.292 | 0.410 | 42/60 | +0.091 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.325 | 0.425 | 44/59 | +0.069 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.573 | 0.475 | 49/54 | +0.065 | STANDARD |

**CBJ @ STL** · priced 163/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Jordan Binnington (CONFIRMED) exp shots 27.71, exp saves 24.16 (sd 6.57), pull risk 0.053
- CBJ net: Jet Greaves (PROJECTED) exp shots 26.17, exp saves 22.42 (sd 6.24), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Adam Jiricek: 1+ points | 0.287 | 0.410 | 43/61 | +0.086 | PRIOR_HEAVY |
| Adam Jiricek: 1+ assists | 0.234 | 0.330 | 34/68 | +0.071 | PRIOR_HEAVY |
| Robert Thomas: 1+ assists | 0.435 | 0.530 | 54/48 | +0.068 | STANDARD |
| Matthew Knies: 1+ assists | 0.264 | 0.355 | 36/65 | +0.071 | STANDARD |
| Charlie Coyle: 2+ points | 0.166 | 0.085 | 14/97 | +0.017 | STANDARD |
| Charlie Coyle: 1+ points | 0.505 | 0.425 | 44/59 | +0.048 | STANDARD |

**TOR @ COL** · priced 166/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.57, exp saves 21.73 (sd 6.03), pull risk 0.045
- TOR net: Anthony Stolarz (PROJECTED) exp shots 35.35, exp saves 29.62 (sd 8.18), pull risk 0.098

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.483 | 0.595 | 60/41 | +0.090 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.521 | 0.625 | 64/39 | +0.072 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.265 | 28/75 | +0.075 | STANDARD |
| Cale Makar: 2+ points | 0.217 | 0.315 | 32/69 | +0.078 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.365 | 0.460 | 47/55 | +0.068 | STANDARD |
| Cale Makar: 2+ assists | 0.143 | 0.235 | 24/77 | +0.075 | STANDARD |

**TBL @ NYI** · priced 146/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 27.33, exp saves 23.71 (sd 6.44), pull risk 0.052
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 26.5, exp saves 22.83 (sd 6.25), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.352 | 0.555 | 57/46 | +0.170 | STANDARD |
| John Carlson: 1+ assists | 0.273 | 0.470 | 48/54 | +0.170 | STANDARD |
| Brayden Schenn: 1+ points | 0.508 | 0.380 | 40/64 | +0.091 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.191 | 0.310 | 33/71 | +0.084 | STANDARD |
| Nikita Kucherov: 2+ points | 0.277 | 0.380 | 39/63 | +0.077 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.129 | 0.230 | 24/78 | +0.079 | STANDARD |

**ANA @ CGY** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.92, exp saves 26.72 (sd 7.17), pull risk 0.066
- ANA net: Ville Husso (PROJECTED) exp shots 26.97, exp saves 23.24 (sd 6.53), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.220 | 0.095 | 16/97 | +0.050 | STANDARD |
| Alex Killorn: 1+ assists | 0.314 | 0.195 | 25/86 | +0.051 | STANDARD |
| Aydar Suniev: 1+ goals | 0.194 | 0.085 | 14/97 | +0.046 | PRIOR_HEAVY |
| Leo Carlsson: 1+ assists | 0.391 | 0.495 | 50/51 | +0.081 | STANDARD |
| Beckett Sennecke: 2+ points | 0.235 | 0.140 | 26/98 | -0.038 | STANDARD |
| Jackson LaCombe: 2+ points | 0.217 | 0.125 | 21/96 | -0.005 | STANDARD |

**LAK @ VGK** · priced 157/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.29, exp saves 23.01 (sd 6.25), pull risk 0.046
- LAK net: Darcy Kuemper (PROJECTED) exp shots 28.34, exp saves 24.27 (sd 6.63), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.358 | 0.505 | 51/50 | +0.124 | STANDARD |
| Mitch Marner: 2+ points | 0.190 | 0.325 | 34/69 | +0.105 | STANDARD |
| Mitch Marner: 1+ assists | 0.405 | 0.530 | 54/48 | +0.098 | STANDARD |
| Jack Eichel: 2+ points | 0.244 | 0.355 | 37/66 | +0.080 | STANDARD |
| Jack Eichel: 1+ assists | 0.443 | 0.545 | 55/46 | +0.080 | STANDARD |
| Artemi Panarin: 1+ points | 0.541 | 0.635 | 64/37 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
