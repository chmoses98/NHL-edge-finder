# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T21:04:14Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.57 | +8.20 | +23.80 | 0.717 | -28.27 | -41.57 | 72.33 |
| B thesis-diversified (joint) ← optimiser card | 147.85 | +36.70 | +18.81 | +30.63 | 0.657 | -49.17 | -64.88 | 163.58 |
| C best expression per thesis | 150.01 | +31.24 | +13.52 | +26.51 | 0.703 | -36.51 | -51.37 | 120.00 |
| R FUNDED research stakes | 15.00 | +3.16 | +2.04 | -0.76 | 0.242 | -9.89 | -9.89 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  342 bet sides mapped, 20 +EV candidates, 4 on card

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

portfolios: A EV +9.96 (adj +1.92) on $37.50, P(profit) 0.6644, adj growth 16.5 bp · B EV +13.52 (adj +6.35) on $40.72, P(profit) 0.4041, adj growth 55.7 bp · C EV +12.42 (adj +5.36) on $47.86, P(profit) 0.7106, adj growth 47.9 bp · R EV +1.45 (adj +1.01) on $3.00, P(profit) 0.1577, adj growth 32.3 bp

## OTT @ BOS  ·  10000 joint draws  ·  366 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

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
| Hayden Hodgson: 1+ goals YES | 6 | 0.100 | 0.088 | +0.036 | +0.024 | $5.39 | FUNDED_RESEARCH | $2 | OTT:OFFENSE_4PLUS | FRAGILE (0.16) | EVIDENCE_STRONGER | D |
| Marat Khusnutdinov: 1+ goals YES | 10 | 0.151 | 0.136 | +0.045 | +0.030 | $7.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Nick Cousins: 1+ goals YES | 7 | 0.110 | 0.099 | +0.035 | +0.024 | $5.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Casey Mittelstadt: 1+ goals YES | 14 | 0.190 | 0.176 | +0.042 | +0.028 | $7.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Hayden Hodgson: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (19.86 vs 11.39 bp); despite a smaller raw edge (+0.036 vs +0.036/contract); relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: OTT offense suppressed (<= 2 goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes; why: higher confidence-adjusted growth (19.81 vs 13.23 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: BOS offense suppressed (<= 2 goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes; why: higher confidence-adjusted growth (17.71 vs 11.39 bp); despite a smaller raw edge (+0.035 vs +0.036/contract); relationships: KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense suppressed (<= 2 goals)
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes; why: higher confidence-adjusted growth (13.23 vs 2.48 bp); despite a smaller raw edge (+0.042 vs +0.051/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3561): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis OTT:OFFENSE_4PLUS (p 0.3555): highest fidelity KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-OTTMAMADIO22-1|yes (same contract)
- thesis BOS:SUPPRESSED (p 0.4243): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no (same contract)
- KXNHLGOAL-26OCT05OTTBOS-OTTHHODGSON42-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 84% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.158)
- KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4243, phi -0.183)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4252, phi -0.145)
- KXNHLGOAL-26OCT05OTTBOS-BOSCMITTELSTADT11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4243, phi -0.199)

portfolios: A EV +4.93 (adj +1.70) on $37.50, P(profit) 0.8087, adj growth 16.3 bp · B EV +11.16 (adj +7.43) on $26.43, P(profit) 0.4555, adj growth 63.4 bp · C EV +7.71 (adj +3.94) on $45.59, P(profit) 0.6646, adj growth 34.7 bp · R EV +1.14 (adj +0.74) on $2.00, P(profit) 0.1003, adj growth 23.1 bp

