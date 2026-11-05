# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-05T12:46:06Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +26.99 | +9.73 | +25.68 | 0.690 | -38.81 | -54.36 | 84.29 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +28.65 | +13.99 | +23.18 | 0.652 | -44.49 | -60.99 | 121.94 |
| C best expression per thesis | 79.65 | +19.80 | +9.41 | +11.30 | 0.595 | -38.21 | -50.89 | 81.21 |
| R FUNDED research stakes | 27.00 | +5.25 | +2.06 | +4.24 | 0.617 | -11.41 | -14.94 | 0.00 |

## UTA @ MTL  ·  10000 joint draws  ·  422 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_UTA_win | p_overtime | goals | shots MTL/UTA | MTL/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.07 | 27.1/27.5 | 24.1/23.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.54 | 0.46 | 0.00 | 9.43 | 28.9/29.5 | 23.7/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.56 | 0.44 | 0.46 | 5.99 | 27.2/27.6 | 24.4/23.8 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.095 | 0.48 | 0.52 | 0.00 | 6.05 | 21.8/33.2 | 29.4/18.5 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.084 | 0.49 | 0.51 | 0.48 | 5.96 | 21.8/32.9 | 29.4/18.6 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.077 | 0.45 | 0.55 | 0.00 | 9.35 | 23.1/34.6 | 27.8/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 18 | 0.230 | 0.210 | +0.039 | +0.019 | $5.25 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Barrett Hayton: 1+ goals YES | 17 | 0.203 | 0.193 | +0.023 | +0.013 | $3.72 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Jake Evans: 1+ goals YES | 14 | 0.171 | 0.160 | +0.023 | +0.011 | $2.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MTL:WINS_BY_2PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Noah Dobson: 1+ assists YES | 32 | 0.391 | 0.345 | +0.056 | +0.010 | $3.21 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTABHAYTON27-1|yes; why: higher confidence-adjusted growth (5.28 vs 2.61 bp); relationships: KXNHLGOAL-26NOV05UTAMTL-UTABHAYTON27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: UTA offense suppressed (<= 2 goals)
- **Barrett Hayton: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes has the higher standalone adjusted growth (5.28 vs 2.61 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.010); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: UTA offense suppressed (<= 2 goals)
- **Jake Evans: 1+ goals YES** — thesis: MTL wins by 2+; alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJANDERSON17-1|yes; why: higher confidence-adjusted growth (2.22 vs 0.95 bp); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV05UTAMTL-UTABHAYTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: MOSTLY_INDEPENDENT (phi 0.059); failure: MTL offense suppressed (<= 2 goals)
- **Noah Dobson: 1+ assists YES** — thesis: MTL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes has the higher standalone adjusted growth (2.22 vs 1.00 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.059); they share one thesis budget; relationships: KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV05UTAMTL-UTABHAYTON27-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: MOSTLY_INDEPENDENT (phi 0.059); failure: MTL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.10, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.4117): highest fidelity KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes (same contract)
- thesis MTL:WINS_BY_2PLUS (p 0.3001): highest fidelity KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes (same contract)
- thesis MTL:OFFENSE_4PLUS (p 0.439): highest fidelity KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV05UTAMTL-UTALCROUSE67-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3738, phi -0.223)
- KXNHLGOAL-26NOV05UTAMTL-UTABHAYTON27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3738, phi -0.194)
- KXNHLGOAL-26NOV05UTAMTL-MTLJEVANS71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3444, phi -0.195)
- KXNHLAST-26NOV05UTAMTL-MTLNDOBSON53-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 45% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:SUPPRESSED (p 0.3444, phi -0.285)

