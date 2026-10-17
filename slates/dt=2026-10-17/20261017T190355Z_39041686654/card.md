# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-17T19:03:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.04 | +26.85 | +6.77 | +25.44 | 0.835 | -7.97 | -17.42 | 63.76 |
| B thesis-diversified (joint) ← optimiser card | 148.49 | +21.14 | +9.53 | +20.05 | 0.775 | -13.22 | -22.01 | 91.56 |
| C best expression per thesis | 149.22 | +28.75 | +9.39 | +28.63 | 0.791 | -16.76 | -29.12 | 87.70 |
| R FUNDED research stakes | 21.00 | +2.54 | +1.38 | +1.24 | 0.615 | -4.77 | -6.52 | 0.00 |

## CAR @ WPG  ·  10000 joint draws  ·  440 bet sides mapped, 17 +EV candidates, 4 on card

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
| Sebastian Aho: 1+ assists NO | 45 | 0.630 | 0.510 | +0.162 | +0.042 | $6.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CAR:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Morgan Barron: 1+ goals YES | 10 | 0.136 | 0.125 | +0.029 | +0.019 | $1.60 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Kyle Connor: 1+ goals YES | 37 | 0.412 | 0.400 | +0.025 | +0.014 | $1.80 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 31 | 0.352 | 0.338 | +0.027 | +0.013 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ assists NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17CARWPG-WPG3|yes; why: higher confidence-adjusted growth (15.72 vs 6.00 bp); wins across more scripts (relative breadth 1.011 vs 0.485); relationships: KXNHLGOAL-26OCT17CARWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CAR offense succeeds (4+ goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: higher confidence-adjusted growth (8.23 vs 7.54 bp); despite a smaller raw edge (+0.029 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.97 vs 0.554); relationships: KXNHLAST-26OCT17CARWPG-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: WPG offense suppressed (<= 2 goals)
- **Kyle Connor: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes has the higher standalone adjusted growth (7.54 vs 1.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.250); relationships: KXNHLAST-26OCT17CARWPG-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17CARWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT17CARWPG-WPG5|yes; why: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.45 vs 0.99 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT17CARWPG-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17CARWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.13, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis CAR:SUPPRESSED (p 0.3699): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-CAR4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT17CARWPG-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3734): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes (same contract)
- thesis WPG:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes (same contract)
- KXNHLAST-26OCT17CARWPG-CARSAHO20-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.5 pts; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4113, phi -0.276)
- KXNHLGOAL-26OCT17CARWPG-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.172)
- KXNHLGOAL-26OCT17CARWPG-WPGKCONNOR81-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.315)
- KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4046, phi -0.282)
- override: Player prop expression KXNHLGOAL-26OCT17CARWPG-WPGMSCHEIFELE55-1|yes selected over broad KXNHLTEAMTOTAL-26OCT17CARWPG-WPG2|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.45 vs 0.99 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.50 (adj +0.56) on $12.78, P(profit) 0.6868, adj growth 5.3 bp · B EV +2.95 (adj +1.00) on $11.44, P(profit) 0.6799, adj growth 9.6 bp · C EV +4.80 (adj +1.38) on $13.59, P(profit) 0.7092, adj growth 12.9 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.4116, adj growth 1.3 bp

