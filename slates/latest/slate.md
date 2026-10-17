# NHL slate 2026-10-16 — RESEARCH_ONLY

generated 2026-10-17T01:21:00Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 1 · markets on board: 2976 · contracts joined: 238 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 213, 'OK': 15, 'NO_EDGE': 10}
families: {'period_winner': 9, 'period_spread': 6, 'period_total': 9, 'player_assists': 37, 'game_early_goal': 1, 'first_goal': 36, 'game_winner': 2, 'player_goals': 59, 'game_overtime': 1, 'player_points': 53, 'goalie_saves': 2, 'game_spread': 4, 'team_total': 10, 'game_total': 9}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ ANA | 2026-10-17T02:00:00Z | T-30m | 0.539 | 0.461 | 0.170 | 6.64 | 3.44 | 3.20 | 238 (25/213) | CONFIRMED/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA5 | team_total | 0.271 | 0.225 | 0.234 | 23 | 78 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT16BOSANA-9 | game_total | 0.235 | 0.195 | 0.203 | 20 | 81 | yes | +0.024 | OK |
| KXNHLTOTAL-26OCT16BOSANA-8 | game_total | 0.327 | 0.285 | 0.293 | 29 | 72 | yes | +0.023 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLGAME-26OCT16BOSANA-ANA | game_winner | 0.539 | 0.495 | 0.504 | 50 | 51 | yes | +0.021 | OK |
| KXNHLGAME-26OCT16BOSANA-BOS | game_winner | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.021 | OK |
| KXNHLSPREAD-26OCT16BOSANA-ANA2 | game_spread | 0.323 | 0.285 | 0.292 | 29 | 72 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA6 | team_total | 0.131 | 0.100 | 0.106 | 11 | 91 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT16BOSANA-BOS2 | game_spread | 0.261 | 0.295 | 0.288 | 30 | 71 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 | team_total | 0.461 | 0.420 | 0.428 | 43 | 59 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT16BOSANA-10 | game_total | 0.117 | 0.090 | 0.095 | 10 | 92 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA3 | team_total | 0.673 | 0.640 | 0.647 | 65 | 37 | yes | +0.007 | OK |
| KXNHLTOTAL-26OCT16BOSANA-7 | game_total | 0.524 | 0.495 | 0.501 | 50 | 51 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT16BOSANA-6 | game_total | 0.632 | 0.605 | 0.611 | 61 | 40 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-ANA2 | team_total | 0.855 | 0.835 | 0.839 | 84 | 17 | yes | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS2 | team_total | 0.821 | 0.840 | 0.836 | 85 | 17 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLSPREAD-26OCT16BOSANA-ANA3 | game_spread | 0.200 | 0.185 | 0.188 | 19 | 82 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-3 | game_total | 0.975 | 0.975 | 0.975 | 98 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-4 | game_total | 0.889 | 0.885 | 0.886 | 89 | 12 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS3 | team_total | 0.624 | 0.640 | 0.637 | 65 | 37 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT16BOSANA-5 | game_total | 0.820 | 0.825 | 0.824 | 83 | 18 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS5 | team_total | 0.229 | 0.225 | 0.226 | 23 | 78 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS6 | team_total | 0.103 | 0.100 | 0.101 | 11 | 91 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT16BOSANA-BOS4 | team_total | 0.410 | 0.415 | 0.414 | 42 | 59 |  | -0.017 | NO_EDGE |
| KXNHL1P-26OCT16BOSANA-ANA | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-BOS | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT16BOSANA-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16BOSANA-ANA2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT16BOSANA-BOS2 | period_spread |  | 0.105 |  | 12 | 91 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16BOSANA-1 | period_total |  | 0.835 |  | 84 | 17 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16BOSANA-2 | period_total |  | 0.555 |  | 56 | 45 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT16BOSANA-3 | period_total |  | 0.285 |  | 29 | 72 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16BOSANA-ANA | period_winner |  | 0.345 |  | 36 | 67 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16BOSANA-BOS | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT16BOSANA-TIE | period_winner |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16BOSANA-ANA2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT16BOSANA-BOS2 | period_spread |  | 0.115 |  | 13 | 90 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16BOSANA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16BOSANA-2 | period_total |  | 0.620 |  | 63 | 39 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT16BOSANA-3 | period_total |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16BOSANA-ANA | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16BOSANA-BOS | period_winner |  | 0.360 |  | 37 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT16BOSANA-TIE | period_winner |  | 0.255 |  | 27 | 76 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16BOSANA-ANA2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT16BOSANA-BOS2 | period_spread |  | 0.145 |  | 16 | 87 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16BOSANA-1 | period_total |  | 0.910 |  | 93 | 11 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16BOSANA-2 | period_total |  | 0.660 |  | 67 | 35 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT16BOSANA-3 | period_total |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAAGREER18-1 | player_assists |  |  |  | 18 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAAKILLORN17-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAAKILLORN17-2 | player_assists |  | 0.040 |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANABSENNECKE45-1 | player_assists |  | 0.390 |  | 40 | 62 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANABSENNECKE45-2 | player_assists |  | 0.065 |  | 9 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANACGAUTHIER61-1 | player_assists |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANACGAUTHIER61-2 | player_assists |  | 0.080 |  | 9 | 93 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAFVATRANO77-1 | player_assists |  | 0.120 |  | 19 | 95 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAJCAULFIELD28-1 | player_assists |  | 0.275 |  | 28 | 73 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAJCAULFIELD28-2 | player_assists |  | 0.045 |  | 6 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-1 | player_assists |  | 0.470 |  | 48 | 54 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAJLACOMBE2-2 | player_assists |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANAJMALOTT39-1 | player_assists |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANALCARLSSON91-1 | player_assists |  | 0.430 |  | 44 | 58 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANALCARLSSON91-2 | player_assists |  | 0.120 |  | 14 | 90 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANANKLEPOV40-1 | player_assists |  | 0.225 |  | 23 | 78 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANANNESTERENKO13-1 | player_assists |  | 0.225 |  | 24 | 79 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-ANATWASHE42-1 | player_assists |  |  |  | 17 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-1 | player_assists |  | 0.455 |  | 46 | 55 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSCMCAVOY73-2 | player_assists |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSCMITTELSTADT11-1 | player_assists |  | 0.265 |  | 27 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSCMITTELSTADT11-2 | player_assists |  | 0.040 |  | 5 | 97 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSDPASTRNAK88-1 | player_assists |  | 0.535 |  | 54 | 47 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSDPASTRNAK88-2 | player_assists |  | 0.160 |  | 18 | 86 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSELINDHOLM28-1 | player_assists |  | 0.305 |  | 31 | 70 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSELINDHOLM28-2 | player_assists |  |  |  | 5 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSFMINTEN93-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSFMINTEN93-2 | player_assists |  | 0.050 |  | 6 | 96 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSJHAGENS44-1 | player_assists |  |  |  | 23 |  |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSJPETERKA10-1 | player_assists |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT16BOSANA-BOSMGEEKIE39-1 | player_assists |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BOS @ ANA | 0.539 | 0.548 | 0.170 | 0.213 | 6.64 | 6.76 | 1.016/0.999 | KXNHLTEAMTOTAL-26OCT16BOSANA-ANA4 +0.023 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 4 recommended · full analysis in card.md / packet.json `thesis_card`

