# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-21T00:26:42Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +34.37 | +9.12 | +33.04 | 0.727 | -37.11 | -55.02 | 76.15 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +34.38 | +19.03 | +25.36 | 0.647 | -50.38 | -65.58 | 166.61 |
| C best expression per thesis | 150.00 | +29.49 | +12.55 | +25.35 | 0.672 | -37.72 | -54.13 | 110.21 |
| R FUNDED research stakes | 22.00 | +2.43 | +1.06 | +1.89 | 0.654 | -8.00 | -10.48 | 0.00 |

## MIN @ EDM  ·  10000 joint draws  ·  480 bet sides mapped, 17 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.551 / away 0.449

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_MIN_win | p_overtime | goals | shots EDM/MIN | EDM/MIN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.64 | 0.36 | 0.00 | 6.06 | 28.3/28.3 | 25.3/24.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.116 | 0.65 | 0.35 | 0.00 | 9.45 | 30.2/30.0 | 24.5/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.47 | 5.95 | 28.8/28.5 | 25.2/25.4 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.083 | 0.67 | 0.33 | 0.00 | 5.99 | 33.5/22.5 | 19.8/29.0 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.067 | 0.54 | 0.46 | 0.48 | 5.97 | 34.2/22.9 | 19.7/30.6 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.066 | 0.70 | 0.30 | 0.00 | 9.6 | 35.8/24.4 | 19.6/27.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 12 | 0.190 | 0.171 | +0.062 | +0.044 | $9.87 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Kasperi Kapanen: 1+ assists YES | 22 | 0.311 | 0.263 | +0.079 | +0.031 | $6.96 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.42) | EVIDENCE_MIXED | D |
| Connor McDavid: 1+ assists NO | 32 | 0.410 | 0.362 | +0.074 | +0.027 | $11.40 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.67) | EVIDENCE_MIXED | D |
| Zach Hyman: 1+ goals YES | 32 | 0.375 | 0.360 | +0.040 | +0.025 | $9.02 | FUNDED_RESEARCH | $3 | EDM:OFFENSE_4PLUS | DIRECT (0.50) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: higher confidence-adjusted growth (36.35 vs 11.66 bp); despite a smaller raw edge (+0.062 vs +0.079/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: EDM offense suppressed (<= 2 goals)
- **Kasperi Kapanen: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes; why: higher confidence-adjusted growth (11.66 vs 5.96 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: MOSTLY_INDEPENDENT (phi 0.125); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.18 vs 2.63 bp); despite a smaller raw edge (+0.074 vs +0.093/contract); relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.055); KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi -0.049); KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.207); failure: EDM offense succeeds (4+ goals)
- **Zach Hyman: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes has the higher standalone adjusted growth (11.66 vs 5.96 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.125); they share one thesis budget; relationships: KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: MOSTLY_INDEPENDENT (phi 0.125); KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.207); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · high event (8+) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4983): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [STRUCTURAL], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:SUPPRESSED (p 0.2913): highest fidelity KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.3219): highest fidelity KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT20MINEDM-EDM3|yes (same contract)
- KXNHLGOAL-26OCT20MINEDM-EDMAFORMENTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.178)
- KXNHLAST-26OCT20MINEDM-EDMKKAPANEN42-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 58% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.211)
- KXNHLAST-26OCT20MINEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 33% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4983, phi -0.328)
- KXNHLGOAL-26OCT20MINEDM-EDMZHYMAN18-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 50% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2913, phi -0.265)

portfolios: A EV +8.50 (adj +2.84) on $37.50, P(profit) 0.7003, adj growth 24.5 bp · B EV +10.81 (adj +5.90) on $37.25, P(profit) 0.4194, adj growth 51.7 bp · C EV +6.68 (adj +2.63) on $32.70, P(profit) 0.5431, adj growth 23.2 bp · R EV +0.35 (adj +0.22) on $3.00, P(profit) 0.3749, adj growth 7.3 bp

