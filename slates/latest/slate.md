# NHL slate 2026-10-17 — RESEARCH_ONLY

generated 2026-10-17T06:04:16Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 14 · simulated (not started): 14 · markets on board: 2563 · contracts joined: 776 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 426, 'OK': 238, 'NO_EDGE': 112}
families: {'period_winner': 126, 'period_spread': 84, 'period_total': 126, 'game_early_goal': 14, 'game_winner': 28, 'player_goals': 62, 'game_overtime': 14, 'game_spread': 56, 'team_total': 140, 'game_total': 126}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 2026-10-17T17:00:00Z | T-6h | 0.565 | 0.435 | 0.177 | 6.11 | 3.25 | 2.86 | 113 (25/88) | PROJECTED/PROJECTED |
| CAR @ WPG | 2026-10-17T19:30:00Z | T-12h | 0.431 | 0.569 | 0.178 | 6.05 | 2.80 | 3.25 | 51 (25/26) | PROBABLE/PROJECTED |
| VAN @ TBL | 2026-10-17T20:00:00Z | T-12h | 0.696 | 0.304 | 0.154 | 6.26 | 3.77 | 2.49 | 51 (25/26) | PROJECTED/PROJECTED |
| SEA @ FLA | 2026-10-17T22:00:00Z | T-12h | 0.537 | 0.463 | 0.169 | 6.46 | 3.35 | 3.10 | 51 (25/26) | PROJECTED/PROJECTED |
| NYI @ TOR | 2026-10-17T23:00:00Z | T-12h | 0.483 | 0.517 | 0.175 | 6.39 | 3.14 | 3.25 | 51 (25/26) | PROJECTED/PROJECTED |
| BUF @ MTL | 2026-10-17T23:00:00Z | T-12h | 0.503 | 0.497 | 0.173 | 6.28 | 3.16 | 3.12 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ DET | 2026-10-17T23:00:00Z | T-12h | 0.544 | 0.456 | 0.181 | 6.03 | 3.15 | 2.88 | 51 (25/26) | PROJECTED/PROJECTED |
| OTT @ PHI | 2026-10-17T23:00:00Z | T-12h | 0.475 | 0.525 | 0.187 | 5.61 | 2.74 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| NYR @ CBJ | 2026-10-17T23:00:00Z | T-12h | 0.531 | 0.469 | 0.181 | 5.91 | 3.05 | 2.86 | 51 (25/26) | PROJECTED/PROJECTED |
| DAL @ CHI | 2026-10-17T23:00:00Z | T-12h | 0.467 | 0.533 | 0.180 | 5.67 | 2.74 | 2.93 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ NSH | 2026-10-18T00:00:00Z | T-12h | 0.553 | 0.447 | 0.174 | 6.54 | 3.44 | 3.10 | 51 (25/26) | PROJECTED/PROJECTED |
| BOS @ LAK | 2026-10-18T01:00:00Z | T-12h | 0.525 | 0.475 | 0.178 | 5.88 | 3.03 | 2.86 | 51 (25/26) | PROJECTED/PROJECTED |
| EDM @ UTA | 2026-10-18T02:00:00Z | T-12h | 0.556 | 0.444 | 0.167 | 6.74 | 3.56 | 3.18 | 51 (25/26) | PROJECTED/CONFIRMED |
| PIT @ VGK | 2026-10-18T02:00:00Z | T-12h | 0.576 | 0.424 | 0.169 | 6.77 | 3.63 | 3.14 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL4 | team_total | 0.349 | 0.485 | 0.457 | 50 | 53 | no | +0.104 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL3 | team_total | 0.569 | 0.695 | 0.671 | 71 | 32 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK2 | game_spread | 0.357 | 0.480 | 0.455 | 49 | 53 | no | +0.095 | OK |
| KXNHLGAME-26OCT17DALCHI-CHI | game_winner | 0.467 | 0.355 | 0.377 | 36 | 65 | yes | +0.091 | OK |
| KXNHLGAME-26OCT17DALCHI-DAL | game_winner | 0.533 | 0.645 | 0.623 | 65 | 36 | no | +0.091 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL3 | game_spread | 0.181 | 0.285 | 0.261 | 29 | 72 | no | +0.085 | OK |
| KXNHLSPREAD-26OCT17PITVGK-VGK3 | game_spread | 0.231 | 0.340 | 0.316 | 35 | 67 | no | +0.083 | OK |
| KXNHLSPREAD-26OCT17DALCHI-DAL2 | game_spread | 0.301 | 0.410 | 0.387 | 42 | 60 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT4 | team_total | 0.394 | 0.290 | 0.310 | 30 | 72 | yes | +0.080 | OK |
| KXNHLGAME-26OCT17PITVGK-PIT | game_winner | 0.424 | 0.325 | 0.344 | 33 | 68 | yes | +0.079 | OK |
| KXNHLGAME-26OCT17PITVGK-VGK | game_winner | 0.576 | 0.675 | 0.656 | 68 | 33 | no | +0.079 | OK |
| KXNHLGAME-26OCT17SEAFLA-FLA | game_winner | 0.537 | 0.635 | 0.616 | 64 | 37 | no | +0.076 | OK |
| KXNHLGAME-26OCT17SEAFLA-SEA | game_winner | 0.463 | 0.365 | 0.384 | 37 | 64 | yes | +0.076 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB3 | game_spread | 0.330 | 0.425 | 0.405 | 43 | 58 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT5 | team_total | 0.220 | 0.135 | 0.149 | 14 | 87 | yes | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL5 | team_total | 0.176 | 0.275 | 0.253 | 29 | 74 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL2 | team_total | 0.784 | 0.870 | 0.856 | 88 | 14 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT17VANTB-TB2 | game_spread | 0.476 | 0.570 | 0.551 | 58 | 44 | no | +0.067 | OK |
| KXNHLGAME-26OCT17VANTB-TB | game_winner | 0.696 | 0.775 | 0.761 | 78 | 23 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT17PITVGK-PIT2 | game_spread | 0.228 | 0.155 | 0.168 | 16 | 85 | yes | +0.059 | OK |
| KXNHLTOTAL-26OCT17DALCHI-5 | game_total | 0.704 | 0.775 | 0.762 | 78 | 23 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB4 | team_total | 0.540 | 0.620 | 0.604 | 63 | 39 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4 | team_total | 0.388 | 0.310 | 0.325 | 32 | 70 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA3 | game_spread | 0.204 | 0.275 | 0.260 | 28 | 73 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT3 | team_total | 0.609 | 0.535 | 0.550 | 54 | 47 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT17DALCHI-7 | game_total | 0.361 | 0.440 | 0.424 | 45 | 57 | no | +0.051 | OK |
| KXNHLSPREAD-26OCT17DALCHI-CHI2 | game_spread | 0.252 | 0.185 | 0.197 | 19 | 82 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT17DALCHI-6 | game_total | 0.472 | 0.550 | 0.534 | 56 | 46 | no | +0.051 | OK |
| KXNHLGAME-26OCT17VANTB-VAN | game_winner | 0.304 | 0.235 | 0.248 | 24 | 77 | yes | +0.051 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-6 | game_total | 0.513 | 0.585 | 0.571 | 59 | 42 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-7 | game_total | 0.403 | 0.475 | 0.460 | 48 | 53 | no | +0.050 | OK |
| KXNHLGAME-26OCT17NYITOR-NYI | game_winner | 0.517 | 0.445 | 0.459 | 45 | 56 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-FLA2 | game_spread | 0.324 | 0.400 | 0.384 | 41 | 61 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT17SEAFLA-SEA2 | game_spread | 0.258 | 0.195 | 0.207 | 20 | 81 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH3 | team_total | 0.673 | 0.600 | 0.615 | 61 | 41 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-PIT6 | team_total | 0.100 | 0.045 | 0.053 | 5 | 96 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA3 | team_total | 0.603 | 0.525 | 0.541 | 54 | 49 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH5 | team_total | 0.266 | 0.205 | 0.216 | 21 | 80 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 | team_total | 0.461 | 0.385 | 0.400 | 40 | 63 | yes | +0.044 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR2 | game_spread | 0.271 | 0.335 | 0.322 | 34 | 67 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT17STLNSH-8 | game_total | 0.306 | 0.245 | 0.257 | 25 | 76 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB3 | team_total | 0.736 | 0.800 | 0.788 | 81 | 21 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-5 | game_total | 0.737 | 0.800 | 0.788 | 81 | 21 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 | team_total | 0.401 | 0.470 | 0.456 | 48 | 54 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK4 | team_total | 0.501 | 0.565 | 0.552 | 57 | 44 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT17PITVGK-PIT3 | game_spread | 0.136 | 0.085 | 0.094 | 9 | 92 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA5 | team_total | 0.210 | 0.150 | 0.161 | 16 | 86 | yes | +0.041 | OK |
| KXNHLGAME-26OCT17BUFMTL-BUF | game_winner | 0.497 | 0.435 | 0.447 | 44 | 57 | yes | +0.040 | OK |
| KXNHLGAME-26OCT17BUFMTL-MTL | game_winner | 0.503 | 0.565 | 0.553 | 57 | 44 | no | +0.040 | OK |
| KXNHLGAME-26OCT17NYITOR-TOR | game_winner | 0.483 | 0.545 | 0.533 | 55 | 46 | no | +0.039 | OK |
| KXNHLTOTAL-26OCT17DALCHI-4 | game_total | 0.802 | 0.855 | 0.845 | 86 | 15 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT17DALCHI-DAL6 | team_total | 0.073 | 0.130 | 0.116 | 14 | 88 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT17NYITOR-NYI2 | game_spread | 0.302 | 0.245 | 0.256 | 25 | 76 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT17STLNSH-6 | game_total | 0.616 | 0.550 | 0.563 | 56 | 46 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT17SJDET-5 | game_total | 0.750 | 0.805 | 0.795 | 81 | 20 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT17VANTB-TB5 | team_total | 0.335 | 0.405 | 0.391 | 42 | 61 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT17STLNSH-NSH6 | team_total | 0.134 | 0.080 | 0.089 | 9 | 93 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT17DALCHI-8 | game_total | 0.190 | 0.245 | 0.233 | 25 | 76 | no | +0.037 | OK |
| KXNHLTOTAL-26OCT17STLNSH-7 | game_total | 0.504 | 0.445 | 0.457 | 45 | 56 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT17BUFMTL-MTL3 | game_spread | 0.181 | 0.235 | 0.223 | 24 | 77 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ4 | team_total | 0.376 | 0.440 | 0.427 | 45 | 57 | no | +0.037 | OK |
| KXNHLGAME-26OCT17STLNSH-NSH | game_winner | 0.553 | 0.495 | 0.507 | 50 | 51 | yes | +0.036 | OK |
| KXNHLGAME-26OCT17STLNSH-STL | game_winner | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT17NYRCBJ-8 | game_total | 0.221 | 0.275 | 0.264 | 28 | 73 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ3 | team_total | 0.548 | 0.605 | 0.594 | 61 | 40 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT3 | team_total | 0.558 | 0.620 | 0.608 | 63 | 39 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL3 | team_total | 0.620 | 0.680 | 0.668 | 69 | 33 | no | +0.035 | OK |
| KXNHLSPREAD-26OCT17NYITOR-TOR3 | game_spread | 0.164 | 0.220 | 0.208 | 23 | 79 | no | +0.035 | OK |
| KXNHLGAME-26OCT17CARWPG-WPG | game_winner | 0.431 | 0.375 | 0.386 | 38 | 63 | yes | +0.035 | OK |
| KXNHLSPREAD-26OCT17OTTPHI-OTT3 | game_spread | 0.164 | 0.215 | 0.204 | 22 | 79 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-NYI4 | team_total | 0.419 | 0.365 | 0.376 | 37 | 64 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT17OTTPHI-5 | game_total | 0.695 | 0.745 | 0.735 | 75 | 26 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT17NJWSH-NJ5 | team_total | 0.167 | 0.215 | 0.205 | 22 | 79 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT17SJDET-7 | game_total | 0.421 | 0.480 | 0.468 | 49 | 53 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT17NYITOR-NYI3 | team_total | 0.638 | 0.580 | 0.592 | 59 | 43 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT17STLNSH-NSH2 | game_spread | 0.335 | 0.285 | 0.295 | 29 | 72 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT4 | team_total | 0.333 | 0.395 | 0.382 | 41 | 62 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT17OTTPHI-OTT2 | team_total | 0.779 | 0.830 | 0.821 | 84 | 18 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA6 | team_total | 0.094 | 0.050 | 0.057 | 6 | 96 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT17PITVGK-VGK5 | team_total | 0.304 | 0.365 | 0.352 | 38 | 65 | no | +0.030 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ WSH | 0.565 | 0.554 | 0.177 | 0.220 | 6.11 | 6.17 | 0.961/0.987 | KXNHLTEAMTOTAL-26OCT17NJWSH-NJ4 +0.018 |
| CAR @ WPG | 0.431 | 0.465 | 0.178 | 0.222 | 6.05 | 6.33 | 0.994/0.997 | KXNHLTEAMTOTAL-26OCT17CARWPG-WPG3 +0.068 |
| VAN @ TBL | 0.696 | 0.633 | 0.154 | 0.208 | 6.26 | 6.21 | 0.958/1.026 | KXNHLSPREAD-26OCT17VANTB-TB2 -0.076 |
| SEA @ FLA | 0.537 | 0.524 | 0.169 | 0.218 | 6.46 | 6.26 | 0.998/1.005 | KXNHLTOTAL-26OCT17SEAFLA-8 -0.039 |
| NYI @ TOR | 0.483 | 0.519 | 0.175 | 0.215 | 6.39 | 6.25 | 0.965/0.956 | KXNHLTEAMTOTAL-26OCT17NYITOR-NYI4 -0.040 |
| BUF @ MTL | 0.503 | 0.523 | 0.173 | 0.222 | 6.28 | 6.41 | 0.976/0.998 | KXNHLTEAMTOTAL-26OCT17BUFMTL-MTL4 +0.031 |
| SJS @ DET | 0.544 | 0.515 | 0.181 | 0.219 | 6.03 | 6.26 | 1.015/1.027 | KXNHLTEAMTOTAL-26OCT17SJDET-SJ4 +0.047 |
| OTT @ PHI | 0.475 | 0.489 | 0.187 | 0.226 | 5.61 | 5.74 | 0.993/0.998 | KXNHLTOTAL-26OCT17OTTPHI-7 +0.031 |
| NYR @ CBJ | 0.531 | 0.557 | 0.181 | 0.218 | 5.91 | 6.08 | 0.964/0.992 | KXNHLTEAMTOTAL-26OCT17NYRCBJ-CBJ4 +0.040 |
| DAL @ CHI | 0.467 | 0.454 | 0.180 | 0.214 | 5.67 | 6.18 | 1.003/0.986 | KXNHLTOTAL-26OCT17DALCHI-7 +0.088 |
| STL @ NSH | 0.553 | 0.504 | 0.174 | 0.219 | 6.54 | 6.40 | 0.994/1.016 | KXNHLTEAMTOTAL-26OCT17STLNSH-NSH4 -0.053 |
| BOS @ LAK | 0.525 | 0.520 | 0.178 | 0.217 | 5.88 | 6.09 | 0.989/0.986 | KXNHLTOTAL-26OCT17BOSLA-7 +0.035 |
| EDM @ UTA | 0.556 | 0.522 | 0.167 | 0.208 | 6.74 | 6.87 | 0.993/1.023 | KXNHLTEAMTOTAL-26OCT17EDMUTA-EDM4 +0.046 |
| PIT @ VGK | 0.576 | 0.599 | 0.169 | 0.211 | 6.77 | 6.51 | 1.004/1.021 | KXNHLTOTAL-26OCT17PITVGK-8 -0.046 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Carolina wins by over 1.5 goals NO @ 61c · p 0.6972 (adj 0.6511) · $8.61 · thesis WPG:WINS
- Winnipeg wins by over 1.5 goals YES @ 20c · p 0.2647 (adj 0.2298) · $3.28 · thesis WPG:WINS_BY_2PLUS
- Carolina wins by over 2.5 goals NO @ 74c · p 0.811 (adj 0.773) · $9.84 · thesis WPG:WINS
- Vancouver wins by over 1.5 goals YES @ 11c · p 0.1795 (adj 0.1422) · $4.15 · thesis VAN:WINS_BY_2PLUS
- Tampa Bay wins by over 2.5 goals NO @ 58c · p 0.7221 (adj 0.6265) · $11.12 · thesis GAME:TIGHT
- Vancouver over 3.5 goals scored YES @ 22c · p 0.2948 (adj 0.2524) · $1.27 · thesis VAN:OFFENSE_4PLUS
- Tampa Bay over 5.5 goals scored NO @ 79c · p 0.8643 (adj 0.8196) · $14.15 · thesis VAN:WINS
- Florida wins by over 2.5 goals NO @ 73c · p 0.7989 (adj 0.762) · $14.89 · thesis SEA:WINS
- Florida wins by over 1.5 goals NO @ 61c · p 0.6902 (adj 0.6451) · $2.37 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 20c · p 0.2536 (adj 0.2243) · $2.22 · thesis SEA:WINS_BY_2PLUS
- Dallas wins by over 2.5 goals NO @ 72c · p 0.8022 (adj 0.7586) · $20.0 · thesis CHI:WINS
- Chicago over 3.5 goals scored YES @ 29c · p 0.3575 (adj 0.3213) · $1.55 · thesis CHI:OFFENSE_4PLUS
- Chicago wins by over 1.5 goals YES @ 19c · p 0.2448 (adj 0.2149) · $1.31 · thesis CHI:WINS_BY_2PLUS
- Vegas wins by over 1.5 goals NO @ 53c · p 0.6165 (adj 0.5683) · $11.83 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ WSH** · priced 60/62 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 29.7, exp saves 25.97 (sd 6.91), pull risk 0.047
- NJD net: Jake Allen (PROJECTED) exp shots 26.3, exp saves 22.66 (sd 6.33), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Aliaksei Protas: 1+ goals | 0.244 | 0.100 | 18/98 | +0.054 | STANDARD |
| Alex Ovechkin: 1+ goals | 0.289 | 0.170 | 30/96 | -0.026 | STANDARD |
| Boone Jenner: 1+ goals | 0.204 | 0.100 | 17/97 | +0.024 | STANDARD |
| Jesper Bratt: 1+ goals | 0.231 | 0.140 | 24/96 | -0.022 | STANDARD |
| Anthony Mantha: 1+ goals | 0.193 | 0.110 | 20/98 | -0.019 | STANDARD |
| Cody Glass: 1+ goals | 0.154 | 0.075 | 13/98 | +0.016 | STANDARD |