## VAN @ TBL  ·  10000 joint draws  ·  382 bet sides mapped, 30 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.759 / away 0.241

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_VAN_win | p_overtime | goals | shots TBL/VAN | TBL/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.158 | 0.71 | 0.29 | 0.00 | 6.04 | 33.2/20.8 | 18.3/28.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.55 | 0.45 | 0.47 | 5.92 | 33.4/21.0 | 17.9/29.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.109 | 0.73 | 0.27 | 0.00 | 9.27 | 35.1/22.5 | 18.1/27.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.096 | 0.66 | 0.34 | 0.00 | 6.02 | 27.4/26.5 | 23.6/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.52 | 0.48 | 0.47 | 5.94 | 27.5/26.6 | 23.4/24.1 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.071 | 0.65 | 0.35 | 0.00 | 3.42 | 31.5/19.8 | 18.6/29.0 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 42 | 0.607 | 0.482 | +0.170 | +0.045 | $2.89 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 2.5 goals NO | 55 | 0.728 | 0.609 | +0.160 | +0.042 | $3.88 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| John Carlson: 1+ goals NO | 82 | 0.876 | 0.860 | +0.046 | +0.029 | $5.63 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 57 | 0.637 | 0.619 | +0.050 | +0.032 | $3.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB3|no; why: higher confidence-adjusted growth (18.05 vs 15.46 bp); relationships: KXNHLSPREAD-26OCT17VANTB-TB3|no: DUPLICATIVE (phi 0.76); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.207); failure: TBL wins by 2+
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT17VANTB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT17VANTB-TB2|no has the higher standalone adjusted growth (18.05 vs 15.46 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.760); they share one thesis budget; relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: DUPLICATIVE (phi 0.76); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.183); failure: TBL wins by 2+
- **John Carlson: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: KXNHLSPREAD-26OCT17VANTB-VAN2|yes has the higher standalone adjusted growth (22.91 vs 13.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.073); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: MOSTLY_INDEPENDENT (phi 0.113); KXNHLSPREAD-26OCT17VANTB-TB3|no: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT17VANTB-VAN2|yes; why: Player prop expression KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26OCT17VANTB-TB2|no: REINFORCING (phi 0.207); KXNHLSPREAD-26OCT17VANTB-TB3|no: REINFORCING (phi 0.183); KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.16, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.11.
- thesis VAN:WINS_BY_2PLUS (p 0.1954): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no (same contract)
- thesis VAN:OFFENSE_4PLUS (p 0.3038): highest fidelity KXNHLTEAMTOTAL-26OCT17VANTB-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3193): highest fidelity KXNHLSPREAD-26OCT17VANTB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17VANTB-TB2|no — Player prop expression KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26OCT17VANTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 19.2 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3931, phi -1.0)
- KXNHLSPREAD-26OCT17VANTB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 18.3 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3931, phi -0.76)
- KXNHLGOAL-26OCT17VANTB-TBJCARLSON74-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4754, phi -0.145)
- KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4754, phi -0.272)
- override: Player prop expression KXNHLGOAL-26OCT17VANTB-TBNKUCHEROV86-1|no selected over player prop KXNHLAST-26OCT17VANTB-TBJCARLSON74-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.83 vs 0.84 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.57 (adj +0.98) on $12.78, P(profit) 0.7864, adj growth 9.3 bp · B EV +2.87 (adj +1.00) on $16.36, P(profit) 0.6497, adj growth 9.7 bp · C EV +4.87 (adj +1.59) on $10.52, P(profit) 0.6069, adj growth 14.8 bp · R EV +0.78 (adj +0.25) on $4.00, P(profit) 0.7114, adj growth 9.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17VANTB-VAN|yes == KXNHLGAME-26OCT17VANTB-TB|no

## SEA @ FLA  ·  10000 joint draws  ·  418 bet sides mapped, 21 +EV candidates, 4 on card

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
| Ben Meyers: 1+ goals YES | 10 | 0.148 | 0.135 | +0.042 | +0.028 | $2.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 63 | 0.709 | 0.688 | +0.062 | +0.041 | $4.96 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Ryan Winterton: 1+ goals YES | 11 | 0.155 | 0.142 | +0.038 | +0.025 | $1.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 63 | 0.694 | 0.676 | +0.047 | +0.030 | $4.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes; why: higher confidence-adjusted growth (17.95 vs 12.66 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: SEA offense suppressed (<= 2 goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (16.50 vs 8.77 bp); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: FLA offense succeeds (4+ goals)
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes; why: higher confidence-adjusted growth (12.66 vs 7.37 bp); despite a smaller raw edge (+0.038 vs +0.062/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.535); relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: SEA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (16.50 vs 8.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: FLA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis FLA:SUPPRESSED (p 0.3867): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:OFFENSE_4PLUS (p 0.3753): highest fidelity KXNHLTEAMTOTAL-26OCT17SEAFLA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS_BY_2PLUS (p 0.2633): highest fidelity KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17SEAFLA-SEA2|yes (same contract)
- KXNHLGOAL-26OCT17SEAFLA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.183)
- KXNHLGOAL-26OCT17SEAFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.247)
- KXNHLGOAL-26OCT17SEAFLA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4037, phi -0.205)
- KXNHLGOAL-26OCT17SEAFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4008, phi -0.229)

