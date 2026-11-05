# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T14:01:35Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +26.21 | +9.56 | +25.17 | 0.719 | -29.01 | -43.03 | 86.15 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +26.78 | +14.90 | +24.14 | 0.700 | -31.62 | -46.25 | 137.72 |
| C best expression per thesis | 149.98 | +24.64 | +12.61 | +21.48 | 0.683 | -34.02 | -48.37 | 114.59 |
| R FUNDED research stakes | 19.00 | +2.72 | +1.33 | +1.47 | 0.596 | -6.94 | -8.18 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  422 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.54 | 0.46 | 0.00 | 6.05 | 27.3/27.7 | 24.3/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.53 | 0.47 | 0.46 | 6.0 | 27.3/27.8 | 24.5/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.57 | 0.43 | 0.00 | 9.41 | 28.6/29.0 | 23.3/21.9 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.094 | 0.47 | 0.53 | 0.00 | 6.04 | 21.7/32.9 | 29.0/18.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.50 | 0.50 | 0.46 | 5.91 | 21.8/33.1 | 29.8/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.075 | 0.43 | 0.57 | 0.00 | 9.34 | 23.3/34.7 | 27.7/18.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 17 | 0.233 | 0.216 | +0.053 | +0.036 | $5.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Josh Anderson: 1+ goals YES | 18 | 0.229 | 0.214 | +0.039 | +0.024 | $3.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 14 | 0.173 | 0.162 | +0.024 | +0.013 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 67 | 0.712 | 0.700 | +0.027 | +0.015 | $6.52 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTABHAYTON27-1|yes; why: higher confidence-adjusted growth (18.69 vs 0.17 bp); alternative not eligible: confidence-adjusted EV +0.0035 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.01); failure: UTA offense suppressed (<= 2 goals)
- **Josh Anderson: 1+ goals YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (8.08 vs 3.14 bp); relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.018); failure: MTL offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLSPREAD-26NOV05UTAMTL-UTA2|no; why: higher confidence-adjusted growth (3.14 vs 0.52 bp); despite a smaller raw edge (+0.024 vs +0.034/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0071 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA wins (incl. OT/SO)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no; why: Player prop expression KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.01); failure: UTA offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4101): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4392): highest fidelity KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MTL:WINS_BY_2PLUS (p 0.3004): highest fidelity KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes (same contract)
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.371, phi -0.211)
- KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3422, phi -0.212)
- KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:WINS (p 0.4803, phi -0.207)
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.4101, phi -0.229)
- override: Player prop expression KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no selected over player prop KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.85 vs 0.87 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.86 (adj +1.47) on $16.20, P(profit) 0.5589, adj growth 13.8 bp · B EV +3.09 (adj +1.98) on $18.36, P(profit) 0.4862, adj growth 18.3 bp · C EV +3.81 (adj +2.44) on $22.62, P(profit) 0.4862, adj growth 22.1 bp · R EV +0.08 (adj +0.04) on $2.00, P(profit) 0.7121, adj growth 1.6 bp

## VGK @ DET  ·  10000 joint draws  ·  404 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.131 | 0.43 | 0.57 | 0.00 | 6.04 | 27.1/26.9 | 22.9/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.47 | 0.53 | 0.49 | 5.97 | 27.1/27.0 | 23.7/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.42 | 0.58 | 0.00 | 9.3 | 28.7/28.8 | 22.4/22.9 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.077 | 0.48 | 0.52 | 0.00 | 5.96 | 31.8/21.3 | 17.7/28.3 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.54 | 0.46 | 0.46 | 5.9 | 32.3/21.7 | 18.3/28.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.062 | 0.33 | 0.67 | 0.00 | 6.03 | 21.2/31.4 | 26.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.066 | +0.025 | +0.013 | $1.48 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ivan Barbashev: 1+ assists YES | 28 | 0.349 | 0.312 | +0.055 | +0.018 | $3.09 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.50) | EVIDENCE_MIXED | D |
| Sheldon Dries: 1+ goals YES | 9 | 0.114 | 0.107 | +0.019 | +0.011 | $1.62 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (6.70 vs 3.34 bp); despite a smaller raw edge (+0.025 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26NOV05VGKDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: VGK offense suppressed (<= 2 goals)
- **Ivan Barbashev: 1+ assists YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VGKDET-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (3.34 vs 0.40 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.063); KXNHLGOAL-26NOV05VGKDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: VGK offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLPTS-26NOV05VGKDET-DETACOPP18-1|yes; why: higher confidence-adjusted growth (3.15 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.030/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.424): highest fidelity KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3565): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3663, phi -0.13)
- KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3663, phi -0.279)
- KXNHLGOAL-26NOV05VGKDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4235, phi -0.16)

