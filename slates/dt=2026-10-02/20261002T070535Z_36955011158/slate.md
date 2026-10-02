# NHL slate 2026-10-02 — RESEARCH_ONLY

generated 2026-10-02T07:05:35Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 5 · simulated (not started): 5 · markets on board: 2569 · contracts joined: 255 (unjoined to any game: 1524)
gates: {'UNSUPPORTED': 130, 'NO_EDGE': 43, 'OK': 82}
families: {'period_winner': 45, 'period_spread': 30, 'period_total': 45, 'game_early_goal': 5, 'game_winner': 10, 'game_overtime': 5, 'game_spread': 20, 'team_total': 50, 'game_total': 45}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 2026-10-02T22:30:00Z | T-12h | 0.523 | 0.477 | 0.183 | 5.87 | 3.01 | 2.86 | 51 (25/26) | PROJECTED/PROJECTED |
| WSH @ CAR | 2026-10-02T23:00:00Z | T-12h | 0.530 | 0.470 | 0.186 | 5.85 | 3.01 | 2.84 | 51 (25/26) | PROJECTED/CONFIRMED |
| BOS @ WPG | 2026-10-03T00:00:00Z | T-12h | 0.495 | 0.505 | 0.182 | 5.78 | 2.87 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ DAL | 2026-10-03T01:00:00Z | T-12h | 0.538 | 0.462 | 0.174 | 5.97 | 3.10 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| ANA @ VGK | 2026-10-03T02:00:00Z | T-12h | 0.595 | 0.405 | 0.169 | 6.41 | 3.51 | 2.91 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT02STLDAL-DAL2 | game_spread | 0.314 | 0.405 | 0.386 | 41 | 60 | no | +0.070 | OK |
| KXNHLGAME-26OCT02STLDAL-DAL | game_winner | 0.538 | 0.625 | 0.608 | 63 | 38 | no | +0.065 | OK |
| KXNHLGAME-26OCT02STLDAL-STL | game_winner | 0.462 | 0.375 | 0.392 | 38 | 63 | yes | +0.065 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL4 | team_total | 0.388 | 0.485 | 0.465 | 50 | 53 | no | +0.064 | OK |
| KXNHLSPREAD-26OCT02STLDAL-DAL3 | game_spread | 0.186 | 0.270 | 0.251 | 28 | 74 | no | +0.061 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL2 | game_spread | 0.253 | 0.185 | 0.197 | 19 | 82 | yes | +0.052 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-6 | game_total | 0.501 | 0.580 | 0.564 | 59 | 43 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-7 | game_total | 0.393 | 0.465 | 0.450 | 47 | 54 | no | +0.050 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL3 | team_total | 0.607 | 0.685 | 0.670 | 70 | 33 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 | team_total | 0.367 | 0.450 | 0.433 | 47 | 57 | no | +0.046 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL5 | team_total | 0.203 | 0.275 | 0.259 | 29 | 74 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR3 | game_spread | 0.175 | 0.235 | 0.222 | 24 | 77 | no | +0.042 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-4 | game_total | 0.822 | 0.880 | 0.870 | 89 | 13 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-5 | game_total | 0.728 | 0.790 | 0.779 | 80 | 22 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR5 | team_total | 0.191 | 0.255 | 0.241 | 27 | 76 | no | +0.037 | OK |
| KXNHLGAME-26OCT02WSHCAR-CAR | game_winner | 0.530 | 0.585 | 0.574 | 59 | 42 | no | +0.033 | OK |
| KXNHLGAME-26OCT02WSHCAR-WSH | game_winner | 0.470 | 0.415 | 0.426 | 42 | 59 | yes | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL2 | team_total | 0.810 | 0.860 | 0.851 | 87 | 15 | no | +0.031 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-5 | game_total | 0.718 | 0.765 | 0.756 | 77 | 24 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 | team_total | 0.554 | 0.610 | 0.599 | 62 | 40 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT02NYRDET-5 | game_total | 0.729 | 0.775 | 0.766 | 78 | 23 | no | +0.029 | OK |
| KXNHLSPREAD-26OCT02STLDAL-STL3 | game_spread | 0.145 | 0.105 | 0.112 | 11 | 90 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG4 | team_total | 0.337 | 0.395 | 0.383 | 41 | 62 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR3 | team_total | 0.588 | 0.645 | 0.634 | 66 | 37 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT02WSHCAR-CAR2 | game_spread | 0.299 | 0.345 | 0.335 | 35 | 66 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-9 | game_total | 0.145 | 0.190 | 0.180 | 20 | 82 | no | +0.025 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK3 | game_spread | 0.242 | 0.285 | 0.276 | 29 | 72 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET4 | team_total | 0.369 | 0.425 | 0.414 | 44 | 59 | no | +0.024 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-7 | game_total | 0.380 | 0.430 | 0.420 | 44 | 58 | no | +0.023 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG3 | game_spread | 0.157 | 0.195 | 0.187 | 20 | 81 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-8 | game_total | 0.215 | 0.265 | 0.254 | 28 | 75 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT02NYRDET-4 | game_total | 0.820 | 0.860 | 0.853 | 87 | 15 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-6 | game_total | 0.492 | 0.535 | 0.526 | 54 | 47 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-4 | game_total | 0.811 | 0.850 | 0.843 | 86 | 16 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK4 | team_total | 0.484 | 0.535 | 0.525 | 55 | 48 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET3 | team_total | 0.586 | 0.630 | 0.621 | 64 | 38 | no | +0.018 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET5 | team_total | 0.190 | 0.225 | 0.218 | 23 | 78 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-VGK2 | game_spread | 0.376 | 0.415 | 0.407 | 42 | 59 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26OCT02NYRDET-DET2 | team_total | 0.794 | 0.835 | 0.827 | 85 | 18 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT02NYRDET-7 | game_total | 0.398 | 0.435 | 0.428 | 44 | 57 | no | +0.014 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-8 | game_total | 0.203 | 0.235 | 0.228 | 24 | 77 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG5 | team_total | 0.166 | 0.205 | 0.197 | 22 | 81 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-DAL6 | team_total | 0.090 | 0.130 | 0.121 | 15 | 89 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR2 | team_total | 0.798 | 0.835 | 0.828 | 85 | 18 | no | +0.012 | OK |
| KXNHLSPREAD-26OCT02BOSWPG-WPG2 | game_spread | 0.273 | 0.305 | 0.299 | 31 | 70 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR6 | team_total | 0.082 | 0.115 | 0.108 | 13 | 90 | no | +0.011 | OK |
| KXNHLSPREAD-26OCT02NYRDET-DET3 | game_spread | 0.177 | 0.205 | 0.199 | 21 | 80 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK5 | team_total | 0.284 | 0.330 | 0.321 | 35 | 69 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-5 | game_total | 0.799 | 0.830 | 0.824 | 84 | 18 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL2 | team_total | 0.773 | 0.740 | 0.747 | 75 | 27 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT02NYRDET-DET2 | game_spread | 0.295 | 0.325 | 0.319 | 33 | 68 | no | +0.009 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL3 | team_total | 0.556 | 0.510 | 0.519 | 53 | 51 | yes | +0.009 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.009 | OK |
| KXNHLGAME-26OCT02ANAVGK-VGK | game_winner | 0.595 | 0.625 | 0.619 | 63 | 38 | no | +0.008 | OK |
| KXNHLGAME-26OCT02ANAVGK-ANA | game_winner | 0.405 | 0.375 | 0.381 | 38 | 63 | yes | +0.008 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-3 | game_total | 0.949 | 0.965 | 0.962 | 97 | 4 | no | +0.008 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL5 | team_total | 0.167 | 0.135 | 0.141 | 15 | 88 | yes | +0.008 | OK |
| KXNHLGAME-26OCT02BOSWPG-BOS | game_winner | 0.505 | 0.475 | 0.481 | 48 | 53 | yes | +0.007 | OK |
| KXNHLGAME-26OCT02BOSWPG-WPG | game_winner | 0.495 | 0.525 | 0.519 | 53 | 48 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02STLDAL-4 | game_total | 0.834 | 0.860 | 0.855 | 87 | 15 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-7 | game_total | 0.486 | 0.515 | 0.509 | 52 | 49 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-4 | game_total | 0.876 | 0.905 | 0.900 | 92 | 11 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK3 | team_total | 0.689 | 0.725 | 0.718 | 74 | 29 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-6 | game_total | 0.597 | 0.625 | 0.619 | 63 | 38 | no | +0.007 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-8 | game_total | 0.289 | 0.315 | 0.310 | 32 | 69 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG2 | team_total | 0.773 | 0.800 | 0.795 | 81 | 21 | no | +0.006 | OK |
| KXNHLTOTAL-26OCT02ANAVGK-9 | game_total | 0.203 | 0.230 | 0.224 | 24 | 78 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02NYRDET-3 | game_total | 0.952 | 0.965 | 0.963 | 97 | 4 | no | +0.005 | OK |
| KXNHLTEAMTOTAL-26OCT02STLDAL-STL6 | team_total | 0.069 | 0.050 | 0.053 | 6 | 96 | yes | +0.005 | OK |
| KXNHLTOTAL-26OCT02NYRDET-6 | game_total | 0.507 | 0.535 | 0.529 | 54 | 47 | no | +0.005 | OK |
| KXNHLTOTAL-26OCT02STLDAL-7 | game_total | 0.408 | 0.435 | 0.430 | 44 | 57 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT02WSHCAR-10 | game_total | 0.061 | 0.085 | 0.080 | 10 | 93 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK6 | team_total | 0.137 | 0.170 | 0.163 | 19 | 85 | no | +0.004 | OK |
| KXNHLSPREAD-26OCT02ANAVGK-ANA3 | game_spread | 0.121 | 0.105 | 0.108 | 11 | 90 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT02BOSWPG-9 | game_total | 0.138 | 0.155 | 0.151 | 16 | 85 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT02NYRDET-8 | game_total | 0.215 | 0.235 | 0.231 | 24 | 77 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02NYRDET-9 | game_total | 0.148 | 0.165 | 0.161 | 17 | 84 | no | +0.003 | OK |
| KXNHLTEAMTOTAL-26OCT02ANAVGK-VGK2 | team_total | 0.859 | 0.885 | 0.880 | 90 | 13 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02STLDAL-5 | game_total | 0.745 | 0.770 | 0.765 | 78 | 24 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT02STLDAL-3 | game_total | 0.955 | 0.965 | 0.963 | 97 | 4 | no | +0.002 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NYR @ DET | 0.523 | 0.506 | 0.183 | 0.218 | 5.87 | 6.07 | 1.003/0.957 | KXNHLTEAMTOTAL-26OCT02NYRDET-NYR3 +0.037 |
| WSH @ CAR | 0.530 | 0.560 | 0.186 | 0.226 | 5.85 | 6.25 | 0.997/0.938 | KXNHLTEAMTOTAL-26OCT02WSHCAR-CAR4 +0.073 |
| BOS @ WPG | 0.495 | 0.526 | 0.182 | 0.218 | 5.78 | 6.07 | 0.988/0.968 | KXNHLTEAMTOTAL-26OCT02BOSWPG-WPG3 +0.055 |
| STL @ DAL | 0.538 | 0.545 | 0.174 | 0.218 | 5.97 | 6.13 | 0.986/0.993 | KXNHLTOTAL-26OCT02STLDAL-7 +0.032 |
| ANA @ VGK | 0.595 | 0.598 | 0.169 | 0.213 | 6.41 | 6.41 | 1.003/1.016 | KXNHLSPREAD-26OCT02ANAVGK-VGK3 +0.011 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Dallas wins by over 1.5 goals NO @ 60c · p 0.6781 (adj 0.6365) · $11.01 · thesis STL:WINS
- Dallas wins NO @ 38c · p 0.4514 (adj 0.4132) · $1.11 · thesis STL:WINS
- St. Louis wins by over 1.5 goals YES @ 19c · p 0.2397 (adj 0.2123) · $1.3 · thesis STL:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**NYR @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: John Gibson (PROJECTED) exp shots 25.06, exp saves 21.83 (sd 6.08), pull risk 0.056
- NYR net: Igor Shesterkin (PROJECTED) exp shots 28.53, exp saves 24.68 (sd 6.71), pull risk 0.058

**WSH @ CAR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 23.54, exp saves 20.54 (sd 5.91), pull risk 0.055
- WSH net: Logan Thompson (CONFIRMED) exp shots 30.5, exp saves 26.12 (sd 7.1), pull risk 0.069

**BOS @ WPG** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (PROJECTED) exp shots 26.1, exp saves 22.72 (sd 6.23), pull risk 0.052
- BOS net: Jeremy Swayman (PROJECTED) exp shots 28.24, exp saves 24.34 (sd 6.7), pull risk 0.061

**STL @ DAL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DAL net: Jake Oettinger (PROJECTED) exp shots 24.53, exp saves 21.39 (sd 5.98), pull risk 0.054
- STL net: Joel Hofer (PROJECTED) exp shots 26.73, exp saves 22.84 (sd 6.43), pull risk 0.067

**ANA @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 28.77, exp saves 25.18 (sd 6.72), pull risk 0.051
- ANA net: Lukas Dostal (PROJECTED) exp shots 27.59, exp saves 23.49 (sd 6.62), pull risk 0.075

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
