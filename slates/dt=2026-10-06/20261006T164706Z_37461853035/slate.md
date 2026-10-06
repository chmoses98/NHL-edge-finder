# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T16:47:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 3720 · contracts joined: 1837 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 1612, 'OK': 128, 'NO_EDGE': 97}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'player_assists': 223, 'game_early_goal': 9, 'first_goal': 316, 'game_winner': 18, 'player_goals': 554, 'game_overtime': 9, 'player_points': 278, 'goalie_saves': 7, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-6h | 0.489 | 0.511 | 0.172 | 6.65 | 3.29 | 3.36 | 200 (25/175) | CONFIRMED/CONFIRMED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-6h | 0.507 | 0.493 | 0.179 | 6.05 | 3.04 | 3.01 | 208 (25/183) | CONFIRMED/PROJECTED |
| OTT @ DET | 2026-10-06T23:00:00Z | T-6h | 0.577 | 0.423 | 0.177 | 6.12 | 3.31 | 2.81 | 200 (25/175) | PROBABLE/PROJECTED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-6h | 0.498 | 0.502 | 0.178 | 6.02 | 3.02 | 3.00 | 210 (25/185) | CONFIRMED/PROJECTED |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-6h | 0.522 | 0.478 | 0.175 | 6.42 | 3.28 | 3.14 | 207 (25/182) | PROBABLE/CONFIRMED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-6h | 0.616 | 0.384 | 0.170 | 6.06 | 3.40 | 2.66 | 207 (25/182) | PROJECTED/CONFIRMED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-6h | 0.437 | 0.563 | 0.181 | 5.84 | 2.72 | 3.12 | 199 (25/174) | PROBABLE/PROJECTED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-6h | 0.482 | 0.518 | 0.178 | 6.24 | 3.07 | 3.17 | 197 (25/172) | PROJECTED/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-6h | 0.561 | 0.439 | 0.176 | 6.16 | 3.26 | 2.90 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.443 | 0.325 | 0.347 | 34 | 69 | yes | +0.087 | OK |
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.482 | 0.375 | 0.396 | 38 | 63 | yes | +0.086 | OK |
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.511 | 0.405 | 0.426 | 41 | 60 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.651 | 0.540 | 0.563 | 55 | 47 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.256 | 0.155 | 0.172 | 17 | 86 | yes | +0.076 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.518 | 0.615 | 0.596 | 62 | 39 | no | +0.076 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.489 | 0.585 | 0.566 | 59 | 42 | no | +0.074 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.322 | 0.235 | 0.251 | 24 | 77 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.300 | 0.215 | 0.231 | 22 | 79 | yes | +0.068 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.523 | 0.435 | 0.452 | 44 | 57 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.182 | 0.265 | 0.247 | 27 | 74 | no | +0.065 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.561 | 0.475 | 0.492 | 48 | 53 | yes | +0.064 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.439 | 0.525 | 0.508 | 53 | 48 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.300 | 0.385 | 0.367 | 39 | 62 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.283 | 0.365 | 0.348 | 37 | 64 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.236 | 0.165 | 0.178 | 17 | 84 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-6 | game_total | 0.631 | 0.555 | 0.570 | 56 | 45 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.175 | 0.245 | 0.230 | 25 | 76 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.126 | 0.060 | 0.070 | 7 | 95 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.842 | 0.765 | 0.782 | 78 | 25 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.120 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.596 | 0.525 | 0.539 | 53 | 48 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.270 | 0.205 | 0.217 | 21 | 80 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.237 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT3 | team_total | 0.536 | 0.610 | 0.596 | 62 | 40 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.382 | 0.310 | 0.324 | 32 | 70 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.644 | 0.575 | 0.589 | 58 | 43 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.422 | 0.355 | 0.368 | 36 | 65 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.137 | 0.195 | 0.182 | 20 | 81 | no | +0.042 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.423 | 0.485 | 0.472 | 49 | 52 | no | +0.040 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.577 | 0.515 | 0.528 | 52 | 49 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.187 | 0.135 | 0.144 | 14 | 87 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.352 | 0.295 | 0.306 | 30 | 71 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.219 | 0.280 | 0.267 | 29 | 73 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.203 | 0.150 | 0.160 | 16 | 86 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.766 | 0.815 | 0.806 | 82 | 19 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.622 | 0.675 | 0.665 | 68 | 33 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT06UTANJ-6 | game_total | 0.531 | 0.585 | 0.574 | 59 | 42 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.322 | 0.385 | 0.372 | 40 | 63 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT06UTANJ-5 | game_total | 0.747 | 0.795 | 0.786 | 80 | 21 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.231 | 0.180 | 0.190 | 19 | 83 | yes | +0.031 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.553 | 0.605 | 0.595 | 61 | 40 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.220 | 0.175 | 0.183 | 18 | 83 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ4 | team_total | 0.374 | 0.430 | 0.419 | 44 | 58 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ3 | team_total | 0.585 | 0.635 | 0.625 | 64 | 37 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT06UTANJ-4 | game_total | 0.834 | 0.875 | 0.868 | 88 | 13 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.219 | 0.265 | 0.255 | 27 | 74 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.162 | 0.205 | 0.196 | 21 | 80 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-5 | game_total | 0.819 | 0.775 | 0.784 | 78 | 23 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.752 | 0.795 | 0.787 | 80 | 21 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.206 | 0.165 | 0.173 | 17 | 84 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ5 | team_total | 0.191 | 0.240 | 0.230 | 25 | 77 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR2 | game_spread | 0.392 | 0.345 | 0.354 | 35 | 66 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-10 | game_total | 0.120 | 0.080 | 0.087 | 9 | 93 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.108 | 0.070 | 0.076 | 8 | 94 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.649 | 0.600 | 0.610 | 61 | 41 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.160 | 0.125 | 0.131 | 13 | 88 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR3 | team_total | 0.582 | 0.630 | 0.620 | 64 | 38 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.819 | 0.860 | 0.853 | 87 | 15 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.343 | 0.395 | 0.384 | 41 | 62 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT5 | team_total | 0.159 | 0.200 | 0.191 | 21 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-4 | game_total | 0.889 | 0.855 | 0.862 | 86 | 15 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR2 | game_spread | 0.275 | 0.315 | 0.307 | 32 | 69 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.403 | 0.445 | 0.437 | 45 | 56 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.241 | 0.205 | 0.212 | 21 | 80 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.830 | 0.790 | 0.799 | 80 | 22 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI3 | game_spread | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.801 | 0.755 | 0.765 | 77 | 26 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN2 | game_spread | 0.267 | 0.305 | 0.297 | 31 | 70 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT06CARMTL-6 | game_total | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR2 | team_total | 0.794 | 0.830 | 0.823 | 84 | 18 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.090 | 0.060 | 0.065 | 7 | 95 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI2 | game_spread | 0.193 | 0.225 | 0.218 | 23 | 78 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET4 | team_total | 0.432 | 0.390 | 0.398 | 40 | 62 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR4 | team_total | 0.369 | 0.405 | 0.398 | 41 | 60 | no | +0.015 | OK |
| KXNHLGAME-26OCT06MINBUF-BUF | game_winner | 0.522 | 0.485 | 0.492 | 49 | 52 | yes | +0.014 | OK |
| KXNHLGAME-26OCT06UTANJ-UTA | game_winner | 0.502 | 0.465 | 0.472 | 47 | 54 | yes | +0.014 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.489 | 0.522 | 0.172 | 0.219 | 6.65 | 6.20 | 0.955/1.004 | KXNHLTOTAL-26OCT06NSHTOR-6 -0.078 |
| CAR @ MTL | 0.507 | 0.523 | 0.179 | 0.223 | 6.05 | 6.22 | 0.942/0.997 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL4 +0.036 |
| OTT @ DET | 0.577 | 0.519 | 0.177 | 0.224 | 6.12 | 6.05 | 0.998/1.040 | KXNHLSPREAD-26OCT06OTTDET-DET2 -0.061 |
| UTA @ NJD | 0.498 | 0.489 | 0.178 | 0.218 | 6.02 | 6.10 | 0.983/0.992 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA4 +0.024 |
| MIN @ BUF | 0.522 | 0.506 | 0.175 | 0.215 | 6.42 | 6.40 | 0.999/0.991 | KXNHLSPREAD-26OCT06MINBUF-MIN3 +0.018 |
| NYI @ NYR | 0.616 | 0.574 | 0.170 | 0.220 | 6.06 | 5.99 | 0.957/0.977 | KXNHLSPREAD-26OCT06NYINYR-NYR2 -0.052 |
| STL @ CHI | 0.437 | 0.445 | 0.181 | 0.218 | 5.84 | 6.17 | 0.995/0.993 | KXNHLTOTAL-26OCT06STLCHI-7 +0.057 |
| VGK @ SEA | 0.482 | 0.482 | 0.178 | 0.222 | 6.24 | 6.10 | 1.005/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.030 |
| FLA @ LAK | 0.561 | 0.582 | 0.176 | 0.222 | 6.16 | 5.94 | 0.992/1.007 | KXNHLTOTAL-26OCT06FLALA-6 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 35 recommended · full analysis in card.md / packet.json `thesis_card`