portfolios: A EV +2.46 (adj +1.07) on $10.05, P(profit) 0.4614, adj growth 9.4 bp · B EV +1.57 (adj +0.73) on $6.18, P(profit) 0.4614, adj growth 6.7 bp · C EV +0.76 (adj +0.25) on $4.10, P(profit) 0.3489, adj growth 2.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  390 bet sides mapped, 4 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.171 | 0.83 | 0.17 | 0.00 | 6.04 | 32.8/20.4 | 18.4/27.1 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.124 | 0.83 | 0.17 | 0.00 | 9.26 | 34.6/21.8 | 17.9/25.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.60 | 0.40 | 0.48 | 5.94 | 33.1/20.8 | 17.8/29.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.104 | 0.79 | 0.21 | 0.00 | 6.0 | 27.2/26.4 | 24.0/22.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.79 | 0.21 | 0.00 | 9.32 | 29.0/28.0 | 23.7/20.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.54 | 0.46 | 0.50 | 5.98 | 27.3/26.6 | 23.3/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 41 | 0.500 | 0.453 | +0.073 | +0.026 | $5.37 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 20 | 0.244 | 0.226 | +0.033 | +0.014 | $1.93 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ assists NO | 35 | 0.417 | 0.376 | +0.052 | +0.010 | $1.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV05CHITB-TB3|no; why: higher confidence-adjusted growth (5.83 vs 1.49 bp); despite a smaller raw edge (+0.073 vs +0.079/contract); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: REINFORCING (phi 0.151); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.225); failure: TBL wins by 2+
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (5.83 vs 2.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.151); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.151); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: CHI offense suppressed (<= 2 goals)
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CHITB-TB2|no has the higher standalone adjusted growth (5.83 vs 1.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.225); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.225); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.12, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:TIGHT (p 0.3739): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no (same contract)
- thesis CHI:OFFENSE_4PLUS (p 0.239): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.2449): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CHITB-TB2|no — override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CHITB-TB3|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-1|no kept
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.5, phi -1.0)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.552, phi -0.251)
- KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5652, phi -0.311)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV05CHITB-TB3|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-1|no kept

portfolios: A EV +2.45 (adj +0.60) on $16.20, P(profit) 0.551, adj growth 5.0 bp · B EV +1.38 (adj +0.48) on $8.42, P(profit) 0.5897, adj growth 4.5 bp · C EV +1.30 (adj +0.45) on $7.58, P(profit) 0.5, adj growth 4.1 bp · R EV +0.34 (adj +0.12) on $2.00, P(profit) 0.5, adj growth 4.4 bp

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 12 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.126 | 0.61 | 0.39 | 0.00 | 6.0 | 33.2/21.4 | 18.5/29.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.54 | 0.46 | 0.45 | 5.89 | 33.5/21.7 | 18.5/29.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.56 | 0.44 | 0.00 | 6.04 | 27.5/26.9 | 23.7/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.49 | 0.51 | 0.47 | 5.95 | 27.8/27.1 | 23.8/24.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.088 | 0.62 | 0.38 | 0.00 | 9.23 | 34.7/22.9 | 17.9/27.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.071 | 0.56 | 0.44 | 0.00 | 9.26 | 29.6/28.9 | 23.2/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jack Hughes: 1+ goals NO | 59 | 0.661 | 0.641 | +0.054 | +0.034 | $11.25 | FUNDED_RESEARCH | $3 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Robert Thomas: 1+ goals YES | 22 | 0.270 | 0.254 | +0.038 | +0.022 | $3.78 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Dylan Holloway: 1+ goals YES | 23 | 0.272 | 0.259 | +0.030 | +0.017 | $3.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 12 | 0.146 | 0.138 | +0.019 | +0.011 | $1.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (10.43 vs 4.09 bp); despite a smaller raw edge (+0.054 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense succeeds (4+ goals)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (5.68 vs 4.09 bp); despite a smaller raw edge (+0.038 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05STLNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: STL offense suppressed (<= 2 goals)
- **Dylan Holloway: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (5.68 vs 3.29 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.008); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05STLNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: STL offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05STLNJ-NJDHAMILTON7-1|yes; why: higher confidence-adjusted growth (2.33 vs 0.04 bp); despite a smaller raw edge (+0.019 vs +0.029/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0019 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.3723): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:OFFENSE_4PLUS (p 0.3471): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4543): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4173, phi -0.252)
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4352, phi -0.251)
- KXNHLGOAL-26NOV05STLNJ-STLDHOLLOWAY81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4352, phi -0.256)
- KXNHLGOAL-26NOV05STLNJ-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.3723, phi -0.169)

