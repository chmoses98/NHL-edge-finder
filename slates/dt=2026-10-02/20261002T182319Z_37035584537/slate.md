# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T18:23:19Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3204 · contracts joined: 890 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 765, 'OK': 85, 'NO_EDGE': 40}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 125, 'game_early_goal': 5, 'first_goal': 174, 'game_winner': 10, 'player_goals': 174, 'game_overtime': 5, 'player_points': 155, 'goalie_saves': 7, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 2026-10-02T22:30:00Z | T-3h | 0.563 | 0.437 | 0.174 | 5.97 | 3.18 | 2.79 | 173 (25/148) | PROBABLE/PROJECTED |
| WSH @ CAR | 2026-10-02T23:00:00Z | T-3h | 0.537 | 0.463 | 0.179 | 5.79 | 3.01 | 2.78 | 186 (25/161) | CONFIRMED/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-3h | 0.478 | 0.522 | 0.181 | 5.65 | 2.76 | 2.89 | 175 (25/150) | PROBABLE/CONFIRMED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-6h | 0.533 | 0.467 | 0.177 | 5.90 | 3.05 | 2.86 | 173 (25/148) | CONFIRMED/CONFIRMED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-6h | 0.596 | 0.404 | 0.172 | 6.42 | 3.51 | 2.91 | 183 (25/158) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.533 | 0.635 | 0.615 | 64 | 37 | no | +0.081 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.182 | 0.275 | 0.254 | 28 | 73 | no | +0.075 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.467 | 0.375 | 0.393 | 38 | 63 | yes | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.530 | 0.615 | 0.598 | 62 | 39 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.593 | 0.675 | 0.659 | 68 | 33 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.306 | 0.390 | 0.372 | 40 | 62 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.376 | 0.460 | 0.443 | 47 | 55 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.466 | 0.545 | 0.529 | 55 | 46 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.309 | 0.390 | 0.373 | 40 | 62 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.490 | 0.565 | 0.550 | 57 | 44 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.363 | 0.445 | 0.428 | 46 | 57 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.718 | 0.785 | 0.773 | 79 | 22 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.699 | 0.765 | 0.753 | 77 | 24 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.355 | 0.425 | 0.411 | 43 | 58 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.815 | 0.875 | 0.864 | 88 | 13 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.587 | 0.655 | 0.642 | 66 | 35 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.046 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.378 | 0.445 | 0.431 | 45 | 56 | no | +0.044 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.800 | 0.855 | 0.845 | 86 | 15 | no | +0.041 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.404 | 0.345 | 0.357 | 35 | 66 | yes | +0.038 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.596 | 0.655 | 0.643 | 66 | 35 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.554 | 0.495 | 0.507 | 50 | 51 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.804 | 0.855 | 0.846 | 86 | 15 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.184 | 0.235 | 0.224 | 24 | 77 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.146 | 0.195 | 0.184 | 20 | 81 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.185 | 0.235 | 0.224 | 24 | 77 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.205 | 0.255 | 0.244 | 26 | 75 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.757 | 0.810 | 0.800 | 82 | 20 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.514 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.189 | 0.245 | 0.233 | 26 | 77 | no | +0.028 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.260 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.522 | 0.475 | 0.484 | 48 | 53 | yes | +0.024 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.478 | 0.525 | 0.516 | 53 | 48 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.311 | 0.355 | 0.346 | 36 | 65 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.797 | 0.845 | 0.836 | 86 | 17 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.283 | 0.325 | 0.316 | 33 | 68 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.481 | 0.525 | 0.516 | 53 | 48 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.139 | 0.175 | 0.167 | 18 | 83 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.334 | 0.290 | 0.299 | 30 | 72 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.085 | 0.115 | 0.108 | 12 | 89 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.688 | 0.725 | 0.718 | 73 | 28 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT02NYRDET-NYR3 | game_spread | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.824 | 0.855 | 0.849 | 86 | 15 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.486 | 0.525 | 0.517 | 53 | 48 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.794 | 0.830 | 0.823 | 84 | 18 | no | +0.016 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.537 | 0.575 | 0.567 | 58 | 43 | no | +0.016 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.463 | 0.425 | 0.433 | 43 | 58 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.598 | 0.635 | 0.628 | 64 | 37 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.164 | 0.135 | 0.140 | 14 | 87 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.216 | 0.185 | 0.191 | 19 | 82 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.290 | 0.325 | 0.318 | 33 | 68 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.860 | 0.890 | 0.885 | 90 | 12 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-10 | game_total | 0.054 | 0.075 | 0.070 | 8 | 93 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-BOS2 | game_spread | 0.294 | 0.265 | 0.271 | 27 | 74 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.141 | 0.170 | 0.164 | 18 | 84 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT02NYRDET-6 | game_total | 0.524 | 0.555 | 0.549 | 56 | 45 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT02NYRDET-NYR2 | game_spread | 0.228 | 0.255 | 0.249 | 26 | 75 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.948 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-NYR3 | team_total | 0.534 | 0.565 | 0.559 | 57 | 44 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02NYRDET-4 | game_total | 0.834 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-WSH2 | team_total | 0.762 | 0.790 | 0.785 | 80 | 22 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-10 | game_total | 0.059 | 0.080 | 0.075 | 9 | 93 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG6 | team_total | 0.060 | 0.080 | 0.075 | 9 | 93 | no | +0.006 | OK |
| KXNHLGAME-26OCT02NYRDET-NYR | game_winner | 0.437 | 0.465 | 0.459 | 47 | 54 | no | +0.006 | OK |
| KXNHLGAME-26OCT02NYRDET-DET | game_winner | 0.563 | 0.535 | 0.541 | 54 | 47 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT02NYRDET-5 | game_total | 0.742 | 0.770 | 0.765 | 78 | 24 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.122 | 0.105 | 0.108 | 11 | 90 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.953 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL6 | team_total | 0.067 | 0.045 | 0.049 | 6 | 97 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR6 | team_total | 0.082 | 0.095 | 0.092 | 10 | 91 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-3 | game_total | 0.945 | 0.960 | 0.957 | 97 | 5 | no | +0.002 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 0.563 | 0.542 | 0.174 | 0.212 | 5.97 | 6.12 | 0.998/0.983 | KXNHLTOTAL-26OCT02NYRDET-7 +0.032 |
| WSH @ CAR | 0.537 | 0.563 | 0.179 | 0.214 | 5.79 | 6.22 | 0.984/0.938 | KXNHLTOTAL-26OCT02WSHCAR-7 +0.076 |
| BOS @ WPG | 0.478 | 0.512 | 0.181 | 0.221 | 5.65 | 6.06 | 0.995/0.955 | KXNHLTOTAL-26OCT02BOSWPG-7 +0.074 |
| STL @ DAL | 0.533 | 0.533 | 0.177 | 0.215 | 5.90 | 6.10 | 0.994/0.976 | KXNHLTOTAL-26OCT02STLDAL-7 +0.035 |
| ANA @ VGK | 0.596 | 0.593 | 0.172 | 0.208 | 6.42 | 6.42 | 1.003/1.016 | KXNHLSPREAD-26OCT02ANAVGK-VGK3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 18 recommended · full analysis in card.md / packet.json `thesis_card`

