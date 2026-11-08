# NHL slate 2026-11-08 — RESEARCH_ONLY

generated 2026-11-08T20:30:26Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 6 · simulated (not started): 4 · markets on board: 2904 · contracts joined: 898 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 798, 'OK': 70, 'NO_EDGE': 30}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 125, 'game_early_goal': 4, 'first_goal': 146, 'game_winner': 8, 'player_goals': 255, 'game_overtime': 4, 'player_points': 162, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ WPG | 2026-11-08T23:00:00Z | T-90m | 0.442 | 0.558 | 0.182 | 5.96 | 2.80 | 3.16 | 210 (25/185) | PROBABLE/PROJECTED |
| NJD @ TOR | 2026-11-09T00:00:00Z | T-3h | 0.457 | 0.543 | 0.171 | 6.54 | 3.12 | 3.43 | 227 (25/202) | PROBABLE/PROJECTED |
| PHI @ CGY | 2026-11-09T00:00:00Z | T-3h | 0.577 | 0.423 | 0.187 | 5.43 | 2.93 | 2.50 | 231 (25/206) | CONFIRMED/PROBABLE |
| PIT @ ANA | 2026-11-09T01:00:00Z | T-3h | 0.604 | 0.396 | 0.156 | 7.22 | 3.97 | 3.25 | 230 (25/205) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 | team_total | 0.460 | 0.590 | 0.564 | 60 | 42 | no | +0.103 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI4 | team_total | 0.251 | 0.380 | 0.352 | 39 | 63 | no | +0.102 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI2 | team_total | 0.706 | 0.805 | 0.787 | 81 | 20 | no | +0.083 | OK |
| KXNHLGAME-26NOV08PHICGY-CGY | game_winner | 0.577 | 0.475 | 0.495 | 48 | 53 | yes | +0.079 | OK |
| KXNHLGAME-26NOV08PHICGY-PHI | game_winner | 0.423 | 0.525 | 0.505 | 53 | 48 | no | +0.079 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI2 | game_spread | 0.209 | 0.305 | 0.284 | 31 | 70 | no | +0.076 | OK |
| KXNHLTOTAL-26NOV08PHICGY-5 | game_total | 0.666 | 0.755 | 0.738 | 76 | 25 | no | +0.071 | OK |
| KXNHLSPREAD-26NOV08PHICGY-PHI3 | game_spread | 0.111 | 0.195 | 0.175 | 20 | 81 | no | +0.069 | OK |
| KXNHLGAME-26NOV08PITANA-ANA | game_winner | 0.604 | 0.515 | 0.533 | 52 | 49 | yes | +0.067 | OK |
| KXNHLGAME-26NOV08PITANA-PIT | game_winner | 0.396 | 0.485 | 0.467 | 49 | 52 | no | +0.067 | OK |
| KXNHLTOTAL-26NOV08PHICGY-6 | game_total | 0.427 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV08PHICGY-7 | game_total | 0.319 | 0.405 | 0.387 | 41 | 60 | no | +0.065 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA2 | game_spread | 0.398 | 0.315 | 0.331 | 32 | 69 | yes | +0.063 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA5 | team_total | 0.377 | 0.290 | 0.306 | 30 | 72 | yes | +0.062 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT2 | game_spread | 0.217 | 0.295 | 0.278 | 30 | 71 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI5 | team_total | 0.113 | 0.195 | 0.176 | 21 | 82 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA4 | team_total | 0.573 | 0.490 | 0.507 | 50 | 52 | yes | +0.056 | OK |
| KXNHLTOTAL-26NOV08TBWPG-6 | game_total | 0.519 | 0.595 | 0.580 | 60 | 41 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA6 | team_total | 0.210 | 0.140 | 0.152 | 15 | 87 | yes | +0.052 | OK |
| KXNHLTOTAL-26NOV08PHICGY-4 | game_total | 0.770 | 0.840 | 0.828 | 85 | 17 | no | +0.050 | OK |
| KXNHLTOTAL-26NOV08PHICGY-8 | game_total | 0.159 | 0.225 | 0.210 | 23 | 78 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA3 | team_total | 0.759 | 0.695 | 0.709 | 70 | 31 | yes | +0.045 | OK |
| KXNHLTOTAL-26NOV08TBWPG-7 | game_total | 0.409 | 0.475 | 0.462 | 48 | 53 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV08PITANA-PIT3 | game_spread | 0.127 | 0.185 | 0.172 | 19 | 82 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY2 | game_spread | 0.327 | 0.265 | 0.277 | 27 | 74 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV08PITANA-ANA3 | game_spread | 0.272 | 0.210 | 0.222 | 22 | 80 | yes | +0.040 | OK |
| KXNHLTOTAL-26NOV08TBWPG-5 | game_total | 0.739 | 0.795 | 0.785 | 80 | 21 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB4 | team_total | 0.398 | 0.455 | 0.443 | 46 | 55 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB5 | team_total | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.032 | OK |
| KXNHLGAME-26NOV08NJTOR-NJ | game_winner | 0.543 | 0.595 | 0.585 | 60 | 41 | no | +0.030 | OK |
| KXNHLGAME-26NOV08NJTOR-TOR | game_winner | 0.457 | 0.405 | 0.415 | 41 | 60 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3 | team_total | 0.606 | 0.555 | 0.565 | 56 | 45 | yes | +0.029 | OK |
| KXNHLTOTAL-26NOV08TBWPG-8 | game_total | 0.230 | 0.275 | 0.266 | 28 | 73 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV08PHICGY-9 | game_total | 0.106 | 0.150 | 0.140 | 16 | 86 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV08PHICGY-PHI6 | team_total | 0.041 | 0.080 | 0.070 | 9 | 93 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV08NJTOR-9 | game_total | 0.225 | 0.185 | 0.192 | 19 | 82 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV08TBWPG-4 | game_total | 0.829 | 0.870 | 0.863 | 88 | 14 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB3 | team_total | 0.622 | 0.665 | 0.657 | 67 | 34 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR5 | team_total | 0.212 | 0.175 | 0.182 | 18 | 83 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV08PITANA-8 | game_total | 0.408 | 0.365 | 0.373 | 37 | 64 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG2 | team_total | 0.757 | 0.795 | 0.788 | 80 | 21 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV08TBWPG-9 | game_total | 0.158 | 0.195 | 0.187 | 20 | 81 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB2 | team_total | 0.822 | 0.860 | 0.853 | 87 | 15 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 | team_total | 0.534 | 0.575 | 0.567 | 58 | 43 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV08PITANA-9 | game_total | 0.311 | 0.275 | 0.282 | 28 | 73 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV08PITANA-10 | game_total | 0.176 | 0.140 | 0.147 | 15 | 87 | yes | +0.017 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB3 | game_spread | 0.201 | 0.240 | 0.232 | 25 | 77 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT2 | team_total | 0.826 | 0.860 | 0.854 | 87 | 15 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG4 | team_total | 0.319 | 0.360 | 0.352 | 37 | 65 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR4 | team_total | 0.391 | 0.350 | 0.358 | 36 | 66 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT3 | team_total | 0.630 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV08NJTOR-8 | game_total | 0.308 | 0.270 | 0.277 | 28 | 74 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-ANA2 | team_total | 0.901 | 0.870 | 0.877 | 88 | 14 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV08PHICGY-3 | game_total | 0.933 | 0.960 | 0.956 | 97 | 5 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV08PHICGY-10 | game_total | 0.043 | 0.065 | 0.060 | 7 | 94 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ3 | game_spread | 0.216 | 0.250 | 0.243 | 26 | 76 | no | +0.011 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR2 | game_spread | 0.249 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLGAME-26NOV08TBWPG-TB | game_winner | 0.558 | 0.585 | 0.580 | 59 | 42 | no | +0.005 | OK |
| KXNHLGAME-26NOV08TBWPG-WPG | game_winner | 0.442 | 0.415 | 0.420 | 42 | 59 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV08TBWPG-10 | game_total | 0.070 | 0.095 | 0.089 | 11 | 92 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV08NJTOR-7 | game_total | 0.503 | 0.475 | 0.481 | 48 | 53 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV08NJTOR-10 | game_total | 0.111 | 0.090 | 0.094 | 10 | 92 | yes | +0.004 | OK |
| KXNHLSPREAD-26NOV08TBWPG-TB2 | game_spread | 0.330 | 0.355 | 0.350 | 36 | 65 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV08PITANA-2 | game_total | 0.994 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |
| KXNHLSPREAD-26NOV08PHICGY-CGY3 | game_spread | 0.193 | 0.170 | 0.174 | 18 | 84 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV08TBWPG-3 | game_total | 0.955 | 0.975 | 0.972 | 99 | 4 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV08TBWPG-WPG5 | team_total | 0.159 | 0.180 | 0.176 | 19 | 83 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV08NJTOR-TOR3 | game_spread | 0.149 | 0.135 | 0.138 | 14 | 87 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT5 | team_total | 0.236 | 0.260 | 0.255 | 27 | 75 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV08NJTOR-NJ2 | game_spread | 0.334 | 0.355 | 0.351 | 36 | 65 | no | +0.000 | OK |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR2 | team_total | 0.811 | 0.790 | 0.794 | 80 | 22 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-7 | game_total | 0.606 | 0.580 | 0.585 | 59 | 43 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08NJTOR-TOR6 | team_total | 0.093 | 0.075 | 0.078 | 9 | 94 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV08PITANA-6 | game_total | 0.712 | 0.695 | 0.698 | 70 | 31 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08TBWPG-TB6 | team_total | 0.097 | 0.115 | 0.111 | 13 | 90 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV08TBWPG-WPG3 | game_spread | 0.127 | 0.140 | 0.137 | 15 | 87 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-4 | game_total | 0.883 | 0.870 | 0.873 | 88 | 14 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV08PITANA-PIT4 | team_total | 0.418 | 0.445 | 0.439 | 46 | 57 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV08NJTOR-6 | game_total | 0.612 | 0.595 | 0.598 | 60 | 41 |  | -0.005 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TBL @ WPG | 0.442 | 0.483 | 0.182 | 0.224 | 5.96 | 6.16 | 1.002/0.958 | KXNHLTEAMTOTAL-26NOV08TBWPG-WPG3 +0.060 |
| NJD @ TOR | 0.457 | 0.502 | 0.171 | 0.219 | 6.54 | 6.34 | 0.960/0.959 | KXNHLSPREAD-26NOV08NJTOR-NJ2 -0.049 |
| PHI @ CGY | 0.577 | 0.503 | 0.187 | 0.226 | 5.43 | 5.97 | 0.978/0.994 | KXNHLTEAMTOTAL-26NOV08PHICGY-PHI3 +0.122 |
| PIT @ ANA | 0.604 | 0.637 | 0.156 | 0.192 | 7.22 | 7.14 | 0.986/1.033 | KXNHLSPREAD-26NOV08PITANA-ANA3 +0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 14 recommended · full analysis in card.md / packet.json `thesis_card`

