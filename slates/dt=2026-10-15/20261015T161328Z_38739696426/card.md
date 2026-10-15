# NHL THESIS CARD — RESEARCH_ONLY — status **COMPLETE**

generated 2026-10-15T16:13:28Z · nhl-thesis-1.1 · gate PASS · nominal bankroll $1000 (quarter Kelly; caps bet 2% / game 5% / thesis 3% / slate 15%)

**Research execution (RESEARCH GOVERNANCE, not model truth):** research bankroll $250, whole-dollar stakes, max $5 per wager; ≤ 1 funded player prop per game; ≤ 2 funded player props with adjusted p < 0.30 per slate; player props 10+ pts from the Kalshi mid need corroboration. SHADOW_ONLY = $0 (logged for learning). Nothing is placed.

## Slate portfolios (simulated P/L on the joint draws)

EV / median / P(profit) / percentiles use the MODEL's joint distribution at executable costs; 'EV adj' and 'adj growth' use the confidence-adjusted probabilities (the optimiser's objective). A uses raw model probabilities and independent stakes, so its model EV can look larger.

| portfolio | stake | EV (model) | EV adj | median | P(profit) | p10 | p05 | adj growth bp |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A highest edges (independent) | 149.96 | +26.91 | +7.18 | +26.51 | 0.814 | -11.83 | -22.54 | 67.09 |
| B thesis-diversified (joint) ← optimiser card | 150.00 | +21.95 | +10.41 | +20.18 | 0.762 | -15.48 | -24.43 | 99.47 |
| C best expression per thesis | 150.01 | +24.96 | +9.24 | +21.95 | 0.757 | -16.45 | -26.67 | 86.31 |
| R FUNDED research stakes | 17.00 | +1.59 | +0.93 | +0.56 | 0.557 | -4.17 | -5.77 | 0.00 |

## BUF @ TOR  ·  10000 joint draws  ·  444 bet sides mapped, 3 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.519 / away 0.480

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_TOR_win | p_BUF_win | p_overtime | goals | shots TOR/BUF | TOR/BUF starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.114 | 0.50 | 0.50 | 0.00 | 6.06 | 28.1/28.8 | 25.2/24.6 | even strength |
| BUF shot control · normal event (5-7) · decided (2+) | 0.110 | 0.48 | 0.52 | 0.00 | 6.0 | 22.2/34.0 | 30.2/18.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.107 | 0.51 | 0.49 | 0.49 | 5.95 | 28.2/28.9 | 25.4/24.9 | even strength |
| BUF shot control · normal event (5-7) · tight (1-goal/OT) | 0.106 | 0.48 | 0.52 | 0.48 | 5.92 | 22.4/34.5 | 31.2/19.2 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.089 | 0.53 | 0.47 | 0.00 | 9.36 | 29.3/30.2 | 23.9/22.8 | even strength |
| BUF shot control · high event (8+) · decided (2+) | 0.086 | 0.45 | 0.55 | 0.00 | 9.39 | 23.7/36.0 | 29.0/18.4 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Owen Power: 1+ goals NO | 88 | 0.915 | 0.902 | +0.028 | +0.015 | $7.27 | FUNDED_RESEARCH | $2 | BUF:SUPPRESSED | DIRECT (0.96) | EVIDENCE_STRONGER | D |
| Sergei Bobrovsky: 26+ saves YES | 49 | 0.566 | 0.525 | +0.058 | +0.018 | $3.31 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TOR:NET_HIGH_VOLUME | DIRECT (0.93) | EVIDENCE_MIXED | D |
| Gavin McKenna: 1+ assists NO | 70 | 0.763 | 0.729 | +0.049 | +0.014 | $5.01 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | TOR:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Owen Power: 1+ goals NO** — thesis: BUF offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15BUFTOR-BUFTTHOMPSON72-1|no; why: higher confidence-adjusted growth (5.07 vs 0.25 bp); alternative not eligible: confidence-adjusted EV +0.0051 below the 0.010/contract floor; relationships: KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: BUF offense succeeds (4+ goals)
- **Sergei Bobrovsky: 26+ saves YES** — thesis: TOR net faces heavy volume (33+ shots; BUF pressure); alternative: no other contract in this game expresses this thesis (phi >= 0.20); why: only expression of its thesis on the board; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.039); KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: MOSTLY_INDEPENDENT (phi -0.025); failure: TOR net faces light volume (<= 25 shots; BUF suppressed)
- **Gavin McKenna: 1+ assists NO** — thesis: TOR offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15BUFTOR-TORAMATTHEWS34-1|no; why: higher confidence-adjusted growth (2.23 vs 0.30 bp); alternative not eligible: confidence-adjusted EV +0.0058 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: MOSTLY_INDEPENDENT (phi -0.025); failure: TOR offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.11, BUF shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TOR:NET_HIGH_VOLUME (p 0.3635): highest fidelity KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes [DIRECT], best adjusted EV KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes (same contract)
- thesis TOR:SUPPRESSED (p 0.3639): highest fidelity KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no (same contract)
- thesis BUF:SUPPRESSED (p 0.3752): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15BUFTOR-BUFOPOWER25-1|no: FUNDED_RESEARCH; family TRUSTED; loses 4% of the draws where the thesis happens; fragile player expression; opposing: failure thesis BUF:OFFENSE_4PLUS (p 0.4055, phi -0.117)
- KXNHLSAVE-26OCT15BUFTOR-TORSBOBROVSKY72-26|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family MIXED; loses 7% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:NET_LOW_VOLUME (p 0.2268, phi -0.618)
- KXNHLAST-26OCT15BUFTOR-TORGMCKENNA92-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TOR:OFFENSE_4PLUS (p 0.4115, phi -0.217)

portfolios: A EV +0.98 (adj +0.33) on $13.80, P(profit) 0.5539, adj growth 3.2 bp · B EV +0.95 (adj +0.34) on $15.59, P(profit) 0.3958, adj growth 3.3 bp · C EV +1.01 (adj +0.31) on $11.70, P(profit) 0.4266, adj growth 2.9 bp · R EV +0.06 (adj +0.03) on $2.00, P(profit) 0.915, adj growth 1.3 bp

