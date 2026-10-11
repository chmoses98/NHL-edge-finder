# NHL slate 2026-10-11 — RESEARCH_ONLY

generated 2026-10-11T07:24:51Z · model DATA_ONLY_V1 · sim nhl-sim-1.1 · 20000 sims/game

games on date: 3 · simulated (not started): 3 · markets on board: 2173 · contracts joined: 153 (unjoined to any game: 1569)
gates: {'UNSUPPORTED': 78, 'OK': 39, 'NO_EDGE': 36}
families: {'period_winner': 27, 'period_spread': 18, 'period_total': 27, 'game_early_goal': 3, 'game_winner': 6, 'game_overtime': 3, 'game_spread': 12, 'team_total': 30, 'game_total': 27}

| game | start UTC | horizon | P(home) | P(away) | P(OT) | exp total | home G | away G | contracts (supported/unsupported) | goalies H/A |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ WSH | 2026-10-11T21:00:00Z | T-12h | 0.585 | 0.415 | 0.170 | 6.10 | 3.32 | 2.77 | 51 (25/26) | PROJECTED/PROJECTED |
| VAN @ NYR | 2026-10-11T22:00:00Z | T-12h | 0.646 | 0.354 | 0.161 | 6.53 | 3.73 | 2.80 | 51 (25/26) | PROJECTED/PROJECTED |
| CAR @ PHI | 2026-10-11T23:00:00Z | T-12h | 0.393 | 0.607 | 0.168 | 5.94 | 2.63 | 3.30 | 51 (25/26) | PROJECTED/PROJECTED |

## Contracts (research view; sorted by fee-adjusted EV of the best side; NOT recommendations)

