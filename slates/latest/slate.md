# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-10T20:38:39Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 7 · markets on board: 3388 · contracts joined: 1560 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1385, 'NO_EDGE': 76, 'OK': 99}
families: {'period_winner': 63, 'period_spread': 42, 'period_total': 63, 'player_assists': 232, 'game_early_goal': 7, 'first_goal': 237, 'game_winner': 14, 'player_goals': 419, 'game_overtime': 7, 'player_points': 304, 'goalie_saves': 11, 'game_spread': 28, 'team_total': 70, 'game_total': 63}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ TOR | 2026-11-11T00:00:00Z | T-3h | 0.400 | 0.600 | 0.164 | 6.77 | 3.05 | 3.72 | 224 (25/199) | CONFIRMED/CONFIRMED |
| MIN @ MTL | 2026-11-11T00:00:00Z | T-3h | 0.507 | 0.493 | 0.182 | 5.97 | 3.01 | 2.96 | 231 (25/206) | CONFIRMED/CONFIRMED |
| WSH @ OTT | 2026-11-11T00:00:00Z | T-3h | 0.453 | 0.547 | 0.164 | 6.62 | 3.15 | 3.48 | 230 (25/205) | CONFIRMED/PROJECTED |
| NJD @ WPG | 2026-11-11T00:00:00Z | T-3h | 0.429 | 0.571 | 0.173 | 6.15 | 2.86 | 3.29 | 220 (25/195) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-11-11T00:30:00Z | T-3h | 0.509 | 0.491 | 0.167 | 6.48 | 3.27 | 3.21 | 222 (25/197) | CONFIRMED/CONFIRMED |
| DET @ STL | 2026-11-11T01:00:00Z | T-3h | 0.595 | 0.405 | 0.175 | 5.80 | 3.19 | 2.61 | 230 (25/205) | CONFIRMED/CONFIRMED |
| NSH @ LAK | 2026-11-11T03:00:00Z | T-6h | 0.571 | 0.429 | 0.179 | 5.99 | 3.22 | 2.77 | 203 (25/178) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN3 | team_total | 0.574 | 0.655 | 0.639 | 66 | 35 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN4 | team_total | 0.355 | 0.425 | 0.411 | 43 | 58 | no | +0.047 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-8 | game_total | 0.299 | 0.230 | 0.243 | 24 | 78 | yes | +0.046 | OK |
| KXNHLTOTAL-26NOV10MINMTL-5 | game_total | 0.744 | 0.805 | 0.794 | 81 | 20 | no | +0.045 | OK |
| KXNHLTOTAL-26NOV10NJWPG-7 | game_total | 0.439 | 0.505 | 0.492 | 51 | 50 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ5 | team_total | 0.241 | 0.180 | 0.191 | 19 | 83 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ6 | team_total | 0.113 | 0.065 | 0.073 | 7 | 94 | yes | +0.038 | OK |
| KXNHLTOTAL-26NOV10MINMTL-6 | game_total | 0.525 | 0.585 | 0.573 | 59 | 42 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-9 | game_total | 0.218 | 0.165 | 0.175 | 17 | 84 | yes | +0.038 | OK |
| KXNHLTOTAL-26NOV10NJWPG-5 | game_total | 0.764 | 0.815 | 0.806 | 82 | 19 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-WSH2 | game_spread | 0.339 | 0.285 | 0.295 | 29 | 72 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH6 | team_total | 0.141 | 0.095 | 0.103 | 10 | 91 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH4 | team_total | 0.470 | 0.415 | 0.426 | 42 | 59 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET3 | team_total | 0.490 | 0.545 | 0.534 | 55 | 46 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-10 | game_total | 0.107 | 0.065 | 0.072 | 7 | 94 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MIN2 | game_spread | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN2 | team_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV10MINMTL-7 | game_total | 0.412 | 0.465 | 0.454 | 47 | 54 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MIN3 | game_spread | 0.159 | 0.205 | 0.195 | 21 | 80 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ4 | team_total | 0.426 | 0.370 | 0.381 | 38 | 64 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV10MINMTL-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.029 | OK |
| KXNHLGAME-26NOV10MINMTL-MIN | game_winner | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET4 | team_total | 0.276 | 0.325 | 0.315 | 33 | 68 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH3 | team_total | 0.524 | 0.575 | 0.565 | 58 | 43 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-OTT3 | game_spread | 0.151 | 0.195 | 0.185 | 20 | 81 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-6 | game_total | 0.605 | 0.555 | 0.565 | 56 | 45 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV10NJWPG-6 | game_total | 0.556 | 0.605 | 0.595 | 61 | 40 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-WSH3 | game_spread | 0.217 | 0.175 | 0.183 | 18 | 83 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-7 | game_total | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV10DETSTL-5 | game_total | 0.721 | 0.765 | 0.757 | 77 | 24 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN5 | team_total | 0.182 | 0.230 | 0.220 | 24 | 78 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH5 | team_total | 0.278 | 0.235 | 0.243 | 24 | 77 | yes | +0.025 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-10 | game_total | 0.120 | 0.085 | 0.091 | 9 | 92 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET2 | team_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH4 | team_total | 0.310 | 0.355 | 0.346 | 36 | 65 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-8 | game_total | 0.318 | 0.275 | 0.283 | 28 | 73 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV10NSHLA-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-9 | game_total | 0.234 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLTOTAL-26NOV10NJWPG-4 | game_total | 0.850 | 0.885 | 0.879 | 89 | 12 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH3 | team_total | 0.679 | 0.635 | 0.644 | 64 | 37 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV10NSHLA-6 | game_total | 0.522 | 0.565 | 0.557 | 57 | 44 | no | +0.020 | OK |
| KXNHLGAME-26NOV10WSHOTT-OTT | game_winner | 0.453 | 0.495 | 0.487 | 50 | 51 | no | +0.020 | OK |
| KXNHLGAME-26NOV10WSHOTT-WSH | game_winner | 0.547 | 0.505 | 0.513 | 51 | 50 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV10NSHLA-7 | game_total | 0.413 | 0.455 | 0.447 | 46 | 55 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-OTT2 | game_spread | 0.256 | 0.295 | 0.287 | 30 | 71 | no | +0.019 | OK |
| KXNHLGAME-26NOV10MINMTL-MTL | game_winner | 0.507 | 0.465 | 0.473 | 47 | 54 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ3 | team_total | 0.636 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-4 | game_total | 0.833 | 0.865 | 0.859 | 87 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ2 | team_total | 0.829 | 0.795 | 0.802 | 80 | 21 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-7 | game_total | 0.514 | 0.475 | 0.483 | 48 | 53 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET5 | team_total | 0.127 | 0.155 | 0.149 | 16 | 85 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-4 | game_total | 0.817 | 0.845 | 0.840 | 85 | 16 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-8 | game_total | 0.204 | 0.235 | 0.228 | 24 | 77 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10MINMTL-9 | game_total | 0.156 | 0.185 | 0.179 | 19 | 82 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MTL2 | game_spread | 0.287 | 0.255 | 0.261 | 26 | 75 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV10DETSTL-7 | game_total | 0.381 | 0.415 | 0.408 | 42 | 59 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV10DETSTL-DET3 | game_spread | 0.110 | 0.140 | 0.133 | 15 | 87 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10COLTOR-10 | game_total | 0.129 | 0.105 | 0.109 | 11 | 90 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4 | team_total | 0.431 | 0.465 | 0.458 | 47 | 54 | no | +0.012 | OK |
| KXNHLGAME-26NOV10FLACBJ-CBJ | game_winner | 0.509 | 0.475 | 0.482 | 48 | 53 | yes | +0.012 | OK |
| KXNHLGAME-26NOV10FLACBJ-FLA | game_winner | 0.491 | 0.525 | 0.518 | 53 | 48 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10MINMTL-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-WPG4 | team_total | 0.333 | 0.370 | 0.362 | 38 | 64 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH2 | team_total | 0.851 | 0.825 | 0.830 | 83 | 18 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-WPG2 | team_total | 0.768 | 0.800 | 0.794 | 81 | 21 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV10DETSTL-6 | game_total | 0.492 | 0.525 | 0.518 | 53 | 48 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-5 | game_total | 0.802 | 0.770 | 0.777 | 78 | 24 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA6 | team_total | 0.106 | 0.085 | 0.089 | 9 | 92 | yes | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH2 | game_spread | 0.217 | 0.250 | 0.243 | 26 | 76 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH2 | team_total | 0.758 | 0.790 | 0.784 | 80 | 22 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-4 | game_total | 0.878 | 0.850 | 0.856 | 86 | 16 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-6 | game_total | 0.626 | 0.595 | 0.601 | 60 | 41 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV10COLTOR-8 | game_total | 0.344 | 0.315 | 0.321 | 32 | 69 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV10NSHLA-8 | game_total | 0.228 | 0.255 | 0.249 | 26 | 75 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT2 | team_total | 0.811 | 0.835 | 0.830 | 84 | 17 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ5 | team_total | 0.238 | 0.265 | 0.259 | 27 | 74 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV10DETSTL-3 | game_total | 0.950 | 0.970 | 0.967 | 98 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.153 | 0.180 | 0.174 | 19 | 83 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV10MINMTL-8 | game_total | 0.230 | 0.260 | 0.254 | 27 | 75 | no | +0.007 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ TOR | 0.400 | 0.434 | 0.164 | 0.210 | 6.77 | 6.70 | 0.988/0.979 | KXNHLGAME-26NOV10COLTOR-COL -0.034 |
| MIN @ MTL | 0.507 | 0.516 | 0.182 | 0.216 | 5.97 | 6.55 | 0.983/0.991 | KXNHLTOTAL-26NOV10MINMTL-7 +0.099 |
| WSH @ OTT | 0.453 | 0.536 | 0.164 | 0.209 | 6.62 | 6.50 | 1.071/0.961 | KXNHLSPREAD-26NOV10WSHOTT-WSH2 -0.084 |
| NJD @ WPG | 0.429 | 0.484 | 0.173 | 0.218 | 6.15 | 6.18 | 0.996/0.983 | KXNHLSPREAD-26NOV10NJWPG-NJ2 -0.058 |
| FLA @ CBJ | 0.509 | 0.567 | 0.167 | 0.218 | 6.48 | 6.35 | 1.008/1.015 | KXNHLGAME-26NOV10FLACBJ-CBJ +0.057 |
| DET @ STL | 0.595 | 0.595 | 0.175 | 0.217 | 5.80 | 6.11 | 0.977/0.994 | KXNHLTOTAL-26NOV10DETSTL-7 +0.059 |
| NSH @ LAK | 0.571 | 0.581 | 0.179 | 0.216 | 5.99 | 6.18 | 0.987/1.000 | KXNHLTOTAL-26NOV10NSHLA-7 +0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 11c · p 0.167 (adj 0.1515) · $5.22 · thesis TOR:OFFENSE_4PLUS
- Dakota Joshua: 1+ goals YES @ 11c · p 0.1513 (adj 0.1397) · $3.53 · thesis TOR:OFFENSE_4PLUS
- Brandon Duhaime: 1+ goals YES @ 8c · p 0.108 (adj 0.0998) · $2.2 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 19c · p 0.2324 (adj 0.2205) · $3.43 · thesis TOR:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 54c · p 0.6264 (adj 0.6036) · $12.22 · thesis MIN:SUPPRESSED
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1351 (adj 0.1226) · $4.15 · thesis MIN:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 11c · p 0.1586 (adj 0.1452) · $4.39 · thesis MTL:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 16c · p 0.2129 (adj 0.1984) · $4.72 · thesis MTL:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2291 (adj 0.2106) · $6.9 · thesis WSH:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 15c · p 0.2088 (adj 0.1929) · $5.49 · thesis OTT:OFFENSE_4PLUS
- Fabian Zetterlund: 1+ assists YES @ 22c · p 0.3021 (adj 0.2586) · $3.95 · thesis OTT:OFFENSE_4PLUS
- Jordan Spence: 1+ goals YES @ 6c · p 0.0876 (adj 0.0794) · $2.14 · thesis OTT:OFFENSE_4PLUS
- Tyrel Bauer: 1+ goals NO @ 94c · p 0.9712 (adj 0.9621) · $12.22 · thesis DIFFUSE
- Jack Hughes: 1+ goals NO @ 59c · p 0.659 (adj 0.6393) · $12.22 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 13c · p 0.1621 (adj 0.1528) · $2.56 · thesis NJD:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 10c · p 0.1268 (adj 0.1188) · $2.03 · thesis NJD:OFFENSE_4PLUS
- Mathieu Olivier: 2+ goals YES @ 1c · p 0.0343 (adj 0.0307) · $2.01 · thesis CBJ:WINS_BY_2PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.2294 (adj 0.2083) · $5.75 · thesis CBJ:OFFENSE_4PLUS
- Dmitri Voronkov: 1+ goals YES @ 14c · p 0.1851 (adj 0.1726) · $4.07 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 24c · p 0.2974 (adj 0.2818) · $5.79 · thesis CBJ:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1692 (adj 0.1581) · $3.3 · thesis STL:OFFENSE_4PLUS
- Cam Fowler: 1+ goals NO @ 92c · p 0.9468 (adj 0.9388) · $12.22 · thesis STL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 26c · p 0.3011 (adj 0.2896) · $3.05 · thesis STL:OFFENSE_4PLUS
- Philip Broberg: 1+ assists YES @ 38c · p 0.4426 (adj 0.4088) · $2.23 · thesis STL:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0773 (adj 0.0692) · $2.28 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ goals NO @ 62c · p 0.687 (adj 0.669) · $12.22 · thesis LAK:SUPPRESSED
- Scott Laughton: 1+ goals YES @ 11c · p 0.1438 (adj 0.1341) · $2.75 · thesis LAK:WINS_BY_2PLUS
- Steven Stamkos: 1+ goals NO @ 65c · p 0.6964 (adj 0.6823) · $6.94 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**COL @ TOR** · priced 165/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 33.11, exp saves 28.15 (sd 7.61), pull risk 0.086
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.65, exp saves 23.18 (sd 6.45), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Tavares: 1+ assists | 0.296 | 0.405 | 42/61 | +0.077 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.510 | 0.600 | 61/41 | +0.063 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.360 | 0.435 | 44/57 | +0.052 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.235 | 25/78 | +0.046 | STANDARD |
| Cale Makar: 1+ points | 0.584 | 0.650 | 66/36 | +0.040 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.705 | 0.770 | 78/24 | +0.043 | STANDARD |

