# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-27T00:56:18Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 1 · markets on board: 2959 · contracts joined: 273 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 248, 'NO_EDGE': 15, 'OK': 10}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 52, 'game_early_goal': 1, 'first_goal': 39, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 65, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ EDM | 2026-10-27T01:30:00Z | T-30m | 0.607 | 0.393 | 0.166 | 6.55 | 3.63 | 2.93 | 273 (25/248) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.811 | 0.850 | 0.843 | 86 | 16 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.505 | 0.545 | 0.537 | 55 | 46 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.618 | 0.655 | 0.648 | 66 | 35 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.713 | 0.750 | 0.743 | 76 | 26 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.302 | 0.335 | 0.328 | 34 | 67 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.872 | 0.900 | 0.895 | 91 | 11 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.884 | 0.905 | 0.901 | 91 | 10 | no | +0.009 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.259 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.389 | 0.415 | 0.410 | 42 | 59 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.988 | 0.990 | 0.990 |  | 1 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.780 | 0.795 | 0.792 | 80 | 21 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.116 | 0.125 | 0.123 | 13 | 88 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.507 | 0.525 | 0.521 | 53 | 48 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.973 | 0.980 | 0.979 | 99 | 3 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.225 | 0.235 | 0.233 | 24 | 77 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.077 | 0.070 | 0.071 | 8 | 94 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.313 | 0.325 | 0.323 | 33 | 68 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.562 | 0.575 | 0.572 | 58 | 43 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.112 | 0.115 | 0.114 | 12 | 89 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.345 | 0.355 | 0.353 | 36 | 65 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.393 | 0.385 | 0.387 | 39 | 62 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.607 | 0.615 | 0.613 | 62 | 39 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.156 | 0.160 | 0.159 | 17 | 85 |  | -0.015 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.205 | 0.205 | 0.205 | 21 | 80 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.180 | 0.180 | 0.180 | 19 | 83 |  | -0.020 | NO_EDGE |
| KXNHL1P-26OCT26DETEDM-DET | period_winner |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26DETEDM-EDM | period_winner |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26DETEDM-TIE | period_winner |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26DETEDM-DET2 | period_spread |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26DETEDM-EDM2 | period_spread |  | 0.150 |  | 17 | 87 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26DETEDM-1 | period_total |  | 0.865 |  | 87 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26DETEDM-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT26DETEDM-3 | period_total |  | 0.310 |  | 32 | 70 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26DETEDM-DET | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26DETEDM-EDM | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT26DETEDM-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT26DETEDM-DET2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT26DETEDM-EDM2 | period_spread |  | 0.175 |  | 19 | 84 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26DETEDM-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26DETEDM-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT26DETEDM-3 | period_total |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26DETEDM-DET | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26DETEDM-EDM | period_winner |  | 0.465 |  | 47 | 54 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT26DETEDM-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT26DETEDM-DET2 | period_spread |  | 0.110 |  | 13 | 91 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT26DETEDM-EDM2 | period_spread |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26DETEDM-1 | period_total |  | 0.920 |  | 94 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26DETEDM-2 | period_total |  | 0.710 |  | 74 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT26DETEDM-3 | period_total |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETACOPP18-1 | player_assists |  | 0.235 |  | 25 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETADEBRINCAT93-1 | player_assists |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETADEBRINCAT93-2 | player_assists |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETAENGLUND-1 | player_assists |  | 0.075 |  | 14 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETAJOHANSSON20-1 | player_assists |  | 0.080 |  | 14 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETAJOHANSSON42-1 | player_assists |  | 0.085 |  | 15 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETBCHIAROT8-1 | player_assists |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETDLARKIN71-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETDLARKIN71-2 | player_assists |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETEFINNIE58-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETEFINNIE58-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETJCOMPHER37-1 | player_assists |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETJFAULK72-1 | player_assists |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETJFAULK72-2 | player_assists |  | 0.040 |  | 6 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETKKOLESAR55-1 | player_assists |  | 0.070 |  | 12 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETLRAYMOND23-1 | player_assists |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETLRAYMOND23-2 | player_assists |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETMBRANDSEGGNYGRD28-1 | player_assists |  | 0.235 |  | 26 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETMRASMUSSEN27-1 | player_assists |  | 0.180 |  | 21 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETMSEIDER53-1 | player_assists |  | 0.420 |  | 43 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETMSEIDER53-2 | player_assists |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETNDANIELSON29-1 | player_assists |  | 0.095 |  | 17 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETVARVIDSSON33-1 | player_assists |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETVARVIDSSON33-2 | player_assists |  | 0.065 |  | 9 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-DETWWALLINDER54-1 | player_assists |  | 0.195 |  | 21 | 82 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-EDMAFORMENTON26-1 | player_assists |  | 0.165 |  | 19 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-EDMCDACH34-1 | player_assists |  | 0.105 |  | 19 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-1 | player_assists |  | 0.705 |  | 71 | 30 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-2 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-EDMCMCDAVID97-3 | player_assists |  | 0.130 |  | 15 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT26DETEDM-EDMCMURPHY5-1 | player_assists |  | 0.115 |  | 21 | 98 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| DET @ EDM | 0.607 | 0.645 | 0.166 | 0.207 | 6.55 | 6.65 | 1.022/1.000 | KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 +0.039 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Vasily Podkolzin: 1+ assists YES @ 30c · p 0.3908 (adj 0.3429) · $10.33 · thesis EDM:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 30c · p 0.376 (adj 0.3355) · $9.51 · thesis EDM:SUPPRESSED
- Vasily Podkolzin: 1+ goals YES @ 26c · p 0.2997 (adj 0.2885) · $6.69 · thesis EDM:OFFENSE_4PLUS
- Alex Formenton: 1+ goals YES @ 16c · p 0.1898 (adj 0.1811) · $3.39 · thesis EDM:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**DET @ EDM** · priced 207/222 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (CONFIRMED) exp shots 27.49, exp saves 24.09 (sd 6.52), pull risk 0.053
- DET net: Michal Postava (CONFIRMED) exp shots 28.12, exp saves 23.68 (sd 6.88), pull risk 0.092

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Connor McDavid: 2+ points | 0.469 | 0.600 | 61/41 | +0.104 | STANDARD |
| Connor McDavid: 2+ assists | 0.247 | 0.375 | 39/64 | +0.097 | STANDARD |
| Leon Draisaitl: 2+ points | 0.363 | 0.490 | 50/52 | +0.099 | STANDARD |
| Ben Chiarot: 1+ points | 0.263 | 0.140 | 17/89 | +0.083 | STANDARD |
| Ryan Nugent-Hopkins: 1+ assists | 0.293 | 0.410 | 42/60 | +0.090 | STANDARD |
| Ben Chiarot: 1+ assists | 0.221 | 0.115 | 13/90 | +0.083 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
