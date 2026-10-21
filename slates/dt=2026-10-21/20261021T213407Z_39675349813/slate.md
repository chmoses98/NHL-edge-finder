# NHL slate 2026-10-21 — RESEARCH_ONLY

generated 2026-10-21T21:34:07Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2804 · contracts joined: 516 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 466, 'OK': 38, 'NO_EDGE': 12}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 88, 'game_early_goal': 2, 'first_goal': 74, 'game_winner': 4, 'player_goals': 129, 'game_overtime': 2, 'player_points': 119, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BUF | 2026-10-21T23:30:00Z | T-90m | 0.627 | 0.373 | 0.178 | 5.71 | 3.22 | 2.48 | 270 (25/245) | CONFIRMED/CONFIRMED |
| FLA @ OTT | 2026-10-21T23:30:00Z | T-90m | 0.527 | 0.473 | 0.175 | 6.23 | 3.20 | 3.03 | 246 (25/221) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT21PHIBUF-5 | game_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-7 | game_total | 0.454 | 0.385 | 0.399 | 39 | 62 | yes | +0.048 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-7 | game_total | 0.365 | 0.440 | 0.425 | 45 | 57 | no | +0.048 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-4 | game_total | 0.805 | 0.865 | 0.854 | 87 | 14 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-6 | game_total | 0.564 | 0.495 | 0.509 | 50 | 51 | yes | +0.046 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-6 | game_total | 0.477 | 0.545 | 0.532 | 55 | 46 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4 | team_total | 0.418 | 0.490 | 0.475 | 50 | 52 | no | +0.045 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-8 | game_total | 0.265 | 0.205 | 0.216 | 21 | 80 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF3 | team_total | 0.637 | 0.700 | 0.688 | 71 | 31 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI3 | team_total | 0.458 | 0.515 | 0.504 | 52 | 49 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-8 | game_total | 0.194 | 0.250 | 0.238 | 26 | 76 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5 | team_total | 0.223 | 0.175 | 0.184 | 18 | 83 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF2 | team_total | 0.832 | 0.880 | 0.871 | 89 | 13 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT6 | team_total | 0.104 | 0.065 | 0.072 | 7 | 94 | yes | +0.030 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-9 | game_total | 0.185 | 0.145 | 0.152 | 15 | 86 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT21PHIBUF-BUF3 | game_spread | 0.240 | 0.290 | 0.280 | 30 | 72 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF5 | team_total | 0.224 | 0.265 | 0.256 | 27 | 74 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-9 | game_total | 0.130 | 0.170 | 0.161 | 18 | 84 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI2 | team_total | 0.700 | 0.735 | 0.728 | 74 | 27 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI4 | team_total | 0.251 | 0.285 | 0.278 | 29 | 72 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-5 | game_total | 0.778 | 0.745 | 0.752 | 75 | 26 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF6 | team_total | 0.098 | 0.130 | 0.123 | 14 | 88 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA6 | team_total | 0.087 | 0.065 | 0.069 | 7 | 94 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4 | team_total | 0.408 | 0.370 | 0.378 | 38 | 64 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-3 | game_total | 0.946 | 0.970 | 0.966 | 98 | 4 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-10 | game_total | 0.086 | 0.060 | 0.065 | 7 | 95 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT21PHIBUF-BUF2 | game_spread | 0.382 | 0.415 | 0.408 | 42 | 59 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-10 | game_total | 0.054 | 0.080 | 0.074 | 9 | 93 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT3 | team_total | 0.628 | 0.595 | 0.602 | 60 | 41 | yes | +0.011 | OK |
| KXNHLGAME-26OCT21PHIBUF-BUF | game_winner | 0.627 | 0.655 | 0.649 | 66 | 35 | no | +0.007 | OK |
| KXNHLGAME-26OCT21PHIBUF-PHI | game_winner | 0.373 | 0.345 | 0.351 | 35 | 66 | yes | +0.007 | OK |
| KXNHLSPREAD-26OCT21FLAOTT-FLA3 | game_spread | 0.154 | 0.180 | 0.174 | 19 | 83 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA5 | team_total | 0.196 | 0.175 | 0.179 | 18 | 83 | yes | +0.006 | OK |
| KXNHLSPREAD-26OCT21FLAOTT-FLA2 | game_spread | 0.260 | 0.285 | 0.280 | 29 | 72 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA4 | team_total | 0.369 | 0.340 | 0.346 | 35 | 67 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-2 | game_total | 0.976 | 0.985 | 0.983 | 99 | 2 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT2 | team_total | 0.823 | 0.800 | 0.805 | 81 | 21 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI5 | team_total | 0.112 | 0.125 | 0.122 | 13 | 88 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-4 | game_total | 0.858 | 0.840 | 0.844 | 85 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA3 | team_total | 0.585 | 0.565 | 0.569 | 57 | 44 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA2 | team_total | 0.799 | 0.785 | 0.788 | 79 | 22 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT21FLAOTT-2 | game_total | 0.984 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT21FLAOTT-OTT2 | game_spread | 0.308 | 0.295 | 0.297 | 30 | 71 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT21PHIBUF-PHI2 | game_spread | 0.182 | 0.175 | 0.176 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT21FLAOTT-3 | game_total | 0.963 | 0.960 | 0.961 | 97 | 5 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26OCT21FLAOTT-FLA | game_winner | 0.473 | 0.485 | 0.483 | 49 | 52 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT21FLAOTT-OTT | game_winner | 0.527 | 0.515 | 0.517 | 52 | 49 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT21PHIBUF-PHI3 | game_spread | 0.096 | 0.100 | 0.099 | 11 | 91 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI6 | team_total | 0.040 | 0.040 | 0.040 | 5 | 97 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT21FLAOTT-OTT3 | game_spread | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.012 | NO_EDGE |
| KXNHL1P-26OCT21PHIBUF-BUF | period_winner |  | 0.395 |  | 41 | 62 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT21PHIBUF-PHI | period_winner |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT21PHIBUF-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT21PHIBUF-BUF2 | period_spread |  | 0.145 |  | 15 | 86 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT21PHIBUF-PHI2 | period_spread |  | 0.065 |  | 8 | 95 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT21PHIBUF-1 | period_total |  | 0.835 |  | 85 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT21PHIBUF-2 | period_total |  | 0.540 |  | 55 | 47 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT21PHIBUF-3 | period_total |  | 0.260 |  | 27 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT21PHIBUF-BUF | period_winner |  | 0.425 |  | 44 | 59 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT21PHIBUF-PHI | period_winner |  | 0.270 |  | 29 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT21PHIBUF-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT21PHIBUF-BUF2 | period_spread |  | 0.170 |  | 19 | 85 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT21PHIBUF-PHI2 | period_spread |  | 0.070 |  | 9 | 95 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT21PHIBUF-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT21PHIBUF-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT21PHIBUF-3 | period_total |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT21PHIBUF-BUF | period_winner |  | 0.450 |  | 46 | 56 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT21PHIBUF-PHI | period_winner |  | 0.275 |  | 29 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT21PHIBUF-TIE | period_winner |  | 0.255 |  | 28 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT21PHIBUF-BUF2 | period_spread |  | 0.215 |  | 23 | 80 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT21PHIBUF-PHI2 | period_spread |  | 0.090 |  | 11 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT21PHIBUF-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT21PHIBUF-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT21PHIBUF-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFBMALENSTYN29-1 | player_assists |  | 0.070 |  | 13 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJDOAN91-1 | player_assists |  | 0.295 |  | 30 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJDOAN91-2 | player_assists |  | 0.070 |  | 8 | 94 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJKULICH20-1 | player_assists |  | 0.280 |  | 30 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJKULICH20-2 | player_assists |  | 0.050 |  | 7 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJNORRIS9-1 | player_assists |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BUF | 0.627 | 0.564 | 0.178 | 0.218 | 5.71 | 5.99 | 1.002/0.994 | KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI3 +0.082 |
| FLA @ OTT | 0.527 | 0.582 | 0.175 | 0.215 | 6.23 | 6.15 | 0.983/0.991 | KXNHLGAME-26OCT21FLAOTT-OTT +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Tage Thompson: 1+ goals NO @ 61c · p 0.682 (adj 0.6615) · $17.75 · thesis BUF:SUPPRESSED
- Rasmus Dahlin: 1+ assists NO @ 49c · p 0.6369 (adj 0.5382) · $12.25 · thesis BUF:SUPPRESSED
- Noel Acciari: 1+ assists NO @ 77c · p 0.8364 (adj 0.8007) · $18.58 · thesis PHI:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 64c · p 0.7229 (adj 0.7009) · $20.0 · thesis FLA:SUPPRESSED
- Ridly Greig: 1+ goals YES @ 15c · p 0.1954 (adj 0.1815) · $6.8 · thesis OTT:OFFENSE_4PLUS
- Jake Sanderson: 1+ assists NO @ 58c · p 0.6714 (adj 0.6232) · $19.35 · thesis OTT:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 9c · p 0.1165 (adj 0.1086) · $3.56 · thesis OTT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BUF** · priced 217/219 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 24.46, exp saves 21.35 (sd 5.97), pull risk 0.046
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.82, exp saves 24.88 (sd 6.8), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Rasmus Dahlin: 1+ points | 0.462 | 0.620 | 63/39 | +0.132 | STANDARD |
| Rasmus Dahlin: 1+ assists | 0.363 | 0.515 | 52/49 | +0.129 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.128 | 0.260 | 27/75 | +0.108 | STANDARD |
| Tage Thompson: 2+ points | 0.194 | 0.305 | 32/71 | +0.082 | STANDARD |
| Jiri Kulich: 1+ assists | 0.172 | 0.280 | 30/74 | +0.074 | STANDARD |
| Rasmus Dahlin: 2+ assists | 0.078 | 0.180 | 19/83 | +0.083 | STANDARD |

**FLA @ OTT** · priced 182/195 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROBABLE) exp shots 25.61, exp saves 22.37 (sd 6.09), pull risk 0.049
- FLA net: Akira Schmid (CONFIRMED) exp shots 27.07, exp saves 23.12 (sd 6.56), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Seth Jones: 1+ assists | 0.351 | 0.455 | 46/55 | +0.082 | STANDARD |
| Brady Tkachuk: 1+ points | 0.496 | 0.595 | 61/42 | +0.067 | STANDARD |
| Jake Sanderson: 1+ assists | 0.329 | 0.425 | 43/58 | +0.074 | STANDARD |
| Warren Foegele: 1+ points | 0.396 | 0.305 | 31/70 | +0.071 | STANDARD |
| Brady Tkachuk: 1+ goals | 0.277 | 0.365 | 37/64 | +0.067 | STANDARD |
| Ridly Greig: 1+ points | 0.402 | 0.315 | 32/69 | +0.067 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
