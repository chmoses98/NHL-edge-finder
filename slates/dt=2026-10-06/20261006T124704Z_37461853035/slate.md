# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T12:47:04Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 3409 · contracts joined: 1526 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 1301, 'OK': 122, 'NO_EDGE': 103}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'player_assists': 172, 'game_early_goal': 9, 'first_goal': 246, 'game_winner': 18, 'player_goals': 431, 'game_overtime': 9, 'player_points': 218, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-6h | 0.450 | 0.550 | 0.170 | 6.39 | 3.04 | 3.35 | 198 (25/173) | PROJECTED/PROJECTED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-6h | 0.498 | 0.502 | 0.175 | 6.10 | 3.04 | 3.06 | 208 (25/183) | PROJECTED/PROJECTED |
| OTT @ DET | 2026-10-06T23:00:00Z | T-6h | 0.576 | 0.424 | 0.175 | 6.14 | 3.31 | 2.83 | 200 (25/175) | PROJECTED/PROJECTED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-6h | 0.499 | 0.501 | 0.182 | 6.05 | 3.02 | 3.03 | 209 (25/184) | PROJECTED/PROJECTED |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-6h | 0.525 | 0.475 | 0.174 | 6.46 | 3.32 | 3.14 | 205 (25/180) | PROBABLE/PROJECTED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-6h | 0.572 | 0.428 | 0.183 | 5.78 | 3.11 | 2.67 | 206 (25/181) | PROJECTED/PROJECTED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-6h | 0.432 | 0.568 | 0.177 | 5.85 | 2.72 | 3.13 | 198 (25/173) | PROJECTED/PROJECTED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-12h | 0.482 | 0.518 | 0.178 | 6.24 | 3.07 | 3.17 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-12h | 0.561 | 0.439 | 0.176 | 6.16 | 3.26 | 2.90 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.550 | 0.405 | 0.433 | 41 | 60 | yes | +0.123 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.450 | 0.585 | 0.558 | 59 | 42 | no | +0.113 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.653 | 0.530 | 0.555 | 54 | 48 | yes | +0.096 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.441 | 0.320 | 0.343 | 33 | 69 | yes | +0.095 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.333 | 0.220 | 0.240 | 23 | 79 | yes | +0.090 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.247 | 0.355 | 0.332 | 36 | 65 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.145 | 0.245 | 0.222 | 25 | 76 | no | +0.082 | OK |
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.482 | 0.385 | 0.404 | 39 | 62 | yes | +0.076 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.518 | 0.615 | 0.596 | 62 | 39 | no | +0.076 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.561 | 0.465 | 0.484 | 47 | 54 | yes | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.252 | 0.160 | 0.176 | 17 | 85 | yes | +0.072 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.439 | 0.525 | 0.508 | 53 | 48 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.300 | 0.385 | 0.367 | 39 | 62 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.207 | 0.135 | 0.147 | 14 | 87 | yes | +0.058 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.576 | 0.495 | 0.511 | 50 | 51 | yes | +0.058 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.424 | 0.505 | 0.489 | 51 | 50 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.350 | 0.275 | 0.289 | 28 | 73 | yes | +0.056 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.182 | 0.255 | 0.239 | 26 | 75 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.337 | 0.265 | 0.279 | 27 | 74 | yes | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.845 | 0.765 | 0.783 | 78 | 25 | yes | +0.053 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.137 | 0.205 | 0.190 | 21 | 80 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.596 | 0.525 | 0.539 | 53 | 48 | yes | +0.049 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.270 | 0.205 | 0.217 | 21 | 80 | yes | +0.048 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.237 | 0.305 | 0.291 | 31 | 70 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.644 | 0.570 | 0.585 | 58 | 44 | yes | +0.047 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.123 | 0.185 | 0.171 | 19 | 82 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.223 | 0.285 | 0.272 | 29 | 72 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR4 | team_total | 0.371 | 0.440 | 0.426 | 45 | 57 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR3 | team_total | 0.585 | 0.650 | 0.637 | 66 | 36 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.122 | 0.065 | 0.074 | 8 | 95 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.382 | 0.315 | 0.328 | 33 | 70 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.422 | 0.355 | 0.368 | 37 | 66 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.203 | 0.150 | 0.160 | 16 | 86 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.622 | 0.680 | 0.669 | 69 | 33 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.322 | 0.385 | 0.372 | 40 | 63 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.768 | 0.815 | 0.806 | 82 | 19 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT3 | team_total | 0.542 | 0.605 | 0.593 | 62 | 41 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.343 | 0.400 | 0.388 | 41 | 61 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.231 | 0.180 | 0.190 | 19 | 83 | yes | +0.031 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.758 | 0.805 | 0.796 | 81 | 20 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.221 | 0.175 | 0.184 | 18 | 83 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.553 | 0.610 | 0.599 | 62 | 40 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.168 | 0.215 | 0.205 | 22 | 79 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.403 | 0.460 | 0.448 | 47 | 55 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.240 | 0.190 | 0.199 | 20 | 82 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET4 | team_total | 0.435 | 0.380 | 0.391 | 39 | 63 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.155 | 0.195 | 0.186 | 20 | 81 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.204 | 0.165 | 0.172 | 17 | 84 | yes | +0.024 | OK |
| KXNHLGAME-26OCT06UTANJ-NJ | game_winner | 0.499 | 0.545 | 0.536 | 55 | 46 | no | +0.024 | OK |
| KXNHLGAME-26OCT06UTANJ-UTA | game_winner | 0.501 | 0.455 | 0.464 | 46 | 55 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.649 | 0.595 | 0.606 | 61 | 42 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.286 | 0.240 | 0.249 | 25 | 77 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA2 | team_total | 0.777 | 0.820 | 0.812 | 83 | 19 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.160 | 0.125 | 0.131 | 13 | 88 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-6 | game_total | 0.589 | 0.545 | 0.554 | 55 | 46 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.819 | 0.855 | 0.848 | 86 | 15 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR5 | team_total | 0.197 | 0.240 | 0.231 | 25 | 77 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR2 | team_total | 0.800 | 0.840 | 0.833 | 85 | 17 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT06CARMTL-6 | game_total | 0.543 | 0.585 | 0.577 | 59 | 42 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.830 | 0.790 | 0.799 | 80 | 22 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.801 | 0.760 | 0.769 | 77 | 25 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.476 | 0.435 | 0.443 | 44 | 57 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT06UTANJ-5 | game_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET6 | team_total | 0.114 | 0.080 | 0.086 | 9 | 93 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.219 | 0.265 | 0.255 | 28 | 75 | no | +0.018 | OK |
| KXNHLGAME-26OCT06MINBUF-BUF | game_winner | 0.525 | 0.485 | 0.493 | 49 | 52 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.171 | 0.205 | 0.198 | 21 | 80 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF3 | team_total | 0.653 | 0.615 | 0.623 | 62 | 39 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ3 | team_total | 0.587 | 0.630 | 0.621 | 64 | 38 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT06CARMTL-4 | game_total | 0.846 | 0.875 | 0.870 | 88 | 13 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR4 | team_total | 0.377 | 0.420 | 0.411 | 43 | 59 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.206 | 0.175 | 0.181 | 18 | 83 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.090 | 0.060 | 0.065 | 7 | 95 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT5 | team_total | 0.164 | 0.200 | 0.192 | 21 | 81 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT06CARMTL-7 | game_total | 0.428 | 0.465 | 0.458 | 47 | 54 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ2 | game_spread | 0.281 | 0.315 | 0.308 | 32 | 69 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-10 | game_total | 0.099 | 0.075 | 0.079 | 8 | 93 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT06UTANJ-NJ2 | team_total | 0.796 | 0.830 | 0.824 | 84 | 18 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.108 | 0.075 | 0.081 | 9 | 94 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA5 | team_total | 0.176 | 0.210 | 0.203 | 22 | 80 | no | +0.012 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.450 | 0.509 | 0.170 | 0.222 | 6.39 | 6.24 | 0.978/0.994 | KXNHLSPREAD-26OCT06NSHTOR-NSH2 -0.060 |
| CAR @ MTL | 0.498 | 0.520 | 0.175 | 0.218 | 6.10 | 6.24 | 0.952/0.997 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL4 +0.035 |
| OTT @ DET | 0.576 | 0.518 | 0.175 | 0.221 | 6.14 | 6.05 | 1.003/1.040 | KXNHLSPREAD-26OCT06OTTDET-DET2 -0.057 |
| UTA @ NJD | 0.499 | 0.482 | 0.182 | 0.220 | 6.05 | 6.10 | 0.987/0.992 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA4 +0.022 |
| MIN @ BUF | 0.525 | 0.514 | 0.174 | 0.212 | 6.46 | 6.43 | 0.999/1.003 | KXNHLSPREAD-26OCT06MINBUF-MIN3 +0.017 |
| NYI @ NYR | 0.572 | 0.565 | 0.183 | 0.228 | 5.78 | 5.94 | 0.957/0.956 | KXNHLTOTAL-26OCT06NYINYR-7 +0.033 |
| STL @ CHI | 0.432 | 0.439 | 0.177 | 0.217 | 5.85 | 6.19 | 1.003/0.993 | KXNHLTOTAL-26OCT06STLCHI-7 +0.063 |
| VGK @ SEA | 0.482 | 0.482 | 0.178 | 0.222 | 6.24 | 6.10 | 1.005/1.003 | KXNHLTOTAL-26OCT06VGKSEA-6 -0.030 |
| FLA @ LAK | 0.561 | 0.582 | 0.176 | 0.222 | 6.16 | 5.94 | 0.992/1.007 | KXNHLTOTAL-26OCT06FLALA-6 -0.041 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Gavin McKenna: 1+ goals NO @ 78c · p 0.845 (adj 0.825) · $7.22 · thesis TOR:SUPPRESSED
- Mavrik Bourque: 1+ goals YES @ 17c · p 0.2192 (adj 0.2031) · $3.36 · thesis NSH:OFFENSE_4PLUS
- Gavin McKenna: 1+ assists NO @ 67c · p 0.8237 (adj 0.7108) · $7.22 · thesis TOR:SUPPRESSED
- Auston Matthews: 1+ goals NO @ 62c · p 0.6597 (adj 0.6485) · $2.46 · thesis TOR:SUPPRESSED
- Alexandre Texier: 1+ goals YES @ 11c · p 0.1449 (adj 0.1324) · $2.31 · thesis MTL:OFFENSE_4PLUS
- Chris Kreider: 1+ assists NO @ 73c · p 0.8623 (adj 0.7601) · $11.27 · thesis MTL:SUPPRESSED
- Jake Evans: 1+ goals YES @ 12c · p 0.153 (adj 0.1397) · $1.85 · thesis MTL:WINS_BY_2PLUS
- Nikolaj Ehlers: 1+ goals NO @ 74c · p 0.7817 (adj 0.7688) · $8.8 · thesis CAR:SUPPRESSED
- Carter Yakemchuk: 1+ goals NO @ 88c · p 0.9347 (adj 0.916) · $9.58 · thesis OTT:SUPPRESSED
- William Eklund: 1+ assists NO @ 67c · p 0.823 (adj 0.7008) · $7.33 · thesis OTT:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 15c · p 0.1817 (adj 0.17) · $1.76 · thesis DET:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 16c · p 0.2097 (adj 0.1948) · $4.02 · thesis UTA:OFFENSE_4PLUS
- Vincent Trocheck: 1+ assists NO @ 67c · p 0.8311 (adj 0.7101) · $11.27 · thesis UTA:SUPPRESSED
- Luke Evangelista: 1+ goals NO @ 77c · p 0.8154 (adj 0.8028) · $11.27 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 12c · p 0.1477 (adj 0.1383) · $1.57 · thesis NJD:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1452 (adj 0.1314) · $3.53 · thesis MIN:OFFENSE_4PLUS
- Jiri Kulich: 1+ goals YES @ 15c · p 0.1866 (adj 0.1762) · $2.68 · thesis BUF:OFFENSE_4PLUS
- Marcus Foligno: 1+ goals YES @ 10c · p 0.1288 (adj 0.1191) · $1.84 · thesis MIN:OFFENSE_4PLUS
- Peyton Krebs: 1+ goals YES @ 12c · p 0.1499 (adj 0.1412) · $1.94 · thesis BUF:OFFENSE_4PLUS
- Matt Rempe: 1+ goals YES @ 7c · p 0.0971 (adj 0.0878) · $1.81 · thesis NYR:OFFENSE_4PLUS
- Ryan Greene: 1+ goals YES @ 11c · p 0.1774 (adj 0.1531) · $4.96 · thesis CHI:OFFENSE_4PLUS
- Philip Broberg: 1+ goals YES @ 7c · p 0.099 (adj 0.088) · $1.84 · thesis STL:OFFENSE_4PLUS
- Patrick Kane: 2+ assists NO @ 91c · p 0.9625 (adj 0.9263) · $11.27 · thesis CHI:SUPPRESSED
- Vegas wins by over 1.5 goals NO @ 62c · p 0.7098 (adj 0.6624) · $8.33 · thesis SEA:WINS
- Vegas wins by over 2.5 goals NO @ 75c · p 0.8177 (adj 0.7813) · $2.62 · thesis SEA:WINS
- Florida wins by over 2.5 goals NO @ 80c · p 0.8814 (adj 0.8382) · $8.6 · thesis LAK:WINS
- Florida wins by over 1.5 goals NO @ 70c · p 0.7911 (adj 0.743) · $6.64 · thesis LAK:WINS
- Los Angeles wins by over 1.5 goals YES @ 27c · p 0.3455 (adj 0.3053) · $1.66 · thesis LAK:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 145/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.05, exp saves 25.95 (sd 6.94), pull risk 0.061
- NSH net: Justus Annunen (PROJECTED) exp shots 28.03, exp saves 24.17 (sd 6.67), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Gavin McKenna: 1+ assists | 0.176 | 0.350 | 37/67 | +0.138 | PRIOR_HEAVY |
| Kirill Marchenko: 1+ assists | 0.287 | 0.435 | 46/59 | +0.106 | STANDARD |
| Jonathan Marchessault: 1+ points | 0.494 | 0.375 | 40/65 | +0.077 | STANDARD |
| Kirill Marchenko: 1+ points | 0.484 | 0.600 | 63/43 | +0.069 | STANDARD |
| Jonathan Marchessault: 1+ assists | 0.368 | 0.255 | 27/76 | +0.084 | STANDARD |
| Darren Raddysh: 1+ assists | 0.314 | 0.425 | 45/60 | +0.069 | STANDARD |

