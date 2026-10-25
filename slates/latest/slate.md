# NHL slate 2026-10-25 — RESEARCH_ONLY

generated 2026-10-25T04:47:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2501 · contracts joined: 255 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 130, 'OK': 88, 'NO_EDGE': 37}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'game_early_goal': 5, 'game_winner': 10, 'game_overtime': 5, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 2026-10-25T19:00:00Z | T-12h | 0.495 | 0.505 | 0.182 | 6.02 | 3.00 | 3.02 | 51 (25/26) | PROJECTED/CONFIRMED |
| NYI @ DAL | 2026-10-25T22:00:00Z | T-12h | 0.563 | 0.437 | 0.187 | 5.51 | 2.94 | 2.56 | 51 (25/26) | PROJECTED/PROJECTED |
| MTL @ WPG | 2026-10-25T23:00:00Z | T-12h | 0.469 | 0.531 | 0.178 | 5.93 | 2.87 | 3.06 | 51 (25/26) | PROJECTED/PROJECTED |
| COL @ NSH | 2026-10-26T00:00:00Z | T-12h | 0.422 | 0.578 | 0.170 | 6.43 | 2.96 | 3.47 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ VAN | 2026-10-26T02:00:00Z | T-12h | 0.437 | 0.563 | 0.163 | 6.76 | 3.18 | 3.58 | 51 (25/26) | PROJECTED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT25FLACHI-CHI | game_winner | 0.495 | 0.375 | 0.398 | 38 | 63 | yes | +0.099 | OK |
| KXNHLGAME-26OCT25FLACHI-FLA | game_winner | 0.505 | 0.625 | 0.602 | 63 | 38 | no | +0.099 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA4 | team_total | 0.367 | 0.490 | 0.465 | 50 | 52 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA2 | game_spread | 0.283 | 0.400 | 0.375 | 41 | 61 | no | +0.091 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA3 | team_total | 0.588 | 0.705 | 0.683 | 72 | 31 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT25FLACHI-FLA3 | game_spread | 0.170 | 0.275 | 0.251 | 28 | 73 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL3 | game_spread | 0.231 | 0.335 | 0.312 | 34 | 67 | no | +0.083 | OK |
| KXNHLGAME-26OCT25COLNSH-COL | game_winner | 0.578 | 0.675 | 0.656 | 68 | 33 | no | +0.077 | OK |
| KXNHLGAME-26OCT25COLNSH-NSH | game_winner | 0.422 | 0.325 | 0.344 | 33 | 68 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI2 | game_spread | 0.277 | 0.185 | 0.201 | 19 | 82 | yes | +0.076 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA5 | team_total | 0.193 | 0.295 | 0.272 | 31 | 72 | no | +0.073 | OK |
| KXNHLSPREAD-26OCT25COLNSH-COL2 | game_spread | 0.361 | 0.460 | 0.440 | 47 | 55 | no | +0.072 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL4 | team_total | 0.349 | 0.445 | 0.425 | 46 | 57 | no | +0.064 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL4 | team_total | 0.470 | 0.560 | 0.542 | 57 | 45 | no | +0.063 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL5 | team_total | 0.273 | 0.365 | 0.346 | 38 | 65 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL3 | team_total | 0.679 | 0.760 | 0.745 | 77 | 25 | no | +0.058 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL2 | game_spread | 0.325 | 0.405 | 0.388 | 41 | 60 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL3 | team_total | 0.578 | 0.660 | 0.644 | 67 | 35 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN2 | game_spread | 0.350 | 0.430 | 0.413 | 44 | 58 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA2 | team_total | 0.799 | 0.875 | 0.862 | 89 | 14 | no | +0.052 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-DAL3 | game_spread | 0.195 | 0.270 | 0.254 | 28 | 74 | no | +0.052 | OK |
| KXNHLGAME-26OCT25MINVAN-MIN | game_winner | 0.563 | 0.635 | 0.621 | 64 | 37 | no | +0.051 | OK |
| KXNHLGAME-26OCT25NYIDAL-DAL | game_winner | 0.563 | 0.640 | 0.625 | 65 | 37 | no | +0.050 | OK |
| KXNHLGAME-26OCT25NYIDAL-NYI | game_winner | 0.437 | 0.360 | 0.375 | 37 | 65 | yes | +0.050 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH2 | game_spread | 0.225 | 0.165 | 0.176 | 17 | 84 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL5 | team_total | 0.174 | 0.245 | 0.229 | 26 | 77 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL2 | team_total | 0.790 | 0.850 | 0.839 | 86 | 16 | no | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-FLA6 | team_total | 0.084 | 0.140 | 0.127 | 15 | 87 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN3 | team_total | 0.616 | 0.550 | 0.563 | 56 | 46 | yes | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN4 | team_total | 0.404 | 0.335 | 0.348 | 35 | 68 | yes | +0.038 | OK |
| KXNHLSPREAD-26OCT25FLACHI-CHI3 | game_spread | 0.162 | 0.115 | 0.123 | 12 | 89 | yes | +0.035 | OK |
| KXNHLTOTAL-26OCT25FLACHI-6 | game_total | 0.529 | 0.585 | 0.574 | 59 | 42 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN5 | team_total | 0.224 | 0.165 | 0.176 | 18 | 85 | yes | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL6 | team_total | 0.136 | 0.190 | 0.178 | 20 | 82 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT25FLACHI-7 | game_total | 0.419 | 0.475 | 0.464 | 48 | 53 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN2 | game_spread | 0.243 | 0.190 | 0.200 | 20 | 82 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT25MINVAN-MIN3 | game_spread | 0.224 | 0.280 | 0.268 | 29 | 73 | no | +0.032 | OK |
| KXNHLGAME-26OCT25MINVAN-VAN | game_winner | 0.437 | 0.385 | 0.395 | 39 | 62 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI4 | team_total | 0.364 | 0.315 | 0.325 | 32 | 69 | yes | +0.029 | OK |
| KXNHLTOTAL-26OCT25FLACHI-5 | game_total | 0.752 | 0.795 | 0.787 | 80 | 21 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-5 | game_total | 0.679 | 0.725 | 0.716 | 73 | 28 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI2 | game_spread | 0.216 | 0.170 | 0.179 | 18 | 84 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH4 | team_total | 0.351 | 0.305 | 0.314 | 31 | 70 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-COL2 | team_total | 0.858 | 0.900 | 0.893 | 91 | 11 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI3 | team_total | 0.583 | 0.530 | 0.541 | 54 | 48 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT25FLACHI-4 | game_total | 0.838 | 0.875 | 0.868 | 88 | 13 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT25COLNSH-NSH3 | game_spread | 0.129 | 0.090 | 0.097 | 10 | 92 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH3 | team_total | 0.570 | 0.520 | 0.530 | 53 | 49 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT25NYIDAL-DAL6 | team_total | 0.072 | 0.110 | 0.101 | 12 | 90 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-6 | game_total | 0.442 | 0.485 | 0.476 | 49 | 52 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT25MINVAN-7 | game_total | 0.538 | 0.490 | 0.500 | 50 | 52 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-7 | game_total | 0.334 | 0.375 | 0.367 | 38 | 63 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT25MINVAN-6 | game_total | 0.646 | 0.605 | 0.613 | 61 | 40 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN6 | team_total | 0.104 | 0.065 | 0.072 | 8 | 95 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-4 | game_total | 0.781 | 0.820 | 0.813 | 83 | 19 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH5 | team_total | 0.187 | 0.150 | 0.157 | 16 | 86 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT25COLNSH-7 | game_total | 0.486 | 0.525 | 0.517 | 53 | 48 | no | +0.016 | OK |
| KXNHLSPREAD-26OCT25MINVAN-VAN3 | game_spread | 0.143 | 0.110 | 0.116 | 12 | 90 | yes | +0.016 | OK |
| KXNHLTOTAL-26OCT25MINVAN-9 | game_total | 0.247 | 0.210 | 0.217 | 22 | 80 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT25FLACHI-8 | game_total | 0.231 | 0.270 | 0.262 | 28 | 74 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-4 | game_total | 0.827 | 0.855 | 0.850 | 86 | 15 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-VAN2 | team_total | 0.815 | 0.775 | 0.783 | 79 | 24 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-10 | game_total | 0.043 | 0.065 | 0.060 | 7 | 94 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-9 | game_total | 0.109 | 0.135 | 0.129 | 14 | 87 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT25MINVAN-8 | game_total | 0.338 | 0.305 | 0.311 | 31 | 70 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT25MINVAN-10 | game_total | 0.130 | 0.100 | 0.105 | 11 | 91 | yes | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT25MTLWPG-WPG4 | team_total | 0.333 | 0.370 | 0.363 | 38 | 64 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT25MINVAN-5 | game_total | 0.831 | 0.805 | 0.810 | 81 | 20 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI2 | team_total | 0.792 | 0.765 | 0.771 | 77 | 24 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 | team_total | 0.493 | 0.530 | 0.523 | 54 | 48 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT25MTLWPG-5 | game_total | 0.738 | 0.765 | 0.760 | 77 | 24 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI5 | team_total | 0.189 | 0.160 | 0.165 | 17 | 85 | yes | +0.009 | OK |
| KXNHLSPREAD-26OCT25NYIDAL-NYI3 | game_spread | 0.115 | 0.090 | 0.095 | 10 | 92 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT25NYIDAL-3 | game_total | 0.938 | 0.960 | 0.956 | 97 | 5 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT25FLACHI-9 | game_total | 0.162 | 0.185 | 0.180 | 19 | 82 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH2 | team_total | 0.789 | 0.760 | 0.766 | 77 | 25 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN3 | team_total | 0.700 | 0.730 | 0.724 | 74 | 28 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25FLACHI-CHI6 | team_total | 0.080 | 0.060 | 0.064 | 7 | 95 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25COLNSH-NSH6 | team_total | 0.080 | 0.060 | 0.064 | 7 | 95 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT25MINVAN-MIN2 | team_total | 0.867 | 0.885 | 0.882 | 89 | 12 | no | +0.005 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ CHI | 0.495 | 0.476 | 0.182 | 0.220 | 6.02 | 6.24 | 1.003/0.991 | KXNHLTOTAL-26OCT25FLACHI-7 +0.044 |
| NYI @ DAL | 0.563 | 0.554 | 0.187 | 0.223 | 5.51 | 5.98 | 0.986/0.956 | KXNHLTOTAL-26OCT25NYIDAL-7 +0.085 |
| MTL @ WPG | 0.469 | 0.480 | 0.178 | 0.221 | 5.93 | 6.22 | 1.001/0.976 | KXNHLTOTAL-26OCT25MTLWPG-7 +0.047 |
| COL @ NSH | 0.422 | 0.426 | 0.170 | 0.209 | 6.43 | 6.49 | 1.000/0.976 | KXNHLTEAMTOTAL-26OCT25COLNSH-NSH4 +0.016 |
| MIN @ VAN | 0.437 | 0.496 | 0.163 | 0.218 | 6.76 | 6.51 | 1.025/1.032 | KXNHLTEAMTOTAL-26OCT25MINVAN-MIN4 -0.067 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 10 recommended · full analysis in card.md / packet.json `thesis_card`

