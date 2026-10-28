# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T18:34:56Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3177 · contracts joined: 973 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 873, 'OK': 72, 'NO_EDGE': 28}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 158, 'game_early_goal': 4, 'first_goal': 144, 'game_winner': 8, 'player_goals': 251, 'game_overtime': 4, 'player_points': 212, 'goalie_saves': 4, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 2026-10-28T23:30:00Z | T-3h | 0.655 | 0.345 | 0.167 | 5.96 | 3.48 | 2.49 | 257 (25/232) | PROJECTED/PROJECTED |
| CGY @ EDM | 2026-10-29T00:30:00Z | T-3h | 0.585 | 0.415 | 0.171 | 6.27 | 3.41 | 2.87 | 255 (25/230) | PROJECTED/CONFIRMED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-6h | 0.580 | 0.420 | 0.177 | 6.12 | 3.31 | 2.81 | 234 (25/209) | CONFIRMED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-6h | 0.567 | 0.433 | 0.165 | 6.77 | 3.60 | 3.17 | 227 (25/202) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.433 | 0.565 | 0.539 | 57 | 44 | no | +0.109 | OK |
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.567 | 0.435 | 0.461 | 44 | 57 | yes | +0.109 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.357 | 0.255 | 0.274 | 26 | 75 | yes | +0.083 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.238 | 0.335 | 0.314 | 34 | 67 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.493 | 0.400 | 0.418 | 41 | 61 | yes | +0.066 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.143 | 0.225 | 0.206 | 23 | 78 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.301 | 0.220 | 0.235 | 23 | 79 | yes | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.610 | 0.690 | 0.675 | 70 | 32 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.399 | 0.480 | 0.464 | 49 | 53 | no | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.698 | 0.620 | 0.636 | 63 | 39 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.230 | 0.165 | 0.177 | 17 | 84 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.813 | 0.875 | 0.864 | 88 | 13 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.454 | 0.530 | 0.515 | 54 | 48 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.230 | 0.295 | 0.281 | 30 | 71 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.260 | 0.330 | 0.315 | 34 | 68 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.157 | 0.100 | 0.110 | 11 | 91 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.671 | 0.730 | 0.719 | 74 | 28 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.222 | 0.280 | 0.268 | 29 | 73 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.549 | 0.605 | 0.594 | 61 | 40 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.852 | 0.900 | 0.892 | 91 | 11 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.463 | 0.515 | 0.505 | 52 | 49 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.781 | 0.830 | 0.821 | 84 | 18 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.365 | 0.415 | 0.405 | 42 | 59 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.740 | 0.785 | 0.777 | 79 | 22 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.764 | 0.805 | 0.797 | 81 | 20 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.862 | 0.895 | 0.889 | 90 | 11 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.284 | 0.330 | 0.320 | 34 | 68 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.324 | 0.365 | 0.357 | 37 | 64 | no | +0.020 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.585 | 0.625 | 0.617 | 63 | 38 | no | +0.019 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.415 | 0.375 | 0.383 | 38 | 63 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.267 | 0.305 | 0.297 | 31 | 70 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.575 | 0.620 | 0.611 | 63 | 39 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.867 | 0.830 | 0.838 | 84 | 18 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.125 | 0.160 | 0.152 | 17 | 85 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.836 | 0.865 | 0.859 | 87 | 14 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.764 | 0.795 | 0.789 | 80 | 21 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.428 | 0.465 | 0.458 | 47 | 54 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.838 | 0.865 | 0.860 | 87 | 14 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.860 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.273 | 0.310 | 0.302 | 32 | 70 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.850 | 0.880 | 0.874 | 89 | 13 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.187 | 0.220 | 0.213 | 23 | 79 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.472 | 0.505 | 0.498 | 51 | 50 | no | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.655 | 0.685 | 0.679 | 69 | 32 | no | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.345 | 0.315 | 0.321 | 32 | 69 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.122 | 0.145 | 0.140 | 15 | 86 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.896 | 0.915 | 0.912 | 92 | 9 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.960 | 0.975 | 0.973 | 98 | 3 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.435 | 0.465 | 0.459 | 47 | 54 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.105 | 0.130 | 0.125 | 14 | 88 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.343 | 0.310 | 0.316 | 32 | 70 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.124 | 0.105 | 0.109 | 11 | 90 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.218 | 0.190 | 0.195 | 20 | 82 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT28NJCOL-10 | game_total | 0.077 | 0.095 | 0.091 | 10 | 91 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.134 | 0.110 | 0.115 | 12 | 90 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-9 | game_total | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.222 | 0.245 | 0.240 | 25 | 76 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.174 | 0.195 | 0.191 | 20 | 81 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.691 | 0.715 | 0.710 | 72 | 29 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.089 | 0.105 | 0.102 | 11 | 90 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.252 | 0.280 | 0.274 | 29 | 73 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.650 | 0.680 | 0.674 | 69 | 33 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.539 | 0.565 | 0.560 | 57 | 44 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.828 | 0.850 | 0.846 | 86 | 16 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.158 | 0.180 | 0.175 | 19 | 83 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.966 | 0.975 | 0.973 | 98 | 3 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-8 | game_total | 0.226 | 0.245 | 0.241 | 25 | 76 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.246 | 0.270 | 0.265 | 28 | 74 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.957 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.253 | 0.235 | 0.239 | 24 | 77 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.150 | 0.146 | 16 | 86 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI6 | team_total | 0.041 | 0.035 | 0.036 | 4 | 97 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.221 | 0.235 | 0.232 | 24 | 77 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL6 | team_total | 0.117 | 0.125 | 0.123 | 13 | 88 |  | -0.005 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.655 | 0.557 | 0.167 | 0.224 | 5.96 | 6.00 | 0.961/0.992 | KXNHLSPREAD-26OCT28PHIWSH-WSH2 -0.102 |
| CGY @ EDM | 0.585 | 0.663 | 0.171 | 0.195 | 6.27 | 6.71 | 1.009/0.978 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.111 |
| NJD @ COL | 0.580 | 0.625 | 0.177 | 0.215 | 6.12 | 6.34 | 0.979/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.061 |
| TOR @ SEA | 0.567 | 0.546 | 0.165 | 0.214 | 6.77 | 6.61 | 1.019/0.965 | KXNHLSPREAD-26OCT28TORSEA-SEA2 -0.029 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 17c · p 0.2393 (adj 0.2207) · $11.36 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 10c · p 0.145 (adj 0.1325) · $6.47 · thesis PHI:OFFENSE_4PLUS
- Cole Knuble: 1+ goals YES @ 12c · p 0.1654 (adj 0.149) · $5.47 · thesis PHI:OFFENSE_4PLUS
- Jordan Kyrou: 1+ goals NO @ 74c · p 0.7843 (adj 0.772) · $19.44 · thesis WSH:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 13c · p 0.2014 (adj 0.1785) · $9.99 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 8c · p 0.1111 (adj 0.0996) · $3.32 · thesis CGY:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 32c · p 0.3699 (adj 0.3562) · $7.17 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ goals YES @ 46c · p 0.5099 (adj 0.4962) · $8.35 · thesis EDM:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1233 (adj 0.1137) · $4.44 · thesis NJD:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 68c · p 0.723 (adj 0.711) · $12.82 · thesis NJD:SUPPRESSED
- Timo Meier: 1+ goals NO @ 76c · p 0.7971 (adj 0.7866) · $15.35 · thesis NJD:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 28c · p 0.3185 (adj 0.3076) · $4.51 · thesis COL:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.162 (adj 0.1465) · $8.19 · thesis TOR:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1649 (adj 0.1549) · $3.98 · thesis SEA:OFFENSE_4PLUS
- Toronto wins by over 1.5 goals NO @ 67c · p 0.7503 (adj 0.7077) · $12.95 · thesis SEA:WINS
- Toronto wins by over 2.5 goals NO @ 78c · p 0.8474 (adj 0.8112) · $16.21 · thesis SEA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 195/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.27 (sd 6.06), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 27.44, exp saves 23.58 (sd 6.57), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joseph Woll: 28+ saves | 0.263 | 0.445 | 50/61 | +0.111 |  |
| Martin Fehervary: 1+ assists | 0.290 | 0.115 | 21/98 | +0.069 | STANDARD |
| Martin Fehervary: 1+ points | 0.326 | 0.225 | 25/80 | +0.063 | STANDARD |
| Timothy Liljegren: 1+ points | 0.208 | 0.110 | 17/95 | +0.028 | STANDARD |
| Noah Cates: 1+ points | 0.362 | 0.265 | 28/75 | +0.068 | STANDARD |
| Jordan Kyrou: 1+ points | 0.447 | 0.540 | 55/47 | +0.066 | STANDARD |

