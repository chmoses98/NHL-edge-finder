# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T21:46:57Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 3715 · contracts joined: 1832 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 1607, 'OK': 140, 'NO_EDGE': 85}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'player_assists': 221, 'game_early_goal': 9, 'first_goal': 314, 'game_winner': 18, 'player_goals': 551, 'game_overtime': 9, 'player_points': 276, 'goalie_saves': 11, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-60m | 0.489 | 0.511 | 0.172 | 6.65 | 3.29 | 3.36 | 200 (25/175) | CONFIRMED/CONFIRMED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-60m | 0.508 | 0.492 | 0.179 | 6.05 | 3.05 | 3.01 | 202 (25/177) | CONFIRMED/PROBABLE |
| OTT @ DET | 2026-10-06T23:00:00Z | T-60m | 0.577 | 0.423 | 0.177 | 6.12 | 3.31 | 2.81 | 199 (25/174) | PROBABLE/PROJECTED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-60m | 0.500 | 0.500 | 0.176 | 6.00 | 3.01 | 3.00 | 210 (25/185) | CONFIRMED/PROBABLE |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-60m | 0.522 | 0.478 | 0.175 | 6.42 | 3.28 | 3.14 | 207 (25/182) | PROBABLE/CONFIRMED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-90m | 0.629 | 0.371 | 0.175 | 5.97 | 3.40 | 2.58 | 207 (25/182) | CONFIRMED/CONFIRMED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-90m | 0.426 | 0.574 | 0.182 | 5.78 | 2.67 | 3.12 | 199 (25/174) | PROBABLE/CONFIRMED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-3h | 0.503 | 0.497 | 0.174 | 6.38 | 3.21 | 3.17 | 198 (25/173) | PROBABLE/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-3h | 0.557 | 0.443 | 0.172 | 6.25 | 3.31 | 2.94 | 210 (25/185) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.503 | 0.375 | 0.400 | 38 | 63 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.443 | 0.320 | 0.343 | 33 | 69 | yes | +0.097 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.497 | 0.615 | 0.592 | 62 | 39 | no | +0.097 | OK |
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.511 | 0.405 | 0.426 | 41 | 60 | yes | +0.084 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.489 | 0.595 | 0.574 | 60 | 41 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.651 | 0.545 | 0.567 | 55 | 46 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.286 | 0.385 | 0.364 | 39 | 62 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.624 | 0.525 | 0.545 | 53 | 48 | yes | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.256 | 0.155 | 0.172 | 17 | 86 | yes | +0.076 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.172 | 0.265 | 0.244 | 27 | 74 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.291 | 0.205 | 0.221 | 21 | 80 | yes | +0.070 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.322 | 0.235 | 0.251 | 24 | 77 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.300 | 0.215 | 0.231 | 22 | 79 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.412 | 0.315 | 0.334 | 33 | 70 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.523 | 0.435 | 0.452 | 44 | 57 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.283 | 0.365 | 0.348 | 37 | 64 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.842 | 0.760 | 0.779 | 77 | 25 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.229 | 0.150 | 0.164 | 16 | 86 | yes | +0.060 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.557 | 0.475 | 0.491 | 48 | 53 | yes | +0.059 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.236 | 0.165 | 0.178 | 17 | 84 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.651 | 0.575 | 0.591 | 58 | 43 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-6 | game_total | 0.631 | 0.555 | 0.570 | 56 | 45 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.175 | 0.245 | 0.230 | 25 | 76 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.126 | 0.060 | 0.070 | 7 | 95 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.187 | 0.125 | 0.136 | 13 | 88 | yes | +0.049 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.434 | 0.365 | 0.378 | 37 | 64 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.181 | 0.125 | 0.135 | 13 | 88 | yes | +0.043 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.120 | 0.175 | 0.163 | 18 | 83 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.823 | 0.760 | 0.774 | 77 | 25 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.352 | 0.295 | 0.306 | 30 | 71 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR4 | team_total | 0.365 | 0.425 | 0.413 | 43 | 58 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.219 | 0.275 | 0.263 | 28 | 73 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.240 | 0.295 | 0.283 | 30 | 71 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR2 | game_spread | 0.402 | 0.345 | 0.356 | 35 | 66 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-10 | game_total | 0.120 | 0.075 | 0.083 | 8 | 93 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.620 | 0.675 | 0.664 | 68 | 33 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT06UTANJ-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.106 | 0.060 | 0.067 | 7 | 95 | yes | +0.031 | OK |
| KXNHLGAME-26OCT06CARMTL-CAR | game_winner | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLGAME-26OCT06CARMTL-MTL | game_winner | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.211 | 0.165 | 0.173 | 17 | 84 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI2 | game_spread | 0.177 | 0.225 | 0.215 | 23 | 78 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT06UTANJ-5 | game_total | 0.748 | 0.795 | 0.786 | 80 | 21 | no | +0.031 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.423 | 0.475 | 0.465 | 48 | 53 | no | +0.030 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.577 | 0.525 | 0.535 | 53 | 48 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.241 | 0.190 | 0.199 | 20 | 82 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR3 | team_total | 0.585 | 0.640 | 0.629 | 65 | 37 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI3 | game_spread | 0.095 | 0.135 | 0.126 | 14 | 87 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-5 | game_total | 0.819 | 0.775 | 0.784 | 78 | 23 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT3 | team_total | 0.536 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR2 | game_spread | 0.278 | 0.325 | 0.315 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ4 | team_total | 0.367 | 0.415 | 0.405 | 42 | 59 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR2 | team_total | 0.794 | 0.840 | 0.832 | 85 | 17 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ2 | team_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06UTANJ-4 | game_total | 0.838 | 0.875 | 0.868 | 88 | 13 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.755 | 0.795 | 0.787 | 80 | 21 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT06STLCHI-6 | game_total | 0.490 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLGAME-26OCT06NYINYR-NYI | game_winner | 0.371 | 0.415 | 0.406 | 42 | 59 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.766 | 0.805 | 0.798 | 81 | 20 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT06CARMTL-4 | game_total | 0.840 | 0.875 | 0.869 | 88 | 13 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.649 | 0.605 | 0.614 | 61 | 40 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.322 | 0.370 | 0.360 | 38 | 64 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.820 | 0.855 | 0.848 | 86 | 15 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF4 | team_total | 0.428 | 0.385 | 0.393 | 39 | 62 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.352 | 0.395 | 0.386 | 40 | 61 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06CARMTL-7 | game_total | 0.421 | 0.465 | 0.456 | 47 | 54 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-8 | game_total | 0.284 | 0.245 | 0.253 | 25 | 76 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ3 | team_total | 0.583 | 0.630 | 0.621 | 64 | 38 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-4 | game_total | 0.889 | 0.855 | 0.862 | 86 | 15 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT06STLCHI-5 | game_total | 0.717 | 0.755 | 0.748 | 76 | 25 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.241 | 0.205 | 0.212 | 21 | 80 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.220 | 0.185 | 0.192 | 19 | 82 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ5 | team_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.218 | 0.255 | 0.247 | 26 | 75 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.170 | 0.205 | 0.198 | 21 | 80 | no | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.489 | 0.524 | 0.172 | 0.222 | 6.65 | 6.20 | 0.955/1.004 | KXNHLTOTAL-26OCT06NSHTOR-6 -0.072 |
| CAR @ MTL | 0.508 | 0.519 | 0.179 | 0.221 | 6.05 | 6.19 | 0.942/0.986 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL3 +0.031 |
| OTT @ DET | 0.577 | 0.523 | 0.177 | 0.218 | 6.12 | 6.07 | 0.998/1.050 | KXNHLSPREAD-26OCT06OTTDET-DET2 -0.055 |
| UTA @ NJD | 0.500 | 0.488 | 0.176 | 0.221 | 6.00 | 6.10 | 0.983/0.990 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA4 +0.025 |
| MIN @ BUF | 0.522 | 0.506 | 0.175 | 0.215 | 6.42 | 6.40 | 0.999/0.991 | KXNHLSPREAD-26OCT06MINBUF-MIN3 +0.018 |
| NYI @ NYR | 0.629 | 0.588 | 0.175 | 0.220 | 5.97 | 5.93 | 0.934/0.977 | KXNHLSPREAD-26OCT06NYINYR-NYR2 -0.052 |
| STL @ CHI | 0.426 | 0.434 | 0.182 | 0.217 | 5.78 | 6.13 | 0.995/0.976 | KXNHLTOTAL-26OCT06STLCHI-7 +0.061 |
| VGK @ SEA | 0.503 | 0.485 | 0.174 | 0.223 | 6.38 | 6.10 | 1.001/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.045 |
| FLA @ LAK | 0.557 | 0.580 | 0.172 | 0.220 | 6.25 | 5.96 | 0.995/1.014 | KXNHLTOTAL-26OCT06FLALA-6 -0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 36 recommended · full analysis in card.md / packet.json `thesis_card`

