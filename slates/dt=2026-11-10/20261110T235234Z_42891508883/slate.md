# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-10T23:52:34Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 7 · markets on board: 3429 · contracts joined: 1601 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 1426, 'NO_EDGE': 72, 'OK': 103}
families: {'period_winner': 63, 'period_spread': 42, 'period_total': 63, 'player_assists': 242, 'game_early_goal': 7, 'first_goal': 239, 'game_winner': 14, 'player_goals': 421, 'game_overtime': 7, 'player_points': 330, 'goalie_saves': 12, 'game_spread': 28, 'team_total': 70, 'game_total': 63}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| COL @ TOR | 2026-11-11T00:00:00Z | T-<10m | 0.400 | 0.600 | 0.164 | 6.77 | 3.05 | 3.72 | 228 (25/203) | CONFIRMED/CONFIRMED |
| MIN @ MTL | 2026-11-11T00:00:00Z | T-<10m | 0.507 | 0.493 | 0.182 | 5.97 | 3.01 | 2.96 | 231 (25/206) | CONFIRMED/CONFIRMED |
| WSH @ OTT | 2026-11-11T00:00:00Z | T-<10m | 0.428 | 0.572 | 0.166 | 6.52 | 3.04 | 3.48 | 233 (25/208) | CONFIRMED/CONFIRMED |
| NJD @ WPG | 2026-11-11T00:00:00Z | T-<10m | 0.429 | 0.571 | 0.173 | 6.15 | 2.86 | 3.29 | 220 (25/195) | CONFIRMED/CONFIRMED |
| FLA @ CBJ | 2026-11-11T00:30:00Z | T-30m | 0.509 | 0.491 | 0.167 | 6.48 | 3.27 | 3.21 | 222 (25/197) | CONFIRMED/CONFIRMED |
| DET @ STL | 2026-11-11T01:00:00Z | T-60m | 0.595 | 0.405 | 0.175 | 5.80 | 3.19 | 2.61 | 237 (25/212) | CONFIRMED/CONFIRMED |
| NSH @ LAK | 2026-11-11T03:00:00Z | T-3h | 0.571 | 0.429 | 0.179 | 5.99 | 3.22 | 2.77 | 230 (25/205) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN3 | team_total | 0.574 | 0.655 | 0.639 | 66 | 35 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN4 | team_total | 0.355 | 0.435 | 0.419 | 44 | 57 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-8 | game_total | 0.299 | 0.235 | 0.247 | 24 | 77 | yes | +0.046 | OK |
| KXNHLGAME-26NOV10WSHOTT-WSH | game_winner | 0.572 | 0.505 | 0.518 | 51 | 50 | yes | +0.044 | OK |
| KXNHLTOTAL-26NOV10MINMTL-7 | game_total | 0.412 | 0.475 | 0.462 | 48 | 53 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ5 | team_total | 0.241 | 0.185 | 0.195 | 19 | 82 | yes | +0.040 | OK |
| KXNHLTOTAL-26NOV10MINMTL-6 | game_total | 0.525 | 0.585 | 0.573 | 59 | 42 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-9 | game_total | 0.218 | 0.165 | 0.175 | 17 | 84 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN5 | team_total | 0.182 | 0.235 | 0.224 | 24 | 77 | no | +0.036 | OK |
| KXNHLTOTAL-26NOV10NJWPG-5 | game_total | 0.764 | 0.815 | 0.806 | 82 | 19 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV10MINMTL-5 | game_total | 0.744 | 0.795 | 0.785 | 80 | 21 | no | +0.035 | OK |
| KXNHLGAME-26NOV10WSHOTT-OTT | game_winner | 0.428 | 0.485 | 0.474 | 49 | 52 | no | +0.034 | OK |
| KXNHLTOTAL-26NOV10NJWPG-7 | game_total | 0.439 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH6 | team_total | 0.140 | 0.095 | 0.103 | 10 | 91 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET3 | team_total | 0.490 | 0.545 | 0.534 | 55 | 46 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-10 | game_total | 0.107 | 0.065 | 0.072 | 7 | 94 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MIN2 | game_spread | 0.273 | 0.325 | 0.314 | 33 | 68 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV10MINMTL-MIN2 | team_total | 0.789 | 0.840 | 0.831 | 85 | 17 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-OTT2 | game_spread | 0.235 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV10MINMTL-MIN3 | game_spread | 0.159 | 0.205 | 0.195 | 21 | 80 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ4 | team_total | 0.426 | 0.370 | 0.381 | 38 | 64 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV10MINMTL-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.029 | OK |
| KXNHLGAME-26NOV10MINMTL-MIN | game_winner | 0.493 | 0.545 | 0.535 | 55 | 46 | no | +0.029 | OK |
| KXNHLGAME-26NOV10MINMTL-MTL | game_winner | 0.507 | 0.455 | 0.465 | 46 | 55 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET4 | team_total | 0.276 | 0.325 | 0.315 | 33 | 68 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-OTT3 | game_spread | 0.141 | 0.185 | 0.175 | 19 | 82 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH3 | team_total | 0.524 | 0.575 | 0.565 | 58 | 43 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ6 | team_total | 0.113 | 0.075 | 0.082 | 8 | 93 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-6 | game_total | 0.605 | 0.555 | 0.565 | 56 | 45 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV10NJWPG-6 | game_total | 0.556 | 0.605 | 0.595 | 61 | 40 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-WSH2 | game_spread | 0.352 | 0.305 | 0.314 | 31 | 70 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-7 | game_total | 0.494 | 0.445 | 0.455 | 45 | 56 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV10DETSTL-5 | game_total | 0.721 | 0.765 | 0.757 | 77 | 24 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET2 | team_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT2 | team_total | 0.796 | 0.835 | 0.828 | 84 | 17 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH4 | team_total | 0.310 | 0.355 | 0.346 | 36 | 65 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10NSHLA-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10MINMTL-9 | game_total | 0.156 | 0.195 | 0.187 | 20 | 81 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV10NJWPG-4 | game_total | 0.850 | 0.885 | 0.879 | 89 | 12 | no | +0.023 | OK |
| KXNHLGAME-26NOV10FLACBJ-CBJ | game_winner | 0.509 | 0.465 | 0.474 | 47 | 54 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV10DETSTL-DET3 | game_spread | 0.110 | 0.145 | 0.137 | 15 | 86 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT3 | team_total | 0.582 | 0.625 | 0.617 | 63 | 38 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT4 | team_total | 0.372 | 0.415 | 0.406 | 42 | 59 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ3 | team_total | 0.644 | 0.685 | 0.677 | 69 | 32 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV10DETSTL-6 | game_total | 0.492 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV10NSHLA-6 | game_total | 0.522 | 0.565 | 0.557 | 57 | 44 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH2 | game_spread | 0.217 | 0.255 | 0.247 | 26 | 75 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV10NSHLA-7 | game_total | 0.413 | 0.455 | 0.447 | 46 | 55 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ3 | team_total | 0.636 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-4 | game_total | 0.833 | 0.865 | 0.859 | 87 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-OTT5 | team_total | 0.199 | 0.235 | 0.228 | 24 | 77 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV10MINMTL-8 | game_total | 0.230 | 0.265 | 0.258 | 27 | 74 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH3 | team_total | 0.681 | 0.640 | 0.648 | 65 | 37 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH4 | team_total | 0.472 | 0.435 | 0.442 | 44 | 57 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH2 | team_total | 0.854 | 0.825 | 0.831 | 83 | 18 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET5 | team_total | 0.127 | 0.155 | 0.149 | 16 | 85 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-4 | game_total | 0.817 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV10WSHOTT-WSH3 | game_spread | 0.225 | 0.195 | 0.201 | 20 | 81 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV10WSHOTT-WSH5 | team_total | 0.277 | 0.240 | 0.247 | 25 | 77 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-7 | game_total | 0.381 | 0.415 | 0.408 | 42 | 59 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ4 | team_total | 0.431 | 0.465 | 0.458 | 47 | 54 | no | +0.012 | OK |
| KXNHLGAME-26NOV10FLACBJ-FLA | game_winner | 0.491 | 0.525 | 0.518 | 53 | 48 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10MINMTL-3 | game_total | 0.956 | 0.975 | 0.972 | 98 | 3 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10NJWPG-9 | game_total | 0.177 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-WPG4 | team_total | 0.333 | 0.365 | 0.358 | 37 | 64 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-5 | game_total | 0.802 | 0.775 | 0.781 | 78 | 23 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA6 | team_total | 0.106 | 0.085 | 0.089 | 9 | 92 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV10NSHLA-3 | game_total | 0.958 | 0.975 | 0.972 | 98 | 3 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH2 | team_total | 0.758 | 0.790 | 0.784 | 80 | 22 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-4 | game_total | 0.878 | 0.855 | 0.860 | 86 | 15 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV10COLTOR-7 | game_total | 0.543 | 0.575 | 0.569 | 58 | 43 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10COLTOR-COL4 | team_total | 0.523 | 0.555 | 0.549 | 56 | 45 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV10NSHLA-8 | game_total | 0.228 | 0.255 | 0.249 | 26 | 75 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10NJWPG-NJ5 | team_total | 0.238 | 0.270 | 0.263 | 28 | 74 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ2 | team_total | 0.829 | 0.805 | 0.810 | 81 | 20 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV10DETSTL-3 | game_total | 0.950 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.153 | 0.180 | 0.174 | 19 | 83 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET6 | team_total | 0.049 | 0.065 | 0.061 | 7 | 94 | no | +0.007 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-CBJ3 | game_spread | 0.186 | 0.165 | 0.169 | 17 | 84 | yes | +0.006 | OK |

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

