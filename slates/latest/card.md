# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-28T19:25:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.76 | +7.63 | +25.59 | 0.674 | -44.80 | -62.78 | 61.08 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +28.08 | +16.32 | +24.15 | 0.641 | -54.52 | -65.70 | 141.84 |
| C best expression per thesis | 112.72 | +19.89 | +10.49 | +14.02 | 0.598 | -43.75 | -56.23 | 91.07 |
| R FUNDED research stakes | 18.00 | +2.99 | +1.59 | +1.51 | 0.579 | -10.71 | -11.36 | 0.00 |

## PHI @ WSH  ·  10000 joint draws  ·  488 bet sides mapped, 22 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.673 / away 0.327

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_PHI_win | p_overtime | goals | shots WSH/PHI | WSH/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.60 | 0.40 | 0.00 | 5.96 | 26.5/26.4 | 23.2/22.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.52 | 0.48 | 0.50 | 5.88 | 26.8/26.5 | 23.4/23.6 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.093 | 0.63 | 0.37 | 0.00 | 5.97 | 31.5/21.0 | 18.2/27.3 | even strength |
| WSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.56 | 0.44 | 0.47 | 5.86 | 31.9/21.2 | 18.2/28.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.59 | 0.41 | 0.00 | 9.25 | 28.3/28.0 | 22.6/21.5 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.58 | 0.42 | 0.00 | 3.47 | 25.4/25.1 | 23.5/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Couturier: 1+ goals YES | 10 | 0.145 | 0.133 | +0.039 | +0.026 | $6.45 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Aliaksei Protas: 1+ goals YES | 18 | 0.239 | 0.222 | +0.049 | +0.032 | $8.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 16 | 0.209 | 0.196 | +0.040 | +0.026 | $7.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jordan Kyrou: 1+ goals NO | 74 | 0.784 | 0.772 | +0.031 | +0.018 | $19.47 | FUNDED_RESEARCH | $5 | WSH:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
- **Sean Couturier: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes; why: higher confidence-adjusted growth (15.41 vs 10.49 bp); despite a smaller raw edge (+0.039 vs +0.040/contract); relationships: KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes; why: higher confidence-adjusted growth (14.00 vs 1.34 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.015); failure: WSH offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes has the higher standalone adjusted growth (15.41 vs 10.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: PHI offense suppressed (<= 2 goals)
- **Jordan Kyrou: 1+ goals NO** — thesis: WSH offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no; why: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: WSH offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WSH shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:OFFENSE_4PLUS (p 0.304): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-PHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:OFFENSE_4PLUS (p 0.4038): highest fidelity KXNHLAST-26OCT28PHIWSH-WSHRLEONARD9-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WSH:SUPPRESSED (p 0.3834): highest fidelity KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no — Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLGOAL-26OCT28PHIWSH-PHISCOUTURIER14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.199)
- KXNHLGOAL-26OCT28PHIWSH-WSHAPROTAS21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.3834, phi -0.24)
- KXNHLGOAL-26OCT28PHIWSH-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4725, phi -0.216)
- KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:OFFENSE_4PLUS (p 0.4038, phi -0.234)
- override: Player prop expression KXNHLGOAL-26OCT28PHIWSH-WSHJKYROU25-1|no selected over broad KXNHLTEAMTOTAL-26OCT28PHIWSH-WSH3|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.90 vs 0.97 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.88 (adj +1.40) on $37.50, P(profit) 0.5627, adj growth 9.4 bp · B EV +7.08 (adj +4.63) on $41.85, P(profit) 0.4564, adj growth 40.1 bp · C EV +8.00 (adj +4.41) on $33.94, P(profit) 0.6284, adj growth 38.2 bp · R EV +0.20 (adj +0.12) on $5.00, P(profit) 0.7843, adj growth 4.3 bp
equivalent contracts collapsed: KXNHLGAME-26OCT28PHIWSH-WSH|no == KXNHLGAME-26OCT28PHIWSH-PHI|yes

