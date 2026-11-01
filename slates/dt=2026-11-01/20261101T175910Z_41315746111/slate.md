# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T17:59:10Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2802 · contracts joined: 1098 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 973, 'OK': 75, 'NO_EDGE': 50}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 150, 'game_early_goal': 5, 'first_goal': 175, 'game_winner': 10, 'player_goals': 299, 'game_overtime': 5, 'player_points': 210, 'goalie_saves': 9, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CAR | 2026-11-01T18:00:00Z | T-<10m | 0.694 | 0.306 | 0.165 | 5.90 | 3.57 | 2.33 | 231 (25/206) | CONFIRMED/CONFIRMED |
| MIN @ WSH | 2026-11-01T20:30:00Z | T-90m | 0.535 | 0.465 | 0.177 | 6.04 | 3.12 | 2.91 | 219 (25/194) | PROJECTED/CONFIRMED |
| UTA @ PHI | 2026-11-01T21:00:00Z | T-3h | 0.444 | 0.556 | 0.184 | 5.92 | 2.78 | 3.14 | 208 (25/183) | PROJECTED/PROJECTED |
| EDM @ NYR | 2026-11-01T23:00:00Z | T-3h | 0.516 | 0.484 | 0.171 | 6.46 | 3.28 | 3.19 | 222 (25/197) | CONFIRMED/CONFIRMED |
| OTT @ ANA | 2026-11-02T01:00:00Z | T-6h | 0.562 | 0.438 | 0.167 | 6.83 | 3.62 | 3.22 | 218 (25/193) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.562 | 0.465 | 0.484 | 47 | 54 | yes | +0.075 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.438 | 0.535 | 0.516 | 54 | 47 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.500 | 0.425 | 0.440 | 43 | 58 | yes | +0.052 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4 | team_total | 0.392 | 0.475 | 0.458 | 49 | 54 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.704 | 0.635 | 0.649 | 64 | 37 | yes | +0.048 | OK |
| KXNHLGAME-26NOV01UTAPHI-UTA | game_winner | 0.556 | 0.625 | 0.612 | 63 | 38 | no | +0.047 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.347 | 0.285 | 0.297 | 29 | 72 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN4 | team_total | 0.343 | 0.405 | 0.392 | 41 | 60 | no | +0.041 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA3 | game_spread | 0.199 | 0.255 | 0.243 | 26 | 75 | no | +0.038 | OK |
| KXNHLGAME-26NOV01UTAPHI-PHI | game_winner | 0.444 | 0.385 | 0.397 | 39 | 62 | yes | +0.037 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-6 | game_total | 0.516 | 0.575 | 0.563 | 58 | 43 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA3 | team_total | 0.618 | 0.675 | 0.664 | 68 | 33 | no | +0.037 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA2 | game_spread | 0.328 | 0.385 | 0.373 | 39 | 62 | no | +0.035 | OK |
| KXNHLSPREAD-26NOV01WPGCAR-CAR3 | game_spread | 0.312 | 0.365 | 0.354 | 37 | 64 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.411 | 0.470 | 0.458 | 48 | 54 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.305 | 0.245 | 0.256 | 26 | 77 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR4 | team_total | 0.492 | 0.545 | 0.534 | 55 | 46 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.624 | 0.680 | 0.669 | 69 | 33 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.823 | 0.870 | 0.861 | 88 | 14 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR5 | team_total | 0.287 | 0.335 | 0.325 | 34 | 67 | no | +0.028 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-7 | game_total | 0.395 | 0.445 | 0.435 | 45 | 56 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2 | team_total | 0.814 | 0.860 | 0.852 | 87 | 15 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN2 | team_total | 0.783 | 0.830 | 0.821 | 84 | 18 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN3 | game_spread | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-5 | game_total | 0.734 | 0.780 | 0.771 | 79 | 23 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-5 | game_total | 0.734 | 0.780 | 0.771 | 79 | 23 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA5 | team_total | 0.214 | 0.260 | 0.250 | 27 | 75 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-PHI2 | game_spread | 0.233 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-4 | game_total | 0.830 | 0.865 | 0.858 | 87 | 14 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN2 | game_spread | 0.255 | 0.295 | 0.287 | 30 | 71 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN3 | team_total | 0.562 | 0.610 | 0.601 | 62 | 40 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-8 | game_total | 0.217 | 0.260 | 0.251 | 27 | 75 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR2 | team_total | 0.874 | 0.910 | 0.904 | 92 | 10 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-4 | game_total | 0.832 | 0.870 | 0.863 | 88 | 14 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.157 | 0.115 | 0.123 | 13 | 90 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR6 | team_total | 0.141 | 0.175 | 0.168 | 18 | 83 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV01MINWSH-4 | game_total | 0.843 | 0.875 | 0.869 | 88 | 13 | no | +0.019 | OK |
| KXNHLSPREAD-26NOV01WPGCAR-CAR2 | game_spread | 0.464 | 0.505 | 0.497 | 51 | 50 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV01MINWSH-6 | game_total | 0.535 | 0.575 | 0.567 | 58 | 43 | no | +0.018 | OK |
| KXNHLGAME-26NOV01MINWSH-MIN | game_winner | 0.465 | 0.505 | 0.497 | 51 | 50 | no | +0.017 | OK |
| KXNHLGAME-26NOV01MINWSH-WSH | game_winner | 0.535 | 0.495 | 0.503 | 50 | 51 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.230 | 0.270 | 0.262 | 28 | 74 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-9 | game_total | 0.144 | 0.175 | 0.168 | 18 | 83 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR3 | game_spread | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV01MINWSH-5 | game_total | 0.753 | 0.790 | 0.783 | 80 | 22 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN5 | team_total | 0.174 | 0.210 | 0.202 | 22 | 80 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-7 | game_total | 0.399 | 0.435 | 0.428 | 44 | 57 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-6 | game_total | 0.510 | 0.545 | 0.538 | 55 | 46 | no | +0.012 | OK |
| KXNHLGAME-26NOV01WPGCAR-CAR | game_winner | 0.694 | 0.725 | 0.719 | 73 | 28 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR3 | team_total | 0.706 | 0.740 | 0.733 | 75 | 27 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA6 | team_total | 0.094 | 0.115 | 0.110 | 12 | 89 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-4 | game_total | 0.874 | 0.895 | 0.891 | 90 | 11 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR2 | team_total | 0.832 | 0.865 | 0.859 | 88 | 15 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR3 | team_total | 0.635 | 0.670 | 0.663 | 68 | 34 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV01MINWSH-9 | game_total | 0.162 | 0.185 | 0.180 | 19 | 82 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV01MINWSH-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLGAME-26NOV01EDMNYR-EDM | game_winner | 0.484 | 0.455 | 0.461 | 46 | 55 | yes | +0.007 | OK |
| KXNHLGAME-26NOV01EDMNYR-NYR | game_winner | 0.516 | 0.545 | 0.539 | 55 | 46 | no | +0.007 | OK |
| KXNHLSPREAD-26NOV01MINWSH-WSH2 | game_spread | 0.311 | 0.285 | 0.290 | 29 | 72 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV01MINWSH-10 | game_total | 0.070 | 0.085 | 0.082 | 9 | 92 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR2 | game_spread | 0.302 | 0.325 | 0.320 | 33 | 68 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLGAME-26NOV01WPGCAR-WPG | game_winner | 0.306 | 0.285 | 0.289 | 29 | 72 | yes | +0.002 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-3 | game_total | 0.956 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-EDM2 | game_spread | 0.275 | 0.255 | 0.259 | 26 | 75 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.870 | 0.845 | 0.850 | 86 | 17 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-10 | game_total | 0.065 | 0.075 | 0.073 | 8 | 93 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 | team_total | 0.528 | 0.505 | 0.510 | 51 | 50 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV01MINWSH-7 | game_total | 0.422 | 0.445 | 0.440 | 45 | 56 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01MINWSH-8 | game_total | 0.237 | 0.255 | 0.251 | 26 | 75 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.905 | 0.920 | 0.917 | 93 | 9 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.354 | 0.335 | 0.339 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-5 | game_total | 0.802 | 0.820 | 0.816 | 83 | 19 |  | -0.003 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CAR | 0.694 | 0.633 | 0.165 | 0.214 | 5.90 | 6.37 | 1.003/1.004 | KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG3 +0.106 |
| MIN @ WSH | 0.535 | 0.542 | 0.177 | 0.216 | 6.04 | 6.31 | 0.961/0.991 | KXNHLTOTAL-26NOV01MINWSH-7 +0.048 |
| UTA @ PHI | 0.444 | 0.495 | 0.184 | 0.221 | 5.92 | 6.11 | 0.994/0.993 | KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 +0.068 |
| EDM @ NYR | 0.516 | 0.503 | 0.171 | 0.211 | 6.46 | 6.68 | 0.988/1.000 | KXNHLTOTAL-26NOV01EDMNYR-7 +0.039 |
| OTT @ ANA | 0.562 | 0.586 | 0.167 | 0.213 | 6.83 | 6.57 | 0.968/1.034 | KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Gabriel Vilardi: 1+ goals YES @ 20c · p 0.2703 (adj 0.2515) · $9.55 · thesis WPG:OFFENSE_4PLUS
- Alex Iafallo: 1+ goals YES @ 11c · p 0.1558 (adj 0.1431) · $5.36 · thesis WPG:OFFENSE_4PLUS
- Sebastian Aho: 1+ assists NO @ 54c · p 0.6176 (adj 0.5763) · $8.55 · thesis CAR:SUPPRESSED
- Carolina wins by over 2.5 goals NO @ 64c · p 0.7115 (adj 0.6733) · $2.17 · thesis GAME:TIGHT
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.246 (adj 0.2245) · $7.38 · thesis WSH:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 56c · p 0.6385 (adj 0.6176) · $15.96 · thesis MIN:SUPPRESSED
- Pierre-Luc Dubois: 1+ goals YES @ 18c · p 0.2252 (adj 0.2114) · $4.41 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 24c · p 0.3221 (adj 0.2761) · $4.46 · thesis WSH:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 11c · p 0.1896 (adj 0.1684) · $9.74 · thesis PHI:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2529 (adj 0.2284) · $12.27 · thesis PHI:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 66c · p 0.708 (adj 0.6947) · $10.93 · thesis UTA:SUPPRESSED
- Jack McBain: 1+ goals YES @ 11c · p 0.1383 (adj 0.1287) · $2.35 · thesis UTA:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 8c · p 0.1364 (adj 0.1223) · $7.07 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 12c · p 0.1674 (adj 0.1518) · $5.11 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 36c · p 0.4578 (adj 0.3877) · $4.11 · thesis EDM:SUPPRESSED
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3751 (adj 0.284) · $2.25 · thesis NYR:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2467 (adj 0.2225) · $10.7 · thesis ANA:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8805 (adj 0.8327) · $14.46 · thesis ANA:WINS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1355 (adj 0.1254) · $3.7 · thesis ANA:OFFENSE_4PLUS
- Ottawa over 4.5 goals scored NO @ 74c · p 0.8151 (adj 0.7726) · $9.47 · thesis ANA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ CAR** · priced 177/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 23.11, exp saves 20.33 (sd 5.67), pull risk 0.046
- WPG net: Stuart Skinner (CONFIRMED) exp shots 31.46, exp saves 26.61 (sd 7.37), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jalen Chatfield: 1+ points | 0.316 | 0.135 | 25/98 | +0.053 | STANDARD |
| Kyle Connor: 2+ points | 0.248 | 0.140 | 21/93 | +0.026 | STANDARD |
| Cole Perfetti: 1+ points | 0.535 | 0.430 | 46/60 | +0.057 | STANDARD |
| Jesperi Kotkaniemi: 1+ assists | 0.220 | 0.115 | 22/99 | -0.012 | STANDARD |
| Cole Perfetti: 1+ assists | 0.375 | 0.275 | 28/73 | +0.080 | STANDARD |
| Stuart Skinner: 30+ saves | 0.339 | 0.435 | 48/61 | +0.034 |  |

