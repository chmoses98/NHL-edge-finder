# NHL slate 2026-10-18 — RESEARCH_ONLY

generated 2026-10-18T07:34:02Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 2 · simulated (not started): 2 · markets on board: 2098 · contracts joined: 102 (unjoined to any game: 1571)
gates: {'UNSUPPORTED': 52, 'OK': 22, 'NO_EDGE': 28}
families: {'period_winner': 18, 'period_spread': 12, 'period_total': 18, 'game_early_goal': 2, 'game_winner': 4, 'game_overtime': 2, 'game_spread': 8, 'team_total': 20, 'game_total': 18}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ MIN | 2026-10-18T22:00:00Z | T-12h | 0.577 | 0.423 | 0.181 | 5.88 | 3.18 | 2.70 | 51 (25/26) | CONFIRMED/PROJECTED |
| CAR @ CGY | 2026-10-19T00:00:00Z | T-12h | 0.351 | 0.649 | 0.169 | 6.19 | 2.62 | 3.57 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN4 | team_total | 0.405 | 0.495 | 0.477 | 50 | 51 | no | +0.067 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN5 | team_total | 0.216 | 0.300 | 0.282 | 31 | 71 | no | +0.059 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-7 | game_total | 0.396 | 0.475 | 0.459 | 48 | 53 | no | +0.057 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-6 | game_total | 0.508 | 0.590 | 0.574 | 60 | 42 | no | +0.055 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-MIN3 | game_spread | 0.214 | 0.285 | 0.270 | 29 | 72 | no | +0.052 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-5 | game_total | 0.729 | 0.800 | 0.787 | 81 | 21 | no | +0.049 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN3 | team_total | 0.626 | 0.705 | 0.690 | 72 | 31 | no | +0.049 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-4 | game_total | 0.822 | 0.875 | 0.866 | 88 | 13 | no | +0.040 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-8 | game_total | 0.219 | 0.275 | 0.263 | 28 | 73 | no | +0.037 | OK |
| KXNHLGAME-26OCT18CBJMIN-CBJ | game_winner | 0.423 | 0.365 | 0.376 | 37 | 64 | yes | +0.037 | OK |
| KXNHLGAME-26OCT18CBJMIN-MIN | game_winner | 0.577 | 0.635 | 0.624 | 64 | 37 | no | +0.037 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-MIN2 | game_spread | 0.347 | 0.405 | 0.393 | 41 | 60 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN6 | team_total | 0.098 | 0.145 | 0.134 | 15 | 86 | no | +0.034 | OK |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-MIN2 | team_total | 0.825 | 0.870 | 0.862 | 88 | 14 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-9 | game_total | 0.150 | 0.195 | 0.185 | 21 | 82 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-10 | game_total | 0.066 | 0.100 | 0.092 | 11 | 91 | no | +0.018 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-CBJ2 | game_spread | 0.215 | 0.185 | 0.191 | 19 | 82 | yes | +0.014 | OK |
| KXNHLTOTAL-26OCT18CARCGY-4 | game_total | 0.853 | 0.875 | 0.871 | 88 | 13 | no | +0.009 | OK |
| KXNHLTOTAL-26OCT18CBJMIN-3 | game_total | 0.950 | 0.970 | 0.967 | 98 | 4 | no | +0.008 | OK |
| KXNHLSPREAD-26OCT18CARCGY-CAR3 | game_spread | 0.283 | 0.310 | 0.304 | 32 | 70 | no | +0.003 | OK |
| KXNHLTOTAL-26OCT18CARCGY-2 | game_total | 0.984 | 0.975 | 0.977 | 98 | 3 | yes | +0.002 | OK |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY6 | team_total | 0.053 | 0.045 | 0.047 | 5 | 96 | yes | +0.000 | OK |
| KXNHLSPREAD-26OCT18CBJMIN-CBJ3 | game_spread | 0.116 | 0.100 | 0.103 | 11 | 91 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-5 | game_total | 0.769 | 0.790 | 0.786 | 80 | 22 |  | -0.002 | NO_EDGE |
| KXNHLGAME-26OCT18CARCGY-CAR | game_winner | 0.649 | 0.665 | 0.662 | 67 | 34 |  | -0.005 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ2 | team_total | 0.742 | 0.760 | 0.756 | 77 | 25 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-3 | game_total | 0.963 | 0.970 | 0.969 | 98 | 4 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT18CARCGY-CGY3 | game_spread | 0.090 | 0.095 | 0.094 | 10 | 91 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR4 | team_total | 0.489 | 0.510 | 0.506 | 52 | 50 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR3 | team_total | 0.703 | 0.720 | 0.717 | 73 | 29 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ6 | team_total | 0.055 | 0.055 | 0.055 | 6 | 95 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT18CARCGY-CAR2 | game_spread | 0.421 | 0.435 | 0.432 | 44 | 57 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR2 | team_total | 0.871 | 0.875 | 0.874 | 88 | 13 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT18CARCGY-CGY2 | game_spread | 0.170 | 0.165 | 0.166 | 17 | 84 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-7 | game_total | 0.443 | 0.460 | 0.457 | 47 | 55 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT18CBJMIN-2 | game_total | 0.979 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY2 | team_total | 0.727 | 0.740 | 0.737 | 75 | 27 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR6 | team_total | 0.147 | 0.140 | 0.141 | 15 | 87 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-10 | game_total | 0.087 | 0.095 | 0.093 | 11 | 92 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ4 | team_total | 0.299 | 0.310 | 0.308 | 32 | 70 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ5 | team_total | 0.145 | 0.145 | 0.145 | 15 | 86 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-6 | game_total | 0.556 | 0.570 | 0.567 | 58 | 44 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-9 | game_total | 0.184 | 0.185 | 0.185 | 19 | 82 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT18CARCGY-CGY | game_winner | 0.351 | 0.345 | 0.346 | 35 | 66 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY5 | team_total | 0.132 | 0.130 | 0.130 | 14 | 88 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CAR5 | team_total | 0.294 | 0.305 | 0.303 | 32 | 71 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ3 | team_total | 0.513 | 0.525 | 0.523 | 54 | 49 |  | -0.021 | NO_EDGE |
| KXNHLTOTAL-26OCT18CARCGY-8 | game_total | 0.263 | 0.260 | 0.261 | 27 | 75 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY4 | team_total | 0.278 | 0.285 | 0.284 | 30 | 73 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3 | team_total | 0.487 | 0.495 | 0.493 | 51 | 52 |  | -0.024 | NO_EDGE |
| KXNHL1P-26OCT18CBJMIN-CBJ | period_winner |  | 0.270 |  | 30 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CBJMIN-MIN | period_winner |  | 0.375 |  | 40 | 65 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CBJMIN-TIE | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CBJMIN-CBJ2 | period_spread |  | 0.115 |  | 17 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CBJMIN-MIN2 | period_spread |  | 0.170 |  | 21 | 87 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CBJMIN-1 | period_total |  | 0.835 |  | 86 | 19 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CBJMIN-2 | period_total |  | 0.530 |  | 55 | 49 |  |  | UNSUPPORTED |
| KXNHL1PTOTAL-26OCT18CBJMIN-3 | period_total |  | 0.285 |  | 30 | 73 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CBJMIN-CBJ | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CBJMIN-MIN | period_winner |  | 0.400 |  | 43 | 63 |  |  | UNSUPPORTED |
| KXNHL2P-26OCT18CBJMIN-TIE | period_winner |  | 0.285 |  | 31 | 74 |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT18CBJMIN-CBJ2 | period_spread |  |  |  | 22 |  |  |  | UNSUPPORTED |
| KXNHL2PSPREAD-26OCT18CBJMIN-MIN2 | period_spread |  | 0.175 |  | 29 | 94 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CBJMIN-1 | period_total |  | 0.875 |  | 98 | 23 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CBJMIN-2 | period_total |  | 0.610 |  | 63 | 41 |  |  | UNSUPPORTED |
| KXNHL2PTOTAL-26OCT18CBJMIN-3 | period_total |  | 0.335 |  | 41 | 74 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CBJMIN-CBJ | period_winner |  | 0.295 |  | 32 | 73 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CBJMIN-MIN | period_winner |  | 0.425 |  | 45 | 60 |  |  | UNSUPPORTED |
| KXNHL3P-26OCT18CBJMIN-TIE | period_winner |  | 0.255 |  | 28 | 77 |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT18CBJMIN-CBJ2 | period_spread |  |  |  | 23 |  |  |  | UNSUPPORTED |
| KXNHL3PSPREAD-26OCT18CBJMIN-MIN2 | period_spread |  | 0.220 |  | 34 | 90 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CBJMIN-1 | period_total |  | 0.895 |  | 99 | 20 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CBJMIN-2 | period_total |  | 0.655 |  | 73 | 42 |  |  | UNSUPPORTED |
| KXNHL3PTOTAL-26OCT18CBJMIN-3 | period_total |  | 0.420 |  | 47 | 63 |  |  | UNSUPPORTED |
| KXNHLF10G-26OCT18CBJMIN-Y | game_early_goal |  | 0.585 |  | 60 | 43 |  |  | UNSUPPORTED |
| KXNHLOT-26OCT18CBJMIN-1 | game_overtime |  | 0.205 |  | 21 | 80 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CARCGY-CAR | period_winner |  | 0.375 |  | 39 | 64 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CARCGY-CGY | period_winner |  | 0.265 |  | 29 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT18CARCGY-TIE | period_winner |  | 0.325 |  | 35 | 70 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT18CARCGY-CAR2 | period_spread |  | 0.145 |  | 24 | 95 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| CBJ @ MIN | 0.577 | 0.556 | 0.181 | 0.220 | 5.88 | 6.18 | 0.991/0.965 | KXNHLTEAMTOTAL-26OCT18CBJMIN-CBJ3 +0.058 |
| CAR @ CGY | 0.351 | 0.422 | 0.169 | 0.214 | 6.19 | 6.32 | 0.998/0.997 | KXNHLTEAMTOTAL-26OCT18CARCGY-CGY3 +0.077 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 3 recommended · full analysis in card.md / packet.json `thesis_card`

- Minnesota wins by over 2.5 goals NO @ 72c · p 0.7847 (adj 0.7498) · $16.26 · thesis CBJ:WINS
- Carolina wins by over 1.5 goals NO @ 57c · p 0.6394 (adj 0.6022) · $7.17 · thesis GAME:TIGHT
- Carolina wins by over 2.5 goals NO @ 70c · p 0.7632 (adj 0.7266) · $4.13 · thesis GAME:TIGHT

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**CBJ @ MIN** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- MIN net: Jesper Wallstedt (CONFIRMED) exp shots 28.71, exp saves 25.05 (sd 6.65), pull risk 0.052
- CBJ net: Jet Greaves (PROJECTED) exp shots 28.7, exp saves 24.54 (sd 6.77), pull risk 0.069

**CAR @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Dustin Wolf (PROJECTED) exp shots 31.92, exp saves 27.19 (sd 7.33), pull risk 0.076
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 24.78, exp saves 21.77 (sd 6.04), pull risk 0.051

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
