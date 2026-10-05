# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T16:56:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +29.63 | +8.71 | +25.82 | 0.695 | -35.46 | -49.52 | 73.40 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +29.95 | +13.47 | +26.92 | 0.687 | -34.42 | -50.16 | 121.13 |
| C best expression per thesis | 150.00 | +26.53 | +10.91 | +24.84 | 0.685 | -33.52 | -51.17 | 96.66 |
| R FUNDED research stakes | 13.00 | +2.65 | +1.66 | -0.40 | 0.320 | -7.33 | -13.00 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  346 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.660 / away 0.340

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_PHI_win | p_overtime | goals | shots TBL/PHI | TBL/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.126 | 0.68 | 0.32 | 0.00 | 5.98 | 31.3/20.3 | 17.7/26.9 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.54 | 0.46 | 0.49 | 5.84 | 32.1/20.7 | 17.6/28.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.59 | 0.41 | 0.00 | 5.96 | 26.5/26.1 | 22.9/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.51 | 0.49 | 0.45 | 5.86 | 26.5/26.0 | 22.8/23.2 | even strength |
| TBL shot control · low event (<=4) · decided (2+) | 0.073 | 0.62 | 0.38 | 0.00 | 3.41 | 30.2/19.3 | 17.9/28.0 | even strength |
| TBL shot control · low event (<=4) · tight (1-goal/OT) | 0.068 | 0.54 | 0.46 | 0.45 | 2.75 | 30.2/19.0 | 17.6/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| John Carlson: 1+ assists NO | 52 | 0.722 | 0.588 | +0.184 | +0.050 | $18.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 11 | 0.156 | 0.142 | +0.039 | +0.025 | $5.42 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Tampa Bay wins by over 2.5 goals NO | 69 | 0.783 | 0.734 | +0.078 | +0.029 | $15.83 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 15 | 0.195 | 0.181 | +0.036 | +0.022 | $5.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (22.02 vs 8.80 bp); relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: TBL offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (13.27 vs 8.80 bp); despite a smaller raw edge (+0.039 vs +0.078/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.017); failure: PHI offense suppressed (<= 2 goals)
- **Tampa Bay wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT05PHITB-TB2|no; why: higher confidence-adjusted growth (8.80 vs 5.97 bp); wins across more scripts (relative breadth 0.989 vs 0.869); relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.149); KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.107); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.108); failure: TBL wins by 2+
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (13.27 vs 8.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.017); they share one thesis budget; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLSPREAD-26OCT05PHITB-TB3|no: MOSTLY_INDEPENDENT (phi 0.108); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis TBL:SUPPRESSED (p 0.3945): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:OFFENSE_4PLUS (p 0.2807): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3853, phi -0.227)
- KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.501, phi -0.222)
- KXNHLSPREAD-26OCT05PHITB-TB3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3393, phi -0.735)
- KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.501, phi -0.228)

portfolios: A EV +10.59 (adj +1.88) on $39.55, P(profit) 0.6644, adj growth 15.8 bp · B EV +10.94 (adj +4.22) on $44.46, P(profit) 0.6947, adj growth 37.9 bp · C EV +11.02 (adj +3.96) on $45.65, P(profit) 0.6449, adj growth 35.2 bp · R EV +0.44 (adj +0.16) on $4.00, P(profit) 0.7826, adj growth 6.1 bp

## OTT @ BOS  ·  10000 joint draws  ·  362 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.54 | 0.46 | 0.00 | 5.97 | 27.4/28.0 | 24.6/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.48 | 5.89 | 27.4/27.8 | 24.4/24.1 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.104 | 0.45 | 0.55 | 0.00 | 5.99 | 21.5/33.1 | 29.2/18.3 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.46 | 0.54 | 0.46 | 5.87 | 21.8/33.5 | 30.0/18.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.070 | 0.52 | 0.48 | 0.00 | 9.12 | 28.5/29.1 | 23.2/22.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.061 | 0.54 | 0.46 | 0.00 | 3.42 | 26.1/26.6 | 24.8/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marat Khusnutdinov: 1+ goals YES | 10 | 0.151 | 0.137 | +0.045 | +0.031 | $6.82 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 67 | 0.834 | 0.724 | +0.148 | +0.039 | $17.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| JJ Peterka: 1+ assists NO | 69 | 0.785 | 0.735 | +0.080 | +0.030 | $17.45 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 8 | 0.111 | 0.101 | +0.026 | +0.016 | $3.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes; why: higher confidence-adjusted growth (21.48 vs 2.48 bp); despite a smaller raw edge (+0.045 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: BOS offense suppressed (<= 2 goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (15.30 vs 4.76 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: OTT offense succeeds (4+ goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05OTTBOS-BOSDPASTRNAK88-1|no; why: higher confidence-adjusted growth (9.46 vs 1.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.028); KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: BOS offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (6.89 vs 5.92 bp); despite a smaller raw edge (+0.026 vs +0.028/contract); relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.01); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:SUPPRESSED (p 0.4243): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLAST-26OCT05OTTBOS-OTTJSPENCE10-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:SUPPRESSED (p 0.4252): highest fidelity KXNHLAST-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4243, phi -0.183)
- KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 16.9 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3555, phi -0.187)
- KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3561, phi -0.2)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.147)