**MIN @ WSH** · priced 164/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.92, exp saves 25.21 (sd 6.74), pull risk 0.054
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.72, exp saves 23.78 (sd 6.62), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Logan Thompson: 26+ saves | 0.477 | 0.340 | 52/84 | -0.061 |  |
| Kirill Kaprizov: 2+ points | 0.264 | 0.380 | 39/63 | +0.090 | STANDARD |
| Ryan Leonard: 1+ assists | 0.322 | 0.230 | 24/78 | +0.069 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.416 | 0.505 | 51/50 | +0.067 | STANDARD |
| Aliaksei Protas: 1+ goals | 0.246 | 0.160 | 18/86 | +0.056 | STANDARD |
| Aliaksei Protas: 1+ points | 0.459 | 0.375 | 39/64 | +0.053 | STANDARD |

**UTA @ PHI** · priced 154/157 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 27.72, exp saves 23.98 (sd 6.56), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.2, exp saves 21.85 (sd 6.15), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Sanheim: 1+ points | 0.409 | 0.305 | 32/71 | +0.074 | STANDARD |
| Christian Dvorak: 1+ points | 0.473 | 0.370 | 39/65 | +0.066 | STANDARD |
| Matvei Michkov: 1+ assists | 0.394 | 0.295 | 31/72 | +0.069 | STANDARD |
| Christian Dvorak: 1+ goals | 0.253 | 0.155 | 16/85 | +0.083 | STANDARD |
| Clayton Keller: 1+ assists | 0.426 | 0.515 | 52/49 | +0.067 | STANDARD |
| Clayton Keller: 1+ points | 0.570 | 0.655 | 66/35 | +0.064 | STANDARD |

