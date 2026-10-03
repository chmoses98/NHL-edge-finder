# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-03T00:15:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 2 · markets on board: 3198 · contracts joined: 356 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 306, 'OK': 38, 'NO_EDGE': 12}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 52, 'game_early_goal': 2, 'first_goal': 68, 'game_winner': 4, 'player_goals': 68, 'game_overtime': 2, 'player_points': 63, 'goalie_saves': 3, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ DAL | 2026-10-03T01:00:00Z | T-30m | 0.533 | 0.467 | 0.177 | 5.90 | 3.05 | 2.86 | 173 (25/148) | CONFIRMED/CONFIRMED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-90m | 0.589 | 0.411 | 0.169 | 6.46 | 3.52 | 2.94 | 183 (25/158) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.533 | 0.635 | 0.615 | 64 | 37 | no | +0.081 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.467 | 0.365 | 0.385 | 37 | 64 | yes | +0.081 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.182 | 0.275 | 0.254 | 28 | 73 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.483 | 0.575 | 0.557 | 58 | 43 | no | +0.070 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.306 | 0.395 | 0.376 | 40 | 61 | no | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.593 | 0.675 | 0.659 | 68 | 33 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.376 | 0.455 | 0.439 | 46 | 55 | no | +0.057 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.411 | 0.345 | 0.358 | 35 | 66 | yes | +0.045 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.589 | 0.655 | 0.642 | 66 | 35 | no | +0.045 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.242 | 0.305 | 0.292 | 31 | 70 | no | +0.044 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.253 | 0.190 | 0.202 | 20 | 82 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.196 | 0.255 | 0.242 | 26 | 75 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.689 | 0.750 | 0.738 | 76 | 26 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.804 | 0.855 | 0.846 | 86 | 15 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.289 | 0.345 | 0.333 | 35 | 66 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.372 | 0.425 | 0.414 | 43 | 58 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.334 | 0.280 | 0.290 | 29 | 73 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT02STLDAL-6 | game_total | 0.514 | 0.565 | 0.555 | 57 | 44 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.824 | 0.865 | 0.858 | 87 | 14 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.554 | 0.505 | 0.515 | 51 | 50 | yes | +0.027 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.799 | 0.835 | 0.828 | 84 | 17 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.493 | 0.535 | 0.527 | 54 | 47 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.146 | 0.115 | 0.121 | 12 | 89 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.085 | 0.115 | 0.108 | 12 | 89 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.606 | 0.645 | 0.637 | 65 | 36 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.143 | 0.180 | 0.172 | 19 | 83 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.876 | 0.905 | 0.900 | 91 | 10 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.217 | 0.185 | 0.191 | 19 | 82 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.400 | 0.435 | 0.428 | 44 | 57 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.863 | 0.890 | 0.885 | 90 | 12 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.298 | 0.325 | 0.320 | 33 | 68 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.123 | 0.105 | 0.108 | 11 | 90 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.769 | 0.740 | 0.746 | 75 | 27 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.164 | 0.140 | 0.144 | 15 | 87 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA4 | team_total | 0.349 | 0.325 | 0.330 | 33 | 68 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL6 | team_total | 0.067 | 0.045 | 0.049 | 6 | 97 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA5 | team_total | 0.182 | 0.160 | 0.164 | 17 | 85 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT02STLDAL-9 | game_total | 0.151 | 0.165 | 0.162 | 17 | 84 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-10 | game_total | 0.103 | 0.115 | 0.113 | 12 | 89 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-8 | game_total | 0.218 | 0.235 | 0.232 | 24 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-3 | game_total | 0.971 | 0.980 | 0.978 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-2 | game_total | 0.988 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.213 | 0.225 | 0.223 | 23 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.953 | 0.960 | 0.959 | 97 | 5 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-10 | game_total | 0.064 | 0.070 | 0.069 | 8 | 94 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT02STLDAL-2 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA3 | team_total | 0.565 | 0.550 | 0.553 | 56 | 46 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-ANA2 | team_total | 0.782 | 0.780 | 0.780 | 79 | 23 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT02STLDAL-DAL | period_winner |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT02STLDAL-STL | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT02STLDAL-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT02STLDAL-DAL2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT02STLDAL-STL2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT02STLDAL-1 | period_total |  | 0.835 |  | 86 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT02STLDAL-2 | period_total |  | 0.525 |  | 54 | 49 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT02STLDAL-3 | period_total |  | 0.235 |  | 26 | 79 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT02STLDAL-DAL | period_winner |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT02STLDAL-STL | period_winner |  | 0.270 |  | 29 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT02STLDAL-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT02STLDAL-DAL2 | period_spread |  | 0.155 |  | 17 | 86 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT02STLDAL-STL2 | period_spread |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT02STLDAL-1 | period_total |  | 0.880 |  | 91 | 15 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT02STLDAL-2 | period_total |  | 0.590 |  | 61 | 43 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT02STLDAL-3 | period_total |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT02STLDAL-DAL | period_winner |  | 0.420 |  | 44 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT02STLDAL-STL | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT02STLDAL-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT02STLDAL-DAL2 | period_spread |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT02STLDAL-STL2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT02STLDAL-1 | period_total |  | 0.905 |  | 93 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT02STLDAL-2 | period_total |  | 0.645 |  | 67 | 38 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT02STLDAL-3 | period_total |  | 0.360 |  | 38 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02STLDAL-DALJROBERTSON21-1 | player_assists |  | 0.480 |  | 49 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02STLDAL-DALJROBERTSON21-2 | player_assists |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02STLDAL-DALMHEISKANEN4-1 | player_assists |  | 0.505 |  | 51 | 50 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02STLDAL-DALMHEISKANEN4-2 | player_assists |  | 0.155 |  | 16 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02STLDAL-DALMHEISKANEN4-3 | player_assists |  | 0.035 |  | 5 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT02STLDAL-DALMRANTANEN96-1 | player_assists |  | 0.510 |  | 52 | 50 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| STL @ DAL | 0.533 | 0.533 | 0.177 | 0.215 | 5.90 | 6.10 | 0.994/0.976 | KXNHLTOTAL-26OCT02STLDAL-7 +0.035 |
| ANA @ VGK | 0.589 | 0.597 | 0.169 | 0.212 | 6.46 | 6.41 | 1.003/1.015 | KXNHLTOTAL-26OCT02ANAVGK-6 -0.016 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Pius Suter: 1+ goals YES @ 11c · p 0.1583 (adj 0.145) · $6.75 · thesis STL:OFFENSE_4PLUS
- Dallas wins NO @ 37c · p 0.4586 (adj 0.4165) · $6.1 · thesis STL:WINS
- Mikko Rantanen: 1+ goals NO @ 68c · p 0.7383 (adj 0.7225) · $20.0 · thesis DAL:SUPPRESSED
- Dylan Holloway: 1+ goals YES @ 26c · p 0.3124 (adj 0.2981) · $6.92 · thesis STL:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 7c · p 0.1141 (adj 0.1018) · $6.14 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 22c · p 0.3635 (adj 0.267) · $8.41 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2329 (adj 0.2184) · $8.01 · thesis ANA:OFFENSE_4PLUS
- Braeden Bowman: 1+ goals YES @ 15c · p 0.1953 (adj 0.1827) · $6.64 · thesis VGK:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**STL @ DAL** · priced 118/122 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (CONFIRMED) exp shots 24.53, exp saves 21.4 (sd 6.0), pull risk 0.053
- STL net: Joel Hofer (CONFIRMED) exp shots 26.73, exp saves 22.91 (sd 6.37), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mason McTavish: 1+ assists | 0.126 | 0.280 | 30/74 | +0.121 | STANDARD |
| Mikko Rantanen: 2+ points | 0.193 | 0.325 | 33/68 | +0.111 | STANDARD |
| Mason McTavish: 1+ points | 0.300 | 0.425 | 44/59 | +0.093 | STANDARD |
| Miro Heiskanen: 1+ points | 0.472 | 0.595 | 61/42 | +0.091 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.404 | 0.510 | 52/50 | +0.079 | STANDARD |
| Jason Robertson: 1+ assists | 0.377 | 0.480 | 49/53 | +0.076 | STANDARD |

**ANA @ VGK** · priced 130/132 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (CONFIRMED) exp shots 28.77, exp saves 25.15 (sd 6.74), pull risk 0.053
- ANA net: Lukas Dostal (CONFIRMED) exp shots 27.58, exp saves 23.43 (sd 6.66), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Carter Hart: 24+ saves | 0.596 | 0.425 | 51/66 | +0.068 |  |
| Alex Killorn: 1+ points | 0.510 | 0.355 | 37/66 | +0.123 | STANDARD |
| Alex Killorn: 1+ assists | 0.363 | 0.215 | 22/79 | +0.131 | STANDARD |
| Lukas Dostal: 28+ saves | 0.262 | 0.380 | 48/72 | +0.004 |  |
| Leo Carlsson: 1+ assists | 0.293 | 0.400 | 41/61 | +0.080 | STANDARD |
| Mitch Marner: 1+ assists | 0.430 | 0.525 | 53/48 | +0.072 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
