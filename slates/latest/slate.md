# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-13T23:24:56Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 10 · markets on board: 5640 · contracts joined: 2451 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 2201, 'OK': 127, 'NO_EDGE': 123}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 394, 'game_early_goal': 10, 'first_goal': 363, 'game_winner': 20, 'player_goals': 618, 'game_overtime': 10, 'player_points': 546, 'goalie_saves': 20, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ OTT | 2026-10-13T23:30:00Z | T-<10m | 0.429 | 0.571 | 0.175 | 6.21 | 2.88 | 3.33 | 244 (25/219) | CONFIRMED/PROBABLE |
| VAN @ NYI | 2026-10-13T23:45:00Z | T-10m | 0.661 | 0.339 | 0.160 | 6.30 | 3.68 | 2.62 | 233 (25/208) | CONFIRMED/PROBABLE |
| PIT @ CHI | 2026-10-14T00:00:00Z | T-30m | 0.463 | 0.537 | 0.180 | 6.13 | 2.94 | 3.19 | 227 (25/202) | CONFIRMED/CONFIRMED |
| MIN @ WPG | 2026-10-14T00:15:00Z | T-30m | 0.544 | 0.456 | 0.180 | 6.10 | 3.19 | 2.91 | 242 (25/217) | CONFIRMED/CONFIRMED |
| COL @ DAL | 2026-10-14T00:30:00Z | T-60m | 0.496 | 0.504 | 0.178 | 5.91 | 2.95 | 2.96 | 238 (25/213) | CONFIRMED/CONFIRMED |
| VGK @ NSH | 2026-10-14T00:45:00Z | T-60m | 0.533 | 0.467 | 0.171 | 6.49 | 3.35 | 3.14 | 246 (25/221) | PROBABLE/PROBABLE |
| TOR @ UTA | 2026-10-14T01:00:00Z | T-90m | 0.674 | 0.326 | 0.152 | 6.79 | 3.98 | 2.81 | 242 (25/217) | PROBABLE/CONFIRMED |
| CGY @ ANA | 2026-10-14T01:45:00Z | T-90m | 0.645 | 0.355 | 0.171 | 6.36 | 3.64 | 2.72 | 257 (25/232) | CONFIRMED/PROBABLE |
| EDM @ LAK | 2026-10-14T02:30:00Z | T-3h | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 245 (25/220) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-3h | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT13VGKNSH-NSH | game_winner | 0.533 | 0.445 | 0.463 | 45 | 56 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT4 | team_total | 0.403 | 0.485 | 0.468 | 49 | 52 | no | +0.059 | OK |
| KXNHLGAME-26OCT13TORUTA-TOR | game_winner | 0.326 | 0.405 | 0.389 | 41 | 60 | no | +0.057 | OK |
| KXNHLGAME-26OCT13TORUTA-UTA | game_winner | 0.674 | 0.595 | 0.611 | 60 | 41 | yes | +0.057 | OK |
| KXNHLTOTAL-26OCT13PITCHI-7 | game_total | 0.436 | 0.515 | 0.499 | 52 | 49 | no | +0.056 | OK |
| KXNHLGAME-26OCT13VGKNSH-VGK | game_winner | 0.467 | 0.545 | 0.529 | 55 | 46 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA2 | game_spread | 0.461 | 0.385 | 0.400 | 39 | 62 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH5 | team_total | 0.258 | 0.190 | 0.202 | 20 | 82 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH2 | game_spread | 0.320 | 0.255 | 0.267 | 26 | 75 | yes | +0.047 | OK |
| KXNHLTOTAL-26OCT13PITCHI-5 | game_total | 0.763 | 0.825 | 0.814 | 83 | 18 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH4 | team_total | 0.442 | 0.370 | 0.384 | 38 | 64 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT5 | team_total | 0.221 | 0.285 | 0.271 | 29 | 72 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT13PITCHI-6 | game_total | 0.549 | 0.615 | 0.602 | 62 | 39 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH3 | team_total | 0.649 | 0.585 | 0.598 | 59 | 42 | yes | +0.042 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK2 | game_spread | 0.264 | 0.325 | 0.312 | 33 | 68 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-VGK3 | game_spread | 0.158 | 0.215 | 0.203 | 22 | 79 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT3 | team_total | 0.626 | 0.685 | 0.674 | 69 | 32 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA4 | team_total | 0.577 | 0.510 | 0.523 | 52 | 50 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA6 | team_total | 0.208 | 0.145 | 0.156 | 16 | 87 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT13TORUTA-UTA3 | game_spread | 0.321 | 0.265 | 0.276 | 27 | 74 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA5 | team_total | 0.371 | 0.310 | 0.322 | 32 | 70 | yes | +0.036 | OK |
| KXNHLGAME-26OCT13PITCHI-CHI | game_winner | 0.463 | 0.405 | 0.416 | 41 | 60 | yes | +0.036 | OK |
| KXNHLGAME-26OCT13PITCHI-PIT | game_winner | 0.537 | 0.595 | 0.584 | 60 | 41 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL6 | team_total | 0.119 | 0.075 | 0.082 | 8 | 93 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 | team_total | 0.539 | 0.595 | 0.584 | 60 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR2 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT13PITCHI-4 | game_total | 0.850 | 0.895 | 0.887 | 90 | 11 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN4 | team_total | 0.341 | 0.395 | 0.384 | 40 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT3 | game_spread | 0.195 | 0.245 | 0.234 | 25 | 76 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT13TORUTA-TOR3 | game_spread | 0.090 | 0.135 | 0.125 | 14 | 87 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA3 | team_total | 0.766 | 0.715 | 0.726 | 72 | 29 | yes | +0.032 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-8 | game_total | 0.304 | 0.255 | 0.264 | 26 | 75 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH6 | team_total | 0.127 | 0.080 | 0.088 | 9 | 93 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 | team_total | 0.324 | 0.375 | 0.364 | 38 | 63 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13VGKNSH-NSH3 | game_spread | 0.199 | 0.155 | 0.163 | 16 | 85 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT13MINWPG-MIN2 | game_spread | 0.247 | 0.295 | 0.285 | 30 | 71 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT2 | team_total | 0.824 | 0.870 | 0.862 | 88 | 14 | no | +0.028 | OK |
| KXNHLGAME-26OCT13MINWPG-MIN | game_winner | 0.456 | 0.505 | 0.495 | 51 | 50 | no | +0.026 | OK |
| KXNHLGAME-26OCT13MINWPG-WPG | game_winner | 0.544 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT13MINWPG-MIN3 | game_spread | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT13PITCHI-PIT2 | game_spread | 0.318 | 0.365 | 0.355 | 37 | 64 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT13STLOTT-10 | game_total | 0.088 | 0.055 | 0.061 | 6 | 95 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.359 | 0.315 | 0.324 | 32 | 69 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT13PITCHI-9 | game_total | 0.175 | 0.215 | 0.207 | 22 | 79 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL3 | team_total | 0.649 | 0.605 | 0.614 | 61 | 40 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN3 | team_total | 0.561 | 0.605 | 0.596 | 61 | 40 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR3 | team_total | 0.531 | 0.575 | 0.566 | 58 | 43 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT13STLOTT-STL2 | game_spread | 0.347 | 0.305 | 0.313 | 31 | 70 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT13TORUTA-8 | game_total | 0.346 | 0.305 | 0.313 | 31 | 70 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ2 | team_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT3 | game_spread | 0.130 | 0.165 | 0.157 | 17 | 84 | no | +0.021 | OK |
| KXNHLGAME-26OCT13BOSSJ-BOS | game_winner | 0.587 | 0.545 | 0.554 | 55 | 46 | yes | +0.020 | OK |
| KXNHLGAME-26OCT13BOSSJ-SJ | game_winner | 0.413 | 0.455 | 0.446 | 46 | 55 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT13PITCHI-PIT6 | team_total | 0.102 | 0.135 | 0.128 | 14 | 87 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT13STLOTT-OTT2 | game_spread | 0.227 | 0.265 | 0.257 | 27 | 74 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT13MINWPG-5 | game_total | 0.759 | 0.795 | 0.788 | 80 | 21 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-VGK4 | team_total | 0.394 | 0.435 | 0.427 | 44 | 57 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT13STLOTT-STL3 | game_spread | 0.219 | 0.185 | 0.192 | 19 | 82 | yes | +0.019 | OK |
| KXNHLGAME-26OCT13CGYANA-ANA | game_winner | 0.645 | 0.605 | 0.613 | 61 | 40 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR4 | team_total | 0.316 | 0.365 | 0.355 | 38 | 65 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT13TORUTA-10 | game_total | 0.135 | 0.105 | 0.111 | 11 | 90 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13COLDAL-DAL4 | team_total | 0.355 | 0.395 | 0.387 | 40 | 61 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-TOR2 | team_total | 0.761 | 0.795 | 0.788 | 80 | 21 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13TORUTA-UTA2 | team_total | 0.905 | 0.870 | 0.878 | 88 | 14 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT13STLOTT-STL5 | team_total | 0.250 | 0.215 | 0.222 | 22 | 79 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT13PITCHI-8 | game_total | 0.249 | 0.285 | 0.278 | 29 | 72 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT13MINWPG-MIN2 | team_total | 0.782 | 0.815 | 0.809 | 82 | 19 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT13VGKNSH-NSH2 | team_total | 0.838 | 0.800 | 0.808 | 81 | 21 | yes | +0.017 | OK |
| KXNHLSPREAD-26OCT13CGYANA-CGY2 | game_spread | 0.172 | 0.205 | 0.198 | 21 | 80 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT13VGKNSH-9 | game_total | 0.217 | 0.180 | 0.187 | 19 | 83 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT13EDMLA-LA3 | game_spread | 0.135 | 0.165 | 0.159 | 17 | 84 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ5 | team_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT13STLOTT-8 | game_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT13STLOTT-6 | game_total | 0.561 | 0.525 | 0.532 | 53 | 48 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT13VANNYI-9 | game_total | 0.194 | 0.165 | 0.170 | 17 | 84 | yes | +0.014 | OK |
| KXNHLGAME-26OCT13STLOTT-OTT | game_winner | 0.429 | 0.465 | 0.458 | 47 | 54 | no | +0.014 | OK |
| KXNHLGAME-26OCT13STLOTT-STL | game_winner | 0.571 | 0.535 | 0.542 | 54 | 47 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT13STLOTT-9 | game_total | 0.182 | 0.150 | 0.156 | 16 | 86 | yes | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
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


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 40 recommended · full analysis in card.md / packet.json `thesis_card`

