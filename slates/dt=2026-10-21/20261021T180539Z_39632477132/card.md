# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T18:05:39Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +12.19 | +3.89 | +8.21 | 0.655 | -37.52 | -44.58 | 32.03 |
| B thesis-diversified (joint) ← optimiser card | 82.13 | +6.68 | +3.85 | +9.70 | 0.602 | -30.97 | -41.45 | 34.27 |
| C best expression per thesis | 58.50 | +7.46 | +3.11 | +5.25 | 0.612 | -28.02 | -36.95 | 27.84 |
| R FUNDED research stakes | 13.00 | +0.91 | +0.51 | +0.57 | 0.656 | -7.05 | -7.05 | 0.00 |

## PHI @ BUF  ·  10000 joint draws  ·  518 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.625 / away 0.375

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
| Noah Cates: 1+ goals YES | 13 | 0.166 | 0.156 | +0.028 | +0.018 | $4.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Tage Thompson: 1+ goals NO | 61 | 0.656 | 0.644 | +0.030 | +0.017 | $11.62 | FUNDED_RESEARCH | $3 | BUF:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Rasmus Dahlin: 1+ goals NO | 79 | 0.825 | 0.815 | +0.023 | +0.013 | $16.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 19 | 0.224 | 0.213 | +0.023 | +0.012 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes; why: higher confidence-adjusted growth (5.68 vs 2.62 bp); despite a smaller raw edge (+0.028 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT21PHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: PHI offense suppressed (<= 2 goals)
- **Tage Thompson: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT21PHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: BUF offense succeeds (4+ goals)
- **Rasmus Dahlin: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no; why: KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no has the higher standalone adjusted growth (5.68 vs 2.42 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.017); relationships: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: BUF offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes; why: Player prop expression KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.36 vs 0.50 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT21PHIBUF-BUFRDAHLIN26-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts BUF shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3051): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes — Player prop expression KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.36 vs 0.50 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis BUF:SUPPRESSED (p 0.3786): highest fidelity KXNHLTEAMTOTAL-26OCT21PHIBUF-BUF4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no — Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis GAME:TIGHT (p 0.448): highest fidelity KXNHLSPREAD-26OCT21PHIBUF-BUF2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21PHIBUF-BUF2|no (same contract)
- KXNHLGOAL-26OCT21PHIBUF-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4706, phi -0.199)
- KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.261)
- KXNHLGOAL-26OCT21PHIBUF-BUFRDAHLIN26-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4027, phi -0.193)
- KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4706, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT21PHIBUF-BUFTTHOMPSON72-1|no selected over player prop KXNHLAST-26OCT21PHIBUF-BUFRDAHLIN26-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 0.82 vs 0.82 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT21PHIBUF-PHICDVORAK22-1|yes selected over player prop KXNHLAST-26OCT21PHIBUF-PHIDBARKEY86-1|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.36 vs 0.50 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.42 (adj +1.95) on $50.00, P(profit) 0.5157, adj growth 14.7 bp · B EV +2.40 (adj +1.41) on $36.51, P(profit) 0.6626, adj growth 12.3 bp · C EV +4.24 (adj +1.36) on $22.68, P(profit) 0.6938, adj growth 11.8 bp · R EV +0.14 (adj +0.08) on $3.00, P(profit) 0.6565, adj growth 2.8 bp

## FLA @ OTT  ·  10000 joint draws  ·  450 bet sides mapped, 11 +EV candidates, 4 on card

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
| Brady Tkachuk: 1+ goals NO | 64 | 0.722 | 0.701 | +0.066 | +0.044 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 9 | 0.117 | 0.109 | +0.021 | +0.013 | $3.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Florida wins by over 2.5 goals NO | 83 | 0.884 | 0.855 | +0.044 | +0.015 | $18.59 | FUNDED_RESEARCH | $5 | OTT:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 16 | 0.195 | 0.184 | +0.026 | +0.015 | $3.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT21FLAOTT-FLASJONES3-1|no; why: higher confidence-adjusted growth (19.28 vs 4.45 bp); despite a smaller raw edge (+0.066 vs +0.072/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: FLA offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: higher confidence-adjusted growth (4.14 vs 3.81 bp); despite a smaller raw edge (+0.021 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: OTT offense suppressed (<= 2 goals)
- **Florida wins by over 2.5 goals NO** — thesis: OTT wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: Broad expression KXNHLSPREAD-26OCT21FLAOTT-FLA3|no selected over player prop KXNHLAST-26OCT21FLAOTT-FLASJONES3-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.088); KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.09); failure: FLA wins by 2+
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no; why: KXNHLSPREAD-26OCT21FLAOTT-FLA2|no has the higher standalone adjusted growth (3.81 vs 3.31 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.112); relationships: KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: MOSTLY_INDEPENDENT (phi 0.09); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4671): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no — Broad expression KXNHLSPREAD-26OCT21FLAOTT-FLA3|no selected over player prop KXNHLAST-26OCT21FLAOTT-FLASJONES3-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis OTT:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5829): highest fidelity KXNHLSPREAD-26OCT21FLAOTT-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT21FLAOTT-FLA2|no (same contract)
- KXNHLGOAL-26OCT21FLAOTT-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3092, phi -0.232)
- KXNHLGOAL-26OCT21FLAOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.142)
- KXNHLSPREAD-26OCT21FLAOTT-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.21, phi -0.702)
- KXNHLGOAL-26OCT21FLAOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3486, phi -0.195)
- override: Broad expression KXNHLSPREAD-26OCT21FLAOTT-FLA3|no selected over player prop KXNHLAST-26OCT21FLAOTT-FLASJONES3-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.80 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.77 (adj +1.94) on $50.00, P(profit) 0.6632, adj growth 17.3 bp · B EV +4.28 (adj +2.44) on $45.62, P(profit) 0.6934, adj growth 22.0 bp · C EV +3.22 (adj +1.75) on $35.82, P(profit) 0.5942, adj growth 16.0 bp · R EV +0.77 (adj +0.43) on $10.00, P(profit) 0.6559, adj growth 15.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
