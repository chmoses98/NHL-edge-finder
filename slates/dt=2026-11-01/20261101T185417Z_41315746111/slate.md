# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T18:54:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 4 · markets on board: 2766 · contracts joined: 868 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 768, 'OK': 62, 'NO_EDGE': 38}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 116, 'game_early_goal': 4, 'first_goal': 139, 'game_winner': 8, 'player_goals': 238, 'game_overtime': 4, 'player_points': 163, 'goalie_saves': 8, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ WSH | 2026-11-01T20:30:00Z | T-90m | 0.558 | 0.442 | 0.182 | 5.92 | 3.13 | 2.80 | 219 (25/194) | CONFIRMED/CONFIRMED |
| UTA @ PHI | 2026-11-01T21:00:00Z | T-90m | 0.452 | 0.548 | 0.178 | 5.86 | 2.78 | 3.09 | 209 (25/184) | CONFIRMED/PROJECTED |
| EDM @ NYR | 2026-11-01T23:00:00Z | T-3h | 0.516 | 0.484 | 0.171 | 6.46 | 3.28 | 3.19 | 222 (25/197) | CONFIRMED/CONFIRMED |
| OTT @ ANA | 2026-11-02T01:00:00Z | T-6h | 0.562 | 0.438 | 0.167 | 6.83 | 3.62 | 3.22 | 218 (25/193) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.562 | 0.465 | 0.484 | 47 | 54 | yes | +0.075 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.438 | 0.535 | 0.516 | 54 | 47 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN4 | team_total | 0.316 | 0.405 | 0.386 | 41 | 60 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4 | team_total | 0.383 | 0.470 | 0.452 | 48 | 54 | no | +0.060 | OK |
| KXNHLGAME-26NOV01UTAPHI-UTA | game_winner | 0.548 | 0.625 | 0.610 | 63 | 38 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.500 | 0.425 | 0.440 | 43 | 58 | yes | +0.052 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.148 | 0.215 | 0.200 | 22 | 79 | no | +0.051 | OK |
| KXNHLGAME-26NOV01MINWSH-MIN | game_winner | 0.442 | 0.515 | 0.500 | 52 | 49 | no | +0.051 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN3 | team_total | 0.534 | 0.610 | 0.595 | 62 | 40 | no | +0.049 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA3 | game_spread | 0.198 | 0.265 | 0.250 | 27 | 74 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN2 | team_total | 0.763 | 0.825 | 0.814 | 83 | 18 | no | +0.046 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.249 | 0.315 | 0.301 | 32 | 69 | no | +0.046 | OK |
| KXNHLGAME-26NOV01UTAPHI-PHI | game_winner | 0.452 | 0.385 | 0.398 | 39 | 62 | yes | +0.045 | OK |
| KXNHLTOTAL-26NOV01MINWSH-6 | game_total | 0.509 | 0.575 | 0.562 | 58 | 43 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN2 | game_spread | 0.233 | 0.295 | 0.282 | 30 | 71 | no | +0.043 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.347 | 0.285 | 0.297 | 29 | 72 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA2 | game_spread | 0.321 | 0.385 | 0.372 | 39 | 62 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.305 | 0.240 | 0.252 | 25 | 77 | yes | +0.042 | OK |
| KXNHLGAME-26NOV01MINWSH-WSH | game_winner | 0.558 | 0.495 | 0.508 | 50 | 51 | yes | +0.041 | OK |
| KXNHLTOTAL-26NOV01MINWSH-5 | game_total | 0.738 | 0.795 | 0.784 | 80 | 21 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA3 | team_total | 0.605 | 0.670 | 0.657 | 68 | 34 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.823 | 0.880 | 0.870 | 89 | 13 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.704 | 0.640 | 0.653 | 65 | 37 | yes | +0.038 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN3 | game_spread | 0.133 | 0.185 | 0.174 | 19 | 82 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2 | team_total | 0.807 | 0.860 | 0.850 | 87 | 15 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA5 | team_total | 0.203 | 0.260 | 0.248 | 27 | 75 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN5 | team_total | 0.157 | 0.210 | 0.198 | 22 | 80 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.411 | 0.470 | 0.458 | 48 | 54 | no | +0.032 | OK |
| KXNHLTOTAL-26NOV01MINWSH-7 | game_total | 0.401 | 0.455 | 0.444 | 46 | 55 | no | +0.031 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-PHI2 | game_spread | 0.242 | 0.195 | 0.204 | 20 | 81 | yes | +0.031 | OK |
| KXNHLTOTAL-26NOV01MINWSH-4 | game_total | 0.832 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.157 | 0.110 | 0.118 | 12 | 90 | yes | +0.030 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-5 | game_total | 0.728 | 0.780 | 0.770 | 79 | 23 | no | +0.029 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-4 | game_total | 0.823 | 0.865 | 0.857 | 87 | 14 | no | +0.028 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.227 | 0.185 | 0.193 | 19 | 82 | yes | +0.027 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-7 | game_total | 0.392 | 0.435 | 0.426 | 44 | 57 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.624 | 0.680 | 0.669 | 70 | 34 | no | +0.021 | OK |
| KXNHLSPREAD-26NOV01MINWSH-WSH2 | game_spread | 0.324 | 0.285 | 0.293 | 29 | 72 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-6 | game_total | 0.504 | 0.545 | 0.537 | 55 | 46 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV01MINWSH-8 | game_total | 0.219 | 0.255 | 0.248 | 26 | 75 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV01MINWSH-9 | game_total | 0.152 | 0.185 | 0.178 | 19 | 82 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.230 | 0.270 | 0.262 | 28 | 74 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR3 | game_spread | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA6 | team_total | 0.089 | 0.115 | 0.109 | 12 | 89 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR2 | team_total | 0.832 | 0.855 | 0.851 | 86 | 15 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR3 | team_total | 0.635 | 0.670 | 0.663 | 68 | 34 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-5 | game_total | 0.802 | 0.830 | 0.825 | 84 | 18 | no | +0.008 | OK |
| KXNHLTOTAL-26NOV01MINWSH-10 | game_total | 0.067 | 0.090 | 0.085 | 10 | 92 | no | +0.008 | OK |
| KXNHLGAME-26NOV01EDMNYR-EDM | game_winner | 0.484 | 0.455 | 0.461 | 46 | 55 | yes | +0.007 | OK |
| KXNHLGAME-26NOV01EDMNYR-NYR | game_winner | 0.516 | 0.545 | 0.539 | 55 | 46 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-3 | game_total | 0.953 | 0.970 | 0.967 | 98 | 4 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-9 | game_total | 0.147 | 0.170 | 0.165 | 18 | 84 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-8 | game_total | 0.215 | 0.240 | 0.235 | 25 | 77 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN6 | team_total | 0.063 | 0.080 | 0.076 | 9 | 93 | no | +0.003 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR2 | game_spread | 0.302 | 0.325 | 0.320 | 33 | 68 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV01MINWSH-3 | game_total | 0.956 | 0.975 | 0.972 | 99 | 4 | no | +0.002 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-EDM2 | game_spread | 0.275 | 0.255 | 0.259 | 26 | 75 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.870 | 0.845 | 0.850 | 86 | 17 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 | team_total | 0.528 | 0.505 | 0.510 | 51 | 50 | yes | +0.001 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-10 | game_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV01OTTANA-4 | game_total | 0.905 | 0.920 | 0.917 | 93 | 9 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-4 | game_total | 0.874 | 0.890 | 0.887 | 90 | 12 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.354 | 0.335 | 0.339 | 34 | 67 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-2 | game_total | 0.989 | 0.980 | 0.982 | 99 | 3 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-10 | game_total | 0.135 | 0.125 | 0.127 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM6 | team_total | 0.103 | 0.090 | 0.093 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-9 | game_total | 0.260 | 0.245 | 0.248 | 25 | 76 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01MINWSH-WSH6 | team_total | 0.092 | 0.080 | 0.082 | 9 | 93 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6 | team_total | 0.060 | 0.050 | 0.052 | 6 | 96 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI2 | team_total | 0.759 | 0.745 | 0.748 | 75 | 26 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV01UTAPHI-PHI3 | game_spread | 0.132 | 0.125 | 0.126 | 13 | 88 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26NOV01MINWSH-WSH3 | game_spread | 0.194 | 0.185 | 0.187 | 19 | 82 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV01UTAPHI-10 | game_total | 0.063 | 0.070 | 0.068 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT6 | team_total | 0.111 | 0.125 | 0.122 | 14 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-7 | game_total | 0.491 | 0.505 | 0.502 | 51 | 50 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI4 | team_total | 0.316 | 0.305 | 0.307 | 31 | 70 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV01MINWSH-2 | game_total | 0.981 | 0.980 | 0.980 | 99 | 3 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-6 | game_total | 0.603 | 0.615 | 0.613 | 62 | 39 |  | -0.010 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MIN @ WSH | 0.558 | 0.553 | 0.182 | 0.217 | 5.92 | 6.25 | 0.939/0.991 | KXNHLTOTAL-26NOV01MINWSH-7 +0.059 |
| UTA @ PHI | 0.452 | 0.497 | 0.178 | 0.218 | 5.86 | 6.11 | 0.995/0.993 | KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 +0.066 |
| EDM @ NYR | 0.516 | 0.503 | 0.171 | 0.211 | 6.46 | 6.68 | 0.988/1.000 | KXNHLTOTAL-26NOV01EDMNYR-7 +0.039 |
| OTT @ ANA | 0.562 | 0.586 | 0.167 | 0.213 | 6.83 | 6.57 | 0.968/1.034 | KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2481 (adj 0.2273) · $10.23 · thesis WSH:OFFENSE_4PLUS
- Kirill Kaprizov: 1+ goals NO @ 56c · p 0.6401 (adj 0.6188) · $20.0 · thesis MIN:SUPPRESSED
- Ryan Leonard: 1+ assists YES @ 24c · p 0.3289 (adj 0.2794) · $7.54 · thesis WSH:OFFENSE_4PLUS
- Yakov Trenin: 1+ goals YES @ 10c · p 0.1306 (adj 0.1205) · $3.78 · thesis MIN:OFFENSE_4PLUS
- Christian Dvorak: 1+ goals YES @ 16c · p 0.249 (adj 0.2255) · $11.32 · thesis PHI:OFFENSE_4PLUS
- Sean Couturier: 1+ goals YES @ 11c · p 0.1863 (adj 0.1635) · $8.36 · thesis PHI:OFFENSE_4PLUS
- Travis Sanheim: 1+ goals YES @ 9c · p 0.1344 (adj 0.1183) · $4.03 · thesis PHI:OFFENSE_4PLUS
- Matvei Michkov: 1+ goals YES @ 26c · p 0.3175 (adj 0.3006) · $6.29 · thesis PHI:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 11c · p 0.1674 (adj 0.1518) · $8.94 · thesis EDM:OFFENSE_4PLUS
- Filip Hallander: 1+ goals YES @ 9c · p 0.1364 (adj 0.121) · $6.18 · thesis EDM:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 8c · p 0.1155 (adj 0.1016) · $3.81 · thesis NYR:OFFENSE_4PLUS
- Ryan Nugent-Hopkins: 1+ assists NO @ 63c · p 0.7145 (adj 0.6698) · $18.61 · thesis EDM:SUPPRESSED
- Ottawa wins by over 2.5 goals NO @ 79c · p 0.8805 (adj 0.8327) · $15.94 · thesis ANA:WINS
- Jeff Malott: 1+ goals YES @ 10c · p 0.1355 (adj 0.1254) · $4.82 · thesis ANA:OFFENSE_4PLUS
- Ottawa over 4.5 goals scored NO @ 74c · p 0.8151 (adj 0.7726) · $14.06 · thesis ANA:WINS
- Fabian Zetterlund: 1+ goals YES @ 17c · p 0.1996 (adj 0.191) · $4.42 · thesis OTT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MIN @ WSH** · priced 164/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (CONFIRMED) exp shots 28.92, exp saves 25.22 (sd 6.8), pull risk 0.057
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.72, exp saves 23.77 (sd 6.61), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Kirill Kaprizov: 2+ points | 0.248 | 0.380 | 39/63 | +0.106 | STANDARD |
| Kirill Kaprizov: 1+ assists | 0.400 | 0.505 | 51/50 | +0.082 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.613 | 0.715 | 72/29 | +0.083 | STANDARD |
| Ryan Leonard: 1+ assists | 0.329 | 0.230 | 24/78 | +0.076 | STANDARD |
| Matt Boldy: 1+ assists | 0.373 | 0.470 | 48/54 | +0.069 | STANDARD |
| Quinn Hughes: 1+ assists | 0.518 | 0.610 | 62/40 | +0.065 | STANDARD |

