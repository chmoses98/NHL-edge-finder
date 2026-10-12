# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T16:29:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.83 | +6.12 | +25.92 | 0.715 | -34.78 | -50.04 | 51.36 |
| B thesis-diversified (joint) ← optimiser card | 124.76 | +16.92 | +8.48 | +14.49 | 0.601 | -35.40 | -49.02 | 75.11 |
| C best expression per thesis | 82.51 | +13.18 | +5.23 | +15.18 | 0.659 | -27.94 | -39.90 | 46.27 |
| R FUNDED research stakes | 13.00 | +0.72 | +0.46 | -0.52 | 0.455 | -6.28 | -7.62 | 0.00 |

## FLA @ BUF  ·  10000 joint draws  ·  440 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.511 / away 0.489

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_FLA_win | p_overtime | goals | shots BUF/FLA | BUF/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.61 | 0.39 | 0.00 | 5.96 | 27.1/26.9 | 23.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.51 | 0.49 | 0.48 | 5.89 | 27.2/27.0 | 23.8/24.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.092 | 0.67 | 0.33 | 0.00 | 5.98 | 32.0/21.5 | 18.8/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.62 | 0.38 | 0.00 | 9.18 | 28.7/28.5 | 23.4/21.8 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.56 | 0.44 | 0.47 | 5.88 | 32.4/21.6 | 18.5/28.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.056 | 0.60 | 0.40 | 0.00 | 3.45 | 25.9/25.6 | 24.0/23.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 68 | 0.759 | 0.738 | +0.064 | +0.043 | $15.00 | FUNDED_RESEARCH | $4 | FLA:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.137 | 0.126 | +0.031 | +0.019 | $4.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 69 | 0.748 | 0.732 | +0.043 | +0.027 | $15.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Josh Norris: 1+ goals YES | 19 | 0.228 | 0.217 | +0.027 | +0.017 | $5.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (18.86 vs 12.67 bp); despite a smaller raw edge (+0.064 vs +0.145/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: FLA offense succeeds (4+ goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12FLABUF-FLACVERHAEGHE23-1|yes; why: higher confidence-adjusted growth (8.31 vs 0.66 bp); despite a smaller raw edge (+0.031 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0081 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no; why: Player prop expression KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.86 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: FLA offense succeeds (4+ goals)
- **Josh Norris: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes; why: KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes has the higher standalone adjusted growth (3.73 vs 3.71 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.004); relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4581): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no — Player prop expression KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.86 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis BUF:OFFENSE_4PLUS (p 0.4271): highest fidelity KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT12FLABUF-BUFZBENSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:WINS (p 0.576): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3236, phi -0.225)
- KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4581, phi -0.194)
- KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3236, phi -0.223)
- KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3483, phi -0.216)
- override: Player prop expression KXNHLGOAL-26OCT12FLABUF-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no because adjusted EV differs by only 0.9 pts while thesis capture is 0.86 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +8.99 (adj +2.01) on $50.00, P(profit) 0.6867, adj growth 17.2 bp · B EV +4.41 (adj +2.80) on $40.02, P(profit) 0.7033, adj growth 25.4 bp · C EV +3.24 (adj +1.85) on $36.14, P(profit) 0.6919, adj growth 16.8 bp · R EV +0.37 (adj +0.24) on $4.00, P(profit) 0.7587, adj growth 9.3 bp