- Gavin McKenna: 1+ goals NO @ 79c · p 0.8457 (adj 0.8305) · $8.65 · thesis TOR:SUPPRESSED
- Adam Wilsby: 1+ goals YES @ 4c · p 0.0624 (adj 0.0556) · $1.25 · thesis NSH:OFFENSE_4PLUS
- Alexander Kerfoot: 1+ goals YES @ 12c · p 0.1556 (adj 0.1454) · $2.07 · thesis NSH:OFFENSE_4PLUS
- Ryan O'Reilly: 1+ goals YES @ 25c · p 0.2991 (adj 0.2856) · $3.18 · thesis NSH:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 72c · p 0.8549 (adj 0.7607) · $8.65 · thesis MTL:SUPPRESSED
- Jake Evans: 1+ goals YES @ 11c · p 0.1428 (adj 0.1321) · $1.74 · thesis MTL:WINS_BY_2PLUS
- Phillip Danault: 1+ goals YES @ 10c · p 0.1275 (adj 0.1194) · $1.49 · thesis MTL:OFFENSE_4PLUS
- Alexandre Texier: 1+ goals YES @ 12c · p 0.1499 (adj 0.1412) · $1.72 · thesis MTL:OFFENSE_4PLUS
- William Eklund: 1+ assists NO @ 66c · p 0.8486 (adj 0.7228) · $8.65 · thesis OTT:SUPPRESSED
- Andrew Copp: 1+ goals YES @ 18c · p 0.2284 (adj 0.215) · $3.15 · thesis DET:OFFENSE_4PLUS
- Jordan Spence: 1+ assists YES @ 27c · p 0.3533 (adj 0.3066) · $3.24 · thesis OTT:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 39c · p 0.4432 (adj 0.4286) · $3.95 · thesis DET:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8417 (adj 0.7236) · $8.23 · thesis UTA:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2129 (adj 0.1984) · $3.35 · thesis UTA:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 64c · p 0.8084 (adj 0.6892) · $8.23 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 11c · p 0.1427 (adj 0.1333) · $1.82 · thesis NJD:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1473 (adj 0.1317) · $3.54 · thesis MIN:OFFENSE_4PLUS
- Zach Metsa: 1+ goals NO @ 93c · p 0.9624 (adj 0.9531) · $8.65 · thesis DIFFUSE
- Ryan Hartman: 1+ assists YES @ 21c · p 0.3495 (adj 0.2523) · $2.71 · thesis MIN:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 11c · p 0.1418 (adj 0.1326) · $1.78 · thesis BUF:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 8c · p 0.1112 (adj 0.1009) · $1.66 · thesis NYI:OFFENSE_4PLUS
- Matthew Schaefer: 1+ goals NO @ 81c · p 0.8538 (adj 0.8416) · $8.65 · thesis NYI:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3369 (adj 0.2934) · $2.57 · thesis NYR:OFFENSE_4PLUS
- Matt Rempe: 1+ goals YES @ 8c · p 0.1027 (adj 0.0958) · $1.09 · thesis NYR:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1687 (adj 0.1528) · $4.0 · thesis CHI:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 7c · p 0.1003 (adj 0.0915) · $1.74 · thesis STL:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7383 (adj 0.6354) · $8.65 · thesis CHI:SUPPRESSED
- Dillon Dube: 1+ goals YES @ 8c · p 0.1061 (adj 0.0983) · $1.45 · thesis STL:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 10c · p 0.1407 (adj 0.1293) · $2.36 · thesis SEA:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0757 (adj 0.0668) · $1.51 · thesis VGK:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1144 (adj 0.1008) · $1.43 · thesis SEA:OFFENSE_4PLUS
- Vegas wins by over 1.5 goals NO @ 62c · p 0.7087 (adj 0.6619) · $7.23 · thesis SEA:WINS
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7706 (adj 0.7467) · $7.97 · thesis FLA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 63c · p 0.7886 (adj 0.6823) · $7.97 · thesis LAK:SUPPRESSED
- Alex Laferriere: 1+ assists YES @ 27c · p 0.3866 (adj 0.3076) · $2.95 · thesis LAK:OFFENSE_4PLUS
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2745 (adj 0.2621) · $2.72 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 147/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 30.05, exp saves 26.01 (sd 6.97), pull risk 0.061
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.03, exp saves 24.15 (sd 6.66), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Stolarz: 25+ saves | 0.590 | 0.405 | 50/69 | +0.073 |  |
| Gavin McKenna: 1+ assists | 0.176 | 0.320 | 33/69 | +0.119 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.292 | 0.420 | 44/60 | +0.091 | STANDARD |
| Kirill Marchenko: 1+ points | 0.487 | 0.605 | 62/41 | +0.086 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.490 | 0.385 | 40/63 | +0.073 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.359 | 0.255 | 27/76 | +0.076 | STANDARD |

