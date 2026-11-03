# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-03T12:28:16Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.99 | +29.07 | +9.44 | +23.93 | 0.649 | -54.48 | -73.35 | 72.53 |
| B thesis-diversified (joint) ← optimiser card | 76.66 | +15.52 | +6.32 | +12.15 | 0.626 | -35.86 | -46.84 | 54.86 |
| C best expression per thesis | 55.11 | +16.16 | +6.65 | +12.11 | 0.577 | -31.63 | -55.10 | 57.56 |
| R FUNDED research stakes | 20.00 | +4.29 | +1.71 | +3.01 | 0.584 | -9.51 | -13.90 | 0.00 |

## UTA @ TOR  ·  10000 joint draws  ·  430 bet sides mapped, 2 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_UTA_win | p_overtime | goals | shots TOR/UTA | TOR/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.51 | 0.49 | 0.00 | 6.09 | 28.4/28.8 | 25.2/24.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.110 | 0.51 | 0.49 | 0.00 | 9.45 | 30.3/30.9 | 24.9/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.49 | 0.51 | 0.48 | 5.98 | 28.6/29.0 | 25.5/25.2 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.094 | 0.46 | 0.54 | 0.00 | 6.02 | 22.6/34.5 | 30.6/19.3 | even strength |
| UTA shot control · high event (8+) · decided (2+) | 0.092 | 0.43 | 0.57 | 0.00 | 9.42 | 24.3/36.3 | 29.1/18.9 | even strength |
| UTA shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.47 | 0.53 | 0.48 | 5.98 | 22.9/34.8 | 31.3/19.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 12 | 0.173 | 0.151 | +0.046 | +0.024 | $5.97 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Lawson Crouse: 1+ goals YES | 17 | 0.223 | 0.198 | +0.043 | +0.018 | $5.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03UTATOR-TOR6|yes; why: higher confidence-adjusted growth (11.04 vs 0.17 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.852 vs 0.341); alternative not eligible: confidence-adjusted EV +0.0028 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: TOR offense suppressed (<= 2 goals)
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03UTATOR-UTABHAYTON27-1|yes; why: higher confidence-adjusted growth (4.93 vs 0.26 bp); alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: UTA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis TOR:OFFENSE_4PLUS (p 0.4294): highest fidelity KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes (same contract)
- thesis UTA:OFFENSE_4PLUS (p 0.4395): highest fidelity KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes (same contract)
- KXNHLGOAL-26NOV03UTATOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3446, phi -0.195)
- KXNHLGOAL-26NOV03UTATOR-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3439, phi -0.2)

portfolios: A EV +4.67 (adj +2.26) on $15.59, P(profit) 0.3569, adj growth 18.4 bp · B EV +3.35 (adj +1.63) on $11.00, P(profit) 0.3569, adj growth 14.1 bp · C EV +3.35 (adj +1.63) on $11.00, P(profit) 0.3569, adj growth 14.1 bp · R EV +0.72 (adj +0.38) on $2.00, P(profit) 0.1734, adj growth 12.3 bp

## WPG @ MTL  ·  10000 joint draws  ·  366 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MTL_win | p_WPG_win | p_overtime | goals | shots MTL/WPG | MTL/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.05 | 27.1/27.0 | 24.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.50 | 5.95 | 27.3/27.4 | 24.1/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.65 | 0.35 | 0.00 | 9.22 | 28.5/28.4 | 23.4/21.7 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.68 | 0.32 | 0.00 | 6.04 | 31.6/21.4 | 18.8/27.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.067 | 0.56 | 0.44 | 0.00 | 6.01 | 21.4/31.7 | 28.2/17.8 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.52 | 0.48 | 0.46 | 5.92 | 32.1/21.9 | 18.8/28.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Winnipeg over 5.5 goals scored YES | 4 | 0.071 | 0.053 | +0.028 | +0.010 | $1.90 | FUNDED_RESEARCH | $1 | GAME:HIGH_EVENT | FRAGILE (0.24) | EVIDENCE_MIXED | D |
- **Winnipeg over 5.5 goals scored YES** — thesis: high-event game (8+ goals); alternative: KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG5|yes; why: higher confidence-adjusted growth (5.33 vs 0.83 bp); despite a smaller raw edge (+0.028 vs +0.031/contract); alternative not eligible: confidence-adjusted EV +0.0067 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: MTL wins (incl. OT/SO)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis GAME:HIGH_EVENT (p 0.2683): highest fidelity KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes [FRAGILE], best adjusted EV KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes (same contract)
- KXNHLTEAMTOTAL-26NOV03WPGMTL-WPG6|yes: FUNDED_RESEARCH; family MIXED; loses 76% of the draws where the thesis happens; opposing: failure thesis MTL:WINS (p 0.5815, phi -0.296)

