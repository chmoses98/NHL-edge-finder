# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T23:14:23Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +27.77 | +9.46 | +26.49 | 0.748 | -22.80 | -35.88 | 86.64 |
| B thesis-diversified (joint) ← optimiser card | 150.01 | +26.68 | +14.25 | +24.13 | 0.737 | -22.36 | -34.88 | 134.58 |
| C best expression per thesis | 149.99 | +22.59 | +11.26 | +20.47 | 0.719 | -23.62 | -35.32 | 105.81 |
| R FUNDED research stakes | 19.00 | +2.94 | +1.76 | +1.38 | 0.538 | -7.31 | -9.19 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  440 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.475 / away 0.525

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.01 | 27.1/27.5 | 24.2/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.50 | 0.50 | 0.49 | 5.99 | 27.4/27.6 | 24.4/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.101 | 0.57 | 0.43 | 0.00 | 9.41 | 28.8/29.1 | 23.4/22.1 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.096 | 0.49 | 0.51 | 0.00 | 5.99 | 21.8/33.2 | 29.4/18.4 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.49 | 0.51 | 0.44 | 5.93 | 21.8/33.0 | 29.6/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.072 | 0.50 | 0.50 | 0.00 | 9.35 | 23.3/34.8 | 28.1/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dylan Guenther: 1+ goals NO | 66 | 0.719 | 0.703 | +0.043 | +0.027 | $8.03 | FUNDED_RESEARCH | $3 | UTA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 18 | 0.225 | 0.210 | +0.035 | +0.020 | $2.53 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Cole Caufield: 1+ assists YES | 33 | 0.413 | 0.369 | +0.068 | +0.024 | $3.16 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.57) | EVIDENCE_MIXED | D |
| Utah wins by over 2.5 goals NO | 79 | 0.841 | 0.813 | +0.039 | +0.011 | $5.10 | FUNDED_RESEARCH | $2 | MTL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no; why: higher confidence-adjusted growth (7.52 vs 2.04 bp); despite a smaller raw edge (+0.043 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: MOSTLY_INDEPENDENT (phi 0.134); failure: UTA offense succeeds (4+ goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTAALEE72-1|yes; why: higher confidence-adjusted growth (5.61 vs 0.46 bp); alternative not eligible: confidence-adjusted EV +0.0060 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: INTENTIONAL_DIVERSIFIER (phi -0.149); failure: UTA offense suppressed (<= 2 goals)
- **Cole Caufield: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: higher confidence-adjusted growth (5.40 vs 2.06 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: MOSTLY_INDEPENDENT (phi 0.146); failure: MTL offense suppressed (<= 2 goals)
- **Utah wins by over 2.5 goals NO** — thesis: MTL wins (incl. OT/SO); alternative: KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes; why: Broad expression KXNHLSPREAD-26NOV05UTAMTL-UTA3|no selected over player prop KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.149); KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: MOSTLY_INDEPENDENT (phi 0.146); failure: UTA wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:SUPPRESSED (p 0.3901): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no — Broad expression KXNHLSPREAD-26NOV05UTAMTL-UTA3|no selected over player prop KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis UTA:OFFENSE_4PLUS (p 0.398): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.4339): highest fidelity KXNHLSPREAD-26NOV05UTAMTL-UTA3|no [DIRECT], best adjusted EV KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.398, phi -0.241)
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3901, phi -0.226)
- KXNHLAST-26NOV05UTAMTL-MTLCCAUFIELD13-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 43% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3462, phi -0.271)
- KXNHLSPREAD-26NOV05UTAMTL-UTA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis UTA:WINS_BY_2PLUS (p 0.2606, phi -0.733)
- override: Broad expression KXNHLSPREAD-26NOV05UTAMTL-UTA3|no selected over player prop KXNHLAST-26NOV05UTAMTL-UTAVTROCHECK16-1|no because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.87 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.44 (adj +0.53) on $14.88, P(profit) 0.6803, adj growth 5.1 bp · B EV +1.85 (adj +0.88) on $18.82, P(profit) 0.4417, adj growth 8.4 bp · C EV +2.04 (adj +1.03) on $17.23, P(profit) 0.4888, adj growth 9.7 bp · R EV +0.29 (adj +0.15) on $5.00, P(profit) 0.6267, adj growth 5.6 bp

