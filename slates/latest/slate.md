# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T22:03:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 4 · markets on board: 2689 · contracts joined: 897 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 797, 'OK': 72, 'NO_EDGE': 28}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 125, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 255, 'game_overtime': 4, 'player_points': 162, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ WPG | 2026-11-08T23:00:00Z | T-30m | 0.442 | 0.558 | 0.180 | 5.96 | 2.80 | 3.16 | 210 (25/185) | PROBABLE/PROJECTED |
| NJD @ TOR | 2026-11-09T00:00:00Z | T-90m | 0.452 | 0.548 | 0.171 | 6.55 | 3.11 | 3.44 | 226 (25/201) | CONFIRMED/PROJECTED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-90m | 0.571 | 0.429 | 0.189 | 5.44 | 2.93 | 2.51 | 231 (25/206) | CONFIRMED/PROBABLE |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-90m | 0.605 | 0.395 | 0.156 | 7.22 | 3.97 | 3.25 | 230 (25/205) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.252 | 0.380 | 0.352 | 39 | 63 | no | +0.101 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.463 | 0.585 | 0.561 | 59 | 42 | no | +0.100 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.708 | 0.805 | 0.788 | 81 | 20 | no | +0.081 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.212 | 0.305 | 0.285 | 31 | 70 | no | +0.074 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.571 | 0.475 | 0.494 | 48 | 53 | yes | +0.073 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.429 | 0.525 | 0.506 | 53 | 48 | no | +0.073 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.666 | 0.755 | 0.739 | 76 | 25 | no | +0.070 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.110 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.399 | 0.315 | 0.331 | 32 | 69 | yes | +0.064 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.378 | 0.295 | 0.311 | 30 | 71 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.211 | 0.135 | 0.148 | 14 | 87 | yes | +0.063 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.321 | 0.405 | 0.388 | 41 | 60 | no | +0.062 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.431 | 0.515 | 0.498 | 52 | 49 | no | +0.061 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.112 | 0.195 | 0.175 | 21 | 82 | no | +0.057 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.605 | 0.525 | 0.541 | 53 | 48 | yes | +0.057 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.395 | 0.475 | 0.459 | 48 | 53 | no | +0.057 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.769 | 0.840 | 0.827 | 85 | 17 | no | +0.051 | OK |
| KXNHLTOTAL-26NOV08TBWPG-6 | game_total | 0.522 | 0.595 | 0.581 | 60 | 41 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.607 | 0.535 | 0.550 | 54 | 47 | yes | +0.050 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.329 | 0.265 | 0.277 | 27 | 74 | yes | +0.046 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.042 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.273 | 0.210 | 0.222 | 22 | 80 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV08TBWPG-7 | game_total | 0.412 | 0.475 | 0.462 | 48 | 53 | no | +0.041 | OK |
| KXNHLTOTAL-26NOV08TBWPG-5 | game_total | 0.740 | 0.800 | 0.789 | 81 | 21 | no | +0.038 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.162 | 0.215 | 0.204 | 22 | 79 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.573 | 0.505 | 0.519 | 52 | 51 | yes | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB5 | team_total | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB4 | team_total | 0.398 | 0.460 | 0.447 | 47 | 55 | no | +0.035 | OK |
| KXNHLTOTAL-26NOV08TBWPG-4 | game_total | 0.830 | 0.875 | 0.867 | 88 | 13 | no | +0.033 | OK |
| KXNHLTOTAL-26NOV08TBWPG-8 | game_total | 0.224 | 0.275 | 0.264 | 28 | 73 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.228 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.105 | 0.150 | 0.140 | 16 | 86 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV08TBWPG-9 | game_total | 0.154 | 0.195 | 0.186 | 20 | 81 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.759 | 0.710 | 0.720 | 72 | 30 | yes | +0.025 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.548 | 0.595 | 0.586 | 60 | 41 | no | +0.025 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.452 | 0.405 | 0.414 | 41 | 60 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.042 | 0.075 | 0.067 | 8 | 93 | no | +0.023 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG2 | team_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB3 | team_total | 0.623 | 0.665 | 0.657 | 67 | 34 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG4 | team_total | 0.323 | 0.365 | 0.356 | 37 | 64 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.386 | 0.345 | 0.353 | 35 | 66 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 | team_total | 0.533 | 0.575 | 0.567 | 58 | 43 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.312 | 0.270 | 0.278 | 28 | 74 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.312 | 0.275 | 0.282 | 28 | 73 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.177 | 0.140 | 0.147 | 15 | 87 | yes | +0.018 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR2 | game_spread | 0.249 | 0.215 | 0.222 | 22 | 79 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.417 | 0.455 | 0.447 | 46 | 55 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.629 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.503 | 0.465 | 0.473 | 47 | 54 | yes | +0.015 | OK |
| KXNHLTOTAL-26NOV08PHICGY-10 | game_total | 0.041 | 0.070 | 0.063 | 8 | 94 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.902 | 0.870 | 0.877 | 88 | 14 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ3 | game_spread | 0.214 | 0.250 | 0.242 | 26 | 76 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB3 | game_spread | 0.204 | 0.235 | 0.229 | 24 | 77 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV08PHICGY-3 | game_total | 0.934 | 0.960 | 0.956 | 97 | 5 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR6 | team_total | 0.097 | 0.070 | 0.075 | 8 | 94 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB2 | team_total | 0.820 | 0.855 | 0.849 | 87 | 16 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.211 | 0.180 | 0.186 | 19 | 83 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR2 | team_total | 0.809 | 0.780 | 0.786 | 79 | 23 | yes | +0.008 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY3 | game_spread | 0.197 | 0.170 | 0.175 | 18 | 84 | yes | +0.006 | OK |
| KXNHLTOTAL-26NOV08TBWPG-10 | game_total | 0.069 | 0.090 | 0.085 | 10 | 92 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV08NJTOR-10 | game_total | 0.112 | 0.090 | 0.094 | 10 | 92 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.825 | 0.855 | 0.849 | 87 | 16 | no | +0.005 | OK |
| KXNHLGAME-26NOV08TBWPG-WPG | game_winner | 0.442 | 0.415 | 0.420 | 42 | 59 | yes | +0.005 | OK |
| KXNHLGAME-26NOV08TBWPG-TB | game_winner | 0.558 | 0.585 | 0.580 | 59 | 42 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV08NJTOR-6 | game_total | 0.612 | 0.585 | 0.590 | 59 | 42 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-NJ6 | team_total | 0.131 | 0.105 | 0.110 | 12 | 91 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB2 | game_spread | 0.332 | 0.360 | 0.354 | 37 | 65 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG5 | team_total | 0.159 | 0.180 | 0.176 | 19 | 83 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.236 | 0.260 | 0.255 | 27 | 75 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV08TBWPG-3 | game_total | 0.957 | 0.975 | 0.972 | 99 | 4 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-2 | game_total | 0.990 | 0.980 | 0.983 | 99 | 3 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26NOV08NJTOR-NJ2 | game_spread | 0.335 | 0.355 | 0.351 | 36 | 65 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26NOV08NJTOR-TOR3 | game_spread | 0.147 | 0.135 | 0.137 | 14 | 87 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV08PHICGY-2 | game_total | 0.970 | 0.980 | 0.978 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.712 | 0.695 | 0.698 | 70 | 31 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-4 | game_total | 0.883 | 0.870 | 0.873 | 88 | 14 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB6 | team_total | 0.098 | 0.110 | 0.107 | 12 | 90 |  | -0.004 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ WPG | 0.442 | 0.483 | 0.180 | 0.224 | 5.96 | 6.16 | 1.002/0.958 | KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 +0.061 |
| NJD @ TOR | 0.452 | 0.501 | 0.171 | 0.221 | 6.55 | 6.33 | 0.956/0.959 | KXNHLTEAMTOTAL-26NOV08NJTOR-NJ4 -0.057 |
| PHI @ CGY | 0.571 | 0.503 | 0.189 | 0.226 | 5.44 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.119 |
| PIT @ ANA | 0.605 | 0.637 | 0.156 | 0.192 | 7.22 | 7.14 | 0.986/1.033 | KXNHLSPREAD-26NOV08PITANA-ANA3 +0.036 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Charle-Edouard D'Astous: 1+ goals NO @ 89c · p 0.9206 (adj 0.9117) · $20.0 · thesis TBL:SUPPRESSED
- Cole Perfetti: 1+ assists YES @ 32c · p 0.396 (adj 0.3555) · $6.58 · thesis WPG:OFFENSE_4PLUS
- Cole Koepke: 1+ goals YES @ 9c · p 0.1131 (adj 0.1061) · $2.48 · thesis WPG:OFFENSE_4PLUS
- Tampa Bay wins by over 2.5 goals NO @ 77c · p 0.8211 (adj 0.7931) · $8.39 · thesis WPG:WINS
- Brandon Duhaime: 1+ goals YES @ 6c · p 0.1005 (adj 0.0891) · $5.81 · thesis TOR:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1485 (adj 0.1339) · $6.75 · thesis TOR:WINS_BY_2PLUS
- Easton Cowan: 1+ goals YES @ 17c · p 0.2239 (adj 0.2092) · $8.4 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 9c · p 0.1286 (adj 0.1177) · $5.28 · thesis TOR:OFFENSE_4PLUS
- Travis Konecny: 1+ assists NO @ 65c · p 0.7386 (adj 0.6893) · $15.15 · thesis PHI:SUPPRESSED
- Porter Martone: 1+ goals NO @ 77c · p 0.813 (adj 0.7985) · $14.85 · thesis PHI:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 9c · p 0.1155 (adj 0.1066) · $2.75 · thesis CGY:OFFENSE_4PLUS
- Martin Pospisil: 1+ goals YES @ 11c · p 0.1371 (adj 0.1278) · $2.85 · thesis CGY:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 18c · p 0.2373 (adj 0.2217) · $8.42 · thesis ANA:OFFENSE_4PLUS
- Pittsburgh wins by over 1.5 goals NO @ 71c · p 0.8047 (adj 0.7549) · $20.0 · thesis ANA:WINS
- Kaedan Korczak: 1+ goals YES @ 3c · p 0.051 (adj 0.0432) · $2.43 · thesis DIFFUSE
- Beckett Sennecke: 1+ goals YES @ 35c · p 0.4007 (adj 0.3868) · $6.83 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ WPG** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 28.45, exp saves 24.6 (sd 6.75), pull risk 0.061
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.33 (sd 6.15), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.463 | 0.620 | 63/39 | +0.131 | STANDARD |
| Nikita Kucherov: 2+ points | 0.270 | 0.400 | 41/61 | +0.103 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.126 | 0.225 | 24/79 | +0.072 | STANDARD |
| John Carlson: 1+ points | 0.377 | 0.470 | 48/54 | +0.066 | STANDARD |
| Cole Perfetti: 1+ assists | 0.396 | 0.315 | 32/69 | +0.061 | STANDARD |
| Nikita Kucherov: 1+ points | 0.640 | 0.720 | 75/31 | +0.035 | STANDARD |

