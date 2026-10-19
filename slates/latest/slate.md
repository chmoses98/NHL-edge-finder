# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T15:12:45Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3103 · contracts joined: 879 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 779, 'NO_EDGE': 62, 'OK': 38}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 118, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 252, 'game_overtime': 4, 'player_points': 159, 'game_spread': 16, 'team_total': 40, 'game_total': 36, 'goalie_saves': 1}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-6h | 0.581 | 0.419 | 0.176 | 6.13 | 3.32 | 2.81 | 218 (25/193) | PROBABLE/PROJECTED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-6h | 0.373 | 0.627 | 0.171 | 5.95 | 2.57 | 3.38 | 203 (25/178) | CONFIRMED/PROJECTED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-6h | 0.540 | 0.460 | 0.169 | 6.82 | 3.54 | 3.28 | 222 (25/197) | PROBABLE/PROJECTED |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-6h | 0.619 | 0.381 | 0.165 | 6.69 | 3.75 | 2.94 | 236 (25/211) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.255 | 0.335 | 0.318 | 34 | 67 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.449 | 0.535 | 0.518 | 55 | 48 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.398 | 0.465 | 0.451 | 47 | 54 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.252 | 0.325 | 0.309 | 34 | 69 | no | +0.043 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.627 | 0.685 | 0.674 | 69 | 32 | no | +0.037 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.373 | 0.315 | 0.326 | 32 | 69 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.742 | 0.795 | 0.785 | 80 | 21 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.672 | 0.730 | 0.719 | 74 | 28 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.524 | 0.575 | 0.565 | 58 | 43 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.833 | 0.875 | 0.867 | 88 | 13 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.763 | 0.805 | 0.797 | 81 | 20 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.407 | 0.455 | 0.445 | 46 | 55 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.118 | 0.155 | 0.147 | 16 | 85 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.225 | 0.265 | 0.257 | 27 | 74 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.851 | 0.890 | 0.883 | 90 | 12 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.120 | 0.155 | 0.147 | 16 | 85 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT19ANANYR-7 | game_total | 0.435 | 0.475 | 0.467 | 48 | 53 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.536 | 0.580 | 0.571 | 59 | 43 | no | +0.017 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.153 | 0.185 | 0.178 | 19 | 82 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.763 | 0.800 | 0.793 | 81 | 21 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.321 | 0.360 | 0.352 | 37 | 65 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.849 | 0.875 | 0.870 | 88 | 13 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.119 | 0.095 | 0.099 | 10 | 91 | yes | +0.012 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.180 | 0.155 | 0.160 | 16 | 85 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.218 | 0.245 | 0.240 | 25 | 76 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT19SJTOR-TOR3 | game_spread | 0.210 | 0.235 | 0.230 | 24 | 77 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.134 | 0.115 | 0.119 | 12 | 89 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.834 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.826 | 0.845 | 0.841 | 85 | 16 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.078 | 0.065 | 0.067 | 7 | 94 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.954 | 0.970 | 0.967 | 98 | 4 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.046 | 0.035 | 0.037 | 4 | 97 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT19ANANYR-6 | game_total | 0.550 | 0.580 | 0.574 | 59 | 43 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.110 | 0.125 | 0.122 | 13 | 88 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.158 | 0.180 | 0.175 | 19 | 83 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.067 | 0.080 | 0.077 | 9 | 93 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.093 | 0.080 | 0.083 | 9 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.250 | 0.270 | 0.266 | 28 | 74 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-7 | game_total | 0.526 | 0.545 | 0.541 | 55 | 46 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.352 | 0.330 | 0.334 | 34 | 68 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.259 | 0.240 | 0.244 | 25 | 77 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-10 | game_total | 0.080 | 0.090 | 0.088 | 10 | 92 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.381 | 0.365 | 0.368 | 37 | 64 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-ANA | game_winner | 0.419 | 0.435 | 0.432 | 44 | 57 |  | -0.006 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-NYR | game_winner | 0.581 | 0.565 | 0.568 | 57 | 44 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-9 | game_total | 0.176 | 0.190 | 0.187 | 20 | 82 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.983 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26OCT19SJTOR-SJ | game_winner | 0.460 | 0.445 | 0.448 | 45 | 56 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT19SJTOR-TOR | game_winner | 0.540 | 0.555 | 0.552 | 56 | 45 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ2 | team_total | 0.828 | 0.835 | 0.834 | 84 | 17 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-4 | game_total | 0.902 | 0.910 | 0.908 | 92 | 10 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT19ANANYR-NYR2 | game_spread | 0.356 | 0.340 | 0.343 | 35 | 67 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.778 | 0.790 | 0.788 | 80 | 22 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.276 | 0.285 | 0.283 | 29 | 72 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.893 | 0.900 | 0.899 | 91 | 11 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR2 | team_total | 0.862 | 0.870 | 0.868 | 88 | 14 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.115 | 0.115 | 0.115 | 12 | 89 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ2 | game_spread | 0.262 | 0.255 | 0.256 | 26 | 75 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.842 | 0.850 | 0.848 | 86 | 16 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-7 | game_total | 0.544 | 0.555 | 0.553 | 56 | 45 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA5 | team_total | 0.326 | 0.340 | 0.337 | 35 | 67 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.240 | 0.225 | 0.228 | 24 | 79 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-6 | game_total | 0.636 | 0.645 | 0.643 | 65 | 36 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.173 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI5 | team_total | 0.125 | 0.120 | 0.121 | 13 | 89 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.124 | 0.120 | 0.121 | 13 | 89 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA3 | team_total | 0.730 | 0.740 | 0.738 | 75 | 27 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.887 | 0.890 | 0.889 | 90 | 12 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT19ANANYR-NYR3 | game_spread | 0.222 | 0.230 | 0.228 | 24 | 78 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR4 | team_total | 0.437 | 0.450 | 0.447 | 46 | 56 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA4 | team_total | 0.527 | 0.535 | 0.533 | 54 | 47 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI2 | team_total | 0.719 | 0.715 | 0.716 | 72 | 29 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT2 | game_spread | 0.196 | 0.195 | 0.195 | 20 | 81 |  | -0.015 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.581 | 0.535 | 0.176 | 0.213 | 6.13 | 6.47 | 0.990/1.024 | KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 +0.076 |
| COL @ PHI | 0.373 | 0.445 | 0.171 | 0.220 | 5.95 | 5.95 | 0.990/0.976 | KXNHLSPREAD-26OCT19COLPHI-COL2 -0.077 |
| SJS @ TOR | 0.540 | 0.527 | 0.169 | 0.218 | 6.82 | 6.41 | 0.984/1.034 | KXNHLTOTAL-26OCT19SJTOR-8 -0.068 |
| PIT @ UTA | 0.619 | 0.582 | 0.165 | 0.213 | 6.69 | 6.66 | 0.993/1.033 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.050 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 16 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.2281 (adj 0.2048) · $14.62 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1341 (adj 0.1243) · $4.58 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.121 (adj 0.1108) · $3.62 · thesis ANA:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 9c · p 0.1193 (adj 0.1095) · $3.53 · thesis NYR:OFFENSE_4PLUS
- T.J. Hughes: 1+ goals NO @ 79c · p 0.8518 (adj 0.8351) · $15.58 · thesis COL:SUPPRESSED
- Nathan MacKinnon: 1+ goals NO @ 54c · p 0.6201 (adj 0.5976) · $14.42 · thesis COL:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7977 (adj 0.7114) · $11.72 · thesis PHI:WINS
- Colorado wins by over 1.5 goals NO @ 54c · p 0.6778 (adj 0.585) · $4.99 · thesis PHI:WINS
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1444 (adj 0.1358) · $5.33 · thesis TOR:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 78c · p 0.8249 (adj 0.8124) · $20.0 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ goals YES @ 20c · p 0.239 (adj 0.228) · $5.68 · thesis SJS:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 35c · p 0.4069 (adj 0.376) · $5.4 · thesis GAME:LOW_EVENT
- Lawson Crouse: 1+ goals YES @ 20c · p 0.2461 (adj 0.2308) · $5.93 · thesis UTA:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1506 (adj 0.1417) · $3.87 · thesis PIT:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 13c · p 0.1639 (adj 0.1517) · $3.82 · thesis UTA:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6552) · $12.86 · thesis UTA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 158/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROBABLE) exp shots 28.93, exp saves 25.11 (sd 6.78), pull risk 0.061
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.95, exp saves 21.4 (sd 6.11), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Beckett Sennecke: 2+ points | 0.244 | 0.145 | 21/92 | +0.022 | STANDARD |
| Jackson LaCombe: 2+ points | 0.229 | 0.130 | 20/94 | +0.017 | STANDARD |
| Alex Killorn: 1+ points | 0.487 | 0.390 | 40/62 | +0.071 | STANDARD |
| A.J. Greer: 1+ goals | 0.228 | 0.135 | 14/87 | +0.080 | STANDARD |
| Alex Killorn: 1+ assists | 0.340 | 0.250 | 26/76 | +0.066 | STANDARD |
| Jackson LaCombe: 1+ points | 0.599 | 0.515 | 53/50 | +0.051 | STANDARD |

