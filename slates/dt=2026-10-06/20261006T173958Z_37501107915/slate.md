# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T17:39:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 3721 · contracts joined: 1838 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 1613, 'OK': 130, 'NO_EDGE': 95}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'player_assists': 223, 'game_early_goal': 9, 'first_goal': 316, 'game_winner': 18, 'player_goals': 554, 'game_overtime': 9, 'player_points': 278, 'goalie_saves': 8, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-3h | 0.489 | 0.511 | 0.172 | 6.65 | 3.29 | 3.36 | 200 (25/175) | CONFIRMED/CONFIRMED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-3h | 0.508 | 0.492 | 0.179 | 6.05 | 3.05 | 3.01 | 209 (25/184) | CONFIRMED/PROBABLE |
| OTT @ DET | 2026-10-06T23:00:00Z | T-3h | 0.577 | 0.423 | 0.177 | 6.12 | 3.31 | 2.81 | 200 (25/175) | PROBABLE/PROJECTED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-3h | 0.500 | 0.500 | 0.176 | 6.00 | 3.01 | 3.00 | 210 (25/185) | CONFIRMED/PROBABLE |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-3h | 0.522 | 0.478 | 0.175 | 6.42 | 3.28 | 3.14 | 207 (25/182) | PROBABLE/CONFIRMED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-3h | 0.629 | 0.371 | 0.175 | 5.97 | 3.40 | 2.58 | 207 (25/182) | CONFIRMED/CONFIRMED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-6h | 0.426 | 0.574 | 0.182 | 5.78 | 2.67 | 3.12 | 199 (25/174) | PROBABLE/CONFIRMED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-6h | 0.479 | 0.521 | 0.175 | 6.25 | 3.07 | 3.18 | 197 (25/172) | PROBABLE/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-6h | 0.561 | 0.439 | 0.176 | 6.16 | 3.26 | 2.90 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.443 | 0.320 | 0.343 | 33 | 69 | yes | +0.097 | OK |
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.511 | 0.405 | 0.426 | 41 | 60 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.651 | 0.540 | 0.563 | 55 | 47 | yes | +0.084 | OK |
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.479 | 0.375 | 0.395 | 38 | 63 | yes | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.256 | 0.160 | 0.177 | 17 | 85 | yes | +0.076 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.489 | 0.585 | 0.566 | 59 | 42 | no | +0.074 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.521 | 0.615 | 0.597 | 62 | 39 | no | +0.073 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.322 | 0.235 | 0.251 | 24 | 77 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.300 | 0.215 | 0.231 | 22 | 79 | yes | +0.068 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.523 | 0.435 | 0.452 | 44 | 57 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.182 | 0.265 | 0.247 | 27 | 74 | no | +0.064 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.561 | 0.475 | 0.492 | 48 | 53 | yes | +0.064 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.439 | 0.525 | 0.508 | 53 | 48 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.300 | 0.385 | 0.367 | 39 | 62 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.255 | 0.270 | 26 | 75 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.283 | 0.365 | 0.348 | 37 | 64 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.596 | 0.515 | 0.531 | 52 | 49 | yes | +0.058 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.236 | 0.165 | 0.178 | 17 | 84 | yes | +0.056 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-6 | game_total | 0.631 | 0.555 | 0.570 | 56 | 45 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.175 | 0.245 | 0.230 | 25 | 76 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.126 | 0.060 | 0.070 | 7 | 95 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.842 | 0.765 | 0.782 | 78 | 25 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.120 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.237 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.644 | 0.575 | 0.589 | 58 | 43 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.268 | 0.200 | 0.212 | 21 | 81 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.422 | 0.355 | 0.368 | 36 | 65 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.137 | 0.195 | 0.182 | 20 | 81 | no | +0.042 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.423 | 0.485 | 0.472 | 49 | 52 | no | +0.040 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.577 | 0.515 | 0.528 | 52 | 49 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.187 | 0.135 | 0.144 | 14 | 87 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.352 | 0.295 | 0.306 | 30 | 71 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.219 | 0.275 | 0.263 | 28 | 73 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT3 | team_total | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ4 | team_total | 0.367 | 0.430 | 0.417 | 44 | 58 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR2 | game_spread | 0.402 | 0.345 | 0.356 | 35 | 66 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-10 | game_total | 0.120 | 0.075 | 0.083 | 8 | 93 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.380 | 0.315 | 0.328 | 33 | 70 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.204 | 0.150 | 0.160 | 16 | 86 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT06UTANJ-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.766 | 0.815 | 0.806 | 82 | 19 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.622 | 0.675 | 0.665 | 68 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.322 | 0.380 | 0.368 | 39 | 63 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI2 | game_spread | 0.177 | 0.225 | 0.215 | 23 | 78 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.343 | 0.400 | 0.388 | 41 | 61 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT06UTANJ-5 | game_total | 0.748 | 0.800 | 0.790 | 81 | 21 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.231 | 0.180 | 0.190 | 19 | 83 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ3 | team_total | 0.583 | 0.635 | 0.625 | 64 | 37 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.553 | 0.605 | 0.595 | 61 | 40 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.220 | 0.175 | 0.183 | 18 | 83 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.170 | 0.215 | 0.205 | 22 | 79 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI3 | game_spread | 0.095 | 0.135 | 0.126 | 14 | 87 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-5 | game_total | 0.819 | 0.775 | 0.784 | 78 | 23 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.206 | 0.165 | 0.173 | 17 | 84 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.221 | 0.265 | 0.256 | 27 | 74 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ2 | team_total | 0.796 | 0.840 | 0.832 | 85 | 17 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06UTANJ-4 | game_total | 0.838 | 0.875 | 0.868 | 88 | 13 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.165 | 0.205 | 0.197 | 21 | 80 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.755 | 0.795 | 0.787 | 80 | 21 | no | +0.023 | OK |
| KXNHLGAME-26OCT06NYINYR-NYI | game_winner | 0.371 | 0.415 | 0.406 | 42 | 59 | no | +0.022 | OK |
| KXNHLGAME-26OCT06NYINYR-NYR | game_winner | 0.629 | 0.585 | 0.594 | 59 | 42 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.649 | 0.605 | 0.614 | 61 | 40 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF4 | team_total | 0.428 | 0.385 | 0.393 | 39 | 62 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT5 | team_total | 0.159 | 0.200 | 0.191 | 21 | 81 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-4 | game_total | 0.889 | 0.855 | 0.862 | 86 | 15 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.158 | 0.125 | 0.131 | 13 | 88 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT06STLCHI-5 | game_total | 0.717 | 0.755 | 0.748 | 76 | 25 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.241 | 0.205 | 0.212 | 21 | 80 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ5 | team_total | 0.189 | 0.235 | 0.225 | 25 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.830 | 0.790 | 0.799 | 80 | 22 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.801 | 0.760 | 0.769 | 77 | 25 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN2 | game_spread | 0.267 | 0.305 | 0.297 | 31 | 70 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.823 | 0.865 | 0.857 | 88 | 15 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR3 | team_total | 0.585 | 0.630 | 0.621 | 64 | 38 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.404 | 0.445 | 0.437 | 45 | 56 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR4 | team_total | 0.365 | 0.405 | 0.397 | 41 | 60 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT06UTANJ-7 | game_total | 0.416 | 0.455 | 0.447 | 46 | 55 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR2 | game_spread | 0.278 | 0.315 | 0.307 | 32 | 69 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR3 | game_spread | 0.259 | 0.225 | 0.232 | 23 | 78 | yes | +0.017 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.489 | 0.522 | 0.172 | 0.219 | 6.65 | 6.20 | 0.955/1.004 | KXNHLTOTAL-26OCT06NSHTOR-6 -0.078 |
| CAR @ MTL | 0.508 | 0.519 | 0.179 | 0.221 | 6.05 | 6.19 | 0.942/0.986 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL3 +0.031 |
| OTT @ DET | 0.577 | 0.519 | 0.177 | 0.224 | 6.12 | 6.05 | 0.998/1.040 | KXNHLSPREAD-26OCT06OTTDET-DET2 -0.061 |
| UTA @ NJD | 0.500 | 0.488 | 0.176 | 0.221 | 6.00 | 6.10 | 0.983/0.990 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA4 +0.025 |
| MIN @ BUF | 0.522 | 0.506 | 0.175 | 0.215 | 6.42 | 6.40 | 0.999/0.991 | KXNHLSPREAD-26OCT06MINBUF-MIN3 +0.018 |
| NYI @ NYR | 0.629 | 0.588 | 0.175 | 0.220 | 5.97 | 5.93 | 0.934/0.977 | KXNHLSPREAD-26OCT06NYINYR-NYR2 -0.052 |
| STL @ CHI | 0.426 | 0.434 | 0.182 | 0.217 | 5.78 | 6.13 | 0.995/0.976 | KXNHLTOTAL-26OCT06STLCHI-7 +0.061 |
| VGK @ SEA | 0.479 | 0.482 | 0.175 | 0.224 | 6.25 | 6.10 | 1.001/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.030 |
| FLA @ LAK | 0.561 | 0.582 | 0.176 | 0.222 | 6.16 | 5.94 | 0.992/1.007 | KXNHLTOTAL-26OCT06FLALA-6 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 33 recommended · full analysis in card.md / packet.json `thesis_card`

