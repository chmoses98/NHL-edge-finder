# NHL slate 2026-10-07 — RESEARCH_ONLY

generated 2026-10-07T18:54:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2818 · contracts joined: 644 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 569, 'OK': 38, 'NO_EDGE': 37}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 84, 'game_early_goal': 3, 'first_goal': 106, 'game_winner': 6, 'player_goals': 191, 'game_overtime': 3, 'player_points': 106, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 2026-10-07T23:30:00Z | T-3h | 0.611 | 0.389 | 0.166 | 6.58 | 3.64 | 2.93 | 224 (25/199) | CONFIRMED/CONFIRMED |
| COL @ WPG | 2026-10-07T23:30:00Z | T-3h | 0.442 | 0.558 | 0.174 | 6.18 | 2.92 | 3.27 | 211 (25/186) | PROJECTED/PROBABLE |
| EDM @ ANA | 2026-10-08T02:00:00Z | T-6h | 0.497 | 0.503 | 0.165 | 6.91 | 3.44 | 3.47 | 209 (25/184) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL4 | team_total | 0.424 | 0.525 | 0.505 | 53 | 48 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL3 | game_spread | 0.206 | 0.295 | 0.275 | 30 | 71 | no | +0.070 | OK |
| KXNHLGAME-26OCT07COLWPG-WPG | game_winner | 0.442 | 0.355 | 0.372 | 36 | 65 | yes | +0.066 | OK |
| KXNHLGAME-26OCT07COLWPG-COL | game_winner | 0.558 | 0.645 | 0.628 | 65 | 36 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL2 | game_spread | 0.330 | 0.415 | 0.397 | 42 | 59 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 | team_total | 0.643 | 0.720 | 0.705 | 73 | 29 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL5 | team_total | 0.236 | 0.310 | 0.294 | 32 | 70 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG2 | game_spread | 0.239 | 0.185 | 0.195 | 19 | 82 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT07COLWPG-7 | game_total | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT07COLWPG-6 | game_total | 0.558 | 0.615 | 0.604 | 62 | 39 | no | +0.035 | OK |
| KXNHLGAME-26OCT07EDMANA-EDM | game_winner | 0.503 | 0.555 | 0.545 | 56 | 45 | no | +0.029 | OK |
| KXNHLGAME-26OCT07EDMANA-ANA | game_winner | 0.497 | 0.445 | 0.455 | 45 | 56 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL2 | team_total | 0.833 | 0.885 | 0.876 | 90 | 13 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM2 | game_spread | 0.299 | 0.345 | 0.335 | 35 | 66 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT07COLWPG-4 | game_total | 0.850 | 0.890 | 0.883 | 90 | 12 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT07EDMANA-ANA2 | game_spread | 0.294 | 0.255 | 0.263 | 26 | 75 | yes | +0.021 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM3 | game_spread | 0.189 | 0.225 | 0.217 | 23 | 78 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT07COLWPG-5 | game_total | 0.770 | 0.810 | 0.802 | 82 | 20 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA6 | team_total | 0.135 | 0.105 | 0.110 | 11 | 90 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT07COLWPG-8 | game_total | 0.259 | 0.295 | 0.288 | 30 | 71 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL6 | team_total | 0.109 | 0.145 | 0.137 | 16 | 87 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM2 | team_total | 0.851 | 0.875 | 0.871 | 88 | 13 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG3 | game_spread | 0.137 | 0.115 | 0.119 | 12 | 89 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT07EDMANA-10 | game_total | 0.147 | 0.125 | 0.129 | 13 | 88 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT07EDMANA-5 | game_total | 0.844 | 0.865 | 0.861 | 87 | 14 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA5 | team_total | 0.271 | 0.240 | 0.246 | 25 | 77 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT07PITWSH-9 | game_total | 0.229 | 0.205 | 0.210 | 21 | 80 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA4 | team_total | 0.464 | 0.430 | 0.437 | 44 | 58 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT07COLWPG-9 | game_total | 0.182 | 0.210 | 0.204 | 22 | 80 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH5 | team_total | 0.310 | 0.285 | 0.290 | 29 | 72 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT07PITWSH-PIT3 | game_spread | 0.117 | 0.135 | 0.131 | 14 | 87 | no | +0.005 | OK |
| KXNHLGAME-26OCT07PITWSH-PIT | game_winner | 0.389 | 0.415 | 0.410 | 42 | 59 | no | +0.004 | OK |
| KXNHLGAME-26OCT07PITWSH-WSH | game_winner | 0.611 | 0.585 | 0.590 | 59 | 42 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT07COLWPG-10 | game_total | 0.083 | 0.100 | 0.096 | 11 | 91 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH4 | team_total | 0.508 | 0.485 | 0.490 | 49 | 52 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT07EDMANA-9 | game_total | 0.274 | 0.250 | 0.255 | 26 | 76 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT07EDMANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG6 | team_total | 0.075 | 0.060 | 0.063 | 7 | 95 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG4 | team_total | 0.345 | 0.320 | 0.325 | 33 | 69 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG5 | team_total | 0.179 | 0.160 | 0.164 | 17 | 85 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-8 | game_total | 0.363 | 0.345 | 0.349 | 35 | 66 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH6 | team_total | 0.156 | 0.140 | 0.143 | 15 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-4 | game_total | 0.887 | 0.895 | 0.893 | 90 | 11 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-10 | game_total | 0.113 | 0.105 | 0.107 | 11 | 90 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT2 | team_total | 0.782 | 0.795 | 0.792 | 80 | 21 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-7 | game_total | 0.564 | 0.545 | 0.549 | 55 | 46 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-PIT2 | game_spread | 0.203 | 0.215 | 0.212 | 22 | 79 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH2 | game_spread | 0.392 | 0.375 | 0.378 | 38 | 63 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA3 | team_total | 0.671 | 0.645 | 0.650 | 66 | 37 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-3 | game_total | 0.974 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA2 | team_total | 0.853 | 0.840 | 0.843 | 85 | 17 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-2 | game_total | 0.983 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT07EDMANA-ANA3 | game_spread | 0.182 | 0.170 | 0.172 | 18 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG3 | team_total | 0.558 | 0.540 | 0.544 | 55 | 47 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH2 | team_total | 0.877 | 0.875 | 0.875 | 88 | 13 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM5 | team_total | 0.277 | 0.285 | 0.283 | 29 | 72 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM3 | team_total | 0.676 | 0.685 | 0.683 | 69 | 32 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG2 | team_total | 0.781 | 0.770 | 0.772 | 78 | 24 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH3 | team_total | 0.713 | 0.700 | 0.703 | 71 | 31 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-8 | game_total | 0.313 | 0.305 | 0.307 | 31 | 70 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-4 | game_total | 0.906 | 0.910 | 0.909 | 92 | 10 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT3 | team_total | 0.566 | 0.575 | 0.573 | 58 | 43 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-6 | game_total | 0.622 | 0.615 | 0.616 | 62 | 39 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-5 | game_total | 0.814 | 0.815 | 0.815 | 82 | 19 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT6 | team_total | 0.078 | 0.075 | 0.076 | 9 | 94 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-6 | game_total | 0.668 | 0.665 | 0.666 | 67 | 34 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH3 | game_spread | 0.255 | 0.255 | 0.255 | 26 | 75 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT5 | team_total | 0.178 | 0.185 | 0.184 | 20 | 83 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-7 | game_total | 0.509 | 0.505 | 0.506 | 51 | 50 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM6 | team_total | 0.140 | 0.135 | 0.136 | 15 | 88 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM4 | team_total | 0.467 | 0.465 | 0.465 | 47 | 54 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 | team_total | 0.346 | 0.350 | 0.349 | 36 | 66 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT07PITWSH-PIT | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-WSH | period_winner |  | 0.375 |  | 38 | 63 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-PIT2 | period_spread |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-WSH2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 0.611 | 0.547 | 0.166 | 0.213 | 6.58 | 6.68 | 0.937/1.042 | KXNHLGAME-26OCT07PITWSH-PIT +0.064 |
| COL @ WPG | 0.442 | 0.434 | 0.174 | 0.217 | 6.18 | 6.30 | 0.988/0.977 | KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 +0.025 |
| EDM @ ANA | 0.497 | 0.498 | 0.165 | 0.210 | 6.91 | 6.83 | 1.016/0.994 | KXNHLTOTAL-26OCT07EDMANA-6 -0.019 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Rickard Rakell: 1+ goals YES @ 26c · p 0.3504 (adj 0.3266) · $17.12 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 20c · p 0.2651 (adj 0.2476) · $11.05 · thesis WSH:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.17 (adj 0.1562) · $7.28 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1304 (adj 0.1178) · $5.5 · thesis PIT:OFFENSE_4PLUS
- Brad Lambert: 1+ goals YES @ 7c · p 0.1084 (adj 0.0963) · $4.79 · thesis WPG:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 59c · p 0.6523 (adj 0.6342) · $12.84 · thesis COL:SUPPRESSED
- Nazem Kadri: 1+ goals NO @ 73c · p 0.7803 (adj 0.7665) · $17.16 · thesis COL:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 71c · p 0.7836 (adj 0.7443) · $11.44 · thesis WPG:WINS
- A.J. Greer: 1+ goals YES @ 17c · p 0.2459 (adj 0.2244) · $12.12 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 7c · p 0.1193 (adj 0.102) · $5.94 · thesis ANA:OFFENSE_4PLUS
- Alex Formenton: 2+ goals YES @ 1c · p 0.025 (adj 0.0213) · $1.97 · thesis EDM:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 7c · p 0.111 (adj 0.097) · $5.11 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ WSH** · priced 164/173 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.09, exp saves 24.36 (sd 6.71), pull risk 0.067
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.5, exp saves 22.59 (sd 6.38), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Arturs Silovs: 27+ saves | 0.259 | 0.495 | 51/52 | +0.204 |  |
| Egor Chinakhov: 1+ assists | 0.345 | 0.195 | 21/82 | +0.124 | STANDARD |
| Alex Tuch: 1+ assists | 0.215 | 0.365 | 38/65 | +0.119 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.168 | 0.300 | 31/71 | +0.108 | STANDARD |
| Jordan Kyrou: 1+ points | 0.361 | 0.485 | 49/52 | +0.102 | STANDARD |
| Rickard Rakell: 1+ points | 0.608 | 0.495 | 51/52 | +0.080 | STANDARD |

