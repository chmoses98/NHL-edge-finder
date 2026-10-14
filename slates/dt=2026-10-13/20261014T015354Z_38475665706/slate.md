# NHL slate 2026-10-13 — RESEARCH_ONLY

generated 2026-10-14T01:53:54Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 16 · simulated (not started): 2 · markets on board: 4861 · contracts joined: 522 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 472, 'NO_EDGE': 29, 'OK': 21}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 95, 'game_early_goal': 2, 'first_goal': 75, 'game_winner': 4, 'player_goals': 123, 'game_overtime': 2, 'player_points': 123, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ LAK | 2026-10-14T02:30:00Z | T-30m | 0.440 | 0.560 | 0.173 | 6.27 | 2.94 | 3.33 | 245 (25/220) | CONFIRMED/CONFIRMED |
| BOS @ SJS | 2026-10-14T03:00:00Z | T-60m | 0.413 | 0.587 | 0.175 | 6.17 | 2.82 | 3.36 | 277 (25/252) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT13BOSSJ-SJ3 | game_spread | 0.122 | 0.175 | 0.163 | 18 | 83 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 | team_total | 0.539 | 0.595 | 0.584 | 60 | 41 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-SJ2 | game_spread | 0.214 | 0.265 | 0.254 | 27 | 74 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ4 | team_total | 0.324 | 0.375 | 0.364 | 38 | 63 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS2 | game_spread | 0.359 | 0.315 | 0.324 | 32 | 69 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ2 | team_total | 0.757 | 0.800 | 0.792 | 81 | 21 | no | +0.021 | OK |
| KXNHLGAME-26OCT13BOSSJ-BOS | game_winner | 0.587 | 0.545 | 0.554 | 55 | 46 | yes | +0.020 | OK |
| KXNHLGAME-26OCT13BOSSJ-SJ | game_winner | 0.413 | 0.455 | 0.446 | 46 | 55 | no | +0.020 | OK |
| KXNHLSPREAD-26OCT13EDMLA-LA3 | game_spread | 0.135 | 0.165 | 0.159 | 17 | 84 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ5 | team_total | 0.164 | 0.195 | 0.188 | 20 | 81 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS6 | team_total | 0.121 | 0.095 | 0.100 | 10 | 91 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT13BOSSJ-BOS3 | game_spread | 0.231 | 0.205 | 0.210 | 21 | 80 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-5 | game_total | 0.769 | 0.795 | 0.790 | 80 | 21 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-4 | game_total | 0.853 | 0.875 | 0.871 | 88 | 13 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM6 | team_total | 0.115 | 0.095 | 0.099 | 10 | 91 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ6 | team_total | 0.067 | 0.085 | 0.081 | 9 | 92 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS3 | team_total | 0.662 | 0.635 | 0.640 | 64 | 37 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT13BOSSJ-3 | game_total | 0.964 | 0.975 | 0.973 | 98 | 3 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA2 | team_total | 0.784 | 0.805 | 0.801 | 81 | 20 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT13EDMLA-3 | game_total | 0.965 | 0.975 | 0.973 | 98 | 3 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA4 | team_total | 0.352 | 0.375 | 0.370 | 38 | 63 | no | +0.002 | OK |
| KXNHLSPREAD-26OCT13EDMLA-LA2 | game_spread | 0.237 | 0.255 | 0.251 | 26 | 75 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS5 | team_total | 0.252 | 0.235 | 0.238 | 24 | 77 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-10 | game_total | 0.083 | 0.075 | 0.076 | 8 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-7 | game_total | 0.446 | 0.465 | 0.461 | 47 | 54 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-6 | game_total | 0.557 | 0.575 | 0.571 | 58 | 43 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA3 | team_total | 0.567 | 0.585 | 0.581 | 59 | 42 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT13EDMLA-EDM2 | game_spread | 0.340 | 0.325 | 0.328 | 33 | 68 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS2 | team_total | 0.844 | 0.830 | 0.833 | 84 | 18 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM5 | team_total | 0.248 | 0.230 | 0.233 | 24 | 78 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-8 | game_total | 0.267 | 0.255 | 0.257 | 26 | 75 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-5 | game_total | 0.785 | 0.795 | 0.793 | 80 | 21 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-2 | game_total | 0.986 | 0.990 | 0.989 |  | 2 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-9 | game_total | 0.177 | 0.185 | 0.183 | 19 | 82 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT13EDMLA-EDM | game_winner | 0.560 | 0.545 | 0.548 | 55 | 46 |  | -0.008 | NO_EDGE |
| KXNHLGAME-26OCT13EDMLA-LA | game_winner | 0.440 | 0.455 | 0.452 | 46 | 55 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT13BOSSJ-8 | game_total | 0.255 | 0.265 | 0.263 | 27 | 74 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-10 | game_total | 0.087 | 0.085 | 0.085 | 9 | 92 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA6 | team_total | 0.076 | 0.075 | 0.075 | 8 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM3 | team_total | 0.656 | 0.645 | 0.647 | 65 | 36 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-LA5 | team_total | 0.181 | 0.185 | 0.184 | 19 | 82 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-4 | game_total | 0.866 | 0.865 | 0.865 | 87 | 14 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-9 | game_total | 0.187 | 0.185 | 0.185 | 19 | 82 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM2 | team_total | 0.843 | 0.840 | 0.841 | 85 | 17 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT13EDMLA-EDM3 | game_spread | 0.214 | 0.215 | 0.215 | 22 | 79 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-7 | game_total | 0.462 | 0.465 | 0.464 | 47 | 54 |  | -0.019 | NO_EDGE |
| KXNHLTOTAL-26OCT13EDMLA-6 | game_total | 0.577 | 0.575 | 0.575 | 58 | 43 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13BOSSJ-BOS4 | team_total | 0.444 | 0.440 | 0.441 | 45 | 57 |  | -0.024 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT13EDMLA-EDM4 | team_total | 0.441 | 0.440 | 0.440 | 45 | 57 |  | -0.026 | NO_EDGE |
| KXNHL1P-26OCT13EDMLA-EDM | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT13EDMLA-LA | period_winner |  | 0.315 |  | 32 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT13EDMLA-TIE | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT13EDMLA-EDM2 | period_spread |  | 0.105 |  | 11 | 90 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT13EDMLA-LA2 | period_spread |  | 0.085 |  | 9 | 92 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT13EDMLA-1 | period_total |  | 0.825 |  | 83 | 18 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT13EDMLA-2 | period_total |  | 0.540 |  | 55 | 47 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT13EDMLA-3 | period_total |  | 0.265 |  | 28 | 75 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT13EDMLA-EDM | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT13EDMLA-LA | period_winner |  | 0.320 |  | 33 | 69 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT13EDMLA-TIE | period_winner |  | 0.305 |  | 32 | 71 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT13EDMLA-EDM2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT13EDMLA-LA2 | period_spread |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT13EDMLA-1 | period_total |  | 0.895 |  | 91 | 12 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT13EDMLA-2 | period_total |  | 0.610 |  | 62 | 40 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT13EDMLA-3 | period_total |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT13EDMLA-EDM | period_winner |  | 0.395 |  | 40 | 61 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT13EDMLA-LA | period_winner |  | 0.355 |  | 36 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT13EDMLA-TIE | period_winner |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT13EDMLA-EDM2 | period_spread |  | 0.160 |  | 17 | 85 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT13EDMLA-LA2 | period_spread |  | 0.135 |  | 14 | 87 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT13EDMLA-1 | period_total |  | 0.920 |  | 93 | 9 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT13EDMLA-2 | period_total |  | 0.665 |  | 67 | 34 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT13EDMLA-3 | period_total |  | 0.385 |  | 39 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13EDMLA-EDMAFORMENTON26-1 | player_assists |  | 0.100 |  | 18 | 98 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-1 | player_assists |  | 0.635 |  | 64 | 37 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-2 | player_assists |  | 0.260 |  | 28 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13EDMLA-EDMCMCDAVID97-3 | player_assists |  | 0.075 |  | 8 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13EDMLA-EDMCMURPHY5-1 | player_assists |  | 0.205 |  | 22 | 81 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT13EDMLA-EDMEBOUCHARD2-1 | player_assists |  | 0.565 |  | 57 | 44 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| EDM @ LAK | 0.440 | 0.480 | 0.173 | 0.218 | 6.27 | 6.25 | 0.995/0.994 | KXNHLSPREAD-26OCT13EDMLA-EDM2 -0.043 |
| BOS @ SJS | 0.413 | 0.507 | 0.175 | 0.216 | 6.17 | 6.40 | 1.039/0.956 | KXNHLTEAMTOTAL-26OCT13BOSSJ-SJ3 +0.094 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Artemi Panarin: 2+ assists NO @ 82c · p 0.9048 (adj 0.8599) · $20.0 · thesis LAK:SUPPRESSED
- Kasperi Kapanen: 1+ assists YES @ 25c · p 0.3335 (adj 0.2893) · $8.53 · thesis EDM:OFFENSE_4PLUS
- Leon Draisaitl: 1+ assists NO @ 41c · p 0.5647 (adj 0.4449) · $8.6 · thesis EDM:SUPPRESSED
- Trevor Moore: 1+ goals YES @ 20c · p 0.2328 (adj 0.2233) · $3.77 · thesis LAK:OFFENSE_4PLUS
- Casey Mittelstadt: 1+ goals YES @ 14c · p 0.1849 (adj 0.1724) · $6.98 · thesis BOS:OFFENSE_4PLUS
- Charlie McAvoy: 1+ assists NO @ 55c · p 0.7032 (adj 0.6004) · $20.0 · thesis BOS:SUPPRESSED
- Marat Khusnutdinov: 1+ goals YES @ 11c · p 0.148 (adj 0.1372) · $5.52 · thesis BOS:OFFENSE_4PLUS
- Kiefer Sherwood: 1+ goals YES @ 17c · p 0.2154 (adj 0.2028) · $6.44 · thesis SJS:OFFENSE_4PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**EDM @ LAK** · priced 191/194 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- LAK net: Darcy Kuemper (CONFIRMED) exp shots 28.16, exp saves 24.3 (sd 6.72), pull risk 0.065
- EDM net: Devon Levi (CONFIRMED) exp shots 27.62, exp saves 23.94 (sd 6.59), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Joel Edmundson: 1+ points | 0.274 | 0.090 | 15/97 | +0.115 | STANDARD |
| Leon Draisaitl: 1+ assists | 0.435 | 0.595 | 60/41 | +0.138 | STANDARD |
| Joel Edmundson: 1+ assists | 0.226 | 0.070 | 12/98 | +0.099 | STANDARD |
| Connor McDavid: 1+ assists | 0.481 | 0.635 | 64/37 | +0.132 | STANDARD |
| Brian Dumoulin: 1+ assists | 0.213 | 0.075 | 13/98 | +0.075 | STANDARD |
| Connor McDavid: 2+ points | 0.337 | 0.475 | 49/54 | +0.105 | STANDARD |

**BOS @ SJS** · priced 219/226 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- SJS net: Yaroslav Askarov (CONFIRMED) exp shots 26.63, exp saves 22.95 (sd 6.44), pull risk 0.069
- BOS net: Jeremy Swayman (CONFIRMED) exp shots 27.58, exp saves 23.85 (sd 6.47), pull risk 0.06

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie McAvoy: 1+ points | 0.396 | 0.555 | 56/45 | +0.137 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.297 | 0.455 | 46/55 | +0.136 | STANDARD |
| Macklin Celebrini: 1+ assists | 0.420 | 0.565 | 57/44 | +0.123 | STANDARD |
| Jeremy Swayman: 25+ saves | 0.455 | 0.310 | 53/91 | -0.092 |  |
| Sam Dickinson: 1+ assists | 0.215 | 0.075 | 13/98 | +0.077 | STANDARD |
| Nikita Zadorov: 1+ assists | 0.230 | 0.095 | 17/98 | +0.050 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
