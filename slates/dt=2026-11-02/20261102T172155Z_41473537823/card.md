# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T17:21:55Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +22.02 | +10.63 | +10.12 | 0.578 | -55.03 | -66.75 | 80.70 |
| B thesis-diversified (joint) ← optimiser card | 122.74 | +14.20 | +8.11 | +9.30 | 0.588 | -36.72 | -51.35 | 70.76 |
| C best expression per thesis | 73.34 | +11.09 | +5.55 | +4.44 | 0.571 | -29.14 | -39.77 | 47.85 |
| R FUNDED research stakes | 17.00 | +1.22 | +0.77 | +3.52 | 0.571 | -9.26 | -10.61 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  428 bet sides mapped, 1 +EV candidates, 1 on card

sportsbook moneyline consensus (5 books): home 0.479 / away 0.521

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_VGK_win | p_overtime | goals | shots BOS/VGK | BOS/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.52 | 0.48 | 0.00 | 6.02 | 27.2/27.5 | 24.1/23.5 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.52 | 0.48 | 0.47 | 6.0 | 27.3/27.6 | 24.4/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.54 | 0.46 | 0.00 | 9.37 | 28.7/29.0 | 23.0/22.2 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.092 | 0.47 | 0.53 | 0.00 | 6.03 | 21.6/32.5 | 28.7/18.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.080 | 0.48 | 0.52 | 0.47 | 5.95 | 21.7/32.8 | 29.3/18.5 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.058 | 0.46 | 0.54 | 0.00 | 9.21 | 23.3/34.3 | 27.7/17.8 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Casey Mittelstadt: 1+ goals YES | 15 | 0.185 | 0.175 | +0.026 | +0.016 | $4.63 | FUNDED_RESEARCH | $2 | BOS:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
- **Casey Mittelstadt: 1+ goals YES** — thesis: BOS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02VGKBOS-BOSPZACHA18-1|yes; why: higher confidence-adjusted growth (4.35 vs 0.01 bp); alternative not eligible: confidence-adjusted EV +0.0008 below the 0.010/contract floor; relationships: only recommended bet in this game; failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BOS:OFFENSE_4PLUS (p 0.4201): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02VGKBOS-BOSCMITTELSTADT11-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3655, phi -0.188)

portfolios: A EV +1.31 (adj +0.81) on $7.84, P(profit) 0.1854, adj growth 6.3 bp · B EV +0.77 (adj +0.48) on $4.63, P(profit) 0.1854, adj growth 4.1 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.33 (adj +0.21) on $2.00, P(profit) 0.1854, adj growth 6.4 bp

## DET @ FLA  ·  10000 joint draws  ·  416 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.618 / away 0.382

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.58 | 0.42 | 0.00 | 6.02 | 26.9/27.0 | 23.9/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.52 | 0.48 | 0.46 | 5.95 | 27.2/27.1 | 23.8/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.61 | 0.39 | 0.00 | 9.41 | 28.6/28.7 | 23.0/21.8 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.078 | 0.66 | 0.34 | 0.00 | 6.03 | 31.7/21.2 | 18.4/27.3 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.066 | 0.52 | 0.48 | 0.00 | 6.05 | 21.8/31.6 | 27.9/18.5 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.57 | 0.43 | 0.49 | 5.91 | 32.0/22.1 | 18.9/28.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 63 | 0.700 | 0.681 | +0.053 | +0.035 | $17.15 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.126 | 0.112 | +0.030 | +0.016 | $3.89 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.674 | 0.659 | +0.037 | +0.023 | $12.85 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Alex DeBrincat: 1+ goals YES | 35 | 0.398 | 0.385 | +0.032 | +0.019 | $7.37 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | DIRECT (0.59) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (11.59 vs 4.91 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLTOTAL-26NOV02DETFLA-8|yes; why: higher confidence-adjusted growth (6.39 vs 1.80 bp); despite a smaller raw edge (+0.030 vs +0.042/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.885 vs 0.336); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (11.59 vs 4.91 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: FLA offense succeeds (4+ goals)
- **Alex DeBrincat: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.59 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.009); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3456): highest fidelity KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3612): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes (same contract)
- thesis GAME:HIGH_EVENT (p 0.2844): highest fidelity KXNHLTOTAL-26NOV02DETFLA-7|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.262)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3456, phi -0.149)
- KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4446, phi -0.23)
- KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 41% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4281, phi -0.322)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-DETADEBRINCAT93-1|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.59 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +6.41 (adj +2.26) on $49.79, P(profit) 0.4726, adj growth 17.6 bp · B EV +4.04 (adj +2.41) on $41.26, P(profit) 0.6111, adj growth 21.5 bp · C EV +3.37 (adj +1.61) on $28.48, P(profit) 0.7774, adj growth 14.4 bp · R EV +0.41 (adj +0.27) on $5.00, P(profit) 0.6997, adj growth 9.7 bp

