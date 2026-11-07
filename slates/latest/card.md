# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-07T23:37:22Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.03 | +27.76 | +7.96 | +26.96 | 0.757 | -21.77 | -34.13 | 72.25 |
| B thesis-diversified (joint) ← optimiser card | 149.99 | +27.21 | +14.76 | +24.49 | 0.722 | -27.55 | -40.09 | 137.91 |
| C best expression per thesis | 150.00 | +25.57 | +11.48 | +23.96 | 0.719 | -26.65 | -40.20 | 106.14 |
| R FUNDED research stakes | 19.00 | +3.10 | +1.80 | +1.82 | 0.576 | -7.80 | -9.91 | 0.00 |

## MTL @ TOR  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.473 / away 0.527

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_MTL_win | p_overtime | goals | shots TOR/MTL | TOR/MTL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.56 | 0.44 | 0.00 | 6.11 | 29.0/29.1 | 25.8/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.117 | 0.52 | 0.48 | 0.00 | 9.47 | 30.5/30.4 | 24.1/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.50 | 0.50 | 0.47 | 6.06 | 28.9/29.0 | 25.5/25.5 | even strength |
| MTL shot control · normal event (5-7) · decided (2+) | 0.071 | 0.47 | 0.53 | 0.00 | 6.07 | 23.0/34.0 | 30.0/19.7 | even strength |
| TOR shot control · normal event (5-7) · decided (2+) | 0.064 | 0.59 | 0.41 | 0.00 | 6.09 | 33.9/23.0 | 19.9/29.5 | even strength |
| MTL shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.49 | 0.51 | 0.47 | 5.94 | 23.2/34.0 | 30.4/20.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Teddy Blueger: 1+ goals YES | 11 | 0.169 | 0.151 | +0.052 | +0.034 | $4.10 | FUNDED_RESEARCH | $2 | TOR:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Nick Suzuki: 1+ assists NO | 47 | 0.620 | 0.519 | +0.133 | +0.032 | $5.72 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Nick Suzuki: 2+ assists NO | 84 | 0.917 | 0.871 | +0.068 | +0.022 | $8.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MTL:SUPPRESSED | DIRECT (0.99) | EVIDENCE_MIXED | D |
- **Teddy Blueger: 1+ goals YES** — thesis: TOR offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (23.42 vs 0.83 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: MOSTLY_INDEPENDENT (phi -0.012); failure: TOR offense suppressed (<= 2 goals)
- **Nick Suzuki: 1+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07MTLTOR-MTL2|no; why: higher confidence-adjusted growth (8.88 vs 0.83 bp); alternative not eligible: confidence-adjusted EV +0.0090 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: DUPLICATIVE (phi 0.384); failure: MTL offense succeeds (4+ goals)
- **Nick Suzuki: 2+ assists NO** — thesis: MTL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no; why: second expression of the same thesis: KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no has the higher standalone adjusted growth (8.88 vs 8.13 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.384); they share one thesis budget; relationships: KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: DUPLICATIVE (phi 0.384); failure: MTL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:OFFENSE_4PLUS (p 0.4641): highest fidelity KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes (same contract)
- thesis MTL:SUPPRESSED (p 0.3655): highest fidelity KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no (same contract)
- KXNHLGOAL-26NOV07MTLTOR-TORTBLUEGER73-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:SUPPRESSED (p 0.3264, phi -0.194)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.5 pts; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4176, phi -0.288)
- KXNHLAST-26NOV07MTLTOR-MTLNSUZUKI14-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 1% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MTL:OFFENSE_4PLUS (p 0.4176, phi -0.229)

portfolios: A EV +4.15 (adj +1.85) on $16.67, P(profit) 0.6831, adj growth 17.2 bp · B EV +4.10 (adj +1.78) on $18.74, P(profit) 0.6831, adj growth 16.7 bp · C EV +4.72 (adj +2.02) on $14.18, P(profit) 0.6831, adj growth 18.6 bp · R EV +0.89 (adj +0.58) on $2.00, P(profit) 0.1691, adj growth 19.9 bp