portfolios: A EV +2.84 (adj +1.03) on $4.34, P(profit) 0.0706, adj growth 7.1 bp · B EV +1.24 (adj +0.45) on $1.90, P(profit) 0.0706, adj growth 3.9 bp · C EV +1.24 (adj +0.45) on $1.90, P(profit) 0.0706, adj growth 3.9 bp · R EV +0.65 (adj +0.24) on $1.00, P(profit) 0.0706, adj growth 6.7 bp

## DET @ TBL  ·  10000 joint draws  ·  404 bet sides mapped, 2 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_DET_win | p_overtime | goals | shots TBL/DET | TBL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.66 | 0.34 | 0.00 | 6.01 | 27.3/27.1 | 24.3/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.55 | 0.45 | 0.46 | 5.97 | 27.3/27.0 | 23.9/23.8 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.101 | 0.76 | 0.24 | 0.00 | 6.0 | 32.6/21.5 | 19.3/27.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.66 | 0.34 | 0.00 | 9.32 | 29.1/28.8 | 23.7/22.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.56 | 0.44 | 0.49 | 5.9 | 32.3/21.7 | 18.6/28.9 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.064 | 0.72 | 0.28 | 0.00 | 9.32 | 34.1/22.9 | 18.6/25.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tampa Bay wins by over 1.5 goals NO | 52 | 0.606 | 0.560 | +0.068 | +0.023 | $12.62 | FUNDED_RESEARCH | $4 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Tampa Bay wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26NOV03DETTB-TB3|no; why: higher confidence-adjusted growth (4.59 vs 1.83 bp); relationships: only recommended bet in this game; failure: TBL wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, TBL shot control · normal event (5-7) · decided (2+) 0.10.
- thesis GAME:TIGHT (p 0.415): highest fidelity KXNHLSPREAD-26NOV03DETTB-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03DETTB-TB2|no (same contract)
- KXNHLSPREAD-26NOV03DETTB-TB2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis TBL:WINS_BY_2PLUS (p 0.3944, phi -1.0)

portfolios: A EV +2.44 (adj +0.74) on $23.80, P(profit) 0.6056, adj growth 5.9 bp · B EV +1.60 (adj +0.54) on $12.62, P(profit) 0.6056, adj growth 4.7 bp · C EV +1.60 (adj +0.54) on $12.62, P(profit) 0.6056, adj growth 4.7 bp · R EV +0.51 (adj +0.17) on $4.00, P(profit) 0.6056, adj growth 5.7 bp

