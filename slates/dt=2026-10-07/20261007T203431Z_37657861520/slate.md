# NHL slate 2026-10-07 — RESEARCH_ONLY

generated 2026-10-07T20:34:31Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2831 · contracts joined: 644 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 569, 'OK': 38, 'NO_EDGE': 37}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 84, 'game_early_goal': 3, 'first_goal': 106, 'game_winner': 6, 'player_goals': 191, 'game_overtime': 3, 'player_points': 106, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 2026-10-07T23:30:00Z | T-90m | 0.611 | 0.389 | 0.166 | 6.58 | 3.64 | 2.93 | 224 (25/199) | CONFIRMED/CONFIRMED |
| COL @ WPG | 2026-10-07T23:30:00Z | T-90m | 0.442 | 0.558 | 0.174 | 6.18 | 2.92 | 3.27 | 211 (25/186) | PROJECTED/PROBABLE |
| EDM @ ANA | 2026-10-08T02:00:00Z | T-3h | 0.497 | 0.503 | 0.165 | 6.91 | 3.44 | 3.47 | 209 (25/184) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL4 | team_total | 0.424 | 0.525 | 0.505 | 53 | 48 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL3 | game_spread | 0.206 | 0.295 | 0.275 | 30 | 71 | no | +0.070 | OK |
| KXNHLGAME-26OCT07COLWPG-WPG | game_winner | 0.442 | 0.355 | 0.372 | 36 | 65 | yes | +0.066 | OK |
| KXNHLGAME-26OCT07COLWPG-COL | game_winner | 0.558 | 0.645 | 0.628 | 65 | 36 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 | team_total | 0.643 | 0.725 | 0.709 | 73 | 28 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL2 | game_spread | 0.330 | 0.415 | 0.397 | 42 | 59 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL5 | team_total | 0.236 | 0.315 | 0.298 | 32 | 69 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL2 | team_total | 0.833 | 0.895 | 0.884 | 90 | 11 | no | +0.050 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG2 | game_spread | 0.239 | 0.185 | 0.195 | 19 | 82 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT07COLWPG-7 | game_total | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT07COLWPG-6 | game_total | 0.558 | 0.615 | 0.604 | 62 | 39 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL6 | team_total | 0.109 | 0.155 | 0.145 | 16 | 85 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT07COLWPG-5 | game_total | 0.770 | 0.815 | 0.807 | 82 | 19 | no | +0.029 | OK |
| KXNHLGAME-26OCT07EDMANA-EDM | game_winner | 0.503 | 0.555 | 0.545 | 56 | 45 | no | +0.029 | OK |
| KXNHLGAME-26OCT07EDMANA-ANA | game_winner | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM2 | game_spread | 0.299 | 0.345 | 0.335 | 35 | 66 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT07COLWPG-4 | game_total | 0.850 | 0.890 | 0.883 | 90 | 12 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT07EDMANA-ANA2 | game_spread | 0.294 | 0.255 | 0.263 | 26 | 75 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM3 | game_spread | 0.189 | 0.225 | 0.217 | 23 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA6 | team_total | 0.135 | 0.105 | 0.110 | 11 | 90 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT07COLWPG-8 | game_total | 0.259 | 0.295 | 0.288 | 30 | 71 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT07COLWPG-9 | game_total | 0.182 | 0.215 | 0.208 | 22 | 79 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT07EDMANA-9 | game_total | 0.274 | 0.245 | 0.251 | 25 | 76 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM2 | team_total | 0.851 | 0.875 | 0.871 | 88 | 13 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG3 | game_spread | 0.137 | 0.115 | 0.119 | 12 | 89 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT07EDMANA-10 | game_total | 0.147 | 0.125 | 0.129 | 13 | 88 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT07EDMANA-5 | game_total | 0.844 | 0.865 | 0.861 | 87 | 14 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA5 | team_total | 0.271 | 0.245 | 0.250 | 25 | 76 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA4 | team_total | 0.464 | 0.430 | 0.437 | 44 | 58 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH5 | team_total | 0.310 | 0.285 | 0.290 | 29 | 72 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT07PITWSH-PIT3 | game_spread | 0.117 | 0.135 | 0.131 | 14 | 87 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA3 | team_total | 0.671 | 0.645 | 0.650 | 65 | 36 | yes | +0.005 | OK |
| KXNHLGAME-26OCT07PITWSH-PIT | game_winner | 0.389 | 0.415 | 0.410 | 42 | 59 | no | +0.004 | OK |
| KXNHLGAME-26OCT07PITWSH-WSH | game_winner | 0.611 | 0.585 | 0.590 | 59 | 42 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT07COLWPG-10 | game_total | 0.083 | 0.100 | 0.096 | 11 | 91 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH4 | team_total | 0.508 | 0.485 | 0.490 | 49 | 52 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT07EDMANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG6 | team_total | 0.075 | 0.060 | 0.063 | 7 | 95 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG4 | team_total | 0.345 | 0.320 | 0.325 | 33 | 69 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG5 | team_total | 0.179 | 0.160 | 0.164 | 17 | 85 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-8 | game_total | 0.313 | 0.295 | 0.299 | 30 | 71 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-4 | game_total | 0.906 | 0.915 | 0.913 | 92 | 9 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-8 | game_total | 0.363 | 0.345 | 0.349 | 35 | 66 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH6 | team_total | 0.156 | 0.140 | 0.143 | 15 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-9 | game_total | 0.229 | 0.210 | 0.214 | 22 | 80 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-4 | game_total | 0.887 | 0.895 | 0.893 | 90 | 11 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-10 | game_total | 0.113 | 0.100 | 0.103 | 11 | 91 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT2 | team_total | 0.782 | 0.800 | 0.796 | 81 | 21 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-7 | game_total | 0.564 | 0.545 | 0.549 | 55 | 46 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-PIT2 | game_spread | 0.203 | 0.215 | 0.212 | 22 | 79 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-5 | game_total | 0.814 | 0.825 | 0.823 | 83 | 18 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH2 | game_spread | 0.392 | 0.375 | 0.378 | 38 | 63 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-3 | game_total | 0.974 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA2 | team_total | 0.853 | 0.840 | 0.843 | 85 | 17 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT07EDMANA-ANA3 | game_spread | 0.182 | 0.170 | 0.172 | 18 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG3 | team_total | 0.558 | 0.540 | 0.544 | 55 | 47 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH2 | team_total | 0.877 | 0.875 | 0.875 | 88 | 13 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM5 | team_total | 0.277 | 0.285 | 0.283 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM3 | team_total | 0.676 | 0.685 | 0.683 | 69 | 32 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG2 | team_total | 0.781 | 0.770 | 0.772 | 78 | 24 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH3 | team_total | 0.713 | 0.700 | 0.703 | 71 | 31 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT6 | team_total | 0.078 | 0.080 | 0.080 | 9 | 93 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT3 | team_total | 0.566 | 0.575 | 0.573 | 58 | 43 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-6 | game_total | 0.622 | 0.615 | 0.616 | 62 | 39 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-6 | game_total | 0.668 | 0.665 | 0.666 | 67 | 34 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM6 | team_total | 0.140 | 0.145 | 0.144 | 16 | 87 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH3 | game_spread | 0.255 | 0.255 | 0.255 | 26 | 75 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT5 | team_total | 0.178 | 0.180 | 0.180 | 19 | 83 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-7 | game_total | 0.509 | 0.505 | 0.506 | 51 | 50 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM4 | team_total | 0.467 | 0.465 | 0.465 | 47 | 54 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 | team_total | 0.346 | 0.350 | 0.349 | 36 | 66 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT07PITWSH-PIT | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-WSH | period_winner |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-PIT2 | period_spread |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-WSH2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 0.611 | 0.547 | 0.166 | 0.213 | 6.58 | 6.68 | 0.937/1.042 | KXNHLGAME-26OCT07PITWSH-PIT +0.064 |
| COL @ WPG | 0.442 | 0.434 | 0.174 | 0.217 | 6.18 | 6.30 | 0.988/0.977 | KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 +0.025 |
| EDM @ ANA | 0.497 | 0.498 | 0.165 | 0.210 | 6.91 | 6.83 | 1.016/0.994 | KXNHLTOTAL-26OCT07EDMANA-6 -0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Rickard Rakell: 1+ goals YES @ 27c · p 0.3504 (adj 0.3291) · $14.91 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 20c · p 0.2651 (adj 0.2476) · $11.06 · thesis WSH:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.17 (adj 0.1562) · $7.32 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1304 (adj 0.119) · $5.87 · thesis PIT:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 58c · p 0.6523 (adj 0.6317) · $18.59 · thesis COL:SUPPRESSED
- Alex Iafallo: 1+ goals YES @ 13c · p 0.1744 (adj 0.162) · $6.3 · thesis WPG:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 71c · p 0.7836 (adj 0.7443) · $10.35 · thesis WPG:WINS
- Martin Necas: 1+ goals NO @ 65c · p 0.699 (adj 0.6843) · $11.41 · thesis COL:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 12c · p 0.2125 (adj 0.1881) · $14.68 · thesis EDM:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2459 (adj 0.2232) · $14.19 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 7c · p 0.1193 (adj 0.1032) · $6.02 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 7c · p 0.1097 (adj 0.0985) · $5.67 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ WSH** · priced 164/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.09, exp saves 24.36 (sd 6.71), pull risk 0.067
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.5, exp saves 22.59 (sd 6.38), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 27+ saves | 0.259 | 0.470 | 50/56 | +0.164 |  |
| Alex Tuch: 1+ assists | 0.215 | 0.370 | 38/64 | +0.129 | STANDARD |
| Egor Chinakhov: 1+ assists | 0.345 | 0.210 | 22/80 | +0.113 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.168 | 0.300 | 31/71 | +0.108 | STANDARD |
| Jordan Kyrou: 1+ points | 0.361 | 0.485 | 49/52 | +0.102 | STANDARD |
| Egor Chinakhov: 1+ points | 0.496 | 0.390 | 40/62 | +0.079 | STANDARD |

