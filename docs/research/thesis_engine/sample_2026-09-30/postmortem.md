# Thesis-card postmortem — RESEARCH_ONLY

evaluated 2026-10-01T05:30:00Z · games 2 · rows (all runs) 27

## Final card (chosen bets, last pregame run)

```
{
 "n": 8,
 "won": 3,
 "expression_results": {
  "THESIS_RIGHT_EXPRESSION_WON": 2,
  "THESIS_RIGHT_EXPRESSION_LOST": 2,
  "THESIS_WRONG_EXPRESSION_LOST": 3,
  "THESIS_WRONG_EXPRESSION_WON": 1
 },
 "thesis_hit_rate": 0.5,
 "mean_clv": -0.0063,
 "n_clv": 8,
 "brier_model": 0.0917,
 "brier_adjusted": 0.1,
 "brier_kalshi_mid": 0.1033,
 "realized_profit": -12.42,
 "stake": 92.48
}
```

## Final shortlist (all shortlisted, last pregame run)

```
{
 "n": 27,
 "won": 14,
 "expression_results": {
  "THESIS_RIGHT_EXPRESSION_WON": 10,
  "THESIS_RIGHT_EXPRESSION_LOST": 3,
  "THESIS_WRONG_EXPRESSION_LOST": 10,
  "THESIS_WRONG_EXPRESSION_WON": 4
 },
 "thesis_hit_rate": 0.481,
 "mean_clv": -0.0056,
 "n_clv": 27,
 "brier_model": 0.0974,
 "brier_adjusted": 0.1027,
 "brier_kalshi_mid": 0.1072,
 "realized_profit": -12.42,
 "stake": 92.48
}
```

## game 2026020006: realised script PIT shot control · normal event (5-7) · decided (2+)

portfolio: {"n_bets": 4, "stake": 44.24, "realized_profit": -16.26, "expected_profit": 7.89, "realized_vs_simulated": "<= p25", "largest_thesis_share": 0.452, "n_theses": 3, "theses_with_multiple_losses": ["PIT:OFFENSE_4PLUS"], "multiple_losses_on_one_thesis": [{"thesis": "PIT:OFFENSE_4PLUS", "thesis_happened": true, "n_lost": 2, "loss": 16.57, "reading": "thesis happened but its expressions missed: expression risk, not a thesis error"}]}

| bet | chosen | stake | won | thesis | thesis hit | expression | model P(bet|thesis outcome) | model P(win|realised script) | CLV | P/L |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|
| KXNHLGOAL-26SEP30PITPHI-PHIPMARTONE94-1|no | True | 20.0 | True | PHI:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8841 | 0.7898 | -0.005 | 7.98 |
| KXNHLGOAL-26SEP30PITPHI-PITCDEWAR19-1|yes | True | 7.06 | False | PIT:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.2573 | 0.1792 | -0.005 | -7.06 |
| KXNHLGOAL-26SEP30PITPHI-PHISCOUTURIER14-1|yes | True | 7.67 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1107 | 0.2197 | -0.005 | -7.67 |
| KXNHLGOAL-26SEP30PITPHI-PHIJDRYSDALE9-1|no | False | 0.0 | True | PHI:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9615 | 0.9218 | 0.0 | None |
| KXNHLGOAL-26SEP30PITPHI-PITRRAKELL67-1|yes | True | 9.51 | False | PIT:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.4947 | 0.3208 | -0.005 | -9.51 |
| KXNHLGOAL-26SEP30PITPHI-PHICDVORAK22-1|yes | False | 0.0 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1559 | 0.1954 | -0.005 | None |
| KXNHLGOAL-26SEP30PITPHI-PITESODERBLOM25-1|yes | False | 0.0 | False | PIT:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_LOST | 0.2049 | 0.1307 | -0.005 | None |
| KXNHLGOAL-26SEP30PITPHI-PITFHALLANDER11-1|yes | False | 0.0 | True | PIT:OFFENSE_4PLUS | True | THESIS_RIGHT_EXPRESSION_WON | 0.2222 | 0.1334 | -0.01 | None |
| KXNHLGOAL-26SEP30PITPHI-PHICGRUNDSTROM91-1|yes | False | 0.0 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0875 | 0.1348 | -0.005 | None |
| KXNHLGOAL-26SEP30PITPHI-PITKLETANG58-1|no | False | 0.0 | True | PIT:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_WON | 0.9085 | 0.934 | 0.0 | None |
| KXNHLAST-26SEP30PITPHI-PITSCROSBY87-1|no | False | 0.0 | False | PIT:SUPPRESSED | False | THESIS_WRONG_EXPRESSION_LOST | 0.5005 | 0.6321 | -0.005 | None |
| KXNHLGOAL-26SEP30PITPHI-PHINACCIARI52-1|yes | False | 0.0 | False | PHI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0877 | 0.1213 | -0.005 | None |

