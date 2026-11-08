# NHL slate 2026-11-07 — RESEARCH_ONLY

generated 2026-11-08T01:24:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 12 · simulated (not started): 3 · markets on board: 3569 · contracts joined: 684 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 609, 'OK': 45, 'NO_EDGE': 30}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 102, 'game_early_goal': 3, 'first_goal': 108, 'game_winner': 6, 'player_goals': 186, 'game_overtime': 3, 'player_points': 131, 'goalie_saves': 4, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ COL | 2026-11-08T02:00:00Z | T-30m | 0.630 | 0.370 | 0.174 | 6.23 | 3.53 | 2.69 | 238 (25/213) | CONFIRMED/PROJECTED |
| PIT @ LAK | 2026-11-08T02:00:00Z | T-30m | 0.571 | 0.429 | 0.171 | 6.64 | 3.55 | 3.09 | 221 (25/196) | PROBABLE/CONFIRMED |
| VAN @ EDM | 2026-11-08T03:00:00Z | T-90m | 0.734 | 0.266 | 0.139 | 7.19 | 4.43 | 2.76 | 225 (25/200) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26NOV07PITLA-LA3 | team_total | 0.695 | 0.635 | 0.647 | 64 | 37 | yes | +0.039 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA5 | team_total | 0.288 | 0.230 | 0.241 | 24 | 78 | yes | +0.035 | OK |
| KXNHLGAME-26NOV07PITLA-LA | game_winner | 0.571 | 0.515 | 0.526 | 52 | 49 | yes | +0.033 | OK |
| KXNHLGAME-26NOV07PITLA-PIT | game_winner | 0.429 | 0.485 | 0.474 | 49 | 52 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3 | team_total | 0.519 | 0.465 | 0.476 | 47 | 54 | yes | +0.032 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL3 | game_spread | 0.263 | 0.315 | 0.304 | 32 | 69 | no | +0.032 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT2 | game_spread | 0.236 | 0.285 | 0.275 | 29 | 72 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA6 | team_total | 0.146 | 0.100 | 0.108 | 11 | 91 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 | team_total | 0.484 | 0.535 | 0.525 | 54 | 47 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA4 | team_total | 0.486 | 0.435 | 0.445 | 44 | 57 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM3 | game_spread | 0.398 | 0.445 | 0.435 | 45 | 56 | no | +0.025 | OK |
| KXNHLGAME-26NOV07VANEDM-EDM | game_winner | 0.734 | 0.775 | 0.767 | 78 | 23 | no | +0.024 | OK |
| KXNHLGAME-26NOV07VANEDM-VAN | game_winner | 0.266 | 0.225 | 0.233 | 23 | 78 | yes | +0.024 | OK |
| KXNHLTOTAL-26NOV07PITLA-9 | game_total | 0.235 | 0.195 | 0.202 | 20 | 81 | yes | +0.023 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA2 | game_spread | 0.358 | 0.310 | 0.319 | 32 | 70 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN4 | team_total | 0.306 | 0.260 | 0.269 | 27 | 75 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL2 | team_total | 0.862 | 0.900 | 0.893 | 91 | 11 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV07PITLA-8 | game_total | 0.325 | 0.285 | 0.293 | 29 | 72 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV07DETCOL-5 | game_total | 0.770 | 0.810 | 0.802 | 82 | 20 | no | +0.019 | OK |
| KXNHLTOTAL-26NOV07VANEDM-8 | game_total | 0.405 | 0.365 | 0.373 | 37 | 64 | yes | +0.019 | OK |
| KXNHLTOTAL-26NOV07DETCOL-6 | game_total | 0.566 | 0.605 | 0.597 | 61 | 40 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN5 | team_total | 0.153 | 0.120 | 0.126 | 13 | 89 | yes | +0.015 | OK |
| KXNHLGAME-26NOV07DETCOL-DET | game_winner | 0.370 | 0.335 | 0.342 | 34 | 67 | yes | +0.015 | OK |
| KXNHLGAME-26NOV07DETCOL-COL | game_winner | 0.630 | 0.665 | 0.658 | 67 | 34 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL3 | team_total | 0.692 | 0.735 | 0.727 | 75 | 28 | no | +0.014 | OK |
| KXNHLSPREAD-26NOV07VANEDM-EDM2 | game_spread | 0.539 | 0.575 | 0.568 | 58 | 43 | no | +0.014 | OK |
| KXNHLTOTAL-26NOV07PITLA-10 | game_total | 0.120 | 0.095 | 0.100 | 10 | 91 | yes | +0.014 | OK |
| KXNHLTOTAL-26NOV07VANEDM-10 | game_total | 0.172 | 0.145 | 0.150 | 15 | 86 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV07PITLA-PIT3 | game_spread | 0.138 | 0.165 | 0.159 | 17 | 84 | no | +0.013 | OK |
| KXNHLTOTAL-26NOV07PITLA-6 | game_total | 0.629 | 0.595 | 0.602 | 60 | 41 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN6 | team_total | 0.065 | 0.040 | 0.044 | 5 | 97 | yes | +0.012 | OK |
| KXNHLTOTAL-26NOV07PITLA-7 | game_total | 0.518 | 0.485 | 0.492 | 49 | 52 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL5 | team_total | 0.285 | 0.325 | 0.317 | 34 | 69 | no | +0.010 | OK |
| KXNHLSPREAD-26NOV07DETCOL-COL2 | game_spread | 0.403 | 0.435 | 0.429 | 44 | 57 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26NOV07PITLA-LA2 | team_total | 0.869 | 0.835 | 0.842 | 85 | 18 | yes | +0.010 | OK |
| KXNHLSPREAD-26NOV07PITLA-LA3 | game_spread | 0.231 | 0.205 | 0.210 | 21 | 80 | yes | +0.010 | OK |
| KXNHLTOTAL-26NOV07DETCOL-7 | game_total | 0.454 | 0.485 | 0.479 | 49 | 52 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV07DETCOL-4 | game_total | 0.854 | 0.880 | 0.875 | 89 | 13 | no | +0.009 | OK |
| KXNHLTOTAL-26NOV07VANEDM-9 | game_total | 0.302 | 0.275 | 0.280 | 28 | 73 | yes | +0.007 | OK |
| KXNHLTOTAL-26NOV07PITLA-4 | game_total | 0.892 | 0.875 | 0.879 | 88 | 13 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV07VANEDM-2 | game_total | 0.994 | 0.985 | 0.988 | 99 | 2 | yes | +0.004 | OK |
| KXNHLTOTAL-26NOV07DETCOL-9 | game_total | 0.187 | 0.210 | 0.205 | 22 | 80 | no | +0.001 | OK |
| KXNHLSPREAD-26NOV07VANEDM-VAN2 | game_spread | 0.129 | 0.110 | 0.114 | 12 | 90 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM2 | team_total | 0.935 | 0.945 | 0.943 | 95 | 6 | no | +0.001 | OK |
| KXNHLTOTAL-26NOV07PITLA-2 | game_total | 0.991 | 0.980 | 0.983 | 99 | 3 | yes | +0.000 | OK |
| KXNHLTOTAL-26NOV07DETCOL-8 | game_total | 0.266 | 0.285 | 0.281 | 29 | 72 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM6 | team_total | 0.283 | 0.265 | 0.269 | 27 | 74 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-6 | game_total | 0.713 | 0.695 | 0.699 | 70 | 31 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-VAN2 | team_total | 0.752 | 0.730 | 0.735 | 74 | 28 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-4 | game_total | 0.928 | 0.935 | 0.934 | 94 | 7 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-COL6 | team_total | 0.145 | 0.165 | 0.161 | 18 | 85 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV07PITLA-3 | game_total | 0.976 | 0.970 | 0.971 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07DETCOL-3 | game_total | 0.963 | 0.975 | 0.973 | 99 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-3 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-7 | game_total | 0.601 | 0.580 | 0.584 | 59 | 43 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV07DETCOL-2 | game_total | 0.985 | 0.980 | 0.981 | 99 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT2 | team_total | 0.806 | 0.815 | 0.813 | 82 | 19 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26NOV07VANEDM-VAN3 | game_spread | 0.067 | 0.060 | 0.061 | 7 | 95 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT4 | team_total | 0.382 | 0.395 | 0.392 | 40 | 61 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26NOV07DETCOL-DET2 | game_spread | 0.182 | 0.175 | 0.176 | 18 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM3 | team_total | 0.829 | 0.845 | 0.842 | 86 | 17 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET5 | team_total | 0.139 | 0.130 | 0.132 | 14 | 88 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26NOV07DETCOL-DET3 | game_spread | 0.096 | 0.095 | 0.095 | 10 | 91 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV07PITLA-5 | game_total | 0.820 | 0.810 | 0.812 | 82 | 20 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT6 | team_total | 0.095 | 0.090 | 0.091 | 10 | 92 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV07DETCOL-10 | game_total | 0.089 | 0.090 | 0.090 | 10 | 92 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV07VANEDM-5 | game_total | 0.871 | 0.870 | 0.870 | 88 | 14 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET3 | team_total | 0.511 | 0.500 | 0.502 | 51 | 51 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET6 | team_total | 0.056 | 0.055 | 0.055 | 7 | 96 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM4 | team_total | 0.663 | 0.670 | 0.669 | 68 | 34 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET2 | team_total | 0.744 | 0.740 | 0.741 | 75 | 27 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07DETCOL-DET4 | team_total | 0.294 | 0.290 | 0.291 | 30 | 72 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT5 | team_total | 0.210 | 0.210 | 0.210 | 22 | 80 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07PITLA-PIT3 | team_total | 0.595 | 0.595 | 0.595 | 60 | 41 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV07VANEDM-EDM5 | team_total | 0.465 | 0.470 | 0.469 | 48 | 54 |  | -0.022 | NO_EDGE |
| KXNHL1P-26NOV07DETCOL-COL | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07DETCOL-DET | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV07DETCOL-TIE | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07DETCOL-COL2 | period_spread |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV07DETCOL-DET2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ COL | 0.630 | 0.661 | 0.174 | 0.202 | 6.23 | 6.48 | 0.979/1.015 | KXNHLTEAMTOTAL-26NOV07DETCOL-COL4 +0.054 |
| PIT @ LAK | 0.571 | 0.546 | 0.171 | 0.218 | 6.64 | 6.35 | 0.994/1.012 | KXNHLTOTAL-26NOV07PITLA-8 -0.051 |
| VAN @ EDM | 0.734 | 0.670 | 0.139 | 0.190 | 7.19 | 6.99 | 0.994/1.030 | KXNHLSPREAD-26NOV07VANEDM-EDM2 -0.076 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Sheldon Dries: 1+ goals YES @ 7c · p 0.1065 (adj 0.0961) · $5.18 · thesis DET:OFFENSE_4PLUS
- Carter Mazur: 1+ goals YES @ 6c · p 0.0851 (adj 0.0763) · $2.96 · thesis DET:OFFENSE_4PLUS
- Sam Malinski: 1+ assists YES @ 25c · p 0.318 (adj 0.2815) · $5.29 · thesis COL:OFFENSE_4PLUS
- Lucas Raymond: 1+ assists NO @ 60c · p 0.6819 (adj 0.636) · $13.65 · thesis DET:SUPPRESSED
- Joel Edmundson: 1+ goals YES @ 5c · p 0.0751 (adj 0.0676) · $3.37 · thesis LAK:OFFENSE_4PLUS
- Kaedan Korczak: 1+ goals YES @ 4c · p 0.054 (adj 0.053) · $2.73 · thesis DIFFUSE
- Ben Kindel: 1+ assists NO @ 70c · p 0.7767 (adj 0.7333) · $19.29 · thesis PIT:SUPPRESSED
- Artemi Panarin: 1+ goals NO @ 63c · p 0.6797 (adj 0.666) · $14.18 · thesis LAK:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.3483 (adj 0.325) · $16.95 · thesis EDM:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2205 (adj 0.2041) · $8.81 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 10c · p 0.1436 (adj 0.1302) · $5.5 · thesis VAN:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 57c · p 0.7356 (adj 0.6215) · $18.74 · thesis EDM:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**DET @ COL** · priced 178/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 26.53, exp saves 23.51 (sd 6.29), pull risk 0.046
- DET net: Daniil Tarasov (PROJECTED) exp shots 30.11, exp saves 25.32 (sd 7.17), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.370 | 0.470 | 49/55 | +0.063 | STANDARD |
| Lucas Raymond: 1+ assists | 0.318 | 0.410 | 42/60 | +0.065 | STANDARD |
| Lucas Raymond: 1+ points | 0.486 | 0.575 | 59/44 | +0.057 | STANDARD |
| Lucas Raymond: 2+ points | 0.145 | 0.220 | 23/79 | +0.053 | STANDARD |
| Sam Malinski: 1+ assists | 0.318 | 0.245 | 25/76 | +0.055 | STANDARD |
| Sam Malinski: 1+ points | 0.376 | 0.305 | 32/71 | +0.041 | STANDARD |