## STL @ NYR  ·  10000 joint draws  ·  382 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_STL_win | p_overtime | goals | shots NYR/STL | NYR/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.55 | 0.45 | 0.00 | 6.04 | 26.7/26.7 | 23.4/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.50 | 0.50 | 0.49 | 5.94 | 26.7/26.7 | 23.4/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.55 | 0.45 | 0.00 | 9.31 | 28.5/28.4 | 22.9/22.1 | even strength |
| NYR shot control · normal event (5-7) · decided (2+) | 0.072 | 0.63 | 0.37 | 0.00 | 6.04 | 31.4/21.3 | 18.5/27.3 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.070 | 0.48 | 0.52 | 0.00 | 6.0 | 21.4/31.7 | 27.9/18.1 | even strength |
| NYR shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.53 | 0.47 | 0.48 | 5.88 | 31.6/21.4 | 18.3/28.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## MIN @ PHI  ·  10000 joint draws  ·  412 bet sides mapped, 13 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PHI_win | p_MIN_win | p_overtime | goals | shots PHI/MIN | PHI/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.54 | 0.46 | 0.00 | 5.99 | 27.0/27.3 | 24.0/23.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.52 | 0.48 | 0.48 | 5.87 | 27.1/27.4 | 24.2/23.8 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.091 | 0.50 | 0.50 | 0.00 | 5.94 | 21.5/32.8 | 29.1/18.2 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.50 | 0.50 | 0.47 | 5.85 | 21.7/32.8 | 29.3/18.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.55 | 0.45 | 0.00 | 9.21 | 28.8/29.1 | 23.2/22.6 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.062 | 0.56 | 0.44 | 0.00 | 3.48 | 25.8/26.2 | 24.4/23.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Philadelphia wins by over 1.5 goals YES | 20 | 0.289 | 0.242 | +0.078 | +0.031 | $6.39 | FUNDED_RESEARCH | $2 | PHI:WINS_BY_2PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Philadelphia over 3.5 goals scored YES | 29 | 0.380 | 0.330 | +0.075 | +0.025 | $3.17 | FUNDED_RESEARCH | $1 | PHI:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Christian Dvorak: 1+ goals YES | 17 | 0.217 | 0.196 | +0.037 | +0.016 | $3.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Matt Boldy: 1+ goals NO | 64 | 0.687 | 0.670 | +0.031 | +0.014 | $7.20 | FUNDED_RESEARCH | $2 | MIN:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Philadelphia wins by over 1.5 goals YES** — thesis: PHI wins by 2+; alternative: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes; why: higher confidence-adjusted growth (12.46 vs 8.36 bp); relationships: KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: REINFORCING (phi 0.532); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: REINFORCING (phi 0.173); failure: MIN wins (incl. OT/SO)
- **Philadelphia over 3.5 goals scored YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes selected over broad KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.532); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: REINFORCING (phi 0.187); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.025); failure: PHI offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: second expression of the same thesis: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes has the higher standalone adjusted growth (12.46 vs 3.58 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.146); they share one thesis budget; relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: MOSTLY_INDEPENDENT (phi 0.146); KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: REINFORCING (phi 0.187); KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: MOSTLY_INDEPENDENT (phi 0.013); failure: PHI offense suppressed (<= 2 goals)
- **Matt Boldy: 1+ goals NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes; why: Player prop expression KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no selected over broad KXNHLSPREAD-26NOV03MINPHI-MIN3|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.78 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: REINFORCING (phi 0.173); KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: MOSTLY_INDEPENDENT (phi 0.025); KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, MIN shot control · normal event (5-7) · decided (2+) 0.09.
- thesis PHI:WINS_BY_2PLUS (p 0.2894): highest fidelity KXNHLSPREAD-26NOV03MINPHI-PHI2|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3682): highest fidelity KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — Broad expression KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes selected over broad KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis PHI:WINS (p 0.5266): highest fidelity KXNHLSPREAD-26NOV03MINPHI-MIN2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03MINPHI-PHI2|yes — Player prop expression KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no selected over broad KXNHLSPREAD-26NOV03MINPHI-MIN3|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.78 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLSPREAD-26NOV03MINPHI-PHI2|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis MIN:WINS (p 0.4734, phi -0.605)
- KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PHI:SUPPRESSED (p 0.4034, phi -0.643)
- KXNHLGOAL-26NOV03MINPHI-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4034, phi -0.2)
- KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.341, phi -0.265)
- override: Player prop expression KXNHLGOAL-26NOV03MINPHI-MINMBOLDY12-1|no selected over broad KXNHLSPREAD-26NOV03MINPHI-MIN3|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.78 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26NOV03MINPHI-PHI4|yes selected over broad KXNHLTEAMTOTAL-26NOV03MINPHI-PHI5|yes because adjusted EV is 0.4 pts higher while thesis capture is 1.00 vs 0.53 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.13 (adj +0.96) on $29.75, P(profit) 0.6469, adj growth 7.9 bp · B EV +4.13 (adj +1.63) on $19.83, P(profit) 0.4502, adj growth 14.1 bp · C EV +3.16 (adj +1.25) on $8.54, P(profit) 0.2894, adj growth 10.9 bp · R EV +1.08 (adj +0.42) on $5.00, P(profit) 0.3789, adj growth 14.2 bp
equivalent contracts collapsed: KXNHLGAME-26NOV03MINPHI-MIN|no == KXNHLGAME-26NOV03MINPHI-PHI|yes

