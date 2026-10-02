# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T23:22:37Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 3 · markets on board: 3244 · contracts joined: 531 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 456, 'OK': 61, 'NO_EDGE': 14}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 76, 'game_early_goal': 3, 'first_goal': 103, 'game_winner': 6, 'player_goals': 103, 'game_overtime': 3, 'player_points': 92, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ WPG | 2026-10-03T00:00:00Z | T-30m | 0.478 | 0.522 | 0.181 | 5.65 | 2.76 | 2.89 | 175 (25/150) | PROBABLE/CONFIRMED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-90m | 0.533 | 0.467 | 0.177 | 5.90 | 3.05 | 2.86 | 173 (25/148) | CONFIRMED/CONFIRMED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-90m | 0.589 | 0.411 | 0.169 | 6.46 | 3.52 | 2.94 | 183 (25/158) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.533 | 0.635 | 0.615 | 64 | 37 | no | +0.081 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.467 | 0.365 | 0.385 | 37 | 64 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.306 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.182 | 0.265 | 0.247 | 27 | 74 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.530 | 0.615 | 0.598 | 62 | 39 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.593 | 0.675 | 0.659 | 68 | 33 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.483 | 0.565 | 0.549 | 57 | 44 | no | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.376 | 0.455 | 0.439 | 46 | 55 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.309 | 0.385 | 0.369 | 39 | 62 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.196 | 0.265 | 0.250 | 27 | 74 | no | +0.050 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.699 | 0.765 | 0.753 | 77 | 24 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.355 | 0.425 | 0.411 | 43 | 58 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.466 | 0.535 | 0.521 | 54 | 47 | no | +0.047 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.411 | 0.345 | 0.358 | 35 | 66 | yes | +0.045 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.589 | 0.655 | 0.642 | 66 | 35 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.242 | 0.305 | 0.292 | 31 | 70 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.689 | 0.745 | 0.734 | 75 | 26 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.804 | 0.855 | 0.846 | 86 | 15 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.289 | 0.345 | 0.333 | 35 | 66 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.146 | 0.195 | 0.184 | 20 | 81 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.185 | 0.235 | 0.224 | 24 | 77 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.757 | 0.810 | 0.800 | 82 | 20 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.372 | 0.425 | 0.414 | 43 | 58 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.800 | 0.850 | 0.841 | 86 | 16 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.149 | 0.200 | 0.189 | 21 | 81 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.334 | 0.285 | 0.295 | 29 | 72 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.146 | 0.105 | 0.112 | 11 | 90 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.514 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.824 | 0.865 | 0.858 | 87 | 14 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.554 | 0.505 | 0.515 | 51 | 50 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.260 | 0.305 | 0.296 | 31 | 70 | no | +0.025 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.522 | 0.475 | 0.484 | 48 | 53 | yes | +0.024 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.478 | 0.525 | 0.516 | 53 | 48 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.400 | 0.445 | 0.436 | 45 | 56 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.863 | 0.895 | 0.889 | 90 | 11 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.085 | 0.115 | 0.108 | 12 | 89 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.606 | 0.645 | 0.637 | 65 | 36 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.143 | 0.175 | 0.168 | 18 | 83 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.876 | 0.905 | 0.900 | 91 | 10 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.217 | 0.185 | 0.191 | 19 | 82 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-10 | game_total | 0.054 | 0.075 | 0.070 | 8 | 93 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-BOS2 | game_spread | 0.294 | 0.265 | 0.271 | 27 | 74 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS2 | team_total | 0.779 | 0.805 | 0.800 | 81 | 20 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-3 | game_total | 0.971 | 0.985 | 0.983 | 99 | 2 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS4 | team_total | 0.336 | 0.370 | 0.363 | 38 | 64 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.298 | 0.325 | 0.320 | 33 | 68 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.123 | 0.105 | 0.108 | 11 | 90 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG6 | team_total | 0.060 | 0.080 | 0.075 | 9 | 93 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS3 | team_total | 0.557 | 0.585 | 0.580 | 59 | 42 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.769 | 0.740 | 0.746 | 75 | 27 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.164 | 0.140 | 0.144 | 15 | 87 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.953 | 0.965 | 0.963 | 97 | 4 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS5 | team_total | 0.167 | 0.185 | 0.181 | 19 | 82 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL6 | team_total | 0.067 | 0.050 | 0.053 | 6 | 96 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA5 | team_total | 0.182 | 0.165 | 0.168 | 17 | 84 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-3 | game_total | 0.945 | 0.960 | 0.957 | 97 | 5 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT02STLDAL-9 | game_total | 0.151 | 0.165 | 0.162 | 17 | 84 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-10 | game_total | 0.103 | 0.115 | 0.113 | 12 | 89 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-8 | game_total | 0.218 | 0.235 | 0.232 | 24 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA3 | team_total | 0.565 | 0.545 | 0.549 | 55 | 46 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.213 | 0.225 | 0.223 | 23 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-BOS6 | team_total | 0.072 | 0.075 | 0.074 | 8 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA4 | team_total | 0.349 | 0.330 | 0.334 | 34 | 68 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT02BOSWPG-2 | game_total | 0.975 | 0.980 | 0.979 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-10 | game_total | 0.064 | 0.065 | 0.065 | 7 | 94 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT02BOSWPG-BOS3 | game_spread | 0.170 | 0.165 | 0.166 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-2 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA2 | team_total | 0.782 | 0.775 | 0.776 | 79 | 24 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT02BOSWPG-BOS | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT02BOSWPG-TIE | period_winner |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT02BOSWPG-WPG | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT02BOSWPG-BOS2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT02BOSWPG-WPG2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ WPG | 0.478 | 0.512 | 0.181 | 0.221 | 5.65 | 6.06 | 0.995/0.955 | KXNHLTOTAL-26OCT02BOSWPG-7 +0.074 |
| STL @ DAL | 0.533 | 0.533 | 0.177 | 0.215 | 5.90 | 6.10 | 0.994/0.976 | KXNHLTOTAL-26OCT02STLDAL-7 +0.035 |
| ANA @ VGK | 0.589 | 0.597 | 0.169 | 0.212 | 6.46 | 6.41 | 1.003/1.015 | KXNHLTOTAL-26OCT02ANAVGK-6 -0.016 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Marat Khusnutdinov: 1+ goals YES @ 9c · p 0.1446 (adj 0.1297) · $8.25 · thesis BOS:OFFENSE_4PLUS
- Elias Lindholm: 1+ goals YES @ 18c · p 0.2306 (adj 0.2167) · $8.21 · thesis BOS:OFFENSE_4PLUS
- JJ Peterka: 1+ assists NO @ 70c · p 0.8359 (adj 0.7411) · $20.0 · thesis BOS:SUPPRESSED
- Mark Scheifele: 1+ goals YES @ 30c · p 0.3387 (adj 0.3278) · $5.0 · thesis WPG:OFFENSE_4PLUS
- Pius Suter: 1+ goals YES @ 11c · p 0.1583 (adj 0.145) · $6.42 · thesis STL:OFFENSE_4PLUS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7383 (adj 0.7225) · $18.26 · thesis DAL:SUPPRESSED
- Mason McTavish: 1+ assists NO @ 74c · p 0.8743 (adj 0.7773) · $18.26 · thesis STL:SUPPRESSED
- Dylan Holloway: 1+ goals YES @ 26c · p 0.3124 (adj 0.2981) · $7.07 · thesis STL:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 7c · p 0.1141 (adj 0.1018) · $6.11 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2329 (adj 0.2184) · $8.08 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 23c · p 0.3635 (adj 0.2702) · $6.47 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1093 (adj 0.1007) · $3.54 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BOS @ WPG** · priced 124/124 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 26.1, exp saves 22.64 (sd 6.23), pull risk 0.056
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 28.23, exp saves 24.41 (sd 6.55), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| JJ Peterka: 1+ points | 0.349 | 0.500 | 51/51 | +0.124 | STANDARD |
| JJ Peterka: 1+ assists | 0.164 | 0.310 | 32/70 | +0.121 | STANDARD |
| Elias Lindholm: 1+ points | 0.498 | 0.400 | 41/61 | +0.071 | STANDARD |
| JJ Peterka: 2+ points | 0.068 | 0.160 | 17/85 | +0.073 | STANDARD |
| Stuart Skinner: 23+ saves | 0.503 | 0.420 | 54/70 | -0.055 |  |
| Morgan Geekie: 1+ assists | 0.353 | 0.290 | 30/72 | +0.039 | STANDARD |

