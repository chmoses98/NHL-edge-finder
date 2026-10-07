# NHL slate 2026-10-07 — RESEARCH_ONLY

generated 2026-10-07T16:16:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2816 · contracts joined: 642 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 567, 'OK': 32, 'NO_EDGE': 43}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 84, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 192, 'game_overtime': 3, 'player_points': 106, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 2026-10-07T23:30:00Z | T-6h | 0.611 | 0.389 | 0.166 | 6.58 | 3.64 | 2.93 | 223 (25/198) | CONFIRMED/CONFIRMED |
| COL @ WPG | 2026-10-07T23:30:00Z | T-6h | 0.442 | 0.558 | 0.174 | 6.18 | 2.92 | 3.27 | 212 (25/187) | PROJECTED/PROBABLE |
| EDM @ ANA | 2026-10-08T02:00:00Z | T-6h | 0.499 | 0.501 | 0.167 | 6.90 | 3.44 | 3.46 | 207 (25/182) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL4 | team_total | 0.424 | 0.515 | 0.497 | 52 | 49 | no | +0.068 | OK |
| KXNHLGAME-26OCT07COLWPG-WPG | game_winner | 0.442 | 0.355 | 0.372 | 36 | 65 | yes | +0.066 | OK |
| KXNHLGAME-26OCT07COLWPG-COL | game_winner | 0.558 | 0.645 | 0.628 | 65 | 36 | no | +0.066 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL2 | game_spread | 0.330 | 0.415 | 0.397 | 42 | 59 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 | team_total | 0.643 | 0.715 | 0.701 | 72 | 29 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT07COLWPG-COL3 | game_spread | 0.206 | 0.275 | 0.260 | 28 | 73 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL5 | team_total | 0.236 | 0.305 | 0.290 | 32 | 71 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG2 | game_spread | 0.239 | 0.185 | 0.195 | 19 | 82 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT07COLWPG-7 | game_total | 0.447 | 0.505 | 0.493 | 51 | 50 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT07COLWPG-4 | game_total | 0.850 | 0.895 | 0.887 | 90 | 11 | no | +0.033 | OK |
| KXNHLGAME-26OCT07EDMANA-ANA | game_winner | 0.499 | 0.445 | 0.456 | 45 | 56 | yes | +0.031 | OK |
| KXNHLGAME-26OCT07EDMANA-EDM | game_winner | 0.501 | 0.555 | 0.544 | 56 | 45 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM2 | game_spread | 0.299 | 0.345 | 0.335 | 35 | 66 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT07COLWPG-6 | game_total | 0.558 | 0.605 | 0.596 | 61 | 40 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT07EDMANA-ANA2 | game_spread | 0.295 | 0.255 | 0.263 | 26 | 75 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT07EDMANA-EDM3 | game_spread | 0.189 | 0.225 | 0.217 | 23 | 78 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT07COLWPG-5 | game_total | 0.770 | 0.810 | 0.802 | 82 | 20 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL2 | team_total | 0.833 | 0.875 | 0.867 | 89 | 14 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT07COLWPG-8 | game_total | 0.259 | 0.295 | 0.288 | 30 | 71 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT07COLWPG-COL6 | team_total | 0.109 | 0.145 | 0.137 | 16 | 87 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT07EDMANA-9 | game_total | 0.273 | 0.245 | 0.251 | 25 | 76 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT07EDMANA-5 | game_total | 0.842 | 0.865 | 0.861 | 87 | 14 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT07COLWPG-WPG3 | game_spread | 0.137 | 0.115 | 0.119 | 12 | 89 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA5 | team_total | 0.271 | 0.240 | 0.246 | 25 | 77 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA6 | team_total | 0.134 | 0.115 | 0.119 | 12 | 89 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA4 | team_total | 0.463 | 0.430 | 0.437 | 44 | 58 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT07PITWSH-PIT3 | game_spread | 0.117 | 0.135 | 0.131 | 14 | 87 | no | +0.005 | OK |
| KXNHLGAME-26OCT07PITWSH-PIT | game_winner | 0.389 | 0.415 | 0.410 | 42 | 59 | no | +0.004 | OK |
| KXNHLGAME-26OCT07PITWSH-WSH | game_winner | 0.611 | 0.585 | 0.590 | 59 | 42 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT07EDMANA-10 | game_total | 0.141 | 0.120 | 0.124 | 13 | 89 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT07EDMANA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH4 | team_total | 0.508 | 0.485 | 0.490 | 49 | 52 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM2 | team_total | 0.852 | 0.870 | 0.867 | 88 | 14 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG4 | team_total | 0.345 | 0.320 | 0.325 | 33 | 69 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG5 | team_total | 0.179 | 0.160 | 0.164 | 17 | 85 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-8 | game_total | 0.364 | 0.345 | 0.349 | 35 | 66 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-9 | game_total | 0.182 | 0.200 | 0.196 | 21 | 81 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-9 | game_total | 0.229 | 0.210 | 0.214 | 22 | 80 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-4 | game_total | 0.887 | 0.895 | 0.893 | 90 | 11 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-10 | game_total | 0.113 | 0.105 | 0.107 | 11 | 90 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA3 | team_total | 0.672 | 0.650 | 0.654 | 66 | 36 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-PIT2 | game_spread | 0.203 | 0.215 | 0.212 | 22 | 79 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH2 | game_spread | 0.392 | 0.375 | 0.378 | 38 | 63 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-3 | game_total | 0.974 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT07EDMANA-ANA3 | game_spread | 0.184 | 0.175 | 0.177 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-7 | game_total | 0.561 | 0.545 | 0.548 | 55 | 46 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-ANA2 | team_total | 0.852 | 0.840 | 0.842 | 85 | 17 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-2 | game_total | 0.983 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT07PITWSH-WSH3 | game_spread | 0.255 | 0.245 | 0.247 | 25 | 76 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM3 | team_total | 0.673 | 0.690 | 0.687 | 70 | 32 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT07COLWPG-10 | game_total | 0.083 | 0.095 | 0.093 | 11 | 92 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT5 | team_total | 0.178 | 0.190 | 0.188 | 20 | 82 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH2 | team_total | 0.877 | 0.870 | 0.871 | 88 | 14 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG6 | team_total | 0.075 | 0.065 | 0.067 | 8 | 95 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH3 | team_total | 0.713 | 0.700 | 0.703 | 71 | 31 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-8 | game_total | 0.313 | 0.305 | 0.307 | 31 | 70 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT3 | team_total | 0.566 | 0.580 | 0.577 | 59 | 43 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH6 | team_total | 0.156 | 0.140 | 0.143 | 16 | 88 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-4 | game_total | 0.907 | 0.910 | 0.909 | 92 | 10 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT2 | team_total | 0.782 | 0.795 | 0.792 | 81 | 22 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-6 | game_total | 0.622 | 0.615 | 0.616 | 62 | 39 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-WSH5 | team_total | 0.310 | 0.295 | 0.298 | 31 | 72 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-5 | game_total | 0.814 | 0.815 | 0.815 | 82 | 19 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT6 | team_total | 0.078 | 0.075 | 0.076 | 9 | 94 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT07PITWSH-7 | game_total | 0.509 | 0.505 | 0.506 | 51 | 50 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM5 | team_total | 0.275 | 0.275 | 0.275 | 28 | 73 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG3 | team_total | 0.558 | 0.545 | 0.548 | 56 | 47 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT07EDMANA-6 | game_total | 0.666 | 0.660 | 0.661 | 67 | 35 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07COLWPG-WPG2 | team_total | 0.781 | 0.770 | 0.772 | 79 | 25 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM4 | team_total | 0.464 | 0.465 | 0.465 | 47 | 54 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07PITWSH-PIT4 | team_total | 0.346 | 0.350 | 0.349 | 36 | 66 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT07EDMANA-EDM6 | team_total | 0.141 | 0.140 | 0.140 | 16 | 88 |  | -0.028 | NO_EDGE |
| KXNHL1P-26OCT07PITWSH-PIT | period_winner |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-TIE | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT07PITWSH-WSH | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-PIT2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT07PITWSH-WSH2 | period_spread |  | 0.135 |  | 16 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ WSH | 0.611 | 0.547 | 0.166 | 0.213 | 6.58 | 6.68 | 0.937/1.042 | KXNHLGAME-26OCT07PITWSH-PIT +0.064 |
| COL @ WPG | 0.442 | 0.434 | 0.174 | 0.217 | 6.18 | 6.30 | 0.988/0.977 | KXNHLTEAMTOTAL-26OCT07COLWPG-COL3 +0.025 |
| EDM @ ANA | 0.499 | 0.492 | 0.167 | 0.215 | 6.90 | 6.86 | 1.024/0.994 | KXNHLTOTAL-26OCT07EDMANA-8 -0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Rickard Rakell: 1+ goals YES @ 26c · p 0.3504 (adj 0.3266) · $17.12 · thesis PIT:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 20c · p 0.2651 (adj 0.2476) · $11.04 · thesis WSH:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.17 (adj 0.1562) · $7.29 · thesis PIT:OFFENSE_4PLUS
- Blake Lizotte: 1+ goals YES @ 9c · p 0.1304 (adj 0.1165) · $5.14 · thesis PIT:OFFENSE_4PLUS
- Morgan Barron: 1+ goals YES @ 9c · p 0.135 (adj 0.12) · $6.0 · thesis WPG:OFFENSE_4PLUS
- Zachary L'Heureux: 1+ goals YES @ 10c · p 0.1436 (adj 0.1277) · $5.42 · thesis COL:OFFENSE_4PLUS
- Martin Necas: 1+ goals NO @ 64c · p 0.699 (adj 0.683) · $18.07 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 60c · p 0.6523 (adj 0.6367) · $11.93 · thesis COL:SUPPRESSED
- Alex Formenton: 2+ goals YES @ 1c · p 0.0274 (adj 0.0231) · $2.23 · thesis EDM:OFFENSE_4PLUS
- Alex Killorn: 1+ assists YES @ 25c · p 0.3444 (adj 0.2947) · $9.06 · thesis ANA:OFFENSE_4PLUS
- Judd Caulfield: 1+ goals YES @ 8c · p 0.1207 (adj 0.1043) · $4.24 · thesis ANA:OFFENSE_4PLUS
- Mattias Ekholm: 1+ goals YES @ 8c · p 0.1161 (adj 0.1008) · $3.65 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ WSH** · priced 163/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.09, exp saves 24.36 (sd 6.71), pull risk 0.067
- PIT net: Arturs Silovs (CONFIRMED) exp shots 26.5, exp saves 22.59 (sd 6.38), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Egor Chinakhov: 1+ assists | 0.345 | 0.200 | 22/82 | +0.113 | STANDARD |
| Alex Tuch: 1+ assists | 0.215 | 0.345 | 36/67 | +0.099 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.168 | 0.295 | 31/72 | +0.098 | STANDARD |
| Jordan Kyrou: 1+ points | 0.361 | 0.485 | 49/52 | +0.102 | STANDARD |
| Rickard Rakell: 1+ points | 0.608 | 0.485 | 50/53 | +0.090 | STANDARD |
| Rickard Rakell: 2+ points | 0.242 | 0.125 | 17/92 | +0.062 | STANDARD |

