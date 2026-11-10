# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-10T21:32:10Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 7 · markets on board: 3406 · contracts joined: 1578 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1403, 'NO_EDGE': 74, 'OK': 101}
families: {'period_winner': 63, 'period_spread': 42, 'period_total': 63, 'player_assists': 238, 'game_early_goal': 7, 'first_goal': 238, 'game_winner': 14, 'player_goals': 420, 'game_overtime': 7, 'player_points': 313, 'goalie_saves': 12, 'game_spread': 28, 'team_total': 70, 'game_total': 63}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ TOR | 2026-11-11T00:00:00Z | T-90m | 0.400 | 0.600 | 0.164 | 6.77 | 3.05 | 3.72 | 224 (25/199) | CONFIRMED/CONFIRMED |
| MIN @ MTL | 2026-11-11T00:00:00Z | T-90m | 0.507 | 0.493 | 0.182 | 5.97 | 3.01 | 2.96 | 231 (25/206) | CONFIRMED/CONFIRMED |
| WSH @ OTT | 2026-11-11T00:00:00Z | T-90m | 0.428 | 0.572 | 0.166 | 6.52 | 3.04 | 3.48 | 231 (25/206) | CONFIRMED/CONFIRMED |
| NJD @ WPG | 2026-11-11T00:00:00Z | T-90m | 0.429 | 0.571 | 0.173 | 6.15 | 2.86 | 3.29 | 220 (25/195) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-11-11T00:30:00Z | T-90m | 0.509 | 0.491 | 0.167 | 6.48 | 3.27 | 3.21 | 222 (25/197) | CONFIRMED/CONFIRMED |
| DET @ STL | 2026-11-11T01:00:00Z | T-3h | 0.595 | 0.405 | 0.175 | 5.80 | 3.19 | 2.61 | 230 (25/205) | CONFIRMED/CONFIRMED |
| NSH @ LAK | 2026-11-11T03:00:00Z | T-3h | 0.571 | 0.429 | 0.179 | 5.99 | 3.22 | 2.77 | 220 (25/195) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN3 | team_total | 0.574 | 0.655 | 0.639 | 66 | 35 | no | +0.060 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-WSH2 | game_spread | 0.352 | 0.285 | 0.298 | 29 | 72 | yes | +0.048 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN4 | team_total | 0.355 | 0.430 | 0.415 | 44 | 58 | no | +0.047 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-8 | game_total | 0.299 | 0.230 | 0.243 | 24 | 78 | yes | +0.046 | OK |
| KXNHLGAME-26NOV10WSHOTT-OTT | game_winner | 0.428 | 0.495 | 0.482 | 50 | 51 | no | +0.044 | OK |
| KXNHLGAME-26NOV10WSHOTT-WSH | game_winner | 0.572 | 0.505 | 0.518 | 51 | 50 | yes | +0.044 | OK |
| KXNHLTOTAL-26NOV10NJWPG-7 | game_total | 0.439 | 0.505 | 0.492 | 51 | 50 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ5 | team_total | 0.241 | 0.180 | 0.191 | 19 | 83 | yes | +0.040 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-OTT2 | game_spread | 0.235 | 0.295 | 0.282 | 30 | 71 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ4 | team_total | 0.426 | 0.365 | 0.377 | 37 | 64 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ6 | team_total | 0.113 | 0.065 | 0.073 | 7 | 94 | yes | +0.038 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-OTT3 | game_spread | 0.141 | 0.195 | 0.183 | 20 | 81 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV10MINMTL-6 | game_total | 0.525 | 0.585 | 0.573 | 59 | 42 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-9 | game_total | 0.218 | 0.165 | 0.175 | 17 | 84 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN5 | team_total | 0.182 | 0.235 | 0.224 | 24 | 77 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV10NJWPG-5 | game_total | 0.764 | 0.815 | 0.806 | 82 | 19 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH4 | team_total | 0.472 | 0.415 | 0.426 | 42 | 59 | yes | +0.035 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-WSH3 | game_spread | 0.225 | 0.175 | 0.184 | 18 | 83 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV10MINMTL-5 | game_total | 0.744 | 0.800 | 0.790 | 81 | 21 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH6 | team_total | 0.140 | 0.095 | 0.103 | 10 | 91 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET3 | team_total | 0.490 | 0.545 | 0.534 | 55 | 46 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-10 | game_total | 0.107 | 0.065 | 0.072 | 7 | 94 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MIN2 | game_spread | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN2 | team_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLTOTAL-26NOV10MINMTL-7 | game_total | 0.412 | 0.465 | 0.454 | 47 | 54 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MIN3 | game_spread | 0.159 | 0.205 | 0.195 | 21 | 80 | no | +0.030 | OK |
| KXNHLTOTAL-26NOV10MINMTL-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET4 | team_total | 0.276 | 0.325 | 0.315 | 33 | 68 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH3 | team_total | 0.524 | 0.575 | 0.565 | 58 | 43 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-6 | game_total | 0.605 | 0.555 | 0.565 | 56 | 45 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV10NJWPG-6 | game_total | 0.556 | 0.605 | 0.595 | 61 | 40 | no | +0.027 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-7 | game_total | 0.494 | 0.440 | 0.451 | 45 | 57 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV10DETSTL-5 | game_total | 0.721 | 0.765 | 0.757 | 77 | 24 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH3 | team_total | 0.681 | 0.635 | 0.645 | 64 | 37 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET2 | team_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT2 | team_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH4 | team_total | 0.310 | 0.355 | 0.346 | 36 | 65 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10NSHLA-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH5 | team_total | 0.277 | 0.235 | 0.243 | 24 | 77 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV10NJWPG-4 | game_total | 0.850 | 0.885 | 0.879 | 89 | 12 | no | +0.023 | OK |
| KXNHLGAME-26NOV10FLACBJ-CBJ | game_winner | 0.509 | 0.465 | 0.474 | 47 | 54 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT3 | team_total | 0.582 | 0.625 | 0.617 | 63 | 38 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT4 | team_total | 0.372 | 0.415 | 0.406 | 42 | 59 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-WPG4 | team_total | 0.333 | 0.375 | 0.366 | 38 | 63 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV10NSHLA-6 | game_total | 0.522 | 0.565 | 0.557 | 57 | 44 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH2 | game_spread | 0.217 | 0.255 | 0.247 | 26 | 75 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV10NSHLA-7 | game_total | 0.413 | 0.455 | 0.447 | 46 | 55 | no | +0.019 | OK |
| KXNHLGAME-26NOV10MINMTL-MIN | game_winner | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLGAME-26NOV10MINMTL-MTL | game_winner | 0.507 | 0.465 | 0.473 | 47 | 54 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ3 | team_total | 0.636 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-4 | game_total | 0.833 | 0.865 | 0.859 | 87 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT5 | team_total | 0.199 | 0.235 | 0.228 | 24 | 77 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ2 | team_total | 0.829 | 0.795 | 0.802 | 80 | 21 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV10MINMTL-8 | game_total | 0.230 | 0.265 | 0.258 | 27 | 74 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH2 | team_total | 0.854 | 0.825 | 0.831 | 83 | 18 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET5 | team_total | 0.127 | 0.155 | 0.149 | 16 | 85 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-4 | game_total | 0.817 | 0.845 | 0.840 | 85 | 16 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10MINMTL-9 | game_total | 0.156 | 0.190 | 0.183 | 20 | 82 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MTL2 | game_spread | 0.287 | 0.255 | 0.261 | 26 | 75 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV10DETSTL-7 | game_total | 0.381 | 0.415 | 0.408 | 42 | 59 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV10DETSTL-DET3 | game_spread | 0.110 | 0.140 | 0.133 | 15 | 87 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4 | team_total | 0.431 | 0.465 | 0.458 | 47 | 54 | no | +0.012 | OK |
| KXNHLGAME-26NOV10FLACBJ-FLA | game_winner | 0.491 | 0.525 | 0.518 | 53 | 48 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10MINMTL-3 | game_total | 0.956 | 0.980 | 0.977 | 99 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-8 | game_total | 0.305 | 0.275 | 0.281 | 28 | 73 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-WPG2 | team_total | 0.768 | 0.800 | 0.794 | 81 | 21 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV10DETSTL-6 | game_total | 0.492 | 0.525 | 0.518 | 53 | 48 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-5 | game_total | 0.802 | 0.770 | 0.777 | 78 | 24 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA6 | team_total | 0.106 | 0.085 | 0.089 | 9 | 92 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH2 | team_total | 0.758 | 0.790 | 0.784 | 80 | 22 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-4 | game_total | 0.878 | 0.855 | 0.860 | 86 | 15 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV10WSHOTT-9 | game_total | 0.221 | 0.195 | 0.200 | 20 | 81 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV10COLTOR-8 | game_total | 0.344 | 0.315 | 0.321 | 32 | 69 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ5 | team_total | 0.238 | 0.265 | 0.259 | 27 | 74 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV10COLTOR-9 | game_total | 0.250 | 0.225 | 0.230 | 23 | 78 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV10DETSTL-3 | game_total | 0.950 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.153 | 0.175 | 0.170 | 18 | 83 | no | +0.007 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-CBJ3 | game_spread | 0.186 | 0.165 | 0.169 | 17 | 84 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-CBJ2 | game_spread | 0.300 | 0.275 | 0.280 | 28 | 73 | yes | +0.006 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ TOR | 0.400 | 0.434 | 0.164 | 0.210 | 6.77 | 6.70 | 0.988/0.979 | KXNHLGAME-26NOV10COLTOR-COL -0.034 |
| MIN @ MTL | 0.507 | 0.516 | 0.182 | 0.216 | 5.97 | 6.55 | 0.983/0.991 | KXNHLTOTAL-26NOV10MINMTL-7 +0.099 |
| WSH @ OTT | 0.428 | 0.528 | 0.166 | 0.220 | 6.52 | 6.45 | 1.071/0.938 | KXNHLGAME-26NOV10WSHOTT-OTT +0.100 |
| NJD @ WPG | 0.429 | 0.484 | 0.173 | 0.218 | 6.15 | 6.18 | 0.996/0.983 | KXNHLSPREAD-26NOV10NJWPG-NJ2 -0.058 |
| FLA @ CBJ | 0.509 | 0.567 | 0.167 | 0.218 | 6.48 | 6.35 | 1.008/1.015 | KXNHLGAME-26NOV10FLACBJ-CBJ +0.057 |
| DET @ STL | 0.595 | 0.595 | 0.175 | 0.217 | 5.80 | 6.11 | 0.977/0.994 | KXNHLTOTAL-26NOV10DETSTL-7 +0.059 |
| NSH @ LAK | 0.571 | 0.581 | 0.179 | 0.216 | 5.99 | 6.18 | 0.987/1.000 | KXNHLTOTAL-26NOV10NSHLA-7 +0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 28 recommended · full analysis in card.md / packet.json `thesis_card`