- Michael Amadio: 1+ goals YES @ 13c · p 0.1785 (adj 0.1651) · $3.16 · thesis OTT:OFFENSE_4PLUS
- Stephen Halliday: 1+ goals YES @ 11c · p 0.1483 (adj 0.1375) · $2.35 · thesis OTT:OFFENSE_4PLUS
- Nick Cousins: 1+ goals YES @ 9c · p 0.1183 (adj 0.11) · $1.55 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 71c · p 0.838 (adj 0.745) · $8.54 · thesis OTT:SUPPRESSED
- Drew O'Connor: 1+ goals YES @ 13c · p 0.1852 (adj 0.1689) · $3.51 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2194 (adj 0.2033) · $2.84 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 10c · p 0.1314 (adj 0.1223) · $1.73 · thesis VAN:OFFENSE_4PLUS
- Adam Pelech: 1+ goals YES @ 5c · p 0.0729 (adj 0.0634) · $1.01 · thesis NYI:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 12c · p 0.182 (adj 0.1653) · $4.23 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 53c · p 0.7353 (adj 0.5954) · $8.54 · thesis CHI:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 12c · p 0.1659 (adj 0.1532) · $2.85 · thesis PIT:OFFENSE_4PLUS
- Anton Frondell: 1+ assists YES @ 27c · p 0.3342 (adj 0.2996) · $2.36 · thesis CHI:OFFENSE_4PLUS
- Neal Pionk: 1+ goals NO @ 86c · p 0.9322 (adj 0.9129) · $8.54 · thesis WPG:SUPPRESSED
- Olli Maatta: 1+ goals YES @ 4c · p 0.0672 (adj 0.0566) · $1.21 · thesis MIN:OFFENSE_4PLUS
- Rieger Lorenz: 1+ goals YES @ 10c · p 0.1353 (adj 0.1252) · $2.09 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 22c · p 0.3052 (adj 0.2576) · $2.96 · thesis MIN:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 9c · p 0.1355 (adj 0.1216) · $2.7 · thesis COL:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 20c · p 0.256 (adj 0.2408) · $3.74 · thesis COL:OFFENSE_4PLUS
- Arttu Hyry: 1+ goals YES @ 9c · p 0.1161 (adj 0.1083) · $1.38 · thesis DAL:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 58c · p 0.6302 (adj 0.6164) · $5.14 · thesis COL:SUPPRESSED
- Adam Wilsby: 1+ goals YES @ 4c · p 0.0651 (adj 0.0551) · $1.12 · thesis NSH:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 71c · p 0.7616 (adj 0.7475) · $8.54 · thesis VGK:SUPPRESSED
- Brady Skjei: 1+ assists YES @ 23c · p 0.308 (adj 0.2615) · $2.38 · thesis NSH:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0695 (adj 0.0634) · $1.02 · thesis VGK:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 70c · p 0.7882 (adj 0.7391) · $8.0 · thesis UTA:SUPPRESSED
- Easton Cowan: 1+ assists YES @ 24c · p 0.3101 (adj 0.2701) · $2.39 · thesis TOR:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6552) · $4.82 · thesis UTA:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 64c · p 0.6829 (adj 0.6709) · $5.22 · thesis TOR:SUPPRESSED
- A.J. Greer: 2+ goals YES @ 2c · p 0.0442 (adj 0.0382) · $1.47 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1395 (adj 0.1284) · $2.45 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 11c · p 0.149 (adj 0.138) · $2.45 · thesis ANA:OFFENSE_4PLUS
- Nikita Nesterenko: 1+ assists NO @ 74c · p 0.8073 (adj 0.7687) · $8.46 · thesis ANA:SUPPRESSED
- Artemi Panarin: 2+ assists NO @ 82c · p 0.9098 (adj 0.8624) · $8.54 · thesis LAK:SUPPRESSED
- Andre Lee: 1+ goals YES @ 8c · p 0.1107 (adj 0.1018) · $1.79 · thesis LAK:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 15c · p 0.1914 (adj 0.1798) · $2.35 · thesis EDM:OFFENSE_4PLUS
- Mattias Ekholm: 1+ assists YES @ 28c · p 0.3533 (adj 0.3116) · $2.28 · thesis EDM:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $2.71 · thesis BOS:OFFENSE_4PLUS
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.148 (adj 0.1372) · $2.28 · thesis BOS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2154 (adj 0.2028) · $2.72 · thesis SJS:OFFENSE_4PLUS
- JJ Peterka: 1+ goals NO @ 74c · p 0.7912 (adj 0.7772) · $8.54 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**STL @ OTT** · priced 185/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 24.35, exp saves 21.12 (sd 5.93), pull risk 0.059
- STL net: Joel Hofer (PROBABLE) exp shots 28.14, exp saves 24.3 (sd 6.76), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ assists | 0.162 | 0.305 | 32/71 | +0.114 | STANDARD |
| Andre Burakovsky: 1+ points | 0.294 | 0.435 | 46/59 | +0.099 | STANDARD |
| Michael Amadio: 1+ assists | 0.267 | 0.130 | 24/98 | +0.014 | STANDARD |
| Jordan Spence: 1+ points | 0.404 | 0.270 | 28/74 | +0.110 | STANDARD |
| Jordan Spence: 1+ assists | 0.342 | 0.215 | 23/80 | +0.099 | STANDARD |
| Jonatan Berggren: 1+ assists | 0.259 | 0.145 | 27/98 | -0.025 | STANDARD |

