# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T15:26:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 150.01 | +26.92 | +7.95 | +26.20 | 0.764 | -18.69 | -29.22 | 73.02 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +19.48 | +9.02 | +18.44 | 0.740 | -17.07 | -27.13 | 85.87 |
| C best expression per thesis | 150.01 | +22.64 | +9.67 | +20.72 | 0.721 | -23.91 | -36.40 | 89.66 |
| R FUNDED research stakes | 20.00 | +2.31 | +1.12 | +1.40 | 0.612 | -5.16 | -6.96 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  442 bet sides mapped, 0 +EV candidates, 0 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.55 | 0.45 | 0.00 | 6.07 | 27.8/28.4 | 24.9/24.0 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.110 | 0.47 | 0.53 | 0.00 | 6.01 | 22.2/34.1 | 30.2/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.103 | 0.54 | 0.46 | 0.46 | 6.0 | 28.1/28.8 | 25.4/24.7 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.102 | 0.49 | 0.51 | 0.45 | 5.94 | 22.3/34.4 | 30.9/19.0 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.093 | 0.51 | 0.49 | 0.00 | 9.26 | 29.5/30.3 | 24.4/23.4 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.083 | 0.45 | 0.55 | 0.00 | 9.31 | 23.7/36.2 | 29.0/18.4 | even strength |

_no bet on this game passes: +EV at the executable ask under both the model and the confidence-adjusted probability_

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.

portfolios: A EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · B EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · C EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## NYI @ OTT  ·  10000 joint draws  ·  444 bet sides mapped, 3 +EV candidates, 3 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.126 | 0.62 | 0.38 | 0.00 | 5.95 | 27.0/26.7 | 23.8/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.51 | 0.49 | 0.48 | 5.87 | 27.1/26.9 | 23.6/23.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.088 | 0.68 | 0.32 | 0.00 | 5.94 | 31.8/21.1 | 18.6/27.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.079 | 0.63 | 0.37 | 0.00 | 9.29 | 28.7/28.5 | 23.2/21.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.073 | 0.56 | 0.44 | 0.46 | 5.87 | 31.9/21.1 | 18.0/28.4 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.057 | 0.60 | 0.40 | 0.00 | 3.46 | 25.4/25.3 | 23.7/23.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ondrej Palat: 1+ goals YES | 9 | 0.126 | 0.115 | +0.030 | +0.020 | $1.97 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | NYI:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Carter Yakemchuk: 1+ assists NO | 68 | 0.754 | 0.712 | +0.059 | +0.017 | $6.06 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.87) | EVIDENCE_MIXED | D |
| Ridly Greig: 1+ goals YES | 15 | 0.179 | 0.169 | +0.020 | +0.010 | $1.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Ondrej Palat: 1+ goals YES** — thesis: NYI offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15NYIOTT-NYI3|yes; why: higher confidence-adjusted growth (9.62 vs 0.40 bp); despite a smaller raw edge (+0.030 vs +0.036/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0068 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.002); failure: NYI offense suppressed (<= 2 goals)
- **Carter Yakemchuk: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15NYIOTT-OTTDBATHERSON19-1|no; why: higher confidence-adjusted growth (2.86 vs 0.17 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0041 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi -0.047); failure: OTT offense succeeds (4+ goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYIOTT-OTTJSPENCE10-1|yes; why: higher confidence-adjusted growth (1.66 vs 0.97 bp); despite a smaller raw edge (+0.020 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0095 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: MOSTLY_INDEPENDENT (phi 0.002); KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: MOSTLY_INDEPENDENT (phi -0.047); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:SUPPRESSED (p 0.3641): highest fidelity KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no (same contract)
- thesis OTT:OFFENSE_4PLUS (p 0.4227): highest fidelity KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes (same contract)
- thesis NYI:OFFENSE_4PLUS (p 0.3057): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15NYIOTT-NYIOPALAT81-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYI:SUPPRESSED (p 0.4764, phi -0.18)
- KXNHLAST-26OCT15NYIOTT-OTTCYAKEMCHUK26-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.4227, phi -0.214)
- KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3641, phi -0.194)

