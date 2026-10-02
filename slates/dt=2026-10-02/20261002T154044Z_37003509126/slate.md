# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T15:40:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3198 · contracts joined: 884 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 759, 'OK': 78, 'NO_EDGE': 47}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 125, 'game_early_goal': 5, 'first_goal': 174, 'game_winner': 10, 'player_goals': 174, 'game_overtime': 5, 'player_points': 155, 'game_spread': 20, 'team_total': 50, 'game_total': 45, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 2026-10-02T22:30:00Z | T-6h | 0.563 | 0.437 | 0.174 | 5.97 | 3.18 | 2.79 | 171 (25/146) | PROBABLE/PROJECTED |
| WSH @ CAR | 2026-10-02T23:00:00Z | T-6h | 0.536 | 0.464 | 0.182 | 5.79 | 3.01 | 2.78 | 186 (25/161) | PROBABLE/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-6h | 0.493 | 0.507 | 0.182 | 5.78 | 2.87 | 2.91 | 174 (25/149) | PROJECTED/PROJECTED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-6h | 0.538 | 0.462 | 0.185 | 5.98 | 3.11 | 2.87 | 172 (25/147) | PROJECTED/PROJECTED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-6h | 0.596 | 0.404 | 0.172 | 6.42 | 3.51 | 2.91 | 181 (25/156) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.538 | 0.635 | 0.616 | 64 | 37 | no | +0.075 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.462 | 0.375 | 0.392 | 38 | 63 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.310 | 0.395 | 0.377 | 40 | 61 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.190 | 0.265 | 0.249 | 27 | 74 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.330 | 0.405 | 0.390 | 41 | 60 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.812 | 0.875 | 0.864 | 88 | 13 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.493 | 0.565 | 0.551 | 57 | 44 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.586 | 0.660 | 0.646 | 67 | 35 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.607 | 0.685 | 0.670 | 70 | 33 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.367 | 0.440 | 0.425 | 45 | 57 | no | +0.046 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.239 | 0.305 | 0.291 | 31 | 70 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.390 | 0.455 | 0.442 | 46 | 55 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.381 | 0.445 | 0.432 | 45 | 56 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.206 | 0.270 | 0.256 | 28 | 74 | no | +0.040 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.404 | 0.345 | 0.357 | 35 | 66 | yes | +0.038 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.720 | 0.780 | 0.769 | 79 | 23 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.248 | 0.195 | 0.205 | 20 | 81 | yes | +0.036 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.181 | 0.235 | 0.223 | 24 | 77 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.283 | 0.335 | 0.324 | 34 | 67 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.206 | 0.260 | 0.249 | 27 | 75 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.188 | 0.245 | 0.233 | 26 | 77 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.718 | 0.765 | 0.756 | 77 | 24 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.688 | 0.740 | 0.730 | 75 | 27 | no | +0.029 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.596 | 0.645 | 0.635 | 65 | 36 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.558 | 0.605 | 0.596 | 61 | 40 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.142 | 0.105 | 0.112 | 11 | 90 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.489 | 0.540 | 0.530 | 55 | 47 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.137 | 0.180 | 0.171 | 19 | 83 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.311 | 0.355 | 0.346 | 36 | 65 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.381 | 0.425 | 0.416 | 43 | 58 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.167 | 0.205 | 0.197 | 21 | 80 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.481 | 0.530 | 0.520 | 54 | 48 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.336 | 0.290 | 0.299 | 30 | 72 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.799 | 0.845 | 0.837 | 86 | 17 | no | +0.021 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.524 | 0.565 | 0.557 | 57 | 44 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.555 | 0.510 | 0.519 | 52 | 50 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.813 | 0.860 | 0.852 | 88 | 16 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT02NYRDET-NYR3 | game_spread | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.814 | 0.850 | 0.843 | 86 | 16 | no | +0.017 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.464 | 0.425 | 0.433 | 43 | 58 | yes | +0.017 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.536 | 0.575 | 0.567 | 58 | 43 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.269 | 0.305 | 0.298 | 31 | 70 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-10 | game_total | 0.059 | 0.085 | 0.079 | 9 | 92 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.794 | 0.830 | 0.823 | 84 | 18 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02NYRDET-5 | game_total | 0.742 | 0.775 | 0.769 | 78 | 23 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.203 | 0.235 | 0.228 | 24 | 77 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.216 | 0.185 | 0.191 | 19 | 82 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.775 | 0.815 | 0.807 | 83 | 20 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.089 | 0.120 | 0.113 | 13 | 89 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.860 | 0.890 | 0.885 | 90 | 12 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.746 | 0.775 | 0.769 | 78 | 23 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.141 | 0.170 | 0.164 | 18 | 84 | no | +0.010 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.507 | 0.475 | 0.481 | 48 | 53 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-NYR3 | team_total | 0.534 | 0.570 | 0.563 | 58 | 44 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.415 | 0.445 | 0.439 | 45 | 56 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.834 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.166 | 0.140 | 0.145 | 15 | 87 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-NYR4 | team_total | 0.318 | 0.350 | 0.343 | 36 | 66 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-10 | game_total | 0.059 | 0.075 | 0.071 | 8 | 93 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.486 | 0.515 | 0.509 | 52 | 49 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.952 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLGAME-26OCT02NYRDET-NYR | game_winner | 0.437 | 0.465 | 0.459 | 47 | 54 | no | +0.006 | OK |
| KXNHLGAME-26OCT02NYRDET-DET | game_winner | 0.563 | 0.535 | 0.541 | 54 | 47 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.598 | 0.625 | 0.620 | 63 | 38 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.290 | 0.315 | 0.310 | 32 | 69 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.136 | 0.155 | 0.151 | 16 | 85 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.122 | 0.105 | 0.108 | 11 | 90 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT02NYRDET-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.207 | 0.225 | 0.221 | 23 | 78 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.774 | 0.745 | 0.751 | 76 | 27 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-10 | game_total | 0.102 | 0.115 | 0.112 | 12 | 89 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA6 | team_total | 0.075 | 0.065 | 0.067 | 7 | 94 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT02NYRDET-DET2 | game_spread | 0.336 | 0.315 | 0.319 | 32 | 69 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-3 | game_total | 0.968 | 0.975 | 0.974 | 98 | 3 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT02NYRDET-NYR2 | game_spread | 0.228 | 0.245 | 0.242 | 25 | 76 |  | -0.001 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 0.563 | 0.542 | 0.174 | 0.212 | 5.97 | 6.12 | 0.998/0.983 | KXNHLTOTAL-26OCT02NYRDET-7 +0.032 |
| WSH @ CAR | 0.536 | 0.563 | 0.182 | 0.219 | 5.79 | 6.22 | 0.986/0.938 | KXNHLTOTAL-26OCT02WSHCAR-7 +0.074 |
| BOS @ WPG | 0.493 | 0.525 | 0.182 | 0.216 | 5.78 | 6.07 | 0.988/0.968 | KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 +0.061 |
| STL @ DAL | 0.538 | 0.546 | 0.185 | 0.220 | 5.98 | 6.13 | 0.986/0.993 | KXNHLTOTAL-26OCT02STLDAL-7 +0.032 |
| ANA @ VGK | 0.596 | 0.593 | 0.172 | 0.208 | 6.42 | 6.42 | 1.003/1.016 | KXNHLSPREAD-26OCT02ANAVGK-VGK3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Nate Danielson: 1+ goals YES @ 10c · p 0.1294 (adj 0.1208) · $2.87 · thesis DET:OFFENSE_4PLUS
- Sean Durzi: 1+ goals NO @ 91c · p 0.935 (adj 0.9275) · $11.96 · thesis NYR:SUPPRESSED
- Pavel Dorofeyev: 1+ assists NO @ 72c · p 0.8251 (adj 0.7503) · $10.67 · thesis NYR:SUPPRESSED
- J.T. Compher: 1+ goals YES @ 15c · p 0.1801 (adj 0.1701) · $2.38 · thesis DET:OFFENSE_4PLUS
- William Carrier: 1+ goals YES @ 8c · p 0.1206 (adj 0.108) · $4.19 · thesis CAR:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2242 (adj 0.2094) · $6.49 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 12c · p 0.1565 (adj 0.1474) · $4.27 · thesis WSH:OFFENSE_4PLUS
- Alex Tuch: 1+ assists NO @ 77c · p 0.8819 (adj 0.7994) · $15.09 · thesis WSH:SUPPRESSED
- Elias Lindholm: 1+ goals YES @ 18c · p 0.2314 (adj 0.2173) · $5.92 · thesis BOS:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1656 (adj 0.1567) · $3.84 · thesis WPG:OFFENSE_4PLUS
- Mark Scheifele: 1+ goals YES @ 28c · p 0.3306 (adj 0.3167) · $5.95 · thesis WPG:OFFENSE_4PLUS
- Cole Perfetti: 1+ goals NO @ 73c · p 0.7757 (adj 0.763) · $14.44 · thesis WPG:SUPPRESSED
- Miro Heiskanen: 1+ goals NO @ 85c · p 0.8933 (adj 0.8812) · $13.84 · thesis DAL:SUPPRESSED
- Dallas wins NO @ 37c · p 0.4591 (adj 0.4121) · $5.86 · thesis STL:WINS
- Jimmy Snuggerud: 1+ goals YES @ 25c · p 0.298 (adj 0.2848) · $4.18 · thesis STL:OFFENSE_4PLUS
- Mason McTavish: 1+ assists NO @ 77c · p 0.8801 (adj 0.7955) · $13.84 · thesis STL:SUPPRESSED
- Tim Washe: 1+ goals YES @ 8c · p 0.1134 (adj 0.1026) · $3.11 · thesis ANA:OFFENSE_4PLUS
- Mitch Marner: 1+ goals NO @ 68c · p 0.7361 (adj 0.7183) · $15.07 · thesis VGK:SUPPRESSED
- Alex Killorn: 1+ assists YES @ 23c · p 0.362 (adj 0.2632) · $4.05 · thesis ANA:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 6c · p 0.0828 (adj 0.0746) · $1.99 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ DET** · priced 114/120 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROBABLE) exp shots 25.06, exp saves 21.9 (sd 6.11), pull risk 0.055
- NYR net: Dylan Garand (PROJECTED) exp shots 28.53, exp saves 24.54 (sd 6.78), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Pavel Dorofeyev: 1+ assists | 0.175 | 0.290 | 30/72 | +0.091 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.406 | 0.510 | 52/50 | +0.077 | STANDARD |
| Gabe Perreault: 1+ assists | 0.300 | 0.235 | 25/78 | +0.036 | STANDARD |
| Alex DeBrincat: 1+ assists | 0.356 | 0.415 | 43/60 | +0.027 | STANDARD |
| Gabe Perreault: 1+ points | 0.439 | 0.385 | 40/63 | +0.022 | STANDARD |
| Viktor Arvidsson: 1+ assists | 0.273 | 0.320 | 34/70 | +0.012 | STANDARD |

