# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T17:04:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2797 · contracts joined: 1093 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 968, 'OK': 72, 'NO_EDGE': 53}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 150, 'game_early_goal': 5, 'first_goal': 174, 'game_winner': 10, 'player_goals': 299, 'game_overtime': 5, 'player_points': 210, 'goalie_saves': 5, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CAR | 2026-11-01T18:00:00Z | T-30m | 0.701 | 0.299 | 0.161 | 5.95 | 3.61 | 2.34 | 231 (25/206) | CONFIRMED/PROJECTED |
| MIN @ WSH | 2026-11-01T20:30:00Z | T-3h | 0.535 | 0.465 | 0.177 | 6.04 | 3.12 | 2.91 | 218 (25/193) | PROJECTED/CONFIRMED |
| UTA @ PHI | 2026-11-01T21:00:00Z | T-3h | 0.444 | 0.556 | 0.184 | 5.92 | 2.78 | 3.14 | 207 (25/182) | PROJECTED/PROJECTED |
| EDM @ NYR | 2026-11-01T23:00:00Z | T-3h | 0.516 | 0.484 | 0.171 | 6.46 | 3.28 | 3.19 | 220 (25/195) | CONFIRMED/CONFIRMED |
| OTT @ ANA | 2026-11-02T01:00:00Z | T-6h | 0.562 | 0.438 | 0.167 | 6.83 | 3.62 | 3.22 | 217 (25/192) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.562 | 0.465 | 0.484 | 47 | 54 | yes | +0.075 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.438 | 0.525 | 0.507 | 53 | 48 | no | +0.065 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.704 | 0.635 | 0.649 | 64 | 37 | yes | +0.048 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.347 | 0.285 | 0.297 | 29 | 72 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.500 | 0.430 | 0.444 | 44 | 58 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.305 | 0.240 | 0.252 | 25 | 77 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN4 | team_total | 0.343 | 0.410 | 0.396 | 42 | 60 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4 | team_total | 0.392 | 0.460 | 0.446 | 47 | 55 | no | +0.040 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA3 | game_spread | 0.199 | 0.255 | 0.243 | 26 | 75 | no | +0.038 | OK |
| KXNHLGAME-26NOV01UTAPHI-PHI | game_winner | 0.444 | 0.385 | 0.397 | 39 | 62 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA3 | team_total | 0.618 | 0.680 | 0.668 | 69 | 33 | no | +0.037 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA2 | game_spread | 0.328 | 0.385 | 0.373 | 39 | 62 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.411 | 0.470 | 0.458 | 48 | 54 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-6 | game_total | 0.522 | 0.575 | 0.564 | 58 | 43 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.157 | 0.110 | 0.118 | 12 | 90 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.823 | 0.870 | 0.861 | 88 | 14 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-4 | game_total | 0.834 | 0.875 | 0.868 | 88 | 13 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2 | team_total | 0.814 | 0.860 | 0.852 | 87 | 15 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN2 | team_total | 0.783 | 0.830 | 0.821 | 84 | 18 | no | +0.027 | OK |
| KXNHLGAME-26NOV01UTAPHI-UTA | game_winner | 0.556 | 0.605 | 0.595 | 61 | 40 | no | +0.027 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN3 | game_spread | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-5 | game_total | 0.742 | 0.785 | 0.777 | 79 | 22 | no | +0.026 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-5 | game_total | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA5 | team_total | 0.214 | 0.260 | 0.250 | 27 | 75 | no | +0.023 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-PHI2 | game_spread | 0.233 | 0.195 | 0.202 | 20 | 81 | yes | +0.022 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-4 | game_total | 0.830 | 0.865 | 0.858 | 87 | 14 | no | +0.022 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN2 | game_spread | 0.255 | 0.295 | 0.287 | 30 | 71 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN3 | team_total | 0.562 | 0.610 | 0.601 | 62 | 40 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.624 | 0.675 | 0.665 | 69 | 34 | no | +0.021 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-7 | game_total | 0.404 | 0.445 | 0.437 | 45 | 56 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV01MINWSH-4 | game_total | 0.843 | 0.875 | 0.869 | 88 | 13 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV01MINWSH-6 | game_total | 0.535 | 0.575 | 0.567 | 58 | 43 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR4 | team_total | 0.505 | 0.545 | 0.537 | 55 | 46 | no | +0.018 | OK |
| KXNHLGAME-26NOV01MINWSH-MIN | game_winner | 0.465 | 0.505 | 0.497 | 51 | 50 | no | +0.017 | OK |
| KXNHLGAME-26NOV01MINWSH-WSH | game_winner | 0.535 | 0.495 | 0.503 | 50 | 51 | yes | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.230 | 0.270 | 0.262 | 28 | 74 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR2 | team_total | 0.877 | 0.910 | 0.904 | 92 | 10 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR5 | team_total | 0.299 | 0.335 | 0.328 | 34 | 67 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR3 | game_spread | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV01MINWSH-5 | game_total | 0.753 | 0.790 | 0.783 | 80 | 22 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN5 | team_total | 0.174 | 0.210 | 0.202 | 22 | 80 | no | +0.015 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-7 | game_total | 0.399 | 0.435 | 0.428 | 44 | 57 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR6 | team_total | 0.147 | 0.175 | 0.169 | 18 | 83 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-6 | game_total | 0.510 | 0.545 | 0.538 | 55 | 46 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-8 | game_total | 0.225 | 0.260 | 0.253 | 27 | 75 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-9 | game_total | 0.149 | 0.175 | 0.170 | 18 | 83 | no | +0.011 | OK |
| KXNHLSPREAD-26NOV01WPGCAR-CAR3 | game_spread | 0.324 | 0.355 | 0.349 | 36 | 65 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA6 | team_total | 0.094 | 0.115 | 0.110 | 12 | 89 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-4 | game_total | 0.874 | 0.895 | 0.891 | 90 | 11 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR2 | team_total | 0.832 | 0.865 | 0.859 | 88 | 15 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV01MINWSH-9 | game_total | 0.162 | 0.185 | 0.180 | 19 | 82 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV01MINWSH-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLGAME-26NOV01EDMNYR-EDM | game_winner | 0.484 | 0.455 | 0.461 | 46 | 55 | yes | +0.007 | OK |
| KXNHLGAME-26NOV01EDMNYR-NYR | game_winner | 0.516 | 0.545 | 0.539 | 55 | 46 | no | +0.007 | OK |
| KXNHLSPREAD-26NOV01MINWSH-WSH2 | game_spread | 0.311 | 0.285 | 0.290 | 29 | 72 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.006 | OK |
| KXNHLGAME-26NOV01WPGCAR-CAR | game_winner | 0.701 | 0.725 | 0.720 | 73 | 28 | no | +0.005 | OK |
| KXNHLGAME-26NOV01WPGCAR-WPG | game_winner | 0.299 | 0.275 | 0.280 | 28 | 73 | yes | +0.005 | OK |
| KXNHLTOTAL-26NOV01MINWSH-10 | game_total | 0.070 | 0.085 | 0.082 | 9 | 92 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV01WPGCAR-CAR3 | team_total | 0.712 | 0.740 | 0.735 | 75 | 27 | no | +0.004 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR2 | game_spread | 0.302 | 0.325 | 0.320 | 33 | 68 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-3 | game_total | 0.956 | 0.970 | 0.968 | 98 | 4 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-EDM2 | game_spread | 0.275 | 0.255 | 0.259 | 26 | 75 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.870 | 0.845 | 0.850 | 86 | 17 | yes | +0.001 | OK |
| KXNHLSPREAD-26NOV01WPGCAR-CAR2 | game_spread | 0.472 | 0.495 | 0.490 | 50 | 51 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV01MINWSH-7 | game_total | 0.422 | 0.445 | 0.440 | 45 | 56 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01WPGCAR-3 | game_total | 0.957 | 0.965 | 0.964 | 97 | 4 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV01MINWSH-8 | game_total | 0.237 | 0.260 | 0.255 | 27 | 75 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.905 | 0.920 | 0.917 | 93 | 9 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR3 | team_total | 0.635 | 0.665 | 0.659 | 68 | 35 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01WPGCAR-10 | game_total | 0.068 | 0.075 | 0.073 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01WPGCAR-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV01WPGCAR-WPG3 | game_spread | 0.068 | 0.075 | 0.074 | 8 | 93 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-5 | game_total | 0.802 | 0.820 | 0.816 | 83 | 19 |  | -0.003 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CAR | 0.701 | 0.636 | 0.161 | 0.213 | 5.95 | 6.36 | 1.003/1.002 | KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG3 +0.106 |
| MIN @ WSH | 0.535 | 0.542 | 0.177 | 0.216 | 6.04 | 6.31 | 0.961/0.991 | KXNHLTOTAL-26NOV01MINWSH-7 +0.048 |
| UTA @ PHI | 0.444 | 0.495 | 0.184 | 0.221 | 5.92 | 6.11 | 0.994/0.993 | KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 +0.068 |
| EDM @ NYR | 0.516 | 0.503 | 0.171 | 0.211 | 6.46 | 6.68 | 0.988/1.000 | KXNHLTOTAL-26NOV01EDMNYR-7 +0.039 |
| OTT @ ANA | 0.562 | 0.586 | 0.167 | 0.213 | 6.83 | 6.57 | 0.968/1.034 | KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 20 recommended · full analysis in card.md / packet.json `thesis_card`

