# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T11:24:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 2746 · contracts joined: 522 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 422, 'NO_EDGE': 56, 'OK': 44}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 52, 'game_early_goal': 4, 'first_goal': 72, 'game_winner': 8, 'player_goals': 122, 'game_overtime': 4, 'player_points': 72, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-6h | 0.577 | 0.423 | 0.174 | 6.19 | 3.33 | 2.85 | 218 (25/193) | PROJECTED/PROJECTED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-6h | 0.400 | 0.600 | 0.175 | 5.79 | 2.59 | 3.20 | 202 (25/177) | PROJECTED/PROJECTED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-12h | 0.500 | 0.500 | 0.173 | 6.57 | 3.28 | 3.28 | 51 (25/26) | PROJECTED/PROJECTED |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-12h | 0.623 | 0.377 | 0.162 | 6.71 | 3.76 | 2.95 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.409 | 0.525 | 0.502 | 53 | 48 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.222 | 0.325 | 0.302 | 33 | 68 | no | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.634 | 0.725 | 0.708 | 73 | 28 | no | +0.071 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.364 | 0.455 | 0.436 | 46 | 55 | no | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.219 | 0.310 | 0.290 | 32 | 70 | no | +0.066 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.717 | 0.795 | 0.781 | 80 | 21 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.493 | 0.575 | 0.559 | 58 | 43 | no | +0.060 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.400 | 0.325 | 0.339 | 33 | 68 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.829 | 0.890 | 0.879 | 90 | 12 | no | +0.044 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.600 | 0.665 | 0.652 | 67 | 34 | no | +0.044 | OK |
| KXNHLGAME-26OCT19SJTOR-SJ | game_winner | 0.500 | 0.435 | 0.448 | 44 | 57 | yes | +0.043 | OK |
| KXNHLGAME-26OCT19SJTOR-TOR | game_winner | 0.500 | 0.565 | 0.552 | 57 | 44 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.380 | 0.450 | 0.436 | 46 | 56 | no | +0.042 | OK |
| KXNHLSPREAD-26OCT19SJTOR-TOR3 | game_spread | 0.180 | 0.235 | 0.223 | 24 | 77 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4 | team_total | 0.425 | 0.495 | 0.481 | 51 | 52 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.815 | 0.865 | 0.856 | 87 | 14 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.097 | 0.145 | 0.134 | 15 | 86 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.203 | 0.260 | 0.248 | 27 | 75 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.136 | 0.185 | 0.174 | 19 | 82 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT19SJTOR-TOR2 | game_spread | 0.293 | 0.345 | 0.334 | 35 | 66 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR3 | team_total | 0.641 | 0.695 | 0.685 | 71 | 32 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR5 | team_total | 0.243 | 0.295 | 0.284 | 31 | 72 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR6 | team_total | 0.112 | 0.145 | 0.138 | 15 | 86 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.812 | 0.845 | 0.839 | 85 | 16 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR2 | team_total | 0.833 | 0.865 | 0.859 | 87 | 14 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT19SJTOR-SJ2 | game_spread | 0.292 | 0.255 | 0.262 | 26 | 75 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.124 | 0.155 | 0.148 | 16 | 85 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.196 | 0.160 | 0.167 | 17 | 85 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.060 | 0.090 | 0.083 | 10 | 92 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT19SJTOR-7 | game_total | 0.508 | 0.545 | 0.538 | 55 | 46 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT19SJTOR-4 | game_total | 0.882 | 0.905 | 0.901 | 91 | 10 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.118 | 0.095 | 0.099 | 10 | 91 | yes | +0.011 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.947 | 0.970 | 0.966 | 98 | 4 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT19SJTOR-SJ3 | game_spread | 0.180 | 0.155 | 0.160 | 16 | 85 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.769 | 0.795 | 0.790 | 80 | 21 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT19SJTOR-6 | game_total | 0.615 | 0.650 | 0.643 | 66 | 36 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.771 | 0.800 | 0.794 | 81 | 21 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT19ANANYR-7 | game_total | 0.449 | 0.475 | 0.470 | 48 | 53 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.046 | 0.035 | 0.037 | 4 | 97 | yes | +0.004 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.224 | 0.245 | 0.241 | 25 | 76 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.110 | 0.125 | 0.122 | 13 | 88 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.331 | 0.360 | 0.354 | 37 | 65 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.977 | 0.985 | 0.984 | 99 | 2 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.242 | 0.220 | 0.224 | 23 | 79 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.276 | 0.295 | 0.291 | 30 | 71 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.228 | 0.245 | 0.241 | 25 | 76 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-6 | game_total | 0.564 | 0.585 | 0.581 | 59 | 42 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI5 | team_total | 0.125 | 0.135 | 0.133 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.164 | 0.175 | 0.173 | 18 | 83 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT19ANANYR-NYR2 | game_spread | 0.352 | 0.335 | 0.338 | 34 | 67 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.176 | 0.165 | 0.167 | 17 | 84 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.962 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.826 | 0.840 | 0.837 | 85 | 17 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.101 | 0.095 | 0.096 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.069 | 0.065 | 0.066 | 7 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.550 | 0.575 | 0.570 | 59 | 44 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.312 | 0.330 | 0.326 | 34 | 68 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-10 | game_total | 0.082 | 0.090 | 0.088 | 10 | 92 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ4 | team_total | 0.429 | 0.405 | 0.410 | 42 | 61 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.889 | 0.885 | 0.886 | 89 | 12 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ3 | team_total | 0.638 | 0.620 | 0.624 | 63 | 39 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.377 | 0.365 | 0.367 | 37 | 64 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-9 | game_total | 0.179 | 0.190 | 0.188 | 20 | 82 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.256 | 0.265 | 0.263 | 27 | 74 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.118 | 0.115 | 0.116 | 12 | 89 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-NYR | game_winner | 0.577 | 0.565 | 0.567 | 57 | 44 |  | -0.010 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-ANA | game_winner | 0.423 | 0.435 | 0.433 | 44 | 57 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.840 | 0.845 | 0.844 | 85 | 16 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.779 | 0.790 | 0.788 | 80 | 22 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19ANANYR-NYR3 | game_spread | 0.220 | 0.225 | 0.224 | 23 | 78 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA2 | game_spread | 0.406 | 0.415 | 0.413 | 42 | 59 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI4 | team_total | 0.269 | 0.280 | 0.278 | 29 | 73 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.116 | 0.120 | 0.119 | 13 | 89 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.577 | 0.532 | 0.174 | 0.214 | 6.19 | 6.49 | 0.992/1.024 | KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 +0.066 |
| COL @ PHI | 0.400 | 0.445 | 0.175 | 0.223 | 5.79 | 5.97 | 0.993/0.976 | KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3 +0.061 |
| SJS @ TOR | 0.500 | 0.538 | 0.173 | 0.213 | 6.57 | 6.36 | 0.965/1.027 | KXNHLTEAMTOTAL-26OCT19SJTOR-SJ4 -0.049 |
| PIT @ UTA | 0.623 | 0.583 | 0.162 | 0.209 | 6.71 | 6.67 | 0.993/1.033 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.042 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 9 recommended · full analysis in card.md / packet.json `thesis_card`

