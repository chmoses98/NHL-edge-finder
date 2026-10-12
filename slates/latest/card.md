# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-12T15:40:29Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 145.24 | +21.79 | +6.10 | +24.23 | 0.693 | -38.03 | -49.11 | 51.05 |
| B thesis-diversified (joint) ← optimiser card | 115.11 | +14.28 | +8.73 | +5.88 | 0.612 | -43.08 | -55.39 | 76.45 |
| C best expression per thesis | 103.90 | +11.90 | +5.37 | +12.79 | 0.627 | -32.53 | -44.12 | 47.91 |
| R FUNDED research stakes | 19.00 | +1.40 | +0.77 | +1.68 | 0.719 | -6.34 | -11.81 | 0.00 |

## FLA @ BUF  ·  10000 joint draws  ·  434 bet sides mapped, 14 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BUF_win | p_FLA_win | p_overtime | goals | shots BUF/FLA | BUF/FLA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.122 | 0.62 | 0.38 | 0.00 | 5.98 | 27.1/26.7 | 23.7/23.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.44 | 5.91 | 27.3/27.2 | 24.0/24.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.089 | 0.68 | 0.32 | 0.00 | 5.99 | 32.2/21.4 | 18.7/27.7 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.61 | 0.39 | 0.00 | 9.22 | 28.8/28.6 | 23.2/22.3 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.56 | 0.44 | 0.50 | 5.9 | 32.4/21.6 | 18.5/29.1 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.058 | 0.59 | 0.41 | 0.00 | 3.41 | 26.3/25.9 | 24.2/24.2 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 68 | 0.751 | 0.732 | +0.056 | +0.037 | $20.00 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Sandis Vilmanis: 1+ goals YES | 10 | 0.138 | 0.126 | +0.032 | +0.020 | $5.44 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.22) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 71 | 0.784 | 0.744 | +0.059 | +0.020 | $17.25 | FUNDED_RESEARCH | $5 | BUF:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Josh Norris: 1+ goals YES | 19 | 0.229 | 0.218 | +0.028 | +0.017 | $4.40 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | BUF:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12FLABUF-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (14.25 vs 10.48 bp); despite a smaller raw edge (+0.056 vs +0.136/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: REINFORCING (phi 0.186); KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: MOSTLY_INDEPENDENT (phi 0.015); failure: FLA offense succeeds (4+ goals)
- **Sandis Vilmanis: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12FLABUF-FLACVERHAEGHE23-1|yes; why: higher confidence-adjusted growth (8.97 vs 0.26 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: INTENTIONAL_DIVERSIFIER (phi -0.134); KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: MOSTLY_INDEPENDENT (phi 0.006); failure: FLA offense suppressed (<= 2 goals)
- **Florida wins by over 1.5 goals NO** — thesis: BUF wins (incl. OT/SO); alternative: KXNHLPTS-26OCT12FLABUF-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (4.36 vs 2.15 bp); despite a smaller raw edge (+0.059 vs +0.129/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: REINFORCING (phi 0.186); KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.134); KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: MOSTLY_INDEPENDENT (phi 0.123); failure: FLA wins by 2+
- **Josh Norris: 1+ goals YES** — thesis: BUF offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT12FLABUF-FLA2|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT12FLABUF-FLA2|no has the higher standalone adjusted growth (4.36 vs 4.01 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.123); they share one thesis budget; relationships: KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.015); KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT12FLABUF-FLA2|no: MOSTLY_INDEPENDENT (phi 0.123); failure: BUF offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.4617): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis BUF:WINS (p 0.5811): highest fidelity KXNHLSPREAD-26OCT12FLABUF-FLA2|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no (same contract)
- thesis BUF:OFFENSE_4PLUS (p 0.4319): highest fidelity KXNHLTEAMTOTAL-26OCT12FLABUF-BUF3|yes [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT12FLABUF-FLA2|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT12FLABUF-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.3194, phi -0.254)
- KXNHLGOAL-26OCT12FLABUF-FLASVILMANIS95-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 78% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.4617, phi -0.162)
- KXNHLSPREAD-26OCT12FLABUF-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.2164, phi -1.0)
- KXNHLGOAL-26OCT12FLABUF-BUFJNORRIS9-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:SUPPRESSED (p 0.3527, phi -0.209)

portfolios: A EV +8.63 (adj +1.98) on $50.00, P(profit) 0.6796, adj growth 16.8 bp · B EV +5.28 (adj +2.94) on $47.09, P(profit) 0.6993, adj growth 26.0 bp · C EV +3.44 (adj +1.74) on $47.93, P(profit) 0.6218, adj growth 15.7 bp · R EV +0.81 (adj +0.40) on $10.00, P(profit) 0.6218, adj growth 14.4 bp

