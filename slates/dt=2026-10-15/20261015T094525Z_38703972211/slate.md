# NHL slate 2026-10-15 — RESEARCH_ONLY

generated 2026-10-15T09:45:25Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 11 · simulated (not started): 11 · markets on board: 2482 · contracts joined: 561 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 286, 'OK': 184, 'NO_EDGE': 91}
families: {'period_winner': 99, 'period_spread': 66, 'period_total': 99, 'game_early_goal': 11, 'game_winner': 22, 'game_overtime': 11, 'game_spread': 44, 'team_total': 110, 'game_total': 99}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 2026-10-15T23:00:00Z | T-12h | 0.450 | 0.550 | 0.169 | 6.68 | 3.18 | 3.50 | 51 (25/26) | PROJECTED/PROJECTED |
| NYI @ OTT | 2026-10-15T23:00:00Z | T-12h | 0.536 | 0.464 | 0.174 | 6.00 | 3.11 | 2.89 | 51 (25/26) | PROJECTED/PROJECTED |
| SEA @ TBL | 2026-10-15T23:00:00Z | T-12h | 0.614 | 0.386 | 0.172 | 6.06 | 3.38 | 2.68 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ FLA | 2026-10-15T23:00:00Z | T-12h | 0.609 | 0.391 | 0.166 | 6.67 | 3.69 | 2.98 | 51 (25/26) | PROJECTED/PROJECTED |
| NYR @ NJD | 2026-10-15T23:00:00Z | T-12h | 0.491 | 0.508 | 0.186 | 5.94 | 2.95 | 2.99 | 51 (25/26) | PROJECTED/PROJECTED |
| PHI @ DET | 2026-10-15T23:30:00Z | T-12h | 0.600 | 0.400 | 0.176 | 5.77 | 3.19 | 2.58 | 51 (25/26) | CONFIRMED/PROJECTED |
| WPG @ CHI | 2026-10-16T00:00:00Z | T-12h | 0.490 | 0.510 | 0.180 | 5.86 | 2.91 | 2.95 | 51 (25/26) | PROJECTED/PROJECTED |
| SJS @ NSH | 2026-10-16T00:00:00Z | T-12h | 0.534 | 0.466 | 0.172 | 6.38 | 3.30 | 3.08 | 51 (25/26) | PROJECTED/PROJECTED |
| STL @ MIN | 2026-10-16T00:00:00Z | T-12h | 0.528 | 0.472 | 0.178 | 6.04 | 3.11 | 2.93 | 51 (25/26) | PROJECTED/PROJECTED |
| UTA @ EDM | 2026-10-16T01:00:00Z | T-12h | 0.562 | 0.438 | 0.169 | 6.66 | 3.54 | 3.13 | 51 (25/26) | PROJECTED/PROJECTED |
| CGY @ VGK | 2026-10-16T02:00:00Z | T-12h | 0.665 | 0.335 | 0.163 | 6.24 | 3.66 | 2.58 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT15VANFLA-FLA | game_winner | 0.609 | 0.735 | 0.712 | 74 | 27 | no | +0.107 | OK |
| KXNHLGAME-26OCT15VANFLA-VAN | game_winner | 0.391 | 0.265 | 0.288 | 27 | 74 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3 | team_total | 0.574 | 0.435 | 0.463 | 45 | 58 | yes | +0.107 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4 | team_total | 0.354 | 0.230 | 0.252 | 24 | 78 | yes | +0.101 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA3 | game_spread | 0.262 | 0.375 | 0.351 | 38 | 63 | no | +0.091 | OK |
| KXNHLSPREAD-26OCT15VANFLA-FLA2 | game_spread | 0.395 | 0.505 | 0.483 | 51 | 50 | no | +0.087 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5 | team_total | 0.189 | 0.095 | 0.110 | 10 | 91 | yes | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2 | team_total | 0.785 | 0.685 | 0.707 | 69 | 32 | yes | +0.080 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK3 | game_spread | 0.295 | 0.395 | 0.374 | 40 | 61 | no | +0.079 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB4 | team_total | 0.450 | 0.555 | 0.534 | 57 | 46 | no | +0.073 | OK |
| KXNHLGAME-26OCT15SEATB-SEA | game_winner | 0.386 | 0.295 | 0.312 | 30 | 71 | yes | +0.072 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB2 | game_spread | 0.383 | 0.475 | 0.456 | 48 | 53 | no | +0.070 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB5 | team_total | 0.255 | 0.350 | 0.330 | 36 | 66 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-VGK2 | game_spread | 0.443 | 0.535 | 0.517 | 54 | 47 | no | +0.069 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN2 | game_spread | 0.207 | 0.120 | 0.134 | 13 | 89 | yes | +0.069 | OK |
| KXNHLSPREAD-26OCT15SEATB-TB3 | game_spread | 0.246 | 0.335 | 0.316 | 34 | 67 | no | +0.069 | OK |
| KXNHLGAME-26OCT15CGYVGK-VGK | game_winner | 0.665 | 0.745 | 0.730 | 75 | 26 | no | +0.062 | OK |
| KXNHLGAME-26OCT15CGYVGK-CGY | game_winner | 0.335 | 0.255 | 0.270 | 26 | 75 | yes | +0.062 | OK |
| KXNHLGAME-26OCT15SEATB-TB | game_winner | 0.614 | 0.695 | 0.679 | 70 | 31 | no | +0.061 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 | team_total | 0.354 | 0.445 | 0.426 | 46 | 57 | no | +0.059 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ3 | game_spread | 0.160 | 0.235 | 0.218 | 24 | 77 | no | +0.058 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG4 | team_total | 0.351 | 0.435 | 0.418 | 45 | 58 | no | +0.052 | OK |
| KXNHLGAME-26OCT15NYRNJ-NJ | game_winner | 0.491 | 0.565 | 0.550 | 57 | 44 | no | +0.051 | OK |
| KXNHLGAME-26OCT15NYRNJ-NYR | game_winner | 0.508 | 0.435 | 0.450 | 44 | 57 | yes | +0.051 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ3 | team_total | 0.573 | 0.650 | 0.635 | 66 | 36 | no | +0.051 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-5 | game_total | 0.729 | 0.795 | 0.783 | 80 | 21 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG3 | team_total | 0.575 | 0.645 | 0.631 | 65 | 36 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB3 | team_total | 0.668 | 0.740 | 0.726 | 75 | 27 | no | +0.048 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK5 | team_total | 0.307 | 0.380 | 0.365 | 39 | 63 | no | +0.047 | OK |
| KXNHLTOTAL-26OCT15VANFLA-8 | game_total | 0.329 | 0.265 | 0.277 | 27 | 74 | yes | +0.045 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NYR2 | game_spread | 0.286 | 0.225 | 0.236 | 23 | 78 | yes | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ2 | team_total | 0.788 | 0.845 | 0.835 | 85 | 16 | no | +0.043 | OK |
| KXNHLGAME-26OCT15BUFTOR-BUF | game_winner | 0.550 | 0.485 | 0.498 | 49 | 52 | yes | +0.043 | OK |
| KXNHLGAME-26OCT15BUFTOR-TOR | game_winner | 0.450 | 0.515 | 0.502 | 52 | 49 | no | +0.043 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK4 | team_total | 0.511 | 0.590 | 0.574 | 61 | 43 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI3 | team_total | 0.481 | 0.550 | 0.536 | 56 | 46 | no | +0.041 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-7 | game_total | 0.392 | 0.455 | 0.442 | 46 | 55 | no | +0.040 | OK |
| KXNHLSPREAD-26OCT15NYRNJ-NJ2 | game_spread | 0.276 | 0.340 | 0.327 | 35 | 67 | no | +0.039 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-OTT3 | game_spread | 0.190 | 0.245 | 0.233 | 25 | 76 | no | +0.038 | OK |
| KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ5 | team_total | 0.180 | 0.245 | 0.231 | 26 | 77 | no | +0.037 | OK |
| KXNHLGAME-26OCT15NYIOTT-OTT | game_winner | 0.536 | 0.595 | 0.583 | 60 | 41 | no | +0.037 | OK |
| KXNHLGAME-26OCT15NYIOTT-NYI | game_winner | 0.464 | 0.405 | 0.417 | 41 | 60 | yes | +0.037 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-6 | game_total | 0.506 | 0.565 | 0.553 | 57 | 44 | no | +0.037 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG2 | team_total | 0.794 | 0.845 | 0.836 | 85 | 16 | no | +0.036 | OK |
| KXNHLSPREAD-26OCT15SEATB-SEA2 | game_spread | 0.194 | 0.145 | 0.154 | 15 | 86 | yes | +0.035 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB2 | team_total | 0.849 | 0.895 | 0.887 | 90 | 11 | no | +0.034 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-BUF2 | game_spread | 0.338 | 0.280 | 0.291 | 29 | 73 | yes | +0.033 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR3 | game_spread | 0.155 | 0.205 | 0.194 | 21 | 80 | no | +0.033 | OK |
| KXNHLSPREAD-26OCT15VANFLA-VAN3 | game_spread | 0.118 | 0.070 | 0.078 | 8 | 94 | yes | +0.033 | OK |
| KXNHLTOTAL-26OCT15VANFLA-7 | game_total | 0.521 | 0.465 | 0.476 | 47 | 54 | yes | +0.033 | OK |
| KXNHLGAME-26OCT15WPGCHI-WPG | game_winner | 0.510 | 0.565 | 0.554 | 57 | 44 | no | +0.033 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY5 | team_total | 0.128 | 0.085 | 0.092 | 9 | 92 | yes | +0.032 | OK |
| KXNHLSPREAD-26OCT15BUFTOR-TOR2 | game_spread | 0.253 | 0.310 | 0.298 | 32 | 70 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-7 | game_total | 0.401 | 0.455 | 0.444 | 46 | 55 | no | +0.032 | OK |
| KXNHLTOTAL-26OCT15SEATB-7 | game_total | 0.421 | 0.475 | 0.464 | 48 | 53 | no | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3 | team_total | 0.559 | 0.500 | 0.512 | 51 | 51 | yes | +0.032 | OK |
| KXNHLTEAMTOTAL-26OCT15VANFLA-VAN6 | team_total | 0.085 | 0.035 | 0.042 | 5 | 98 | yes | +0.031 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI4 | team_total | 0.275 | 0.330 | 0.318 | 34 | 68 | no | +0.030 | OK |
| KXNHLTOTAL-26OCT15VANFLA-9 | game_total | 0.241 | 0.190 | 0.200 | 20 | 82 | yes | +0.030 | OK |
| KXNHLSPREAD-26OCT15NYIOTT-NYI2 | game_spread | 0.252 | 0.205 | 0.214 | 21 | 80 | yes | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT15WPGCHI-WPG5 | team_total | 0.178 | 0.230 | 0.219 | 24 | 78 | no | +0.030 | OK |
| KXNHLTEAMTOTAL-26OCT15SEATB-TB6 | team_total | 0.121 | 0.170 | 0.159 | 18 | 84 | no | +0.030 | OK |
| KXNHLSPREAD-26OCT15CGYVGK-CGY2 | game_spread | 0.157 | 0.115 | 0.122 | 12 | 89 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT15WPGCHI-WPG3 | game_spread | 0.169 | 0.215 | 0.205 | 22 | 79 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK3 | team_total | 0.718 | 0.775 | 0.764 | 79 | 24 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-4 | game_total | 0.823 | 0.870 | 0.861 | 88 | 14 | no | +0.029 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY3 | team_total | 0.476 | 0.420 | 0.431 | 43 | 59 | yes | +0.029 | OK |
| KXNHLSPREAD-26OCT15STLMIN-MIN2 | game_spread | 0.306 | 0.355 | 0.345 | 36 | 65 | no | +0.028 | OK |
| KXNHLTOTAL-26OCT15NYRNJ-5 | game_total | 0.741 | 0.790 | 0.781 | 80 | 22 | no | +0.027 | OK |
| KXNHLTEAMTOTAL-26OCT15PHIDET-PHI2 | team_total | 0.721 | 0.770 | 0.761 | 78 | 24 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT15CGYVGK-CGY4 | team_total | 0.269 | 0.220 | 0.229 | 23 | 79 | yes | +0.026 | OK |
| KXNHLTOTAL-26OCT15PHIDET-5 | game_total | 0.721 | 0.765 | 0.757 | 77 | 24 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI4 | team_total | 0.341 | 0.285 | 0.296 | 30 | 73 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT15BUFTOR-BUF6 | team_total | 0.143 | 0.100 | 0.108 | 11 | 91 | yes | +0.026 | OK |
| KXNHLSPREAD-26OCT15PHIDET-PHI3 | game_spread | 0.106 | 0.145 | 0.136 | 15 | 86 | no | +0.026 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-9 | game_total | 0.145 | 0.185 | 0.176 | 19 | 82 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT15WPGCHI-8 | game_total | 0.212 | 0.255 | 0.246 | 26 | 75 | no | +0.025 | OK |
| KXNHLTOTAL-26OCT15VANFLA-6 | game_total | 0.632 | 0.585 | 0.595 | 59 | 42 | yes | +0.025 | OK |
| KXNHLGAME-26OCT15STLMIN-STL | game_winner | 0.472 | 0.425 | 0.434 | 43 | 58 | yes | +0.025 | OK |
| KXNHLGAME-26OCT15STLMIN-MIN | game_winner | 0.528 | 0.575 | 0.566 | 58 | 43 | no | +0.025 | OK |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| BUF @ TOR | 0.450 | 0.511 | 0.169 | 0.220 | 6.68 | 6.47 | 0.978/0.997 | KXNHLSPREAD-26OCT15BUFTOR-BUF2 -0.066 |
| NYI @ OTT | 0.536 | 0.576 | 0.174 | 0.219 | 6.00 | 6.12 | 0.998/0.956 | KXNHLTEAMTOTAL-26OCT15NYIOTT-OTT4 +0.047 |
| SEA @ TBL | 0.614 | 0.583 | 0.172 | 0.217 | 6.06 | 6.09 | 0.958/1.005 | KXNHLTEAMTOTAL-26OCT15SEATB-SEA3 +0.036 |
| VAN @ FLA | 0.609 | 0.561 | 0.166 | 0.213 | 6.67 | 6.43 | 0.998/1.026 | KXNHLTEAMTOTAL-26OCT15VANFLA-FLA4 -0.057 |
| NYR @ NJD | 0.491 | 0.516 | 0.186 | 0.218 | 5.94 | 6.05 | 0.987/0.992 | KXNHLTEAMTOTAL-26OCT15NYRNJ-NJ4 +0.032 |
| PHI @ DET | 0.600 | 0.512 | 0.176 | 0.225 | 5.77 | 5.82 | 1.024/0.991 | KXNHLGAME-26OCT15PHIDET-PHI +0.088 |
| WPG @ CHI | 0.490 | 0.480 | 0.180 | 0.219 | 5.86 | 6.20 | 1.003/0.988 | KXNHLTOTAL-26OCT15WPGCHI-7 +0.061 |
| SJS @ NSH | 0.534 | 0.532 | 0.172 | 0.214 | 6.38 | 6.51 | 1.000/1.026 | KXNHLTOTAL-26OCT15SJNSH-7 +0.035 |
| STL @ MIN | 0.528 | 0.549 | 0.178 | 0.216 | 6.04 | 6.40 | 0.995/0.993 | KXNHLTEAMTOTAL-26OCT15STLMIN-MIN4 +0.060 |
| UTA @ EDM | 0.562 | 0.579 | 0.169 | 0.210 | 6.66 | 6.78 | 0.994/0.992 | KXNHLTEAMTOTAL-26OCT15UTAEDM-EDM3 +0.029 |
| CGY @ VGK | 0.665 | 0.662 | 0.163 | 0.205 | 6.24 | 6.17 | 1.003/0.997 | KXNHLTEAMTOTAL-26OCT15CGYVGK-VGK6 -0.014 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 9 recommended · full analysis in card.md / packet.json `thesis_card`

