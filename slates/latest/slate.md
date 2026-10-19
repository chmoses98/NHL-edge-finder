# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-19T13:22:42Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 4 · markets on board: 3102 · contracts joined: 878 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 778, 'NO_EDGE': 62, 'OK': 38}
families: {'period_winner': 36, 'period_spread': 24, 'period_total': 36, 'player_assists': 118, 'game_early_goal': 4, 'first_goal': 145, 'game_winner': 8, 'player_goals': 252, 'game_overtime': 4, 'player_points': 159, 'game_spread': 16, 'team_total': 40, 'game_total': 36}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 2026-10-19T23:00:00Z | T-6h | 0.577 | 0.423 | 0.173 | 6.17 | 3.33 | 2.84 | 218 (25/193) | PROJECTED/PROJECTED |
| COL @ PHI | 2026-10-19T23:00:00Z | T-6h | 0.394 | 0.606 | 0.181 | 5.77 | 2.58 | 3.20 | 202 (25/177) | PROJECTED/PROJECTED |
| SJS @ TOR | 2026-10-19T23:30:00Z | T-6h | 0.541 | 0.459 | 0.164 | 6.80 | 3.54 | 3.26 | 222 (25/197) | PROJECTED/PROJECTED |
| PIT @ UTA | 2026-10-20T01:00:00Z | T-6h | 0.619 | 0.381 | 0.165 | 6.69 | 3.75 | 2.94 | 236 (25/211) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL4 | team_total | 0.412 | 0.525 | 0.502 | 53 | 48 | no | +0.090 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL3 | game_spread | 0.226 | 0.330 | 0.307 | 34 | 68 | no | +0.079 | OK |
| KXNHLSPREAD-26OCT19COLPHI-COL2 | game_spread | 0.366 | 0.465 | 0.445 | 47 | 54 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL5 | team_total | 0.219 | 0.320 | 0.298 | 33 | 69 | no | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL3 | team_total | 0.635 | 0.725 | 0.708 | 73 | 28 | no | +0.071 | OK |
| KXNHLGAME-26OCT19COLPHI-COL | game_winner | 0.606 | 0.685 | 0.670 | 69 | 32 | no | +0.059 | OK |
| KXNHLGAME-26OCT19COLPHI-PHI | game_winner | 0.394 | 0.315 | 0.330 | 32 | 69 | yes | +0.059 | OK |
| KXNHLTOTAL-26OCT19COLPHI-5 | game_total | 0.720 | 0.795 | 0.781 | 80 | 21 | no | +0.058 | OK |
| KXNHLTOTAL-26OCT19COLPHI-7 | game_total | 0.380 | 0.455 | 0.440 | 46 | 55 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT19COLPHI-6 | game_total | 0.492 | 0.565 | 0.551 | 57 | 44 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL6 | team_total | 0.093 | 0.155 | 0.140 | 16 | 85 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-COL2 | team_total | 0.829 | 0.890 | 0.880 | 90 | 12 | no | +0.043 | OK |
| KXNHLTOTAL-26OCT19COLPHI-9 | game_total | 0.133 | 0.185 | 0.174 | 19 | 82 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT19COLPHI-8 | game_total | 0.201 | 0.260 | 0.247 | 27 | 75 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT19COLPHI-4 | game_total | 0.816 | 0.865 | 0.856 | 87 | 14 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT19COLPHI-PHI2 | game_spread | 0.196 | 0.155 | 0.163 | 16 | 85 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT19ANANYR-5 | game_total | 0.770 | 0.805 | 0.798 | 81 | 20 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT19COLPHI-10 | game_total | 0.056 | 0.085 | 0.078 | 9 | 92 | no | +0.019 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA3 | game_spread | 0.125 | 0.155 | 0.148 | 16 | 85 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT19SJTOR-TOR3 | game_spread | 0.214 | 0.245 | 0.239 | 25 | 76 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT19ANANYR-4 | game_total | 0.850 | 0.875 | 0.870 | 88 | 13 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT19COLPHI-3 | game_total | 0.947 | 0.970 | 0.966 | 98 | 4 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA2 | team_total | 0.769 | 0.800 | 0.794 | 81 | 21 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ6 | team_total | 0.115 | 0.095 | 0.099 | 10 | 91 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT19ANANYR-3 | game_total | 0.960 | 0.975 | 0.973 | 98 | 3 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT19ANANYR-7 | game_total | 0.445 | 0.475 | 0.469 | 48 | 53 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT19SJTOR-5 | game_total | 0.834 | 0.855 | 0.851 | 86 | 15 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT19ANANYR-6 | game_total | 0.556 | 0.585 | 0.579 | 59 | 42 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 | team_total | 0.546 | 0.580 | 0.573 | 59 | 43 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA4 | team_total | 0.329 | 0.360 | 0.354 | 37 | 65 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.826 | 0.845 | 0.841 | 85 | 16 | no | +0.005 | OK |
| KXNHLSPREAD-26OCT19ANANYR-ANA2 | game_spread | 0.224 | 0.245 | 0.241 | 25 | 76 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT19COLPHI-2 | game_total | 0.977 | 0.985 | 0.984 | 99 | 2 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI6 | team_total | 0.044 | 0.035 | 0.037 | 4 | 97 | yes | +0.002 | OK |
| KXNHLGAME-26OCT19SJTOR-SJ | game_winner | 0.459 | 0.435 | 0.440 | 44 | 57 | yes | +0.002 | OK |
| KXNHLGAME-26OCT19SJTOR-TOR | game_winner | 0.541 | 0.565 | 0.560 | 57 | 44 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT19SJTOR-2 | game_total | 0.992 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.985 | 0.987 | 99 | 2 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ5 | team_total | 0.240 | 0.220 | 0.224 | 23 | 79 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT19COLPHI-PHI3 | game_spread | 0.103 | 0.095 | 0.097 | 10 | 91 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-10 | game_total | 0.135 | 0.125 | 0.127 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-SJ4 | team_total | 0.423 | 0.405 | 0.409 | 41 | 60 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.977 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA5 | team_total | 0.165 | 0.175 | 0.173 | 18 | 83 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-4 | game_total | 0.899 | 0.905 | 0.904 | 91 | 10 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.381 | 0.365 | 0.368 | 37 | 64 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-9 | game_total | 0.257 | 0.240 | 0.243 | 25 | 77 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.078 | 0.070 | 0.072 | 8 | 94 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-10 | game_total | 0.082 | 0.090 | 0.088 | 10 | 92 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.110 | 0.120 | 0.118 | 13 | 89 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-ANA6 | team_total | 0.067 | 0.065 | 0.065 | 7 | 94 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-8 | game_total | 0.348 | 0.335 | 0.338 | 34 | 67 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-2 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR2 | team_total | 0.860 | 0.865 | 0.864 | 87 | 14 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR2 | team_total | 0.839 | 0.845 | 0.844 | 85 | 16 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-SJ2 | game_spread | 0.264 | 0.255 | 0.257 | 26 | 75 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.778 | 0.790 | 0.788 | 80 | 22 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.887 | 0.885 | 0.885 | 89 | 12 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.276 | 0.285 | 0.283 | 29 | 72 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.893 | 0.900 | 0.899 | 91 | 11 |  | -0.010 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-ANA | game_winner | 0.423 | 0.435 | 0.433 | 44 | 57 |  | -0.010 | NO_EDGE |
| KXNHLGAME-26OCT19ANANYR-NYR | game_winner | 0.577 | 0.565 | 0.567 | 57 | 44 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19ANANYR-NYR6 | team_total | 0.117 | 0.115 | 0.115 | 12 | 89 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT19SJTOR-7 | game_total | 0.543 | 0.555 | 0.553 | 56 | 45 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-8 | game_total | 0.257 | 0.270 | 0.267 | 28 | 74 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19SJTOR-TOR2 | game_spread | 0.335 | 0.345 | 0.343 | 35 | 66 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-8 | game_total | 0.326 | 0.335 | 0.333 | 34 | 67 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR4 | team_total | 0.484 | 0.500 | 0.497 | 51 | 51 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA5 | team_total | 0.326 | 0.340 | 0.337 | 35 | 67 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR6 | team_total | 0.147 | 0.140 | 0.141 | 15 | 87 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-6 | game_total | 0.636 | 0.645 | 0.643 | 65 | 36 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19ANANYR-9 | game_total | 0.182 | 0.190 | 0.188 | 20 | 82 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI2 | team_total | 0.721 | 0.715 | 0.716 | 72 | 29 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR5 | team_total | 0.289 | 0.300 | 0.298 | 31 | 71 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.124 | 0.120 | 0.121 | 13 | 89 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-7 | game_total | 0.526 | 0.535 | 0.533 | 54 | 47 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19SJTOR-TOR3 | team_total | 0.689 | 0.700 | 0.698 | 71 | 31 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19COLPHI-PHI4 | team_total | 0.269 | 0.260 | 0.262 | 27 | 75 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA4 | team_total | 0.527 | 0.535 | 0.533 | 54 | 47 |  | -0.015 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| ANA @ NYR | 0.577 | 0.532 | 0.173 | 0.218 | 6.17 | 6.47 | 0.992/1.024 | KXNHLTEAMTOTAL-26OCT19ANANYR-ANA3 +0.066 |
| COL @ PHI | 0.394 | 0.445 | 0.181 | 0.221 | 5.77 | 5.96 | 0.993/0.976 | KXNHLTEAMTOTAL-26OCT19COLPHI-PHI3 +0.057 |
| SJS @ TOR | 0.541 | 0.540 | 0.164 | 0.220 | 6.80 | 6.37 | 0.965/1.034 | KXNHLTOTAL-26OCT19SJTOR-8 -0.068 |
| PIT @ UTA | 0.619 | 0.582 | 0.165 | 0.213 | 6.69 | 6.66 | 0.993/1.033 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.050 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 13 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.229 (adj 0.2043) · $14.29 · thesis ANA:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 9c · p 0.1217 (adj 0.1113) · $3.93 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1308 (adj 0.1218) · $3.64 · thesis ANA:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ assists NO @ 69c · p 0.7609 (adj 0.7229) · $16.21 · thesis NYR:SUPPRESSED
- Travis Sanheim: 1+ goals YES @ 9c · p 0.1367 (adj 0.1175) · $5.18 · thesis PHI:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 55c · p 0.6243 (adj 0.6007) · $19.61 · thesis COL:SUPPRESSED
- Noah Cates: 1+ goals YES @ 14c · p 0.1931 (adj 0.1711) · $5.83 · thesis PHI:OFFENSE_4PLUS
- Trevor Zegras: 1+ goals YES @ 25c · p 0.2947 (adj 0.2798) · $5.41 · thesis PHI:OFFENSE_4PLUS
- Ivar Stenberg: 1+ goals NO @ 78c · p 0.8293 (adj 0.8157) · $15.67 · thesis SJS:SUPPRESSED
- Mason Marchment: 1+ assists NO @ 71c · p 0.7769 (adj 0.7385) · $9.58 · thesis SJS:SUPPRESSED
- Full Game: Over 6.5 goals scored NO @ 45c · p 0.5203 (adj 0.4826) · $4.75 · thesis SJS:SUPPRESSED
- Tyler Toffoli: 1+ assists YES @ 25c · p 0.3135 (adj 0.2742) · $4.31 · thesis SJS:OFFENSE_4PLUS
- Dylan Guenther: 1+ goals NO @ 62c · p 0.6686 (adj 0.6514) · $10.51 · thesis UTA:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**ANA @ NYR** · priced 158/167 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 28.93, exp saves 25.07 (sd 6.74), pull risk 0.064
- ANA net: Lukas Dostal (PROJECTED) exp shots 24.95, exp saves 21.37 (sd 6.13), pull risk 0.074

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| A.J. Greer: 1+ goals | 0.229 | 0.130 | 14/88 | +0.081 | STANDARD |
| Alex Killorn: 1+ points | 0.482 | 0.385 | 40/63 | +0.065 | STANDARD |
| Alex Killorn: 1+ assists | 0.334 | 0.250 | 26/76 | +0.060 | STANDARD |
| Jackson LaCombe: 1+ points | 0.593 | 0.510 | 52/50 | +0.055 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.517 | 0.435 | 44/57 | +0.060 | STANDARD |
| Alex Killorn: 1+ goals | 0.225 | 0.145 | 20/91 | +0.014 | STANDARD |