portfolios: A EV +2.89 (adj +1.07) on $17.14, P(profit) 0.5446, adj growth 9.3 bp · B EV +2.54 (adj +1.13) on $15.15, P(profit) 0.4935, adj growth 9.9 bp · C EV +1.65 (adj +0.81) on $8.78, P(profit) 0.3636, adj growth 7.1 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VGK @ DET  ·  10000 joint draws  ·  404 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_VGK_win | p_overtime | goals | shots DET/VGK | DET/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.43 | 0.57 | 0.00 | 6.02 | 27.2/27.2 | 23.3/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.48 | 5.93 | 27.0/27.0 | 23.6/23.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.092 | 0.41 | 0.59 | 0.00 | 9.28 | 28.6/28.5 | 21.8/23.1 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.075 | 0.47 | 0.53 | 0.00 | 6.05 | 32.0/21.6 | 18.1/28.5 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.50 | 0.50 | 0.48 | 5.93 | 32.1/21.8 | 18.4/28.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.058 | 0.38 | 0.62 | 0.00 | 5.95 | 21.4/31.5 | 26.9/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 5 | 0.078 | 0.067 | +0.025 | +0.014 | $2.95 | FUNDED_RESEARCH | $1 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLAST-26NOV05VGKDET-VGKIBARBASHEV49-1|yes; why: higher confidence-adjusted growth (8.34 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0004 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: VGK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:OFFENSE_4PLUS (p 0.4231): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05VGKDET-VGKBMCNABB3-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3631, phi -0.122)

portfolios: A EV +1.15 (adj +0.65) on $2.46, P(profit) 0.0782, adj growth 5.7 bp · B EV +1.38 (adj +0.78) on $2.95, P(profit) 0.0782, adj growth 6.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.47 (adj +0.26) on $1.00, P(profit) 0.0782, adj growth 8.6 bp

## CHI @ TBL  ·  10000 joint draws  ·  390 bet sides mapped, 5 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_CHI_win | p_overtime | goals | shots TBL/CHI | TBL/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.172 | 0.82 | 0.18 | 0.00 | 6.0 | 33.0/20.5 | 18.5/27.5 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.59 | 0.41 | 0.49 | 5.92 | 32.9/20.9 | 17.9/29.3 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.115 | 0.83 | 0.17 | 0.00 | 9.33 | 34.9/22.1 | 18.3/26.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.105 | 0.77 | 0.23 | 0.00 | 6.04 | 27.2/26.3 | 23.9/22.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.57 | 0.43 | 0.46 | 5.94 | 27.0/26.3 | 23.1/23.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.78 | 0.22 | 0.00 | 9.31 | 28.6/27.6 | 23.1/20.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay over 3.5 goals scored NO | 37 | 0.448 | 0.406 | +0.061 | +0.020 | $4.74 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay over 4.5 goals scored NO | 58 | 0.660 | 0.615 | +0.063 | +0.018 | $5.44 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Tampa Bay wins by over 1.5 goals NO | 41 | 0.510 | 0.442 | +0.083 | +0.015 | $1.05 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay over 3.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no; why: higher confidence-adjusted growth (3.71 vs 2.98 bp); despite a smaller raw edge (+0.061 vs +0.063/contract); relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: DUPLICATIVE (phi 0.646); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.571); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay over 4.5 goals scored NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no has the higher standalone adjusted growth (3.71 vs 2.98 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.646); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: DUPLICATIVE (phi 0.646); KXNHLSPREAD-26NOV05CHITB-TB2|no: REINFORCING (phi 0.515); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no; why: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: REINFORCING (phi 0.571); KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: REINFORCING (phi 0.515); failure: TBL wins by 2+

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.17, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.12, TBL shot control · high event (8+) · decided (2+) 0.11.
- thesis TBL:SUPPRESSED (p 0.2575): highest fidelity KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no (same contract)
- thesis GAME:TIGHT (p 0.3795): highest fidelity KXNHLSPREAD-26NOV05CHITB-TB2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no — Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLTEAMTOTAL-26NOV05CHITB-TB4|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5419, phi -0.979)
- KXNHLTEAMTOTAL-26NOV05CHITB-TB5|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.5419, phi -0.659)
- KXNHLSPREAD-26NOV05CHITB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 10.5 pts; opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.4903, phi -1.0)
- override: Broad expression KXNHLSPREAD-26NOV05CHITB-TB2|no selected over broad KXNHLTEAMTOTAL-26NOV05CHITB-TB6|no because adjusted EV is 0.2 pts higher while thesis capture is 1.00 vs 0.96 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +2.79 (adj +0.53) on $18.72, P(profit) 0.6047, adj growth 4.1 bp · B EV +1.53 (adj +0.45) on $11.23, P(profit) 0.536, adj growth 3.9 bp · C EV +1.26 (adj +0.41) on $7.92, P(profit) 0.4478, adj growth 3.6 bp · R EV +0.72 (adj +0.20) on $5.00, P(profit) 0.536, adj growth 6.3 bp