- Teddy Blueger: 1+ goals YES @ 10c · p 0.167 (adj 0.149) · $6.15 · thesis TOR:OFFENSE_4PLUS
- Dakota Joshua: 1+ goals YES @ 11c · p 0.1513 (adj 0.1397) · $3.41 · thesis TOR:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ assists NO @ 40c · p 0.4902 (adj 0.4426) · $6.42 · thesis COL:SUPPRESSED
- Brandon Duhaime: 1+ goals YES @ 8c · p 0.108 (adj 0.0998) · $2.2 · thesis TOR:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 9c · p 0.1351 (adj 0.1226) · $4.1 · thesis MIN:OFFENSE_4PLUS
- Phillip Danault: 1+ goals YES @ 11c · p 0.1586 (adj 0.1452) · $4.48 · thesis MTL:OFFENSE_4PLUS
- Josh Anderson: 1+ goals YES @ 16c · p 0.2129 (adj 0.1984) · $4.84 · thesis MTL:OFFENSE_4PLUS
- Nick Suzuki: 1+ assists NO @ 53c · p 0.6058 (adj 0.5629) · $6.1 · thesis MTL:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2246 (adj 0.2097) · $5.15 · thesis WSH:OFFENSE_4PLUS
- Artem Zub: 1+ goals YES @ 4c · p 0.0587 (adj 0.0528) · $1.38 · thesis OTT:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 17c · p 0.2069 (adj 0.1964) · $2.83 · thesis WSH:OFFENSE_4PLUS
- Ridly Greig: 1+ goals YES @ 16c · p 0.1983 (adj 0.185) · $2.69 · thesis OTT:OFFENSE_4PLUS
- Tyrel Bauer: 1+ goals NO @ 94c · p 0.9712 (adj 0.9621) · $12.03 · thesis DIFFUSE
- Jack Hughes: 1+ goals NO @ 59c · p 0.659 (adj 0.6393) · $12.03 · thesis NJD:SUPPRESSED
- Amadeus Lombardi: 1+ goals YES @ 10c · p 0.1268 (adj 0.1188) · $2.0 · thesis NJD:OFFENSE_4PLUS
- Cody Glass: 1+ goals YES @ 13c · p 0.1621 (adj 0.1516) · $2.3 · thesis NJD:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 15c · p 0.2294 (adj 0.2083) · $7.91 · thesis CBJ:OFFENSE_4PLUS
- Dmitri Voronkov: 1+ goals YES @ 14c · p 0.1851 (adj 0.1726) · $3.98 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 24c · p 0.2974 (adj 0.2818) · $5.5 · thesis CBJ:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 65c · p 0.7146 (adj 0.696) · $12.03 · thesis FLA:SUPPRESSED
- Pius Suter: 1+ goals YES @ 13c · p 0.1692 (adj 0.1581) · $3.23 · thesis STL:OFFENSE_4PLUS
- Cam Fowler: 1+ goals NO @ 92c · p 0.9468 (adj 0.9388) · $12.03 · thesis STL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 26c · p 0.3011 (adj 0.2896) · $3.03 · thesis STL:OFFENSE_4PLUS
- Justin Barron: 1+ assists YES @ 15c · p 0.2509 (adj 0.1715) · $1.36 · thesis STL:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0773 (adj 0.0692) · $2.23 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ goals NO @ 63c · p 0.687 (adj 0.6715) · $11.26 · thesis LAK:SUPPRESSED
- Steven Stamkos: 1+ goals NO @ 65c · p 0.6964 (adj 0.6811) · $6.6 · thesis NSH:SUPPRESSED
- Alex Laferriere: 1+ goals YES @ 27c · p 0.3086 (adj 0.2977) · $2.74 · thesis LAK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**COL @ TOR** · priced 169/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 33.12, exp saves 28.13 (sd 7.61), pull risk 0.083
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.66, exp saves 23.24 (sd 6.52), pull risk 0.062

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Tavares: 1+ assists | 0.296 | 0.405 | 41/60 | +0.087 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.510 | 0.605 | 61/40 | +0.073 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.360 | 0.445 | 45/56 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.162 | 0.245 | 26/77 | +0.056 | STANDARD |
| Teddy Blueger: 1+ goals | 0.167 | 0.095 | 10/91 | +0.061 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.705 | 0.775 | 79/24 | +0.043 | STANDARD |

