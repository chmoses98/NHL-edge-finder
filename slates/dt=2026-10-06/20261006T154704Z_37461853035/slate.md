# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T15:47:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 3713 · contracts joined: 1830 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 1605, 'OK': 134, 'NO_EDGE': 91}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'player_assists': 223, 'game_early_goal': 9, 'first_goal': 316, 'game_winner': 18, 'player_goals': 554, 'game_overtime': 9, 'player_points': 278, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-6h | 0.450 | 0.550 | 0.170 | 6.39 | 3.04 | 3.35 | 198 (25/173) | PROJECTED/PROJECTED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-6h | 0.498 | 0.502 | 0.175 | 6.10 | 3.04 | 3.06 | 208 (25/183) | PROJECTED/PROJECTED |
| OTT @ DET | 2026-10-06T23:00:00Z | T-6h | 0.577 | 0.423 | 0.177 | 6.12 | 3.31 | 2.81 | 200 (25/175) | PROBABLE/PROJECTED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-6h | 0.499 | 0.501 | 0.182 | 6.05 | 3.02 | 3.03 | 209 (25/184) | PROJECTED/PROJECTED |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-6h | 0.525 | 0.475 | 0.174 | 6.46 | 3.32 | 3.14 | 205 (25/180) | PROBABLE/PROJECTED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-6h | 0.616 | 0.384 | 0.170 | 6.06 | 3.40 | 2.66 | 206 (25/181) | PROJECTED/PROBABLE |
| STL @ CHI | 2026-10-07T00:00:00Z | T-6h | 0.432 | 0.568 | 0.177 | 5.85 | 2.72 | 3.13 | 198 (25/173) | PROJECTED/PROJECTED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-6h | 0.482 | 0.518 | 0.178 | 6.24 | 3.07 | 3.17 | 197 (25/172) | PROJECTED/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-6h | 0.561 | 0.439 | 0.176 | 6.16 | 3.26 | 2.90 | 209 (25/184) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.550 | 0.405 | 0.433 | 41 | 60 | yes | +0.123 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.450 | 0.585 | 0.558 | 59 | 42 | no | +0.113 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.333 | 0.215 | 0.236 | 22 | 79 | yes | +0.101 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.247 | 0.365 | 0.339 | 37 | 64 | no | +0.097 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.653 | 0.540 | 0.563 | 55 | 47 | yes | +0.086 | OK |
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.482 | 0.375 | 0.396 | 38 | 63 | yes | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.441 | 0.325 | 0.347 | 34 | 69 | yes | +0.085 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.145 | 0.245 | 0.222 | 25 | 76 | no | +0.082 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.518 | 0.615 | 0.596 | 62 | 39 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.252 | 0.155 | 0.172 | 17 | 86 | yes | +0.072 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.182 | 0.265 | 0.247 | 27 | 74 | no | +0.065 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.561 | 0.475 | 0.492 | 48 | 53 | yes | +0.064 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.439 | 0.525 | 0.508 | 53 | 48 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.300 | 0.385 | 0.367 | 39 | 62 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.207 | 0.135 | 0.147 | 14 | 87 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.845 | 0.765 | 0.783 | 78 | 25 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.120 | 0.185 | 0.170 | 19 | 82 | no | +0.050 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.423 | 0.495 | 0.480 | 50 | 51 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.596 | 0.525 | 0.539 | 53 | 48 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.270 | 0.205 | 0.217 | 21 | 80 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.237 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.122 | 0.060 | 0.069 | 7 | 95 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.219 | 0.285 | 0.271 | 29 | 72 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.382 | 0.310 | 0.324 | 32 | 70 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.644 | 0.575 | 0.589 | 58 | 43 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.422 | 0.355 | 0.368 | 36 | 65 | yes | +0.046 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.137 | 0.195 | 0.182 | 20 | 81 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR4 | team_total | 0.371 | 0.435 | 0.422 | 44 | 57 | no | +0.042 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.577 | 0.515 | 0.528 | 52 | 49 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR3 | team_total | 0.585 | 0.650 | 0.637 | 66 | 36 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.352 | 0.295 | 0.306 | 30 | 71 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT3 | team_total | 0.536 | 0.600 | 0.587 | 61 | 41 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.203 | 0.150 | 0.160 | 16 | 86 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.286 | 0.235 | 0.245 | 24 | 77 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.766 | 0.815 | 0.806 | 82 | 19 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.622 | 0.675 | 0.665 | 68 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.322 | 0.385 | 0.372 | 40 | 63 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.231 | 0.180 | 0.190 | 19 | 83 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.758 | 0.805 | 0.796 | 81 | 20 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR5 | team_total | 0.197 | 0.245 | 0.235 | 25 | 76 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.553 | 0.610 | 0.599 | 62 | 40 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.220 | 0.175 | 0.183 | 18 | 83 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.241 | 0.195 | 0.204 | 20 | 81 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.219 | 0.265 | 0.255 | 27 | 74 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ3 | team_total | 0.587 | 0.640 | 0.630 | 65 | 37 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT06UTANJ-6 | game_total | 0.536 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.206 | 0.165 | 0.173 | 17 | 84 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYR2 | game_spread | 0.392 | 0.345 | 0.354 | 35 | 66 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ5 | team_total | 0.193 | 0.235 | 0.226 | 24 | 77 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.155 | 0.195 | 0.186 | 20 | 81 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.204 | 0.165 | 0.172 | 17 | 84 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ2 | team_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06UTANJ-4 | game_total | 0.839 | 0.875 | 0.868 | 88 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.108 | 0.070 | 0.076 | 8 | 94 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA2 | team_total | 0.777 | 0.820 | 0.812 | 83 | 19 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.649 | 0.600 | 0.610 | 61 | 41 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.160 | 0.125 | 0.131 | 13 | 88 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.819 | 0.865 | 0.857 | 88 | 15 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.343 | 0.395 | 0.384 | 41 | 62 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT5 | team_total | 0.159 | 0.200 | 0.191 | 21 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ4 | team_total | 0.373 | 0.425 | 0.414 | 44 | 59 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF4 | team_total | 0.437 | 0.395 | 0.403 | 40 | 61 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR2 | team_total | 0.800 | 0.845 | 0.837 | 86 | 17 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.403 | 0.445 | 0.437 | 45 | 56 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN2 | game_spread | 0.266 | 0.305 | 0.297 | 31 | 70 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.830 | 0.790 | 0.799 | 80 | 22 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI3 | game_spread | 0.103 | 0.135 | 0.128 | 14 | 87 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.801 | 0.755 | 0.765 | 77 | 26 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.476 | 0.435 | 0.443 | 44 | 57 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT06UTANJ-5 | game_total | 0.750 | 0.790 | 0.782 | 80 | 22 | no | +0.018 | OK |
| KXNHLGAME-26OCT06MINBUF-BUF | game_winner | 0.525 | 0.485 | 0.493 | 49 | 52 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR2 | team_total | 0.803 | 0.840 | 0.833 | 85 | 17 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.171 | 0.205 | 0.198 | 21 | 80 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF3 | team_total | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR4 | team_total | 0.454 | 0.415 | 0.423 | 42 | 59 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06NYINYR-NYR5 | team_total | 0.258 | 0.225 | 0.231 | 23 | 78 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.090 | 0.060 | 0.065 | 7 | 95 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT06NYINYR-NYI2 | game_spread | 0.193 | 0.225 | 0.218 | 23 | 78 | no | +0.015 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.450 | 0.509 | 0.170 | 0.222 | 6.39 | 6.24 | 0.978/0.994 | KXNHLSPREAD-26OCT06NSHTOR-NSH2 -0.060 |
| CAR @ MTL | 0.498 | 0.520 | 0.175 | 0.218 | 6.10 | 6.24 | 0.952/0.997 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL4 +0.035 |
| OTT @ DET | 0.577 | 0.519 | 0.177 | 0.224 | 6.12 | 6.05 | 0.998/1.040 | KXNHLSPREAD-26OCT06OTTDET-DET2 -0.061 |
| UTA @ NJD | 0.499 | 0.482 | 0.182 | 0.220 | 6.05 | 6.10 | 0.987/0.992 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA4 +0.022 |
| MIN @ BUF | 0.525 | 0.514 | 0.174 | 0.212 | 6.46 | 6.43 | 0.999/1.003 | KXNHLSPREAD-26OCT06MINBUF-MIN3 +0.017 |
| NYI @ NYR | 0.616 | 0.571 | 0.170 | 0.216 | 6.06 | 5.98 | 0.957/0.973 | KXNHLSPREAD-26OCT06NYINYR-NYR2 -0.055 |
| STL @ CHI | 0.432 | 0.439 | 0.177 | 0.217 | 5.85 | 6.19 | 1.003/0.993 | KXNHLTOTAL-26OCT06STLCHI-7 +0.063 |
| VGK @ SEA | 0.482 | 0.482 | 0.178 | 0.222 | 6.24 | 6.10 | 1.005/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.030 |
| FLA @ LAK | 0.561 | 0.582 | 0.176 | 0.222 | 6.16 | 5.94 | 0.992/1.007 | KXNHLTOTAL-26OCT06FLALA-6 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 32 recommended · full analysis in card.md / packet.json `thesis_card`

