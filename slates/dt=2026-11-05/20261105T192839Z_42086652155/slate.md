# NHL slate 2026-11-05 — RESEARCH_ONLY

generated 2026-11-05T19:28:39Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 4069 · contracts joined: 2415 (unjoined to any game: 1275)
gates: {'UNSUPPORTED': 2140, 'OK': 125, 'NO_EDGE': 150}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'player_assists': 321, 'game_early_goal': 11, 'first_goal': 394, 'game_winner': 22, 'player_goals': 683, 'game_overtime': 11, 'player_points': 442, 'goalie_saves': 14, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 2026-11-06T00:00:00Z | T-3h | 0.518 | 0.482 | 0.166 | 6.53 | 3.33 | 3.20 | 219 (25/194) | CONFIRMED/PROBABLE |
| VGK @ DET | 2026-11-06T00:00:00Z | T-3h | 0.513 | 0.487 | 0.179 | 6.06 | 3.06 | 3.00 | 217 (25/192) | PROBABLE/PROJECTED |
| CHI @ TBL | 2026-11-06T00:00:00Z | T-3h | 0.752 | 0.248 | 0.143 | 6.30 | 4.00 | 2.30 | 212 (25/187) | PROBABLE/PROJECTED |
| STL @ NJD | 2026-11-06T00:00:00Z | T-3h | 0.658 | 0.342 | 0.157 | 6.58 | 3.81 | 2.77 | 223 (25/198) | PROBABLE/CONFIRMED |
| CAR @ NYI | 2026-11-06T00:00:00Z | T-3h | 0.447 | 0.553 | 0.178 | 6.05 | 2.86 | 3.19 | 216 (25/191) | CONFIRMED/PROJECTED |
| PHI @ NYR | 2026-11-06T00:00:00Z | T-3h | 0.629 | 0.371 | 0.175 | 5.99 | 3.39 | 2.61 | 229 (25/204) | CONFIRMED/CONFIRMED |
| BOS @ PIT | 2026-11-06T00:00:00Z | T-3h | 0.452 | 0.548 | 0.176 | 6.53 | 3.10 | 3.43 | 223 (25/198) | CONFIRMED/PROJECTED |
| DAL @ CBJ | 2026-11-06T00:00:00Z | T-3h | 0.433 | 0.567 | 0.181 | 5.99 | 2.80 | 3.19 | 207 (25/182) | CONFIRMED/CONFIRMED |
| VAN @ WPG | 2026-11-06T00:00:00Z | T-3h | 0.609 | 0.391 | 0.167 | 6.46 | 3.58 | 2.88 | 211 (25/186) | CONFIRMED/PROBABLE |
| ANA @ EDM | 2026-11-06T01:00:00Z | T-3h | 0.641 | 0.359 | 0.157 | 7.01 | 4.00 | 3.01 | 235 (25/210) | PROBABLE/PROBABLE |
| NSH @ COL | 2026-11-06T02:30:00Z | T-6h | 0.654 | 0.346 | 0.161 | 6.59 | 3.80 | 2.79 | 223 (25/198) | CONFIRMED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26NOV05CARNYI-NYI | game_winner | 0.447 | 0.355 | 0.373 | 36 | 65 | yes | +0.071 | OK |
| KXNHLGAME-26NOV05CARNYI-CAR | game_winner | 0.553 | 0.645 | 0.627 | 65 | 36 | no | +0.071 | OK |
| KXNHLGAME-26NOV05VGKDET-VGK | game_winner | 0.487 | 0.575 | 0.558 | 58 | 43 | no | +0.066 | OK |
| KXNHLTOTAL-26NOV05STLNJ-8 | game_total | 0.317 | 0.235 | 0.250 | 24 | 77 | yes | +0.064 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR2 | game_spread | 0.325 | 0.405 | 0.388 | 41 | 60 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR4 | team_total | 0.406 | 0.485 | 0.469 | 49 | 52 | no | +0.057 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK3 | game_spread | 0.162 | 0.235 | 0.219 | 24 | 77 | no | +0.056 | OK |
| KXNHLGAME-26NOV05VGKDET-DET | game_winner | 0.513 | 0.435 | 0.450 | 44 | 57 | yes | +0.056 | OK |
| KXNHLSPREAD-26NOV05CARNYI-CAR3 | game_spread | 0.201 | 0.280 | 0.263 | 29 | 73 | no | +0.055 | OK |
| KXNHLTOTAL-26NOV05STLNJ-6 | game_total | 0.621 | 0.545 | 0.561 | 55 | 46 | yes | +0.054 | OK |
| KXNHLSPREAD-26NOV05VGKDET-VGK2 | game_spread | 0.273 | 0.345 | 0.330 | 35 | 66 | no | +0.052 | OK |
| KXNHLTOTAL-26NOV05STLNJ-7 | game_total | 0.507 | 0.435 | 0.449 | 44 | 57 | yes | +0.050 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB3 | game_spread | 0.394 | 0.465 | 0.451 | 47 | 54 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB4 | team_total | 0.579 | 0.645 | 0.632 | 65 | 36 | no | +0.045 | OK |
| KXNHLSPREAD-26NOV05CHITB-TB2 | game_spread | 0.541 | 0.605 | 0.592 | 61 | 40 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 | team_total | 0.363 | 0.430 | 0.416 | 44 | 58 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR3 | team_total | 0.625 | 0.695 | 0.682 | 71 | 32 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB5 | team_total | 0.374 | 0.435 | 0.423 | 44 | 57 | no | +0.039 | OK |
| KXNHLGAME-26NOV05CHITB-CHI | game_winner | 0.248 | 0.195 | 0.205 | 20 | 81 | yes | +0.037 | OK |
| KXNHLGAME-26NOV05CHITB-TB | game_winner | 0.752 | 0.805 | 0.795 | 81 | 20 | no | +0.037 | OK |
| KXNHLTOTAL-26NOV05STLNJ-9 | game_total | 0.227 | 0.170 | 0.180 | 18 | 84 | yes | +0.037 | OK |
| KXNHLGAME-26NOV05VANWPG-VAN | game_winner | 0.391 | 0.335 | 0.346 | 34 | 67 | yes | +0.035 | OK |
| KXNHLTOTAL-26NOV05CHITB-6 | game_total | 0.579 | 0.635 | 0.624 | 64 | 37 | no | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL3 | team_total | 0.522 | 0.465 | 0.476 | 47 | 54 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ6 | team_total | 0.183 | 0.125 | 0.135 | 14 | 89 | yes | +0.035 | OK |
| KXNHLSPREAD-26NOV05VGKDET-DET2 | game_spread | 0.287 | 0.235 | 0.245 | 24 | 77 | yes | +0.035 | OK |
| KXNHLGAME-26NOV05PHINYR-NYR | game_winner | 0.629 | 0.570 | 0.582 | 58 | 44 | yes | +0.032 | OK |
| KXNHLGAME-26NOV05PHINYR-PHI | game_winner | 0.371 | 0.425 | 0.414 | 43 | 58 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB3 | team_total | 0.779 | 0.825 | 0.816 | 83 | 18 | no | +0.031 | OK |
| KXNHLGAME-26NOV05UTAMTL-MTL | game_winner | 0.518 | 0.465 | 0.476 | 47 | 54 | yes | +0.031 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA3 | game_spread | 0.167 | 0.215 | 0.205 | 22 | 79 | no | +0.031 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 | team_total | 0.345 | 0.290 | 0.301 | 30 | 72 | yes | +0.030 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG3 | game_spread | 0.255 | 0.310 | 0.299 | 32 | 70 | no | +0.030 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL2 | game_spread | 0.313 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLSPREAD-26NOV05CARNYI-NYI2 | game_spread | 0.239 | 0.195 | 0.203 | 20 | 81 | yes | +0.028 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR5 | team_total | 0.220 | 0.270 | 0.260 | 28 | 74 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT3 | game_spread | 0.144 | 0.190 | 0.180 | 20 | 82 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-UTA2 | game_spread | 0.279 | 0.325 | 0.315 | 33 | 68 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA4 | team_total | 0.407 | 0.460 | 0.449 | 47 | 55 | no | +0.026 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI2 | game_spread | 0.183 | 0.225 | 0.216 | 23 | 78 | no | +0.025 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI3 | team_total | 0.487 | 0.535 | 0.526 | 54 | 47 | no | +0.025 | OK |
| KXNHLGAME-26NOV05VANWPG-WPG | game_winner | 0.609 | 0.660 | 0.650 | 67 | 35 | no | +0.025 | OK |
| KXNHLSPREAD-26NOV05PHINYR-PHI3 | game_spread | 0.098 | 0.135 | 0.127 | 14 | 87 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK2 | team_total | 0.796 | 0.845 | 0.836 | 86 | 17 | no | +0.024 | OK |
| KXNHLTOTAL-26NOV05STLNJ-5 | game_total | 0.815 | 0.770 | 0.780 | 78 | 24 | yes | +0.023 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3 | team_total | 0.550 | 0.505 | 0.514 | 51 | 50 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI4 | team_total | 0.273 | 0.320 | 0.310 | 33 | 69 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05UTAMTL-UTA3 | team_total | 0.622 | 0.670 | 0.661 | 68 | 34 | no | +0.022 | OK |
| KXNHLTOTAL-26NOV05CHITB-7 | game_total | 0.461 | 0.505 | 0.496 | 51 | 50 | no | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL6 | team_total | 0.064 | 0.035 | 0.040 | 4 | 97 | yes | +0.022 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK3 | team_total | 0.582 | 0.630 | 0.621 | 64 | 38 | no | +0.022 | OK |
| KXNHLGAME-26NOV05BOSPIT-BOS | game_winner | 0.548 | 0.505 | 0.514 | 51 | 50 | yes | +0.021 | OK |
| KXNHLGAME-26NOV05BOSPIT-PIT | game_winner | 0.452 | 0.495 | 0.486 | 50 | 51 | no | +0.021 | OK |
| KXNHLGAME-26NOV05UTAMTL-UTA | game_winner | 0.482 | 0.525 | 0.516 | 53 | 48 | no | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET4 | team_total | 0.376 | 0.325 | 0.335 | 34 | 69 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET3 | team_total | 0.597 | 0.550 | 0.560 | 56 | 46 | yes | +0.020 | OK |
| KXNHLTOTAL-26NOV05STLNJ-4 | game_total | 0.888 | 0.850 | 0.858 | 86 | 16 | yes | +0.020 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4 | team_total | 0.334 | 0.295 | 0.303 | 30 | 71 | yes | +0.019 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-PIT2 | game_spread | 0.247 | 0.285 | 0.277 | 29 | 72 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-VGK5 | team_total | 0.189 | 0.230 | 0.221 | 24 | 78 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26NOV05VGKDET-DET5 | team_total | 0.198 | 0.155 | 0.163 | 17 | 86 | yes | +0.018 | OK |
| KXNHLTOTAL-26NOV05CARNYI-5 | game_total | 0.750 | 0.785 | 0.778 | 79 | 22 | no | +0.018 | OK |
| KXNHLTOTAL-26NOV05STLNJ-10 | game_total | 0.113 | 0.075 | 0.082 | 9 | 94 | yes | +0.018 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ3 | team_total | 0.741 | 0.700 | 0.709 | 71 | 31 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV05CHITB-8 | game_total | 0.278 | 0.315 | 0.307 | 32 | 69 | no | +0.017 | OK |
| KXNHLSPREAD-26NOV05PHINYR-NYR2 | game_spread | 0.393 | 0.355 | 0.362 | 36 | 65 | yes | +0.017 | OK |
| KXNHLTOTAL-26NOV05CHITB-5 | game_total | 0.783 | 0.815 | 0.809 | 82 | 19 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05CARNYI-CAR2 | team_total | 0.825 | 0.865 | 0.858 | 88 | 15 | no | +0.017 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-NJ4 | team_total | 0.543 | 0.495 | 0.505 | 51 | 52 | yes | +0.015 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL4 | team_total | 0.309 | 0.265 | 0.274 | 28 | 75 | yes | +0.015 | OK |
| KXNHLSPREAD-26NOV05VANWPG-WPG2 | game_spread | 0.388 | 0.425 | 0.418 | 43 | 58 | no | +0.015 | OK |
| KXNHLSPREAD-26NOV05BOSPIT-BOS2 | game_spread | 0.329 | 0.295 | 0.302 | 30 | 71 | yes | +0.014 | OK |
| KXNHLSPREAD-26NOV05UTAMTL-MTL3 | game_spread | 0.194 | 0.165 | 0.171 | 17 | 84 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05VANWPG-VAN5 | team_total | 0.173 | 0.140 | 0.146 | 15 | 87 | yes | +0.014 | OK |
| KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 | team_total | 0.390 | 0.430 | 0.422 | 44 | 58 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05STLNJ-STL5 | team_total | 0.151 | 0.115 | 0.122 | 13 | 90 | yes | +0.013 | OK |
| KXNHLSPREAD-26NOV05DALCBJ-CBJ3 | game_spread | 0.128 | 0.155 | 0.149 | 16 | 85 | no | +0.013 | OK |
| KXNHLTEAMTOTAL-26NOV05CHITB-TB2 | team_total | 0.913 | 0.940 | 0.935 | 95 | 7 | no | +0.013 | OK |
| KXNHLSPREAD-26NOV05VANWPG-VAN2 | game_spread | 0.203 | 0.175 | 0.180 | 18 | 83 | yes | +0.012 | OK |
| KXNHLTEAMTOTAL-26NOV05PHINYR-PHI2 | team_total | 0.725 | 0.765 | 0.757 | 78 | 25 | no | +0.012 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| UTA @ MTL | 0.518 | 0.522 | 0.166 | 0.211 | 6.53 | 6.52 | 0.943/0.999 | KXNHLSPREAD-26NOV05UTAMTL-UTA2 -0.013 |
| VGK @ DET | 0.513 | 0.451 | 0.179 | 0.215 | 6.06 | 6.28 | 1.020/1.004 | KXNHLTEAMTOTAL-26NOV05VGKDET-VGK4 +0.068 |
| CHI @ TBL | 0.752 | 0.719 | 0.143 | 0.183 | 6.30 | 6.37 | 0.952/1.026 | KXNHLTEAMTOTAL-26NOV05CHITB-CHI3 +0.047 |
| STL @ NJD | 0.658 | 0.582 | 0.157 | 0.216 | 6.58 | 6.28 | 0.954/1.032 | KXNHLTEAMTOTAL-26NOV05STLNJ-NJ5 -0.093 |
| CAR @ NYI | 0.447 | 0.470 | 0.178 | 0.221 | 6.05 | 6.40 | 0.978/0.990 | KXNHLTOTAL-26NOV05CARNYI-7 +0.061 |
| PHI @ NYR | 0.629 | 0.540 | 0.175 | 0.224 | 5.99 | 5.98 | 0.988/0.991 | KXNHLGAME-26NOV05PHINYR-NYR -0.090 |
| BOS @ PIT | 0.452 | 0.517 | 0.176 | 0.212 | 6.53 | 6.71 | 1.042/0.969 | KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT4 +0.072 |
| DAL @ CBJ | 0.433 | 0.509 | 0.181 | 0.223 | 5.99 | 6.13 | 1.008/0.969 | KXNHLGAME-26NOV05DALCBJ-DAL -0.076 |
| VAN @ WPG | 0.609 | 0.547 | 0.167 | 0.214 | 6.46 | 6.33 | 1.004/1.030 | KXNHLSPREAD-26NOV05VANWPG-WPG2 -0.064 |
| ANA @ EDM | 0.641 | 0.571 | 0.157 | 0.207 | 7.01 | 7.11 | 0.999/0.976 | KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA3 +0.072 |
| NSH @ COL | 0.654 | 0.655 | 0.161 | 0.199 | 6.59 | 6.65 | 0.979/1.000 | KXNHLSPREAD-26NOV05NSHCOL-COL3 +0.015 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 38 recommended · full analysis in card.md / packet.json `thesis_card`

