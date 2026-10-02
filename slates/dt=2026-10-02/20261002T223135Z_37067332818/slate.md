# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T22:31:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 4 · markets on board: 3276 · contracts joined: 717 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 617, 'OK': 80, 'NO_EDGE': 20}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 104, 'game_early_goal': 4, 'first_goal': 139, 'game_winner': 8, 'player_goals': 139, 'game_overtime': 4, 'player_points': 126, 'goalie_saves': 5, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WSH @ CAR | 2026-10-02T23:00:00Z | T-10m | 0.537 | 0.463 | 0.179 | 5.79 | 3.01 | 2.78 | 186 (25/161) | CONFIRMED/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-60m | 0.478 | 0.522 | 0.181 | 5.65 | 2.76 | 2.89 | 175 (25/150) | PROBABLE/CONFIRMED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-90m | 0.533 | 0.467 | 0.177 | 5.90 | 3.05 | 2.86 | 173 (25/148) | CONFIRMED/CONFIRMED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-3h | 0.589 | 0.411 | 0.169 | 6.46 | 3.52 | 2.94 | 183 (25/158) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.533 | 0.635 | 0.615 | 64 | 37 | no | +0.081 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.467 | 0.365 | 0.385 | 37 | 64 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.182 | 0.275 | 0.254 | 28 | 73 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.363 | 0.460 | 0.440 | 47 | 55 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.306 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.530 | 0.615 | 0.598 | 62 | 39 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.593 | 0.675 | 0.659 | 68 | 33 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.483 | 0.565 | 0.549 | 57 | 44 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.376 | 0.455 | 0.439 | 46 | 55 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.466 | 0.545 | 0.529 | 55 | 46 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.309 | 0.390 | 0.373 | 40 | 62 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.490 | 0.565 | 0.550 | 57 | 44 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.718 | 0.785 | 0.773 | 79 | 22 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.699 | 0.765 | 0.753 | 77 | 24 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.355 | 0.425 | 0.411 | 43 | 58 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.815 | 0.875 | 0.864 | 88 | 13 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.587 | 0.655 | 0.642 | 66 | 35 | no | +0.047 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.589 | 0.655 | 0.642 | 66 | 35 | no | +0.045 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.411 | 0.345 | 0.358 | 35 | 66 | yes | +0.045 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.378 | 0.445 | 0.431 | 45 | 56 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.797 | 0.855 | 0.845 | 86 | 15 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.800 | 0.855 | 0.845 | 86 | 15 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.189 | 0.250 | 0.237 | 26 | 76 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.804 | 0.855 | 0.846 | 86 | 15 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.242 | 0.300 | 0.288 | 31 | 71 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.184 | 0.235 | 0.224 | 24 | 77 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.146 | 0.195 | 0.184 | 20 | 81 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.185 | 0.235 | 0.224 | 24 | 77 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.205 | 0.255 | 0.244 | 26 | 75 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.757 | 0.810 | 0.800 | 82 | 20 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.372 | 0.425 | 0.414 | 43 | 58 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.514 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.554 | 0.505 | 0.515 | 51 | 50 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.289 | 0.335 | 0.325 | 34 | 67 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.260 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.478 | 0.525 | 0.516 | 53 | 48 | no | +0.024 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.522 | 0.475 | 0.484 | 48 | 53 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.311 | 0.355 | 0.346 | 36 | 65 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.139 | 0.180 | 0.171 | 19 | 83 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.863 | 0.895 | 0.889 | 90 | 11 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.334 | 0.290 | 0.299 | 30 | 72 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.085 | 0.115 | 0.108 | 12 | 89 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.606 | 0.645 | 0.637 | 65 | 36 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.143 | 0.180 | 0.172 | 19 | 83 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.876 | 0.905 | 0.900 | 91 | 10 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.824 | 0.855 | 0.849 | 86 | 15 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.217 | 0.185 | 0.191 | 19 | 82 | yes | +0.016 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.463 | 0.425 | 0.433 | 43 | 58 | yes | +0.016 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-3 | game_total | 0.945 | 0.965 | 0.962 | 97 | 4 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-10 | game_total | 0.054 | 0.075 | 0.070 | 8 | 93 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-BOS2 | game_spread | 0.294 | 0.265 | 0.271 | 27 | 74 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS2 | team_total | 0.779 | 0.805 | 0.800 | 81 | 20 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-3 | game_total | 0.971 | 0.985 | 0.983 | 99 | 2 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-WSH5 | team_total | 0.153 | 0.175 | 0.170 | 18 | 83 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.298 | 0.325 | 0.320 | 33 | 68 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.123 | 0.105 | 0.108 | 11 | 90 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG6 | team_total | 0.060 | 0.085 | 0.079 | 10 | 93 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-WSH2 | game_spread | 0.248 | 0.225 | 0.229 | 23 | 78 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS3 | team_total | 0.557 | 0.585 | 0.580 | 59 | 42 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.769 | 0.740 | 0.746 | 75 | 27 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.164 | 0.140 | 0.144 | 15 | 87 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.953 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS5 | team_total | 0.167 | 0.185 | 0.181 | 19 | 82 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL6 | team_total | 0.067 | 0.050 | 0.053 | 6 | 96 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR6 | team_total | 0.082 | 0.095 | 0.092 | 10 | 91 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA5 | team_total | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT02STLDAL-10 | game_total | 0.064 | 0.075 | 0.073 | 8 | 93 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-2 | game_total | 0.978 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WSH @ CAR | 0.537 | 0.563 | 0.179 | 0.214 | 5.79 | 6.22 | 0.984/0.938 | KXNHLTOTAL-26OCT02WSHCAR-7 +0.076 |
| BOS @ WPG | 0.478 | 0.512 | 0.181 | 0.221 | 5.65 | 6.06 | 0.995/0.955 | KXNHLTOTAL-26OCT02BOSWPG-7 +0.074 |
| STL @ DAL | 0.533 | 0.533 | 0.177 | 0.215 | 5.90 | 6.10 | 0.994/0.976 | KXNHLTOTAL-26OCT02STLDAL-7 +0.035 |
| ANA @ VGK | 0.589 | 0.597 | 0.169 | 0.212 | 6.46 | 6.41 | 1.003/1.015 | KXNHLTOTAL-26OCT02ANAVGK-6 -0.016 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Justin Sourdif: 1+ goals YES @ 10c · p 0.15 (adj 0.1362) · $7.49 · thesis WSH:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2343 (adj 0.2195) · $8.52 · thesis WSH:OFFENSE_4PLUS
- Alex Tuch: 1+ assists NO @ 75c · p 0.8768 (adj 0.7911) · $20.0 · thesis WSH:SUPPRESSED
- William Carrier: 1+ goals YES @ 9c · p 0.1258 (adj 0.1143) · $4.55 · thesis CAR:OFFENSE_4PLUS
- Marat Khusnutdinov: 1+ goals YES @ 9c · p 0.1446 (adj 0.1297) · $8.21 · thesis BOS:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 18c · p 0.2306 (adj 0.2167) · $7.63 · thesis BOS:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 29c · p 0.3387 (adj 0.3253) · $7.68 · thesis WPG:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 63c · p 0.6693 (adj 0.6582) · $7.96 · thesis BOS:SUPPRESSED
- Pius Suter: 1+ goals YES @ 11c · p 0.1583 (adj 0.145) · $6.42 · thesis STL:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7383 (adj 0.7225) · $18.26 · thesis DAL:SUPPRESSED
- Mason McTavish: 1+ assists NO @ 74c · p 0.8743 (adj 0.7773) · $18.26 · thesis STL:SUPPRESSED
- Dylan Holloway: 1+ goals YES @ 26c · p 0.3124 (adj 0.2981) · $7.07 · thesis STL:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 7c · p 0.1141 (adj 0.1018) · $6.11 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2329 (adj 0.2184) · $8.08 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 23c · p 0.3635 (adj 0.2702) · $6.47 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1093 (adj 0.1007) · $3.54 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WSH @ CAR** · priced 133/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Brandon Bussi (CONFIRMED) exp shots 23.54, exp saves 20.59 (sd 5.89), pull risk 0.054
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.05 (sd 7.09), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Tuch: 1+ assists | 0.123 | 0.255 | 26/75 | +0.114 | STANDARD |
| Sebastian Aho: 1+ assists | 0.334 | 0.445 | 45/56 | +0.089 | STANDARD |
| Sebastian Aho: 2+ points | 0.162 | 0.255 | 27/76 | +0.065 | STANDARD |
| Sebastian Aho: 1+ points | 0.518 | 0.605 | 62/41 | +0.055 | STANDARD |
| Alex Tuch: 1+ points | 0.342 | 0.425 | 44/59 | +0.051 | STANDARD |
| Logan Thompson: 26+ saves | 0.535 | 0.615 | 63/40 | +0.049 |  |