portfolios: A EV +2.17 (adj +0.62) on $16.20, P(profit) 0.558, adj growth 5.6 bp · B EV +2.24 (adj +1.33) on $19.78, P(profit) 0.4051, adj growth 12.4 bp · C EV +1.98 (adj +1.20) on $18.44, P(profit) 0.7504, adj growth 11.0 bp · R EV +0.27 (adj +0.17) on $3.00, P(profit) 0.6608, adj growth 6.2 bp

## CAR @ NYI  ·  10000 joint draws  ·  420 bet sides mapped, 20 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.121 | 0.41 | 0.59 | 0.00 | 5.96 | 21.0/32.5 | 28.5/18.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.109 | 0.51 | 0.49 | 0.00 | 6.01 | 26.2/26.8 | 23.3/22.6 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.48 | 0.52 | 0.46 | 5.87 | 21.4/33.0 | 29.7/18.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.52 | 0.48 | 0.50 | 5.96 | 26.7/27.4 | 24.1/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.53 | 0.47 | 0.00 | 9.27 | 28.2/28.9 | 23.0/22.2 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.081 | 0.43 | 0.57 | 0.00 | 9.3 | 22.6/34.6 | 27.6/17.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 12 | 0.158 | 0.145 | +0.031 | +0.018 | $2.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 16 | 0.199 | 0.187 | +0.030 | +0.017 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| New York I over 2.5 goals scored YES | 49 | 0.615 | 0.530 | +0.107 | +0.023 | $4.38 | FUNDED_RESEARCH | $2 | NYI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nikolaj Ehlers: 1+ goals NO | 74 | 0.781 | 0.767 | +0.028 | +0.014 | $8.04 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes; why: KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes has the higher standalone adjusted growth (8.32 vs 5.95 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.025); relationships: KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: REINFORCING (phi 0.182); KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.0); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes; why: KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes has the higher standalone adjusted growth (8.32 vs 4.67 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.026); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: REINFORCING (phi 0.21); KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **New York I over 2.5 goals scored YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes selected over player prop KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: REINFORCING (phi 0.182); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: REINFORCING (phi 0.21); KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: NYI offense suppressed (<= 2 goals)
- **Nikolaj Ehlers: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (7.09 vs 2.29 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.116); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: MOSTLY_INDEPENDENT (phi 0.02); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis NYI:OFFENSE_4PLUS (p 0.3867): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes — Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes selected over player prop KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NYI:WINS (p 0.495): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS_BY_2PLUS (p 0.2741): highest fidelity KXNHLSPREAD-26NOV05CARNYI-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-NYI2|yes (same contract)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3955, phi -0.185)
- KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3955, phi -0.212)
- KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 13.0 pts; opposing: failure thesis NYI:SUPPRESSED (p 0.3955, phi -0.979)
- KXNHLGOAL-26NOV05CARNYI-CARNEHLERS27-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4066, phi -0.187)
- override: Broad expression KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes selected over player prop KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes because adjusted EV differs by only 0.5 pts while thesis capture is 1.00 vs 0.52 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.58 (adj +0.56) on $16.20, P(profit) 0.5615, adj growth 4.4 bp · B EV +2.19 (adj +0.90) on $17.07, P(profit) 0.5939, adj growth 8.4 bp · C EV +2.89 (adj +0.98) on $11.16, P(profit) 0.4957, adj growth 8.9 bp · R EV +0.53 (adj +0.15) on $5.00, P(profit) 0.4844, adj growth 5.3 bp

