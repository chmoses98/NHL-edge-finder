# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-08T23:45:53Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +24.13 | +8.27 | +5.55 | 0.517 | -62.68 | -78.85 | 54.40 |
| B thesis-diversified (joint) ← optimiser card | 94.26 | +14.87 | +9.07 | +6.78 | 0.547 | -42.91 | -48.88 | 78.81 |
| C best expression per thesis | 50.66 | +11.74 | +5.76 | +3.01 | 0.614 | -26.95 | -50.66 | 49.40 |
| R FUNDED research stakes | 17.00 | +1.12 | +0.55 | +2.00 | 0.634 | -4.59 | -10.41 | 0.00 |

## NJD @ TOR  ·  10000 joint draws  ·  434 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.409 / away 0.591

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_NJD_win | p_overtime | goals | shots TOR/NJD | TOR/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.132 | 0.45 | 0.55 | 0.00 | 6.04 | 22.9/35.6 | 31.7/19.6 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.48 | 5.91 | 23.3/35.9 | 32.6/20.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.54 | 0.46 | 0.00 | 5.99 | 29.0/29.7 | 26.4/25.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.47 | 5.95 | 29.2/30.1 | 26.8/25.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.084 | 0.44 | 0.56 | 0.00 | 9.27 | 24.7/37.8 | 31.0/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.53 | 0.47 | 0.00 | 9.27 | 30.5/31.3 | 25.3/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 9 | 0.150 | 0.131 | +0.054 | +0.036 | $8.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Colton Sissons: 1+ goals YES | 9 | 0.128 | 0.117 | +0.032 | +0.022 | $5.29 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Easton Cowan: 1+ goals YES | 17 | 0.214 | 0.202 | +0.035 | +0.022 | $6.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 59 | 0.647 | 0.631 | +0.040 | +0.025 | $15.05 | FUNDED_RESEARCH | $4 | NJD:SUPPRESSED | DIRECT (0.80) | EVIDENCE_STRONGER | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes; why: higher confidence-adjusted growth (30.82 vs 7.26 bp); relationships: KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: TOR offense suppressed (<= 2 goals)
- **Colton Sissons: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (30.82 vs 11.51 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.011); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TOR offense suppressed (<= 2 goals)
- **Easton Cowan: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes has the higher standalone adjusted growth (30.82 vs 7.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: TOR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26NOV08NJTOR-NJ4|no; why: Player prop expression KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.80 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: NJD offense succeeds (4+ goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.3902): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-TOR3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TOR:WINS_BY_2PLUS (p 0.2854): highest fidelity KXNHLSPREAD-26NOV08NJTOR-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:SUPPRESSED (p 0.3972): highest fidelity KXNHLTEAMTOTAL-26NOV08NJTOR-NJ4|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08NJTOR-NJ4|no (same contract)
- KXNHLGOAL-26NOV08NJTOR-TORTBLUEGER73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.203)
- KXNHLGOAL-26NOV08NJTOR-TORCSISSONS15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.163)
- KXNHLGOAL-26NOV08NJTOR-TORECOWAN53-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3946, phi -0.224)
- KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 20% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3788, phi -0.258)
- override: Player prop expression KXNHLGOAL-26NOV08NJTOR-NJJHUGHES86-1|no selected over player prop KXNHLAST-26NOV08NJTOR-NJERODRIGUES17-1|no because adjusted EV differs by only 0.4 pts while thesis capture is 0.80 vs 0.93 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +5.55 (adj +1.63) on $50.00, P(profit) 0.6607, adj growth 13.7 bp · B EV +8.67 (adj +5.64) on $34.92, P(profit) 0.4163, adj growth 48.3 bp · C EV +6.42 (adj +3.67) on $20.97, P(profit) 0.6608, adj growth 31.3 bp · R EV +0.26 (adj +0.16) on $4.00, P(profit) 0.6469, adj growth 5.7 bp