## STL @ NJD  ·  10000 joint draws  ·  440 bet sides mapped, 4 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_STL_win | p_overtime | goals | shots NJD/STL | NJD/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.139 | 0.61 | 0.39 | 0.00 | 6.01 | 33.4/21.3 | 18.3/29.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.58 | 0.42 | 0.00 | 6.01 | 27.6/27.0 | 23.7/23.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.54 | 0.46 | 0.47 | 5.91 | 33.5/21.6 | 18.4/30.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.50 | 0.50 | 0.46 | 5.92 | 27.6/27.0 | 23.8/24.4 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.081 | 0.63 | 0.37 | 0.00 | 9.22 | 35.1/22.8 | 17.9/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.073 | 0.55 | 0.45 | 0.00 | 9.24 | 29.6/28.8 | 23.1/23.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| St. Louis over 4.5 goals scored YES | 13 | 0.180 | 0.150 | +0.042 | +0.012 | $1.85 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_MIXED | D |
| Robert Thomas: 1+ goals YES | 23 | 0.270 | 0.257 | +0.028 | +0.014 | $3.13 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.43) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 1.5 goals NO | 60 | 0.667 | 0.631 | +0.050 | +0.014 | $3.11 | FUNDED_RESEARCH | $1 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| New Jersey wins by over 2.5 goals NO | 72 | 0.777 | 0.746 | +0.043 | +0.012 | $5.07 | FUNDED_RESEARCH | $2 | STL:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **St. Louis over 4.5 goals scored YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (2.69 vs 2.35 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: REINFORCING (phi 0.23); KXNHLSPREAD-26NOV05STLNJ-NJ2|no: REINFORCING (phi 0.301); KXNHLSPREAD-26NOV05STLNJ-NJ3|no: REINFORCING (phi 0.232); failure: NJD wins (incl. OT/SO)
- **Robert Thomas: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes has the higher standalone adjusted growth (2.69 vs 2.35 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.230); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: REINFORCING (phi 0.23); KXNHLSPREAD-26NOV05STLNJ-NJ2|no: REINFORCING (phi 0.172); KXNHLSPREAD-26NOV05STLNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.15); failure: STL offense suppressed (<= 2 goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes has the higher standalone adjusted growth (2.69 vs 1.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.301); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: REINFORCING (phi 0.301); KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: REINFORCING (phi 0.172); KXNHLSPREAD-26NOV05STLNJ-NJ3|no: DUPLICATIVE (phi 0.757); failure: NJD wins by 2+
- **New Jersey wins by over 2.5 goals NO** — thesis: STL wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes has the higher standalone adjusted growth (2.69 vs 1.64 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.232); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: REINFORCING (phi 0.232); KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: MOSTLY_INDEPENDENT (phi 0.15); KXNHLSPREAD-26NOV05STLNJ-NJ2|no: DUPLICATIVE (phi 0.757); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis STL:OFFENSE_4PLUS (p 0.3375): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ3|no [DIRECT], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:WINS (p 0.4517): highest fidelity KXNHLSPREAD-26NOV05STLNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05STLNJ-NJ2|no (same contract)
- KXNHLTEAMTOTAL-26NOV05STLNJ-STL5|yes: FUNDED_RESEARCH; family MIXED; loses 47% of the draws where the thesis happens; opposing: failure thesis NJD:WINS (p 0.5483, phi -0.43)
- KXNHLGOAL-26NOV05STLNJ-STLRTHOMAS18-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 57% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4488, phi -0.263)
- KXNHLSPREAD-26NOV05STLNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3329, phi -1.0)
- KXNHLSPREAD-26NOV05STLNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.3329, phi -0.757)

portfolios: A EV +2.32 (adj +0.73) on $18.72, P(profit) 0.3312, adj growth 5.9 bp · B EV +1.48 (adj +0.50) on $13.15, P(profit) 0.3312, adj growth 4.4 bp · C EV +0.92 (adj +0.26) on $2.99, P(profit) 0.1801, adj growth 2.3 bp · R EV +0.51 (adj +0.14) on $4.00, P(profit) 0.6726, adj growth 4.7 bp

