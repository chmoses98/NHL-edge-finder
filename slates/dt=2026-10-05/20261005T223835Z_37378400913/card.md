# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T22:38:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +30.03 | +9.44 | +24.45 | 0.704 | -33.45 | -48.76 | 80.66 |
| B thesis-diversified (joint) ← optimiser card | 149.52 | +36.31 | +18.06 | +27.88 | 0.679 | -42.57 | -60.68 | 158.23 |
| C best expression per thesis | 149.93 | +29.19 | +11.50 | +27.41 | 0.704 | -32.67 | -48.07 | 101.71 |
| R FUNDED research stakes | 10.00 | +2.82 | +1.94 | -2.71 | 0.253 | -10.00 | -10.00 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  342 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.658 / away 0.342

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
| Sean Couturier: 1+ goals YES | 10 | 0.158 | 0.142 | +0.051 | +0.036 | $8.78 | FUNDED_RESEARCH | $3 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| John Carlson: 1+ assists NO | 52 | 0.722 | 0.588 | +0.184 | +0.050 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 15 | 0.195 | 0.183 | +0.036 | +0.024 | $6.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Ilya Mikheyev: 1+ goals YES | 15 | 0.186 | 0.175 | +0.027 | +0.017 | $5.38 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (28.41 vs 9.14 bp); relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT05PHITB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: PHI offense suppressed (<= 2 goals)
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (22.02 vs 8.88 bp); relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT05PHITB-TBIMIKHEYEV95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: TBL offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (28.41 vs 9.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26OCT05PHITB-TBIMIKHEYEV95-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense suppressed (<= 2 goals)
- **Ilya Mikheyev: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05PHITB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (4.42 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: TBL offense suppressed (<= 2 goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.10.
- thesis PHI:OFFENSE_4PLUS (p 0.2807): highest fidelity KXNHLTEAMTOTAL-26OCT05PHITB-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3945): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:TIGHT (p 0.4494): highest fidelity KXNHLSPREAD-26OCT05PHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT05PHITB-TB3|no (same contract)
- KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.501, phi -0.221)
- KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 15% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 20.7 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3853, phi -0.227)
- KXNHLGOAL-26OCT05PHITB-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.501, phi -0.229)
- KXNHLGOAL-26OCT05PHITB-TBIMIKHEYEV95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.3945, phi -0.192)

portfolios: A EV +10.10 (adj +2.04) on $39.70, P(profit) 0.6644, adj growth 17.6 bp · B EV +13.52 (adj +6.35) on $40.72, P(profit) 0.4041, adj growth 55.7 bp · C EV +12.97 (adj +5.60) on $50.00, P(profit) 0.7106, adj growth 49.8 bp · R EV +1.45 (adj +1.01) on $3.00, P(profit) 0.1577, adj growth 32.3 bp

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
| Nick Cousins: 1+ goals YES | 7 | 0.114 | 0.102 | +0.039 | +0.027 | $6.44 | FUNDED_RESEARCH | $2 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| William Eklund: 1+ assists NO | 67 | 0.841 | 0.724 | +0.156 | +0.038 | $20.00 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Marat Khusnutdinov: 1+ goals YES | 10 | 0.143 | 0.129 | +0.037 | +0.023 | $5.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Hayden Hodgson: 1+ goals YES | 6 | 0.092 | 0.082 | +0.029 | +0.018 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (22.32 vs 4.29 bp); relationships: KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.033); failure: OTT offense suppressed (<= 2 goals)
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTDCOZENS24-1|no; why: higher confidence-adjusted growth (14.75 vs 2.21 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: OTT offense succeeds (4+ goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (11.48 vs 0.84 bp); alternative not eligible: confidence-adjusted EV +0.0086 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: BOS offense suppressed (<= 2 goals)
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (11.30 vs 4.29 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis OTT:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4243): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4252): highest fidelity KXNHLAST-26OCT05OTTBOS-OTTDCOZENS24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-OTTDCOZENS24-1|no (same contract)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.161)
- KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 18.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3555, phi -0.187)
- KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4243, phi -0.194)
- KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.145)

portfolios: A EV +6.56 (adj +1.22) on $39.70, P(profit) 0.7097, adj growth 10.9 bp · B EV +11.81 (adj +5.84) on $36.34, P(profit) 0.314, adj growth 50.8 bp · C EV +4.17 (adj +1.26) on $36.16, P(profit) 0.6386, adj growth 11.1 bp · R EV +1.05 (adj +0.73) on $2.00, P(profit) 0.1138, adj growth 23.5 bp

## WPG @ PIT  ·  10000 joint draws  ·  348 bet sides mapped, 5 +EV candidates, 4 on card

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
| Connor Dewar: 1+ goals YES | 14 | 0.198 | 0.182 | +0.049 | +0.034 | $9.03 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 11 | 0.145 | 0.135 | +0.028 | +0.018 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.133 | 0.122 | +0.027 | +0.016 | $4.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Mark Scheifele: 1+ goals YES | 27 | 0.310 | 0.297 | +0.026 | +0.014 | $4.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (19.12 vs 0.69 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (19.12 vs 6.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: PIT offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes; why: higher confidence-adjusted growth (5.77 vs 1.99 bp); relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)
- **Mark Scheifele: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (1.99 vs 0.82 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: WPG offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4982): highest fidelity KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes (same contract)
- thesis WPG:OFFENSE_4PLUS (p 0.3161): highest fidelity KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes (same contract)
- thesis PIT:SUPPRESSED (p 0.2956): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.19)
- KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.171)
- KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4715, phi -0.192)
- KXNHLGOAL-26OCT05WPGPIT-WPGMSCHEIFELE55-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4715, phi -0.283)

portfolios: A EV +7.45 (adj +4.79) on $30.89, P(profit) 0.4042, adj growth 39.1 bp · B EV +5.56 (adj +3.59) on $22.46, P(profit) 0.4042, adj growth 30.9 bp · C EV +3.45 (adj +2.28) on $13.77, P(profit) 0.4473, adj growth 19.6 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

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
| Mikko Rantanen: 1+ goals NO | 67 | 0.729 | 0.713 | +0.043 | +0.027 | $16.44 | FUNDED_RESEARCH | $5 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jason Robertson: 1+ goals NO | 57 | 0.631 | 0.615 | +0.044 | +0.028 | $13.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 69 | 0.820 | 0.729 | +0.115 | +0.024 | $16.44 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Kiefer Sherwood: 1+ goals YES | 15 | 0.187 | 0.177 | +0.029 | +0.018 | $3.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: Player prop expression KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.0); failure: DAL offense succeeds (4+ goals)
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no has the higher standalone adjusted growth (8.71 vs 6.88 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.222); relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.034); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: DAL offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (6.12 vs 0.21 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.037); failure: SJS offense succeeds (4+ goals)
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL2|no; why: higher confidence-adjusted growth (5.17 vs 4.06 bp); despite a smaller raw edge (+0.029 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.037); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:SUPPRESSED (p 0.3644): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no — Player prop expression KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.235)
- KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.258)
- KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.0 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3447, phi -0.213)
- KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4353, phi -0.203)
- override: Player prop expression KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no selected over player prop KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.87 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.91 (adj +1.39) on $39.70, P(profit) 0.7636, adj growth 13.1 bp · B EV +5.42 (adj +2.28) on $50.00, P(profit) 0.4551, adj growth 20.8 bp · C EV +8.60 (adj +2.36) on $50.00, P(profit) 0.6661, adj growth 21.2 bp · R EV +0.32 (adj +0.20) on $5.00, P(profit) 0.7288, adj growth 7.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