## PHI @ CGY  ·  10000 joint draws  ·  452 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.483 / away 0.517

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CGY_win | p_PHI_win | p_overtime | goals | shots CGY/PHI | CGY/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.48 | 0.52 | 0.00 | 6.0 | 27.3/27.2 | 23.6/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.119 | 0.50 | 0.50 | 0.45 | 5.88 | 27.2/27.0 | 23.8/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.076 | 0.48 | 0.52 | 0.00 | 9.25 | 29.0/28.9 | 22.7/23.0 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.074 | 0.57 | 0.43 | 0.00 | 5.99 | 31.8/21.7 | 18.6/27.8 | even strength |
| CGY shot control · normal event (5-7) · tight (1-goal/OT) | 0.068 | 0.50 | 0.50 | 0.50 | 5.91 | 32.3/21.7 | 18.4/29.1 | even strength |
| PHI shot control · normal event (5-7) · decided (2+) | 0.063 | 0.42 | 0.58 | 0.00 | 5.97 | 21.7/31.9 | 27.8/18.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Noah Cates: 1+ goals YES | 12 | 0.151 | 0.142 | +0.024 | +0.015 | $3.93 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 77 | 0.813 | 0.800 | +0.031 | +0.018 | $20.00 | FUNDED_RESEARCH | $5 | PHI:SUPPRESSED | DIRECT (0.90) | EVIDENCE_STRONGER | D |
| Jonathan Castagna: 1+ goals YES | 9 | 0.114 | 0.107 | +0.018 | +0.011 | $2.71 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.18) | EVIDENCE_STRONGER | D |
| Martin Pospisil: 1+ goals YES | 11 | 0.136 | 0.127 | +0.019 | +0.010 | $2.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
- **Noah Cates: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-PHICKNUBLE54-1|yes; why: higher confidence-adjusted growth (4.28 vs 1.32 bp); alternative not eligible: confidence-adjusted EV +0.0085 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi -0.01); failure: PHI offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no; why: Player prop expression KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no selected over player prop KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV08PHICGY-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.017); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PHI offense succeeds (4+ goals)
- **Jonathan Castagna: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (2.95 vs 1.98 bp); despite a smaller raw edge (+0.018 vs +0.020/contract); relationships: KXNHLGOAL-26NOV08PHICGY-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CGY offense suppressed (<= 2 goals)
- **Martin Pospisil: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes; why: higher confidence-adjusted growth (2.13 vs 1.98 bp); despite a smaller raw edge (+0.019 vs +0.020/contract); relationships: KXNHLGOAL-26NOV08PHICGY-PHINCATES27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CGY offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis PHI:SUPPRESSED (p 0.4269): highest fidelity KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no — Player prop expression KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no selected over player prop KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis CGY:OFFENSE_4PLUS (p 0.3493): highest fidelity KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV08PHICGY-CGYMBACKLUND11-1|yes (same contract)
- thesis PHI:OFFENSE_4PLUS (p 0.3556): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV08PHICGY-PHINCATES27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4269, phi -0.164)
- KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no: FUNDED_RESEARCH; family TRUSTED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3556, phi -0.187)
- KXNHLGOAL-26NOV08PHICGY-CGYJCASTAGNA38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 82% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4282, phi -0.143)
- KXNHLGOAL-26NOV08PHICGY-CGYMPOSPISIL76-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4282, phi -0.188)
- override: Player prop expression KXNHLGOAL-26NOV08PHICGY-PHIPMARTONE94-1|no selected over player prop KXNHLAST-26NOV08PHICGY-PHITKONECNY11-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.90 vs 0.86 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.61 (adj +2.25) on $50.00, P(profit) 0.7251, adj growth 18.7 bp · B EV +2.48 (adj +1.44) on $29.34, P(profit) 0.3166, adj growth 12.6 bp · C EV +2.49 (adj +0.96) on $23.32, P(profit) 0.7362, adj growth 8.4 bp · R EV +0.20 (adj +0.11) on $5.00, P(profit) 0.8132, adj growth 4.0 bp

