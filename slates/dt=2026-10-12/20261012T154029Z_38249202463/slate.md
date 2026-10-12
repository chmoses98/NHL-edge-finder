# NHL slate 2026-10-12 — RESEARCH_ONLY

generated 2026-10-12T15:40:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 3140 · contracts joined: 667 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 592, 'OK': 32, 'NO_EDGE': 43}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 94, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 188, 'game_overtime': 3, 'player_points': 123, 'goalie_saves': 2, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 2026-10-12T17:00:00Z | T-60m | 0.621 | 0.379 | 0.166 | 6.29 | 3.54 | 2.76 | 222 (25/197) | PROJECTED/CONFIRMED |
| OTT @ NJD | 2026-10-12T23:00:00Z | T-6h | 0.524 | 0.476 | 0.175 | 6.07 | 3.10 | 2.96 | 223 (25/198) | PROBABLE/PROJECTED |
| VGK @ MIN | 2026-10-13T00:00:00Z | T-6h | 0.532 | 0.468 | 0.176 | 6.11 | 3.16 | 2.96 | 222 (25/197) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT12FLABUF-FLA | game_winner | 0.379 | 0.495 | 0.471 | 50 | 51 | no | +0.094 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF2 | game_spread | 0.400 | 0.295 | 0.315 | 30 | 71 | yes | +0.086 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA2 | game_spread | 0.191 | 0.295 | 0.272 | 30 | 71 | no | +0.084 | OK |
| KXNHLGAME-26OCT12FLABUF-BUF | game_winner | 0.621 | 0.515 | 0.537 | 52 | 49 | yes | +0.084 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF4 | team_total | 0.487 | 0.385 | 0.405 | 39 | 62 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3 | team_total | 0.695 | 0.595 | 0.616 | 60 | 41 | yes | +0.078 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF5 | team_total | 0.285 | 0.200 | 0.215 | 21 | 81 | yes | +0.063 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF3 | game_spread | 0.261 | 0.185 | 0.199 | 19 | 82 | yes | +0.060 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA3 | game_spread | 0.105 | 0.175 | 0.158 | 18 | 83 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF6 | team_total | 0.142 | 0.080 | 0.090 | 9 | 93 | yes | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF2 | team_total | 0.866 | 0.805 | 0.819 | 81 | 20 | yes | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA4 | team_total | 0.311 | 0.375 | 0.362 | 38 | 63 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA3 | team_total | 0.521 | 0.590 | 0.576 | 60 | 42 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA2 | team_total | 0.749 | 0.810 | 0.799 | 82 | 20 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT12FLABUF-7 | game_total | 0.462 | 0.415 | 0.424 | 42 | 59 | yes | +0.025 | OK |
| KXNHLTOTAL-26OCT12FLABUF-8 | game_total | 0.276 | 0.235 | 0.243 | 24 | 77 | yes | +0.023 | OK |
| KXNHLTOTAL-26OCT12FLABUF-6 | game_total | 0.579 | 0.535 | 0.544 | 54 | 47 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA5 | team_total | 0.155 | 0.190 | 0.183 | 20 | 82 | no | +0.015 | OK |
| KXNHLGAME-26OCT12VGKMIN-MIN | game_winner | 0.532 | 0.495 | 0.502 | 50 | 51 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA6 | team_total | 0.062 | 0.090 | 0.084 | 10 | 92 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT12FLABUF-9 | game_total | 0.191 | 0.165 | 0.170 | 17 | 84 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK3 | game_spread | 0.149 | 0.175 | 0.169 | 18 | 83 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT12OTTNJ-NJ3 | game_spread | 0.181 | 0.205 | 0.200 | 21 | 80 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-MIN2 | game_spread | 0.312 | 0.285 | 0.290 | 29 | 72 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK2 | game_spread | 0.258 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT12FLABUF-10 | game_total | 0.090 | 0.075 | 0.078 | 8 | 93 | yes | +0.005 | OK |
| KXNHLGAME-26OCT12VGKMIN-VGK | game_winner | 0.468 | 0.495 | 0.490 | 50 | 51 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN5 | team_total | 0.216 | 0.195 | 0.199 | 20 | 81 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK2 | team_total | 0.785 | 0.805 | 0.801 | 81 | 20 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-5 | game_total | 0.754 | 0.775 | 0.771 | 78 | 23 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN3 | team_total | 0.620 | 0.595 | 0.600 | 60 | 41 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT12OTTNJ-NJ2 | game_spread | 0.304 | 0.325 | 0.321 | 33 | 68 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK3 | team_total | 0.574 | 0.595 | 0.591 | 60 | 41 |  | -0.001 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-OTT | game_winner | 0.476 | 0.455 | 0.459 | 46 | 55 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT2 | team_total | 0.790 | 0.775 | 0.778 | 78 | 23 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK5 | team_total | 0.181 | 0.195 | 0.192 | 20 | 81 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 | team_total | 0.356 | 0.375 | 0.371 | 38 | 63 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-4 | game_total | 0.844 | 0.855 | 0.853 | 86 | 15 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK6 | team_total | 0.078 | 0.090 | 0.087 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN2 | team_total | 0.817 | 0.805 | 0.808 | 81 | 20 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-5 | game_total | 0.761 | 0.775 | 0.772 | 78 | 23 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ4 | team_total | 0.388 | 0.405 | 0.401 | 41 | 60 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-4 | game_total | 0.863 | 0.855 | 0.857 | 86 | 15 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-3 | game_total | 0.967 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-10 | game_total | 0.079 | 0.075 | 0.076 | 8 | 93 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-4 | game_total | 0.847 | 0.860 | 0.858 | 87 | 15 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT6 | team_total | 0.079 | 0.070 | 0.072 | 8 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ5 | team_total | 0.205 | 0.215 | 0.213 | 22 | 79 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3 | team_total | 0.612 | 0.625 | 0.622 | 63 | 38 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-9 | game_total | 0.169 | 0.175 | 0.174 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-10 | game_total | 0.076 | 0.075 | 0.075 | 8 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ2 | team_total | 0.809 | 0.820 | 0.818 | 83 | 19 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN6 | team_total | 0.097 | 0.085 | 0.087 | 10 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-5 | game_total | 0.783 | 0.770 | 0.773 | 78 | 24 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT2 | game_spread | 0.264 | 0.255 | 0.257 | 26 | 75 |  | -0.010 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT3 | game_spread | 0.152 | 0.155 | 0.154 | 16 | 85 |  | -0.011 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-NJ | game_winner | 0.524 | 0.535 | 0.533 | 54 | 47 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-9 | game_total | 0.168 | 0.165 | 0.165 | 17 | 84 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT12VGKMIN-MIN3 | game_spread | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-7 | game_total | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT3 | team_total | 0.574 | 0.560 | 0.563 | 57 | 45 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-8 | game_total | 0.239 | 0.235 | 0.236 | 24 | 77 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ6 | team_total | 0.090 | 0.090 | 0.090 | 10 | 92 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-6 | game_total | 0.538 | 0.545 | 0.544 | 55 | 46 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN4 | team_total | 0.401 | 0.390 | 0.392 | 40 | 62 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-6 | game_total | 0.549 | 0.555 | 0.554 | 56 | 45 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-8 | game_total | 0.245 | 0.245 | 0.245 | 25 | 76 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT5 | team_total | 0.181 | 0.175 | 0.176 | 19 | 84 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT4 | team_total | 0.354 | 0.350 | 0.351 | 36 | 66 |  | -0.022 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-7 | game_total | 0.435 | 0.435 | 0.435 | 44 | 57 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT12FLABUF-BUF | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-FLA | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-TIE | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-BUF2 | period_spread |  | 0.095 |  | 12 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-FLA2 | period_spread |  | 0.085 |  | 10 | 93 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 0.621 | 0.576 | 0.166 | 0.217 | 6.29 | 6.17 | 0.997/1.015 | KXNHLSPREAD-26OCT12FLABUF-BUF2 -0.050 |
| OTT @ NJD | 0.524 | 0.494 | 0.175 | 0.222 | 6.07 | 5.93 | 0.994/0.998 | KXNHLSPREAD-26OCT12OTTNJ-NJ2 -0.038 |
| VGK @ MIN | 0.532 | 0.528 | 0.176 | 0.222 | 6.11 | 6.17 | 0.995/1.003 | KXNHLTOTAL-26OCT12VGKMIN-7 +0.018 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 11 recommended · full analysis in card.md / packet.json `thesis_card`