**COL @ PHI** · priced 139/151 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 30.72, exp saves 26.46 (sd 7.05), pull risk 0.062
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 24.25, exp saves 21.15 (sd 5.91), pull risk 0.05

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.411 | 0.595 | 60/41 | +0.162 | STANDARD |
| Cale Makar: 1+ points | 0.508 | 0.685 | 70/33 | +0.147 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.304 | 0.480 | 50/54 | +0.139 | STANDARD |
| Cale Makar: 2+ points | 0.159 | 0.330 | 36/70 | +0.127 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.459 | 0.605 | 61/40 | +0.124 | STANDARD |
| Christian Dvorak: 1+ goals | 0.256 | 0.135 | 20/93 | +0.044 | STANDARD |

**SJS @ TOR** · priced 170/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Anthony Stolarz (PROJECTED) exp shots 29.27, exp saves 25.43 (sd 6.88), pull risk 0.059
- SJS net: Yaroslav Askarov (PROJECTED) exp shots 27.18, exp saves 23.38 (sd 6.44), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ points | 0.341 | 0.455 | 47/56 | +0.082 | PRIOR_HEAVY |
| Ivar Stenberg: 1+ assists | 0.207 | 0.300 | 32/72 | +0.059 | PRIOR_HEAVY |
| Macklin Celebrini: 2+ points | 0.282 | 0.375 | 39/64 | +0.061 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.431 | 0.515 | 52/49 | +0.062 | STANDARD |
| Macklin Celebrini: 1+ points | 0.647 | 0.730 | 75/29 | +0.048 | STANDARD |
| Gavin McKenna: 1+ points | 0.409 | 0.490 | 50/52 | +0.054 | PRIOR_HEAVY |

**PIT @ UTA** · priced 182/185 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Karel Vejmelka (PROJECTED) exp shots 26.47, exp saves 22.91 (sd 6.41), pull risk 0.063
- PIT net: Arturs Silovs (PROJECTED) exp shots 27.66, exp saves 23.55 (sd 6.73), pull risk 0.083

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Lawson Crouse: 1+ goals | 0.246 | 0.120 | 21/97 | +0.024 | STANDARD |
| Vincent Trocheck: 1+ assists | 0.230 | 0.340 | 36/68 | +0.075 | STANDARD |
| Clayton Keller: 1+ assists | 0.464 | 0.565 | 57/44 | +0.079 | STANDARD |
| Rickard Rakell: 1+ points | 0.571 | 0.475 | 48/53 | +0.074 | STANDARD |
| Vincent Trocheck: 1+ points | 0.390 | 0.480 | 49/53 | +0.062 | STANDARD |
| Clayton Keller: 2+ points | 0.250 | 0.335 | 35/68 | +0.055 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
