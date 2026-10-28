# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T22:13:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3288 · contracts joined: 970 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 870, 'OK': 65, 'NO_EDGE': 35}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 158, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 247, 'game_overtime': 4, 'player_points': 212, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 2026-10-28T23:30:00Z | T-60m | 0.661 | 0.339 | 0.167 | 5.99 | 3.50 | 2.48 | 257 (25/232) | PROJECTED/CONFIRMED |
| CGY @ EDM | 2026-10-29T00:30:00Z | T-90m | 0.576 | 0.424 | 0.175 | 6.33 | 3.41 | 2.92 | 253 (25/228) | CONFIRMED/CONFIRMED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-90m | 0.578 | 0.422 | 0.173 | 6.13 | 3.31 | 2.81 | 231 (25/206) | CONFIRMED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-3h | 0.572 | 0.428 | 0.165 | 6.84 | 3.67 | 3.17 | 229 (25/204) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.428 | 0.555 | 0.530 | 56 | 45 | no | +0.105 | OK |
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.572 | 0.445 | 0.470 | 45 | 56 | yes | +0.105 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.367 | 0.255 | 0.275 | 26 | 75 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.235 | 0.335 | 0.313 | 34 | 67 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.314 | 0.220 | 0.237 | 23 | 79 | yes | +0.072 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.137 | 0.225 | 0.205 | 23 | 78 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.241 | 0.165 | 0.178 | 17 | 84 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.508 | 0.425 | 0.441 | 43 | 58 | yes | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.711 | 0.625 | 0.643 | 64 | 39 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.223 | 0.295 | 0.280 | 30 | 71 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.613 | 0.685 | 0.671 | 69 | 32 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.166 | 0.100 | 0.111 | 11 | 91 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.455 | 0.530 | 0.515 | 54 | 48 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.399 | 0.470 | 0.456 | 48 | 54 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.813 | 0.870 | 0.860 | 88 | 14 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.354 | 0.415 | 0.403 | 42 | 59 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.260 | 0.325 | 0.311 | 34 | 69 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.671 | 0.735 | 0.723 | 75 | 28 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.765 | 0.815 | 0.806 | 82 | 19 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.438 | 0.495 | 0.484 | 50 | 51 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.787 | 0.835 | 0.826 | 84 | 17 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.551 | 0.605 | 0.594 | 61 | 40 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.851 | 0.900 | 0.892 | 91 | 11 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.218 | 0.275 | 0.263 | 29 | 74 | no | +0.029 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.424 | 0.375 | 0.385 | 38 | 63 | yes | +0.027 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.576 | 0.625 | 0.615 | 63 | 38 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.876 | 0.830 | 0.840 | 84 | 18 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.746 | 0.785 | 0.778 | 79 | 22 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.585 | 0.625 | 0.617 | 63 | 38 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.286 | 0.325 | 0.317 | 33 | 68 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.353 | 0.315 | 0.323 | 32 | 69 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.867 | 0.895 | 0.890 | 90 | 11 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.227 | 0.195 | 0.201 | 20 | 81 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.126 | 0.160 | 0.153 | 17 | 85 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.837 | 0.865 | 0.860 | 87 | 14 | no | +0.014 | OK |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.339 | 0.305 | 0.312 | 31 | 70 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.141 | 0.110 | 0.116 | 12 | 90 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.321 | 0.360 | 0.352 | 37 | 65 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.850 | 0.880 | 0.874 | 89 | 13 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.431 | 0.465 | 0.458 | 47 | 54 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.841 | 0.865 | 0.860 | 87 | 14 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.198 | 0.225 | 0.219 | 23 | 78 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.696 | 0.725 | 0.719 | 73 | 28 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.263 | 0.235 | 0.240 | 24 | 77 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.104 | 0.125 | 0.120 | 13 | 88 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.864 | 0.890 | 0.885 | 90 | 12 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.277 | 0.305 | 0.299 | 31 | 70 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.172 | 0.195 | 0.190 | 20 | 81 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.435 | 0.465 | 0.459 | 47 | 54 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.248 | 0.275 | 0.270 | 28 | 73 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.647 | 0.680 | 0.674 | 69 | 33 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY3 | team_total | 0.564 | 0.535 | 0.541 | 54 | 47 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT28NJCOL-10 | game_total | 0.079 | 0.095 | 0.092 | 10 | 91 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.963 | 0.975 | 0.973 | 98 | 3 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.528 | 0.555 | 0.550 | 56 | 45 | no | +0.004 | OK |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.661 | 0.685 | 0.680 | 69 | 32 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.901 | 0.915 | 0.912 | 92 | 9 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.765 | 0.790 | 0.785 | 80 | 22 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.224 | 0.245 | 0.241 | 25 | 76 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.157 | 0.180 | 0.175 | 19 | 83 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.481 | 0.505 | 0.500 | 51 | 50 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.967 | 0.980 | 0.978 | 99 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.246 | 0.270 | 0.265 | 28 | 74 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.127 | 0.115 | 0.117 | 12 | 89 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.958 | 0.970 | 0.968 | 98 | 4 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.543 | 0.565 | 0.561 | 57 | 44 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.094 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.150 | 0.146 | 16 | 86 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI6 | team_total | 0.042 | 0.030 | 0.032 | 4 | 98 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.277 | 0.300 | 0.295 | 31 | 71 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-7 | game_total | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.221 | 0.235 | 0.232 | 24 | 77 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-6 | game_total | 0.653 | 0.635 | 0.639 | 64 | 37 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.125 | 0.135 | 0.133 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY5 | team_total | 0.176 | 0.165 | 0.167 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.835 | 0.850 | 0.847 | 86 | 16 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.661 | 0.558 | 0.167 | 0.216 | 5.99 | 5.99 | 0.961/0.991 | KXNHLGAME-26OCT28PHIWSH-WSH -0.102 |
| CGY @ EDM | 0.576 | 0.660 | 0.175 | 0.195 | 6.33 | 6.74 | 1.023/0.978 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.110 |
| NJD @ COL | 0.578 | 0.625 | 0.173 | 0.215 | 6.13 | 6.34 | 0.979/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.061 |
| TOR @ SEA | 0.572 | 0.560 | 0.165 | 0.210 | 6.84 | 6.67 | 1.019/0.988 | KXNHLTOTAL-26OCT28TORSEA-8 -0.035 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2351 (adj 0.2201) · $7.59 · thesis WSH:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2101 (adj 0.1963) · $6.72 · thesis PHI:OFFENSE_4PLUS
- Dylan Strome: 1+ goals NO @ 72c · p 0.7704 (adj 0.7553) · $17.82 · thesis WSH:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 27c · p 0.342 (adj 0.3035) · $5.98 · thesis WSH:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 14c · p 0.2067 (adj 0.1863) · $8.85 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ goals YES @ 11c · p 0.1652 (adj 0.1502) · $7.96 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 7c · p 0.1086 (adj 0.0952) · $4.16 · thesis CGY:OFFENSE_4PLUS
- Ryan Nugent-Hopkins: 1+ assists NO @ 60c · p 0.6892 (adj 0.6421) · $17.82 · thesis EDM:SUPPRESSED
- Nicolas Roy: 1+ assists NO @ 79c · p 0.8998 (adj 0.8252) · $17.82 · thesis COL:SUPPRESSED
- Jake Allen: 27+ saves NO @ 52c · p 0.6034 (adj 0.5592) · $10.38 · thesis NJD:NET_LOW_VOLUME
- Jack Hughes: 1+ goals NO @ 68c · p 0.723 (adj 0.711) · $11.19 · thesis NJD:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 28c · p 0.3185 (adj 0.3076) · $4.02 · thesis COL:OFFENSE_4PLUS
- Freddy Gaudreau: 1+ goals YES @ 10c · p 0.1634 (adj 0.1438) · $8.04 · thesis SEA:WINS_BY_2PLUS
- Teddy Blueger: 1+ goals YES @ 10c · p 0.1554 (adj 0.1403) · $7.44 · thesis TOR:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 16c · p 0.219 (adj 0.203) · $8.03 · thesis SEA:OFFENSE_4PLUS
- Ben Meyers: 1+ goals YES @ 11c · p 0.1598 (adj 0.1449) · $6.19 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 195/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.23 (sd 6.13), pull risk 0.046
- PHI net: Joseph Woll (CONFIRMED) exp shots 27.44, exp saves 23.53 (sd 6.61), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joseph Woll: 28+ saves | 0.262 | 0.440 | 45/57 | +0.151 |  |
| Martin Fehervary: 1+ assists | 0.291 | 0.195 | 21/82 | +0.069 | STANDARD |
| Noah Cates: 1+ points | 0.365 | 0.270 | 28/74 | +0.071 | STANDARD |
| Cam York: 1+ assists | 0.160 | 0.255 | 26/75 | +0.077 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.264 | 0.355 | 36/65 | +0.070 | STANDARD |
| Jordan Kyrou: 1+ points | 0.450 | 0.540 | 56/48 | +0.053 | STANDARD |