## PHI @ NYR  ·  10000 joint draws  ·  444 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_PHI_win | p_overtime | goals | shots NYR/PHI | NYR/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 5.98 | 26.1/26.1 | 22.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.54 | 0.46 | 0.47 | 5.92 | 26.4/26.3 | 23.0/23.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.078 | 0.62 | 0.38 | 0.00 | 6.01 | 30.9/20.8 | 18.0/26.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.58 | 0.42 | 0.00 | 9.16 | 27.8/27.8 | 22.3/21.5 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.55 | 0.45 | 0.45 | 5.86 | 31.2/21.1 | 17.9/27.9 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.065 | 0.46 | 0.54 | 0.00 | 6.0 | 20.9/30.8 | 27.1/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Christian Dvorak: 1+ goals YES | 16 | 0.209 | 0.196 | +0.040 | +0.026 | $4.91 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 68 | 0.748 | 0.711 | +0.052 | +0.016 | $11.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHICKNUBLE54-1|yes; why: higher confidence-adjusted growth (10.43 vs 0.69 bp); alternative not eligible: confidence-adjusted EV +0.0059 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.252); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.69 vs 0.00 bp); despite a smaller raw edge (+0.052 vs +0.055/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.252); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYR shot control · normal event (5-7) · decided (2+) 0.08.
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4549, phi -0.22)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.238)

portfolios: A EV +1.39 (adj +0.74) on $10.34, P(profit) 0.209, adj growth 7.0 bp · B EV +2.00 (adj +1.02) on $16.16, P(profit) 0.8449, adj growth 9.4 bp · C EV +2.46 (adj +1.25) on $19.91, P(profit) 0.8449, adj growth 11.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## BOS @ PIT  ·  10000 joint draws  ·  424 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_BOS_win | p_overtime | goals | shots PIT/BOS | PIT/BOS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.52 | 0.48 | 0.00 | 6.04 | 27.5/27.2 | 23.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.47 | 0.53 | 0.47 | 6.01 | 27.5/27.2 | 23.8/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.50 | 0.50 | 0.00 | 9.46 | 29.2/28.8 | 22.7/22.9 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.103 | 0.59 | 0.41 | 0.00 | 6.01 | 33.4/21.7 | 18.6/29.2 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.51 | 0.49 | 0.49 | 5.93 | 32.9/21.9 | 18.6/29.6 | even strength |
| PIT shot control · high event (8+) · decided (2+) | 0.085 | 0.58 | 0.42 | 0.00 | 9.38 | 34.9/23.1 | 17.9/27.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 12 | 0.189 | 0.170 | +0.061 | +0.043 | $6.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 2+ goals YES | 6 | 0.092 | 0.081 | +0.029 | +0.017 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 33 | 0.391 | 0.373 | +0.045 | +0.028 | $3.77 | FUNDED_RESEARCH | $1 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 69 | 0.760 | 0.718 | +0.055 | +0.013 | $8.33 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (35.01 vs 2.50 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.045); failure: BOS wins (incl. OT/SO)
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 9.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: DUPLICATIVE (phi 0.399); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.033); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 7.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.020); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: DUPLICATIVE (phi 0.399); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.041); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05BOSPIT-PITBKINDEL81-1|no; why: higher confidence-adjusted growth (1.67 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.045); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.033); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.041); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.3121): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4448): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3703): highest fidelity KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-BOSDPASTRNAK88-1|no (same contract)
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4798, phi -0.221)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.194)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.267)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4448, phi -0.213)

portfolios: A EV +4.07 (adj +2.50) on $16.20, P(profit) 0.4437, adj growth 23.2 bp · B EV +4.88 (adj +2.97) on $19.98, P(profit) 0.4437, adj growth 27.3 bp · C EV +3.88 (adj +2.67) on $13.40, P(profit) 0.1887, adj growth 23.9 bp · R EV +0.13 (adj +0.08) on $1.00, P(profit) 0.3909, adj growth 3.0 bp

