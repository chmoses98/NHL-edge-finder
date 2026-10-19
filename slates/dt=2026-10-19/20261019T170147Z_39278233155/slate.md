# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T17:01:47Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3124 · contracts joined: 900 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 800, 'NO_EDGE': 56, 'OK': 44}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 123, 'game_early_goal': 4, 'first_goal': 147, 'game_winner': 8, 'player_goals': 254, 'game_overtime': 4, 'player_points': 166, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-3h | 0.581 | 0.419 | 0.176 | 6.13 | 3.32 | 2.81 | 220 (25/195) | PROBABLE/PROJECTED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-3h | 0.373 | 0.627 | 0.171 | 5.95 | 2.57 | 3.38 | 204 (25/179) | CONFIRMED/PROJECTED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-6h | 0.546 | 0.454 | 0.167 | 6.90 | 3.59 | 3.30 | 234 (25/209) | CONFIRMED/PROBABLE |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-6h | 0.619 | 0.381 | 0.165 | 6.69 | 3.75 | 2.94 | 242 (25/217) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.255 | 0.335 | 0.318 | 34 | 67 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.449 | 0.530 | 0.514 | 54 | 48 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.398 | 0.465 | 0.451 | 47 | 54 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.252 | 0.320 | 0.306 | 33 | 69 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT19ANANYR-7 | game_total | 0.435 | 0.495 | 0.483 | 50 | 51 | no | +0.038 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.037 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.763 | 0.820 | 0.809 | 83 | 19 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.672 | 0.730 | 0.719 | 74 | 28 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT19ANANYR-6 | game_total | 0.550 | 0.605 | 0.594 | 61 | 40 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.536 | 0.585 | 0.575 | 59 | 42 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.742 | 0.790 | 0.781 | 80 | 22 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.849 | 0.885 | 0.878 | 89 | 12 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.321 | 0.370 | 0.360 | 38 | 64 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.851 | 0.890 | 0.883 | 90 | 12 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.524 | 0.565 | 0.557 | 57 | 44 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.407 | 0.445 | 0.437 | 45 | 56 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.250 | 0.285 | 0.278 | 29 | 72 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR4 | team_total | 0.437 | 0.475 | 0.467 | 48 | 53 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.141 | 0.115 | 0.120 | 12 | 89 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.118 | 0.150 | 0.143 | 16 | 86 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT19ANANYR-9 | game_total | 0.176 | 0.205 | 0.199 | 21 | 80 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.225 | 0.255 | 0.249 | 26 | 75 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.120 | 0.145 | 0.140 | 15 | 86 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR5 | team_total | 0.245 | 0.280 | 0.273 | 29 | 73 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.180 | 0.155 | 0.160 | 16 | 85 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR3 | team_total | 0.655 | 0.690 | 0.683 | 70 | 32 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.218 | 0.245 | 0.240 | 25 | 76 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.093 | 0.075 | 0.078 | 8 | 93 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.271 | 0.240 | 0.246 | 25 | 77 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.115 | 0.135 | 0.131 | 14 | 87 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.153 | 0.180 | 0.174 | 19 | 83 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT19ANANYR-NYR3 | game_spread | 0.222 | 0.245 | 0.240 | 25 | 76 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.826 | 0.845 | 0.841 | 85 | 16 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.763 | 0.795 | 0.789 | 81 | 22 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.121 | 0.100 | 0.104 | 11 | 91 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT19ANANYR-10 | game_total | 0.080 | 0.095 | 0.092 | 10 | 91 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.954 | 0.975 | 0.972 | 99 | 4 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.158 | 0.185 | 0.179 | 20 | 83 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.893 | 0.905 | 0.903 | 91 | 10 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.841 | 0.855 | 0.852 | 86 | 15 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.842 | 0.855 | 0.853 | 86 | 15 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.067 | 0.080 | 0.077 | 9 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-6 | game_total | 0.636 | 0.655 | 0.651 | 66 | 35 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.124 | 0.115 | 0.117 | 12 | 89 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-7 | game_total | 0.526 | 0.550 | 0.545 | 56 | 46 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.887 | 0.900 | 0.897 | 91 | 11 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.361 | 0.340 | 0.344 | 35 | 67 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR6 | team_total | 0.154 | 0.140 | 0.143 | 15 | 87 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR2 | team_total | 0.867 | 0.875 | 0.873 | 88 | 13 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.381 | 0.365 | 0.368 | 37 | 64 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-UTA | game_winner | 0.619 | 0.635 | 0.632 | 64 | 37 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.247 | 0.230 | 0.233 | 24 | 78 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.078 | 0.070 | 0.072 | 8 | 94 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ3 | game_spread | 0.158 | 0.165 | 0.164 | 17 | 84 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.110 | 0.120 | 0.118 | 13 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3 | team_total | 0.480 | 0.460 | 0.464 | 47 | 55 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ4 | team_total | 0.429 | 0.415 | 0.418 | 42 | 59 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.046 | 0.040 | 0.041 | 5 | 97 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.065 | 0.075 | 0.073 | 9 | 94 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-TOR3 | game_spread | 0.217 | 0.225 | 0.223 | 23 | 78 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ3 | team_total | 0.637 | 0.625 | 0.627 | 63 | 38 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.778 | 0.790 | 0.788 | 80 | 22 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.276 | 0.285 | 0.283 | 29 | 72 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-8 | game_total | 0.326 | 0.335 | 0.333 | 34 | 67 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA5 | team_total | 0.326 | 0.340 | 0.337 | 35 | 67 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT19ANANYR-NYR2 | game_spread | 0.356 | 0.365 | 0.363 | 37 | 64 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.173 | 0.180 | 0.179 | 19 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-4 | game_total | 0.907 | 0.910 | 0.909 | 92 | 10 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-6 | game_total | 0.662 | 0.655 | 0.657 | 66 | 35 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI5 | team_total | 0.125 | 0.120 | 0.121 | 13 | 89 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA3 | team_total | 0.730 | 0.740 | 0.738 | 75 | 27 |  | -0.014 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.581 | 0.535 | 0.176 | 0.213 | 6.13 | 6.47 | 0.990/1.024 | KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 +0.076 |
| COL @ PHI | 0.373 | 0.445 | 0.171 | 0.220 | 5.95 | 5.95 | 0.990/0.976 | KXNHLSPREAD-26OCT19COLPHI-COL2 -0.077 |
| SJS @ TOR | 0.546 | 0.531 | 0.167 | 0.218 | 6.90 | 6.44 | 0.988/1.037 | KXNHLTOTAL-26OCT19SJTOR-8 -0.074 |
| PIT @ UTA | 0.619 | 0.582 | 0.165 | 0.213 | 6.69 | 6.66 | 0.993/1.033 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.050 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.2281 (adj 0.2048) · $14.65 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1341 (adj 0.1243) · $4.61 · thesis ANA:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 9c · p 0.1193 (adj 0.1095) · $3.67 · thesis NYR:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ assists NO @ 69c · p 0.7582 (adj 0.7191) · $13.48 · thesis NYR:SUPPRESSED
- Nathan MacKinnon: 2+ goals NO @ 87c · p 0.9165 (adj 0.9024) · $20.0 · thesis COL:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7977 (adj 0.7114) · $20.0 · thesis PHI:WINS
- Nathan MacKinnon: 1+ goals NO @ 56c · p 0.6201 (adj 0.6026) · $9.07 · thesis COL:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 20c · p 0.2312 (adj 0.2221) · $3.37 · thesis SJS:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 20c · p 0.2461 (adj 0.2308) · $6.01 · thesis UTA:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1506 (adj 0.1417) · $3.9 · thesis PIT:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 13c · p 0.1639 (adj 0.1517) · $3.78 · thesis UTA:OFFENSE_4PLUS
- Mikhail Sergachev: 1+ goals NO @ 85c · p 0.8795 (adj 0.8696) · $20.0 · thesis UTA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 160/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROBABLE) exp shots 28.93, exp saves 25.11 (sd 6.78), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.95, exp saves 21.4 (sd 6.11), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Killorn: 1+ points | 0.487 | 0.365 | 37/64 | +0.101 | STANDARD |
| Alex Killorn: 1+ assists | 0.340 | 0.235 | 25/78 | +0.077 | STANDARD |
| A.J. Greer: 1+ goals | 0.228 | 0.135 | 14/87 | +0.080 | STANDARD |
| Jackson LaCombe: 2+ assists | 0.170 | 0.080 | 14/98 | +0.021 | STANDARD |
| Jackson LaCombe: 1+ points | 0.599 | 0.510 | 52/50 | +0.061 | STANDARD |
| Beckett Sennecke: 2+ points | 0.244 | 0.155 | 20/89 | +0.033 | STANDARD |

