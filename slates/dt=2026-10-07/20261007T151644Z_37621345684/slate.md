# NHL slate 2026-10-07 — RESEARCH_ONLY

generated 2026-10-07T15:16:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2816 · contracts joined: 642 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 567, 'NO_EDGE': 45, 'OK': 30}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 84, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 192, 'game_overtime': 3, 'player_points': 106, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 2026-10-07T23:30:00Z | T-6h | 0.592 | 0.408 | 0.170 | 6.45 | 3.52 | 2.94 | 223 (25/198) | CONFIRMED/PROJECTED |
| COL @ WPG | 2026-10-07T23:30:00Z | T-6h | 0.416 | 0.584 | 0.177 | 6.03 | 2.76 | 3.27 | 212 (25/187) | PROJECTED/PROJECTED |
| EDM @ ANA | 2026-10-08T02:00:00Z | T-6h | 0.499 | 0.501 | 0.167 | 6.90 | 3.44 | 3.46 | 207 (25/182) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL4 | team_total | 0.426 | 0.515 | 0.497 | 52 | 49 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT07COLWPG-7 | game_total | 0.419 | 0.505 | 0.488 | 51 | 50 | no | +0.063 | OK |
| KXNHLTOTAL-26OCT07COLWPG-6 | game_total | 0.532 | 0.605 | 0.591 | 61 | 40 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 | team_total | 0.647 | 0.715 | 0.702 | 72 | 29 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT07COLWPG-8 | game_total | 0.233 | 0.295 | 0.282 | 30 | 71 | no | +0.043 | OK |
| KXNHLGAME-26OCT07EDMANA-ANA | game_winner | 0.499 | 0.435 | 0.448 | 44 | 57 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL5 | team_total | 0.236 | 0.305 | 0.290 | 32 | 71 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL2 | game_spread | 0.354 | 0.415 | 0.403 | 42 | 59 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL3 | game_spread | 0.222 | 0.275 | 0.264 | 28 | 73 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT07COLWPG-5 | game_total | 0.756 | 0.805 | 0.796 | 81 | 20 | no | +0.033 | OK |
| KXNHLGAME-26OCT07EDMANA-EDM | game_winner | 0.501 | 0.555 | 0.544 | 56 | 45 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT07COLWPG-4 | game_total | 0.842 | 0.890 | 0.882 | 90 | 12 | no | +0.031 | OK |
| KXNHLGAME-26OCT07COLWPG-COL | game_winner | 0.584 | 0.635 | 0.625 | 64 | 37 | no | +0.029 | OK |
| KXNHLGAME-26OCT07COLWPG-WPG | game_winner | 0.416 | 0.365 | 0.375 | 37 | 64 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL2 | team_total | 0.834 | 0.880 | 0.872 | 89 | 13 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT07COLWPG-9 | game_total | 0.161 | 0.210 | 0.199 | 22 | 80 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM2 | game_spread | 0.299 | 0.345 | 0.335 | 35 | 66 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT07EDMANA-ANA2 | game_spread | 0.295 | 0.255 | 0.263 | 26 | 75 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM3 | game_spread | 0.189 | 0.225 | 0.217 | 23 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA3 | team_total | 0.672 | 0.635 | 0.643 | 64 | 37 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL6 | team_total | 0.109 | 0.140 | 0.133 | 15 | 87 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG2 | game_spread | 0.214 | 0.185 | 0.191 | 19 | 82 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA5 | team_total | 0.271 | 0.240 | 0.246 | 25 | 77 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA6 | team_total | 0.134 | 0.115 | 0.119 | 12 | 89 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA4 | team_total | 0.463 | 0.430 | 0.437 | 44 | 58 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT07PITWSH-4 | game_total | 0.878 | 0.895 | 0.892 | 90 | 11 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT07EDMANA-10 | game_total | 0.141 | 0.120 | 0.124 | 13 | 89 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT07COLWPG-10 | game_total | 0.072 | 0.095 | 0.090 | 11 | 92 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT07EDMANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT07PITWSH-PIT3 | game_spread | 0.121 | 0.135 | 0.132 | 14 | 87 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT07EDMANA-9 | game_total | 0.273 | 0.250 | 0.255 | 26 | 76 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM2 | team_total | 0.852 | 0.870 | 0.867 | 88 | 14 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-8 | game_total | 0.364 | 0.345 | 0.349 | 35 | 66 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-3 | game_total | 0.959 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-3 | game_total | 0.970 | 0.975 | 0.974 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-5 | game_total | 0.802 | 0.815 | 0.812 | 82 | 19 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07EDMANA-ANA3 | game_spread | 0.184 | 0.175 | 0.177 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-7 | game_total | 0.561 | 0.545 | 0.548 | 55 | 46 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-7 | game_total | 0.489 | 0.505 | 0.502 | 51 | 50 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT07COLWPG-WPG3 | game_spread | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA2 | team_total | 0.852 | 0.835 | 0.839 | 85 | 18 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-6 | game_total | 0.600 | 0.615 | 0.612 | 62 | 39 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-5 | game_total | 0.842 | 0.835 | 0.836 | 84 | 17 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM3 | team_total | 0.673 | 0.690 | 0.687 | 70 | 32 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG5 | team_total | 0.150 | 0.165 | 0.162 | 18 | 85 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH3 | game_spread | 0.236 | 0.245 | 0.243 | 25 | 76 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-2 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT5 | team_total | 0.179 | 0.190 | 0.188 | 20 | 82 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-10 | game_total | 0.104 | 0.105 | 0.105 | 11 | 90 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-6 | game_total | 0.666 | 0.655 | 0.657 | 66 | 35 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG3 | team_total | 0.524 | 0.545 | 0.541 | 56 | 47 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-8 | game_total | 0.297 | 0.305 | 0.303 | 31 | 70 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG6 | team_total | 0.060 | 0.065 | 0.064 | 8 | 95 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-4 | game_total | 0.907 | 0.910 | 0.909 | 92 | 10 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH2 | team_total | 0.865 | 0.870 | 0.869 | 88 | 14 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH3 | team_total | 0.689 | 0.700 | 0.698 | 71 | 31 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH2 | game_spread | 0.368 | 0.375 | 0.374 | 38 | 63 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-PIT2 | game_spread | 0.217 | 0.215 | 0.215 | 22 | 79 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT2 | team_total | 0.783 | 0.795 | 0.793 | 81 | 22 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG4 | team_total | 0.310 | 0.320 | 0.318 | 33 | 69 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT07PITWSH-PIT | game_winner | 0.408 | 0.415 | 0.414 | 42 | 59 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT07PITWSH-WSH | game_winner | 0.592 | 0.585 | 0.586 | 59 | 42 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT3 | team_total | 0.569 | 0.580 | 0.578 | 59 | 43 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH4 | team_total | 0.479 | 0.485 | 0.484 | 49 | 52 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM6 | team_total | 0.141 | 0.135 | 0.136 | 15 | 88 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT6 | team_total | 0.077 | 0.075 | 0.075 | 9 | 94 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM5 | team_total | 0.275 | 0.275 | 0.275 | 28 | 73 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH5 | team_total | 0.285 | 0.295 | 0.293 | 31 | 72 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH6 | team_total | 0.139 | 0.135 | 0.136 | 15 | 88 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG2 | team_total | 0.757 | 0.770 | 0.767 | 79 | 25 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-9 | game_total | 0.212 | 0.210 | 0.210 | 22 | 80 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM4 | team_total | 0.464 | 0.465 | 0.465 | 47 | 54 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 | team_total | 0.348 | 0.355 | 0.354 | 37 | 66 |  | -0.023 | NO_EDGE |
| KXNHL1P-26OCT07PITWSH-PIT | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-WSH | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-WSH2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 0.592 | 0.539 | 0.170 | 0.218 | 6.45 | 6.63 | 0.937/1.021 | KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 +0.063 |
| COL @ WPG | 0.416 | 0.434 | 0.177 | 0.220 | 6.03 | 6.29 | 0.988/0.973 | KXNHLTOTAL-26OCT07COLWPG-7 +0.047 |
| EDM @ ANA | 0.499 | 0.492 | 0.167 | 0.215 | 6.90 | 6.86 | 1.024/0.994 | KXNHLTOTAL-26OCT07EDMANA-8 -0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Rickard Rakell: 2+ goals YES @ 4c · p 0.0693 (adj 0.062) · $4.33 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.168 (adj 0.1547) · $7.37 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 20c · p 0.2582 (adj 0.2424) · $9.6 · thesis WSH:OFFENSE_4PLUS
- Boone Jenner: 1+ goals YES @ 14c · p 0.1832 (adj 0.1711) · $6.23 · thesis WSH:OFFENSE_4PLUS
- Morgan Barron: 1+ goals YES @ 8c · p 0.1341 (adj 0.1168) · $7.12 · thesis WPG:OFFENSE_4PLUS
- Josh Morrissey: 2+ goals NO @ 97c · p 0.9945 (adj 0.9871) · $20.0 · thesis DIFFUSE
- Martin Necas: 1+ goals NO @ 64c · p 0.6953 (adj 0.679) · $15.18 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 59c · p 0.6675 (adj 0.6262) · $7.32 · thesis WPG:WINS
- Alex Formenton: 2+ goals YES @ 1c · p 0.0274 (adj 0.0231) · $2.28 · thesis EDM:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1207 (adj 0.1043) · $4.41 · thesis ANA:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1161 (adj 0.1008) · $4.13 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 72c · p 0.8283 (adj 0.7547) · $20.0 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ WSH** · priced 163/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.09, exp saves 24.33 (sd 6.72), pull risk 0.068
- PIT net: Sergei Murashov (PROJECTED) exp shots 26.5, exp saves 22.6 (sd 6.41), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Egor Chinakhov: 1+ assists | 0.351 | 0.200 | 22/82 | +0.119 | STANDARD |
| Alex Tuch: 1+ points | 0.452 | 0.585 | 59/42 | +0.111 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.164 | 0.295 | 31/72 | +0.102 | STANDARD |
| Alex Tuch: 1+ assists | 0.214 | 0.345 | 35/66 | +0.110 | STANDARD |
| Jordan Kyrou: 1+ points | 0.347 | 0.470 | 48/54 | +0.096 | STANDARD |
| Rickard Rakell: 1+ points | 0.603 | 0.485 | 50/53 | +0.085 | STANDARD |