**CAR @ WPG** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Clay Stevenson (PROBABLE) exp shots 29.7, exp saves 25.56 (sd 6.86), pull risk 0.067
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.96, exp saves 20.71 (sd 5.91), pull risk 0.057

**VAN @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 23.47, exp saves 20.68 (sd 5.87), pull risk 0.045
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.69, exp saves 26.09 (sd 7.23), pull risk 0.078

**SEA @ FLA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 25.35, exp saves 22.02 (sd 6.09), pull risk 0.056
- SEA net: Joey Daccord (PROJECTED) exp shots 29.28, exp saves 25.19 (sd 6.9), pull risk 0.064

**NYI @ TOR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.61, exp saves 26.6 (sd 7.02), pull risk 0.059
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.0, exp saves 22.38 (sd 6.34), pull risk 0.065

**BUF @ MTL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (PROJECTED) exp shots 28.31, exp saves 24.63 (sd 6.76), pull risk 0.061
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.14, exp saves 22.49 (sd 6.3), pull risk 0.068

**SJS @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROJECTED) exp shots 25.93, exp saves 22.46 (sd 6.23), pull risk 0.059
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 29.07, exp saves 25.14 (sd 6.79), pull risk 0.061

**OTT @ PHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 27.39, exp saves 23.85 (sd 6.42), pull risk 0.05
- OTT net: Linus Ullmark (PROJECTED) exp shots 24.0, exp saves 20.99 (sd 5.92), pull risk 0.048

