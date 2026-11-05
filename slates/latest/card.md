# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T23:40:13Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.02 | +27.31 | +10.05 | +25.64 | 0.749 | -23.42 | -35.68 | 92.64 |
| B thesis-diversified (joint) ← optimiser card | 148.21 | +27.23 | +15.13 | +25.42 | 0.732 | -26.36 | -39.26 | 142.13 |
| C best expression per thesis | 150.01 | +24.81 | +12.22 | +22.90 | 0.711 | -27.39 | -39.67 | 113.77 |
| R FUNDED research stakes | 17.00 | +1.97 | +1.03 | +1.62 | 0.619 | -5.77 | -7.83 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.474 / away 0.526

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.119 | 0.57 | 0.43 | 0.00 | 6.03 | 27.1/27.4 | 24.3/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.47 | 5.93 | 27.3/27.6 | 24.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.56 | 0.44 | 0.00 | 9.44 | 28.7/29.0 | 23.0/22.4 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.097 | 0.50 | 0.50 | 0.00 | 6.01 | 21.9/32.9 | 29.3/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.48 | 0.52 | 0.47 | 5.95 | 21.9/32.9 | 29.7/18.7 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.070 | 0.51 | 0.49 | 0.00 | 9.42 | 23.4/34.9 | 28.4/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jake Evans: 1+ goals YES | 12 | 0.163 | 0.151 | +0.036 | +0.024 | $2.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists YES | 33 | 0.404 | 0.364 | +0.058 | +0.019 | $2.73 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
| Dylan Guenther: 1+ goals NO | 66 | 0.707 | 0.694 | +0.031 | +0.018 | $5.93 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Phillip Danault: 1+ goals YES | 12 | 0.150 | 0.139 | +0.023 | +0.012 | $1.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Jake Evans: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes; why: higher confidence-adjusted growth (10.77 vs 3.42 bp); despite a smaller raw edge (+0.036 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.037); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.027); KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.022); failure: MTL offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (10.77 vs 3.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.037); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.037); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.049); failure: MTL offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (3.35 vs 1.91 bp); despite a smaller raw edge (+0.031 vs +0.057/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.027); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: MOSTLY_INDEPENDENT (phi 0.031); failure: UTA offense succeeds (4+ goals)
- **Phillip Danault: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (10.77 vs 2.62 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.022); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.049); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.031); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MTL:OFFENSE_4PLUS (p 0.4411): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS_BY_2PLUS (p 0.3122): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS (p 0.5377): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3429, phi -0.189)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3429, phi -0.278)
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3949, phi -0.231)
- KXNHLGOAL-26NOV05UTAMTL-MTLPDANAULT24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3429, phi -0.184)

portfolios: A EV +1.74 (adj +0.72) on $13.84, P(profit) 0.4804, adj growth 6.8 bp · B EV +1.68 (adj +0.91) on $12.48, P(profit) 0.4584, adj growth 8.5 bp · C EV +1.99 (adj +1.06) on $15.29, P(profit) 0.4908, adj growth 9.8 bp · R EV +0.09 (adj +0.05) on $2.00, P(profit) 0.707, adj growth 2.0 bp

