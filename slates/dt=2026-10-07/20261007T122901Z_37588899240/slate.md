# NHL slate 2026-10-07 — RESEARCH_ONLY

generated 2026-10-07T12:29:01Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2660 · contracts joined: 486 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 411, 'NO_EDGE': 44, 'OK': 31}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 59, 'game_early_goal': 3, 'first_goal': 72, 'game_winner': 6, 'player_goals': 129, 'game_overtime': 3, 'player_points': 73, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 2026-10-07T23:30:00Z | T-6h | 0.572 | 0.428 | 0.169 | 6.57 | 3.52 | 3.05 | 223 (25/198) | PROJECTED/PROJECTED |
| COL @ WPG | 2026-10-07T23:30:00Z | T-6h | 0.416 | 0.584 | 0.177 | 6.03 | 2.76 | 3.27 | 212 (25/187) | PROJECTED/PROJECTED |
| EDM @ ANA | 2026-10-08T02:00:00Z | T-12h | 0.499 | 0.501 | 0.167 | 6.90 | 3.44 | 3.46 | 51 (25/26) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL4 | team_total | 0.426 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT07COLWPG-7 | game_total | 0.419 | 0.505 | 0.488 | 51 | 50 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL5 | team_total | 0.236 | 0.310 | 0.294 | 32 | 70 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 | team_total | 0.647 | 0.720 | 0.706 | 73 | 29 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT07COLWPG-8 | game_total | 0.233 | 0.295 | 0.282 | 30 | 71 | no | +0.043 | OK |
| KXNHLGAME-26OCT07EDMANA-ANA | game_winner | 0.499 | 0.435 | 0.448 | 44 | 57 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT07COLWPG-6 | game_total | 0.532 | 0.595 | 0.583 | 60 | 41 | no | +0.041 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL2 | game_spread | 0.354 | 0.415 | 0.403 | 42 | 59 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL2 | team_total | 0.834 | 0.885 | 0.876 | 89 | 12 | no | +0.038 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL3 | game_spread | 0.222 | 0.275 | 0.264 | 28 | 73 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT07COLWPG-5 | game_total | 0.756 | 0.810 | 0.800 | 82 | 20 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT07COLWPG-4 | game_total | 0.842 | 0.885 | 0.877 | 89 | 12 | no | +0.031 | OK |
| KXNHLGAME-26OCT07COLWPG-COL | game_winner | 0.584 | 0.635 | 0.625 | 64 | 37 | no | +0.029 | OK |
| KXNHLGAME-26OCT07COLWPG-WPG | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT07COLWPG-9 | game_total | 0.161 | 0.210 | 0.199 | 22 | 80 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA4 | team_total | 0.463 | 0.415 | 0.424 | 42 | 59 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT07EDMANA-ANA2 | game_spread | 0.295 | 0.255 | 0.263 | 26 | 75 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM3 | game_spread | 0.189 | 0.225 | 0.217 | 23 | 78 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM2 | game_spread | 0.299 | 0.335 | 0.328 | 34 | 67 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL6 | team_total | 0.109 | 0.145 | 0.137 | 16 | 87 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT07COLWPG-10 | game_total | 0.072 | 0.100 | 0.094 | 11 | 91 | no | +0.012 | OK |
| KXNHLGAME-26OCT07EDMANA-EDM | game_winner | 0.501 | 0.535 | 0.528 | 54 | 47 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA5 | team_total | 0.271 | 0.240 | 0.246 | 25 | 77 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA6 | team_total | 0.134 | 0.115 | 0.119 | 12 | 89 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA3 | team_total | 0.672 | 0.640 | 0.647 | 65 | 37 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT07EDMANA-10 | game_total | 0.141 | 0.120 | 0.124 | 13 | 89 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG2 | game_spread | 0.214 | 0.195 | 0.199 | 20 | 81 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM3 | team_total | 0.673 | 0.700 | 0.695 | 71 | 31 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT07EDMANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT07PITWSH-5 | game_total | 0.811 | 0.795 | 0.798 | 80 | 21 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT07PITWSH-4 | game_total | 0.883 | 0.895 | 0.893 | 90 | 11 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT07EDMANA-9 | game_total | 0.273 | 0.250 | 0.255 | 26 | 76 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM2 | team_total | 0.852 | 0.870 | 0.867 | 88 | 14 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT5 | team_total | 0.200 | 0.180 | 0.184 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH3 | game_spread | 0.228 | 0.245 | 0.242 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-PIT2 | game_spread | 0.231 | 0.215 | 0.218 | 22 | 79 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-8 | game_total | 0.364 | 0.345 | 0.349 | 35 | 66 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-10 | game_total | 0.114 | 0.100 | 0.103 | 11 | 91 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH2 | game_spread | 0.357 | 0.375 | 0.371 | 38 | 63 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-9 | game_total | 0.228 | 0.210 | 0.213 | 22 | 80 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT6 | team_total | 0.090 | 0.075 | 0.078 | 9 | 94 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT07EDMANA-ANA3 | game_spread | 0.184 | 0.175 | 0.177 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-7 | game_total | 0.561 | 0.545 | 0.548 | 55 | 46 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT07COLWPG-WPG3 | game_spread | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA2 | team_total | 0.852 | 0.840 | 0.842 | 85 | 17 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-5 | game_total | 0.842 | 0.835 | 0.836 | 84 | 17 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG5 | team_total | 0.150 | 0.165 | 0.162 | 18 | 85 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT07PITWSH-PIT | game_winner | 0.428 | 0.415 | 0.418 | 42 | 59 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-2 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-PIT3 | game_spread | 0.132 | 0.135 | 0.134 | 14 | 87 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-7 | game_total | 0.508 | 0.495 | 0.498 | 50 | 51 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG2 | team_total | 0.757 | 0.775 | 0.772 | 79 | 24 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-8 | game_total | 0.315 | 0.305 | 0.307 | 31 | 70 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-6 | game_total | 0.666 | 0.655 | 0.657 | 66 | 35 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM4 | team_total | 0.464 | 0.485 | 0.481 | 50 | 53 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH2 | team_total | 0.863 | 0.870 | 0.869 | 88 | 14 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG3 | team_total | 0.524 | 0.545 | 0.541 | 56 | 47 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT2 | team_total | 0.799 | 0.790 | 0.792 | 80 | 22 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 | team_total | 0.373 | 0.360 | 0.363 | 37 | 65 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH3 | team_total | 0.688 | 0.700 | 0.698 | 71 | 31 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG6 | team_total | 0.060 | 0.065 | 0.064 | 8 | 95 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT3 | team_total | 0.594 | 0.575 | 0.579 | 59 | 44 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-4 | game_total | 0.907 | 0.910 | 0.909 | 92 | 10 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG4 | team_total | 0.310 | 0.325 | 0.322 | 34 | 69 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-6 | game_total | 0.619 | 0.615 | 0.616 | 62 | 39 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM6 | team_total | 0.141 | 0.135 | 0.136 | 15 | 88 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26OCT07PITWSH-WSH | game_winner | 0.572 | 0.575 | 0.574 | 58 | 43 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM5 | team_total | 0.275 | 0.290 | 0.287 | 31 | 73 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH6 | team_total | 0.139 | 0.135 | 0.136 | 15 | 88 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH5 | team_total | 0.286 | 0.295 | 0.293 | 31 | 72 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH4 | team_total | 0.483 | 0.495 | 0.493 | 51 | 52 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT07PITWSH-PIT | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-WSH | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-WSH2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 0.572 | 0.532 | 0.169 | 0.213 | 6.57 | 6.68 | 0.960/1.021 | KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 +0.048 |
| COL @ WPG | 0.416 | 0.434 | 0.177 | 0.220 | 6.03 | 6.29 | 0.988/0.973 | KXNHLTOTAL-26OCT07COLWPG-7 +0.047 |
| EDM @ ANA | 0.499 | 0.492 | 0.167 | 0.215 | 6.90 | 6.86 | 1.024/0.994 | KXNHLTOTAL-26OCT07EDMANA-8 -0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Rickard Rakell: 1+ goals YES @ 28c · p 0.3461 (adj 0.3258) · $10.34 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1739 (adj 0.1504) · $5.43 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 20c · p 0.2573 (adj 0.2355) · $7.68 · thesis WSH:OFFENSE_4PLUS
- Washington wins by over 1.5 goals NO @ 63c · p 0.6894 (adj 0.6572) · $5.73 · thesis PIT:WINS
- Josh Morrissey: 2+ goals NO @ 97c · p 0.9945 (adj 0.9871) · $20.0 · thesis DIFFUSE
- Nathan MacKinnon: 2+ points NO @ 53c · p 0.708 (adj 0.5707) · $9.6 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ assists NO @ 38c · p 0.5431 (adj 0.417) · $3.82 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 59c · p 0.6675 (adj 0.6262) · $8.78 · thesis WPG:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ WSH** · priced 163/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.09, exp saves 24.31 (sd 6.75), pull risk 0.072
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.5, exp saves 22.62 (sd 6.37), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Egor Chinakhov: 1+ assists | 0.352 | 0.180 | 22/86 | +0.120 | STANDARD |
| Alex Tuch: 1+ points | 0.452 | 0.585 | 59/42 | +0.111 | STANDARD |
| Alex Tuch: 1+ assists | 0.213 | 0.345 | 38/69 | +0.082 | STANDARD |
| Egor Chinakhov: 1+ points | 0.501 | 0.370 | 41/67 | +0.074 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.165 | 0.295 | 32/73 | +0.092 | STANDARD |
| Rickard Rakell: 2+ points | 0.246 | 0.120 | 17/93 | +0.066 | STANDARD |

**COL @ WPG** · priced 159/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 30.69, exp saves 26.24 (sd 7.22), pull risk 0.072
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.1, exp saves 22.75 (sd 6.23), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.292 | 0.475 | 48/53 | +0.161 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.457 | 0.625 | 63/38 | +0.147 | STANDARD |
| Cale Makar: 1+ points | 0.512 | 0.660 | 69/37 | +0.101 | STANDARD |
| Cale Makar: 1+ assists | 0.413 | 0.550 | 57/47 | +0.100 | STANDARD |
| T.J. Hughes: 1+ points | 0.287 | 0.395 | 43/64 | +0.057 | PRIOR_HEAVY |
| Cale Makar: 2+ points | 0.168 | 0.260 | 28/76 | +0.060 | STANDARD |

**EDM @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 28.22, exp saves 24.29 (sd 6.9), pull risk 0.079
- EDM net: Devon Levi (CONFIRMED) exp shots 29.57, exp saves 25.36 (sd 7.02), pull risk 0.078

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
