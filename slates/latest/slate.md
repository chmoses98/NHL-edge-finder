# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-27T00:05:03Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 2 · markets on board: 2952 · contracts joined: 538 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 488, 'OK': 32, 'NO_EDGE': 18}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 100, 'game_early_goal': 2, 'first_goal': 76, 'game_winner': 4, 'player_goals': 129, 'game_overtime': 2, 'player_points': 127, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ CGY | 2026-10-27T00:30:00Z | T-10m | 0.555 | 0.445 | 0.173 | 6.33 | 3.33 | 3.00 | 265 (25/240) | CONFIRMED/PROBABLE |
| DET @ EDM | 2026-10-27T01:30:00Z | T-60m | 0.607 | 0.393 | 0.166 | 6.55 | 3.63 | 2.93 | 273 (25/248) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.361 | 0.490 | 0.464 | 50 | 52 | no | +0.101 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.445 | 0.555 | 0.533 | 56 | 45 | no | +0.088 | OK |
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.555 | 0.445 | 0.467 | 45 | 56 | yes | +0.088 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.579 | 0.690 | 0.669 | 70 | 32 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.246 | 0.345 | 0.324 | 35 | 66 | no | +0.079 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.142 | 0.235 | 0.214 | 24 | 77 | no | +0.075 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.191 | 0.285 | 0.264 | 29 | 72 | no | +0.074 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.332 | 0.245 | 0.261 | 25 | 76 | yes | +0.069 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.792 | 0.870 | 0.857 | 88 | 14 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.206 | 0.155 | 0.164 | 16 | 85 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.784 | 0.840 | 0.830 | 85 | 17 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.580 | 0.635 | 0.624 | 64 | 37 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.469 | 0.525 | 0.514 | 53 | 48 | no | +0.033 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.811 | 0.855 | 0.847 | 86 | 15 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.866 | 0.905 | 0.898 | 91 | 10 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.505 | 0.555 | 0.545 | 56 | 45 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.086 | 0.135 | 0.124 | 15 | 88 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.279 | 0.325 | 0.316 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.441 | 0.395 | 0.404 | 40 | 61 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.654 | 0.615 | 0.623 | 62 | 39 | yes | +0.017 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.618 | 0.655 | 0.648 | 66 | 35 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.507 | 0.545 | 0.537 | 55 | 46 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.302 | 0.340 | 0.332 | 35 | 67 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.884 | 0.905 | 0.901 | 91 | 10 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.199 | 0.225 | 0.220 | 23 | 78 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.249 | 0.220 | 0.226 | 23 | 79 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.259 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.389 | 0.415 | 0.410 | 42 | 59 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.713 | 0.740 | 0.735 | 75 | 27 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.990 | 0.990 |  | 1 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.967 | 0.975 | 0.974 | 98 | 3 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.116 | 0.095 | 0.099 | 11 | 92 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.839 | 0.820 | 0.824 | 83 | 19 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.095 | 0.105 | 0.103 | 11 | 90 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.345 | 0.365 | 0.361 | 37 | 64 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.116 | 0.125 | 0.123 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.112 | 0.105 | 0.106 | 11 | 90 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.973 | 0.975 | 0.975 | 98 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.225 | 0.240 | 0.237 | 25 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.313 | 0.325 | 0.323 | 33 | 68 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.562 | 0.575 | 0.572 | 58 | 43 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.607 | 0.615 | 0.613 | 62 | 39 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.393 | 0.385 | 0.387 | 39 | 62 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.156 | 0.165 | 0.163 | 18 | 85 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.205 | 0.205 | 0.205 | 21 | 80 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.077 | 0.075 | 0.075 | 9 | 94 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.180 | 0.185 | 0.184 | 20 | 83 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT26TORCGY-TOR | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26TORCGY-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26TORCGY-CGY | period_winner |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26TORCGY-TOR2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26TORCGY-CGY2 | period_spread |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26TORCGY-3 | period_total |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26TORCGY-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26TORCGY-1 | period_total |  | 0.850 |  | 86 | 16 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26TORCGY-TOR | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26TORCGY-TIE | period_winner |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26TORCGY-CGY | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT26TORCGY-TOR2 | period_spread |  | 0.140 |  | 16 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT26TORCGY-CGY2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26TORCGY-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26TORCGY-2 | period_total |  | 0.655 |  | 66 | 35 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26TORCGY-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26TORCGY-TOR | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26TORCGY-TIE | period_winner |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26TORCGY-CGY | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT26TORCGY-TOR2 | period_spread |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT26TORCGY-CGY2 | period_spread |  | 0.130 |  | 15 | 89 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26TORCGY-3 | period_total |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26TORCGY-2 | period_total |  | 0.670 |  | 68 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26TORCGY-1 | period_total |  | 0.915 |  | 94 | 11 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-TORZMACEWEN19-1 | player_assists |  | 0.055 |  | 10 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-TORVLETTIERI-1 | player_assists |  | 0.145 |  | 18 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-TORTSTECHER28-1 | player_assists |  | 0.085 |  | 12 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-TOROEKMANLARSSON95-1 | player_assists |  | 0.110 |  | 21 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-TORDMERMIS36-1 | player_assists |  | 0.080 |  | 15 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26TORCGY-TORBDUHAIME24-1 | player_assists |  | 0.055 |  | 10 | 99 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TOR @ CGY | 0.555 | 0.506 | 0.173 | 0.222 | 6.33 | 6.40 | 0.978/0.983 | KXNHLGAME-26OCT26TORCGY-CGY -0.049 |
| DET @ EDM | 0.607 | 0.645 | 0.166 | 0.207 | 6.55 | 6.65 | 1.022/1.000 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Jonathan Castagna: 1+ goals YES @ 12c · p 0.1664 (adj 0.1523) · $6.5 · thesis CGY:OFFENSE_4PLUS
- Teddy Blueger: 1+ goals YES @ 12c · p 0.1598 (adj 0.1449) · $4.7 · thesis TOR:OFFENSE_4PLUS
- Auston Matthews: 1+ assists NO @ 54c · p 0.6274 (adj 0.5812) · $12.84 · thesis TOR:SUPPRESSED
- Kirill Marchenko: 1+ goals NO @ 67c · p 0.7123 (adj 0.7005) · $9.67 · thesis TOR:SUPPRESSED
- Vasily Podkolzin: 1+ assists YES @ 30c · p 0.3908 (adj 0.3429) · $10.91 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 2+ assists NO @ 62c · p 0.7528 (adj 0.6632) · $20.0 · thesis EDM:SUPPRESSED
- Connor McDavid: 1+ assists NO @ 30c · p 0.376 (adj 0.3355) · $5.48 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.2997 (adj 0.2885) · $7.72 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**TOR @ CGY** · priced 202/214 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (CONFIRMED) exp shots 28.89, exp saves 24.88 (sd 6.83), pull risk 0.065
- TOR net: Sergei Bobrovsky (PROBABLE) exp shots 31.56, exp saves 27.24 (sd 7.27), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jonathan Castagna: 1+ points | 0.317 | 0.130 | 25/99 | +0.054 | PRIOR_HEAVY |
| Brandon Duhaime: 1+ points | 0.271 | 0.100 | 19/99 | +0.070 | STANDARD |
| Adam Klapka: 1+ assists | 0.254 | 0.095 | 18/99 | +0.064 | STANDARD |
| Troy Stecher: 1+ assists | 0.231 | 0.085 | 12/95 | +0.103 | STANDARD |
| Gavin McKenna: 1+ points | 0.356 | 0.495 | 51/52 | +0.106 | STANDARD |
| Yan Kuznetsov: 1+ points | 0.231 | 0.095 | 18/99 | +0.040 | STANDARD |

**DET @ EDM** · priced 207/222 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.49, exp saves 24.09 (sd 6.52), pull risk 0.053
- DET net: Michal Postava (CONFIRMED) exp shots 28.12, exp saves 23.68 (sd 6.88), pull risk 0.092

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ assists | 0.247 | 0.385 | 39/62 | +0.116 | STANDARD |
| Leon Draisaitl: 2+ points | 0.363 | 0.495 | 50/51 | +0.109 | STANDARD |
| Connor McDavid: 2+ points | 0.469 | 0.600 | 61/41 | +0.104 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.293 | 0.405 | 41/60 | +0.090 | STANDARD |
| Albert Johansson: 1+ points | 0.215 | 0.105 | 19/98 | +0.014 | STANDARD |
| Ben Chiarot: 1+ points | 0.263 | 0.155 | 19/88 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