**COL @ WPG** · priced 159/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 30.69, exp saves 26.24 (sd 7.22), pull risk 0.072
- COL net: Scott Wedgewood (PROJECTED) exp shots 26.1, exp saves 22.75 (sd 6.23), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.292 | 0.455 | 47/56 | +0.131 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.457 | 0.615 | 63/40 | +0.126 | STANDARD |
| Cale Makar: 1+ points | 0.512 | 0.655 | 67/36 | +0.111 | STANDARD |
| Cale Makar: 1+ assists | 0.413 | 0.555 | 57/46 | +0.110 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.125 | 0.240 | 26/78 | +0.083 | STANDARD |
| Cale Makar: 2+ assists | 0.101 | 0.210 | 23/81 | +0.078 | STANDARD |

**EDM @ ANA** · priced 156/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 28.22, exp saves 24.29 (sd 6.9), pull risk 0.079
- EDM net: Devon Levi (CONFIRMED) exp shots 29.57, exp saves 25.36 (sd 7.02), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Formenton: 1+ goals | 0.218 | 0.080 | 13/97 | +0.080 | STANDARD |
| Connor McDavid: 1+ assists | 0.518 | 0.650 | 66/36 | +0.106 | STANDARD |
| A.J. Greer: 1+ goals | 0.246 | 0.125 | 17/92 | +0.066 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.463 | 0.580 | 59/43 | +0.090 | STANDARD |
| Connor McDavid: 2+ assists | 0.172 | 0.285 | 29/72 | +0.094 | STANDARD |
| Connor McDavid: 2+ points | 0.395 | 0.505 | 52/51 | +0.077 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