## CAR @ NYI  ·  10000 joint draws  ·  420 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_CAR_win | p_overtime | goals | shots NYI/CAR | NYI/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.116 | 0.43 | 0.57 | 0.00 | 6.0 | 21.3/32.8 | 28.8/18.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.112 | 0.51 | 0.49 | 0.00 | 6.01 | 26.3/26.9 | 23.3/22.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.45 | 0.55 | 0.50 | 5.9 | 21.3/32.9 | 29.6/18.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.100 | 0.49 | 0.51 | 0.48 | 5.94 | 26.6/27.3 | 24.0/23.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.55 | 0.45 | 0.00 | 9.32 | 28.5/29.1 | 23.1/21.9 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.085 | 0.45 | 0.55 | 0.00 | 9.23 | 22.6/34.4 | 27.7/17.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New York I wins by over 1.5 goals YES | 20 | 0.276 | 0.236 | +0.065 | +0.024 | $4.38 | FUNDED_RESEARCH | $2 | NYI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Ondrej Palat: 1+ goals YES | 12 | 0.157 | 0.144 | +0.029 | +0.017 | $3.66 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Victor Eklund: 1+ goals YES | 16 | 0.201 | 0.187 | +0.032 | +0.018 | $4.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.257 | 0.240 | +0.036 | +0.019 | $4.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **New York I wins by over 1.5 goals YES** — thesis: NYI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05CARNYI-NYI5|yes; why: higher confidence-adjusted growth (7.77 vs 6.10 bp); relationships: KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: REINFORCING (phi 0.173); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: REINFORCING (phi 0.174); failure: CAR wins (incl. OT/SO)
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (7.77 vs 5.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.131); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: MOSTLY_INDEPENDENT (phi 0.131); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: NYI offense suppressed (<= 2 goals)
- **Victor Eklund: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes has the higher standalone adjusted growth (7.77 vs 4.93 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.173); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.173); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: NYI offense suppressed (<= 2 goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes; why: Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes selected over player prop KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.39 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: REINFORCING (phi 0.174); KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis NYI:WINS_BY_2PLUS (p 0.2763): highest fidelity KXNHLSPREAD-26NOV05CARNYI-NYI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-NYI2|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3918): highest fidelity KXNHLTEAMTOTAL-26NOV05CARNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-NYI2|yes — Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes selected over player prop KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.39 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis NYI:WINS (p 0.4887): highest fidelity KXNHLSPREAD-26NOV05CARNYI-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05CARNYI-NYI2|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV05CARNYI-NYI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS (p 0.5113, phi -0.632)
- KXNHLGOAL-26NOV05CARNYI-NYIOPALAT81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3925, phi -0.182)
- KXNHLGOAL-26NOV05CARNYI-NYIVEKLUND73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3925, phi -0.209)
- KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3925, phi -0.244)
- override: Player prop expression KXNHLGOAL-26NOV05CARNYI-NYIBSCHENN10-1|yes selected over player prop KXNHLAST-26NOV05CARNYI-NYISHOLMSTROM92-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.39 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.06 (adj +0.95) on $18.72, P(profit) 0.5119, adj growth 8.1 bp · B EV +3.69 (adj +1.79) on $16.60, P(profit) 0.582, adj growth 15.7 bp · C EV +2.66 (adj +0.93) on $7.88, P(profit) 0.3423, adj growth 8.1 bp · R EV +0.62 (adj +0.23) on $2.00, P(profit) 0.2763, adj growth 7.8 bp

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
| Christian Dvorak: 1+ goals YES | 16 | 0.209 | 0.194 | +0.040 | +0.025 | $7.88 | FUNDED_RESEARCH | $2 | PHI:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
| Travis Konecny: 1+ assists NO | 68 | 0.748 | 0.711 | +0.052 | +0.016 | $18.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05PHINYR-NYR2|no; why: higher confidence-adjusted growth (9.46 vs 0.14 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0038 below the 0.010/contract floor; relationships: KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: INTENTIONAL_DIVERSIFIER (phi -0.252); failure: PHI offense suppressed (<= 2 goals)
- **Travis Konecny: 1+ assists NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV05PHINYR-PHIMMICHKOV39-1|no; why: higher confidence-adjusted growth (2.69 vs 0.01 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.252); failure: PHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NYR shot control · normal event (5-7) · decided (2+) 0.08.
- thesis PHI:OFFENSE_4PLUS (p 0.324): highest fidelity KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes (same contract)
- thesis PHI:SUPPRESSED (p 0.4549): highest fidelity KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no (same contract)
- KXNHLGOAL-26NOV05PHINYR-PHICDVORAK22-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4549, phi -0.22)
- KXNHLAST-26NOV05PHINYR-PHITKONECNY11-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.324, phi -0.238)

