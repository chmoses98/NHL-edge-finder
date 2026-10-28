# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T20:15:10Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3226 · contracts joined: 970 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 870, 'OK': 71, 'NO_EDGE': 29}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 158, 'game_early_goal': 4, 'first_goal': 142, 'game_winner': 8, 'player_goals': 247, 'game_overtime': 4, 'player_points': 212, 'goalie_saves': 7, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 2026-10-28T23:30:00Z | T-3h | 0.655 | 0.345 | 0.167 | 5.96 | 3.48 | 2.49 | 257 (25/232) | PROJECTED/PROJECTED |
| CGY @ EDM | 2026-10-29T00:30:00Z | T-3h | 0.576 | 0.424 | 0.177 | 6.33 | 3.41 | 2.92 | 253 (25/228) | CONFIRMED/CONFIRMED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-3h | 0.580 | 0.420 | 0.177 | 6.12 | 3.31 | 2.81 | 231 (25/206) | CONFIRMED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-3h | 0.569 | 0.431 | 0.166 | 6.78 | 3.62 | 3.16 | 229 (25/204) | PROBABLE/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.569 | 0.435 | 0.462 | 44 | 57 | yes | +0.112 | OK |
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.431 | 0.555 | 0.530 | 56 | 45 | no | +0.102 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.356 | 0.255 | 0.274 | 26 | 75 | yes | +0.083 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.241 | 0.335 | 0.315 | 34 | 67 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.497 | 0.405 | 0.423 | 41 | 60 | yes | +0.070 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.143 | 0.225 | 0.206 | 23 | 78 | no | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.303 | 0.220 | 0.235 | 23 | 79 | yes | +0.060 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.703 | 0.620 | 0.637 | 63 | 39 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.608 | 0.690 | 0.674 | 70 | 32 | no | +0.057 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.221 | 0.295 | 0.279 | 30 | 71 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.399 | 0.475 | 0.460 | 48 | 53 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.232 | 0.165 | 0.177 | 17 | 84 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.813 | 0.875 | 0.864 | 88 | 13 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.456 | 0.530 | 0.515 | 54 | 48 | no | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.258 | 0.330 | 0.315 | 34 | 68 | no | +0.047 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.349 | 0.415 | 0.401 | 42 | 59 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.157 | 0.100 | 0.110 | 11 | 91 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.672 | 0.730 | 0.719 | 74 | 28 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.222 | 0.280 | 0.268 | 29 | 73 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.549 | 0.605 | 0.594 | 61 | 40 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.789 | 0.835 | 0.827 | 84 | 17 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.853 | 0.900 | 0.892 | 91 | 11 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.740 | 0.785 | 0.777 | 79 | 22 | no | +0.028 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.424 | 0.375 | 0.385 | 38 | 63 | yes | +0.028 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.576 | 0.625 | 0.615 | 63 | 38 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.764 | 0.805 | 0.797 | 81 | 20 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.850 | 0.885 | 0.879 | 89 | 12 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.471 | 0.515 | 0.506 | 52 | 49 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.582 | 0.625 | 0.617 | 63 | 38 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.284 | 0.330 | 0.320 | 34 | 68 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.870 | 0.830 | 0.839 | 84 | 18 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.123 | 0.160 | 0.152 | 17 | 85 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.526 | 0.565 | 0.557 | 57 | 44 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.867 | 0.895 | 0.890 | 90 | 11 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.764 | 0.795 | 0.789 | 80 | 21 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.428 | 0.465 | 0.458 | 47 | 54 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.838 | 0.865 | 0.860 | 87 | 14 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.860 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.196 | 0.225 | 0.219 | 23 | 78 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.275 | 0.305 | 0.299 | 31 | 70 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.472 | 0.505 | 0.498 | 51 | 50 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.324 | 0.360 | 0.353 | 37 | 65 | no | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.345 | 0.315 | 0.321 | 32 | 69 | yes | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.655 | 0.685 | 0.679 | 69 | 32 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.126 | 0.105 | 0.109 | 11 | 90 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.103 | 0.130 | 0.124 | 14 | 88 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.220 | 0.190 | 0.196 | 20 | 82 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.136 | 0.110 | 0.115 | 12 | 90 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.960 | 0.980 | 0.977 | 99 | 3 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.435 | 0.465 | 0.459 | 47 | 54 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.343 | 0.310 | 0.316 | 32 | 70 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.897 | 0.915 | 0.912 | 92 | 9 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT28NJCOL-10 | game_total | 0.077 | 0.095 | 0.091 | 10 | 91 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-9 | game_total | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.222 | 0.245 | 0.240 | 25 | 76 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.836 | 0.860 | 0.855 | 87 | 15 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY3 | team_total | 0.563 | 0.535 | 0.541 | 54 | 47 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.174 | 0.195 | 0.191 | 20 | 81 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.691 | 0.715 | 0.710 | 72 | 29 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.252 | 0.280 | 0.274 | 29 | 73 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.650 | 0.680 | 0.674 | 69 | 33 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.539 | 0.565 | 0.560 | 57 | 44 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.273 | 0.300 | 0.294 | 31 | 71 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.158 | 0.185 | 0.179 | 20 | 83 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY6 | team_total | 0.076 | 0.065 | 0.067 | 7 | 94 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT28TORSEA-5 | game_total | 0.830 | 0.850 | 0.846 | 86 | 16 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-8 | game_total | 0.226 | 0.245 | 0.241 | 25 | 76 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.967 | 0.975 | 0.974 | 98 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.246 | 0.270 | 0.265 | 28 | 74 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.957 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.122 | 0.135 | 0.132 | 14 | 87 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.150 | 0.146 | 16 | 86 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.252 | 0.235 | 0.238 | 24 | 77 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.095 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI6 | team_total | 0.041 | 0.035 | 0.036 | 4 | 97 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ2 | game_spread | 0.221 | 0.235 | 0.232 | 24 | 77 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.004 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.655 | 0.557 | 0.167 | 0.224 | 5.96 | 6.00 | 0.961/0.992 | KXNHLSPREAD-26OCT28PHIWSH-WSH2 -0.102 |
| CGY @ EDM | 0.576 | 0.660 | 0.177 | 0.195 | 6.33 | 6.74 | 1.023/0.978 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.110 |
| NJD @ COL | 0.580 | 0.625 | 0.177 | 0.215 | 6.12 | 6.34 | 0.979/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.061 |
| TOR @ SEA | 0.569 | 0.555 | 0.166 | 0.216 | 6.78 | 6.65 | 1.019/0.979 | KXNHLTOTAL-26OCT28TORSEA-8 -0.022 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Sean Couturier: 1+ goals YES @ 10c · p 0.145 (adj 0.1325) · $6.55 · thesis PHI:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2393 (adj 0.2182) · $7.99 · thesis WSH:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2091 (adj 0.1956) · $7.16 · thesis PHI:OFFENSE_4PLUS
- Cole Knuble: 1+ goals YES @ 12c · p 0.1654 (adj 0.1503) · $5.95 · thesis PHI:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 14c · p 0.2067 (adj 0.185) · $9.59 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 7c · p 0.1086 (adj 0.094) · $4.47 · thesis CGY:OFFENSE_4PLUS
- Jonathan Castagna: 1+ goals YES @ 10c · p 0.1291 (adj 0.1206) · $3.8 · thesis CGY:OFFENSE_4PLUS
- Connor McDavid: 1+ goals YES @ 46c · p 0.5124 (adj 0.498) · $9.75 · thesis EDM:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1233 (adj 0.1137) · $4.61 · thesis NJD:OFFENSE_4PLUS
- Nicolas Roy: 1+ assists NO @ 82c · p 0.8998 (adj 0.8499) · $20.0 · thesis COL:SUPPRESSED
- Jack Hughes: 1+ goals NO @ 68c · p 0.723 (adj 0.711) · $12.59 · thesis NJD:SUPPRESSED
- Jake Allen: 27+ saves NO @ 50c · p 0.6034 (adj 0.5329) · $8.5 · thesis NJD:NET_LOW_VOLUME
- Berkly Catton: 1+ goals YES @ 15c · p 0.2191 (adj 0.1968) · $10.16 · thesis SEA:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 74c · p 0.8081 (adj 0.7898) · $20.0 · thesis TOR:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1564 (adj 0.1411) · $6.21 · thesis TOR:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1689 (adj 0.1579) · $5.32 · thesis SEA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 195/206 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.27 (sd 6.06), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 27.44, exp saves 23.58 (sd 6.57), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joseph Woll: 28+ saves | 0.263 | 0.465 | 48/55 | +0.170 |  |
| Martin Fehervary: 1+ points | 0.326 | 0.220 | 25/81 | +0.063 | STANDARD |
| Martin Fehervary: 1+ assists | 0.290 | 0.185 | 21/84 | +0.069 | STANDARD |
| Noah Cates: 1+ points | 0.362 | 0.265 | 28/75 | +0.068 | STANDARD |
| Jordan Kyrou: 1+ points | 0.447 | 0.540 | 55/47 | +0.066 | STANDARD |
| Timothy Liljegren: 1+ assists | 0.172 | 0.080 | 14/98 | +0.024 | STANDARD |