- Teddy Blueger: 1+ goals YES @ 11c · p 0.167 (adj 0.1515) · $5.48 · thesis TOR:OFFENSE_4PLUS
- Dakota Joshua: 1+ goals YES @ 11c · p 0.1513 (adj 0.1397) · $3.7 · thesis TOR:OFFENSE_4PLUS
- Brandon Duhaime: 1+ goals YES @ 8c · p 0.108 (adj 0.0998) · $2.3 · thesis TOR:OFFENSE_4PLUS
- Easton Cowan: 1+ goals YES @ 19c · p 0.2324 (adj 0.2205) · $3.59 · thesis TOR:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1351 (adj 0.1226) · $4.38 · thesis MIN:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 11c · p 0.1586 (adj 0.1452) · $4.68 · thesis MTL:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 16c · p 0.2129 (adj 0.1984) · $5.03 · thesis MTL:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 53c · p 0.6264 (adj 0.5605) · $4.08 · thesis MIN:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 16c · p 0.2383 (adj 0.2175) · $8.45 · thesis WSH:OFFENSE_4PLUS
- Jordan Spence: 1+ goals YES @ 6c · p 0.086 (adj 0.0782) · $2.22 · thesis OTT:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.2033 (adj 0.19) · $3.69 · thesis OTT:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 17c · p 0.2056 (adj 0.1955) · $2.86 · thesis WSH:OFFENSE_4PLUS
- Tyrel Bauer: 1+ goals NO @ 94c · p 0.9712 (adj 0.9621) · $10.46 · thesis DIFFUSE
- Jack Hughes: 1+ goals NO @ 59c · p 0.659 (adj 0.6393) · $9.97 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 71c · p 0.7589 (adj 0.7454) · $9.26 · thesis NJD:SUPPRESSED
- Cody Glass: 1+ goals YES @ 13c · p 0.1621 (adj 0.1528) · $2.01 · thesis NJD:OFFENSE_4PLUS
- Mathieu Olivier: 2+ goals YES @ 1c · p 0.0343 (adj 0.0307) · $2.11 · thesis CBJ:WINS_BY_2PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.2294 (adj 0.2083) · $6.03 · thesis CBJ:OFFENSE_4PLUS
- Dmitri Voronkov: 1+ goals YES @ 14c · p 0.1851 (adj 0.1726) · $4.27 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 24c · p 0.2974 (adj 0.2818) · $6.07 · thesis CBJ:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 13c · p 0.1692 (adj 0.1581) · $3.52 · thesis STL:OFFENSE_4PLUS
- Cam Fowler: 1+ goals NO @ 92c · p 0.9468 (adj 0.9388) · $12.82 · thesis STL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 26c · p 0.3011 (adj 0.2896) · $3.41 · thesis STL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 58c · p 0.6405 (adj 0.6078) · $4.26 · thesis DET:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0773 (adj 0.0692) · $2.39 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ goals NO @ 62c · p 0.687 (adj 0.669) · $12.82 · thesis LAK:SUPPRESSED
- Scott Laughton: 1+ goals YES @ 11c · p 0.1438 (adj 0.1341) · $2.88 · thesis LAK:WINS_BY_2PLUS
- Steven Stamkos: 1+ goals NO @ 65c · p 0.6964 (adj 0.6823) · $7.28 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**COL @ TOR** · priced 165/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 33.12, exp saves 28.13 (sd 7.61), pull risk 0.083
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.66, exp saves 23.24 (sd 6.52), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Tavares: 1+ assists | 0.296 | 0.400 | 41/61 | +0.077 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.510 | 0.600 | 61/41 | +0.063 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.360 | 0.445 | 46/57 | +0.052 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.235 | 25/78 | +0.046 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.705 | 0.775 | 78/23 | +0.053 | STANDARD |
| Cale Makar: 1+ points | 0.584 | 0.650 | 66/36 | +0.040 | STANDARD |

