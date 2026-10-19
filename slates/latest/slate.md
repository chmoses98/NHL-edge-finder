# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T17:51:47Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3165 · contracts joined: 941 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 841, 'NO_EDGE': 50, 'OK': 50}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 139, 'game_early_goal': 4, 'first_goal': 147, 'game_winner': 8, 'player_goals': 254, 'game_overtime': 4, 'player_points': 191, 'goalie_saves': 6, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-3h | 0.585 | 0.415 | 0.175 | 6.16 | 3.35 | 2.82 | 220 (25/195) | PROBABLE/CONFIRMED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-3h | 0.368 | 0.632 | 0.176 | 5.93 | 2.56 | 3.38 | 235 (25/210) | CONFIRMED/CONFIRMED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-3h | 0.547 | 0.453 | 0.166 | 6.94 | 3.63 | 3.30 | 234 (25/209) | CONFIRMED/CONFIRMED |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-6h | 0.613 | 0.387 | 0.160 | 6.75 | 3.75 | 3.00 | 252 (25/227) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.451 | 0.535 | 0.518 | 54 | 47 | no | +0.062 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.257 | 0.335 | 0.318 | 34 | 67 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.252 | 0.325 | 0.310 | 33 | 68 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.402 | 0.465 | 0.452 | 47 | 54 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.671 | 0.730 | 0.719 | 74 | 28 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.766 | 0.820 | 0.810 | 83 | 19 | no | +0.033 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.368 | 0.315 | 0.325 | 32 | 69 | yes | +0.033 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.632 | 0.685 | 0.675 | 69 | 32 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT19ANANYR-7 | game_total | 0.440 | 0.495 | 0.484 | 50 | 51 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.832 | 0.875 | 0.867 | 88 | 13 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.738 | 0.785 | 0.776 | 79 | 22 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT19ANANYR-6 | game_total | 0.554 | 0.605 | 0.595 | 61 | 40 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.539 | 0.585 | 0.576 | 59 | 42 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.851 | 0.890 | 0.883 | 90 | 12 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.323 | 0.370 | 0.360 | 38 | 64 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.853 | 0.885 | 0.879 | 89 | 12 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR5 | team_total | 0.248 | 0.285 | 0.277 | 29 | 72 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.518 | 0.555 | 0.548 | 56 | 45 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.117 | 0.150 | 0.143 | 16 | 86 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.120 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.765 | 0.800 | 0.793 | 81 | 21 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.369 | 0.330 | 0.338 | 34 | 68 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.277 | 0.240 | 0.247 | 25 | 77 | yes | +0.014 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.120 | 0.145 | 0.140 | 15 | 86 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.254 | 0.285 | 0.279 | 29 | 72 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT19ANANYR-9 | game_total | 0.179 | 0.205 | 0.199 | 21 | 80 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.148 | 0.120 | 0.125 | 13 | 89 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.218 | 0.245 | 0.239 | 25 | 76 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.151 | 0.175 | 0.170 | 18 | 83 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.178 | 0.155 | 0.159 | 16 | 85 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.404 | 0.435 | 0.429 | 44 | 57 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR4 | team_total | 0.444 | 0.475 | 0.469 | 48 | 53 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.886 | 0.905 | 0.901 | 91 | 10 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.961 | 0.975 | 0.973 | 98 | 3 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.092 | 0.075 | 0.078 | 8 | 93 | yes | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.118 | 0.135 | 0.131 | 14 | 87 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR3 | team_total | 0.661 | 0.690 | 0.684 | 70 | 32 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.224 | 0.250 | 0.245 | 26 | 76 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.045 | 0.035 | 0.037 | 4 | 97 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT5 | team_total | 0.193 | 0.175 | 0.178 | 18 | 83 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.955 | 0.975 | 0.972 | 99 | 4 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR6 | team_total | 0.161 | 0.140 | 0.144 | 15 | 87 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT19ANANYR-NYR3 | game_spread | 0.226 | 0.245 | 0.241 | 25 | 76 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.128 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.387 | 0.365 | 0.369 | 37 | 64 | yes | +0.001 | OK |
| KXNHLGAME-26OCT19PITUTA-UTA | game_winner | 0.613 | 0.635 | 0.631 | 64 | 37 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.160 | 0.175 | 0.172 | 18 | 83 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.830 | 0.845 | 0.842 | 85 | 16 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.066 | 0.080 | 0.077 | 9 | 93 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.841 | 0.855 | 0.852 | 86 | 15 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.085 | 0.075 | 0.077 | 8 | 93 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.267 | 0.285 | 0.281 | 29 | 72 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.980 | 0.975 | 0.976 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-7 | game_total | 0.534 | 0.555 | 0.551 | 56 | 45 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.979 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.844 | 0.855 | 0.853 | 86 | 15 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.116 | 0.125 | 0.123 | 13 | 88 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR2 | team_total | 0.866 | 0.875 | 0.873 | 88 | 13 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-6 | game_total | 0.671 | 0.655 | 0.658 | 66 | 35 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT2 | game_spread | 0.207 | 0.195 | 0.197 | 20 | 81 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.898 | 0.905 | 0.904 | 91 | 10 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ3 | team_total | 0.641 | 0.625 | 0.628 | 63 | 38 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.247 | 0.230 | 0.233 | 24 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ4 | team_total | 0.432 | 0.415 | 0.418 | 42 | 59 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI5 | team_total | 0.121 | 0.115 | 0.116 | 12 | 89 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA2 | game_spread | 0.399 | 0.415 | 0.412 | 42 | 59 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-10 | game_total | 0.083 | 0.090 | 0.089 | 10 | 92 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3 | team_total | 0.479 | 0.460 | 0.464 | 47 | 55 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ3 | game_spread | 0.161 | 0.165 | 0.164 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-TOR2 | game_spread | 0.345 | 0.335 | 0.337 | 34 | 67 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ2 | game_spread | 0.262 | 0.255 | 0.256 | 26 | 75 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-7 | game_total | 0.565 | 0.555 | 0.557 | 56 | 45 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA3 | team_total | 0.729 | 0.740 | 0.738 | 75 | 27 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.173 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4 | team_total | 0.504 | 0.490 | 0.493 | 50 | 52 |  | -0.013 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.585 | 0.539 | 0.175 | 0.219 | 6.16 | 6.52 | 0.990/1.043 | KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 +0.072 |
| COL @ PHI | 0.368 | 0.449 | 0.176 | 0.222 | 5.93 | 5.96 | 0.990/0.979 | KXNHLGAME-26OCT19COLPHI-COL -0.081 |
| SJS @ TOR | 0.547 | 0.526 | 0.166 | 0.216 | 6.94 | 6.44 | 0.988/1.040 | KXNHLTOTAL-26OCT19SJTOR-6 -0.080 |
| PIT @ UTA | 0.613 | 0.578 | 0.160 | 0.214 | 6.75 | 6.68 | 1.001/1.033 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.044 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 15 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.219 (adj 0.198) · $10.94 · thesis ANA:OFFENSE_4PLUS
- A.J. Greer: 2+ goals YES @ 1c · p 0.0285 (adj 0.0239) · $1.67 · thesis ANA:OFFENSE_4PLUS
- Gabe Perreault: 1+ assists YES @ 26c · p 0.3355 (adj 0.2953) · $6.35 · thesis NYR:OFFENSE_4PLUS
- Taylor Raddysh: 1+ goals YES @ 9c · p 0.1202 (adj 0.1101) · $3.63 · thesis NYR:OFFENSE_4PLUS
- Nathan MacKinnon: 2+ goals NO @ 86c · p 0.915 (adj 0.8988) · $16.95 · thesis COL:SUPPRESSED
- Trevor Zegras: 1+ goals YES @ 23c · p 0.2963 (adj 0.2785) · $8.5 · thesis PHI:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 55c · p 0.6221 (adj 0.6028) · $12.8 · thesis COL:SUPPRESSED
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7959 (adj 0.7108) · $11.75 · thesis PHI:WINS
- Ivar Stenberg: 1+ goals NO @ 78c · p 0.8176 (adj 0.807) · $18.54 · thesis SJS:SUPPRESSED
- Teddy Blueger: 1+ goals YES @ 11c · p 0.1441 (adj 0.1281) · $2.82 · thesis TOR:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 20c · p 0.2329 (adj 0.2234) · $3.75 · thesis SJS:OFFENSE_4PLUS
- Jack McBain: 1+ goals YES @ 13c · p 0.1673 (adj 0.1555) · $4.72 · thesis UTA:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 20c · p 0.2446 (adj 0.2297) · $5.61 · thesis UTA:OFFENSE_4PLUS
- Rickard Rakell: 1+ goals YES @ 27c · p 0.3164 (adj 0.3035) · $6.53 · thesis PIT:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 12c · p 0.1495 (adj 0.1409) · $3.7 · thesis PIT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 168/169 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROBABLE) exp shots 28.93, exp saves 25.05 (sd 6.81), pull risk 0.063
- ANA net: Ville Husso (CONFIRMED) exp shots 24.95, exp saves 21.34 (sd 6.12), pull risk 0.075

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ville Husso: 25+ saves | 0.297 | 0.435 | 46/59 | +0.096 |  |
| Alex Killorn: 1+ points | 0.469 | 0.365 | 37/64 | +0.082 | STANDARD |
| Dylan Garand: 25+ saves | 0.535 | 0.435 | 45/58 | +0.068 |  |
| Alex Killorn: 1+ assists | 0.329 | 0.230 | 25/79 | +0.066 | STANDARD |
| A.J. Greer: 1+ goals | 0.219 | 0.135 | 14/87 | +0.071 | STANDARD |
| Gabe Perreault: 1+ assists | 0.336 | 0.255 | 26/75 | +0.062 | STANDARD |

