# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-07T13:16:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.42 | +2.95 | +17.50 | 0.636 | -36.92 | -50.19 | 20.50 |
| B thesis-diversified (joint) ← optimiser card | 60.76 | +11.47 | +6.49 | +5.38 | 0.541 | -40.19 | -40.19 | 55.97 |
| C best expression per thesis | 44.50 | +4.62 | +2.34 | +4.43 | 0.539 | -16.85 | -23.93 | 20.62 |
| R FUNDED research stakes | 6.00 | +1.54 | +0.81 | +0.91 | 0.583 | -6.00 | -6.00 | 0.00 |

## PIT @ WSH  ·  10000 joint draws  ·  424 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PIT_win | p_overtime | goals | shots WSH/PIT | WSH/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.46 | 0.00 | 6.05 | 27.2/27.5 | 24.1/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.49 | 5.99 | 27.3/27.7 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.112 | 0.55 | 0.45 | 0.00 | 9.43 | 28.8/29.0 | 23.0/22.2 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.081 | 0.47 | 0.53 | 0.00 | 6.01 | 21.6/32.5 | 28.7/18.4 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.49 | 0.51 | 0.46 | 5.93 | 21.9/32.6 | 29.2/18.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.065 | 0.49 | 0.51 | 0.00 | 9.44 | 23.6/34.6 | 27.8/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Trevor van Riemsdyk: 1+ goals YES | 3 | 0.060 | 0.050 | +0.028 | +0.018 | $3.50 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | FRAGILE (0.09) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 12 | 0.174 | 0.155 | +0.046 | +0.028 | $6.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 28 | 0.346 | 0.326 | +0.052 | +0.032 | $10.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 9 | 0.130 | 0.114 | +0.034 | +0.018 | $4.15 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Trevor van Riemsdyk: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (21.07 vs 15.13 bp); despite a smaller raw edge (+0.028 vs +0.046/contract); relationships: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (15.13 vs 10.52 bp); despite a smaller raw edge (+0.046 vs +0.052/contract); relationships: KXNHLGOAL-26OCT07PITWSH-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.021); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes has the higher standalone adjusted growth (15.13 vs 10.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.016); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes has the higher standalone adjusted growth (15.13 vs 8.11 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.021); they share one thesis budget; relationships: KXNHLGOAL-26OCT07PITWSH-PITTVANRIEMSDYK57-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:OFFENSE_4PLUS (p 0.4131): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:WINS_BY_2PLUS (p 0.265): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.332): highest fidelity KXNHLSPREAD-26OCT07PITWSH-WSH2|no [DIRECT], best adjusted EV KXNHLPTS-26OCT07PITWSH-WSHATUCH89-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT07PITWSH-PITTVANRIEMSDYK57-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 91% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.104)
- KXNHLGOAL-26OCT07PITWSH-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.208)
- KXNHLGOAL-26OCT07PITWSH-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.261)
- KXNHLGOAL-26OCT07PITWSH-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3705, phi -0.174)

portfolios: A EV +13.38 (adj +1.85) on $50.00, P(profit) 0.6607, adj growth 13.0 bp · B EV +8.89 (adj +5.38) on $25.09, P(profit) 0.5537, adj growth 45.9 bp · C EV +2.86 (adj +1.62) on $11.58, P(profit) 0.1739, adj growth 13.9 bp · R EV +0.87 (adj +0.56) on $1.00, P(profit) 0.0598, adj growth 18.1 bp

