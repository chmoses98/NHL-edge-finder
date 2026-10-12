# NHL slate 2026-10-12 — RESEARCH_ONLY

generated 2026-10-12T11:24:10Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2789 · contracts joined: 316 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 241, 'OK': 32, 'NO_EDGE': 43}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'player_assists': 28, 'first_goal': 35, 'player_goals': 62, 'player_points': 38}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 2026-10-12T17:00:00Z | T-3h | 0.615 | 0.386 | 0.171 | 6.23 | 3.48 | 2.75 | 51 (25/26) | PROJECTED/PROJECTED |
| OTT @ NJD | 2026-10-12T23:00:00Z | T-6h | 0.543 | 0.457 | 0.178 | 5.92 | 3.09 | 2.82 | 214 (25/189) | PROJECTED/PROJECTED |
| VGK @ MIN | 2026-10-13T00:00:00Z | T-12h | 0.533 | 0.467 | 0.177 | 6.10 | 3.15 | 2.95 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT12FLABUF-BUF | game_winner | 0.615 | 0.495 | 0.519 | 50 | 51 | yes | +0.097 | OK |
| KXNHLGAME-26OCT12FLABUF-FLA | game_winner | 0.386 | 0.495 | 0.473 | 50 | 51 | no | +0.087 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF2 | game_spread | 0.389 | 0.285 | 0.305 | 29 | 72 | yes | +0.085 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA2 | game_spread | 0.196 | 0.295 | 0.273 | 30 | 71 | no | +0.080 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3 | team_total | 0.685 | 0.595 | 0.614 | 60 | 41 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA3 | team_total | 0.520 | 0.605 | 0.588 | 61 | 40 | no | +0.063 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA3 | game_spread | 0.110 | 0.185 | 0.167 | 19 | 82 | no | +0.060 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF3 | game_spread | 0.257 | 0.185 | 0.198 | 19 | 82 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF4 | team_total | 0.472 | 0.390 | 0.406 | 40 | 62 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA4 | team_total | 0.309 | 0.380 | 0.365 | 39 | 63 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF5 | team_total | 0.274 | 0.205 | 0.218 | 22 | 81 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA2 | team_total | 0.750 | 0.815 | 0.803 | 83 | 20 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF6 | team_total | 0.135 | 0.085 | 0.093 | 10 | 93 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA5 | team_total | 0.152 | 0.195 | 0.186 | 20 | 81 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF2 | team_total | 0.858 | 0.815 | 0.824 | 83 | 20 | yes | +0.018 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-4 | game_total | 0.827 | 0.855 | 0.850 | 86 | 15 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK3 | game_spread | 0.146 | 0.175 | 0.169 | 18 | 83 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA6 | team_total | 0.061 | 0.090 | 0.083 | 10 | 92 | no | +0.014 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK2 | game_spread | 0.254 | 0.285 | 0.279 | 29 | 72 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-5 | game_total | 0.736 | 0.770 | 0.764 | 78 | 24 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-6 | game_total | 0.512 | 0.545 | 0.539 | 55 | 46 | no | +0.010 | OK |
| KXNHLGAME-26OCT12VGKMIN-MIN | game_winner | 0.533 | 0.505 | 0.511 | 51 | 50 | yes | +0.006 | OK |
| KXNHLGAME-26OCT12VGKMIN-VGK | game_winner | 0.467 | 0.495 | 0.489 | 50 | 51 | no | +0.006 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-MIN2 | game_spread | 0.309 | 0.285 | 0.290 | 29 | 72 | yes | +0.005 | OK |
| KXNHLSPREAD-26OCT12OTTNJ-OTT3 | game_spread | 0.138 | 0.155 | 0.151 | 16 | 85 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-3 | game_total | 0.954 | 0.965 | 0.963 | 97 | 4 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-7 | game_total | 0.401 | 0.425 | 0.420 | 43 | 58 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT12FLABUF-10 | game_total | 0.086 | 0.075 | 0.077 | 8 | 93 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-10 | game_total | 0.064 | 0.080 | 0.077 | 9 | 93 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT4 | team_total | 0.323 | 0.345 | 0.341 | 35 | 66 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK3 | team_total | 0.573 | 0.600 | 0.595 | 61 | 41 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT12FLABUF-8 | game_total | 0.263 | 0.245 | 0.249 | 25 | 76 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ4 | team_total | 0.384 | 0.410 | 0.405 | 42 | 60 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN6 | team_total | 0.095 | 0.085 | 0.087 | 9 | 92 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK5 | team_total | 0.180 | 0.195 | 0.192 | 20 | 81 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-3 | game_total | 0.958 | 0.965 | 0.964 | 97 | 4 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-2 | game_total | 0.980 | 0.985 | 0.984 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-9 | game_total | 0.153 | 0.165 | 0.162 | 17 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ5 | team_total | 0.202 | 0.220 | 0.216 | 23 | 79 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-5 | game_total | 0.761 | 0.780 | 0.776 | 79 | 23 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-4 | game_total | 0.845 | 0.860 | 0.857 | 87 | 15 |  | -0.004 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ3 | game_spread | 0.193 | 0.205 | 0.202 | 21 | 80 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK2 | team_total | 0.783 | 0.805 | 0.801 | 82 | 21 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-8 | game_total | 0.222 | 0.240 | 0.236 | 25 | 77 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-7 | game_total | 0.452 | 0.435 | 0.438 | 44 | 57 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-3 | game_total | 0.967 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-9 | game_total | 0.185 | 0.170 | 0.173 | 18 | 84 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT2 | game_spread | 0.243 | 0.255 | 0.252 | 26 | 75 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3 | team_total | 0.610 | 0.630 | 0.626 | 64 | 38 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-4 | game_total | 0.858 | 0.865 | 0.864 | 87 | 14 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN5 | team_total | 0.215 | 0.200 | 0.203 | 21 | 81 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT5 | team_total | 0.158 | 0.175 | 0.172 | 19 | 84 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 | team_total | 0.352 | 0.370 | 0.366 | 38 | 64 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-2 | game_total | 0.982 | 0.980 | 0.980 | 99 | 3 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT3 | team_total | 0.542 | 0.560 | 0.556 | 57 | 45 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT6 | team_total | 0.065 | 0.070 | 0.069 | 8 | 94 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ2 | team_total | 0.809 | 0.825 | 0.822 | 84 | 19 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT2 | team_total | 0.767 | 0.780 | 0.777 | 79 | 23 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK6 | team_total | 0.076 | 0.080 | 0.079 | 9 | 93 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-10 | game_total | 0.076 | 0.080 | 0.079 | 9 | 93 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-6 | game_total | 0.544 | 0.555 | 0.553 | 56 | 45 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ2 | game_spread | 0.317 | 0.325 | 0.323 | 33 | 68 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN3 | team_total | 0.614 | 0.600 | 0.603 | 61 | 41 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT12VGKMIN-MIN3 | game_spread | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-9 | game_total | 0.173 | 0.175 | 0.175 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-6 | game_total | 0.564 | 0.555 | 0.557 | 56 | 45 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN4 | team_total | 0.403 | 0.390 | 0.393 | 40 | 62 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ6 | team_total | 0.089 | 0.090 | 0.090 | 10 | 92 |  | -0.015 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-5 | game_total | 0.774 | 0.780 | 0.779 | 79 | 23 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-8 | game_total | 0.247 | 0.250 | 0.249 | 26 | 76 |  | -0.019 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-OTT | game_winner | 0.457 | 0.455 | 0.455 | 46 | 55 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-NJ | game_winner | 0.543 | 0.545 | 0.545 | 55 | 46 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-7 | game_total | 0.434 | 0.435 | 0.435 | 44 | 57 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN2 | team_total | 0.818 | 0.815 | 0.816 | 83 | 20 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT12FLABUF-BUF | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-FLA | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-TIE | period_winner |  | 0.330 |  | 34 | 68 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-BUF2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-FLA2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 0.615 | 0.570 | 0.171 | 0.215 | 6.23 | 6.14 | 0.997/1.008 | KXNHLGAME-26OCT12FLABUF-BUF -0.044 |
| OTT @ NJD | 0.543 | 0.494 | 0.178 | 0.227 | 5.92 | 5.90 | 0.987/0.998 | KXNHLSPREAD-26OCT12OTTNJ-NJ2 -0.054 |
| VGK @ MIN | 0.533 | 0.529 | 0.177 | 0.220 | 6.10 | 6.15 | 0.995/1.003 | KXNHLTOTAL-26OCT12VGKMIN-5 +0.013 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 7 recommended · full analysis in card.md / packet.json `thesis_card`

