# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T09:50:03Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +31.75 | +8.74 | +1.64 | 0.524 | -53.62 | -53.62 | 22.75 |
| B thesis-diversified (joint) ← optimiser card | 46.05 | +7.15 | +2.03 | +10.00 | 0.623 | -22.76 | -24.62 | 17.72 |
| C best expression per thesis | 33.29 | +6.05 | +1.75 | +8.89 | 0.642 | -9.20 | -15.20 | 15.43 |
| R FUNDED research stakes | 13.00 | +2.64 | +0.74 | +1.68 | 0.665 | -5.24 | -6.98 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


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
| Buffalo wins by over 1.5 goals NO | 60 | 0.671 | 0.633 | +0.054 | +0.016 | $7.68 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 73 | 0.788 | 0.757 | +0.044 | +0.013 | $4.30 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 3.5 goals scored NO | 53 | 0.594 | 0.560 | +0.047 | +0.012 | $1.75 | FUNDED_RESEARCH | $1 | BUF:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: higher confidence-adjusted growth (2.48 vs 1.87 bp); relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.741); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.557); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no has the higher standalone adjusted growth (2.48 vs 1.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.741); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.741); KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: REINFORCING (phi 0.524); failure: BUF wins by 2+
- **Buffalo over 3.5 goals scored NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no has the higher standalone adjusted growth (2.48 vs 1.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.557); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.557); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: REINFORCING (phi 0.524); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.4498): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3826): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -1.0)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -0.741)
- KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.396, phi -0.98)

portfolios: A EV +3.89 (adj +1.10) on $50.00, P(profit) 0.5736, adj growth 5.9 bp · B EV +1.08 (adj +0.32) on $13.73, P(profit) 0.6713, adj growth 2.8 bp · C EV +0.99 (adj +0.30) on $11.16, P(profit) 0.6713, adj growth 2.6 bp · R EV +0.38 (adj +0.11) on $5.00, P(profit) 0.6713, adj growth 3.6 bp

## FLA @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 3 +EV candidates, 3 on card


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
| Florida wins 1st Period by over 1.5 goals YES | 3 | 0.091 | 0.048 | +0.059 | +0.016 | $2.32 | FUNDED_RESEARCH | $1 | FLA:SCORES_FIRST | FRAGILE (0.19) | EVIDENCE_THIN | D |
| Florida wins by over 2.5 goals NO | 82 | 0.877 | 0.846 | +0.046 | +0.015 | $19.34 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 1.5 goals NO | 72 | 0.782 | 0.746 | +0.048 | +0.012 | $10.66 | FUNDED_RESEARCH | $2 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins 1st Period by over 1.5 goals YES** — thesis: FLA scores first; alternative: KXNHL1P-26OCT21FLAOTT-FLA|yes; why: higher confidence-adjusted growth (17.52 vs 0.00 bp); alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: INTENTIONAL_DIVERSIFIER (phi -0.287); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.292); failure: OTT scores first
- **Florida wins by over 2.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (3.77 vs 1.56 bp); despite a smaller raw edge (+0.046 vs +0.048/contract); relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.287); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: DUPLICATIVE (phi 0.71); failure: FLA wins by 2+
- **Florida wins by over 1.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.77 vs 1.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.710); they share one thesis budget; relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.292); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: DUPLICATIVE (phi 0.71); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SCORES_FIRST (p 0.4592): highest fidelity KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes (same contract)
- thesis OTT:WINS (p 0.5747): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA3|no (same contract)
- KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: FUNDED_RESEARCH; family MIXED; loses 81% of the draws where the thesis happens; opposing: failure thesis OTT:SCORES_FIRST (p 0.5397, phi -0.306)
- KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -0.71)
- KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -1.0)

portfolios: A EV +27.85 (adj +7.64) on $50.00, P(profit) 0.0914, adj growth 16.8 bp · B EV +6.07 (adj +1.71) on $32.32, P(profit) 0.8365, adj growth 14.9 bp · C EV +5.06 (adj +1.45) on $22.13, P(profit) 0.9152, adj growth 12.8 bp · R EV +2.26 (adj +0.63) on $8.00, P(profit) 0.8365, adj growth 19.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