- Florida wins by over 2.5 goals NO @ 73c · p 0.8096 (adj 0.7673) · $20.0 · thesis CHI:WINS
- Chicago wins by over 1.5 goals YES @ 19c · p 0.2577 (adj 0.2213) · $4.21 · thesis CHI:WINS_BY_2PLUS
- Dallas wins by over 1.5 goals NO @ 60c · p 0.6717 (adj 0.6333) · $9.85 · thesis GAME:TIGHT
- New York I over 2.5 goals scored YES @ 47c · p 0.5386 (adj 0.4993) · $2.32 · thesis NYI:OFFENSE_4PLUS
- Colorado wins by over 2.5 goals NO @ 67c · p 0.7536 (adj 0.7093) · $19.42 · thesis GAME:TIGHT
- Nashville wins by over 1.5 goals YES @ 17c · p 0.216 (adj 0.1905) · $1.19 · thesis NSH:WINS_BY_2PLUS
- Vancouver wins by over 1.5 goals YES @ 20c · p 0.2794 (adj 0.2347) · $4.29 · thesis VAN:WINS_BY_2PLUS
- Minnesota wins by over 2.5 goals NO @ 73c · p 0.8158 (adj 0.7679) · $19.65 · thesis VAN:WINS
- Minnesota over 2.5 goals scored NO @ 28c · p 0.359 (adj 0.3145) · $1.11 · thesis MIN:SUPPRESSED
- Minnesota over 4.5 goals scored NO @ 69c · p 0.7662 (adj 0.7231) · $2.57 · thesis VAN:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ CHI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CHI net: Spencer Knight (PROJECTED) exp shots 28.48, exp saves 24.4 (sd 6.79), pull risk 0.066
- FLA net: Akira Schmid (CONFIRMED) exp shots 24.45, exp saves 21.18 (sd 6.04), pull risk 0.058

**NYI @ DAL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DAL net: Jake Oettinger (PROJECTED) exp shots 25.4, exp saves 22.15 (sd 6.13), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 26.22, exp saves 22.62 (sd 6.26), pull risk 0.06

**MTL @ WPG** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.43, exp saves 22.91 (sd 6.31), pull risk 0.06
- MTL net: Jacob Fowler (PROJECTED) exp shots 27.53, exp saves 23.97 (sd 6.52), pull risk 0.057

**COL @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/RECENT_SHIFTS
- NSH net: Juuse Saros (PROJECTED) exp shots 32.0, exp saves 27.36 (sd 7.43), pull risk 0.081
- COL net: Mackenzie Blackwood (PROJECTED) exp shots 26.47, exp saves 23.04 (sd 6.33), pull risk 0.06

**MIN @ VAN** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- VAN net: Leevi Merilainen (PROJECTED) exp shots 30.86, exp saves 26.64 (sd 7.05), pull risk 0.064
- MIN net: Calvin Pickard (CONFIRMED) exp shots 25.73, exp saves 22.3 (sd 6.22), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
