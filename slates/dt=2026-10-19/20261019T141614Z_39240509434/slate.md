# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T14:16:14Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3102 · contracts joined: 878 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 778, 'OK': 46, 'NO_EDGE': 54}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 118, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 252, 'game_overtime': 4, 'player_points': 159, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-6h | 0.602 | 0.398 | 0.172 | 6.35 | 3.50 | 2.85 | 218 (25/193) | PROJECTED/PROJECTED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-6h | 0.392 | 0.608 | 0.180 | 5.92 | 2.63 | 3.29 | 202 (25/177) | PROJECTED/PROJECTED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-6h | 0.558 | 0.442 | 0.163 | 6.87 | 3.62 | 3.25 | 222 (25/197) | PROJECTED/PROJECTED |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-6h | 0.610 | 0.391 | 0.163 | 6.86 | 3.80 | 3.07 | 236 (25/211) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.239 | 0.335 | 0.314 | 34 | 67 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.431 | 0.525 | 0.506 | 53 | 48 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.376 | 0.465 | 0.447 | 47 | 54 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.237 | 0.320 | 0.302 | 33 | 69 | no | +0.058 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.608 | 0.685 | 0.670 | 69 | 32 | no | +0.057 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.392 | 0.315 | 0.330 | 32 | 69 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.654 | 0.730 | 0.716 | 74 | 28 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.737 | 0.795 | 0.784 | 80 | 21 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.107 | 0.155 | 0.144 | 16 | 85 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.840 | 0.890 | 0.881 | 90 | 12 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.832 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.513 | 0.570 | 0.559 | 58 | 44 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.113 | 0.155 | 0.146 | 16 | 85 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.405 | 0.455 | 0.445 | 46 | 55 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.220 | 0.265 | 0.256 | 27 | 74 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.193 | 0.155 | 0.162 | 16 | 85 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.149 | 0.185 | 0.177 | 19 | 82 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.207 | 0.245 | 0.237 | 25 | 76 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.092 | 0.065 | 0.070 | 7 | 94 | yes | +0.017 | OK |
| KXNHLGAME-26OCT19ANANYR-ANA | game_winner | 0.398 | 0.435 | 0.428 | 44 | 57 | no | +0.015 | OK |
| KXNHLGAME-26OCT19ANANYR-NYR | game_winner | 0.602 | 0.565 | 0.572 | 57 | 44 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT19ANANYR-NYR2 | game_spread | 0.379 | 0.345 | 0.352 | 35 | 66 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR3 | team_total | 0.688 | 0.655 | 0.662 | 66 | 35 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.140 | 0.115 | 0.120 | 12 | 89 | yes | +0.013 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.107 | 0.080 | 0.085 | 9 | 93 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.138 | 0.115 | 0.119 | 12 | 89 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.117 | 0.095 | 0.099 | 10 | 91 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.768 | 0.800 | 0.794 | 81 | 21 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.065 | 0.085 | 0.081 | 9 | 92 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR4 | team_total | 0.476 | 0.445 | 0.451 | 45 | 56 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.544 | 0.580 | 0.573 | 59 | 43 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.051 | 0.035 | 0.038 | 4 | 97 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.328 | 0.360 | 0.353 | 37 | 65 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.269 | 0.240 | 0.246 | 25 | 77 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.143 | 0.125 | 0.129 | 13 | 88 | yes | +0.005 | OK |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.391 | 0.365 | 0.370 | 37 | 64 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT5 | team_total | 0.205 | 0.180 | 0.185 | 19 | 83 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.838 | 0.855 | 0.852 | 86 | 15 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT19ANANYR-NYR3 | game_spread | 0.245 | 0.225 | 0.229 | 23 | 78 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR5 | team_total | 0.276 | 0.250 | 0.255 | 26 | 76 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.357 | 0.335 | 0.339 | 34 | 67 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.788 | 0.805 | 0.802 | 81 | 20 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.957 | 0.970 | 0.968 | 98 | 4 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.968 | 0.975 | 0.974 | 98 | 3 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT19PITUTA-9 | game_total | 0.262 | 0.245 | 0.248 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR6 | team_total | 0.158 | 0.140 | 0.143 | 15 | 87 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3 | team_total | 0.496 | 0.475 | 0.479 | 48 | 53 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT2 | game_spread | 0.209 | 0.195 | 0.198 | 20 | 81 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.268 | 0.285 | 0.282 | 29 | 72 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-8 | game_total | 0.353 | 0.330 | 0.335 | 34 | 68 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI4 | team_total | 0.280 | 0.260 | 0.264 | 27 | 75 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA2 | game_spread | 0.397 | 0.415 | 0.411 | 42 | 59 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI2 | team_total | 0.730 | 0.715 | 0.718 | 72 | 29 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-6 | game_total | 0.662 | 0.645 | 0.648 | 65 | 36 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.867 | 0.875 | 0.873 | 88 | 13 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.986 | 0.980 | 0.981 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.863 | 0.850 | 0.853 | 86 | 16 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-4 | game_total | 0.899 | 0.905 | 0.904 | 91 | 10 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-UTA | game_winner | 0.610 | 0.625 | 0.622 | 63 | 38 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.119 | 0.125 | 0.124 | 13 | 88 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT3 | team_total | 0.590 | 0.570 | 0.574 | 58 | 44 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI5 | team_total | 0.130 | 0.120 | 0.122 | 13 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-7 | game_total | 0.550 | 0.535 | 0.538 | 54 | 47 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.168 | 0.185 | 0.182 | 20 | 83 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-TOR3 | game_spread | 0.226 | 0.235 | 0.233 | 24 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT4 | team_total | 0.378 | 0.360 | 0.364 | 37 | 65 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.181 | 0.170 | 0.172 | 18 | 84 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.906 | 0.900 | 0.901 | 91 | 11 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.841 | 0.845 | 0.844 | 85 | 16 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-6 | game_total | 0.664 | 0.655 | 0.657 | 66 | 35 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.283 | 0.270 | 0.272 | 28 | 74 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ3 | game_spread | 0.153 | 0.160 | 0.159 | 17 | 85 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.799 | 0.790 | 0.792 | 80 | 22 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.069 | 0.070 | 0.070 | 8 | 94 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.240 | 0.230 | 0.232 | 24 | 78 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.602 | 0.532 | 0.172 | 0.218 | 6.35 | 6.47 | 0.992/1.024 | KXNHLGAME-26OCT19ANANYR-ANA +0.070 |
| COL @ PHI | 0.392 | 0.445 | 0.180 | 0.221 | 5.92 | 5.96 | 0.993/0.976 | KXNHLSPREAD-26OCT19COLPHI-COL2 -0.055 |
| SJS @ TOR | 0.558 | 0.540 | 0.163 | 0.220 | 6.87 | 6.37 | 0.965/1.034 | KXNHLTOTAL-26OCT19SJTOR-6 -0.078 |
| PIT @ UTA | 0.610 | 0.582 | 0.163 | 0.213 | 6.86 | 6.66 | 0.993/1.033 | KXNHLTEAMTOTAL-26OCT19PITUTA-UTA5 -0.045 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.229 (adj 0.2043) · $14.35 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1217 (adj 0.1113) · $3.98 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1308 (adj 0.1218) · $3.62 · thesis ANA:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 9c · p 0.1168 (adj 0.1076) · $3.18 · thesis NYR:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 54c · p 0.6243 (adj 0.602) · $20.0 · thesis COL:SUPPRESSED
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6767 (adj 0.5846) · $4.27 · thesis GAME:TIGHT
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7923 (adj 0.7096) · $8.58 · thesis GAME:TIGHT
- Colorado over 5.5 goals scored NO @ 85c · p 0.9049 (adj 0.875) · $14.35 · thesis PHI:WINS
- Ivar Stenberg: 1+ goals NO @ 78c · p 0.8293 (adj 0.8157) · $20.0 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 19c · p 0.2336 (adj 0.2215) · $6.83 · thesis SJS:OFFENSE_4PLUS
- Full Game: Over 6.5 goals scored NO @ 45c · p 0.5203 (adj 0.4826) · $5.7 · thesis SJS:SUPPRESSED
- Full Game: Over 5.5 goals scored NO @ 35c · p 0.4148 (adj 0.3799) · $2.26 · thesis GAME:LOW_EVENT
- Jack McBain: 1+ goals YES @ 12c · p 0.1639 (adj 0.1504) · $6.12 · thesis UTA:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1506 (adj 0.1405) · $3.53 · thesis PIT:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.654) · $12.2 · thesis UTA:SUPPRESSED
- Andrei Kuzmenko: 1+ goals YES @ 13c · p 0.1576 (adj 0.1482) · $2.91 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 158/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 28.93, exp saves 25.07 (sd 6.74), pull risk 0.064
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.95, exp saves 21.37 (sd 6.13), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.229 | 0.130 | 14/88 | +0.081 | STANDARD |
| Alex Killorn: 1+ points | 0.482 | 0.390 | 40/62 | +0.065 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.517 | 0.430 | 44/58 | +0.060 | STANDARD |
| Alex Killorn: 1+ assists | 0.334 | 0.250 | 26/76 | +0.060 | STANDARD |
| Jackson LaCombe: 1+ points | 0.593 | 0.510 | 53/51 | +0.045 | STANDARD |
| Pavel Dorofeyev: 1+ points | 0.478 | 0.555 | 57/46 | +0.045 | STANDARD |

