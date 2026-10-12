# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T17:17:25Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 100.00 | +17.41 | +4.79 | +18.61 | 0.628 | -35.25 | -52.28 | 38.74 |
| B thesis-diversified (joint) ← optimiser card | 78.05 | +12.35 | +5.94 | +8.63 | 0.521 | -30.89 | -39.97 | 52.28 |
| C best expression per thesis | 64.48 | +6.68 | +3.08 | +4.93 | 0.627 | -28.16 | -34.00 | 27.24 |
| R FUNDED research stakes | 7.00 | +1.21 | +0.93 | +0.62 | 0.736 | -7.00 | -7.00 | 0.00 |

## OTT @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 17 +EV candidates, 4 on card

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
| Jack Hughes: 1+ goals NO | 64 | 0.713 | 0.693 | +0.057 | +0.037 | $19.67 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.172 | 0.160 | +0.034 | +0.022 | $5.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 72 | 0.863 | 0.760 | +0.129 | +0.026 | $19.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 11 | 0.150 | 0.136 | +0.033 | +0.019 | $4.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (13.46 vs 6.53 bp); despite a smaller raw edge (+0.057 vs +0.129/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: NJD offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (8.73 vs 7.61 bp); despite a smaller raw edge (+0.034 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTCYAKEMCHUK26-1|no; why: higher confidence-adjusted growth (7.83 vs 1.52 bp); relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: OTT offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (7.60 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.08.
- thesis NJD:SUPPRESSED (p 0.4609): highest fidelity KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5309): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3622): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3138, phi -0.247)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4223, phi -0.209)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3622, phi -0.162)
- KXNHLGOAL-26OCT12OTTNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4609, phi -0.178)

portfolios: A EV +10.92 (adj +2.77) on $50.00, P(profit) 0.6224, adj growth 23.8 bp · B EV +7.94 (adj +3.54) on $50.00, P(profit) 0.7165, adj growth 31.7 bp · C EV +4.08 (adj +2.31) on $40.54, P(profit) 0.6439, adj growth 20.5 bp · R EV +0.43 (adj +0.28) on $5.00, P(profit) 0.7127, adj growth 10.4 bp

## VGK @ MIN  ·  10000 joint draws  ·  438 bet sides mapped, 6 +EV candidates, 4 on card

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
| Brayden McNabb: 1+ goals YES | 5 | 0.074 | 0.071 | +0.021 | +0.017 | $4.44 | FUNDED_RESEARCH | $2 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 53 | 0.607 | 0.566 | +0.059 | +0.018 | $11.15 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
| Michael McCarron: 1+ goals YES | 9 | 0.113 | 0.106 | +0.017 | +0.010 | $2.76 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Kirill Kaprizov: 1+ assists NO | 53 | 0.603 | 0.564 | +0.055 | +0.016 | $9.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (12.56 vs 1.07 bp); despite a smaller raw edge (+0.021 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (2.96 vs 0.97 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0092 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.057); KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense succeeds (4+ goals)
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT12VGKMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (2.63 vs 0.78 bp); alternative not eligible: confidence-adjusted EV +0.0077 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no: MOSTLY_INDEPENDENT (phi -0.046); failure: MIN offense suppressed (<= 2 goals)
- **Kirill Kaprizov: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (2.37 vs 0.31 bp); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.046); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4346): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no (same contract)
- thesis MIN:SUPPRESSED (p 0.3852): highest fidelity KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3446): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes (same contract)
- KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4346, phi -0.135)
- KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3446, phi -0.27)
- KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3852, phi -0.152)
- KXNHLAST-26OCT12VGKMIN-MINKKAPRIZOV97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.4008, phi -0.293)

portfolios: A EV +6.48 (adj +2.02) on $50.00, P(profit) 0.6013, adj growth 14.9 bp · B EV +4.42 (adj +2.40) on $28.05, P(profit) 0.4867, adj growth 20.6 bp · C EV +2.60 (adj +0.77) on $23.94, P(profit) 0.5374, adj growth 6.7 bp · R EV +0.78 (adj +0.65) on $2.00, P(profit) 0.0742, adj growth 18.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