**COL @ WPG** · priced 160/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 30.69, exp saves 26.24 (sd 7.19), pull risk 0.071
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 26.1, exp saves 22.7 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.406 | 0.580 | 59/43 | +0.147 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.454 | 0.625 | 64/39 | +0.140 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.285 | 0.455 | 47/56 | +0.138 | STANDARD |
| Cale Makar: 1+ points | 0.501 | 0.670 | 68/34 | +0.143 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.128 | 0.290 | 30/72 | +0.138 | STANDARD |
| Cale Makar: 2+ points | 0.158 | 0.305 | 32/71 | +0.117 | STANDARD |

**EDM @ ANA** · priced 158/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 28.22, exp saves 24.35 (sd 6.8), pull risk 0.073
- EDM net: Devon Levi (CONFIRMED) exp shots 29.57, exp saves 25.37 (sd 6.92), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.512 | 0.650 | 66/36 | +0.112 | STANDARD |
| Connor McDavid: 2+ assists | 0.159 | 0.290 | 30/72 | +0.107 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.444 | 0.575 | 58/43 | +0.109 | STANDARD |
| Connor McDavid: 2+ points | 0.386 | 0.500 | 51/51 | +0.087 | STANDARD |
| Mattias Ekholm: 1+ points | 0.422 | 0.310 | 32/70 | +0.087 | STANDARD |
| Devon Levi: 24+ saves | 0.613 | 0.505 | 52/51 | +0.075 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