portfolios: A EV +1.56 (adj +0.80) on $10.70, P(profit) 0.2816, adj growth 7.4 bp · B EV +1.28 (adj +0.63) on $9.24, P(profit) 0.2378, adj growth 5.9 bp · C EV +1.02 (adj +0.34) on $11.19, P(profit) 0.8055, adj growth 3.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 23 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TBL_win | p_SEA_win | p_overtime | goals | shots TBL/SEA | TBL/SEA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| TBL shot control · normal event (5-7) · decided (2+) | 0.136 | 0.68 | 0.32 | 0.00 | 6.0 | 32.8/21.2 | 18.5/28.2 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.59 | 0.41 | 0.00 | 5.98 | 27.3/26.6 | 23.4/23.3 | even strength |
| TBL shot control · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.55 | 0.45 | 0.45 | 5.82 | 33.0/21.5 | 18.4/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.51 | 0.49 | 0.47 | 5.95 | 27.4/26.8 | 23.5/24.2 | even strength |
| TBL shot control · high event (8+) · decided (2+) | 0.081 | 0.71 | 0.29 | 0.00 | 9.18 | 34.4/22.6 | 18.1/26.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.069 | 0.60 | 0.40 | 0.00 | 9.15 | 28.6/28.0 | 22.5/22.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Nikita Kucherov: 1+ assists NO | 35 | 0.487 | 0.395 | +0.122 | +0.029 | $3.39 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.71) | EVIDENCE_MIXED | D |
| Tampa Bay over 5.5 goals scored NO | 83 | 0.889 | 0.857 | +0.049 | +0.017 | $7.51 | FUNDED_RESEARCH | $2 | SEA:WINS | DIRECT (0.99) | EVIDENCE_MIXED | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.640 | 0.626 | +0.034 | +0.020 | $4.18 | FUNDED_RESEARCH | $2 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| Jake Guentzel: 1+ goals NO | 62 | 0.671 | 0.656 | +0.035 | +0.019 | $3.73 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
- **Nikita Kucherov: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLTEAMTOTAL-26OCT15SEATB-TB3|no; why: higher confidence-adjusted growth (7.87 vs 7.35 bp); wins across more scripts (relative breadth 1.0 vs 0.795); relationships: KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no: REINFORCING (phi 0.2); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: REINFORCING (phi 0.163); failure: TBL offense succeeds (4+ goals)
- **Tampa Bay over 5.5 goals scored NO** — thesis: SEA wins (incl. OT/SO); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: Broad expression KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.2); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.195); KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: REINFORCING (phi 0.166); failure: high-event game (8+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no: REINFORCING (phi 0.195); KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no: REINFORCING (phi 0.163); KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no: REINFORCING (phi 0.166); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3553): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SEA:WINS_BY_2PLUS (p 0.2152): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4164): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 29% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 14.3 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.319)
- KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no: FUNDED_RESEARCH; family MIXED; loses 1% of the draws where the thesis happens; opposing: failure thesis GAME:HIGH_EVENT (p 0.2383, phi -0.515)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.26)
- KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.238)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.83 vs 1.00 (DIRECT vs STRUCTURAL; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Broad expression KXNHLTEAMTOTAL-26OCT15SEATB-TB6|no selected over player prop KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no because adjusted EV differs by only 0.8 pts while thesis capture is 1.00 vs 0.83 (STRUCTURAL vs DIRECT; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +4.35 (adj +0.81) on $15.67, P(profit) 0.5933, adj growth 7.3 bp · B EV +2.00 (adj +0.67) on $18.82, P(profit) 0.6121, adj growth 6.4 bp · C EV +3.22 (adj +0.99) on $15.81, P(profit) 0.4934, adj growth 9.1 bp · R EV +0.23 (adj +0.11) on $4.00, P(profit) 0.5987, adj growth 3.9 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15SEATB-TB|no == KXNHLGAME-26OCT15SEATB-SEA|yes

## VAN @ FLA  ·  10000 joint draws  ·  394 bet sides mapped, 31 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.125 | 0.65 | 0.35 | 0.00 | 6.02 | 32.6/21.1 | 18.3/28.0 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.115 | 0.59 | 0.41 | 0.00 | 5.99 | 27.5/26.9 | 23.5/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.099 | 0.52 | 0.48 | 0.47 | 5.89 | 27.4/26.9 | 23.6/24.0 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.097 | 0.54 | 0.46 | 0.47 | 5.95 | 32.5/21.3 | 18.1/29.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.090 | 0.57 | 0.43 | 0.00 | 9.39 | 28.7/28.3 | 22.4/22.1 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.083 | 0.68 | 0.32 | 0.00 | 9.29 | 34.4/22.3 | 17.7/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sam Reinhart: 1+ goals NO | 61 | 0.700 | 0.676 | +0.073 | +0.050 | $5.98 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.696 | 0.674 | +0.059 | +0.038 | $5.98 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | FLA:SUPPRESSED | DIRECT (0.85) | EVIDENCE_STRONGER | D |
| Florida wins by over 1.5 goals NO | 50 | 0.647 | 0.548 | +0.130 | +0.031 | $2.07 | FUNDED_RESEARCH | $1 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Florida wins by over 2.5 goals NO | 63 | 0.769 | 0.675 | +0.123 | +0.029 | $4.29 | FUNDED_RESEARCH | $2 | VAN:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Sam Reinhart: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: higher confidence-adjusted growth (23.29 vs 23.23 bp); despite a smaller raw edge (+0.073 vs +0.085/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 1.019 vs 0.53); relationships: KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT15VANFLA-FLA2|no: REINFORCING (phi 0.207); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.179); failure: FLA offense succeeds (4+ goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no; why: second expression of the same thesis: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no has the higher standalone adjusted growth (23.29 vs 13.68 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.003); they share one thesis budget; relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: MOSTLY_INDEPENDENT (phi 0.003); KXNHLSPREAD-26OCT15VANFLA-FLA2|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: REINFORCING (phi 0.157); failure: FLA offense succeeds (4+ goals)
- **Florida wins by over 1.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (29.07 vs 8.32 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.313); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: REINFORCING (phi 0.207); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.169); KXNHLSPREAD-26OCT15VANFLA-FLA3|no: DUPLICATIVE (phi 0.742); failure: FLA wins by 2+
- **Florida wins by over 2.5 goals NO** — thesis: VAN wins (incl. OT/SO); alternative: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes; why: KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes has the higher standalone adjusted growth (29.07 vs 8.19 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.248); relationships: KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: REINFORCING (phi 0.179); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: REINFORCING (phi 0.157); KXNHLSPREAD-26OCT15VANFLA-FLA2|no: DUPLICATIVE (phi 0.742); failure: FLA wins by 2+

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3497): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN4|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2228): highest fidelity KXNHLSPREAD-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2854): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-FLASREINHART13-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4534, phi -0.249)
- KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 15% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4534, phi -0.243)
- KXNHLSPREAD-26OCT15VANFLA-FLA2|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 15.2 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3527, phi -1.0)
- KXNHLSPREAD-26OCT15VANFLA-FLA3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); LARGE MARKET DISAGREEMENT 14.4 pts; opposing: failure thesis FLA:WINS_BY_2PLUS (p 0.3527, phi -0.742)