## VGK @ DET  ·  10000 joint draws  ·  416 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.430 / away 0.570

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.46 | 0.54 | 0.00 | 5.99 | 27.2/27.1 | 23.3/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.47 | 0.54 | 0.47 | 5.93 | 26.9/26.8 | 23.4/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.41 | 0.59 | 0.00 | 9.3 | 28.8/28.7 | 21.8/23.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.076 | 0.52 | 0.48 | 0.00 | 6.06 | 31.8/21.7 | 18.3/28.1 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.50 | 0.50 | 0.47 | 5.9 | 31.9/21.5 | 18.2/28.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.062 | 0.33 | 0.67 | 0.00 | 6.0 | 21.5/31.7 | 27.3/18.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.076 | 0.066 | +0.023 | +0.012 | $1.21 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Justin Faulk: 1+ assists YES | 25 | 0.314 | 0.279 | +0.051 | +0.016 | $2.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Andrew Copp: 1+ goals YES | 16 | 0.191 | 0.181 | +0.022 | +0.012 | $1.50 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Lucas Raymond: 1+ assists NO | 58 | 0.644 | 0.610 | +0.047 | +0.013 | $4.32 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV05VGKDET-8|yes; why: higher confidence-adjusted growth (6.52 vs 0.02 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.852 vs 0.334); alternative not eligible: confidence-adjusted EV +0.0014 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05VGKDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: VGK offense suppressed (<= 2 goals)
- **Justin Faulk: 1+ assists YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VGKDET-DETACOPP18-1|yes; why: higher confidence-adjusted growth (2.94 vs 2.09 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05VGKDET-DETACOPP18-1|yes: MOSTLY_INDEPENDENT (phi 0.125); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.054); failure: DET offense suppressed (<= 2 goals)
- **Andrew Copp: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes has the higher standalone adjusted growth (2.94 vs 2.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.125); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes: MOSTLY_INDEPENDENT (phi 0.125); KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: INTENTIONAL_DIVERSIFIER (phi -0.151); failure: DET offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-2|no; why: higher confidence-adjusted growth (1.43 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.054); KXNHLGOAL-26NOV05VGKDET-DETACOPP18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.151); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis DET:OFFENSE_4PLUS (p 0.3583): highest fidelity KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4209): highest fidelity KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.421): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3605, phi -0.123)
- KXNHLAST-26NOV05VGKDET-DETJFAULK72-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4209, phi -0.27)
- KXNHLGOAL-26NOV05VGKDET-DETACOPP18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4209, phi -0.239)
- KXNHLAST-26NOV05VGKDET-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3583, phi -0.278)

portfolios: A EV +2.29 (adj +0.92) on $13.76, P(profit) 0.4138, adj growth 8.3 bp · B EV +1.45 (adj +0.61) on $9.13, P(profit) 0.3355, adj growth 5.7 bp · C EV +0.88 (adj +0.26) on $7.19, P(profit) 0.7678, adj growth 2.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.793 / away 0.207

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.177 | 0.84 | 0.16 | 0.00 | 6.05 | 32.9/20.4 | 18.5/27.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.123 | 0.85 | 0.15 | 0.00 | 9.33 | 34.7/22.0 | 18.3/25.4 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.60 | 0.40 | 0.48 | 5.95 | 33.1/20.8 | 17.6/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.099 | 0.80 | 0.20 | 0.00 | 6.03 | 27.2/26.4 | 24.1/22.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.79 | 0.21 | 0.00 | 9.38 | 28.9/27.8 | 23.5/20.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.52 | 0.48 | 0.47 | 6.01 | 27.4/26.6 | 23.3/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 18 | 0.234 | 0.219 | +0.044 | +0.029 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Tampa Bay over 3.5 goals scored NO | 33 | 0.422 | 0.373 | +0.076 | +0.028 | $5.43 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Max Crozier: 1+ goals YES | 5 | 0.075 | 0.066 | +0.022 | +0.013 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:OFFENSE_4PLUS | FRAGILE (0.10) | EVIDENCE_STRONGER | D |
| Arvid Soderblom: 28+ saves NO | 53 | 0.618 | 0.569 | +0.071 | +0.022 | $6.45 | FUNDED_RESEARCH | $2 | CHI:NET_LOW_VOLUME | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (11.77 vs 6.59 bp); despite a smaller raw edge (+0.044 vs +0.077/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CHITB-TBMCROZIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: MOSTLY_INDEPENDENT (phi -0.01); failure: CHI offense suppressed (<= 2 goals)
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (7.51 vs 6.59 bp); despite a smaller raw edge (+0.076 vs +0.077/contract); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CHITB-TBMCROZIER24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: INTENTIONAL_DIVERSIFIER (phi -0.141); failure: TBL offense succeeds (4+ goals)
- **Max Crozier: 1+ goals YES** — thesis: TBL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05CHITB-TBACIRELLI71-1|yes; why: higher confidence-adjusted growth (7.13 vs 0.29 bp); despite a smaller raw edge (+0.022 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0055 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: INTENTIONAL_DIVERSIFIER (phi -0.114); KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: MOSTLY_INDEPENDENT (phi 0.026); failure: TBL offense suppressed (<= 2 goals)
- **Arvid Soderblom: 28+ saves NO** — thesis: CHI net faces light volume (<= 25 shots; TBL suppressed); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: INTENTIONAL_DIVERSIFIER (phi -0.141); KXNHLGOAL-26NOV05CHITB-TBMCROZIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.026); failure: CHI net faces heavy volume (33+ shots; TBL pressure)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.18, TBL shot control · high event (8+) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.2358): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2372): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no (same contract)
- thesis GAME:TIGHT (p 0.3717): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5572, phi -0.272)
- KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.57, phi -0.983)
- KXNHLGOAL-26NOV05CHITB-TBMCROZIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 90% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:SUPPRESSED (p 0.2372, phi -0.107)
- KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); fragile player expression; opposing: failure thesis CHI:NET_HIGH_VOLUME (p 0.3425, phi -0.704)