- Gavin McKenna: 1+ goals NO @ 78c · p 0.845 (adj 0.8275) · $7.41 · thesis TOR:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2192 (adj 0.2056) · $2.93 · thesis NSH:OFFENSE_4PLUS
- Auston Matthews: 1+ goals NO @ 61c · p 0.6597 (adj 0.646) · $4.58 · thesis TOR:SUPPRESSED
- Alexander Kerfoot: 1+ goals YES @ 13c · p 0.1606 (adj 0.1517) · $1.51 · thesis NSH:OFFENSE_4PLUS
- Alexandre Texier: 1+ goals YES @ 11c · p 0.151 (adj 0.1382) · $2.3 · thesis MTL:OFFENSE_4PLUS
- Jake Evans: 1+ goals YES @ 12c · p 0.1583 (adj 0.1425) · $1.6 · thesis MTL:WINS_BY_2PLUS
- Chris Kreider: 1+ assists NO @ 73c · p 0.8525 (adj 0.7631) · $7.99 · thesis MTL:SUPPRESSED
- Nikolaj Ehlers: 1+ goals NO @ 74c · p 0.7817 (adj 0.7688) · $6.39 · thesis CAR:SUPPRESSED
- Carter Yakemchuk: 1+ goals NO @ 86c · p 0.931 (adj 0.912) · $6.0 · thesis OTT:SUPPRESSED
- William Eklund: 1+ assists NO @ 67c · p 0.8443 (adj 0.7278) · $6.0 · thesis OTT:SUPPRESSED
- Viktor Arvidsson: 1+ assists NO @ 67c · p 0.7948 (adj 0.7072) · $6.34 · thesis DET:SUPPRESSED
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8311 (adj 0.7231) · $7.99 · thesis UTA:SUPPRESSED
- Luke Evangelista: 1+ assists NO @ 65c · p 0.8021 (adj 0.6902) · $7.99 · thesis NJD:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2097 (adj 0.1973) · $2.01 · thesis UTA:OFFENSE_4PLUS
- Ryan Hartman: 1+ assists YES @ 20c · p 0.3529 (adj 0.247) · $3.11 · thesis MIN:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1452 (adj 0.1314) · $2.22 · thesis MIN:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 11c · p 0.1499 (adj 0.1387) · $2.2 · thesis BUF:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 15c · p 0.1866 (adj 0.1762) · $1.85 · thesis BUF:OFFENSE_4PLUS
- Oliver Bjorkstrand: 1+ goals NO @ 83c · p 0.8641 (adj 0.8543) · $7.99 · thesis NYR:SUPPRESSED
- Bo Horvat: 1+ goals NO @ 69c · p 0.7349 (adj 0.7212) · $5.65 · thesis NYI:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 27c · p 0.3424 (adj 0.2987) · $2.04 · thesis NYR:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1774 (adj 0.1593) · $4.31 · thesis CHI:OFFENSE_4PLUS
- Patrick Kane: 1+ assists NO @ 59c · p 0.7323 (adj 0.6366) · $7.99 · thesis CHI:SUPPRESSED
- Philip Broberg: 1+ goals YES @ 7c · p 0.099 (adj 0.0905) · $1.6 · thesis STL:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 15c · p 0.177 (adj 0.169) · $1.18 · thesis STL:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 10c · p 0.144 (adj 0.1317) · $2.47 · thesis SEA:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 67c · p 0.7257 (adj 0.7105) · $7.06 · thesis VGK:SUPPRESSED
- Vegas wins by over 2.5 goals NO @ 74c · p 0.8177 (adj 0.7763) · $7.32 · thesis SEA:WINS
- Freddy Gaudreau: 1+ goals YES @ 8c · p 0.1135 (adj 0.1001) · $1.3 · thesis SEA:OFFENSE_4PLUS
- Mats Zuccarello: 1+ assists NO @ 63c · p 0.7877 (adj 0.6819) · $7.52 · thesis LAK:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 70c · p 0.7911 (adj 0.743) · $7.7 · thesis LAK:WINS
- Artemi Panarin: 1+ assists NO @ 49c · p 0.6072 (adj 0.5278) · $4.47 · thesis LAK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 145/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.05, exp saves 25.95 (sd 6.94), pull risk 0.061
- NSH net: Justus Annunen (PROJECTED) exp shots 28.03, exp saves 24.17 (sd 6.67), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ assists | 0.176 | 0.325 | 34/69 | +0.119 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.287 | 0.420 | 43/59 | +0.106 | STANDARD |
| Kirill Marchenko: 1+ points | 0.484 | 0.605 | 62/41 | +0.089 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.494 | 0.375 | 39/64 | +0.087 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.368 | 0.255 | 27/76 | +0.084 | STANDARD |
| Darren Raddysh: 1+ assists | 0.314 | 0.425 | 44/59 | +0.079 | STANDARD |

