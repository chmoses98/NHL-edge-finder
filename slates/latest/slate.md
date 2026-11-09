# NHL slate 2026-11-09 — RESEARCH_ONLY

generated 2026-11-09T21:33:27Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2491 · contracts joined: 692 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 617, 'NO_EDGE': 45, 'OK': 30}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 110, 'game_early_goal': 3, 'first_goal': 105, 'game_winner': 6, 'player_goals': 180, 'game_overtime': 3, 'player_points': 138, 'goalie_saves': 6, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ EDM | 2026-11-10T01:00:00Z | T-3h | 0.589 | 0.411 | 0.167 | 6.45 | 3.51 | 2.94 | 233 (25/208) | CONFIRMED/CONFIRMED |
| PHI @ VAN | 2026-11-10T02:30:00Z | T-3h | 0.520 | 0.480 | 0.175 | 6.44 | 3.28 | 3.16 | 228 (25/203) | PROBABLE/PROBABLE |
| NYI @ SJS | 2026-11-10T03:00:00Z | T-3h | 0.429 | 0.571 | 0.173 | 6.21 | 2.88 | 3.33 | 231 (25/206) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26NOV09PHIVAN-PHI2 | game_spread | 0.273 | 0.345 | 0.330 | 35 | 66 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-VAN2 | game_spread | 0.309 | 0.245 | 0.257 | 25 | 76 | yes | +0.046 | OK |
| KXNHLGAME-26NOV09PHIVAN-PHI | game_winner | 0.480 | 0.545 | 0.532 | 55 | 46 | no | +0.043 | OK |
| KXNHLGAME-26NOV09PHIVAN-VAN | game_winner | 0.520 | 0.455 | 0.468 | 46 | 55 | yes | +0.043 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-PHI3 | game_spread | 0.165 | 0.225 | 0.212 | 23 | 78 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN5 | team_total | 0.240 | 0.175 | 0.187 | 19 | 84 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN6 | team_total | 0.116 | 0.070 | 0.078 | 8 | 94 | yes | +0.031 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-VAN3 | game_spread | 0.187 | 0.145 | 0.153 | 15 | 86 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN3 | team_total | 0.644 | 0.595 | 0.605 | 60 | 41 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN4 | team_total | 0.423 | 0.370 | 0.380 | 38 | 64 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV09NYREDM-EDM4 | team_total | 0.475 | 0.515 | 0.507 | 52 | 49 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV09NYISJ-5 | game_total | 0.772 | 0.805 | 0.799 | 81 | 20 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI2 | team_total | 0.815 | 0.850 | 0.843 | 86 | 16 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-8 | game_total | 0.298 | 0.265 | 0.271 | 27 | 74 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN2 | team_total | 0.834 | 0.795 | 0.803 | 81 | 22 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV09NYREDM-5 | game_total | 0.797 | 0.825 | 0.820 | 83 | 18 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4 | team_total | 0.401 | 0.435 | 0.428 | 44 | 57 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI3 | team_total | 0.614 | 0.650 | 0.643 | 66 | 36 | no | +0.010 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-10 | game_total | 0.104 | 0.080 | 0.084 | 9 | 93 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ2 | team_total | 0.771 | 0.800 | 0.794 | 81 | 21 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV09NYISJ-4 | game_total | 0.855 | 0.875 | 0.871 | 88 | 13 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ4 | team_total | 0.337 | 0.365 | 0.359 | 37 | 64 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV09NYREDM-EDM3 | team_total | 0.689 | 0.715 | 0.710 | 72 | 29 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV09NYREDM-4 | game_total | 0.877 | 0.895 | 0.892 | 90 | 11 | no | +0.006 | OK |
| KXNHLTOTAL-26NOV09NYISJ-7 | game_total | 0.449 | 0.475 | 0.470 | 48 | 53 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV09NYISJ-6 | game_total | 0.561 | 0.585 | 0.580 | 59 | 42 | no | +0.002 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-7 | game_total | 0.489 | 0.465 | 0.470 | 47 | 54 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26NOV09NYREDM-EDM2 | team_total | 0.861 | 0.885 | 0.880 | 90 | 13 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-9 | game_total | 0.212 | 0.190 | 0.194 | 20 | 82 | yes | +0.001 | OK |
| KXNHLSPREAD-26NOV09NYISJ-SJ3 | game_spread | 0.131 | 0.150 | 0.146 | 16 | 86 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV09NYISJ-10 | game_total | 0.085 | 0.095 | 0.093 | 10 | 91 |  | -0.000 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYREDM-EDM3 | game_spread | 0.238 | 0.255 | 0.251 | 26 | 75 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-2 | game_total | 0.989 | 0.985 | 0.986 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-10 | game_total | 0.104 | 0.095 | 0.097 | 10 | 91 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYREDM-NYR3 | game_spread | 0.125 | 0.135 | 0.133 | 14 | 87 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-2 | game_total | 0.988 | 0.980 | 0.982 | 99 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI4 | team_total | 0.436 | 0.455 | 0.451 | 46 | 55 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-6 | game_total | 0.598 | 0.615 | 0.612 | 62 | 39 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-NYR6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26NOV09NYREDM-EDM | game_winner | 0.589 | 0.605 | 0.602 | 61 | 40 |  | -0.005 | NO_EDGE |
| KXNHLGAME-26NOV09NYREDM-NYR | game_winner | 0.411 | 0.395 | 0.398 | 40 | 61 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-2 | game_total | 0.985 | 0.985 | 0.985 | 99 | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-EDM5 | team_total | 0.281 | 0.300 | 0.296 | 31 | 71 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-7 | game_total | 0.488 | 0.505 | 0.502 | 51 | 50 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ5 | team_total | 0.167 | 0.180 | 0.177 | 19 | 83 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-3 | game_total | 0.965 | 0.975 | 0.973 | 99 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-EDM6 | team_total | 0.140 | 0.130 | 0.132 | 14 | 88 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-6 | game_total | 0.598 | 0.580 | 0.584 | 59 | 43 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI6 | team_total | 0.118 | 0.110 | 0.112 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-9 | game_total | 0.211 | 0.205 | 0.206 | 21 | 80 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI2 | team_total | 0.842 | 0.855 | 0.852 | 87 | 16 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI5 | team_total | 0.220 | 0.235 | 0.232 | 25 | 78 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-SJ2 | game_spread | 0.230 | 0.240 | 0.238 | 25 | 77 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-3 | game_total | 0.970 | 0.975 | 0.974 | 99 | 4 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYREDM-NYR2 | game_spread | 0.219 | 0.210 | 0.212 | 22 | 80 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-3 | game_total | 0.971 | 0.975 | 0.974 | 99 | 4 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-5 | game_total | 0.798 | 0.795 | 0.796 | 80 | 21 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI3 | game_spread | 0.221 | 0.230 | 0.228 | 24 | 78 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ3 | team_total | 0.557 | 0.570 | 0.567 | 58 | 44 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-4 | game_total | 0.873 | 0.870 | 0.871 | 88 | 14 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ6 | team_total | 0.070 | 0.075 | 0.074 | 9 | 94 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-NYR2 | team_total | 0.783 | 0.790 | 0.789 | 80 | 22 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-NYI | game_winner | 0.571 | 0.565 | 0.566 | 57 | 44 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-8 | game_total | 0.262 | 0.265 | 0.264 | 27 | 74 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI3 | team_total | 0.650 | 0.665 | 0.662 | 68 | 35 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI6 | team_total | 0.101 | 0.100 | 0.100 | 11 | 91 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-9 | game_total | 0.186 | 0.190 | 0.189 | 20 | 82 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYREDM-EDM2 | game_spread | 0.371 | 0.375 | 0.374 | 38 | 63 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-NYR5 | team_total | 0.183 | 0.180 | 0.181 | 19 | 83 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-SJ | game_winner | 0.429 | 0.425 | 0.426 | 43 | 58 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYREDM-8 | game_total | 0.294 | 0.295 | 0.295 | 30 | 71 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI2 | game_spread | 0.347 | 0.345 | 0.345 | 35 | 66 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-NYR3 | team_total | 0.566 | 0.565 | 0.565 | 57 | 44 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI5 | team_total | 0.249 | 0.250 | 0.250 | 26 | 76 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYREDM-NYR4 | team_total | 0.349 | 0.345 | 0.346 | 36 | 67 |  | -0.027 | NO_EDGE |
| KXNHL1P-26NOV09NYREDM-EDM | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09NYREDM-NYR | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09NYREDM-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09NYREDM-EDM2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09NYREDM-NYR2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ EDM | 0.589 | 0.629 | 0.167 | 0.206 | 6.45 | 6.68 | 0.994/0.988 | KXNHLTEAMTOTAL-26NOV09NYREDM-EDM4 +0.062 |
| PHI @ VAN | 0.520 | 0.530 | 0.175 | 0.214 | 6.44 | 6.18 | 1.030/0.991 | KXNHLTOTAL-26NOV09PHIVAN-6 -0.046 |
| NYI @ SJS | 0.429 | 0.499 | 0.173 | 0.217 | 6.21 | 6.32 | 1.039/0.952 | KXNHLGAME-26NOV09NYISJ-NYI -0.071 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Alex Formenton: 1+ goals YES @ 11c · p 0.1642 (adj 0.1469) · $7.35 · thesis EDM:OFFENSE_4PLUS
- Vasily Podkolzin: 1+ goals YES @ 23c · p 0.283 (adj 0.2685) · $9.42 · thesis EDM:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 69c · p 0.7435 (adj 0.7289) · $19.59 · thesis NYR:SUPPRESSED
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.4998 (adj 0.4524) · $13.64 · thesis EDM:SUPPRESSED
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1737 (adj 0.1565) · $9.8 · thesis VAN:OFFENSE_4PLUS
- Porter Martone: 1+ goals NO @ 73c · p 0.811 (adj 0.7895) · $20.0 · thesis PHI:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2278 (adj 0.2121) · $9.17 · thesis VAN:OFFENSE_4PLUS
- Arshdeep Bains: 1+ goals YES @ 9c · p 0.1259 (adj 0.1157) · $4.85 · thesis VAN:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2237 (adj 0.209) · $8.57 · thesis SJS:OFFENSE_4PLUS
- Michael Misa: 1+ goals YES @ 19c · p 0.2405 (adj 0.2266) · $7.91 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: 1+ goals YES @ 21c · p 0.2569 (adj 0.2439) · $7.2 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 68c · p 0.7605 (adj 0.7177) · $20.0 · thesis SJS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ EDM** · priced 181/182 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 25.22, exp saves 22.05 (sd 6.13), pull risk 0.051
- NYR net: Dylan Garand (CONFIRMED) exp shots 29.05, exp saves 24.49 (sd 6.95), pull risk 0.093

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 1+ assists | 0.612 | 0.730 | 74/28 | +0.094 | STANDARD |
| Leon Draisaitl: 2+ points | 0.376 | 0.485 | 49/52 | +0.086 | STANDARD |
| Connor McDavid: 2+ assists | 0.247 | 0.355 | 37/66 | +0.077 | STANDARD |
| Connor McDavid: 2+ points | 0.462 | 0.565 | 57/44 | +0.081 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.500 | 0.595 | 60/41 | +0.073 | STANDARD |
| Connor McDavid: 3+ points | 0.202 | 0.280 | 30/74 | +0.045 | STANDARD |