**BOS @ WPG** · priced 124/124 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 26.1, exp saves 22.64 (sd 6.23), pull risk 0.056
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.23, exp saves 24.41 (sd 6.55), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Stuart Skinner: 23+ saves | 0.503 | 0.295 | 53/94 | -0.045 |  |
| JJ Peterka: 1+ points | 0.349 | 0.505 | 53/52 | +0.114 | STANDARD |
| JJ Peterka: 1+ assists | 0.164 | 0.305 | 32/71 | +0.111 | STANDARD |
| Elias Lindholm: 1+ points | 0.498 | 0.400 | 41/61 | +0.071 | STANDARD |
| JJ Peterka: 2+ points | 0.068 | 0.165 | 18/85 | +0.073 | STANDARD |
| Morgan Geekie: 1+ points | 0.544 | 0.475 | 49/54 | +0.037 | STANDARD |

**STL @ DAL** · priced 118/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.53, exp saves 21.4 (sd 6.0), pull risk 0.053
- STL net: Joel Hofer (CONFIRMED) exp shots 26.73, exp saves 22.91 (sd 6.37), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.126 | 0.275 | 29/74 | +0.121 | STANDARD |
| Mason McTavish: 1+ points | 0.300 | 0.430 | 44/58 | +0.103 | STANDARD |
| Miro Heiskanen: 1+ points | 0.472 | 0.600 | 62/42 | +0.091 | STANDARD |
| Mikko Rantanen: 2+ points | 0.193 | 0.320 | 34/70 | +0.092 | STANDARD |
| Roope Hintz: 1+ assists | 0.298 | 0.410 | 42/60 | +0.085 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.404 | 0.515 | 52/49 | +0.089 | STANDARD |

**ANA @ VGK** · priced 130/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 28.77, exp saves 25.15 (sd 6.74), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.58, exp saves 23.43 (sd 6.66), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Hart: 24+ saves | 0.596 | 0.430 | 51/65 | +0.068 |  |
| Jack Eichel: 1+ points | 0.626 | 0.470 | 71/77 | -0.098 | STANDARD |
| Alex Killorn: 1+ points | 0.510 | 0.365 | 38/65 | +0.113 | STANDARD |
| Alex Killorn: 1+ assists | 0.363 | 0.220 | 23/79 | +0.121 | STANDARD |
| Lukas Dostal: 28+ saves | 0.262 | 0.385 | 49/72 | +0.004 |  |
| Leo Carlsson: 1+ assists | 0.293 | 0.405 | 41/60 | +0.090 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
