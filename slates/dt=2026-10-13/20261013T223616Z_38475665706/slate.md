# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T22:36:16Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 13 · markets on board: 5755 · contracts joined: 3181 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2856, 'NO_EDGE': 142, 'OK': 183}
families: {'period_winner': 117, 'period_spread': 78, 'period_total': 117, 'player_assists': 514, 'game_early_goal': 13, 'first_goal': 471, 'game_winner': 26, 'player_goals': 809, 'game_overtime': 13, 'player_points': 699, 'goalie_saves': 25, 'game_spread': 52, 'team_total': 130, 'game_total': 117}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WSH @ CAR | 2026-10-13T22:45:00Z | T-<10m | 0.579 | 0.421 | 0.176 | 5.99 | 3.23 | 2.76 | 242 (25/217) | CONFIRMED/CONFIRMED |
| SEA @ PHI | 2026-10-13T23:00:00Z | T-10m | 0.458 | 0.542 | 0.181 | 5.64 | 2.70 | 2.94 | 258 (25/233) | CONFIRMED/CONFIRMED |
| TBL @ NYR | 2026-10-13T23:15:00Z | T-30m | 0.514 | 0.486 | 0.186 | 5.72 | 2.91 | 2.81 | 252 (25/227) | CONFIRMED/PROBABLE |
| STL @ OTT | 2026-10-13T23:30:00Z | T-30m | 0.429 | 0.571 | 0.175 | 6.21 | 2.88 | 3.33 | 242 (25/217) | CONFIRMED/PROBABLE |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-60m | 0.661 | 0.339 | 0.160 | 6.30 | 3.68 | 2.62 | 224 (25/199) | CONFIRMED/PROBABLE |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-60m | 0.463 | 0.537 | 0.180 | 6.13 | 2.94 | 3.19 | 227 (25/202) | CONFIRMED/CONFIRMED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-90m | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 242 (25/217) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-90m | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 238 (25/213) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-90m | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 246 (25/221) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-90m | 0.674 | 0.326 | 0.152 | 6.79 | 3.98 | 2.81 | 242 (25/217) | PROBABLE/CONFIRMED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-3h | 0.645 | 0.355 | 0.171 | 6.36 | 3.64 | 2.72 | 250 (25/225) | CONFIRMED/PROBABLE |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-3h | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 241 (25/216) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-3h | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB3 | team_total | 0.541 | 0.675 | 0.650 | 68 | 33 | no | +0.113 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB4 | team_total | 0.324 | 0.455 | 0.428 | 46 | 55 | no | +0.109 | OK |
| KXNHLGAME-26OCT13TBNYR-NYR | game_winner | 0.514 | 0.405 | 0.426 | 41 | 60 | yes | +0.087 | OK |
| KXNHLGAME-26OCT13TBNYR-TB | game_winner | 0.486 | 0.595 | 0.574 | 60 | 41 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB2 | game_spread | 0.262 | 0.365 | 0.343 | 37 | 64 | no | +0.082 | OK |
| KXNHLSPREAD-26OCT13TBNYR-TB3 | game_spread | 0.147 | 0.245 | 0.222 | 25 | 76 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB5 | team_total | 0.157 | 0.255 | 0.233 | 26 | 75 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB2 | team_total | 0.767 | 0.855 | 0.840 | 86 | 15 | no | +0.074 | OK |
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.533 | 0.445 | 0.463 | 45 | 56 | yes | +0.066 | OK |
| KXNHLTOTAL-26OCT13TBNYR-5 | game_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.403 | 0.485 | 0.468 | 49 | 52 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 | team_total | 0.294 | 0.375 | 0.358 | 38 | 63 | no | +0.059 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.326 | 0.405 | 0.389 | 41 | 60 | no | +0.057 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.674 | 0.595 | 0.611 | 60 | 41 | yes | +0.057 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLTOTAL-26OCT13TBNYR-6 | game_total | 0.478 | 0.555 | 0.540 | 56 | 45 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT13TBNYR-7 | game_total | 0.368 | 0.445 | 0.429 | 45 | 56 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.461 | 0.385 | 0.400 | 39 | 62 | yes | +0.055 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR2 | game_spread | 0.286 | 0.215 | 0.228 | 22 | 79 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-5 | game_total | 0.696 | 0.765 | 0.752 | 77 | 24 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI3 | team_total | 0.514 | 0.585 | 0.571 | 59 | 42 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT13TBNYR-4 | game_total | 0.804 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-6 | game_total | 0.466 | 0.535 | 0.521 | 54 | 47 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT13PITCHI-6 | game_total | 0.549 | 0.615 | 0.602 | 62 | 39 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.585 | 0.598 | 59 | 42 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI5 | team_total | 0.137 | 0.195 | 0.182 | 20 | 81 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.626 | 0.685 | 0.674 | 69 | 32 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.577 | 0.510 | 0.523 | 52 | 50 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-7 | game_total | 0.354 | 0.415 | 0.403 | 42 | 59 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA6 | team_total | 0.208 | 0.145 | 0.156 | 16 | 87 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL5 | team_total | 0.250 | 0.195 | 0.205 | 20 | 81 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.436 | 0.495 | 0.483 | 50 | 51 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI3 | game_spread | 0.133 | 0.185 | 0.174 | 19 | 82 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.763 | 0.815 | 0.805 | 82 | 19 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.371 | 0.310 | 0.322 | 32 | 70 | yes | +0.036 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.463 | 0.405 | 0.416 | 41 | 60 | yes | +0.036 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.537 | 0.595 | 0.584 | 60 | 41 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.221 | 0.280 | 0.267 | 29 | 73 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-5 | game_total | 0.744 | 0.795 | 0.785 | 80 | 21 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL6 | team_total | 0.119 | 0.075 | 0.082 | 8 | 93 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT13SEAPHI-4 | game_total | 0.797 | 0.845 | 0.836 | 85 | 16 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13SEAPHI-PHI2 | game_spread | 0.243 | 0.295 | 0.284 | 30 | 71 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL3 | team_total | 0.649 | 0.595 | 0.606 | 60 | 41 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT13TBNYR-8 | game_total | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13STLOTT-STL2 | game_spread | 0.347 | 0.295 | 0.305 | 30 | 71 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.766 | 0.715 | 0.726 | 72 | 29 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ2 | team_total | 0.757 | 0.805 | 0.796 | 81 | 20 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI2 | team_total | 0.747 | 0.795 | 0.786 | 80 | 21 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13TBNYR-TB6 | team_total | 0.063 | 0.110 | 0.098 | 12 | 90 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-8 | game_total | 0.304 | 0.255 | 0.264 | 26 | 75 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.127 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT13TBNYR-NYR3 | game_spread | 0.169 | 0.125 | 0.133 | 13 | 88 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL4 | team_total | 0.437 | 0.385 | 0.395 | 39 | 62 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-4 | game_total | 0.832 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 | team_total | 0.324 | 0.375 | 0.364 | 38 | 63 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.199 | 0.155 | 0.163 | 16 | 85 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT13MINWPG-MIN2 | game_spread | 0.247 | 0.295 | 0.285 | 30 | 71 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR4 | team_total | 0.316 | 0.370 | 0.359 | 38 | 64 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT2 | team_total | 0.824 | 0.870 | 0.862 | 88 | 14 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT13WSHCAR-CAR4 | team_total | 0.416 | 0.470 | 0.459 | 48 | 54 | no | +0.026 | OK |
| KXNHLGAME-26OCT13MINWPG-MIN | game_winner | 0.456 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT13MINWPG-MIN3 | game_spread | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT2 | game_spread | 0.318 | 0.365 | 0.355 | 37 | 64 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT13WSHCAR-6 | game_total | 0.528 | 0.575 | 0.566 | 58 | 43 | no | +0.025 | OK |
| KXNHLGAME-26OCT13SEAPHI-PHI | game_winner | 0.458 | 0.505 | 0.495 | 51 | 50 | no | +0.025 | OK |
| KXNHLGAME-26OCT13SEAPHI-SEA | game_winner | 0.542 | 0.495 | 0.505 | 50 | 51 | yes | +0.025 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.359 | 0.315 | 0.324 | 32 | 69 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 | team_total | 0.539 | 0.590 | 0.580 | 60 | 42 | no | +0.024 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WSH @ CAR | 0.579 | 0.573 | 0.176 | 0.217 | 5.99 | 6.31 | 1.003/0.938 | KXNHLTOTAL-26OCT13WSHCAR-7 +0.058 |
| SEA @ PHI | 0.458 | 0.530 | 0.181 | 0.227 | 5.64 | 5.96 | 0.994/1.023 | KXNHLTEAMTOTAL-26OCT13SEAPHI-PHI4 +0.090 |
| TBL @ NYR | 0.514 | 0.520 | 0.186 | 0.224 | 5.72 | 6.00 | 0.988/0.957 | KXNHLTOTAL-26OCT13TBNYR-7 +0.054 |
| STL @ OTT | 0.429 | 0.499 | 0.175 | 0.224 | 6.21 | 6.21 | 1.071/0.984 | KXNHLSPREAD-26OCT13STLOTT-STL2 -0.074 |
| VAN @ NYI | 0.661 | 0.593 | 0.160 | 0.210 | 6.30 | 6.26 | 0.947/1.030 | KXNHLSPREAD-26OCT13VANNYI-NYI2 -0.076 |
| PIT @ CHI | 0.463 | 0.446 | 0.180 | 0.212 | 6.13 | 6.40 | 0.988/1.012 | KXNHLTOTAL-26OCT13PITCHI-7 +0.055 |
| MIN @ WPG | 0.544 | 0.518 | 0.180 | 0.218 | 6.10 | 6.23 | 1.003/1.033 | KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 +0.038 |
| COL @ DAL | 0.496 | 0.474 | 0.178 | 0.221 | 5.91 | 6.20 | 0.994/0.979 | KXNHLTEAMTOTAL-26OCT13COLDAL-COL4 +0.059 |
| VGK @ NSH | 0.533 | 0.507 | 0.171 | 0.217 | 6.49 | 6.20 | 1.002/1.004 | KXNHLTOTAL-26OCT13VGKNSH-6 -0.054 |
| TOR @ UTA | 0.674 | 0.597 | 0.152 | 0.209 | 6.79 | 6.40 | 0.991/0.956 | KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 -0.092 |
| CGY @ ANA | 0.645 | 0.631 | 0.171 | 0.210 | 6.36 | 6.41 | 1.016/1.002 | KXNHLTEAMTOTAL-26OCT13CGYANA-CGY2 +0.018 |
| EDM @ LAK | 0.440 | 0.480 | 0.173 | 0.218 | 6.27 | 6.25 | 0.995/0.994 | KXNHLSPREAD-26OCT13EDMLA-EDM2 -0.043 |
| BOS @ SJS | 0.413 | 0.507 | 0.175 | 0.216 | 6.17 | 6.40 | 1.039/0.956 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 +0.094 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 49 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2193 (adj 0.2057) · $2.33 · thesis WSH:OFFENSE_4PLUS
- Jesperi Kotkaniemi: 1+ goals YES @ 11c · p 0.144 (adj 0.133) · $1.37 · thesis CAR:OFFENSE_4PLUS
- Justin Sourdif: 1+ goals YES @ 11c · p 0.1391 (adj 0.1306) · $1.19 · thesis WSH:OFFENSE_4PLUS
- Sebastian Aho: 1+ assists NO @ 54c · p 0.6587 (adj 0.5783) · $4.11 · thesis CAR:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.1444 (adj 0.1321) · $2.11 · thesis SEA:OFFENSE_4PLUS
- Jared McCann: 1+ goals NO @ 72c · p 0.78 (adj 0.7638) · $6.43 · thesis SEA:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 16c · p 0.204 (adj 0.1917) · $2.03 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 19c · p 0.238 (adj 0.2235) · $2.15 · thesis PHI:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 22c · p 0.3128 (adj 0.2639) · $2.56 · thesis NYR:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 76c · p 0.8423 (adj 0.7987) · $6.43 · thesis NYR:WINS
- Jake Guentzel: 1+ goals NO @ 65c · p 0.7001 (adj 0.6863) · $4.33 · thesis TBL:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $2.38 · thesis OTT:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1483 (adj 0.1375) · $1.77 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.838 (adj 0.7516) · $6.43 · thesis OTT:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 9c · p 0.1183 (adj 0.11) · $1.17 · thesis OTT:OFFENSE_4PLUS
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1852 (adj 0.1701) · $2.75 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 18c · p 0.2194 (adj 0.2083) · $1.75 · thesis VAN:OFFENSE_4PLUS
- Kyle Palmieri: 1+ goals NO @ 70c · p 0.7465 (adj 0.7336) · $5.25 · thesis NYI:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 12c · p 0.15 (adj 0.1412) · $1.24 · thesis NYI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.182 (adj 0.1653) · $3.05 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 53c · p 0.7353 (adj 0.5954) · $6.21 · thesis CHI:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1659 (adj 0.1532) · $2.08 · thesis PIT:OFFENSE_4PLUS
- Evgeni Malkin: 1+ assists NO @ 55c · p 0.6401 (adj 0.5925) · $4.74 · thesis PIT:SUPPRESSED
- Neal Pionk: 1+ goals NO @ 87c · p 0.9322 (adj 0.9142) · $6.43 · thesis WPG:SUPPRESSED
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1353 (adj 0.1252) · $1.57 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 23c · p 0.3052 (adj 0.2601) · $1.68 · thesis MIN:OFFENSE_4PLUS
- Morgan Barron: 1+ goals YES @ 11c · p 0.1379 (adj 0.1297) · $1.1 · thesis WPG:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 9c · p 0.1355 (adj 0.1216) · $2.03 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 20c · p 0.256 (adj 0.2408) · $2.82 · thesis COL:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 58c · p 0.6302 (adj 0.6164) · $3.94 · thesis COL:SUPPRESSED
- Gabriel Landeskog: 1+ goals YES @ 20c · p 0.2351 (adj 0.2251) · $1.35 · thesis COL:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 71c · p 0.7616 (adj 0.7475) · $5.7 · thesis VGK:SUPPRESSED
- Brady Skjei: 1+ assists YES @ 23c · p 0.308 (adj 0.264) · $2.07 · thesis NSH:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 68c · p 0.7257 (adj 0.713) · $3.94 · thesis VGK:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 24c · p 0.3101 (adj 0.2701) · $1.78 · thesis TOR:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6552) · $4.23 · thesis UTA:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 64c · p 0.6829 (adj 0.6709) · $3.83 · thesis TOR:SUPPRESSED
- A.J. Greer: 2+ goals YES @ 2c · p 0.0442 (adj 0.0382) · $1.11 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1395 (adj 0.1259) · $2.4 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.149 (adj 0.1367) · $1.72 · thesis ANA:OFFENSE_4PLUS
- Nikita Nesterenko: 1+ assists NO @ 74c · p 0.8073 (adj 0.7687) · $6.32 · thesis ANA:SUPPRESSED
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9098 (adj 0.8624) · $6.43 · thesis LAK:SUPPRESSED
- Andre Lee: 1+ goals YES @ 8c · p 0.1107 (adj 0.1018) · $1.34 · thesis LAK:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ assists YES @ 32c · p 0.4006 (adj 0.3553) · $2.28 · thesis EDM:OFFENSE_4PLUS
- Alex Laferriere: 1+ goals YES @ 25c · p 0.2859 (adj 0.2757) · $1.38 · thesis LAK:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 16c · p 0.2154 (adj 0.2003) · $2.78 · thesis SJS:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $2.0 · thesis BOS:OFFENSE_4PLUS
- Matthew Poitras: 1+ goals YES @ 9c · p 0.1244 (adj 0.1145) · $1.52 · thesis BOS:OFFENSE_4PLUS
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.148 (adj 0.1372) · $1.7 · thesis BOS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WSH @ CAR** · priced 181/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 23.49, exp saves 20.43 (sd 5.81), pull risk 0.056
- WSH net: Logan Thompson (CONFIRMED) exp shots 31.11, exp saves 26.55 (sd 7.27), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ assists | 0.341 | 0.465 | 47/54 | +0.101 | STANDARD |
| Pyotr Kochetkov: 23+ saves | 0.344 | 0.455 | 46/55 | +0.089 |  |
| Sebastian Aho: 1+ points | 0.532 | 0.635 | 64/37 | +0.081 | STANDARD |
| Sebastian Aho: 2+ points | 0.184 | 0.275 | 29/74 | +0.063 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.316 | 0.235 | 24/77 | +0.063 | STANDARD |
| Sebastian Aho: 2+ assists | 0.068 | 0.145 | 16/87 | +0.054 | STANDARD |

