# NHL slate 2026-10-30 — RESEARCH_ONLY

generated 2026-10-30T05:27:55Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2336 · contracts joined: 153 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 78, 'NO_EDGE': 53, 'OK': 22}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 2026-10-30T22:00:00Z | T-12h | 0.524 | 0.476 | 0.176 | 6.23 | 3.19 | 3.04 | 51 (25/26) | PROJECTED/PROJECTED |
| WPG @ FLA | 2026-10-30T23:00:00Z | T-12h | 0.602 | 0.398 | 0.172 | 6.03 | 3.34 | 2.69 | 51 (25/26) | PROJECTED/PROJECTED |
| SEA @ CGY | 2026-10-31T00:00:00Z | T-12h | 0.488 | 0.512 | 0.175 | 6.39 | 3.15 | 3.24 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT30WPGFLA-FLA2 | game_spread | 0.374 | 0.460 | 0.442 | 47 | 55 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-FLA3 | game_spread | 0.240 | 0.320 | 0.303 | 33 | 69 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA4 | team_total | 0.441 | 0.520 | 0.504 | 53 | 49 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA5 | team_total | 0.242 | 0.315 | 0.300 | 33 | 70 | no | +0.043 | OK |
| KXNHLGAME-26OCT30WPGFLA-FLA | game_winner | 0.602 | 0.665 | 0.653 | 67 | 34 | no | +0.043 | OK |
| KXNHLGAME-26OCT30WPGFLA-WPG | game_winner | 0.398 | 0.335 | 0.347 | 34 | 67 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA3 | team_total | 0.666 | 0.730 | 0.718 | 74 | 28 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG2 | game_spread | 0.201 | 0.155 | 0.163 | 16 | 85 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA2 | team_total | 0.845 | 0.885 | 0.878 | 89 | 12 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-FLA6 | team_total | 0.114 | 0.150 | 0.142 | 16 | 86 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT30NJVGK-4 | game_total | 0.851 | 0.875 | 0.870 | 88 | 13 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-8 | game_total | 0.236 | 0.265 | 0.259 | 27 | 74 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-3 | game_total | 0.959 | 0.975 | 0.972 | 98 | 3 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-4 | game_total | 0.844 | 0.865 | 0.861 | 87 | 14 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG5 | team_total | 0.144 | 0.120 | 0.125 | 13 | 89 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-7 | game_total | 0.418 | 0.445 | 0.440 | 45 | 56 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-5 | game_total | 0.754 | 0.775 | 0.771 | 78 | 23 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG6 | team_total | 0.057 | 0.040 | 0.043 | 5 | 97 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA6 | team_total | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT30WPGFLA-WPG3 | game_spread | 0.107 | 0.095 | 0.097 | 10 | 91 | yes | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG4 | team_total | 0.295 | 0.265 | 0.271 | 28 | 75 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-6 | game_total | 0.533 | 0.560 | 0.555 | 57 | 45 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT30WPGFLA-9 | game_total | 0.162 | 0.175 | 0.172 | 18 | 83 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-5 | game_total | 0.772 | 0.785 | 0.782 | 79 | 22 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-3 | game_total | 0.962 | 0.970 | 0.969 | 98 | 4 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA3 | game_spread | 0.184 | 0.195 | 0.193 | 20 | 81 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-9 | game_total | 0.206 | 0.195 | 0.197 | 20 | 81 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY3 | game_spread | 0.166 | 0.175 | 0.173 | 18 | 83 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-10 | game_total | 0.089 | 0.080 | 0.082 | 9 | 93 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK3 | game_spread | 0.186 | 0.195 | 0.193 | 20 | 81 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-5 | game_total | 0.795 | 0.805 | 0.803 | 81 | 20 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-8 | game_total | 0.288 | 0.275 | 0.277 | 28 | 73 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT30WPGFLA-10 | game_total | 0.072 | 0.080 | 0.078 | 9 | 93 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA2 | team_total | 0.827 | 0.840 | 0.837 | 85 | 17 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ6 | team_total | 0.089 | 0.080 | 0.082 | 9 | 93 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ3 | game_spread | 0.158 | 0.170 | 0.167 | 18 | 84 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-10 | game_total | 0.099 | 0.090 | 0.092 | 10 | 92 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-NJ2 | game_spread | 0.265 | 0.275 | 0.273 | 28 | 73 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK2 | team_total | 0.819 | 0.830 | 0.828 | 84 | 18 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY2 | team_total | 0.819 | 0.825 | 0.824 | 83 | 18 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-9 | game_total | 0.189 | 0.180 | 0.182 | 19 | 83 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-3 | game_total | 0.969 | 0.970 | 0.970 | 98 | 4 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 | team_total | 0.506 | 0.485 | 0.489 | 50 | 53 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ2 | team_total | 0.801 | 0.815 | 0.812 | 83 | 20 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-4 | game_total | 0.875 | 0.880 | 0.879 | 89 | 13 |  | -0.013 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-NJ | game_winner | 0.476 | 0.485 | 0.483 | 49 | 52 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT30NJVGK-VGK | game_winner | 0.524 | 0.515 | 0.517 | 52 | 49 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK6 | team_total | 0.102 | 0.095 | 0.096 | 11 | 92 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-CGY | game_winner | 0.488 | 0.495 | 0.494 | 50 | 51 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-SEA2 | game_spread | 0.301 | 0.305 | 0.304 | 31 | 70 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-7 | game_total | 0.481 | 0.475 | 0.476 | 48 | 53 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT30NJVGK-VGK2 | game_spread | 0.302 | 0.305 | 0.304 | 31 | 70 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ3 | team_total | 0.591 | 0.600 | 0.598 | 61 | 41 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-8 | game_total | 0.266 | 0.260 | 0.261 | 27 | 75 |  | -0.018 | NO_EDGE |
| KXNHLSPREAD-26OCT30SEACGY-CGY2 | game_spread | 0.276 | 0.275 | 0.275 | 28 | 73 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK5 | team_total | 0.224 | 0.215 | 0.217 | 23 | 80 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY6 | team_total | 0.098 | 0.095 | 0.096 | 11 | 92 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT30SEACGY-6 | game_total | 0.588 | 0.585 | 0.586 | 59 | 42 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT30SEACGY-SEA | game_winner | 0.512 | 0.515 | 0.514 | 52 | 49 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG2 | team_total | 0.742 | 0.735 | 0.736 | 75 | 28 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY4 | team_total | 0.395 | 0.390 | 0.391 | 40 | 62 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA4 | team_total | 0.416 | 0.425 | 0.423 | 44 | 59 |  | -0.023 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-7 | game_total | 0.456 | 0.460 | 0.459 | 47 | 55 |  | -0.023 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ5 | team_total | 0.197 | 0.195 | 0.195 | 21 | 82 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-NJ4 | team_total | 0.372 | 0.370 | 0.370 | 38 | 64 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA5 | team_total | 0.233 | 0.235 | 0.235 | 25 | 78 |  | -0.025 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY5 | team_total | 0.216 | 0.215 | 0.215 | 23 | 80 |  | -0.026 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK3 | team_total | 0.622 | 0.625 | 0.624 | 64 | 39 |  | -0.029 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-SEA3 | team_total | 0.636 | 0.635 | 0.635 | 65 | 38 |  | -0.030 | NO_EDGE |
| KXNHLTOTAL-26OCT30NJVGK-6 | game_total | 0.563 | 0.565 | 0.565 | 58 | 45 |  | -0.030 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30SEACGY-CGY3 | team_total | 0.616 | 0.615 | 0.615 | 63 | 40 |  | -0.030 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT30NJVGK-VGK4 | team_total | 0.408 | 0.410 | 0.410 | 43 | 61 |  | -0.035 | NO_EDGE |
| KXNHL1P-26OCT30NJVGK-NJ | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-TIE | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT30NJVGK-VGK | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-NJ2 | period_spread |  | 0.125 |  | 21 | 96 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT30NJVGK-VGK2 | period_spread |  | 0.120 |  | 16 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NJD @ VGK | 0.524 | 0.585 | 0.176 | 0.215 | 6.23 | 6.10 | 1.004/0.960 | KXNHLGAME-26OCT30NJVGK-NJ -0.061 |
| WPG @ FLA | 0.602 | 0.569 | 0.172 | 0.214 | 6.03 | 6.12 | 0.999/0.998 | KXNHLTEAMTOTAL-26OCT30WPGFLA-WPG3 +0.049 |
| SEA @ CGY | 0.488 | 0.471 | 0.175 | 0.218 | 6.39 | 6.30 | 0.998/1.006 | KXNHLTOTAL-26OCT30SEACGY-8 -0.022 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- New Jersey wins by over 1.5 goals NO @ 73c · p 0.7833 (adj 0.7541) · $10.97 · thesis VGK:WINS
- Winnipeg wins by over 1.5 goals YES @ 16c · p 0.2227 (adj 0.1889) · $3.76 · thesis WPG:WINS_BY_2PLUS
- Florida over 3.5 goals scored NO @ 49c · p 0.5794 (adj 0.5297) · $7.28 · thesis FLA:SUPPRESSED
- Florida wins by over 1.5 goals NO @ 55c · p 0.6645 (adj 0.5836) · $1.46 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NJD @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Adin Hill (PROJECTED) exp shots 27.81, exp saves 24.54 (sd 6.49), pull risk 0.046
- NJD net: Connor Hellebuyck (PROJECTED) exp shots 27.33, exp saves 23.32 (sd 6.53), pull risk 0.068

**WPG @ FLA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 25.38, exp saves 22.26 (sd 6.01), pull risk 0.05
- WPG net: Nico Daws (PROJECTED) exp shots 27.89, exp saves 23.77 (sd 6.66), pull risk 0.074

**SEA @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 27.64, exp saves 23.78 (sd 6.64), pull risk 0.068
- SEA net: Joey Daccord (PROJECTED) exp shots 29.7, exp saves 25.73 (sd 6.94), pull risk 0.062

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