| ticker | family | P(data) | P(mkt mid) | P(anchored) | yes ask | no ask | best | EV after fee | gate |
|---|---|---:|---:|---:|---:|---:|---|---:|---|
| KXNHLSPREAD-26OCT11SEAWSH-WSH3 | game_spread | 0.229 | 0.305 | 0.289 | 31 | 70 | no | +0.057 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH4 | team_total | 0.437 | 0.525 | 0.507 | 54 | 49 | no | +0.056 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN3 | team_total | 0.529 | 0.445 | 0.462 | 46 | 57 | yes | +0.051 | OK |
| KXNHLSPREAD-26OCT11SEAWSH-WSH2 | game_spread | 0.364 | 0.435 | 0.420 | 44 | 57 | no | +0.049 | OK |
| KXNHLGAME-26OCT11SEAWSH-SEA | game_winner | 0.415 | 0.345 | 0.359 | 35 | 66 | yes | +0.049 | OK |
| KXNHLGAME-26OCT11SEAWSH-WSH | game_winner | 0.585 | 0.655 | 0.641 | 66 | 35 | no | +0.049 | OK |
| KXNHLSPREAD-26OCT11VANNYR-NYR3 | game_spread | 0.280 | 0.345 | 0.331 | 35 | 66 | no | +0.044 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN4 | team_total | 0.318 | 0.245 | 0.259 | 26 | 77 | yes | +0.044 | OK |
| KXNHLTOTAL-26OCT11VANNYR-6 | game_total | 0.619 | 0.555 | 0.568 | 56 | 45 | yes | +0.042 | OK |
| KXNHLTOTAL-26OCT11VANNYR-8 | game_total | 0.305 | 0.245 | 0.256 | 25 | 76 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN5 | team_total | 0.159 | 0.100 | 0.110 | 11 | 91 | yes | +0.042 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH5 | team_total | 0.245 | 0.315 | 0.300 | 33 | 70 | no | +0.041 | OK |
| KXNHLGAME-26OCT11VANNYR-VAN | game_winner | 0.354 | 0.295 | 0.306 | 30 | 71 | yes | +0.040 | OK |
| KXNHLGAME-26OCT11VANNYR-NYR | game_winner | 0.646 | 0.705 | 0.694 | 71 | 30 | no | +0.040 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH3 | team_total | 0.657 | 0.725 | 0.712 | 74 | 29 | no | +0.039 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN2 | team_total | 0.763 | 0.700 | 0.713 | 71 | 31 | yes | +0.039 | OK |
| KXNHLTOTAL-26OCT11VANNYR-7 | game_total | 0.502 | 0.445 | 0.456 | 45 | 56 | yes | +0.034 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-7 | game_total | 0.431 | 0.485 | 0.474 | 49 | 52 | no | +0.032 | OK |
| KXNHLSPREAD-26OCT11VANNYR-NYR2 | game_spread | 0.423 | 0.475 | 0.465 | 48 | 53 | no | +0.029 | OK |
| KXNHLTOTAL-26OCT11VANNYR-9 | game_total | 0.218 | 0.170 | 0.179 | 18 | 84 | yes | +0.028 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-5 | game_total | 0.762 | 0.805 | 0.797 | 81 | 20 | no | +0.027 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-4 | game_total | 0.846 | 0.885 | 0.878 | 89 | 12 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH6 | team_total | 0.115 | 0.160 | 0.150 | 17 | 85 | no | +0.026 | OK |
| KXNHLTEAMTOTAL-26OCT11VANNYR-VAN6 | team_total | 0.066 | 0.035 | 0.040 | 4 | 97 | yes | +0.024 | OK |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-WSH2 | team_total | 0.838 | 0.880 | 0.872 | 89 | 13 | no | +0.024 | OK |
| KXNHLSPREAD-26OCT11SEAWSH-SEA2 | game_spread | 0.213 | 0.175 | 0.182 | 18 | 83 | yes | +0.022 | OK |
| KXNHLSPREAD-26OCT11VANNYR-VAN2 | game_spread | 0.180 | 0.145 | 0.152 | 15 | 86 | yes | +0.022 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-6 | game_total | 0.544 | 0.585 | 0.577 | 59 | 42 | no | +0.019 | OK |
| KXNHLTOTAL-26OCT11VANNYR-10 | game_total | 0.108 | 0.080 | 0.085 | 9 | 93 | yes | +0.012 | OK |
| KXNHLTOTAL-26OCT11CARPHI-5 | game_total | 0.736 | 0.765 | 0.759 | 77 | 24 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-9 | game_total | 0.169 | 0.200 | 0.193 | 21 | 81 | no | +0.011 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-8 | game_total | 0.246 | 0.275 | 0.269 | 28 | 73 | no | +0.010 | OK |
| KXNHLTOTAL-26OCT11VANNYR-5 | game_total | 0.812 | 0.780 | 0.787 | 79 | 23 | yes | +0.010 | OK |
| KXNHLTOTAL-26OCT11VANNYR-4 | game_total | 0.887 | 0.865 | 0.870 | 87 | 14 | yes | +0.010 | OK |
| KXNHLSPREAD-26OCT11CARPHI-CAR3 | game_spread | 0.239 | 0.265 | 0.260 | 27 | 74 | no | +0.008 | OK |
| KXNHLTOTAL-26OCT11SEAWSH-10 | game_total | 0.077 | 0.095 | 0.091 | 10 | 91 | no | +0.007 | OK |
| KXNHLSPREAD-26OCT11VANNYR-VAN3 | game_spread | 0.097 | 0.080 | 0.083 | 9 | 93 | yes | +0.002 | OK |
| KXNHLTOTAL-26OCT11VANNYR-3 | game_total | 0.973 | 0.965 | 0.967 | 97 | 4 | yes | +0.001 | OK |
| KXNHLSPREAD-26OCT11SEAWSH-SEA3 | game_spread | 0.117 | 0.100 | 0.103 | 11 | 91 | yes | +0.000 | OK |
| KXNHLTOTAL-26OCT11VANNYR-2 | game_total | 0.990 | 0.985 | 0.986 | 99 | 2 |  | -0.001 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR5 | team_total | 0.238 | 0.260 | 0.256 | 27 | 75 |  | -0.001 | NO_EDGE |
| KXNHLTOTAL-26OCT11SEAWSH-3 | game_total | 0.960 | 0.965 | 0.964 | 97 | 4 |  | -0.002 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA6 | team_total | 0.062 | 0.050 | 0.052 | 6 | 96 |  | -0.002 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-PHI3 | game_spread | 0.106 | 0.115 | 0.113 | 12 | 89 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26OCT11CARPHI-CAR | game_winner | 0.607 | 0.625 | 0.621 | 63 | 38 |  | -0.003 | NO_EDGE |
| KXNHLGAME-26OCT11CARPHI-PHI | game_winner | 0.393 | 0.375 | 0.379 | 38 | 63 |  | -0.003 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA5 | team_total | 0.154 | 0.140 | 0.143 | 15 | 87 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT11SEAWSH-2 | game_total | 0.984 | 0.985 | 0.985 | 99 | 2 |  | -0.005 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-10 | game_total | 0.069 | 0.065 | 0.066 | 7 | 94 |  | -0.006 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-CAR2 | game_spread | 0.380 | 0.395 | 0.392 | 40 | 61 |  | -0.006 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR6 | team_total | 0.111 | 0.115 | 0.114 | 12 | 89 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-3 | game_total | 0.955 | 0.960 | 0.959 | 97 | 5 |  | -0.008 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR2 | team_total | 0.839 | 0.850 | 0.848 | 86 | 16 |  | -0.008 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-7 | game_total | 0.402 | 0.415 | 0.412 | 42 | 59 |  | -0.009 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-4 | game_total | 0.831 | 0.835 | 0.834 | 84 | 17 |  | -0.011 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-2 | game_total | 0.980 | 0.980 | 0.980 | 99 | 3 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI6 | team_total | 0.053 | 0.050 | 0.051 | 6 | 96 |  | -0.011 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI2 | team_total | 0.728 | 0.740 | 0.738 | 75 | 27 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR4 | team_total | 0.434 | 0.455 | 0.451 | 47 | 56 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR6 | team_total | 0.168 | 0.160 | 0.162 | 17 | 85 |  | -0.012 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-9 | game_total | 0.153 | 0.155 | 0.155 | 16 | 85 |  | -0.012 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI5 | team_total | 0.135 | 0.140 | 0.139 | 15 | 87 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA3 | team_total | 0.525 | 0.505 | 0.509 | 52 | 51 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA2 | team_total | 0.760 | 0.745 | 0.748 | 76 | 27 |  | -0.013 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA4 | team_total | 0.311 | 0.295 | 0.298 | 31 | 72 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-8 | game_total | 0.222 | 0.225 | 0.224 | 23 | 78 |  | -0.014 | NO_EDGE |
| KXNHLSPREAD-26OCT11CARPHI-PHI2 | game_spread | 0.197 | 0.195 | 0.195 | 20 | 81 |  | -0.014 | NO_EDGE |
| KXNHLTOTAL-26OCT11CARPHI-6 | game_total | 0.519 | 0.525 | 0.524 | 53 | 48 |  | -0.016 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI4 | team_total | 0.284 | 0.290 | 0.289 | 30 | 72 |  | -0.018 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-PHI3 | team_total | 0.491 | 0.500 | 0.498 | 51 | 51 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11CARPHI-CAR3 | team_total | 0.653 | 0.665 | 0.663 | 68 | 35 |  | -0.019 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR2 | team_total | 0.887 | 0.885 | 0.885 | 90 | 13 |  | -0.020 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR3 | team_total | 0.733 | 0.735 | 0.735 | 75 | 28 |  | -0.027 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR5 | team_total | 0.323 | 0.325 | 0.325 | 34 | 69 |  | -0.028 | NO_EDGE |
| KXNHLTEAMTOTAL-26OCT11VANNYR-NYR4 | team_total | 0.531 | 0.535 | 0.534 | 55 | 48 |  | -0.028 | NO_EDGE |
| KXNHL1P-26OCT11SEAWSH-SEA | period_winner |  | 0.265 |  | 29 | 76 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11SEAWSH-TIE | period_winner |  | 0.320 |  | 34 | 70 |  |  | UNSUPPORTED |
| KXNHL1P-26OCT11SEAWSH-WSH | period_winner |  | 0.400 |  | 41 | 61 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11SEAWSH-SEA2 | period_spread |  | 0.080 |  | 10 | 94 |  |  | UNSUPPORTED |
| KXNHL1PSPREAD-26OCT11SEAWSH-WSH2 | period_spread |  | 0.120 |  | 18 | 94 |  |  | UNSUPPORTED |

