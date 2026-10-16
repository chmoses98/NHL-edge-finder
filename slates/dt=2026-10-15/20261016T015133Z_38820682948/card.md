# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-16T01:51:33Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 50.00 | +9.45 | +1.19 | +13.70 | 0.509 | -25.33 | -25.33 | 8.52 |
| B thesis-diversified (joint) ← optimiser card | 33.63 | +4.80 | +2.13 | +10.74 | 0.619 | -12.46 | -33.63 | 19.16 |
| C best expression per thesis | 9.49 | +1.44 | +0.14 | +4.56 | 0.778 | -9.49 | -9.49 | 1.24 |
| R FUNDED research stakes | 4.00 | +0.32 | +0.21 | +1.84 | 0.740 | -4.00 | -4.00 | 0.00 |

## CGY @ VGK  ·  10000 joint draws  ·  472 bet sides mapped, 8 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.710 / away 0.290

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.73 | 0.27 | 0.00 | 6.03 | 28.5/28.0 | 25.5/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.115 | 0.81 | 0.19 | 0.00 | 6.0 | 33.8/22.0 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.55 | 0.45 | 0.46 | 5.89 | 28.4/27.8 | 24.4/24.9 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.60 | 0.40 | 0.44 | 5.88 | 33.8/22.4 | 19.4/30.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 9.23 | 29.9/29.3 | 24.3/22.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.080 | 0.80 | 0.20 | 0.00 | 9.2 | 35.6/23.2 | 19.4/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 67 | 0.740 | 0.721 | +0.054 | +0.036 | $15.90 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 6 | 0.085 | 0.079 | +0.021 | +0.015 | $3.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Trevor Connelly: 1+ assists NO | 65 | 0.777 | 0.688 | +0.111 | +0.022 | $14.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15CGYVGK-VGKMMARNER93-2|no; why: higher confidence-adjusted growth (13.08 vs 1.00 bp); despite a smaller raw edge (+0.055 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi 0.041); failure: VGK offense succeeds (4+ goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15CGYVGK-VGKBMCNABB3-1|yes; why: higher confidence-adjusted growth (7.81 vs 0.00 bp); despite a smaller raw edge (+0.021 vs +0.054/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense suppressed (<= 2 goals)
- **Trevor Connelly: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15CGYVGK-VGKMMARNER93-2|no; why: higher confidence-adjusted growth (4.73 vs 1.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.041); KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, VGK shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VGK:SUPPRESSED (p 0.2881): highest fidelity KXNHLPTS-26OCT15CGYVGK-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15CGYVGK-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:OFFENSE_4PLUS (p 0.5061): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.21)
- KXNHLGOAL-26OCT15CGYVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.2881, phi -0.107)
- KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5061, phi -0.212)

portfolios: A EV +9.45 (adj +1.19) on $50.00, P(profit) 0.5094, adj growth 8.5 bp · B EV +4.80 (adj +2.13) on $33.63, P(profit) 0.6187, adj growth 19.2 bp · C EV +1.44 (adj +0.14) on $9.49, P(profit) 0.7779, adj growth 1.2 bp · R EV +0.32 (adj +0.21) on $4.00, P(profit) 0.74, adj growth 7.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
