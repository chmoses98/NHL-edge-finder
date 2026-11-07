# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-07T19:33:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 10 · markets on board: 4310 · contracts joined: 2272 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2022, 'OK': 142, 'NO_EDGE': 108}
families: {'period_winner': 90, 'period_spread': 60, 'period_total': 90, 'player_assists': 328, 'game_early_goal': 10, 'first_goal': 360, 'game_winner': 20, 'player_goals': 618, 'game_overtime': 10, 'player_points': 441, 'goalie_saves': 15, 'game_spread': 40, 'team_total': 100, 'game_total': 90}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ SEA | 2026-11-07T22:00:00Z | T-90m | 0.503 | 0.496 | 0.177 | 6.35 | 3.19 | 3.16 | 228 (25/203) | PROJECTED/PROJECTED |
| MTL @ TOR | 2026-11-08T00:00:00Z | T-3h | 0.459 | 0.541 | 0.165 | 6.72 | 3.22 | 3.50 | 221 (25/196) | CONFIRMED/CONFIRMED |
| UTA @ OTT | 2026-11-08T00:00:00Z | T-3h | 0.446 | 0.554 | 0.163 | 6.70 | 3.18 | 3.52 | 225 (25/200) | CONFIRMED/PROJECTED |
| NJD @ NYI | 2026-11-08T00:00:00Z | T-3h | 0.492 | 0.508 | 0.180 | 5.80 | 2.88 | 2.92 | 220 (25/195) | PROBABLE/CONFIRMED |
| CHI @ CAR | 2026-11-08T01:00:00Z | T-3h | 0.737 | 0.263 | 0.151 | 6.02 | 3.77 | 2.24 | 234 (25/209) | PROBABLE/PROBABLE |
| SJS @ DAL | 2026-11-08T01:00:00Z | T-3h | 0.681 | 0.319 | 0.167 | 5.91 | 3.52 | 2.39 | 233 (25/208) | CONFIRMED/PROJECTED |
| TBL @ MIN | 2026-11-08T01:00:00Z | T-3h | 0.439 | 0.561 | 0.174 | 6.33 | 2.97 | 3.36 | 228 (25/203) | CONFIRMED/CONFIRMED |
| DET @ COL | 2026-11-08T02:00:00Z | T-6h | 0.628 | 0.372 | 0.170 | 6.23 | 3.53 | 2.69 | 238 (25/213) | CONFIRMED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-6h | 0.568 | 0.432 | 0.167 | 6.64 | 3.54 | 3.10 | 220 (25/195) | PROBABLE/CONFIRMED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-6h | 0.735 | 0.265 | 0.136 | 7.19 | 4.43 | 2.76 | 225 (25/200) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4 | team_total | 0.483 | 0.595 | 0.573 | 60 | 41 | no | +0.090 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR3 | game_spread | 0.361 | 0.470 | 0.448 | 48 | 54 | no | +0.082 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CAR2 | game_spread | 0.512 | 0.605 | 0.587 | 61 | 40 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ4 | team_total | 0.345 | 0.440 | 0.420 | 45 | 57 | no | +0.068 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL3 | game_spread | 0.296 | 0.385 | 0.366 | 39 | 62 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR4 | team_total | 0.536 | 0.630 | 0.612 | 64 | 38 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR5 | team_total | 0.330 | 0.420 | 0.401 | 43 | 59 | no | +0.063 | OK |
| KXNHLGAME-26NOV07NJNYI-NJ | game_winner | 0.508 | 0.585 | 0.570 | 59 | 42 | no | +0.055 | OK |
| KXNHLGAME-26NOV07NJNYI-NYI | game_winner | 0.492 | 0.415 | 0.430 | 42 | 59 | yes | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL5 | team_total | 0.282 | 0.360 | 0.344 | 37 | 65 | no | +0.052 | OK |
| KXNHLGAME-26NOV07CHICAR-CAR | game_winner | 0.737 | 0.805 | 0.793 | 81 | 20 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ3 | game_spread | 0.167 | 0.235 | 0.220 | 24 | 77 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ2 | team_total | 0.781 | 0.845 | 0.834 | 85 | 16 | no | +0.050 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NJ2 | game_spread | 0.285 | 0.355 | 0.340 | 36 | 65 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV07SJDAL-DAL2 | game_spread | 0.446 | 0.520 | 0.505 | 53 | 49 | no | +0.047 | OK |
| KXNHLGAME-26NOV07NYRSEA-SEA | game_winner | 0.503 | 0.435 | 0.449 | 44 | 57 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ3 | team_total | 0.568 | 0.640 | 0.626 | 65 | 37 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR3 | team_total | 0.744 | 0.815 | 0.802 | 83 | 20 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR2 | game_spread | 0.281 | 0.345 | 0.332 | 35 | 66 | no | +0.044 | OK |
| KXNHLSPREAD-26NOV07NJNYI-NYI2 | game_spread | 0.275 | 0.215 | 0.226 | 22 | 79 | yes | +0.043 | OK |
| KXNHLGAME-26NOV07CHICAR-CHI | game_winner | 0.263 | 0.205 | 0.216 | 21 | 80 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL3 | team_total | 0.696 | 0.765 | 0.752 | 78 | 25 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA3 | team_total | 0.694 | 0.635 | 0.647 | 64 | 37 | yes | +0.038 | OK |
| KXNHLTOTAL-26NOV07SJDAL-6 | game_total | 0.516 | 0.575 | 0.563 | 58 | 43 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV07CHICAR-6 | game_total | 0.537 | 0.600 | 0.588 | 61 | 41 | no | +0.037 | OK |
| KXNHLGAME-26NOV07NYRSEA-NYR | game_winner | 0.496 | 0.555 | 0.543 | 56 | 45 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV07NJNYI-5 | game_total | 0.722 | 0.775 | 0.765 | 78 | 23 | no | +0.035 | OK |
| KXNHLGAME-26NOV07SJDAL-DAL | game_winner | 0.681 | 0.735 | 0.725 | 74 | 27 | no | +0.035 | OK |
| KXNHLGAME-26NOV07SJDAL-SJ | game_winner | 0.319 | 0.265 | 0.275 | 27 | 74 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.520 | 0.465 | 0.476 | 47 | 54 | yes | +0.033 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.234 | 0.285 | 0.274 | 29 | 72 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07SJDAL-5 | game_total | 0.736 | 0.790 | 0.780 | 80 | 22 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07NJNYI-7 | game_total | 0.381 | 0.435 | 0.424 | 44 | 57 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ5 | team_total | 0.176 | 0.235 | 0.222 | 25 | 78 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV07SJDAL-4 | game_total | 0.831 | 0.875 | 0.867 | 88 | 13 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR6 | team_total | 0.168 | 0.225 | 0.213 | 24 | 79 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-NYR3 | game_spread | 0.168 | 0.220 | 0.209 | 23 | 79 | no | +0.030 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.568 | 0.515 | 0.526 | 52 | 49 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.265 | 0.315 | 0.305 | 32 | 69 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.324 | 0.275 | 0.284 | 28 | 73 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07CHICAR-CAR2 | team_total | 0.896 | 0.935 | 0.928 | 94 | 7 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA4 | team_total | 0.486 | 0.430 | 0.441 | 44 | 58 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-8 | game_total | 0.332 | 0.285 | 0.294 | 29 | 72 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV07CHICAR-7 | game_total | 0.415 | 0.470 | 0.459 | 48 | 54 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV07NYRSEA-SEA2 | game_spread | 0.290 | 0.245 | 0.254 | 25 | 76 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV07SJDAL-8 | game_total | 0.220 | 0.265 | 0.256 | 27 | 74 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.412 | 0.365 | 0.374 | 37 | 64 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV07NYRSEA-NYR4 | team_total | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV07SJDAL-DAL2 | team_total | 0.869 | 0.910 | 0.903 | 92 | 10 | no | +0.025 | OK |
| KXNHLTOTAL-26NOV07SJDAL-7 | game_total | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA5 | team_total | 0.287 | 0.235 | 0.245 | 25 | 78 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV07CHICAR-4 | game_total | 0.839 | 0.880 | 0.873 | 89 | 13 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.481 | 0.535 | 0.524 | 55 | 48 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07PITLA-7 | game_total | 0.519 | 0.475 | 0.484 | 48 | 53 | yes | +0.021 | OK |
| KXNHLTOTAL-26NOV07CHICAR-5 | game_total | 0.748 | 0.795 | 0.786 | 81 | 22 | no | +0.020 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.432 | 0.475 | 0.466 | 48 | 53 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV07CHICAR-8 | game_total | 0.236 | 0.280 | 0.271 | 29 | 73 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.355 | 0.310 | 0.319 | 32 | 70 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV07UTAOTT-10 | game_total | 0.125 | 0.095 | 0.100 | 10 | 91 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.771 | 0.810 | 0.803 | 82 | 20 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV07NJNYI-6 | game_total | 0.495 | 0.535 | 0.527 | 54 | 47 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV07CHICAR-CHI2 | game_spread | 0.113 | 0.085 | 0.090 | 9 | 92 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA6 | team_total | 0.144 | 0.110 | 0.116 | 12 | 90 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.155 | 0.115 | 0.122 | 13 | 90 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV07PITLA-9 | game_total | 0.238 | 0.200 | 0.207 | 21 | 81 | yes | +0.016 | OK |
| KXNHLGAME-26NOV07UTAOTT-UTA | game_winner | 0.554 | 0.515 | 0.523 | 52 | 49 | yes | +0.016 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.628 | 0.665 | 0.658 | 67 | 34 | no | +0.016 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.372 | 0.335 | 0.342 | 34 | 67 | yes | +0.016 | OK |
| KXNHLTOTAL-26NOV07NJNYI-8 | game_total | 0.203 | 0.235 | 0.228 | 24 | 77 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07MTLTOR-MTL6 | team_total | 0.142 | 0.115 | 0.120 | 12 | 89 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07NJNYI-4 | game_total | 0.816 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA6 | team_total | 0.141 | 0.115 | 0.120 | 12 | 89 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07SJDAL-9 | game_total | 0.146 | 0.180 | 0.173 | 19 | 83 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT3 | game_spread | 0.137 | 0.165 | 0.159 | 17 | 84 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07SJDAL-3 | game_total | 0.955 | 0.975 | 0.972 | 98 | 3 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07VANEDM-9 | game_total | 0.307 | 0.270 | 0.277 | 28 | 74 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07NJNYI-NJ6 | team_total | 0.071 | 0.100 | 0.094 | 11 | 91 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07TBMIN-7 | game_total | 0.470 | 0.505 | 0.498 | 51 | 50 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV07UTAOTT-UTA4 | team_total | 0.480 | 0.445 | 0.452 | 45 | 56 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV07CHICAR-9 | game_total | 0.157 | 0.185 | 0.179 | 19 | 82 | no | +0.013 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ SEA | 0.503 | 0.541 | 0.177 | 0.220 | 6.35 | 6.34 | 1.005/0.983 | KXNHLGAME-26NOV07NYRSEA-SEA +0.038 |
| MTL @ TOR | 0.459 | 0.532 | 0.165 | 0.210 | 6.72 | 6.78 | 0.988/0.983 | KXNHLGAME-26NOV07MTLTOR-TOR +0.073 |
| UTA @ OTT | 0.446 | 0.521 | 0.163 | 0.213 | 6.70 | 6.58 | 1.071/0.993 | KXNHLGAME-26NOV07UTAOTT-OTT +0.074 |
| NJD @ NYI | 0.492 | 0.516 | 0.180 | 0.216 | 5.80 | 6.19 | 0.952/0.983 | KXNHLTOTAL-26NOV07NJNYI-7 +0.071 |
| CHI @ CAR | 0.737 | 0.685 | 0.151 | 0.193 | 6.02 | 6.53 | 1.000/0.995 | KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3 +0.106 |
| SJS @ DAL | 0.681 | 0.628 | 0.167 | 0.214 | 5.91 | 6.21 | 0.994/1.027 | KXNHLTEAMTOTAL-26NOV07SJDAL-SJ3 +0.079 |
| TBL @ MIN | 0.439 | 0.486 | 0.174 | 0.214 | 6.33 | 6.43 | 1.033/0.985 | KXNHLGAME-26NOV07TBMIN-MIN +0.048 |
| DET @ COL | 0.628 | 0.661 | 0.170 | 0.202 | 6.23 | 6.48 | 0.979/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.057 |
| PIT @ LAK | 0.568 | 0.546 | 0.167 | 0.218 | 6.64 | 6.35 | 0.994/1.012 | KXNHLTOTAL-26NOV07PITLA-6 -0.050 |
| VAN @ EDM | 0.735 | 0.670 | 0.136 | 0.190 | 7.19 | 6.99 | 0.994/1.030 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.073 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 37 recommended · full analysis in card.md / packet.json `thesis_card`