- Florida wins by over 1.5 goals NO @ 71c · p 0.7783 (adj 0.7417) · $14.44 · thesis BUF:WINS
- Florida wins by over 2.5 goals NO @ 82c · p 0.8678 (adj 0.8414) · $2.65 · thesis BUF:WINS
- Buffalo wins by over 1.5 goals YES @ 29c · p 0.3453 (adj 0.3152) · $1.28 · thesis BUF:WINS_BY_2PLUS
- Jack Hughes: 1+ goals NO @ 63c · p 0.7047 (adj 0.6823) · $16.16 · thesis NJD:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1792 (adj 0.1544) · $3.2 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 73c · p 0.8618 (adj 0.7631) · $16.39 · thesis OTT:SUPPRESSED
- Timo Meier: 1+ goals NO @ 73c · p 0.7769 (adj 0.7614) · $13.84 · thesis NJD:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.85 (sd 6.26), pull risk 0.048
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.92, exp saves 23.89 (sd 6.69), pull risk 0.07

**OTT @ NJD** · priced 163/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 27.04, exp saves 23.42 (sd 6.4), pull risk 0.054
- OTT net: Linus Ullmark (PROJECTED) exp shots 28.15, exp saves 24.49 (sd 6.6), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ points | 0.267 | 0.430 | 45/59 | +0.126 | STANDARD |
| Jack Hughes: 2+ points | 0.192 | 0.345 | 36/67 | +0.122 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.138 | 0.290 | 31/73 | +0.118 | STANDARD |
| Jack Hughes: 1+ assists | 0.364 | 0.515 | 53/50 | +0.118 | STANDARD |
| Luke Evangelista: 1+ points | 0.365 | 0.515 | 53/50 | +0.118 | STANDARD |
| Luke Evangelista: 1+ assists | 0.219 | 0.360 | 38/66 | +0.105 | STANDARD |

**VGK @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.04, exp saves 25.38 (sd 6.74), pull risk 0.056
- VGK net: Carter Hart (PROJECTED) exp shots 27.87, exp saves 24.07 (sd 6.63), pull risk 0.064

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
