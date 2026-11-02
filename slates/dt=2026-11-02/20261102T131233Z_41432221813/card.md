# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-11-02T13:12:33Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 55.04 | +7.96 | +3.37 | +8.60 | 0.506 | -35.70 | -35.70 | 25.86 |
| B thesis-diversified (joint) ← optimiser card | 42.57 | +5.80 | +3.15 | +4.16 | 0.637 | -22.18 | -24.04 | 28.00 |
| C best expression per thesis | 24.64 | +3.56 | +1.85 | +6.30 | 0.759 | -24.64 | -24.64 | 16.65 |
| R FUNDED research stakes | 8.00 | +1.19 | +0.64 | -0.26 | 0.311 | -8.00 | -8.00 | 0.00 |

## VGK @ BOS  ·  10000 joint draws  ·  424 bet sides mapped, 1 +EV candidates, 1 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_BOS_win | p_VGK_win | p_overtime | goals | shots BOS/VGK | BOS/VGK starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.53 | 0.47 | 0.00 | 6.02 | 27.3/27.5 | 24.2/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.47 | 6.02 | 27.3/27.8 | 24.5/23.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.095 | 0.49 | 0.51 | 0.00 | 9.36 | 28.9/29.2 | 23.0/22.7 | even strength |
| VGK shot control · normal event (5-7) · decided (2+) | 0.090 | 0.49 | 0.51 | 0.00 | 6.02 | 21.7/32.5 | 28.7/18.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.081 | 0.48 | 0.52 | 0.49 | 6.02 | 21.9/32.8 | 29.4/18.7 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.066 | 0.46 | 0.54 | 0.00 | 9.36 | 23.2/34.5 | 27.5/17.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| William Borgen: 1+ goals YES | 5 | 0.072 | 0.066 | +0.019 | +0.012 | $2.88 | FUNDED_RESEARCH | $1 | BOS:WINS_BY_2PLUS | FRAGILE (0.15) | EVIDENCE_STRONGER | D |
- **William Borgen: 1+ goals YES** — thesis: BOS wins by 2+; alternative: KXNHLPTS-26NOV02VGKBOS-VGKMMARNER93-1|no; why: higher confidence-adjusted growth (6.32 vs 0.00 bp); despite a smaller raw edge (+0.019 vs +0.069/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: only recommended bet in this game; failure: BOS offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis BOS:WINS_BY_2PLUS (p 0.2948): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26NOV02VGKBOS-BOSWBORGEN17-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 85% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BOS:SUPPRESSED (p 0.3597, phi -0.147)

portfolios: A EV +1.80 (adj +1.15) on $5.04, P(profit) 0.0724, adj growth 8.7 bp · B EV +1.03 (adj +0.66) on $2.88, P(profit) 0.0724, adj growth 5.7 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.36 (adj +0.23) on $1.00, P(profit) 0.0724, adj growth 7.4 bp

## DET @ FLA  ·  10000 joint draws  ·  408 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_DET_win | p_overtime | goals | shots FLA/DET | FLA/DET starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.58 | 0.42 | 0.00 | 6.0 | 27.0/26.8 | 23.8/23.1 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.53 | 0.47 | 0.48 | 5.95 | 27.1/27.0 | 23.7/23.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.60 | 0.40 | 0.00 | 9.24 | 28.6/28.5 | 23.1/22.0 | even strength |
| FLA shot control · normal event (5-7) · decided (2+) | 0.072 | 0.66 | 0.34 | 0.00 | 6.03 | 31.9/21.5 | 18.7/27.4 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.065 | 0.54 | 0.46 | 0.46 | 5.92 | 31.8/21.5 | 18.4/28.5 | even strength |
| DET shot control · normal event (5-7) · decided (2+) | 0.061 | 0.50 | 0.50 | 0.00 | 6.02 | 21.8/32.2 | 28.5/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 63 | 0.705 | 0.685 | +0.059 | +0.039 | $17.02 | FUNDED_RESEARCH | $5 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Cole Schwindt: 1+ goals YES | 9 | 0.128 | 0.112 | +0.032 | +0.016 | $4.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.676 | 0.660 | +0.040 | +0.023 | $12.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Detroit over 3.5 goals scored YES | 29 | 0.361 | 0.321 | +0.057 | +0.016 | $5.64 | FUNDED_RESEARCH | $2 | DET:OFFENSE_4PLUS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no; why: higher confidence-adjusted growth (14.63 vs 5.09 bp); relationships: KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: MOSTLY_INDEPENDENT (phi 0.014); failure: FLA offense succeeds (4+ goals)
- **Cole Schwindt: 1+ goals YES** — thesis: FLA offense succeeds (4+ goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASBENNETT9-1|yes; why: higher confidence-adjusted growth (6.53 vs 0.11 bp); alternative not eligible: confidence-adjusted EV +0.0032 below the 0.010/contract floor; relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: MOSTLY_INDEPENDENT (phi -0.038); failure: FLA offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no; why: Player prop expression KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26NOV02DETFLA-FLASREINHART13-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: MOSTLY_INDEPENDENT (phi 0.001); failure: FLA offense succeeds (4+ goals)
- **Detroit over 3.5 goals scored YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes; why: Broad expression KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.001); failure: DET offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · high event (8+) · decided (2+) 0.09.
- thesis FLA:SUPPRESSED (p 0.3439): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA2|no [DIRECT], best adjusted EV KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no — Player prop expression KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26NOV02DETFLA-FLASREINHART13-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis DET:OFFENSE_4PLUS (p 0.3511): highest fidelity KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes — Broad expression KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis DET:WINS (p 0.4426): highest fidelity KXNHLSPREAD-26NOV02DETFLA-FLA2|no [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26NOV02DETFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4327, phi -0.241)
- KXNHLGOAL-26NOV02DETFLA-FLACSCHWINDT79-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:SUPPRESSED (p 0.3439, phi -0.161)
- KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4327, phi -0.244)
- KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis DET:SUPPRESSED (p 0.4308, phi -0.654)
- override: Player prop expression KXNHLGOAL-26NOV02DETFLA-FLABTKACHUK8-1|no selected over player prop KXNHLAST-26NOV02DETFLA-FLASREINHART13-1|no because adjusted EV is 0.2 pts higher while thesis capture is 0.83 vs 0.83 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26NOV02DETFLA-DET4|yes selected over broad KXNHLTEAMTOTAL-26NOV02DETFLA-DET5|yes because adjusted EV differs by only 0.3 pts while thesis capture is 1.00 vs 0.54 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +6.16 (adj +2.22) on $50.00, P(profit) 0.4676, adj growth 17.2 bp · B EV +4.77 (adj +2.49) on $39.69, P(profit) 0.6194, adj growth 22.3 bp · C EV +3.56 (adj +1.85) on $24.64, P(profit) 0.7595, adj growth 16.6 bp · R EV +0.83 (adj +0.41) on $7.00, P(profit) 0.7054, adj growth 14.5 bp