portfolios: A EV +5.17 (adj +1.02) on $15.67, P(profit) 0.4903, adj growth 8.8 bp · B EV +2.60 (adj +1.15) on $18.32, P(profit) 0.7272, adj growth 11.1 bp · C EV +4.92 (adj +2.48) on $16.56, P(profit) 0.756, adj growth 23.0 bp · R EV +0.87 (adj +0.31) on $5.00, P(profit) 0.722, adj growth 11.7 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  424 bet sides mapped, 10 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.131 | 0.55 | 0.45 | 0.00 | 5.99 | 33.0/21.1 | 17.9/29.0 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.53 | 0.47 | 0.48 | 5.91 | 33.2/21.2 | 18.0/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.108 | 0.49 | 0.51 | 0.00 | 5.99 | 27.2/26.4 | 22.9/23.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.093 | 0.48 | 0.52 | 0.46 | 5.83 | 27.4/27.0 | 23.7/24.2 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.077 | 0.56 | 0.44 | 0.00 | 9.21 | 34.6/22.5 | 17.3/27.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 9.22 | 28.9/28.2 | 22.1/23.1 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Matt Rempe: 1+ goals YES | 6 | 0.087 | 0.078 | +0.023 | +0.014 | $1.35 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.674 | 0.659 | +0.038 | +0.023 | $6.39 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Pavel Dorofeyev: 1+ assists NO | 72 | 0.793 | 0.752 | +0.059 | +0.018 | $7.76 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | NYR:SUPPRESSED | DIRECT (0.90) | EVIDENCE_MIXED | D |
| Cody Glass: 1+ goals YES | 13 | 0.162 | 0.151 | +0.024 | +0.013 | $1.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (7.02 vs 2.40 bp); despite a smaller raw edge (+0.023 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi 0.005); failure: NYR offense suppressed (<= 2 goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no has the higher standalone adjusted growth (5.81 vs 4.95 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.012); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.013); failure: NJD offense succeeds (4+ goals)
- **Pavel Dorofeyev: 1+ assists NO** — thesis: NYR offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15NYRNJ-NYRPDOROFEYEV16-2|no; why: higher confidence-adjusted growth (3.50 vs 0.00 bp); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.042); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: MOSTLY_INDEPENDENT (phi -0.008); failure: NYR offense succeeds (4+ goals)
- **Cody Glass: 1+ goals YES** — thesis: NJD offense succeeds (4+ goals); alternative: KXNHLPTS-26OCT15NYRNJ-NJDMERCER91-1|yes; why: higher confidence-adjusted growth (3.18 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.013); KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: MOSTLY_INDEPENDENT (phi -0.008); failure: NJD offense suppressed (<= 2 goals)

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4084): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS (p 0.4897): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:SUPPRESSED (p 0.4273): highest fidelity KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no (same contract)
- KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4273, phi -0.148)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3698, phi -0.26)
- KXNHLAST-26OCT15NYRNJ-NYRPDOROFEYEV16-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 10% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:OFFENSE_4PLUS (p 0.3642, phi -0.219)
- KXNHLGOAL-26OCT15NYRNJ-NJCGLASS12-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:SUPPRESSED (p 0.4084, phi -0.178)