- A.J. Greer: 1+ goals YES @ 14c · p 0.2351 (adj 0.17) · $4.79 · thesis ANA:OFFENSE_4PLUS
- Tim Washe: 1+ goals YES @ 10c · p 0.1342 (adj 0.1232) · $4.38 · thesis ANA:OFFENSE_4PLUS
- Nikita Klepov: 1+ assists NO @ 78c · p 0.8516 (adj 0.8133) · $20.0 · thesis ANA:SUPPRESSED
- David Pastrnak: 1+ goals NO @ 62c · p 0.676 (adj 0.6595) · $15.76 · thesis BOS:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BOS @ ANA** · priced 186/187 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- ANA net: Lukas Dostal (CONFIRMED) exp shots 25.7, exp saves 22.26 (sd 6.19), pull risk 0.065
- BOS net: Michael DiPietro (CONFIRMED) exp shots 31.08, exp saves 26.46 (sd 7.29), pull risk 0.086

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tim Washe: 1+ points | 0.369 | 0.240 | 25/77 | +0.106 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.327 | 0.455 | 46/55 | +0.105 | STANDARD |
| A.J. Greer: 1+ points | 0.366 | 0.260 | 27/75 | +0.083 | STANDARD |
| Charlie McAvoy: 1+ points | 0.422 | 0.525 | 53/48 | +0.081 | STANDARD |
| Tristan Luneau: 1+ points | 0.368 | 0.265 | 27/74 | +0.084 | STANDARD |
| A.J. Greer: 1+ goals | 0.235 | 0.135 | 14/87 | +0.087 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