## VGK @ DET  ·  10000 joint draws  ·  416 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.431 / away 0.569

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.42 | 0.58 | 0.00 | 6.03 | 27.0/27.0 | 23.2/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.49 | 0.51 | 0.49 | 5.95 | 27.2/27.3 | 24.0/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.42 | 0.58 | 0.00 | 9.31 | 28.7/28.6 | 21.9/23.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 5.99 | 31.6/21.3 | 17.8/27.9 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.50 | 0.50 | 0.44 | 5.89 | 32.1/21.7 | 18.2/28.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.059 | 0.38 | 0.62 | 0.00 | 6.0 | 21.5/31.7 | 27.4/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.067 | +0.025 | +0.014 | $1.27 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 9 | 0.115 | 0.107 | +0.019 | +0.012 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Mark Stone: 1+ assists NO | 56 | 0.624 | 0.590 | +0.047 | +0.012 | $3.43 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | VGK:SUPPRESSED | DIRECT (0.80) | EVIDENCE_MIXED | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (8.17 vs 0.34 bp); despite a smaller raw edge (+0.025 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VGKDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: VGK offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26NOV05VGKDET-DET2|yes; why: higher confidence-adjusted growth (3.41 vs 0.60 bp); despite a smaller raw edge (+0.019 vs +0.030/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; wins across more scripts (relative breadth 0.923 vs 0.822); alternative not eligible: confidence-adjusted EV +0.0044 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense suppressed (<= 2 goals)
- **Mark Stone: 1+ assists NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05VGKDET-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (1.38 vs 0.00 bp); despite a smaller raw edge (+0.047 vs +0.077/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); KXNHLGOAL-26NOV05VGKDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.3615): highest fidelity KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no (same contract)
- thesis VGK:OFFENSE_4PLUS (p 0.4209): highest fidelity - [-], best adjusted EV - — no eligible expression
- thesis DET:OFFENSE_4PLUS (p 0.3568): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3615, phi -0.123)
- KXNHLGOAL-26NOV05VGKDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4279, phi -0.166)
- KXNHLAST-26NOV05VGKDET-VGKMSTONE61-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4209, phi -0.272)

portfolios: A EV +1.70 (adj +0.83) on $9.47, P(profit) 0.7006, adj growth 7.6 bp · B EV +1.10 (adj +0.55) on $5.89, P(profit) 0.7006, adj growth 5.2 bp · C EV +0.29 (adj +0.08) on $3.50, P(profit) 0.6243, adj growth 0.7 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CHI @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.790 / away 0.210

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.173 | 0.84 | 0.16 | 0.00 | 6.02 | 32.7/20.4 | 18.4/27.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.126 | 0.84 | 0.16 | 0.00 | 9.31 | 34.6/21.6 | 17.9/25.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.61 | 0.39 | 0.47 | 5.89 | 33.6/20.9 | 17.9/30.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.78 | 0.22 | 0.00 | 5.99 | 27.2/26.2 | 23.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.55 | 0.45 | 0.47 | 5.91 | 27.3/26.4 | 23.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.78 | 0.22 | 0.00 | 9.39 | 28.7/27.8 | 23.5/20.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay over 3.5 goals scored NO | 33 | 0.424 | 0.374 | +0.078 | +0.029 | $3.78 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.236 | 0.222 | +0.035 | +0.021 | $2.56 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Andrei Vasilevskiy: 19+ saves YES | 50 | 0.644 | 0.541 | +0.127 | +0.023 | $5.44 | SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SHOT_CONTROL | DIRECT (0.94) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 2+ assists NO | 72 | 0.795 | 0.750 | +0.061 | +0.016 | $4.25 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.97) | EVIDENCE_MIXED | D |
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no; why: higher confidence-adjusted growth (8.08 vs 2.81 bp); relationships: KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: REINFORCING (phi 0.292); failure: TBL offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CHITB-TB2|no; why: higher confidence-adjusted growth (6.04 vs 2.50 bp); despite a smaller raw edge (+0.035 vs +0.088/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Andrei Vasilevskiy: 19+ saves YES** — thesis: CHI controls shots (share >= 0.55); alternative: KXNHLSAVE-26NOV05CHITB-CHIASODERBLOM40-28|no; why: higher confidence-adjusted growth (4.71 vs 0.20 bp); alternative not eligible: confidence-adjusted EV +0.0047 below the 0.010/contract floor; relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: MOSTLY_INDEPENDENT (phi -0.024); failure: TBL net faces light volume (<= 25 shots; CHI suppressed)
- **Nikita Kucherov: 2+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no has the higher standalone adjusted growth (8.08 vs 2.81 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.292); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: REINFORCING (phi 0.292); KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · high event (8+) · decided (2+) 0.13, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.2413): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no (same contract)
- thesis GAME:TIGHT (p 0.3689): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2364): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5669, phi -0.981)
- KXNHLGOAL-26NOV05CHITB-CHITBERTUZZI59-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5564, phi -0.249)
- KXNHLSAVE-26NOV05CHITB-TBAVASILEVSKIY88-19|yes: SHADOW_ONLY — LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 6% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis TBL:NET_LOW_VOLUME (p 0.6705, phi -0.466)
- KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 3% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5669, phi -0.295)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no less than the minimum stake; KXNHLAST-26NOV05CHITB-TBNKUCHEROV86-2|no kept