**COL @ PHI** · priced 169/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (CONFIRMED) exp shots 30.72, exp saves 26.48 (sd 7.08), pull risk 0.06
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 24.25, exp saves 21.17 (sd 5.84), pull risk 0.046

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Cates: 1+ points | 0.443 | 0.225 | 29/84 | +0.139 | STANDARD |
| Noah Cates: 1+ assists | 0.307 | 0.100 | 19/99 | +0.106 | STANDARD |
| Cale Makar: 1+ assists | 0.401 | 0.605 | 61/40 | +0.182 | STANDARD |
| Mackenzie Blackwood: 22+ saves | 0.462 | 0.275 | 50/95 | -0.056 |  |
| Nathan MacKinnon: 2+ points | 0.304 | 0.485 | 50/53 | +0.148 | STANDARD |
| Nick Seeler: 1+ points | 0.255 | 0.075 | 14/99 | +0.107 | STANDARD |

**SJS @ TOR** · priced 169/183 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (CONFIRMED) exp shots 29.27, exp saves 25.39 (sd 6.92), pull risk 0.062
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.18, exp saves 23.37 (sd 6.42), pull risk 0.068

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Colton Sissons: 1+ points | 0.352 | 0.215 | 28/85 | +0.057 | STANDARD |
| Colton Sissons: 1+ assists | 0.235 | 0.115 | 22/99 | +0.003 | STANDARD |
| Mason Marchment: 1+ assists | 0.216 | 0.320 | 34/70 | +0.069 | STANDARD |
| Macklin Celebrini: 2+ points | 0.288 | 0.390 | 41/63 | +0.065 | STANDARD |
| Ivar Stenberg: 1+ points | 0.363 | 0.460 | 47/55 | +0.069 | PRIOR_HEAVY |
| Macklin Celebrini: 1+ assists | 0.440 | 0.535 | 55/48 | +0.063 | STANDARD |

**PIT @ UTA** · priced 198/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Sebastian Cossa (CONFIRMED) exp shots 26.47, exp saves 22.95 (sd 6.41), pull risk 0.059
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.66, exp saves 23.58 (sd 6.69), pull risk 0.08

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nate Schmidt: 1+ assists | 0.251 | 0.105 | 20/99 | +0.039 | STANDARD |
| Kaedan Korczak: 1+ assists | 0.234 | 0.095 | 18/99 | +0.044 | STANDARD |
| Andrei Kuzmenko: 1+ points | 0.290 | 0.170 | 33/99 | -0.056 | STANDARD |
| Kaedan Korczak: 1+ points | 0.269 | 0.150 | 23/93 | +0.027 | STANDARD |
| Declan Carlile: 1+ assists | 0.197 | 0.085 | 16/99 | +0.028 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.230 | 0.330 | 35/69 | +0.065 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