portfolios: A EV +2.36 (adj +0.62) on $12.78, P(profit) 0.4954, adj growth 5.7 bp · B EV +2.30 (adj +1.52) on $13.86, P(profit) 0.6292, adj growth 14.6 bp · C EV +2.71 (adj +1.59) on $15.94, P(profit) 0.7518, adj growth 14.9 bp · R EV +0.19 (adj +0.13) on $2.00, P(profit) 0.7086, adj growth 5.0 bp

## NYI @ TOR  ·  10000 joint draws  ·  458 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.554 / away 0.446

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
| Gavin McKenna: 1+ assists NO | 70 | 0.768 | 0.729 | +0.054 | +0.015 | $4.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17NYITOR-TORKMARCHENKO86-1|no; why: higher confidence-adjusted growth (2.26 vs 0.71 bp); alternative not eligible: confidence-adjusted EV +0.0087 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, NYI shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:SUPPRESSED (p 0.3797): highest fidelity KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no (same contract)
- KXNHLAST-26OCT17NYITOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4002, phi -0.222)

portfolios: A EV +0.38 (adj +0.10) on $5.11, P(profit) 0.7684, adj growth 1.0 bp · B EV +0.34 (adj +0.09) on $4.57, P(profit) 0.7684, adj growth 0.9 bp · C EV +0.56 (adj +0.15) on $7.49, P(profit) 0.7684, adj growth 1.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BUF @ MTL  ·  10000 joint draws  ·  414 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.557 / away 0.443

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
| Owen Power: 1+ goals NO | 86 | 0.904 | 0.892 | +0.035 | +0.023 | $6.54 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
| Zach Benson: 1+ goals YES | 23 | 0.276 | 0.264 | +0.034 | +0.021 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Ryan McLeod: 1+ goals YES | 15 | 0.183 | 0.172 | +0.024 | +0.013 | $1.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Chris Kreider: 1+ goals NO | 73 | 0.767 | 0.756 | +0.023 | +0.013 | $4.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (10.54 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: BUF offense succeeds (4+ goals)
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: higher confidence-adjusted growth (5.26 vs 0.66 bp); despite a smaller raw edge (+0.034 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0083 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: BUF offense suppressed (<= 2 goals)
- **Ryan McLeod: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes has the higher standalone adjusted growth (5.26 vs 2.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.014); they share one thesis budget; relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: BUF offense suppressed (<= 2 goals)
- **Chris Kreider: 1+ goals NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17BUFMTL-MTLCCAUFIELD13-1|no; why: higher confidence-adjusted growth (1.84 vs 1.39 bp); despite a smaller raw edge (+0.023 vs +0.024/contract); relationships: KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis BUF:OFFENSE_4PLUS (p 0.3845): highest fidelity KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3662): highest fidelity KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no (same contract)
- thesis BUF:NET_LOW_VOLUME (p 0.4665): highest fidelity KXNHLSAVE-26OCT17BUFMTL-BUFULUUKKONEN1-26|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT17BUFMTL-BUFULUUKKONEN1-26|no (same contract)
- KXNHLGOAL-26OCT17BUFMTL-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3845, phi -0.132)
- KXNHLGOAL-26OCT17BUFMTL-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.243)
- KXNHLGOAL-26OCT17BUFMTL-BUFRMCLEOD71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3882, phi -0.19)
- KXNHLGOAL-26OCT17BUFMTL-MTLCKREIDER22-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4184, phi -0.228)

