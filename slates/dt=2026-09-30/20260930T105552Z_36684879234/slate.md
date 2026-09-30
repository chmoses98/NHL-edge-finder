# NHL slate 2026-09-30 — RESEARCH_ONLY

generated 2026-09-30T10:55:52Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2182 · contracts joined: 153 (unjoined to any game: 1484)
gates: {'UNSUPPORTED': 78, 'NO_EDGE': 43, 'OK': 32}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 2026-09-30T23:30:00Z | T-12h | 0.565 | 0.435 | 0.178 | 6.18 | 3.30 | 2.87 | 51 (25/26) | PROJECTED/PROJECTED |
| NYI @ TOR | 2026-09-30T23:30:00Z | T-12h | 0.467 | 0.533 | 0.176 | 6.26 | 3.02 | 3.24 | 51 (25/26) | PROJECTED/PROBABLE |
| LAK @ COL | 2026-10-01T02:00:00Z | T-12h | 0.646 | 0.354 | 0.172 | 5.80 | 3.35 | 2.45 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLTOTAL-26SEP30LACOL-6 | game_total | 0.494 | 0.585 | 0.567 | 59 | 42 | no | +0.069 | OK |
| KXNHLTOTAL-26SEP30LACOL-7 | game_total | 0.381 | 0.465 | 0.448 | 47 | 54 | no | +0.062 | OK |
| KXNHLTOTAL-26SEP30LACOL-5 | game_total | 0.721 | 0.790 | 0.777 | 80 | 22 | no | +0.047 | OK |
| KXNHLGAME-26SEP30NYITOR-NYI | game_winner | 0.533 | 0.465 | 0.479 | 47 | 54 | yes | +0.046 | OK |
| KXNHLGAME-26SEP30NYITOR-TOR | game_winner | 0.467 | 0.535 | 0.521 | 54 | 47 | no | +0.046 | OK |
| KXNHLTOTAL-26SEP30LACOL-4 | game_total | 0.818 | 0.880 | 0.869 | 89 | 13 | no | +0.044 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR3 | game_spread | 0.145 | 0.205 | 0.192 | 21 | 80 | no | +0.043 | OK |
| KXNHLTOTAL-26SEP30LACOL-8 | game_total | 0.205 | 0.265 | 0.252 | 27 | 74 | no | +0.042 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA4 | team_total | 0.240 | 0.305 | 0.291 | 32 | 71 | no | +0.036 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA3 | team_total | 0.451 | 0.520 | 0.506 | 54 | 50 | no | +0.032 | OK |
| KXNHLSPREAD-26SEP30NYITOR-TOR2 | game_spread | 0.254 | 0.310 | 0.298 | 32 | 70 | no | +0.031 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI2 | game_spread | 0.312 | 0.265 | 0.274 | 27 | 74 | yes | +0.029 | OK |
| KXNHLTOTAL-26SEP30LACOL-9 | game_total | 0.136 | 0.175 | 0.167 | 18 | 83 | no | +0.024 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI3 | team_total | 0.638 | 0.585 | 0.596 | 60 | 43 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI2 | team_total | 0.832 | 0.790 | 0.799 | 80 | 22 | yes | +0.021 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA2 | team_total | 0.697 | 0.745 | 0.736 | 76 | 27 | no | +0.019 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA5 | team_total | 0.104 | 0.145 | 0.136 | 16 | 87 | no | +0.018 | OK |
| KXNHLTOTAL-26SEP30NYITOR-9 | game_total | 0.192 | 0.165 | 0.170 | 17 | 84 | yes | +0.012 | OK |
| KXNHLSPREAD-26SEP30LACOL-LA3 | game_spread | 0.083 | 0.110 | 0.104 | 12 | 90 | no | +0.011 | OK |
| KXNHLSPREAD-26SEP30NYITOR-NYI3 | game_spread | 0.191 | 0.165 | 0.170 | 17 | 84 | yes | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL4 | team_total | 0.442 | 0.490 | 0.480 | 51 | 53 | no | +0.011 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 | team_total | 0.416 | 0.375 | 0.383 | 39 | 64 | yes | +0.010 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL5 | team_total | 0.247 | 0.290 | 0.281 | 31 | 73 | no | +0.009 | OK |
| KXNHLTOTAL-26SEP30NYITOR-8 | game_total | 0.271 | 0.245 | 0.250 | 25 | 76 | yes | +0.008 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR3 | team_total | 0.586 | 0.625 | 0.617 | 64 | 39 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI5 | team_total | 0.228 | 0.190 | 0.197 | 21 | 83 | yes | +0.007 | OK |
| KXNHLTOTAL-26SEP30LACOL-3 | game_total | 0.951 | 0.965 | 0.963 | 97 | 4 | no | +0.006 | OK |
| KXNHLTOTAL-26SEP30LACOL-10 | game_total | 0.060 | 0.080 | 0.076 | 9 | 93 | no | +0.005 | OK |
| KXNHLSPREAD-26SEP30PITPHI-PIT3 | game_spread | 0.130 | 0.145 | 0.142 | 15 | 86 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR2 | team_total | 0.797 | 0.820 | 0.816 | 83 | 19 | no | +0.002 | OK |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5 | team_total | 0.197 | 0.225 | 0.219 | 24 | 79 | no | +0.002 | OK |
| KXNHLSPREAD-26SEP30LACOL-COL3 | game_spread | 0.265 | 0.285 | 0.281 | 29 | 72 | no | +0.001 | OK |
| KXNHLTEAMTOTAL-26SEP30LACOL-LA6 | team_total | 0.037 | 0.055 | 0.051 | 7 | 96 |  | -0.000 | NO_EDGE |
| KXNHLTOTAL-26SEP30LACOL-2 | game_total | 0.979 | 0.985 | 0.984 | 99 | 2 |  | -0.000 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR6 | team_total | 0.085 | 0.100 | 0.097 | 11 | 91 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30NYITOR-NYI6 | team_total | 0.104 | 0.085 | 0.089 | 10 | 93 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4 | team_total | 0.365 | 0.405 | 0.397 | 43 | 62 |  | -0.002 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-4 | game_total | 0.854 | 0.870 | 0.867 | 88 | 14 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL6 | team_total | 0.116 | 0.140 | 0.135 | 16 | 88 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-3 | game_total | 0.963 | 0.965 | 0.965 | 97 | 4 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-7 | game_total | 0.462 | 0.445 | 0.448 | 45 | 56 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-4 | game_total | 0.858 | 0.870 | 0.868 | 88 | 14 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-10 | game_total | 0.089 | 0.075 | 0.078 | 9 | 94 |  | -0.007 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-LA2 | game_spread | 0.167 | 0.175 | 0.173 | 18 | 83 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL2 | team_total | 0.849 | 0.855 | 0.854 | 86 | 15 |  | -0.007 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-3 | game_total | 0.963 | 0.960 | 0.961 | 97 | 5 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT5 | team_total | 0.169 | 0.185 | 0.182 | 20 | 83 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30LACOL-COL3 | team_total | 0.663 | 0.685 | 0.681 | 70 | 33 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PIT2 | game_spread | 0.227 | 0.235 | 0.233 | 24 | 77 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 | team_total | 0.334 | 0.360 | 0.355 | 38 | 66 |  | -0.009 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI2 | team_total | 0.840 | 0.830 | 0.832 | 84 | 18 |  | -0.009 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-LA | game_winner | 0.354 | 0.365 | 0.363 | 37 | 64 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-9 | game_total | 0.178 | 0.175 | 0.176 | 18 | 83 |  | -0.013 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI3 | game_spread | 0.212 | 0.215 | 0.214 | 22 | 79 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-5 | game_total | 0.771 | 0.780 | 0.778 | 79 | 23 |  | -0.013 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-10 | game_total | 0.079 | 0.080 | 0.080 | 9 | 93 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26SEP30PITPHI-PHI2 | game_spread | 0.342 | 0.335 | 0.336 | 34 | 67 |  | -0.014 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT6 | team_total | 0.070 | 0.075 | 0.074 | 9 | 94 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-6 | game_total | 0.571 | 0.565 | 0.566 | 57 | 44 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-6 | game_total | 0.559 | 0.565 | 0.564 | 57 | 44 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI6 | team_total | 0.111 | 0.105 | 0.106 | 12 | 91 |  | -0.016 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-8 | game_total | 0.254 | 0.255 | 0.255 | 26 | 75 |  | -0.017 | NO_EDGE |
| KXNHLSPREAD-26SEP30LACOL-COL2 | game_spread | 0.409 | 0.405 | 0.406 | 41 | 60 |  | -0.018 | NO_EDGE |
| KXNHLTOTAL-26SEP30NYITOR-5 | game_total | 0.777 | 0.780 | 0.779 | 79 | 23 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT2 | team_total | 0.777 | 0.785 | 0.783 | 80 | 23 |  | -0.020 | NO_EDGE |
| KXNHLGAME-26SEP30LACOL-COL | game_winner | 0.646 | 0.645 | 0.645 | 65 | 36 |  | -0.020 | NO_EDGE |
| KXNHLTOTAL-26SEP30PITPHI-7 | game_total | 0.447 | 0.445 | 0.445 | 45 | 56 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI5 | team_total | 0.243 | 0.235 | 0.236 | 25 | 78 |  | -0.021 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PIT3 | team_total | 0.554 | 0.565 | 0.563 | 58 | 45 |  | -0.021 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PHI | game_winner | 0.565 | 0.565 | 0.565 | 57 | 44 |  | -0.022 | NO_EDGE |
| KXNHLGAME-26SEP30PITPHI-PIT | game_winner | 0.435 | 0.435 | 0.435 | 44 | 57 |  | -0.022 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI3 | team_total | 0.648 | 0.635 | 0.638 | 66 | 39 |  | -0.028 | NO_EDGE |
| KXNHLTEAMTOTAL-26SEP30PITPHI-PHI4 | team_total | 0.432 | 0.435 | 0.434 | 45 | 58 |  | -0.029 | NO_EDGE |
| KXNHL1P-26SEP30PITPHI-PHI | period_winner |  | 0.355 |  | 41 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-PIT | period_winner |  | 0.305 |  | 36 | 75 |  |  | UNSUPPORTED |
| KXNHL1P-26SEP30PITPHI-TIE | period_winner |  | 0.345 |  | 40 | 71 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PHI2 | period_spread |  | 0.120 |  | 23 | 99 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26SEP30PITPHI-PIT2 | period_spread |  |  |  | 22 |  |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| PIT @ PHI | 0.565 | 0.542 | 0.178 | 0.215 | 6.18 | 6.24 | 0.993/1.033 | KXNHLTEAMTOTAL-26SEP30PITPHI-PIT4 +0.032 |
| NYI @ TOR | 0.467 | 0.502 | 0.176 | 0.222 | 6.26 | 6.10 | 0.978/0.951 | KXNHLTEAMTOTAL-26SEP30NYITOR-NYI4 -0.044 |
| LAK @ COL | 0.646 | 0.593 | 0.172 | 0.220 | 5.80 | 5.95 | 0.973/0.992 | KXNHLTEAMTOTAL-26SEP30LACOL-LA3 +0.057 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**PIT @ PHI** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- PHI net: Dan Vladar (PROJECTED) exp shots 26.45, exp saves 23.1 (sd 6.33), pull risk 0.055
- PIT net: Arturs Silovs (PROJECTED) exp shots 25.68, exp saves 22.06 (sd 6.24), pull risk 0.071

**NYI @ TOR** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.12, exp saves 26.91 (sd 7.08), pull risk 0.059
- NYI net: Ilya Sorokin (PROBABLE) exp shots 25.96, exp saves 22.54 (sd 6.28), pull risk 0.058

**LAK @ COL** · priced 0/0 player contracts · lineups RECENT_SHIFTS/RECENT_SHIFTS
- COL net: Scott Wedgewood (PROJECTED) exp shots 25.97, exp saves 22.82 (sd 6.17), pull risk 0.045
- LAK net: Darcy Kuemper (PROJECTED) exp shots 31.35, exp saves 26.86 (sd 7.23), pull risk 0.067

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