portfolios: A EV +2.84 (adj +0.52) on $14.88, P(profit) 0.557, adj growth 4.7 bp · B EV +2.99 (adj +0.92) on $16.02, P(profit) 0.7372, adj growth 8.7 bp · C EV +1.60 (adj +0.71) on $7.73, P(profit) 0.5586, adj growth 6.7 bp · R EV +0.23 (adj +0.08) on $1.00, P(profit) 0.4239, adj growth 3.2 bp

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 16 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.665 / away 0.335

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.131 | 0.65 | 0.35 | 0.00 | 5.98 | 33.3/21.3 | 18.5/29.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.57 | 0.43 | 0.00 | 5.99 | 27.5/26.9 | 23.7/23.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.55 | 0.45 | 0.44 | 5.91 | 33.8/21.6 | 18.4/30.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.47 | 0.53 | 0.46 | 5.93 | 27.6/27.1 | 23.8/24.3 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.089 | 0.69 | 0.31 | 0.00 | 9.3 | 35.0/23.1 | 18.3/26.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.57 | 0.43 | 0.00 | 9.17 | 29.6/28.8 | 23.0/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Robert Thomas: 1+ goals YES | 20 | 0.263 | 0.246 | +0.052 | +0.035 | $4.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Justin Barron: 1+ goals YES | 4 | 0.065 | 0.055 | +0.023 | +0.013 | $1.08 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Jimmy Snuggerud: 1+ goals YES | 25 | 0.304 | 0.289 | +0.041 | +0.026 | $3.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.47) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.652 | 0.634 | +0.045 | +0.027 | $6.56 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes; why: higher confidence-adjusted growth (15.88 vs 7.64 bp); relationships: KXNHLGOAL-26NOV05STLNJ-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.022); failure: STL offense suppressed (<= 2 goals)
- **Justin Barron: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 8.24 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.0); failure: STL offense suppressed (<= 2 goals)
- **Jimmy Snuggerud: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes has the higher standalone adjusted growth (15.88 vs 7.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05STLNJ-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: STL offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05STLNJ-NJ2|no; why: higher confidence-adjusted growth (6.59 vs 4.33 bp); despite a smaller raw edge (+0.045 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05STLNJ-STLJBARRON72-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: NJD offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3357): highest fidelity KXNHLTEAMTOTAL-26NOV05STLNJ-STL4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4354): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3527): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.26)
- KXNHLGOAL-26NOV05STLNJ-STLJBARRON72-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.12)
- KXNHLGOAL-26NOV05STLNJ-STLJSNUGGERUD21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 53% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4438, phi -0.271)
- KXNHLGOAL-26NOV05STLNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.4373, phi -0.249)