**MIN @ MTL** · priced 173/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jacob Fowler (CONFIRMED) exp shots 29.26, exp saves 25.32 (sd 6.87), pull risk 0.066
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 26.99, exp saves 23.3 (sd 6.52), pull risk 0.069

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Newhook: 1+ assists | 0.291 | 0.155 | 24/93 | +0.038 | STANDARD |
| Kirill Kaprizov: 2+ points | 0.276 | 0.400 | 41/61 | +0.097 | STANDARD |
| Bobby Brink: 1+ assists | 0.269 | 0.150 | 24/94 | +0.016 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.417 | 0.535 | 54/47 | +0.096 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.632 | 0.745 | 75/26 | +0.094 | STANDARD |
| Quinn Hughes: 1+ assists | 0.557 | 0.665 | 67/34 | +0.087 | STANDARD |

**WSH @ OTT** · priced 172/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Samuel Ersson (CONFIRMED) exp shots 25.77, exp saves 22.34 (sd 6.23), pull risk 0.058
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.23, exp saves 24.22 (sd 6.68), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Stutzle: 1+ assists | 0.439 | 0.535 | 55/48 | +0.064 | STANDARD |
| Alex Ovechkin: 1+ assists | 0.298 | 0.215 | 22/79 | +0.066 | STANDARD |
| Jordan Spence: 1+ points | 0.340 | 0.260 | 27/75 | +0.056 | STANDARD |
| Fabian Zetterlund: 1+ assists | 0.289 | 0.210 | 23/81 | +0.047 | STANDARD |
| Jake Sanderson: 1+ assists | 0.386 | 0.465 | 47/54 | +0.056 | STANDARD |
| Alex Ovechkin: 1+ points | 0.472 | 0.395 | 40/61 | +0.055 | STANDARD |