**VAN @ NYI** · priced 169/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (CONFIRMED) exp shots 24.73, exp saves 21.73 (sd 6.02), pull risk 0.051
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.68, exp saves 25.33 (sd 6.96), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tom Willander: 1+ assists | 0.268 | 0.140 | 26/98 | -0.005 | STANDARD |
| Victor Eklund: 1+ assists | 0.215 | 0.340 | 35/67 | +0.100 | PRIOR_HEAVY |
| Logan Stanley: 1+ assists | 0.226 | 0.115 | 21/98 | +0.004 | STANDARD |
| Kyle Palmieri: 1+ points | 0.430 | 0.540 | 55/47 | +0.083 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.241 | 0.345 | 35/66 | +0.083 | STANDARD |
| Bo Horvat: 1+ points | 0.559 | 0.650 | 66/36 | +0.064 | STANDARD |

**PIT @ CHI** · priced 175/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (CONFIRMED) exp shots 29.01, exp saves 24.77 (sd 6.89), pull risk 0.08
- PIT net: Sergei Murashov (CONFIRMED) exp shots 25.04, exp saves 21.77 (sd 6.08), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.265 | 0.480 | 49/53 | +0.188 | STANDARD |
| Patrick Kane: 1+ points | 0.446 | 0.630 | 64/38 | +0.158 | STANDARD |
| Alex Vlasic: 1+ assists | 0.281 | 0.100 | 18/98 | +0.091 | STANDARD |
| Samuel Girard: 1+ assists | 0.296 | 0.145 | 27/98 | +0.012 | STANDARD |
| Sam Rinzel: 1+ assists | 0.254 | 0.105 | 19/98 | +0.053 | STANDARD |
| Artyom Levshunov: 1+ assists | 0.252 | 0.105 | 19/98 | +0.051 | STANDARD |

