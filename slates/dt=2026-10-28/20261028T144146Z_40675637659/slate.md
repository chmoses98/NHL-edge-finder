# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T14:41:46Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3097 · contracts joined: 893 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 793, 'OK': 63, 'NO_EDGE': 37}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 127, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 252, 'game_overtime': 4, 'player_points': 165, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 2026-10-28T23:30:00Z | T-6h | 0.655 | 0.345 | 0.167 | 5.96 | 3.48 | 2.49 | 216 (25/191) | PROJECTED/PROJECTED |
| CGY @ EDM | 2026-10-29T00:30:00Z | T-6h | 0.599 | 0.401 | 0.168 | 6.37 | 3.51 | 2.86 | 221 (25/196) | PROJECTED/PROJECTED |
| NJD @ COL | 2026-10-29T01:00:00Z | T-6h | 0.576 | 0.424 | 0.174 | 6.15 | 3.31 | 2.84 | 229 (25/204) | PROJECTED/CONFIRMED |
| TOR @ SEA | 2026-10-29T02:00:00Z | T-6h | 0.564 | 0.436 | 0.165 | 6.79 | 3.60 | 3.18 | 227 (25/202) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT28TORSEA-SEA | game_winner | 0.564 | 0.435 | 0.461 | 44 | 57 | yes | +0.106 | OK |
| KXNHLGAME-26OCT28TORSEA-TOR | game_winner | 0.436 | 0.555 | 0.531 | 56 | 45 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA2 | game_spread | 0.351 | 0.255 | 0.273 | 26 | 75 | yes | +0.078 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR2 | game_spread | 0.243 | 0.335 | 0.315 | 34 | 67 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT28TORSEA-TOR3 | game_spread | 0.144 | 0.225 | 0.206 | 23 | 78 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA5 | team_total | 0.300 | 0.220 | 0.235 | 23 | 79 | yes | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4 | team_total | 0.493 | 0.410 | 0.426 | 42 | 60 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA3 | team_total | 0.698 | 0.620 | 0.636 | 63 | 39 | yes | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.403 | 0.480 | 0.464 | 49 | 53 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.616 | 0.690 | 0.676 | 70 | 32 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.157 | 0.100 | 0.110 | 11 | 91 | yes | +0.040 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.230 | 0.175 | 0.185 | 18 | 83 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.740 | 0.795 | 0.785 | 80 | 21 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.814 | 0.870 | 0.860 | 88 | 14 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.223 | 0.280 | 0.268 | 29 | 73 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.244 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.472 | 0.525 | 0.514 | 53 | 48 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.864 | 0.905 | 0.898 | 91 | 10 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.526 | 0.575 | 0.565 | 58 | 43 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.836 | 0.875 | 0.868 | 88 | 13 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.281 | 0.330 | 0.320 | 34 | 68 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.765 | 0.805 | 0.797 | 81 | 20 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.550 | 0.595 | 0.586 | 60 | 41 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.480 | 0.530 | 0.520 | 54 | 48 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.440 | 0.485 | 0.476 | 49 | 52 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.273 | 0.320 | 0.310 | 33 | 69 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.284 | 0.325 | 0.316 | 33 | 68 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-7 | game_total | 0.412 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.870 | 0.825 | 0.835 | 84 | 19 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-8 | game_total | 0.226 | 0.270 | 0.261 | 28 | 74 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.218 | 0.255 | 0.247 | 26 | 75 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.791 | 0.825 | 0.819 | 83 | 18 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.689 | 0.735 | 0.726 | 75 | 28 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.377 | 0.415 | 0.407 | 42 | 59 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.649 | 0.690 | 0.682 | 70 | 32 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.477 | 0.515 | 0.507 | 52 | 49 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.691 | 0.730 | 0.722 | 74 | 28 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.838 | 0.865 | 0.860 | 87 | 14 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.849 | 0.875 | 0.870 | 88 | 13 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.137 | 0.165 | 0.159 | 17 | 84 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.860 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.957 | 0.980 | 0.977 | 99 | 3 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.245 | 0.280 | 0.273 | 29 | 73 | no | +0.011 | OK |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.345 | 0.315 | 0.321 | 32 | 69 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.155 | 0.150 | 16 | 85 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.434 | 0.465 | 0.459 | 47 | 54 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.136 | 0.110 | 0.115 | 12 | 90 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.208 | 0.185 | 0.189 | 19 | 82 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-9 | game_total | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.106 | 0.130 | 0.125 | 14 | 88 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.962 | 0.975 | 0.973 | 98 | 3 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.589 | 0.620 | 0.614 | 63 | 39 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.428 | 0.455 | 0.450 | 46 | 55 | no | +0.004 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.401 | 0.375 | 0.380 | 38 | 63 | yes | +0.004 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.599 | 0.625 | 0.620 | 63 | 38 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.253 | 0.275 | 0.270 | 28 | 73 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.256 | 0.235 | 0.239 | 24 | 77 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI2 | team_total | 0.703 | 0.730 | 0.725 | 74 | 28 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.347 | 0.320 | 0.325 | 33 | 69 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT28NJCOL-9 | game_total | 0.178 | 0.195 | 0.192 | 20 | 81 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.871 | 0.890 | 0.886 | 90 | 12 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.285 | 0.305 | 0.301 | 31 | 70 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-PHI3 | game_spread | 0.085 | 0.095 | 0.093 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.655 | 0.680 | 0.675 | 69 | 33 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.969 | 0.980 | 0.978 | 99 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.895 | 0.910 | 0.907 | 92 | 10 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.124 | 0.135 | 0.133 | 14 | 87 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-10 | game_total | 0.067 | 0.085 | 0.081 | 10 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI4 | team_total | 0.249 | 0.270 | 0.266 | 28 | 74 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.201 | 0.225 | 0.220 | 24 | 79 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.114 | 0.105 | 0.107 | 11 | 90 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.097 | 0.110 | 0.107 | 12 | 90 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI3 | team_total | 0.456 | 0.480 | 0.475 | 49 | 53 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY6 | team_total | 0.071 | 0.065 | 0.066 | 7 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.328 | 0.350 | 0.346 | 36 | 66 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL6 | team_total | 0.118 | 0.125 | 0.124 | 13 | 88 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.655 | 0.557 | 0.167 | 0.224 | 5.96 | 6.00 | 0.961/0.992 | KXNHLSPREAD-26OCT28PHIWSH-WSH2 -0.102 |
| CGY @ EDM | 0.599 | 0.667 | 0.168 | 0.200 | 6.37 | 6.73 | 1.009/0.986 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.092 |
| NJD @ COL | 0.576 | 0.622 | 0.174 | 0.212 | 6.15 | 6.33 | 0.977/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.057 |
| TOR @ SEA | 0.564 | 0.551 | 0.165 | 0.214 | 6.79 | 6.60 | 1.016/0.965 | KXNHLTOTAL-26OCT28TORSEA-8 -0.032 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2393 (adj 0.222) · $8.97 · thesis WSH:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2091 (adj 0.1943) · $6.71 · thesis PHI:OFFENSE_4PLUS
- Jordan Kyrou: 1+ goals NO @ 73c · p 0.7843 (adj 0.7695) · $19.67 · thesis WSH:SUPPRESSED
- Sean Couturier: 1+ goals YES @ 11c · p 0.1464 (adj 0.1348) · $4.52 · thesis PHI:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.2118 (adj 0.1913) · $6.02 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ goals YES @ 46c · p 0.5217 (adj 0.505) · $15.02 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 8c · p 0.1125 (adj 0.1006) · $3.82 · thesis CGY:OFFENSE_4PLUS
- Ryan Nugent-Hopkins: 1+ assists NO @ 60c · p 0.6856 (adj 0.6378) · $17.72 · thesis EDM:SUPPRESSED
- Jack Hughes: 1+ assists NO @ 56c · p 0.6427 (adj 0.5964) · $11.48 · thesis NJD:SUPPRESSED
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1144 (adj 0.1071) · $2.96 · thesis NJD:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 76c · p 0.7965 (adj 0.7861) · $13.66 · thesis NJD:SUPPRESSED
- Artturi Lehkonen: 1+ goals YES @ 29c · p 0.3288 (adj 0.3166) · $4.18 · thesis COL:OFFENSE_4PLUS
- Berkly Catton: 1+ goals YES @ 17c · p 0.2235 (adj 0.2039) · $5.98 · thesis SEA:OFFENSE_4PLUS
- Ryan Winterton: 1+ goals YES @ 12c · p 0.1668 (adj 0.1476) · $4.5 · thesis SEA:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1662 (adj 0.1459) · $5.3 · thesis TOR:OFFENSE_4PLUS
- Toronto wins by over 1.5 goals NO @ 67c · p 0.7533 (adj 0.7091) · $19.51 · thesis SEA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.27 (sd 6.06), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 27.44, exp saves 23.58 (sd 6.57), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Christian Dvorak: 1+ points | 0.435 | 0.345 | 35/66 | +0.069 | STANDARD |
| Jordan Kyrou: 1+ points | 0.447 | 0.535 | 55/48 | +0.056 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.274 | 0.360 | 37/65 | +0.060 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.299 | 0.375 | 39/64 | +0.045 | STANDARD |
| Cole Hutson: 1+ points | 0.373 | 0.445 | 47/58 | +0.030 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.239 | 0.170 | 18/84 | +0.049 | STANDARD |