- Lawson Crouse: 1+ goals YES @ 18c · p 0.2254 (adj 0.2115) · $3.16 · thesis UTA:OFFENSE_4PLUS
- Cole Caufield: 1+ assists YES @ 33c · p 0.4133 (adj 0.3691) · $3.52 · thesis MTL:OFFENSE_4PLUS
- Utah wins by over 2.5 goals NO @ 79c · p 0.8409 (adj 0.813) · $6.11 · thesis MTL:WINS
- Utah wins by over 1.5 goals NO @ 68c · p 0.7394 (adj 0.7072) · $1.79 · thesis MTL:WINS
- Brayden McNabb: 1+ goals YES @ 5c · p 0.078 (adj 0.0685) · $1.59 · thesis VGK:OFFENSE_4PLUS
- Lucas Raymond: 2+ assists NO @ 88c · p 0.9271 (adj 0.8985) · $9.22 · thesis DET:SUPPRESSED
- Tampa Bay wins by over 2.5 goals NO @ 54c · p 0.6349 (adj 0.585) · $7.65 · thesis GAME:TIGHT
- Tyler Bertuzzi: 1+ goals YES @ 19c · p 0.2349 (adj 0.2224) · $2.89 · thesis CHI:OFFENSE_4PLUS
- Andrei Vasilevskiy: 19+ saves YES @ 50c · p 0.6505 (adj 0.5364) · $5.22 · thesis CHI:SHOT_CONTROL
- Connor Bedard: 1+ assists NO @ 58c · p 0.641 (adj 0.608) · $5.71 · thesis CHI:SUPPRESSED
- Robert Thomas: 1+ goals YES @ 19c · p 0.2633 (adj 0.2437) · $5.7 · thesis STL:OFFENSE_4PLUS
- Jimmy Snuggerud: 1+ goals YES @ 25c · p 0.304 (adj 0.2893) · $3.91 · thesis STL:OFFENSE_4PLUS
- Jack Hughes: 1+ goals NO @ 60c · p 0.6516 (adj 0.6374) · $5.79 · thesis NJD:SUPPRESSED
- Dylan Holloway: 1+ goals YES @ 23c · p 0.2705 (adj 0.2591) · $2.36 · thesis STL:OFFENSE_4PLUS
- Ondrej Palat: 1+ goals YES @ 11c · p 0.1581 (adj 0.1436) · $3.16 · thesis NYI:OFFENSE_4PLUS
- Jean-Gabriel Pageau: 1+ goals YES @ 13c · p 0.1697 (adj 0.1585) · $2.58 · thesis NYI:OFFENSE_4PLUS
- Nikolaj Ehlers: 1+ goals NO @ 73c · p 0.7828 (adj 0.7684) · $7.37 · thesis CAR:SUPPRESSED
- Sebastian Aho: 1+ goals NO @ 68c · p 0.7342 (adj 0.7181) · $6.46 · thesis CAR:SUPPRESSED
- Tye Kartye: 1+ assists YES @ 23c · p 0.306 (adj 0.2655) · $3.3 · thesis NYR:OFFENSE_4PLUS
- Travis Sanheim: 1+ assists YES @ 25c · p 0.3058 (adj 0.2754) · $1.74 · thesis PHI:OFFENSE_4PLUS
- Pavel Dorofeyev: 1+ goals NO @ 68c · p 0.7176 (adj 0.7069) · $5.2 · thesis NYR:SUPPRESSED
- Connor Dewar: 1+ goals YES @ 13c · p 0.1775 (adj 0.1631) · $3.1 · thesis PIT:WINS_BY_2PLUS
- Blake Lizotte: 1+ goals YES @ 11c · p 0.1401 (adj 0.1301) · $1.58 · thesis PIT:WINS_BY_2PLUS
- Nick Robertson: 1+ goals YES @ 15c · p 0.1828 (adj 0.1734) · $1.89 · thesis PIT:OFFENSE_4PLUS
- Ben Kindel: 1+ assists NO @ 69c · p 0.7562 (adj 0.7206) · $7.52 · thesis PIT:SUPPRESSED
- Charlie Coyle: 1+ goals YES @ 23c · p 0.2832 (adj 0.2674) · $3.63 · thesis CBJ:OFFENSE_4PLUS
- Mathieu Olivier: 1+ goals YES @ 17c · p 0.2104 (adj 0.1978) · $2.39 · thesis CBJ:WINS_BY_2PLUS
- Cole Sillinger: 1+ goals YES @ 14c · p 0.1783 (adj 0.1637) · $1.84 · thesis CBJ:OFFENSE_4PLUS
- Roope Hintz: 1+ goals YES @ 26c · p 0.2978 (adj 0.2871) · $2.24 · thesis DAL:OFFENSE_4PLUS
- Linus Karlsson: 1+ goals YES @ 16c · p 0.2311 (adj 0.2121) · $5.38 · thesis VAN:OFFENSE_4PLUS
- Marco Rossi: 1+ goals YES @ 16c · p 0.218 (adj 0.2022) · $4.19 · thesis VAN:OFFENSE_4PLUS
- Brendan Gallagher: 1+ goals YES @ 11c · p 0.1516 (adj 0.1387) · $2.49 · thesis VAN:OFFENSE_4PLUS
- Dylan Samberg: 1+ goals YES @ 5c · p 0.0738 (adj 0.0641) · $1.06 · thesis WPG:OFFENSE_4PLUS
- Jeff Malott: 1+ goals YES @ 8c · p 0.127 (adj 0.114) · $3.21 · thesis ANA:OFFENSE_4PLUS
- Alex Killorn: 1+ goals YES @ 16c · p 0.199 (adj 0.188) · $2.46 · thesis ANA:OFFENSE_4PLUS
- Sam Colangelo: 1+ goals YES @ 13c · p 0.1627 (adj 0.152) · $1.82 · thesis ANA:OFFENSE_4PLUS
- Connor McDavid: 1+ assists NO @ 30c · p 0.4215 (adj 0.3328) · $2.71 · thesis EDM:SUPPRESSED
- Mavrik Bourque: 1+ assists NO @ 72c · p 0.7959 (adj 0.7505) · $8.04 · thesis NSH:SUPPRESSED

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**UTA @ MTL** · priced 167/168 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MTL net: Jakub Dobes (CONFIRMED) exp shots 28.98, exp saves 25.12 (sd 6.84), pull risk 0.062
- UTA net: Sebastian Cossa (PROBABLE) exp shots 25.81, exp saves 22.17 (sd 6.29), pull risk 0.073

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mikhail Sergachev: 1+ points | 0.500 | 0.590 | 61/43 | +0.053 | STANDARD |
| Lawson Crouse: 1+ points | 0.429 | 0.340 | 35/67 | +0.063 | STANDARD |
| Cole Caufield: 1+ assists | 0.413 | 0.325 | 33/68 | +0.068 | STANDARD |
| Logan Cooley: 1+ points | 0.520 | 0.600 | 61/41 | +0.053 | STANDARD |
| Lawson Crouse: 1+ assists | 0.263 | 0.185 | 21/84 | +0.041 | STANDARD |
| Noah Dobson: 1+ assists | 0.370 | 0.300 | 32/72 | +0.035 | STANDARD |