portfolios: A EV +2.64 (adj +0.72) on $13.84, P(profit) 0.5552, adj growth 6.7 bp · B EV +3.49 (adj +1.62) on $17.09, P(profit) 0.4605, adj growth 15.2 bp · C EV +3.28 (adj +1.44) on $17.85, P(profit) 0.4092, adj growth 13.4 bp · R EV +0.70 (adj +0.24) on $4.00, P(profit) 0.4218, adj growth 8.8 bp

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 14 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.669 / away 0.331

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.127 | 0.65 | 0.35 | 0.00 | 6.01 | 33.5/21.7 | 19.0/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.54 | 0.46 | 0.46 | 5.88 | 33.6/21.6 | 18.5/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.107 | 0.56 | 0.44 | 0.00 | 6.02 | 27.8/27.1 | 23.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.50 | 0.50 | 0.51 | 5.92 | 27.8/27.1 | 24.0/24.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 9.28 | 35.0/22.7 | 17.7/27.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.62 | 0.38 | 0.00 | 9.31 | 29.4/28.7 | 23.3/22.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 19 | 0.267 | 0.247 | +0.066 | +0.046 | $5.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 58 | 0.648 | 0.630 | +0.051 | +0.033 | $8.80 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.302 | 0.288 | +0.039 | +0.025 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
| Dougie Hamilton: 1+ assists YES | 29 | 0.356 | 0.318 | +0.051 | +0.013 | $2.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.49) | EVIDENCE_MIXED | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (28.04 vs 6.92 bp); relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (9.66 vs 4.29 bp); despite a smaller raw edge (+0.051 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.01 vs 0.88); relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.115); failure: NJD offense succeeds (4+ goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (28.04 vs 6.92 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.012); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: STL offense suppressed (<= 2 goals)
- **Dougie Hamilton: 1+ assists YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05STLNJ-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (1.85 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: INTENTIONAL_DIVERSIFIER (phi -0.115); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3312): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4222): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3464): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4416, phi -0.261)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4401, phi -0.247)
- KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4416, phi -0.274)
- KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 51% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3464, phi -0.259)

portfolios: A EV +3.33 (adj +1.41) on $13.84, P(profit) 0.5245, adj growth 12.9 bp · B EV +3.59 (adj +2.23) on $20.53, P(profit) 0.5498, adj growth 21.0 bp · C EV +4.07 (adj +2.37) on $22.00, P(profit) 0.5057, adj growth 22.0 bp · R EV +0.25 (adj +0.16) on $3.00, P(profit) 0.6478, adj growth 6.1 bp

## CAR @ NYI  ·  10000 joint draws  ·  424 bet sides mapped, 19 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.363 / away 0.637

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.119 | 0.43 | 0.57 | 0.00 | 6.02 | 21.1/32.5 | 28.4/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.48 | 0.52 | 0.00 | 6.02 | 26.4/27.1 | 23.5/23.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.46 | 0.54 | 0.45 | 5.99 | 21.3/32.8 | 29.4/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.46 | 5.97 | 26.8/27.5 | 24.1/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.48 | 0.52 | 0.00 | 9.35 | 28.3/28.8 | 22.8/22.4 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.084 | 0.40 | 0.60 | 0.00 | 9.26 | 22.4/34.6 | 27.2/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sebastian Aho: 1+ goals NO | 67 | 0.733 | 0.715 | +0.048 | +0.029 | $8.80 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.159 | +0.032 | +0.021 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 14 | 0.180 | 0.169 | +0.032 | +0.020 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: higher confidence-adjusted growth (8.84 vs 5.13 bp); despite a smaller raw edge (+0.048 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.001 vs 0.555); relationships: KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: CAR offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 7.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 7.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.130); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:OFFENSE_4PLUS (p 0.3798): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2786): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2671): highest fidelity KXNHLSPREAD-26NOV05CARNYI-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4179, phi -0.239)
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.205)
- KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.208)