## UTA @ OTT  ·  10000 joint draws  ·  446 bet sides mapped, 8 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.478 / away 0.522

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_UTA_win | p_overtime | goals | shots OTT/UTA | OTT/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.53 | 0.47 | 0.00 | 6.02 | 27.0/27.0 | 23.5/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.54 | 0.46 | 0.51 | 5.96 | 27.3/27.2 | 23.9/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.102 | 0.52 | 0.48 | 0.00 | 9.5 | 29.0/28.7 | 22.6/22.6 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.083 | 0.61 | 0.39 | 0.00 | 6.08 | 32.1/21.6 | 18.6/27.4 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.55 | 0.45 | 0.47 | 5.97 | 32.0/21.6 | 18.4/28.6 | even strength |
| UTA shot control · normal event (5-7) · decided (2+) | 0.057 | 0.45 | 0.55 | 0.00 | 6.0 | 21.5/31.8 | 27.9/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Lawson Crouse: 1+ goals YES | 16 | 0.212 | 0.198 | +0.043 | +0.029 | $3.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | UTA:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 16 | 0.201 | 0.190 | +0.032 | +0.020 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Dylan Guenther: 1+ goals NO | 66 | 0.708 | 0.695 | +0.032 | +0.019 | $6.88 | FUNDED_RESEARCH | $2 | UTA:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Tim Stutzle: 1+ goals YES | 33 | 0.370 | 0.359 | +0.025 | +0.014 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | DIRECT (0.52) | EVIDENCE_STRONGER | D |
- **Lawson Crouse: 1+ goals YES** — thesis: UTA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTAALEE72-1|yes; why: higher confidence-adjusted growth (12.49 vs 0.70 bp); alternative not eligible: confidence-adjusted EV +0.0075 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: UTA offense suppressed (<= 2 goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes; why: higher confidence-adjusted growth (6.35 vs 5.21 bp); despite a smaller raw edge (+0.032 vs +0.035/contract); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)
- **Dylan Guenther: 1+ goals NO** — thesis: UTA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV07UTAOTT-UTACKELLER9-1|no; why: higher confidence-adjusted growth (3.52 vs 1.51 bp); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: UTA offense succeeds (4+ goals)
- **Tim Stutzle: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes; why: Player prop expression KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes selected over player prop KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.52 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity); relationships: KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no: MOSTLY_INDEPENDENT (phi 0.006); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis UTA:OFFENSE_4PLUS (p 0.3923): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4332): highest fidelity KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes — Player prop expression KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes selected over player prop KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.52 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)
- thesis UTA:SUPPRESSED (p 0.3856): highest fidelity KXNHLGOAL-26NOV07UTAOTT-UTACKELLER9-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07UTAOTT-UTALCROUSE67-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:SUPPRESSED (p 0.3856, phi -0.214)
- KXNHLGOAL-26NOV07UTAOTT-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.199)
- KXNHLGOAL-26NOV07UTAOTT-UTADGUENTHER11-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis UTA:OFFENSE_4PLUS (p 0.3923, phi -0.213)
- KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 48% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.351, phi -0.266)
- override: Player prop expression KXNHLGOAL-26NOV07UTAOTT-OTTTSTUTZLE18-1|yes selected over player prop KXNHLGOAL-26NOV07UTAOTT-OTTDCOZENS24-1|yes because adjusted EV differs by only 0.8 pts while thesis capture is 0.52 vs 0.41 (DIRECT vs FRAGILE; reliability EVIDENCE_STRONGER vs EVIDENCE_STRONGER; decided on expression fidelity)

portfolios: A EV +2.57 (adj +1.24) on $16.67, P(profit) 0.5603, adj growth 11.4 bp · B EV +2.02 (adj +1.28) on $16.04, P(profit) 0.5353, adj growth 12.0 bp · C EV +2.23 (adj +1.43) on $16.46, P(profit) 0.3718, adj growth 13.2 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.7076, adj growth 2.1 bp

