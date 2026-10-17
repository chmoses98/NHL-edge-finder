# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T17:24:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.97 | +24.77 | +6.00 | +24.21 | 0.791 | -13.05 | -22.09 | 55.92 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +18.10 | +8.72 | +16.64 | 0.735 | -16.63 | -26.00 | 83.31 |
| C best expression per thesis | 150.01 | +21.75 | +8.44 | +20.13 | 0.717 | -22.64 | -32.38 | 78.22 |
| R FUNDED research stakes | 22.00 | +2.49 | +1.16 | +2.00 | 0.647 | -4.87 | -6.57 | 0.00 |

## CAR @ WPG  ·  10000 joint draws  ·  420 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.357 / away 0.643

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_CAR_win | p_overtime | goals | shots WPG/CAR | WPG/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.128 | 0.42 | 0.58 | 0.00 | 6.0 | 20.9/32.9 | 28.9/17.9 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.46 | 0.54 | 0.47 | 5.93 | 20.8/32.7 | 29.2/17.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.48 | 0.52 | 0.00 | 6.03 | 26.4/27.3 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.48 | 0.52 | 0.48 | 5.94 | 26.5/27.2 | 23.8/23.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.088 | 0.39 | 0.61 | 0.00 | 9.3 | 22.2/34.2 | 26.9/17.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.50 | 0.50 | 0.00 | 9.34 | 28.2/28.8 | 22.6/22.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikolaj Ehlers: 1+ goals NO | 73 | 0.777 | 0.764 | +0.033 | +0.020 | $7.22 | FUNDED_RESEARCH | $2 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Kyle Connor: 1+ goals YES | 37 | 0.412 | 0.400 | +0.025 | +0.014 | $1.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 31 | 0.352 | 0.338 | +0.027 | +0.013 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 67 | 0.710 | 0.696 | +0.025 | +0.011 | $3.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CAR:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG3|yes; why: KXNHLSPREAD-26OCT17CARWPG-WPG3|yes has the higher standalone adjusted growth (6.00 vs 4.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.106); relationships: KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17CARWPG-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.014); failure: CAR offense succeeds (4+ goals)
- **Kyle Connor: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17CARWPG-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.53 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17CARWPG-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: WPG offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG3|yes; why: Player prop expression KXNHLGOAL-26OCT17CARWPG-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.86 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes (same contract)
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes (same contract)
- thesis WPG:WINS (p 0.4733): highest fidelity KXNHLSPREAD-26OCT17CARWPG-CAR2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes — Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT17CARWPG-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4113, phi -0.211)
- KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.315)
- KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.282)
- KXNHLGOAL-26OCT17CARWPG-CARSAHO20-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4113, phi -0.242)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.54 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-CARSAHO20-1|no selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.86 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.53 vs 0.55 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.24 (adj +0.52) on $13.71, P(profit) 0.5534, adj growth 4.7 bp · B EV +0.69 (adj +0.37) on $13.89, P(profit) 0.7123, adj growth 3.6 bp · C EV +1.31 (adj +0.49) on $3.45, P(profit) 0.257, adj growth 4.5 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.7767, adj growth 2.0 bp