**CGY @ EDM** · priced 194/204 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.03, exp saves 23.75 (sd 6.49), pull risk 0.051
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.57, exp saves 25.62 (sd 7.41), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Bahl: 1+ assists | 0.260 | 0.115 | 21/98 | +0.039 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.306 | 0.165 | 21/88 | +0.084 | STANDARD |
| Owen Michaels: 1+ points | 0.303 | 0.165 | 23/90 | +0.061 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.481 | 0.355 | 36/65 | +0.104 | STANDARD |
| Zach Whitecloud: 1+ assists | 0.199 | 0.075 | 13/98 | +0.061 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.320 | 0.210 | 23/81 | +0.078 | STANDARD |

**NJD @ COL** · priced 182/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 28.33, exp saves 24.84 (sd 6.56), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.75 (sd 6.93), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.223 | 0.345 | 36/67 | +0.092 | STANDARD |
| Jack Hughes: 1+ assists | 0.354 | 0.465 | 48/55 | +0.078 | STANDARD |
| Nicolas Roy: 1+ assists | 0.100 | 0.205 | 22/81 | +0.079 | STANDARD |
| Jake Allen: 27+ saves | 0.397 | 0.500 | 52/52 | +0.066 |  |
| Jack Hughes: 1+ points | 0.529 | 0.630 | 64/38 | +0.074 | STANDARD |
| Mackenzie Blackwood: 27+ saves | 0.385 | 0.485 | 51/54 | +0.058 |  |

**TOR @ SEA** · priced 170/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROBABLE) exp shots 28.75, exp saves 24.79 (sd 6.82), pull risk 0.069
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.18, exp saves 25.7 (sd 7.07), pull risk 0.077

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.399 | 0.495 | 51/52 | +0.064 | STANDARD |
| Kaapo Kakko: 1+ points | 0.514 | 0.425 | 44/59 | +0.057 | STANDARD |
| Auston Matthews: 2+ points | 0.274 | 0.360 | 38/66 | +0.051 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.384 | 0.300 | 31/71 | +0.059 | STANDARD |
| Gavin McKenna: 1+ points | 0.414 | 0.495 | 51/52 | +0.049 | STANDARD |
| Nick Paul: 1+ points | 0.321 | 0.395 | 42/63 | +0.033 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