## NJD @ NYI  ·  10000 joint draws  ·  442 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.434 / away 0.566

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYI_win | p_NJD_win | p_overtime | goals | shots NYI/NJD | NYI/NJD starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.52 | 0.48 | 0.00 | 6.01 | 27.7/27.9 | 24.6/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.115 | 0.52 | 0.48 | 0.47 | 5.91 | 27.8/27.9 | 24.6/24.5 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.086 | 0.47 | 0.53 | 0.00 | 5.96 | 22.2/33.0 | 29.2/18.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.53 | 0.47 | 0.00 | 9.21 | 29.1/29.4 | 23.4/22.9 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.49 | 0.51 | 0.47 | 5.87 | 22.0/33.2 | 29.9/18.8 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.054 | 0.46 | 0.54 | 0.00 | 9.13 | 23.2/34.4 | 27.6/17.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Jean-Gabriel Pageau: 1+ goals YES | 13 | 0.171 | 0.158 | +0.033 | +0.020 | $2.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 1.5 goals NO | 65 | 0.737 | 0.691 | +0.071 | +0.025 | $6.47 | FUNDED_RESEARCH | $2 | NYI:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Jack Hughes: 1+ goals NO | 63 | 0.685 | 0.670 | +0.039 | +0.024 | $7.09 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Brayden Schenn: 1+ goals YES | 21 | 0.255 | 0.241 | +0.033 | +0.020 | $2.63 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
- **Jean-Gabriel Pageau: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: higher confidence-adjusted growth (7.28 vs 6.26 bp); despite a smaller raw edge (+0.033 vs +0.071/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.012); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: NYI offense suppressed (<= 2 goals)
- **New Jersey wins by over 1.5 goals NO** — thesis: NYI wins (incl. OT/SO); alternative: KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (6.26 vs 5.39 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.12); KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: REINFORCING (phi 0.162); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.143); failure: NJD wins by 2+
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26NOV07NJNYI-NJ2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07NJNYI-NJ2|no has the higher standalone adjusted growth (6.26 vs 5.39 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.162); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi 0.012); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: REINFORCING (phi 0.162); KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: MOSTLY_INDEPENDENT (phi 0.009); failure: NJD offense succeeds (4+ goals)
- **Brayden Schenn: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes has the higher standalone adjusted growth (7.28 vs 4.82 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.024); they share one thesis budget; relationships: KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: MOSTLY_INDEPENDENT (phi -0.024); KXNHLSPREAD-26NOV07NJNYI-NJ2|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: NYI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NJD shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYI:OFFENSE_4PLUS (p 0.3869): highest fidelity KXNHLTEAMTOTAL-26NOV07NJNYI-NYI3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYI:WINS (p 0.5205): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no (same contract)
- thesis NJD:SUPPRESSED (p 0.4205): highest fidelity KXNHLSPREAD-26NOV07NJNYI-NJ3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07NJNYI-NJ2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07NJNYI-NYIJPAGEAU44-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3938, phi -0.194)
- KXNHLSPREAD-26NOV07NJNYI-NJ2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2628, phi -1.0)
- KXNHLGOAL-26NOV07NJNYI-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.366, phi -0.247)
- KXNHLGOAL-26NOV07NJNYI-NYIBSCHENN10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.3938, phi -0.231)

portfolios: A EV +2.27 (adj +0.49) on $16.67, P(profit) 0.6609, adj growth 4.6 bp · B EV +2.09 (adj +1.09) on $18.63, P(profit) 0.6642, adj growth 10.2 bp · C EV +1.82 (adj +0.82) on $13.56, P(profit) 0.7621, adj growth 7.6 bp · R EV +0.33 (adj +0.15) on $4.00, P(profit) 0.5381, adj growth 5.6 bp

