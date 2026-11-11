# NHL slate 2026-11-10 — RESEARCH_ONLY

generated 2026-11-11T00:14:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 7 · simulated (not started): 3 · markets on board: 3410 · contracts joined: 689 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 614, 'OK': 49, 'NO_EDGE': 26}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 110, 'game_early_goal': 3, 'first_goal': 100, 'game_winner': 6, 'player_goals': 172, 'game_overtime': 3, 'player_points': 149, 'goalie_saves': 5, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CBJ | 2026-11-11T00:30:00Z | T-10m | 0.509 | 0.491 | 0.167 | 6.48 | 3.27 | 3.21 | 222 (25/197) | CONFIRMED/CONFIRMED |
| DET @ STL | 2026-11-11T01:00:00Z | T-30m | 0.595 | 0.405 | 0.175 | 5.80 | 3.19 | 2.61 | 237 (25/212) | CONFIRMED/CONFIRMED |
| NSH @ LAK | 2026-11-11T03:00:00Z | T-90m | 0.571 | 0.429 | 0.179 | 5.99 | 3.22 | 2.77 | 230 (25/205) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26NOV10FLACBJ-8 | game_total | 0.299 | 0.235 | 0.247 | 24 | 77 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ5 | team_total | 0.241 | 0.185 | 0.195 | 19 | 82 | yes | +0.040 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-9 | game_total | 0.218 | 0.165 | 0.175 | 17 | 84 | yes | +0.038 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-7 | game_total | 0.494 | 0.435 | 0.447 | 44 | 57 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET3 | team_total | 0.490 | 0.545 | 0.534 | 55 | 46 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-10 | game_total | 0.107 | 0.065 | 0.072 | 7 | 94 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ4 | team_total | 0.426 | 0.375 | 0.385 | 38 | 63 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET4 | team_total | 0.276 | 0.330 | 0.319 | 34 | 68 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH3 | team_total | 0.524 | 0.575 | 0.565 | 58 | 43 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-6 | game_total | 0.605 | 0.555 | 0.565 | 56 | 45 | yes | +0.028 | OK |
| KXNHLTOTAL-26NOV10DETSTL-5 | game_total | 0.721 | 0.765 | 0.757 | 77 | 24 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET2 | team_total | 0.723 | 0.770 | 0.761 | 78 | 24 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH4 | team_total | 0.310 | 0.355 | 0.346 | 36 | 65 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV10NSHLA-5 | game_total | 0.744 | 0.785 | 0.777 | 79 | 22 | no | +0.024 | OK |
| KXNHLGAME-26NOV10FLACBJ-CBJ | game_winner | 0.509 | 0.465 | 0.474 | 47 | 54 | yes | +0.022 | OK |
| KXNHLSPREAD-26NOV10DETSTL-DET3 | game_spread | 0.110 | 0.145 | 0.137 | 15 | 86 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV10DETSTL-6 | game_total | 0.492 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV10NSHLA-6 | game_total | 0.522 | 0.565 | 0.557 | 57 | 44 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH2 | team_total | 0.758 | 0.795 | 0.788 | 80 | 21 | no | +0.020 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH2 | game_spread | 0.217 | 0.255 | 0.247 | 26 | 75 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV10NSHLA-7 | game_total | 0.413 | 0.455 | 0.447 | 46 | 55 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ3 | team_total | 0.636 | 0.595 | 0.603 | 60 | 41 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV10NSHLA-4 | game_total | 0.833 | 0.865 | 0.859 | 87 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ6 | team_total | 0.113 | 0.080 | 0.086 | 9 | 93 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH5 | team_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET5 | team_total | 0.127 | 0.160 | 0.153 | 17 | 85 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-4 | game_total | 0.817 | 0.850 | 0.844 | 86 | 16 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV10DETSTL-7 | game_total | 0.381 | 0.415 | 0.408 | 42 | 59 | no | +0.012 | OK |
| KXNHLGAME-26NOV10FLACBJ-FLA | game_winner | 0.491 | 0.525 | 0.518 | 53 | 48 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-5 | game_total | 0.802 | 0.775 | 0.781 | 78 | 23 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA6 | team_total | 0.106 | 0.085 | 0.089 | 9 | 92 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV10NSHLA-3 | game_total | 0.958 | 0.975 | 0.972 | 98 | 3 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV10NSHLA-NSH3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-4 | game_total | 0.878 | 0.855 | 0.860 | 86 | 15 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV10NSHLA-8 | game_total | 0.228 | 0.255 | 0.249 | 26 | 75 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-CBJ2 | team_total | 0.829 | 0.805 | 0.810 | 81 | 20 | yes | +0.008 | OK |
| KXNHLTOTAL-26NOV10DETSTL-3 | game_total | 0.950 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV10DETSTL-DET6 | team_total | 0.049 | 0.065 | 0.061 | 7 | 94 | no | +0.007 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-CBJ3 | game_spread | 0.186 | 0.165 | 0.169 | 17 | 84 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-CBJ2 | game_spread | 0.300 | 0.275 | 0.280 | 28 | 73 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-FLA3 | game_spread | 0.174 | 0.195 | 0.191 | 20 | 81 | no | +0.005 | OK |
| KXNHLSPREAD-26NOV10DETSTL-DET2 | game_spread | 0.203 | 0.225 | 0.220 | 23 | 78 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV10DETSTL-8 | game_total | 0.204 | 0.230 | 0.225 | 24 | 78 | no | +0.004 | OK |
| KXNHLGAME-26NOV10NSHLA-LA | game_winner | 0.571 | 0.545 | 0.550 | 55 | 46 | yes | +0.003 | OK |
| KXNHLGAME-26NOV10NSHLA-NSH | game_winner | 0.429 | 0.455 | 0.450 | 46 | 55 | no | +0.003 | OK |
| KXNHLSPREAD-26NOV10FLACBJ-FLA2 | game_spread | 0.283 | 0.305 | 0.301 | 31 | 70 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV10NSHLA-9 | game_total | 0.158 | 0.175 | 0.172 | 18 | 83 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV10DETSTL-9 | game_total | 0.140 | 0.155 | 0.152 | 16 | 85 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV10DETSTL-2 | game_total | 0.979 | 0.985 | 0.984 | 99 | 2 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV10FLACBJ-3 | game_total | 0.971 | 0.965 | 0.966 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV10DETSTL-STL2 | game_spread | 0.364 | 0.345 | 0.349 | 35 | 66 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26NOV10DETSTL-DET | game_winner | 0.405 | 0.425 | 0.421 | 43 | 58 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26NOV10DETSTL-STL | game_winner | 0.595 | 0.575 | 0.579 | 58 | 43 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA5 | team_total | 0.229 | 0.215 | 0.218 | 22 | 79 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA2 | game_spread | 0.342 | 0.325 | 0.328 | 33 | 68 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV10FLACBJ-2 | game_total | 0.987 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV10DETSTL-10 | game_total | 0.059 | 0.065 | 0.064 | 7 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-NSH6 | team_total | 0.062 | 0.065 | 0.064 | 7 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA2 | team_total | 0.826 | 0.840 | 0.837 | 85 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA4 | team_total | 0.411 | 0.395 | 0.398 | 40 | 61 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV10NSHLA-10 | game_total | 0.072 | 0.075 | 0.074 | 8 | 93 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10DETSTL-STL6 | team_total | 0.098 | 0.095 | 0.096 | 10 | 91 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA6 | team_total | 0.106 | 0.105 | 0.105 | 11 | 90 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10DETSTL-STL5 | team_total | 0.221 | 0.230 | 0.228 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV10DETSTL-STL3 | game_spread | 0.229 | 0.225 | 0.226 | 23 | 78 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV10NSHLA-LA3 | game_spread | 0.212 | 0.215 | 0.214 | 22 | 79 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10DETSTL-STL3 | team_total | 0.628 | 0.635 | 0.634 | 64 | 37 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10DETSTL-STL4 | team_total | 0.408 | 0.420 | 0.418 | 43 | 59 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA3 | team_total | 0.630 | 0.625 | 0.626 | 63 | 38 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10DETSTL-STL2 | team_total | 0.827 | 0.830 | 0.829 | 84 | 18 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA5 | team_total | 0.225 | 0.225 | 0.225 | 23 | 78 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA2 | team_total | 0.822 | 0.820 | 0.820 | 83 | 19 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10FLACBJ-FLA3 | team_total | 0.627 | 0.620 | 0.621 | 63 | 39 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV10NSHLA-LA4 | team_total | 0.414 | 0.415 | 0.415 | 42 | 59 |  | -0.021 | NO_EDGE |
| KXNHL1P-26NOV10FLACBJ-CBJ | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10FLACBJ-FLA | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV10FLACBJ-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10FLACBJ-CBJ2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV10FLACBJ-FLA2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CBJ | 0.509 | 0.567 | 0.167 | 0.218 | 6.48 | 6.35 | 1.008/1.015 | KXNHLGAME-26NOV10FLACBJ-CBJ +0.057 |
| DET @ STL | 0.595 | 0.595 | 0.175 | 0.217 | 5.80 | 6.11 | 0.977/0.994 | KXNHLTOTAL-26NOV10DETSTL-7 +0.059 |
| NSH @ LAK | 0.571 | 0.581 | 0.179 | 0.216 | 5.99 | 6.18 | 0.987/1.000 | KXNHLTOTAL-26NOV10NSHLA-7 +0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Mathieu Olivier: 1+ goals YES @ 15c · p 0.2294 (adj 0.2083) · $13.15 · thesis CBJ:OFFENSE_4PLUS
- Dmitri Voronkov: 1+ goals YES @ 14c · p 0.1851 (adj 0.1726) · $6.61 · thesis CBJ:OFFENSE_4PLUS
- Charlie Coyle: 1+ goals YES @ 24c · p 0.2974 (adj 0.2818) · $9.13 · thesis CBJ:OFFENSE_4PLUS
- Sam Reinhart: 1+ goals NO @ 65c · p 0.7146 (adj 0.696) · $20.0 · thesis FLA:SUPPRESSED
- Pius Suter: 1+ goals YES @ 13c · p 0.1692 (adj 0.1581) · $5.36 · thesis STL:OFFENSE_4PLUS
- Cam Fowler: 1+ goals NO @ 92c · p 0.9468 (adj 0.9388) · $20.0 · thesis STL:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 26c · p 0.3011 (adj 0.2896) · $5.04 · thesis STL:OFFENSE_4PLUS
- Justin Barron: 1+ assists YES @ 15c · p 0.2509 (adj 0.1715) · $2.27 · thesis STL:OFFENSE_4PLUS
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0773 (adj 0.0692) · $3.71 · thesis LAK:OFFENSE_4PLUS
- Artemi Panarin: 1+ goals NO @ 63c · p 0.687 (adj 0.6715) · $18.65 · thesis LAK:SUPPRESSED
- Steven Stamkos: 1+ goals NO @ 65c · p 0.6964 (adj 0.6811) · $9.34 · thesis NSH:SUPPRESSED
- Mavrik Bourque: 1+ assists NO @ 71c · p 0.7781 (adj 0.7366) · $8.92 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CBJ** · priced 164/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 27.3, exp saves 23.74 (sd 6.36), pull risk 0.056
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.01, exp saves 23.09 (sd 6.51), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mathieu Olivier: 1+ points | 0.436 | 0.315 | 32/69 | +0.101 | STANDARD |
| Cole Sillinger: 1+ points | 0.438 | 0.335 | 35/68 | +0.072 | STANDARD |
| Seth Jones: 1+ points | 0.467 | 0.560 | 57/45 | +0.066 | STANDARD |
| Sam Reinhart: 1+ points | 0.504 | 0.595 | 60/41 | +0.069 | STANDARD |
| Charlie Coyle: 1+ points | 0.584 | 0.495 | 50/51 | +0.066 | STANDARD |
| Matthew Tkachuk: 1+ points | 0.608 | 0.695 | 70/31 | +0.067 | STANDARD |