**VGK @ DET** · priced 158/166 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (PROBABLE) exp shots 26.45, exp saves 22.72 (sd 6.46), pull risk 0.069
- VGK net: Carter Hart (PROJECTED) exp shots 27.41, exp saves 23.76 (sd 6.48), pull risk 0.055

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mitch Marner: 1+ assists | 0.426 | 0.515 | 53/50 | +0.057 | STANDARD |
| Jack Eichel: 1+ assists | 0.445 | 0.525 | 54/49 | +0.047 | STANDARD |
| Ivan Barbashev: 1+ assists | 0.356 | 0.280 | 30/74 | +0.041 | STANDARD |
| Ivan Barbashev: 1+ points | 0.500 | 0.425 | 43/58 | +0.053 | STANDARD |
| Jack Eichel: 2+ points | 0.235 | 0.310 | 33/71 | +0.040 | STANDARD |
| Mark Stone: 1+ assists | 0.376 | 0.445 | 46/57 | +0.037 | STANDARD |

**CHI @ TBL** · priced 150/161 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROBABLE) exp shots 23.1, exp saves 20.72 (sd 5.7), pull risk 0.037
- CHI net: Arvid Soderblom (PROJECTED) exp shots 30.41, exp saves 25.23 (sd 7.29), pull risk 0.107

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Andrei Vasilevskiy: 19+ saves | 0.650 | 0.475 | 50/55 | +0.133 |  |
| Arvid Soderblom: 28+ saves | 0.377 | 0.505 | 52/51 | +0.096 |  |
| Nikita Kucherov: 2+ points | 0.397 | 0.495 | 50/51 | +0.076 | STANDARD |
| Nikita Kucherov: 1+ assists | 0.575 | 0.660 | 67/35 | +0.060 | STANDARD |
| Nikita Kucherov: 2+ assists | 0.213 | 0.295 | 31/72 | +0.053 | STANDARD |
| Nikita Kucherov: 3+ points | 0.155 | 0.225 | 23/78 | +0.053 | STANDARD |

