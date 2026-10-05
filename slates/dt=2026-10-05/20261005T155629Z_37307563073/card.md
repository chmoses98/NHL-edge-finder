# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-05T15:56:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +25.92 | +7.35 | +23.52 | 0.723 | -27.99 | -41.79 | 64.32 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +22.50 | +9.31 | +21.70 | 0.712 | -26.46 | -38.82 | 85.19 |
| C best expression per thesis | 149.66 | +22.02 | +8.91 | +18.67 | 0.683 | -29.92 | -43.42 | 80.08 |
| R FUNDED research stakes | 17.00 | +1.28 | +0.77 | +2.21 | 0.519 | -6.31 | -8.62 | 0.00 |

## PHI @ TBL  ·  10000 joint draws  ·  342 bet sides mapped, 17 +EV candidates, 4 on card


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
| John Carlson: 1+ assists NO | 52 | 0.724 | 0.585 | +0.187 | +0.048 | $14.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Sean Couturier: 1+ goals YES | 11 | 0.156 | 0.142 | +0.039 | +0.025 | $4.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 79 | 0.838 | 0.825 | +0.036 | +0.023 | $14.33 | FUNDED_RESEARCH | $4 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
| Tampa Bay over 4.5 goals scored NO | 73 | 0.795 | 0.760 | +0.052 | +0.017 | $7.98 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (19.89 vs 4.86 bp); relationships: KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT05PHITB-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no: REINFORCING (phi 0.204); failure: TBL offense succeeds (4+ goals)
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05PHITB-TB3|no; why: higher confidence-adjusted growth (13.35 vs 2.78 bp); despite a smaller raw edge (+0.039 vs +0.083/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26OCT05PHITB-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT05PHITB-4|no; why: higher confidence-adjusted growth (7.30 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.992 vs 0.357); alternative not eligible: confidence-adjusted EV +0.0003 below the 0.010/contract floor; relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no: MOSTLY_INDEPENDENT (phi 0.024); failure: PHI offense succeeds (4+ goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no selected over player prop KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: REINFORCING (phi 0.204); KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05PHITB-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.024); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TBL:SUPPRESSED (p 0.3877): highest fidelity KXNHLTEAMTOTAL-26OCT05PHITB-TB4|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no — Broad expression KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no selected over player prop KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:OFFENSE_4PLUS (p 0.2804): highest fidelity KXNHLTEAMTOTAL-26OCT05PHITB-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4998): highest fidelity KXNHLGOAL-26OCT05PHITB-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT05PHITB-PHIPMARTONE94-1|no (same contract)
- KXNHLAST-26OCT05PHITB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 21.4 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3879, phi -0.236)
- KXNHLGOAL-26OCT05PHITB-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4998, phi -0.221)
- KXNHLGOAL-26OCT05PHITB-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.2804, phi -0.2)
- KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3879, phi -0.637)
- override: Broad expression KXNHLTEAMTOTAL-26OCT05PHITB-TB5|no selected over player prop KXNHLAST-26OCT05PHITB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 1.00 vs 0.70 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +10.68 (adj +1.97) on $38.38, P(profit) 0.6694, adj growth 16.9 bp · B EV +7.65 (adj +2.80) on $41.00, P(profit) 0.6628, adj growth 25.9 bp · C EV +9.33 (adj +3.41) on $50.00, P(profit) 0.6628, adj growth 31.0 bp · R EV +0.32 (adj +0.16) on $6.00, P(profit) 0.67, adj growth 6.0 bp