- Gavin McKenna: 1+ goals NO @ 79c · p 0.8457 (adj 0.8305) · $5.98 · thesis TOR:SUPPRESSED
- Gavin McKenna: 1+ assists NO @ 69c · p 0.8239 (adj 0.7271) · $5.98 · thesis TOR:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2056 (adj 0.1942) · $1.69 · thesis NSH:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1364 (adj 0.1285) · $1.29 · thesis TOR:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 71c · p 0.8549 (adj 0.751) · $7.83 · thesis MTL:SUPPRESSED
- Alexandre Texier: 1+ goals YES @ 12c · p 0.1499 (adj 0.1412) · $1.53 · thesis MTL:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 70c · p 0.7428 (adj 0.7308) · $5.56 · thesis CAR:SUPPRESSED
- Nikolaj Ehlers: 1+ goals NO @ 75c · p 0.7865 (adj 0.7749) · $5.01 · thesis CAR:SUPPRESSED
- Carter Yakemchuk: 1+ goals NO @ 86c · p 0.9322 (adj 0.9129) · $7.97 · thesis OTT:SUPPRESSED
- Andrew Copp: 1+ goals YES @ 18c · p 0.2424 (adj 0.2256) · $4.13 · thesis DET:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 10c · p 0.1359 (adj 0.1244) · $1.88 · thesis DET:OFFENSE_4PLUS
- Alex DeBrincat: 1+ goals YES @ 40c · p 0.4441 (adj 0.4318) · $2.78 · thesis DET:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8417 (adj 0.7268) · $7.97 · thesis UTA:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 64c · p 0.8084 (adj 0.6924) · $7.97 · thesis NJD:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2129 (adj 0.1997) · $2.32 · thesis UTA:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1473 (adj 0.1317) · $3.22 · thesis MIN:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 13c · p 0.1878 (adj 0.1721) · $3.61 · thesis BUF:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 20c · p 0.3495 (adj 0.2458) · $2.76 · thesis MIN:OFFENSE_4PLUS
- Marcus Foligno: 1+ goals YES @ 10c · p 0.1346 (adj 0.1247) · $1.81 · thesis MIN:OFFENSE_4PLUS
- Matt Rempe: 1+ goals YES @ 7c · p 0.1027 (adj 0.092) · $1.6 · thesis NYR:OFFENSE_4PLUS
- Bo Horvat: 1+ goals NO @ 69c · p 0.7383 (adj 0.725) · $6.88 · thesis NYI:SUPPRESSED
- Pavel Dorofeyev: 1+ goals NO @ 65c · p 0.6961 (adj 0.6833) · $5.61 · thesis NYR:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 27c · p 0.3369 (adj 0.2959) · $1.57 · thesis NYR:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1687 (adj 0.1528) · $3.69 · thesis CHI:OFFENSE_4PLUS
- Adam Jiricek: 1+ goals NO @ 90c · p 0.9417 (adj 0.93) · $7.97 · thesis DIFFUSE
- Patrick Kane: 1+ assists NO @ 59c · p 0.7383 (adj 0.6387) · $7.97 · thesis CHI:SUPPRESSED
- Freddy Gaudreau: 1+ goals YES @ 7c · p 0.1191 (adj 0.1031) · $2.5 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 10c · p 0.1466 (adj 0.1337) · $2.62 · thesis SEA:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 70c · p 0.751 (adj 0.737) · $7.2 · thesis VGK:SUPPRESSED
- Braeden Bowman: 1+ goals YES @ 15c · p 0.1864 (adj 0.1748) · $1.75 · thesis VGK:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 63c · p 0.7877 (adj 0.6819) · $7.97 · thesis LAK:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 69c · p 0.7502 (adj 0.7339) · $7.97 · thesis FLA:SUPPRESSED
- Los Angeles wins by over 1.5 goals YES @ 26c · p 0.3455 (adj 0.3003) · $3.37 · thesis LAK:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 147/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 30.05, exp saves 26.01 (sd 6.97), pull risk 0.061
- NSH net: Juuse Saros (CONFIRMED) exp shots 28.03, exp saves 24.15 (sd 6.66), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Anthony Stolarz: 25+ saves | 0.590 | 0.415 | 51/68 | +0.063 |  |
| Gavin McKenna: 1+ assists | 0.176 | 0.325 | 34/69 | +0.119 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.292 | 0.420 | 43/59 | +0.101 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.490 | 0.380 | 39/63 | +0.083 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.359 | 0.250 | 26/76 | +0.086 | STANDARD |
| Kirill Marchenko: 1+ points | 0.487 | 0.595 | 61/42 | +0.076 | STANDARD |