## game 2026020008: realised script balanced shots · low event (<=4) · tight (1-goal/OT)

portfolio: {"n_bets": 4, "stake": 48.24, "realized_profit": 3.84, "expected_profit": 8.99, "realized_vs_simulated": "<= p75", "largest_thesis_share": 0.358, "n_theses": 4, "theses_with_multiple_losses": [], "multiple_losses_on_one_thesis": []}

| bet | chosen | stake | won | thesis | thesis hit | expression | model P(bet|thesis outcome) | model P(win|realised script) | CLV | P/L |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|
| KXNHLGOAL-26SEP30NYITOR-TORTBLUEGER73-1|yes | True | 6.27 | False | TOR:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0887 | 0.0685 | -0.005 | -6.27 |
| KXNHLAST-26SEP30NYITOR-TORAMATTHEWS34-1|no | True | 17.26 | True | TOR:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8263 | 0.85 | -0.005 | 10.72 |
| KXNHLGAME-26SEP30NYITOR-TOR|no | True | 12.48 | False | NYI:WINS | False | THESIS_WRONG_EXPRESSION_LOST | 0.0 | 0.5204 | -0.005 | -12.48 |
| KXNHLAST-26SEP30NYITOR-TORDRADDYSH43-2|no | False | 0.0 | True | TOR:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.9934 | 0.9944 | -0.01 | None |
| KXNHLSAVE-26SEP30NYITOR-NYIISOROKIN30-25|no | True | 12.23 | True | NYI:NET_LOW_VOLUME | False | THESIS_WRONG_EXPRESSION_WON | 0.2715 | 0.4722 | -0.015 | 11.87 |
| KXNHLSPREAD-26SEP30NYITOR-TOR2|no | False | 0.0 | True | NYI:WINS | False | THESIS_WRONG_EXPRESSION_WON | 0.4663 | 1.0 | -0.005 | None |
| KXNHLAST-26SEP30NYITOR-NYIMMACCELLI63-1|no | False | 0.0 | True | NYI:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8856 | 0.8907 | -0.005 | None |
| KXNHLAST-26SEP30NYITOR-NYISHOLMSTROM92-1|yes | False | 0.0 | False | NYI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.2295 | 0.1537 | -0.01 | None |
| KXNHLSPREAD-26SEP30NYITOR-TOR3|no | False | 0.0 | True | NYI:WINS | False | THESIS_WRONG_EXPRESSION_WON | 0.6811 | 1.0 | -0.005 | None |
| KXNHLGOAL-26SEP30NYITOR-NYIBSCHENN10-1|yes | False | 0.0 | False | NYI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1664 | 0.1074 | -0.005 | None |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR5|no | False | 0.0 | True | TOR:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 1.0 | -0.005 | None |
| KXNHLGOAL-26SEP30NYITOR-NYIJPAGEAU44-1|yes | False | 0.0 | False | NYI:OFFENSE_4PLUS | False | THESIS_WRONG_EXPRESSION_LOST | 0.1148 | 0.1 | -0.005 | None |
| KXNHLAST-26SEP30NYITOR-TORDRADDYSH43-1|no | False | 0.0 | True | TOR:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8376 | 0.8667 | -0.005 | None |
| KXNHLGOAL-26SEP30NYITOR-TORAMATTHEWS34-1|no | False | 0.0 | True | TOR:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 0.8235 | 0.7796 | -0.005 | None |
| KXNHLTEAMTOTAL-26SEP30NYITOR-TOR4|no | False | 0.0 | True | TOR:SUPPRESSED | True | THESIS_RIGHT_EXPRESSION_WON | 1.0 | 1.0 | -0.005 | None |

_Prospective thesis-card evidence. THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO results are kept separate on purpose: a right thesis expressed through a contract that lost is not a wrong prediction. A handful of games proves nothing; never tune to one slate._