**COL @ PHI** · priced 141/153 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 30.72, exp saves 26.47 (sd 7.09), pull risk 0.061
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.25, exp saves 21.15 (sd 5.86), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.417 | 0.605 | 61/40 | +0.166 | STANDARD |
| Cale Makar: 2+ points | 0.156 | 0.335 | 35/68 | +0.148 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.298 | 0.475 | 49/54 | +0.145 | STANDARD |
| Cale Makar: 1+ points | 0.512 | 0.680 | 70/34 | +0.132 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.453 | 0.605 | 61/40 | +0.130 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.097 | 0.245 | 25/76 | +0.130 | STANDARD |

**SJS @ TOR** · priced 169/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.27, exp saves 25.35 (sd 6.93), pull risk 0.065
- SJS net: Yaroslav Askarov (PROBABLE) exp shots 27.18, exp saves 23.38 (sd 6.5), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colton Sissons: 1+ assists | 0.245 | 0.125 | 23/98 | +0.003 | STANDARD |
| Macklin Celebrini: 2+ points | 0.290 | 0.400 | 42/62 | +0.073 | STANDARD |
| Colton Sissons: 1+ points | 0.360 | 0.260 | 33/81 | +0.014 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.439 | 0.535 | 55/48 | +0.064 | STANDARD |
| Ivar Stenberg: 1+ points | 0.360 | 0.455 | 47/56 | +0.063 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.220 | 0.300 | 32/72 | +0.046 | PRIOR_HEAVY |

**PIT @ UTA** · priced 188/191 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.47, exp saves 22.91 (sd 6.41), pull risk 0.063
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.66, exp saves 23.55 (sd 6.73), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| John Marino: 1+ assists | 0.375 | 0.165 | 30/97 | +0.060 | STANDARD |
| John Marino: 1+ points | 0.415 | 0.240 | 38/90 | +0.019 | STANDARD |
| Nate Schmidt: 1+ points | 0.307 | 0.140 | 25/97 | +0.044 | STANDARD |
| Nate Schmidt: 1+ assists | 0.259 | 0.105 | 20/99 | +0.047 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.230 | 0.335 | 35/68 | +0.075 | STANDARD |
| Nick Robertson: 1+ assists | 0.191 | 0.100 | 19/99 | -0.010 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