**WSH @ CAR** · priced 133/135 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Brandon Bussi (PROBABLE) exp shots 23.54, exp saves 20.55 (sd 5.9), pull risk 0.057
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.12 (sd 7.12), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Tuch: 1+ assists | 0.118 | 0.245 | 26/77 | +0.100 | STANDARD |
| Sebastian Aho: 1+ assists | 0.329 | 0.455 | 47/56 | +0.093 | STANDARD |
| Sebastian Aho: 2+ points | 0.157 | 0.255 | 28/77 | +0.060 | STANDARD |
| Sebastian Aho: 1+ points | 0.512 | 0.605 | 63/42 | +0.050 | STANDARD |
| Alex Tuch: 1+ points | 0.337 | 0.425 | 45/60 | +0.046 | STANDARD |
| K'Andre Miller: 1+ assists | 0.356 | 0.280 | 31/75 | +0.031 | STANDARD |

**BOS @ WPG** · priced 123/123 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.1, exp saves 22.68 (sd 6.22), pull risk 0.056
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.24, exp saves 24.33 (sd 6.61), pull risk 0.058

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ assists | 0.160 | 0.300 | 32/72 | +0.106 | STANDARD |
| JJ Peterka: 1+ points | 0.346 | 0.485 | 50/53 | +0.107 | STANDARD |
| Elias Lindholm: 1+ points | 0.498 | 0.390 | 41/63 | +0.071 | STANDARD |
| Elias Lindholm: 1+ assists | 0.346 | 0.275 | 29/74 | +0.042 | STANDARD |
| Mark Scheifele: 2+ points | 0.286 | 0.220 | 28/84 | -0.009 | STANDARD |
| Morgan Geekie: 1+ assists | 0.342 | 0.285 | 30/73 | +0.027 | STANDARD |