## CHI @ CAR  ·  10000 joint draws  ·  462 bet sides mapped, 19 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.787 / away 0.213

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CAR_win | p_CHI_win | p_overtime | goals | shots CAR/CHI | CAR/CHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.205 | 0.79 | 0.21 | 0.00 | 6.04 | 34.4/20.2 | 18.0/29.3 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.160 | 0.81 | 0.19 | 0.00 | 9.39 | 36.3/21.7 | 17.7/27.3 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.152 | 0.57 | 0.43 | 0.49 | 5.97 | 34.5/20.7 | 17.5/30.9 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.081 | 0.74 | 0.26 | 0.00 | 3.48 | 32.9/19.1 | 18.0/30.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.070 | 0.74 | 0.26 | 0.00 | 6.03 | 28.0/26.6 | 24.0/23.2 | even strength |
| CAR shot control · low event (<=4) · tight (1-goal/OT) | 0.064 | 0.57 | 0.43 | 0.52 | 2.9 | 33.0/19.1 | 17.6/31.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dillon Boucher: 1+ goals YES | 5 | 0.089 | 0.077 | +0.036 | +0.024 | $2.52 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.703 | 0.680 | +0.067 | +0.044 | $9.76 | FUNDED_RESEARCH | $3 | CAR:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 19 | 0.243 | 0.227 | +0.042 | +0.026 | $3.84 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.41) | EVIDENCE_STRONGER | D |
| Oliver Moore: 1+ goals YES | 12 | 0.153 | 0.143 | +0.026 | +0.015 | $2.03 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Dillon Boucher: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (23.40 vs 9.45 bp); despite a smaller raw edge (+0.036 vs +0.042/contract); relationships: KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: CHI offense suppressed (<= 2 goals)
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLGAME-26NOV07CHICAR-CAR|no; why: higher confidence-adjusted growth (18.05 vs 8.19 bp); despite a smaller raw edge (+0.067 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.007); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.016); failure: CAR offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGAME-26NOV07CHICAR-CAR|no; why: higher confidence-adjusted growth (9.45 vs 8.19 bp); despite a smaller raw edge (+0.042 vs +0.102/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)
- **Oliver Moore: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes has the higher standalone adjusted growth (9.45 vs 4.47 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.007); they share one thesis budget; relationships: KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi -0.016); KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.20, CAR shot control · high event (8+) · decided (2+) 0.16, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.15.
- thesis CAR:SUPPRESSED (p 0.2461): highest fidelity KXNHLSPREAD-26NOV07CHICAR-CAR3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:OFFENSE_4PLUS (p 0.2753): highest fidelity KXNHLTEAMTOTAL-26NOV07CHICAR-CHI3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.313): highest fidelity KXNHLGAME-26NOV07CHICAR-CHI|yes [STRUCTURAL], best adjusted EV KXNHLGAME-26NOV07CHICAR-CHI|yes (same contract)
- KXNHLGOAL-26NOV07CHICAR-CHIDBOUCHER36-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.159)
- KXNHLGOAL-26NOV07CHICAR-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.5519, phi -0.228)
- KXNHLGOAL-26NOV07CHICAR-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 59% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.253)
- KXNHLGOAL-26NOV07CHICAR-CHIOMOORE11-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.5084, phi -0.178)

portfolios: A EV +3.81 (adj +0.76) on $16.67, P(profit) 0.604, adj growth 6.8 bp · B EV +3.96 (adj +2.54) on $18.16, P(profit) 0.3833, adj growth 23.8 bp · C EV +2.21 (adj +1.42) on $16.40, P(profit) 0.777, adj growth 13.3 bp · R EV +0.32 (adj +0.21) on $3.00, P(profit) 0.7034, adj growth 7.8 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07CHICAR-CAR|no == KXNHLGAME-26NOV07CHICAR-CHI|yes