## COL @ WPG  ·  10000 joint draws  ·  416 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_COL_win | p_overtime | goals | shots WPG/COL | WPG/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.113 | 0.42 | 0.58 | 0.00 | 6.02 | 27.7/28.4 | 24.3/24.6 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 6.01 | 22.1/34.2 | 29.8/19.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.46 | 5.93 | 28.0/28.7 | 25.4/24.7 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.48 | 5.92 | 22.6/34.5 | 31.1/19.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.44 | 0.56 | 0.00 | 9.28 | 29.4/30.2 | 23.5/23.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.077 | 0.36 | 0.64 | 0.00 | 9.35 | 23.8/36.0 | 28.7/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Josh Morrissey: 2+ goals NO | 97 | 0.995 | 0.987 | +0.022 | +0.015 | $20.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.135 | 0.120 | +0.029 | +0.014 | $3.18 | FUNDED_RESEARCH | $1 | WPG:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Colorado wins by over 1.5 goals NO | 59 | 0.667 | 0.626 | +0.061 | +0.019 | $9.49 | FUNDED_RESEARCH | $3 | WPG:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Colorado over 3.5 goals scored NO | 49 | 0.559 | 0.522 | +0.051 | +0.014 | $3.00 | FUNDED_RESEARCH | $1 | COL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Josh Morrissey: 2+ goals NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: MOSTLY_INDEPENDENT (phi -0.001); failure: WPG offense succeeds (4+ goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL2|no; why: higher confidence-adjusted growth (4.40 vs 3.43 bp); despite a smaller raw edge (+0.029 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT07COLWPG-COL2|no: MOSTLY_INDEPENDENT (phi 0.114); KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: MOSTLY_INDEPENDENT (phi 0.019); failure: WPG offense suppressed (<= 2 goals)
- **Colorado wins by over 1.5 goals NO** — thesis: WPG wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no; why: higher confidence-adjusted growth (3.43 vs 1.80 bp); relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.024); KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.114); KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: REINFORCING (phi 0.541); failure: COL wins by 2+
- **Colorado over 3.5 goals scored NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT07COLWPG-COL2|no; why: Broad expression KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no selected over player prop KXNHLAST-26OCT07COLWPG-COLTHUGHES13-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLSPREAD-26OCT07COLWPG-COL2|no: REINFORCING (phi 0.541); failure: COL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis WPG:OFFENSE_4PLUS (p 0.3482): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:WINS (p 0.4464): highest fidelity KXNHLSPREAD-26OCT07COLWPG-COL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no (same contract)
- thesis COL:SUPPRESSED (p 0.3522): highest fidelity KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT07COLWPG-COL2|no — Broad expression KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no selected over player prop KXNHLAST-26OCT07COLWPG-COLTHUGHES13-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT07COLWPG-WPGJMORRISSEY44-2|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3482, phi -0.073)
- KXNHLGOAL-26OCT07COLWPG-WPGMBARRON36-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4303, phi -0.171)
- KXNHLSPREAD-26OCT07COLWPG-COL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:WINS_BY_2PLUS (p 0.3325, phi -1.0)
- KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4302, phi -0.978)
- override: Broad expression KXNHLTEAMTOTAL-26OCT07COLWPG-COL4|no selected over player prop KXNHLAST-26OCT07COLWPG-COLTHUGHES13-1|no because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.92 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.04 (adj +1.10) on $50.00, P(profit) 0.6644, adj growth 7.5 bp · B EV +2.58 (adj +1.11) on $35.67, P(profit) 0.6901, adj growth 10.1 bp · C EV +1.75 (adj +0.72) on $32.92, P(profit) 0.663, adj growth 6.7 bp · R EV +0.67 (adj +0.25) on $5.00, P(profit) 0.5575, adj growth 8.5 bp

## EDM @ ANA  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_EDM_win | p_overtime | goals | shots ANA/EDM | ANA/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.47 | 0.53 | 0.00 | 6.07 | 29.0/28.9 | 24.9/25.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.120 | 0.49 | 0.51 | 0.00 | 9.56 | 30.6/30.3 | 23.8/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.48 | 6.04 | 29.0/28.7 | 25.3/25.7 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.55 | 0.45 | 0.00 | 6.08 | 34.0/23.0 | 19.6/29.7 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.45 | 5.98 | 33.9/23.0 | 19.9/30.4 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.064 | 0.54 | 0.46 | 0.00 | 9.41 | 35.9/24.6 | 18.8/28.7 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