## DET @ SEA  ·  10000 joint draws  ·  450 bet sides mapped, 18 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.485 / away 0.515

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_DET_win | p_overtime | goals | shots SEA/DET | SEA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.63 | 0.37 | 0.00 | 6.02 | 27.8/28.1 | 25.1/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.52 | 0.48 | 0.48 | 5.92 | 27.9/28.3 | 25.0/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.091 | 0.64 | 0.36 | 0.00 | 9.26 | 29.6/29.9 | 24.5/22.6 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.090 | 0.58 | 0.42 | 0.00 | 6.04 | 22.4/33.7 | 30.3/18.6 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.082 | 0.50 | 0.50 | 0.47 | 5.87 | 22.2/33.6 | 30.3/19.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.56 | 0.44 | 0.00 | 3.45 | 26.8/27.1 | 25.3/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ben Meyers: 1+ goals YES | 11 | 0.153 | 0.141 | +0.036 | +0.024 | $5.13 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Adam Larsson: 1+ assists YES | 19 | 0.313 | 0.230 | +0.113 | +0.029 | $5.47 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
| Dylan Larkin: 1+ goals NO | 68 | 0.741 | 0.725 | +0.046 | +0.030 | $17.55 | FUNDED_RESEARCH | $5 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
| Kaapo Kakko: 1+ goals YES | 17 | 0.213 | 0.201 | +0.033 | +0.021 | $5.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
- **Ben Meyers: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: higher confidence-adjusted growth (12.40 vs 11.45 bp); despite a smaller raw edge (+0.037 vs +0.113/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.023); KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: SEA offense suppressed (<= 2 goals)
- **Adam Larsson: 1+ assists YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes; why: higher confidence-adjusted growth (11.45 vs 6.68 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.074); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi 0.067); failure: SEA offense suppressed (<= 2 goals)
- **Dylan Larkin: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT20DETSEA-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.09 vs 6.02 bp); despite a smaller raw edge (+0.046 vs +0.070/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.023); KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.008); KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: DET offense succeeds (4+ goals)
- **Kaapo Kakko: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes; why: second expression of the same thesis: KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes has the higher standalone adjusted growth (11.45 vs 6.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.067); they share one thesis budget; relationships: KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: MOSTLY_INDEPENDENT (phi 0.067); KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: SEA offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis SEA:OFFENSE_4PLUS (p 0.4437): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [DIRECT], best adjusted EV KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis DET:SUPPRESSED (p 0.4539): highest fidelity KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.58): highest fidelity KXNHLSPREAD-26OCT20DETSEA-DET3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT20DETSEA-DET4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20DETSEA-SEABMEYERS59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.164)
- KXNHLAST-26OCT20DETSEA-SEAALARSSON6-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 12.8 pts; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.235)
- KXNHLGOAL-26OCT20DETSEA-DETDLARKIN71-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3287, phi -0.226)
- KXNHLGOAL-26OCT20DETSEA-SEAKKAKKO84-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.3419, phi -0.21)

portfolios: A EV +9.56 (adj +2.56) on $37.50, P(profit) 0.5286, adj growth 21.2 bp · B EV +6.77 (adj +3.21) on $33.16, P(profit) 0.4398, adj growth 28.5 bp · C EV +5.88 (adj +2.10) on $42.99, P(profit) 0.7482, adj growth 18.8 bp · R EV +0.33 (adj +0.21) on $5.00, P(profit) 0.7414, adj growth 7.7 bp