**SEA @ PHI** · priced 206/207 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 26.23, exp saves 22.78 (sd 6.24), pull risk 0.05
- SEA net: Philipp Grubauer (CONFIRMED) exp shots 26.94, exp saves 23.3 (sd 6.32), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ assists | 0.202 | 0.490 | 92/94 | -0.146 | STANDARD |
| Freddy Gaudreau: 1+ points | 0.299 | 0.485 | 91/94 | -0.243 | STANDARD |
| Adam Larsson: 1+ assists | 0.254 | 0.115 | 20/97 | +0.043 | STANDARD |
| Jared McCann: 1+ points | 0.442 | 0.545 | 55/46 | +0.081 | STANDARD |
| Mackie Samoskevich: 1+ assists | 0.138 | 0.240 | 25/77 | +0.080 | STANDARD |
| David Jiricek: 1+ points | 0.256 | 0.355 | 36/65 | +0.078 | STANDARD |

**TBL @ NYR** · priced 195/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 27.72, exp saves 24.06 (sd 6.54), pull risk 0.056
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 24.07, exp saves 20.8 (sd 5.9), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Carlson: 1+ points | 0.376 | 0.545 | 56/47 | +0.136 | STANDARD |
| John Carlson: 1+ assists | 0.294 | 0.455 | 46/55 | +0.138 | STANDARD |
| Andrei Vasilevskiy: 24+ saves | 0.309 | 0.460 | 47/55 | +0.124 |  |
| Nikita Kucherov: 1+ assists | 0.469 | 0.615 | 62/39 | +0.124 | STANDARD |
| Nikita Kucherov: 2+ points | 0.278 | 0.405 | 41/60 | +0.106 | STANDARD |
| Nikita Kucherov: 1+ points | 0.637 | 0.745 | 75/26 | +0.089 | STANDARD |