- Gavin McKenna: 1+ goals NO @ 78c · p 0.8457 (adj 0.828) · $7.61 · thesis TOR:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2056 (adj 0.1955) · $1.82 · thesis NSH:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 61c · p 0.6597 (adj 0.6448) · $4.49 · thesis TOR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1364 (adj 0.1285) · $1.28 · thesis TOR:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 11c · p 0.1498 (adj 0.1373) · $2.17 · thesis MTL:WINS_BY_2PLUS
- Chris Kreider: 1+ assists NO @ 71c · p 0.8572 (adj 0.7518) · $8.07 · thesis MTL:SUPPRESSED
- Alexandre Texier: 1+ goals YES @ 12c · p 0.1515 (adj 0.1411) · $1.53 · thesis MTL:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 70c · p 0.746 (adj 0.732) · $6.17 · thesis CAR:SUPPRESSED
- William Eklund: 1+ assists NO @ 67c · p 0.8461 (adj 0.7284) · $8.07 · thesis OTT:SUPPRESSED
- Andrew Copp: 1+ goals YES @ 18c · p 0.2424 (adj 0.223) · $3.83 · thesis DET:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 10c · p 0.1359 (adj 0.1244) · $1.89 · thesis DET:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 40c · p 0.4441 (adj 0.4318) · $2.81 · thesis DET:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8356 (adj 0.7247) · $8.07 · thesis UTA:SUPPRESSED
- Anthony Mantha: 1+ assists NO @ 73c · p 0.8213 (adj 0.7732) · $8.07 · thesis NJD:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2112 (adj 0.1984) · $2.17 · thesis UTA:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 12c · p 0.1495 (adj 0.1396) · $1.3 · thesis NJD:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1473 (adj 0.133) · $2.48 · thesis MIN:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 21c · p 0.3495 (adj 0.2491) · $2.29 · thesis MIN:OFFENSE_4PLUS
- Marcus Foligno: 1+ goals YES @ 10c · p 0.1346 (adj 0.1247) · $1.87 · thesis MIN:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 11c · p 0.1426 (adj 0.1332) · $1.75 · thesis BUF:OFFENSE_4PLUS
- Oliver Bjorkstrand: 1+ goals NO @ 83c · p 0.8655 (adj 0.8554) · $8.07 · thesis NYR:SUPPRESSED
- Ondrej Palat: 1+ goals YES @ 9c · p 0.113 (adj 0.106) · $1.07 · thesis NYI:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 27c · p 0.3421 (adj 0.2985) · $2.01 · thesis NYR:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 69c · p 0.7306 (adj 0.7179) · $4.53 · thesis NYI:SUPPRESSED
- Ryan Greene: 1+ goals YES @ 11c · p 0.1812 (adj 0.1622) · $4.57 · thesis CHI:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 7c · p 0.1025 (adj 0.0931) · $1.78 · thesis STL:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7344 (adj 0.6373) · $8.07 · thesis CHI:SUPPRESSED
- Mason McTavish: 1+ goals NO @ 74c · p 0.7746 (adj 0.7647) · $3.96 · thesis STL:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 10c · p 0.144 (adj 0.1317) · $2.49 · thesis SEA:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 67c · p 0.7257 (adj 0.7105) · $7.13 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 74c · p 0.8177 (adj 0.7763) · $7.39 · thesis SEA:WINS
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1135 (adj 0.1001) · $1.31 · thesis SEA:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 63c · p 0.7877 (adj 0.6819) · $7.59 · thesis LAK:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 70c · p 0.7911 (adj 0.743) · $7.77 · thesis LAK:WINS
- Artemi Panarin: 1+ assists NO @ 49c · p 0.6072 (adj 0.5278) · $4.51 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 147/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 30.05, exp saves 26.01 (sd 6.97), pull risk 0.061
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.03, exp saves 24.15 (sd 6.66), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Stolarz: 25+ saves | 0.590 | 0.440 | 52/64 | +0.053 |  |
| Gavin McKenna: 1+ assists | 0.176 | 0.325 | 34/69 | +0.119 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.292 | 0.420 | 43/59 | +0.101 | STANDARD |
| Kirill Marchenko: 1+ points | 0.487 | 0.605 | 62/41 | +0.086 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.490 | 0.375 | 39/64 | +0.083 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.359 | 0.255 | 27/76 | +0.076 | STANDARD |