## DATA_ONLY_V2 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

| game | V1 P(home) | V2 P(home) | V1 P(OT) | V2 P(OT) | V1 exp total | V2 exp total | V2 goalie factors H/A | largest V1/V2 gap |
|---|---:|---:|---:|---:|---:|---:|---|---|
| SEA @ WSH | 0.585 | 0.564 | 0.170 | 0.208 | 6.10 | 6.40 | 0.961/1.015 | KXNHLTEAMTOTAL-26OCT11SEAWSH-SEA3 +0.053 |
| VAN @ NYR | 0.646 | 0.575 | 0.161 | 0.214 | 6.53 | 6.36 | 0.983/1.021 | KXNHLGAME-26OCT11VANNYR-NYR -0.071 |
| CAR @ PHI | 0.393 | 0.486 | 0.168 | 0.221 | 5.94 | 6.03 | 0.992/0.997 | KXNHLGAME-26OCT11CARPHI-CAR -0.093 |

_DATA_ONLY_V2 is a SHADOW research arm that began at this run's timestamp; it never gates, never replaces V1 and carries no authority. Period prices are PARTIAL_RULES_VERIFIED_NO_SETTLEMENT._


## Thesis card (RESEARCH_ONLY): status COMPLETE · gate PASS · 9 recommended · full analysis in card.md / packet.json `thesis_card`