## DAL @ CBJ  ·  10000 joint draws  ·  392 bet sides mapped, 8 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_DAL_win | p_overtime | goals | shots CBJ/DAL | CBJ/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.54 | 0.46 | 0.00 | 6.03 | 25.8/25.9 | 22.5/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.49 | 5.92 | 25.8/25.8 | 22.6/22.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.55 | 0.45 | 0.00 | 9.29 | 27.6/27.6 | 21.9/21.3 | even strength |
| CBJ shot control · normal event (5-7) · decided (2+) | 0.075 | 0.63 | 0.37 | 0.00 | 5.99 | 30.5/20.7 | 17.8/26.2 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 5.95 | 20.5/30.1 | 26.4/17.2 | even strength |
| CBJ shot control · normal event (5-7) · tight (1-goal/OT) | 0.066 | 0.56 | 0.44 | 0.49 | 5.9 | 30.4/20.6 | 17.4/26.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Damon Severson: 1+ goals YES | 7 | 0.111 | 0.099 | +0.036 | +0.025 | $3.27 | FUNDED_RESEARCH | $1 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.285 | 0.270 | +0.043 | +0.028 | $4.92 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 16 | 0.196 | 0.185 | +0.027 | +0.015 | $2.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.213 | 0.201 | +0.023 | +0.011 | $1.69 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: higher confidence-adjusted growth (18.48 vs 9.14 bp); despite a smaller raw edge (+0.036 vs +0.043/contract); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: higher confidence-adjusted growth (9.14 vs 4.22 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.917 vs 0.312); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (9.14 vs 3.65 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes has the higher standalone adjusted growth (9.14 vs 1.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.000); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:OFFENSE_4PLUS (p 0.397): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2477): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes (same contract)
- thesis CBJ:WINS_BY_2PLUS (p 0.3064): highest fidelity KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.141)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.234)
- KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.191)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.245)

portfolios: A EV +2.30 (adj +0.79) on $16.20, P(profit) 0.5049, adj growth 6.5 bp · B EV +3.04 (adj +1.96) on $12.31, P(profit) 0.493, adj growth 18.1 bp · C EV +1.61 (adj +0.87) on $6.96, P(profit) 0.3345, adj growth 7.9 bp · R EV +0.48 (adj +0.33) on $1.00, P(profit) 0.1105, adj growth 11.8 bp

## VAN @ WPG  ·  10000 joint draws  ·  408 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| WPG shot control · normal event (5-7) · decided (2+) | 0.117 | 0.62 | 0.38 | 0.00 | 6.02 | 32.6/21.1 | 18.2/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.53 | 0.47 | 0.00 | 6.06 | 27.3/26.7 | 23.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.50 | 0.50 | 0.50 | 5.94 | 27.4/26.8 | 23.5/24.1 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.53 | 0.47 | 0.49 | 5.86 | 32.8/21.4 | 18.2/29.5 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.079 | 0.62 | 0.38 | 0.00 | 9.28 | 34.4/22.7 | 17.7/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.58 | 0.42 | 0.00 | 9.3 | 29.1/28.5 | 22.9/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 17 | 0.229 | 0.208 | +0.049 | +0.028 | $4.09 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.215 | 0.195 | +0.046 | +0.026 | $3.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Winnipeg wins by over 2.5 goals NO | 70 | 0.795 | 0.745 | +0.080 | +0.030 | $11.25 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Liam Ohgren: 1+ goals YES | 14 | 0.178 | 0.168 | +0.030 | +0.019 | $2.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (11.75 vs 10.10 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26NOV05VANWPG-WPG3|no: MOSTLY_INDEPENDENT (phi 0.114); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (11.75 vs 10.10 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLSPREAD-26NOV05VANWPG-WPG3|no: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: VAN offense suppressed (<= 2 goals)
- **Winnipeg wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN3|yes; why: higher confidence-adjusted growth (9.89 vs 4.52 bp); wins across more scripts (relative breadth 1.005 vs 0.466); relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.114); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.124); KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: MOSTLY_INDEPENDENT (phi 0.1); failure: WPG wins by 2+
- **Liam Ohgren: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (11.75 vs 6.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLSPREAD-26NOV05VANWPG-WPG3|no: MOSTLY_INDEPENDENT (phi 0.1); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts WPG shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis VAN:OFFENSE_4PLUS (p 0.3614): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4556): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.2426): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4173, phi -0.229)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4173, phi -0.228)
- KXNHLSPREAD-26NOV05VANWPG-WPG3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.3143, phi -0.75)
- KXNHLGOAL-26NOV05VANWPG-VANLOHGREN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4173, phi -0.201)