## CAR @ VAN  ·  10000 joint draws  ·  452 bet sides mapped, 34 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.280 / away 0.720

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VAN_win | p_CAR_win | p_overtime | goals | shots VAN/CAR | VAN/CAR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| CAR shot control · normal event (5-7) · decided (2+) | 0.171 | 0.37 | 0.63 | 0.00 | 6.02 | 20.8/34.0 | 29.5/18.0 | even strength |
| CAR shot control · normal event (5-7) · tight (1-goal/OT) | 0.144 | 0.48 | 0.52 | 0.48 | 5.95 | 21.1/34.6 | 31.1/17.8 | even strength |
| CAR shot control · high event (8+) · decided (2+) | 0.128 | 0.37 | 0.63 | 0.00 | 9.39 | 22.5/36.1 | 28.6/17.4 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.082 | 0.42 | 0.58 | 0.00 | 6.04 | 27.0/28.3 | 24.3/23.8 | even strength |
| CAR shot control · low event (<=4) · decided (2+) | 0.073 | 0.41 | 0.59 | 0.00 | 3.47 | 19.8/32.7 | 30.3/18.2 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.071 | 0.48 | 0.52 | 0.49 | 5.98 | 26.7/28.0 | 24.7/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Filip Chytil: 1+ goals YES | 16 | 0.249 | 0.225 | +0.080 | +0.056 | $12.57 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.39) | EVIDENCE_STRONGER | D |
| Carolina wins by over 1.5 goals NO | 49 | 0.657 | 0.545 | +0.149 | +0.038 | $5.32 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Carolina wins by over 2.5 goals NO | 62 | 0.769 | 0.669 | +0.133 | +0.033 | $9.35 | FUNDED_RESEARCH | $3 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Sebastian Aho: 1+ goals NO | 62 | 0.685 | 0.668 | +0.049 | +0.031 | $15.71 | FUNDED_RESEARCH | $4 | CAR:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Filip Chytil: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHL1PSPREAD-26OCT20CARVAN-VAN2|yes; why: higher confidence-adjusted growth (47.34 vs 25.62 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_THIN; relationships: KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: MOSTLY_INDEPENDENT (phi 0.134); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VAN offense suppressed (<= 2 goals)
- **Carolina wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 12.36 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.164); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: REINFORCING (phi 0.164); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.187); failure: CAR wins by 2+
- **Carolina wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes has the higher standalone adjusted growth (47.34 vs 10.04 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.134); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.134); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: DUPLICATIVE (phi 0.757); KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: REINFORCING (phi 0.162); failure: CAR wins by 2+
- **Sebastian Aho: 1+ goals NO** — thesis: CAR offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20CARVAN-CAR2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT20CARVAN-CAR2|no has the higher standalone adjusted growth (12.36 vs 9.26 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.187); they share one thesis budget; relationships: KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLSPREAD-26OCT20CARVAN-CAR2|no: REINFORCING (phi 0.187); KXNHLSPREAD-26OCT20CARVAN-CAR3|no: REINFORCING (phi 0.162); failure: CAR offense succeeds (4+ goals)

**Review**: scripts CAR shot control · normal event (5-7) · decided (2+) 0.17, CAR shot control · normal event (5-7) · tight (1-goal/OT) 0.14, CAR shot control · high event (8+) · decided (2+) 0.13.
- thesis VAN:OFFENSE_4PLUS (p 0.3652): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS (p 0.4391): highest fidelity KXNHLSPREAD-26OCT20CARVAN-CAR2|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:SCORES_FIRST (p 0.4662): highest fidelity KXNHLTEAMTOTAL-26OCT20CARVAN-VAN2|yes [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20CARVAN-CAR2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20CARVAN-VANFCHYTIL77-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 61% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4186, phi -0.236)
- KXNHLSPREAD-26OCT20CARVAN-CAR2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 17.2 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -1.0)
- KXNHLSPREAD-26OCT20CARVAN-CAR3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.4 pts; opposing: failure thesis CAR:WINS_BY_2PLUS (p 0.3434, phi -0.757)
- KXNHLGOAL-26OCT20CARVAN-CARSAHO20-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CAR:OFFENSE_4PLUS (p 0.458, phi -0.245)