- Washington wins by over 1.5 goals NO @ 57c · p 0.652 (adj 0.6085) · $9.7 · thesis SEA:WINS
- Washington wins by over 2.5 goals NO @ 70c · p 0.7669 (adj 0.7309) · $4.06 · thesis SEA:WINS
- Seattle wins by over 1.5 goals YES @ 18c · p 0.2288 (adj 0.2019) · $1.41 · thesis SEA:WINS_BY_2PLUS
- Vancouver over 4.5 goals scored YES @ 11c · p 0.1845 (adj 0.1422) · $3.23 · thesis VAN:OFFENSE_4PLUS
- Vancouver wins by over 1.5 goals YES @ 15c · p 0.2194 (adj 0.1822) · $2.47 · thesis VAN:WINS_BY_2PLUS
- New York R wins by over 2.5 goals NO @ 66c · p 0.7666 (adj 0.6941) · $6.58 · thesis GAME:TIGHT
- Vancouver over 1.5 goals scored YES @ 71c · p 0.7835 (adj 0.7417) · $6.29 · thesis VAN:WINS
- Carolina wins by over 2.5 goals NO @ 74c · p 0.8242 (adj 0.7796) · $20.0 · thesis PHI:WINS
- Philadelphia wins by over 1.5 goals YES @ 20c · p 0.2626 (adj 0.2288) · $3.16 · thesis PHI:WINS_BY_2PLUS

## PLAYER_SIM_V1 shadow (RESEARCH_ONLY; not a gate, not a recommendation)

**SEA @ WSH** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- WSH net: Logan Thompson (PROJECTED) exp shots 26.2, exp saves 22.84 (sd 6.35), pull risk 0.059
- SEA net: Philipp Grubauer (PROJECTED) exp shots 28.6, exp saves 24.42 (sd 6.71), pull risk 0.074

**VAN @ NYR** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- NYR net: Dylan Garand (PROJECTED) exp shots 25.36, exp saves 22.17 (sd 6.15), pull risk 0.054
- VAN net: Kevin Lankinen (PROJECTED) exp shots 27.14, exp saves 23.3 (sd 6.54), pull risk 0.074

**CAR @ PHI** · priced 0/0 player contracts · lineups LINES_PROJECTED/LINES_PROJECTED
- PHI net: Joseph Woll (PROJECTED) exp shots 30.15, exp saves 26.04 (sd 6.92), pull risk 0.057
- CAR net: Pyotr Kochetkov (PROJECTED) exp shots 22.75, exp saves 19.73 (sd 5.68), pull risk 0.054

_PLAYER_SIM_V1 is a SHADOW research arm: joint goals / assists / points / saves / first goal from the nhl-sim-2.0 draw. It never gates, never changes V1 or V2 and carries no authority. Probabilities are conditional on the player playing._


_RESEARCH_ONLY: every row is a research observation; nothing here is a recommendation and no wagering authority exists._
