# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T13:10:54Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 130.00 | +16.03 | +3.32 | +18.23 | 0.691 | -30.91 | -49.41 | 26.57 |
| B thesis-diversified (joint) ← optimiser card | 95.28 | +11.68 | +4.29 | +15.41 | 0.600 | -28.14 | -37.88 | 38.61 |
| C best expression per thesis | 72.96 | +7.85 | +2.83 | +6.46 | 0.678 | -23.69 | -29.61 | 25.43 |
| R FUNDED research stakes | 12.00 | +1.05 | +0.50 | +2.64 | 0.557 | -5.10 | -12.00 | 0.00 |

## FLA @ BUF  ·  10000 joint draws  ·  98 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_FLA_win | p_overtime | goals | shots BUF/FLA | BUF/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.62 | 0.38 | 0.00 | 5.99 | 27.2/27.1 | 24.0/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.53 | 0.47 | 0.48 | 5.95 | 27.2/27.0 | 23.8/23.9 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.094 | 0.68 | 0.32 | 0.00 | 6.02 | 32.3/21.5 | 18.8/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.61 | 0.39 | 0.00 | 9.32 | 28.7/28.4 | 23.0/22.0 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.47 | 5.89 | 32.5/21.5 | 18.4/29.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.60 | 0.40 | 0.00 | 3.48 | 26.0/25.8 | 24.1/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Florida wins by over 1.5 goals NO | 71 | 0.782 | 0.743 | +0.057 | +0.019 | $16.18 | FUNDED_RESEARCH | $5 | BUF:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Buffalo over 2.5 goals scored YES | 59 | 0.660 | 0.622 | +0.053 | +0.015 | $4.34 | FUNDED_RESEARCH | $2 | BUF:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Florida wins by over 1.5 goals NO** — thesis: BUF wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes; why: higher confidence-adjusted growth (3.97 vs 2.17 bp); wins across more scripts (relative breadth 0.97 vs 0.864); relationships: KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes: REINFORCING (phi 0.475); failure: FLA wins by 2+
- **Buffalo over 2.5 goals scored YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT12FLABUF-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT12FLABUF-FLA2|no has the higher standalone adjusted growth (3.97 vs 2.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.475); they share one thesis budget; relationships: KXNHLSPREAD-26OCT12FLABUF-FLA2|no: REINFORCING (phi 0.475); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis BUF:WINS (p 0.5824): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4297): highest fidelity KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26OCT12FLABUF-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -1.0)
- KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis BUF:SUPPRESSED (p 0.3513, phi -0.976)

portfolios: A EV +3.32 (adj +1.03) on $40.00, P(profit) 0.6086, adj growth 7.6 bp · B EV +1.66 (adj +0.53) on $20.52, P(profit) 0.7818, adj growth 4.7 bp · C EV +1.51 (adj +0.50) on $19.01, P(profit) 0.7818, adj growth 4.4 bp · R EV +0.57 (adj +0.18) on $7.00, P(profit) 0.6086, adj growth 6.1 bp

## OTT @ NJD  ·  10000 joint draws  ·  424 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_OTT_win | p_overtime | goals | shots NJD/OTT | NJD/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.46 | 0.54 | 0.00 | 5.96 | 27.6/27.4 | 23.8/24.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.49 | 0.51 | 0.50 | 5.89 | 27.8/27.7 | 24.4/24.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.079 | 0.56 | 0.44 | 0.00 | 5.96 | 32.9/22.1 | 18.8/28.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.47 | 0.53 | 0.00 | 9.12 | 29.0/29.1 | 23.2/23.4 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.52 | 0.48 | 0.48 | 5.77 | 32.7/22.2 | 19.0/29.3 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 3.43 | 26.5/26.3 | 24.4/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 63 | 0.709 | 0.688 | +0.062 | +0.041 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Warren Foegele: 1+ goals YES | 12 | 0.161 | 0.148 | +0.034 | +0.021 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 72 | 0.865 | 0.761 | +0.131 | +0.027 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Michael Amadio: 1+ goals YES | 13 | 0.176 | 0.153 | +0.038 | +0.016 | $4.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no; why: higher confidence-adjusted growth (16.50 vs 3.73 bp); relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NJD offense succeeds (4+ goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (8.36 vs 4.40 bp); despite a smaller raw edge (+0.034 vs +0.038/contract); relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (8.19 vs 0.12 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0036 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: OTT offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (4.40 vs 3.55 bp); despite a smaller raw edge (+0.038 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4506): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3517): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5129): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3316, phi -0.233)
- KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4255, phi -0.182)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3517, phi -0.164)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4255, phi -0.218)

portfolios: A EV +8.16 (adj +1.49) on $50.00, P(profit) 0.7782, adj growth 13.4 bp · B EV +8.09 (adj +3.38) on $49.64, P(profit) 0.7224, adj growth 30.5 bp · C EV +5.32 (adj +2.09) on $33.95, P(profit) 0.5225, adj growth 18.9 bp · R EV +0.48 (adj +0.32) on $5.00, P(profit) 0.7086, adj growth 11.8 bp

## VGK @ MIN  ·  10000 joint draws  ·  384 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_VGK_win | p_overtime | goals | shots MIN/VGK | MIN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.02 | 28.5/28.7 | 25.3/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.47 | 5.92 | 28.7/28.8 | 25.5/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.19 | 30.0/30.1 | 24.4/23.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 6.02 | 22.5/33.5 | 29.9/19.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.47 | 0.53 | 0.45 | 5.89 | 23.1/34.0 | 30.7/19.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.54 | 0.46 | 0.00 | 3.48 | 27.4/27.4 | 25.4/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 2+ assists NO | 86 | 0.913 | 0.879 | +0.044 | +0.010 | $19.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ assists NO | 51 | 0.621 | 0.542 | +0.093 | +0.015 | $5.14 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
- **Mitch Marner: 2+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (2.10 vs 1.91 bp); despite a smaller raw edge (+0.044 vs +0.093/contract); relationships: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: DUPLICATIVE (phi 0.396); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no; why: second expression of the same thesis: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no has the higher standalone adjusted growth (2.10 vs 1.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.396); they share one thesis budget; relationships: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no: DUPLICATIVE (phi 0.396); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4241): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.259)
- KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.1 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.279)

portfolios: A EV +4.55 (adj +0.80) on $40.00, P(profit) 0.6207, adj growth 5.6 bp · B EV +1.93 (adj +0.38) on $25.12, P(profit) 0.6207, adj growth 3.4 bp · C EV +1.02 (adj +0.24) on $20.00, P(profit) 0.9127, adj growth 2.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