**MIN @ MTL** · priced 173/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 29.26, exp saves 25.32 (sd 6.87), pull risk 0.066
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.99, exp saves 23.3 (sd 6.52), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.276 | 0.395 | 41/62 | +0.087 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.417 | 0.535 | 54/47 | +0.096 | STANDARD |
| Quinn Hughes: 1+ assists | 0.557 | 0.665 | 67/34 | +0.087 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.632 | 0.735 | 74/27 | +0.084 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.374 | 0.475 | 48/53 | +0.079 | STANDARD |
| Matt Boldy: 1+ assists | 0.400 | 0.500 | 51/51 | +0.072 | STANDARD |

**WSH @ OTT** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 25.77, exp saves 22.34 (sd 6.23), pull risk 0.058
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.23, exp saves 24.22 (sd 6.68), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Spence: 1+ points | 0.346 | 0.245 | 25/76 | +0.083 | STANDARD |
| Tim Stutzle: 1+ assists | 0.439 | 0.530 | 54/48 | +0.063 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.238 | 0.155 | 16/85 | +0.069 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.286 | 0.205 | 21/80 | +0.065 | STANDARD |
| Jordan Spence: 1+ assists | 0.285 | 0.205 | 21/80 | +0.063 | STANDARD |
| Jake Sanderson: 1+ assists | 0.390 | 0.465 | 47/54 | +0.053 | STANDARD |

