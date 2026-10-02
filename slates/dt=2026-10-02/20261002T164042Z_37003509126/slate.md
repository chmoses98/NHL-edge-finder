# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T16:40:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3200 · contracts joined: 886 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 761, 'OK': 82, 'NO_EDGE': 43}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 125, 'game_early_goal': 5, 'first_goal': 174, 'game_winner': 10, 'player_goals': 174, 'game_overtime': 5, 'player_points': 155, 'game_spread': 20, 'team_total': 50, 'game_total': 45, 'goalie_saves': 3}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 2026-10-02T22:30:00Z | T-3h | 0.563 | 0.437 | 0.174 | 5.97 | 3.18 | 2.79 | 171 (25/146) | PROBABLE/PROJECTED |
| WSH @ CAR | 2026-10-02T23:00:00Z | T-6h | 0.537 | 0.463 | 0.179 | 5.79 | 3.01 | 2.78 | 186 (25/161) | CONFIRMED/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-6h | 0.498 | 0.502 | 0.182 | 5.77 | 2.88 | 2.89 | 175 (25/150) | PROBABLE/PROJECTED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-6h | 0.538 | 0.462 | 0.177 | 5.95 | 3.10 | 2.85 | 173 (25/148) | CONFIRMED/PROJECTED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-6h | 0.596 | 0.404 | 0.172 | 6.42 | 3.51 | 2.91 | 181 (25/156) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.538 | 0.635 | 0.616 | 64 | 37 | no | +0.076 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.462 | 0.375 | 0.392 | 38 | 63 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.191 | 0.275 | 0.257 | 28 | 73 | no | +0.065 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.313 | 0.395 | 0.378 | 40 | 61 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.490 | 0.565 | 0.550 | 57 | 44 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.363 | 0.445 | 0.428 | 46 | 57 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.718 | 0.785 | 0.773 | 79 | 22 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.607 | 0.675 | 0.662 | 68 | 33 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.815 | 0.875 | 0.864 | 88 | 13 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.248 | 0.185 | 0.197 | 19 | 82 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.386 | 0.455 | 0.441 | 46 | 55 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.378 | 0.445 | 0.431 | 45 | 56 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.204 | 0.265 | 0.252 | 27 | 74 | no | +0.042 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.404 | 0.345 | 0.357 | 35 | 66 | yes | +0.038 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.596 | 0.655 | 0.643 | 66 | 35 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.587 | 0.650 | 0.638 | 66 | 36 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.184 | 0.235 | 0.224 | 24 | 77 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.205 | 0.260 | 0.248 | 27 | 75 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.716 | 0.765 | 0.756 | 77 | 24 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.283 | 0.335 | 0.324 | 34 | 67 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.335 | 0.390 | 0.379 | 40 | 62 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.688 | 0.735 | 0.726 | 74 | 27 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.189 | 0.245 | 0.233 | 26 | 77 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.376 | 0.425 | 0.415 | 43 | 58 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.558 | 0.610 | 0.600 | 62 | 40 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.552 | 0.505 | 0.514 | 51 | 50 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.488 | 0.540 | 0.530 | 55 | 47 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.140 | 0.105 | 0.111 | 11 | 90 | yes | +0.024 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.311 | 0.355 | 0.346 | 36 | 65 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.797 | 0.840 | 0.832 | 85 | 17 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.167 | 0.205 | 0.197 | 21 | 80 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.481 | 0.525 | 0.516 | 53 | 48 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.139 | 0.180 | 0.171 | 19 | 83 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.522 | 0.565 | 0.556 | 57 | 44 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.811 | 0.850 | 0.843 | 86 | 16 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.160 | 0.195 | 0.187 | 20 | 81 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.812 | 0.860 | 0.851 | 88 | 16 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.333 | 0.295 | 0.302 | 30 | 71 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.740 | 0.775 | 0.768 | 78 | 23 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT02NYRDET-NYR3 | game_spread | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.486 | 0.525 | 0.517 | 53 | 48 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.794 | 0.830 | 0.823 | 84 | 18 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02NYRDET-5 | game_total | 0.742 | 0.775 | 0.769 | 78 | 23 | no | +0.016 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.463 | 0.425 | 0.433 | 43 | 58 | yes | +0.016 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.216 | 0.185 | 0.191 | 19 | 82 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.088 | 0.125 | 0.117 | 14 | 89 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.775 | 0.815 | 0.807 | 83 | 20 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.204 | 0.235 | 0.228 | 24 | 77 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.860 | 0.890 | 0.885 | 90 | 12 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.829 | 0.855 | 0.850 | 86 | 15 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.141 | 0.170 | 0.164 | 18 | 84 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.276 | 0.305 | 0.299 | 31 | 70 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-NYR2 | team_total | 0.759 | 0.790 | 0.784 | 80 | 22 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-NYR3 | team_total | 0.534 | 0.565 | 0.559 | 57 | 44 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-10 | game_total | 0.058 | 0.075 | 0.071 | 8 | 93 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-NYR4 | team_total | 0.318 | 0.350 | 0.343 | 36 | 66 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-WSH2 | team_total | 0.762 | 0.790 | 0.785 | 80 | 22 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-10 | game_total | 0.059 | 0.080 | 0.075 | 9 | 93 | no | +0.006 | OK |
| KXNHLGAME-26OCT02NYRDET-NYR | game_winner | 0.437 | 0.465 | 0.459 | 47 | 54 | no | +0.006 | OK |
| KXNHLGAME-26OCT02NYRDET-DET | game_winner | 0.563 | 0.535 | 0.541 | 54 | 47 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.598 | 0.625 | 0.620 | 63 | 38 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.290 | 0.315 | 0.310 | 32 | 69 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.122 | 0.105 | 0.108 | 11 | 90 | yes | +0.005 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.502 | 0.475 | 0.480 | 48 | 53 | yes | +0.004 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.498 | 0.525 | 0.520 | 53 | 48 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.163 | 0.140 | 0.144 | 15 | 87 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT02STLDAL-8 | game_total | 0.224 | 0.245 | 0.241 | 25 | 76 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.138 | 0.155 | 0.152 | 16 | 85 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02NYRDET-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.207 | 0.225 | 0.221 | 23 | 78 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.411 | 0.435 | 0.430 | 44 | 57 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-10 | game_total | 0.102 | 0.115 | 0.112 | 12 | 89 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA6 | team_total | 0.075 | 0.065 | 0.067 | 7 | 94 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-2 | game_total | 0.978 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 0.563 | 0.542 | 0.174 | 0.212 | 5.97 | 6.12 | 0.998/0.983 | KXNHLTOTAL-26OCT02NYRDET-7 +0.032 |
| WSH @ CAR | 0.537 | 0.563 | 0.179 | 0.214 | 5.79 | 6.22 | 0.984/0.938 | KXNHLTOTAL-26OCT02WSHCAR-7 +0.076 |
| BOS @ WPG | 0.498 | 0.519 | 0.182 | 0.218 | 5.77 | 6.09 | 0.995/0.968 | KXNHLTOTAL-26OCT02BOSWPG-7 +0.057 |
| STL @ DAL | 0.538 | 0.543 | 0.177 | 0.219 | 5.95 | 6.15 | 0.994/0.993 | KXNHLTOTAL-26OCT02STLDAL-7 +0.035 |
| ANA @ VGK | 0.596 | 0.593 | 0.172 | 0.208 | 6.42 | 6.42 | 1.003/1.016 | KXNHLSPREAD-26OCT02ANAVGK-VGK3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 19 recommended · full analysis in card.md / packet.json `thesis_card`