**STL @ NJD** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Connor Hellebuyck (PROBABLE) exp shots 24.87, exp saves 21.6 (sd 6.06), pull risk 0.055
- STL net: Jordan Binnington (CONFIRMED) exp shots 30.21, exp saves 25.9 (sd 7.1), pull risk 0.072

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Jack Hughes: 1+ assists | 0.420 | 0.530 | 54/48 | +0.082 | STANDARD |
| Dylan Holloway: 1+ points | 0.542 | 0.435 | 45/58 | +0.074 | STANDARD |
| Jack Hughes: 2+ points | 0.259 | 0.365 | 38/65 | +0.075 | STANDARD |
| Luke Evangelista: 1+ assists | 0.247 | 0.350 | 37/67 | +0.067 | STANDARD |
| Jordan Binnington: 28+ saves | 0.406 | 0.495 | 51/52 | +0.057 |  |
| Dylan Holloway: 1+ assists | 0.373 | 0.285 | 29/72 | +0.069 | STANDARD |

**CAR @ NYI** · priced 162/165 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYI net: Semyon Varlamov (CONFIRMED) exp shots 29.43, exp saves 25.26 (sd 6.94), pull risk 0.067
- CAR net: Brandon Bussi (PROJECTED) exp shots 24.49, exp saves 21.24 (sd 6.06), pull risk 0.059

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Sebastian Aho: 1+ points | 0.506 | 0.630 | 64/38 | +0.097 | STANDARD |
| Sebastian Aho: 1+ assists | 0.329 | 0.445 | 46/57 | +0.084 | STANDARD |
| Andrei Svechnikov: 1+ points | 0.494 | 0.585 | 60/43 | +0.059 | STANDARD |
| Andrei Svechnikov: 2+ points | 0.146 | 0.235 | 25/78 | +0.062 | STANDARD |
| Sebastian Aho: 2+ points | 0.157 | 0.245 | 26/77 | +0.061 | STANDARD |
| Andrei Svechnikov: 1+ assists | 0.309 | 0.395 | 41/62 | +0.055 | STANDARD |