**COL @ PHI** · priced 139/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 30.72, exp saves 26.46 (sd 7.05), pull risk 0.062
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.25, exp saves 21.15 (sd 5.91), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.159 | 0.345 | 36/67 | +0.156 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.304 | 0.485 | 50/53 | +0.149 | STANDARD |
| Cale Makar: 1+ assists | 0.411 | 0.590 | 60/42 | +0.152 | STANDARD |
| Cale Makar: 1+ points | 0.508 | 0.655 | 70/39 | +0.085 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.459 | 0.590 | 61/43 | +0.093 | STANDARD |
| Nathan MacKinnon: 1+ points | 0.659 | 0.785 | 80/23 | +0.098 | STANDARD |

**SJS @ TOR** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 29.27, exp saves 25.43 (sd 6.88), pull risk 0.059
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.18, exp saves 23.38 (sd 6.44), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.341 | 0.455 | 47/56 | +0.082 | PRIOR_HEAVY |
| Macklin Celebrini: 1+ assists | 0.431 | 0.525 | 53/48 | +0.072 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.207 | 0.300 | 32/72 | +0.059 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.282 | 0.375 | 39/64 | +0.061 | STANDARD |
| Tyler Toffoli: 1+ assists | 0.314 | 0.230 | 25/79 | +0.050 | STANDARD |
| Mason Marchment: 1+ assists | 0.223 | 0.305 | 32/71 | +0.052 | STANDARD |

**PIT @ UTA** · priced 182/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.47, exp saves 22.91 (sd 6.41), pull risk 0.063
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.66, exp saves 23.55 (sd 6.73), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.230 | 0.340 | 36/68 | +0.075 | STANDARD |
| Clayton Keller: 1+ assists | 0.464 | 0.565 | 57/44 | +0.079 | STANDARD |
| Clayton Keller: 2+ points | 0.250 | 0.340 | 36/68 | +0.055 | STANDARD |
| Vincent Trocheck: 1+ points | 0.390 | 0.475 | 49/54 | +0.052 | STANDARD |
| Nick Robertson: 1+ assists | 0.191 | 0.110 | 21/99 | -0.030 | STANDARD |
| Clayton Keller: 2+ assists | 0.126 | 0.205 | 21/80 | +0.063 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