## OTT @ BOS  ·  10000 joint draws  ·  360 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_OTT_win | p_overtime | goals | shots BOS/OTT | BOS/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.52 | 0.48 | 0.00 | 5.99 | 27.2/27.7 | 24.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.51 | 0.49 | 0.48 | 5.91 | 27.3/27.9 | 24.6/23.9 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.105 | 0.48 | 0.52 | 0.00 | 5.97 | 21.7/33.1 | 29.3/18.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.47 | 5.9 | 21.7/33.1 | 29.6/18.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.58 | 0.42 | 0.00 | 9.12 | 28.8/29.3 | 23.6/22.4 | even strength |
| OTT shot control · high event (8+) · decided (2+) | 0.065 | 0.46 | 0.54 | 0.00 | 9.1 | 23.1/34.4 | 27.7/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Eklund: 1+ assists NO | 67 | 0.836 | 0.725 | +0.151 | +0.039 | $16.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Marat Khusnutdinov: 1+ goals YES | 11 | 0.153 | 0.140 | +0.036 | +0.023 | $5.04 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| JJ Peterka: 1+ assists NO | 69 | 0.782 | 0.734 | +0.077 | +0.029 | $16.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 9 | 0.115 | 0.106 | +0.019 | +0.010 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
- **William Eklund: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (15.92 vs 3.35 bp); relationships: KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: OTT offense succeeds (4+ goals)
- **Marat Khusnutdinov: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes; why: higher confidence-adjusted growth (11.11 vs 4.16 bp); despite a smaller raw edge (+0.036 vs +0.060/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: BOS offense suppressed (<= 2 goals)
- **JJ Peterka: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05OTTBOS-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (8.65 vs 0.83 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT05OTTBOS-OTTCGIROUX28-1|yes; why: higher confidence-adjusted growth (2.69 vs 2.16 bp); despite a smaller raw edge (+0.019 vs +0.047/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.10.
- thesis BOS:OFFENSE_4PLUS (p 0.3766): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSMGEEKIE39-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.4044): highest fidelity KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no (same contract)
- thesis OTT:SUPPRESSED (p 0.4181): highest fidelity KXNHLAST-26OCT05OTTBOS-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05OTTBOS-OTTTSTUTZLE18-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLAST-26OCT05OTTBOS-OTTWEKLUND27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.1 pts; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.3504, phi -0.167)
- KXNHLGOAL-26OCT05OTTBOS-BOSMKHUSNUTDINOV92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.4044, phi -0.189)
- KXNHLAST-26OCT05OTTBOS-BOSJPETERKA10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.3766, phi -0.209)
- KXNHLGOAL-26OCT05OTTBOS-OTTNCOUSINS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4181, phi -0.166)

portfolios: A EV +6.16 (adj +1.90) on $38.38, P(profit) 0.6246, adj growth 17.3 bp · B EV +7.43 (adj +2.85) on $40.12, P(profit) 0.742, adj growth 26.3 bp · C EV +6.32 (adj +2.68) on $42.59, P(profit) 0.6555, adj growth 23.6 bp · R EV +0.62 (adj +0.40) on $2.00, P(profit) 0.1533, adj growth 12.9 bp

## WPG @ PIT  ·  10000 joint draws  ·  346 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_WPG_win | p_overtime | goals | shots PIT/WPG | PIT/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.69 | 0.31 | 0.00 | 6.03 | 27.1/26.9 | 24.1/22.7 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.104 | 0.73 | 0.27 | 0.00 | 6.03 | 32.6/21.5 | 19.0/27.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 5.92 | 27.3/26.8 | 23.5/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.68 | 0.32 | 0.00 | 9.35 | 28.9/28.4 | 23.5/21.5 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.58 | 0.42 | 0.46 | 5.98 | 32.6/21.7 | 18.6/28.9 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.076 | 0.77 | 0.23 | 0.00 | 9.32 | 34.0/22.8 | 18.5/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 14 | 0.187 | 0.174 | +0.039 | +0.026 | $5.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Isak Rosen: 1+ goals NO | 87 | 0.896 | 0.888 | +0.018 | +0.011 | $16.40 | FUNDED_RESEARCH | $5 | WPG:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 12 | 0.147 | 0.138 | +0.019 | +0.010 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 33 | 0.367 | 0.357 | +0.022 | +0.011 | $3.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITRRAKELL67-1|yes; why: higher confidence-adjusted growth (11.33 vs 1.25 bp); relationships: KXNHLGOAL-26OCT05WPGPIT-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT05WPGPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: PIT offense suppressed (<= 2 goals)
- **Isak Rosen: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05WPGPIT-WPGJMORRISSEY44-1|no; why: higher confidence-adjusted growth (2.33 vs 0.01 bp); despite a smaller raw edge (+0.018 vs +0.029/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT05WPGPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: WPG offense succeeds (4+ goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (11.33 vs 2.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT05WPGPIT-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT05WPGPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (11.33 vs 1.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26OCT05WPGPIT-WPGIROSEN27-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, PIT shot control · normal event (5-7) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.5016): highest fidelity KXNHLGOAL-26OCT05WPGPIT-PITRRAKELL67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.4703): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT05WPGPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2942, phi -0.195)
- KXNHLGOAL-26OCT05WPGPIT-WPGIROSEN27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3122, phi -0.15)
- KXNHLGOAL-26OCT05WPGPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2942, phi -0.176)
- KXNHLGOAL-26OCT05WPGPIT-PITRRAKELL67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.2942, phi -0.247)