- Isak Rosen: 1+ goals YES @ 9c · p 0.1212 (adj 0.1121) · $4.1 · thesis WPG:OFFENSE_4PLUS
- Cole Perfetti: 1+ assists YES @ 32c · p 0.396 (adj 0.353) · $6.18 · thesis WPG:OFFENSE_4PLUS
- Nikita Kucherov: 1+ assists NO @ 40c · p 0.5372 (adj 0.4268) · $4.19 · thesis TBL:SUPPRESSED
- Easton Cowan: 1+ goals YES @ 17c · p 0.2221 (adj 0.2066) · $7.55 · thesis TOR:OFFENSE_4PLUS
- Colton Sissons: 1+ goals YES @ 9c · p 0.1276 (adj 0.1157) · $4.9 · thesis TOR:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1464 (adj 0.1248) · $4.38 · thesis TOR:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 61c · p 0.6684 (adj 0.6525) · $17.07 · thesis NJD:SUPPRESSED
- Travis Konecny: 1+ assists NO @ 65c · p 0.7386 (adj 0.6893) · $19.06 · thesis PHI:SUPPRESSED
- Jonathan Castagna: 1+ goals YES @ 9c · p 0.1155 (adj 0.1079) · $3.12 · thesis CGY:OFFENSE_4PLUS
- Martin Pospisil: 1+ goals YES @ 11c · p 0.1371 (adj 0.1278) · $2.86 · thesis CGY:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 11c · p 0.1565 (adj 0.1436) · $6.57 · thesis ANA:OFFENSE_4PLUS
- Pittsburgh wins by over 1.5 goals NO @ 71c · p 0.8047 (adj 0.7549) · $20.0 · thesis ANA:WINS
- Kaedan Korczak: 1+ goals YES @ 3c · p 0.051 (adj 0.0432) · $2.45 · thesis DIFFUSE
- Connor Dewar: 1+ goals YES @ 12c · p 0.1586 (adj 0.1464) · $6.15 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TBL @ WPG** · priced 158/159 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROBABLE) exp shots 28.45, exp saves 24.6 (sd 6.75), pull risk 0.061
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 25.75, exp saves 22.33 (sd 6.15), pull risk 0.053

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nikita Kucherov: 1+ assists | 0.463 | 0.610 | 62/40 | +0.120 | STANDARD |
| Nikita Kucherov: 2+ points | 0.270 | 0.400 | 41/61 | +0.103 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.126 | 0.225 | 25/80 | +0.062 | STANDARD |
| Cole Perfetti: 1+ assists | 0.396 | 0.310 | 32/70 | +0.061 | STANDARD |
| Nikita Kucherov: 1+ points | 0.640 | 0.725 | 76/31 | +0.035 | STANDARD |
| John Carlson: 1+ points | 0.377 | 0.460 | 47/55 | +0.056 | STANDARD |

