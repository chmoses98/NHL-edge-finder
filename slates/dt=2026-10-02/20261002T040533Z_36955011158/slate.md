# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T04:05:33Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 3084 · contracts joined: 255 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 130, 'OK': 82, 'NO_EDGE': 43}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'game_early_goal': 5, 'game_winner': 10, 'game_overtime': 5, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 2026-10-02T22:30:00Z | T-12h | 0.523 | 0.477 | 0.182 | 5.88 | 3.02 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| WSH @ CAR | 2026-10-02T23:00:00Z | T-12h | 0.527 | 0.473 | 0.180 | 5.84 | 3.01 | 2.83 | 51 (25/26) | PROJECTED/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-12h | 0.494 | 0.506 | 0.179 | 5.78 | 2.87 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-12h | 0.536 | 0.464 | 0.183 | 5.98 | 3.10 | 2.88 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-12h | 0.595 | 0.405 | 0.168 | 6.42 | 3.51 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.536 | 0.635 | 0.616 | 64 | 37 | no | +0.078 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.310 | 0.405 | 0.385 | 41 | 60 | no | +0.073 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.464 | 0.375 | 0.392 | 38 | 63 | yes | +0.067 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.189 | 0.280 | 0.260 | 29 | 73 | no | +0.067 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.723 | 0.800 | 0.786 | 81 | 21 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.390 | 0.480 | 0.462 | 50 | 54 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.500 | 0.580 | 0.564 | 59 | 43 | no | +0.053 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.391 | 0.465 | 0.450 | 47 | 54 | no | +0.052 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.364 | 0.450 | 0.432 | 47 | 57 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.248 | 0.185 | 0.197 | 19 | 82 | yes | +0.047 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.205 | 0.270 | 0.256 | 28 | 74 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.605 | 0.680 | 0.666 | 70 | 34 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.179 | 0.235 | 0.223 | 24 | 77 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.586 | 0.650 | 0.638 | 66 | 36 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.190 | 0.255 | 0.241 | 27 | 76 | no | +0.037 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.527 | 0.585 | 0.574 | 59 | 42 | no | +0.036 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.473 | 0.415 | 0.426 | 42 | 59 | yes | +0.036 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.816 | 0.875 | 0.865 | 89 | 14 | no | +0.036 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.212 | 0.265 | 0.254 | 27 | 74 | no | +0.034 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.716 | 0.765 | 0.756 | 77 | 24 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.814 | 0.860 | 0.852 | 87 | 15 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.143 | 0.105 | 0.112 | 11 | 90 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.144 | 0.185 | 0.176 | 19 | 82 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.380 | 0.425 | 0.416 | 43 | 58 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.490 | 0.540 | 0.530 | 55 | 47 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.301 | 0.345 | 0.336 | 35 | 66 | no | +0.023 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.480 | 0.525 | 0.516 | 53 | 48 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.331 | 0.395 | 0.382 | 42 | 63 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET4 | team_total | 0.371 | 0.425 | 0.414 | 44 | 59 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT02NYRDET-5 | game_total | 0.735 | 0.775 | 0.767 | 78 | 23 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.244 | 0.285 | 0.277 | 29 | 72 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.284 | 0.335 | 0.324 | 35 | 68 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.811 | 0.855 | 0.847 | 87 | 16 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.557 | 0.500 | 0.511 | 52 | 52 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.483 | 0.535 | 0.525 | 55 | 48 | no | +0.020 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET5 | team_total | 0.190 | 0.225 | 0.218 | 23 | 78 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET3 | team_total | 0.586 | 0.630 | 0.621 | 64 | 38 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.557 | 0.605 | 0.596 | 62 | 41 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT02NYRDET-4 | game_total | 0.826 | 0.860 | 0.854 | 87 | 15 | no | +0.015 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.088 | 0.125 | 0.117 | 14 | 89 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT02NYRDET-6 | game_total | 0.508 | 0.545 | 0.538 | 55 | 46 | no | +0.015 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.272 | 0.305 | 0.298 | 31 | 70 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.860 | 0.890 | 0.885 | 90 | 12 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.798 | 0.835 | 0.828 | 85 | 18 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL4 | team_total | 0.336 | 0.295 | 0.303 | 31 | 72 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR6 | team_total | 0.082 | 0.115 | 0.108 | 13 | 90 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT02NYRDET-7 | game_total | 0.392 | 0.430 | 0.422 | 44 | 58 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.798 | 0.830 | 0.824 | 84 | 18 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.747 | 0.775 | 0.770 | 78 | 23 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT02NYRDET-DET3 | game_spread | 0.178 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.169 | 0.205 | 0.197 | 22 | 81 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET2 | team_total | 0.799 | 0.830 | 0.824 | 84 | 18 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.773 | 0.735 | 0.743 | 75 | 28 | yes | +0.010 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.494 | 0.525 | 0.519 | 53 | 48 | no | +0.009 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.506 | 0.475 | 0.481 | 48 | 53 | yes | +0.009 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.405 | 0.375 | 0.381 | 38 | 63 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.688 | 0.725 | 0.718 | 74 | 29 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT02NYRDET-DET2 | game_spread | 0.297 | 0.325 | 0.319 | 33 | 68 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.167 | 0.135 | 0.141 | 15 | 88 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.876 | 0.900 | 0.896 | 91 | 11 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.376 | 0.405 | 0.399 | 41 | 60 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.597 | 0.625 | 0.619 | 63 | 38 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.951 | 0.965 | 0.963 | 97 | 4 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL6 | team_total | 0.070 | 0.050 | 0.054 | 6 | 96 | yes | +0.006 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.835 | 0.860 | 0.855 | 87 | 15 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.773 | 0.805 | 0.799 | 82 | 21 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02NYRDET-9 | game_total | 0.145 | 0.170 | 0.165 | 18 | 84 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02NYRDET-8 | game_total | 0.212 | 0.240 | 0.234 | 25 | 77 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.203 | 0.230 | 0.224 | 24 | 78 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.291 | 0.320 | 0.314 | 33 | 69 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA2 | game_spread | 0.215 | 0.195 | 0.199 | 20 | 81 | yes | +0.004 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.121 | 0.105 | 0.108 | 11 | 90 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.138 | 0.160 | 0.155 | 17 | 85 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.138 | 0.170 | 0.163 | 19 | 85 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT02NYRDET-3 | game_total | 0.956 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.412 | 0.435 | 0.430 | 44 | 57 | no | +0.001 | OK |
| KXNHLGAME-26OCT02NYRDET-DET | game_winner | 0.523 | 0.545 | 0.541 | 55 | 46 | no | +0.000 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 0.523 | 0.506 | 0.182 | 0.218 | 5.88 | 6.07 | 1.003/0.957 | KXNHLTOTAL-26OCT02NYRDET-7 +0.040 |
| WSH @ CAR | 0.527 | 0.560 | 0.180 | 0.226 | 5.84 | 6.25 | 0.997/0.938 | KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 +0.076 |
| BOS @ WPG | 0.494 | 0.526 | 0.179 | 0.218 | 5.78 | 6.07 | 0.988/0.968 | KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 +0.060 |
| STL @ DAL | 0.536 | 0.545 | 0.183 | 0.218 | 5.98 | 6.13 | 0.986/0.993 | KXNHLTOTAL-26OCT02STLDAL-7 +0.029 |
| ANA @ VGK | 0.595 | 0.598 | 0.168 | 0.213 | 6.42 | 6.41 | 1.003/1.016 | KXNHLTOTAL-26OCT02ANAVGK-8 -0.009 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 2 recommended · full analysis in card.md / packet.json `thesis_card`

- Dallas wins NO @ 37c · p 0.4514 (adj 0.4082) · $5.82 · thesis STL:WINS
- Dallas wins by over 1.5 goals NO @ 60c · p 0.6781 (adj 0.6365) · $7.48 · thesis STL:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ DET** · priced 0/0 player contracts · lineups RECENT_SHIFTS/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 25.06, exp saves 21.85 (sd 6.09), pull risk 0.056
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.53, exp saves 24.73 (sd 6.71), pull risk 0.054

**WSH @ CAR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.54, exp saves 20.55 (sd 5.93), pull risk 0.054
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.11 (sd 7.12), pull risk 0.071

**BOS @ WPG** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.09, exp saves 22.69 (sd 6.22), pull risk 0.053
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.23, exp saves 24.31 (sd 6.67), pull risk 0.061

**STL @ DAL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.53, exp saves 21.39 (sd 5.99), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 26.73, exp saves 22.85 (sd 6.4), pull risk 0.064

**ANA @ VGK** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- VGK net: Carter Hart (PROJECTED) exp shots 28.77, exp saves 25.18 (sd 6.71), pull risk 0.051
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.58, exp saves 23.46 (sd 6.56), pull risk 0.074

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