**MIN @ WPG** · priced 188/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 28.08, exp saves 24.44 (sd 6.61), pull risk 0.06
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.09, exp saves 24.3 (sd 6.62), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Iafallo: 1+ assists | 0.287 | 0.100 | 18/98 | +0.097 | STANDARD |
| Dylan DeMelo: 1+ assists | 0.262 | 0.110 | 20/98 | +0.050 | STANDARD |
| Alex Iafallo: 1+ points | 0.419 | 0.295 | 31/72 | +0.094 | STANDARD |
| Adam Lowry: 1+ points | 0.338 | 0.215 | 29/86 | +0.034 | STANDARD |
| Adam Lowry: 1+ assists | 0.224 | 0.110 | 20/98 | +0.013 | STANDARD |
| Jonas Brodin: 1+ assists | 0.222 | 0.110 | 20/98 | +0.010 | STANDARD |

**COL @ DAL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 28.74, exp saves 24.86 (sd 6.83), pull risk 0.062
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.31, exp saves 22.04 (sd 6.17), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brent Burns: 1+ assists | 0.269 | 0.125 | 23/98 | +0.026 | STANDARD |
| Sam Malinski: 1+ assists | 0.285 | 0.170 | 30/96 | -0.030 | STANDARD |
| Sam Steel: 1+ assists | 0.232 | 0.120 | 22/98 | +0.000 | STANDARD |
| Roope Hintz: 1+ assists | 0.286 | 0.395 | 40/61 | +0.088 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.286 | 0.390 | 40/62 | +0.077 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.409 | 0.510 | 52/50 | +0.073 | STANDARD |