- Ben Meyers: 1+ goals YES @ 10c · p 0.1501 (adj 0.1363) · $3.74 · thesis SEA:OFFENSE_4PLUS
- Jani Nyman: 1+ goals YES @ 11c · p 0.1535 (adj 0.1401) · $2.95 · thesis SEA:OFFENSE_4PLUS
- Kaapo Kakko: 1+ goals YES @ 15c · p 0.1937 (adj 0.1815) · $3.12 · thesis SEA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 66c · p 0.7115 (adj 0.6961) · $7.68 · thesis NYR:SUPPRESSED
- Brandon Duhaime: 1+ goals YES @ 7c · p 0.1064 (adj 0.096) · $2.56 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 2+ assists NO @ 83c · p 0.9171 (adj 0.8686) · $9.75 · thesis MTL:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1691 (adj 0.1481) · $2.55 · thesis TOR:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 48c · p 0.6201 (adj 0.5225) · $5.09 · thesis MTL:SUPPRESSED
- Lawson Crouse: 1+ goals YES @ 17c · p 0.2123 (adj 0.1992) · $2.75 · thesis UTA:OFFENSE_4PLUS
- Dylan Cozens: 1+ goals YES @ 25c · p 0.2979 (adj 0.2847) · $3.51 · thesis OTT:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 16c · p 0.2013 (adj 0.1847) · $2.13 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ goals YES @ 20c · p 0.2399 (adj 0.2274) · $2.42 · thesis OTT:OFFENSE_4PLUS
- New York I wins by over 1.5 goals YES @ 22c · p 0.2981 (adj 0.2566) · $2.52 · thesis NYI:WINS_BY_2PLUS
- Adam Pelech: 1+ goals YES @ 4c · p 0.0607 (adj 0.0543) · $1.18 · thesis DIFFUSE
- New Jersey wins by over 1.5 goals NO @ 65c · p 0.739 (adj 0.692) · $8.62 · thesis NYI:WINS
- Cody Glass: 1+ goals YES @ 11c · p 0.1403 (adj 0.1315) · $2.39 · thesis NJD:OFFENSE_4PLUS
- Dillon Boucher: 1+ goals YES @ 5c · p 0.0895 (adj 0.0771) · $2.56 · thesis CHI:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 62c · p 0.7034 (adj 0.6801) · $9.89 · thesis CAR:SUPPRESSED
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.243 (adj 0.2273) · $3.9 · thesis CHI:OFFENSE_4PLUS
- Oliver Moore: 1+ goals YES @ 11c · p 0.1534 (adj 0.1363) · $2.47 · thesis CHI:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 63c · p 0.6875 (adj 0.6719) · $8.54 · thesis DAL:SUPPRESSED
- Jacob Trouba: 1+ goals YES @ 5c · p 0.0736 (adj 0.0652) · $1.26 · thesis SJS:OFFENSE_4PLUS
- San Jose over 3.5 goals scored YES @ 23c · p 0.2946 (adj 0.2573) · $1.72 · thesis SJS:OFFENSE_4PLUS
- Dallas over 3.5 goals scored NO @ 41c · p 0.5133 (adj 0.4429) · $1.75 · thesis DAL:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1383 (adj 0.125) · $3.53 · thesis MIN:OFFENSE_4PLUS
- Bobby Brink: 1+ goals YES @ 14c · p 0.1867 (adj 0.17) · $2.87 · thesis MIN:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ assists NO @ 52c · p 0.6149 (adj 0.565) · $8.29 · thesis MIN:SUPPRESSED
- Blake Coleman: 1+ goals YES @ 20c · p 0.2424 (adj 0.2306) · $2.9 · thesis MIN:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ assists YES @ 28c · p 0.3437 (adj 0.3094) · $2.51 · thesis COL:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0751 (adj 0.0688) · $1.82 · thesis LAK:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1258 (adj 0.1106) · $1.83 · thesis PIT:WINS_BY_2PLUS
- Ben Kindel: 1+ goals NO @ 77c · p 0.814 (adj 0.8017) · $9.89 · thesis PIT:SUPPRESSED
- Andre Lee: 1+ goals YES @ 10c · p 0.1253 (adj 0.1177) · $1.47 · thesis LAK:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 9c · p 0.1436 (adj 0.129) · $3.98 · thesis VAN:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 15c · p 0.2205 (adj 0.1966) · $4.82 · thesis VAN:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 27c · p 0.3483 (adj 0.3275) · $7.3 · thesis EDM:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.2125 (adj 0.1969) · $3.72 · thesis VAN:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ SEA** · priced 176/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Joey Daccord (PROJECTED) exp shots 27.17, exp saves 23.64 (sd 6.44), pull risk 0.057
- NYR net: Dylan Garand (PROJECTED) exp shots 27.28, exp saves 23.37 (sd 6.57), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Freddy Gaudreau: 1+ points | 0.413 | 0.190 | 37/99 | +0.027 | STANDARD |
| Freddy Gaudreau: 1+ assists | 0.286 | 0.125 | 24/99 | +0.033 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.183 | 0.100 | 16/96 | +0.014 | STANDARD |
| Bobby McMann: 1+ assists | 0.308 | 0.240 | 25/77 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ goals | 0.288 | 0.350 | 36/66 | +0.036 | STANDARD |
| Vladislav Gavrikov: 1+ assists | 0.315 | 0.255 | 27/76 | +0.031 | STANDARD |