## NYI @ OTT  ·  10000 joint draws  ·  450 bet sides mapped, 4 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.593 / away 0.407

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_OTT_win | p_NYI_win | p_overtime | goals | shots OTT/NYI | OTT/NYI starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.63 | 0.37 | 0.00 | 6.03 | 26.8/26.5 | 23.6/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.113 | 0.52 | 0.48 | 0.49 | 5.88 | 26.9/26.6 | 23.5/23.7 | even strength |
| OTT shot control · normal event (5-7) · decided (2+) | 0.090 | 0.71 | 0.29 | 0.00 | 6.04 | 31.7/21.0 | 18.5/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.085 | 0.65 | 0.35 | 0.00 | 9.27 | 28.7/28.3 | 22.9/21.7 | even strength |
| OTT shot control · normal event (5-7) · tight (1-goal/OT) | 0.078 | 0.56 | 0.45 | 0.47 | 5.86 | 31.8/21.3 | 18.2/28.6 | even strength |
| balanced shots · low event (<=4) · tight (1-goal/OT) | 0.056 | 0.52 | 0.48 | 0.47 | 2.79 | 25.5/25.3 | 23.8/24.0 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Andre Burakovsky: 1+ assists NO | 75 | 0.829 | 0.784 | +0.066 | +0.021 | $7.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | OTT:SUPPRESSED | DIRECT (0.92) | EVIDENCE_MIXED | D |
| Nick Cousins: 1+ goals YES | 10 | 0.134 | 0.122 | +0.028 | +0.015 | $1.42 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Warren Foegele: 1+ goals YES | 14 | 0.176 | 0.165 | +0.028 | +0.016 | $1.67 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.25) | EVIDENCE_STRONGER | D |
| Ridly Greig: 1+ goals YES | 15 | 0.184 | 0.174 | +0.025 | +0.015 | $1.64 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | OTT:OFFENSE_4PLUS | FRAGILE (0.27) | EVIDENCE_STRONGER | D |
- **Andre Burakovsky: 1+ assists NO** — thesis: OTT offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15NYIOTT-OTTDBATHERSON19-1|no; why: higher confidence-adjusted growth (5.49 vs 0.26 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; alternative not eligible: confidence-adjusted EV +0.0050 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15NYIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.071); failure: OTT offense succeeds (4+ goals)
- **Nick Cousins: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (5.36 vs 3.73 bp); relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.003); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.013); failure: OTT offense suppressed (<= 2 goals)
- **Warren Foegele: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes; why: higher confidence-adjusted growth (4.59 vs 3.73 bp); relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: MOSTLY_INDEPENDENT (phi -0.017); KXNHLGOAL-26OCT15NYIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi -0.008); KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: OTT offense suppressed (<= 2 goals)
- **Ridly Greig: 1+ goals YES** — thesis: OTT offense succeeds (4+ goals); alternative: KXNHLTOTAL-26OCT15NYIOTT-8|yes; why: higher confidence-adjusted growth (3.73 vs 1.12 bp); despite a smaller raw edge (+0.025 vs +0.035/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.884 vs 0.326); alternative not eligible: confidence-adjusted EV +0.0093 below the 0.010/contract floor; relationships: KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: INTENTIONAL_DIVERSIFIER (phi -0.071); KXNHLGOAL-26OCT15NYIOTT-OTTNCOUSINS21-1|yes: MOSTLY_INDEPENDENT (phi 0.013); KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: OTT offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, OTT shot control · normal event (5-7) · decided (2+) 0.09.
- thesis OTT:OFFENSE_4PLUS (p 0.435): highest fidelity KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes (same contract)
- thesis OTT:SUPPRESSED (p 0.3461): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLAST-26OCT15NYIOTT-OTTABURAKOVSKY95-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 8% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:OFFENSE_4PLUS (p 0.435, phi -0.193)
- KXNHLGOAL-26OCT15NYIOTT-OTTNCOUSINS21-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3461, phi -0.165)
- KXNHLGOAL-26OCT15NYIOTT-OTTWFOEGELE37-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 75% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3461, phi -0.165)
- KXNHLGOAL-26OCT15NYIOTT-OTTRGREIG71-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 73% of the draws where the thesis happens; fragile player expression; opposing: failure thesis OTT:SUPPRESSED (p 0.3461, phi -0.198)

portfolios: A EV +1.77 (adj +0.91) on $11.96, P(profit) 0.4161, adj growth 8.5 bp · B EV +1.56 (adj +0.75) on $12.00, P(profit) 0.3628, adj growth 7.2 bp · C EV +0.34 (adj +0.21) on $2.15, P(profit) 0.1838, adj growth 1.9 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## SEA @ TBL  ·  10000 joint draws  ·  398 bet sides mapped, 26 +EV candidates, 3 on card

sportsbook moneyline consensus (5 books): home 0.700 / away 0.300

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
| John Carlson: 1+ assists NO | 51 | 0.680 | 0.566 | +0.153 | +0.039 | $4.67 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_MIXED | D |
| Jake Guentzel: 1+ goals NO | 61 | 0.671 | 0.654 | +0.044 | +0.028 | $3.93 | FUNDED_RESEARCH | $1 | TBL:SUPPRESSED | DIRECT (0.83) | EVIDENCE_STRONGER | D |
| Nikita Kucherov: 1+ goals NO | 59 | 0.640 | 0.625 | +0.034 | +0.018 | $2.30 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | TBL:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
- **John Carlson: 1+ assists NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no; why: higher confidence-adjusted growth (13.22 vs 10.14 bp); relationships: KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi 0.143); failure: TBL offense succeeds (4+ goals)
- **Jake Guentzel: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.71 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.139); KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TBL offense succeeds (4+ goals)
- **Nikita Kucherov: 1+ goals NO** — thesis: TBL offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no; why: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: MOSTLY_INDEPENDENT (phi 0.143); KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: MOSTLY_INDEPENDENT (phi -0.02); failure: TBL offense succeeds (4+ goals)

**Review**: scripts TBL shot control · normal event (5-7) · decided (2+) 0.14, balanced shots · normal event (5-7) · decided (2+) 0.11, TBL shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis TBL:SUPPRESSED (p 0.3553): highest fidelity KXNHLTEAMTOTAL-26OCT15SEATB-TB5|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.71 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- thesis SEA:WINS_BY_2PLUS (p 0.2152): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis SEA:WINS (p 0.4164): highest fidelity KXNHLSPREAD-26OCT15SEATB-TB2|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no — Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- KXNHLAST-26OCT15SEATB-TBJCARLSON74-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 17% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.5 pts; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.243)
- KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no: FUNDED_RESEARCH; family TRUSTED; loses 17% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.238)
- KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis TBL:OFFENSE_4PLUS (p 0.4272, phi -0.26)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBNKUCHEROV86-1|no selected over broad KXNHLTEAMTOTAL-26OCT15SEATB-SEA2|yes because adjusted EV is 0.0 pts higher while thesis capture is 0.76 vs 0.98 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)
- override: Player prop expression KXNHLGOAL-26OCT15SEATB-TBJGUENTZEL59-1|no selected over player prop KXNHLAST-26OCT15SEATB-TBNKUCHEROV86-1|no because adjusted EV differs by only 0.5 pts while thesis capture is 0.83 vs 0.71 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +4.60 (adj +0.94) on $13.80, P(profit) 0.6253, adj growth 8.8 bp · B EV +1.76 (adj +0.59) on $10.90, P(profit) 0.6215, adj growth 5.7 bp · C EV +4.47 (adj +1.52) on $18.15, P(profit) 0.6586, adj growth 14.4 bp · R EV +0.07 (adj +0.04) on $1.00, P(profit) 0.671, adj growth 1.7 bp