portfolios: A EV +2.00 (adj +0.54) on $16.20, P(profit) 0.6857, adj growth 4.9 bp · B EV +3.90 (adj +2.01) on $21.62, P(profit) 0.4687, adj growth 18.7 bp · C EV +2.95 (adj +1.39) on $18.95, P(profit) 0.8225, adj growth 12.8 bp · R EV +0.89 (adj +0.44) on $5.00, P(profit) 0.2293, adj growth 15.6 bp

## ANA @ EDM  ·  10000 joint draws  ·  450 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.146 | 0.62 | 0.38 | 0.00 | 9.75 | 29.7/29.7 | 24.0/22.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.63 | 0.37 | 0.00 | 6.12 | 27.9/27.9 | 24.8/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.53 | 0.47 | 0.47 | 6.09 | 28.1/28.2 | 24.8/24.5 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.070 | 0.68 | 0.32 | 0.00 | 9.67 | 34.6/23.8 | 18.8/26.5 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.068 | 0.52 | 0.48 | 0.58 | 9.86 | 29.8/29.8 | 23.0/23.1 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.066 | 0.54 | 0.46 | 0.00 | 9.63 | 24.0/34.5 | 27.9/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 9 | 0.127 | 0.115 | +0.031 | +0.019 | $2.72 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.202 | 0.189 | +0.033 | +0.019 | $3.11 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Alex Formenton: 1+ goals YES | 14 | 0.176 | 0.166 | +0.028 | +0.018 | $2.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Pavel Mintyukov: 1+ goals YES | 6 | 0.085 | 0.076 | +0.021 | +0.012 | $1.58 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (9.14 vs 5.86 bp); despite a smaller raw edge (+0.031 vs +0.033/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes; why: higher confidence-adjusted growth (5.86 vs 3.76 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: ANA offense suppressed (<= 2 goals)
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (5.36 vs 3.52 bp); despite a smaller raw edge (+0.028 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: EDM offense suppressed (<= 2 goals)
- **Pavel Mintyukov: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes has the higher standalone adjusted growth (5.86 vs 5.09 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.011); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.15, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4363): highest fidelity KXNHLTOTAL-26NOV05ANAEDM-9|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.5554): highest fidelity KXNHLTOTAL-26NOV05ANAEDM-9|yes [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2508): highest fidelity KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.151)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.196)
- KXNHLGOAL-26NOV05ANAEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2508, phi -0.157)
- KXNHLGOAL-26NOV05ANAEDM-ANAPMINTYUKOV98-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3512, phi -0.131)

portfolios: A EV +2.93 (adj +0.67) on $16.20, P(profit) 0.5839, adj growth 6.1 bp · B EV +2.49 (adj +1.52) on $10.12, P(profit) 0.4755, adj growth 14.0 bp · C EV +2.99 (adj +1.11) on $26.86, P(profit) 0.7, adj growth 10.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_NSH_win | p_overtime | goals | shots COL/NSH | COL/NSH starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.152 | 0.76 | 0.24 | 0.00 | 6.01 | 34.8/22.2 | 20.0/29.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.117 | 0.79 | 0.21 | 0.00 | 9.31 | 36.8/23.6 | 19.5/27.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.59 | 0.41 | 0.47 | 5.97 | 35.3/22.6 | 19.5/31.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.71 | 0.29 | 0.00 | 6.07 | 29.2/28.4 | 25.7/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.71 | 0.29 | 0.00 | 9.44 | 30.9/30.0 | 25.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.51 | 0.49 | 0.47 | 5.98 | 29.2/28.5 | 25.2/25.9 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
