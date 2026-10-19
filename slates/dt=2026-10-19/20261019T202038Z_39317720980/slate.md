# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T20:20:38Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3201 · contracts joined: 977 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 877, 'NO_EDGE': 56, 'OK': 44}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 153, 'game_early_goal': 4, 'first_goal': 146, 'game_winner': 8, 'player_goals': 253, 'game_overtime': 4, 'player_points': 213, 'goalie_saves': 8, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-90m | 0.596 | 0.404 | 0.174 | 6.12 | 3.35 | 2.77 | 242 (25/217) | CONFIRMED/CONFIRMED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-90m | 0.368 | 0.632 | 0.176 | 5.93 | 2.56 | 3.38 | 235 (25/210) | CONFIRMED/CONFIRMED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-3h | 0.547 | 0.453 | 0.166 | 6.94 | 3.63 | 3.30 | 248 (25/223) | CONFIRMED/CONFIRMED |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-3h | 0.622 | 0.378 | 0.159 | 6.83 | 3.82 | 3.01 | 252 (25/227) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.451 | 0.540 | 0.522 | 55 | 47 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.257 | 0.335 | 0.318 | 34 | 67 | no | +0.058 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.368 | 0.305 | 0.317 | 31 | 70 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.252 | 0.315 | 0.302 | 32 | 69 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT19ANANYR-7 | game_total | 0.433 | 0.495 | 0.482 | 50 | 51 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.759 | 0.815 | 0.805 | 82 | 19 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT19ANANYR-6 | game_total | 0.545 | 0.605 | 0.593 | 61 | 40 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.671 | 0.730 | 0.719 | 74 | 28 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.632 | 0.685 | 0.675 | 69 | 32 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.312 | 0.365 | 0.354 | 37 | 64 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.832 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.738 | 0.785 | 0.776 | 79 | 22 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.848 | 0.885 | 0.878 | 89 | 12 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.117 | 0.160 | 0.151 | 17 | 85 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.851 | 0.890 | 0.883 | 90 | 12 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.148 | 0.115 | 0.121 | 12 | 89 | yes | +0.020 | OK |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.249 | 0.285 | 0.278 | 29 | 72 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.116 | 0.145 | 0.139 | 15 | 86 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.212 | 0.245 | 0.238 | 25 | 76 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT19ANANYR-9 | game_total | 0.174 | 0.205 | 0.198 | 21 | 80 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.518 | 0.555 | 0.548 | 56 | 45 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.120 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.369 | 0.335 | 0.342 | 34 | 67 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.277 | 0.245 | 0.251 | 25 | 76 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.955 | 0.980 | 0.976 | 99 | 3 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.224 | 0.255 | 0.249 | 26 | 75 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR6 | team_total | 0.161 | 0.135 | 0.140 | 14 | 87 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR4 | team_total | 0.442 | 0.475 | 0.468 | 48 | 53 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR5 | team_total | 0.247 | 0.280 | 0.273 | 29 | 73 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.151 | 0.175 | 0.170 | 18 | 83 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.178 | 0.150 | 0.155 | 16 | 86 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.404 | 0.435 | 0.429 | 44 | 57 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.153 | 0.175 | 0.170 | 18 | 83 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.962 | 0.975 | 0.973 | 98 | 3 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.133 | 0.115 | 0.118 | 12 | 89 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.061 | 0.075 | 0.072 | 8 | 93 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR3 | team_total | 0.662 | 0.690 | 0.684 | 70 | 32 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.045 | 0.035 | 0.037 | 4 | 97 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.086 | 0.075 | 0.077 | 8 | 93 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.066 | 0.080 | 0.077 | 9 | 93 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.276 | 0.295 | 0.291 | 30 | 71 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.980 | 0.975 | 0.976 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.906 | 0.915 | 0.913 | 92 | 9 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT19ANANYR-NYR3 | game_spread | 0.229 | 0.245 | 0.242 | 25 | 76 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.844 | 0.855 | 0.853 | 86 | 15 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4 | team_total | 0.504 | 0.485 | 0.489 | 49 | 52 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.845 | 0.855 | 0.853 | 86 | 15 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.092 | 0.085 | 0.086 | 9 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-4 | game_total | 0.908 | 0.915 | 0.914 | 92 | 9 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR5 | team_total | 0.311 | 0.290 | 0.294 | 30 | 72 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT5 | team_total | 0.197 | 0.180 | 0.183 | 19 | 83 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-6 | game_total | 0.671 | 0.655 | 0.658 | 66 | 35 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ3 | team_total | 0.641 | 0.625 | 0.628 | 63 | 38 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.247 | 0.230 | 0.233 | 24 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-10 | game_total | 0.080 | 0.090 | 0.088 | 10 | 92 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.118 | 0.125 | 0.124 | 13 | 88 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI5 | team_total | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.378 | 0.365 | 0.368 | 37 | 64 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-UTA | game_winner | 0.622 | 0.635 | 0.632 | 64 | 37 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.891 | 0.900 | 0.898 | 91 | 11 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.839 | 0.850 | 0.848 | 86 | 16 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3 | team_total | 0.479 | 0.460 | 0.464 | 47 | 55 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT2 | game_spread | 0.201 | 0.195 | 0.196 | 20 | 81 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ3 | game_spread | 0.161 | 0.165 | 0.164 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-TOR2 | game_spread | 0.345 | 0.335 | 0.337 | 34 | 67 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-ANA | game_winner | 0.404 | 0.415 | 0.413 | 42 | 59 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-NYR | game_winner | 0.596 | 0.585 | 0.587 | 59 | 42 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.114 | 0.115 | 0.115 | 12 | 89 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ2 | game_spread | 0.262 | 0.255 | 0.256 | 26 | 75 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.789 | 0.785 | 0.786 | 79 | 22 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-7 | game_total | 0.565 | 0.555 | 0.557 | 56 | 45 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.183 | 0.185 | 0.185 | 19 | 82 |  | -0.014 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.596 | 0.544 | 0.174 | 0.212 | 6.12 | 6.51 | 0.988/1.043 | KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 +0.078 |
| COL @ PHI | 0.368 | 0.449 | 0.176 | 0.222 | 5.93 | 5.96 | 0.990/0.979 | KXNHLGAME-26OCT19COLPHI-COL -0.081 |
| SJS @ TOR | 0.547 | 0.526 | 0.166 | 0.216 | 6.94 | 6.44 | 0.988/1.040 | KXNHLTOTAL-26OCT19SJTOR-6 -0.080 |
| PIT @ UTA | 0.622 | 0.585 | 0.159 | 0.207 | 6.83 | 6.69 | 1.001/1.042 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.216 (adj 0.1958) · $10.31 · thesis ANA:OFFENSE_4PLUS
- A.J. Greer: 2+ goals YES @ 1c · p 0.0289 (adj 0.0242) · $1.75 · thesis ANA:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 9c · p 0.1169 (adj 0.1089) · $3.52 · thesis NYR:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1175 (adj 0.1069) · $2.74 · thesis ANA:OFFENSE_4PLUS
- Nathan MacKinnon: 2+ goals NO @ 86c · p 0.9187 (adj 0.9028) · $19.81 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.6226 (adj 0.6045) · $10.19 · thesis COL:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7959 (adj 0.7108) · $19.55 · thesis PHI:WINS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1441 (adj 0.1343) · $4.51 · thesis TOR:OFFENSE_4PLUS
- Mason Marchment: 1+ assists NO @ 70c · p 0.7838 (adj 0.7344) · $18.91 · thesis SJS:SUPPRESSED
- Yaroslav Askarov: 26+ saves NO @ 56c · p 0.6448 (adj 0.5949) · $10.05 · thesis SJS:NET_LOW_VOLUME
- Mason Marchment: 1+ goals YES @ 20c · p 0.2329 (adj 0.2234) · $3.76 · thesis SJS:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 11c · p 0.1576 (adj 0.1432) · $6.76 · thesis PIT:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 13c · p 0.1691 (adj 0.1568) · $5.23 · thesis UTA:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 29c · p 0.345 (adj 0.3287) · $8.16 · thesis PIT:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 27c · p 0.3211 (adj 0.3058) · $7.25 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 186/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 28.93, exp saves 25.07 (sd 6.81), pull risk 0.063
- ANA net: Ville Husso (CONFIRMED) exp shots 24.95, exp saves 21.3 (sd 6.11), pull risk 0.078

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Washe: 1+ points | 0.319 | 0.175 | 24/89 | +0.066 | STANDARD |
| Noah Warren: 1+ assists | 0.230 | 0.095 | 17/98 | +0.050 | PRIOR_HEAVY |
| Vladislav Gavrikov: 1+ assists | 0.334 | 0.205 | 24/83 | +0.081 | STANDARD |
| Tim Washe: 1+ assists | 0.224 | 0.100 | 18/98 | +0.034 | STANDARD |
| Noah Laba: 1+ assists | 0.213 | 0.090 | 16/98 | +0.043 | STANDARD |
| Ville Husso: 25+ saves | 0.294 | 0.410 | 42/60 | +0.089 |  |