## VAN @ FLA  ·  10000 joint draws  ·  388 bet sides mapped, 27 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.715 / away 0.285

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_FLA_win | p_VAN_win | p_overtime | goals | shots FLA/VAN | FLA/VAN starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| FLA shot control · normal event (5-7) · decided (2+) | 0.119 | 0.63 | 0.37 | 0.00 | 6.02 | 32.5/21.1 | 18.3/28.3 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.117 | 0.60 | 0.40 | 0.00 | 6.04 | 27.3/26.8 | 23.6/23.3 | even strength |
| FLA shot control · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.56 | 0.44 | 0.46 | 5.92 | 32.9/21.4 | 18.2/29.4 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.098 | 0.52 | 0.48 | 0.45 | 5.98 | 27.1/26.6 | 23.3/23.7 | even strength |
| FLA shot control · high event (8+) · decided (2+) | 0.089 | 0.69 | 0.31 | 0.00 | 9.26 | 34.3/22.7 | 18.1/26.8 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.086 | 0.59 | 0.41 | 0.00 | 9.34 | 28.9/28.4 | 22.6/22.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Drew O'Connor: 1+ goals YES | 11 | 0.184 | 0.163 | +0.067 | +0.046 | $3.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Marco Rossi: 1+ goals YES | 17 | 0.245 | 0.225 | +0.065 | +0.045 | $3.95 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.38) | EVIDENCE_STRONGER | D |
| Linus Karlsson: 1+ goals YES | 16 | 0.229 | 0.210 | +0.059 | +0.041 | $3.46 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VAN:OFFENSE_4PLUS | FRAGILE (0.35) | EVIDENCE_STRONGER | D |
| Brady Tkachuk: 1+ goals NO | 62 | 0.695 | 0.674 | +0.058 | +0.037 | $6.79 | FUNDED_RESEARCH | $2 | FLA:SUPPRESSED | DIRECT (0.86) | EVIDENCE_STRONGER | D |
- **Drew O'Connor: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes; why: higher confidence-adjusted growth (43.69 vs 29.71 bp); relationships: KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.019); failure: VAN offense suppressed (<= 2 goals)
- **Marco Rossi: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (43.69 vs 29.71 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.015); they share one thesis budget; relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.015); KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.009); failure: VAN offense suppressed (<= 2 goals)
- **Linus Karlsson: 1+ goals YES** — thesis: VAN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes has the higher standalone adjusted growth (43.69 vs 25.21 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.001); they share one thesis budget; relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi -0.01); KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: MOSTLY_INDEPENDENT (phi 0.008); failure: VAN offense suppressed (<= 2 goals)
- **Brady Tkachuk: 1+ goals NO** — thesis: FLA offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes; why: KXNHLSPREAD-26OCT15VANFLA-VAN2|yes has the higher standalone adjusted growth (23.10 vs 13.09 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.147); relationships: KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: MOSTLY_INDEPENDENT (phi 0.019); KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: MOSTLY_INDEPENDENT (phi 0.009); KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: MOSTLY_INDEPENDENT (phi 0.008); failure: FLA offense succeeds (4+ goals)

**Review**: scripts FLA shot control · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.12, FLA shot control · normal event (5-7) · tight (1-goal/OT) 0.10.
- thesis VAN:OFFENSE_4PLUS (p 0.3486): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN3|yes [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis VAN:WINS_BY_2PLUS (p 0.2226): highest fidelity KXNHLSPREAD-26OCT15VANFLA-VAN2|yes [STRUCTURAL], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis GAME:HIGH_EVENT (p 0.2875): highest fidelity KXNHLTEAMTOTAL-26OCT15VANFLA-VAN2|yes [DIRECT], best adjusted EV KXNHLTEAMTOTAL-26OCT15VANFLA-VAN5|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15VANFLA-VANDOCONNOR18-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4364, phi -0.203)
- KXNHLGOAL-26OCT15VANFLA-VANMROSSI23-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 62% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4364, phi -0.238)
- KXNHLGOAL-26OCT15VANFLA-VANLKARLSSON94-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 65% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VAN:SUPPRESSED (p 0.4364, phi -0.212)
- KXNHLGOAL-26OCT15VANFLA-FLABTKACHUK8-1|no: FUNDED_RESEARCH; family TRUSTED; loses 14% of the draws where the thesis happens; fragile player expression; opposing: failure thesis FLA:OFFENSE_4PLUS (p 0.4593, phi -0.251)

portfolios: A EV +3.78 (adj +0.81) on $13.80, P(profit) 0.5323, adj growth 7.4 bp · B EV +5.28 (adj +3.60) on $17.69, P(profit) 0.5275, adj growth 34.4 bp · C EV +6.18 (adj +3.30) on $11.04, P(profit) 0.3893, adj growth 30.4 bp · R EV +0.18 (adj +0.12) on $2.00, P(profit) 0.6948, adj growth 4.5 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15VANFLA-VAN|yes == KXNHLGAME-26OCT15VANFLA-FLA|no