portfolios: A EV +1.61 (adj +0.83) on $11.95, P(profit) 0.209, adj growth 7.7 bp · B EV +3.27 (adj +1.59) on $26.78, P(profit) 0.8449, adj growth 14.0 bp · C EV +3.46 (adj +1.69) on $28.34, P(profit) 0.8449, adj growth 14.7 bp · R EV +0.47 (adj +0.29) on $2.00, P(profit) 0.209, adj growth 9.9 bp

## BOS @ PIT  ·  10000 joint draws  ·  424 bet sides mapped, 7 +EV candidates, 4 on card


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
| Connor Dewar: 1+ goals YES | 12 | 0.189 | 0.170 | +0.061 | +0.043 | $10.24 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 2+ goals YES | 6 | 0.092 | 0.081 | +0.029 | +0.017 | $2.80 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Rickard Rakell: 1+ goals YES | 33 | 0.391 | 0.373 | +0.045 | +0.028 | $6.17 | FUNDED_RESEARCH | $2 | PIT:OFFENSE_4PLUS | DIRECT (0.53) | EVIDENCE_STRONGER | D |
| Hendrix Lapierre: 1+ goals YES | 12 | 0.152 | 0.142 | +0.025 | +0.015 | $3.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV05BOSPIT-PIT6|yes; why: higher confidence-adjusted growth (35.01 vs 0.13 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.845 vs 0.323); alternative not eligible: confidence-adjusted EV +0.0023 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: BOS wins (incl. OT/SO)
- **Rickard Rakell: 2+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 9.88 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.004); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: DUPLICATIVE (phi 0.399); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: PIT offense suppressed (<= 2 goals)
- **Rickard Rakell: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: Player prop expression KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes because adjusted EV is 1.1 pts higher while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: DUPLICATIVE (phi 0.399); KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)
- **Hendrix Lapierre: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes has the higher standalone adjusted growth (35.01 vs 4.08 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis PIT:WINS_BY_2PLUS (p 0.3121): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes (same contract)
- thesis PIT:OFFENSE_4PLUS (p 0.4448): highest fidelity KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes — Player prop expression KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes because adjusted EV is 1.1 pts higher while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis PIT:SUPPRESSED (p 0.3355): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV05BOSPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:WINS (p 0.4798, phi -0.221)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-2|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.194)
- KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 47% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.267)
- KXNHLGOAL-26NOV05BOSPIT-PITHLAPIERRE22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3355, phi -0.156)
- override: Player prop expression KXNHLGOAL-26NOV05BOSPIT-PITRRAKELL67-1|yes selected over player prop KXNHLGOAL-26NOV05BOSPIT-PITNROBERTSON14-1|yes because adjusted EV is 1.1 pts higher while thesis capture is 0.53 vs 0.27 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +4.11 (adj +2.50) on $18.72, P(profit) 0.5098, adj growth 23.2 bp · B EV +7.69 (adj +5.08) on $22.78, P(profit) 0.3758, adj growth 43.8 bp · C EV +5.28 (adj +3.69) on $10.96, P(profit) 0.1887, adj growth 31.4 bp · R EV +0.26 (adj +0.16) on $2.00, P(profit) 0.3909, adj growth 5.8 bp