**CAR @ MTL** · priced 148/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.78, exp saves 26.7 (sd 7.14), pull risk 0.057
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.05, exp saves 19.89 (sd 5.8), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.143 | 0.305 | 32/71 | +0.133 | STANDARD |
| Sebastian Aho: 1+ assists | 0.305 | 0.435 | 45/58 | +0.098 | STANDARD |
| Sebastian Aho: 1+ points | 0.480 | 0.600 | 62/42 | +0.083 | STANDARD |
| Chris Kreider: 1+ points | 0.339 | 0.455 | 46/55 | +0.093 | STANDARD |
| Sebastian Aho: 2+ points | 0.143 | 0.230 | 25/79 | +0.055 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.305 | 0.385 | 40/63 | +0.048 | STANDARD |

**OTT @ DET** · priced 141/149 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 27.75, exp saves 24.07 (sd 6.56), pull risk 0.052
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.38, exp saves 22.78 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.154 | 0.335 | 34/67 | +0.161 | STANDARD |
| William Eklund: 1+ points | 0.320 | 0.500 | 51/51 | +0.152 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.259 | 0.430 | 44/58 | +0.144 | PRIOR_HEAVY |
| Carter Yakemchuk: 1+ assists | 0.208 | 0.345 | 36/67 | +0.107 | PRIOR_HEAVY |
| Andrew Copp: 1+ points | 0.580 | 0.445 | 45/56 | +0.112 | STANDARD |
| Andrew Copp: 1+ assists | 0.447 | 0.330 | 34/68 | +0.091 | STANDARD |