**CAR @ MTL** · priced 148/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 30.78, exp saves 26.69 (sd 7.18), pull risk 0.059
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.05, exp saves 19.88 (sd 5.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.147 | 0.285 | 30/73 | +0.109 | STANDARD |
| Sebastian Aho: 1+ assists | 0.304 | 0.430 | 44/58 | +0.099 | STANDARD |
| Sebastian Aho: 1+ points | 0.483 | 0.600 | 62/42 | +0.080 | STANDARD |
| Chris Kreider: 1+ points | 0.335 | 0.440 | 45/57 | +0.077 | STANDARD |
| Sebastian Aho: 2+ points | 0.141 | 0.230 | 25/79 | +0.057 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.303 | 0.385 | 40/63 | +0.050 | STANDARD |

**OTT @ DET** · priced 146/149 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 27.75, exp saves 24.07 (sd 6.57), pull risk 0.052
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.38, exp saves 22.78 (sd 6.33), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ points | 0.321 | 0.505 | 52/51 | +0.152 | STANDARD |
| William Eklund: 1+ assists | 0.156 | 0.335 | 34/67 | +0.159 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.257 | 0.425 | 44/59 | +0.136 | PRIOR_HEAVY |
| Carter Yakemchuk: 1+ assists | 0.203 | 0.340 | 36/68 | +0.101 | PRIOR_HEAVY |
| Viktor Arvidsson: 1+ assists | 0.205 | 0.340 | 35/67 | +0.109 | STANDARD |
| Tim Stutzle: 1+ assists | 0.373 | 0.485 | 50/53 | +0.079 | STANDARD |

**UTA @ NJD** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.63, exp saves 23.01 (sd 6.39), pull risk 0.062
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.76, exp saves 24.94 (sd 6.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.198 | 0.370 | 39/65 | +0.136 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.169 | 0.335 | 34/67 | +0.146 | STANDARD |
| Luke Evangelista: 1+ points | 0.345 | 0.500 | 51/51 | +0.127 | STANDARD |
| Vincent Trocheck: 1+ points | 0.334 | 0.455 | 46/55 | +0.099 | STANDARD |
| Jack Hughes: 1+ assists | 0.399 | 0.505 | 52/51 | +0.074 | STANDARD |
| Jack Hughes: 2+ points | 0.232 | 0.335 | 35/68 | +0.073 | STANDARD |

**MIN @ BUF** · priced 149/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.96 (sd 6.57), pull risk 0.063
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.86, exp saves 25.79 (sd 6.97), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ assists | 0.353 | 0.190 | 20/82 | +0.142 | STANDARD |
| Ryan Hartman: 1+ points | 0.515 | 0.375 | 38/63 | +0.119 | STANDARD |
| Tage Thompson: 1+ assists | 0.344 | 0.460 | 48/56 | +0.079 | STANDARD |
| Tage Thompson: 2+ points | 0.196 | 0.305 | 32/71 | +0.079 | STANDARD |
| Tage Thompson: 1+ points | 0.561 | 0.660 | 67/35 | +0.073 | STANDARD |
| Max Shabanov: 1+ assists | 0.209 | 0.300 | 32/72 | +0.056 | STANDARD |

**NYI @ NYR** · priced 155/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.05, exp saves 24.52 (sd 6.61), pull risk 0.045
- NYI net: Semyon Varlamov (PROBABLE) exp shots 25.47, exp saves 21.89 (sd 6.23), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kyle Palmieri: 1+ assists | 0.175 | 0.285 | 30/73 | +0.081 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.342 | 0.255 | 27/76 | +0.059 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.395 | 0.310 | 32/70 | +0.059 | STANDARD |
| Matias Maccelli: 1+ assists | 0.186 | 0.270 | 29/75 | +0.050 | STANDARD |
| Kyle Palmieri: 1+ points | 0.362 | 0.440 | 46/58 | +0.041 | STANDARD |
| Gabe Perreault: 1+ assists | 0.318 | 0.245 | 27/78 | +0.035 | STANDARD |

**STL @ CHI** · priced 138/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.19, exp saves 23.26 (sd 6.51), pull risk 0.068
- STL net: Joel Hofer (PROJECTED) exp shots 25.55, exp saves 22.32 (sd 6.19), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.268 | 0.415 | 42/59 | +0.125 | STANDARD |
| Mason McTavish: 1+ assists | 0.210 | 0.320 | 34/70 | +0.075 | STANDARD |
| Patrick Kane: 1+ points | 0.459 | 0.565 | 58/45 | +0.074 | STANDARD |
| Mason McTavish: 1+ points | 0.389 | 0.490 | 50/52 | +0.073 | STANDARD |
| Ryan Greene: 1+ goals | 0.177 | 0.105 | 11/90 | +0.061 | STANDARD |
| Patrick Kane: 2+ points | 0.125 | 0.195 | 22/83 | +0.035 | STANDARD |

**VGK @ SEA** · priced 146/146 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 28.49, exp saves 24.53 (sd 6.67), pull risk 0.061
- VGK net: Carter Hart (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.22), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 2+ points | 0.205 | 0.350 | 36/66 | +0.119 | STANDARD |
| Jack Eichel: 1+ assists | 0.405 | 0.545 | 56/47 | +0.108 | STANDARD |
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
| Brady Tkachuk: 1+ points | 0.420 | 0.565 | 59/46 | +0.102 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.232 | 0.375 | 39/64 | +0.112 | STANDARD |
| Sam Reinhart: 1+ points | 0.468 | 0.600 | 62/42 | +0.095 | STANDARD |
| Artemi Panarin: 1+ assists | 0.393 | 0.515 | 52/49 | +0.100 | STANDARD |
| Mats Zuccarello: 1+ points | 0.380 | 0.500 | 51/51 | +0.092 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