**CAR @ MTL** · priced 155/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (PROJECTED) exp shots 30.78, exp saves 26.69 (sd 7.18), pull risk 0.059
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.05, exp saves 19.88 (sd 5.81), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Chris Kreider: 1+ assists | 0.138 | 0.295 | 32/73 | +0.119 | STANDARD |
| Sebastian Aho: 1+ assists | 0.304 | 0.435 | 46/59 | +0.089 | STANDARD |
| Chris Kreider: 1+ points | 0.324 | 0.445 | 47/58 | +0.079 | STANDARD |
| Sebastian Aho: 1+ points | 0.483 | 0.600 | 63/43 | +0.070 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.303 | 0.390 | 41/63 | +0.050 | STANDARD |
| Sebastian Aho: 2+ points | 0.141 | 0.225 | 26/81 | +0.038 | STANDARD |

**OTT @ DET** · priced 144/149 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 27.75, exp saves 24.02 (sd 6.53), pull risk 0.053
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.38, exp saves 22.76 (sd 6.26), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| William Eklund: 1+ assists | 0.177 | 0.365 | 40/67 | +0.138 | STANDARD |
| William Eklund: 1+ points | 0.346 | 0.510 | 54/52 | +0.116 | STANDARD |
| Carter Yakemchuk: 1+ points | 0.240 | 0.385 | 41/64 | +0.104 | PRIOR_HEAVY |
| Carter Yakemchuk: 1+ assists | 0.188 | 0.295 | 32/73 | +0.069 | PRIOR_HEAVY |
| William Eklund: 2+ points | 0.071 | 0.170 | 20/86 | +0.060 | STANDARD |
| Tim Stutzle: 1+ assists | 0.385 | 0.475 | 52/57 | +0.028 | STANDARD |