## OTT @ NJD  ·  10000 joint draws  ·  438 bet sides mapped, 15 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_OTT_win | p_overtime | goals | shots NJD/OTT | NJD/OTT starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.47 | 0.53 | 0.00 | 5.97 | 27.5/27.4 | 23.7/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.50 | 0.50 | 0.48 | 5.87 | 27.9/27.8 | 24.6/24.6 | even strength |
| NJD shot control · normal event (5-7) · decided (2+) | 0.080 | 0.53 | 0.47 | 0.00 | 5.95 | 32.5/21.9 | 18.6/28.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.074 | 0.49 | 0.51 | 0.00 | 9.16 | 29.0/29.0 | 22.9/23.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.53 | 0.47 | 0.49 | 5.85 | 33.2/22.1 | 19.0/29.9 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.067 | 0.48 | 0.52 | 0.48 | 2.77 | 26.1/26.0 | 24.5/24.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Warren Foegele: 1+ goals YES | 11 | 0.157 | 0.144 | +0.040 | +0.027 | $7.07 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 63 | 0.702 | 0.683 | +0.056 | +0.037 | $20.00 | FUNDED_RESEARCH | $5 | NJD:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Michael Amadio: 1+ goals YES | 13 | 0.177 | 0.163 | +0.039 | +0.025 | $6.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Amadeus Lombardi: 1+ goals YES | 9 | 0.124 | 0.115 | +0.029 | +0.019 | $4.79 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:WINS_BY_2PLUS | FRAGILE (0.24) | EVIDENCE_STRONGER | D |
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (15.43 vs 7.12 bp); despite a smaller raw edge (+0.040 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.014); failure: OTT offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT12OTTNJ-NJJHUGHES86-1|no; why: higher confidence-adjusted growth (12.88 vs 5.19 bp); despite a smaller raw edge (+0.056 vs +0.121/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense succeeds (4+ goals)
- **Michael Amadio: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12OTTNJ-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (11.01 vs 7.12 bp); despite a smaller raw edge (+0.039 vs +0.068/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.002); KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: OTT offense suppressed (<= 2 goals)
- **Amadeus Lombardi: 1+ goals YES** — thesis: NJD wins by 2+; alternative: KXNHLPTS-26OCT12OTTNJ-OTTTSTUTZLE18-1|no; why: higher confidence-adjusted growth (8.70 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.014); KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, NJD shot control · normal event (5-7) · decided (2+) 0.08.
- thesis NJD:SUPPRESSED (p 0.448): highest fidelity KXNHLSPREAD-26OCT12OTTNJ-NJ2|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NJD:WINS_BY_2PLUS (p 0.2602): highest fidelity KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes (same contract)
- thesis NJD:OFFENSE_4PLUS (p 0.3328): highest fidelity KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes (same contract)
- KXNHLGOAL-26OCT12OTTNJ-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4216, phi -0.188)
- KXNHLGOAL-26OCT12OTTNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3328, phi -0.245)
- KXNHLGOAL-26OCT12OTTNJ-OTTMAMADIO22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.4216, phi -0.214)
- KXNHLGOAL-26OCT12OTTNJ-NJALOMBARDI93-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 76% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.448, phi -0.193)

portfolios: A EV +10.65 (adj +2.65) on $50.00, P(profit) 0.616, adj growth 22.6 bp · B EV +7.42 (adj +4.88) on $38.33, P(profit) 0.3928, adj growth 42.5 bp · C EV +7.94 (adj +3.33) on $42.73, P(profit) 0.6494, adj growth 29.6 bp · R EV +0.43 (adj +0.28) on $5.00, P(profit) 0.7022, adj growth 10.3 bp

## VGK @ MIN  ·  10000 joint draws  ·  440 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_VGK_win | p_overtime | goals | shots MIN/VGK | MIN/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.55 | 0.45 | 0.00 | 6.02 | 28.5/28.7 | 25.3/24.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.114 | 0.51 | 0.49 | 0.47 | 5.92 | 28.7/28.8 | 25.5/25.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.57 | 0.43 | 0.00 | 9.19 | 30.0/30.1 | 24.4/23.6 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.079 | 0.50 | 0.50 | 0.00 | 6.02 | 22.5/33.5 | 29.9/19.2 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.072 | 0.47 | 0.53 | 0.45 | 5.89 | 23.1/34.0 | 30.7/19.9 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.060 | 0.54 | 0.46 | 0.00 | 3.48 | 27.4/27.4 | 25.4/25.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Michael McCarron: 1+ goals YES | 9 | 0.115 | 0.107 | +0.019 | +0.011 | $2.94 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.17) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 68 | 0.723 | 0.711 | +0.028 | +0.016 | $13.52 | FUNDED_RESEARCH | $4 | VGK:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Mitch Marner: 1+ goals NO | 72 | 0.759 | 0.748 | +0.025 | +0.014 | $13.23 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
- **Michael McCarron: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT12VGKMIN-MINJSPURGEON46-1|yes; why: higher confidence-adjusted growth (3.32 vs 0.01 bp); despite a smaller raw edge (+0.019 vs +0.041/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0009 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.029); failure: MIN offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (2.58 vs 2.19 bp); relationships: KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VGK offense succeeds (4+ goals)
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no has the higher standalone adjusted growth (2.58 vs 2.19 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.013); they share one thesis budget; relationships: KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: MOSTLY_INDEPENDENT (phi 0.029); KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.013); failure: VGK offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis VGK:SUPPRESSED (p 0.4241): highest fidelity KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis MIN:OFFENSE_4PLUS (p 0.3972): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT12VGKMIN-MINMMCCARRON47-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 83% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3814, phi -0.144)
- KXNHLGOAL-26OCT12VGKMIN-VGKJEICHEL9-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.228)
- KXNHLGOAL-26OCT12VGKMIN-VGKMMARNER93-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.3492, phi -0.213)

portfolios: A EV +2.52 (adj +1.47) on $45.24, P(profit) 0.5964, adj growth 11.6 bp · B EV +1.57 (adj +0.91) on $29.69, P(profit) 0.5964, adj growth 8.0 bp · C EV +0.53 (adj +0.30) on $13.24, P(profit) 0.723, adj growth 2.6 bp · R EV +0.16 (adj +0.09) on $4.00, P(profit) 0.723, adj growth 3.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