## SJS @ DAL  ·  10000 joint draws  ·  456 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.723 / away 0.277

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DAL_win | p_SJS_win | p_overtime | goals | shots DAL/SJS | DAL/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.69 | 0.31 | 0.00 | 6.0 | 26.3/26.0 | 23.2/21.9 | even strength |
| DAL shot control · normal event (5-7) · decided (2+) | 0.114 | 0.74 | 0.26 | 0.00 | 5.98 | 31.4/20.7 | 18.4/26.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.52 | 0.48 | 0.48 | 5.94 | 26.7/26.4 | 23.2/23.4 | even strength |
| DAL shot control · normal event (5-7) · tight (1-goal/OT) | 0.089 | 0.59 | 0.41 | 0.47 | 5.87 | 31.7/20.7 | 17.7/28.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.68 | 0.32 | 0.00 | 9.37 | 28.1/27.7 | 22.6/21.0 | even strength |
| DAL shot control · high event (8+) · decided (2+) | 0.075 | 0.77 | 0.23 | 0.00 | 9.29 | 33.3/22.0 | 17.8/24.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Dallas wins by over 1.5 goals NO | 50 | 0.594 | 0.545 | +0.077 | +0.027 | $5.96 | FUNDED_RESEARCH | $2 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| San Jose over 1.5 goals scored YES | 67 | 0.747 | 0.706 | +0.062 | +0.021 | $8.02 | FUNDED_RESEARCH | $3 | SJS:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Macklin Celebrini: 1+ assists NO | 53 | 0.611 | 0.566 | +0.064 | +0.018 | $8.80 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ goals YES | 19 | 0.223 | 0.214 | +0.022 | +0.013 | $1.42 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
- **Dallas wins by over 1.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes; why: higher confidence-adjusted growth (6.46 vs 4.31 bp); relationships: KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes: REINFORCING (phi 0.435); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.139); failure: DAL wins by 2+
- **San Jose over 1.5 goals scored YES** — thesis: SJS wins (incl. OT/SO); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL2|no; why: second expression of the same thesis: KXNHLSPREAD-26NOV07SJDAL-DAL2|no has the higher standalone adjusted growth (6.46 vs 4.31 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.435); they share one thesis budget; relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: REINFORCING (phi 0.435); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.324); KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes: REINFORCING (phi 0.208); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07SJDAL-SJISTENBERG41-1|no; why: higher confidence-adjusted growth (2.93 vs 1.65 bp); relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: INTENTIONAL_DIVERSIFIER (phi -0.211); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes: INTENTIONAL_DIVERSIFIER (phi -0.324); KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07SJDAL-DAL2|no; why: Player prop expression KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.36 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLSPREAD-26NOV07SJDAL-DAL2|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes: REINFORCING (phi 0.208); KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.112); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, DAL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis GAME:TIGHT (p 0.4148): highest fidelity KXNHLSPREAD-26NOV07SJDAL-DAL2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.284): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no — Player prop expression KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.36 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DAL:SUPPRESSED (p 0.3168): highest fidelity KXNHLTEAMTOTAL-26NOV07SJDAL-DAL4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26NOV07SJDAL-DAL2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLSPREAD-26NOV07SJDAL-DAL2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DAL:WINS_BY_2PLUS (p 0.4057, phi -1.0)
- KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis SJS:SUPPRESSED (p 0.5044, phi -0.577)
- KXNHLAST-26NOV07SJDAL-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 23% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.284, phi -0.297)
- KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.5044, phi -0.231)
- override: override declined: the joint re-optimisation gives KXNHLSPREAD-26NOV07SJDAL-DAL3|no less than the minimum stake; KXNHLTEAMTOTAL-26NOV07SJDAL-SJ2|yes kept
- override: Player prop expression KXNHLGOAL-26NOV07SJDAL-SJMMARCHMENT27-1|yes selected over broad KXNHLTEAMTOTAL-26NOV07SJDAL-SJ4|yes because adjusted EV differs by only 0.9 pts while thesis capture is 0.36 vs 1.00 (FRAGILE vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.03 (adj +0.70) on $16.67, P(profit) 0.4928, adj growth 5.8 bp · B EV +2.79 (adj +0.94) on $24.20, P(profit) 0.523, adj growth 8.8 bp · C EV +2.66 (adj +0.94) on $29.41, P(profit) 0.5797, adj growth 8.8 bp · R EV +0.57 (adj +0.19) on $5.00, P(profit) 0.5368, adj growth 7.0 bp
equivalent contracts collapsed: KXNHLGAME-26NOV07SJDAL-SJ|yes == KXNHLGAME-26NOV07SJDAL-DAL|no

## TBL @ MIN  ·  10000 joint draws  ·  428 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.449 / away 0.551

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_TBL_win | p_overtime | goals | shots MIN/TBL | MIN/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.124 | 0.50 | 0.50 | 0.50 | 6.0 | 27.8/27.9 | 24.6/24.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.48 | 0.52 | 0.00 | 6.0 | 27.6/27.9 | 24.3/24.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.094 | 0.47 | 0.53 | 0.00 | 9.45 | 29.5/29.6 | 23.1/23.4 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.073 | 0.40 | 0.60 | 0.00 | 5.99 | 22.0/32.8 | 28.7/19.1 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.062 | 0.48 | 0.52 | 0.47 | 5.96 | 22.5/33.0 | 29.8/19.2 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.059 | 0.48 | 0.52 | 0.00 | 6.04 | 32.2/22.0 | 18.4/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Yakov Trenin: 1+ goals YES | 9 | 0.138 | 0.125 | +0.043 | +0.029 | $3.54 | FUNDED_RESEARCH | $1 | MIN:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Michael McCarron: 1+ goals YES | 11 | 0.155 | 0.143 | +0.038 | +0.026 | $3.43 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Bobby Brink: 1+ goals YES | 14 | 0.187 | 0.174 | +0.038 | +0.025 | $3.41 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Quinn Hughes: 1+ assists NO | 37 | 0.444 | 0.405 | +0.058 | +0.018 | $4.57 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
- **Yakov Trenin: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (20.94 vs 10.94 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: MOSTLY_INDEPENDENT (phi -0.035); failure: MIN offense suppressed (<= 2 goals)
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes; why: higher confidence-adjusted growth (13.88 vs 10.94 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.02); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); failure: MIN offense suppressed (<= 2 goals)
- **Bobby Brink: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07TBMIN-MINBCOLEMAN20-1|yes; why: higher confidence-adjusted growth (10.94 vs 4.88 bp); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi 0.024); KXNHLGOAL-26NOV07TBMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: MIN offense suppressed (<= 2 goals)
- **Quinn Hughes: 1+ assists NO** — thesis: MIN offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no; why: higher confidence-adjusted growth (3.04 vs 2.46 bp); despite a smaller raw edge (+0.058 vs +0.089/contract); relationships: KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: MOSTLY_INDEPENDENT (phi -0.035); KXNHLGOAL-26NOV07TBMIN-MINMMCCARRON47-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.065); failure: MIN offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis MIN:OFFENSE_4PLUS (p 0.384): highest fidelity KXNHLAST-26NOV07TBMIN-MINJBRODIN25-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:SUPPRESSED (p 0.388): highest fidelity KXNHLAST-26NOV07TBMIN-MINMBOLDY12-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis TBL:SUPPRESSED (p 0.3573): highest fidelity KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07TBMIN-TBNKUCHEROV86-1|no (same contract)
- KXNHLGOAL-26NOV07TBMIN-MINYTRENIN13-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.169)
- KXNHLGOAL-26NOV07TBMIN-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.174)
- KXNHLGOAL-26NOV07TBMIN-MINBBRINK10-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.388, phi -0.203)
- KXNHLAST-26NOV07TBMIN-MINQHUGHES43-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:OFFENSE_4PLUS (p 0.384, phi -0.321)