## NYR @ NJD  ·  10000 joint draws  ·  424 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.549 / away 0.451

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NJD_win | p_NYR_win | p_overtime | goals | shots NJD/NYR | NJD/NYR starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| NJD shot control · normal event (5-7) · decided (2+) | 0.129 | 0.54 | 0.46 | 0.00 | 5.99 | 33.0/21.1 | 17.9/29.2 | even strength |
| NJD shot control · normal event (5-7) · tight (1-goal/OT) | 0.116 | 0.52 | 0.48 | 0.47 | 5.87 | 33.0/21.3 | 18.2/29.8 | even strength |
| balanced shots · normal event (5-7) · decided (2+) | 0.106 | 0.48 | 0.52 | 0.00 | 6.02 | 27.3/26.7 | 23.1/23.9 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.095 | 0.49 | 0.51 | 0.50 | 5.94 | 27.4/26.7 | 23.4/24.1 | even strength |
| NJD shot control · high event (8+) · decided (2+) | 0.073 | 0.57 | 0.43 | 0.00 | 9.17 | 34.8/22.8 | 17.4/28.1 | even strength |
| NJD shot control · low event (<=4) · decided (2+) | 0.070 | 0.55 | 0.45 | 0.00 | 3.46 | 31.5/20.0 | 18.4/29.5 | late empty net |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Matt Rempe: 1+ goals YES | 6 | 0.090 | 0.082 | +0.026 | +0.018 | $1.49 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NYR:OFFENSE_4PLUS | FRAGILE (0.14) | EVIDENCE_STRONGER | D |
| Timo Meier: 1+ goals NO | 73 | 0.777 | 0.764 | +0.033 | +0.020 | $6.36 | FUNDED_RESEARCH | $2 | NJD:SUPPRESSED | DIRECT (0.88) | EVIDENCE_STRONGER | D |
| Jack Hughes: 1+ goals NO | 62 | 0.671 | 0.657 | +0.035 | +0.021 | $4.54 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | NJD:SUPPRESSED | DIRECT (0.82) | EVIDENCE_STRONGER | D |
| New Jersey wins by over 2.5 goals NO | 77 | 0.823 | 0.794 | +0.041 | +0.012 | $2.73 | FUNDED_RESEARCH | $1 | NYR:WINS | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
- **Matt Rempe: 1+ goals YES** — thesis: NYR offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes; why: higher confidence-adjusted growth (10.90 vs 3.31 bp); despite a smaller raw edge (+0.026 vs +0.053/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.065); failure: NYR offense suppressed (<= 2 goals)
- **Timo Meier: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no has the higher standalone adjusted growth (6.24 vs 4.61 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it +0.044); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: MOSTLY_INDEPENDENT (phi 0.121); failure: NJD offense succeeds (4+ goals)
- **Jack Hughes: 1+ goals NO** — thesis: NJD offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no; why: KXNHLAST-26OCT15NYRNJ-NJJHUGHES86-2|no has the higher standalone adjusted growth (6.24 vs 4.05 bp), but the joint optimum prefers this bet in combination with the rest of the card (phi with it -0.024); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.006); KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: REINFORCING (phi 0.153); failure: NJD offense succeeds (4+ goals)
- **New Jersey wins by over 2.5 goals NO** — thesis: NYR wins (incl. OT/SO); alternative: KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no; why: Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ3|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.98 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity); relationships: KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: MOSTLY_INDEPENDENT (phi 0.065); KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: MOSTLY_INDEPENDENT (phi 0.121); KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: REINFORCING (phi 0.153); failure: NJD wins by 2+

**Review**: scripts NJD shot control · normal event (5-7) · decided (2+) 0.13, NJD shot control · normal event (5-7) · tight (1-goal/OT) 0.12, balanced shots · normal event (5-7) · decided (2+) 0.11.
- thesis NJD:SUPPRESSED (p 0.4147): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:WINS (p 0.4932): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [STRUCTURAL], best adjusted EV KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis NYR:OFFENSE_4PLUS (p 0.3577): highest fidelity KXNHLSPREAD-26OCT15NYRNJ-NJ3|no [DIRECT], best adjusted EV KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes — Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ3|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.98 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)
- KXNHLGOAL-26OCT15NYRNJ-NYRMREMPE73-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 86% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NYR:SUPPRESSED (p 0.4207, phi -0.14)
- KXNHLGOAL-26OCT15NYRNJ-NJTMEIER28-1|no: FUNDED_RESEARCH; family TRUSTED; loses 12% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3686, phi -0.211)
- KXNHLGOAL-26OCT15NYRNJ-NJJHUGHES86-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 18% of the draws where the thesis happens; fragile player expression; opposing: failure thesis NJD:OFFENSE_4PLUS (p 0.3686, phi -0.24)
- KXNHLSPREAD-26OCT15NYRNJ-NJ3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis NJD:WINS_BY_2PLUS (p 0.2835, phi -0.737)
- override: Broad expression KXNHLSPREAD-26OCT15NYRNJ-NJ3|no selected over player prop KXNHLAST-26OCT15NYRNJ-NYRGPERREAULT94-1|yes because adjusted EV differs by only 0.6 pts while thesis capture is 0.98 vs 0.49 (DIRECT vs FRAGILE; reliability EVIDENCE_MIXED vs EVIDENCE_MIXED; decided on expression fidelity)

portfolios: A EV +1.81 (adj +0.50) on $13.80, P(profit) 0.6186, adj growth 4.7 bp · B EV +1.29 (adj +0.77) on $15.12, P(profit) 0.5669, adj growth 7.3 bp · C EV +1.83 (adj +0.66) on $23.70, P(profit) 0.617, adj growth 6.3 bp · R EV +0.14 (adj +0.07) on $3.00, P(profit) 0.6586, adj growth 2.6 bp

## PHI @ DET  ·  10000 joint draws  ·  406 bet sides mapped, 7 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.559 / away 0.441

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
| Nate Danielson: 1+ goals NO | 84 | 0.887 | 0.873 | +0.038 | +0.023 | $7.27 | FUNDED_RESEARCH | $2 | DET:SUPPRESSED | DIRECT (0.94) | EVIDENCE_STRONGER | D |
| Christian Dvorak: 1+ goals YES | 19 | 0.233 | 0.221 | +0.032 | +0.020 | $2.20 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:OFFENSE_4PLUS | FRAGILE (0.36) | EVIDENCE_STRONGER | D |
| Sheldon Dries: 1+ goals YES | 9 | 0.121 | 0.109 | +0.025 | +0.013 | $1.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | DET:OFFENSE_4PLUS | FRAGILE (0.21) | EVIDENCE_STRONGER | D |
| Porter Martone: 1+ goals NO | 78 | 0.822 | 0.810 | +0.030 | +0.018 | $7.27 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | PHI:SUPPRESSED | DIRECT (0.91) | EVIDENCE_STRONGER | D |
- **Nate Danielson: 1+ goals NO** — thesis: DET offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no; why: higher confidence-adjusted growth (9.52 vs 3.46 bp); despite a smaller raw edge (+0.038 vs +0.058/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.021); failure: DET offense succeeds (4+ goals)
- **Christian Dvorak: 1+ goals YES** — thesis: PHI offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15PHIDET-DET3|no; why: higher confidence-adjusted growth (5.49 vs 1.38 bp); despite a smaller raw edge (+0.032 vs +0.037/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.002); KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi -0.011); failure: PHI offense suppressed (<= 2 goals)
- **Sheldon Dries: 1+ goals YES** — thesis: DET offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15PHIDET-DETEFINNIE58-1|yes; why: higher confidence-adjusted growth (4.52 vs 0.00 bp); evidence EVIDENCE_STRONGER vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi -0.009); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi 0.007); KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: MOSTLY_INDEPENDENT (phi 0.003); failure: DET offense suppressed (<= 2 goals)
- **Porter Martone: 1+ goals NO** — thesis: PHI offense suppressed (<= 2 goals); alternative: KXNHLTOTAL-26OCT15PHIDET-4|no; why: higher confidence-adjusted growth (4.31 vs 0.78 bp); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.988 vs 0.35); alternative not eligible: confidence-adjusted EV +0.0069 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: MOSTLY_INDEPENDENT (phi 0.021); KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: MOSTLY_INDEPENDENT (phi -0.011); KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: MOSTLY_INDEPENDENT (phi 0.003); failure: PHI offense succeeds (4+ goals)

