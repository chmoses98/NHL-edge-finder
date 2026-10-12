# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T23:28:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +7.93 | +2.27 | +11.97 | 0.505 | -32.88 | -32.88 | 17.25 |
| B thesis-diversified (joint) ← optimiser card | 35.54 | +7.46 | +4.37 | -8.65 | 0.328 | -35.54 | -35.54 | 38.06 |
| C best expression per thesis | 37.07 | +4.53 | +1.49 | +2.53 | 0.701 | -14.93 | -24.36 | 13.50 |
| R FUNDED research stakes | 2.00 | +0.80 | +0.55 | -2.00 | 0.134 | -2.00 | -2.00 | 0.00 |

## VGK @ MIN  ·  10000 joint draws  ·  444 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.500 / away 0.500

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_VGK_win | p_overtime | goals | shots MIN/VGK | MIN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.57 | 0.43 | 0.00 | 6.03 | 28.3/28.5 | 25.3/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.89 | 28.4/28.7 | 25.4/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.087 | 0.57 | 0.43 | 0.00 | 9.17 | 29.8/30.1 | 24.5/23.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.075 | 0.50 | 0.50 | 0.00 | 6.0 | 22.8/34.0 | 30.0/19.5 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.48 | 0.52 | 0.44 | 5.87 | 23.0/34.2 | 30.8/19.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.64 | 0.36 | 0.00 | 5.96 | 32.9/22.7 | 19.7/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Rieger Lorenz: 1+ goals YES | 9 | 0.134 | 0.122 | +0.038 | +0.026 | $6.52 | FUNDED_RESEARCH | $2 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 73 | 0.823 | 0.774 | +0.079 | +0.030 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Braeden Bowman: 1+ goals YES | 12 | 0.160 | 0.148 | +0.032 | +0.021 | $5.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.074 | 0.067 | +0.021 | +0.014 | $3.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes; why: higher confidence-adjusted growth (16.82 vs 3.81 bp); despite a smaller raw edge (+0.038 vs +0.061/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: MIN offense suppressed (<= 2 goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (10.39 vs 2.96 bp); relationships: KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.026); failure: VGK offense succeeds (4+ goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (8.58 vs 1.07 bp); despite a smaller raw edge (+0.032 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (7.77 vs 1.07 bp); despite a smaller raw edge (+0.021 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.026); KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4346): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.4008): highest fidelity KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes (same contract)
- thesis MIN:SUPPRESSED (p 0.3852): highest fidelity KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no (same contract)
- KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3852, phi -0.171)
- KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3446, phi -0.192)
- KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4346, phi -0.179)
- KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4346, phi -0.135)

portfolios: A EV +7.93 (adj +2.27) on $50.00, P(profit) 0.5054, adj growth 17.2 bp · B EV +7.46 (adj +4.37) on $35.54, P(profit) 0.3278, adj growth 38.1 bp · C EV +4.53 (adj +1.49) on $37.07, P(profit) 0.7009, adj growth 13.5 bp · R EV +0.80 (adj +0.55) on $2.00, P(profit) 0.1342, adj growth 18.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