## VAN @ TBL  ·  10000 joint draws  ·  388 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.760 / away 0.239

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.156 | 0.71 | 0.29 | 0.00 | 5.95 | 33.1/20.7 | 18.2/28.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.123 | 0.55 | 0.45 | 0.48 | 5.9 | 33.4/21.1 | 18.0/30.0 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.105 | 0.73 | 0.27 | 0.00 | 9.3 | 35.0/22.1 | 17.9/26.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.101 | 0.66 | 0.34 | 0.00 | 6.03 | 27.4/26.6 | 23.7/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.54 | 0.46 | 0.48 | 5.9 | 27.4/26.6 | 23.3/24.0 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.069 | 0.68 | 0.32 | 0.00 | 3.44 | 31.8/19.8 | 18.5/29.3 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.607 | 0.482 | +0.170 | +0.045 | $2.88 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 54 | 0.726 | 0.602 | +0.168 | +0.044 | $4.97 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| John Carlson: 1+ goals NO | 82 | 0.878 | 0.860 | +0.048 | +0.030 | $6.15 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 58 | 0.647 | 0.627 | +0.050 | +0.030 | $4.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB3|no; why: higher confidence-adjusted growth (18.13 vs 17.46 bp); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: DUPLICATIVE (phi 0.765); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.208); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.13 vs 17.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.765); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.765); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.184); failure: TBL wins by 2+
- **John Carlson: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.13 vs 13.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.090); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.09); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: Player prop expression KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.82 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: REINFORCING (phi 0.208); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.184); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.2999): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4201): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.1871): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- KXNHLSPREAD-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.2 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3928, phi -1.0)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.1 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3928, phi -0.765)
- KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.477, phi -0.13)
- KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.477, phi -0.25)
- override: Player prop expression KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.82 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.74 (adj +0.86) on $13.71, P(profit) 0.7284, adj growth 8.2 bp · B EV +3.32 (adj +1.12) on $18.09, P(profit) 0.6514, adj growth 10.8 bp · C EV +5.41 (adj +1.97) on $14.82, P(profit) 0.6561, adj growth 18.2 bp · R EV +1.11 (adj +0.33) on $5.00, P(profit) 0.71, adj growth 12.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-TB|no == KXNHLGAME-26OCT17VANTB-VAN|yes

## SEA @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.632 / away 0.368

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_SEA_win | p_overtime | goals | shots FLA/SEA | FLA/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.02 | 27.2/26.9 | 23.2/23.7 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.108 | 0.58 | 0.42 | 0.00 | 6.0 | 32.9/21.5 | 18.5/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.49 | 0.51 | 0.49 | 5.94 | 27.5/27.1 | 23.7/24.2 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.55 | 0.45 | 0.49 | 5.91 | 33.0/21.6 | 18.5/29.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.4 | 29.3/28.8 | 23.2/22.8 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.071 | 0.57 | 0.43 | 0.00 | 9.29 | 34.9/23.1 | 17.8/27.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 10 | 0.148 | 0.135 | +0.042 | +0.028 | $2.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.155 | 0.142 | +0.038 | +0.025 | $2.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 64 | 0.709 | 0.690 | +0.052 | +0.034 | $7.24 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Mackie Samoskevich: 1+ goals YES | 19 | 0.233 | 0.221 | +0.033 | +0.021 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (17.95 vs 12.66 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: SEA offense suppressed (<= 2 goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes; why: higher confidence-adjusted growth (12.66 vs 7.37 bp); despite a smaller raw edge (+0.038 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.535); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17SEAFLA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: SEA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.32 vs 8.77 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17SEAFLA-SEAMSAMOSKEVICH11-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Mackie Samoskevich: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (12.66 vs 5.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis SEA:OFFENSE_4PLUS (p 0.3753): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.3867): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2633): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.183)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.205)
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.247)
- KXNHLGOAL-26OCT17SEAFLA-SEAMSAMOSKEVICH11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.212)

portfolios: A EV +2.15 (adj +0.51) on $13.71, P(profit) 0.6479, adj growth 4.7 bp · B EV +2.67 (adj +1.75) on $14.24, P(profit) 0.3991, adj growth 16.7 bp · C EV +2.64 (adj +1.51) on $16.56, P(profit) 0.7518, adj growth 14.1 bp · R EV +0.16 (adj +0.10) on $2.00, P(profit) 0.7086, adj growth 4.0 bp

## NYI @ TOR  ·  10000 joint draws  ·  442 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.543 / away 0.457

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NYI_win | p_overtime | goals | shots TOR/NYI | TOR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.53 | 0.47 | 0.00 | 6.0 | 28.1/28.5 | 25.1/24.5 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.106 | 0.46 | 0.54 | 0.00 | 5.95 | 22.0/34.1 | 30.3/18.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.47 | 5.98 | 28.0/28.6 | 25.4/24.6 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.49 | 5.95 | 22.1/34.2 | 30.9/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.54 | 0.46 | 0.00 | 9.28 | 29.4/30.3 | 24.5/23.2 | even strength |
| NYI shot control · high event (8+) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 9.2 | 24.0/36.2 | 29.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Gavin McKenna: 1+ assists NO | 70 | 0.768 | 0.729 | +0.054 | +0.015 | $5.05 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYITOR-TORDRADDYSH43-1|no; why: higher confidence-adjusted growth (2.26 vs 0.38 bp); alternative not eligible: confidence-adjusted EV +0.0065 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3797): highest fidelity KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no (same contract)
- KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4002, phi -0.222)