**NJD @ WPG** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Nico Daws (CONFIRMED) exp shots 29.6, exp saves 25.53 (sd 6.77), pull risk 0.06
- NJD net: Jake Allen (CONFIRMED) exp shots 26.25, exp saves 22.73 (sd 6.35), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.249 | 0.395 | 40/61 | +0.124 | STANDARD |
| Josh Morrissey: 1+ assists | 0.308 | 0.440 | 45/57 | +0.105 | STANDARD |
| Jack Hughes: 1+ assists | 0.419 | 0.550 | 56/46 | +0.104 | STANDARD |
| Jack Hughes: 1+ points | 0.620 | 0.740 | 75/27 | +0.097 | STANDARD |
| Josh Morrissey: 1+ points | 0.384 | 0.500 | 51/51 | +0.089 | STANDARD |
| Jesper Bratt: 1+ assists | 0.411 | 0.510 | 52/50 | +0.072 | STANDARD |

**FLA @ CBJ** · priced 164/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.3, exp saves 23.74 (sd 6.36), pull risk 0.056
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.01, exp saves 23.09 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mathieu Olivier: 1+ points | 0.436 | 0.315 | 32/69 | +0.101 | STANDARD |
| Cole Sillinger: 1+ points | 0.438 | 0.335 | 35/68 | +0.072 | STANDARD |
| Sam Reinhart: 1+ points | 0.504 | 0.595 | 61/42 | +0.058 | STANDARD |
| Charlie Coyle: 1+ points | 0.584 | 0.495 | 50/51 | +0.066 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.229 | 0.145 | 15/86 | +0.070 | STANDARD |
| Seth Jones: 1+ points | 0.467 | 0.550 | 56/46 | +0.056 | STANDARD |