**CAR @ MTL** · priced 149/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.78, exp saves 26.8 (sd 7.13), pull risk 0.053
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.05, exp saves 19.88 (sd 5.78), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.145 | 0.290 | 30/72 | +0.121 | STANDARD |
| Sebastian Aho: 1+ points | 0.489 | 0.615 | 63/40 | +0.094 | STANDARD |
| Chris Kreider: 1+ points | 0.339 | 0.460 | 47/55 | +0.094 | STANDARD |
| Sebastian Aho: 1+ assists | 0.316 | 0.435 | 44/57 | +0.097 | STANDARD |
| Sebastian Aho: 2+ points | 0.145 | 0.245 | 26/77 | +0.073 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.379 | 0.460 | 48/56 | +0.044 | STANDARD |

**OTT @ DET** · priced 140/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 27.75, exp saves 24.02 (sd 6.57), pull risk 0.054
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.38, exp saves 22.72 (sd 6.37), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.151 | 0.345 | 35/66 | +0.173 | STANDARD |
| William Eklund: 1+ points | 0.316 | 0.495 | 50/51 | +0.156 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.259 | 0.430 | 44/58 | +0.144 | PRIOR_HEAVY |
| Andrew Copp: 1+ points | 0.555 | 0.415 | 42/59 | +0.118 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.203 | 0.335 | 34/67 | +0.111 | PRIOR_HEAVY |
| William Eklund: 2+ points | 0.054 | 0.165 | 17/84 | +0.097 | STANDARD |