**UTA @ NJD** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 26.63, exp saves 23.01 (sd 6.39), pull risk 0.062
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.76, exp saves 24.94 (sd 6.73), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.169 | 0.355 | 38/67 | +0.146 | STANDARD |
| Luke Evangelista: 1+ assists | 0.198 | 0.380 | 40/64 | +0.146 | STANDARD |
| Luke Evangelista: 1+ points | 0.345 | 0.490 | 51/53 | +0.107 | STANDARD |
| Vincent Trocheck: 1+ points | 0.334 | 0.455 | 48/57 | +0.079 | STANDARD |
| Jack Hughes: 1+ assists | 0.399 | 0.510 | 52/50 | +0.084 | STANDARD |
| Jack Hughes: 2+ points | 0.232 | 0.340 | 36/68 | +0.073 | STANDARD |

**MIN @ BUF** · priced 149/154 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.96 (sd 6.57), pull risk 0.063
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.86, exp saves 25.79 (sd 6.97), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ryan Hartman: 1+ assists | 0.353 | 0.115 | 21/98 | +0.131 | STANDARD |
| Ryan Hartman: 1+ points | 0.515 | 0.395 | 40/61 | +0.098 | STANDARD |
| Tage Thompson: 2+ points | 0.196 | 0.305 | 34/73 | +0.060 | STANDARD |
| Tage Thompson: 1+ points | 0.561 | 0.660 | 68/36 | +0.063 | STANDARD |
| Tage Thompson: 1+ assists | 0.344 | 0.440 | 47/59 | +0.050 | STANDARD |
| Max Shabanov: 1+ assists | 0.209 | 0.305 | 34/73 | +0.047 | STANDARD |