portfolios: A EV +1.55 (adj +0.45) on $15.67, P(profit) 0.325, adj growth 4.2 bp · B EV +1.75 (adj +0.85) on $16.96, P(profit) 0.6389, adj growth 8.1 bp · C EV +2.36 (adj +0.85) on $30.08, P(profit) 0.6246, adj growth 8.1 bp · R EV +0.12 (adj +0.07) on $2.00, P(profit) 0.6741, adj growth 2.7 bp

## PHI @ DET  ·  10000 joint draws  ·  406 bet sides mapped, 6 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_DET_win | p_PHI_win | p_overtime | goals | shots DET/PHI | DET/PHI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| DET shot control · normal event (5-7) · decided (2+) | 0.112 | 0.54 | 0.46 | 0.00 | 5.93 | 32.3/21.1 | 18.0/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.111 | 0.50 | 0.50 | 0.00 | 5.96 | 27.2/26.8 | 23.3/23.7 | even strength |
| DET shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.55 | 0.45 | 0.47 | 5.84 | 32.9/21.3 | 18.2/29.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.105 | 0.50 | 0.50 | 0.49 | 5.89 | 27.3/26.8 | 23.5/24.0 | even strength |
| balanced shots · low event (<=4) · decided (2+) | 0.067 | 0.49 | 0.51 | 0.00 | 3.44 | 26.3/25.6 | 23.8/24.5 | even strength |
| DET shot control · low event (<=4) · tight (1-goal/OT) | 0.066 | 0.49 | 0.51 | 0.49 | 2.77 | 31.2/20.3 | 18.8/29.7 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Sheldon Dries: 1+ goals YES | 9 | 0.121 | 0.113 | +0.025 | +0.017 | $1.80 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $2.39 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Viktor Arvidsson: 1+ assists NO | 66 | 0.734 | 0.694 | +0.058 | +0.019 | $6.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DET:SUPPRESSED | DIRECT (0.86) | EVIDENCE_MIXED | D |
| Denver Barkey: 1+ goals YES | 14 | 0.173 | 0.163 | +0.025 | +0.014 | $1.56 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.29) | EVIDENCE_STRONGER | D |
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15PHIDET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (7.35 vs 0.00 bp); despite a smaller raw edge (+0.025 vs +0.034/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: DET offense suppressed (<= 2 goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes; why: higher confidence-adjusted growth (5.49 vs 3.42 bp); relationships: KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.001); failure: PHI offense suppressed (<= 2 goals)
- **Viktor Arvidsson: 1+ assists NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (3.46 vs 0.78 bp); wins across more scripts (relative breadth 0.992 vs 0.35); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: MOSTLY_INDEPENDENT (phi -0.002); failure: DET offense succeeds (4+ goals)
- **Denver Barkey: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes has the higher standalone adjusted growth (5.49 vs 3.42 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: MOSTLY_INDEPENDENT (phi -0.002); failure: PHI offense suppressed (<= 2 goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes (same contract)
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no (same contract)
- thesis DET:OFFENSE_4PLUS (p 0.3447): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4363, phi -0.176)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)
- KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.244)
- KXNHLGOAL-26OCT15PHIDET-PHIDBARKEY86-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 71% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.216)