**UTA @ NJD** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.37), pull risk 0.063
- UTA net: Karel Vejmelka (PROBABLE) exp shots 28.76, exp saves 24.97 (sd 6.68), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.192 | 0.375 | 39/64 | +0.152 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.158 | 0.340 | 35/67 | +0.156 | STANDARD |
| Luke Evangelista: 1+ points | 0.336 | 0.505 | 52/51 | +0.136 | STANDARD |
| Vincent Trocheck: 1+ points | 0.325 | 0.460 | 47/55 | +0.108 | STANDARD |
| Jack Hughes: 2+ points | 0.230 | 0.345 | 37/68 | +0.075 | STANDARD |
| Jack Hughes: 1+ assists | 0.395 | 0.510 | 53/51 | +0.077 | STANDARD |

**MIN @ BUF** · priced 149/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.64), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.86, exp saves 25.82 (sd 6.99), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colten Ellis: 25+ saves | 0.460 | 0.290 | 53/95 | -0.087 |  |
| Ryan Hartman: 1+ points | 0.514 | 0.355 | 36/65 | +0.138 | STANDARD |
| Ryan Hartman: 1+ assists | 0.349 | 0.200 | 21/81 | +0.128 | STANDARD |
| Jesper Wallstedt: 25+ saves | 0.578 | 0.435 | 50/63 | +0.061 |  |
| Tage Thompson: 1+ assists | 0.340 | 0.445 | 47/58 | +0.063 | STANDARD |
| Tage Thompson: 1+ points | 0.556 | 0.660 | 68/36 | +0.067 | STANDARD |

