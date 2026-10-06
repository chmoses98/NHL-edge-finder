# NHL slate 2026-10-06 — RESEARCH_ONLY

generated 2026-10-06T04:11:01Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 9 · simulated (not started): 9 · markets on board: 2342 · contracts joined: 459 (unjoined to any game: 1532)
gates: {'UNSUPPORTED': 234, 'OK': 118, 'NO_EDGE': 107}
families: {'period_winner': 81, 'period_spread': 54, 'period_total': 81, 'game_early_goal': 9, 'game_winner': 18, 'game_overtime': 9, 'game_spread': 36, 'team_total': 90, 'game_total': 81}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 2026-10-06T23:00:00Z | T-12h | 0.448 | 0.552 | 0.168 | 6.46 | 3.07 | 3.39 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ MTL | 2026-10-06T23:00:00Z | T-12h | 0.497 | 0.503 | 0.182 | 6.17 | 3.07 | 3.10 | 51 (25/26) | PROJECTED/PROJECTED |
| OTT @ DET | 2026-10-06T23:00:00Z | T-12h | 0.552 | 0.448 | 0.175 | 6.22 | 3.28 | 2.94 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ NJD | 2026-10-06T23:00:00Z | T-12h | 0.500 | 0.500 | 0.174 | 6.09 | 3.05 | 3.05 | 51 (25/26) | PROJECTED/PROJECTED |
| MIN @ BUF | 2026-10-06T23:00:00Z | T-12h | 0.531 | 0.469 | 0.177 | 6.52 | 3.36 | 3.16 | 51 (25/26) | PROBABLE/PROJECTED |
| NYI @ NYR | 2026-10-06T23:30:00Z | T-12h | 0.577 | 0.423 | 0.183 | 5.84 | 3.15 | 2.69 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ CHI | 2026-10-07T00:00:00Z | T-12h | 0.434 | 0.566 | 0.179 | 5.91 | 2.75 | 3.16 | 51 (25/26) | PROJECTED/PROJECTED |
| VGK @ SEA | 2026-10-07T01:40:00Z | T-12h | 0.484 | 0.516 | 0.180 | 6.30 | 3.10 | 3.20 | 51 (25/26) | PROJECTED/PROJECTED |
| FLA @ LAK | 2026-10-07T02:00:00Z | T-12h | 0.556 | 0.444 | 0.175 | 6.22 | 3.29 | 2.93 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT06NSHTOR-NSH | game_winner | 0.552 | 0.415 | 0.442 | 42 | 59 | yes | +0.115 | OK |
| KXNHLGAME-26OCT06NSHTOR-TOR | game_winner | 0.448 | 0.585 | 0.558 | 59 | 42 | no | +0.115 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH4 | team_total | 0.451 | 0.320 | 0.345 | 33 | 69 | yes | +0.106 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH3 | team_total | 0.663 | 0.540 | 0.565 | 55 | 47 | yes | +0.095 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH2 | game_spread | 0.335 | 0.225 | 0.245 | 23 | 78 | yes | +0.093 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR2 | game_spread | 0.251 | 0.355 | 0.333 | 36 | 65 | no | +0.083 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH5 | team_total | 0.261 | 0.160 | 0.177 | 17 | 85 | yes | +0.081 | OK |
| KXNHLGAME-26OCT06VGKSEA-SEA | game_winner | 0.484 | 0.385 | 0.404 | 39 | 62 | yes | +0.077 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-TOR3 | game_spread | 0.146 | 0.235 | 0.215 | 24 | 77 | no | +0.072 | OK |
| KXNHLGAME-26OCT06FLALA-FLA | game_winner | 0.444 | 0.535 | 0.517 | 54 | 47 | no | +0.069 | OK |
| KXNHLGAME-26OCT06VGKSEA-VGK | game_winner | 0.516 | 0.605 | 0.588 | 61 | 40 | no | +0.067 | OK |
| KXNHLSPREAD-26OCT06NSHTOR-NSH3 | game_spread | 0.212 | 0.135 | 0.148 | 14 | 87 | yes | +0.063 | OK |
| KXNHLGAME-26OCT06FLALA-LA | game_winner | 0.556 | 0.475 | 0.491 | 48 | 53 | yes | +0.059 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK3 | game_spread | 0.181 | 0.255 | 0.239 | 26 | 75 | no | +0.056 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA2 | game_spread | 0.338 | 0.265 | 0.279 | 27 | 74 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA4 | team_total | 0.430 | 0.355 | 0.370 | 36 | 65 | yes | +0.054 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH2 | team_total | 0.846 | 0.770 | 0.787 | 78 | 24 | yes | +0.054 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA3 | game_spread | 0.136 | 0.205 | 0.189 | 21 | 80 | no | +0.053 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA2 | game_spread | 0.273 | 0.205 | 0.217 | 21 | 80 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA4 | team_total | 0.385 | 0.310 | 0.324 | 32 | 70 | yes | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA3 | team_total | 0.603 | 0.525 | 0.541 | 54 | 49 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-VGK2 | game_spread | 0.299 | 0.365 | 0.351 | 37 | 64 | no | +0.045 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR3 | team_total | 0.590 | 0.655 | 0.642 | 66 | 35 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-NSH6 | team_total | 0.126 | 0.065 | 0.075 | 8 | 95 | yes | +0.041 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA3 | team_total | 0.647 | 0.580 | 0.594 | 59 | 43 | yes | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA5 | team_total | 0.238 | 0.185 | 0.195 | 19 | 82 | yes | +0.037 | OK |
| KXNHLSPREAD-26OCT06FLALA-FLA2 | game_spread | 0.239 | 0.295 | 0.283 | 30 | 71 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR4 | team_total | 0.376 | 0.445 | 0.431 | 46 | 57 | no | +0.037 | OK |
| KXNHLGAME-26OCT06OTTDET-DET | game_winner | 0.552 | 0.495 | 0.507 | 50 | 51 | yes | +0.035 | OK |
| KXNHLGAME-26OCT06OTTDET-OTT | game_winner | 0.448 | 0.505 | 0.493 | 51 | 50 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK4 | team_total | 0.410 | 0.470 | 0.458 | 48 | 54 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-8 | game_total | 0.295 | 0.245 | 0.255 | 25 | 76 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ3 | game_spread | 0.167 | 0.215 | 0.205 | 22 | 79 | no | +0.031 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT3 | game_spread | 0.139 | 0.185 | 0.175 | 19 | 82 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA5 | team_total | 0.210 | 0.155 | 0.165 | 17 | 86 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR2 | team_total | 0.801 | 0.845 | 0.837 | 85 | 16 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET2 | game_spread | 0.332 | 0.285 | 0.294 | 29 | 72 | yes | +0.027 | OK |
| KXNHLSPREAD-26OCT06OTTDET-OTT2 | game_spread | 0.240 | 0.285 | 0.276 | 29 | 72 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN3 | game_spread | 0.154 | 0.195 | 0.186 | 20 | 81 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK3 | team_total | 0.629 | 0.680 | 0.670 | 69 | 33 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26OCT06NSHTOR-TOR5 | team_total | 0.203 | 0.250 | 0.240 | 26 | 76 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK5 | team_total | 0.223 | 0.270 | 0.260 | 28 | 74 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA2 | team_total | 0.834 | 0.790 | 0.800 | 80 | 22 | yes | +0.023 | OK |
| KXNHLGAME-26OCT06UTANJ-NJ | game_winner | 0.500 | 0.545 | 0.536 | 55 | 46 | no | +0.022 | OK |
| KXNHLGAME-26OCT06UTANJ-UTA | game_winner | 0.500 | 0.455 | 0.464 | 46 | 55 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA3 | team_total | 0.561 | 0.610 | 0.600 | 62 | 40 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT06VGKSEA-SEA3 | game_spread | 0.160 | 0.125 | 0.131 | 13 | 88 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-6 | game_total | 0.599 | 0.555 | 0.564 | 56 | 45 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT06FLALA-LA3 | game_spread | 0.211 | 0.170 | 0.178 | 18 | 84 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-9 | game_total | 0.211 | 0.175 | 0.182 | 18 | 83 | yes | +0.021 | OK |
| KXNHLTOTAL-26OCT06CARMTL-5 | game_total | 0.769 | 0.810 | 0.802 | 82 | 20 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA6 | team_total | 0.094 | 0.060 | 0.066 | 7 | 95 | yes | +0.019 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-7 | game_total | 0.486 | 0.445 | 0.453 | 45 | 56 | yes | +0.019 | OK |
| KXNHLSPREAD-26OCT06STLCHI-CHI3 | game_spread | 0.123 | 0.155 | 0.148 | 16 | 85 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-LA6 | team_total | 0.114 | 0.075 | 0.082 | 9 | 94 | yes | +0.018 | OK |
| KXNHLSPREAD-26OCT06CARMTL-CAR3 | game_spread | 0.171 | 0.205 | 0.198 | 21 | 80 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-VGK2 | team_total | 0.823 | 0.855 | 0.849 | 86 | 15 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA2 | team_total | 0.782 | 0.820 | 0.813 | 83 | 19 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 | team_total | 0.347 | 0.390 | 0.381 | 40 | 62 | no | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT06VGKSEA-SEA2 | team_total | 0.808 | 0.765 | 0.774 | 78 | 25 | yes | +0.016 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET3 | team_total | 0.642 | 0.600 | 0.609 | 61 | 41 | yes | +0.015 | OK |
| KXNHLTOTAL-26OCT06NYINYR-4 | game_total | 0.816 | 0.845 | 0.840 | 85 | 16 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT06OTTDET-DET3 | game_spread | 0.205 | 0.175 | 0.181 | 18 | 83 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET6 | team_total | 0.110 | 0.080 | 0.085 | 9 | 93 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT06MINBUF-BUF3 | team_total | 0.660 | 0.620 | 0.628 | 63 | 39 | yes | +0.014 | OK |
| KXNHLGAME-26OCT06MINBUF-BUF | game_winner | 0.531 | 0.495 | 0.502 | 50 | 51 | yes | +0.014 | OK |
| KXNHLGAME-26OCT06MINBUF-MIN | game_winner | 0.469 | 0.505 | 0.498 | 51 | 50 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-DET5 | team_total | 0.235 | 0.200 | 0.207 | 21 | 81 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT4 | team_total | 0.350 | 0.395 | 0.386 | 41 | 62 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT06OTTDET-OTT2 | team_total | 0.786 | 0.815 | 0.809 | 82 | 19 | no | +0.013 | OK |
| KXNHLTOTAL-26OCT06MINBUF-8 | game_total | 0.307 | 0.275 | 0.281 | 28 | 73 | yes | +0.013 | OK |
| KXNHLSPREAD-26OCT06MINBUF-BUF2 | game_spread | 0.317 | 0.285 | 0.291 | 29 | 72 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT06NSHTOR-4 | game_total | 0.880 | 0.855 | 0.860 | 86 | 15 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT06CARMTL-7 | game_total | 0.441 | 0.475 | 0.468 | 48 | 53 | no | +0.012 | OK |
| KXNHLTOTAL-26OCT06CARMTL-6 | game_total | 0.552 | 0.585 | 0.578 | 59 | 42 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT06FLALA-10 | game_total | 0.086 | 0.065 | 0.069 | 7 | 94 | yes | +0.011 | OK |
| KXNHLSPREAD-26OCT06MINBUF-MIN2 | game_spread | 0.265 | 0.295 | 0.289 | 30 | 71 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR5 | team_total | 0.207 | 0.240 | 0.233 | 25 | 77 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT06UTANJ-NJ2 | game_spread | 0.284 | 0.315 | 0.309 | 32 | 69 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT06CARMTL-CAR2 | team_total | 0.810 | 0.835 | 0.830 | 84 | 17 | no | +0.011 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NSH @ TOR | 0.448 | 0.507 | 0.168 | 0.217 | 6.46 | 6.29 | 0.978/0.994 | KXNHLGAME-26OCT06NSHTOR-TOR +0.059 |
| CAR @ MTL | 0.497 | 0.518 | 0.182 | 0.217 | 6.17 | 6.29 | 0.952/0.997 | KXNHLTEAMTOTAL-26OCT06CARMTL-MTL3 +0.030 |
| OTT @ DET | 0.552 | 0.502 | 0.175 | 0.222 | 6.22 | 6.11 | 1.003/1.040 | KXNHLGAME-26OCT06OTTDET-OTT +0.051 |
| UTA @ NJD | 0.500 | 0.489 | 0.174 | 0.219 | 6.09 | 6.15 | 0.987/0.992 | KXNHLTEAMTOTAL-26OCT06UTANJ-UTA3 +0.018 |
| MIN @ BUF | 0.531 | 0.515 | 0.177 | 0.216 | 6.52 | 6.47 | 0.999/1.003 | KXNHLSPREAD-26OCT06MINBUF-BUF2 -0.022 |
| NYI @ NYR | 0.577 | 0.563 | 0.183 | 0.220 | 5.84 | 5.98 | 0.957/0.956 | KXNHLTEAMTOTAL-26OCT06NYINYR-NYI3 +0.028 |
| STL @ CHI | 0.434 | 0.440 | 0.179 | 0.221 | 5.91 | 6.25 | 1.003/0.993 | KXNHLTOTAL-26OCT06STLCHI-7 +0.060 |
| VGK @ SEA | 0.484 | 0.483 | 0.180 | 0.219 | 6.30 | 6.14 | 1.005/1.003 | KXNHLTOTAL-26OCT06VGKSEA-8 -0.030 |
| FLA @ LAK | 0.556 | 0.578 | 0.175 | 0.224 | 6.22 | 6.00 | 0.992/1.007 | KXNHLTEAMTOTAL-26OCT06FLALA-FLA4 -0.037 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 8 recommended · full analysis in card.md / packet.json `thesis_card`