portfolios: A EV +1.63 (adj +0.55) on $12.78, P(profit) 0.4011, adj growth 5.3 bp · B EV +0.89 (adj +0.54) on $14.15, P(profit) 0.3948, adj growth 5.2 bp · C EV +1.62 (adj +0.53) on $15.09, P(profit) 0.6412, adj growth 4.9 bp · R EV +0.08 (adj +0.05) on $2.00, P(profit) 0.9039, adj growth 2.1 bp

## SJS @ DET  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.583 / away 0.417

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_SJS_win | p_overtime | goals | shots DET/SJS | DET/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.52 | 0.48 | 0.00 | 5.99 | 27.6/27.3 | 23.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.48 | 5.92 | 27.8/27.4 | 24.1/24.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.104 | 0.58 | 0.42 | 0.00 | 5.98 | 32.9/21.6 | 18.5/28.8 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.51 | 0.49 | 0.48 | 5.85 | 33.1/22.0 | 18.8/29.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.52 | 0.48 | 0.00 | 9.26 | 29.0/28.8 | 22.9/22.9 | even strength |
| DET shot control · high event (8+) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 9.21 | 34.5/23.4 | 18.4/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Danielson: 1+ goals NO | 84 | 0.884 | 0.872 | +0.035 | +0.022 | $6.54 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Barclay Goodrow: 1+ goals YES | 6 | 0.085 | 0.077 | +0.021 | +0.013 | $1.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 42 | 0.595 | 0.460 | +0.157 | +0.023 | $3.74 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
| Detroit wins by over 2.5 goals NO | 76 | 0.811 | 0.783 | +0.038 | +0.010 | $4.15 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: higher confidence-adjusted growth (8.66 vs 1.87 bp); despite a smaller raw edge (+0.035 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.005 vs 0.89); relationships: KXNHLGOAL-26OCT17SJDET-SJBGOODROW23-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLSPREAD-26OCT17SJDET-DET3|no: MOSTLY_INDEPENDENT (phi 0.098); failure: DET offense succeeds (4+ goals)
- **Barclay Goodrow: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT17SJDET-DET3|no; why: higher confidence-adjusted growth (6.35 vs 1.26 bp); despite a smaller raw edge (+0.021 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLSPREAD-26OCT17SJDET-DET3|no: MOSTLY_INDEPENDENT (phi 0.09); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17SJDET-SJLCAGNONI42-1|no; why: higher confidence-adjusted growth (4.62 vs 0.77 bp); evidence CALIBRATION_WARNING vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT17SJDET-SJBGOODROW23-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLSPREAD-26OCT17SJDET-DET3|no: INTENTIONAL_DIVERSIFIER (phi -0.163); failure: SJS offense succeeds (4+ goals)
- **Detroit wins by over 2.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no; why: KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no has the higher standalone adjusted growth (1.87 vs 1.26 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.504); relationships: KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.098); KXNHLGOAL-26OCT17SJDET-SJBGOODROW23-1|yes: MOSTLY_INDEPENDENT (phi 0.09); KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.163); failure: DET wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DET shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4125): highest fidelity KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no (same contract)
- thesis SJS:WINS (p 0.4876): highest fidelity KXNHLSPREAD-26OCT17SJDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT17SJDET-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17SJDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3892, phi -0.152)
- KXNHLGOAL-26OCT17SJDET-SJBGOODROW23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4125, phi -0.149)
- KXNHLAST-26OCT17SJDET-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.9 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3648, phi -0.285)
- KXNHLSPREAD-26OCT17SJDET-DET3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:WINS_BY_2PLUS (p 0.2983, phi -0.741)

portfolios: A EV +2.01 (adj +0.35) on $12.78, P(profit) 0.68, adj growth 3.3 bp · B EV +2.15 (adj +0.64) on $15.46, P(profit) 0.5679, adj growth 6.1 bp · C EV +2.71 (adj +0.46) on $14.98, P(profit) 0.4672, adj growth 4.3 bp · R EV +0.18 (adj +0.08) on $4.00, P(profit) 0.7289, adj growth 3.0 bp

