# Thesis-card postmortem — RESEARCH_ONLY

evaluated 2026-10-02T13:00:00Z · thesis-postmortem-2.0 · rows (all generations) 416

All P/L below is **FINAL_CARD_UNIQUE**: per game, only the decisions of the ONE latest complete pregame thesis-card snapshot. Repeated generations are in ALL_PROSPECTIVE_DECISIONS (calibration research, no P/L).

## Slate 2026-10-02: **PARTIAL — 0/5 games evaluated**

scheduled 5 · final 0 · settled 0 · events ingested 0 · thesis-evaluated 0 · final_card_complete False · postmortem_complete False

missing / pending:
- 2026020017: game not started: the snapshot shown is the latest so far, not yet final
- 2026020018: game not started: the snapshot shown is the latest so far, not yet final
- 2026020019: game not started: the snapshot shown is the latest so far, not yet final
- 2026020020: game not started: the snapshot shown is the latest so far, not yet final
- 2026020021: game not started: the snapshot shown is the latest so far, not yet final

> INTERIM (PARTIAL — 0/5 games evaluated): covers evaluated games only; NOT the slate's final ROI

invariant final_card_n 0 <= sum(game card caps) 0: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 0 | 0.00 | +0.00 | - |
| FUNDED research stakes | - | - | - | no research layer on these decisions (logged before nhl-card-1.1) |

- THESIS: 0 distinct theses, hit rate - vs mean p - (Brier -)
- EXPRESSION: thesis right + won 0 · right + lost 0 · wrong + won 0 · wrong + lost 0
  - by fidelity: 
  - broad vs player: 
- PRICE: mean CLV - (n 0), mean adjusted EV at entry -
- MODEL: Brier raw - · adjusted - · Kalshi mid - (n 0)
- PORTFOLIO: funded 0 · shadow on card 0 · mean |phi| among card pairs - · mean largest thesis share -
- GOVERNANCE: funded player props 0 · shadow player props 0 · large-disagreement gates 0 · overrides 0


#### game 2026020017 NYR @ DET: NOT_STARTED · snapshot snap-5401311ea3ca2f25fd25 @ 2026-10-02T12:40:45Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02NYRDET-DETNDANIELSON29-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.40 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT02NYRDET-DETMSEIDER53-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.74 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT02NYRDET-NYRSDURZI5-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.74 | - | - | - | DIRECT | - | - |

#### game 2026020018 WSH @ CAR: NOT_STARTED · snapshot snap-5401311ea3ca2f25fd25 @ 2026-10-02T12:40:45Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02WSHCAR-CARWCARRIER28-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 5.55 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT02WSHCAR-WSHAPROTAS21-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 6.66 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT02WSHCAR-WSHATUCH89-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.74 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT02WSHCAR-WSHJSOURDIF34-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.73 | - | - | - | FRAGILE | - | - |

#### game 2026020019 BOS @ WPG: NOT_STARTED · snapshot snap-5401311ea3ca2f25fd25 @ 2026-10-02T12:40:45Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT02BOSWPG-BOSELINDHOLM28-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 7.08 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT02BOSWPG-WPGCPERFETTI91-1|no | LEGACY_NO_RESEARCH_LAYER | - | 17.73 | - | - | - | DIRECT | - | - |
| KXNHLAST-26OCT02BOSWPG-BOSJPETERKA10-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.74 | - | - | - | DIRECT | - | - |

#### game 2026020020 STL @ DAL: NOT_STARTED · snapshot snap-5401311ea3ca2f25fd25 @ 2026-10-02T12:40:45Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGAME-26OCT02STLDAL-DAL|no | LEGACY_NO_RESEARCH_LAYER | - | 7.03 | - | - | - | STRUCTURAL | - | - |
| KXNHLSPREAD-26OCT02STLDAL-DAL2|no | LEGACY_NO_RESEARCH_LAYER | - | 4.26 | - | - | - | STRUCTURAL | - | - |
| KXNHLSPREAD-26OCT02STLDAL-DAL3|no | LEGACY_NO_RESEARCH_LAYER | - | 3.02 | - | - | - | STRUCTURAL | - | - |

#### game 2026020021 ANA @ VGK: NOT_STARTED · snapshot snap-5401311ea3ca2f25fd25 @ 2026-10-02T12:40:45Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHL3PSPREAD-26OCT02ANAVGK-VGK2|no | LEGACY_NO_RESEARCH_LAYER | - | 17.60 | - | - | - | DIRECT | - | - |