**Review**: scripts DET shot control · normal event (5-7) · decided (2+) 0.11, balanced shots · normal event (5-7) · decided (2+) 0.11, DET shot control · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis PHI:OFFENSE_4PLUS (p 0.3214): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis PHI:SUPPRESSED (p 0.4542): highest fidelity KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no [DIRECT], best adjusted EV KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no (same contract)
- thesis DET:SUPPRESSED (p 0.4363): highest fidelity KXNHLSPREAD-26OCT15PHIDET-DET3|no [STRUCTURAL], best adjusted EV KXNHLAST-26OCT15PHIDET-DETVARVIDSSON33-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15PHIDET-DETNDANIELSON29-1|no: FUNDED_RESEARCH; family TRUSTED; loses 6% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:OFFENSE_4PLUS (p 0.3447, phi -0.153)
- KXNHLGOAL-26OCT15PHIDET-PHICDVORAK22-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 64% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:SUPPRESSED (p 0.4542, phi -0.224)
- KXNHLGOAL-26OCT15PHIDET-DETSDRIES15-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 79% of the draws where the thesis happens; fragile player expression; opposing: failure thesis DET:SUPPRESSED (p 0.4363, phi -0.176)
- KXNHLGOAL-26OCT15PHIDET-PHIPMARTONE94-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 9% of the draws where the thesis happens; fragile player expression; opposing: failure thesis PHI:OFFENSE_4PLUS (p 0.3214, phi -0.199)

portfolios: A EV +1.02 (adj +0.47) on $13.80, P(profit) 0.6705, adj growth 4.5 bp · B EV +1.26 (adj +0.76) on $17.95, P(profit) 0.317, adj growth 7.3 bp · C EV +1.68 (adj +0.78) on $24.88, P(profit) 0.6078, adj growth 7.3 bp · R EV +0.09 (adj +0.06) on $2.00, P(profit) 0.8871, adj growth 2.2 bp

## WPG @ CHI  ·  10000 joint draws  ·  412 bet sides mapped, 5 +EV candidates, 2 on card

sportsbook moneyline consensus (5 books): home 0.455 / away 0.545

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_CHI_win | p_WPG_win | p_overtime | goals | shots CHI/WPG | CHI/WPG starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.124 | 0.49 | 0.51 | 0.00 | 6.0 | 26.2/26.5 | 23.0/22.8 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.118 | 0.50 | 0.50 | 0.48 | 5.92 | 26.7/27.0 | 23.6/23.4 | even strength |
| WPG shot control · normal event (5-7) · decided (2+) | 0.093 | 0.42 | 0.58 | 0.00 | 5.98 | 21.0/31.7 | 27.8/18.0 | even strength |
| WPG shot control · normal event (5-7) · tight (1-goal/OT) | 0.087 | 0.46 | 0.54 | 0.47 | 5.85 | 21.1/32.1 | 28.6/17.9 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.081 | 0.51 | 0.49 | 0.00 | 9.28 | 28.1/28.5 | 22.4/22.0 | even strength |
| WPG shot control · high event (8+) · decided (2+) | 0.058 | 0.42 | 0.58 | 0.00 | 9.3 | 22.2/33.7 | 26.3/17.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Roman Kantserov: 1+ goals NO | 74 | 0.799 | 0.783 | +0.045 | +0.029 | $6.48 | FUNDED_RESEARCH | $2 | CHI:SUPPRESSED | DIRECT (0.89) | EVIDENCE_STRONGER | D |
| Connor Bedard: 1+ assists NO | 51 | 0.668 | 0.556 | +0.141 | +0.028 | $4.42 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | CHI:SUPPRESSED | DIRECT (0.82) | EVIDENCE_MIXED | D |
- **Roman Kantserov: 1+ goals NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (10.32 vs 6.95 bp); despite a smaller raw edge (+0.045 vs +0.141/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: REINFORCING (phi 0.164); failure: CHI offense succeeds (4+ goals)
- **Connor Bedard: 1+ assists NO** — thesis: CHI offense suppressed (<= 2 goals); alternative: KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no; why: higher confidence-adjusted growth (6.95 vs 3.21 bp); evidence EVIDENCE_MIXED vs EVIDENCE_STRONGER; relationships: KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: REINFORCING (phi 0.164); failure: CHI offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.12, WPG shot control · normal event (5-7) · decided (2+) 0.09.
- thesis CHI:SUPPRESSED (p 0.4115): highest fidelity KXNHLGOAL-26OCT15WPGCHI-CHICBEDARD98-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- KXNHLGOAL-26OCT15WPGCHI-CHIRKANTSEROV80-1|no: FUNDED_RESEARCH; family TRUSTED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3691, phi -0.174)
- KXNHLAST-26OCT15WPGCHI-CHICBEDARD98-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 18% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 17.3 pts; fragile player expression; opposing: failure thesis CHI:OFFENSE_4PLUS (p 0.3691, phi -0.25)

portfolios: A EV +2.11 (adj +0.51) on $13.80, P(profit) 0.6682, adj growth 4.9 bp · B EV +1.57 (adj +0.49) on $10.90, P(profit) 0.5647, adj growth 4.7 bp · C EV +2.15 (adj +0.43) on $8.04, P(profit) 0.6682, adj growth 4.0 bp · R EV +0.12 (adj +0.08) on $2.00, P(profit) 0.7989, adj growth 3.0 bp

