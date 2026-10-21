# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T10:50:00Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 90.00 | +27.15 | +7.55 | +6.46 | 0.621 | -52.35 | -52.35 | 30.48 |
| B thesis-diversified (joint) ← optimiser card | 48.61 | +7.52 | +2.16 | +7.74 | 0.726 | -25.21 | -30.06 | 18.94 |
| C best expression per thesis | 35.74 | +5.87 | +1.68 | +6.65 | 0.738 | -11.66 | -17.44 | 14.89 |
| R FUNDED research stakes | 14.00 | +2.78 | +0.79 | +1.72 | 0.677 | -7.03 | -7.03 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.118 | 0.65 | 0.35 | 0.00 | 5.99 | 32.4/20.9 | 18.2/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 6.02 | 26.9/26.3 | 23.2/23.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.56 | 0.44 | 0.45 | 5.84 | 32.2/21.1 | 17.9/29.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.51 | 0.49 | 0.45 | 5.91 | 27.3/26.7 | 23.4/24.0 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.067 | 0.66 | 0.34 | 0.00 | 9.13 | 33.7/22.0 | 17.4/26.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.066 | 0.57 | 0.43 | 0.00 | 9.19 | 28.6/28.1 | 22.3/22.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Buffalo wins by over 2.5 goals NO | 73 | 0.788 | 0.757 | +0.044 | +0.013 | $12.58 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 61 | 0.671 | 0.638 | +0.045 | +0.011 | $1.03 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: higher confidence-adjusted growth (1.87 vs 1.24 bp); despite a smaller raw edge (+0.044 vs +0.045/contract); wins across more scripts (relative breadth 0.988 vs 0.873); relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.741); failure: BUF wins by 2+
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no has the higher standalone adjusted growth (1.87 vs 1.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.741); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.741); failure: BUF wins by 2+

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.4498): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF3|no (same contract)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -0.741)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -1.0)

portfolios: A EV +2.62 (adj +0.71) on $40.00, P(profit) 0.6713, adj growth 4.1 bp · B EV +0.82 (adj +0.23) on $13.60, P(profit) 0.7881, adj growth 2.1 bp · C EV +0.81 (adj +0.23) on $13.61, P(profit) 0.7881, adj growth 2.1 bp · R EV +0.31 (adj +0.09) on $5.00, P(profit) 0.7881, adj growth 2.8 bp

## FLA @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 6.02 | 26.5/26.3 | 23.3/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.46 | 5.91 | 26.6/26.5 | 23.3/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.088 | 0.67 | 0.33 | 0.00 | 5.94 | 31.2/20.8 | 18.2/26.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.61 | 0.39 | 0.00 | 9.11 | 28.1/27.9 | 22.7/21.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.57 | 0.43 | 0.46 | 5.9 | 31.7/21.2 | 18.0/28.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.58 | 0.42 | 0.00 | 3.45 | 25.3/25.2 | 23.6/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins 1st Period by over 1.5 goals YES | 3 | 0.091 | 0.048 | +0.059 | +0.016 | $2.37 | FUNDED_RESEARCH | $1 | FLA:SCORES_FIRST | FRAGILE (0.19) | EVIDENCE_THIN | D |
| Florida wins by over 2.5 goals NO | 82 | 0.877 | 0.846 | +0.046 | +0.015 | $19.43 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 72 | 0.782 | 0.748 | +0.048 | +0.014 | $10.57 | FUNDED_RESEARCH | $2 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 4.5 goals scored YES | 19 | 0.242 | 0.213 | +0.041 | +0.013 | $2.64 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Florida wins 1st Period by over 1.5 goals YES** — thesis: FLA scores first; alternative: KXNHL1P-26OCT21FLAOTT-FLA|yes; why: higher confidence-adjusted growth (17.52 vs 0.00 bp); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.287); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.292); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); failure: OTT scores first
- **Florida wins by over 2.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (3.77 vs 2.30 bp); despite a smaller raw edge (+0.046 vs +0.048/contract); relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.287); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: DUPLICATIVE (phi 0.71); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: REINFORCING (phi 0.205); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.77 vs 2.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.710); they share one thesis budget; relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.292); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: DUPLICATIVE (phi 0.71); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: REINFORCING (phi 0.281); failure: FLA wins by 2+
- **Ottawa over 4.5 goals scored YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.77 vs 2.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.205); they share one thesis budget; relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: REINFORCING (phi 0.205); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: REINFORCING (phi 0.281); failure: FLA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SCORES_FIRST (p 0.4592): highest fidelity KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes (same contract)
- thesis OTT:WINS (p 0.5747): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA3|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4312): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA3|no (same contract)
- KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: FUNDED_RESEARCH; family MIXED; loses 81% of the draws where the thesis happens; opposing: failure thesis OTT:SCORES_FIRST (p 0.5397, phi -0.306)
- KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -0.71)
- KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -1.0)
- KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: FUNDED_RESEARCH; family MIXED; loses 44% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.4253, phi -0.426)

portfolios: A EV +24.53 (adj +6.84) on $50.00, P(profit) 0.3201, adj growth 26.4 bp · B EV +6.70 (adj +1.93) on $35.01, P(profit) 0.8378, adj growth 16.9 bp · C EV +5.06 (adj +1.45) on $22.13, P(profit) 0.9152, adj growth 12.8 bp · R EV +2.47 (adj +0.70) on $9.00, P(profit) 0.3201, adj growth 22.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