- J.T. Compher: 1+ goals YES @ 14c · p 0.1801 (adj 0.1688) · $5.33 · thesis DET:OFFENSE_4PLUS
- Nate Danielson: 1+ goals YES @ 10c · p 0.1294 (adj 0.1208) · $3.57 · thesis DET:OFFENSE_4PLUS
- William Carrier: 1+ goals YES @ 8c · p 0.1258 (adj 0.1131) · $6.28 · thesis CAR:OFFENSE_4PLUS
- Justin Sourdif: 1+ goals YES @ 10c · p 0.15 (adj 0.135) · $6.7 · thesis WSH:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2343 (adj 0.2195) · $8.08 · thesis WSH:OFFENSE_4PLUS
- Alex Tuch: 1+ assists NO @ 75c · p 0.8768 (adj 0.7911) · $18.96 · thesis WSH:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 9c · p 0.1446 (adj 0.121) · $5.45 · thesis BOS:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 18c · p 0.2306 (adj 0.2167) · $7.88 · thesis BOS:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 28c · p 0.3387 (adj 0.3228) · $9.53 · thesis WPG:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 72c · p 0.8359 (adj 0.7476) · $18.96 · thesis BOS:SUPPRESSED
- Pius Suter: 1+ goals YES @ 10c · p 0.1583 (adj 0.1425) · $8.6 · thesis STL:OFFENSE_4PLUS
- Jonatan Berggren: 1+ goals YES @ 9c · p 0.1258 (adj 0.1156) · $4.69 · thesis STL:OFFENSE_4PLUS
- Tyler Myers: 1+ goals YES @ 4c · p 0.0627 (adj 0.0558) · $2.79 · thesis DIFFUSE
- Mason McTavish: 1+ assists NO @ 74c · p 0.8743 (adj 0.7773) · $18.96 · thesis STL:SUPPRESSED
- Tim Washe: 1+ goals YES @ 7c · p 0.1137 (adj 0.1015) · $5.98 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.233 (adj 0.2185) · $7.68 · thesis ANA:OFFENSE_4PLUS
- Marc Gatcomb: 1+ goals YES @ 8c · p 0.1158 (adj 0.1043) · $4.26 · thesis VGK:OFFENSE_4PLUS
- Braeden Bowman: 1+ goals YES @ 15c · p 0.195 (adj 0.1825) · $6.3 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ DET** · priced 116/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 25.06, exp saves 21.89 (sd 6.11), pull risk 0.055
- NYR net: Dylan Garand (PROJECTED) exp shots 28.53, exp saves 24.54 (sd 6.78), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ assists | 0.175 | 0.280 | 30/74 | +0.072 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.406 | 0.500 | 51/51 | +0.067 | STANDARD |
| Gabe Perreault: 1+ assists | 0.300 | 0.225 | 23/78 | +0.057 | STANDARD |
| Gabe Perreault: 1+ points | 0.439 | 0.370 | 40/66 | +0.022 | STANDARD |
| Adam Fox: 2+ points | 0.156 | 0.100 | 19/99 | -0.044 | STANDARD |
| Alex DeBrincat: 1+ assists | 0.356 | 0.410 | 42/60 | +0.027 | STANDARD |

