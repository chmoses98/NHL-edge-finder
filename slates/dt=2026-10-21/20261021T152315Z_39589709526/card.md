# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T15:23:15Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +12.75 | +4.04 | +13.30 | 0.615 | -38.74 | -57.12 | 32.08 |
| B thesis-diversified (joint) ← optimiser card | 71.12 | +10.29 | +3.96 | +10.59 | 0.615 | -28.72 | -40.56 | 34.71 |
| C best expression per thesis | 61.52 | +8.11 | +2.63 | +8.96 | 0.657 | -27.72 | -32.32 | 23.25 |
| R FUNDED research stakes | 11.00 | +1.33 | +0.60 | +1.10 | 0.628 | -6.41 | -9.66 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.122 | 0.62 | 0.38 | 0.00 | 5.97 | 32.2/20.9 | 18.1/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.58 | 0.42 | 0.00 | 6.0 | 27.2/26.8 | 23.5/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.46 | 5.88 | 26.9/26.3 | 23.2/23.6 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.58 | 0.42 | 0.48 | 5.86 | 32.6/21.0 | 18.0/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.57 | 0.43 | 0.00 | 9.17 | 28.4/27.8 | 22.4/22.1 | even strength |
| BUF shot control · low event (<=4) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.47 | 2.77 | 30.8/19.4 | 18.0/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 8 | 0.108 | 0.098 | +0.022 | +0.013 | $3.09 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ assists NO | 49 | 0.631 | 0.530 | +0.124 | +0.022 | $10.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BUF:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 60 | 0.669 | 0.632 | +0.053 | +0.015 | $4.52 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 2.5 goals NO | 73 | 0.787 | 0.756 | +0.044 | +0.012 | $3.75 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: higher confidence-adjusted growth (4.70 vs 2.21 bp); despite a smaller raw edge (+0.022 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: MOSTLY_INDEPENDENT (phi 0.106); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: MOSTLY_INDEPENDENT (phi 0.091); failure: PHI offense suppressed (<= 2 goals)
- **Rasmus Dahlin: 1+ assists NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: higher confidence-adjusted growth (4.29 vs 2.21 bp); wins across more scripts (relative breadth 0.996 vs 0.894); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: REINFORCING (phi 0.188); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: REINFORCING (phi 0.171); failure: BUF offense succeeds (4+ goals)
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: higher confidence-adjusted growth (2.21 vs 1.77 bp); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.106); KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no: REINFORCING (phi 0.188); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.74); failure: BUF wins by 2+
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no has the higher standalone adjusted growth (2.21 vs 1.77 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.740); they share one thesis budget; relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.091); KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no: REINFORCING (phi 0.171); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.74); failure: BUF wins by 2+

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis BUF:SUPPRESSED (p 0.3827): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.3107): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4408): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4749, phi -0.185)
- KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.3999, phi -0.266)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3305, phi -1.0)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3305, phi -0.74)

portfolios: A EV +7.08 (adj +2.00) on $50.00, P(profit) 0.5764, adj growth 15.0 bp · B EV +4.03 (adj +1.12) on $22.07, P(profit) 0.5764, adj growth 9.7 bp · C EV +3.26 (adj +0.66) on $18.57, P(profit) 0.6311, adj growth 5.8 bp · R EV +0.49 (adj +0.22) on $4.00, P(profit) 0.6896, adj growth 7.3 bp

## FLA @ OTT  ·  10000 joint draws  ·  428 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 5.97 | 26.4/26.3 | 23.4/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.47 | 5.88 | 26.3/26.3 | 23.1/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.086 | 0.69 | 0.31 | 0.00 | 6.05 | 31.2/21.0 | 18.3/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.61 | 0.39 | 0.00 | 9.21 | 28.3/28.0 | 22.8/21.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.54 | 0.46 | 0.48 | 5.91 | 31.4/21.1 | 18.0/28.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.058 | 0.69 | 0.31 | 0.00 | 9.27 | 33.6/22.7 | 18.0/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 65 | 0.717 | 0.697 | +0.051 | +0.031 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 15 | 0.198 | 0.182 | +0.039 | +0.023 | $6.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.668 | 0.619 | +0.071 | +0.022 | $18.24 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
| Ottawa over 4.5 goals scored YES | 19 | 0.246 | 0.215 | +0.045 | +0.015 | $4.56 | FUNDED_RESEARCH | $2 | OTT:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (9.33 vs 1.70 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: INTENTIONAL_DIVERSIFIER (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes; why: higher confidence-adjusted growth (8.72 vs 2.90 bp); despite a smaller raw edge (+0.039 vs +0.045/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.901 vs 0.513); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: REINFORCING (phi 0.153); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT21FLAOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (4.39 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: INTENTIONAL_DIVERSIFIER (phi -0.214); failure: OTT offense succeeds (4+ goals)
- **Ottawa over 4.5 goals scored YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (2.90 vs 1.70 bp); despite a smaller raw edge (+0.045 vs +0.049/contract); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.002); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: REINFORCING (phi 0.153); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.214); failure: FLA wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4611): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.3554): highest fidelity KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4289): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3205, phi -0.251)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3554, phi -0.192)
- KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4289, phi -0.241)
- KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes: FUNDED_RESEARCH; family MIXED; loses 43% of the draws where the thesis happens; opposing: failure thesis FLA:WINS (p 0.4269, phi -0.425)

portfolios: A EV +5.67 (adj +2.04) on $50.00, P(profit) 0.5331, adj growth 17.1 bp · B EV +6.26 (adj +2.84) on $49.05, P(profit) 0.6687, adj growth 25.0 bp · C EV +4.85 (adj +1.97) on $42.95, P(profit) 0.6024, adj growth 17.4 bp · R EV +0.83 (adj +0.38) on $7.00, P(profit) 0.7871, adj growth 12.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