**NJD @ TOR** · priced 165/175 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (CONFIRMED) exp shots 32.87, exp saves 28.45 (sd 7.41), pull risk 0.061
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.54, exp saves 22.91 (sd 6.4), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.249 | 0.365 | 37/64 | +0.094 | STANDARD |
| John Tavares: 1+ assists | 0.249 | 0.360 | 38/66 | +0.076 | STANDARD |
| Easton Cowan: 1+ points | 0.511 | 0.405 | 41/60 | +0.084 | STANDARD |
| Jack Hughes: 2+ points | 0.257 | 0.355 | 36/65 | +0.077 | STANDARD |
| Evan Rodrigues: 1+ points | 0.269 | 0.365 | 38/65 | +0.065 | STANDARD |
| Evan Rodrigues: 1+ assists | 0.153 | 0.245 | 25/76 | +0.074 | STANDARD |

**PHI @ CGY** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.17 (sd 6.4), pull risk 0.053
- PHI net: Dan Vladar (PROBABLE) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.261 | 0.360 | 37/65 | +0.073 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.505 | 51/50 | +0.054 | STANDARD |
| Porter Martone: 1+ points | 0.400 | 0.465 | 48/55 | +0.033 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.245 | 26/77 | +0.031 | STANDARD |
| Porter Martone: 1+ assists | 0.263 | 0.305 | 31/70 | +0.022 | STANDARD |
| Joel Farabee: 3+ points | 0.040 | 0.080 | 7/ | -0.034 | STANDARD |

**PIT @ ANA** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (PROJECTED) exp shots 26.45, exp saves 23.05 (sd 6.45), pull risk 0.064
- PIT net: Arturs Silovs (PROJECTED) exp shots 28.23, exp saves 23.69 (sd 7.01), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sidney Crosby: 1+ assists | 0.368 | 0.455 | 47/56 | +0.055 | STANDARD |
| Ben Kindel: 1+ points | 0.411 | 0.495 | 51/52 | +0.052 | STANDARD |
| Erik Karlsson: 1+ points | 0.502 | 0.585 | 61/44 | +0.041 | STANDARD |
| Erik Karlsson: 1+ assists | 0.422 | 0.500 | 51/51 | +0.051 | STANDARD |
| Erik Karlsson: 2+ points | 0.158 | 0.230 | 25/79 | +0.040 | STANDARD |
| Alex Killorn: 1+ goals | 0.237 | 0.175 | 18/83 | +0.047 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