portfolios: A EV +2.85 (adj +0.66) on $14.88, P(profit) 0.5476, adj growth 5.7 bp · B EV +2.61 (adj +1.63) on $15.17, P(profit) 0.4499, adj growth 15.4 bp · C EV +2.70 (adj +1.63) on $19.20, P(profit) 0.5435, adj growth 15.3 bp · R EV +0.15 (adj +0.09) on $2.00, P(profit) 0.6516, adj growth 3.3 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05STLNJ-STL|yes == KXNHLGAME-26NOV05STLNJ-NJ|no

## CAR @ NYI  ·  10000 joint draws  ·  424 bet sides mapped, 19 +EV candidates, 4 on card

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
| Sebastian Aho: 1+ goals NO | 67 | 0.733 | 0.715 | +0.048 | +0.029 | $8.03 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.170 | 0.159 | +0.032 | +0.021 | $2.21 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Adam Pelech: 1+ goals YES | 4 | 0.063 | 0.055 | +0.020 | +0.012 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Anthony Duclair: 1+ goals YES | 14 | 0.180 | 0.169 | +0.032 | +0.020 | $2.25 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05CARNYI-CAR2|no; why: higher confidence-adjusted growth (8.84 vs 6.47 bp); despite a smaller raw edge (+0.048 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: CAR offense succeeds (4+ goals)
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 7.70 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi 0.012); failure: NYI offense suppressed (<= 2 goals)
- **Adam Pelech: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.022); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: NYI offense suppressed (<= 2 goals)
- **Anthony Duclair: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes; why: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI6|yes has the higher standalone adjusted growth (9.93 vs 7.11 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.130); relationships: KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV05CARNYI-NYIAPELECH3-1|yes: MOSTLY_INDEPENDENT (phi -0.02); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis GAME:HIGH_EVENT (p 0.2786): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:OFFENSE_4PLUS (p 0.3798): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.474): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-CAR2|no (same contract)
- KXNHLGOAL-26NOV05CARNYI-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.4179, phi -0.239)
- KXNHLGOAL-26NOV05CARNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.205)
- KXNHLGOAL-26NOV05CARNYI-NYIAPELECH3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.101)
- KXNHLGOAL-26NOV05CARNYI-NYIADUCLAIR11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3998, phi -0.208)

portfolios: A EV +2.88 (adj +0.52) on $14.88, P(profit) 0.5401, adj growth 4.3 bp · B EV +2.05 (adj +1.28) on $13.54, P(profit) 0.3619, adj growth 12.1 bp · C EV +2.64 (adj +1.22) on $16.58, P(profit) 0.5883, adj growth 11.5 bp · R EV +0.21 (adj +0.13) on $3.00, P(profit) 0.7332, adj growth 4.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05CARNYI-NYI|yes == KXNHLGAME-26NOV05CARNYI-CAR|no

## PHI @ NYR  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.569 / away 0.431

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
| Tye Kartye: 1+ assists YES | 23 | 0.306 | 0.266 | +0.064 | +0.023 | $2.89 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.209 | 0.198 | +0.029 | +0.018 | $2.65 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 67 | 0.743 | 0.702 | +0.058 | +0.016 | $7.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Pavel Dorofeyev: 1+ goals NO | 68 | 0.718 | 0.707 | +0.022 | +0.012 | $4.50 | FUNDED_RESEARCH | $2 | NYR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Tye Kartye: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05PHINYR-NYRALAFRENIERE13-1|yes; why: higher confidence-adjusted growth (6.31 vs 0.30 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0054 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: INTENTIONAL_DIVERSIFIER (phi -0.078); failure: NYR offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes; why: higher confidence-adjusted growth (4.95 vs 1.69 bp); despite a smaller raw edge (+0.029 vs +0.043/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.004); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05PHINYR-PHITKONECNY11-1|no; why: higher confidence-adjusted growth (2.68 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.243); KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: PHI offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ goals NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV05PHINYR-NYRWCUYLLE50-1|no; why: higher confidence-adjusted growth (1.42 vs 1.31 bp); relationships: KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.078); KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: NYR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis NYR:OFFENSE_4PLUS (p 0.3829): highest fidelity KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLAST-26NOV05PHINYR-PHITSANHEIM6-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4576): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- KXNHLAST-26NOV05PHINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3983, phi -0.251)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4576, phi -0.232)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.222)
- KXNHLGOAL-26NOV05PHINYR-NYRPDOROFEYEV16-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3829, phi -0.226)