portfolios: A EV +5.21 (adj +1.54) on $39.55, P(profit) 0.7576, adj growth 14.4 bp · B EV +9.72 (adj +4.36) on $45.22, P(profit) 0.7413, adj growth 39.3 bp · C EV +6.13 (adj +2.44) on $45.62, P(profit) 0.707, adj growth 21.7 bp · R EV +0.85 (adj +0.58) on $2.00, P(profit) 0.1514, adj growth 19.8 bp

## WPG @ PIT  ·  10000 joint draws  ·  348 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.612 / away 0.388

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
| Connor Dewar: 1+ goals YES | 14 | 0.198 | 0.182 | +0.049 | +0.034 | $8.21 | FUNDED_RESEARCH | $3 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.133 | 0.123 | +0.027 | +0.017 | $4.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Egor Chinakhov: 1+ assists YES | 32 | 0.382 | 0.346 | +0.047 | +0.011 | $3.17 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (19.12 vs 1.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi 0.034); failure: PIT offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (6.70 vs 0.36 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WPG offense suppressed (<= 2 goals)
- **Egor Chinakhov: 1+ assists YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (19.12 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.034); they share one thesis budget; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4982): highest fidelity KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3161): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.19)
- KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4715, phi -0.192)
- KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.276)

portfolios: A EV +7.25 (adj +4.00) on $31.35, P(profit) 0.5678, adj growth 31.6 bp · B EV +4.21 (adj +2.63) on $15.52, P(profit) 0.3067, adj growth 23.0 bp · C EV +3.00 (adj +2.04) on $9.03, P(profit) 0.1977, adj growth 17.6 bp · R EV +1.00 (adj +0.68) on $3.00, P(profit) 0.1977, adj growth 22.1 bp

## SJS @ DAL  ·  10000 joint draws  ·  362 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.639 / away 0.361

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.56 | 0.44 | 0.00 | 6.0 | 26.6/26.3 | 23.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.53 | 0.47 | 0.46 | 5.95 | 26.6/26.4 | 23.0/23.3 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.096 | 0.64 | 0.36 | 0.00 | 5.98 | 31.3/20.6 | 17.8/27.0 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.54 | 0.46 | 0.46 | 5.86 | 31.5/20.8 | 17.7/28.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.57 | 0.43 | 0.00 | 9.39 | 28.1/27.6 | 21.8/21.5 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.065 | 0.65 | 0.35 | 0.00 | 9.16 | 33.3/22.2 | 17.5/26.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jason Robertson: 1+ goals NO | 56 | 0.630 | 0.611 | +0.053 | +0.034 | $13.14 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 67 | 0.732 | 0.715 | +0.046 | +0.030 | $13.99 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 69 | 0.818 | 0.728 | +0.113 | +0.023 | $14.20 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 15 | 0.189 | 0.178 | +0.030 | +0.019 | $3.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no; why: higher confidence-adjusted growth (10.35 vs 9.05 bp); relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: DAL offense succeeds (4+ goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no has the higher standalone adjusted growth (10.35 vs 9.05 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: DAL offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (5.81 vs 5.37 bp); relationships: KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: SJS offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL2|no; why: higher confidence-adjusted growth (5.70 vs 4.04 bp); despite a smaller raw edge (+0.030 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.016); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:SUPPRESSED (p 0.3657): highest fidelity KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4387): highest fidelity KXNHLAST-26OCT05SJDAL-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:OFFENSE_4PLUS (p 0.3448): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4204, phi -0.253)
- KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4204, phi -0.217)
- KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.8 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3448, phi -0.2)
- KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4387, phi -0.216)

portfolios: A EV +6.58 (adj +1.29) on $39.55, P(profit) 0.733, adj growth 11.6 bp · B EV +5.08 (adj +2.26) on $44.80, P(profit) 0.4597, adj growth 21.0 bp · C EV +6.38 (adj +2.47) on $49.70, P(profit) 0.5938, adj growth 22.1 bp · R EV +0.36 (adj +0.24) on $4.00, P(profit) 0.6299, adj growth 8.5 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
