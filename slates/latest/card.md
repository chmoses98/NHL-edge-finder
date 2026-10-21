# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T14:35:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +13.51 | +5.93 | -0.03 | 0.491 | -45.09 | -62.12 | 44.75 |
| B thesis-diversified (joint) ← optimiser card | 65.56 | +9.10 | +5.08 | +2.89 | 0.600 | -27.14 | -42.55 | 43.53 |
| C best expression per thesis | 50.19 | +3.44 | +1.51 | +14.50 | 0.552 | -30.55 | -30.55 | 13.33 |
| R FUNDED research stakes | 11.00 | +1.90 | +1.18 | +2.16 | 0.601 | -5.35 | -11.00 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  420 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.122 | 0.64 | 0.36 | 0.00 | 5.99 | 32.4/20.9 | 18.2/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.59 | 0.41 | 0.00 | 5.97 | 27.0/26.5 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.47 | 5.89 | 27.4/26.9 | 23.6/24.2 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.45 | 5.84 | 32.1/20.9 | 17.8/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 9.15 | 28.8/28.0 | 22.7/22.3 | even strength |
| BUF shot control · low event (<=4) · decided (2+) | 0.067 | 0.63 | 0.37 | 0.00 | 3.44 | 31.0/19.8 | 18.3/28.6 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Travis Sanheim: 1+ goals YES | 6 | 0.105 | 0.093 | +0.041 | +0.029 | $6.34 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 73 | 0.786 | 0.755 | +0.042 | +0.012 | $8.22 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 60 | 0.664 | 0.630 | +0.048 | +0.013 | $2.68 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jiri Kulich: 1+ goals YES | 20 | 0.233 | 0.222 | +0.021 | +0.011 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: higher confidence-adjusted growth (28.71 vs 1.54 bp); despite a smaller raw edge (+0.041 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: MOSTLY_INDEPENDENT (phi 0.106); KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: PHI offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: higher confidence-adjusted growth (1.54 vs 1.53 bp); despite a smaller raw edge (+0.042 vs +0.048/contract); wins across more scripts (relative breadth 1.005 vs 0.89); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.735); KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.168); failure: BUF wins by 2+
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF2|no selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.94 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.106); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.735); KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: BUF wins by 2+
- **Jiri Kulich: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFOPOWER25-1|yes; why: higher confidence-adjusted growth (1.51 vs 0.07 bp); despite a smaller raw edge (+0.021 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: INTENTIONAL_DIVERSIFIER (phi -0.168); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: INTENTIONAL_DIVERSIFIER (phi -0.174); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3069): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no — Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF2|no selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.94 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis GAME:TIGHT (p 0.4406): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4015): highest fidelity KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes (same contract)
- KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4747, phi -0.162)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3357, phi -0.735)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3357, phi -1.0)
- KXNHLGOAL-26OCT21PHIBUF-BUFJKULICH20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3811, phi -0.212)
- override: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF2|no selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV is 0.3 pts higher while thesis capture is 0.94 vs 0.50 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +9.73 (adj +4.61) on $50.00, P(profit) 0.3459, adj growth 33.2 bp · B EV +5.13 (adj +3.22) on $20.91, P(profit) 0.2382, adj growth 27.2 bp · C EV +1.23 (adj +0.43) on $18.59, P(profit) 0.8646, adj growth 3.8 bp · R EV +1.54 (adj +0.97) on $6.00, P(profit) 0.1052, adj growth 30.9 bp

## FLA @ OTT  ·  10000 joint draws  ·  422 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.61 | 0.39 | 0.00 | 5.97 | 26.4/26.3 | 23.4/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.47 | 5.88 | 26.3/26.3 | 23.0/23.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.086 | 0.69 | 0.31 | 0.00 | 6.05 | 31.3/21.0 | 18.3/26.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.61 | 0.39 | 0.00 | 9.22 | 28.3/28.0 | 22.8/21.6 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.54 | 0.46 | 0.48 | 5.91 | 31.5/21.1 | 18.0/28.0 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.058 | 0.69 | 0.31 | 0.00 | 9.27 | 33.6/22.6 | 18.0/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 65 | 0.714 | 0.694 | +0.048 | +0.028 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 10 | 0.129 | 0.119 | +0.023 | +0.013 | $3.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 74 | 0.806 | 0.768 | +0.052 | +0.014 | $17.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Claude Giroux: 1+ goals YES | 18 | 0.220 | 0.203 | +0.029 | +0.013 | $3.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT21FLAOTT-FLASREINHART13-1|no; why: higher confidence-adjusted growth (7.93 vs 2.54 bp); relationships: KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT21FLAOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: FLA offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (3.77 vs 2.46 bp); despite a smaller raw edge (+0.023 vs +0.049/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT21FLAOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT21FLAOTT-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (2.46 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: OTT offense succeeds (4+ goals)
- **Claude Giroux: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no has the higher standalone adjusted growth (2.46 vs 2.43 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.125); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26OCT21FLAOTT-OTTABURAKOVSKY95-1|no: INTENTIONAL_DIVERSIFIER (phi -0.064); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4611): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.4289): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA2|no (same contract)
- thesis OTT:WINS (p 0.5731): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA2|no (same contract)
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3205, phi -0.239)
- KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3554, phi -0.167)
- KXNHLAST-26OCT21FLAOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4289, phi -0.181)
- KXNHLGOAL-26OCT21FLAOTT-OTTCGIROUX28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3554, phi -0.203)

portfolios: A EV +3.78 (adj +1.32) on $50.00, P(profit) 0.6992, adj growth 11.6 bp · B EV +3.97 (adj +1.86) on $44.65, P(profit) 0.6589, adj growth 16.4 bp · C EV +2.21 (adj +1.08) on $31.60, P(profit) 0.5856, adj growth 9.6 bp · R EV +0.36 (adj +0.21) on $5.00, P(profit) 0.714, adj growth 7.6 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
