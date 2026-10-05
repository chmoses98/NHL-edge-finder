# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T23:28:36Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 143.58 | +22.61 | +7.55 | +16.65 | 0.622 | -32.17 | -45.71 | 63.04 |
| B thesis-diversified (joint) ← optimiser card | 105.58 | +20.13 | +11.13 | +18.18 | 0.606 | -38.15 | -53.67 | 97.28 |
| C best expression per thesis | 104.50 | +19.06 | +7.84 | +17.52 | 0.647 | -35.71 | -49.26 | 68.74 |
| R FUNDED research stakes | 11.00 | +1.48 | +0.84 | +1.41 | 0.633 | -5.89 | -5.89 | 0.00 |

## OTT @ BOS  ·  10000 joint draws  ·  366 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 5.96 | 27.4/28.0 | 24.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.9 | 27.4/27.8 | 24.4/24.0 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.105 | 0.45 | 0.55 | 0.00 | 5.99 | 21.5/33.1 | 29.2/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.46 | 0.54 | 0.46 | 5.87 | 21.8/33.5 | 30.0/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.52 | 0.48 | 0.00 | 9.12 | 28.5/29.1 | 23.2/22.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.53 | 0.47 | 0.00 | 3.43 | 26.1/26.6 | 24.8/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nick Cousins: 1+ goals YES | 7 | 0.114 | 0.097 | +0.039 | +0.022 | $5.03 | FUNDED_RESEARCH | $2 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 67 | 0.841 | 0.724 | +0.156 | +0.038 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Hayden Hodgson: 1+ goals YES | 6 | 0.092 | 0.082 | +0.029 | +0.018 | $4.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.163 | 0.157 | +0.025 | +0.019 | $5.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (14.93 vs 6.63 bp); relationships: KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (14.75 vs 5.94 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: OTT offense succeeds (4+ goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (11.30 vs 6.63 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTJSPENCE10-2|yes; why: higher confidence-adjusted growth (6.63 vs 0.19 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.4252): highest fidelity KXNHLAST-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.4243): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no (same contract)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.161)
- KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3555, phi -0.187)
- KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.145)
- KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.212)

portfolios: A EV +8.99 (adj +1.85) on $50.00, P(profit) 0.6981, adj growth 16.2 bp · B EV +10.07 (adj +4.54) on $34.68, P(profit) 0.3282, adj growth 39.9 bp · C EV +5.55 (adj +2.03) on $40.30, P(profit) 0.5924, adj growth 17.7 bp · R EV +1.05 (adj +0.59) on $2.00, P(profit) 0.1138, adj growth 18.1 bp

## WPG @ PIT  ·  10000 joint draws  ·  348 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.616 / away 0.385

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_WPG_win | p_overtime | goals | shots PIT/WPG | PIT/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.68 | 0.32 | 0.00 | 5.98 | 27.2/26.8 | 24.0/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.108 | 0.74 | 0.26 | 0.00 | 5.99 | 32.4/21.3 | 18.9/27.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.54 | 0.46 | 0.45 | 5.9 | 27.0/26.9 | 23.6/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.68 | 0.32 | 0.00 | 9.42 | 29.0/28.6 | 23.4/21.7 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.47 | 5.92 | 32.5/21.6 | 18.5/29.0 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.079 | 0.76 | 0.24 | 0.00 | 9.35 | 34.2/22.9 | 18.6/25.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 14 | 0.198 | 0.182 | +0.049 | +0.034 | $9.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.310 | 0.299 | +0.026 | +0.015 | $5.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.803 | 0.792 | +0.021 | +0.010 | $12.14 | FUNDED_RESEARCH | $4 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (19.12 vs 0.69 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PIT offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05WPGPIT-WPGGVILARDI13-2|yes; why: despite a smaller raw edge (+0.026 vs +0.033/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.926 vs 0.734); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: WPG offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (1.29 vs 0.11 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4982): highest fidelity KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3161): highest fidelity KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.2956): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.19)
- KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4715, phi -0.283)
- KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4982, phi -0.181)

portfolios: A EV +6.17 (adj +4.01) on $43.58, P(profit) 0.3979, adj growth 31.2 bp · B EV +3.82 (adj +2.48) on $26.37, P(profit) 0.3979, adj growth 21.4 bp · C EV +3.49 (adj +2.33) on $14.20, P(profit) 0.4473, adj growth 20.0 bp · R EV +0.11 (adj +0.05) on $4.00, P(profit) 0.8032, adj growth 1.7 bp

## SJS @ DAL  ·  10000 joint draws  ·  358 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.643 / away 0.357

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.02 | 26.6/26.3 | 23.1/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.48 | 5.88 | 26.6/26.3 | 23.1/23.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.103 | 0.61 | 0.39 | 0.00 | 6.04 | 31.6/20.8 | 18.0/27.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.53 | 0.47 | 0.49 | 5.9 | 31.4/20.7 | 17.6/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.56 | 0.44 | 0.00 | 9.27 | 28.3/27.9 | 22.3/22.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.068 | 0.66 | 0.34 | 0.00 | 9.2 | 33.0/22.2 | 17.5/25.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 13 | 0.187 | 0.172 | +0.050 | +0.034 | $8.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 67 | 0.729 | 0.713 | +0.043 | +0.027 | $16.65 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jason Robertson: 1+ goals NO | 57 | 0.631 | 0.615 | +0.044 | +0.028 | $13.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Igor Chernyshov: 1+ goals YES | 17 | 0.212 | 0.201 | +0.032 | +0.021 | $5.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes; why: higher confidence-adjusted growth (20.62 vs 6.23 bp); relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: SJS offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: Player prop expression KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DAL offense succeeds (4+ goals)
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no has the higher standalone adjusted growth (8.71 vs 6.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.222); relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: DAL offense succeeds (4+ goals)
- **Igor Chernyshov: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes has the higher standalone adjusted growth (20.62 vs 6.23 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DAL:SUPPRESSED (p 0.3644): highest fidelity KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no — Player prop expression KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no (same contract)
- KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4353, phi -0.203)
- KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.235)
- KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.258)
- KXNHLGOAL-26OCT05SJDAL-SJICHERNYSHOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4353, phi -0.214)
- override: Player prop expression KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +7.45 (adj +1.69) on $50.00, P(profit) 0.7636, adj growth 15.6 bp · B EV +6.24 (adj +4.11) on $44.53, P(profit) 0.6348, adj growth 36.0 bp · C EV +10.02 (adj +3.48) on $50.00, P(profit) 0.6769, adj growth 31.0 bp · R EV +0.32 (adj +0.20) on $5.00, P(profit) 0.7288, adj growth 7.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
