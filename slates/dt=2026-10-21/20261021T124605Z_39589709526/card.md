# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T12:46:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 98.28 | +32.87 | +10.59 | +3.02 | 0.523 | -56.29 | -78.10 | 53.17 |
| B thesis-diversified (joint) ← optimiser card | 58.55 | +10.58 | +4.11 | +12.55 | 0.605 | -28.08 | -43.97 | 36.08 |
| C best expression per thesis | 54.64 | +8.26 | +2.99 | +16.46 | 0.574 | -14.03 | -30.55 | 26.58 |
| R FUNDED research stakes | 15.00 | +3.39 | +1.23 | +3.74 | 0.578 | -7.38 | -10.69 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  380 bet sides mapped, 3 +EV candidates, 3 on card


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
| Travis Sanheim: 1+ goals YES | 7 | 0.105 | 0.091 | +0.031 | +0.017 | $3.75 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 73 | 0.786 | 0.755 | +0.042 | +0.012 | $7.29 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo wins by over 1.5 goals NO | 60 | 0.664 | 0.630 | +0.048 | +0.013 | $2.95 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Travis Sanheim: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: higher confidence-adjusted growth (8.78 vs 1.54 bp); despite a smaller raw edge (+0.031 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: MOSTLY_INDEPENDENT (phi 0.083); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: MOSTLY_INDEPENDENT (phi 0.106); failure: PHI offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: higher confidence-adjusted growth (1.54 vs 1.53 bp); despite a smaller raw edge (+0.042 vs +0.048/contract); wins across more scripts (relative breadth 1.005 vs 0.89); relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.083); KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: DUPLICATIVE (phi 0.735); failure: BUF wins by 2+
- **Buffalo wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT21PHIBUF-BUF3|no has the higher standalone adjusted growth (1.54 vs 1.53 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.735); they share one thesis budget; relationships: KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.106); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: DUPLICATIVE (phi 0.735); failure: BUF wins by 2+

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.3069): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4406): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- KXNHLGOAL-26OCT21PHIBUF-PHITSANHEIM6-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4747, phi -0.162)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3357, phi -0.735)
- KXNHLSPREAD-26OCT21PHIBUF-BUF2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3357, phi -1.0)

portfolios: A EV +6.07 (adj +2.60) on $48.28, P(profit) 0.6842, adj growth 16.6 bp · B EV +2.18 (adj +1.02) on $13.99, P(profit) 0.6842, adj growth 8.8 bp · C EV +0.69 (adj +0.19) on $12.29, P(profit) 0.7857, adj growth 1.7 bp · R EV +0.60 (adj +0.28) on $4.00, P(profit) 0.6842, adj growth 9.4 bp

## FLA @ OTT  ·  10000 joint draws  ·  398 bet sides mapped, 9 +EV candidates, 4 on card


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
| Florida wins 1st Period by over 1.5 goals YES | 3 | 0.097 | 0.050 | +0.065 | +0.018 | $2.46 | FUNDED_RESEARCH | $1 | FLA:SCORES_FIRST | FRAGILE (0.20) | EVIDENCE_THIN | D |
| Brady Tkachuk: 1+ goals NO | 64 | 0.714 | 0.693 | +0.058 | +0.037 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 72 | 0.783 | 0.749 | +0.049 | +0.015 | $19.12 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 16 | 0.192 | 0.180 | +0.023 | +0.011 | $2.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Florida wins 1st Period by over 1.5 goals YES** — thesis: FLA scores first; alternative: KXNHLFIRSTGOAL-26OCT21FLAOTT-FLASBENNETT9|yes; why: higher confidence-adjusted growth (21.63 vs 0.00 bp); evidence EVIDENCE_THIN vs EVIDENCE_MIXED; alternative not eligible: raw EV <= 0 at the executable ask, confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.279); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.035); failure: OTT scores first
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: higher confidence-adjusted growth (13.26 vs 3.30 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.075); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no has the higher standalone adjusted growth (3.30 vs 2.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.719); relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: INTENTIONAL_DIVERSIFIER (phi -0.279); KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.114); failure: FLA wins by 2+
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA3|no; why: Player prop expression KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes selected over broad KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.28 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: MOSTLY_INDEPENDENT (phi 0.114); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SCORES_FIRST (p 0.4575): highest fidelity KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes [FRAGILE], best adjusted EV KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes (same contract)
- thesis FLA:SUPPRESSED (p 0.4611): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5731): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-OTT2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHL1PSPREAD-26OCT21FLAOTT-FLA2|yes: FUNDED_RESEARCH; family MIXED; loses 80% of the draws where the thesis happens; opposing: failure thesis OTT:SCORES_FIRST (p 0.5412, phi -0.323)
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3205, phi -0.239)
- KXNHLSPREAD-26OCT21FLAOTT-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2172, phi -1.0)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3554, phi -0.194)
- override: Player prop expression KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes selected over broad KXNHLTEAMTOTAL-26OCT21FLAOTT-OTT5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.28 vs 0.57 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +26.80 (adj +7.99) on $50.00, P(profit) 0.4387, adj growth 36.6 bp · B EV +8.40 (adj +3.09) on $44.56, P(profit) 0.6661, adj growth 27.3 bp · C EV +7.57 (adj +2.80) on $42.35, P(profit) 0.7022, adj growth 24.9 bp · R EV +2.79 (adj +0.95) on $11.00, P(profit) 0.6556, adj growth 31.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