**NJD @ WPG** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Nico Daws (CONFIRMED) exp shots 29.6, exp saves 25.53 (sd 6.77), pull risk 0.06
- NJD net: Jake Allen (CONFIRMED) exp shots 26.25, exp saves 22.73 (sd 6.35), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.249 | 0.390 | 40/62 | +0.114 | STANDARD |
| Jack Hughes: 1+ assists | 0.419 | 0.550 | 56/46 | +0.104 | STANDARD |
| Josh Morrissey: 1+ points | 0.384 | 0.505 | 51/50 | +0.099 | STANDARD |
| Josh Morrissey: 1+ assists | 0.308 | 0.425 | 43/58 | +0.095 | STANDARD |
| Jack Hughes: 1+ points | 0.620 | 0.730 | 74/28 | +0.086 | STANDARD |
| Luke Evangelista: 1+ assists | 0.257 | 0.355 | 36/65 | +0.077 | STANDARD |

**FLA @ CBJ** · priced 164/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.3, exp saves 23.74 (sd 6.36), pull risk 0.056
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.01, exp saves 23.09 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mathieu Olivier: 1+ points | 0.436 | 0.315 | 32/69 | +0.101 | STANDARD |
| Cole Sillinger: 1+ points | 0.438 | 0.340 | 36/68 | +0.062 | STANDARD |
| Sam Reinhart: 1+ points | 0.504 | 0.600 | 61/41 | +0.069 | STANDARD |
| Charlie Coyle: 1+ points | 0.584 | 0.495 | 50/51 | +0.066 | STANDARD |
| Matthew Tkachuk: 1+ points | 0.608 | 0.695 | 70/31 | +0.067 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.229 | 0.145 | 15/86 | +0.070 | STANDARD |