## OTT @ PHI  ·  10000 joint draws  ·  438 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.417 / away 0.583

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
| Tim Stutzle: 1+ assists NO | 49 | 0.626 | 0.531 | +0.118 | +0.024 | $3.77 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.809 | +0.030 | +0.017 | $6.54 | FUNDED_RESEARCH | $2 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Dylan Cozens: 1+ goals NO | 72 | 0.763 | 0.751 | +0.029 | +0.017 | $4.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Tim Stutzle: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no; why: higher confidence-adjusted growth (4.88 vs 3.24 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.115); failure: OTT offense succeeds (4+ goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-PHIDJIRICEK55-1|no; why: higher confidence-adjusted growth (4.00 vs 0.68 bp); despite a smaller raw edge (+0.030 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0078 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: PHI offense succeeds (4+ goals)
- **Dylan Cozens: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no; why: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.87 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: MOSTLY_INDEPENDENT (phi 0.115); KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:SUPPRESSED (p 0.4466): highest fidelity KXNHLAST-26OCT17OTTPHI-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no — Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.87 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis PHI:SUPPRESSED (p 0.4749): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT17OTTPHI-OTTTSTUTZLE18-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.6 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.275)
- KXNHLGOAL-26OCT17OTTPHI-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3027, phi -0.183)
- KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3398, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT17OTTPHI-OTTDCOZENS24-1|no selected over player prop KXNHLAST-26OCT17OTTPHI-OTTABURAKOVSKY95-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.87 vs 0.92 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +1.94 (adj +0.39) on $12.78, P(profit) 0.6057, adj growth 3.7 bp · B EV +1.31 (adj +0.42) on $14.91, P(profit) 0.5136, adj growth 4.1 bp · C EV +1.57 (adj +0.31) on $6.71, P(profit) 0.626, adj growth 2.9 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.8224, adj growth 1.7 bp

## NYR @ CBJ  ·  10000 joint draws  ·  418 bet sides mapped, 3 +EV candidates, 2 on card

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
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.791 | 0.748 | +0.057 | +0.014 | $4.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 69 | 0.728 | 0.716 | +0.023 | +0.011 | $2.66 | FUNDED_RESEARCH | $1 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT17NYRCBJ-4|no; why: KXNHLTOTAL-26OCT17NYRCBJ-4|no has the higher standalone adjusted growth (2.60 vs 2.17 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.134); relationships: KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT17NYRCBJ-4|no; why: KXNHLTOTAL-26OCT17NYRCBJ-4|no has the higher standalone adjusted growth (2.60 vs 1.23 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.132); relationships: KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, CBJ shot control · normal event (5-7) · decided (2+) 0.11, CBJ shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:LOW_EVENT (p 0.263): highest fidelity KXNHLTOTAL-26OCT17NYRCBJ-4|no [DIRECT], best adjusted EV KXNHLTOTAL-26OCT17NYRCBJ-4|no (same contract)
- thesis NYR:SUPPRESSED (p 0.4701): highest fidelity KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLAST-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.219)
- KXNHLGOAL-26OCT17NYRCBJ-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3121, phi -0.228)

portfolios: A EV +1.28 (adj +0.41) on $12.63, P(profit) 0.6104, adj growth 3.6 bp · B EV +0.42 (adj +0.12) on $7.00, P(profit) 0.5748, adj growth 1.2 bp · C EV +0.43 (adj +0.14) on $1.54, P(profit) 0.1629, adj growth 1.3 bp · R EV +0.03 (adj +0.02) on $1.00, P(profit) 0.7277, adj growth 0.6 bp

