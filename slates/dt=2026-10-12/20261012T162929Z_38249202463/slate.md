# NHL slate 2026-10-12 — RESEARCH_ONLY

generated 2026-10-12T16:29:29Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 3143 · contracts joined: 670 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 595, 'OK': 36, 'NO_EDGE': 39}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'player_assists': 95, 'game_early_goal': 3, 'first_goal': 107, 'game_winner': 6, 'player_goals': 188, 'game_overtime': 3, 'player_points': 125, 'goalie_saves': 2, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 2026-10-12T17:00:00Z | T-30m | 0.626 | 0.374 | 0.168 | 6.31 | 3.55 | 2.76 | 225 (25/200) | CONFIRMED/CONFIRMED |
| OTT @ NJD | 2026-10-12T23:00:00Z | T-6h | 0.528 | 0.472 | 0.175 | 6.10 | 3.14 | 2.96 | 223 (25/198) | PROBABLE/CONFIRMED |
| VGK @ MIN | 2026-10-13T00:00:00Z | T-6h | 0.543 | 0.457 | 0.181 | 6.06 | 3.16 | 2.90 | 222 (25/197) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT12FLABUF-BUF | game_winner | 0.626 | 0.515 | 0.538 | 52 | 49 | yes | +0.088 | OK |
| KXNHLGAME-26OCT12FLABUF-FLA | game_winner | 0.374 | 0.485 | 0.462 | 49 | 52 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF2 | game_spread | 0.401 | 0.295 | 0.315 | 30 | 71 | yes | +0.086 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF4 | team_total | 0.487 | 0.380 | 0.401 | 39 | 63 | yes | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3 | team_total | 0.697 | 0.595 | 0.616 | 60 | 41 | yes | +0.080 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA2 | game_spread | 0.191 | 0.285 | 0.264 | 29 | 72 | no | +0.074 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF5 | team_total | 0.287 | 0.200 | 0.216 | 21 | 81 | yes | +0.065 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF3 | game_spread | 0.263 | 0.185 | 0.199 | 19 | 82 | yes | +0.062 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA3 | game_spread | 0.105 | 0.175 | 0.159 | 18 | 83 | no | +0.055 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF6 | team_total | 0.143 | 0.080 | 0.090 | 9 | 93 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF2 | team_total | 0.868 | 0.805 | 0.819 | 81 | 20 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA4 | team_total | 0.309 | 0.375 | 0.361 | 38 | 63 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA3 | team_total | 0.523 | 0.590 | 0.577 | 60 | 42 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA2 | team_total | 0.751 | 0.805 | 0.795 | 81 | 20 | no | +0.038 | OK |
| KXNHLTOTAL-26OCT12FLABUF-7 | game_total | 0.466 | 0.415 | 0.425 | 42 | 59 | yes | +0.029 | OK |
| KXNHLGAME-26OCT12VGKMIN-MIN | game_winner | 0.543 | 0.495 | 0.505 | 50 | 51 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT12FLABUF-8 | game_total | 0.273 | 0.235 | 0.242 | 24 | 77 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT12FLABUF-6 | game_total | 0.577 | 0.535 | 0.544 | 54 | 47 | yes | +0.020 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK2 | game_spread | 0.246 | 0.285 | 0.277 | 29 | 72 | no | +0.020 | OK |
| KXNHLGAME-26OCT12VGKMIN-VGK | game_winner | 0.457 | 0.495 | 0.487 | 50 | 51 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA5 | team_total | 0.154 | 0.190 | 0.182 | 20 | 82 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK3 | game_spread | 0.145 | 0.175 | 0.169 | 18 | 83 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT12FLABUF-9 | game_total | 0.195 | 0.165 | 0.171 | 17 | 84 | yes | +0.015 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-MIN2 | game_spread | 0.319 | 0.285 | 0.292 | 29 | 72 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 | team_total | 0.342 | 0.375 | 0.368 | 38 | 63 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK3 | team_total | 0.562 | 0.595 | 0.588 | 60 | 41 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK2 | team_total | 0.778 | 0.805 | 0.800 | 81 | 20 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT12FLABUF-10 | game_total | 0.094 | 0.075 | 0.079 | 8 | 93 | yes | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK5 | team_total | 0.173 | 0.200 | 0.194 | 21 | 81 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN3 | team_total | 0.621 | 0.595 | 0.600 | 60 | 41 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN5 | team_total | 0.215 | 0.195 | 0.199 | 20 | 81 | yes | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK6 | team_total | 0.072 | 0.090 | 0.086 | 10 | 92 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT12VGKMIN-5 | game_total | 0.755 | 0.775 | 0.771 | 78 | 23 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT12FLABUF-2 | game_total | 0.987 | 0.990 | 0.989 |  | 1 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA6 | team_total | 0.064 | 0.075 | 0.073 | 8 | 93 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT12FLABUF-5 | game_total | 0.783 | 0.765 | 0.769 | 77 | 24 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-3 | game_total | 0.958 | 0.965 | 0.964 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-4 | game_total | 0.843 | 0.860 | 0.857 | 87 | 15 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-4 | game_total | 0.844 | 0.855 | 0.853 | 86 | 15 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-4 | game_total | 0.865 | 0.855 | 0.857 | 86 | 15 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN2 | team_total | 0.817 | 0.805 | 0.807 | 81 | 20 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-2 | game_total | 0.983 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-3 | game_total | 0.967 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-6 | game_total | 0.538 | 0.555 | 0.552 | 56 | 45 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT6 | team_total | 0.080 | 0.075 | 0.076 | 8 | 93 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-9 | game_total | 0.174 | 0.165 | 0.167 | 17 | 84 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT12VGKMIN-MIN3 | game_spread | 0.194 | 0.185 | 0.187 | 19 | 82 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-8 | game_total | 0.246 | 0.235 | 0.237 | 24 | 77 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ3 | game_spread | 0.186 | 0.200 | 0.197 | 21 | 81 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT3 | game_spread | 0.149 | 0.155 | 0.154 | 16 | 85 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-9 | game_total | 0.168 | 0.175 | 0.174 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN6 | team_total | 0.098 | 0.085 | 0.087 | 10 | 93 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-10 | game_total | 0.077 | 0.075 | 0.075 | 8 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ5 | team_total | 0.213 | 0.205 | 0.207 | 21 | 80 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-10 | game_total | 0.074 | 0.075 | 0.075 | 8 | 93 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-8 | game_total | 0.237 | 0.245 | 0.243 | 25 | 76 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3 | team_total | 0.616 | 0.605 | 0.607 | 61 | 40 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ6 | team_total | 0.095 | 0.090 | 0.091 | 10 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-5 | game_total | 0.760 | 0.765 | 0.764 | 77 | 24 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-7 | game_total | 0.426 | 0.435 | 0.433 | 44 | 57 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ2 | game_spread | 0.309 | 0.315 | 0.314 | 32 | 69 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN4 | team_total | 0.403 | 0.385 | 0.389 | 40 | 63 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT3 | team_total | 0.572 | 0.565 | 0.566 | 57 | 44 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ2 | team_total | 0.815 | 0.820 | 0.819 | 83 | 19 |  | -0.016 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT2 | game_spread | 0.254 | 0.255 | 0.255 | 26 | 75 |  | -0.017 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT4 | team_total | 0.353 | 0.360 | 0.359 | 37 | 65 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT2 | team_total | 0.792 | 0.790 | 0.790 | 80 | 22 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-NJ | game_winner | 0.528 | 0.525 | 0.526 | 53 | 48 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-OTT | game_winner | 0.472 | 0.475 | 0.474 | 48 | 53 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT5 | team_total | 0.180 | 0.180 | 0.180 | 19 | 83 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ4 | team_total | 0.396 | 0.395 | 0.395 | 40 | 61 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-6 | game_total | 0.546 | 0.545 | 0.545 | 55 | 46 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-7 | game_total | 0.436 | 0.435 | 0.435 | 44 | 57 |  | -0.021 | NO_EDGE |
| KXNHL1P-26OCT12FLABUF-BUF | period_winner |  | 0.345 |  | 35 | 66 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-FLA | period_winner |  | 0.325 |  | 33 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-TIE | period_winner |  | 0.335 |  | 34 | 67 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-BUF2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-FLA2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 0.626 | 0.577 | 0.168 | 0.220 | 6.31 | 6.19 | 1.000/1.015 | KXNHLSPREAD-26OCT12FLABUF-BUF2 -0.050 |
| OTT @ NJD | 0.528 | 0.481 | 0.175 | 0.227 | 6.10 | 5.85 | 0.994/0.968 | KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3 -0.064 |
| VGK @ MIN | 0.543 | 0.532 | 0.181 | 0.218 | 6.06 | 6.16 | 0.991/1.003 | KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 +0.022 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 12 recommended · full analysis in card.md / packet.json `thesis_card`

