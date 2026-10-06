# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T22:37:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 3717 · contracts joined: 1832 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 1607, 'OK': 138, 'NO_EDGE': 87}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'player_assists': 221, 'game_early_goal': 9, 'first_goal': 314, 'game_winner': 18, 'player_goals': 551, 'game_overtime': 9, 'player_points': 276, 'goalie_saves': 11, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-10m | 0.489 | 0.511 | 0.172 | 6.65 | 3.29 | 3.36 | 200 (25/175) | CONFIRMED/CONFIRMED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-10m | 0.508 | 0.492 | 0.179 | 6.05 | 3.05 | 3.01 | 202 (25/177) | CONFIRMED/PROBABLE |
| OTT @ DET | 2026-10-06T23:00:00Z | T-10m | 0.591 | 0.409 | 0.174 | 6.23 | 3.41 | 2.82 | 199 (25/174) | PROBABLE/CONFIRMED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-10m | 0.500 | 0.500 | 0.176 | 6.00 | 3.01 | 3.00 | 210 (25/185) | CONFIRMED/PROBABLE |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-10m | 0.522 | 0.478 | 0.175 | 6.42 | 3.28 | 3.14 | 207 (25/182) | PROBABLE/CONFIRMED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-30m | 0.629 | 0.371 | 0.175 | 5.97 | 3.40 | 2.58 | 207 (25/182) | CONFIRMED/CONFIRMED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-60m | 0.426 | 0.574 | 0.182 | 5.78 | 2.67 | 3.12 | 199 (25/174) | PROBABLE/CONFIRMED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-3h | 0.503 | 0.497 | 0.174 | 6.38 | 3.21 | 3.17 | 198 (25/173) | PROBABLE/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-3h | 0.557 | 0.443 | 0.172 | 6.25 | 3.31 | 2.94 | 210 (25/185) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.503 | 0.375 | 0.400 | 38 | 63 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.443 | 0.315 | 0.339 | 33 | 70 | yes | +0.097 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.497 | 0.615 | 0.592 | 62 | 39 | no | +0.097 | OK |
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.511 | 0.405 | 0.426 | 41 | 60 | yes | +0.084 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.489 | 0.595 | 0.574 | 60 | 41 | no | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.651 | 0.545 | 0.567 | 55 | 46 | yes | +0.084 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.286 | 0.385 | 0.364 | 39 | 62 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.624 | 0.525 | 0.545 | 53 | 48 | yes | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.256 | 0.160 | 0.177 | 17 | 85 | yes | +0.076 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.172 | 0.265 | 0.244 | 27 | 74 | no | +0.075 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.283 | 0.375 | 0.356 | 38 | 63 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.291 | 0.205 | 0.221 | 21 | 80 | yes | +0.070 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.322 | 0.235 | 0.251 | 24 | 77 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.300 | 0.215 | 0.231 | 22 | 79 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.412 | 0.315 | 0.334 | 33 | 70 | yes | +0.067 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.523 | 0.435 | 0.452 | 44 | 57 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.842 | 0.765 | 0.782 | 77 | 24 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.229 | 0.150 | 0.164 | 16 | 86 | yes | +0.060 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.236 | 0.165 | 0.178 | 17 | 84 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.651 | 0.575 | 0.591 | 58 | 43 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.054 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-6 | game_total | 0.631 | 0.555 | 0.570 | 56 | 45 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.175 | 0.245 | 0.230 | 25 | 76 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.126 | 0.060 | 0.070 | 7 | 95 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.187 | 0.125 | 0.136 | 13 | 88 | yes | +0.049 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.443 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.557 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.675 | 0.605 | 0.620 | 61 | 40 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.434 | 0.365 | 0.378 | 37 | 64 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.371 | 0.305 | 0.318 | 31 | 70 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.240 | 0.305 | 0.291 | 31 | 70 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.134 | 0.195 | 0.181 | 20 | 81 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.117 | 0.175 | 0.162 | 18 | 83 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.181 | 0.125 | 0.135 | 13 | 88 | yes | +0.043 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.409 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR4 | team_total | 0.365 | 0.425 | 0.413 | 43 | 58 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET4 | team_total | 0.454 | 0.395 | 0.407 | 40 | 61 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.210 | 0.265 | 0.253 | 27 | 74 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-10 | game_total | 0.120 | 0.070 | 0.078 | 8 | 94 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.257 | 0.205 | 0.215 | 21 | 80 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.620 | 0.675 | 0.664 | 68 | 33 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT06UTANJ-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.591 | 0.535 | 0.546 | 54 | 47 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.165 | 0.215 | 0.204 | 22 | 79 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.106 | 0.060 | 0.067 | 7 | 95 | yes | +0.031 | OK |
| KXNHLGAME-26OCT06CARMTL-CAR | game_winner | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLGAME-26OCT06CARMTL-MTL | game_winner | 0.508 | 0.455 | 0.466 | 46 | 55 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.211 | 0.165 | 0.173 | 17 | 84 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.823 | 0.765 | 0.778 | 78 | 25 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT06UTANJ-5 | game_total | 0.748 | 0.795 | 0.786 | 80 | 21 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR3 | team_total | 0.585 | 0.640 | 0.629 | 65 | 37 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI3 | game_spread | 0.095 | 0.135 | 0.126 | 14 | 87 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT3 | team_total | 0.536 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-5 | game_total | 0.819 | 0.775 | 0.784 | 78 | 23 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR2 | game_spread | 0.278 | 0.325 | 0.315 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ4 | team_total | 0.367 | 0.415 | 0.405 | 42 | 59 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR2 | team_total | 0.794 | 0.840 | 0.832 | 85 | 17 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT06UTANJ-4 | game_total | 0.838 | 0.875 | 0.868 | 88 | 13 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.765 | 0.805 | 0.797 | 81 | 20 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.755 | 0.795 | 0.787 | 80 | 21 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT06STLCHI-6 | game_total | 0.490 | 0.535 | 0.526 | 54 | 47 | no | +0.023 | OK |
| KXNHLGAME-26OCT06NYINYR-NYI | game_winner | 0.371 | 0.415 | 0.406 | 42 | 59 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.233 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.820 | 0.855 | 0.848 | 86 | 15 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF4 | team_total | 0.428 | 0.385 | 0.393 | 39 | 62 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI2 | game_spread | 0.177 | 0.215 | 0.207 | 22 | 79 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.352 | 0.395 | 0.386 | 40 | 61 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06VGKSEA-8 | game_total | 0.284 | 0.245 | 0.253 | 25 | 76 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ3 | team_total | 0.583 | 0.625 | 0.617 | 63 | 38 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-4 | game_total | 0.889 | 0.855 | 0.862 | 86 | 15 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.324 | 0.370 | 0.361 | 38 | 64 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT06STLCHI-5 | game_total | 0.717 | 0.755 | 0.748 | 76 | 25 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ5 | team_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.218 | 0.255 | 0.247 | 26 | 75 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.241 | 0.195 | 0.204 | 21 | 82 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.170 | 0.205 | 0.198 | 21 | 80 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.115 | 0.080 | 0.086 | 9 | 93 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.404 | 0.445 | 0.437 | 45 | 56 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET6 | team_total | 0.125 | 0.090 | 0.096 | 10 | 92 | yes | +0.019 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.489 | 0.524 | 0.172 | 0.222 | 6.65 | 6.20 | 0.955/1.004 | KXNHLTOTAL-26OCT06NSHTOR-6 -0.072 |
| CAR @ MTL | 0.508 | 0.519 | 0.179 | 0.221 | 6.05 | 6.19 | 0.942/0.986 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL3 +0.031 |
| OTT @ DET | 0.591 | 0.531 | 0.174 | 0.220 | 6.23 | 6.12 | 0.998/1.071 | KXNHLSPREAD-26OCT06OTTDET-DET2 -0.068 |
| UTA @ NJD | 0.500 | 0.488 | 0.176 | 0.221 | 6.00 | 6.10 | 0.983/0.990 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA4 +0.025 |
| MIN @ BUF | 0.522 | 0.506 | 0.175 | 0.215 | 6.42 | 6.40 | 0.999/0.991 | KXNHLSPREAD-26OCT06MINBUF-MIN3 +0.018 |
| NYI @ NYR | 0.629 | 0.588 | 0.175 | 0.220 | 5.97 | 5.93 | 0.934/0.977 | KXNHLSPREAD-26OCT06NYINYR-NYR2 -0.052 |
| STL @ CHI | 0.426 | 0.434 | 0.182 | 0.217 | 5.78 | 6.13 | 0.995/0.976 | KXNHLTOTAL-26OCT06STLCHI-7 +0.061 |
| VGK @ SEA | 0.503 | 0.485 | 0.174 | 0.223 | 6.38 | 6.10 | 1.001/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.045 |
| FLA @ LAK | 0.557 | 0.580 | 0.172 | 0.220 | 6.25 | 5.96 | 0.995/1.014 | KXNHLTOTAL-26OCT06FLALA-6 -0.060 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 36 recommended · full analysis in card.md / packet.json `thesis_card`