portfolios: A EV +2.74 (adj +0.62) on $13.84, P(profit) 0.5401, adj growth 5.3 bp · B EV +1.68 (adj +1.07) on $13.62, P(profit) 0.3175, adj growth 10.1 bp · C EV +2.33 (adj +1.10) on $12.72, P(profit) 0.7728, adj growth 10.3 bp · R EV +0.21 (adj +0.13) on $3.00, P(profit) 0.7332, adj growth 4.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.571 / away 0.429

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_PHI_win | p_overtime | goals | shots NYR/PHI | NYR/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.55 | 0.45 | 0.00 | 6.03 | 26.5/26.4 | 23.2/22.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.47 | 5.88 | 26.2/26.3 | 22.9/23.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.078 | 0.57 | 0.43 | 0.00 | 9.19 | 27.8/27.7 | 22.3/21.5 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.073 | 0.64 | 0.36 | 0.00 | 6.0 | 30.5/20.6 | 17.8/26.3 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.56 | 0.44 | 0.44 | 5.86 | 31.1/20.9 | 17.8/27.7 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.065 | 0.50 | 0.50 | 0.00 | 5.96 | 21.0/30.6 | 27.0/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $2.82 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.743 | 0.702 | +0.058 | +0.016 | $8.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Travis Sanheim: 1+ assists YES | 25 | 0.306 | 0.275 | +0.043 | +0.012 | $1.56 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_MIXED | D |
| Will Cuylle: 1+ goals NO | 77 | 0.803 | 0.792 | +0.021 | +0.010 | $5.31 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (4.95 vs 1.69 bp); despite a smaller raw edge (+0.029 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.68 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense succeeds (4+ goals)
- **Travis Sanheim: 1+ assists YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes has the higher standalone adjusted growth (4.95 vs 1.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.122); they share one thesis budget; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.122); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.079); KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: PHI offense suppressed (<= 2 goals)
- **Will Cuylle: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05PHINYR-NYR4|no; why: higher confidence-adjusted growth (1.31 vs 0.17 bp); despite a smaller raw edge (+0.021 vs +0.031/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.994 vs 0.869); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4576): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.3983): highest fidelity KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no (same contract)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.232)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.222)
- KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.269)
- KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no: FUNDED_RESEARCH; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3829, phi -0.222)

portfolios: A EV +1.32 (adj +0.51) on $13.84, P(profit) 0.4053, adj growth 4.8 bp · B EV +1.60 (adj +0.64) on $18.45, P(profit) 0.736, adj growth 6.0 bp · C EV +1.57 (adj +0.67) on $19.61, P(profit) 0.6956, adj growth 6.2 bp · R EV +0.05 (adj +0.03) on $2.00, P(profit) 0.8033, adj growth 0.9 bp

## BOS @ PIT  ·  10000 joint draws  ·  472 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.515 / away 0.485

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.54 | 0.46 | 0.00 | 6.08 | 27.6/27.3 | 23.9/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.113 | 0.52 | 0.48 | 0.00 | 9.5 | 29.1/28.9 | 22.6/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.107 | 0.62 | 0.38 | 0.00 | 6.07 | 33.1/21.9 | 19.0/28.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.48 | 0.52 | 0.48 | 6.01 | 27.7/27.4 | 24.0/24.4 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.088 | 0.59 | 0.41 | 0.00 | 9.41 | 34.8/23.0 | 17.7/27.3 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.56 | 0.44 | 0.48 | 5.95 | 33.2/22.0 | 18.7/29.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.189 | 0.170 | +0.061 | +0.043 | $4.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.153 | 0.136 | +0.047 | +0.030 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Mark Kastelic: 1+ goals YES | 9 | 0.119 | 0.111 | +0.024 | +0.015 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BOS:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 32 | 0.373 | 0.359 | +0.038 | +0.023 | $3.66 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (35.01 vs 20.24 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLGOAL-26NOV05BOSPIT-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 20.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.034); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLGOAL-26NOV05BOSPIT-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: PIT offense suppressed (<= 2 goals)
- **Mark Kastelic: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (5.59 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0052 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: BOS offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 5.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV05BOSPIT-BOSMKASTELIC47-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, PIT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.329): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4699): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3763): highest fidelity KXNHLAST-26NOV05BOSPIT-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3206, phi -0.211)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3206, phi -0.187)
- KXNHLGOAL-26NOV05BOSPIT-BOSMKASTELIC47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3763, phi -0.157)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3206, phi -0.247)

