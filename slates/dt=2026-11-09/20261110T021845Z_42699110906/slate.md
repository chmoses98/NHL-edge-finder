# NHL slate 2026-11-09 — RESEARCH_ONLY

generated 2026-11-10T02:18:45Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2696 · contracts joined: 474 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 424, 'OK': 23, 'NO_EDGE': 27}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 78, 'game_early_goal': 2, 'first_goal': 70, 'game_winner': 4, 'player_goals': 121, 'game_overtime': 2, 'player_points': 99, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ VAN | 2026-11-10T02:30:00Z | T-10m | 0.515 | 0.484 | 0.176 | 6.51 | 3.30 | 3.21 | 231 (25/206) | CONFIRMED/CONFIRMED |
| NYI @ SJS | 2026-11-10T03:00:00Z | T-30m | 0.429 | 0.571 | 0.173 | 6.21 | 2.88 | 3.33 | 243 (25/218) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV09PHIVAN-PHI | game_winner | 0.484 | 0.565 | 0.549 | 57 | 44 | no | +0.058 | OK |
| KXNHLGAME-26NOV09PHIVAN-VAN | game_winner | 0.515 | 0.435 | 0.451 | 44 | 57 | yes | +0.058 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-PHI3 | game_spread | 0.167 | 0.235 | 0.220 | 24 | 77 | no | +0.051 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-PHI2 | game_spread | 0.278 | 0.345 | 0.331 | 35 | 66 | no | +0.047 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-VAN2 | game_spread | 0.300 | 0.245 | 0.255 | 25 | 76 | yes | +0.037 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN5 | team_total | 0.245 | 0.195 | 0.204 | 20 | 81 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN4 | team_total | 0.430 | 0.375 | 0.386 | 38 | 63 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN3 | team_total | 0.646 | 0.595 | 0.605 | 60 | 41 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-VAN3 | game_spread | 0.186 | 0.145 | 0.152 | 15 | 86 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN2 | team_total | 0.836 | 0.795 | 0.804 | 80 | 21 | yes | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4 | team_total | 0.412 | 0.455 | 0.446 | 46 | 55 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN6 | team_total | 0.115 | 0.075 | 0.082 | 9 | 94 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV09NYISJ-5 | game_total | 0.772 | 0.805 | 0.799 | 81 | 20 | no | +0.017 | OK |
| KXNHLTOTAL-26NOV09NYISJ-6 | game_total | 0.561 | 0.595 | 0.588 | 60 | 41 | no | +0.012 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-8 | game_total | 0.306 | 0.275 | 0.281 | 28 | 73 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI3 | team_total | 0.623 | 0.655 | 0.649 | 66 | 35 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-10 | game_total | 0.107 | 0.085 | 0.089 | 9 | 92 | yes | +0.011 | OK |
| KXNHLSPREAD-26NOV09NYISJ-SJ3 | game_spread | 0.131 | 0.155 | 0.150 | 16 | 85 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-9 | game_total | 0.221 | 0.195 | 0.200 | 20 | 81 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ2 | team_total | 0.771 | 0.795 | 0.790 | 80 | 21 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV09NYISJ-4 | game_total | 0.855 | 0.875 | 0.871 | 88 | 13 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ4 | team_total | 0.337 | 0.365 | 0.359 | 37 | 64 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV09NYISJ-7 | game_total | 0.449 | 0.475 | 0.470 | 48 | 53 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-3 | game_total | 0.970 | 0.965 | 0.966 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI2 | team_total | 0.822 | 0.845 | 0.841 | 86 | 17 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI5 | team_total | 0.230 | 0.245 | 0.242 | 25 | 76 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI4 | team_total | 0.436 | 0.460 | 0.455 | 47 | 55 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI3 | game_spread | 0.221 | 0.235 | 0.232 | 24 | 77 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ3 | team_total | 0.557 | 0.575 | 0.571 | 58 | 43 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ6 | team_total | 0.070 | 0.065 | 0.066 | 7 | 94 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-7 | game_total | 0.503 | 0.485 | 0.489 | 49 | 52 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI3 | team_total | 0.650 | 0.670 | 0.666 | 68 | 34 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-6 | game_total | 0.611 | 0.595 | 0.598 | 60 | 41 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-2 | game_total | 0.985 | 0.980 | 0.981 |  | 2 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-9 | game_total | 0.186 | 0.195 | 0.193 | 20 | 81 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ5 | team_total | 0.167 | 0.180 | 0.177 | 19 | 83 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-3 | game_total | 0.965 | 0.975 | 0.973 | 99 | 4 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI6 | team_total | 0.118 | 0.110 | 0.112 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-2 | game_total | 0.988 | 0.990 | 0.990 |  | 2 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-10 | game_total | 0.085 | 0.085 | 0.085 | 9 | 92 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-4 | game_total | 0.877 | 0.875 | 0.875 | 88 | 13 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI2 | team_total | 0.842 | 0.855 | 0.852 | 87 | 16 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-SJ2 | game_spread | 0.230 | 0.235 | 0.234 | 24 | 77 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI5 | team_total | 0.249 | 0.245 | 0.246 | 25 | 76 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-5 | game_total | 0.803 | 0.805 | 0.805 | 81 | 20 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-NYI | game_winner | 0.571 | 0.565 | 0.566 | 57 | 44 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-8 | game_total | 0.262 | 0.265 | 0.264 | 27 | 74 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-SJ | game_winner | 0.429 | 0.425 | 0.426 | 43 | 58 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI2 | game_spread | 0.347 | 0.345 | 0.345 | 35 | 66 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI6 | team_total | 0.105 | 0.110 | 0.109 | 13 | 91 |  | -0.020 | NO_EDGE |
| KXNHL1P-26NOV09PHIVAN-PHI | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09PHIVAN-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09PHIVAN-VAN | period_winner |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09PHIVAN-PHI2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09PHIVAN-VAN2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09PHIVAN-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09PHIVAN-2 | period_total |  | 0.575 |  | 58 | 43 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09PHIVAN-3 | period_total |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09PHIVAN-PHI | period_winner |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09PHIVAN-TIE | period_winner |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09PHIVAN-VAN | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV09PHIVAN-PHI2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV09PHIVAN-VAN2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09PHIVAN-1 | period_total |  | 0.900 |  | 91 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09PHIVAN-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09PHIVAN-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09PHIVAN-PHI | period_winner |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09PHIVAN-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09PHIVAN-VAN | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV09PHIVAN-PHI2 | period_spread |  | 0.175 |  | 20 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV09PHIVAN-VAN2 | period_spread |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09PHIVAN-1 | period_total |  | 0.910 |  | 92 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09PHIVAN-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09PHIVAN-3 | period_total |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHICDVORAK22-1 | player_assists |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHICDVORAK22-2 | player_assists |  | 0.040 |  | 7 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIDBARKEY86-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIJDRYSDALE9-1 | player_assists |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIJDRYSDALE9-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIMMICHKOV39-1 | player_assists |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ VAN | 0.515 | 0.531 | 0.176 | 0.222 | 6.51 | 6.20 | 1.034/0.990 | KXNHLTOTAL-26NOV09PHIVAN-6 -0.054 |
| NYI @ SJS | 0.429 | 0.499 | 0.173 | 0.217 | 6.21 | 6.32 | 1.039/0.952 | KXNHLGAME-26NOV09NYISJ-NYI -0.071 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1698 (adj 0.1524) · $8.49 · thesis VAN:OFFENSE_4PLUS
- Porter Martone: 1+ goals NO @ 74c · p 0.8162 (adj 0.7959) · $17.59 · thesis PHI:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2263 (adj 0.211) · $8.42 · thesis VAN:OFFENSE_4PLUS
- Matvei Michkov: 1+ goals NO @ 70c · p 0.7447 (adj 0.7323) · $12.41 · thesis PHI:SUPPRESSED
- Michael Misa: 2+ goals YES @ 1c · p 0.0294 (adj 0.027) · $3.42 · thesis SJS:OFFENSE_4PLUS
- Kiefer Sherwood: First Goalscorer YES @ 2c · p 0.0365 (adj 0.0333) · $2.75 · thesis SJS:SCORES_FIRST
- Sam Dickinson: 1+ goals YES @ 5c · p 0.0729 (adj 0.0672) · $3.49 · thesis SJS:OFFENSE_4PLUS
- Mason Marchment: First Goalscorer YES @ 3c · p 0.0441 (adj 0.0421) · $2.56 · thesis SJS:SCORES_FIRST

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ VAN** · priced 169/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (CONFIRMED) exp shots 26.87, exp saves 23.32 (sd 6.37), pull risk 0.058
- PHI net: Joseph Woll (CONFIRMED) exp shots 25.06, exp saves 21.59 (sd 6.12), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ points | 0.426 | 0.555 | 56/45 | +0.107 | STANDARD |
| Trevor Zegras: 1+ points | 0.489 | 0.595 | 60/41 | +0.084 | STANDARD |
| Travis Konecny: 1+ assists | 0.269 | 0.375 | 38/63 | +0.084 | STANDARD |
| Porter Martone: 1+ points | 0.395 | 0.480 | 49/53 | +0.057 | STANDARD |
| Porter Martone: 1+ goals | 0.184 | 0.265 | 27/74 | +0.063 | STANDARD |
| Travis Konecny: 2+ points | 0.109 | 0.185 | 20/83 | +0.052 | STANDARD |

**NYI @ SJS** · priced 189/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.92, exp saves 24.18 (sd 6.65), pull risk 0.063
- NYI net: Ilya Sorokin (PROBABLE) exp shots 27.14, exp saves 23.58 (sd 6.57), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Macklin Celebrini: 1+ assists | 0.441 | 0.550 | 56/46 | +0.082 | STANDARD |
| Sam Dickinson: 1+ points | 0.290 | 0.190 | 20/82 | +0.079 | STANDARD |
| Ivar Stenberg: 1+ points | 0.376 | 0.470 | 48/54 | +0.067 | STANDARD |
| Macklin Celebrini: 2+ points | 0.286 | 0.380 | 39/63 | +0.068 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.226 | 0.305 | 31/70 | +0.059 | STANDARD |
| Kiefer Sherwood: 1+ points | 0.416 | 0.345 | 35/66 | +0.050 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
