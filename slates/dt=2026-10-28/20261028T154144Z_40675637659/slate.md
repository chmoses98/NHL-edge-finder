# NHL slate 2026-10-28 — RESEARCH_ONLY

generated 2026-10-28T15:41:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

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
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA6 | team_total | 0.157 | 0.095 | 0.105 | 10 | 91 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT28TORSEA-SEA3 | game_spread | 0.230 | 0.165 | 0.177 | 17 | 84 | yes | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR4 | team_total | 0.403 | 0.480 | 0.464 | 49 | 53 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR3 | team_total | 0.616 | 0.690 | 0.676 | 70 | 32 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-5 | game_total | 0.740 | 0.795 | 0.785 | 80 | 21 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR2 | team_total | 0.814 | 0.870 | 0.860 | 88 | 14 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR5 | team_total | 0.223 | 0.280 | 0.268 | 29 | 73 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT28NJCOL-6 | game_total | 0.550 | 0.605 | 0.594 | 61 | 40 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT28NJCOL-7 | game_total | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM3 | game_spread | 0.244 | 0.295 | 0.284 | 30 | 71 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-6 | game_total | 0.526 | 0.575 | 0.565 | 58 | 43 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-7 | game_total | 0.477 | 0.525 | 0.515 | 53 | 48 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM5 | team_total | 0.281 | 0.330 | 0.320 | 34 | 68 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT28NJCOL-5 | game_total | 0.765 | 0.805 | 0.797 | 81 | 20 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 | team_total | 0.480 | 0.530 | 0.520 | 54 | 48 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH5 | team_total | 0.273 | 0.315 | 0.306 | 32 | 69 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH3 | game_spread | 0.284 | 0.330 | 0.320 | 34 | 68 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-7 | game_total | 0.412 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-SEA2 | team_total | 0.870 | 0.830 | 0.839 | 84 | 18 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4 | team_total | 0.472 | 0.515 | 0.506 | 52 | 49 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM2 | team_total | 0.864 | 0.900 | 0.893 | 91 | 11 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-5 | game_total | 0.791 | 0.825 | 0.819 | 83 | 18 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM3 | team_total | 0.689 | 0.735 | 0.726 | 75 | 28 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT28CGYEDM-EDM2 | game_spread | 0.377 | 0.415 | 0.407 | 42 | 59 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-4 | game_total | 0.836 | 0.870 | 0.864 | 88 | 14 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3 | team_total | 0.691 | 0.725 | 0.718 | 73 | 28 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL2 | team_total | 0.838 | 0.865 | 0.860 | 87 | 14 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT28NJCOL-4 | game_total | 0.849 | 0.875 | 0.870 | 88 | 13 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM6 | team_total | 0.137 | 0.165 | 0.159 | 17 | 84 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH2 | team_total | 0.860 | 0.890 | 0.884 | 90 | 12 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT28TORSEA-8 | game_total | 0.347 | 0.315 | 0.321 | 32 | 69 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-8 | game_total | 0.226 | 0.260 | 0.253 | 27 | 75 | no | +0.011 | OK |
| KXNHLGAME-26OCT28PHIWSH-PHI | game_winner | 0.345 | 0.315 | 0.321 | 32 | 69 | yes | +0.010 | OK |
| KXNHLGAME-26OCT28PHIWSH-WSH | game_winner | 0.655 | 0.685 | 0.679 | 69 | 32 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT28TORSEA-4 | game_total | 0.895 | 0.915 | 0.911 | 92 | 9 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT28NJCOL-COL3 | game_spread | 0.218 | 0.250 | 0.243 | 26 | 76 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 | team_total | 0.434 | 0.465 | 0.459 | 47 | 54 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT28TORSEA-10 | game_total | 0.136 | 0.110 | 0.115 | 12 | 90 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT28NJCOL-NJ3 | game_spread | 0.124 | 0.145 | 0.141 | 15 | 86 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-9 | game_total | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ4 | team_total | 0.328 | 0.355 | 0.350 | 36 | 65 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28TORSEA-TOR6 | team_total | 0.106 | 0.130 | 0.125 | 14 | 88 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL3 | team_total | 0.649 | 0.680 | 0.674 | 69 | 33 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28NJCOL-3 | game_total | 0.962 | 0.975 | 0.973 | 98 | 3 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-6 | game_total | 0.589 | 0.620 | 0.614 | 63 | 39 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT28PHIWSH-WSH2 | game_spread | 0.428 | 0.455 | 0.450 | 46 | 55 | no | +0.004 | OK |
| KXNHLGAME-26OCT28CGYEDM-CGY | game_winner | 0.401 | 0.375 | 0.380 | 38 | 63 | yes | +0.004 | OK |
| KXNHLGAME-26OCT28CGYEDM-EDM | game_winner | 0.599 | 0.625 | 0.620 | 63 | 38 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT28NJCOL-8 | game_total | 0.253 | 0.275 | 0.270 | 28 | 73 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT28TORSEA-9 | game_total | 0.256 | 0.230 | 0.235 | 24 | 78 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-COL5 | team_total | 0.245 | 0.270 | 0.265 | 28 | 74 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-4 | game_total | 0.871 | 0.890 | 0.886 | 90 | 12 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28PHIWSH-3 | game_total | 0.957 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT28CGYEDM-8 | game_total | 0.285 | 0.305 | 0.301 | 31 | 70 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT28TORSEA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ2 | team_total | 0.768 | 0.790 | 0.786 | 80 | 22 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT28PHIWSH-PHI3 | game_spread | 0.085 | 0.095 | 0.093 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH6 | team_total | 0.132 | 0.150 | 0.146 | 16 | 86 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ5 | team_total | 0.161 | 0.180 | 0.176 | 19 | 83 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-10 | game_total | 0.067 | 0.075 | 0.073 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-9 | game_total | 0.201 | 0.220 | 0.216 | 23 | 79 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT28CGYEDM-CGY3 | game_spread | 0.114 | 0.105 | 0.107 | 11 | 90 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-10 | game_total | 0.097 | 0.110 | 0.107 | 12 | 90 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT28CGYEDM-CGY2 | game_spread | 0.208 | 0.190 | 0.194 | 20 | 82 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28CGYEDM-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT28PHIWSH-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI3 | team_total | 0.456 | 0.480 | 0.475 | 49 | 53 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28CGYEDM-CGY6 | team_total | 0.071 | 0.065 | 0.066 | 7 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT28NJCOL-NJ3 | team_total | 0.546 | 0.565 | 0.561 | 57 | 44 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT28TORSEA-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT28NJCOL-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ WSH | 0.655 | 0.557 | 0.167 | 0.224 | 5.96 | 6.00 | 0.961/0.992 | KXNHLSPREAD-26OCT28PHIWSH-WSH2 -0.102 |
| CGY @ EDM | 0.599 | 0.667 | 0.168 | 0.200 | 6.37 | 6.73 | 1.009/0.986 | KXNHLTEAMTOTAL-26OCT28CGYEDM-EDM4 +0.092 |
| NJD @ COL | 0.576 | 0.622 | 0.174 | 0.212 | 6.15 | 6.33 | 0.977/0.983 | KXNHLTEAMTOTAL-26OCT28NJCOL-COL4 +0.057 |
| TOR @ SEA | 0.564 | 0.551 | 0.165 | 0.214 | 6.79 | 6.60 | 1.016/0.965 | KXNHLTOTAL-26OCT28TORSEA-8 -0.032 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Christian Dvorak: 1+ goals YES @ 15c · p 0.2091 (adj 0.1931) · $9.1 · thesis PHI:OFFENSE_4PLUS
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2393 (adj 0.222) · $10.82 · thesis WSH:OFFENSE_4PLUS
- Washington over 2.5 goals scored NO @ 28c · p 0.3714 (adj 0.3232) · $11.24 · thesis WSH:SUPPRESSED
- Jordan Kyrou: 1+ goals NO @ 74c · p 0.7843 (adj 0.772) · $12.84 · thesis WSH:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 15c · p 0.2118 (adj 0.1901) · $8.35 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ goals YES @ 12c · p 0.1653 (adj 0.149) · $4.09 · thesis EDM:OFFENSE_4PLUS
- Brennan Othmann: 1+ goals YES @ 8c · p 0.1125 (adj 0.1019) · $4.14 · thesis CGY:OFFENSE_4PLUS
- Connor McDavid: 1+ goals YES @ 46c · p 0.5217 (adj 0.505) · $8.91 · thesis EDM:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1144 (adj 0.1071) · $2.96 · thesis NJD:OFFENSE_4PLUS
- Connor Brown: 1+ goals YES @ 13c · p 0.1604 (adj 0.149) · $3.17 · thesis NJD:OFFENSE_4PLUS
- Timo Meier: 1+ goals NO @ 76c · p 0.7965 (adj 0.7861) · $12.2 · thesis NJD:SUPPRESSED
- Nico Hischier: 1+ assists NO @ 64c · p 0.7102 (adj 0.6701) · $9.43 · thesis NJD:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1662 (adj 0.1484) · $7.94 · thesis TOR:OFFENSE_4PLUS
- Gavin McKenna: 1+ goals NO @ 75c · p 0.8116 (adj 0.795) · $18.99 · thesis TOR:SUPPRESSED
- Ryan Winterton: 1+ goals YES @ 13c · p 0.1668 (adj 0.1563) · $4.08 · thesis SEA:OFFENSE_4PLUS
- Toronto wins by over 1.5 goals NO @ 67c · p 0.7533 (adj 0.7091) · $18.99 · thesis SEA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ WSH** · priced 159/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 25.45, exp saves 22.27 (sd 6.06), pull risk 0.045
- PHI net: Joseph Woll (PROJECTED) exp shots 27.44, exp saves 23.58 (sd 6.57), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jordan Kyrou: 1+ points | 0.447 | 0.535 | 55/48 | +0.056 | STANDARD |
| Pierre-Luc Dubois: 1+ assists | 0.274 | 0.360 | 37/65 | +0.060 | STANDARD |
| Christian Dvorak: 1+ points | 0.434 | 0.350 | 36/66 | +0.058 | STANDARD |
| Cole Hutson: 1+ points | 0.373 | 0.455 | 47/56 | +0.050 | STANDARD |
| Jordan Kyrou: 1+ assists | 0.299 | 0.370 | 38/64 | +0.045 | STANDARD |
| Ryan Leonard: 1+ assists | 0.341 | 0.270 | 28/74 | +0.047 | STANDARD |