portfolios: A EV +3.54 (adj +2.10) on $13.84, P(profit) 0.3084, adj growth 20.0 bp · B EV +4.46 (adj +2.97) on $13.13, P(profit) 0.3921, adj growth 27.8 bp · C EV +3.92 (adj +2.26) on $18.96, P(profit) 0.5589, adj growth 20.9 bp · R EV +0.11 (adj +0.07) on $1.00, P(profit) 0.3732, adj growth 2.6 bp

## DAL @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 6 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.462 / away 0.538

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.50 | 0.50 | 0.00 | 6.02 | 26.0/25.8 | 22.4/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.51 | 0.49 | 0.49 | 5.95 | 25.9/25.9 | 22.5/22.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.53 | 0.47 | 0.00 | 9.25 | 27.3/27.4 | 21.8/21.0 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.074 | 0.60 | 0.40 | 0.00 | 5.96 | 30.3/20.3 | 17.3/26.4 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.069 | 0.45 | 0.55 | 0.00 | 6.01 | 20.8/30.7 | 26.8/17.8 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.58 | 0.42 | 0.49 | 5.91 | 30.2/20.4 | 17.3/26.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mathieu Olivier: 1+ goals YES | 16 | 0.210 | 0.197 | +0.041 | +0.027 | $2.30 | FUNDED_RESEARCH | $1 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.283 | 0.269 | +0.041 | +0.026 | $3.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.108 | 0.099 | +0.023 | +0.014 | $1.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: higher confidence-adjusted growth (11.28 vs 3.18 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.293); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.28 vs 8.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.28 vs 5.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.236)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.245)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.141)

portfolios: A EV +2.30 (adj +1.43) on $11.82, P(profit) 0.6242, adj growth 13.3 bp · B EV +1.57 (adj +1.00) on $7.43, P(profit) 0.4958, adj growth 9.5 bp · C EV +0.96 (adj +0.63) on $3.96, P(profit) 0.2104, adj growth 5.9 bp · R EV +0.24 (adj +0.16) on $1.00, P(profit) 0.2104, adj growth 5.9 bp

## VAN @ WPG  ·  10000 joint draws  ·  398 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| WPG shot control · normal event (5-7) · decided (2+) | 0.118 | 0.63 | 0.37 | 0.00 | 6.02 | 32.6/21.0 | 18.1/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.56 | 0.44 | 0.00 | 5.95 | 27.5/26.9 | 23.5/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.104 | 0.51 | 0.49 | 0.44 | 5.92 | 27.5/27.1 | 23.8/24.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.59 | 0.41 | 0.46 | 5.97 | 32.7/21.4 | 18.2/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.56 | 0.44 | 0.00 | 9.34 | 28.6/28.0 | 22.0/22.0 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.081 | 0.64 | 0.36 | 0.00 | 9.2 | 34.0/22.6 | 17.9/26.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Marco Rossi: 1+ goals YES | 16 | 0.220 | 0.202 | +0.051 | +0.032 | $3.79 | FUNDED_RESEARCH | $1 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 17 | 0.230 | 0.211 | +0.050 | +0.032 | $3.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Liam Ohgren: 1+ goals YES | 14 | 0.179 | 0.168 | +0.031 | +0.020 | $2.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: higher confidence-adjusted growth (15.78 vs 14.57 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes has the higher standalone adjusted growth (15.78 vs 14.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes has the higher standalone adjusted growth (15.78 vs 11.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.023); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes has the higher standalone adjusted growth (15.78 vs 6.80 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts WPG shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.354): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2433): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.3501): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no (same contract)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.424, phi -0.212)
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.424, phi -0.229)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.424, phi -0.203)
- KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.424, phi -0.189)

