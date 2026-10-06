# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-06T23:27:05Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.00 | +27.82 | +9.47 | +23.68 | 0.680 | -41.03 | -56.00 | 80.08 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +24.37 | +11.56 | +19.51 | 0.679 | -35.55 | -50.31 | 103.60 |
| C best expression per thesis | 149.99 | +17.91 | +8.58 | +13.51 | 0.652 | -32.33 | -45.12 | 76.91 |
| R FUNDED research stakes | 20.00 | +2.28 | +1.39 | +0.82 | 0.575 | -8.61 | -9.17 | 0.00 |

## NYI @ NYR  ·  10000 joint draws  ·  406 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.591 / away 0.409

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NYR_win | p_NYI_win | p_overtime | goals | shots NYR/NYI | NYR/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.125 | 0.66 | 0.34 | 0.00 | 5.97 | 26.6/27.0 | 24.3/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.54 | 0.46 | 0.47 | 5.87 | 26.9/27.2 | 24.0/23.6 | even strength |
| NYI shot control · normal event (5-7) · decided (2+) | 0.088 | 0.57 | 0.43 | 0.00 | 5.97 | 21.5/32.4 | 29.0/17.9 | even strength |
| NYI shot control · normal event (5-7) · tight (1-goal/OT) | 0.088 | 0.51 | 0.49 | 0.50 | 5.85 | 21.3/32.3 | 29.2/18.1 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.65 | 0.35 | 0.00 | 9.07 | 28.2/28.6 | 23.5/21.2 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.63 | 0.37 | 0.00 | 3.5 | 25.7/26.1 | 24.6/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 8 | 0.111 | 0.102 | +0.026 | +0.017 | $3.75 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Tye Kartye: 1+ goals YES | 12 | 0.154 | 0.144 | +0.027 | +0.017 | $3.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Vladislav Gavrikov: 1+ assists YES | 26 | 0.327 | 0.289 | +0.054 | +0.015 | $3.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_MIXED | D |
| Bo Horvat: 1+ goals NO | 70 | 0.738 | 0.728 | +0.024 | +0.013 | $10.54 | FUNDED_RESEARCH | $3 | NYI:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT06NYINYR-NYI3|yes; why: higher confidence-adjusted growth (7.94 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT06NYINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: NYI offense suppressed (<= 2 goals)
- **Tye Kartye: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes; why: higher confidence-adjusted growth (5.52 vs 2.51 bp); despite a smaller raw edge (+0.027 vs +0.054/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.014); failure: NYR offense suppressed (<= 2 goals)
- **Vladislav Gavrikov: 1+ assists YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06NYINYR-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (2.51 vs 0.45 bp); alternative not eligible: confidence-adjusted EV +0.0064 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLGOAL-26OCT06NYINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi 0.109); KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: MOSTLY_INDEPENDENT (phi -0.006); failure: NYR offense suppressed (<= 2 goals)
- **Bo Horvat: 1+ goals NO** — thesis: NYI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06NYINYR-NYIKPALMIERI21-1|no; why: higher confidence-adjusted growth (1.76 vs 0.25 bp); despite a smaller raw edge (+0.024 vs +0.075/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0046 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT06NYINYR-NYRTKARTYE24-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: NYI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, NYI shot control · normal event (5-7) · decided (2+) 0.09.
- thesis NYR:OFFENSE_4PLUS (p 0.4177): highest fidelity KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes (same contract)
- thesis NYI:SUPPRESSED (p 0.4901): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no (same contract)
- thesis NYR:SUPPRESSED (p 0.3608): highest fidelity KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06NYINYR-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT06NYINYR-NYIOPALAT81-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4901, phi -0.181)
- KXNHLGOAL-26OCT06NYINYR-NYRTKARTYE24-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3608, phi -0.183)
- KXNHLAST-26OCT06NYINYR-NYRVGAVRIKOV44-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.3608, phi -0.245)
- KXNHLGOAL-26OCT06NYINYR-NYIBHORVAT14-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:OFFENSE_4PLUS (p 0.2881, phi -0.241)

