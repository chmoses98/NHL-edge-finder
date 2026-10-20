# NHL slate 2026-10-19 — RESEARCH_ONLY

generated 2026-10-20T00:30:23Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 4 · simulated (not started): 1 · markets on board: 3108 · contracts joined: 252 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 227, 'NO_EDGE': 22, 'OK': 3}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 40, 'game_early_goal': 1, 'first_goal': 36, 'game_winner': 2, 'player_goals': 66, 'game_overtime': 1, 'player_points': 57, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ UTA | 2026-10-20T01:00:00Z | T-10m | 0.622 | 0.378 | 0.159 | 6.83 | 3.82 | 3.01 | 252 (25/227) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA2 | team_total | 0.891 | 0.905 | 0.902 | 91 | 10 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT19PITUTA-5 | game_total | 0.839 | 0.855 | 0.852 | 86 | 15 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT6 | team_total | 0.086 | 0.075 | 0.077 | 8 | 93 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT19PITUTA-UTA3 | game_spread | 0.276 | 0.295 | 0.291 | 30 | 71 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-2 | game_total | 0.991 | 0.990 | 0.990 |  | 1 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-3 | game_total | 0.978 | 0.975 | 0.976 | 98 | 3 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT5 | team_total | 0.197 | 0.185 | 0.187 | 19 | 82 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-9 | game_total | 0.258 | 0.245 | 0.248 | 25 | 76 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-10 | game_total | 0.133 | 0.120 | 0.122 | 13 | 89 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-7 | game_total | 0.550 | 0.565 | 0.562 | 57 | 44 |  | -0.007 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-PIT | game_winner | 0.378 | 0.365 | 0.368 | 37 | 64 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT19PITUTA-UTA | game_winner | 0.622 | 0.635 | 0.632 | 64 | 37 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT2 | game_spread | 0.201 | 0.195 | 0.196 | 20 | 81 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA4 | team_total | 0.543 | 0.555 | 0.553 | 56 | 45 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT2 | team_total | 0.789 | 0.800 | 0.798 | 81 | 21 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-PIT3 | game_spread | 0.114 | 0.115 | 0.115 | 12 | 89 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA3 | team_total | 0.738 | 0.750 | 0.748 | 76 | 26 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-4 | game_total | 0.906 | 0.910 | 0.909 | 92 | 10 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT3 | team_total | 0.577 | 0.585 | 0.583 | 59 | 42 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-6 | game_total | 0.659 | 0.665 | 0.664 | 67 | 34 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT19PITUTA-8 | game_total | 0.350 | 0.345 | 0.346 | 35 | 66 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA6 | team_total | 0.183 | 0.180 | 0.181 | 19 | 83 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-PIT4 | team_total | 0.362 | 0.365 | 0.364 | 37 | 64 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT19PITUTA-UTA5 | team_total | 0.343 | 0.350 | 0.349 | 36 | 66 |  | -0.019 | NO_EDGE |
| KXNHLSPREAD-26OCT19PITUTA-UTA2 | game_spread | 0.408 | 0.405 | 0.406 | 41 | 60 |  | -0.019 | NO_EDGE |
| KXNHL1P-26OCT19PITUTA-PIT | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT19PITUTA-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT19PITUTA-UTA | period_winner |  | 0.405 |  | 41 | 60 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT19PITUTA-PIT2 | period_spread |  | 0.075 |  | 9 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT19PITUTA-UTA2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT19PITUTA-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT19PITUTA-2 | period_total |  | 0.615 |  | 62 | 39 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT19PITUTA-3 | period_total |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT19PITUTA-PIT | period_winner |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT19PITUTA-TIE | period_winner |  | 0.270 |  | 29 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT19PITUTA-UTA | period_winner |  | 0.420 |  | 44 | 60 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT19PITUTA-PIT2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT19PITUTA-UTA2 | period_spread |  | 0.180 |  | 20 | 84 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT19PITUTA-1 | period_total |  | 0.925 |  | 94 | 9 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT19PITUTA-2 | period_total |  | 0.660 |  | 68 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT19PITUTA-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT19PITUTA-PIT | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT19PITUTA-TIE | period_winner |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT19PITUTA-UTA | period_winner |  | 0.455 |  | 47 | 56 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT19PITUTA-PIT2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT19PITUTA-UTA2 | period_spread |  | 0.230 |  | 25 | 79 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT19PITUTA-1 | period_total |  | 0.935 |  | 95 | 8 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT19PITUTA-2 | period_total |  | 0.700 |  | 72 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT19PITUTA-3 | period_total |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITAKUZMENKO62-1 | player_assists |  | 0.175 |  | 21 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITBKINDEL81-1 | player_assists |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITBRUST17-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITBRUST17-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITDCARLILE72-1 | player_assists |  | 0.135 |  | 16 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITEKARLSSON65-1 | player_assists |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITEKARLSSON65-2 | player_assists |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITEMALKIN71-1 | player_assists |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITEMALKIN71-2 | player_assists |  |  |  | 7 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITKKORCZAK6-1 | player_assists |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITKLETANG58-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITNROBERTSON14-1 | player_assists |  | 0.090 |  | 17 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITRRAKELL67-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITRRAKELL67-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITSCROSBY87-1 | player_assists |  | 0.480 |  | 49 | 53 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITSCROSBY87-2 | player_assists |  | 0.135 |  | 15 | 88 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITTNOVAK18-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITTNOVAK18-2 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-PITVKOIVUNEN41-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTAALEE72-1 | player_assists |  | 0.235 |  | 24 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTABHAYTON27-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTACKELLER9-1 | player_assists |  | 0.540 |  | 55 | 47 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTACKELLER9-2 | player_assists |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTACKELLER9-3 | player_assists |  |  |  | 6 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTADGUENTHER11-1 | player_assists |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTADGUENTHER11-2 | player_assists |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTAJMARINO6-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTAJMARINO6-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTAKYAMAMOTO56-1 | player_assists |  | 0.245 |  | 25 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTALCOOLEY92-1 | player_assists |  | 0.410 |  | 42 | 60 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT19PITUTA-UTALCOOLEY92-2 | player_assists |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ UTA | 0.622 | 0.585 | 0.159 | 0.207 | 6.83 | 6.69 | 1.001/1.042 | KXNHLSPREAD-26OCT19PITUTA-UTA2 -0.047 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Jack McBain: 1+ goals YES @ 11c · p 0.1691 (adj 0.1531) · $9.2 · thesis UTA:OFFENSE_4PLUS
- Connor Dewar: 1+ goals YES @ 11c · p 0.156 (adj 0.1432) · $6.94 · thesis PIT:OFFENSE_4PLUS
- Bryan Rust: 1+ goals YES @ 28c · p 0.3447 (adj 0.326) · $10.49 · thesis PIT:OFFENSE_4PLUS
- Lawson Crouse: 1+ goals YES @ 20c · p 0.2433 (adj 0.2312) · $6.15 · thesis UTA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ UTA** · priced 198/201 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- UTA net: Sebastian Cossa (CONFIRMED) exp shots 26.47, exp saves 22.95 (sd 6.37), pull risk 0.062
- PIT net: Arturs Silovs (CONFIRMED) exp shots 27.66, exp saves 23.55 (sd 6.68), pull risk 0.081

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Vincent Trocheck: 1+ assists | 0.228 | 0.340 | 35/67 | +0.086 | STANDARD |
| Nick Robertson: 1+ assists | 0.196 | 0.090 | 17/99 | +0.017 | STANDARD |
| Rickard Rakell: 1+ assists | 0.396 | 0.305 | 31/70 | +0.071 | STANDARD |
| Rickard Rakell: 1+ points | 0.589 | 0.500 | 51/51 | +0.062 | STANDARD |
| Vincent Trocheck: 2+ points | 0.092 | 0.175 | 18/83 | +0.068 | STANDARD |
| Arturs Silovs: 26+ saves | 0.383 | 0.465 | 47/54 | +0.059 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