- Gavin McKenna: 1+ goals NO @ 79c · p 0.8457 (adj 0.8305) · $8.1 · thesis TOR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1364 (adj 0.126) · $2.03 · thesis TOR:OFFENSE_4PLUS
- Adam Wilsby: 1+ goals YES @ 4c · p 0.0624 (adj 0.0556) · $1.17 · thesis NSH:OFFENSE_4PLUS
- Alexander Kerfoot: 1+ goals YES @ 12c · p 0.1556 (adj 0.1454) · $1.93 · thesis NSH:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 11c · p 0.1428 (adj 0.1321) · $1.6 · thesis MTL:WINS_BY_2PLUS
- Nikolaj Ehlers: 1+ goals NO @ 74c · p 0.7852 (adj 0.7727) · $7.91 · thesis CAR:SUPPRESSED
- Alexandre Texier: 1+ goals YES @ 12c · p 0.1499 (adj 0.1412) · $1.6 · thesis MTL:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 73c · p 0.8549 (adj 0.7607) · $8.1 · thesis MTL:SUPPRESSED
- William Eklund: 1+ assists NO @ 66c · p 0.8539 (adj 0.7214) · $8.1 · thesis OTT:SUPPRESSED
- Andrew Copp: 1+ goals YES @ 18c · p 0.2343 (adj 0.2195) · $3.51 · thesis DET:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 39c · p 0.4565 (adj 0.4386) · $5.42 · thesis DET:OFFENSE_4PLUS
- Jordan Spence: 1+ assists YES @ 26c · p 0.34 (adj 0.2975) · $3.21 · thesis OTT:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8417 (adj 0.7236) · $7.7 · thesis UTA:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2129 (adj 0.1984) · $3.14 · thesis UTA:OFFENSE_4PLUS
- Luke Evangelista: 1+ assists NO @ 64c · p 0.8084 (adj 0.6892) · $7.7 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 11c · p 0.1427 (adj 0.1333) · $1.7 · thesis NJD:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1473 (adj 0.1317) · $3.31 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 21c · p 0.3495 (adj 0.2523) · $2.47 · thesis MIN:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 11c · p 0.1418 (adj 0.1326) · $1.69 · thesis BUF:OFFENSE_4PLUS
- Michael McCarron: 1+ goals YES @ 10c · p 0.1287 (adj 0.1203) · $1.41 · thesis MIN:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 8c · p 0.1112 (adj 0.1009) · $1.59 · thesis NYI:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3272 (adj 0.2886) · $2.12 · thesis NYR:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 70c · p 0.7383 (adj 0.7275) · $4.77 · thesis NYI:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.6975 (adj 0.6869) · $4.13 · thesis NYR:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 11c · p 0.1687 (adj 0.1528) · $3.44 · thesis CHI:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 7c · p 0.1003 (adj 0.0915) · $1.53 · thesis STL:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7383 (adj 0.6354) · $7.64 · thesis CHI:SUPPRESSED
- Mason McTavish: 1+ assists NO @ 70c · p 0.7863 (adj 0.7381) · $7.64 · thesis STL:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.1407 (adj 0.1293) · $2.33 · thesis SEA:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 70c · p 0.7599 (adj 0.7437) · $8.1 · thesis VGK:SUPPRESSED
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1144 (adj 0.1033) · $1.75 · thesis SEA:OFFENSE_4PLUS
- Matty Beniers: 1+ goals YES @ 18c · p 0.2282 (adj 0.2149) · $2.94 · thesis SEA:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 69c · p 0.7706 (adj 0.7492) · $7.04 · thesis FLA:SUPPRESSED
- Mats Zuccarello: 1+ assists NO @ 64c · p 0.7886 (adj 0.6855) · $7.04 · thesis LAK:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 23c · p 0.2745 (adj 0.2621) · $2.43 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ assists NO @ 49c · p 0.6102 (adj 0.5288) · $3.73 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 147/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 30.05, exp saves 26.01 (sd 6.97), pull risk 0.061
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.03, exp saves 24.15 (sd 6.66), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Stolarz: 25+ saves | 0.590 | 0.400 | 48/68 | +0.093 |  |
| Gavin McKenna: 1+ assists | 0.176 | 0.325 | 34/69 | +0.119 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.292 | 0.420 | 44/60 | +0.091 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.490 | 0.375 | 39/64 | +0.083 | STANDARD |
| Kirill Marchenko: 1+ points | 0.487 | 0.600 | 62/42 | +0.076 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.359 | 0.250 | 26/76 | +0.086 | STANDARD |