**NYI @ NYR** · priced 156/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.05, exp saves 24.57 (sd 6.5), pull risk 0.044
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 25.47, exp saves 21.89 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Palmieri: 1+ assists | 0.171 | 0.285 | 30/73 | +0.085 | STANDARD |
| Kyle Palmieri: 1+ points | 0.350 | 0.450 | 47/57 | +0.063 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.389 | 0.300 | 31/71 | +0.064 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.337 | 0.250 | 26/76 | +0.063 | STANDARD |
| Semyon Varlamov: 24+ saves | 0.389 | 0.475 | 54/59 | +0.004 |  |
| Matias Maccelli: 1+ assists | 0.183 | 0.265 | 28/75 | +0.054 | STANDARD |

**STL @ CHI** · priced 148/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.19, exp saves 23.24 (sd 6.49), pull risk 0.067
- STL net: Joel Hofer (CONFIRMED) exp shots 25.55, exp saves 22.31 (sd 6.13), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 23+ saves | 0.547 | 0.300 | 55/95 | -0.020 |  |
| Patrick Kane: 1+ assists | 0.262 | 0.420 | 43/59 | +0.131 | STANDARD |
| Bowen Byram: 1+ points | 0.316 | 0.445 | 45/56 | +0.107 | STANDARD |
| Patrick Kane: 1+ points | 0.444 | 0.570 | 58/44 | +0.099 | STANDARD |
| Mason McTavish: 1+ points | 0.392 | 0.495 | 51/52 | +0.071 | STANDARD |
| Bowen Byram: 1+ assists | 0.229 | 0.330 | 34/68 | +0.075 | STANDARD |

**VGK @ SEA** · priced 143/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.49, exp saves 24.64 (sd 6.77), pull risk 0.058
- VGK net: Adin Hill (PROJECTED) exp shots 25.65, exp saves 22.19 (sd 6.17), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.206 | 0.350 | 36/66 | +0.118 | STANDARD |
| Jack Eichel: 1+ assists | 0.407 | 0.540 | 55/47 | +0.106 | STANDARD |
| Mitch Marner: 1+ assists | 0.385 | 0.505 | 52/51 | +0.088 | STANDARD |
| Jack Eichel: 1+ points | 0.570 | 0.685 | 69/32 | +0.095 | STANDARD |
| Mitch Marner: 1+ points | 0.530 | 0.640 | 65/37 | +0.084 | STANDARD |
| Mitch Marner: 2+ points | 0.185 | 0.290 | 31/73 | +0.071 | STANDARD |

**FLA @ LAK** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 26.39, exp saves 23.09 (sd 6.23), pull risk 0.049
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.81, exp saves 23.61 (sd 6.55), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.211 | 0.375 | 38/63 | +0.142 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.375 | 38/63 | +0.122 | STANDARD |
| Brady Tkachuk: 1+ points | 0.422 | 0.565 | 58/45 | +0.110 | STANDARD |
| Sam Reinhart: 1+ points | 0.460 | 0.595 | 61/42 | +0.103 | STANDARD |
| Artemi Panarin: 1+ assists | 0.390 | 0.515 | 52/49 | +0.103 | STANDARD |
| Alex Laferriere: 1+ assists | 0.387 | 0.265 | 27/74 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