- Sam Reinhart: 1+ goals NO @ 68c · p 0.7513 (adj 0.7322) · $20.0 · thesis FLA:SUPPRESSED
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1383 (adj 0.1262) · $5.44 · thesis FLA:OFFENSE_4PLUS
- Florida wins by over 1.5 goals NO @ 71c · p 0.7836 (adj 0.7443) · $17.25 · thesis BUF:WINS
- Josh Norris: 1+ goals YES @ 19c · p 0.229 (adj 0.218) · $4.4 · thesis BUF:OFFENSE_4PLUS
- Warren Foegele: 1+ goals YES @ 11c · p 0.1572 (adj 0.1442) · $7.07 · thesis OTT:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 63c · p 0.7022 (adj 0.6829) · $20.0 · thesis NJD:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1768 (adj 0.1626) · $6.46 · thesis OTT:OFFENSE_4PLUS
- Amadeus Lombardi: 1+ goals YES @ 9c · p 0.1243 (adj 0.1145) · $4.79 · thesis NJD:WINS_BY_2PLUS
- Michael McCarron: 1+ goals YES @ 9c · p 0.1147 (adj 0.1073) · $2.94 · thesis MIN:OFFENSE_4PLUS
- Jack Eichel: 1+ goals NO @ 68c · p 0.723 (adj 0.711) · $13.52 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 72c · p 0.7591 (adj 0.7481) · $13.23 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ BUF** · priced 168/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.79 (sd 6.29), pull risk 0.054
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.92, exp saves 23.95 (sd 6.6), pull risk 0.067

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Noah Ostlund: 2+ assists | 0.052 | 0.265 | 52/99 | -0.042 | STANDARD |
| Brady Tkachuk: 1+ assists | 0.238 | 0.395 | 40/61 | +0.136 | STANDARD |
| Brady Tkachuk: 1+ points | 0.424 | 0.575 | 58/43 | +0.129 | STANDARD |
| Ryan McLeod: 1+ assists | 0.291 | 0.140 | 27/99 | +0.007 | STANDARD |
| Sam Reinhart: 1+ points | 0.460 | 0.565 | 57/44 | +0.083 | STANDARD |
| Sam Reinhart: 1+ assists | 0.280 | 0.375 | 38/63 | +0.073 | STANDARD |