## DAL @ CHI  ·  10000 joint draws  ·  398 bet sides mapped, 22 +EV candidates, 4 on card

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
| Anton Frondell: 1+ goals YES | 19 | 0.247 | 0.231 | +0.047 | +0.030 | $2.80 | FUNDED_RESEARCH | $1 | CHI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Frank Nazar: 1+ goals YES | 19 | 0.241 | 0.227 | +0.041 | +0.027 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 24 | 0.295 | 0.280 | +0.042 | +0.027 | $2.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Ryan Greene: 1+ goals YES | 11 | 0.148 | 0.135 | +0.032 | +0.018 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Anton Frondell: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes; why: higher confidence-adjusted growth (11.99 vs 9.54 bp); relationships: KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: CHI offense suppressed (<= 2 goals)
- **Frank Nazar: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (11.99 vs 9.54 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: CHI offense suppressed (<= 2 goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (11.99 vs 8.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes has the higher standalone adjusted growth (11.99 vs 6.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3529): highest fidelity KXNHLTEAMTOTAL-26OCT17DALCHI-CHI4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS_BY_2PLUS (p 0.2507): highest fidelity KXNHLSPREAD-26OCT17DALCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes (same contract)
- thesis CHI:WINS (p 0.4708): highest fidelity KXNHLSPREAD-26OCT17DALCHI-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT17DALCHI-CHI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT17DALCHI-CHIAFRONDELL16-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.246)
- KXNHLGOAL-26OCT17DALCHI-CHIFNAZAR91-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.247)
- KXNHLGOAL-26OCT17DALCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.259)
- KXNHLGOAL-26OCT17DALCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4271, phi -0.195)

portfolios: A EV +2.49 (adj +0.47) on $12.78, P(profit) 0.6154, adj growth 4.4 bp · B EV +2.04 (adj +1.29) on $9.66, P(profit) 0.6549, adj growth 12.3 bp · C EV +3.24 (adj +1.26) on $13.44, P(profit) 0.4045, adj growth 11.7 bp · R EV +0.23 (adj +0.15) on $1.00, P(profit) 0.2475, adj growth 5.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT17DALCHI-DAL|no == KXNHLGAME-26OCT17DALCHI-CHI|yes

## STL @ NSH  ·  10000 joint draws  ·  422 bet sides mapped, 2 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

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
| Adam Wilsby: 1+ goals YES | 4 | 0.071 | 0.063 | +0.028 | +0.020 | $1.47 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 24 | 0.284 | 0.272 | +0.031 | +0.019 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (20.87 vs 0.94 bp); despite a smaller raw edge (+0.028 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.912 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: NSH offense suppressed (<= 2 goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT17STLNSH-9|yes; why: higher confidence-adjusted growth (4.02 vs 0.94 bp); despite a smaller raw edge (+0.031 vs +0.032/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.895 vs 0.376); alternative not eligible: confidence-adjusted EV +0.0082 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis STL:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.4176): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT17STLNSH-NSHAWILSBY2-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.3659, phi -0.106)
- KXNHLGOAL-26OCT17STLNSH-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3808, phi -0.248)

portfolios: A EV +1.54 (adj +1.08) on $4.50, P(profit) 0.3333, adj growth 10.1 bp · B EV +1.20 (adj +0.84) on $3.42, P(profit) 0.3333, adj growth 8.0 bp · C EV +0.40 (adj +0.24) on $3.25, P(profit) 0.2836, adj growth 2.2 bp · R EV +0.65 (adj +0.47) on $1.00, P(profit) 0.0706, adj growth 16.2 bp