portfolios: A EV +5.68 (adj +2.68) on $37.50, P(profit) 0.4778, adj growth 20.9 bp · B EV +3.00 (adj +1.64) on $21.69, P(profit) 0.4185, adj growth 14.4 bp · C EV +1.60 (adj +0.61) on $24.64, P(profit) 0.656, adj growth 5.4 bp · R EV +0.10 (adj +0.05) on $3.00, P(profit) 0.7383, adj growth 1.9 bp

## STL @ CHI  ·  10000 joint draws  ·  394 bet sides mapped, 9 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.434 / away 0.566

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_STL_win | p_overtime | goals | shots CHI/STL | CHI/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.128 | 0.41 | 0.59 | 0.00 | 5.99 | 26.4/26.7 | 22.8/23.3 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.48 | 0.52 | 0.45 | 5.91 | 26.5/26.7 | 23.4/23.1 | even strength |
| STL shot control · normal event (5-7) · decided (2+) | 0.081 | 0.34 | 0.66 | 0.00 | 5.94 | 20.9/31.3 | 26.9/18.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.41 | 0.59 | 0.00 | 9.24 | 27.7/28.1 | 21.7/22.4 | even strength |
| STL shot control · normal event (5-7) · tight (1-goal/OT) | 0.076 | 0.45 | 0.55 | 0.47 | 5.89 | 21.3/31.8 | 28.5/18.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.059 | 0.42 | 0.58 | 0.00 | 3.45 | 25.0/25.2 | 23.1/23.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 11 | 0.169 | 0.153 | +0.052 | +0.036 | $7.66 | FUNDED_RESEARCH | $2 | CHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
| Patrick Kane: 1+ assists NO | 59 | 0.738 | 0.635 | +0.131 | +0.029 | $16.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Mason McTavish: 1+ assists NO | 70 | 0.786 | 0.738 | +0.072 | +0.023 | $16.90 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Philip Broberg: 1+ goals YES | 7 | 0.100 | 0.088 | +0.026 | +0.013 | $2.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | STL:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06STLCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (26.53 vs 0.22 bp); alternative not eligible: confidence-adjusted EV +0.0045 below the 0.010/contract floor; relationships: KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.006); failure: CHI offense suppressed (<= 2 goals)
- **Patrick Kane: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no; why: higher confidence-adjusted growth (7.46 vs 2.77 bp); relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.031); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi 0.019); failure: CHI offense succeeds (4+ goals)
- **Mason McTavish: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no; why: higher confidence-adjusted growth (5.93 vs 1.66 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: MOSTLY_INDEPENDENT (phi -0.024); failure: STL offense succeeds (4+ goals)
- **Philip Broberg: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLAST-26OCT06STLCHI-STLPBUCHNEVICH89-1|yes; why: higher confidence-adjusted growth (5.39 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0006 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: MOSTLY_INDEPENDENT (phi -0.024); failure: STL offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, STL shot control · normal event (5-7) · decided (2+) 0.08.
- thesis CHI:OFFENSE_4PLUS (p 0.3242): highest fidelity KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes (same contract)
- thesis CHI:SUPPRESSED (p 0.4578): highest fidelity KXNHLAST-26OCT06STLCHI-CHIBBYRAM24-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.3661): highest fidelity KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT06STLCHI-STLMMCTAVISH83-1|no (same contract)
- KXNHLGOAL-26OCT06STLCHI-CHIRGREENE20-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4578, phi -0.22)
- KXNHLAST-26OCT06STLCHI-CHIPKANE88-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.8 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3242, phi -0.242)
- KXNHLAST-26OCT06STLCHI-STLMMCTAVISH83-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.4172, phi -0.205)
- KXNHLGOAL-26OCT06STLCHI-STLPBROBERG6-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.3661, phi -0.113)

