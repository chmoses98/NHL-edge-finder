# NHL slate 2026-10-21 — RESEARCH_ONLY

generated 2026-10-21T17:08:36Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2775 · contracts joined: 500 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 450, 'NO_EDGE': 15, 'OK': 35}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 84, 'game_early_goal': 2, 'first_goal': 74, 'game_winner': 4, 'player_goals': 128, 'game_overtime': 2, 'player_points': 110, 'goalie_saves': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BUF | 2026-10-21T23:30:00Z | T-6h | 0.627 | 0.373 | 0.178 | 5.71 | 3.22 | 2.48 | 269 (25/244) | CONFIRMED/CONFIRMED |
| FLA @ OTT | 2026-10-21T23:30:00Z | T-6h | 0.527 | 0.473 | 0.175 | 6.23 | 3.20 | 3.03 | 231 (25/206) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT21PHIBUF-5 | game_total | 0.708 | 0.785 | 0.771 | 79 | 22 | no | +0.060 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-6 | game_total | 0.477 | 0.555 | 0.540 | 56 | 45 | no | +0.055 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-7 | game_total | 0.365 | 0.440 | 0.425 | 45 | 57 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4 | team_total | 0.418 | 0.485 | 0.471 | 49 | 52 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF3 | team_total | 0.637 | 0.695 | 0.684 | 70 | 31 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-4 | game_total | 0.805 | 0.860 | 0.850 | 87 | 15 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI3 | team_total | 0.458 | 0.515 | 0.504 | 52 | 49 | no | +0.035 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-8 | game_total | 0.194 | 0.245 | 0.234 | 25 | 76 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-9 | game_total | 0.130 | 0.175 | 0.165 | 18 | 83 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-7 | game_total | 0.454 | 0.405 | 0.415 | 41 | 60 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-6 | game_total | 0.564 | 0.515 | 0.525 | 52 | 49 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI4 | team_total | 0.251 | 0.300 | 0.290 | 31 | 71 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF5 | team_total | 0.224 | 0.265 | 0.256 | 27 | 74 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5 | team_total | 0.223 | 0.185 | 0.192 | 19 | 82 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF2 | team_total | 0.832 | 0.865 | 0.859 | 87 | 14 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT6 | team_total | 0.104 | 0.070 | 0.076 | 8 | 94 | yes | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI2 | team_total | 0.700 | 0.735 | 0.728 | 74 | 27 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT21PHIBUF-BUF3 | game_spread | 0.240 | 0.275 | 0.268 | 28 | 73 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-9 | game_total | 0.185 | 0.155 | 0.161 | 16 | 85 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF6 | team_total | 0.098 | 0.130 | 0.123 | 14 | 88 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-8 | game_total | 0.265 | 0.230 | 0.237 | 24 | 78 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4 | team_total | 0.408 | 0.370 | 0.378 | 38 | 64 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-3 | game_total | 0.946 | 0.970 | 0.966 | 98 | 4 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-10 | game_total | 0.054 | 0.080 | 0.074 | 9 | 93 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT3 | team_total | 0.628 | 0.595 | 0.602 | 60 | 41 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI5 | team_total | 0.112 | 0.135 | 0.130 | 14 | 87 | no | +0.010 | OK |
| KXNHLSPREAD-26OCT21FLAOTT-FLA3 | game_spread | 0.154 | 0.175 | 0.171 | 18 | 83 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT21FLAOTT-FLA2 | game_spread | 0.260 | 0.285 | 0.280 | 29 | 72 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-5 | game_total | 0.778 | 0.755 | 0.760 | 76 | 25 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT21FLAOTT-OTT2 | game_spread | 0.308 | 0.285 | 0.289 | 29 | 72 | yes | +0.003 | OK |
| KXNHLTOTAL-26OCT21PHIBUF-2 | game_total | 0.976 | 0.985 | 0.983 | 99 | 2 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA6 | team_total | 0.087 | 0.070 | 0.073 | 8 | 94 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT2 | team_total | 0.823 | 0.800 | 0.805 | 81 | 21 | yes | +0.002 | OK |
| KXNHLSPREAD-26OCT21PHIBUF-BUF2 | game_spread | 0.382 | 0.405 | 0.400 | 41 | 60 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-10 | game_total | 0.086 | 0.070 | 0.073 | 8 | 94 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT21FLAOTT-4 | game_total | 0.858 | 0.845 | 0.848 | 85 | 16 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT21FLAOTT-FLA | game_winner | 0.473 | 0.495 | 0.491 | 50 | 51 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT21FLAOTT-OTT | game_winner | 0.527 | 0.505 | 0.509 | 51 | 50 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT21PHIBUF-PHI3 | game_spread | 0.096 | 0.105 | 0.103 | 11 | 90 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI6 | team_total | 0.040 | 0.045 | 0.044 | 5 | 96 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA5 | team_total | 0.196 | 0.175 | 0.179 | 19 | 84 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT21FLAOTT-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA4 | team_total | 0.369 | 0.355 | 0.358 | 36 | 65 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT21FLAOTT-2 | game_total | 0.984 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA3 | team_total | 0.585 | 0.575 | 0.577 | 58 | 43 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT21FLAOTT-OTT3 | game_spread | 0.188 | 0.180 | 0.182 | 19 | 83 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT21PHIBUF-PHI2 | game_spread | 0.182 | 0.185 | 0.184 | 19 | 82 |  | -0.012 | NO_EDGE |
| KXNHLGAME-26OCT21PHIBUF-BUF | game_winner | 0.627 | 0.635 | 0.633 | 64 | 37 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT21PHIBUF-PHI | game_winner | 0.373 | 0.365 | 0.367 | 37 | 64 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT21FLAOTT-FLA2 | team_total | 0.799 | 0.795 | 0.796 | 81 | 22 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT21PHIBUF-BUF | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT21PHIBUF-PHI | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT21PHIBUF-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT21PHIBUF-BUF2 | period_spread |  | 0.125 |  | 16 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT21PHIBUF-PHI2 | period_spread |  | 0.060 |  | 9 | 97 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT21PHIBUF-1 | period_total |  | 0.820 |  | 83 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT21PHIBUF-2 | period_total |  | 0.530 |  | 54 | 48 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT21PHIBUF-3 | period_total |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT21PHIBUF-BUF | period_winner |  | 0.405 |  | 42 | 61 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT21PHIBUF-PHI | period_winner |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT21PHIBUF-TIE | period_winner |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT21PHIBUF-BUF2 | period_spread |  | 0.170 |  | 20 | 86 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT21PHIBUF-PHI2 | period_spread |  | 0.075 |  | 10 | 95 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT21PHIBUF-1 | period_total |  | 0.895 |  | 92 | 13 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT21PHIBUF-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT21PHIBUF-3 | period_total |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT21PHIBUF-BUF | period_winner |  | 0.435 |  | 45 | 58 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT21PHIBUF-PHI | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT21PHIBUF-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT21PHIBUF-BUF2 | period_spread |  | 0.215 |  | 24 | 81 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT21PHIBUF-PHI2 | period_spread |  | 0.110 |  | 15 | 93 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT21PHIBUF-1 | period_total |  | 0.890 |  | 91 | 13 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT21PHIBUF-2 | period_total |  | 0.650 |  | 66 | 36 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT21PHIBUF-3 | period_total |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFBMALENSTYN29-1 | player_assists |  | 0.065 |  | 12 | 99 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJDOAN91-1 | player_assists |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJDOAN91-2 | player_assists |  | 0.060 |  | 8 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJKULICH20-1 | player_assists |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJKULICH20-2 | player_assists |  | 0.045 |  | 7 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT21PHIBUF-BUFJNORRIS9-1 | player_assists |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PHI @ BUF | 0.627 | 0.564 | 0.178 | 0.218 | 5.71 | 5.99 | 1.002/0.994 | KXNHLTEAMTOTAL-26OCT21PHIBUF-PHI3 +0.082 |
| FLA @ OTT | 0.527 | 0.582 | 0.175 | 0.215 | 6.23 | 6.15 | 0.983/0.991 | KXNHLGAME-26OCT21FLAOTT-OTT +0.055 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Jiri Kulich: 1+ goals YES @ 18c · p 0.2183 (adj 0.2075) · $6.09 · thesis BUF:OFFENSE_4PLUS
- Tage Thompson: 1+ goals NO @ 61c · p 0.6565 (adj 0.6424) · $7.35 · thesis BUF:SUPPRESSED
- Buffalo wins by over 1.5 goals NO @ 60c · p 0.6687 (adj 0.6319) · $8.24 · thesis GAME:TIGHT
- Buffalo over 3.5 goals scored NO @ 52c · p 0.5882 (adj 0.5516) · $5.32 · thesis BUF:SUPPRESSED
- Brady Tkachuk: 1+ goals NO @ 65c · p 0.7224 (adj 0.7018) · $20.0 · thesis FLA:SUPPRESSED
- Nick Cousins: 1+ goals YES @ 9c · p 0.1165 (adj 0.1086) · $3.1 · thesis OTT:OFFENSE_4PLUS
- Florida wins by over 2.5 goals NO @ 83c · p 0.8842 (adj 0.8546) · $18.63 · thesis OTT:WINS
- Ridly Greig: 1+ goals YES @ 16c · p 0.1954 (adj 0.184) · $3.92 · thesis OTT:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PHI @ BUF** · priced 210/218 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (CONFIRMED) exp shots 24.46, exp saves 21.36 (sd 5.97), pull risk 0.046
- PHI net: Dan Vladar (CONFIRMED) exp shots 28.82, exp saves 24.88 (sd 6.8), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Oliver Bonk: 1+ assists | 0.265 | 0.125 | 24/99 | +0.012 | PRIOR_HEAVY |
| Rasmus Dahlin: 1+ assists | 0.368 | 0.505 | 51/50 | +0.115 | STANDARD |
| Oliver Bonk: 1+ points | 0.321 | 0.185 | 29/92 | +0.016 | PRIOR_HEAVY |
| Rasmus Dahlin: 1+ points | 0.476 | 0.610 | 62/40 | +0.107 | STANDARD |
| Nick Seeler: 1+ points | 0.227 | 0.095 | 17/98 | +0.047 | STANDARD |
| Rasmus Dahlin: 2+ points | 0.139 | 0.270 | 29/75 | +0.098 | STANDARD |

**FLA @ OTT** · priced 167/180 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROBABLE) exp shots 25.61, exp saves 22.37 (sd 6.09), pull risk 0.049
- FLA net: Akira Schmid (CONFIRMED) exp shots 27.07, exp saves 23.12 (sd 6.56), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 2+ points | 0.148 | 0.265 | 27/74 | +0.099 | STANDARD |
| Seth Jones: 1+ assists | 0.351 | 0.455 | 46/55 | +0.082 | STANDARD |
| Jake Sanderson: 1+ assists | 0.329 | 0.430 | 44/58 | +0.074 | STANDARD |
| Brady Tkachuk: 1+ points | 0.497 | 0.590 | 60/42 | +0.066 | STANDARD |
| Jake Sanderson: 1+ points | 0.416 | 0.500 | 51/51 | +0.056 | STANDARD |
| Brady Tkachuk: 1+ goals | 0.278 | 0.360 | 37/65 | +0.056 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