**PHI @ VAN** · priced 168/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 26.63, exp saves 23.16 (sd 6.3), pull risk 0.056
- PHI net: Joseph Woll (PROBABLE) exp shots 25.08, exp saves 21.59 (sd 6.15), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ points | 0.425 | 0.555 | 56/45 | +0.107 | STANDARD |
| Travis Konecny: 1+ assists | 0.258 | 0.380 | 39/63 | +0.096 | STANDARD |
| Travis Konecny: 2+ points | 0.107 | 0.195 | 21/82 | +0.063 | STANDARD |
| Porter Martone: 1+ goals | 0.189 | 0.275 | 28/73 | +0.067 | STANDARD |
| Porter Martone: 1+ points | 0.406 | 0.485 | 50/53 | +0.047 | STANDARD |
| Owen Tippett: 1+ points | 0.371 | 0.450 | 46/56 | +0.051 | STANDARD |

**NYI @ SJS** · priced 170/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.92, exp saves 24.19 (sd 6.68), pull risk 0.063
- NYI net: Ilya Sorokin (PROBABLE) exp shots 27.14, exp saves 23.6 (sd 6.57), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Ivar Stenberg: 1+ assists | 0.239 | 0.325 | 33/68 | +0.065 | STANDARD |
| Michael Misa: 1+ points | 0.520 | 0.440 | 45/57 | +0.052 | STANDARD |
| Collin Graf: 1+ assists | 0.262 | 0.185 | 20/83 | +0.051 | STANDARD |
| Adam Pelech: 1+ points | 0.294 | 0.220 | 24/80 | +0.041 | STANDARD |
| Collin Graf: 1+ points | 0.392 | 0.320 | 33/69 | +0.047 | STANDARD |
| Matthew Schaefer: 1+ points | 0.569 | 0.640 | 65/37 | +0.045 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