**MTL @ TOR** · priced 167/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.0, exp saves 25.08 (sd 6.94), pull risk 0.07
- MTL net: Jacob Fowler (CONFIRMED) exp shots 28.71, exp saves 24.68 (sd 6.91), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nick Suzuki: 1+ assists | 0.380 | 0.530 | 54/48 | +0.123 | STANDARD |
| Oliver Ekman-Larsson: 1+ assists | 0.241 | 0.125 | 24/99 | -0.012 | STANDARD |
| Alexandre Texier: 1+ assists | 0.229 | 0.120 | 23/99 | -0.013 | STANDARD |
| Nick Suzuki: 2+ assists | 0.083 | 0.180 | 19/83 | +0.077 | STANDARD |
| Nick Suzuki: 1+ points | 0.576 | 0.670 | 69/35 | +0.058 | STANDARD |
| Easton Cowan: 1+ points | 0.519 | 0.430 | 45/59 | +0.052 | STANDARD |

**UTA @ OTT** · priced 168/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 26.39, exp saves 22.89 (sd 6.44), pull risk 0.067
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.47, exp saves 23.56 (sd 6.6), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Fabian Zetterlund: 1+ assists | 0.307 | 0.215 | 24/81 | +0.055 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.474 | 0.385 | 40/63 | +0.057 | STANDARD |
| Clayton Keller: 1+ points | 0.588 | 0.665 | 68/35 | +0.047 | STANDARD |
| Mikhail Sergachev: 2+ points | 0.151 | 0.220 | 24/80 | +0.038 | STANDARD |
| Mikhail Sergachev: 1+ points | 0.506 | 0.575 | 60/45 | +0.026 | STANDARD |
| Clayton Keller: 1+ assists | 0.452 | 0.520 | 54/50 | +0.031 | STANDARD |

