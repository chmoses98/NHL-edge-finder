# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T17:44:59Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3168 · contracts joined: 964 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 864, 'OK': 70, 'NO_EDGE': 30}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 154, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 252, 'game_overtime': 4, 'player_points': 207, 'game_spread': 16, 'team_total': 40, 'game_total': 36, 'goalie_saves': 2}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 2026-10-28T23:30:00Z | T-3h | 0.655 | 0.345 | 0.167 | 5.96 | 3.48 | 2.49 | 260 (25/235) | PROJECTED/PROJECTED |
| CGY @ EDM | 2026-10-29T00:30:00Z | T-6h | 0.585 | 0.415 | 0.171 | 6.27 | 3.41 | 2.87 | 244 (25/219) | PROJECTED/CONFIRMED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-6h | 0.578 | 0.422 | 0.177 | 6.14 | 3.32 | 2.82 | 233 (25/208) | PROBABLE/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-6h | 0.564 | 0.436 | 0.165 | 6.79 | 3.60 | 3.18 | 227 (25/202) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.564 | 0.435 | 0.461 | 44 | 57 | yes | +0.106 | OK |
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.436 | 0.555 | 0.531 | 56 | 45 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.351 | 0.255 | 0.273 | 26 | 75 | yes | +0.078 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.243 | 0.335 | 0.315 | 34 | 67 | no | +0.071 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.493 | 0.400 | 0.418 | 41 | 61 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.144 | 0.225 | 0.206 | 23 | 78 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.300 | 0.220 | 0.235 | 23 | 79 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.698 | 0.620 | 0.636 | 63 | 39 | yes | +0.052 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.230 | 0.165 | 0.177 | 17 | 84 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.403 | 0.480 | 0.464 | 49 | 53 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.454 | 0.530 | 0.515 | 54 | 48 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.616 | 0.690 | 0.676 | 70 | 32 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.230 | 0.295 | 0.281 | 30 | 71 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.260 | 0.330 | 0.315 | 34 | 68 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.814 | 0.870 | 0.860 | 88 | 14 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.437 | 0.495 | 0.483 | 50 | 51 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.671 | 0.730 | 0.719 | 74 | 28 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.223 | 0.280 | 0.268 | 29 | 73 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.551 | 0.605 | 0.594 | 61 | 40 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.852 | 0.900 | 0.892 | 91 | 11 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.157 | 0.105 | 0.114 | 12 | 91 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.463 | 0.515 | 0.505 | 52 | 49 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.781 | 0.825 | 0.817 | 83 | 18 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.365 | 0.415 | 0.405 | 42 | 59 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.740 | 0.785 | 0.777 | 79 | 22 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.764 | 0.805 | 0.797 | 81 | 20 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.273 | 0.315 | 0.306 | 32 | 69 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.862 | 0.895 | 0.889 | 90 | 11 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.284 | 0.330 | 0.320 | 34 | 68 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.870 | 0.830 | 0.839 | 84 | 18 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-8 | game_total | 0.226 | 0.265 | 0.257 | 27 | 74 | no | +0.020 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.585 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.415 | 0.375 | 0.383 | 38 | 63 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.267 | 0.305 | 0.297 | 31 | 70 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.575 | 0.620 | 0.611 | 63 | 39 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.125 | 0.160 | 0.152 | 17 | 85 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.836 | 0.865 | 0.859 | 87 | 14 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.860 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.850 | 0.880 | 0.874 | 89 | 13 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.347 | 0.310 | 0.317 | 32 | 70 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.187 | 0.220 | 0.213 | 23 | 79 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.841 | 0.865 | 0.860 | 87 | 14 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.768 | 0.795 | 0.790 | 80 | 21 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.472 | 0.505 | 0.498 | 51 | 50 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.432 | 0.465 | 0.458 | 47 | 54 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.121 | 0.145 | 0.140 | 15 | 86 | no | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.345 | 0.315 | 0.321 | 32 | 69 | yes | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.655 | 0.685 | 0.679 | 69 | 32 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.324 | 0.360 | 0.353 | 37 | 65 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.895 | 0.915 | 0.911 | 92 | 9 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.136 | 0.110 | 0.115 | 12 | 90 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.124 | 0.105 | 0.109 | 11 | 90 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.218 | 0.190 | 0.195 | 20 | 82 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.526 | 0.555 | 0.549 | 56 | 45 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.221 | 0.245 | 0.240 | 25 | 76 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-9 | game_total | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.106 | 0.135 | 0.129 | 15 | 88 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.962 | 0.975 | 0.973 | 98 | 3 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.174 | 0.195 | 0.191 | 20 | 81 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.155 | 0.180 | 0.175 | 19 | 83 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.691 | 0.715 | 0.710 | 72 | 29 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.650 | 0.680 | 0.674 | 69 | 33 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.089 | 0.105 | 0.102 | 11 | 90 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.428 | 0.455 | 0.450 | 46 | 55 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.253 | 0.280 | 0.274 | 29 | 73 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.256 | 0.235 | 0.239 | 24 | 77 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.966 | 0.980 | 0.978 | 99 | 3 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-7 | game_total | 0.412 | 0.435 | 0.430 | 44 | 57 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.957 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.831 | 0.845 | 0.842 | 85 | 16 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT28PHIWSH-PHI3 | game_spread | 0.085 | 0.095 | 0.093 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.150 | 0.146 | 16 | 86 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.247 | 0.270 | 0.265 | 28 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.544 | 0.565 | 0.561 | 57 | 44 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI6 | team_total | 0.041 | 0.035 | 0.036 | 4 | 97 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.219 | 0.235 | 0.232 | 24 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-10 | game_total | 0.078 | 0.090 | 0.088 | 10 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.655 | 0.557 | 0.167 | 0.224 | 5.96 | 6.00 | 0.961/0.992 | KXNHLSPREAD-26OCT28PHIWSH-WSH2 -0.102 |
| CGY @ EDM | 0.585 | 0.663 | 0.171 | 0.195 | 6.27 | 6.71 | 1.009/0.978 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.111 |
| NJD @ COL | 0.578 | 0.624 | 0.177 | 0.207 | 6.14 | 6.32 | 0.978/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.064 |
| TOR @ SEA | 0.564 | 0.551 | 0.165 | 0.214 | 6.79 | 6.60 | 1.016/0.965 | KXNHLTOTAL-26OCT28TORSEA-8 -0.032 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2393 (adj 0.222) · $10.11 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 11c · p 0.145 (adj 0.1325) · $3.82 · thesis PHI:OFFENSE_4PLUS
- Washington over 3.5 goals scored NO @ 50c · p 0.5866 (adj 0.5408) · $14.13 · thesis WSH:SUPPRESSED
- Jordan Kyrou: 1+ goals NO @ 74c · p 0.7843 (adj 0.772) · $13.21 · thesis WSH:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 14c · p 0.2014 (adj 0.1835) · $9.06 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ goals YES @ 11c · p 0.1623 (adj 0.1467) · $7.7 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 8c · p 0.1116 (adj 0.1) · $3.39 · thesis CGY:OFFENSE_4PLUS
- Ryan Nugent-Hopkins: 1+ assists NO @ 60c · p 0.6835 (adj 0.6367) · $16.1 · thesis EDM:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 28c · p 0.3276 (adj 0.3145) · $6.74 · thesis COL:OFFENSE_4PLUS
- Connor Brown: 1+ goals YES @ 13c · p 0.1608 (adj 0.1518) · $3.66 · thesis NJD:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1149 (adj 0.1074) · $2.9 · thesis NJD:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 76c · p 0.7968 (adj 0.7863) · $14.48 · thesis NJD:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1662 (adj 0.1472) · $9.44 · thesis TOR:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 16c · p 0.2235 (adj 0.2051) · $9.39 · thesis SEA:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 75c · p 0.8116 (adj 0.795) · $19.1 · thesis TOR:SUPPRESSED
- Mackie Samoskevich: 1+ goals YES @ 20c · p 0.2478 (adj 0.2346) · $6.77 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 198/209 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.27 (sd 6.06), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 27.44, exp saves 23.58 (sd 6.57), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Martin Fehervary: 1+ assists | 0.290 | 0.115 | 21/98 | +0.069 | STANDARD |
| Matt Roy: 1+ assists | 0.203 | 0.100 | 18/98 | +0.013 | STANDARD |
| Martin Fehervary: 1+ points | 0.326 | 0.225 | 25/80 | +0.063 | STANDARD |
| Timothy Liljegren: 1+ assists | 0.172 | 0.075 | 13/98 | +0.034 | STANDARD |
| Noah Cates: 1+ points | 0.362 | 0.270 | 28/74 | +0.068 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.274 | 0.365 | 38/65 | +0.060 | STANDARD |

