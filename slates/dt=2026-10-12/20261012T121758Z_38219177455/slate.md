# NHL slate 2026-10-12 — RESEARCH_ONLY

generated 2026-10-12T12:17:58Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2932 · contracts joined: 459 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 384, 'OK': 35, 'NO_EDGE': 40}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27, 'player_assists': 48, 'first_goal': 70, 'player_goals': 125, 'player_points': 63}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 2026-10-12T17:00:00Z | T-3h | 0.613 | 0.387 | 0.168 | 6.24 | 3.49 | 2.76 | 51 (25/26) | PROJECTED/PROJECTED |
| OTT @ NJD | 2026-10-12T23:00:00Z | T-6h | 0.544 | 0.456 | 0.179 | 5.94 | 3.11 | 2.83 | 214 (25/189) | PROJECTED/PROJECTED |
| VGK @ MIN | 2026-10-13T00:00:00Z | T-6h | 0.532 | 0.468 | 0.176 | 6.11 | 3.16 | 2.96 | 194 (25/169) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT12FLABUF-BUF | game_winner | 0.613 | 0.495 | 0.519 | 50 | 51 | yes | +0.096 | OK |
| KXNHLGAME-26OCT12FLABUF-FLA | game_winner | 0.387 | 0.495 | 0.473 | 50 | 51 | no | +0.086 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF2 | game_spread | 0.393 | 0.295 | 0.313 | 30 | 71 | yes | +0.078 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA2 | game_spread | 0.199 | 0.295 | 0.274 | 30 | 71 | no | +0.077 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3 | team_total | 0.685 | 0.595 | 0.614 | 60 | 41 | yes | +0.068 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA3 | team_total | 0.522 | 0.605 | 0.589 | 61 | 40 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT12FLABUF-FLA3 | game_spread | 0.110 | 0.185 | 0.167 | 19 | 82 | no | +0.059 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF4 | team_total | 0.474 | 0.390 | 0.407 | 40 | 62 | yes | +0.058 | OK |
| KXNHLSPREAD-26OCT12FLABUF-BUF3 | game_spread | 0.258 | 0.185 | 0.198 | 19 | 82 | yes | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF5 | team_total | 0.278 | 0.200 | 0.214 | 21 | 81 | yes | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA4 | team_total | 0.310 | 0.380 | 0.366 | 39 | 63 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA2 | team_total | 0.750 | 0.815 | 0.803 | 83 | 20 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF6 | team_total | 0.138 | 0.085 | 0.094 | 10 | 93 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-BUF2 | team_total | 0.859 | 0.810 | 0.821 | 82 | 20 | yes | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA5 | team_total | 0.155 | 0.195 | 0.186 | 20 | 81 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT12FLABUF-8 | game_total | 0.268 | 0.235 | 0.241 | 24 | 77 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT12FLABUF-FLA6 | team_total | 0.062 | 0.090 | 0.084 | 10 | 92 | no | +0.013 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK3 | game_spread | 0.149 | 0.175 | 0.169 | 18 | 83 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-4 | game_total | 0.832 | 0.855 | 0.851 | 86 | 15 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT12FLABUF-7 | game_total | 0.455 | 0.425 | 0.431 | 43 | 58 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-MIN2 | game_spread | 0.312 | 0.285 | 0.290 | 29 | 72 | yes | +0.008 | OK |
| KXNHLSPREAD-26OCT12VGKMIN-VGK2 | game_spread | 0.258 | 0.285 | 0.280 | 29 | 72 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-5 | game_total | 0.742 | 0.770 | 0.765 | 78 | 24 | no | +0.005 | OK |
| KXNHLGAME-26OCT12VGKMIN-MIN | game_winner | 0.532 | 0.505 | 0.510 | 51 | 50 | yes | +0.005 | OK |
| KXNHLGAME-26OCT12VGKMIN-VGK | game_winner | 0.468 | 0.495 | 0.490 | 50 | 51 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK2 | team_total | 0.785 | 0.805 | 0.801 | 81 | 20 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-6 | game_total | 0.519 | 0.545 | 0.540 | 55 | 46 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT12FLABUF-10 | game_total | 0.089 | 0.075 | 0.078 | 8 | 93 | yes | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN3 | team_total | 0.620 | 0.595 | 0.600 | 60 | 41 | yes | +0.003 | OK |
| KXNHLSPREAD-26OCT12OTTNJ-OTT3 | game_spread | 0.139 | 0.155 | 0.152 | 16 | 85 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN6 | team_total | 0.097 | 0.085 | 0.087 | 9 | 92 | yes | +0.001 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-10 | game_total | 0.065 | 0.080 | 0.077 | 9 | 93 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT12OTTNJ-7 | game_total | 0.403 | 0.425 | 0.420 | 43 | 58 | no | +0.000 | OK |
| KXNHLTOTAL-26OCT12FLABUF-6 | game_total | 0.568 | 0.545 | 0.550 | 55 | 46 | yes | +0.000 | OK |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK3 | team_total | 0.574 | 0.595 | 0.591 | 60 | 41 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-8 | game_total | 0.219 | 0.240 | 0.236 | 25 | 77 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT4 | team_total | 0.326 | 0.345 | 0.341 | 35 | 66 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-2 | game_total | 0.981 | 0.985 | 0.984 | 99 | 2 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26OCT12OTTNJ-9 | game_total | 0.153 | 0.165 | 0.162 | 17 | 84 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK5 | team_total | 0.181 | 0.195 | 0.192 | 20 | 81 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK6 | team_total | 0.078 | 0.090 | 0.087 | 10 | 92 |  | -0.003 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ3 | game_spread | 0.192 | 0.205 | 0.202 | 21 | 80 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN2 | team_total | 0.817 | 0.805 | 0.808 | 81 | 20 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ4 | team_total | 0.387 | 0.410 | 0.405 | 42 | 60 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-5 | game_total | 0.761 | 0.780 | 0.776 | 79 | 23 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-3 | game_total | 0.961 | 0.965 | 0.964 | 97 | 4 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-9 | game_total | 0.185 | 0.170 | 0.173 | 18 | 84 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-OTT2 | game_spread | 0.242 | 0.255 | 0.252 | 26 | 75 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN5 | team_total | 0.216 | 0.200 | 0.203 | 21 | 81 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-4 | game_total | 0.847 | 0.860 | 0.858 | 87 | 15 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-4 | game_total | 0.858 | 0.865 | 0.864 | 87 | 14 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ5 | team_total | 0.205 | 0.220 | 0.217 | 23 | 79 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-3 | game_total | 0.966 | 0.965 | 0.965 | 97 | 4 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-2 | game_total | 0.983 | 0.980 | 0.981 | 99 | 3 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-9 | game_total | 0.169 | 0.175 | 0.174 | 18 | 83 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT3 | team_total | 0.542 | 0.560 | 0.556 | 57 | 45 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ3 | team_total | 0.614 | 0.630 | 0.627 | 64 | 38 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT6 | team_total | 0.067 | 0.070 | 0.069 | 8 | 94 |  | -0.010 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT2 | team_total | 0.768 | 0.780 | 0.778 | 79 | 23 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-OTT5 | team_total | 0.161 | 0.175 | 0.172 | 19 | 84 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-VGK4 | team_total | 0.356 | 0.370 | 0.367 | 38 | 64 |  | -0.012 | NO_EDGE |
| KXNHLSPREAD-26OCT12VGKMIN-MIN3 | game_spread | 0.188 | 0.185 | 0.186 | 19 | 82 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ2 | team_total | 0.812 | 0.825 | 0.822 | 84 | 19 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26OCT12OTTNJ-NJ2 | game_spread | 0.318 | 0.325 | 0.324 | 33 | 68 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12OTTNJ-NJ6 | team_total | 0.088 | 0.090 | 0.090 | 10 | 92 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-10 | game_total | 0.079 | 0.080 | 0.080 | 9 | 93 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT12FLABUF-5 | game_total | 0.776 | 0.775 | 0.775 | 78 | 23 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT12VGKMIN-MIN4 | team_total | 0.401 | 0.390 | 0.392 | 40 | 62 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-6 | game_total | 0.549 | 0.555 | 0.554 | 56 | 45 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-8 | game_total | 0.245 | 0.250 | 0.249 | 26 | 76 |  | -0.018 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-NJ | game_winner | 0.544 | 0.545 | 0.545 | 55 | 46 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26OCT12OTTNJ-OTT | game_winner | 0.456 | 0.455 | 0.455 | 46 | 55 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT12VGKMIN-7 | game_total | 0.435 | 0.435 | 0.435 | 44 | 57 |  | -0.022 | NO_EDGE |
| KXNHL1P-26OCT12FLABUF-BUF | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-FLA | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT12FLABUF-TIE | period_winner |  | 0.325 |  | 34 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-BUF2 | period_spread |  | 0.090 |  | 10 | 92 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT12FLABUF-FLA2 | period_spread |  | 0.100 |  | 12 | 92 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| FLA @ BUF | 0.613 | 0.576 | 0.168 | 0.224 | 6.24 | 6.16 | 0.997/1.008 | KXNHLSPREAD-26OCT12FLABUF-BUF2 -0.048 |
| OTT @ NJD | 0.544 | 0.497 | 0.179 | 0.230 | 5.94 | 5.92 | 0.987/0.998 | KXNHLSPREAD-26OCT12OTTNJ-NJ2 -0.050 |
| VGK @ MIN | 0.532 | 0.528 | 0.176 | 0.222 | 6.11 | 6.17 | 0.995/1.003 | KXNHLTOTAL-26OCT12VGKMIN-7 +0.018 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Florida wins by over 1.5 goals NO @ 71c · p 0.7818 (adj 0.7434) · $13.7 · thesis BUF:WINS
- Florida wins by over 2.5 goals NO @ 82c · p 0.8738 (adj 0.8444) · $10.28 · thesis BUF:WINS
- Jack Hughes: 1+ goals NO @ 63c · p 0.7086 (adj 0.6877) · $20.0 · thesis NJD:SUPPRESSED
- Warren Foegele: 1+ goals YES @ 12c · p 0.1609 (adj 0.1482) · $5.55 · thesis OTT:OFFENSE_4PLUS
- Andre Burakovsky: 1+ assists NO @ 72c · p 0.8651 (adj 0.761) · $20.0 · thesis OTT:SUPPRESSED
- Michael Amadio: 1+ goals YES @ 13c · p 0.1763 (adj 0.1535) · $4.09 · thesis OTT:OFFENSE_4PLUS
- Mitch Marner: 2+ assists NO @ 86c · p 0.9127 (adj 0.8788) · $20.0 · thesis VGK:SUPPRESSED
- Mitch Marner: 1+ assists NO @ 51c · p 0.6207 (adj 0.539) · $3.36 · thesis VGK:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**FLA @ BUF** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.82 (sd 6.24), pull risk 0.052
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.92, exp saves 23.91 (sd 6.64), pull risk 0.069