portfolios: A EV +3.39 (adj +0.66) on $16.67, P(profit) 0.6627, adj growth 6.0 bp · B EV +4.27 (adj +2.64) on $14.95, P(profit) 0.4083, adj growth 24.5 bp · C EV +2.87 (adj +1.07) on $12.33, P(profit) 0.3779, adj growth 9.9 bp · R EV +0.44 (adj +0.31) on $1.00, P(profit) 0.1383, adj growth 11.2 bp

## DET @ COL  ·  10000 joint draws  ·  454 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.664 / away 0.336

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_COL_win | p_DET_win | p_overtime | goals | shots COL/DET | COL/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.74 | 0.26 | 0.00 | 5.99 | 28.6/28.2 | 25.7/23.9 | even strength |
| COL shot control · normal event (5-7) · decided (2+) | 0.112 | 0.76 | 0.24 | 0.00 | 6.01 | 33.7/22.1 | 19.8/28.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.54 | 0.46 | 0.47 | 5.99 | 28.4/28.0 | 24.6/25.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.098 | 0.73 | 0.27 | 0.00 | 9.37 | 30.0/29.7 | 24.8/22.4 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.088 | 0.80 | 0.20 | 0.00 | 9.32 | 35.9/23.7 | 19.8/27.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.60 | 0.40 | 0.44 | 5.98 | 34.2/22.6 | 19.3/30.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Carter Mazur: 1+ goals YES | 6 | 0.085 | 0.075 | +0.021 | +0.011 | $1.29 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Artturi Lehkonen: 1+ assists YES | 28 | 0.344 | 0.309 | +0.050 | +0.015 | $2.48 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_MIXED | D |
| Sam Malinski: 1+ assists YES | 25 | 0.318 | 0.277 | +0.055 | +0.013 | $1.84 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_MIXED | D |
| Lucas Raymond: 1+ assists NO | 61 | 0.682 | 0.638 | +0.055 | +0.012 | $4.22 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Carter Mazur: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHL2PTOTAL-26NOV07DETCOL-2|yes; why: higher confidence-adjusted growth (4.44 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.022); failure: DET offense suppressed (<= 2 goals)
- **Artturi Lehkonen: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes; why: higher confidence-adjusted growth (2.44 vs 2.01 bp); despite a smaller raw edge (+0.050 vs +0.055/contract); relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: MOSTLY_INDEPENDENT (phi 0.046); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: COL offense suppressed (<= 2 goals)
- **Sam Malinski: 1+ assists YES** — thesis: COL offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes; why: second expression of the same thesis: KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes has the higher standalone adjusted growth (2.44 vs 2.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.046); they share one thesis budget; relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi 0.046); KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: COL offense suppressed (<= 2 goals)
- **Lucas Raymond: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLPTS-26NOV07DETCOL-DETLRAYMOND23-1|no; why: higher confidence-adjusted growth (1.30 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: MOSTLY_INDEPENDENT (phi -0.022); KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: DET offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, COL shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis COL:OFFENSE_4PLUS (p 0.5356): highest fidelity KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes [FRAGILE], best adjusted EV KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4945): highest fidelity KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.2909): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV07DETCOL-DETCMAZUR34-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4945, phi -0.143)
- KXNHLAST-26NOV07DETCOL-COLALEHKONEN62-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2617, phi -0.236)
- KXNHLAST-26NOV07DETCOL-COLSMALINSKI70-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:SUPPRESSED (p 0.2617, phi -0.218)
- KXNHLAST-26NOV07DETCOL-DETLRAYMOND23-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.2909, phi -0.265)