- Gabriel Vilardi: 1+ goals YES @ 21c · p 0.2624 (adj 0.2481) · $5.56 · thesis WPG:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 71c · p 0.7623 (adj 0.748) · $12.03 · thesis CAR:SUPPRESSED
- Mark Scheifele: 1+ goals YES @ 26c · p 0.3108 (adj 0.2969) · $5.41 · thesis WPG:OFFENSE_4PLUS
- Sebastian Aho: 1+ goals NO @ 66c · p 0.7105 (adj 0.6954) · $8.86 · thesis CAR:SUPPRESSED
- Kirill Kaprizov: 1+ goals NO @ 55c · p 0.6385 (adj 0.6151) · $13.93 · thesis MIN:SUPPRESSED
- Aliaksei Protas: 1+ goals YES @ 18c · p 0.246 (adj 0.2258) · $6.92 · thesis WSH:OFFENSE_4PLUS
- Pierre-Luc Dubois: 1+ goals YES @ 18c · p 0.2252 (adj 0.2114) · $4.19 · thesis WSH:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1317 (adj 0.1213) · $2.73 · thesis MIN:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.2529 (adj 0.2284) · $9.7 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 12c · p 0.1896 (adj 0.1709) · $6.55 · thesis PHI:OFFENSE_4PLUS
- Noah Cates: 1+ goals YES @ 12c · p 0.1727 (adj 0.157) · $4.65 · thesis PHI:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 66c · p 0.708 (adj 0.6947) · $9.67 · thesis UTA:SUPPRESSED
- Alex Formenton: 1+ goals YES @ 12c · p 0.1674 (adj 0.1518) · $4.44 · thesis EDM:OFFENSE_4PLUS
- Vladislav Gavrikov: 1+ assists YES @ 26c · p 0.3751 (adj 0.297) · $4.88 · thesis NYR:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 71c · p 0.8187 (adj 0.7415) · $13.93 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 26c · p 0.3549 (adj 0.2867) · $3.09 · thesis EDM:OFFENSE_4PLUS
- A.J. Greer: 1+ goals YES @ 16c · p 0.2467 (adj 0.2225) · $9.34 · thesis ANA:OFFENSE_4PLUS
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8805 (adj 0.8327) · $12.63 · thesis ANA:WINS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1355 (adj 0.1254) · $3.23 · thesis ANA:OFFENSE_4PLUS
- Ottawa over 4.5 goals scored NO @ 74c · p 0.8151 (adj 0.7726) · $8.27 · thesis ANA:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ CAR** · priced 176/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (CONFIRMED) exp shots 23.11, exp saves 20.36 (sd 5.68), pull risk 0.044
- WPG net: Stuart Skinner (PROJECTED) exp shots 31.46, exp saves 26.54 (sd 7.37), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jalen Chatfield: 1+ points | 0.323 | 0.215 | 26/83 | +0.049 | STANDARD |
| Cole Perfetti: 1+ assists | 0.377 | 0.275 | 28/73 | +0.083 | STANDARD |
| Jesperi Kotkaniemi: 1+ assists | 0.222 | 0.125 | 23/98 | -0.021 | STANDARD |
| Sebastian Aho: 1+ points | 0.560 | 0.655 | 66/35 | +0.074 | STANDARD |
| Cole Perfetti: 1+ points | 0.542 | 0.450 | 46/56 | +0.064 | STANDARD |
| Shayne Gostisbehere: 1+ assists | 0.374 | 0.465 | 47/54 | +0.069 | STANDARD |