**NJD @ NYI** · priced 166/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Ilya Sorokin (PROBABLE) exp shots 28.65, exp saves 24.91 (sd 6.74), pull risk 0.057
- NJD net: Jake Allen (CONFIRMED) exp shots 26.66, exp saves 23.05 (sd 6.42), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.381 | 0.510 | 52/50 | +0.102 | STANDARD |
| Jack Hughes: 2+ points | 0.214 | 0.325 | 34/69 | +0.081 | STANDARD |
| Emil Heineman: 1+ assists | 0.300 | 0.195 | 20/81 | +0.089 | STANDARD |
| Luke Evangelista: 1+ assists | 0.228 | 0.330 | 34/68 | +0.077 | STANDARD |
| Emil Heineman: 1+ points | 0.435 | 0.350 | 37/67 | +0.049 | STANDARD |
| Jack Hughes: 1+ points | 0.580 | 0.665 | 69/36 | +0.044 | STANDARD |

**CHI @ CAR** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROBABLE) exp shots 21.81, exp saves 19.44 (sd 5.57), pull risk 0.045
- CHI net: Spencer Knight (PROBABLE) exp shots 33.1, exp saves 27.69 (sd 7.63), pull risk 0.097

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 2+ points | 0.204 | 0.335 | 35/68 | +0.100 | STANDARD |
| Sebastian Aho: 1+ assists | 0.380 | 0.495 | 51/52 | +0.083 | STANDARD |
| Tyler Bertuzzi: 1+ points | 0.465 | 0.355 | 36/65 | +0.089 | STANDARD |
| Sebastian Aho: 1+ points | 0.561 | 0.655 | 70/39 | +0.032 | STANDARD |
| Sebastian Aho: 1+ goals | 0.297 | 0.390 | 40/62 | +0.067 | STANDARD |
| Nikolaj Ehlers: 1+ assists | 0.392 | 0.480 | 49/53 | +0.060 | STANDARD |