**DET @ STL** · priced 177/186 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- STL net: Joel Hofer (CONFIRMED) exp shots 27.85, exp saves 24.43 (sd 6.49), pull risk 0.047
- DET net: John Gibson (CONFIRMED) exp shots 26.39, exp saves 22.57 (sd 6.41), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Justin Barron: 1+ assists | 0.251 | 0.145 | 15/86 | +0.092 | STANDARD |
| Ben Chiarot: 1+ points | 0.261 | 0.170 | 21/87 | +0.039 | STANDARD |
| Justin Barron: 1+ points | 0.314 | 0.230 | 24/78 | +0.061 | STANDARD |
| Lucas Raymond: 1+ assists | 0.359 | 0.430 | 44/58 | +0.043 | STANDARD |
| Lucas Raymond: 1+ points | 0.523 | 0.590 | 60/42 | +0.040 | STANDARD |
| Robert Thomas: 1+ assists | 0.445 | 0.510 | 52/50 | +0.037 | STANDARD |

**NSH @ LAK** · priced 169/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Anton Forsberg (CONFIRMED) exp shots 26.6, exp saves 23.25 (sd 6.29), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 29.67, exp saves 25.51 (sd 6.87), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.305 | 0.195 | 21/82 | +0.083 | STANDARD |
| Artemi Panarin: 1+ assists | 0.439 | 0.545 | 55/46 | +0.084 | STANDARD |
| Artemi Panarin: 2+ points | 0.250 | 0.355 | 36/65 | +0.084 | STANDARD |
| Joel Edmundson: 1+ assists | 0.247 | 0.150 | 19/89 | +0.046 | STANDARD |
| Artemi Panarin: 1+ points | 0.612 | 0.705 | 71/30 | +0.073 | STANDARD |
| Roman Josi: 1+ assists | 0.442 | 0.530 | 54/48 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