**MIN @ WSH** · priced 163/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.92, exp saves 25.21 (sd 6.74), pull risk 0.054
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.72, exp saves 23.78 (sd 6.62), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.264 | 0.380 | 39/63 | +0.090 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.623 | 0.720 | 74/30 | +0.063 | STANDARD |
| Kirill Kaprizov: 1+ goals | 0.361 | 0.455 | 46/55 | +0.071 | STANDARD |
| Quinn Hughes: 2+ points | 0.219 | 0.310 | 32/70 | +0.067 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.416 | 0.505 | 51/50 | +0.067 | STANDARD |
| Ryan Leonard: 1+ assists | 0.322 | 0.235 | 25/78 | +0.059 | STANDARD |

**UTA @ PHI** · priced 153/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 27.72, exp saves 23.98 (sd 6.56), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.2, exp saves 21.85 (sd 6.15), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Sanheim: 1+ points | 0.409 | 0.305 | 32/71 | +0.074 | STANDARD |
| Christian Dvorak: 1+ goals | 0.253 | 0.155 | 16/85 | +0.083 | STANDARD |
| Matvei Michkov: 1+ assists | 0.394 | 0.300 | 31/71 | +0.069 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Clayton Keller: 2+ points | 0.212 | 0.305 | 32/71 | +0.064 | STANDARD |
| Christian Dvorak: 1+ points | 0.473 | 0.380 | 39/63 | +0.066 | STANDARD |