**WSH @ CAR** · priced 133/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Brandon Bussi (CONFIRMED) exp shots 23.54, exp saves 20.59 (sd 5.89), pull risk 0.054
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.05 (sd 7.09), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Tuch: 1+ assists | 0.123 | 0.255 | 26/75 | +0.114 | STANDARD |
| Sebastian Aho: 1+ assists | 0.334 | 0.445 | 47/58 | +0.069 | STANDARD |
| Boone Jenner: 1+ goals | 0.151 | 0.065 | 11/98 | +0.034 | STANDARD |
| Shayne Gostisbehere: 1+ points | 0.410 | 0.495 | 51/52 | +0.053 | STANDARD |
| Sebastian Aho: 1+ points | 0.518 | 0.600 | 62/42 | +0.045 | STANDARD |
| K'Andre Miller: 1+ assists | 0.352 | 0.270 | 29/75 | +0.047 | STANDARD |

**BOS @ WPG** · priced 124/124 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 26.1, exp saves 22.64 (sd 6.23), pull risk 0.056
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.23, exp saves 24.41 (sd 6.55), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ points | 0.349 | 0.495 | 51/52 | +0.114 | STANDARD |
| JJ Peterka: 1+ assists | 0.164 | 0.300 | 32/72 | +0.102 | STANDARD |
| Elias Lindholm: 1+ points | 0.498 | 0.395 | 42/63 | +0.061 | STANDARD |
| Casey Mittelstadt: 1+ goals | 0.182 | 0.085 | 16/99 | +0.013 | STANDARD |
| Marat Khusnutdinov: 1+ goals | 0.145 | 0.050 | 9/99 | +0.049 | STANDARD |
| Viggo Bjorck: 1+ goals | 0.188 | 0.105 | 20/99 | -0.023 | PRIOR_HEAVY |

**STL @ DAL** · priced 118/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.53, exp saves 21.4 (sd 6.0), pull risk 0.053
- STL net: Joel Hofer (CONFIRMED) exp shots 26.73, exp saves 22.91 (sd 6.37), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.126 | 0.275 | 29/74 | +0.121 | STANDARD |
| Mason McTavish: 1+ points | 0.300 | 0.430 | 44/58 | +0.103 | STANDARD |
| Miro Heiskanen: 1+ points | 0.472 | 0.595 | 61/42 | +0.091 | STANDARD |
| Roope Hintz: 1+ assists | 0.298 | 0.410 | 43/61 | +0.075 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.404 | 0.515 | 53/50 | +0.079 | STANDARD |
| Jason Robertson: 1+ assists | 0.377 | 0.485 | 50/53 | +0.076 | STANDARD |

**ANA @ VGK** · priced 130/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 28.77, exp saves 25.14 (sd 6.75), pull risk 0.055
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.58, exp saves 23.41 (sd 6.72), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Hart: 24+ saves | 0.593 | 0.280 | 51/95 | +0.066 |  |
| Alex Killorn: 1+ points | 0.516 | 0.350 | 36/66 | +0.140 | STANDARD |
| Alex Killorn: 1+ assists | 0.369 | 0.215 | 23/80 | +0.127 | STANDARD |
| Jack Eichel: 1+ assists | 0.452 | 0.550 | 57/47 | +0.061 | STANDARD |
| Leo Carlsson: 1+ assists | 0.299 | 0.395 | 41/62 | +0.065 | STANDARD |
| Jack Eichel: 2+ points | 0.258 | 0.345 | 36/67 | +0.056 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