portfolios: A EV +0.41 (adj +0.11) on $5.49, P(profit) 0.7684, adj growth 1.1 bp · B EV +0.38 (adj +0.10) on $5.05, P(profit) 0.7684, adj growth 1.0 bp · C EV +0.58 (adj +0.16) on $7.78, P(profit) 0.7684, adj growth 1.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  414 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.559 / away 0.441

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_BUF_win | p_overtime | goals | shots MTL/BUF | MTL/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.55 | 0.45 | 0.00 | 6.03 | 27.3/27.6 | 24.2/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.47 | 5.98 | 27.4/27.8 | 24.6/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.55 | 0.45 | 0.00 | 9.28 | 28.7/29.1 | 23.5/22.2 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.086 | 0.49 | 0.51 | 0.00 | 6.07 | 21.7/32.7 | 28.9/18.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.50 | 0.50 | 0.43 | 5.91 | 21.6/32.5 | 29.0/18.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.063 | 0.45 | 0.55 | 0.00 | 9.21 | 23.3/34.7 | 27.9/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 87 | 0.904 | 0.893 | +0.026 | +0.015 | $7.24 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ goals NO | 73 | 0.767 | 0.756 | +0.023 | +0.013 | $4.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 24 | 0.276 | 0.265 | +0.024 | +0.012 | $1.42 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (4.66 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: BUF offense succeeds (4+ goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (2.88 vs 1.65 bp); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: BUF offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (1.84 vs 1.13 bp); despite a smaller raw edge (+0.023 vs +0.024/contract); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: MTL offense succeeds (4+ goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (1.65 vs 0.32 bp); despite a smaller raw edge (+0.024 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MTL:SUPPRESSED (p 0.3662): highest fidelity KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.3845): highest fidelity KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes (same contract)
- thesis BUF:NET_LOW_VOLUME (p 0.4665): highest fidelity KXNHLSAVE-26OCT17BUFMTL-BUFULUUKKONEN1-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT17BUFMTL-BUFULUUKKONEN1-26|no (same contract)
- KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3845, phi -0.132)
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.19)
- KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4184, phi -0.228)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.243)

portfolios: A EV +1.67 (adj +0.36) on $13.71, P(profit) 0.4925, adj growth 3.5 bp · B EV +0.70 (adj +0.38) on $14.64, P(profit) 0.3403, adj growth 3.7 bp · C EV +1.58 (adj +0.32) on $13.77, P(profit) 0.6412, adj growth 3.0 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.9039, adj growth 1.3 bp