**NYR @ CBJ** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Jet Greaves (PROJECTED) exp shots 24.38, exp saves 21.34 (sd 5.93), pull risk 0.05
- NYR net: Dylan Garand (PROJECTED) exp shots 28.58, exp saves 24.53 (sd 6.67), pull risk 0.065

**DAL @ CHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.33, exp saves 23.55 (sd 6.53), pull risk 0.066
- DAL net: Jake Oettinger (PROJECTED) exp shots 23.84, exp saves 20.68 (sd 5.87), pull risk 0.055

**STL @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Justus Annunen (PROJECTED) exp shots 27.32, exp saves 23.62 (sd 6.49), pull risk 0.067
- STL net: Jordan Binnington (PROJECTED) exp shots 27.33, exp saves 23.54 (sd 6.62), pull risk 0.069

**BOS @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (PROJECTED) exp shots 25.88, exp saves 22.51 (sd 6.26), pull risk 0.057
- BOS net: Michael DiPietro (PROJECTED) exp shots 29.68, exp saves 25.67 (sd 6.85), pull risk 0.057

**EDM @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.03, exp saves 23.34 (sd 6.56), pull risk 0.069
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.83, exp saves 23.8 (sd 6.81), pull risk 0.08

**PIT @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 26.53, exp saves 23.24 (sd 6.39), pull risk 0.056
- PIT net: Sergei Murashov (PROJECTED) exp shots 28.1, exp saves 23.86 (sd 6.81), pull risk 0.082

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