- Seattle wins by over 1.5 goals YES @ 15c · p 0.213 (adj 0.179) · $3.99 · thesis SEA:WINS_BY_2PLUS
- Tampa Bay wins by over 1.5 goals NO @ 53c · p 0.646 (adj 0.5674) · $4.65 · thesis GAME:TIGHT
- Tampa Bay wins by over 2.5 goals NO @ 67c · p 0.7677 (adj 0.7009) · $4.63 · thesis GAME:TIGHT
- Vancouver over 4.5 goals scored YES @ 10c · p 0.1892 (adj 0.1421) · $6.41 · thesis VAN:OFFENSE_4PLUS
- Florida wins by over 1.5 goals NO @ 50c · p 0.6519 (adj 0.5499) · $2.54 · thesis VAN:WINS
- Florida wins by over 2.5 goals NO @ 63c · p 0.7719 (adj 0.6764) · $15.37 · thesis VAN:WINS
- New Jersey wins by over 2.5 goals NO @ 77c · p 0.8223 (adj 0.7936) · $14.36 · thesis NYR:WINS
- Vegas wins by over 1.5 goals NO @ 47c · p 0.5627 (adj 0.5138) · $10.73 · thesis GAME:TIGHT
- Vegas wins by over 2.5 goals NO @ 61c · p 0.6908 (adj 0.6479) · $4.0 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**BUF @ TOR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 30.87, exp saves 26.69 (sd 7.16), pull risk 0.067
- BUF net: Ukko-Pekka Luukkonen (PROJECTED) exp shots 26.02, exp saves 22.45 (sd 6.34), pull risk 0.067