**PHI @ NYR** · priced 177/178 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (CONFIRMED) exp shots 25.8, exp saves 22.51 (sd 6.14), pull risk 0.049
- PHI net: Joseph Woll (CONFIRMED) exp shots 26.19, exp saves 22.68 (sd 6.17), pull risk 0.057

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Tye Kartye: 1+ assists | 0.306 | 0.225 | 23/78 | +0.064 | STANDARD |
| Dylan Garand: 22+ saves | 0.562 | 0.485 | 51/54 | +0.034 |  |
| Travis Konecny: 1+ points | 0.420 | 0.495 | 51/52 | +0.043 | STANDARD |
| Christian Dvorak: 1+ points | 0.445 | 0.375 | 40/65 | +0.028 | STANDARD |
| Alexis Lafreniere: 2+ points | 0.212 | 0.145 | 20/91 | +0.001 | STANDARD |
| Travis Sanheim: 1+ points | 0.374 | 0.310 | 33/71 | +0.029 | STANDARD |

**BOS @ PIT** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PIT net: Arturs Silovs (CONFIRMED) exp shots 25.87, exp saves 22.21 (sd 6.39), pull risk 0.073
- BOS net: Jeremy Swayman (PROJECTED) exp shots 29.12, exp saves 25.04 (sd 6.84), pull risk 0.079

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| David Pastrnak: 1+ assists | 0.461 | 0.545 | 55/46 | +0.062 | STANDARD |
| Sidney Crosby: 1+ assists | 0.402 | 0.480 | 49/53 | +0.050 | STANDARD |
| David Pastrnak: 2+ points | 0.280 | 0.355 | 36/65 | +0.054 | STANDARD |
| Ben Kindel: 1+ assists | 0.244 | 0.315 | 32/69 | +0.051 | STANDARD |
| Pavel Zacha: 1+ assists | 0.359 | 0.430 | 44/58 | +0.044 | STANDARD |
| Charlie McAvoy: 1+ assists | 0.399 | 0.470 | 48/54 | +0.044 | STANDARD |