- Nate Danielson: 1+ goals YES @ 10c · p 0.1294 (adj 0.1208) · $3.47 · thesis DET:OFFENSE_4PLUS
- Oliver Bjorkstrand: 1+ goals NO @ 83c · p 0.8619 (adj 0.8527) · $18.13 · thesis NYR:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 15c · p 0.1801 (adj 0.1701) · $2.88 · thesis DET:OFFENSE_4PLUS
- William Carrier: 1+ goals YES @ 8c · p 0.1258 (adj 0.1131) · $6.09 · thesis CAR:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2343 (adj 0.217) · $9.62 · thesis WSH:OFFENSE_4PLUS
- Alex Tuch: 1+ assists NO @ 76c · p 0.8768 (adj 0.7944) · $18.13 · thesis WSH:SUPPRESSED
- Boone Jenner: 1+ goals YES @ 11c · p 0.1513 (adj 0.1335) · $3.88 · thesis WSH:OFFENSE_4PLUS
- Marat Khusnutdinov: 1+ goals YES @ 10c · p 0.1422 (adj 0.1291) · $5.21 · thesis BOS:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 18c · p 0.2325 (adj 0.2181) · $7.8 · thesis BOS:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1644 (adj 0.1545) · $4.11 · thesis WPG:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 72c · p 0.8412 (adj 0.7494) · $18.13 · thesis BOS:SUPPRESSED
- Miro Heiskanen: 1+ goals NO @ 85c · p 0.9007 (adj 0.8868) · $18.13 · thesis DAL:SUPPRESSED
- Pius Suter: 1+ goals YES @ 11c · p 0.1525 (adj 0.1406) · $5.49 · thesis STL:OFFENSE_4PLUS
- Dylan Holloway: 1+ goals YES @ 26c · p 0.3129 (adj 0.2984) · $7.33 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 25c · p 0.2995 (adj 0.2859) · $6.51 · thesis STL:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 8c · p 0.1134 (adj 0.1038) · $4.01 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1125 (adj 0.1019) · $3.49 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 23c · p 0.362 (adj 0.2665) · $5.25 · thesis ANA:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0828 (adj 0.0746) · $2.34 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ DET** · priced 114/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 25.06, exp saves 21.9 (sd 6.11), pull risk 0.055
- NYR net: Dylan Garand (PROJECTED) exp shots 28.53, exp saves 24.54 (sd 6.78), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ assists | 0.175 | 0.285 | 30/73 | +0.081 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.406 | 0.510 | 52/50 | +0.077 | STANDARD |
| Pavel Dorofeyev: 2+ points | 0.101 | 0.180 | 20/84 | +0.049 | STANDARD |
| Gabe Perreault: 1+ assists | 0.300 | 0.230 | 24/78 | +0.047 | STANDARD |
| Gabe Perreault: 1+ points | 0.439 | 0.380 | 40/64 | +0.022 | STANDARD |
| Alex DeBrincat: 1+ assists | 0.356 | 0.415 | 43/60 | +0.027 | STANDARD |