- Sam Reinhart: 1+ goals NO @ 68c · p 0.7587 (adj 0.7378) · $15.0 · thesis FLA:SUPPRESSED
- Sandis Vilmanis: 1+ goals YES @ 10c · p 0.1373 (adj 0.1255) · $4.9 · thesis FLA:OFFENSE_4PLUS
- Brady Tkachuk: 1+ goals NO @ 69c · p 0.748 (adj 0.7323) · $15.0 · thesis FLA:SUPPRESSED
- Josh Norris: 1+ goals YES @ 19c · p 0.2281 (adj 0.2173) · $5.12 · thesis BUF:OFFENSE_4PLUS
- Michael Amadio: 1+ goals YES @ 13c · p 0.1737 (adj 0.1615) · $5.55 · thesis OTT:OFFENSE_4PLUS
- Jordan Spence: 1+ assists YES @ 24c · p 0.3206 (adj 0.2778) · $6.51 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 72c · p 0.8641 (adj 0.7574) · $18.97 · thesis OTT:SUPPRESSED
- Timo Meier: 1+ goals NO @ 73c · p 0.779 (adj 0.7655) · $18.97 · thesis NJD:SUPPRESSED
- Olli Maatta: 1+ goals YES @ 4c · p 0.0616 (adj 0.0562) · $3.17 · thesis MIN:OFFENSE_4PLUS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.0698 (adj 0.0673) · $3.68 · thesis VGK:OFFENSE_4PLUS
- Mitch Marner: 1+ assists NO @ 53c · p 0.6226 (adj 0.5738) · $15.66 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ goals NO @ 73c · p 0.7667 (adj 0.7563) · $12.23 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ BUF** · priced 171/174 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Colten Ellis (CONFIRMED) exp shots 26.02, exp saves 22.86 (sd 6.17), pull risk 0.048
- FLA net: Jacob Markstrom (CONFIRMED) exp shots 27.92, exp saves 23.86 (sd 6.66), pull risk 0.071

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Brady Tkachuk: 1+ assists | 0.228 | 0.395 | 40/61 | +0.145 | STANDARD |
| Peyton Krebs: 1+ assists | 0.290 | 0.130 | 24/98 | +0.038 | STANDARD |
| Brady Tkachuk: 1+ points | 0.421 | 0.580 | 59/43 | +0.132 | STANDARD |
| Sam Reinhart: 1+ points | 0.451 | 0.580 | 59/43 | +0.102 | STANDARD |
| Brady Tkachuk: 2+ points | 0.103 | 0.210 | 22/80 | +0.086 | STANDARD |
| Sam Reinhart: 1+ assists | 0.276 | 0.375 | 38/63 | +0.078 | STANDARD |