**NYI @ NYR** · priced 155/155 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.05, exp saves 24.48 (sd 6.46), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 25.47, exp saves 21.9 (sd 6.2), pull risk 0.064

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.334 | 0.235 | 28/81 | +0.040 | STANDARD |
| Kyle Palmieri: 1+ assists | 0.175 | 0.270 | 30/76 | +0.052 | STANDARD |
| Kyle Palmieri: 1+ points | 0.357 | 0.440 | 47/59 | +0.036 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.387 | 0.305 | 33/72 | +0.042 | STANDARD |
| Gabe Perreault: 1+ assists | 0.307 | 0.230 | 27/81 | +0.023 | STANDARD |
| Matias Maccelli: 1+ assists | 0.193 | 0.265 | 29/76 | +0.034 | STANDARD |

**STL @ CHI** · priced 138/147 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.19, exp saves 23.26 (sd 6.51), pull risk 0.068
- STL net: Joel Hofer (PROJECTED) exp shots 25.55, exp saves 22.32 (sd 6.19), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Patrick Kane: 1+ assists | 0.268 | 0.410 | 44/62 | +0.096 | STANDARD |
| Mason McTavish: 1+ assists | 0.210 | 0.325 | 35/70 | +0.075 | STANDARD |
| Patrick Kane: 1+ points | 0.459 | 0.570 | 59/45 | +0.074 | STANDARD |
| Ryan Greene: 1+ goals | 0.177 | 0.080 | 11/95 | +0.061 | STANDARD |
| Mason McTavish: 1+ points | 0.389 | 0.485 | 52/55 | +0.043 | STANDARD |
| Tyler Bertuzzi: 2+ points | 0.192 | 0.100 | 18/98 | +0.001 | STANDARD |

**VGK @ SEA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 28.49, exp saves 24.53 (sd 6.67), pull risk 0.061
- VGK net: Carter Hart (PROJECTED) exp shots 25.65, exp saves 22.21 (sd 6.22), pull risk 0.06

**FLA @ LAK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.39, exp saves 23.13 (sd 6.23), pull risk 0.044
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.81, exp saves 23.66 (sd 6.48), pull risk 0.063

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