**UTA @ NJD** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 26.63, exp saves 23.0 (sd 6.36), pull risk 0.061
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.76, exp saves 24.99 (sd 6.71), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.164 | 0.335 | 34/67 | +0.150 | STANDARD |
| Luke Evangelista: 1+ assists | 0.200 | 0.365 | 38/65 | +0.134 | STANDARD |
| Luke Evangelista: 1+ points | 0.345 | 0.495 | 51/52 | +0.117 | STANDARD |
| Vincent Trocheck: 1+ points | 0.327 | 0.455 | 46/55 | +0.105 | STANDARD |
| Jack Hughes: 1+ assists | 0.396 | 0.515 | 53/50 | +0.087 | STANDARD |
| Jack Hughes: 2+ points | 0.228 | 0.335 | 35/68 | +0.077 | STANDARD |

**MIN @ BUF** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.64), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.86, exp saves 25.82 (sd 6.99), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ assists | 0.349 | 0.195 | 21/82 | +0.128 | STANDARD |
| Ryan Hartman: 1+ points | 0.514 | 0.375 | 38/63 | +0.118 | STANDARD |
| Jesper Wallstedt: 25+ saves | 0.578 | 0.445 | 51/62 | +0.051 |  |
| Tage Thompson: 1+ assists | 0.336 | 0.455 | 47/56 | +0.087 | STANDARD |
| Tage Thompson: 2+ points | 0.199 | 0.300 | 32/72 | +0.067 | STANDARD |
| Tage Thompson: 1+ points | 0.555 | 0.655 | 66/35 | +0.079 | STANDARD |