- Toronto wins by over 1.5 goals NO @ 65c · p 0.7124 (adj 0.6787) · $8.25 · thesis NSH:WINS
- Nashville over 3.5 goals scored YES @ 33c · p 0.3922 (adj 0.3561) · $2.24 · thesis NSH:OFFENSE_4PLUS
- New Jersey wins by over 2.5 goals NO @ 79c · p 0.8418 (adj 0.8134) · $16.74 · thesis UTA:WINS
- Vegas wins by over 2.5 goals NO @ 75c · p 0.8218 (adj 0.7834) · $20.0 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 21c · p 0.267 (adj 0.236) · $2.61 · thesis SEA:WINS_BY_2PLUS
- Florida wins by over 2.5 goals NO @ 80c · p 0.8788 (adj 0.8369) · $19.59 · thesis LAK:WINS
- Los Angeles wins by over 1.5 goals YES @ 27c · p 0.3498 (adj 0.3074) · $5.36 · thesis LAK:WINS_BY_2PLUS
- Florida wins by over 1.5 goals NO @ 71c · p 0.7863 (adj 0.7457) · $5.06 · thesis LAK:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NSH @ TOR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.05, exp saves 25.99 (sd 6.98), pull risk 0.06
- NSH net: Justus Annunen (PROJECTED) exp shots 28.03, exp saves 24.11 (sd 6.69), pull risk 0.062

