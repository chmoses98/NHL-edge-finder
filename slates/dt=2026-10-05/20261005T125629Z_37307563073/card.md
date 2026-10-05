# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T12:56:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.43 | +9.16 | +16.19 | 0.641 | -43.02 | -55.26 | 76.42 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +25.70 | +10.33 | +20.13 | 0.702 | -35.92 | -49.76 | 91.51 |
| C best expression per thesis | 99.38 | +14.69 | +4.90 | +19.22 | 0.662 | -28.03 | -31.57 | 44.47 |
| R FUNDED research stakes | 19.00 | +2.04 | +1.11 | -0.61 | 0.311 | -7.61 | -7.61 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  342 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_PHI_win | p_overtime | goals | shots TBL/PHI | TBL/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.123 | 0.69 | 0.31 | 0.00 | 5.98 | 31.6/20.2 | 17.6/27.0 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.49 | 5.84 | 31.7/20.6 | 17.6/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.58 | 0.42 | 0.00 | 5.96 | 26.3/25.7 | 22.5/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.52 | 0.48 | 0.50 | 5.89 | 26.4/26.1 | 22.9/23.3 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.069 | 0.65 | 0.35 | 0.00 | 3.44 | 30.1/19.2 | 17.9/27.6 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.53 | 0.47 | 0.45 | 2.71 | 30.0/19.2 | 17.9/28.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 52 | 0.724 | 0.585 | +0.187 | +0.048 | $19.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 11 | 0.156 | 0.141 | +0.039 | +0.024 | $5.49 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 70 | 0.788 | 0.742 | +0.074 | +0.027 | $16.94 | FUNDED_RESEARCH | $5 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.195 | 0.183 | +0.025 | +0.014 | $3.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (19.89 vs 7.88 bp); relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: TBL offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (12.08 vs 7.88 bp); despite a smaller raw edge (+0.039 vs +0.074/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: PHI offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB2|no; why: higher confidence-adjusted growth (7.88 vs 4.15 bp); wins across more scripts (relative breadth 0.989 vs 0.86); relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.112); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.11); failure: TBL wins by 2+
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (12.08 vs 3.07 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.000); they share one thesis budget; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.11); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TBL:SUPPRESSED (p 0.3877): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.2804): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- thesis GAME:TIGHT (p 0.4514): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.4 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3879, phi -0.236)
- KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4998, phi -0.221)
- KXNHLSPREAD-26OCT05PHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3382, phi -0.725)
- KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4998, phi -0.206)

portfolios: A EV +9.73 (adj +2.07) on $44.56, P(profit) 0.6985, adj growth 18.1 bp · B EV +10.91 (adj +3.79) on $45.48, P(profit) 0.6593, adj growth 33.8 bp · C EV +8.86 (adj +3.04) on $50.00, P(profit) 0.6471, adj growth 27.9 bp · R EV +1.19 (adj +0.60) on $7.00, P(profit) 0.1563, adj growth 20.1 bp

## OTT @ BOS  ·  10000 joint draws  ·  368 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.54 | 0.46 | 0.00 | 6.01 | 27.3/27.9 | 24.5/23.5 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.45 | 0.55 | 0.47 | 5.89 | 21.9/33.2 | 29.9/18.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.104 | 0.50 | 0.50 | 0.00 | 6.01 | 21.7/33.0 | 29.1/18.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.50 | 0.50 | 0.48 | 5.89 | 27.3/27.7 | 24.3/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.53 | 0.47 | 0.00 | 9.18 | 28.9/29.4 | 23.3/22.6 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.061 | 0.44 | 0.56 | 0.00 | 9.23 | 23.2/35.1 | 28.2/17.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carter Yakemchuk: 1+ goals NO | 88 | 0.932 | 0.917 | +0.045 | +0.029 | $19.52 | FUNDED_RESEARCH | $5 | OTT:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 8 | 0.110 | 0.099 | +0.025 | +0.013 | $3.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.166 | 0.154 | +0.028 | +0.017 | $4.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 68 | 0.800 | 0.716 | +0.105 | +0.020 | $19.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
- **Carter Yakemchuk: 1+ goals NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-2|no; why: higher confidence-adjusted growth (19.27 vs 0.23 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0034 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.001); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (5.05 vs 4.96 bp); despite a smaller raw edge (+0.025 vs +0.028/contract); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: OTT offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (4.96 vs 1.43 bp); despite a smaller raw edge (+0.028 vs +0.052/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: OTT offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05OTTBOS-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (4.30 vs 1.17 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0100 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: BOS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, OTT shot control · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.3598): highest fidelity KXNHLAST-26OCT05OTTBOS-OTTCGIROUX28-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.4233): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis BOS:SUPPRESSED (p 0.4023): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3598, phi -0.102)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4233, phi -0.156)
- KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4233, phi -0.202)
- KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.0 pts; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3723, phi -0.215)