**CGY @ EDM** · priced 195/202 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.03, exp saves 23.73 (sd 6.47), pull risk 0.051
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.57, exp saves 25.62 (sd 7.41), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kevin Bahl: 1+ assists | 0.258 | 0.115 | 21/98 | +0.036 | STANDARD |
| Zach Whitecloud: 1+ points | 0.236 | 0.105 | 16/95 | +0.066 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.482 | 0.370 | 38/64 | +0.086 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.672 | 0.565 | 57/44 | +0.085 | STANDARD |
| Adam Klapka: 1+ assists | 0.217 | 0.110 | 20/98 | +0.006 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.316 | 0.220 | 23/79 | +0.074 | STANDARD |

**NJD @ COL** · priced 179/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 28.33, exp saves 24.84 (sd 6.56), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.75 (sd 6.93), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.223 | 0.350 | 36/66 | +0.101 | STANDARD |
| Nicolas Roy: 1+ assists | 0.100 | 0.215 | 22/79 | +0.098 | STANDARD |
| Jack Hughes: 1+ assists | 0.354 | 0.460 | 47/55 | +0.078 | STANDARD |
| Jack Hughes: 1+ points | 0.529 | 0.630 | 64/38 | +0.074 | STANDARD |
| Luke Evangelista: 1+ points | 0.379 | 0.470 | 48/54 | +0.064 | STANDARD |
| Jake Allen: 27+ saves | 0.397 | 0.485 | 49/52 | +0.066 |  |

**TOR @ SEA** · priced 172/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROBABLE) exp shots 28.75, exp saves 24.87 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 30.18, exp saves 25.64 (sd 7.12), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.374 | 0.500 | 51/51 | +0.098 | STANDARD |
| Auston Matthews: 2+ points | 0.261 | 0.360 | 37/65 | +0.073 | STANDARD |
| Gavin McKenna: 1+ points | 0.437 | 0.535 | 54/47 | +0.075 | STANDARD |
| William Nylander: 1+ assists | 0.394 | 0.490 | 50/52 | +0.069 | STANDARD |
| William Nylander: 2+ points | 0.231 | 0.320 | 33/69 | +0.064 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.389 | 0.300 | 31/71 | +0.064 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
