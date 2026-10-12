# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T22:30:01Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +18.87 | +4.53 | +20.53 | 0.637 | -26.46 | -42.01 | 37.53 |
| B thesis-diversified (joint) ← optimiser card | 84.93 | +13.18 | +7.01 | +5.84 | 0.639 | -35.18 | -41.22 | 62.62 |
| C best expression per thesis | 70.65 | +9.66 | +3.71 | +11.45 | 0.572 | -27.03 | -30.62 | 33.30 |
| R FUNDED research stakes | 6.00 | +1.15 | +0.78 | +0.10 | 0.752 | -6.00 | -6.00 | 0.00 |

## OTT @ NJD  ·  10000 joint draws  ·  470 bet sides mapped, 23 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.521 / away 0.479

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_OTT_win | p_overtime | goals | shots NJD/OTT | NJD/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.47 | 0.53 | 0.00 | 5.95 | 27.5/27.4 | 23.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.48 | 0.52 | 0.45 | 5.88 | 27.5/27.5 | 24.2/24.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.54 | 0.46 | 0.46 | 5.83 | 32.8/22.2 | 18.9/29.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.075 | 0.48 | 0.52 | 0.00 | 5.98 | 32.7/22.1 | 18.7/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.42 | 0.58 | 0.00 | 9.12 | 29.3/29.0 | 22.7/23.8 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.45 | 0.55 | 0.00 | 3.42 | 26.1/26.0 | 24.1/24.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 64 | 0.713 | 0.693 | +0.057 | +0.037 | $15.00 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 72 | 0.863 | 0.767 | +0.129 | +0.033 | $15.31 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 13 | 0.172 | 0.160 | +0.034 | +0.022 | $4.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 73 | 0.780 | 0.766 | +0.036 | +0.022 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJAMANTHA39-1|no; why: higher confidence-adjusted growth (13.46 vs 10.02 bp); despite a smaller raw edge (+0.057 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense succeeds (4+ goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (12.19 vs 0.94 bp); despite a smaller raw edge (+0.129 vs +0.137/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: Player prop expression KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes selected over player prop KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.28 vs 0.48 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: OTT offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.88 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.08.
- thesis NJD:SUPPRESSED (p 0.4609): highest fidelity KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.88 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis OTT:OFFENSE_4PLUS (p 0.3622): highest fidelity KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.4223): highest fidelity KXNHLPTS-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no [DIRECT], best adjusted EV KXNHLPTS-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no (same contract)
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3138, phi -0.247)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3622, phi -0.162)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4223, phi -0.209)
- KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3138, phi -0.206)
- override: Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.88 vs 0.79 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes selected over player prop KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.28 vs 0.48 (FRAGILE vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +10.27 (adj +1.86) on $50.00, P(profit) 0.7324, adj growth 16.6 bp · B EV +5.71 (adj +2.64) on $49.39, P(profit) 0.5656, adj growth 24.6 bp · C EV +4.96 (adj +2.20) on $33.74, P(profit) 0.6029, adj growth 19.6 bp · R EV +0.34 (adj +0.23) on $4.00, P(profit) 0.7127, adj growth 8.4 bp

## VGK @ MIN  ·  10000 joint draws  ·  444 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.495 / away 0.505

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
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (16.82 vs 4.00 bp); despite a smaller raw edge (+0.038 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT12VGKMIN-VGKTCONNELLY24-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: MIN offense suppressed (<= 2 goals)
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

portfolios: A EV +8.60 (adj +2.67) on $50.00, P(profit) 0.5054, adj growth 20.9 bp · B EV +7.46 (adj +4.37) on $35.54, P(profit) 0.3278, adj growth 38.1 bp · C EV +4.70 (adj +1.51) on $36.91, P(profit) 0.6999, adj growth 13.7 bp · R EV +0.80 (adj +0.55) on $2.00, P(profit) 0.1342, adj growth 18.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