portfolios: A EV +2.52 (adj +0.93) on $14.88, P(profit) 0.5221, adj growth 8.6 bp · B EV +2.00 (adj +0.81) on $17.88, P(profit) 0.7406, adj growth 7.7 bp · C EV +2.31 (adj +0.93) on $20.71, P(profit) 0.7406, adj growth 8.8 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.7176, adj growth 1.2 bp

## BOS @ PIT  ·  10000 joint draws  ·  440 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.507 / away 0.492

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
| Connor Dewar: 1+ goals YES | 12 | 0.189 | 0.170 | +0.061 | +0.043 | $4.32 | FUNDED_RESEARCH | $2 | PIT:WINS_BY_2PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.153 | 0.139 | +0.047 | +0.033 | $3.18 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Charlie McAvoy: 1+ assists NO | 52 | 0.600 | 0.555 | +0.063 | +0.018 | $3.53 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | BOS:SUPPRESSED | DIRECT (0.79) | EVIDENCE_MIXED | D |
| Ben Kindel: 1+ assists NO | 69 | 0.757 | 0.721 | +0.052 | +0.016 | $7.35 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.88) | EVIDENCE_MIXED | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes; why: higher confidence-adjusted growth (35.01 vs 23.69 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.049); failure: PIT offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 23.69 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.034); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.034); KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); failure: PIT offense suppressed (<= 2 goals)
- **Charlie McAvoy: 1+ assists NO** — thesis: BOS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05BOSPIT-BOSJPETERKA10-1|no; why: higher confidence-adjusted growth (2.75 vs 1.52 bp); relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: BOS offense succeeds (4+ goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05BOSPIT-PITBKINDEL81-1|no; why: higher confidence-adjusted growth (2.64 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, PIT shot control · normal event (5-7) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.329): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4699): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BOS:SUPPRESSED (p 0.3763): highest fidelity KXNHLAST-26NOV05BOSPIT-BOSJPETERKA10-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3206, phi -0.211)
- KXNHLGOAL-26NOV05BOSPIT-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3206, phi -0.187)
- KXNHLAST-26NOV05BOSPIT-BOSCMCAVOY73-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 21% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:OFFENSE_4PLUS (p 0.4197, phi -0.285)
- KXNHLAST-26NOV05BOSPIT-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.4699, phi -0.212)

portfolios: A EV +3.81 (adj +2.33) on $14.88, P(profit) 0.3084, adj growth 22.0 bp · B EV +4.44 (adj +2.71) on $18.38, P(profit) 0.3084, adj growth 25.5 bp · C EV +3.84 (adj +2.12) on $20.16, P(profit) 0.3809, adj growth 19.8 bp · R EV +0.96 (adj +0.67) on $2.00, P(profit) 0.1887, adj growth 24.0 bp

## DAL @ CBJ  ·  10000 joint draws  ·  404 bet sides mapped, 5 +EV candidates, 4 on card

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
| Mathieu Olivier: 1+ goals YES | 16 | 0.210 | 0.197 | +0.041 | +0.027 | $3.07 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:WINS_BY_2PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Charlie Coyle: 1+ goals YES | 23 | 0.283 | 0.269 | +0.041 | +0.026 | $3.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_STRONGER | D |
| Damon Severson: 1+ goals YES | 8 | 0.108 | 0.100 | +0.023 | +0.015 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Sean Monahan: 1+ goals YES | 16 | 0.197 | 0.186 | +0.027 | +0.017 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: higher confidence-adjusted growth (11.28 vs 3.18 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.906 vs 0.293); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: CBJ offense suppressed (<= 2 goals)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.28 vs 8.14 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: CBJ offense suppressed (<= 2 goals)
- **Damon Severson: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.28 vs 6.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.006); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CBJ offense suppressed (<= 2 goals)
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes has the higher standalone adjusted growth (11.28 vs 4.30 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.003); they share one thesis budget; relationships: KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis CBJ:WINS_BY_2PLUS (p 0.289): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.3817): highest fidelity KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.236)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.245)
- KXNHLGOAL-26NOV05DALCBJ-CBJDSEVERSON78-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.141)
- KXNHLGOAL-26NOV05DALCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4006, phi -0.192)

