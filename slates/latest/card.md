# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T09:02:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 90.00 | +7.39 | +2.20 | +12.09 | 0.586 | -47.22 | -63.11 | 14.30 |
| B thesis-diversified (joint) ← optimiser card | 38.24 | +2.94 | +0.92 | +6.28 | 0.691 | -17.80 | -17.80 | 8.17 |
| C best expression per thesis | 31.16 | +2.10 | +0.67 | +11.02 | 0.587 | -13.07 | -13.07 | 6.01 |
| R FUNDED research stakes | 12.00 | +1.01 | +0.31 | +1.57 | 0.669 | -5.98 | -5.98 | 0.00 |

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
| Buffalo wins by over 1.5 goals NO | 60 | 0.671 | 0.633 | +0.054 | +0.016 | $8.46 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 73 | 0.788 | 0.757 | +0.044 | +0.013 | $5.00 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: higher confidence-adjusted growth (2.48 vs 1.87 bp); relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.741); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no has the higher standalone adjusted growth (2.48 vs 1.87 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.741); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.741); failure: BUF wins by 2+

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.4498): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -1.0)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3287, phi -0.741)

portfolios: A EV +2.96 (adj +0.87) on $40.00, P(profit) 0.6713, adj growth 5.7 bp · B EV +1.05 (adj +0.31) on $13.46, P(profit) 0.6713, adj growth 2.7 bp · C EV +0.99 (adj +0.30) on $11.16, P(profit) 0.6713, adj growth 2.6 bp · R EV +0.38 (adj +0.11) on $5.00, P(profit) 0.6713, adj growth 3.7 bp

## FLA @ OTT  ·  10000 joint draws  ·  98 bet sides mapped, 4 +EV candidates, 3 on card


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
| Florida wins by over 2.5 goals NO | 82 | 0.877 | 0.846 | +0.046 | +0.015 | $20.00 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 3.5 goals scored YES | 37 | 0.442 | 0.404 | +0.056 | +0.017 | $3.31 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ottawa over 4.5 goals scored YES | 19 | 0.242 | 0.213 | +0.041 | +0.013 | $1.47 | FUNDED_RESEARCH | $1 | OTT:OFFENSE_4PLUS | DIRECT (0.56) | EVIDENCE_MIXED | D |
- **Florida wins by over 2.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes; why: higher confidence-adjusted growth (3.77 vs 2.77 bp); despite a smaller raw edge (+0.046 vs +0.056/contract); wins across more scripts (relative breadth 1.015 vs 0.71); relationships: KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes: DUPLICATIVE (phi 0.303); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: REINFORCING (phi 0.205); failure: FLA wins by 2+
- **Ottawa over 3.5 goals scored YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.77 vs 2.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.303); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: DUPLICATIVE (phi 0.303); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: DUPLICATIVE (phi 0.634); failure: OTT offense suppressed (<= 2 goals)
- **Ottawa over 4.5 goals scored YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.77 vs 2.16 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.205); they share one thesis budget; relationships: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: REINFORCING (phi 0.205); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes: DUPLICATIVE (phi 0.634); failure: FLA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:WINS (p 0.5747): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.4312): highest fidelity KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes (same contract)
- KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -0.71)
- KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis OTT:SUPPRESSED (p 0.3567, phi -0.663)
- KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: FUNDED_RESEARCH; family MIXED; loses 44% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.4253, phi -0.426)

portfolios: A EV +4.43 (adj +1.33) on $50.00, P(profit) 0.4372, adj growth 8.6 bp · B EV +1.90 (adj +0.61) on $24.78, P(profit) 0.4372, adj growth 5.5 bp · C EV +1.12 (adj +0.37) on $20.00, P(profit) 0.8767, adj growth 3.4 bp · R EV +0.63 (adj +0.20) on $7.00, P(profit) 0.4382, adj growth 6.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