**OTT @ NJD** · priced 163/163 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 27.04, exp saves 23.4 (sd 6.38), pull risk 0.054
- OTT net: Linus Ullmark (PROJECTED) exp shots 28.15, exp saves 24.44 (sd 6.6), pull risk 0.051

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andre Burakovsky: 1+ points | 0.268 | 0.430 | 45/59 | +0.125 | STANDARD |
| Andre Burakovsky: 1+ assists | 0.135 | 0.295 | 31/72 | +0.131 | STANDARD |
| Jack Hughes: 2+ points | 0.190 | 0.345 | 36/67 | +0.124 | STANDARD |
| Luke Evangelista: 1+ points | 0.360 | 0.510 | 53/51 | +0.113 | STANDARD |
| Jack Hughes: 1+ assists | 0.367 | 0.515 | 53/50 | +0.116 | STANDARD |
| Luke Evangelista: 1+ assists | 0.214 | 0.360 | 38/66 | +0.111 | STANDARD |

**VGK @ MIN** · priced 143/143 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.04, exp saves 25.4 (sd 6.81), pull risk 0.054
- VGK net: Carter Hart (PROJECTED) exp shots 27.87, exp saves 24.1 (sd 6.51), pull risk 0.063

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matt Boldy: 1+ goals | 0.341 | 0.210 | 39/97 | -0.066 | STANDARD |
| Mitch Marner: 1+ assists | 0.379 | 0.505 | 52/51 | +0.093 | STANDARD |
| Kirill Kaprizov: 1+ points | 0.615 | 0.495 | 72/73 | -0.119 | STANDARD |
| Jack Eichel: 2+ points | 0.223 | 0.335 | 36/69 | +0.073 | STANDARD |
| Jack Eichel: 1+ assists | 0.421 | 0.525 | 54/49 | +0.072 | STANDARD |
| Ryan Hartman: 1+ goals | 0.224 | 0.120 | 21/97 | +0.002 | STANDARD |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