## DAL @ CBJ  ·  10000 joint draws  ·  392 bet sides mapped, 6 +EV candidates, 4 on card


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
| Columbus over 5.5 goals scored YES | 6 | 0.095 | 0.075 | +0.031 | +0.011 | $1.52 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.34) | EVIDENCE_MIXED | D |
| Charlie Coyle: 1+ goals YES | 24 | 0.285 | 0.270 | +0.033 | +0.018 | $4.32 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Columbus over 2.5 goals scored YES | 55 | 0.623 | 0.584 | +0.056 | +0.017 | $4.30 | FUNDED_RESEARCH | $2 | CBJ:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Mathieu Olivier: 1+ goals YES | 18 | 0.213 | 0.201 | +0.023 | +0.011 | $2.12 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.34) | EVIDENCE_STRONGER | D |
- **Columbus over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes; why: higher confidence-adjusted growth (4.22 vs 2.51 bp); despite a smaller raw edge (+0.031 vs +0.056/contract); relationships: KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: INTENTIONAL_DIVERSIFIER (phi 0.139); KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes: REINFORCING (phi 0.251); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: REINFORCING (phi 0.173); failure: DAL wins (incl. OT/SO)
- **Charlie Coyle: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes has the higher standalone adjusted growth (4.22 vs 3.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.139); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: INTENTIONAL_DIVERSIFIER (phi 0.139); KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes: REINFORCING (phi 0.233); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: CBJ offense suppressed (<= 2 goals)
- **Columbus over 2.5 goals scored YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes has the higher standalone adjusted growth (4.22 vs 2.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.251); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: REINFORCING (phi 0.251); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: REINFORCING (phi 0.233); KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: REINFORCING (phi 0.237); failure: CBJ offense suppressed (<= 2 goals)
- **Mathieu Olivier: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes; why: second expression of the same thesis: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes has the higher standalone adjusted growth (4.22 vs 1.70 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.173); they share one thesis budget; relationships: KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: REINFORCING (phi 0.173); KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: MOSTLY_INDEPENDENT (phi -0.0); KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes: REINFORCING (phi 0.237); failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis GAME:HIGH_EVENT (p 0.2477): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes (same contract)
- thesis CBJ:OFFENSE_4PLUS (p 0.397): highest fidelity KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CBJ:WINS_BY_2PLUS (p 0.3064): highest fidelity KXNHLSPREAD-26NOV05DALCBJ-CBJ2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes: FUNDED_RESEARCH; family MIXED; loses 66% of the draws where the thesis happens; opposing: failure thesis DAL:WINS (p 0.4675, phi -0.285)
- KXNHLGOAL-26NOV05DALCBJ-CBJCCOYLE3-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.234)
- KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ3|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.977)
- KXNHLGOAL-26NOV05DALCBJ-CBJMOLIVIER24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 66% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.3877, phi -0.245)
- override: override declined: the joint re-optimisation gives KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ4|yes less than the minimum stake; KXNHLTEAMTOTAL-26NOV05DALCBJ-CBJ6|yes kept

portfolios: A EV +2.48 (adj +0.71) on $18.72, P(profit) 0.5049, adj growth 5.3 bp · B EV +1.97 (adj +0.81) on $12.26, P(profit) 0.4332, adj growth 7.1 bp · C EV +1.08 (adj +0.38) on $2.26, P(profit) 0.0946, adj growth 3.3 bp · R EV +0.68 (adj +0.23) on $3.00, P(profit) 0.6232, adj growth 7.0 bp