**MIN @ MTL** · priced 173/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 29.25, exp saves 25.31 (sd 6.87), pull risk 0.066
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.98, exp saves 23.33 (sd 6.48), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.276 | 0.395 | 41/62 | +0.087 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.417 | 0.530 | 54/48 | +0.086 | STANDARD |
| Quinn Hughes: 1+ assists | 0.557 | 0.665 | 67/34 | +0.087 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.632 | 0.735 | 74/27 | +0.084 | STANDARD |
| Matt Boldy: 1+ assists | 0.400 | 0.500 | 51/51 | +0.072 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.374 | 0.465 | 47/54 | +0.069 | STANDARD |

**WSH @ OTT** · priced 169/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 25.76, exp saves 22.31 (sd 6.23), pull risk 0.063
- WSH net: Logan Thompson (PROJECTED) exp shots 28.22, exp saves 24.24 (sd 6.62), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ points | 0.352 | 0.230 | 25/79 | +0.089 | STANDARD |
| Fabian Zetterlund: 1+ points | 0.468 | 0.375 | 39/64 | +0.061 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.302 | 0.215 | 22/79 | +0.070 | STANDARD |
| Jordan Spence: 1+ assists | 0.290 | 0.205 | 22/81 | +0.058 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.288 | 0.205 | 22/81 | +0.056 | STANDARD |
| Tim Stutzle: 1+ assists | 0.454 | 0.530 | 54/48 | +0.049 | STANDARD |