**CAR @ MTL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- MTL net: Jakub Dobes (PROJECTED) exp shots 30.78, exp saves 26.67 (sd 7.19), pull risk 0.061
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.05, exp saves 19.87 (sd 5.83), pull risk 0.068

**OTT @ DET** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 27.75, exp saves 23.94 (sd 6.61), pull risk 0.058
- OTT net: Samuel Ersson (PROJECTED) exp shots 26.38, exp saves 22.79 (sd 6.37), pull risk 0.06

**UTA @ NJD** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NJD net: Jake Allen (PROJECTED) exp shots 26.63, exp saves 22.97 (sd 6.43), pull risk 0.062
- UTA net: Karel Vejmelka (PROJECTED) exp shots 28.76, exp saves 24.97 (sd 6.74), pull risk 0.057

**MIN @ BUF** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- BUF net: Colten Ellis (PROBABLE) exp shots 27.67, exp saves 23.91 (sd 6.62), pull risk 0.066
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 29.86, exp saves 25.77 (sd 7.05), pull risk 0.065

**NYI @ NYR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.05, exp saves 24.5 (sd 6.53), pull risk 0.046
- NYI net: Ilya Sorokin (PROJECTED) exp shots 25.47, exp saves 21.93 (sd 6.21), pull risk 0.065

**STL @ CHI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CHI net: Spencer Knight (PROJECTED) exp shots 27.19, exp saves 23.2 (sd 6.52), pull risk 0.072
- STL net: Joel Hofer (PROJECTED) exp shots 25.55, exp saves 22.28 (sd 6.1), pull risk 0.052

**VGK @ SEA** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- SEA net: Joey Daccord (PROJECTED) exp shots 28.49, exp saves 24.57 (sd 6.72), pull risk 0.062
- VGK net: Carter Hart (PROJECTED) exp shots 25.65, exp saves 22.22 (sd 6.13), pull risk 0.056

**FLA @ LAK** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.39, exp saves 23.09 (sd 6.27), pull risk 0.05
- FLA net: Jacob Markstrom (PROJECTED) exp shots 27.81, exp saves 23.64 (sd 6.56), pull risk 0.066

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