**CAR @ MTL** · priced 149/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.78, exp saves 26.8 (sd 7.13), pull risk 0.053
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.05, exp saves 19.88 (sd 5.78), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.145 | 0.290 | 31/73 | +0.111 | STANDARD |
| Chris Kreider: 1+ points | 0.339 | 0.470 | 48/54 | +0.104 | STANDARD |
| Sebastian Aho: 1+ assists | 0.316 | 0.435 | 44/57 | +0.097 | STANDARD |
| Sebastian Aho: 1+ points | 0.489 | 0.605 | 62/41 | +0.084 | STANDARD |
| Sebastian Aho: 2+ points | 0.145 | 0.245 | 26/77 | +0.073 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.379 | 0.465 | 48/55 | +0.054 | STANDARD |

**OTT @ DET** · priced 138/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 27.75, exp saves 24.11 (sd 6.58), pull risk 0.05
- OTT net: Samuel Ersson (CONFIRMED) exp shots 26.38, exp saves 22.71 (sd 6.35), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.146 | 0.350 | 36/66 | +0.178 | STANDARD |
| William Eklund: 1+ points | 0.309 | 0.495 | 50/51 | +0.164 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.258 | 0.430 | 44/58 | +0.145 | PRIOR_HEAVY |
| Andrew Copp: 1+ points | 0.567 | 0.415 | 42/59 | +0.130 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.203 | 0.335 | 34/67 | +0.112 | PRIOR_HEAVY |
| Tim Stutzle: 1+ assists | 0.373 | 0.490 | 50/52 | +0.089 | STANDARD |