portfolios: A EV +12.32 (adj +2.85) on $37.50, P(profit) 0.5489, adj growth 22.7 bp · B EV +10.62 (adj +5.80) on $42.95, P(profit) 0.5943, adj growth 50.9 bp · C EV +13.71 (adj +6.27) on $32.61, P(profit) 0.4248, adj growth 54.4 bp · R EV +1.52 (adj +0.50) on $9.00, P(profit) 0.5589, adj growth 17.8 bp
equivalent contracts collapsed: KXNHLGAME-26OCT20CARVAN-VAN|yes == KXNHLGAME-26OCT20CARVAN-CAR|no

## TBL @ VGK  ·  10000 joint draws  ·  490 bet sides mapped, 11 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.502 / away 0.498

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_TBL_win | p_overtime | goals | shots VGK/TBL | VGK/TBL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.130 | 0.63 | 0.37 | 0.00 | 6.03 | 26.8/26.8 | 23.8/22.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.54 | 0.46 | 0.49 | 5.94 | 26.8/27.1 | 23.8/23.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.65 | 0.35 | 0.00 | 9.21 | 28.5/28.5 | 23.4/21.5 | even strength |
| TBL shot control · normal event (5-7) · decided (2+) | 0.072 | 0.58 | 0.42 | 0.00 | 5.95 | 21.4/31.7 | 28.4/17.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.067 | 0.70 | 0.30 | 0.00 | 5.99 | 31.4/21.2 | 18.5/26.7 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.061 | 0.54 | 0.46 | 0.53 | 2.82 | 25.4/25.4 | 23.9/23.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Brayden McNabb: 1+ goals YES | 4 | 0.080 | 0.069 | +0.037 | +0.026 | $4.74 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Brett Howden: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $5.10 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 72 | 0.767 | 0.754 | +0.033 | +0.020 | $16.79 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 65 | 0.696 | 0.682 | +0.030 | +0.016 | $10.01 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Brayden McNabb: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes; why: higher confidence-adjusted growth (34.44 vs 5.57 bp); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.011); failure: VGK offense suppressed (<= 2 goals)
- **Brett Howden: 1+ goals YES** — thesis: VGK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: higher confidence-adjusted growth (5.57 vs 5.30 bp); despite a smaller raw edge (+0.032 vs +0.063/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.016); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.02); failure: VGK offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT20TBVGK-4|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT20TBVGK-VGKTCONNELLY24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.89 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: VGK offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT20TBVGK-TB2|no; why: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over broad KXNHLSPREAD-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.78 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: MOSTLY_INDEPENDENT (phi 0.02); KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: TBL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.08.
- thesis VGK:OFFENSE_4PLUS (p 0.4283): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis VGK:WINS (p 0.5848): highest fidelity KXNHLSPREAD-26OCT20TBVGK-TB2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no (same contract)
- thesis TBL:SUPPRESSED (p 0.4793): highest fidelity KXNHLTEAMTOTAL-26OCT20TBVGK-TB4|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT20TBVGK-TB2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT20TBVGK-VGKBMCNABB3-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.131)
- KXNHLGOAL-26OCT20TBVGK-VGKBHOWDEN21-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:SUPPRESSED (p 0.3602, phi -0.236)
- KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.4283, phi -0.197)
- KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.3048, phi -0.253)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-VGKMMARNER93-1|no selected over player prop KXNHLAST-26OCT20TBVGK-VGKTCONNELLY24-1|no because adjusted EV is 0.1 pts higher while thesis capture is 0.89 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT20TBVGK-TBNKUCHEROV86-1|no selected over broad KXNHLSPREAD-26OCT20TBVGK-TB2|no because adjusted EV differs by only 0.6 pts while thesis capture is 0.78 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.99 (adj +0.87) on $37.50, P(profit) 0.7657, adj growth 7.8 bp · B EV +6.19 (adj +4.12) on $36.64, P(profit) 0.6546, adj growth 35.5 bp · C EV +3.22 (adj +1.55) on $41.70, P(profit) 0.657, adj growth 13.8 bp · R EV +0.22 (adj +0.13) on $5.00, P(profit) 0.7669, adj growth 4.7 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