**SJS @ DAL** · priced 179/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.49, exp saves 21.6 (sd 5.9), pull risk 0.045
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.67, exp saves 23.5 (sd 6.65), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Collin Graf: 1+ points | 0.361 | 0.180 | 32/96 | +0.025 | STANDARD |
| Collin Graf: 1+ assists | 0.240 | 0.110 | 20/98 | +0.029 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.186 | 0.295 | 31/72 | +0.080 | STANDARD |
| Mikko Rantanen: 2+ points | 0.284 | 0.390 | 41/63 | +0.070 | STANDARD |
| Ivar Stenberg: 1+ points | 0.312 | 0.415 | 43/60 | +0.071 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.489 | 0.575 | 60/45 | +0.044 | STANDARD |

**TBL @ MIN** · priced 165/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Calvin Pickard (CONFIRMED) exp shots 28.08, exp saves 24.13 (sd 6.68), pull risk 0.068
- TBL net: Dennis Hildeby (CONFIRMED) exp shots 27.46, exp saves 23.81 (sd 6.5), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.491 | 0.625 | 64/39 | +0.102 | STANDARD |
| Dennis Hildeby: 25+ saves | 0.450 | 0.330 | 53/87 | -0.098 |  |
| Matt Boldy: 1+ assists | 0.373 | 0.485 | 49/52 | +0.090 | STANDARD |
| Nikita Kucherov: 2+ points | 0.295 | 0.405 | 42/61 | +0.078 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.278 | 0.385 | 40/63 | +0.076 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.145 | 0.245 | 27/78 | +0.063 | STANDARD |