## COL @ CHI  ·  10000 joint draws  ·  426 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_COL_win | p_overtime | goals | shots CHI/COL | CHI/COL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| COL shot control · normal event (5-7) · decided (2+) | 0.155 | 0.28 | 0.72 | 0.00 | 6.04 | 21.4/34.2 | 29.2/19.0 | even strength |
| COL shot control · high event (8+) · decided (2+) | 0.113 | 0.23 | 0.77 | 0.00 | 9.36 | 23.2/36.4 | 28.0/18.8 | even strength |
| COL shot control · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.43 | 0.57 | 0.48 | 5.98 | 21.9/34.8 | 31.4/18.7 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.100 | 0.33 | 0.67 | 0.00 | 6.06 | 27.6/28.7 | 24.1/24.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.085 | 0.48 | 0.52 | 0.46 | 5.91 | 27.6/28.6 | 25.1/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.33 | 0.67 | 0.00 | 9.37 | 29.2/30.2 | 23.3/24.0 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts COL shot control · normal event (5-7) · decided (2+) 0.15, COL shot control · high event (8+) · decided (2+) 0.11, COL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## CGY @ SJS  ·  10000 joint draws  ·  98 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_SJS_win | p_CGY_win | p_overtime | goals | shots SJS/CGY | SJS/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.60 | 0.40 | 0.00 | 6.06 | 28.8/28.7 | 25.5/24.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.53 | 0.47 | 0.47 | 5.92 | 28.8/28.8 | 25.5/25.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.099 | 0.57 | 0.43 | 0.00 | 9.32 | 29.9/29.8 | 24.3/23.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.074 | 0.66 | 0.34 | 0.00 | 6.02 | 33.7/22.7 | 20.0/29.1 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.064 | 0.52 | 0.48 | 0.46 | 5.98 | 33.9/23.0 | 19.8/30.6 | even strength |
| CGY shot control · normal event (5-7) · decided (2+) | 0.058 | 0.55 | 0.45 | 0.00 | 6.03 | 22.9/33.3 | 30.0/19.3 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