**CGY @ EDM** · priced 160/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.03, exp saves 23.8 (sd 6.4), pull risk 0.048
- CGY net: Devin Cooley (PROJECTED) exp shots 30.57, exp saves 25.51 (sd 7.45), pull risk 0.105

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vasily Podkolzin: 2+ points | 0.314 | 0.135 | 21/94 | +0.092 | STANDARD |
| Evan Bouchard: 1+ points | 0.748 | 0.610 | 69/47 | +0.043 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.480 | 0.350 | 36/66 | +0.104 | STANDARD |
| Kasperi Kapanen: 1+ assists | 0.320 | 0.200 | 24/84 | +0.068 | STANDARD |
| Vasily Podkolzin: 1+ points | 0.674 | 0.555 | 56/45 | +0.097 | STANDARD |
| Kasperi Kapanen: 1+ points | 0.449 | 0.345 | 37/68 | +0.063 | STANDARD |

**NJD @ COL** · priced 174/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 28.33, exp saves 24.83 (sd 6.58), pull risk 0.048
- NJD net: Jake Allen (CONFIRMED) exp shots 29.11, exp saves 24.79 (sd 6.94), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 1+ points | 0.714 | 0.395 | 73/94 | -0.029 | STANDARD |
| Luke Evangelista: 1+ assists | 0.213 | 0.340 | 35/67 | +0.101 | STANDARD |
| Jack Hughes: 1+ assists | 0.357 | 0.460 | 47/55 | +0.075 | STANDARD |
| Luke Evangelista: 1+ points | 0.372 | 0.465 | 48/55 | +0.060 | STANDARD |
| Nico Hischier: 1+ assists | 0.290 | 0.370 | 38/64 | +0.054 | STANDARD |
| Cale Makar: 1+ assists | 0.438 | 0.515 | 53/50 | +0.045 | STANDARD |

**TOR @ SEA** · priced 170/176 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.75, exp saves 24.83 (sd 6.78), pull risk 0.065
- TOR net: Anthony Stolarz (PROJECTED) exp shots 30.18, exp saves 25.72 (sd 7.05), pull risk 0.076

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Berkly Catton: 1+ goals | 0.224 | 0.100 | 16/96 | +0.054 | STANDARD |
| Auston Matthews: 1+ assists | 0.393 | 0.500 | 51/51 | +0.079 | STANDARD |
| Auston Matthews: 2+ points | 0.283 | 0.370 | 38/64 | +0.061 | STANDARD |
| Kaapo Kakko: 1+ assists | 0.385 | 0.300 | 31/71 | +0.060 | STANDARD |
| Gavin McKenna: 1+ points | 0.416 | 0.495 | 51/52 | +0.046 | STANDARD |
| William Nylander: 1+ assists | 0.396 | 0.470 | 48/54 | +0.046 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