**STL @ OTT** · priced 185/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 24.35, exp saves 21.12 (sd 5.93), pull risk 0.059
- STL net: Joel Hofer (PROBABLE) exp shots 28.14, exp saves 24.3 (sd 6.76), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ points | 0.404 | 0.265 | 27/74 | +0.120 | STANDARD |
| Michael Amadio: 1+ assists | 0.267 | 0.130 | 24/98 | +0.014 | STANDARD |
| Andre Burakovsky: 1+ points | 0.294 | 0.430 | 44/58 | +0.109 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.162 | 0.295 | 30/71 | +0.114 | STANDARD |
| Jordan Spence: 1+ assists | 0.342 | 0.225 | 24/79 | +0.089 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.259 | 0.150 | 27/97 | -0.025 | STANDARD |

**VAN @ NYI** · priced 160/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.73 (sd 6.02), pull risk 0.051
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.68, exp saves 25.33 (sd 6.96), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Victor Eklund: 1+ assists | 0.215 | 0.340 | 35/67 | +0.100 | PRIOR_HEAVY |
| Kyle Palmieri: 1+ points | 0.430 | 0.540 | 55/47 | +0.083 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.241 | 0.345 | 35/66 | +0.083 | STANDARD |
| Victor Eklund: 1+ points | 0.377 | 0.480 | 49/53 | +0.075 | PRIOR_HEAVY |
| Bo Horvat: 1+ points | 0.559 | 0.650 | 66/36 | +0.064 | STANDARD |
| Matias Maccelli: 1+ assists | 0.267 | 0.350 | 36/66 | +0.058 | STANDARD |