## BOS @ LAK  ·  10000 joint draws  ·  404 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.553 / away 0.447

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_BOS_win | p_overtime | goals | shots LAK/BOS | LAK/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.55 | 0.45 | 0.00 | 5.97 | 28.1/27.5 | 24.1/24.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.111 | 0.63 | 0.37 | 0.00 | 5.93 | 33.3/21.8 | 19.1/29.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.49 | 0.51 | 0.47 | 5.93 | 28.1/27.7 | 24.5/24.7 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.53 | 0.47 | 0.42 | 5.83 | 33.5/22.0 | 18.8/30.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.55 | 0.45 | 0.00 | 9.19 | 29.3/28.9 | 23.2/22.9 | even strength |
| LAK shot control · high event (8+) · decided (2+) | 0.062 | 0.64 | 0.36 | 0.00 | 9.18 | 35.0/23.5 | 18.6/27.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Artemi Panarin: 1+ assists NO | 49 | 0.623 | 0.530 | +0.115 | +0.022 | $3.83 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Charlie McAvoy: 1+ assists NO | 59 | 0.671 | 0.628 | +0.064 | +0.021 | $5.08 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| JJ Peterka: 1+ assists NO | 72 | 0.783 | 0.747 | +0.049 | +0.013 | $4.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
| Elias Lindholm: 1+ goals YES | 20 | 0.232 | 0.222 | +0.021 | +0.010 | $1.43 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
- **Artemi Panarin: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (4.38 vs 2.65 bp); relationships: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: LAK offense succeeds (4+ goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (4.02 vs 1.75 bp); relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.169); failure: BOS offense succeeds (4+ goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no; why: second expression of the same thesis: KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no has the higher standalone adjusted growth (4.02 vs 1.75 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: BOS offense succeeds (4+ goals)
- **Elias Lindholm: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT17BOSLA-BOSMKHUSNUTDINOV92-1|yes; why: higher confidence-adjusted growth (1.43 vs 0.02 bp); despite a smaller raw edge (+0.021 vs +0.076/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0015 below the 0.010/contract floor; relationships: KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: INTENTIONAL_DIVERSIFIER (phi -0.169); KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis LAK:SUPPRESSED (p 0.3978): highest fidelity KXNHLAST-26OCT17BOSLA-LAAPANARIN10-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.4519): highest fidelity KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:OFFENSE_4PLUS (p 0.3292): highest fidelity KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes (same contract)
- KXNHLAST-26OCT17BOSLA-LAAPANARIN10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.3926, phi -0.292)
- KXNHLAST-26OCT17BOSLA-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.259)
- KXNHLAST-26OCT17BOSLA-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3292, phi -0.212)
- KXNHLGOAL-26OCT17BOSLA-BOSELINDHOLM28-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4519, phi -0.243)

portfolios: A EV +1.49 (adj +0.35) on $12.78, P(profit) 0.7327, adj growth 3.4 bp · B EV +1.82 (adj +0.48) on $14.45, P(profit) 0.5184, adj growth 4.7 bp · C EV +2.55 (adj +0.68) on $17.06, P(profit) 0.534, adj growth 6.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ UTA  ·  10000 joint draws  ·  432 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.553 / away 0.447

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_UTA_win | p_EDM_win | p_overtime | goals | shots UTA/EDM | UTA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.53 | 0.47 | 0.00 | 6.05 | 27.4/27.3 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 9.51 | 29.2/29.1 | 23.2/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.47 | 6.04 | 27.8/27.7 | 24.3/24.3 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.075 | 0.59 | 0.41 | 0.00 | 6.09 | 32.6/21.8 | 18.7/28.0 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.064 | 0.62 | 0.38 | 0.00 | 9.52 | 34.0/23.2 | 18.0/26.3 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.53 | 0.47 | 0.49 | 6.05 | 32.7/22.0 | 18.7/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nate Schmidt: 1+ goals YES | 4 | 0.067 | 0.059 | +0.024 | +0.016 | $1.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ assists NO | 71 | 0.798 | 0.751 | +0.073 | +0.027 | $6.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 8 | 0.110 | 0.101 | +0.025 | +0.016 | $1.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Zach Hyman: 1+ goals YES | 31 | 0.358 | 0.344 | +0.033 | +0.018 | $2.80 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
- **Nate Schmidt: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes; why: higher confidence-adjusted growth (13.17 vs 1.58 bp); relationships: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: UTA offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-1|no; why: higher confidence-adjusted growth (8.04 vs 3.60 bp); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.218); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (7.00 vs 5.23 bp); despite a smaller raw edge (+0.025 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.106); KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes; why: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.51 vs 0.50 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: INTENTIONAL_DIVERSIFIER (phi -0.218); KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.3535): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no (same contract)
- thesis EDM:OFFENSE_4PLUS (p 0.4295): highest fidelity KXNHLAST-26OCT17EDMUTA-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes — Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.51 vs 0.50 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis UTA:OFFENSE_4PLUS (p 0.4702): highest fidelity KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17EDMUTA-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26OCT17EDMUTA-UTANSCHMIDT88-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3208, phi -0.107)
- KXNHLAST-26OCT17EDMUTA-EDMCMCDAVID97-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4295, phi -0.328)
- KXNHLGOAL-26OCT17EDMUTA-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.149)
- KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.3535, phi -0.271)
- override: Player prop expression KXNHLGOAL-26OCT17EDMUTA-EDMZHYMAN18-1|yes selected over player prop KXNHLAST-26OCT17EDMUTA-EDMMEKHOLM14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.51 vs 0.50 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.13 (adj +0.63) on $12.78, P(profit) 0.5682, adj growth 6.0 bp · B EV +2.01 (adj +1.11) on $11.93, P(profit) 0.3772, adj growth 10.6 bp · C EV +2.48 (adj +0.91) on $21.54, P(profit) 0.7383, adj growth 8.6 bp · R EV +0.10 (adj +0.06) on $1.00, P(profit) 0.358, adj growth 2.1 bp

