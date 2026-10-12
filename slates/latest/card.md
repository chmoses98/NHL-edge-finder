# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T14:51:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 125.24 | +15.61 | +4.52 | +17.25 | 0.685 | -27.75 | -42.99 | 39.34 |
| B thesis-diversified (joint) ← optimiser card | 113.49 | +14.69 | +7.61 | +13.76 | 0.605 | -29.81 | -46.92 | 68.22 |
| C best expression per thesis | 98.93 | +12.95 | +4.79 | +17.08 | 0.631 | -28.43 | -37.41 | 42.66 |
| R FUNDED research stakes | 17.00 | +1.19 | +0.66 | +1.93 | 0.593 | -5.80 | -11.25 | 0.00 |

## FLA @ BUF  ·  10000 joint draws  ·  432 bet sides mapped, 9 +EV candidates, 4 on card


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
| Sandis Vilmanis: 1+ goals YES | 10 | 0.134 | 0.124 | +0.028 | +0.018 | $4.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 69 | 0.747 | 0.731 | +0.042 | +0.026 | $15.32 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Sam Reinhart: 1+ goals NO | 69 | 0.748 | 0.731 | +0.043 | +0.026 | $14.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 71 | 0.782 | 0.743 | +0.057 | +0.019 | $13.07 | FUNDED_RESEARCH | $4 | BUF:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12FLABUF-FLAGFORSLING42-1|yes; why: higher confidence-adjusted growth (7.29 vs 0.00 bp); despite a smaller raw edge (+0.028 vs +0.037/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.131); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no; why: Player prop expression KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.87 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: MOSTLY_INDEPENDENT (phi 0.149); failure: FLA offense succeeds (4+ goals)
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no; why: KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no has the higher standalone adjusted growth (7.35 vs 7.25 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.227); relationships: KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: REINFORCING (phi 0.189); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: BUF wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes; why: higher confidence-adjusted growth (3.97 vs 1.02 bp); wins across more scripts (relative breadth 0.97 vs 0.864); relationships: KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.131); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: REINFORCING (phi 0.189); failure: FLA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no — Player prop expression KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.87 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis BUF:WINS (p 0.5824): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4297): highest fidelity KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4646, phi -0.172)
- KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3157, phi -0.24)
- KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3157, phi -0.253)
- KXNHLSPREAD-26OCT12FLABUF-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -1.0)
- override: Player prop expression KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.87 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.15 (adj +1.55) on $50.00, P(profit) 0.7028, adj growth 13.4 bp · B EV +3.89 (adj +2.14) on $47.11, P(profit) 0.5565, adj growth 19.3 bp · C EV +5.90 (adj +1.58) on $49.21, P(profit) 0.7396, adj growth 14.0 bp · R EV +0.55 (adj +0.25) on $8.00, P(profit) 0.6105, adj growth 9.1 bp

## OTT @ NJD  ·  10000 joint draws  ·  436 bet sides mapped, 14 +EV candidates, 4 on card


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
| Warren Foegele: 1+ goals YES | 11 | 0.161 | 0.147 | +0.044 | +0.030 | $6.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 63 | 0.709 | 0.688 | +0.062 | +0.041 | $18.55 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.176 | 0.162 | +0.038 | +0.024 | $5.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 71 | 0.865 | 0.754 | +0.141 | +0.030 | $18.55 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (18.68 vs 10.69 bp); relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: OTT offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (16.50 vs 5.94 bp); despite a smaller raw edge (+0.062 vs +0.126/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (10.69 vs 7.55 bp); despite a smaller raw edge (+0.038 vs +0.069/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT12OTTNJ-4|no; why: higher confidence-adjusted growth (10.02 vs 0.06 bp); wins across more scripts (relative breadth 0.999 vs 0.352); alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4506): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3517): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5129): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4255, phi -0.182)
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3316, phi -0.233)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4255, phi -0.218)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.0 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3517, phi -0.164)

portfolios: A EV +8.62 (adj +1.88) on $50.00, P(profit) 0.7782, adj growth 17.4 bp · B EV +9.67 (adj +4.80) on $50.00, P(profit) 0.7279, adj growth 43.1 bp · C EV +6.52 (adj +2.91) on $36.48, P(profit) 0.5405, adj growth 26.1 bp · R EV +0.48 (adj +0.32) on $5.00, P(profit) 0.7086, adj growth 11.8 bp

## VGK @ MIN  ·  10000 joint draws  ·  440 bet sides mapped, 2 +EV candidates, 2 on card


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
| Michael McCarron: 1+ goals YES | 9 | 0.115 | 0.107 | +0.019 | +0.011 | $3.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $13.37 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT12VGKMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.32 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.042/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: MIN offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-1|no; why: higher confidence-adjusted growth (2.58 vs 0.93 bp); despite a smaller raw edge (+0.028 vs +0.040/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0096 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.011); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4241): highest fidelity KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no (same contract)
- thesis MIN:OFFENSE_4PLUS (p 0.3972): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3814, phi -0.144)
- KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.228)

portfolios: A EV +1.84 (adj +1.09) on $25.24, P(profit) 0.7563, adj growth 8.6 bp · B EV +1.13 (adj +0.67) on $16.38, P(profit) 0.7563, adj growth 5.8 bp · C EV +0.53 (adj +0.30) on $13.24, P(profit) 0.723, adj growth 2.6 bp · R EV +0.16 (adj +0.09) on $4.00, P(profit) 0.723, adj growth 3.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