**NJD @ TOR** · priced 173/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROBABLE) exp shots 32.87, exp saves 28.37 (sd 7.47), pull risk 0.065
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 26.54, exp saves 23.0 (sd 6.29), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 2+ points | 0.229 | 0.355 | 36/65 | +0.105 | STANDARD |
| John Tavares: 1+ assists | 0.245 | 0.370 | 38/64 | +0.098 | STANDARD |
| Jack Hughes: 1+ assists | 0.396 | 0.520 | 53/49 | +0.097 | STANDARD |
| Easton Cowan: 2+ points | 0.160 | 0.055 | 10/99 | +0.053 | STANDARD |
| Luke Evangelista: 1+ assists | 0.246 | 0.350 | 37/67 | +0.068 | STANDARD |
| Jesper Bratt: 1+ assists | 0.382 | 0.480 | 49/53 | +0.070 | STANDARD |

**PHI @ CGY** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 26.62, exp saves 23.17 (sd 6.4), pull risk 0.053
- PHI net: Dan Vladar (PROBABLE) exp shots 27.45, exp saves 23.82 (sd 6.48), pull risk 0.056

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ assists | 0.261 | 0.360 | 37/65 | +0.073 | STANDARD |
| Travis Konecny: 1+ points | 0.428 | 0.495 | 51/52 | +0.034 | STANDARD |
| Porter Martone: 1+ points | 0.400 | 0.465 | 48/55 | +0.033 | STANDARD |
| Porter Martone: 1+ goals | 0.187 | 0.240 | 26/78 | +0.021 | STANDARD |
| Travis Sanheim: 1+ points | 0.380 | 0.335 | 34/67 | +0.025 | STANDARD |
| Porter Martone: 1+ assists | 0.263 | 0.305 | 31/70 | +0.022 | STANDARD |

**PIT @ ANA** · priced 178/179 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (PROJECTED) exp shots 26.45, exp saves 23.05 (sd 6.45), pull risk 0.064
- PIT net: Arturs Silovs (PROJECTED) exp shots 28.23, exp saves 23.69 (sd 7.01), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 25+ saves | 0.458 | 0.355 | 48/77 | -0.039 |  |
| Ben Kindel: 1+ points | 0.411 | 0.495 | 51/52 | +0.052 | STANDARD |
| Erik Karlsson: 1+ points | 0.502 | 0.585 | 61/44 | +0.041 | STANDARD |
| Sidney Crosby: 1+ assists | 0.368 | 0.450 | 47/57 | +0.045 | STANDARD |
| Erik Karlsson: 1+ assists | 0.422 | 0.500 | 51/51 | +0.051 | STANDARD |
| Sam Colangelo: 1+ goals | 0.170 | 0.105 | 14/93 | +0.022 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