## SJS @ NSH  ·  10000 joint draws  ·  456 bet sides mapped, 5 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.557 / away 0.443

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_NSH_win | p_SJS_win | p_overtime | goals | shots NSH/SJS | NSH/SJS starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.133 | 0.55 | 0.45 | 0.00 | 6.05 | 27.8/27.6 | 24.2/24.0 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.110 | 0.52 | 0.48 | 0.46 | 5.93 | 27.7/27.8 | 24.4/24.4 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.103 | 0.55 | 0.45 | 0.00 | 9.46 | 29.2/29.3 | 23.4/22.7 | even strength |
| NSH shot control · normal event (5-7) · decided (2+) | 0.069 | 0.62 | 0.38 | 0.00 | 5.98 | 32.2/21.9 | 19.0/27.8 | even strength |
| SJS shot control · normal event (5-7) · decided (2+) | 0.068 | 0.49 | 0.51 | 0.00 | 6.04 | 22.1/32.8 | 28.8/18.7 | even strength |
| SJS shot control · normal event (5-7) · tight (1-goal/OT) | 0.059 | 0.50 | 0.50 | 0.45 | 5.95 | 22.1/32.6 | 29.4/18.9 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Collin Graf: 1+ goals YES | 13 | 0.168 | 0.156 | +0.030 | +0.018 | $1.92 | SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.26) | EVIDENCE_STRONGER | D |
| Ivar Stenberg: 1+ assists NO | 68 | 0.807 | 0.718 | +0.112 | +0.023 | $7.27 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.91) | EVIDENCE_MIXED | D |
| Mason Marchment: 1+ goals YES | 21 | 0.245 | 0.234 | +0.024 | +0.012 | $1.61 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | SJS:OFFENSE_4PLUS | FRAGILE (0.37) | EVIDENCE_STRONGER | D |
| Macklin Celebrini: 1+ assists NO | 43 | 0.576 | 0.459 | +0.129 | +0.012 | $2.46 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | SJS:SUPPRESSED | DIRECT (0.77) | CALIBRATION_WARNING | D |
- **Collin Graf: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes; why: higher confidence-adjusted growth (5.74 vs 1.88 bp); relationships: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.089); failure: SJS offense suppressed (<= 2 goals)
- **Ivar Stenberg: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no; why: higher confidence-adjusted growth (5.41 vs 1.25 bp); despite a smaller raw edge (+0.112 vs +0.129/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.052); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: MOSTLY_INDEPENDENT (phi 0.046); failure: SJS offense succeeds (4+ goals)
- **Mason Marchment: 1+ goals YES** — thesis: SJS offense succeeds (4+ goals); alternative: KXNHLTEAMTOTAL-26OCT15SJNSH-SJ5|yes; why: higher confidence-adjusted growth (1.88 vs 0.25 bp); despite a smaller raw edge (+0.024 vs +0.024/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; wins across more scripts (relative breadth 0.872 vs 0.542); alternative not eligible: confidence-adjusted EV +0.0043 below the 0.010/contract floor; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: MOSTLY_INDEPENDENT (phi 0.001); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi -0.037); KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: INTENTIONAL_DIVERSIFIER (phi -0.115); failure: SJS offense suppressed (<= 2 goals)
- **Macklin Celebrini: 1+ assists NO** — thesis: SJS offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no; why: second expression of the same thesis: KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no has the higher standalone adjusted growth (5.41 vs 1.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.046); they share one thesis budget; relationships: KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.089); KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: MOSTLY_INDEPENDENT (phi 0.046); KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.115); failure: SJS offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis SJS:SUPPRESSED (p 0.3922): highest fidelity KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no (same contract)
- thesis SJS:OFFENSE_4PLUS (p 0.3937): highest fidelity KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes (same contract)
- KXNHLGOAL-26OCT15SJNSH-SJCGRAF51-1|yes: SHADOW_ONLY — LOW_PROB_PLAYER_PROP_SLATE_CAP; family TRUSTED; loses 74% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3922, phi -0.188)
- KXNHLAST-26OCT15SJNSH-SJISTENBERG41-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 9% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3937, phi -0.212)
- KXNHLGOAL-26OCT15SJNSH-SJMMARCHMENT27-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 63% of the draws where the thesis happens; fragile player expression; opposing: failure thesis SJS:SUPPRESSED (p 0.3922, phi -0.238)
- KXNHLAST-26OCT15SJNSH-SJMCELEBRINI71-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family WARNING; loses 23% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 15.6 pts; fragile player expression; opposing: failure thesis SJS:OFFENSE_4PLUS (p 0.3937, phi -0.276)

portfolios: A EV +2.86 (adj +0.67) on $13.80, P(profit) 0.6803, adj growth 6.3 bp · B EV +2.46 (adj +0.64) on $13.26, P(profit) 0.6603, adj growth 6.1 bp · C EV +1.82 (adj +0.44) on $12.00, P(profit) 0.8073, adj growth 4.2 bp · R EV +0.00 (adj +0.00) on $0.00, P(profit) 0, adj growth 0.0 bp

## STL @ MIN  ·  10000 joint draws  ·  430 bet sides mapped, 6 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.564 / away 0.436

**Game scripts** (shot control · environment · margin; 18 occur, top 6 shown)

| script | freq | p_MIN_win | p_STL_win | p_overtime | goals | shots MIN/STL | MIN/STL starter saves | driver |
|---|---:|---:|---:|---:|---:|---|---|---|
| balanced shots · normal event (5-7) · decided (2+) | 0.123 | 0.58 | 0.42 | 0.00 | 6.04 | 27.7/27.4 | 23.9/23.7 | even strength |
| balanced shots · normal event (5-7) · tight (1-goal/OT) | 0.111 | 0.55 | 0.45 | 0.46 | 5.99 | 27.7/27.6 | 24.2/24.3 | even strength |
| balanced shots · high event (8+) · decided (2+) | 0.100 | 0.58 | 0.42 | 0.00 | 9.3 | 29.3/29.1 | 23.3/22.9 | even strength |
| MIN shot control · normal event (5-7) · decided (2+) | 0.081 | 0.66 | 0.34 | 0.00 | 6.01 | 32.7/21.9 | 19.2/28.3 | even strength |
| MIN shot control · normal event (5-7) · tight (1-goal/OT) | 0.077 | 0.53 | 0.47 | 0.48 | 5.93 | 32.7/22.1 | 18.9/29.3 | even strength |
| MIN shot control · high event (8+) · decided (2+) | 0.061 | 0.62 | 0.38 | 0.00 | 9.21 | 34.7/23.4 | 18.4/27.3 | even strength |

**Card**

