# NHL slate 2026-10-14 — RESEARCH_ONLY

generated 2026-10-14T23:25:15Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2792 · contracts joined: 516 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 466, 'NO_EDGE': 17, 'OK': 33}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'player_assists': 90, 'game_early_goal': 2, 'first_goal': 72, 'game_winner': 4, 'player_goals': 125, 'game_overtime': 2, 'player_points': 123, 'goalie_saves': 4, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ WSH | 2026-10-14T23:30:00Z | T-<10m | 0.519 | 0.481 | 0.175 | 6.44 | 3.29 | 3.15 | 266 (25/241) | CONFIRMED/CONFIRMED |
| DAL @ COL | 2026-10-15T00:30:00Z | T-60m | 0.615 | 0.385 | 0.180 | 5.60 | 3.15 | 2.45 | 250 (25/225) | PROBABLE/CONFIRMED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26OCT14DALCOL-5 | game_total | 0.688 | 0.785 | 0.768 | 79 | 22 | no | +0.080 | OK |
| KXNHLTOTAL-26OCT14DALCOL-6 | game_total | 0.463 | 0.565 | 0.545 | 57 | 44 | no | +0.079 | OK |
| KXNHLTOTAL-26OCT14DALCOL-7 | game_total | 0.350 | 0.445 | 0.425 | 45 | 56 | no | +0.073 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-DAL3 | team_total | 0.451 | 0.540 | 0.522 | 55 | 47 | no | +0.061 | OK |
| KXNHLTOTAL-26OCT14DALCOL-4 | game_total | 0.792 | 0.865 | 0.852 | 87 | 14 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-DAL2 | team_total | 0.694 | 0.765 | 0.752 | 77 | 24 | no | +0.053 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-DAL4 | team_total | 0.244 | 0.325 | 0.308 | 34 | 69 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT14DALCOL-8 | game_total | 0.178 | 0.250 | 0.234 | 26 | 76 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-DAL5 | team_total | 0.104 | 0.160 | 0.147 | 17 | 85 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT14MTLWSH-5 | game_total | 0.798 | 0.845 | 0.836 | 85 | 16 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT14DALCOL-9 | game_total | 0.119 | 0.170 | 0.159 | 18 | 84 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT14DALCOL-DAL3 | game_spread | 0.091 | 0.135 | 0.125 | 14 | 87 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-COL5 | team_total | 0.209 | 0.255 | 0.245 | 26 | 75 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-COL4 | team_total | 0.396 | 0.445 | 0.435 | 45 | 56 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-COL3 | team_total | 0.624 | 0.665 | 0.657 | 67 | 34 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-COL2 | team_total | 0.822 | 0.855 | 0.849 | 86 | 15 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT14MTLWSH-6 | game_total | 0.595 | 0.635 | 0.627 | 64 | 37 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT14DALCOL-3 | game_total | 0.939 | 0.965 | 0.961 | 97 | 4 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT14DALCOL-DAL2 | game_spread | 0.183 | 0.215 | 0.208 | 22 | 79 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT14DALCOL-10 | game_total | 0.051 | 0.075 | 0.069 | 8 | 93 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT14MTLWSH-4 | game_total | 0.874 | 0.895 | 0.891 | 90 | 11 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-DAL6 | team_total | 0.038 | 0.060 | 0.055 | 7 | 95 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT14DALCOL-COL6 | team_total | 0.095 | 0.115 | 0.111 | 12 | 89 | no | +0.009 | OK |
| KXNHLGAME-26OCT14DALCOL-COL | game_winner | 0.615 | 0.585 | 0.591 | 59 | 42 | yes | +0.008 | OK |
| KXNHLGAME-26OCT14DALCOL-DAL | game_winner | 0.385 | 0.415 | 0.409 | 42 | 59 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT14DALCOL-2 | game_total | 0.972 | 0.985 | 0.983 | 99 | 2 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-WSH4 | team_total | 0.426 | 0.455 | 0.449 | 46 | 55 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-WSH2 | team_total | 0.835 | 0.855 | 0.851 | 86 | 15 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT14MTLWSH-7 | game_total | 0.488 | 0.515 | 0.510 | 52 | 49 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-WSH3 | team_total | 0.640 | 0.665 | 0.660 | 67 | 34 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-WSH5 | team_total | 0.243 | 0.265 | 0.260 | 27 | 74 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT14MTLWSH-WSH3 | game_spread | 0.188 | 0.210 | 0.205 | 22 | 80 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT14MTLWSH-2 | game_total | 0.988 | 0.990 | 0.990 |  | 1 | no | +0.001 | OK |
| KXNHLSPREAD-26OCT14MTLWSH-MTL3 | game_spread | 0.160 | 0.175 | 0.172 | 18 | 83 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT14MTLWSH-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT14MTLWSH-8 | game_total | 0.296 | 0.315 | 0.311 | 32 | 69 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-MTL4 | team_total | 0.396 | 0.415 | 0.411 | 42 | 59 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-MTL6 | team_total | 0.100 | 0.095 | 0.096 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-MTL5 | team_total | 0.215 | 0.230 | 0.227 | 24 | 78 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-MTL2 | team_total | 0.818 | 0.825 | 0.824 | 83 | 18 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT14MTLWSH-WSH2 | game_spread | 0.306 | 0.315 | 0.313 | 32 | 69 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT14MTLWSH-10 | game_total | 0.106 | 0.105 | 0.105 | 11 | 90 |  | -0.011 | NO_EDGE |
| KXNHLSPREAD-26OCT14DALCOL-COL2 | game_spread | 0.375 | 0.365 | 0.367 | 37 | 64 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-WSH6 | team_total | 0.116 | 0.120 | 0.119 | 13 | 89 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT14DALCOL-COL3 | game_spread | 0.231 | 0.235 | 0.234 | 24 | 77 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT14MTLWSH-MTL3 | team_total | 0.617 | 0.625 | 0.623 | 63 | 38 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT14MTLWSH-MTL2 | game_spread | 0.270 | 0.275 | 0.274 | 28 | 73 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT14MTLWSH-9 | game_total | 0.212 | 0.220 | 0.218 | 23 | 79 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT14MTLWSH-WSH | game_winner | 0.519 | 0.525 | 0.524 | 53 | 48 |  | -0.017 | NO_EDGE |
| KXNHLGAME-26OCT14MTLWSH-MTL | game_winner | 0.481 | 0.480 | 0.480 | 49 | 53 |  | -0.027 | NO_EDGE |
| KXNHL1P-26OCT14MTLWSH-MTL | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT14MTLWSH-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT14MTLWSH-WSH | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT14MTLWSH-MTL2 | period_spread |  | 0.100 |  | 11 | 91 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT14MTLWSH-WSH2 | period_spread |  | 0.125 |  | 14 | 89 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT14MTLWSH-1 | period_total |  | 0.865 |  | 87 | 14 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT14MTLWSH-2 | period_total |  | 0.605 |  | 61 | 40 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT14MTLWSH-3 | period_total |  | 0.300 |  | 31 | 71 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT14MTLWSH-MTL | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT14MTLWSH-TIE | period_winner |  | 0.290 |  | 31 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT14MTLWSH-WSH | period_winner |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT14MTLWSH-MTL2 | period_spread |  | 0.125 |  | 13 | 88 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT14MTLWSH-WSH2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT14MTLWSH-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT14MTLWSH-2 | period_total |  | 0.645 |  | 66 | 37 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT14MTLWSH-3 | period_total |  | 0.365 |  | 38 | 65 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT14MTLWSH-MTL | period_winner |  | 0.350 |  | 36 | 66 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT14MTLWSH-TIE | period_winner |  | 0.250 |  | 26 | 76 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT14MTLWSH-WSH | period_winner |  | 0.385 |  | 40 | 63 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT14MTLWSH-MTL2 | period_spread |  | 0.140 |  | 15 | 87 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT14MTLWSH-WSH2 | period_spread |  | 0.165 |  | 18 | 85 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT14MTLWSH-1 | period_total |  | 0.915 |  | 93 | 10 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT14MTLWSH-2 | period_total |  | 0.690 |  | 70 | 32 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT14MTLWSH-3 | period_total |  | 0.415 |  | 42 | 59 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT14MTLWSH-MTLACARRIER45-1 | player_assists |  | 0.190 |  | 21 | 83 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT14MTLWSH-MTLANEWHOOK15-1 | player_assists |  | 0.220 |  | 24 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT14MTLWSH-MTLATEXIER85-1 | player_assists |  | 0.225 |  | 25 | 80 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT14MTLWSH-MTLCCAUFIELD13-1 | player_assists |  | 0.380 |  | 39 | 63 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT14MTLWSH-MTLCCAUFIELD13-2 | player_assists |  | 0.095 |  | 11 | 92 |  |  | UNSUPPORTED |
| KXNHLAST-26OCT14MTLWSH-MTLCKREIDER22-1 | player_assists |  | 0.270 |  | 28 | 74 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| MTL @ WSH | 0.519 | 0.534 | 0.175 | 0.221 | 6.44 | 6.32 | 1.015/0.942 | KXNHLTOTAL-26OCT14MTLWSH-8 -0.027 |
| DAL @ COL | 0.615 | 0.603 | 0.180 | 0.215 | 5.60 | 6.14 | 0.972/0.968 | KXNHLTOTAL-26OCT14DALCOL-7 +0.090 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Aliaksei Protas: 1+ goals YES @ 18c · p 0.2387 (adj 0.2228) · $9.97 · thesis WSH:OFFENSE_4PLUS
- Ryan Leonard: 1+ assists YES @ 31c · p 0.3933 (adj 0.3467) · $7.91 · thesis WSH:OFFENSE_4PLUS
- Justin Sourdif: 1+ goals YES @ 13c · p 0.1615 (adj 0.1524) · $3.99 · thesis WSH:OFFENSE_4PLUS
- Full Game: Over 5.5 goals scored NO @ 37c · p 0.4302 (adj 0.3976) · $9.68 · thesis GAME:LOW_EVENT
- Josh Manson: 1+ goals YES @ 4c · p 0.077 (adj 0.0678) · $5.43 · thesis COL:OFFENSE_4PLUS
- Nathan MacKinnon: 3+ assists NO @ 92c · p 0.9695 (adj 0.9423) · $19.96 · thesis COL:SUPPRESSED
- Devon Toews: 1+ assists YES @ 30c · p 0.3863 (adj 0.3407) · $8.97 · thesis COL:OFFENSE_4PLUS
- Tyler Seguin: 1+ assists NO @ 71c · p 0.7802 (adj 0.7401) · $15.64 · thesis DAL:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**MTL @ WSH** · priced 201/215 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Charlie Lindgren (CONFIRMED) exp shots 26.21, exp saves 22.72 (sd 6.36), pull risk 0.059
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.03, exp saves 24.26 (sd 6.69), pull risk 0.066

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Alex Tuch: 1+ assists | 0.233 | 0.345 | 36/67 | +0.082 | STANDARD |
| Alex Tuch: 1+ points | 0.460 | 0.555 | 57/46 | +0.063 | STANDARD |
| Nick Suzuki: 1+ assists | 0.460 | 0.555 | 57/46 | +0.062 | STANDARD |
| Ryan Leonard: 1+ assists | 0.393 | 0.300 | 31/71 | +0.068 | STANDARD |
| Chris Kreider: 1+ points | 0.385 | 0.465 | 48/55 | +0.048 | STANDARD |
| Justin Sourdif: 1+ points | 0.400 | 0.320 | 33/69 | +0.054 | STANDARD |

**DAL @ COL** · priced 191/199 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Scott Wedgewood (PROBABLE) exp shots 24.58, exp saves 21.61 (sd 5.93), pull risk 0.044
- DAL net: Casey DeSmith (CONFIRMED) exp shots 29.48, exp saves 25.16 (sd 6.85), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nathan MacKinnon: 2+ points | 0.341 | 0.490 | 50/52 | +0.122 | STANDARD |
| Jason Robertson: 1+ assists | 0.343 | 0.455 | 47/56 | +0.080 | STANDARD |
| Mikko Rantanen: 2+ points | 0.186 | 0.295 | 32/73 | +0.070 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.382 | 0.490 | 50/52 | +0.080 | STANDARD |
| Brett Kulak: 1+ assists | 0.212 | 0.115 | 22/99 | -0.020 | STANDARD |
| Jason Robertson: 2+ points | 0.213 | 0.310 | 33/71 | +0.062 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