## WPG @ PIT  ·  10000 joint draws  ·  348 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.613 / away 0.387

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
| Connor Dewar: 1+ goals YES | 14 | 0.198 | 0.182 | +0.049 | +0.034 | $9.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Morgan Barron: 1+ goals YES | 10 | 0.133 | 0.122 | +0.027 | +0.016 | $4.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WPG:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ goals NO | 77 | 0.803 | 0.794 | +0.021 | +0.011 | $13.69 | FUNDED_RESEARCH | $4 | PIT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Egor Chinakhov: 1+ assists YES | 32 | 0.382 | 0.346 | +0.047 | +0.011 | $3.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes; why: higher confidence-adjusted growth (19.12 vs 1.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi 0.034); failure: PIT offense suppressed (<= 2 goals)
- **Morgan Barron: 1+ goals YES** — thesis: WPG offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-WPGGVILARDI13-1|yes; why: higher confidence-adjusted growth (5.77 vs 0.82 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WPG offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ goals NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITEMALKIN71-1|no; why: higher confidence-adjusted growth (1.63 vs 0.11 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: MOSTLY_INDEPENDENT (phi -0.049); failure: PIT offense succeeds (4+ goals)
- **Egor Chinakhov: 1+ assists YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (19.12 vs 1.17 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.034); they share one thesis budget; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.049); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, PIT shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4982): highest fidelity KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:OFFENSE_4PLUS (p 0.3161): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis PIT:SUPPRESSED (p 0.2956): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.19)
- KXNHLGOAL-26OCT05WPGPIT-WPGMBARRON36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:SUPPRESSED (p 0.4715, phi -0.192)
- KXNHLGOAL-26OCT05WPGPIT-PITBKINDEL81-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4982, phi -0.181)
- KXNHLAST-26OCT05WPGPIT-PITECHINAKHOV59-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2956, phi -0.276)

portfolios: A EV +6.10 (adj +3.31) on $37.50, P(profit) 0.5087, adj growth 27.5 bp · B EV +4.95 (adj +3.00) on $30.70, P(profit) 0.3067, adj growth 25.9 bp · C EV +2.89 (adj +1.97) on $8.70, P(profit) 0.1977, adj growth 17.0 bp · R EV +0.11 (adj +0.06) on $4.00, P(profit) 0.8032, adj growth 2.0 bp

## SJS @ DAL  ·  10000 joint draws  ·  358 bet sides mapped, 20 +EV candidates, 4 on card

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
| Roope Hintz: 1+ assists NO | 58 | 0.726 | 0.628 | +0.129 | +0.031 | $13.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | DAL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Mikko Rantanen: 1+ goals NO | 67 | 0.729 | 0.713 | +0.043 | +0.027 | $13.59 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 69 | 0.820 | 0.729 | +0.115 | +0.024 | $15.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Dallas wins by over 1.5 goals NO | 59 | 0.671 | 0.628 | +0.064 | +0.021 | $7.83 | FUNDED_RESEARCH | $2 | SJS:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Roope Hintz: 1+ assists NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no; why: higher confidence-adjusted growth (8.71 vs 7.65 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.085); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLSPREAD-26OCT05SJDAL-DAL2|no: REINFORCING (phi 0.17); failure: DAL offense succeeds (4+ goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: second expression of the same thesis: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no has the higher standalone adjusted growth (8.71 vs 7.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.085); they share one thesis budget; relationships: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi 0.085); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT05SJDAL-DAL2|no: REINFORCING (phi 0.163); failure: DAL offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (6.12 vs 0.21 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT05SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: SJS offense succeeds (4+ goals)
- **Dallas wins by over 1.5 goals NO** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL3|no; why: higher confidence-adjusted growth (4.06 vs 3.35 bp); relationships: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no: REINFORCING (phi 0.17); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: REINFORCING (phi 0.163); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: INTENTIONAL_DIVERSIFIER (phi -0.133); failure: DAL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:SUPPRESSED (p 0.3644): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.4353): highest fidelity KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3447): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.1 pts; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.236)
- KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4208, phi -0.235)
- KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.0 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3447, phi -0.213)
- KXNHLSPREAD-26OCT05SJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.3291, phi -1.0)

portfolios: A EV +5.59 (adj +1.27) on $37.50, P(profit) 0.7636, adj growth 12.0 bp · B EV +7.06 (adj +2.03) on $50.00, P(profit) 0.6975, adj growth 18.6 bp · C EV +8.23 (adj +2.25) on $47.86, P(profit) 0.6661, adj growth 20.4 bp · R EV +0.46 (adj +0.23) on $6.00, P(profit) 0.5229, adj growth 8.3 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