**DET @ STL** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.85, exp saves 24.43 (sd 6.49), pull risk 0.047
- DET net: John Gibson (CONFIRMED) exp shots 26.39, exp saves 22.57 (sd 6.41), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Barron: 1+ assists | 0.251 | 0.145 | 15/86 | +0.092 | STANDARD |
| Justin Barron: 1+ points | 0.314 | 0.215 | 24/81 | +0.061 | STANDARD |
| Ben Chiarot: 1+ points | 0.261 | 0.185 | 21/84 | +0.039 | STANDARD |
| Lucas Raymond: 1+ points | 0.523 | 0.590 | 60/42 | +0.040 | STANDARD |
| Lucas Raymond: 1+ assists | 0.359 | 0.425 | 43/58 | +0.043 | STANDARD |
| Robert Thomas: 1+ assists | 0.445 | 0.510 | 52/50 | +0.037 | STANDARD |

**NSH @ LAK** · priced 169/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.6, exp saves 23.25 (sd 6.29), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 29.67, exp saves 25.51 (sd 6.87), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ assists | 0.247 | 0.135 | 19/92 | +0.046 | STANDARD |
| Joel Edmundson: 1+ points | 0.305 | 0.195 | 21/82 | +0.083 | STANDARD |
| Artemi Panarin: 1+ assists | 0.439 | 0.545 | 55/46 | +0.084 | STANDARD |
| Artemi Panarin: 2+ points | 0.250 | 0.355 | 36/65 | +0.084 | STANDARD |
| Artemi Panarin: 1+ points | 0.612 | 0.705 | 71/30 | +0.073 | STANDARD |
| Roman Josi: 1+ assists | 0.442 | 0.530 | 54/48 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