**OTT @ NJD** · priced 170/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Nico Daws (PROBABLE) exp shots 27.04, exp saves 23.33 (sd 6.4), pull risk 0.055
- OTT net: Linus Ullmark (CONFIRMED) exp shots 28.15, exp saves 24.49 (sd 6.51), pull risk 0.048

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Nico Daws: 23+ saves | 0.543 | 0.305 | 55/94 | -0.024 |  |
| Andre Burakovsky: 1+ assists | 0.136 | 0.300 | 32/72 | +0.130 | STANDARD |
| Andre Burakovsky: 1+ points | 0.273 | 0.435 | 45/58 | +0.130 | STANDARD |
| Jack Hughes: 1+ assists | 0.360 | 0.520 | 53/49 | +0.132 | STANDARD |
| Luke Evangelista: 1+ assists | 0.217 | 0.360 | 38/66 | +0.107 | STANDARD |
| Jack Hughes: 2+ points | 0.193 | 0.335 | 35/68 | +0.112 | STANDARD |

**VGK @ MIN** · priced 169/171 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 29.04, exp saves 25.33 (sd 6.79), pull risk 0.054
- VGK net: Carter Hart (PROJECTED) exp shots 27.87, exp saves 24.03 (sd 6.63), pull risk 0.065

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Eichel: 1+ assists | 0.419 | 0.545 | 55/46 | +0.104 | STANDARD |
| Jack Eichel: 1+ points | 0.581 | 0.685 | 69/32 | +0.083 | STANDARD |
| Mitch Marner: 1+ assists | 0.377 | 0.475 | 48/53 | +0.075 | STANDARD |
| Trevor Connelly: 1+ assists | 0.180 | 0.275 | 30/75 | +0.057 | PRIOR_HEAVY |
| Jack Eichel: 2+ points | 0.221 | 0.315 | 32/69 | +0.074 | STANDARD |
| Ryan Hartman: 1+ points | 0.481 | 0.395 | 41/62 | +0.054 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