**CGY @ EDM** · priced 195/202 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.03, exp saves 23.73 (sd 6.47), pull risk 0.051
- CGY net: Devin Cooley (CONFIRMED) exp shots 30.57, exp saves 25.62 (sd 7.41), pull risk 0.101

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonathan Castagna: 1+ points | 0.253 | 0.105 | 19/98 | +0.052 | PRIOR_HEAVY |
| Kevin Bahl: 1+ assists | 0.258 | 0.115 | 21/98 | +0.036 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.482 | 0.355 | 36/65 | +0.106 | STANDARD |
| Vasily Podkolzin: 2+ points | 0.316 | 0.190 | 20/82 | +0.105 | STANDARD |
| Owen Michaels: 1+ points | 0.301 | 0.185 | 23/86 | +0.058 | STANDARD |
| Evan Bouchard: 2+ assists | 0.284 | 0.170 | 26/92 | +0.011 | STANDARD |

**NJD @ COL** · priced 179/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 28.33, exp saves 24.84 (sd 6.56), pull risk 0.045
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.75 (sd 6.93), pull risk 0.082

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.223 | 0.345 | 36/67 | +0.092 | STANDARD |
| Jack Hughes: 1+ assists | 0.354 | 0.465 | 48/55 | +0.078 | STANDARD |
| Jake Allen: 27+ saves | 0.397 | 0.505 | 51/50 | +0.086 |  |
| Jack Hughes: 1+ points | 0.529 | 0.630 | 64/38 | +0.074 | STANDARD |
| Nicolas Roy: 1+ assists | 0.100 | 0.200 | 22/82 | +0.069 | STANDARD |
| Mackenzie Blackwood: 27+ saves | 0.385 | 0.480 | 51/55 | +0.048 |  |

**TOR @ SEA** · priced 172/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROBABLE) exp shots 28.75, exp saves 24.92 (sd 6.78), pull risk 0.063
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.18, exp saves 25.68 (sd 7.08), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.376 | 0.500 | 51/51 | +0.097 | STANDARD |
| Gavin McKenna: 1+ points | 0.431 | 0.535 | 54/47 | +0.081 | STANDARD |
| Auston Matthews: 2+ points | 0.258 | 0.360 | 37/65 | +0.076 | STANDARD |
| Berkly Catton: 1+ goals | 0.219 | 0.130 | 15/89 | +0.060 | STANDARD |
| William Nylander: 2+ points | 0.233 | 0.320 | 33/69 | +0.062 | STANDARD |
| Kaapo Kakko: 1+ points | 0.512 | 0.430 | 44/58 | +0.055 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