**UTA @ NJD** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.37), pull risk 0.063
- UTA net: Karel Vejmelka (PROBABLE) exp shots 28.76, exp saves 24.97 (sd 6.68), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.192 | 0.375 | 39/64 | +0.152 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.158 | 0.340 | 35/67 | +0.156 | STANDARD |
| Luke Evangelista: 1+ points | 0.336 | 0.505 | 52/51 | +0.136 | STANDARD |
| Vincent Trocheck: 1+ points | 0.325 | 0.455 | 47/56 | +0.098 | STANDARD |
| Jack Hughes: 1+ assists | 0.395 | 0.515 | 53/50 | +0.087 | STANDARD |
| Jack Hughes: 2+ points | 0.230 | 0.340 | 36/68 | +0.075 | STANDARD |

**MIN @ BUF** · priced 149/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.64), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.86, exp saves 25.82 (sd 6.99), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colten Ellis: 25+ saves | 0.460 | 0.290 | 53/95 | -0.087 |  |
| Ryan Hartman: 1+ points | 0.514 | 0.355 | 36/65 | +0.138 | STANDARD |
| Ryan Hartman: 1+ assists | 0.349 | 0.200 | 21/81 | +0.128 | STANDARD |
| Tage Thompson: 1+ assists | 0.340 | 0.460 | 48/56 | +0.083 | STANDARD |
| Tage Thompson: 2+ points | 0.198 | 0.300 | 32/72 | +0.068 | STANDARD |
| Tage Thompson: 1+ points | 0.556 | 0.655 | 66/35 | +0.078 | STANDARD |