portfolios: A EV +2.48 (adj +1.55) on $12.71, P(profit) 0.6242, adj growth 14.5 bp · B EV +2.03 (adj +1.31) on $9.87, P(profit) 0.5961, adj growth 12.4 bp · C EV +0.86 (adj +0.57) on $3.57, P(profit) 0.2104, adj growth 5.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  406 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.653 / away 0.347

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.56 | 0.44 | 0.00 | 6.05 | 27.4/26.7 | 23.4/23.5 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.112 | 0.62 | 0.38 | 0.00 | 6.01 | 32.8/21.2 | 18.3/28.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.50 | 0.50 | 0.48 | 6.0 | 27.5/27.0 | 23.8/24.2 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.56 | 0.44 | 0.46 | 5.96 | 32.5/21.2 | 17.9/29.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.31 | 28.6/28.2 | 22.3/22.2 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.079 | 0.60 | 0.40 | 0.00 | 9.24 | 34.2/22.6 | 17.6/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Linus Karlsson: 1+ goals YES | 16 | 0.231 | 0.212 | +0.062 | +0.043 | $4.69 | FUNDED_RESEARCH | $2 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 16 | 0.218 | 0.202 | +0.049 | +0.033 | $3.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 11 | 0.152 | 0.140 | +0.035 | +0.023 | $2.28 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Winnipeg over 3.5 goals scored NO | 47 | 0.563 | 0.514 | +0.075 | +0.026 | $4.68 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (27.65 vs 16.47 bp); relationships: KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: MOSTLY_INDEPENDENT (phi 0.0); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 16.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: MOSTLY_INDEPENDENT (phi 0.029); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (27.65 vs 11.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: MOSTLY_INDEPENDENT (phi 0.032); failure: VAN offense suppressed (<= 2 goals)
- **Winnipeg over 3.5 goals scored NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: higher confidence-adjusted growth (6.08 vs 4.64 bp); wins across more scripts (relative breadth 0.898 vs 0.545); relationships: KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.0); KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.032); failure: WPG offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3572): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis WPG:SUPPRESSED (p 0.356): highest fidelity KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no (same contract)
- thesis VAN:WINS_BY_2PLUS (p 0.242): highest fidelity KXNHLSPREAD-26NOV05VANWPG-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05VANWPG-VANLKARLSSON94-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.205)
- KXNHLGOAL-26NOV05VANWPG-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.226)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4165, phi -0.206)
- KXNHLTEAMTOTAL-26NOV05VANWPG-WPG4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.4261, phi -0.977)

portfolios: A EV +2.47 (adj +0.49) on $14.88, P(profit) 0.5677, adj growth 4.3 bp · B EV +4.14 (adj +2.58) on $15.25, P(profit) 0.4883, adj growth 24.4 bp · C EV +3.12 (adj +1.80) on $20.62, P(profit) 0.6528, adj growth 16.9 bp · R EV +1.04 (adj +0.61) on $4.00, P(profit) 0.6636, adj growth 22.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV05VANWPG-VAN|yes == KXNHLGAME-26NOV05VANWPG-WPG|no