**NYI @ NYR** · priced 156/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.05, exp saves 24.53 (sd 6.51), pull risk 0.044
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 25.47, exp saves 21.85 (sd 6.27), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Palmieri: 1+ assists | 0.174 | 0.285 | 30/73 | +0.082 | STANDARD |
| Semyon Varlamov: 24+ saves | 0.387 | 0.475 | 53/58 | +0.016 |  |
| Vladislav Gavrikov: 1+ assists | 0.342 | 0.255 | 27/76 | +0.058 | STANDARD |
| Kyle Palmieri: 1+ points | 0.353 | 0.440 | 46/58 | +0.050 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.393 | 0.310 | 32/70 | +0.057 | STANDARD |
| Gabe Perreault: 1+ assists | 0.319 | 0.240 | 26/78 | +0.045 | STANDARD |

**STL @ CHI** · priced 139/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.19, exp saves 23.28 (sd 6.45), pull risk 0.068
- STL net: Joel Hofer (PROJECTED) exp shots 25.55, exp saves 22.35 (sd 6.13), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.266 | 0.415 | 42/59 | +0.127 | STANDARD |
| Mason McTavish: 1+ assists | 0.201 | 0.320 | 34/70 | +0.084 | STANDARD |
| Mason McTavish: 1+ points | 0.380 | 0.490 | 50/52 | +0.082 | STANDARD |
| Patrick Kane: 1+ points | 0.453 | 0.560 | 57/45 | +0.079 | STANDARD |
| Patrick Kane: 2+ points | 0.123 | 0.205 | 22/81 | +0.056 | STANDARD |
| Ryan Greene: 1+ goals | 0.181 | 0.105 | 11/90 | +0.064 | STANDARD |

**VGK @ SEA** · priced 146/146 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 28.49, exp saves 24.53 (sd 6.67), pull risk 0.061
- VGK net: Carter Hart (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.22), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.205 | 0.355 | 37/66 | +0.119 | STANDARD |
| Jack Eichel: 1+ assists | 0.405 | 0.535 | 54/47 | +0.108 | STANDARD |
| Jack Eichel: 1+ points | 0.565 | 0.685 | 70/33 | +0.090 | STANDARD |
| Mitch Marner: 1+ assists | 0.393 | 0.505 | 52/51 | +0.080 | STANDARD |
| Mark Stone: 1+ assists | 0.367 | 0.465 | 48/55 | +0.066 | STANDARD |
| Mitch Marner: 1+ points | 0.537 | 0.635 | 64/37 | +0.077 | STANDARD |

**FLA @ LAK** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.39, exp saves 23.13 (sd 6.23), pull risk 0.044
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.81, exp saves 23.66 (sd 6.48), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.212 | 0.375 | 38/63 | +0.141 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.375 | 39/64 | +0.112 | STANDARD |
| Brady Tkachuk: 1+ points | 0.420 | 0.560 | 58/46 | +0.102 | STANDARD |
| Sam Reinhart: 1+ points | 0.468 | 0.600 | 62/42 | +0.095 | STANDARD |
| Artemi Panarin: 1+ assists | 0.393 | 0.515 | 52/49 | +0.100 | STANDARD |
| Mats Zuccarello: 1+ points | 0.380 | 0.500 | 51/51 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