**NJD @ WPG** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Nico Daws (CONFIRMED) exp shots 29.59, exp saves 25.53 (sd 6.78), pull risk 0.06
- NJD net: Jake Allen (CONFIRMED) exp shots 26.24, exp saves 22.71 (sd 6.36), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.249 | 0.390 | 40/62 | +0.114 | STANDARD |
| Jack Hughes: 1+ assists | 0.419 | 0.550 | 56/46 | +0.104 | STANDARD |
| Josh Morrissey: 1+ assists | 0.308 | 0.435 | 45/58 | +0.095 | STANDARD |
| Josh Morrissey: 1+ points | 0.384 | 0.500 | 51/51 | +0.089 | STANDARD |
| Jack Hughes: 1+ points | 0.620 | 0.725 | 73/28 | +0.086 | STANDARD |
| Luke Evangelista: 1+ assists | 0.257 | 0.355 | 36/65 | +0.077 | STANDARD |

**FLA @ CBJ** · priced 164/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.28, exp saves 23.77 (sd 6.31), pull risk 0.051
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.0, exp saves 23.08 (sd 6.48), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mathieu Olivier: 1+ points | 0.436 | 0.315 | 32/69 | +0.101 | STANDARD |
| Cole Sillinger: 1+ points | 0.438 | 0.330 | 35/69 | +0.072 | STANDARD |
| Sam Reinhart: 1+ points | 0.504 | 0.595 | 61/42 | +0.058 | STANDARD |
| Charlie Coyle: 1+ points | 0.584 | 0.495 | 50/51 | +0.066 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.229 | 0.145 | 15/86 | +0.070 | STANDARD |
| Cole Sillinger: 1+ assists | 0.304 | 0.220 | 23/79 | +0.061 | STANDARD |