**NYI @ NYR** · priced 154/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.05, exp saves 24.57 (sd 6.5), pull risk 0.044
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 25.47, exp saves 21.89 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Palmieri: 1+ assists | 0.171 | 0.290 | 30/72 | +0.095 | STANDARD |
| Kyle Palmieri: 1+ points | 0.350 | 0.445 | 46/57 | +0.063 | STANDARD |
| Semyon Varlamov: 24+ saves | 0.389 | 0.480 | 53/57 | +0.024 |  |
| Matias Maccelli: 1+ assists | 0.183 | 0.270 | 29/75 | +0.054 | STANDARD |
| Gabe Perreault: 1+ points | 0.467 | 0.390 | 40/62 | +0.051 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.327 | 0.250 | 26/76 | +0.054 | STANDARD |

**STL @ CHI** · priced 148/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.19, exp saves 23.24 (sd 6.49), pull risk 0.067
- STL net: Joel Hofer (CONFIRMED) exp shots 25.55, exp saves 22.31 (sd 6.13), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 23+ saves | 0.547 | 0.295 | 54/95 | -0.010 |  |
| Patrick Kane: 1+ assists | 0.262 | 0.420 | 43/59 | +0.131 | STANDARD |
| Patrick Kane: 1+ points | 0.444 | 0.570 | 58/44 | +0.099 | STANDARD |
| Bowen Byram: 1+ assists | 0.229 | 0.335 | 34/67 | +0.085 | STANDARD |
| Bowen Byram: 1+ points | 0.316 | 0.420 | 43/59 | +0.077 | STANDARD |
| Mason McTavish: 1+ points | 0.392 | 0.495 | 51/52 | +0.071 | STANDARD |

**VGK @ SEA** · priced 143/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.49, exp saves 24.64 (sd 6.77), pull risk 0.058
- VGK net: Adin Hill (PROJECTED) exp shots 25.65, exp saves 22.19 (sd 6.17), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joey Daccord: 25+ saves | 0.503 | 0.290 | 53/95 | -0.045 |  |
| Jack Eichel: 2+ points | 0.206 | 0.355 | 37/66 | +0.118 | STANDARD |
| Jack Eichel: 1+ assists | 0.407 | 0.545 | 56/47 | +0.106 | STANDARD |
| Mitch Marner: 1+ assists | 0.385 | 0.505 | 52/51 | +0.088 | STANDARD |
| Mitch Marner: 1+ points | 0.530 | 0.650 | 66/36 | +0.094 | STANDARD |
| Jack Eichel: 1+ points | 0.570 | 0.685 | 69/32 | +0.095 | STANDARD |

**FLA @ LAK** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 26.39, exp saves 23.09 (sd 6.23), pull risk 0.049
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.81, exp saves 23.61 (sd 6.55), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.211 | 0.370 | 38/64 | +0.132 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.375 | 38/63 | +0.122 | STANDARD |
| Brady Tkachuk: 1+ points | 0.422 | 0.565 | 58/45 | +0.110 | STANDARD |
| Sam Reinhart: 1+ points | 0.460 | 0.595 | 61/42 | +0.103 | STANDARD |
| Artemi Panarin: 1+ assists | 0.390 | 0.515 | 52/49 | +0.103 | STANDARD |
| Alex Laferriere: 1+ assists | 0.387 | 0.265 | 27/74 | +0.103 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