portfolios: A EV +3.69 (adj +2.27) on $34.86, P(profit) 0.5252, adj growth 18.8 bp · B EV +2.41 (adj +1.49) on $27.89, P(profit) 0.5211, adj growth 13.3 bp · C EV +1.85 (adj +1.23) on $7.07, P(profit) 0.1873, adj growth 10.6 bp · R EV +0.11 (adj +0.06) on $5.00, P(profit) 0.8964, adj growth 2.2 bp

## SJS @ DAL  ·  10000 joint draws  ·  364 bet sides mapped, 13 +EV candidates, 4 on card


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
| Kiefer Sherwood: 1+ goals YES | 14 | 0.190 | 0.176 | +0.041 | +0.028 | $5.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Mikko Rantanen: 1+ goals NO | 67 | 0.726 | 0.711 | +0.041 | +0.025 | $14.83 | FUNDED_RESEARCH | $4 | DAL:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ assists NO | 69 | 0.817 | 0.728 | +0.112 | +0.023 | $14.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Jason Robertson: 1+ goals NO | 59 | 0.632 | 0.619 | +0.025 | +0.012 | $5.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DAL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_STRONGER | D |
- **Kiefer Sherwood: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT05SJDAL-DAL2|no; why: higher confidence-adjusted growth (13.02 vs 4.87 bp); despite a smaller raw edge (+0.041 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: SJS offense suppressed (<= 2 goals)
- **Mikko Rantanen: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT05SJDAL-DALRHINTZ24-1|no; why: higher confidence-adjusted growth (6.51 vs 5.43 bp); despite a smaller raw edge (+0.041 vs +0.110/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: DAL offense succeeds (4+ goals)
- **Mason Marchment: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (5.62 vs 0.27 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0053 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: SJS offense succeeds (4+ goals)
- **Jason Robertson: 1+ goals NO** — thesis: DAL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no; why: Player prop expression KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no selected over broad KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: DAL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, DAL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis DAL:SUPPRESSED (p 0.3632): highest fidelity KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no — Player prop expression KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no selected over broad KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SJS:SUPPRESSED (p 0.4372): highest fidelity KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3415): highest fidelity KXNHLSPREAD-26OCT05SJDAL-DAL3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT05SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT05SJDAL-SJKSHERWOOD44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.4372, phi -0.204)
- KXNHLGOAL-26OCT05SJDAL-DALMRANTANEN96-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4226, phi -0.218)
- KXNHLAST-26OCT05SJDAL-SJMMARCHMENT27-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3415, phi -0.2)
- KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DAL:OFFENSE_4PLUS (p 0.4226, phi -0.261)
- override: Player prop expression KXNHLGOAL-26OCT05SJDAL-DALJROBERTSON21-1|no selected over broad KXNHLTEAMTOTAL-26OCT05SJDAL-DAL4|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.81 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.40 (adj +1.21) on $38.38, P(profit) 0.7635, adj growth 11.3 bp · B EV +5.01 (adj +2.17) on $41.00, P(profit) 0.6687, adj growth 19.8 bp · C EV +4.53 (adj +1.59) on $50.00, P(profit) 0.6969, adj growth 14.9 bp · R EV +0.24 (adj +0.15) on $4.00, P(profit) 0.726, adj growth 5.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