## VGK @ PIT  ·  10000 joint draws  ·  400 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_PIT_win | p_VGK_win | p_overtime | goals | shots PIT/VGK | PIT/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.48 | 0.52 | 0.00 | 6.04 | 27.4/27.3 | 23.7/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.50 | 0.50 | 0.48 | 5.99 | 27.4/27.3 | 24.1/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.45 | 0.55 | 0.00 | 9.39 | 28.8/28.8 | 22.7/22.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.073 | 0.56 | 0.44 | 0.00 | 6.02 | 31.7/21.4 | 18.4/27.9 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.068 | 0.45 | 0.55 | 0.00 | 6.03 | 21.7/32.2 | 28.2/18.6 | even strength |
| PIT shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.53 | 0.47 | 0.47 | 5.94 | 32.5/22.0 | 18.7/29.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Connor Dewar: 1+ goals YES | 13 | 0.167 | 0.149 | +0.029 | +0.011 | $2.83 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHL2PSPREAD-26NOV03VGKPIT-PIT2|yes; why: higher confidence-adjusted growth (2.12 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis PIT:OFFENSE_4PLUS (p 0.4073): highest fidelity KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes (same contract)
- KXNHLGOAL-26NOV03VGKPIT-PITCDEWAR19-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.3735, phi -0.198)