portfolios: A EV +6.74 (adj +1.34) on $44.56, P(profit) 0.7035, adj growth 11.4 bp · B EV +5.76 (adj +2.25) on $46.64, P(profit) 0.809, adj growth 20.3 bp · C EV +1.78 (adj +0.77) on $24.48, P(profit) 0.1659, adj growth 7.0 bp · R EV +0.25 (adj +0.16) on $5.00, P(profit) 0.9322, adj growth 6.4 bp

## WPG @ PIT  ·  10000 joint draws  ·  350 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_WPG_win | p_overtime | goals | shots PIT/WPG | PIT/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.68 | 0.32 | 0.00 | 6.01 | 27.1/26.8 | 24.1/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.102 | 0.73 | 0.27 | 0.00 | 6.06 | 32.1/21.2 | 18.8/27.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.51 | 0.49 | 0.46 | 5.97 | 27.5/27.2 | 24.0/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.43 | 29.0/28.5 | 23.3/21.7 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.57 | 0.43 | 0.46 | 5.95 | 32.5/21.6 | 18.4/29.0 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.077 | 0.75 | 0.25 | 0.00 | 9.31 | 34.2/22.6 | 18.4/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Hallander: 1+ goals YES | 14 | 0.183 | 0.168 | +0.034 | +0.020 | $5.21 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Connor Dewar: 1+ goals YES | 15 | 0.187 | 0.176 | +0.028 | +0.017 | $4.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Filip Hallander: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (6.73 vs 4.88 bp); relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: PIT offense suppressed (<= 2 goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLAST-26OCT05WPGPIT-WPGMSCHEIFELE55-1|no; why: higher confidence-adjusted growth (4.88 vs 0.00 bp); despite a smaller raw edge (+0.028 vs +0.062/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT05WPGPIT-PITFHALLANDER11-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, PIT shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4986): highest fidelity KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:WINS_BY_2PLUS (p 0.4017): highest fidelity KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26OCT05WPGPIT-PITFHALLANDER11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2934, phi -0.161)
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2934, phi -0.204)

portfolios: A EV +3.36 (adj +2.00) on $16.32, P(profit) 0.3335, adj growth 15.7 bp · B EV +2.03 (adj +1.21) on $9.92, P(profit) 0.3335, adj growth 10.5 bp · C EV +0.86 (adj +0.53) on $4.90, P(profit) 0.1867, adj growth 4.6 bp · R EV +0.46 (adj +0.27) on $2.00, P(profit) 0.1827, adj growth 8.6 bp

## SJS @ DAL  ·  10000 joint draws  ·  364 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.58 | 0.42 | 0.00 | 6.02 | 26.5/26.2 | 23.1/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.48 | 5.94 | 26.7/26.3 | 23.1/23.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.100 | 0.64 | 0.36 | 0.00 | 6.01 | 31.4/20.8 | 17.9/27.1 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.55 | 0.45 | 0.49 | 5.9 | 31.6/21.0 | 17.9/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.21 | 28.1/27.6 | 22.1/21.8 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.066 | 0.65 | 0.35 | 0.00 | 9.28 | 33.0/22.2 | 17.5/25.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Kiefer Sherwood: 1+ goals YES | 13 | 0.190 | 0.172 | +0.052 | +0.034 | $8.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 69 | 0.817 | 0.725 | +0.112 | +0.020 | $19.52 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Miro Heiskanen: 1+ goals NO | 86 | 0.892 | 0.882 | +0.024 | +0.013 | $19.52 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.95) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL2|no; why: higher confidence-adjusted growth (21.29 vs 0.68 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0085 below the 0.010/contract floor; relationships: KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT05SJDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT05SJDAL-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (4.14 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT05SJDAL-DALMHEISKANEN4-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: SJS offense succeeds (4+ goals)
- **Miro Heiskanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL2|no; why: higher confidence-adjusted growth (3.50 vs 0.68 bp); despite a smaller raw edge (+0.024 vs +0.038/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0085 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.4372): highest fidelity KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3415): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis DAL:SUPPRESSED (p 0.3632): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4372, phi -0.204)
- KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.2 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3415, phi -0.2)
- KXNHLGOAL-26OCT05SJDAL-DALMHEISKANEN4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 5% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4226, phi -0.134)

portfolios: A EV +7.61 (adj +3.75) on $44.56, P(profit) 0.1898, adj growth 31.2 bp · B EV +7.01 (adj +3.08) on $47.97, P(profit) 0.7847, adj growth 26.9 bp · C EV +3.18 (adj +0.56) on $20.00, P(profit) 0.8172, adj growth 5.0 bp · R EV +0.14 (adj +0.08) on $5.00, P(profit) 0.8925, adj growth 2.8 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