**DET @ COL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.53, exp saves 23.51 (sd 6.29), pull risk 0.046
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.32 (sd 7.17), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lucas Raymond: 1+ assists | 0.318 | 0.410 | 43/61 | +0.055 | STANDARD |
| Sam Malinski: 1+ assists | 0.318 | 0.230 | 26/80 | +0.045 | STANDARD |
| Lucas Raymond: 1+ points | 0.486 | 0.570 | 60/46 | +0.037 | STANDARD |
| Sam Malinski: 1+ points | 0.376 | 0.295 | 32/73 | +0.041 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.370 | 0.440 | 46/58 | +0.033 | STANDARD |
| Artturi Lehkonen: 1+ assists | 0.344 | 0.275 | 28/73 | +0.050 | STANDARD |

**PIT @ LAK** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.28, exp saves 23.67 (sd 6.45), pull risk 0.059
- PIT net: Sergei Murashov (CONFIRMED) exp shots 27.6, exp saves 23.6 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.418 | 0.530 | 54/48 | +0.085 | STANDARD |
| Artemi Panarin: 2+ points | 0.238 | 0.340 | 35/67 | +0.077 | STANDARD |
| Ben Kindel: 1+ points | 0.364 | 0.460 | 48/56 | +0.058 | STANDARD |
| Erik Karlsson: 1+ assists | 0.408 | 0.485 | 49/52 | +0.055 | STANDARD |
| Erik Karlsson: 1+ points | 0.487 | 0.560 | 59/47 | +0.025 | STANDARD |
| Trevor Moore: 1+ points | 0.428 | 0.360 | 39/67 | +0.022 | STANDARD |

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.32 (sd 5.93), pull risk 0.052
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.14, exp saves 25.04 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.264 | 0.405 | 43/62 | +0.099 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.617 | 0.485 | 51/54 | +0.090 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.416 | 0.300 | 32/72 | +0.080 | STANDARD |
| Leon Draisaitl: 2+ points | 0.433 | 0.545 | 56/47 | +0.080 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.252 | 0.140 | 16/88 | +0.083 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.343 | 0.450 | 47/57 | +0.070 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