**COL @ WPG** · priced 160/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 30.69, exp saves 26.24 (sd 7.19), pull risk 0.071
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 26.1, exp saves 22.7 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.285 | 0.470 | 48/54 | +0.157 | STANDARD |
| Cale Makar: 1+ assists | 0.406 | 0.585 | 59/42 | +0.157 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.454 | 0.625 | 63/38 | +0.150 | STANDARD |
| Cale Makar: 1+ points | 0.501 | 0.665 | 67/34 | +0.143 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.128 | 0.280 | 29/73 | +0.128 | STANDARD |
| Cale Makar: 2+ points | 0.158 | 0.310 | 32/70 | +0.127 | STANDARD |

**EDM @ ANA** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 28.22, exp saves 24.35 (sd 6.8), pull risk 0.073
- EDM net: Devon Levi (CONFIRMED) exp shots 29.57, exp saves 25.37 (sd 6.92), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.512 | 0.670 | 68/34 | +0.132 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.444 | 0.575 | 58/43 | +0.109 | STANDARD |
| Connor McDavid: 2+ assists | 0.159 | 0.285 | 30/73 | +0.097 | STANDARD |
| Connor McDavid: 2+ points | 0.386 | 0.500 | 51/51 | +0.087 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.310 | 32/70 | +0.087 | STANDARD |
| Devon Levi: 24+ saves | 0.613 | 0.510 | 52/50 | +0.075 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