## SJS @ DET  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.584 / away 0.416

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.55 | 0.45 | 0.00 | 6.05 | 27.8/27.5 | 24.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.48 | 5.93 | 27.7/27.3 | 24.1/24.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.104 | 0.60 | 0.40 | 0.00 | 6.01 | 32.8/21.8 | 18.8/28.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.45 | 5.88 | 33.1/21.9 | 18.7/29.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.52 | 0.48 | 0.00 | 9.28 | 29.3/29.0 | 23.2/23.3 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 9.17 | 34.8/23.0 | 18.1/27.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 84 | 0.882 | 0.870 | +0.033 | +0.021 | $7.24 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Luca Cagnoni: 1+ goals NO | 91 | 0.939 | 0.929 | +0.024 | +0.014 | $7.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Kiefer Sherwood: 1+ goals YES | 17 | 0.204 | 0.193 | +0.024 | +0.013 | $1.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Detroit over 3.5 goals scored NO | 53 | 0.592 | 0.558 | +0.044 | +0.011 | $1.68 | FUNDED_RESEARCH | $1 | DET:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: higher confidence-adjusted growth (7.64 vs 1.06 bp); despite a smaller raw edge (+0.033 vs +0.044/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.0 vs 0.894); relationships: KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no: REINFORCING (phi 0.152); failure: DET offense succeeds (4+ goals)
- **Luca Cagnoni: 1+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SJDET-DET3|no; why: higher confidence-adjusted growth (2.48 vs 1.06 bp); despite a smaller raw edge (+0.024 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no: MOSTLY_INDEPENDENT (phi 0.015); failure: SJS offense suppressed (<= 2 goals)
- **Detroit over 3.5 goals scored NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17SJDET-DET3|no; why: alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: REINFORCING (phi 0.152); KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3587): highest fidelity KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.419): highest fidelity KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJMMARCHMENT27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.3823): highest fidelity KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no (same contract)
- KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3965, phi -0.15)
- KXNHLGOAL-26OCT17SJDET-SJLCAGNONI42-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3587, phi -0.107)
- KXNHLGOAL-26OCT17SJDET-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.419, phi -0.227)
- KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3965, phi -0.976)

portfolios: A EV +1.10 (adj +0.22) on $13.71, P(profit) 0.7147, adj growth 2.1 bp · B EV +0.78 (adj +0.42) on $17.52, P(profit) 0.5902, adj growth 4.1 bp · C EV +1.22 (adj +0.49) on $23.30, P(profit) 0.5457, adj growth 4.6 bp · R EV +0.16 (adj +0.07) on $3.00, P(profit) 0.5461, adj growth 2.6 bp

## OTT @ PHI  ·  10000 joint draws  ·  442 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.421 / away 0.579

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_OTT_win | p_overtime | goals | shots PHI/OTT | PHI/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.49 | 0.51 | 0.00 | 5.99 | 25.6/26.1 | 22.5/22.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.93 | 25.6/26.2 | 22.9/22.3 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.099 | 0.40 | 0.60 | 0.00 | 5.95 | 20.5/31.4 | 27.2/17.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.45 | 0.55 | 0.49 | 5.8 | 20.7/31.5 | 28.1/17.7 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.50 | 0.50 | 0.00 | 3.41 | 24.5/25.0 | 23.0/22.7 | even strength |
| OTT shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.76 | 19.0/29.7 | 28.2/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.809 | +0.030 | +0.017 | $6.21 | FUNDED_RESEARCH | $2 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 74 | 0.851 | 0.769 | +0.098 | +0.016 | $5.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Tim Stutzle: 1+ assists NO | 50 | 0.626 | 0.534 | +0.108 | +0.017 | $2.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Carter Yakemchuk: 1+ assists NO | 71 | 0.780 | 0.738 | +0.056 | +0.013 | $3.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-PHIDJIRICEK55-1|no; why: higher confidence-adjusted growth (4.00 vs 0.00 bp); despite a smaller raw edge (+0.030 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense succeeds (4+ goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (2.89 vs 2.49 bp); despite a smaller raw edge (+0.098 vs +0.108/contract); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.031); KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: OTT offense succeeds (4+ goals)
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (2.49 vs 1.91 bp); relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.031); KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: OTT offense succeeds (4+ goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no has the higher standalone adjusted growth (2.49 vs 1.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.078); they share one thesis budget; relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.078); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4466): highest fidelity KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4749): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3027, phi -0.183)
- KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.6 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.187)
- KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.275)
- KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.216)

portfolios: A EV +1.56 (adj +0.32) on $13.71, P(profit) 0.5753, adj growth 3.1 bp · B EV +1.65 (adj +0.38) on $17.07, P(profit) 0.6319, adj growth 3.7 bp · C EV +1.07 (adj +0.17) on $5.10, P(profit) 0.626, adj growth 1.5 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.8224, adj growth 1.7 bp

