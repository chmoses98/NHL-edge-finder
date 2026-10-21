# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T20:46:02Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +12.85 | +3.89 | +17.13 | 0.617 | -27.37 | -43.21 | 33.20 |
| B thesis-diversified (joint) ← optimiser card | 77.79 | +9.18 | +4.88 | +12.04 | 0.561 | -33.01 | -47.82 | 43.02 |
| C best expression per thesis | 77.66 | +9.93 | +4.14 | +4.73 | 0.669 | -27.56 | -38.06 | 37.13 |
| R FUNDED research stakes | 11.00 | +0.78 | +0.42 | +0.59 | 0.645 | -6.21 | -6.91 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  518 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.633 / away 0.367

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_PHI_win | p_overtime | goals | shots BUF/PHI | BUF/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| BUF shot control · normal event (5-7) · decided (2+) | 0.120 | 0.66 | 0.34 | 0.00 | 5.99 | 32.6/20.8 | 18.1/28.1 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.59 | 0.41 | 0.00 | 6.01 | 27.0/26.6 | 23.4/23.1 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.49 | 5.88 | 32.3/21.0 | 17.8/28.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.53 | 0.47 | 0.47 | 5.88 | 27.0/26.6 | 23.5/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.58 | 0.42 | 0.00 | 9.24 | 28.6/28.1 | 22.5/21.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.066 | 0.65 | 0.35 | 0.00 | 9.19 | 34.0/22.4 | 17.7/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Noah Cates: 1+ goals YES | 13 | 0.166 | 0.156 | +0.028 | +0.018 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Sean Couturier: 1+ goals YES | 14 | 0.173 | 0.162 | +0.025 | +0.014 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Buffalo wins by over 2.5 goals NO | 72 | 0.785 | 0.750 | +0.051 | +0.016 | $10.62 | FUNDED_RESEARCH | $3 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tage Thompson: 1+ goals NO | 61 | 0.656 | 0.642 | +0.030 | +0.016 | $9.28 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT21PHIBUF-PHISCOUTURIER14-1|yes; why: higher confidence-adjusted growth (5.68 vs 3.24 bp); relationships: KXNHLGOAL-26OCT21PHIBUF-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: PHI offense suppressed (<= 2 goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes has the higher standalone adjusted growth (5.68 vs 3.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.024); they share one thesis budget; relationships: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: PHI offense suppressed (<= 2 goals)
- **Buffalo wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT21PHIBUF-BUF2|no; why: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF3|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.105); KXNHLGOAL-26OCT21PHIBUF-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.119); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: REINFORCING (phi 0.168); failure: BUF wins by 2+
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT21PHIBUF-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: REINFORCING (phi 0.168); failure: BUF offense succeeds (4+ goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3051): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:SUPPRESSED (p 0.3786): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no — Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:TIGHT (p 0.448): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF3|no (same contract)
- KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4706, phi -0.199)
- KXNHLGOAL-26OCT21PHIBUF-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4706, phi -0.227)
- KXNHLSPREAD-26OCT21PHIBUF-BUF3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:WINS_BY_2PLUS (p 0.3313, phi -0.743)
- KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.261)
- override: Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-2|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.82 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLSPREAD-26OCT21PHIBUF-BUF3|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 1.00 vs 0.82 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +7.46 (adj +2.01) on $50.00, P(profit) 0.5953, adj growth 16.3 bp · B EV +2.65 (adj +1.36) on $27.79, P(profit) 0.6584, adj growth 11.8 bp · C EV +4.45 (adj +1.44) on $27.66, P(profit) 0.6025, adj growth 12.5 bp · R EV +0.35 (adj +0.14) on $6.00, P(profit) 0.5484, adj growth 4.9 bp

## FLA @ OTT  ·  10000 joint draws  ·  462 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.504 / away 0.496

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_FLA_win | p_overtime | goals | shots OTT/FLA | OTT/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.62 | 0.38 | 0.00 | 6.0 | 26.3/26.1 | 23.2/22.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.46 | 5.92 | 26.9/26.7 | 23.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.65 | 0.35 | 0.00 | 9.23 | 28.1/27.9 | 22.7/21.4 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.087 | 0.68 | 0.32 | 0.00 | 5.96 | 31.4/20.9 | 18.4/27.0 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.58 | 0.42 | 0.46 | 5.86 | 31.6/21.1 | 17.9/28.3 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.058 | 0.50 | 0.50 | 0.48 | 2.8 | 25.0/24.8 | 23.3/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brady Tkachuk: 1+ goals NO | 65 | 0.723 | 0.703 | +0.057 | +0.037 | $19.96 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $7.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Jake Sanderson: 1+ assists NO | 58 | 0.671 | 0.623 | +0.074 | +0.026 | $19.34 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 9 | 0.117 | 0.109 | +0.021 | +0.013 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (13.92 vs 3.81 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: FLA offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (9.20 vs 3.81 bp); despite a smaller raw edge (+0.036 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense suppressed (<= 2 goals)
- **Jake Sanderson: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT21FLAOTT-OTTJSANDERSON85-1|no; why: higher confidence-adjusted growth (6.23 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes has the higher standalone adjusted growth (9.20 vs 4.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.004); they share one thesis budget; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4671): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.3486): highest fidelity KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no (same contract)
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3092, phi -0.233)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.195)
- KXNHLAST-26OCT21FLAOTT-OTTJSANDERSON85-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.424, phi -0.252)
- KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.142)

portfolios: A EV +5.39 (adj +1.88) on $50.00, P(profit) 0.6608, adj growth 16.9 bp · B EV +6.53 (adj +3.52) on $50.00, P(profit) 0.6203, adj growth 31.2 bp · C EV +5.48 (adj +2.70) on $50.00, P(profit) 0.5943, adj growth 24.6 bp · R EV +0.43 (adj +0.28) on $5.00, P(profit) 0.7229, adj growth 10.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