**CAR @ MTL** · priced 149/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 30.78, exp saves 26.8 (sd 7.13), pull risk 0.053
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.05, exp saves 19.88 (sd 5.78), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.145 | 0.305 | 32/71 | +0.130 | STANDARD |
| Sebastian Aho: 1+ assists | 0.309 | 0.435 | 45/58 | +0.094 | STANDARD |
| Chris Kreider: 1+ points | 0.339 | 0.465 | 48/55 | +0.094 | STANDARD |
| Sebastian Aho: 1+ points | 0.487 | 0.605 | 62/41 | +0.086 | STANDARD |
| Sebastian Aho: 2+ points | 0.146 | 0.240 | 26/78 | +0.062 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.380 | 0.460 | 47/55 | +0.053 | STANDARD |

**OTT @ DET** · priced 141/149 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 27.75, exp saves 24.07 (sd 6.56), pull risk 0.052
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.38, exp saves 22.78 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Yakemchuk: 1+ points | 0.259 | 0.440 | 45/57 | +0.154 | PRIOR_HEAVY |
| William Eklund: 1+ assists | 0.154 | 0.325 | 34/69 | +0.141 | STANDARD |
| William Eklund: 1+ points | 0.320 | 0.490 | 50/52 | +0.142 | STANDARD |
| Andrew Copp: 1+ points | 0.580 | 0.415 | 42/59 | +0.142 | STANDARD |
| Carter Yakemchuk: 1+ assists | 0.208 | 0.345 | 36/67 | +0.107 | PRIOR_HEAVY |
| Andrew Copp: 1+ assists | 0.447 | 0.325 | 33/68 | +0.101 | STANDARD |