## COL @ CHI  ·  10000 joint draws  ·  432 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.330 / away 0.670

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.146 | 0.28 | 0.72 | 0.00 | 6.08 | 21.6/34.7 | 29.7/19.1 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.126 | 0.43 | 0.56 | 0.46 | 5.97 | 22.0/34.7 | 31.1/18.8 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.109 | 0.24 | 0.76 | 0.00 | 9.3 | 22.9/36.2 | 28.0/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.34 | 0.66 | 0.00 | 6.01 | 27.6/28.5 | 24.1/24.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.30 | 0.70 | 0.00 | 9.36 | 29.0/30.2 | 22.6/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.083 | 0.45 | 0.56 | 0.45 | 5.96 | 27.5/28.4 | 24.9/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Tyler Bertuzzi: 1+ goals YES | 21 | 0.269 | 0.252 | +0.048 | +0.030 | $9.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_STRONGER | D |
| Cale Makar: 1+ goals NO | 77 | 0.815 | 0.803 | +0.033 | +0.020 | $20.00 | FUNDED_RESEARCH | $5 | COL:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 62 | 0.697 | 0.648 | +0.060 | +0.012 | $12.19 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.81) | EVIDENCE_MIXED | D |
| Nathan MacKinnon: 1+ assists NO | 41 | 0.477 | 0.439 | +0.050 | +0.012 | $3.92 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | COL:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2|yes; why: higher confidence-adjusted growth (11.50 vs 1.59 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: INTENTIONAL_DIVERSIFIER (phi -0.132); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: CHI offense suppressed (<= 2 goals)
- **Cale Makar: 1+ goals NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no; why: higher confidence-adjusted growth (5.39 vs 1.22 bp); despite a smaller raw edge (+0.033 vs +0.050/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi 0.116); failure: COL offense succeeds (4+ goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (1.37 vs 0.79 bp); alternative not eligible: confidence-adjusted EV +0.0094 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.132); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi -0.007); KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: CHI offense succeeds (4+ goals)
- **Nathan MacKinnon: 1+ assists NO** — thesis: COL offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-2|no; why: higher confidence-adjusted growth (1.22 vs 0.15 bp); alternative not eligible: confidence-adjusted EV +0.0033 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: MOSTLY_INDEPENDENT (phi 0.116); KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.003); failure: COL offense succeeds (4+ goals)

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.13, COL shot control · high event (8+) · decided (2+) 0.11.
- thesis CHI:OFFENSE_4PLUS (p 0.3109): highest fidelity KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:WINS (p 0.3646): highest fidelity KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26NOV02COLCHI-CHI2|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4673): highest fidelity KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no [DIRECT], best adjusted EV KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no (same contract)
- KXNHLGOAL-26NOV02COLCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4673, phi -0.254)
- KXNHLGOAL-26NOV02COLCHI-COLCMAKAR8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5117, phi -0.167)
- KXNHLAST-26NOV02COLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 19% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3109, phi -0.24)
- KXNHLAST-26NOV02COLCHI-COLNMACKINNON29-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; fragile player expression; opposing: failure thesis COL:OFFENSE_4PLUS (p 0.5117, phi -0.3)

portfolios: A EV +5.76 (adj +2.21) on $49.79, P(profit) 0.5238, adj growth 18.2 bp · B EV +4.56 (adj +2.19) on $45.88, P(profit) 0.478, adj growth 19.2 bp · C EV +4.47 (adj +1.82) on $37.91, P(profit) 0.4337, adj growth 15.8 bp · R EV +0.21 (adj +0.13) on $5.00, P(profit) 0.8154, adj growth 4.7 bp

## CGY @ SJS  ·  10000 joint draws  ·  438 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.532 / away 0.468

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.60 | 0.40 | 0.00 | 6.06 | 28.8/28.7 | 25.5/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.92 | 28.8/28.8 | 25.5/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.57 | 0.43 | 0.00 | 9.32 | 29.9/29.8 | 24.3/23.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 6.02 | 33.7/22.7 | 20.0/29.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.46 | 5.98 | 33.9/23.0 | 19.8/30.6 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 6.03 | 22.9/33.3 | 30.0/19.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Zach Whitecloud: 1+ goals YES | 2 | 0.043 | 0.036 | +0.021 | +0.015 | $2.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DIFFUSE | NONE | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 77 | 0.823 | 0.807 | +0.041 | +0.025 | $20.00 | FUNDED_RESEARCH | $5 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
| Michael Misa: 1+ goals YES | 19 | 0.227 | 0.214 | +0.026 | +0.013 | $4.00 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.32) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 24 | 0.280 | 0.266 | +0.027 | +0.013 | $4.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
- **Zach Whitecloud: 1+ goals YES** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: CGY offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26NOV02CGYSJ-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (8.11 vs 0.00 bp); despite a smaller raw edge (+0.041 vs +0.047/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.018); failure: SJS offense succeeds (4+ goals)
- **Michael Misa: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (2.40 vs 2.05 bp); despite a smaller raw edge (+0.026 vs +0.027/contract); relationships: KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLAST-26NOV02CGYSJ-SJJTROUBA65-1|yes; why: higher confidence-adjusted growth (2.05 vs 0.07 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0027 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.018); KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: MOSTLY_INDEPENDENT (phi -0.027); failure: SJS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.4478): highest fidelity KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes (same contract)
- thesis SJS:SUPPRESSED (p 0.3356): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02CGYSJ-CGYZWHITECLOUD28-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; no single thesis (diffuse); fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.4202, phi -0.09)
- KXNHLGOAL-26NOV02CGYSJ-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.4478, phi -0.182)
- KXNHLGOAL-26NOV02CGYSJ-SJMMISA77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 68% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3356, phi -0.2)
- KXNHLGOAL-26NOV02CGYSJ-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3356, phi -0.207)

portfolios: A EV +8.54 (adj +5.35) on $42.58, P(profit) 0.4077, adj growth 38.7 bp · B EV +4.83 (adj +3.03) on $30.97, P(profit) 0.4077, adj growth 25.9 bp · C EV +3.25 (adj +2.12) on $6.95, P(profit) 0.3094, adj growth 17.6 bp · R EV +0.26 (adj +0.16) on $5.00, P(profit) 0.8232, adj growth 5.9 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