## CGY @ EDM  ·  10000 joint draws  ·  488 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.627 / away 0.373

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_CGY_win | p_overtime | goals | shots EDM/CGY | EDM/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.73 | 0.27 | 0.00 | 6.05 | 28.9/28.4 | 25.8/24.2 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.113 | 0.77 | 0.23 | 0.00 | 6.07 | 34.3/22.4 | 20.2/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.107 | 0.70 | 0.30 | 0.00 | 9.49 | 30.4/30.0 | 24.8/22.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.096 | 0.77 | 0.23 | 0.00 | 9.42 | 36.0/24.0 | 19.7/27.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.55 | 0.45 | 0.47 | 5.96 | 28.9/28.4 | 25.1/25.5 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.59 | 0.41 | 0.46 | 5.92 | 34.7/22.8 | 19.7/31.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 14 | 0.207 | 0.185 | +0.058 | +0.037 | $9.43 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Connor McDavid: 2+ goals YES | 11 | 0.165 | 0.149 | +0.048 | +0.032 | $7.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ryan Shea: 1+ goals YES | 6 | 0.083 | 0.076 | +0.019 | +0.012 | $2.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 10 | 0.129 | 0.121 | +0.023 | +0.014 | $3.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: higher confidence-adjusted growth (22.64 vs 21.18 bp); wins across more scripts (relative breadth 0.826 vs 0.719); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-EDMRSHEA6-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 2+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28CGYEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (21.18 vs 5.10 bp); despite a smaller raw edge (+0.048 vs +0.106/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28CGYEDM-EDMRSHEA6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: EDM offense suppressed (<= 2 goals)
- **Ryan Shea: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes has the higher standalone adjusted growth (21.18 vs 5.33 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: EDM offense suppressed (<= 2 goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes; why: higher confidence-adjusted growth (4.63 vs 2.85 bp); despite a smaller raw edge (+0.023 vs +0.024/contract); relationships: KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT28CGYEDM-EDMRSHEA6-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, EDM shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5559): highest fidelity KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes — override declined: the joint re-optimisation gives KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes less than the minimum stake; KXNHLGOAL-26OCT28CGYEDM-EDMRSHEA6-1|yes kept
- thesis EDM:SUPPRESSED (p 0.2493): highest fidelity KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT28CGYEDM-EDMCMCDAVID97-2|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.318): highest fidelity KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28CGYEDM-CGYASUNIEV61-1|yes (same contract)
- KXNHLGOAL-26OCT28CGYEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.178)
- KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.228)
- KXNHLGOAL-26OCT28CGYEDM-EDMRSHEA6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2493, phi -0.109)
- KXNHLGOAL-26OCT28CGYEDM-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4641, phi -0.195)
- override: override declined: the joint re-optimisation gives KXNHLGOAL-26OCT28CGYEDM-EDMCMCDAVID97-1|yes less than the minimum stake; KXNHLGOAL-26OCT28CGYEDM-EDMRSHEA6-1|yes kept

portfolios: A EV +8.94 (adj +3.62) on $37.50, P(profit) 0.6095, adj growth 31.0 bp · B EV +8.69 (adj +5.57) on $24.12, P(profit) 0.4768, adj growth 48.0 bp · C EV +5.08 (adj +2.86) on $26.58, P(profit) 0.2933, adj growth 24.6 bp · R EV +1.18 (adj +0.74) on $3.00, P(profit) 0.2067, adj growth 24.4 bp

## NJD @ COL  ·  10000 joint draws  ·  462 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.572 / away 0.428

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NJD_win | p_overtime | goals | shots COL/NJD | COL/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.68 | 0.32 | 0.00 | 6.05 | 28.8/28.6 | 25.8/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.57 | 0.43 | 0.46 | 5.9 | 28.5/28.6 | 25.3/25.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.097 | 0.68 | 0.32 | 0.00 | 9.32 | 30.3/30.3 | 25.3/22.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.72 | 0.28 | 0.00 | 6.0 | 33.8/23.1 | 20.5/28.9 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.49 | 5.85 | 34.0/23.0 | 19.9/30.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.063 | 0.75 | 0.25 | 0.00 | 9.22 | 35.4/24.2 | 20.0/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Amadeus Lombardi: 1+ goals YES | 9 | 0.123 | 0.114 | +0.028 | +0.018 | $4.51 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Nicolas Roy: 1+ assists NO | 82 | 0.900 | 0.850 | +0.070 | +0.020 | $19.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.96) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $12.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Jake Allen: 27+ saves NO | 52 | 0.603 | 0.554 | +0.066 | +0.017 | $9.30 | FUNDED_RESEARCH | $3 | NJD:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes; why: higher confidence-adjusted growth (8.02 vs 2.11 bp); relationships: KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.021); failure: NJD offense suppressed (<= 2 goals)
- **Nicolas Roy: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT28NJCOL-COLCMAKAR8-1|no; why: higher confidence-adjusted growth (6.01 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi -0.028); failure: COL offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no; why: higher confidence-adjusted growth (2.58 vs 2.39 bp); relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: MOSTLY_INDEPENDENT (phi 0.032); failure: NJD offense succeeds (4+ goals)
- **Jake Allen: 27+ saves NO** — thesis: NJD net faces light volume (<= 25 shots; COL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.021); KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.032); failure: NJD net faces heavy volume (33+ shots; COL pressure)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis NJD:SUPPRESSED (p 0.4797): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJTMEIER28-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:NET_LOW_VOLUME (p 0.3032): highest fidelity KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no [STRUCTURAL], best adjusted EV KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3008): highest fidelity KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28NJCOL-NJCBROWN16-1|yes (same contract)
- KXNHLGOAL-26OCT28NJCOL-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4797, phi -0.174)
- KXNHLAST-26OCT28NJCOL-COLNROY10-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.4821, phi -0.134)
- KXNHLGOAL-26OCT28NJCOL-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3008, phi -0.248)
- KXNHLSAVE-26OCT28NJCOL-NJJALLEN34-27|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis NJD:NET_HIGH_VOLUME (p 0.2768, phi -0.626)

