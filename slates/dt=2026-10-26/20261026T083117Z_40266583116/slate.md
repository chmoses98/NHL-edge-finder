# NHL slate 2026-10-26 — RESEARCH_ONLY

generated 2026-10-26T08:31:17Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2370 · contracts joined: 153 (unjoined to any game: 1538)
gates: {'UNSUPPORTED': 78, 'OK': 42, 'NO_EDGE': 33}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 2026-10-26T23:00:00Z | T-12h | 0.611 | 0.389 | 0.177 | 5.99 | 3.34 | 2.65 | 51 (25/26) | PROJECTED/PROJECTED |
| TOR @ CGY | 2026-10-27T00:30:00Z | T-12h | 0.533 | 0.467 | 0.174 | 6.41 | 3.31 | 3.10 | 51 (25/26) | PROJECTED/PROJECTED |
| DET @ EDM | 2026-10-27T01:30:00Z | T-12h | 0.609 | 0.391 | 0.169 | 6.44 | 3.57 | 2.88 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLGAME-26OCT26TORCGY-CGY | game_winner | 0.533 | 0.415 | 0.438 | 42 | 59 | yes | +0.096 | OK |
| KXNHLGAME-26OCT26TORCGY-TOR | game_winner | 0.467 | 0.585 | 0.562 | 59 | 42 | no | +0.096 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR2 | game_spread | 0.263 | 0.375 | 0.351 | 38 | 63 | no | +0.090 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR4 | team_total | 0.384 | 0.505 | 0.480 | 52 | 51 | no | +0.088 | OK |
| KXNHLSPREAD-26OCT26TORCGY-TOR3 | game_spread | 0.155 | 0.255 | 0.232 | 26 | 75 | no | +0.082 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR3 | team_total | 0.599 | 0.705 | 0.685 | 72 | 31 | no | +0.076 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY2 | game_spread | 0.319 | 0.235 | 0.250 | 24 | 77 | yes | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR5 | team_total | 0.210 | 0.305 | 0.284 | 32 | 71 | no | +0.066 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR2 | team_total | 0.808 | 0.870 | 0.859 | 88 | 14 | no | +0.043 | OK |
| KXNHLSPREAD-26OCT26TORCGY-CGY3 | game_spread | 0.198 | 0.145 | 0.155 | 15 | 86 | yes | +0.039 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA3 | game_spread | 0.104 | 0.145 | 0.136 | 15 | 86 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM4 | team_total | 0.495 | 0.550 | 0.539 | 56 | 46 | no | +0.028 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA3 | team_total | 0.496 | 0.555 | 0.543 | 57 | 46 | no | +0.027 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR2 | game_spread | 0.382 | 0.330 | 0.340 | 34 | 68 | yes | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-TOR6 | team_total | 0.096 | 0.145 | 0.134 | 16 | 87 | no | +0.026 | OK |
| KXNHLSPREAD-26OCT26LANYR-LA2 | game_spread | 0.194 | 0.235 | 0.226 | 24 | 77 | no | +0.024 | OK |
| KXNHLGAME-26OCT26LANYR-LA | game_winner | 0.389 | 0.440 | 0.430 | 45 | 57 | no | +0.024 | OK |
| KXNHLGAME-26OCT26LANYR-NYR | game_winner | 0.611 | 0.565 | 0.574 | 57 | 44 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA2 | team_total | 0.735 | 0.785 | 0.776 | 80 | 23 | no | +0.023 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA4 | team_total | 0.282 | 0.330 | 0.320 | 34 | 68 | no | +0.022 | OK |
| KXNHLTOTAL-26OCT26TORCGY-4 | game_total | 0.872 | 0.905 | 0.899 | 91 | 10 | no | +0.021 | OK |
| KXNHLTOTAL-26OCT26TORCGY-7 | game_total | 0.484 | 0.525 | 0.517 | 53 | 48 | no | +0.018 | OK |
| KXNHLTOTAL-26OCT26TORCGY-6 | game_total | 0.597 | 0.640 | 0.632 | 65 | 37 | no | +0.017 | OK |
| KXNHLSPREAD-26OCT26DETEDM-EDM3 | game_spread | 0.250 | 0.285 | 0.278 | 29 | 72 | no | +0.016 | OK |
| KXNHLTOTAL-26OCT26TORCGY-8 | game_total | 0.290 | 0.330 | 0.322 | 34 | 68 | no | +0.015 | OK |
| KXNHLTOTAL-26OCT26DETEDM-5 | game_total | 0.796 | 0.825 | 0.819 | 83 | 18 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM5 | team_total | 0.291 | 0.335 | 0.326 | 35 | 68 | no | +0.014 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY3 | team_total | 0.650 | 0.605 | 0.614 | 62 | 41 | yes | +0.013 | OK |
| KXNHLTOTAL-26OCT26TORCGY-5 | game_total | 0.797 | 0.825 | 0.820 | 83 | 18 | no | +0.012 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY4 | team_total | 0.439 | 0.395 | 0.404 | 41 | 62 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT26DETEDM-7 | game_total | 0.492 | 0.525 | 0.518 | 53 | 48 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT26DETEDM-4 | game_total | 0.873 | 0.900 | 0.895 | 91 | 11 | no | +0.010 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM2 | team_total | 0.866 | 0.895 | 0.890 | 91 | 12 | no | +0.007 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA5 | team_total | 0.135 | 0.165 | 0.159 | 18 | 85 | no | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR2 | team_total | 0.845 | 0.825 | 0.829 | 83 | 18 | yes | +0.006 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM6 | team_total | 0.146 | 0.170 | 0.165 | 18 | 84 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT26DETEDM-EDM3 | team_total | 0.702 | 0.735 | 0.729 | 75 | 28 | no | +0.004 | OK |
| KXNHLTOTAL-26OCT26TORCGY-10 | game_total | 0.099 | 0.120 | 0.116 | 13 | 89 | no | +0.004 | OK |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY5 | team_total | 0.246 | 0.215 | 0.221 | 23 | 80 | yes | +0.004 | OK |
| KXNHLTOTAL-26OCT26TORCGY-9 | game_total | 0.205 | 0.225 | 0.221 | 23 | 78 | no | +0.003 | OK |
| KXNHLSPREAD-26OCT26LANYR-NYR3 | game_spread | 0.244 | 0.220 | 0.225 | 23 | 79 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT26DETEDM-6 | game_total | 0.603 | 0.630 | 0.625 | 64 | 38 | no | +0.001 | OK |
| KXNHLTOTAL-26OCT26TORCGY-3 | game_total | 0.969 | 0.975 | 0.974 | 98 | 3 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR4 | team_total | 0.444 | 0.415 | 0.421 | 43 | 60 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-9 | game_total | 0.211 | 0.225 | 0.222 | 23 | 78 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY2 | team_total | 0.836 | 0.810 | 0.816 | 83 | 21 |  | -0.003 | NO_EDGE |
| KXNHLTOTAL-26OCT26TORCGY-2 | game_total | 0.987 | 0.985 | 0.985 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26TORCGY-CGY6 | team_total | 0.113 | 0.095 | 0.098 | 11 | 92 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-2 | game_total | 0.982 | 0.985 | 0.984 | 99 | 2 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-8 | game_total | 0.299 | 0.320 | 0.316 | 33 | 69 |  | -0.004 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-2 | game_total | 0.986 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-9 | game_total | 0.156 | 0.165 | 0.163 | 17 | 84 |  | -0.005 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-EDM2 | game_spread | 0.389 | 0.405 | 0.402 | 41 | 60 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-10 | game_total | 0.069 | 0.065 | 0.066 | 7 | 94 |  | -0.006 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-4 | game_total | 0.836 | 0.845 | 0.843 | 85 | 16 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR3 | team_total | 0.660 | 0.635 | 0.640 | 65 | 38 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR5 | team_total | 0.246 | 0.225 | 0.229 | 24 | 79 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET2 | team_total | 0.775 | 0.790 | 0.787 | 80 | 22 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-LA6 | team_total | 0.054 | 0.065 | 0.063 | 8 | 95 |  | -0.007 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET3 | team_total | 0.551 | 0.570 | 0.566 | 58 | 44 |  | -0.008 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET2 | game_spread | 0.203 | 0.195 | 0.197 | 20 | 81 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-10 | game_total | 0.103 | 0.115 | 0.112 | 13 | 90 |  | -0.009 | NO_EDGE |
| KXNHLSPREAD-26OCT26DETEDM-DET3 | game_spread | 0.112 | 0.115 | 0.114 | 12 | 89 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-5 | game_total | 0.746 | 0.755 | 0.753 | 76 | 25 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-7 | game_total | 0.413 | 0.425 | 0.423 | 43 | 58 |  | -0.010 | NO_EDGE |
| KXNHLTOTAL-26OCT26DETEDM-3 | game_total | 0.968 | 0.970 | 0.970 | 98 | 4 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-3 | game_total | 0.958 | 0.960 | 0.960 | 97 | 5 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-8 | game_total | 0.229 | 0.235 | 0.234 | 24 | 77 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET5 | team_total | 0.173 | 0.180 | 0.179 | 19 | 83 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26LANYR-NYR6 | team_total | 0.113 | 0.105 | 0.107 | 12 | 91 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT26LANYR-6 | game_total | 0.527 | 0.535 | 0.533 | 54 | 47 |  | -0.014 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-DET | game_winner | 0.391 | 0.385 | 0.386 | 39 | 62 |  | -0.015 | NO_EDGE |
| KXNHLGAME-26OCT26DETEDM-EDM | game_winner | 0.609 | 0.615 | 0.614 | 62 | 39 |  | -0.015 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET6 | team_total | 0.072 | 0.075 | 0.074 | 9 | 94 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT26DETEDM-DET4 | team_total | 0.332 | 0.345 | 0.342 | 36 | 67 |  | -0.018 | NO_EDGE |
| KXNHL1P-26OCT26LANYR-LA | period_winner |  | 0.295 |  | 31 | 72 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-NYR | period_winner |  | 0.335 |  | 35 | 68 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT26LANYR-TIE | period_winner |  | 0.330 |  | 35 | 69 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-LA2 | period_spread |  | 0.120 |  | 17 | 93 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT26LANYR-NYR2 | period_spread |  | 0.140 |  | 17 | 89 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| LAK @ NYR | 0.611 | 0.555 | 0.177 | 0.216 | 5.99 | 6.02 | 0.992/0.992 | KXNHLGAME-26OCT26LANYR-LA +0.056 |
| TOR @ CGY | 0.533 | 0.500 | 0.174 | 0.216 | 6.41 | 6.41 | 0.986/0.978 | KXNHLSPREAD-26OCT26TORCGY-CGY2 -0.034 |
| DET @ EDM | 0.609 | 0.646 | 0.169 | 0.199 | 6.44 | 6.61 | 1.009/1.002 | KXNHLSPREAD-26OCT26DETEDM-EDM3 +0.057 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 2 recommended · full analysis in card.md / packet.json `thesis_card`

- Toronto wins by over 1.5 goals NO @ 63c · p 0.7153 (adj 0.6702) · $10.94 · thesis CGY:WINS
- Toronto wins by over 2.5 goals NO @ 75c · p 0.8216 (adj 0.7833) · $13.04 · thesis CGY:WINS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**LAK @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 28.09, exp saves 24.53 (sd 6.68), pull risk 0.054
- LAK net: Darcy Kuemper (PROJECTED) exp shots 26.31, exp saves 22.6 (sd 6.31), pull risk 0.06

**TOR @ CGY** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- CGY net: Devin Cooley (PROJECTED) exp shots 28.89, exp saves 24.82 (sd 6.78), pull risk 0.065
- TOR net: Sergei Bobrovsky (PROJECTED) exp shots 31.56, exp saves 27.28 (sd 7.37), pull risk 0.071

**DET @ EDM** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- EDM net: Tristan Jarry (PROJECTED) exp shots 27.49, exp saves 24.16 (sd 6.56), pull risk 0.053
- DET net: John Gibson (PROJECTED) exp shots 28.12, exp saves 23.68 (sd 6.75), pull risk 0.09

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