portfolios: A EV +1.42 (adj +0.71) on $15.67, P(profit) 0.3525, adj growth 6.7 bp · B EV +1.67 (adj +0.89) on $12.22, P(profit) 0.3685, adj growth 8.4 bp · C EV +1.39 (adj +0.63) on $13.08, P(profit) 0.7972, adj growth 5.8 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## WPG @ CHI  ·  10000 joint draws  ·  416 bet sides mapped, 7 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.121 | 0.50 | 0.50 | 0.00 | 6.0 | 26.6/27.0 | 23.5/22.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.109 | 0.50 | 0.50 | 0.47 | 5.87 | 26.3/26.6 | 23.4/23.0 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.096 | 0.44 | 0.56 | 0.00 | 6.01 | 21.0/31.9 | 27.8/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.086 | 0.48 | 0.52 | 0.46 | 5.91 | 21.3/32.0 | 28.5/18.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.080 | 0.48 | 0.52 | 0.00 | 9.36 | 27.8/28.2 | 21.8/21.8 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.060 | 0.38 | 0.62 | 0.00 | 9.23 | 22.3/33.4 | 25.9/17.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ryan Greene: 1+ goals YES | 12 | 0.176 | 0.159 | +0.049 | +0.031 | $2.97 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.28) | EVIDENCE_STRONGER | D |
| Neal Pionk: 1+ goals NO | 89 | 0.927 | 0.914 | +0.030 | +0.017 | $7.64 | FUNDED_RESEARCH | $2 | WPG:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Roman Kantserov: 1+ goals NO | 74 | 0.789 | 0.776 | +0.036 | +0.022 | $7.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Tyler Bertuzzi: 1+ goals YES | 28 | 0.321 | 0.308 | +0.026 | +0.014 | $1.70 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CHI:OFFENSE_4PLUS | FRAGILE (0.48) | EVIDENCE_STRONGER | D |
- **Ryan Greene: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes; why: higher confidence-adjusted growth (18.65 vs 1.99 bp); relationships: KXNHLGOAL-26OCT15WPGCHI-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.007); failure: CHI offense suppressed (<= 2 goals)
- **Neal Pionk: 1+ goals NO** — thesis: WPG offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15WPGCHI-WPG3|no; why: higher confidence-adjusted growth (7.14 vs 0.00 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; alternative not eligible: confidence-adjusted EV +0.0002 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi -0.006); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.004); failure: WPG offense succeeds (4+ goals)
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15WPGCHI-CHIPKANE88-1|no; why: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT15WPGCHI-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: MOSTLY_INDEPENDENT (phi 0.016); failure: CHI offense succeeds (4+ goals)
- **Tyler Bertuzzi: 1+ goals YES** — thesis: CHI offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes has the higher standalone adjusted growth (18.65 vs 1.99 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.007); they share one thesis budget; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15WPGCHI-WPGNPIONK4-1|no: MOSTLY_INDEPENDENT (phi 0.004); KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: MOSTLY_INDEPENDENT (phi 0.016); failure: CHI offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, WPG shot control · normal event (5-7) · decided (2+) 0.10.
- thesis CHI:OFFENSE_4PLUS (p 0.3693): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CHI:SUPPRESSED (p 0.4146): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no (same contract)
- thesis WPG:SUPPRESSED (p 0.4): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15WPGCHI-CHIRGREENE20-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 72% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.203)
- KXNHLGOAL-26OCT15WPGCHI-WPGNPIONK4-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis WPG:OFFENSE_4PLUS (p 0.3851, phi -0.122)
- KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3693, phi -0.203)
- KXNHLGOAL-26OCT15WPGCHI-CHITBERTUZZI59-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 52% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:SUPPRESSED (p 0.4146, phi -0.264)
- override: Player prop expression KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no selected over player prop KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-2|no because adjusted EV differs by only 0.3 pts while thesis capture is 0.89 vs 0.99 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.80 (adj +1.12) on $15.67, P(profit) 0.5824, adj growth 10.7 bp · B EV +1.91 (adj +1.18) on $19.94, P(profit) 0.3714, adj growth 11.2 bp · C EV +2.42 (adj +1.53) on $16.90, P(profit) 0.1764, adj growth 14.0 bp · R EV +0.07 (adj +0.04) on $2.00, P(profit) 0.9271, adj growth 1.5 bp