## ANA @ EDM  ·  10000 joint draws  ·  466 bet sides mapped, 19 +EV candidates, 4 on card

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
| Jeff Malott: 1+ goals YES | 9 | 0.122 | 0.113 | +0.027 | +0.017 | $1.76 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 29 | 0.410 | 0.329 | +0.105 | +0.024 | $3.10 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Sam Colangelo: 1+ goals YES | 13 | 0.166 | 0.156 | +0.029 | +0.018 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Alex Killorn: 1+ goals YES | 16 | 0.199 | 0.188 | +0.029 | +0.018 | $2.09 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (7.37 vs 5.23 bp); despite a smaller raw edge (+0.027 vs +0.029/contract); relationships: KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: ANA offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV05ANAEDM-EDMRNUGENTHOPKINS93-1|no; why: higher confidence-adjusted growth (6.02 vs 3.54 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: EDM offense succeeds (4+ goals)
- **Sam Colangelo: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes; why: higher confidence-adjusted growth (5.97 vs 5.23 bp); despite a smaller raw edge (+0.028 vs +0.029/contract); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)
- **Alex Killorn: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05ANAEDM-ANAJCAULFIELD28-1|yes; why: higher confidence-adjusted growth (5.23 vs 4.54 bp); relationships: KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis EDM:SUPPRESSED (p 0.2668): highest fidelity KXNHLPTS-26NOV05ANAEDM-EDMLDRAISAITL29-3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:WINS (p 0.4343): highest fidelity KXNHLSPREAD-26NOV05ANAEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis ANA:OFFENSE_4PLUS (p 0.433): highest fidelity KXNHLSPREAD-26NOV05ANAEDM-EDM3|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV05ANAEDM-ANABSENNECKE45-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05ANAEDM-ANAJMALOTT39-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.148)
- KXNHLAST-26NOV05ANAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.5 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.5288, phi -0.319)
- KXNHLGOAL-26NOV05ANAEDM-ANASCOLANGELO12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.175)
- KXNHLGOAL-26NOV05ANAEDM-ANAAKILLORN17-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.3567, phi -0.206)

portfolios: A EV +3.68 (adj +0.56) on $14.88, P(profit) 0.54, adj growth 5.0 bp · B EV +2.34 (adj +1.06) on $8.97, P(profit) 0.6548, adj growth 10.0 bp · C EV +2.21 (adj +0.80) on $10.02, P(profit) 0.7069, adj growth 7.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NSH @ COL  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

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
| Mavrik Bourque: 1+ assists NO | 72 | 0.796 | 0.755 | +0.062 | +0.021 | $8.03 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NSH:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Adam Wilsby: 1+ goals YES | 5 | 0.070 | 0.064 | +0.016 | +0.010 | $1.01 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.11) | EVIDENCE_STRONGER | D |
| Adam Edstrom: 1+ goals YES | 13 | 0.156 | 0.148 | +0.018 | +0.010 | $1.19 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NSH:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Mavrik Bourque: 1+ assists NO** — thesis: NSH offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV05NSHCOL-NSHMBOURQUE22-1|no; why: higher confidence-adjusted growth (5.13 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi -0.019); failure: NSH offense succeeds (4+ goals)
- **Adam Wilsby: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes; why: higher confidence-adjusted growth (4.41 vs 1.98 bp); despite a smaller raw edge (+0.016 vs +0.018/contract); relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NSH offense suppressed (<= 2 goals)
- **Adam Edstrom: 1+ goals YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26NOV05NSHCOL-NSH2|yes; why: higher confidence-adjusted growth (1.98 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: NSH offense suppressed (<= 2 goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.12, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NSH:SUPPRESSED (p 0.4705): highest fidelity KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3136): highest fidelity KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes (same contract)
- KXNHLAST-26NOV05NSHCOL-NSHMBOURQUE22-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:OFFENSE_4PLUS (p 0.3136, phi -0.2)
- KXNHLGOAL-26NOV05NSHCOL-NSHAWILSBY2-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 89% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.122)
- KXNHLGOAL-26NOV05NSHCOL-NSHAEDSTROM84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NSH:SUPPRESSED (p 0.4705, phi -0.216)

portfolios: A EV +1.10 (adj +0.54) on $8.81, P(profit) 0.2148, adj growth 5.1 bp · B EV +1.14 (adj +0.52) on $10.22, P(profit) 0.8137, adj growth 4.9 bp · C EV +0.96 (adj +0.37) on $10.67, P(profit) 0.7959, adj growth 3.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