**PIT @ CHI** · priced 175/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 29.01, exp saves 24.77 (sd 6.89), pull risk 0.08
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.04, exp saves 21.77 (sd 6.08), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.265 | 0.480 | 49/53 | +0.188 | STANDARD |
| Alex Vlasic: 1+ assists | 0.281 | 0.100 | 18/98 | +0.091 | STANDARD |
| Patrick Kane: 1+ points | 0.446 | 0.625 | 63/38 | +0.158 | STANDARD |
| Samuel Girard: 1+ assists | 0.296 | 0.140 | 26/98 | +0.023 | STANDARD |
| Sam Rinzel: 1+ assists | 0.254 | 0.105 | 19/98 | +0.053 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.252 | 0.105 | 19/98 | +0.051 | STANDARD |

**MIN @ WPG** · priced 188/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Iafallo: 1+ assists | 0.287 | 0.105 | 19/98 | +0.086 | STANDARD |
| Dylan DeMelo: 1+ assists | 0.262 | 0.110 | 20/98 | +0.050 | STANDARD |
| Dylan DeMelo: 1+ points | 0.303 | 0.170 | 25/91 | +0.039 | STANDARD |
| Alex Iafallo: 1+ points | 0.419 | 0.290 | 31/73 | +0.094 | STANDARD |
| Adam Lowry: 1+ assists | 0.224 | 0.110 | 20/98 | +0.013 | STANDARD |
| Jonas Brodin: 1+ assists | 0.222 | 0.110 | 20/98 | +0.010 | STANDARD |