## NYR @ CBJ  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.548 / away 0.452

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_NYR_win | p_overtime | goals | shots CBJ/NYR | CBJ/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.116 | 0.62 | 0.38 | 0.00 | 6.01 | 26.8/26.2 | 23.2/22.7 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.109 | 0.66 | 0.34 | 0.00 | 5.96 | 32.1/20.9 | 18.1/27.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.55 | 0.45 | 0.49 | 5.87 | 32.5/21.3 | 18.1/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.49 | 5.92 | 26.9/26.5 | 23.3/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.56 | 0.44 | 0.00 | 9.15 | 28.2/27.7 | 22.2/22.0 | even strength |
| CBJ shot control · high event (8+) · decided (2+) | 0.069 | 0.66 | 0.34 | 0.00 | 9.18 | 33.7/22.2 | 17.6/26.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.791 | 0.748 | +0.057 | +0.014 | $5.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 69 | 0.728 | 0.716 | +0.023 | +0.011 | $3.41 | FUNDED_RESEARCH | $1 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no; why: higher confidence-adjusted growth (2.17 vs 1.23 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no has the higher standalone adjusted growth (2.17 vs 1.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYR:SUPPRESSED (p 0.4701): highest fidelity KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.219)
- KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.228)

portfolios: A EV +0.60 (adj +0.18) on $10.77, P(profit) 0.5748, adj growth 1.7 bp · B EV +0.52 (adj +0.15) on $8.75, P(profit) 0.5748, adj growth 1.5 bp · C EV +0.64 (adj +0.16) on $8.20, P(profit) 0.791, adj growth 1.4 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.7277, adj growth 0.6 bp

## DAL @ CHI  ·  10000 joint draws  ·  396 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.344 / away 0.656

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_DAL_win | p_overtime | goals | shots CHI/DAL | CHI/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.48 | 0.52 | 0.00 | 5.98 | 25.6/26.0 | 22.5/22.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.109 | 0.39 | 0.61 | 0.00 | 5.99 | 20.0/30.8 | 26.5/17.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.47 | 0.53 | 0.46 | 5.91 | 25.7/26.2 | 22.8/22.5 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.46 | 0.54 | 0.47 | 5.91 | 20.3/31.2 | 27.9/17.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.075 | 0.49 | 0.51 | 0.00 | 9.32 | 27.2/27.7 | 21.7/21.4 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.064 | 0.36 | 0.64 | 0.00 | 9.13 | 21.5/32.5 | 25.5/16.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Frank Nazar: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $2.80 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.148 | 0.135 | +0.032 | +0.018 | $1.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Anton Frondell: 1+ goals YES | 20 | 0.247 | 0.232 | +0.036 | +0.021 | $2.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Cole Smith: 1+ goals YES | 7 | 0.095 | 0.088 | +0.021 | +0.013 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17DALCHI-CHI2|yes; why: higher confidence-adjusted growth (9.54 vs 9.50 bp); despite a smaller raw edge (+0.041 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.946 vs 0.536); relationships: KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes has the higher standalone adjusted growth (9.54 vs 6.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: CHI offense suppressed (<= 2 goals)
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes has the higher standalone adjusted growth (9.54 vs 5.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CHI offense suppressed (<= 2 goals)
- **Cole Smith: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes has the higher standalone adjusted growth (9.54 vs 5.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3529): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2507): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes (same contract)
- thesis CHI:WINS (p 0.4708): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.247)
- KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.195)
- KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.246)
- KXNHLGOAL-26OCT17DALCHI-CHICSMITH22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.154)

portfolios: A EV +3.45 (adj +0.88) on $13.71, P(profit) 0.4708, adj growth 7.8 bp · B EV +1.71 (adj +1.05) on $7.79, P(profit) 0.5562, adj growth 10.0 bp · C EV +2.94 (adj +1.20) on $15.02, P(profit) 0.4018, adj growth 11.1 bp · R EV +0.20 (adj +0.13) on $1.00, P(profit) 0.2415, adj growth 4.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17DALCHI-DAL|no == KXNHLGAME-26OCT17DALCHI-CHI|yes