**UTA @ NJD** · priced 159/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.37), pull risk 0.063
- UTA net: Karel Vejmelka (PROBABLE) exp shots 28.76, exp saves 24.97 (sd 6.68), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.192 | 0.370 | 38/64 | +0.152 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.158 | 0.335 | 34/67 | +0.156 | STANDARD |
| Luke Evangelista: 1+ points | 0.336 | 0.495 | 50/51 | +0.136 | STANDARD |
| Vincent Trocheck: 1+ points | 0.325 | 0.455 | 46/55 | +0.108 | STANDARD |
| Jack Hughes: 1+ assists | 0.395 | 0.515 | 53/50 | +0.087 | STANDARD |
| Jack Hughes: 2+ points | 0.230 | 0.335 | 35/68 | +0.075 | STANDARD |

**MIN @ BUF** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.9 (sd 6.64), pull risk 0.065
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.86, exp saves 25.82 (sd 6.99), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colten Ellis: 25+ saves | 0.460 | 0.300 | 54/94 | -0.097 |  |
| Ryan Hartman: 1+ assists | 0.349 | 0.190 | 20/82 | +0.138 | STANDARD |
| Jesper Wallstedt: 25+ saves | 0.578 | 0.435 | 51/64 | +0.051 |  |
| Ryan Hartman: 1+ points | 0.514 | 0.375 | 38/63 | +0.118 | STANDARD |
| Tage Thompson: 1+ assists | 0.336 | 0.455 | 47/56 | +0.087 | STANDARD |
| Tage Thompson: 2+ points | 0.199 | 0.300 | 31/71 | +0.077 | STANDARD |