**CGY @ EDM** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.03, exp saves 23.8 (sd 6.4), pull risk 0.048
- CGY net: Devin Cooley (PROJECTED) exp shots 30.57, exp saves 25.51 (sd 7.45), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vasily Podkolzin: 2+ points | 0.314 | 0.160 | 22/90 | +0.082 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.674 | 0.555 | 56/45 | +0.097 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.320 | 0.205 | 22/81 | +0.088 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.480 | 0.365 | 38/65 | +0.084 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.314 | 0.410 | 42/60 | +0.069 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.449 | 0.355 | 38/67 | +0.053 | STANDARD |

**NJD @ COL** · priced 174/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 28.33, exp saves 24.83 (sd 6.58), pull risk 0.048
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.79 (sd 6.94), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Luke Evangelista: 1+ assists | 0.213 | 0.335 | 35/68 | +0.091 | STANDARD |
| Luke Evangelista: 1+ points | 0.372 | 0.470 | 49/55 | +0.060 | STANDARD |
| Jack Hughes: 1+ assists | 0.357 | 0.450 | 46/56 | +0.065 | STANDARD |
| Cale Makar: 1+ assists | 0.438 | 0.520 | 53/49 | +0.055 | STANDARD |
| Nico Hischier: 1+ assists | 0.290 | 0.370 | 38/64 | +0.054 | STANDARD |
| Jack Hughes: 1+ points | 0.544 | 0.620 | 63/39 | +0.049 | STANDARD |

**TOR @ SEA** · priced 170/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.75, exp saves 24.83 (sd 6.78), pull risk 0.065
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.18, exp saves 25.72 (sd 7.05), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Auston Matthews: 1+ assists | 0.393 | 0.500 | 51/51 | +0.079 | STANDARD |
| Auston Matthews: 2+ points | 0.283 | 0.370 | 39/65 | +0.051 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.385 | 0.300 | 32/72 | +0.049 | STANDARD |
| Teddy Blueger: 1+ goals | 0.166 | 0.085 | 12/95 | +0.039 | STANDARD |
| Berkly Catton: 1+ goals | 0.224 | 0.145 | 17/88 | +0.044 | STANDARD |
| Mackie Samoskevich: 1+ goals | 0.248 | 0.170 | 21/87 | +0.026 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