| bet | ask | p model | p adj | EV raw | EV adj | optimiser stake | research status | research $ | thesis | fidelity (capture) | reliability | bench |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|---|---|
| Ross Johnston: 1+ goals YES | 5 | 0.075 | 0.068 | +0.022 | +0.015 | $1.23 | FUNDED_RESEARCH | $1 | STL:OFFENSE_4PLUS | FRAGILE (0.12) | EVIDENCE_STRONGER | D |
| Ryan Hartman: 1+ goals YES | 19 | 0.232 | 0.219 | +0.032 | +0.018 | $1.96 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.33) | EVIDENCE_STRONGER | D |
| Rieger Lorenz: 1+ goals YES | 10 | 0.138 | 0.120 | +0.032 | +0.014 | $1.22 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | MIN:OFFENSE_4PLUS | FRAGILE (0.20) | EVIDENCE_STRONGER | D |
| Adam Jiricek: 1+ assists NO | 72 | 0.784 | 0.747 | +0.050 | +0.013 | $5.12 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED | $0 | STL:SUPPRESSED | DIRECT (0.89) | EVIDENCE_MIXED | D |
- **Ross Johnston: 1+ goals YES** — thesis: STL offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes; why: higher confidence-adjusted growth (8.81 vs 1.68 bp); despite a smaller raw edge (+0.022 vs +0.025/contract); relationships: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi -0.038); failure: STL offense suppressed (<= 2 goals)
- **Ryan Hartman: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: higher confidence-adjusted growth (4.60 vs 2.07 bp); despite a smaller raw edge (+0.032 vs +0.055/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi 0.014); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi 0.005); failure: MIN offense suppressed (<= 2 goals)
- **Rieger Lorenz: 1+ goals YES** — thesis: MIN offense succeeds (4+ goals); alternative: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes; why: second expression of the same thesis: KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes has the higher standalone adjusted growth (4.60 vs 4.25 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it -0.005); they share one thesis budget; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.004); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi -0.005); KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no: MOSTLY_INDEPENDENT (phi -0.007); failure: MIN offense suppressed (<= 2 goals)
- **Adam Jiricek: 1+ assists NO** — thesis: STL offense suppressed (<= 2 goals); alternative: KXNHLPTS-26OCT15STLMIN-STLAJIRICEK36-1|no; why: higher confidence-adjusted growth (1.82 vs 0.00 bp); despite a smaller raw edge (+0.050 vs +0.068/contract); evidence EVIDENCE_MIXED vs CALIBRATION_WARNING; alternative not eligible: confidence-adjusted EV <= 0; relationships: KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: MOSTLY_INDEPENDENT (phi -0.038); KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: MOSTLY_INDEPENDENT (phi 0.005); KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: STL offense succeeds (4+ goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11, balanced shots · high event (8+) · decided (2+) 0.10.
- thesis MIN:OFFENSE_4PLUS (p 0.4345): highest fidelity KXNHLAST-26OCT15STLMIN-MINRHARTMAN38-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis STL:SUPPRESSED (p 0.4256): highest fidelity KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no [DIRECT], best adjusted EV KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no (same contract)
- thesis STL:OFFENSE_4PLUS (p 0.3552): highest fidelity KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes [FRAGILE], best adjusted EV KXNHLGOAL-26OCT15STLMIN-STLRTHOMAS18-1|yes (same contract)
- KXNHLGOAL-26OCT15STLMIN-STLRJOHNSTON49-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 88% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:SUPPRESSED (p 0.4256, phi -0.141)
- KXNHLGOAL-26OCT15STLMIN-MINRHARTMAN38-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 67% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.209)
- KXNHLGOAL-26OCT15STLMIN-MINRLORENZ61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 80% of the draws where the thesis happens; fragile player expression; opposing: failure thesis MIN:SUPPRESSED (p 0.3426, phi -0.153)
- KXNHLAST-26OCT15STLMIN-STLAJIRICEK36-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; family MIXED; loses 11% of the draws where the thesis happens; fragile player expression; opposing: failure thesis STL:OFFENSE_4PLUS (p 0.3552, phi -0.203)

portfolios: A EV +2.29 (adj +0.81) on $13.80, P(profit) 0.5051, adj growth 7.3 bp · B EV +1.53 (adj +0.76) on $9.53, P(profit) 0.3877, adj growth 7.2 bp · C EV +1.15 (adj +0.49) on $12.15, P(profit) 0.3822, adj growth 4.5 bp · R EV +0.41 (adj +0.27) on $1.00, P(profit) 0.0754, adj growth 9.0 bp

## UTA @ EDM  ·  10000 joint draws  ·  452 bet sides mapped, 10 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.524 / away 0.475

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
| Alex Formenton: 1+ goals YES | 16 | 0.217 | 0.193 | +0.047 | +0.023 | $2.45 | FUNDED_RESEARCH | $1 | EDM:OFFENSE_4PLUS | FRAGILE (0.30) | EVIDENCE_STRONGER | D |
| Connor McDavid: 1+ assists NO | 32 | 0.452 | 0.363 | +0.117 | +0.028 | $4.70 | SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED | $0 | EDM:SUPPRESSED | DIRECT (0.70) | EVIDENCE_MIXED | D |
| Mattias Ekholm: 1+ goals YES | 9 | 0.129 | 0.111 | +0.033 | +0.015 | $1.48 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.19) | EVIDENCE_STRONGER | D |
| Vasily Podkolzin: 1+ goals YES | 30 | 0.338 | 0.327 | +0.023 | +0.013 | $2.83 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | EDM:OFFENSE_4PLUS | FRAGILE (0.46) | EVIDENCE_STRONGER | D |
- **Alex Formenton: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (8.26 vs 5.31 bp); despite a smaller raw edge (+0.047 vs +0.100/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.009); failure: EDM offense suppressed (<= 2 goals)
- **Connor McDavid: 1+ assists NO** — thesis: EDM offense suppressed (<= 2 goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no; why: higher confidence-adjusted growth (7.49 vs 4.65 bp); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.06); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: INTENTIONAL_DIVERSIFIER (phi -0.253); failure: EDM offense succeeds (4+ goals)
- **Mattias Ekholm: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes; why: higher confidence-adjusted growth (5.48 vs 5.31 bp); despite a smaller raw edge (+0.033 vs +0.100/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi 0.006); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.111); KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: EDM offense suppressed (<= 2 goals)
- **Vasily Podkolzin: 1+ goals YES** — thesis: EDM offense succeeds (4+ goals); alternative: KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes; why: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.46 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: MOSTLY_INDEPENDENT (phi -0.009); KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: INTENTIONAL_DIVERSIFIER (phi -0.253); KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: MOSTLY_INDEPENDENT (phi -0.007); failure: EDM offense suppressed (<= 2 goals)