**DAL @ CBJ** · priced 151/156 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CBJ net: Cam Talbot (CONFIRMED) exp shots 25.44, exp saves 22.08 (sd 6.18), pull risk 0.055
- DAL net: Casey DeSmith (CONFIRMED) exp shots 25.62, exp saves 22.16 (sd 6.17), pull risk 0.061

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Charlie Coyle: 1+ goals | 0.283 | 0.220 | 23/79 | +0.041 | STANDARD |
| Cole Sillinger: 1+ goals | 0.178 | 0.120 | 14/90 | +0.030 | STANDARD |
| Mathieu Olivier: 1+ goals | 0.210 | 0.160 | 17/85 | +0.031 | STANDARD |
| Mikko Rantanen: 1+ assists | 0.437 | 0.485 | 51/54 | +0.006 | STANDARD |
| Arttu Hyry: 1+ points | 0.338 | 0.290 | 31/73 | +0.013 | STANDARD |
| Sean Monahan: 1+ goals | 0.197 | 0.150 | 17/87 | +0.017 | STANDARD |

**VAN @ WPG** · priced 153/160 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WPG net: Stuart Skinner (CONFIRMED) exp shots 24.76, exp saves 21.54 (sd 6.0), pull risk 0.056
- VAN net: Leevi Merilainen (PROBABLE) exp shots 29.31, exp saves 25.02 (sd 6.89), pull risk 0.07

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Elias Pettersson (#40): 1+ goals | 0.229 | 0.140 | 24/96 | -0.023 | STANDARD |
| Mark Scheifele: 1+ assists | 0.506 | 0.590 | 60/42 | +0.057 | STANDARD |
| Kyle Connor: 2+ points | 0.304 | 0.385 | 41/64 | +0.040 | STANDARD |
| Neal Pionk: 1+ points | 0.463 | 0.540 | 55/47 | +0.049 | STANDARD |
| Linus Karlsson: 1+ goals | 0.231 | 0.155 | 16/85 | +0.062 | STANDARD |
| Kyle Connor: 1+ assists | 0.435 | 0.510 | 52/50 | +0.048 | STANDARD |

**ANA @ EDM** · priced 183/184 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Matt Tomkins (PROBABLE) exp shots 27.9, exp saves 24.15 (sd 6.78), pull risk 0.075
- ANA net: Laurent Brossoit (PROBABLE) exp shots 27.83, exp saves 23.64 (sd 6.82), pull risk 0.089

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Matt Tomkins: 25+ saves | 0.481 | 0.325 | 44/79 | +0.024 |  |
| Leon Draisaitl: 2+ points | 0.378 | 0.515 | 53/50 | +0.104 | STANDARD |
| Connor McDavid: 1+ assists | 0.579 | 0.715 | 73/30 | +0.107 | STANDARD |
| Connor McDavid: 2+ points | 0.446 | 0.580 | 60/44 | +0.096 | STANDARD |
| Connor McDavid: 2+ assists | 0.218 | 0.345 | 36/67 | +0.096 | STANDARD |
| Leon Draisaitl: 3+ points | 0.141 | 0.265 | 28/75 | +0.095 | STANDARD |

**NSH @ COL** · priced 171/172 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- COL net: Mackenzie Blackwood (CONFIRMED) exp shots 25.73, exp saves 22.64 (sd 6.23), pull risk 0.051
- NSH net: Juuse Saros (PROJECTED) exp shots 32.54, exp saves 27.26 (sd 7.57), pull risk 0.094

| contract | P(model) | P(mkt) | yes/no ask | best EV after fee | quality |
|---|---:|---:|---|---:|---|
| Mavrik Bourque: 1+ assists | 0.204 | 0.295 | 31/72 | +0.062 | STANDARD |
| Nathan MacKinnon: 2+ points | 0.381 | 0.460 | 48/56 | +0.042 | STANDARD |
| Nathan MacKinnon: 2+ assists | 0.172 | 0.250 | 27/77 | +0.046 | STANDARD |
| Nathan MacKinnon: 1+ assists | 0.527 | 0.605 | 62/41 | +0.046 | STANDARD |
| Mavrik Bourque: 1+ points | 0.353 | 0.425 | 44/59 | +0.040 | STANDARD |
| Mackenzie Blackwood: 22+ saves | 0.571 | 0.515 | 53/50 | +0.023 |  |

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