portfolios: A EV +2.21 (adj +0.41) on $13.84, P(profit) 0.566, adj growth 3.5 bp · B EV +3.53 (adj +2.26) on $12.68, P(profit) 0.5799, adj growth 21.2 bp · C EV +1.87 (adj +1.02) on $6.37, P(profit) 0.3852, adj growth 9.5 bp · R EV +0.30 (adj +0.19) on $1.00, P(profit) 0.2204, adj growth 7.1 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05VANWPG-WPG|no == KXNHLGAME-26NOV05VANWPG-VAN|yes

## ANA @ EDM  ·  10000 joint draws  ·  466 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.629 / away 0.371

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.134 | 0.62 | 0.38 | 0.00 | 9.65 | 29.5/29.5 | 23.7/22.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.60 | 0.40 | 0.00 | 6.12 | 28.0/28.0 | 24.8/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.53 | 0.47 | 0.47 | 6.05 | 28.0/27.9 | 24.6/24.4 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 9.52 | 34.7/23.9 | 18.9/27.1 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.60 | 9.78 | 30.0/30.0 | 23.4/23.6 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.064 | 0.66 | 0.34 | 0.00 | 6.08 | 32.9/22.1 | 19.5/28.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $1.92 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 29 | 0.410 | 0.329 | +0.105 | +0.024 | $3.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.166 | 0.156 | +0.029 | +0.018 | $2.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.188 | +0.029 | +0.018 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.37 vs 5.23 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (6.02 vs 3.54 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense succeeds (4+ goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (5.97 vs 5.23 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (5.23 vs 4.50 bp); despite a smaller raw edge (+0.029 vs +0.035/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2668): highest fidelity KXNHLPTS-26NOV05ANAEDM-EDMLDRAISAITL29-3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4343): highest fidelity KXNHLSPREAD-26NOV05ANAEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.433): highest fidelity KXNHLSPREAD-26NOV05ANAEDM-EDM3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.148)
- KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5288, phi -0.319)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.175)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.206)

portfolios: A EV +3.43 (adj +0.52) on $13.84, P(profit) 0.54, adj growth 4.7 bp · B EV +2.56 (adj +1.16) on $9.83, P(profit) 0.6548, adj growth 10.9 bp · C EV +2.45 (adj +0.89) on $11.11, P(profit) 0.7069, adj growth 8.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.657 / away 0.343

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.148 | 0.75 | 0.25 | 0.00 | 6.04 | 34.7/22.2 | 19.9/29.7 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.120 | 0.76 | 0.24 | 0.00 | 9.41 | 37.0/23.8 | 19.4/28.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.58 | 0.42 | 0.50 | 5.98 | 35.4/22.8 | 19.6/31.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.69 | 0.31 | 0.00 | 6.07 | 29.1/28.2 | 25.6/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.73 | 0.27 | 0.00 | 9.44 | 30.9/29.8 | 24.7/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.54 | 0.46 | 0.48 | 6.03 | 29.4/28.6 | 25.2/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mavrik Bourque: 1+ assists NO | 72 | 0.796 | 0.755 | +0.062 | +0.021 | $8.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.070 | 0.064 | +0.016 | +0.010 | $1.10 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.156 | 0.148 | +0.018 | +0.010 | $1.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Nathan MacKinnon: 1+ assists NO | 40 | 0.473 | 0.431 | +0.056 | +0.015 | $2.66 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.73) | EVIDENCE_MIXED | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.13 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: NSH offense succeeds (4+ goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (4.41 vs 1.98 bp); despite a smaller raw edge (+0.016 vs +0.018/contract); relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26NOV05NSHCOL-NSH2|yes; why: higher confidence-adjusted growth (1.98 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: NSH offense suppressed (<= 2 goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05NSHCOL-COLCMAKAR8-2|no; why: higher confidence-adjusted growth (1.93 vs 0.68 bp); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4705): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3136): highest fidelity KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes (same contract)
- thesis COL:SUPPRESSED (p 0.256): highest fidelity KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3136, phi -0.2)
- KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.122)
- KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.216)
- KXNHLAST-26NOV05NSHCOL-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 27% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5392, phi -0.308)

portfolios: A EV +1.77 (adj +0.69) on $13.72, P(profit) 0.4969, adj growth 6.4 bp · B EV +1.60 (adj +0.66) on $13.84, P(profit) 0.4969, adj growth 6.2 bp · C EV +1.49 (adj +0.52) on $14.95, P(profit) 0.4574, adj growth 4.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