**NYI @ OTT** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- OTT net: Linus Ullmark (PROJECTED) exp shots 25.99, exp saves 22.64 (sd 6.13), pull risk 0.048
- NYI net: Ilya Sorokin (PROJECTED) exp shots 27.57, exp saves 23.53 (sd 6.55), pull risk 0.071

**SEA @ TBL** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- TBL net: Andrei Vasilevskiy (PROJECTED) exp shots 24.41, exp saves 21.31 (sd 5.93), pull risk 0.051
- SEA net: Joey Daccord (PROJECTED) exp shots 30.0, exp saves 25.44 (sd 6.93), pull risk 0.07

**VAN @ FLA** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- FLA net: Akira Schmid (PROJECTED) exp shots 24.7, exp saves 21.6 (sd 6.14), pull risk 0.059
- VAN net: Leevi Merilainen (PROJECTED) exp shots 29.21, exp saves 24.94 (sd 6.85), pull risk 0.078

**NYR @ NJD** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NJD net: Jake Allen (PROJECTED) exp shots 24.13, exp saves 21.0 (sd 5.98), pull risk 0.054
- NYR net: Dylan Garand (PROJECTED) exp shots 29.99, exp saves 25.85 (sd 6.94), pull risk 0.058

**PHI @ DET** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- DET net: Daniil Tarasov (CONFIRMED) exp shots 24.83, exp saves 21.6 (sd 5.99), pull risk 0.051
- PHI net: Joseph Woll (PROJECTED) exp shots 29.07, exp saves 25.27 (sd 6.73), pull risk 0.054