## SJS @ NSH  ·  10000 joint draws  ·  456 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.55 | 0.45 | 0.00 | 6.05 | 27.6/27.8 | 24.4/23.6 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.112 | 0.48 | 0.52 | 0.45 | 5.99 | 27.9/27.9 | 24.4/24.5 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.105 | 0.57 | 0.43 | 0.00 | 9.29 | 28.9/28.8 | 23.1/22.2 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.068 | 0.48 | 0.52 | 0.00 | 6.0 | 22.1/32.7 | 28.7/18.9 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.067 | 0.60 | 0.40 | 0.00 | 6.02 | 32.7/22.1 | 19.1/28.3 | even strength |
| NSH shot control · normal event (5-7) · tight (1-goal/OT) | 0.061 | 0.53 | 0.47 | 0.47 | 5.87 | 32.5/22.1 | 18.9/29.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ivar Stenberg: 2+ assists NO | 93 | 0.980 | 0.952 | +0.045 | +0.018 | $7.98 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | DIFFUSE | NONE | EVIDENCE_MIXED | D |
| Collin Graf: 1+ goals YES | 13 | 0.173 | 0.160 | +0.035 | +0.022 | $2.36 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
| Mason Marchment: 1+ goals YES | 20 | 0.242 | 0.227 | +0.031 | +0.015 | $1.88 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ goals NO | 80 | 0.834 | 0.824 | +0.022 | +0.013 | $7.12 | FUNDED_RESEARCH | $2 | SJS:SUPPRESSED | DIRECT (0.92) | EVIDENCE_STRONGER | D |
- **Ivar Stenberg: 2+ assists NO** — thesis: no single thesis (diffuse dependence on the game script); alternative: diffuse bet (no thesis event with phi >= 0.10): there is no thesis to compare expressions of; why: diffuse script dependence; chosen on its own confidence-adjusted growth; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.004); failure: SJS offense succeeds (4+ goals)
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (8.58 vs 3.06 bp); relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: MOSTLY_INDEPENDENT (phi -0.027); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: SJS offense suppressed (<= 2 goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes has the higher standalone adjusted growth (8.58 vs 3.06 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.010); they share one thesis budget; relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.005); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ goals NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (2.34 vs 0.16 bp); despite a smaller raw edge (+0.022 vs +0.114/contract); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV +0.0042 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.005); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:OFFENSE_4PLUS (p 0.3914): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SJS:SUPPRESSED (p 0.3847): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-2|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; no single thesis (diffuse); fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.121)
- KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3847, phi -0.192)
- KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3847, phi -0.226)
- KXNHLGOAL-26OCT15SJNSH-SJISTENBERG41-1|no: FUNDED_RESEARCH; family TRUSTED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3914, phi -0.198)