portfolios: A EV +2.82 (adj +0.87) on $16.67, P(profit) 0.5131, adj growth 7.7 bp · B EV +1.60 (adj +0.53) on $9.82, P(profit) 0.4579, adj growth 4.9 bp · C EV +0.95 (adj +0.25) on $8.02, P(profit) 0.3437, adj growth 2.3 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## PIT @ LAK  ·  10000 joint draws  ·  436 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.526 / away 0.474

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_PIT_win | p_overtime | goals | shots LAK/PIT | LAK/PIT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.127 | 0.57 | 0.42 | 0.00 | 5.99 | 27.7/27.5 | 24.1/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.53 | 0.47 | 0.43 | 5.93 | 27.3/27.4 | 24.2/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.088 | 0.58 | 0.42 | 0.00 | 9.24 | 29.0/29.0 | 23.4/22.4 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.071 | 0.64 | 0.36 | 0.00 | 6.02 | 32.4/22.0 | 19.3/28.2 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.55 | 0.45 | 0.46 | 5.9 | 32.2/22.0 | 18.9/28.8 | even strength |
| PIT shot control · normal event (5-7) · decided (2+) | 0.066 | 0.47 | 0.53 | 0.00 | 6.02 | 21.7/31.7 | 27.8/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Joel Edmundson: 1+ goals YES | 5 | 0.075 | 0.068 | +0.022 | +0.014 | $1.67 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Blake Lizotte: 1+ goals YES | 10 | 0.126 | 0.118 | +0.019 | +0.012 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:WINS_BY_2PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ben Kindel: 1+ assists NO | 71 | 0.777 | 0.738 | +0.052 | +0.014 | $7.54 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | PIT:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Connor Dewar: 1+ goals YES | 13 | 0.157 | 0.149 | +0.019 | +0.011 | $1.59 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PIT:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
- **Joel Edmundson: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26NOV07PITLA-PIT2|no; why: higher confidence-adjusted growth (8.55 vs 0.07 bp); despite a smaller raw edge (+0.022 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0026 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: LAK offense suppressed (<= 2 goals)
- **Blake Lizotte: 1+ goals YES** — thesis: PIT wins by 2+; alternative: KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes; why: higher confidence-adjusted growth (3.17 vs 2.12 bp); relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: PIT offense suppressed (<= 2 goals)
- **Ben Kindel: 1+ assists NO** — thesis: PIT offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV07PITLA-PITSCROSBY87-1|no; why: higher confidence-adjusted growth (2.14 vs 1.21 bp); relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.019); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi -0.029); KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense succeeds (4+ goals)
- **Connor Dewar: 1+ goals YES** — thesis: PIT offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes has the higher standalone adjusted growth (3.17 vs 2.12 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.002); they share one thesis budget; relationships: KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: MOSTLY_INDEPENDENT (phi -0.025); KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: MOSTLY_INDEPENDENT (phi -0.044); failure: PIT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis PIT:WINS_BY_2PLUS (p 0.2416): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:OFFENSE_4PLUS (p 0.3534): highest fidelity KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PIT:SUPPRESSED (p 0.4178): highest fidelity KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no (same contract)
- KXNHLGOAL-26NOV07PITLA-LAJEDMUNDSON6-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.357, phi -0.132)
- KXNHLGOAL-26NOV07PITLA-PITBLIZOTTE46-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4178, phi -0.192)
- KXNHLAST-26NOV07PITLA-PITBKINDEL81-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:OFFENSE_4PLUS (p 0.3534, phi -0.232)
- KXNHLGOAL-26NOV07PITLA-PITCDEWAR19-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PIT:SUPPRESSED (p 0.4178, phi -0.197)