portfolios: A EV +7.70 (adj +3.31) on $37.50, P(profit) 0.561, adj growth 29.8 bp · B EV +9.64 (adj +4.16) on $44.03, P(profit) 0.6847, adj growth 36.9 bp · C EV +8.05 (adj +3.63) on $37.20, P(profit) 0.6468, adj growth 31.7 bp · R EV +0.89 (adj +0.61) on $2.00, P(profit) 0.1687, adj growth 21.4 bp

## VGK @ SEA  ·  10000 joint draws  ·  384 bet sides mapped, 15 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.397 / away 0.603

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SEA_win | p_VGK_win | p_overtime | goals | shots SEA/VGK | SEA/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.49 | 0.51 | 0.00 | 5.98 | 26.8/27.3 | 23.7/23.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.47 | 5.88 | 27.0/27.3 | 24.1/23.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.104 | 0.41 | 0.59 | 0.00 | 5.96 | 21.4/32.3 | 28.3/18.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.46 | 0.54 | 0.48 | 5.85 | 21.4/32.4 | 29.0/18.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.077 | 0.52 | 0.48 | 0.00 | 9.16 | 28.2/28.6 | 23.0/22.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.50 | 0.50 | 0.00 | 3.44 | 25.5/26.0 | 24.1/23.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Winterton: 1+ goals YES | 10 | 0.141 | 0.129 | +0.034 | +0.023 | $4.81 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.23) | EVIDENCE_STRONGER | D |
| Freddy Gaudreau: 1+ goals YES | 8 | 0.114 | 0.105 | +0.029 | +0.019 | $3.90 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SEA:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 70 | 0.760 | 0.744 | +0.045 | +0.029 | $17.61 | FUNDED_RESEARCH | $5 | VGK:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 74 | 0.819 | 0.777 | +0.065 | +0.024 | $16.49 | FUNDED_RESEARCH | $5 | SEA:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Ryan Winterton: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK3|no; why: higher confidence-adjusted growth (11.89 vs 6.54 bp); despite a smaller raw edge (+0.034 vs +0.065/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.095); failure: SEA offense suppressed (<= 2 goals)
- **Freddy Gaudreau: 1+ goals YES** — thesis: SEA offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes has the higher standalone adjusted growth (11.89 vs 10.32 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.084); failure: SEA offense suppressed (<= 2 goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06VGKSEA-VGKJEICHEL9-2|no; why: higher confidence-adjusted growth (9.07 vs 7.14 bp); despite a smaller raw edge (+0.045 vs +0.067/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.003); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.01); KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: MOSTLY_INDEPENDENT (phi 0.13); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLSPREAD-26OCT06VGKSEA-VGK2|no; why: higher confidence-adjusted growth (6.54 vs 6.10 bp); despite a smaller raw edge (+0.065 vs +0.072/contract); relationships: KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.095); KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: MOSTLY_INDEPENDENT (phi 0.084); KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.13); failure: VGK wins by 2+

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, VGK shot control · normal event (5-7) · decided (2+) 0.10.
- thesis SEA:OFFENSE_4PLUS (p 0.3591): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VGK:SUPPRESSED (p 0.402): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4912): highest fidelity KXNHLSPREAD-26OCT06VGKSEA-VGK2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT06VGKSEA-VGK2|no (same contract)
- KXNHLGOAL-26OCT06VGKSEA-SEARWINTERTON26-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 77% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.186)
- KXNHLGOAL-26OCT06VGKSEA-SEAFGAUDREAU89-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SEA:SUPPRESSED (p 0.4263, phi -0.17)
- KXNHLGOAL-26OCT06VGKSEA-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3788, phi -0.223)
- KXNHLSPREAD-26OCT06VGKSEA-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.2913, phi -0.734)

portfolios: A EV +4.86 (adj +1.35) on $37.50, P(profit) 0.6885, adj growth 11.3 bp · B EV +5.44 (adj +3.16) on $42.80, P(profit) 0.7126, adj growth 28.0 bp · C EV +4.42 (adj +2.43) on $42.01, P(profit) 0.6842, adj growth 21.5 bp · R EV +0.75 (adj +0.36) on $10.00, P(profit) 0.6437, adj growth 12.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT06VGKSEA-VGK|no == KXNHLGAME-26OCT06VGKSEA-SEA|yes

