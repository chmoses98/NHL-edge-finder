# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T14:01:45Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +21.82 | +4.41 | +23.23 | 0.716 | -29.85 | -45.97 | 36.92 |
| B thesis-diversified (joint) ← optimiser card | 123.89 | +14.14 | +6.56 | +14.06 | 0.656 | -29.97 | -40.90 | 59.55 |
| C best expression per thesis | 103.09 | +10.97 | +4.93 | +11.67 | 0.603 | -28.81 | -40.42 | 44.33 |
| R FUNDED research stakes | 15.00 | +1.14 | +0.67 | +2.63 | 0.589 | -6.54 | -9.25 | 0.00 |

## FLA @ BUF  ·  10000 joint draws  ·  412 bet sides mapped, 10 +EV candidates, 4 on card


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
| Sam Reinhart: 1+ goals NO | 68 | 0.748 | 0.730 | +0.053 | +0.035 | $15.00 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 68 | 0.747 | 0.729 | +0.051 | +0.034 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 71 | 0.782 | 0.743 | +0.057 | +0.019 | $10.32 | FUNDED_RESEARCH | $3 | BUF:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Zach Benson: 1+ goals YES | 23 | 0.269 | 0.257 | +0.027 | +0.015 | $3.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (12.51 vs 11.65 bp); relationships: KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: REINFORCING (phi 0.189); KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no has the higher standalone adjusted growth (12.51 vs 11.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: BUF wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes; why: higher confidence-adjusted growth (3.97 vs 1.02 bp); wins across more scripts (relative breadth 0.97 vs 0.864); relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: REINFORCING (phi 0.189); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.125); failure: FLA wins by 2+
- **Zach Benson: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT12FLABUF-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT12FLABUF-FLA2|no has the higher standalone adjusted growth (3.97 vs 2.52 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.125); they share one thesis budget; relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: MOSTLY_INDEPENDENT (phi 0.125); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4646): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:WINS (p 0.5824): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4297): highest fidelity KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3157, phi -0.253)
- KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3157, phi -0.24)
- KXNHLSPREAD-26OCT12FLABUF-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2182, phi -1.0)
- KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3513, phi -0.223)

portfolios: A EV +8.71 (adj +1.37) on $50.00, P(profit) 0.624, adj growth 10.3 bp · B EV +3.47 (adj +1.96) on $43.89, P(profit) 0.5754, adj growth 18.0 bp · C EV +3.20 (adj +1.61) on $46.61, P(profit) 0.6188, adj growth 14.4 bp · R EV +0.54 (adj +0.28) on $7.00, P(profit) 0.6188, adj growth 10.2 bp

## OTT @ NJD  ·  10000 joint draws  ·  424 bet sides mapped, 15 +EV candidates, 4 on card


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
| Jack Hughes: 1+ goals NO | 63 | 0.709 | 0.688 | +0.062 | +0.041 | $19.25 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.176 | 0.162 | +0.038 | +0.024 | $6.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Warren Foegele: 1+ goals YES | 12 | 0.161 | 0.148 | +0.034 | +0.021 | $5.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Andre Burakovsky: 1+ assists NO | 72 | 0.865 | 0.761 | +0.131 | +0.027 | $19.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (16.50 vs 5.94 bp); despite a smaller raw edge (+0.062 vs +0.126/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (10.69 vs 3.55 bp); despite a smaller raw edge (+0.038 vs +0.059/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: OTT offense suppressed (<= 2 goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (10.69 vs 8.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (8.19 vs 0.86 bp); despite a smaller raw edge (+0.131 vs +0.135/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0097 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: OTT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.4506): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3517): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5129): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3316, phi -0.233)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4255, phi -0.218)
- KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4255, phi -0.182)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.0 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3517, phi -0.164)

portfolios: A EV +8.46 (adj +1.76) on $50.00, P(profit) 0.7782, adj growth 16.2 bp · B EV +8.41 (adj +3.90) on $50.00, P(profit) 0.7224, adj growth 35.1 bp · C EV +6.52 (adj +2.91) on $36.48, P(profit) 0.5405, adj growth 26.1 bp · R EV +0.48 (adj +0.32) on $5.00, P(profit) 0.7086, adj growth 11.8 bp

## VGK @ MIN  ·  10000 joint draws  ·  388 bet sides mapped, 3 +EV candidates, 3 on card


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
| Mitch Marner: 2+ assists NO | 85 | 0.913 | 0.876 | +0.054 | +0.017 | $16.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.98) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ assists NO | 51 | 0.621 | 0.545 | +0.093 | +0.018 | $5.13 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Jack Eichel: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $8.86 | FUNDED_RESEARCH | $3 | VGK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 2+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (5.55 vs 2.85 bp); despite a smaller raw edge (+0.054 vs +0.093/contract); relationships: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: DUPLICATIVE (phi 0.396); KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.067); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no; why: second expression of the same thesis: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no has the higher standalone adjusted growth (5.55 vs 2.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.396); they share one thesis budget; relationships: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no: DUPLICATIVE (phi 0.396); KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.086); failure: VGK offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no; why: second expression of the same thesis: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no has the higher standalone adjusted growth (5.55 vs 2.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.067); they share one thesis budget; relationships: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no: MOSTLY_INDEPENDENT (phi 0.067); KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.086); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4241): highest fidelity KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 2% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.259)
- KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.6 pts; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.279)
- KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.228)

portfolios: A EV +4.65 (adj +1.28) on $50.00, P(profit) 0.6207, adj growth 10.4 bp · B EV +2.26 (adj +0.70) on $30.00, P(profit) 0.6683, adj growth 6.4 bp · C EV +1.25 (adj +0.41) on $20.00, P(profit) 0.9127, adj growth 3.8 bp · R EV +0.12 (adj +0.07) on $3.00, P(profit) 0.723, adj growth 2.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