## PIT @ VGK  ·  10000 joint draws  ·  424 bet sides mapped, 9 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.642 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_PIT_win | p_overtime | goals | shots VGK/PIT | VGK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.69 | 0.31 | 0.00 | 6.04 | 27.7/27.5 | 24.8/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.71 | 0.29 | 0.00 | 9.35 | 29.1/28.8 | 23.9/21.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.55 | 0.45 | 0.46 | 6.0 | 27.6/27.4 | 24.1/24.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.094 | 0.74 | 0.26 | 0.00 | 6.02 | 32.4/21.6 | 19.2/27.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.48 | 5.93 | 32.3/21.7 | 18.6/28.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.067 | 0.77 | 0.23 | 0.00 | 9.33 | 34.2/23.0 | 18.8/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 67 | 0.734 | 0.716 | +0.049 | +0.030 | $6.54 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Bryan Rust: 1+ goals YES | 24 | 0.286 | 0.271 | +0.033 | +0.018 | $1.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 64 | 0.679 | 0.668 | +0.023 | +0.012 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (9.39 vs 1.33 bp); relationships: KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.018); failure: VGK offense succeeds (4+ goals)
- **Bryan Rust: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT17PITVGK-PITBRUST17-2|yes; why: KXNHLPTS-26OCT17PITVGK-PITBRUST17-2|yes has the higher standalone adjusted growth (5.73 vs 3.72 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.444); relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: PIT offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no; why: Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes (same contract)
- thesis VGK:SUPPRESSED (p 0.2823): highest fidelity KXNHLPTS-26OCT17PITVGK-VGKJEICHEL9-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no — Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis VGK:NET_HIGH_VOLUME (p 0.1594): highest fidelity KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT17PITVGK-VGKAHILL33-22|yes (same contract)
- KXNHLGOAL-26OCT17PITVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.202)
- KXNHLGOAL-26OCT17PITVGK-PITBRUST17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4708, phi -0.264)
- KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5155, phi -0.226)
- override: Player prop expression KXNHLGOAL-26OCT17PITVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT17PITVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.85 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.53 (adj +0.28) on $12.78, P(profit) 0.6238, adj growth 2.6 bp · B EV +0.82 (adj +0.48) on $11.28, P(profit) 0.6136, adj growth 4.6 bp · C EV +0.80 (adj +0.15) on $8.07, P(profit) 0.4108, adj growth 1.4 bp · R EV +0.14 (adj +0.09) on $2.00, P(profit) 0.7344, adj growth 3.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