**OTT @ NJD** · priced 170/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROBABLE) exp shots 27.04, exp saves 23.37 (sd 6.44), pull risk 0.054
- OTT net: Linus Ullmark (PROJECTED) exp shots 28.15, exp saves 24.36 (sd 6.61), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ points | 0.272 | 0.440 | 46/58 | +0.131 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.139 | 0.305 | 32/71 | +0.137 | STANDARD |
| Jack Hughes: 1+ assists | 0.372 | 0.520 | 53/49 | +0.121 | STANDARD |
| Jack Hughes: 2+ points | 0.194 | 0.335 | 35/68 | +0.111 | STANDARD |
| Luke Evangelista: 1+ assists | 0.218 | 0.355 | 37/66 | +0.107 | STANDARD |
| Luke Evangelista: 1+ points | 0.365 | 0.500 | 51/51 | +0.107 | STANDARD |

**VGK @ MIN** · priced 171/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.04, exp saves 25.4 (sd 6.81), pull risk 0.054
- VGK net: Carter Hart (PROJECTED) exp shots 27.87, exp saves 24.1 (sd 6.51), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Trevor Connelly: 2+ assists | 0.016 | 0.190 | 37/99 | -0.007 | PRIOR_HEAVY |
| Max Shabanov: 1+ points | 0.371 | 0.225 | 44/99 | -0.086 | STANDARD |
| Jack Eichel: 1+ assists | 0.421 | 0.545 | 55/46 | +0.102 | STANDARD |
| Jack Eichel: 1+ points | 0.582 | 0.685 | 69/32 | +0.083 | STANDARD |
| Trevor Connelly: 1+ assists | 0.184 | 0.285 | 30/73 | +0.072 | PRIOR_HEAVY |
| Mitch Marner: 1+ assists | 0.379 | 0.480 | 49/53 | +0.073 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