## STL @ NSH  ·  10000 joint draws  ·  416 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.495 / away 0.505

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_STL_win | p_overtime | goals | shots NSH/STL | NSH/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.48 | 0.52 | 0.00 | 6.04 | 27.3/27.5 | 23.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.51 | 0.49 | 0.49 | 5.97 | 27.5/27.5 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.50 | 0.50 | 0.00 | 9.39 | 29.1/29.0 | 22.9/22.8 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.068 | 0.47 | 0.53 | 0.00 | 6.0 | 21.6/31.9 | 27.9/18.4 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.068 | 0.59 | 0.41 | 0.00 | 5.98 | 32.2/21.8 | 18.7/28.2 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.46 | 5.92 | 32.3/22.0 | 18.7/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Peterson: 1+ goals YES | 7 | 0.102 | 0.092 | +0.027 | +0.018 | $1.57 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.071 | 0.065 | +0.017 | +0.012 | $1.06 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
- **Dylan Peterson: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (9.81 vs 1.03 bp); alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: STL offense suppressed (<= 2 goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (6.21 vs 0.94 bp); despite a smaller raw edge (+0.017 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.912 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-STLDPETERSON32-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4049): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis NSH:OFFENSE_4PLUS (p 0.4176): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17STLNSH-STLDPETERSON32-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.148)
- KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.106)

portfolios: A EV +1.13 (adj +0.76) on $3.25, P(profit) 0.1653, adj growth 7.1 bp · B EV +0.91 (adj +0.62) on $2.63, P(profit) 0.1653, adj growth 5.8 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.36 (adj +0.24) on $1.00, P(profit) 0.1015, adj growth 8.3 bp

## BOS @ LAK  ·  10000 joint draws  ·  388 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.553 / away 0.447

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.54 | 0.46 | 0.00 | 5.97 | 27.9/27.4 | 24.1/24.2 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.110 | 0.61 | 0.39 | 0.00 | 5.93 | 33.2/21.8 | 18.9/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.47 | 5.8 | 28.0/27.5 | 24.3/24.8 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.54 | 0.46 | 0.47 | 5.83 | 33.3/22.0 | 18.7/30.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.52 | 0.48 | 0.00 | 9.2 | 29.7/29.1 | 23.3/23.2 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.061 | 0.63 | 0.37 | 0.00 | 9.18 | 34.7/23.3 | 18.4/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Matthew Poitras: 1+ goals YES | 10 | 0.127 | 0.118 | +0.021 | +0.011 | $1.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 71 | 0.788 | 0.739 | +0.063 | +0.015 | $5.58 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Matthew Poitras: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes; why: higher confidence-adjusted growth (2.95 vs 0.88 bp); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.031); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: higher confidence-adjusted growth (2.31 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0057 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BOSLA-BOSMPOITRAS51-1|yes: MOSTLY_INDEPENDENT (phi -0.031); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis BOS:SUPPRESSED (p 0.4548): highest fidelity KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no (same contract)
- thesis BOS:OFFENSE_4PLUS (p 0.3324): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17BOSLA-BOSMPOITRAS51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4548, phi -0.177)
- KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3324, phi -0.223)