**WPG @ CHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CHI net: Spencer Knight (PROJECTED) exp shots 27.63, exp saves 23.91 (sd 6.64), pull risk 0.066
- WPG net: Stuart Skinner (PROJECTED) exp shots 25.12, exp saves 21.77 (sd 6.05), pull risk 0.056

**SJS @ NSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NSH net: Juuse Saros (PROJECTED) exp shots 27.54, exp saves 23.93 (sd 6.63), pull risk 0.063
- SJS net: Alex Nedeljkovic (PROJECTED) exp shots 27.64, exp saves 23.66 (sd 6.68), pull risk 0.077

**STL @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (PROJECTED) exp shots 26.75, exp saves 23.2 (sd 6.39), pull risk 0.059
- STL net: Joel Hofer (PROJECTED) exp shots 28.41, exp saves 24.37 (sd 6.81), pull risk 0.072

**UTA @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Devon Levi (PROJECTED) exp shots 27.2, exp saves 23.68 (sd 6.47), pull risk 0.059
- UTA net: Karel Vejmelka (PROJECTED) exp shots 27.99, exp saves 23.74 (sd 6.78), pull risk 0.088

**CGY @ VGK** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- VGK net: Carter Hart (PROJECTED) exp shots 26.2, exp saves 23.23 (sd 6.23), pull risk 0.04
- CGY net: Dustin Wolf (PROJECTED) exp shots 30.19, exp saves 25.41 (sd 7.14), pull risk 0.088

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