portfolios: A EV +3.96 (adj +0.88) on $37.50, P(profit) 0.733, adj growth 7.9 bp · B EV +4.56 (adj +1.88) on $45.60, P(profit) 0.4714, adj growth 16.7 bp · C EV +2.10 (adj +0.81) on $24.96, P(profit) 0.515, adj growth 7.1 bp · R EV +0.37 (adj +0.09) on $3.00, P(profit) 0.6034, adj growth 3.1 bp

## TOR @ SEA  ·  10000 joint draws  ·  438 bet sides mapped, 20 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.446 / away 0.554

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_TOR_win | p_overtime | goals | shots SEA/TOR | SEA/TOR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.59 | 0.41 | 0.00 | 6.06 | 29.3/29.1 | 25.8/25.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.51 | 0.49 | 0.46 | 6.02 | 29.3/29.2 | 25.8/26.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.108 | 0.59 | 0.41 | 0.00 | 9.49 | 31.0/31.0 | 25.1/24.0 | even strength |
| SEA shot control · normal event (5-7) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 6.03 | 34.4/23.2 | 20.2/30.0 | even strength |
| SEA shot control · high event (8+) · decided (2+) | 0.067 | 0.66 | 0.34 | 0.00 | 9.38 | 36.2/24.9 | 19.9/28.3 | even strength |
| SEA shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.56 | 0.44 | 0.44 | 5.98 | 34.4/23.4 | 20.1/31.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.156 | 0.142 | +0.040 | +0.025 | $7.13 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Berkly Catton: 1+ goals YES | 16 | 0.219 | 0.198 | +0.050 | +0.029 | $7.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Toronto wins by over 1.5 goals NO | 67 | 0.763 | 0.714 | +0.077 | +0.028 | $19.53 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ryan Winterton: 1+ goals YES | 13 | 0.169 | 0.158 | +0.031 | +0.020 | $4.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT28TORSEA-TORMRIELLY44-1|yes; why: higher confidence-adjusted growth (13.43 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: INTENTIONAL_DIVERSIFIER (phi -0.172); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: TOR offense suppressed (<= 2 goals)
- **Berkly Catton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: higher confidence-adjusted growth (12.58 vs 8.24 bp); despite a smaller raw edge (+0.050 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Toronto wins by over 1.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR3|no; why: higher confidence-adjusted growth (8.24 vs 6.02 bp); relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.172); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.135); KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.1); failure: TOR wins by 2+
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT28TORSEA-TOR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT28TORSEA-TOR2|no has the higher standalone adjusted growth (8.24 vs 7.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.100); they share one thesis budget; relationships: KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLSPREAD-26OCT28TORSEA-TOR2|no: MOSTLY_INDEPENDENT (phi 0.1); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3882): highest fidelity KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes (same contract)
- thesis SEA:OFFENSE_4PLUS (p 0.4677): highest fidelity KXNHLTEAMTOTAL-26OCT28TORSEA-SEA4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:SUPPRESSED (p 0.3912): highest fidelity KXNHLSPREAD-26OCT28TORSEA-TOR3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT28TORSEA-TOR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT28TORSEA-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3912, phi -0.2)
- KXNHLGOAL-26OCT28TORSEA-SEABCATTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3252, phi -0.198)
- KXNHLSPREAD-26OCT28TORSEA-TOR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TOR:WINS_BY_2PLUS (p 0.2372, phi -1.0)
- KXNHLGOAL-26OCT28TORSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3252, phi -0.176)

portfolios: A EV +6.98 (adj +1.73) on $37.50, P(profit) 0.4787, adj growth 12.7 bp · B EV +7.74 (adj +4.24) on $38.43, P(profit) 0.44, adj growth 37.0 bp · C EV +4.70 (adj +2.41) on $27.24, P(profit) 0.8264, adj growth 21.3 bp · R EV +1.24 (adj +0.64) on $7.00, P(profit) 0.8264, adj growth 22.4 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
