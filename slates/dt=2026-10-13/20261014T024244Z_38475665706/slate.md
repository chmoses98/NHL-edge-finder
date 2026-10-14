# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-14T02:42:44Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 1 · markets on board: 3994 · contracts joined: 277 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 252, 'OK': 18, 'NO_EDGE': 7}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 52, 'game_early_goal': 1, 'first_goal': 39, 'game_winner': 2, 'player_goals': 64, 'game_overtime': 1, 'player_points': 69, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ SJS | 2026-10-14T03:00:00Z | T-10m | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 | team_total | 0.539 | 0.595 | 0.584 | 60 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ2 | team_total | 0.757 | 0.810 | 0.800 | 82 | 20 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 | team_total | 0.324 | 0.375 | 0.364 | 38 | 63 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.359 | 0.315 | 0.324 | 32 | 69 | yes | +0.024 | OK |
| KXNHLGAME-26OCT13BOSSJ-BOS | game_winner | 0.587 | 0.545 | 0.554 | 55 | 46 | yes | +0.020 | OK |
| KXNHLGAME-26OCT13BOSSJ-SJ | game_winner | 0.413 | 0.455 | 0.446 | 46 | 55 | no | +0.020 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-5 | game_total | 0.769 | 0.805 | 0.798 | 81 | 20 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ5 | team_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS6 | team_total | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS3 | game_spread | 0.231 | 0.205 | 0.210 | 21 | 80 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-4 | game_total | 0.853 | 0.875 | 0.871 | 88 | 13 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ6 | team_total | 0.067 | 0.085 | 0.081 | 9 | 92 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-6 | game_total | 0.557 | 0.585 | 0.579 | 59 | 42 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-7 | game_total | 0.446 | 0.475 | 0.469 | 48 | 53 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS3 | team_total | 0.662 | 0.635 | 0.640 | 64 | 37 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-3 | game_total | 0.964 | 0.975 | 0.973 | 98 | 3 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS5 | team_total | 0.252 | 0.235 | 0.238 | 24 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-10 | game_total | 0.083 | 0.075 | 0.076 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS2 | team_total | 0.844 | 0.835 | 0.837 | 84 | 17 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-9 | game_total | 0.177 | 0.185 | 0.183 | 19 | 82 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-8 | game_total | 0.255 | 0.265 | 0.263 | 27 | 74 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS4 | team_total | 0.444 | 0.445 | 0.445 | 45 | 56 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT13BOSSJ-BOS | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT13BOSSJ-SJ | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT13BOSSJ-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT13BOSSJ-BOS2 | period_spread |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT13BOSSJ-SJ2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT13BOSSJ-1 | period_total |  | 0.835 |  | 84 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT13BOSSJ-2 | period_total |  | 0.550 |  | 56 | 46 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT13BOSSJ-3 | period_total |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT13BOSSJ-BOS | period_winner |  | 0.360 |  | 38 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT13BOSSJ-SJ | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT13BOSSJ-TIE | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT13BOSSJ-BOS2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT13BOSSJ-SJ2 | period_spread |  | 0.110 |  | 12 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT13BOSSJ-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT13BOSSJ-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT13BOSSJ-3 | period_total |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT13BOSSJ-BOS | period_winner |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT13BOSSJ-SJ | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT13BOSSJ-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT13BOSSJ-BOS2 | period_spread |  | 0.165 |  | 17 | 84 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT13BOSSJ-SJ2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT13BOSSJ-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT13BOSSJ-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT13BOSSJ-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-1 | player_assists |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSCMCAVOY73-2 | player_assists |  | 0.120 |  | 13 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSCMITTELSTADT11-1 | player_assists |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSDPASTRNAK88-1 | player_assists |  | 0.515 |  | 53 | 50 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSDPASTRNAK88-2 | player_assists |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSELINDHOLM28-1 | player_assists |  | 0.290 |  | 30 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSELINDHOLM28-2 | player_assists |  | 0.045 |  | 5 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSFBRUNET42-1 | player_assists |  | 0.130 |  | 24 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSFMINTEN93-1 | player_assists |  | 0.240 |  | 25 | 77 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSHLINDHOLM27-1 | player_assists |  | 0.280 |  | 29 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSHLINDHOLM27-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSJHAGENS44-1 | player_assists |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSJPETERKA10-1 | player_assists |  | 0.255 |  | 26 | 75 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMGEEKIE39-1 | player_assists |  | 0.340 |  | 35 | 67 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMGEEKIE39-2 | player_assists |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMKASTELIC47-1 | player_assists |  | 0.130 |  | 17 | 91 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMKHUSNUTDINOV92-1 | player_assists |  | 0.130 |  | 24 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMLOHREI6-1 | player_assists |  | 0.305 |  | 33 | 72 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMLOHREI6-2 | player_assists |  | 0.055 |  | 7 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSMPOITRAS51-1 | player_assists |  | 0.135 |  | 16 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSNZADOROV91-1 | player_assists |  | 0.100 |  | 18 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSPZACHA18-1 | player_assists |  | 0.370 |  | 38 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSPZACHA18-2 | player_assists |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSTJEANNOT84-1 | player_assists |  | 0.125 |  | 17 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-BOSWBORGEN17-1 | player_assists |  | 0.115 |  | 21 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-SJAWENNBERG21-1 | player_assists |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-SJAWENNBERG21-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-SJBGOODROW23-1 | player_assists |  | 0.060 |  | 10 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-SJCGRAF51-1 | player_assists |  | 0.120 |  | 22 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-SJDNURSE25-1 | player_assists |  | 0.240 |  | 26 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13BOSSJ-SJDORLOV9-1 | player_assists |  | 0.300 |  | 32 | 72 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ SJS | 0.413 | 0.507 | 0.175 | 0.216 | 6.17 | 6.40 | 1.039/0.956 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 +0.094 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- Kiefer Sherwood: 1+ goals YES @ 16c · p 0.2154 (adj 0.2003) · $8.37 · thesis SJS:OFFENSE_4PLUS
- Mark Kastelic: 1+ goals YES @ 8c · p 0.1159 (adj 0.1057) · $5.16 · thesis BOS:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $6.99 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 55c · p 0.7032 (adj 0.6004) · $20.0 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BOS @ SJS** · priced 219/226 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.44), pull risk 0.069
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.58, exp saves 23.85 (sd 6.47), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.396 | 0.555 | 56/45 | +0.137 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.297 | 0.455 | 46/55 | +0.136 | STANDARD |
| Sam Dickinson: 1+ assists | 0.215 | 0.075 | 13/98 | +0.077 | STANDARD |
| Sam Dickinson: 1+ points | 0.265 | 0.125 | 17/92 | +0.085 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.555 | 56/45 | +0.113 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.230 | 0.100 | 18/98 | +0.040 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