portfolios: A EV +1.99 (adj +0.80) on $15.67, P(profit) 0.3701, adj growth 7.6 bp · B EV +1.45 (adj +0.77) on $19.34, P(profit) 0.3345, adj growth 7.4 bp · C EV +1.49 (adj +0.79) on $15.67, P(profit) 0.1729, adj growth 7.4 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.8336, adj growth 1.2 bp

## STL @ MIN  ·  10000 joint draws  ·  430 bet sides mapped, 5 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.129 | 0.58 | 0.42 | 0.00 | 6.02 | 27.7/27.4 | 24.2/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.51 | 0.49 | 0.47 | 5.96 | 27.9/27.5 | 24.2/24.6 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.096 | 0.57 | 0.43 | 0.00 | 9.35 | 29.4/29.3 | 23.5/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.086 | 0.65 | 0.35 | 0.00 | 6.0 | 32.7/21.9 | 19.1/28.0 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.074 | 0.58 | 0.42 | 0.45 | 5.96 | 33.3/22.4 | 19.2/29.7 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.61 | 0.39 | 0.00 | 9.35 | 34.5/23.4 | 18.3/27.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ross Johnston: 1+ goals YES | 5 | 0.078 | 0.070 | +0.024 | +0.016 | $1.49 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | FRAGILE (0.13) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 19 | 0.230 | 0.217 | +0.029 | +0.017 | $2.04 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.135 | 0.119 | +0.029 | +0.013 | $1.05 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ assists YES | 24 | 0.309 | 0.269 | +0.056 | +0.017 | $1.81 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.44) | EVIDENCE_MIXED | D |
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (11.00 vs 2.01 bp); despite a smaller raw edge (+0.024 vs +0.026/contract); relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.004); failure: STL offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (3.69 vs 3.15 bp); despite a smaller raw edge (+0.029 vs +0.056/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.018); failure: MIN offense suppressed (<= 2 goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (3.69 vs 3.57 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.002); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.141); failure: MIN offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ assists YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (3.69 vs 3.15 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.018); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.018); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi 0.141); failure: MIN offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4373): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3598): highest fidelity KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 87% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4272, phi -0.132)
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.199)
- KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.163)
- KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 56% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3471, phi -0.261)

portfolios: A EV +2.69 (adj +1.06) on $13.95, P(profit) 0.5251, adj growth 9.3 bp · B EV +1.66 (adj +0.86) on $6.39, P(profit) 0.5627, adj growth 8.1 bp · C EV +0.70 (adj +0.38) on $5.42, P(profit) 0.4344, adj growth 3.5 bp · R EV +0.46 (adj +0.30) on $1.00, P(profit) 0.0777, adj growth 10.2 bp

## UTA @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 11 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_EDM_win | p_UTA_win | p_overtime | goals | shots EDM/UTA | EDM/UTA starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.63 | 0.37 | 0.00 | 6.07 | 27.5/27.5 | 24.5/23.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.111 | 0.60 | 0.40 | 0.00 | 9.46 | 29.4/29.3 | 23.8/22.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.108 | 0.51 | 0.49 | 0.45 | 6.07 | 28.1/28.0 | 24.7/24.7 | even strength |
| EDM shot control · normal event (5-7) · decided (2+) | 0.077 | 0.67 | 0.33 | 0.00 | 6.07 | 32.8/22.1 | 19.4/28.1 | even strength |
| EDM shot control · high event (8+) · decided (2+) | 0.071 | 0.69 | 0.31 | 0.00 | 9.48 | 34.3/23.4 | 18.9/26.2 | even strength |
| EDM shot control · normal event (5-7) · tight (1-goal/OT) | 0.063 | 0.56 | 0.44 | 0.45 | 5.94 | 32.9/22.3 | 19.2/29.5 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Alex Formenton: 1+ goals YES | 16 | 0.217 | 0.195 | +0.047 | +0.026 | $2.85 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.452 | 0.363 | +0.117 | +0.028 | $4.65 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.129 | 0.113 | +0.033 | +0.017 | $1.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Mattias Ekholm: 1+ assists YES | 29 | 0.394 | 0.320 | +0.089 | +0.015 | $2.11 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:OFFENSE_4PLUS | DIRECT (0.51) | EVIDENCE_MIXED | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes; why: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes has the higher standalone adjusted growth (10.34 vs 10.12 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.000); relationships: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.072); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.49 vs 4.65 bp); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.09); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes; why: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes has the higher standalone adjusted growth (10.34 vs 7.46 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.073); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense suppressed (<= 2 goals)
- **Mattias Ekholm: 1+ assists YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes; why: Player prop expression KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.072); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.09); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.003); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:OFFENSE_4PLUS (p 0.4964): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMKKAPANEN42-1|yes — Player prop expression KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- thesis EDM:SUPPRESSED (p 0.2932): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis UTA:SUPPRESSED (p 0.3988): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.19)
- KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4964, phi -0.318)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.154)
- KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 49% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 11.4 pts; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.24)
- override: Player prop expression KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMVPODKOLZIN92-2|yes because adjusted EV differs by only 0.3 pts while thesis capture is 0.51 vs 0.21 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +3.56 (adj +0.71) on $15.67, P(profit) 0.6694, adj growth 6.7 bp · B EV +3.69 (adj +1.26) on $11.48, P(profit) 0.6516, adj growth 11.9 bp · C EV +3.80 (adj +1.09) on $8.65, P(profit) 0.5365, adj growth 10.1 bp · R EV +0.28 (adj +0.15) on $1.00, P(profit) 0.2168, adj growth 5.6 bp