## VAN @ WPG  ·  10000 joint draws  ·  408 bet sides mapped, 9 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WPG_win | p_VAN_win | p_overtime | goals | shots WPG/VAN | WPG/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.54 | 0.46 | 0.00 | 6.01 | 27.2/26.9 | 23.6/23.4 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.114 | 0.63 | 0.37 | 0.00 | 6.03 | 32.4/21.1 | 18.2/28.2 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.54 | 0.46 | 0.47 | 5.91 | 32.8/21.6 | 18.4/29.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.101 | 0.49 | 0.51 | 0.44 | 5.93 | 27.2/26.8 | 23.5/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.33 | 28.9/28.3 | 22.6/22.5 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.084 | 0.62 | 0.38 | 0.00 | 9.27 | 34.4/22.6 | 17.6/27.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vancouver wins by over 1.5 goals YES | 17 | 0.248 | 0.206 | +0.068 | +0.027 | $4.64 | FUNDED_RESEARCH | $2 | VAN:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Winnipeg wins by over 2.5 goals NO | 70 | 0.791 | 0.743 | +0.076 | +0.028 | $18.90 | FUNDED_RESEARCH | $5 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Brendan Gallagher: 1+ goals YES | 12 | 0.158 | 0.141 | +0.030 | +0.013 | $2.16 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Vancouver wins by over 1.5 goals YES** — thesis: VAN wins by 2+; alternative: KXNHLSPREAD-26NOV05VANWPG-WPG3|no; why: higher confidence-adjusted growth (10.33 vs 8.56 bp); despite a smaller raw edge (+0.068 vs +0.076/contract); relationships: KXNHLSPREAD-26NOV05VANWPG-WPG3|no: REINFORCING (phi 0.295); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: REINFORCING (phi 0.186); failure: WPG wins (incl. OT/SO)
- **Winnipeg wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.33 vs 8.56 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.295); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.295); KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.093); failure: WPG wins by 2+
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes has the higher standalone adjusted growth (10.33 vs 3.45 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.186); they share one thesis budget; relationships: KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: REINFORCING (phi 0.186); KXNHLSPREAD-26NOV05VANWPG-WPG3|no: MOSTLY_INDEPENDENT (phi 0.093); failure: VAN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.11, WPG shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:WINS_BY_2PLUS (p 0.2479): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis VAN:WINS (p 0.4566): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- thesis WPG:SUPPRESSED (p 0.366): highest fidelity KXNHLSPREAD-26NOV05VANWPG-WPG3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV05VANWPG-WPG3|no (same contract)
- KXNHLSPREAD-26NOV05VANWPG-VAN2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS (p 0.5434, phi -0.626)
- KXNHLSPREAD-26NOV05VANWPG-WPG3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis WPG:WINS_BY_2PLUS (p 0.3234, phi -0.744)
- KXNHLGOAL-26NOV05VANWPG-VANBGALLAGHER7-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4226, phi -0.204)

portfolios: A EV +4.10 (adj +1.39) on $18.72, P(profit) 0.6766, adj growth 12.0 bp · B EV +4.28 (adj +1.66) on $25.70, P(profit) 0.7907, adj growth 14.6 bp · C EV +2.62 (adj +1.02) on $6.93, P(profit) 0.2479, adj growth 8.9 bp · R EV +1.29 (adj +0.49) on $7.00, P(profit) 0.2479, adj growth 16.6 bp

## ANA @ EDM  ·  10000 joint draws  ·  98 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_ANA_win | p_overtime | goals | shots EDM/ANA | EDM/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.140 | 0.59 | 0.41 | 0.00 | 9.64 | 29.5/29.4 | 23.7/22.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.120 | 0.60 | 0.40 | 0.00 | 6.1 | 28.0/28.2 | 24.9/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.51 | 0.49 | 0.47 | 6.04 | 28.1/28.2 | 24.8/24.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.073 | 0.67 | 0.33 | 0.00 | 9.59 | 34.8/23.9 | 18.9/26.6 | even strength |
| balanced shots · high event (8+) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.59 | 9.99 | 30.0/30.2 | 23.6/23.2 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.064 | 0.57 | 0.43 | 0.00 | 6.03 | 22.4/32.7 | 29.4/18.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Anaheim over 4.5 goals scored YES | 20 | 0.263 | 0.224 | +0.052 | +0.013 | $3.39 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | DIRECT (0.61) | EVIDENCE_MIXED | D |
- **Anaheim over 4.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA6|yes; why: higher confidence-adjusted growth (2.12 vs 1.77 bp); wins across more scripts (relative breadth 0.533 vs 0.348); alternative not eligible: confidence-adjusted EV +0.0084 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: EDM wins (incl. OT/SO)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.4305): highest fidelity KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes (same contract)
- KXNHLTEAMTOTAL-26NOV05ANAEDM-ANA5|yes: FUNDED_RESEARCH; family MIXED; loses 39% of the draws where the thesis happens; opposing: failure thesis EDM:WINS (p 0.5694, phi -0.489)

portfolios: A EV +1.50 (adj +0.37) on $6.13, P(profit) 0.2629, adj growth 2.9 bp · B EV +0.83 (adj +0.20) on $3.39, P(profit) 0.2629, adj growth 1.8 bp · C EV +0.88 (adj +0.22) on $3.59, P(profit) 0.2629, adj growth 1.9 bp · R EV +0.24 (adj +0.06) on $1.00, P(profit) 0.2629, adj growth 2.1 bp

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