**DET @ STL** · priced 170/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.84, exp saves 24.4 (sd 6.5), pull risk 0.047
- DET net: John Gibson (CONFIRMED) exp shots 26.38, exp saves 22.57 (sd 6.39), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Barron: 1+ assists | 0.251 | 0.105 | 19/98 | +0.050 | STANDARD |
| J.T. Compher: 1+ assists | 0.219 | 0.120 | 22/98 | -0.013 | STANDARD |
| Justin Barron: 1+ points | 0.314 | 0.215 | 24/81 | +0.061 | STANDARD |
| Philip Broberg: 1+ assists | 0.443 | 0.375 | 38/63 | +0.046 | STANDARD |
| Lucas Raymond: 1+ points | 0.523 | 0.590 | 60/42 | +0.040 | STANDARD |
| Robert Thomas: 1+ assists | 0.445 | 0.510 | 52/50 | +0.037 | STANDARD |

**NSH @ LAK** · priced 144/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.59, exp saves 23.28 (sd 6.31), pull risk 0.05
- NSH net: Juuse Saros (PROJECTED) exp shots 29.66, exp saves 25.48 (sd 6.87), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 1+ assists | 0.439 | 0.545 | 55/46 | +0.084 | STANDARD |
| Artemi Panarin: 2+ points | 0.250 | 0.350 | 36/66 | +0.074 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.222 | 0.315 | 33/70 | +0.063 | STANDARD |
| Artemi Panarin: 1+ points | 0.612 | 0.700 | 71/31 | +0.063 | STANDARD |
| Roman Josi: 1+ assists | 0.442 | 0.530 | 54/48 | +0.060 | STANDARD |
| Steven Stamkos: 1+ points | 0.532 | 0.615 | 62/39 | +0.061 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