**VGK @ NSH** · priced 194/195 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROBABLE) exp shots 29.36, exp saves 25.59 (sd 6.81), pull risk 0.055
- VGK net: Adin Hill (PROBABLE) exp shots 26.27, exp saves 22.66 (sd 6.25), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Hanifin: 1+ assists | 0.260 | 0.100 | 18/98 | +0.070 | STANDARD |
| Jack Eichel: 1+ assists | 0.425 | 0.555 | 56/45 | +0.108 | STANDARD |
| Jack Eichel: 2+ points | 0.216 | 0.340 | 35/67 | +0.099 | STANDARD |
| Nicolas Hague: 1+ assists | 0.193 | 0.075 | 12/97 | +0.066 | STANDARD |
| Brayden McNabb: 1+ assists | 0.243 | 0.125 | 23/98 | +0.000 | STANDARD |
| Jack Eichel: 1+ points | 0.583 | 0.695 | 70/31 | +0.092 | STANDARD |

**TOR @ UTA** · priced 190/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROBABLE) exp shots 25.03, exp saves 21.92 (sd 6.07), pull risk 0.052
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 31.85, exp saves 26.98 (sd 7.41), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Barrett Hayton: 1+ assists | 0.258 | 0.130 | 24/98 | +0.005 | STANDARD |
| Anthony Stolarz: 29+ saves | 0.416 | 0.290 | 53/95 | -0.131 |  |
| Jake McCabe: 1+ assists | 0.226 | 0.110 | 20/98 | +0.015 | STANDARD |
| Darren Raddysh: 1+ points | 0.406 | 0.510 | 52/50 | +0.076 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.212 | 0.310 | 32/70 | +0.074 | STANDARD |
| Darren Raddysh: 1+ assists | 0.319 | 0.415 | 43/60 | +0.064 | STANDARD |

**CGY @ ANA** · priced 198/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 26.29, exp saves 23.15 (sd 6.3), pull risk 0.047
- CGY net: Dustin Wolf (PROBABLE) exp shots 31.79, exp saves 26.75 (sd 7.4), pull risk 0.088

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Warren: 1+ assists | 0.294 | 0.100 | 18/98 | +0.104 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.237 | 0.075 | 12/97 | +0.110 | STANDARD |
| Noah Warren: 1+ points | 0.341 | 0.190 | 20/82 | +0.130 | PRIOR_HEAVY |
| Zach Whitecloud: 1+ assists | 0.223 | 0.080 | 13/97 | +0.085 | STANDARD |
| Tim Washe: 1+ assists | 0.256 | 0.115 | 21/98 | +0.034 | STANDARD |
| Kevin Bahl: 1+ points | 0.277 | 0.150 | 16/86 | +0.107 | STANDARD |

**EDM @ LAK** · priced 191/194 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
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
| Charlie McAvoy: 1+ assists | 0.297 | 0.455 | 46/55 | +0.136 | STANDARD |
| Jeremy Swayman: 25+ saves | 0.455 | 0.300 | 55/95 | -0.112 |  |
| Nikita Zadorov: 1+ assists | 0.230 | 0.095 | 17/98 | +0.050 | STANDARD |
| Sam Dickinson: 1+ assists | 0.215 | 0.080 | 14/98 | +0.066 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.550 | 56/46 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