## FLA @ LAK  ·  10000 joint draws  ·  416 bet sides mapped, 21 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.487 / away 0.513

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_LAK_win | p_FLA_win | p_overtime | goals | shots LAK/FLA | LAK/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.63 | 0.37 | 0.00 | 5.95 | 27.0/26.9 | 23.9/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.117 | 0.53 | 0.47 | 0.46 | 5.91 | 27.1/27.0 | 23.8/23.8 | even strength |
| LAK shot control · normal event (5-7) · decided (2+) | 0.083 | 0.69 | 0.31 | 0.00 | 6.0 | 32.4/21.6 | 18.9/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.072 | 0.62 | 0.38 | 0.00 | 9.15 | 29.0/28.7 | 23.5/22.3 | even strength |
| LAK shot control · normal event (5-7) · tight (1-goal/OT) | 0.070 | 0.56 | 0.44 | 0.45 | 5.85 | 31.9/21.8 | 18.7/28.5 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.52 | 0.48 | 0.46 | 2.81 | 25.6/25.4 | 24.0/24.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 68 | 0.771 | 0.747 | +0.075 | +0.051 | $17.61 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Mats Zuccarello: 1+ assists NO | 64 | 0.789 | 0.685 | +0.133 | +0.029 | $17.61 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | LAK:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
| Alex Laferriere: 1+ goals YES | 23 | 0.275 | 0.262 | +0.032 | +0.020 | $6.26 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | LAK:OFFENSE_4PLUS | FRAGILE (0.40) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT06FLALA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (27.67 vs 8.50 bp); relationships: KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: MOSTLY_INDEPENDENT (phi -0.0); failure: FLA offense succeeds (4+ goals)
- **Mats Zuccarello: 1+ assists NO** — thesis: LAK offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT06FLALA-LAAPANARIN10-2|no; why: higher confidence-adjusted growth (8.41 vs 6.59 bp); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.011); KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.113); failure: LAK offense succeeds (4+ goals)
- **Alex Laferriere: 1+ goals YES** — thesis: LAK offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT06FLALA-FLA3|no; why: Player prop expression KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.40 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.0); KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: INTENTIONAL_DIVERSIFIER (phi -0.113); failure: LAK offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, LAK shot control · normal event (5-7) · decided (2+) 0.08.
- thesis FLA:SUPPRESSED (p 0.4918): highest fidelity KXNHLTEAMTOTAL-26OCT06FLALA-FLA4|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis LAK:OFFENSE_4PLUS (p 0.4049): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [DIRECT], best adjusted EV KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes — Player prop expression KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.40 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis LAK:WINS (p 0.5803): highest fidelity KXNHLSPREAD-26OCT06FLALA-FLA3|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT06FLALA-FLA4|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT06FLALA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.2891, phi -0.237)
- KXNHLAST-26OCT06FLALA-LAMZUCCARELLO36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.9 pts; fragile player expression; opposing: failure thesis LAK:OFFENSE_4PLUS (p 0.4049, phi -0.188)
- KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 60% of the draws where the thesis happens; fragile player expression; opposing: failure thesis LAK:SUPPRESSED (p 0.3764, phi -0.239)
- override: Player prop expression KXNHLGOAL-26OCT06FLALA-LAALAFERRIERE14-1|yes selected over player prop KXNHLAST-26OCT06FLALA-LAALAFERRIERE14-1|yes because adjusted EV differs by only 0.4 pts while thesis capture is 0.40 vs 0.54 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +9.58 (adj +2.13) on $37.50, P(profit) 0.7042, adj growth 18.1 bp · B EV +6.29 (adj +2.60) on $41.48, P(profit) 0.7135, adj growth 24.3 bp · C EV +3.84 (adj +1.91) on $46.14, P(profit) 0.6343, adj growth 18.3 bp · R EV +0.54 (adj +0.37) on $5.00, P(profit) 0.7706, adj growth 14.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