**WSH @ CAR** · priced 133/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Brandon Bussi (CONFIRMED) exp shots 23.54, exp saves 20.59 (sd 5.89), pull risk 0.054
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.09 (sd 7.05), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Tuch: 1+ assists | 0.123 | 0.250 | 26/76 | +0.104 | STANDARD |
| Sebastian Aho: 1+ assists | 0.334 | 0.450 | 47/57 | +0.079 | STANDARD |
| Sebastian Aho: 2+ points | 0.162 | 0.255 | 28/77 | +0.056 | STANDARD |
| Sebastian Aho: 1+ points | 0.518 | 0.610 | 63/41 | +0.055 | STANDARD |
| Alex Tuch: 1+ points | 0.342 | 0.420 | 44/60 | +0.041 | STANDARD |
| Alex Tuch: 1+ goals | 0.252 | 0.175 | 25/90 | -0.011 | STANDARD |

**BOS @ WPG** · priced 124/124 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 26.1, exp saves 22.66 (sd 6.18), pull risk 0.056
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.24, exp saves 24.4 (sd 6.6), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ points | 0.343 | 0.495 | 50/51 | +0.130 | STANDARD |
| JJ Peterka: 1+ assists | 0.159 | 0.300 | 32/72 | +0.107 | STANDARD |
| Elias Lindholm: 1+ points | 0.495 | 0.395 | 41/62 | +0.069 | STANDARD |
| JJ Peterka: 2+ points | 0.072 | 0.150 | 17/87 | +0.050 | STANDARD |
| Elias Lindholm: 1+ assists | 0.343 | 0.275 | 29/74 | +0.038 | STANDARD |
| Morgan Geekie: 1+ assists | 0.358 | 0.290 | 30/72 | +0.043 | STANDARD |

**STL @ DAL** · priced 122/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.53, exp saves 21.36 (sd 5.94), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 26.73, exp saves 22.85 (sd 6.42), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.127 | 0.250 | 27/77 | +0.091 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.605 | 62/41 | +0.091 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.403 | 0.525 | 54/49 | +0.090 | STANDARD |
| Roope Hintz: 1+ assists | 0.293 | 0.410 | 43/61 | +0.080 | STANDARD |
| Mikko Rantanen: 2+ points | 0.205 | 0.315 | 32/69 | +0.090 | STANDARD |
| Jason Robertson: 1+ assists | 0.381 | 0.490 | 50/52 | +0.082 | STANDARD |

**ANA @ VGK** · priced 128/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 28.77, exp saves 25.13 (sd 6.71), pull risk 0.055
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.59, exp saves 23.42 (sd 6.74), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.506 | 0.350 | 36/66 | +0.130 | STANDARD |
| Alex Killorn: 1+ assists | 0.362 | 0.215 | 23/80 | +0.120 | STANDARD |
| Leo Carlsson: 1+ assists | 0.298 | 0.415 | 43/60 | +0.085 | STANDARD |
| Jack Eichel: 1+ assists | 0.452 | 0.550 | 57/47 | +0.061 | STANDARD |
| Jack Eichel: 2+ points | 0.258 | 0.355 | 37/66 | +0.066 | STANDARD |
| Leo Carlsson: 2+ points | 0.155 | 0.235 | 25/78 | +0.053 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