**COL @ PHI** · priced 140/152 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 30.72, exp saves 26.47 (sd 7.09), pull risk 0.061
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.25, exp saves 21.15 (sd 5.86), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 2+ points | 0.156 | 0.345 | 36/67 | +0.158 | STANDARD |
| Cale Makar: 1+ assists | 0.417 | 0.595 | 60/41 | +0.156 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.298 | 0.475 | 49/54 | +0.145 | STANDARD |
| Cale Makar: 1+ points | 0.512 | 0.675 | 69/34 | +0.132 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.453 | 0.605 | 61/40 | +0.130 | STANDARD |
| Nathan MacKinnon: 3+ points | 0.097 | 0.225 | 25/80 | +0.092 | STANDARD |

**SJS @ TOR** · priced 161/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 29.27, exp saves 25.39 (sd 6.9), pull risk 0.06
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.18, exp saves 23.4 (sd 6.48), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.355 | 0.460 | 48/56 | +0.068 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.286 | 0.385 | 40/63 | +0.067 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.435 | 0.525 | 53/48 | +0.068 | STANDARD |
| Mason Marchment: 1+ assists | 0.226 | 0.305 | 32/71 | +0.050 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.217 | 0.295 | 31/72 | +0.049 | PRIOR_HEAVY |
| Macklin Celebrini: 3+ points | 0.098 | 0.165 | 18/85 | +0.043 | STANDARD |

**PIT @ UTA** · priced 182/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.47, exp saves 22.91 (sd 6.41), pull risk 0.063
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.66, exp saves 23.55 (sd 6.73), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.230 | 0.335 | 35/68 | +0.075 | STANDARD |
| Vincent Trocheck: 1+ points | 0.390 | 0.480 | 49/53 | +0.062 | STANDARD |
| Nick Robertson: 1+ assists | 0.191 | 0.105 | 19/98 | -0.010 | STANDARD |
| Clayton Keller: 2+ points | 0.250 | 0.330 | 35/69 | +0.045 | STANDARD |
| Clayton Keller: 2+ assists | 0.126 | 0.205 | 21/80 | +0.063 | STANDARD |
| Rickard Rakell: 1+ assists | 0.380 | 0.305 | 32/71 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