**STL @ DAL** · priced 121/121 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.53, exp saves 21.43 (sd 5.95), pull risk 0.051
- STL net: Joel Hofer (PROJECTED) exp shots 26.73, exp saves 22.86 (sd 6.4), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.120 | 0.250 | 27/77 | +0.098 | STANDARD |
| Mason McTavish: 1+ points | 0.292 | 0.415 | 43/60 | +0.091 | STANDARD |
| Jason Robertson: 1+ points | 0.607 | 0.485 | 70/73 | -0.107 | STANDARD |
| Roope Hintz: 1+ assists | 0.292 | 0.410 | 43/61 | +0.081 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.401 | 0.515 | 53/50 | +0.081 | STANDARD |
| Miro Heiskanen: 1+ points | 0.482 | 0.595 | 62/43 | +0.071 | STANDARD |

**ANA @ VGK** · priced 128/130 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 28.77, exp saves 25.13 (sd 6.71), pull risk 0.055
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.59, exp saves 23.42 (sd 6.74), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ assists | 0.362 | 0.210 | 23/81 | +0.120 | STANDARD |
| Alex Killorn: 1+ points | 0.506 | 0.360 | 38/66 | +0.110 | STANDARD |
| Leo Carlsson: 1+ assists | 0.298 | 0.415 | 43/60 | +0.085 | STANDARD |
| Jack Eichel: 1+ points | 0.621 | 0.525 | 71/66 | -0.104 | STANDARD |
| Jackson LaCombe: 2+ points | 0.203 | 0.115 | 19/96 | +0.003 | STANDARD |
| Jack Eichel: 2+ points | 0.258 | 0.345 | 36/67 | +0.056 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
