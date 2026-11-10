# NHL slate 2026-11-09 — RESEARCH_ONLY

generated 2026-11-10T01:00:06Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2498 · contracts joined: 466 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 416, 'OK': 26, 'NO_EDGE': 24}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 77, 'game_early_goal': 2, 'first_goal': 68, 'game_winner': 4, 'player_goals': 118, 'game_overtime': 2, 'player_points': 97, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ VAN | 2026-11-10T02:30:00Z | T-60m | 0.520 | 0.480 | 0.175 | 6.44 | 3.28 | 3.16 | 223 (25/198) | PROBABLE/PROBABLE |
| NYI @ SJS | 2026-11-10T03:00:00Z | T-90m | 0.429 | 0.571 | 0.173 | 6.21 | 2.88 | 3.33 | 243 (25/218) | CONFIRMED/PROBABLE |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV09PHIVAN-PHI | game_winner | 0.480 | 0.555 | 0.540 | 56 | 45 | no | +0.053 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-PHI3 | game_spread | 0.165 | 0.235 | 0.220 | 24 | 77 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-PHI2 | game_spread | 0.273 | 0.345 | 0.330 | 35 | 66 | no | +0.052 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-VAN2 | game_spread | 0.309 | 0.245 | 0.257 | 25 | 76 | yes | +0.046 | OK |
| KXNHLGAME-26NOV09PHIVAN-VAN | game_winner | 0.520 | 0.455 | 0.468 | 46 | 55 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN6 | team_total | 0.116 | 0.070 | 0.078 | 8 | 94 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN5 | team_total | 0.240 | 0.195 | 0.204 | 20 | 81 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV09PHIVAN-VAN3 | game_spread | 0.187 | 0.145 | 0.153 | 15 | 86 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN3 | team_total | 0.644 | 0.595 | 0.605 | 60 | 41 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN4 | team_total | 0.423 | 0.375 | 0.384 | 38 | 63 | yes | +0.027 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI4 | team_total | 0.401 | 0.445 | 0.436 | 45 | 56 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI3 | team_total | 0.614 | 0.655 | 0.647 | 66 | 35 | no | +0.020 | OK |
| KXNHLTOTAL-26NOV09NYISJ-5 | game_total | 0.772 | 0.805 | 0.799 | 81 | 20 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI2 | team_total | 0.815 | 0.850 | 0.843 | 86 | 16 | no | +0.016 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-8 | game_total | 0.298 | 0.265 | 0.271 | 27 | 74 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-VAN2 | team_total | 0.834 | 0.800 | 0.807 | 81 | 21 | yes | +0.013 | OK |
| KXNHLTOTAL-26NOV09NYISJ-6 | game_total | 0.561 | 0.595 | 0.588 | 60 | 41 | no | +0.012 | OK |
| KXNHLSPREAD-26NOV09NYISJ-SJ3 | game_spread | 0.131 | 0.155 | 0.150 | 16 | 85 | no | +0.011 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-10 | game_total | 0.104 | 0.080 | 0.084 | 9 | 93 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI5 | team_total | 0.220 | 0.245 | 0.240 | 25 | 76 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ2 | team_total | 0.771 | 0.800 | 0.794 | 81 | 21 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV09NYISJ-4 | game_total | 0.855 | 0.875 | 0.871 | 88 | 13 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ4 | team_total | 0.337 | 0.365 | 0.359 | 37 | 64 | no | +0.007 | OK |
| KXNHLTOTAL-26NOV09NYISJ-7 | game_total | 0.449 | 0.475 | 0.470 | 48 | 53 | no | +0.004 | OK |
| KXNHLTOTAL-26NOV09NYISJ-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTOTAL-26NOV09PHIVAN-9 | game_total | 0.212 | 0.195 | 0.198 | 20 | 81 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI4 | team_total | 0.436 | 0.455 | 0.451 | 46 | 55 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ3 | team_total | 0.557 | 0.575 | 0.571 | 58 | 43 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ6 | team_total | 0.070 | 0.075 | 0.074 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI3 | team_total | 0.650 | 0.670 | 0.666 | 68 | 34 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-2 | game_total | 0.985 | 0.990 | 0.989 |  | 2 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-SJ5 | team_total | 0.167 | 0.180 | 0.177 | 19 | 83 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-7 | game_total | 0.489 | 0.475 | 0.478 | 48 | 53 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-6 | game_total | 0.598 | 0.585 | 0.588 | 59 | 42 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI6 | team_total | 0.118 | 0.110 | 0.112 | 12 | 90 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-10 | game_total | 0.085 | 0.085 | 0.085 | 9 | 92 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-3 | game_total | 0.971 | 0.970 | 0.970 | 98 | 4 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-4 | game_total | 0.873 | 0.875 | 0.875 | 88 | 13 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI2 | team_total | 0.842 | 0.855 | 0.852 | 87 | 16 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-SJ2 | game_spread | 0.230 | 0.235 | 0.234 | 24 | 77 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI3 | game_spread | 0.221 | 0.225 | 0.224 | 23 | 78 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-NYI | game_winner | 0.571 | 0.565 | 0.566 | 57 | 44 |  | -0.016 | NO_EDGE |
| KXNHLGAME-26NOV09NYISJ-SJ | game_winner | 0.429 | 0.435 | 0.434 | 44 | 57 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-8 | game_total | 0.262 | 0.265 | 0.264 | 27 | 74 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09PHIVAN-PHI6 | team_total | 0.101 | 0.100 | 0.100 | 11 | 91 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26NOV09NYISJ-9 | game_total | 0.186 | 0.190 | 0.189 | 20 | 82 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26NOV09NYISJ-NYI2 | game_spread | 0.347 | 0.345 | 0.345 | 35 | 66 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-5 | game_total | 0.798 | 0.800 | 0.800 | 81 | 21 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26NOV09PHIVAN-2 | game_total | 0.988 | 0.990 | 0.990 |  | 3 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26NOV09NYISJ-NYI5 | team_total | 0.249 | 0.250 | 0.250 | 26 | 76 |  | -0.022 | NO_EDGE |
| KXNHL1P-26NOV09PHIVAN-PHI | period_winner |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09PHIVAN-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26NOV09PHIVAN-VAN | period_winner |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09PHIVAN-PHI2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26NOV09PHIVAN-VAN2 | period_spread |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09PHIVAN-1 | period_total |  | 0.840 |  | 85 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09PHIVAN-2 | period_total |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26NOV09PHIVAN-3 | period_total |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09PHIVAN-PHI | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09PHIVAN-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26NOV09PHIVAN-VAN | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV09PHIVAN-PHI2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26NOV09PHIVAN-VAN2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09PHIVAN-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09PHIVAN-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26NOV09PHIVAN-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09PHIVAN-PHI | period_winner |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09PHIVAN-TIE | period_winner |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26NOV09PHIVAN-VAN | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV09PHIVAN-PHI2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26NOV09PHIVAN-VAN2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09PHIVAN-1 | period_total |  | 0.910 |  | 92 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09PHIVAN-2 | period_total |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26NOV09PHIVAN-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHICDVORAK22-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHICDVORAK22-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIDBARKEY86-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIJDRYSDALE9-1 | player_assists |  | 0.365 |  | 37 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIJDRYSDALE9-2 | player_assists |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26NOV09PHIVAN-PHIMMICHKOV39-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ VAN | 0.520 | 0.530 | 0.175 | 0.214 | 6.44 | 6.18 | 1.030/0.991 | KXNHLTOTAL-26NOV09PHIVAN-6 -0.046 |
| NYI @ SJS | 0.429 | 0.499 | 0.173 | 0.217 | 6.21 | 6.32 | 1.039/0.952 | KXNHLGAME-26NOV09NYISJ-NYI -0.071 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1737 (adj 0.1565) · $9.8 · thesis VAN:OFFENSE_4PLUS
- Porter Martone: 1+ goals NO @ 74c · p 0.8154 (adj 0.7953) · $20.0 · thesis PHI:SUPPRESSED
- Linus Karlsson: 1+ goals YES @ 17c · p 0.2278 (adj 0.2121) · $9.17 · thesis VAN:OFFENSE_4PLUS
- Arshdeep Bains: 1+ goals YES @ 9c · p 0.1259 (adj 0.1157) · $4.84 · thesis VAN:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2143 (adj 0.202) · $6.25 · thesis SJS:OFFENSE_4PLUS
- Ivar Stenberg: 1+ assists NO @ 70c · p 0.774 (adj 0.7345) · $19.37 · thesis SJS:SUPPRESSED
- Michael Misa: 1+ goals YES @ 19c · p 0.2291 (adj 0.2181) · $5.05 · thesis SJS:OFFENSE_4PLUS
- Matthew Schaefer: 1+ goals NO @ 76c · p 0.8022 (adj 0.7904) · $19.33 · thesis NYI:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ VAN** · priced 163/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROBABLE) exp shots 26.87, exp saves 23.33 (sd 6.44), pull risk 0.059
- PHI net: Joseph Woll (PROBABLE) exp shots 25.06, exp saves 21.55 (sd 6.15), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Travis Konecny: 1+ points | 0.435 | 0.555 | 56/45 | +0.097 | STANDARD |
| Travis Konecny: 1+ assists | 0.271 | 0.370 | 38/64 | +0.073 | STANDARD |
| Trevor Zegras: 1+ points | 0.494 | 0.590 | 60/42 | +0.069 | STANDARD |
| Porter Martone: 1+ goals | 0.185 | 0.265 | 27/74 | +0.062 | STANDARD |
| Porter Martone: 1+ points | 0.399 | 0.475 | 49/54 | +0.044 | STANDARD |
| Travis Konecny: 2+ points | 0.112 | 0.185 | 20/83 | +0.048 | STANDARD |

**NYI @ SJS** · priced 189/192 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 27.92, exp saves 24.18 (sd 6.65), pull risk 0.063
- NYI net: Ilya Sorokin (PROBABLE) exp shots 27.14, exp saves 23.58 (sd 6.57), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sam Dickinson: 1+ points | 0.290 | 0.165 | 21/88 | +0.069 | STANDARD |
| Michael Kesselring: 1+ assists | 0.203 | 0.085 | 16/99 | +0.033 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.441 | 0.535 | 55/48 | +0.062 | STANDARD |
| Ivar Stenberg: 1+ points | 0.376 | 0.470 | 48/54 | +0.067 | STANDARD |
| Macklin Celebrini: 2+ points | 0.286 | 0.380 | 39/63 | +0.068 | STANDARD |
| Ivar Stenberg: 1+ assists | 0.226 | 0.305 | 31/70 | +0.059 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
