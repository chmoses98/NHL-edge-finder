# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T19:54:40Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +19.93 | +3.96 | +21.66 | 0.637 | -40.58 | -57.89 | 27.84 |
| B thesis-diversified (joint) ← optimiser card | 68.44 | +13.00 | +7.10 | +2.53 | 0.527 | -41.82 | -41.82 | 61.82 |
| C best expression per thesis | 46.50 | +6.56 | +2.61 | -0.32 | 0.490 | -20.29 | -26.53 | 23.14 |
| R FUNDED research stakes | 7.00 | +1.13 | +0.86 | +0.51 | 0.736 | -7.00 | -7.00 | 0.00 |

## OTT @ NJD  ·  10000 joint draws  ·  470 bet sides mapped, 19 +EV candidates, 4 on card

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
| Michael Amadio: 1+ goals YES | 13 | 0.172 | 0.160 | +0.034 | +0.022 | $5.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Cody Glass: 1+ goals YES | 11 | 0.150 | 0.137 | +0.033 | +0.020 | $5.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 65 | 0.713 | 0.695 | +0.047 | +0.029 | $19.54 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 72 | 0.863 | 0.760 | +0.129 | +0.026 | $19.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (8.73 vs 7.61 bp); despite a smaller raw edge (+0.034 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: OTT offense suppressed (<= 2 goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (8.62 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJAMANTHA39-1|no; why: KXNHLAST-26OCT12OTTNJ-NJAMANTHA39-1|no has the higher standalone adjusted growth (10.02 vs 8.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.165); relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense succeeds (4+ goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (7.83 vs 0.92 bp); alternative not eligible: confidence-adjusted EV +0.0088 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.08.
- thesis NJD:SUPPRESSED (p 0.4609): highest fidelity KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJAMANTHA39-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3622): highest fidelity KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3138): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4223, phi -0.209)
- KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4609, phi -0.178)
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3138, phi -0.247)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3622, phi -0.162)

portfolios: A EV +11.46 (adj +1.69) on $50.00, P(profit) 0.5755, adj growth 12.3 bp · B EV +7.66 (adj +3.36) on $50.00, P(profit) 0.7165, adj growth 29.8 bp · C EV +3.42 (adj +1.70) on $25.94, P(profit) 0.8656, adj growth 15.2 bp · R EV +0.35 (adj +0.21) on $5.00, P(profit) 0.7127, adj growth 7.7 bp

## VGK @ MIN  ·  10000 joint draws  ·  438 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

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
| Brayden McNabb: 1+ goals YES | 5 | 0.074 | 0.071 | +0.021 | +0.017 | $4.32 | FUNDED_RESEARCH | $2 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Braeden Bowman: 1+ goals YES | 12 | 0.160 | 0.148 | +0.032 | +0.021 | $5.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.134 | 0.126 | +0.028 | +0.019 | $5.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Yakov Trenin: 1+ goals YES | 9 | 0.121 | 0.109 | +0.025 | +0.013 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (12.56 vs 1.07 bp); despite a smaller raw edge (+0.021 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12VGKMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: VGK offense suppressed (<= 2 goals)
- **Braeden Bowman: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (8.58 vs 1.07 bp); despite a smaller raw edge (+0.032 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12VGKMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (8.46 vs 4.00 bp); despite a smaller raw edge (+0.028 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12VGKMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: MIN offense suppressed (<= 2 goals)
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (4.52 vs 4.00 bp); despite a smaller raw edge (+0.025 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.4008): highest fidelity KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT12VGKMIN-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.4346): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes (same contract)
- KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4346, phi -0.135)
- KXNHLGOAL-26OCT12VGKMIN-VGKBBOWMAN42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4346, phi -0.179)
- KXNHLGOAL-26OCT12VGKMIN-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3852, phi -0.171)
- KXNHLGOAL-26OCT12VGKMIN-MINYTRENIN13-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3852, phi -0.13)

portfolios: A EV +8.47 (adj +2.27) on $50.00, P(profit) 0.5817, adj growth 15.5 bp · B EV +5.33 (adj +3.74) on $18.44, P(profit) 0.4098, adj growth 32.0 bp · C EV +3.14 (adj +0.91) on $20.56, P(profit) 0.4526, adj growth 8.0 bp · R EV +0.78 (adj +0.65) on $2.00, P(profit) 0.0742, adj growth 18.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