- Tim Washe: 1+ goals YES @ 10c · p 0.1311 (adj 0.1221) · $4.02 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1251 (adj 0.1088) · $3.05 · thesis ANA:OFFENSE_4PLUS
- Alexis Lafreniere: 2+ assists YES @ 7c · p 0.1005 (adj 0.0853) · $2.43 · thesis NYR:OFFENSE_4PLUS
- Jackson LaCombe: 1+ assists YES @ 45c · p 0.5301 (adj 0.485) · $6.78 · thesis ANA:OFFENSE_4PLUS
- Travis Sanheim: 1+ goals YES @ 9c · p 0.1398 (adj 0.1199) · $5.5 · thesis PHI:OFFENSE_4PLUS
- Colorado over 4.5 goals scored NO @ 70c · p 0.7896 (adj 0.7398) · $10.91 · thesis COL:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 68c · p 0.7976 (adj 0.7179) · $7.01 · thesis GAME:TIGHT
- Colorado over 5.5 goals scored NO @ 86c · p 0.9114 (adj 0.8832) · $12.08 · thesis PHI:WINS
- Full Game: Over 6.5 goals scored NO @ 46c · p 0.5202 (adj 0.4876) · $4.88 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 158/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 28.93, exp saves 25.11 (sd 6.75), pull risk 0.059
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.95, exp saves 21.36 (sd 6.08), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cutter Gauthier: 1+ goals | 0.356 | 0.195 | 36/97 | -0.021 | STANDARD |
| Beckett Sennecke: 1+ goals | 0.340 | 0.180 | 33/97 | -0.006 | STANDARD |
| A.J. Greer: 1+ goals | 0.231 | 0.085 | 14/97 | +0.082 | STANDARD |
| Alexis Lafreniere: 1+ goals | 0.337 | 0.195 | 36/97 | -0.039 | STANDARD |
| Leo Carlsson: 1+ goals | 0.325 | 0.190 | 30/92 | +0.010 | STANDARD |
| J.T. Miller: 1+ goals | 0.269 | 0.155 | 28/97 | -0.025 | STANDARD |

**COL @ PHI** · priced 139/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 30.72, exp saves 26.49 (sd 7.06), pull risk 0.06
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.25, exp saves 21.17 (sd 5.81), pull risk 0.045

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.412 | 0.600 | 61/41 | +0.161 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.298 | 0.475 | 49/54 | +0.145 | STANDARD |
| Cale Makar: 2+ points | 0.161 | 0.335 | 35/68 | +0.143 | STANDARD |
| Trevor Zegras: 1+ goals | 0.294 | 0.145 | 26/97 | +0.020 | STANDARD |
| Cale Makar: 1+ points | 0.508 | 0.655 | 70/39 | +0.086 | STANDARD |
| Matvei Michkov: 1+ goals | 0.294 | 0.155 | 28/97 | -0.000 | STANDARD |

**SJS @ TOR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 29.27, exp saves 25.43 (sd 6.86), pull risk 0.06
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.18, exp saves 23.34 (sd 6.49), pull risk 0.07

**PIT @ UTA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.47, exp saves 22.96 (sd 6.37), pull risk 0.058
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.66, exp saves 23.55 (sd 6.69), pull risk 0.08

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