portfolios: A EV +1.03 (adj +0.39) on $4.95, P(profit) 0.1666, adj growth 3.0 bp · B EV +0.59 (adj +0.22) on $2.83, P(profit) 0.1666, adj growth 1.9 bp · C EV +0.59 (adj +0.22) on $2.83, P(profit) 0.1666, adj growth 1.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## DAL @ WSH  ·  10000 joint draws  ·  402 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_WSH_win | p_DAL_win | p_overtime | goals | shots WSH/DAL | WSH/DAL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.132 | 0.56 | 0.44 | 0.00 | 5.98 | 25.9/26.0 | 22.8/22.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.50 | 0.50 | 0.47 | 5.96 | 26.1/26.2 | 23.0/22.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.082 | 0.60 | 0.40 | 0.00 | 9.35 | 27.6/27.7 | 22.2/20.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.076 | 0.50 | 0.50 | 0.00 | 5.95 | 20.7/30.8 | 27.1/17.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.47 | 0.53 | 0.46 | 5.86 | 20.6/30.8 | 27.5/17.5 | even strength |
| WSH shot control · normal event (5-7) · decided (2+) | 0.062 | 0.65 | 0.35 | 0.00 | 6.02 | 30.4/20.8 | 18.1/26.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Aliaksei Protas: 1+ goals YES | 18 | 0.235 | 0.211 | +0.045 | +0.021 | $5.98 | FUNDED_RESEARCH | $2 | WSH:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Aliaksei Protas: 1+ goals YES** — thesis: WSH offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV03DALWSH-WSHPDUBOIS80-1|yes; why: higher confidence-adjusted growth (6.28 vs 0.48 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: WSH offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis WSH:OFFENSE_4PLUS (p 0.4079): highest fidelity KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes (same contract)
- KXNHLGOAL-26NOV03DALWSH-WSHAPROTAS21-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WSH:SUPPRESSED (p 0.38, phi -0.234)

portfolios: A EV +1.95 (adj +0.92) on $8.26, P(profit) 0.2353, adj growth 7.5 bp · B EV +1.41 (adj +0.66) on $5.98, P(profit) 0.2353, adj growth 5.8 bp · C EV +1.41 (adj +0.66) on $5.98, P(profit) 0.2353, adj growth 5.8 bp · R EV +0.47 (adj +0.22) on $2.00, P(profit) 0.2353, adj growth 7.3 bp

## COL @ CBJ  ·  10000 joint draws  ·  408 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CBJ_win | p_COL_win | p_overtime | goals | shots CBJ/COL | CBJ/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.46 | 0.54 | 0.00 | 6.01 | 28.0/28.4 | 24.6/24.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.94 | 28.1/28.5 | 25.3/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.47 | 0.53 | 0.00 | 9.34 | 29.5/29.9 | 23.8/23.4 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.091 | 0.38 | 0.62 | 0.00 | 6.0 | 22.2/33.9 | 29.8/19.3 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.43 | 0.57 | 0.46 | 5.87 | 22.6/34.1 | 30.5/19.6 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.059 | 0.39 | 0.61 | 0.00 | 9.22 | 23.5/35.2 | 28.2/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sean Monahan: 1+ goals YES | 15 | 0.180 | 0.172 | +0.021 | +0.013 | $3.59 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | CBJ:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Sean Monahan: 1+ goals YES** — thesis: CBJ offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26NOV03COLCBJ-CBJ2|yes; why: higher confidence-adjusted growth (2.59 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: CBJ offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis CBJ:OFFENSE_4PLUS (p 0.3645): highest fidelity KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes (same contract)
- KXNHLGOAL-26NOV03COLCBJ-CBJSMONAHAN23-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CBJ:SUPPRESSED (p 0.4172, phi -0.211)

portfolios: A EV +0.51 (adj +0.30) on $3.80, P(profit) 0.1804, adj growth 2.6 bp · B EV +0.49 (adj +0.29) on $3.59, P(profit) 0.1804, adj growth 2.5 bp · C EV +0.49 (adj +0.29) on $3.59, P(profit) 0.1804, adj growth 2.5 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## EDM @ NJD  ·  10000 joint draws  ·  98 bet sides mapped, 8 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_EDM_win | p_overtime | goals | shots NJD/EDM | NJD/EDM starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.47 | 0.53 | 0.00 | 6.07 | 28.2/27.8 | 24.0/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.49 | 0.51 | 0.47 | 6.0 | 28.2/28.0 | 24.6/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.49 | 0.51 | 0.00 | 9.43 | 29.7/29.4 | 23.3/23.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.093 | 0.56 | 0.44 | 0.00 | 6.07 | 33.6/22.0 | 18.9/29.7 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.54 | 0.46 | 0.43 | 5.93 | 33.1/22.0 | 18.8/29.6 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.073 | 0.54 | 0.46 | 0.00 | 9.41 | 35.2/23.8 | 18.2/28.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| New Jersey wins by over 1.5 goals NO | 64 | 0.717 | 0.676 | +0.061 | +0.020 | $4.16 | FUNDED_RESEARCH | $2 | EDM:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **New Jersey wins by over 1.5 goals NO** — thesis: EDM wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes; why: KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes has the higher standalone adjusted growth (6.76 vs 3.80 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.325); relationships: only recommended bet in this game; failure: NJD wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis EDM:OFFENSE_4PLUS (p 0.4235): highest fidelity KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3061): highest fidelity KXNHLTOTAL-26NOV03EDMNJ-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:WINS (p 0.5035): highest fidelity KXNHLSPREAD-26NOV03EDMNJ-NJ2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV03EDMNJ-EDM5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV03EDMNJ-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2832, phi -1.0)

portfolios: A EV +5.33 (adj +1.69) on $29.75, P(profit) 0.5743, adj growth 12.2 bp · B EV +0.38 (adj +0.13) on $4.16, P(profit) 0.7168, adj growth 1.2 bp · C EV +1.96 (adj +0.67) on $5.60, P(profit) 0.2427, adj growth 5.8 bp · R EV +0.18 (adj +0.06) on $2.00, P(profit) 0.7168, adj growth 2.3 bp

## CAR @ NSH  ·  10000 joint draws  ·  98 bet sides mapped, 7 +EV candidates, 2 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_CAR_win | p_overtime | goals | shots NSH/CAR | NSH/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.143 | 0.38 | 0.62 | 0.00 | 6.02 | 21.6/34.5 | 30.1/18.7 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.47 | 0.53 | 0.46 | 6.0 | 21.9/34.8 | 31.2/18.7 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.113 | 0.38 | 0.62 | 0.00 | 9.35 | 23.0/35.8 | 28.1/17.9 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.098 | 0.45 | 0.55 | 0.00 | 6.03 | 27.3/28.3 | 24.5/24.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.084 | 0.45 | 0.55 | 0.00 | 9.38 | 29.1/30.1 | 23.3/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.50 | 0.50 | 0.47 | 5.97 | 27.6/28.6 | 25.3/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carolina wins by over 1.5 goals NO | 58 | 0.665 | 0.620 | +0.068 | +0.023 | $11.76 | FUNDED_RESEARCH | $3 | NSH:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Nashville over 4.5 goals scored YES | 15 | 0.211 | 0.176 | +0.053 | +0.017 | $2.99 | FUNDED_RESEARCH | $1 | NSH:OFFENSE_4PLUS | DIRECT (0.55) | EVIDENCE_MIXED | D |
- **Carolina wins by over 1.5 goals NO** — thesis: NSH wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes has the higher standalone adjusted growth (11.37 vs 4.78 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.220); relationships: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: DUPLICATIVE (phi 0.336); failure: CAR wins by 2+
- **Nashville over 4.5 goals scored YES** — thesis: NSH offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLSPREAD-26NOV03CARNSH-CAR2|no: DUPLICATIVE (phi 0.336); failure: CAR wins (incl. OT/SO)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.14, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.13, CAR shot control · high event (8+) · decided (2+) 0.11.
- thesis GAME:HIGH_EVENT (p 0.3104): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes — Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis NSH:WINS (p 0.45): highest fidelity KXNHLSPREAD-26NOV03CARNSH-CAR2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03CARNSH-CAR2|no (same contract)
- thesis NSH:OFFENSE_4PLUS (p 0.3814): highest fidelity KXNHLTEAMTOTAL-26NOV03CARNSH-NSH4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV03CARNSH-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV03CARNSH-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3351, phi -1.0)
- KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes: FUNDED_RESEARCH; family MIXED; loses 45% of the draws where the thesis happens; opposing: failure thesis CAR:WINS (p 0.55, phi -0.466)
- override: Broad expression KXNHLTEAMTOTAL-26NOV03CARNSH-NSH5|yes selected over broad KXNHLTEAMTOTAL-26NOV03CARNSH-NSH6|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.52 vs 0.28 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.18 (adj +1.15) on $29.75, P(profit) 0.5492, adj growth 8.0 bp · B EV +2.33 (adj +0.77) on $14.75, P(profit) 0.671, adj growth 6.7 bp · C EV +2.36 (adj +0.94) on $3.05, P(profit) 0.0946, adj growth 8.1 bp · R EV +0.67 (adj +0.22) on $4.00, P(profit) 0.671, adj growth 7.5 bp

## ANA @ VAN  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_ANA_win | p_overtime | goals | shots VAN/ANA | VAN/ANA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| ANA shot control · normal event (5-7) · decided (2+) | 0.129 | 0.39 | 0.61 | 0.00 | 6.11 | 21.7/33.6 | 29.1/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.110 | 0.45 | 0.55 | 0.00 | 6.05 | 27.3/28.0 | 24.2/23.8 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.46 | 0.54 | 0.45 | 6.02 | 22.0/34.0 | 30.4/18.8 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.102 | 0.35 | 0.65 | 0.00 | 9.49 | 23.0/35.6 | 27.8/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.45 | 0.55 | 0.00 | 9.51 | 29.0/29.9 | 23.1/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.48 | 0.52 | 0.45 | 6.05 | 27.4/28.1 | 24.6/24.1 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts ANA shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.11, ANA shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