**UTA @ PHI** · priced 155/158 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (CONFIRMED) exp shots 27.72, exp saves 24.01 (sd 6.51), pull risk 0.058
- UTA net: Karel Vejmelka (PROJECTED) exp shots 25.2, exp saves 21.85 (sd 6.23), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Sanheim: 1+ points | 0.416 | 0.285 | 31/74 | +0.091 | STANDARD |
| Christian Dvorak: 1+ points | 0.475 | 0.370 | 38/64 | +0.079 | STANDARD |
| Christian Dvorak: 1+ goals | 0.249 | 0.155 | 16/85 | +0.080 | STANDARD |
| Clayton Keller: 1+ assists | 0.422 | 0.515 | 52/49 | +0.071 | STANDARD |
| Sean Couturier: 1+ goals | 0.186 | 0.095 | 11/92 | +0.069 | STANDARD |
| Travis Sanheim: 1+ assists | 0.330 | 0.240 | 26/78 | +0.056 | STANDARD |

**EDM @ NYR** · priced 163/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.57, exp saves 24.68 (sd 6.89), pull risk 0.069
- EDM net: Matt Tomkins (CONFIRMED) exp shots 25.83, exp saves 22.18 (sd 6.28), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Dylan Garand: 24+ saves | 0.569 | 0.435 | 46/59 | +0.092 |  |
| Vladislav Gavrikov: 1+ assists | 0.375 | 0.245 | 26/77 | +0.102 | STANDARD |
| Connor McDavid: 2+ assists | 0.181 | 0.295 | 30/71 | +0.094 | STANDARD |
| Connor McDavid: 1+ assists | 0.542 | 0.655 | 66/35 | +0.092 | STANDARD |
| Vladislav Gavrikov: 1+ points | 0.427 | 0.320 | 33/69 | +0.082 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.355 | 0.250 | 26/76 | +0.081 | STANDARD |

**OTT @ ANA** · priced 164/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.63 (sd 6.52), pull risk 0.056
- OTT net: Jonas Johansson (PROJECTED) exp shots 27.68, exp saves 23.48 (sd 6.69), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.247 | 0.145 | 16/87 | +0.077 | STANDARD |
| Jake Sanderson: 1+ points | 0.445 | 0.540 | 55/47 | +0.068 | STANDARD |
| Thomas Chabot: 1+ assists | 0.246 | 0.340 | 35/67 | +0.069 | STANDARD |
| Jake Sanderson: 1+ assists | 0.361 | 0.455 | 47/56 | +0.062 | STANDARD |
| Alex Killorn: 1+ points | 0.457 | 0.365 | 39/66 | +0.051 | STANDARD |
| Jackson LaCombe: 1+ points | 0.643 | 0.555 | 57/46 | +0.056 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