**DET @ STL** · priced 170/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.85, exp saves 24.43 (sd 6.49), pull risk 0.047
- DET net: John Gibson (CONFIRMED) exp shots 26.39, exp saves 22.57 (sd 6.41), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Barron: 1+ points | 0.314 | 0.210 | 24/82 | +0.061 | STANDARD |
| Justin Barron: 1+ assists | 0.251 | 0.150 | 16/86 | +0.081 | STANDARD |
| Philip Broberg: 1+ assists | 0.443 | 0.375 | 38/63 | +0.046 | STANDARD |
| Dalibor Dvorsky: 1+ assists | 0.202 | 0.135 | 18/91 | +0.012 | STANDARD |
| Lucas Raymond: 1+ points | 0.523 | 0.590 | 60/42 | +0.040 | STANDARD |
| Lucas Raymond: 1+ assists | 0.359 | 0.425 | 43/58 | +0.043 | STANDARD |

**NSH @ LAK** · priced 159/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.6, exp saves 23.25 (sd 6.29), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 29.67, exp saves 25.51 (sd 6.87), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ assists | 0.247 | 0.115 | 19/96 | +0.046 | STANDARD |
| Joel Edmundson: 1+ points | 0.305 | 0.185 | 20/83 | +0.093 | STANDARD |
| Artemi Panarin: 2+ points | 0.250 | 0.360 | 37/65 | +0.084 | STANDARD |
| Artemi Panarin: 1+ assists | 0.439 | 0.545 | 55/46 | +0.084 | STANDARD |
| Artemi Panarin: 1+ points | 0.612 | 0.705 | 71/30 | +0.073 | STANDARD |
| Mavrik Bourque: 1+ assists | 0.222 | 0.305 | 32/71 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