**COL @ DAL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brent Burns: 1+ assists | 0.269 | 0.125 | 23/98 | +0.026 | STANDARD |
| Roope Hintz: 1+ assists | 0.286 | 0.390 | 40/62 | +0.078 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.286 | 0.390 | 40/62 | +0.077 | STANDARD |
| Justin Hryckowian: 1+ assists | 0.237 | 0.135 | 25/98 | -0.026 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.409 | 0.505 | 51/50 | +0.073 | STANDARD |
| Devon Toews: 1+ points | 0.403 | 0.495 | 50/51 | +0.069 | STANDARD |

**VGK @ NSH** · priced 194/195 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Hanifin: 1+ assists | 0.260 | 0.100 | 18/98 | +0.070 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 2+ points | 0.216 | 0.340 | 35/67 | +0.099 | STANDARD |
| Nicolas Hague: 1+ assists | 0.193 | 0.075 | 13/98 | +0.055 | STANDARD |
| Brayden McNabb: 1+ assists | 0.243 | 0.125 | 23/98 | +0.000 | STANDARD |
| Nick Perbix: 1+ assists | 0.195 | 0.080 | 14/98 | +0.047 | STANDARD |

**TOR @ UTA** · priced 190/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 25.03, exp saves 21.92 (sd 6.07), pull risk 0.052
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.85, exp saves 26.98 (sd 7.41), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Darren Raddysh: 1+ assists | 0.319 | 0.425 | 43/58 | +0.084 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.510 | 52/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.212 | 0.310 | 32/70 | +0.074 | STANDARD |
| Easton Cowan: 1+ points | 0.421 | 0.340 | 35/67 | +0.055 | STANDARD |
| John Tavares: 1+ assists | 0.294 | 0.375 | 39/64 | +0.050 | STANDARD |
| Easton Cowan: 1+ assists | 0.310 | 0.230 | 24/78 | +0.057 | STANDARD |