## Slate 2026-10-01: **PARTIAL — 3/8 games evaluated**

scheduled 8 · final 3 · settled 3 · events ingested 4 · thesis-evaluated 3 · final_card_complete False · postmortem_complete False

missing / pending:
- 2026020012: no official FINAL result yet
- 2026020013: no official FINAL result yet
- 2026020014: no official FINAL result yet
- 2026020015: no official FINAL result yet
- 2026020016: no official FINAL result yet

> INTERIM (PARTIAL — 3/8 games evaluated): covers evaluated games only; NOT the slate's final ROI

invariant final_card_n 11 <= sum(game card caps) 12: OK

### FINAL_CARD_UNIQUE

| view | bets | stake | P/L | ROI |
|---|---:|---:|---:|---:|
| nominal optimiser card (B) | 11 | 53.71 | +4.14 | 0.077 |
| FUNDED research stakes | - | - | - | no research layer on these decisions (logged before nhl-card-1.1) |

- THESIS: 7 distinct theses, hit rate 0.429 vs mean p 0.408 (Brier 0.204)
- EXPRESSION: thesis right + won 3 · right + lost 1 · wrong + won 3 · wrong + lost 4
  - by fidelity: DIRECT 4/4; FRAGILE 0/5; STRUCTURAL 2/2
  - broad vs player: BROAD 2/2 (P/L +4.11); FRAGILE_PLAYER 4/9 (P/L +0.03)
- PRICE: mean CLV -0.0064 (n 11), mean adjusted EV at entry 0.0228
- MODEL: Brier raw 0.0486 · adjusted 0.0618 · Kalshi mid 0.0729 (n 11)
- PORTFOLIO: funded 0 · shadow on card 0 · mean |phi| among card pairs 0.075 · mean largest thesis share 0.496
- GOVERNANCE: funded player props 0 · shadow player props 0 · large-disagreement gates 0 · overrides 0


#### game 2026020009 PHI @ NJD: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01PHINJ-PHINACCIARI52-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.33 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0100 | -2.33 |
| KXNHLGOAL-26OCT01PHINJ-PHISCOUTURIER14-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.25 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.25 |
| KXNHLGOAL-26OCT01PHINJ-NJDMERCER91-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.81 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -2.81 |
| KXNHLGOAL-26OCT01PHINJ-NJSNOESEN11-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 1.92 | False | False | THESIS_WRONG_EXPRESSION_LOST | FRAGILE | -0.0050 | -1.92 |

#### game 2026020010 TBL @ NYR: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT01TBNYR-TBJCARLSON74-1|no | LEGACY_NO_RESEARCH_LAYER | - | 9.14 | True | True | THESIS_RIGHT_EXPRESSION_WON | DIRECT | -0.0050 | 6.97 |
| KXNHLSPREAD-26OCT01TBNYR-TB3|no | LEGACY_NO_RESEARCH_LAYER | - | 9.14 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 2.54 |
| KXNHLSPREAD-26OCT01TBNYR-TB2|no | LEGACY_NO_RESEARCH_LAYER | - | 3.28 | True | True | THESIS_RIGHT_EXPRESSION_WON | STRUCTURAL | -0.0050 | 1.57 |

#### game 2026020011 BUF @ CBJ: EVALUATED · snapshot snap-d3683f7e5e8476920334 @ 2026-10-01T22:57:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01BUFCBJ-CBJCCOYLE3-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 4.65 | False | True | THESIS_RIGHT_EXPRESSION_LOST | FRAGILE | -0.0050 | -4.65 |
| KXNHLGOAL-26OCT01BUFCBJ-CBJCGARLAND83-1|no | LEGACY_NO_RESEARCH_LAYER | - | 8.98 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 1.83 |
| KXNHLAST-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 4.78 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0150 | 2.97 |
| KXNHLGOAL-26OCT01BUFCBJ-BUFTTHOMPSON72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 4.43 | True | False | THESIS_WRONG_EXPRESSION_WON | DIRECT | -0.0050 | 2.22 |

#### game 2026020012 MIN @ NSH: NOT_FINAL · snapshot snap-0471fa40e0e6b13c7166 @ 2026-10-01T23:47:02Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01MINNSH-MINRHARTMAN38-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 4.30 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT01MINNSH-MINJSPURGEON46-1|no | LEGACY_NO_RESEARCH_LAYER | - | 13.84 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT01MINNSH-NSHMBOURQUE22-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 2.58 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT01MINNSH-NSHROREILLY90-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.29 | - | - | - | FRAGILE | - | - |