**Review**: scripts balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · high event (8+) · decided (2+) 0.11, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.11.
- thesis EDM:SUPPRESSED (p 0.2932): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-2|no [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no — the best-adjusted-EV expression is kept: the higher-fidelity one is not within one tick of its adjusted EV or is not more reliable / higher fidelity on the preference order
- thesis EDM:OFFENSE_4PLUS (p 0.4964): highest fidelity KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes [DIRECT], best adjusted EV KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes (same contract)
- thesis UTA:SUPPRESSED (p 0.3988): highest fidelity - [-], best adjusted EV - — no eligible expression
- KXNHLGOAL-26OCT15UTAEDM-EDMAFORMENTON26-1|yes: FUNDED_RESEARCH; family TRUSTED; loses 70% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.19)
- KXNHLAST-26OCT15UTAEDM-EDMCMCDAVID97-1|no: SHADOW_ONLY — CALIBRATION_WARNING_UNCORROBORATED; LARGE_MARKET_DISAGREEMENT_UNCORROBORATED; family MIXED; loses 30% of the draws where the thesis happens; LARGE MARKET DISAGREEMENT 13.7 pts; fragile player expression; opposing: failure thesis EDM:OFFENSE_4PLUS (p 0.4964, phi -0.318)
- KXNHLGOAL-26OCT15UTAEDM-EDMMEKHOLM14-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 81% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.154)
- KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 54% of the draws where the thesis happens; fragile player expression; opposing: failure thesis EDM:SUPPRESSED (p 0.2932, phi -0.241)
- override: Player prop expression KXNHLGOAL-26OCT15UTAEDM-EDMVPODKOLZIN92-1|yes selected over player prop KXNHLAST-26OCT15UTAEDM-EDMMEKHOLM14-1|yes because adjusted EV differs by only 1.0 pts while thesis capture is 0.46 vs 0.51 (FRAGILE vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +3.35 (adj +0.75) on $13.80, P(profit) 0.6694, adj growth 7.1 bp · B EV +3.05 (adj +1.07) on $11.46, P(profit) 0.6516, adj growth 10.2 bp · C EV +3.12 (adj +0.72) on $9.06, P(profit) 0.6898, adj growth 6.8 bp · R EV +0.28 (adj +0.14) on $1.00, P(profit) 0.2168, adj growth 5.0 bp

## CGY @ VGK  ·  10000 joint draws  ·  412 bet sides mapped, 12 +EV candidates, 4 on card

sportsbook moneyline consensus (5 books): home 0.726 / away 0.274

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
| Mitch Marner: 1+ goals NO | 68 | 0.742 | 0.725 | +0.046 | +0.030 | $7.04 | FUNDED_RESEARCH | $2 | VGK:SUPPRESSED | DIRECT (0.87) | EVIDENCE_STRONGER | D |
| Vegas wins by over 2.5 goals NO | 61 | 0.690 | 0.648 | +0.064 | +0.021 | $3.36 | FUNDED_RESEARCH | $1 | GAME:TIGHT | STRUCTURAL (1.00) | EVIDENCE_MIXED | D |
| Aydar Suniev: 1+ goals YES | 15 | 0.190 | 0.174 | +0.031 | +0.015 | $1.34 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | CGY:OFFENSE_4PLUS | FRAGILE (0.31) | EVIDENCE_STRONGER | D |
| Jack Eichel: 1+ goals NO | 63 | 0.675 | 0.663 | +0.029 | +0.017 | $3.86 | SHADOW_ONLY — PLAYER_PROP_GAME_CAP | $0 | VGK:SUPPRESSED | DIRECT (0.84) | EVIDENCE_STRONGER | D |
- **Mitch Marner: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: higher confidence-adjusted growth (9.18 vs 4.11 bp); despite a smaller raw edge (+0.046 vs +0.064/contract); evidence EVIDENCE_STRONGER vs EVIDENCE_MIXED; relationships: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.001); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.028); failure: VGK offense succeeds (4+ goals)
- **Vegas wins by over 2.5 goals NO** — thesis: tight game (one-goal final or OT); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK2|no; why: higher confidence-adjusted growth (4.11 vs 3.27 bp); wins across more scripts (relative breadth 1.025 vs 0.85); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi 0.146); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi 0.142); failure: VGK wins by 2+
- **Aydar Suniev: 1+ goals YES** — thesis: CGY offense succeeds (4+ goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: second expression of the same thesis: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no has the higher standalone adjusted growth (4.11 vs 3.49 bp) and is also on the card; the joint optimum keeps both because their outcomes are nearly independent (phi with it +0.133); they share one thesis budget; relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.001); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.133); KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: MOSTLY_INDEPENDENT (phi -0.012); failure: CGY offense suppressed (<= 2 goals)
- **Jack Eichel: 1+ goals NO** — thesis: VGK offense suppressed (<= 2 goals); alternative: KXNHLSPREAD-26OCT15CGYVGK-VGK3|no; why: Player prop expression KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.84 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability); relationships: KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: MOSTLY_INDEPENDENT (phi -0.028); KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: MOSTLY_INDEPENDENT (phi 0.142); KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: MOSTLY_INDEPENDENT (phi -0.012); failure: VGK offense succeeds (4+ goals)

**Review**: scripts VGK shot control · normal event (5-7) · decided (2+) 0.13, balanced shots · normal event (5-7) · decided (2+) 0.12, balanced shots · normal event (5-7) · tight (1-goal/OT) 0.09.
- thesis VGK:SUPPRESSED (p 0.2919): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- thesis GAME:TIGHT (p 0.401): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [STRUCTURAL], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- thesis CGY:OFFENSE_4PLUS (p 0.2574): highest fidelity KXNHLSPREAD-26OCT15CGYVGK-VGK3|no [DIRECT], best adjusted EV KXNHLSPREAD-26OCT15CGYVGK-VGK3|no (same contract)
- KXNHLGOAL-26OCT15CGYVGK-VGKMMARNER93-1|no: FUNDED_RESEARCH; family TRUSTED; loses 13% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.194)
- KXNHLSPREAD-26OCT15CGYVGK-VGK3|no: FUNDED_RESEARCH; family MIXED; cannot lose if the thesis happens (settles from it); opposing: failure thesis VGK:WINS_BY_2PLUS (p 0.4414, phi -0.754)
- KXNHLGOAL-26OCT15CGYVGK-CGYASUNIEV61-1|yes: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 69% of the draws where the thesis happens; fragile player expression; opposing: failure thesis CGY:SUPPRESSED (p 0.5368, phi -0.22)
- KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no: SHADOW_ONLY — PLAYER_PROP_GAME_CAP; family TRUSTED; loses 16% of the draws where the thesis happens; fragile player expression; opposing: failure thesis VGK:OFFENSE_4PLUS (p 0.5032, phi -0.235)
- override: Player prop expression KXNHLGOAL-26OCT15CGYVGK-VGKJEICHEL9-1|no selected over player prop KXNHLAST-26OCT15CGYVGK-VGKTCONNELLY24-1|no because adjusted EV differs by only 0.7 pts while thesis capture is 0.84 vs 0.89 (DIRECT vs DIRECT; reliability EVIDENCE_STRONGER vs EVIDENCE_MIXED; decided on family reliability)

portfolios: A EV +2.34 (adj +0.48) on $13.80, P(profit) 0.5678, adj growth 4.4 bp · B EV +1.24 (adj +0.64) on $15.60, P(profit) 0.5689, adj growth 6.1 bp · C EV +1.22 (adj +0.38) on $17.14, P(profit) 0.6779, adj growth 3.6 bp · R EV +0.23 (adj +0.12) on $3.00, P(profit) 0.5414, adj growth 4.6 bp
equivalent contracts collapsed: KXNHLGAME-26OCT15CGYVGK-VGK|no == KXNHLGAME-26OCT15CGYVGK-CGY|yes

_RESEARCH_ONLY thesis card: B stakes are optimiser suggestions for a nominal bankroll; R (FUNDED_RESEARCH) stakes are whole-dollar research stakes under research governance. Nothing is placed or routed. Every recommended bet is +EV at its executable ask under the model AND the confidence-adjusted probability; the card is emitted only when the completion gate passes._