**COL @ WPG** · priced 161/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 30.69, exp saves 26.24 (sd 7.19), pull risk 0.071
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 26.1, exp saves 22.7 (sd 6.25), pull risk 0.054

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.285 | 0.450 | 47/57 | +0.128 | STANDARD |
| Cale Makar: 1+ points | 0.501 | 0.655 | 67/36 | +0.123 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.454 | 0.605 | 61/40 | +0.130 | STANDARD |
| Cale Makar: 1+ assists | 0.406 | 0.555 | 57/46 | +0.117 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.639 | 0.770 | 80/26 | +0.088 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.128 | 0.245 | 27/78 | +0.080 | STANDARD |

**EDM @ ANA** · priced 156/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (PROJECTED) exp shots 28.22, exp saves 24.29 (sd 6.9), pull risk 0.079
- EDM net: Devon Levi (CONFIRMED) exp shots 29.57, exp saves 25.36 (sd 7.02), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Formenton: 1+ goals | 0.218 | 0.080 | 12/96 | +0.090 | STANDARD |
| Connor McDavid: 1+ assists | 0.518 | 0.650 | 66/36 | +0.106 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.463 | 0.580 | 59/43 | +0.090 | STANDARD |
| A.J. Greer: 1+ goals | 0.246 | 0.130 | 17/91 | +0.066 | STANDARD |
| Connor McDavid: 2+ assists | 0.172 | 0.285 | 29/72 | +0.094 | STANDARD |
| Mattias Ekholm: 1+ points | 0.423 | 0.310 | 33/71 | +0.077 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
