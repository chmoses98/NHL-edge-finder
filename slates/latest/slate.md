# NHL slate 2026-11-01 — RESEARCH_ONLY

generated 2026-11-01T07:53:13Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2092 · contracts joined: 388 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 263, 'NO_EDGE': 62, 'OK': 63}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'player_assists': 27, 'game_early_goal': 5, 'first_goal': 19, 'game_winner': 10, 'player_goals': 62, 'game_overtime': 5, 'player_points': 25, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CAR | 2026-11-01T18:00:00Z | T-6h | 0.720 | 0.280 | 0.156 | 6.14 | 3.78 | 2.36 | 184 (25/159) | PROJECTED/PROJECTED |
| MIN @ WSH | 2026-11-01T20:30:00Z | T-12h | 0.533 | 0.467 | 0.181 | 6.03 | 3.12 | 2.91 | 51 (25/26) | PROJECTED/CONFIRMED |
| UTA @ PHI | 2026-11-01T21:00:00Z | T-12h | 0.458 | 0.542 | 0.179 | 6.00 | 2.87 | 3.13 | 51 (25/26) | PROJECTED/PROJECTED |
| EDM @ NYR | 2026-11-01T23:00:00Z | T-12h | 0.485 | 0.515 | 0.170 | 6.53 | 3.21 | 3.31 | 51 (25/26) | PROJECTED/CONFIRMED |
| OTT @ ANA | 2026-11-02T01:00:00Z | T-12h | 0.556 | 0.444 | 0.164 | 6.94 | 3.65 | 3.29 | 51 (25/26) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV01OTTANA-ANA2 | game_spread | 0.348 | 0.275 | 0.289 | 28 | 73 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA5 | team_total | 0.312 | 0.240 | 0.253 | 25 | 77 | yes | +0.049 | OK |
| KXNHLGAME-26NOV01OTTANA-ANA | game_winner | 0.556 | 0.485 | 0.499 | 49 | 52 | yes | +0.049 | OK |
| KXNHLGAME-26NOV01OTTANA-OTT | game_winner | 0.444 | 0.515 | 0.501 | 52 | 49 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA3 | team_total | 0.710 | 0.645 | 0.659 | 65 | 36 | yes | +0.044 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT2 | game_spread | 0.254 | 0.315 | 0.302 | 32 | 69 | no | +0.041 | OK |
| KXNHLGAME-26NOV01UTAPHI-PHI | game_winner | 0.458 | 0.395 | 0.407 | 40 | 61 | yes | +0.041 | OK |
| KXNHLGAME-26NOV01UTAPHI-UTA | game_winner | 0.542 | 0.605 | 0.593 | 61 | 40 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA4 | team_total | 0.507 | 0.440 | 0.453 | 45 | 57 | yes | +0.040 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA2 | game_spread | 0.317 | 0.375 | 0.363 | 38 | 63 | no | +0.037 | OK |
| KXNHLSPREAD-26NOV01OTTANA-OTT3 | game_spread | 0.152 | 0.205 | 0.193 | 21 | 80 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA6 | team_total | 0.163 | 0.110 | 0.119 | 12 | 90 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN4 | team_total | 0.341 | 0.405 | 0.392 | 42 | 61 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-UTA3 | game_spread | 0.195 | 0.250 | 0.238 | 26 | 76 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA2 | team_total | 0.812 | 0.855 | 0.847 | 86 | 15 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR3 | game_spread | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.029 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-PHI2 | game_spread | 0.249 | 0.205 | 0.213 | 21 | 80 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA3 | team_total | 0.618 | 0.665 | 0.656 | 67 | 34 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN3 | game_spread | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-NYR2 | game_spread | 0.280 | 0.325 | 0.316 | 33 | 68 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV01OTTANA-ANA3 | game_spread | 0.225 | 0.185 | 0.193 | 19 | 82 | yes | +0.025 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-EDM2 | game_spread | 0.306 | 0.265 | 0.273 | 27 | 74 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR2 | team_total | 0.819 | 0.855 | 0.848 | 86 | 15 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA4 | team_total | 0.392 | 0.445 | 0.434 | 46 | 57 | no | +0.021 | OK |
| KXNHLGAME-26NOV01EDMNYR-EDM | game_winner | 0.515 | 0.475 | 0.483 | 48 | 53 | yes | +0.017 | OK |
| KXNHLGAME-26NOV01EDMNYR-NYR | game_winner | 0.485 | 0.525 | 0.517 | 53 | 48 | no | +0.017 | OK |
| KXNHLGAME-26NOV01MINWSH-MIN | game_winner | 0.467 | 0.505 | 0.497 | 51 | 50 | no | +0.016 | OK |
| KXNHLGAME-26NOV01MINWSH-WSH | game_winner | 0.533 | 0.495 | 0.503 | 50 | 51 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-ANA2 | team_total | 0.875 | 0.840 | 0.848 | 85 | 17 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN5 | team_total | 0.173 | 0.210 | 0.202 | 22 | 80 | no | +0.016 | OK |
| KXNHLSPREAD-26NOV01MINWSH-MIN2 | game_spread | 0.251 | 0.285 | 0.278 | 29 | 72 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN3 | team_total | 0.560 | 0.605 | 0.596 | 62 | 41 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM6 | team_total | 0.118 | 0.090 | 0.095 | 10 | 92 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV01OTTANA-9 | game_total | 0.274 | 0.240 | 0.247 | 25 | 77 | yes | +0.011 | OK |
| KXNHLTOTAL-26NOV01MINWSH-9 | game_total | 0.159 | 0.185 | 0.180 | 19 | 82 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV01MINWSH-5 | game_total | 0.758 | 0.785 | 0.780 | 79 | 22 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR4 | team_total | 0.412 | 0.455 | 0.446 | 47 | 56 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT3 | team_total | 0.634 | 0.675 | 0.667 | 69 | 34 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT2 | team_total | 0.831 | 0.855 | 0.850 | 86 | 15 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR3 | team_total | 0.624 | 0.665 | 0.657 | 68 | 35 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV01OTTANA-8 | game_total | 0.365 | 0.330 | 0.337 | 34 | 68 | yes | +0.010 | OK |
| KXNHLSPREAD-26NOV01EDMNYR-EDM3 | game_spread | 0.189 | 0.165 | 0.170 | 17 | 84 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV01OTTANA-6 | game_total | 0.675 | 0.645 | 0.651 | 65 | 36 | yes | +0.009 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-5 | game_total | 0.749 | 0.775 | 0.770 | 78 | 23 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV01MINWSH-6 | game_total | 0.534 | 0.570 | 0.563 | 58 | 44 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA5 | team_total | 0.210 | 0.245 | 0.238 | 26 | 77 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-EDM4 | team_total | 0.434 | 0.400 | 0.407 | 41 | 61 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV01OTTANA-10 | game_total | 0.144 | 0.120 | 0.125 | 13 | 89 | yes | +0.006 | OK |
| KXNHLSPREAD-26NOV01MINWSH-WSH2 | game_spread | 0.311 | 0.285 | 0.290 | 29 | 72 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT4 | team_total | 0.427 | 0.460 | 0.453 | 47 | 55 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI6 | team_total | 0.069 | 0.050 | 0.053 | 6 | 96 | yes | +0.005 | OK |
| KXNHLSPREAD-26NOV01UTAPHI-PHI3 | game_spread | 0.143 | 0.125 | 0.128 | 13 | 88 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN2 | team_total | 0.784 | 0.815 | 0.809 | 83 | 20 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV01MINWSH-10 | game_total | 0.070 | 0.085 | 0.082 | 9 | 92 | no | +0.005 | OK |
| KXNHLTOTAL-26NOV01MINWSH-8 | game_total | 0.233 | 0.260 | 0.254 | 27 | 75 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26NOV01MINWSH-MIN6 | team_total | 0.072 | 0.085 | 0.082 | 9 | 92 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26NOV01OTTANA-OTT5 | team_total | 0.244 | 0.270 | 0.265 | 28 | 74 | no | +0.003 | OK |
| KXNHLSPREAD-26NOV01WPGCAR-WPG3 | game_spread | 0.063 | 0.075 | 0.072 | 8 | 93 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV01OTTANA-2 | game_total | 0.993 | 0.985 | 0.987 | 99 | 2 | yes | +0.003 | OK |
| KXNHLTOTAL-26NOV01MINWSH-7 | game_total | 0.420 | 0.450 | 0.444 | 46 | 56 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV01EDMNYR-10 | game_total | 0.108 | 0.095 | 0.098 | 10 | 91 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI4 | team_total | 0.336 | 0.310 | 0.315 | 32 | 70 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-UTA6 | team_total | 0.094 | 0.110 | 0.107 | 12 | 90 | no | +0.000 | OK |
| KXNHLTOTAL-26NOV01UTAPHI-3 | game_total | 0.958 | 0.975 | 0.972 | 99 | 4 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26NOV01MINWSH-3 | game_total | 0.958 | 0.975 | 0.972 | 99 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 | team_total | 0.546 | 0.525 | 0.529 | 53 | 48 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-5 | game_total | 0.848 | 0.835 | 0.838 | 84 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV01UTAPHI-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01OTTANA-7 | game_total | 0.565 | 0.545 | 0.549 | 55 | 46 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01MINWSH-4 | game_total | 0.844 | 0.860 | 0.857 | 87 | 15 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV01EDMNYR-2 | game_total | 0.988 | 0.985 | 0.986 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV01UTAPHI-7 | game_total | 0.416 | 0.435 | 0.431 | 44 | 57 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01MINWSH-WSH6 | team_total | 0.093 | 0.085 | 0.086 | 9 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR6 | team_total | 0.106 | 0.120 | 0.117 | 13 | 89 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV01EDMNYR-NYR5 | team_total | 0.232 | 0.255 | 0.250 | 27 | 76 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV01WPGCAR-10 | game_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV01UTAPHI-6 | game_total | 0.528 | 0.545 | 0.542 | 55 | 46 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV01WPGCAR-5 | game_total | 0.763 | 0.775 | 0.773 | 78 | 23 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26NOV01WPGCAR-WPG2 | game_spread | 0.127 | 0.135 | 0.133 | 14 | 87 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV01UTAPHI-9 | game_total | 0.156 | 0.170 | 0.167 | 18 | 84 |  | -0.006 | NO_EDGE |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| WPG @ CAR | 0.720 | 0.630 | 0.156 | 0.207 | 6.14 | 6.31 | 0.998/0.998 | KXNHLTEAMTOTAL-26NOV01WPGCAR-WPG3 +0.093 |
| MIN @ WSH | 0.533 | 0.545 | 0.181 | 0.214 | 6.03 | 6.29 | 0.961/0.991 | KXNHLTOTAL-26NOV01MINWSH-7 +0.052 |
| UTA @ PHI | 0.458 | 0.500 | 0.179 | 0.227 | 6.00 | 6.10 | 0.994/0.998 | KXNHLTEAMTOTAL-26NOV01UTAPHI-PHI3 +0.050 |
| EDM @ NYR | 0.485 | 0.472 | 0.170 | 0.213 | 6.53 | 6.69 | 0.987/1.000 | KXNHLTOTAL-26NOV01EDMNYR-7 +0.034 |
| OTT @ ANA | 0.556 | 0.563 | 0.164 | 0.211 | 6.94 | 6.62 | 0.968/1.051 | KXNHLTOTAL-26NOV01OTTANA-6 -0.056 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 10 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Iafallo: 1+ goals YES @ 10c · p 0.1462 (adj 0.1309) · $5.94 · thesis WPG:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 71c · p 0.7612 (adj 0.7459) · $19.01 · thesis CAR:SUPPRESSED
- Carolina wins by over 1.5 goals NO @ 51c · p 0.5869 (adj 0.5459) · $5.04 · thesis GAME:TIGHT
- Mark Scheifele: 1+ goals YES @ 27c · p 0.3084 (adj 0.2951) · $3.14 · thesis WPG:OFFENSE_4PLUS
- Philadelphia wins by over 1.5 goals YES @ 21c · p 0.2802 (adj 0.2426) · $4.5 · thesis PHI:WINS_BY_2PLUS
- Utah wins by over 2.5 goals NO @ 76c · p 0.8309 (adj 0.7904) · $16.82 · thesis PHI:WINS
- Ottawa wins by over 1.5 goals NO @ 69c · p 0.7732 (adj 0.7291) · $10.68 · thesis ANA:WINS
- Anaheim wins by over 1.5 goals YES @ 28c · p 0.3588 (adj 0.3169) · $3.95 · thesis ANA:WINS_BY_2PLUS
- Ottawa wins by over 2.5 goals NO @ 80c · p 0.8639 (adj 0.8295) · $11.64 · thesis ANA:WINS
- Ottawa over 1.5 goals scored NO @ 15c · p 0.2007 (adj 0.1729) · $1.33 · thesis OTT:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**WPG @ CAR** · priced 130/133 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.11, exp saves 20.33 (sd 5.66), pull risk 0.045
- WPG net: Nico Daws (PROJECTED) exp shots 31.46, exp saves 26.58 (sd 7.37), pull risk 0.084

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nicolas Deslauriers: First Goalscorer | 0.013 | 0.475 | 93/98 | +0.006 | STANDARD |
| Sean Walker: First Goalscorer | 0.013 | 0.475 | 93/98 | +0.006 | STANDARD |
| Shayne Gostisbehere: First Goalscorer | 0.021 | 0.475 | 93/98 | -0.002 | STANDARD |
| Mark Jankowski: First Goalscorer | 0.036 | 0.485 | 93/96 | +0.001 | STANDARD |
| William Carrier: First Goalscorer | 0.032 | 0.480 | 93/97 | -0.004 | STANDARD |
| Gabriel Vilardi: 2+ assists | 0.063 | 0.495 | 97/98 | -0.044 | STANDARD |

**MIN @ WSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 28.92, exp saves 25.15 (sd 6.81), pull risk 0.057
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 27.72, exp saves 23.81 (sd 6.62), pull risk 0.063

**UTA @ PHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Dan Vladar (PROJECTED) exp shots 27.72, exp saves 23.98 (sd 6.56), pull risk 0.056
- UTA net: Sebastian Cossa (PROJECTED) exp shots 25.2, exp saves 21.9 (sd 6.18), pull risk 0.056

**EDM @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 28.57, exp saves 24.51 (sd 6.94), pull risk 0.076
- EDM net: Matt Tomkins (CONFIRMED) exp shots 25.83, exp saves 22.28 (sd 6.26), pull risk 0.07

**OTT @ ANA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Laurent Brossoit (CONFIRMED) exp shots 27.11, exp saves 23.53 (sd 6.48), pull risk 0.062
- OTT net: Samuel Ersson (PROJECTED) exp shots 27.68, exp saves 23.56 (sd 6.65), pull risk 0.083

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