## OTT @ NJD  ·  10000 joint draws  ·  438 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.539 / away 0.461

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_OTT_win | p_overtime | goals | shots NJD/OTT | NJD/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.48 | 0.52 | 0.00 | 5.99 | 27.6/27.6 | 23.9/24.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.50 | 0.50 | 0.48 | 5.9 | 27.7/27.8 | 24.4/24.4 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.079 | 0.46 | 0.54 | 0.00 | 5.93 | 32.4/22.0 | 18.4/29.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.46 | 0.54 | 0.00 | 9.11 | 29.2/29.2 | 22.9/23.5 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.48 | 5.88 | 32.5/22.0 | 18.8/29.0 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.069 | 0.50 | 0.50 | 0.47 | 2.78 | 26.0/25.9 | 24.4/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael Amadio: 1+ goals YES | 13 | 0.174 | 0.162 | +0.036 | +0.024 | $5.55 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Jordan Spence: 1+ assists YES | 24 | 0.321 | 0.278 | +0.068 | +0.025 | $6.51 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Andre Burakovsky: 1+ assists NO | 72 | 0.864 | 0.757 | +0.130 | +0.023 | $18.97 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Timo Meier: 1+ goals NO | 73 | 0.779 | 0.765 | +0.035 | +0.022 | $18.97 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (10.08 vs 7.20 bp); despite a smaller raw edge (+0.036 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.007); failure: OTT offense suppressed (<= 2 goals)
- **Jordan Spence: 1+ assists YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes has the higher standalone adjusted growth (10.08 vs 7.20 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.093); they share one thesis budget; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.093); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: OTT offense suppressed (<= 2 goals)
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no; why: higher confidence-adjusted growth (6.14 vs 0.64 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: OTT offense succeeds (4+ goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no; why: Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi 0.012); failure: NJD offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis OTT:OFFENSE_4PLUS (p 0.359): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:WINS (p 0.5306): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.4625): highest fidelity KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no — Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4185, phi -0.204)
- KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4185, phi -0.272)
- KXNHLAST-26OCT12OTTNJ-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 7% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.4 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.359, phi -0.15)
- KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3218, phi -0.223)
- override: Player prop expression KXNHLGOAL-26OCT12OTTNJ-NJTMEIER28-1|no selected over player prop KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.88 vs 0.80 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +10.81 (adj +2.60) on $50.00, P(profit) 0.619, adj growth 22.2 bp · B EV +7.44 (adj +2.75) on $50.00, P(profit) 0.8056, adj growth 24.5 bp · C EV +7.28 (adj +2.53) on $27.75, P(profit) 0.7014, adj growth 22.0 bp · R EV +0.24 (adj +0.15) on $5.00, P(profit) 0.779, adj growth 5.2 bp

## VGK @ MIN  ·  10000 joint draws  ·  436 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.504 / away 0.496

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_VGK_win | p_overtime | goals | shots MIN/VGK | MIN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.03 | 28.4/28.6 | 25.3/24.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.51 | 0.49 | 0.47 | 5.89 | 28.3/28.6 | 25.3/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.57 | 0.43 | 0.00 | 9.22 | 29.8/30.2 | 24.6/23.1 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 5.99 | 22.8/33.9 | 29.9/19.6 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.49 | 0.51 | 0.45 | 5.85 | 23.0/34.1 | 30.8/19.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.061 | 0.65 | 0.35 | 0.00 | 5.98 | 32.8/22.6 | 19.7/28.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Olli Maatta: 1+ goals YES | 4 | 0.062 | 0.056 | +0.019 | +0.013 | $3.17 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Brayden McNabb: 1+ goals YES | 5 | 0.070 | 0.067 | +0.017 | +0.014 | $3.68 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ assists NO | 53 | 0.623 | 0.574 | +0.075 | +0.026 | $15.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.78) | EVIDENCE_MIXED | D |
| Mitch Marner: 1+ goals NO | 73 | 0.767 | 0.756 | +0.023 | +0.013 | $12.23 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Olli Maatta: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes; why: higher confidence-adjusted growth (9.44 vs 1.21 bp); despite a smaller raw edge (+0.019 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: MIN offense suppressed (<= 2 goals)
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKSTHEODORE27-1|yes; why: higher confidence-adjusted growth (8.28 vs 0.98 bp); despite a smaller raw edge (+0.016 vs +0.039/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0099 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12VGKMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-1|no; why: higher confidence-adjusted growth (6.14 vs 1.96 bp); relationships: KXNHLGOAL-26OCT12VGKMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi -0.041); KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no; why: Player prop expression KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.87 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT12VGKMIN-MINOMAATTA3-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4346): highest fidelity KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no — Player prop expression KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.87 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis MIN:OFFENSE_4PLUS (p 0.4008): highest fidelity KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.3446): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT12VGKMIN-MINOMAATTA3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3852, phi -0.114)
- KXNHLGOAL-26OCT12VGKMIN-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.4346, phi -0.111)
- KXNHLAST-26OCT12VGKMIN-VGKMMARNER93-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 22% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3446, phi -0.264)
- KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3446, phi -0.218)
- override: Player prop expression KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT12VGKMIN-VGKTHERTL48-1|no because adjusted EV differs by only 0.2 pts while thesis capture is 0.87 vs 0.85 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.03 (adj +1.51) on $50.00, P(profit) 0.5816, adj growth 12.0 bp · B EV +5.07 (adj +2.93) on $34.74, P(profit) 0.5468, adj growth 25.2 bp · C EV +2.67 (adj +0.85) on $18.62, P(profit) 0.6226, adj growth 7.5 bp · R EV +0.12 (adj +0.07) on $4.00, P(profit) 0.7667, adj growth 2.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