**PIT @ LAK** · priced 169/170 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- LAK net: Darcy Kuemper (PROBABLE) exp shots 27.28, exp saves 23.67 (sd 6.45), pull risk 0.059
- PIT net: Sergei Murashov (CONFIRMED) exp shots 27.6, exp saves 23.6 (sd 6.62), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Artemi Panarin: 2+ points | 0.238 | 0.350 | 37/67 | +0.077 | STANDARD |
| Artemi Panarin: 1+ assists | 0.418 | 0.525 | 53/48 | +0.085 | STANDARD |
| Ben Kindel: 1+ points | 0.364 | 0.465 | 47/54 | +0.078 | STANDARD |
| Ben Kindel: 1+ assists | 0.223 | 0.310 | 32/70 | +0.062 | STANDARD |
| Erik Karlsson: 1+ points | 0.487 | 0.570 | 58/44 | +0.056 | STANDARD |
| Erik Karlsson: 1+ assists | 0.408 | 0.490 | 50/52 | +0.055 | STANDARD |

**VAN @ EDM** · priced 165/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (CONFIRMED) exp shots 24.17, exp saves 21.32 (sd 5.93), pull risk 0.052
- VAN net: Leevi Merilainen (PROBABLE) exp shots 30.14, exp saves 25.04 (sd 7.29), pull risk 0.111

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.264 | 0.440 | 45/57 | +0.148 | STANDARD |
| Connor McDavid: 1+ assists | 0.629 | 0.755 | 77/26 | +0.098 | STANDARD |
| Connor McDavid: 2+ points | 0.513 | 0.630 | 65/39 | +0.080 | STANDARD |
| Vasily Podkolzin: 1+ assists | 0.416 | 0.300 | 31/71 | +0.091 | STANDARD |
| Leon Draisaitl: 2+ points | 0.433 | 0.545 | 56/47 | +0.080 | STANDARD |
| Leon Draisaitl: 2+ assists | 0.187 | 0.295 | 30/71 | +0.088 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
