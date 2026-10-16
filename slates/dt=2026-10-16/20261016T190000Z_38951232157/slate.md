# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-16T19:00:00Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2818 · contracts joined: 445 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 395, 'NO_EDGE': 41, 'OK': 9}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 63, 'game_early_goal': 2, 'first_goal': 73, 'game_winner': 4, 'player_goals': 119, 'game_overtime': 2, 'player_points': 84, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 2026-10-17T01:00:00Z | T-3h | 0.654 | 0.346 | 0.161 | 6.74 | 3.88 | 2.87 | 228 (25/203) | CONFIRMED/CONFIRMED |
| BOS @ ANA | 2026-10-17T02:00:00Z | T-6h | 0.484 | 0.516 | 0.177 | 6.33 | 3.12 | 3.21 | 217 (25/192) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.788 | 0.820 | 0.814 | 83 | 19 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT6 | team_total | 0.074 | 0.055 | 0.058 | 6 | 95 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.866 | 0.885 | 0.881 | 89 | 12 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.387 | 0.420 | 0.413 | 43 | 59 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.164 | 0.185 | 0.181 | 19 | 82 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT16PITCOL-5 | game_total | 0.825 | 0.845 | 0.841 | 85 | 16 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT16PITCOL-10 | game_total | 0.128 | 0.115 | 0.118 | 12 | 89 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT16PITCOL-2 | game_total | 0.991 | 0.985 | 0.986 | 99 | 2 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT5 | team_total | 0.170 | 0.155 | 0.158 | 16 | 85 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT16PITCOL-4 | game_total | 0.895 | 0.910 | 0.907 | 92 | 10 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL2 | team_total | 0.896 | 0.905 | 0.903 | 91 | 10 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.585 | 0.605 | 0.601 | 61 | 40 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-9 | game_total | 0.251 | 0.235 | 0.238 | 24 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.606 | 0.630 | 0.625 | 64 | 38 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.212 | 0.230 | 0.226 | 24 | 78 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.102 | 0.095 | 0.096 | 10 | 91 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.299 | 0.285 | 0.288 | 29 | 72 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.815 | 0.825 | 0.823 | 83 | 18 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.967 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.468 | 0.485 | 0.482 | 49 | 52 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL6 | team_total | 0.194 | 0.180 | 0.183 | 19 | 83 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL3 | game_spread | 0.302 | 0.315 | 0.312 | 32 | 69 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.179 | 0.190 | 0.188 | 20 | 82 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.096 | 0.095 | 0.095 | 10 | 91 |  | -0.010 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.516 | 0.505 | 0.507 | 51 | 50 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL4 | team_total | 0.555 | 0.570 | 0.567 | 58 | 44 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.822 | 0.835 | 0.832 | 85 | 18 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.230 | 0.220 | 0.222 | 23 | 79 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.094 | 0.090 | 0.091 | 10 | 92 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT2 | game_spread | 0.177 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-PIT3 | game_spread | 0.098 | 0.100 | 0.100 | 11 | 91 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-8 | game_total | 0.341 | 0.330 | 0.332 | 34 | 68 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT4 | team_total | 0.331 | 0.320 | 0.322 | 33 | 69 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT3 | team_total | 0.547 | 0.555 | 0.553 | 56 | 45 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.197 | 0.200 | 0.199 | 21 | 81 |  | -0.017 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-7 | game_total | 0.540 | 0.535 | 0.536 | 54 | 47 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.274 | 0.275 | 0.275 | 28 | 73 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.276 | 0.275 | 0.275 | 28 | 73 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT16PITCOL-COL2 | game_spread | 0.438 | 0.435 | 0.436 | 44 | 57 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-PIT | game_winner | 0.346 | 0.345 | 0.345 | 35 | 66 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT16PITCOL-COL | game_winner | 0.654 | 0.655 | 0.655 | 66 | 35 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-PIT2 | team_total | 0.768 | 0.770 | 0.770 | 78 | 24 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.484 | 0.485 | 0.485 | 49 | 52 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.625 | 0.630 | 0.629 | 64 | 38 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL3 | team_total | 0.751 | 0.750 | 0.750 | 76 | 26 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16PITCOL-COL5 | team_total | 0.356 | 0.360 | 0.359 | 37 | 65 |  | -0.022 | NO_EDGE |
| KXNHLTOTAL-26OCT16PITCOL-6 | game_total | 0.647 | 0.650 | 0.649 | 66 | 36 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.417 | 0.415 | 0.415 | 43 | 60 |  | -0.030 | NO_EDGE |
| KXNHL1P-26OCT16PITCOL-COL | period_winner |  | 0.415 |  | 43 | 60 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-PIT | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16PITCOL-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.170 |  | 18 | 84 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.855 |  | 86 | 15 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.595 |  | 60 | 41 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-COL | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-PIT | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16PITCOL-TIE | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.900 |  | 91 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.655 |  | 67 | 36 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-COL | period_winner |  | 0.465 |  | 48 | 55 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-PIT | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16PITCOL-TIE | period_winner |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-COL2 | period_spread |  | 0.245 |  | 26 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16PITCOL-PIT2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-2 | period_total |  | 0.675 |  | 68 | 33 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16PITCOL-3 | period_total |  | 0.425 |  | 44 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLALEHKONEN62-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-1 | player_assists |  | 0.315 |  | 33 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLBNELSON11-2 | player_assists |  | 0.055 |  | 6 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-1 | player_assists |  | 0.680 |  | 69 | 33 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-2 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16PITCOL-COLCMAKAR8-3 | player_assists |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ COL | 0.654 | 0.626 | 0.161 | 0.203 | 6.74 | 6.68 | 0.978/1.042 | KXNHLSPREAD-26OCT16PITCOL-COL2 -0.031 |
| BOS @ ANA | 0.484 | 0.534 | 0.177 | 0.213 | 6.33 | 6.67 | 1.016/0.968 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.078 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Cale Makar: 1+ assists NO @ 33c · p 0.5555 (adj 0.3789) · $11.62 · thesis COL:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 11c · p 0.1434 (adj 0.1326) · $3.98 · thesis PIT:OFFENSE_4PLUS
- Artturi Lehkonen: 1+ goals YES @ 26c · p 0.3068 (adj 0.2939) · $7.53 · thesis COL:OFFENSE_4PLUS
- Nathan MacKinnon: 1+ goals NO @ 52c · p 0.568 (adj 0.5535) · $5.64 · thesis COL:SUPPRESSED
- Nikita Klepov: 1+ assists NO @ 77c · p 0.8624 (adj 0.8137) · $20.0 · thesis ANA:SUPPRESSED
- A.J. Greer: 1+ goals YES @ 13c · p 0.2325 (adj 0.1626) · $5.16 · thesis ANA:OFFENSE_4PLUS
- David Pastrnak: 1+ goals NO @ 62c · p 0.6768 (adj 0.6601) · $16.04 · thesis BOS:SUPPRESSED
- Tim Washe: 1+ goals YES @ 10c · p 0.1283 (adj 0.1187) · $3.26 · thesis ANA:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ COL** · priced 174/177 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.95, exp saves 22.78 (sd 6.25), pull risk 0.053
- PIT net: Arturs Silovs (CONFIRMED) exp shots 30.66, exp saves 25.81 (sd 7.26), pull risk 0.095

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Cale Makar: 1+ assists | 0.445 | 0.680 | 69/33 | +0.210 | STANDARD |
| Cale Makar: 2+ points | 0.191 | 0.375 | 39/64 | +0.153 | STANDARD |
| Cale Makar: 1+ points | 0.553 | 0.695 | 71/32 | +0.111 | STANDARD |
| Cale Makar: 2+ assists | 0.115 | 0.250 | 26/76 | +0.112 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.366 | 0.485 | 50/53 | +0.086 | STANDARD |
| Arturs Silovs: 28+ saves | 0.407 | 0.510 | 52/50 | +0.075 |  |

**BOS @ ANA** · priced 165/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 25.7, exp saves 22.28 (sd 6.24), pull risk 0.063
- BOS net: Jeremy Swayman (PROJECTED) exp shots 31.08, exp saves 26.5 (sd 7.3), pull risk 0.085

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ assists | 0.320 | 0.435 | 44/57 | +0.093 | STANDARD |
| A.J. Greer: 1+ goals | 0.233 | 0.125 | 13/88 | +0.095 | STANDARD |
| Charlie McAvoy: 1+ points | 0.410 | 0.515 | 52/49 | +0.083 | STANDARD |
| Nikita Klepov: 1+ assists | 0.138 | 0.235 | 24/77 | +0.080 | PRIOR_HEAVY |
| Jackson LaCombe: 1+ points | 0.628 | 0.535 | 54/47 | +0.071 | STANDARD |
| Jackson LaCombe: 1+ assists | 0.557 | 0.465 | 48/55 | +0.059 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