**STL @ DAL** · priced 118/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.53, exp saves 21.4 (sd 6.0), pull risk 0.053
- STL net: Joel Hofer (CONFIRMED) exp shots 26.73, exp saves 22.91 (sd 6.37), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.126 | 0.275 | 29/74 | +0.121 | STANDARD |
| Mason McTavish: 1+ points | 0.300 | 0.430 | 44/58 | +0.103 | STANDARD |
| Mikko Rantanen: 2+ points | 0.193 | 0.320 | 33/69 | +0.102 | STANDARD |
| Miro Heiskanen: 1+ points | 0.472 | 0.590 | 61/43 | +0.081 | STANDARD |
| Jason Robertson: 1+ assists | 0.377 | 0.485 | 49/52 | +0.086 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.404 | 0.510 | 52/50 | +0.079 | STANDARD |

**ANA @ VGK** · priced 130/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 28.77, exp saves 25.15 (sd 6.74), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.58, exp saves 23.43 (sd 6.66), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Hart: 24+ saves | 0.596 | 0.430 | 51/65 | +0.068 |  |
| Alex Killorn: 1+ points | 0.510 | 0.365 | 38/65 | +0.113 | STANDARD |
| Alex Killorn: 1+ assists | 0.363 | 0.220 | 23/79 | +0.121 | STANDARD |
| Lukas Dostal: 28+ saves | 0.262 | 0.380 | 48/72 | +0.004 |  |
| Leo Carlsson: 1+ assists | 0.293 | 0.410 | 42/60 | +0.090 | STANDARD |
| Jack Eichel: 1+ assists | 0.460 | 0.555 | 56/45 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