**EDM @ NYR** · priced 161/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.57, exp saves 24.68 (sd 6.89), pull risk 0.069
- EDM net: Matt Tomkins (CONFIRMED) exp shots 25.83, exp saves 22.18 (sd 6.28), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vladislav Gavrikov: 1+ assists | 0.375 | 0.255 | 26/75 | +0.102 | STANDARD |
| Dylan Garand: 24+ saves | 0.569 | 0.450 | 49/59 | +0.062 |  |
| Connor McDavid: 2+ assists | 0.181 | 0.300 | 31/71 | +0.094 | STANDARD |
| Connor McDavid: 1+ assists | 0.542 | 0.650 | 66/36 | +0.082 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.355 | 0.250 | 26/76 | +0.081 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.427 | 0.325 | 33/68 | +0.082 | STANDARD |

**OTT @ ANA** · priced 163/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.52), pull risk 0.056
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.68, exp saves 23.48 (sd 6.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.247 | 0.150 | 16/86 | +0.077 | STANDARD |
| Jake Sanderson: 1+ points | 0.445 | 0.540 | 55/47 | +0.068 | STANDARD |
| Thomas Chabot: 1+ assists | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Jackson LaCombe: 2+ points | 0.263 | 0.175 | 20/85 | +0.052 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.580 | 0.495 | 50/51 | +0.062 | STANDARD |
| Jake Sanderson: 1+ assists | 0.361 | 0.445 | 45/56 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