**NYI @ NYR** · priced 156/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (CONFIRMED) exp shots 28.05, exp saves 24.57 (sd 6.5), pull risk 0.044
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 25.47, exp saves 21.89 (sd 6.24), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Palmieri: 1+ assists | 0.171 | 0.285 | 30/73 | +0.085 | STANDARD |
| Kyle Palmieri: 1+ points | 0.350 | 0.445 | 46/57 | +0.063 | STANDARD |
| Semyon Varlamov: 24+ saves | 0.389 | 0.480 | 56/60 | -0.006 |  |
| Matias Maccelli: 1+ assists | 0.183 | 0.270 | 29/75 | +0.054 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.337 | 0.255 | 27/76 | +0.053 | STANDARD |
| Gabe Perreault: 1+ assists | 0.319 | 0.240 | 26/78 | +0.046 | STANDARD |

**STL @ CHI** · priced 146/148 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROBABLE) exp shots 27.19, exp saves 23.24 (sd 6.49), pull risk 0.067
- STL net: Joel Hofer (CONFIRMED) exp shots 25.55, exp saves 22.31 (sd 6.13), pull risk 0.052

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Spencer Knight: 23+ saves | 0.547 | 0.285 | 52/95 | +0.009 |  |
| Patrick Kane: 1+ assists | 0.262 | 0.415 | 42/59 | +0.131 | STANDARD |
| Bowen Byram: 1+ points | 0.316 | 0.445 | 45/56 | +0.107 | STANDARD |
| Mason McTavish: 1+ assists | 0.208 | 0.320 | 33/69 | +0.087 | STANDARD |
| Patrick Kane: 1+ points | 0.444 | 0.555 | 56/45 | +0.089 | STANDARD |
| Mason McTavish: 1+ points | 0.387 | 0.495 | 51/52 | +0.075 | STANDARD |

**VGK @ SEA** · priced 146/146 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROBABLE) exp shots 28.49, exp saves 24.56 (sd 6.77), pull risk 0.061
- VGK net: Carter Hart (PROJECTED) exp shots 25.65, exp saves 22.26 (sd 6.2), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.203 | 0.355 | 37/66 | +0.121 | STANDARD |
| Jack Eichel: 1+ assists | 0.406 | 0.545 | 56/47 | +0.106 | STANDARD |
| Mitch Marner: 1+ assists | 0.389 | 0.510 | 52/50 | +0.093 | STANDARD |
| Jack Eichel: 1+ points | 0.568 | 0.680 | 69/33 | +0.086 | STANDARD |
| Mitch Marner: 2+ points | 0.180 | 0.285 | 30/73 | +0.076 | STANDARD |
| Jack Eichel: 2+ assists | 0.093 | 0.185 | 20/83 | +0.067 | STANDARD |

**FLA @ LAK** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.39, exp saves 23.13 (sd 6.23), pull risk 0.044
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.81, exp saves 23.66 (sd 6.48), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mats Zuccarello: 1+ assists | 0.212 | 0.375 | 38/63 | +0.141 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.380 | 40/64 | +0.112 | STANDARD |
| Brady Tkachuk: 1+ points | 0.420 | 0.565 | 58/45 | +0.112 | STANDARD |
| Sam Reinhart: 1+ points | 0.468 | 0.605 | 62/41 | +0.106 | STANDARD |
| Artemi Panarin: 1+ assists | 0.393 | 0.515 | 52/49 | +0.100 | STANDARD |
| Sam Reinhart: 2+ points | 0.132 | 0.250 | 26/76 | +0.095 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