**EDM @ NYR** · priced 163/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.57, exp saves 24.68 (sd 6.89), pull risk 0.069
- EDM net: Matt Tomkins (CONFIRMED) exp shots 25.83, exp saves 22.18 (sd 6.28), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.375 | 0.235 | 26/79 | +0.102 | STANDARD |
| Dylan Garand: 24+ saves | 0.569 | 0.435 | 46/59 | +0.092 |  |
| Vasily Podkolzin: 1+ assists | 0.355 | 0.245 | 26/77 | +0.081 | STANDARD |
| Connor McDavid: 1+ assists | 0.542 | 0.650 | 66/36 | +0.082 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.427 | 0.320 | 33/69 | +0.082 | STANDARD |
| Adam Fox: 2+ assists | 0.228 | 0.125 | 22/97 | -0.004 | STANDARD |

**OTT @ ANA** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.52), pull risk 0.056
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.68, exp saves 23.48 (sd 6.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jake Sanderson: 1+ points | 0.445 | 0.545 | 56/47 | +0.068 | STANDARD |
| A.J. Greer: 1+ goals | 0.247 | 0.150 | 16/86 | +0.077 | STANDARD |
| Thomas Chabot: 1+ assists | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Jake Sanderson: 1+ assists | 0.361 | 0.450 | 46/56 | +0.062 | STANDARD |
| Jackson LaCombe: 1+ points | 0.643 | 0.555 | 57/46 | +0.056 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.580 | 0.495 | 50/51 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