#### game 2026020013 CHI @ UTA: NOT_FINAL · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01CHIUTA-CHIRGREENE20-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 7.01 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT01CHIUTA-UTALCROUSE67-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 6.56 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT01CHIUTA-UTAVTROCHECK16-1|no | LEGACY_NO_RESEARCH_LAYER | - | 18.55 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT01CHIUTA-UTAALEE72-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 5.44 | - | - | - | FRAGILE | - | - |

#### game 2026020014 SEA @ CGY: NOT_FINAL · snapshot snap-7c5f74c436d5f9a561e6 @ 2026-10-02T00:37:04Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01SEACGY-SEABMONTOUR62-1|no | LEGACY_NO_RESEARCH_LAYER | - | 15.33 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT01SEACGY-SEAFGAUDREAU89-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.90 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT01SEACGY-CGYAKLAPKA43-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 3.17 | - | - | - | FRAGILE | - | - |
| KXNHLGOAL-26OCT01SEACGY-CGYMTSYPLAKOV72-1|no | LEGACY_NO_RESEARCH_LAYER | - | 15.33 | - | - | - | DIRECT | - | - |

#### game 2026020015 EDM @ VAN: NOT_FINAL · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-1|no | LEGACY_NO_RESEARCH_LAYER | - | 8.55 | - | - | - | DIRECT | - | - |
| KXNHLGOAL-26OCT01EDMVAN-VANDOCONNOR18-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 8.07 | - | - | - | FRAGILE | - | - |
| KXNHLAST-26OCT01EDMVAN-EDMCMCDAVID97-2|no | LEGACY_NO_RESEARCH_LAYER | - | 19.64 | - | - | - | DIRECT | - | - |
| KXNHLSPREAD-26OCT01EDMVAN-EDM3|no | LEGACY_NO_RESEARCH_LAYER | - | 13.74 | - | - | - | STRUCTURAL | - | - |

#### game 2026020016 FLA @ SJS: NOT_FINAL · snapshot snap-87bced70acd8e8ac4de4 @ 2026-10-02T01:27:03Z

| bet | status | research $ | nominal $ | won | thesis hit | expression | fidelity | CLV | P/L nominal |
|---|---|---:|---:|---|---|---|---|---:|---:|
| KXNHLGOAL-26OCT01FLASJ-SJKSHERWOOD44-1|yes | LEGACY_NO_RESEARCH_LAYER | - | 10.14 | - | - | - | FRAGILE | - | - |
| KXNHLSPREAD-26OCT01FLASJ-FLA3|no | LEGACY_NO_RESEARCH_LAYER | - | 19.93 | - | - | - | STRUCTURAL | - | - |
| KXNHLGOAL-26OCT01FLASJ-FLASREINHART13-1|no | LEGACY_NO_RESEARCH_LAYER | - | 19.93 | - | - | - | DIRECT | - | - |

## ALL_PROSPECTIVE_DECISIONS (calibration research; no P/L)

416 scored rows = 61 unique logical wagers (repeat factor 6.82). every scored pregame decision of every generation (repeated observations of one wager are NOT independent; no P/L here).

| family | rows | unique | Brier all rows | Brier last obs | adjusted | Kalshi mid |
|---|---:|---:|---:|---:|---:|---:|
| first_goal | 1 | 1 | 0.0011 | 0.0011 | 0.0010 | 0.0009 |
| game_spread | 57 | 7 | 0.2267 | 0.2023 | 0.2277 | 0.2555 |
| game_total | 3 | 1 | 0.2283 | 0.2283 | 0.2615 | 0.2970 |
| game_winner | 34 | 5 | 0.2161 | 0.2056 | 0.2258 | 0.2439 |
| player_assists | 92 | 10 | 0.2039 | 0.2375 | 0.2219 | 0.2147 |
| player_goals | 188 | 29 | 0.0765 | 0.0712 | 0.0720 | 0.0759 |
| player_points | 14 | 1 | 0.1141 | 0.1122 | 0.2500 | 0.3080 |
| team_total | 27 | 7 | 0.1903 | 0.2281 | 0.2512 | 0.2770 |

_Prospective thesis-card evidence. All P/L is FINAL_CARD_UNIQUE (one latest complete pregame snapshot per game). THESIS / EXPRESSION / PRICE / MODEL / PORTFOLIO / GOVERNANCE are kept separate: a right thesis expressed through a contract that lost is not a wrong prediction. A handful of games proves nothing; never tune to one slate._