portfolios: A EV +1.47 (adj +0.65) on $16.67, P(profit) 0.5014, adj growth 6.1 bp · B EV +1.73 (adj +0.89) on $12.38, P(profit) 0.2881, adj growth 8.3 bp · C EV +0.95 (adj +0.37) on $10.34, P(profit) 0.8088, adj growth 3.4 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## VAN @ EDM  ·  10000 joint draws  ·  428 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.751 / away 0.249

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_VAN_win | p_overtime | goals | shots EDM/VAN | EDM/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| EDM shot control · normal event (5-7) · decided (2+) | 0.147 | 0.80 | 0.20 | 0.00 | 6.08 | 33.2/21.1 | 18.9/28.0 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.141 | 0.80 | 0.20 | 0.00 | 9.49 | 34.8/22.3 | 18.3/25.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.106 | 0.73 | 0.27 | 0.00 | 9.52 | 29.1/28.3 | 23.6/21.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.103 | 0.73 | 0.27 | 0.00 | 6.12 | 27.3/26.6 | 24.1/22.8 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.096 | 0.59 | 0.41 | 0.45 | 6.0 | 33.4/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.54 | 0.46 | 0.48 | 6.02 | 27.7/27.1 | 23.8/24.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Vasily Podkolzin: 1+ goals YES | 27 | 0.348 | 0.326 | +0.065 | +0.042 | $7.01 | FUNDED_RESEARCH | $2 | EDM:OFFENSE_4PLUS | FRAGILE (0.45) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.221 | 0.204 | +0.051 | +0.035 | $4.66 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Brendan Gallagher: 1+ goals YES | 10 | 0.144 | 0.130 | +0.037 | +0.024 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ goals YES | 11 | 0.146 | 0.136 | +0.029 | +0.019 | $2.47 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: higher confidence-adjusted growth (19.17 vs 1.50 bp); despite a smaller raw edge (+0.065 vs +0.091/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.015); failure: EDM offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (18.39 vs 4.89 bp); relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Brendan Gallagher: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes has the higher standalone adjusted growth (18.39 vs 12.85 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.009); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.023); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: VAN offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes; why: second expression of the same thesis: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes has the higher standalone adjusted growth (19.17 vs 7.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts EDM shot control · normal event (5-7) · decided (2+) 0.15, EDM shot control · high event (8+) · decided (2+) 0.14, balanced shots · high event (8+) · decided (2+) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.5979): highest fidelity KXNHLAST-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:OFFENSE_4PLUS (p 0.3223): highest fidelity KXNHLTEAMTOTAL-26NOV07VANEDM-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2184): highest fidelity KXNHLSPREAD-26NOV07VANEDM-EDM3|no [STRUCTURAL], best adjusted EV KXNHLAST-26NOV07VANEDM-EDMCMCDAVID97-2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV07VANEDM-EDMVPODKOLZIN92-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 55% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.226)
- KXNHLGOAL-26NOV07VANEDM-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.239)
- KXNHLGOAL-26NOV07VANEDM-VANBGALLAGHER7-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4569, phi -0.19)
- KXNHLGOAL-26NOV07VANEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2184, phi -0.131)

portfolios: A EV +4.25 (adj +0.74) on $16.67, P(profit) 0.5544, adj growth 6.6 bp · B EV +4.65 (adj +3.07) on $17.07, P(profit) 0.6315, adj growth 28.6 bp · C EV +7.16 (adj +3.16) on $29.30, P(profit) 0.4929, adj growth 29.1 bp · R EV +0.45 (adj +0.30) on $2.00, P(profit) 0.3483, adj growth 11.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