**COL @ PHI** · priced 169/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 30.72, exp saves 26.46 (sd 7.12), pull risk 0.061
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 24.25, exp saves 21.17 (sd 5.84), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.402 | 0.600 | 61/41 | +0.171 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.302 | 0.485 | 50/53 | +0.151 | STANDARD |
| Cale Makar: 2+ points | 0.157 | 0.325 | 34/69 | +0.138 | STANDARD |
| Cale Makar: 1+ points | 0.507 | 0.670 | 68/34 | +0.138 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.462 | 0.610 | 62/40 | +0.121 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.099 | 0.245 | 25/76 | +0.128 | STANDARD |

**SJS @ TOR** · priced 183/197 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.27, exp saves 25.39 (sd 6.92), pull risk 0.062
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.18, exp saves 23.37 (sd 6.42), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colton Sissons: 1+ points | 0.352 | 0.175 | 27/92 | +0.068 | STANDARD |
| Michael Kesselring: 1+ assists | 0.194 | 0.080 | 14/98 | +0.046 | STANDARD |
| Michael Kesselring: 1+ points | 0.236 | 0.130 | 19/93 | +0.035 | STANDARD |
| Ivar Stenberg: 1+ points | 0.363 | 0.465 | 47/54 | +0.079 | PRIOR_HEAVY |
| Yaroslav Askarov: 26+ saves | 0.355 | 0.455 | 47/56 | +0.068 |  |
| Mason Marchment: 1+ assists | 0.216 | 0.315 | 33/70 | +0.069 | STANDARD |

**PIT @ UTA** · priced 192/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Sebastian Cossa (CONFIRMED) exp shots 26.47, exp saves 22.95 (sd 6.37), pull risk 0.062
- PIT net: Arturs Silovs (CONFIRMED) exp shots 27.66, exp saves 23.55 (sd 6.68), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.228 | 0.335 | 35/68 | +0.077 | STANDARD |
| Nick Robertson: 1+ assists | 0.208 | 0.105 | 19/98 | +0.007 | STANDARD |
| Rickard Rakell: 1+ points | 0.597 | 0.495 | 51/52 | +0.069 | STANDARD |
| Rickard Rakell: 1+ assists | 0.405 | 0.310 | 32/70 | +0.070 | STANDARD |
| Declan Carlile: 1+ points | 0.260 | 0.165 | 20/87 | +0.049 | STANDARD |
| Nate Schmidt: 1+ assists | 0.258 | 0.165 | 20/87 | +0.046 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