## PIT @ ANA  ·  10000 joint draws  ·  448 bet sides mapped, 13 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.522 / away 0.478

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_ANA_win | p_PIT_win | p_overtime | goals | shots ANA/PIT | ANA/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · high event (8+) · decided (2+) | 0.135 | 0.69 | 0.31 | 0.00 | 9.73 | 29.4/29.2 | 23.9/21.6 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.118 | 0.70 | 0.30 | 0.00 | 6.09 | 27.4/27.2 | 24.4/22.9 | even strength |
| ANA shot control · high event (8+) · decided (2+) | 0.096 | 0.77 | 0.23 | 0.00 | 9.58 | 34.3/23.0 | 18.7/25.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.094 | 0.56 | 0.44 | 0.47 | 6.08 | 27.6/27.4 | 24.0/24.1 | even strength |
| ANA shot control · normal event (5-7) · decided (2+) | 0.087 | 0.73 | 0.27 | 0.00 | 6.05 | 32.4/21.5 | 19.0/27.6 | even strength |
| ANA shot control · normal event (5-7) · tight (1-goal/OT) | 0.069 | 0.58 | 0.42 | 0.47 | 6.01 | 32.6/22.1 | 18.8/29.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jeff Malott: 1+ goals YES | 11 | 0.156 | 0.143 | +0.039 | +0.027 | $5.02 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | ANA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Pittsburgh wins by over 2.5 goals NO | 82 | 0.889 | 0.852 | +0.059 | +0.022 | $16.45 | FUNDED_RESEARCH | $5 | ANA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Beckett Sennecke: 1+ goals YES | 35 | 0.401 | 0.387 | +0.035 | +0.021 | $5.32 | FUNDED_RESEARCH | $2 | ANA:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_STRONGER | D |
| Anaheim over 3.5 goals scored YES | 52 | 0.599 | 0.557 | +0.061 | +0.019 | $3.21 | FUNDED_RESEARCH | $1 | ANA:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Jeff Malott: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: higher confidence-adjusted growth (14.68 vs 11.70 bp); despite a smaller raw edge (+0.039 vs +0.066/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.816 vs 0.322); relationships: KXNHLSPREAD-26NOV08PITANA-PIT3|no: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes: MOSTLY_INDEPENDENT (phi 0.137); failure: ANA offense suppressed (<= 2 goals)
- **Pittsburgh wins by over 2.5 goals NO** — thesis: ANA wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes has the higher standalone adjusted growth (11.70 vs 7.35 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.178); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.069); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: MOSTLY_INDEPENDENT (phi 0.116); KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes: DUPLICATIVE (phi 0.337); failure: PIT wins by 2+
- **Beckett Sennecke: 1+ goals YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26NOV08PITANA-PIT3|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes: REINFORCING (phi 0.256); failure: ANA offense suppressed (<= 2 goals)
- **Anaheim over 3.5 goals scored YES** — thesis: ANA offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes selected over broad KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.48 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: MOSTLY_INDEPENDENT (phi 0.137); KXNHLSPREAD-26NOV08PITANA-PIT3|no: DUPLICATIVE (phi 0.337); KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: REINFORCING (phi 0.256); failure: ANA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · high event (8+) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, ANA shot control · high event (8+) · decided (2+) 0.10.
- thesis ANA:OFFENSE_4PLUS (p 0.5882): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes — Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis GAME:HIGH_EVENT (p 0.4031): highest fidelity KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes — Broad expression KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes selected over broad KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.48 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis ANA:WINS (p 0.6384): highest fidelity KXNHLSPREAD-26NOV08PITANA-PIT3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV08PITANA-ANAJMALOTT39-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.134)
- KXNHLSPREAD-26NOV08PITANA-PIT3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis PIT:WINS_BY_2PLUS (p 0.1863, phi -0.739)
- KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 49% of the draws where the thesis happens; fragile player expression; opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.247)
- KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis ANA:SUPPRESSED (p 0.2252, phi -0.659)
- override: Player prop expression KXNHLGOAL-26NOV08PITANA-ANABSENNECKE45-1|yes selected over player prop KXNHLGOAL-26NOV08PITANA-ANAAKILLORN17-1|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.51 vs 0.32 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- override: Broad expression KXNHLTEAMTOTAL-26NOV08PITANA-ANA4|yes selected over broad KXNHLTEAMTOTAL-26NOV08PITANA-ANA6|yes because adjusted EV differs by only 0.7 pts while thesis capture is 0.87 vs 0.48 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +13.97 (adj +4.39) on $50.00, P(profit) 0.4562, adj growth 22.0 bp · B EV +3.73 (adj +1.99) on $30.00, P(profit) 0.4717, adj growth 17.9 bp · C EV +2.83 (adj +1.13) on $6.37, P(profit) 0.2143, adj growth 9.7 bp · R EV +0.66 (adj +0.28) on $8.00, P(profit) 0.3739, adj growth 10.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