**CGY @ EDM** · priced 183/193 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.03, exp saves 23.75 (sd 6.49), pull risk 0.051
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.57, exp saves 25.62 (sd 7.41), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Bahl: 1+ assists | 0.257 | 0.115 | 21/98 | +0.035 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.217 | 0.075 | 13/98 | +0.079 | STANDARD |
| Zach Whitecloud: 1+ points | 0.253 | 0.120 | 15/91 | +0.094 | STANDARD |
| Adam Klapka: 1+ points | 0.314 | 0.185 | 27/90 | +0.030 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.481 | 0.355 | 36/65 | +0.104 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.306 | 0.185 | 19/82 | +0.105 | STANDARD |

**NJD @ COL** · priced 175/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROBABLE) exp shots 28.33, exp saves 24.85 (sd 6.6), pull risk 0.047
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.76 (sd 6.91), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.216 | 0.345 | 36/67 | +0.098 | STANDARD |
| Jack Hughes: 1+ assists | 0.359 | 0.465 | 48/55 | +0.073 | STANDARD |
| Luke Evangelista: 1+ points | 0.370 | 0.465 | 48/55 | +0.063 | STANDARD |
| Jack Hughes: 1+ points | 0.542 | 0.630 | 64/38 | +0.062 | STANDARD |
| Jack Hughes: 2+ points | 0.183 | 0.265 | 28/75 | +0.054 | STANDARD |
| Nico Hischier: 1+ assists | 0.292 | 0.370 | 38/64 | +0.052 | STANDARD |

**TOR @ SEA** · priced 170/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.75, exp saves 24.83 (sd 6.78), pull risk 0.065
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.18, exp saves 25.72 (sd 7.05), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.393 | 0.500 | 51/51 | +0.079 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.385 | 0.300 | 31/71 | +0.060 | STANDARD |
| William Nylander: 1+ assists | 0.396 | 0.480 | 50/54 | +0.046 | STANDARD |
| Auston Matthews: 2+ points | 0.283 | 0.365 | 38/65 | +0.051 | STANDARD |
| Freddy Gaudreau: 1+ goals | 0.161 | 0.085 | 15/98 | +0.002 | STANDARD |
| Teddy Blueger: 1+ goals | 0.166 | 0.090 | 10/92 | +0.060 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