## CGY @ VGK  ·  10000 joint draws  ·  412 bet sides mapped, 9 +EV candidates, 4 on card


**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_VGK_win | p_CGY_win | p_overtime | goals | shots VGK/CGY | VGK/CGY starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| VGK shot control · normal event (5-7) · decided (2+) | 0.127 | 0.79 | 0.21 | 0.00 | 5.97 | 33.9/22.1 | 19.9/28.5 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.73 | 0.27 | 0.00 | 6.01 | 28.3/27.8 | 25.3/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.092 | 0.56 | 0.44 | 0.47 | 5.92 | 28.5/28.3 | 24.9/25.3 | even strength |
| VGK shot control · normal event (5-7) · tight (1-goal/OT) | 0.091 | 0.58 | 0.42 | 0.46 | 5.83 | 33.7/22.2 | 18.9/30.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.083 | 0.75 | 0.25 | 0.00 | 9.18 | 29.7/29.2 | 24.6/21.8 | even strength |
| VGK shot control · high event (8+) · decided (2+) | 0.078 | 0.78 | 0.22 | 0.00 | 9.16 | 35.4/23.4 | 19.3/26.6 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Mitch Marner: 1+ goals NO | 68 | 0.742 | 0.721 | +0.046 | +0.026 | $6.80 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 62 | 0.675 | 0.660 | +0.039 | +0.024 | $5.16 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
| Aydar Suniev: 1+ goals YES | 15 | 0.190 | 0.176 | +0.031 | +0.017 | $1.77 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $3.54 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no; why: higher confidence-adjusted growth (7.00 vs 5.41 bp); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.146); failure: VGK offense succeeds (4+ goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (5.41 vs 4.11 bp); despite a smaller raw edge (+0.039 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.142); failure: VGK offense succeeds (4+ goals)
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (4.78 vs 4.11 bp); despite a smaller raw edge (+0.031 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.012); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.133); failure: CGY offense suppressed (<= 2 goals)
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: higher confidence-adjusted growth (4.11 vs 3.27 bp); wins across more scripts (relative breadth 1.025 vs 0.85); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.133); failure: VGK wins by 2+

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis CGY:OFFENSE_4PLUS (p 0.2574): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.194)
- KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.235)
- KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5368, phi -0.22)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)

portfolios: A EV +1.83 (adj +0.47) on $15.67, P(profit) 0.6129, adj growth 4.2 bp · B EV +1.47 (adj +0.76) on $17.29, P(profit) 0.5777, adj growth 7.2 bp · C EV +1.33 (adj +0.59) on $16.65, P(profit) 0.497, adj growth 5.5 bp · R EV +0.23 (adj +0.11) on $3.00, P(profit) 0.5414, adj growth 4.1 bp

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