**CGY @ ANA** · priced 191/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 26.29, exp saves 23.15 (sd 6.3), pull risk 0.047
- CGY net: Dustin Wolf (PROBABLE) exp shots 31.79, exp saves 26.75 (sd 7.4), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ assists | 0.294 | 0.100 | 18/98 | +0.104 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.237 | 0.075 | 13/98 | +0.100 | STANDARD |
| Noah Warren: 1+ points | 0.341 | 0.185 | 20/83 | +0.130 | PRIOR_HEAVY |
| Zach Whitecloud: 1+ assists | 0.223 | 0.080 | 14/98 | +0.075 | STANDARD |
| Tim Washe: 1+ assists | 0.256 | 0.115 | 21/98 | +0.034 | STANDARD |
| Kevin Bahl: 1+ points | 0.277 | 0.140 | 16/88 | +0.107 | STANDARD |

**EDM @ LAK** · priced 187/190 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 28.16, exp saves 24.3 (sd 6.72), pull risk 0.065
- EDM net: Devon Levi (CONFIRMED) exp shots 27.62, exp saves 23.94 (sd 6.59), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ assists | 0.244 | 0.070 | 12/98 | +0.116 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.435 | 0.595 | 60/41 | +0.138 | STANDARD |
| Connor McDavid: 1+ assists | 0.481 | 0.635 | 64/37 | +0.132 | STANDARD |
| Joel Edmundson: 1+ points | 0.297 | 0.150 | 17/87 | +0.117 | STANDARD |
| Leon Draisaitl: 2+ points | 0.290 | 0.435 | 44/57 | +0.123 | STANDARD |
| Connor McDavid: 2+ points | 0.337 | 0.480 | 49/53 | +0.115 | STANDARD |

**BOS @ SJS** · priced 219/226 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.44), pull risk 0.069
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.58, exp saves 23.85 (sd 6.47), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.396 | 0.555 | 56/45 | +0.137 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.297 | 0.455 | 47/56 | +0.126 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.555 | 56/45 | +0.113 | STANDARD |
| Sam Dickinson: 1+ assists | 0.215 | 0.080 | 14/98 | +0.066 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.230 | 0.100 | 18/98 | +0.040 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.183 | 0.310 | 32/70 | +0.103 | PRIOR_HEAVY |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