portfolios: A EV +0.79 (adj +0.28) on $7.07, P(profit) 0.819, adj growth 2.6 bp · B EV +0.70 (adj +0.23) on $6.69, P(profit) 0.819, adj growth 2.2 bp · C EV +0.73 (adj +0.17) on $8.34, P(profit) 0.7878, adj growth 1.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  408 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.555 / away 0.445

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.54 | 0.46 | 0.00 | 6.1 | 27.5/27.6 | 24.3/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.121 | 0.53 | 0.47 | 0.00 | 9.53 | 29.2/29.1 | 23.0/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.49 | 0.51 | 0.47 | 6.02 | 27.7/27.7 | 24.3/24.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.070 | 0.60 | 0.40 | 0.00 | 6.0 | 32.5/21.8 | 18.8/28.2 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 6.05 | 32.7/22.0 | 18.8/29.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.067 | 0.62 | 0.38 | 0.00 | 9.5 | 34.4/23.4 | 18.3/27.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 15 | 0.209 | 0.193 | +0.050 | +0.034 | $3.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Mathieu Joseph: 1+ goals YES | 7 | 0.103 | 0.094 | +0.029 | +0.019 | $1.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 29 | 0.355 | 0.337 | +0.051 | +0.032 | $3.74 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ assists YES | 32 | 0.454 | 0.357 | +0.118 | +0.022 | $2.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.62) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes; why: higher confidence-adjusted growth (18.62 vs 16.43 bp); despite a smaller raw edge (+0.050 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.858 vs 0.732); relationships: KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: EDM offense suppressed (<= 2 goals)
- **Mathieu Joseph: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (18.62 vs 11.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.025); they share one thesis budget; relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes has the higher standalone adjusted growth (18.62 vs 10.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes; why: Player prop expression KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.62 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4307): highest fidelity KXNHLPTS-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes — Player prop expression KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.62 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.3487): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis UTA:SUPPRESSED (p 0.3202): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTADGUENTHER11-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTADGUENTHER11-1|no (same contract)
- KXNHLGOAL-26OCT17EDMUTA-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.206)
- KXNHLGOAL-26OCT17EDMUTA-EDMMJOSEPH21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.133)
- KXNHLGOAL-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.272)
- KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 38% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.9 pts; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3487, phi -0.304)
- override: Player prop expression KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-2|yes because adjusted EV differs by only 0.1 pts while thesis capture is 0.62 vs 0.23 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.87 (adj +0.65) on $13.71, P(profit) 0.624, adj growth 6.0 bp · B EV +3.07 (adj +1.63) on $10.85, P(profit) 0.5381, adj growth 15.5 bp · C EV +2.46 (adj +1.35) on $18.41, P(profit) 0.209, adj growth 12.5 bp · R EV +0.17 (adj +0.11) on $1.00, P(profit) 0.3555, adj growth 4.0 bp

## PIT @ VGK  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.70 | 0.30 | 0.00 | 6.09 | 27.6/27.4 | 24.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.51 | 0.49 | 0.47 | 5.99 | 27.6/27.5 | 24.2/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.71 | 0.29 | 0.00 | 9.5 | 28.8/28.7 | 23.7/21.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.093 | 0.75 | 0.25 | 0.00 | 6.02 | 32.2/21.4 | 19.1/27.3 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.071 | 0.77 | 0.23 | 0.00 | 9.36 | 34.0/23.0 | 18.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.49 | 5.95 | 32.7/21.8 | 18.7/29.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 6 | 0.086 | 0.076 | +0.023 | +0.012 | $1.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.284 | 0.270 | +0.031 | +0.018 | $2.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ goals NO | 75 | 0.791 | 0.777 | +0.028 | +0.014 | $5.50 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 69 | 0.734 | 0.718 | +0.029 | +0.013 | $4.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17PITVGK-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (5.31 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17PITVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: VGK offense suppressed (<= 2 goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-2|yes; why: higher confidence-adjusted growth (3.56 vs 0.81 bp); wins across more scripts (relative breadth 0.928 vs 0.785); alternative not eligible: confidence-adjusted EV +0.0039 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17PITVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Trevor Connelly: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (2.27 vs 1.81 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no; why: Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17PITVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3095): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2848): highest fidelity KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no (same contract)
- thesis PIT:SUPPRESSED (p 0.4763): highest fidelity KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17PITVGK-PITEMALKIN71-1|no (same contract)
- KXNHLGOAL-26OCT17PITVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2848, phi -0.125)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4763, phi -0.276)
- KXNHLGOAL-26OCT17PITVGK-VGKTCONNELLY24-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5106, phi -0.185)
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5106, phi -0.217)
- override: Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.88 vs 0.88 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.08 (adj +0.35) on $13.71, P(profit) 0.5458, adj growth 3.3 bp · B EV +0.99 (adj +0.52) on $12.79, P(profit) 0.7113, adj growth 4.9 bp · C EV +1.17 (adj +0.45) on $15.26, P(profit) 0.6416, adj growth 4.2 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.7907, adj growth 1.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
