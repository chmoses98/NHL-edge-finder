# Kalshi NHL discovery summary

- discovered_at: `2026-11-12T22:55:04Z`  ontology: `2026.09.29.2`  requests: 158
- series enumerated: 16338; NHL series: 78; markets scanned: 3874

## Support states (coverage invariant)

| support | markets |
|---|---:|
| MODELABLE | 562 |
| BUILDABLE | 13 |
| RESEARCH | 2958 |
| UNMODELABLE | 286 |
| UNRESOLVED | 55 |

## NHL series

| series | family | support | fee | unopened | open | closed | settled | strike_types | parse |
|---|---|---|---|---:|---:|---:|---:|---|---|
| KXCANADACUP | season_champion | RESEARCH | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXCONNSMYTHE | season_awards | UNMODELABLE | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXESPYNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNBANHL | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNEXTTEAMNHL | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHL1P | period_winner | RESEARCH | quadratic/1 | 0 | 39 | 0 | 0 | structured | {'high': 39} |
| KXNHL1PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL1PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 26 | 0 | 0 | greater | {'high': 26} |
| KXNHL1PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 39 | 0 | 0 | greater | {'high': 39} |
| KXNHL1STTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2OT | game_multi_overtime | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2P | period_winner | RESEARCH | quadratic/1 | 0 | 39 | 0 | 0 | structured | {'high': 39} |
| KXNHL2PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL2PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 26 | 0 | 0 | greater | {'high': 26} |
| KXNHL2PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 39 | 0 | 0 | greater | {'high': 39} |
| KXNHL30COMEBACK | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3P | period_winner | RESEARCH | quadratic/1 | 0 | 39 | 0 | 0 | structured | {'high': 39} |
| KXNHL3PBTTS | period_btts | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHL3PSPREAD | period_spread | RESEARCH | quadratic/1 | 0 | 26 | 0 | 0 | greater | {'high': 26} |
| KXNHL3PTOTAL | period_total | RESEARCH | quadratic/1 | 0 | 39 | 0 | 0 | greater | {'high': 39} |
| KXNHL4NATIONS | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLADAMS | season_awards | UNMODELABLE | quadratic/1 | 0 | 32 | 0 | 0 | custom | {'low': 32} |
| KXNHLANYGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLAST | player_assists | RESEARCH | quadratic/1 | 0 | 289 | 0 | 0 | greater | {'high': 289} |
| KXNHLATLANTIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLCALDER | season_awards | UNMODELABLE | quadratic/1 | 0 | 40 | 0 | 0 | structured,custom | {'low': 40} |
| KXNHLCENTRAL | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLDRAFTPICK | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLDRAFTTOP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLEAST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLEXPANSION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 1 | 0 | 0 | None | {'low': 1} |
| KXNHLF10G | game_early_goal | RESEARCH | quadratic/1 | 0 | 13 | 0 | 0 | greater_or_equal | {'high': 13} |
| KXNHLFINALSEXACT | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLFIRSTGOAL | first_goal | RESEARCH | quadratic/1 | 0 | 355 | 0 | 0 | structured | {'high': 355} |
| KXNHLGAME | game_winner | MODELABLE | quadratic_with_maker_fees/1 | 0 | 94 | 0 | 0 | structured | {'high': 94} |
| KXNHLGOAL | player_goals | RESEARCH | quadratic/1 | 0 | 612 | 0 | 0 | greater | {'high': 612} |
| KXNHLHART | season_awards | UNMODELABLE | quadratic/1 | 0 | 39 | 0 | 0 | structured | {'low': 39} |
| KXNHLLINDSAY | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 38 | 0 | 0 | structured | {'low': 38} |
| KXNHLMENTION | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLMETROPOLITAN | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLMVP | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTGM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNEXTTEAM | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLNORRIS | season_awards | UNMODELABLE | quadratic/1 | 0 | 35 | 0 | 0 | structured | {'low': 35} |
| KXNHLOT | game_overtime | BUILDABLE | quadratic/1 | 0 | 13 | 0 | 0 | greater | {'high': 13} |
| KXNHLOVERTIME | game_overtime | BUILDABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPACIFIC | season_champion | RESEARCH | quadratic/1 | 0 | 8 | 0 | 0 | structured | {'low': 8} |
| KXNHLPLAYOFF | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPLAYOFFGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPRES | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLPRICE | non_hockey_or_office | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLPSEASONGOALS | UNRESOLVED | UNRESOLVED | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'low': 17} |
| KXNHLPTS | player_points | RESEARCH | quadratic/1 | 0 | 382 | 0 | 0 | greater | {'high': 382} |
| KXNHLRECORDWORST | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXNHLRETIRE | season_awards | UNMODELABLE | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLRICHARD | season_awards | UNMODELABLE | quadratic/1 | 0 | 44 | 0 | 0 | structured | {'low': 44} |
| KXNHLROSS | season_awards | UNMODELABLE | quadratic/1 | 0 | 47 | 0 | 0 | structured | {'low': 47} |
| KXNHLSAVE | goalie_saves | RESEARCH | quadratic/1 | 0 | 17 | 0 | 0 | greater | {'high': 17} |
| KXNHLSAVES | goalie_saves | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSEASONGOALS | season_player_stats | RESEARCH | quadratic/1 | 0 | 87 | 0 | 0 | greater,structured | {'low': 87} |
| KXNHLSEASONPPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 90 | 0 | 0 | greater | {'low': 90} |
| KXNHLSEASONPTS | season_player_stats | RESEARCH | quadratic/1 | 0 | 320 | 0 | 0 | greater_or_equal | {'low': 320} |
| KXNHLSERIES | playoff_series | RESEARCH | quadratic_with_maker_fees/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESGAMES | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESOT | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSCORE | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESSPREAD | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOAL | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSERIESTOTALGOALS | playoff_series | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLSPREAD | game_spread | MODELABLE | quadratic/1 | 0 | 104 | 0 | 0 | greater | {'high': 104} |
| KXNHLTEAMTOTAL | team_total | MODELABLE | quadratic/1 | 0 | 130 | 0 | 0 | greater | {'high': 130} |
| KXNHLTOTAL | game_total | MODELABLE | quadratic/1 | 0 | 234 | 0 | 0 | greater | {'high': 234} |
| KXNHLVEZINA | season_awards | UNMODELABLE | quadratic/1 | 0 | 48 | 0 | 0 | structured | {'low': 48} |
| KXNHLWEST | season_champion | RESEARCH | quadratic_with_maker_fees/1 | 0 | 16 | 0 | 0 | structured | {'low': 16} |
| KXNHLWINS | season_champion | RESEARCH | quadratic/1 | 0 | 0 | 0 | 0 |  | {} |
| KXNHLWSTREAK | season_champion | RESEARCH | quadratic/1 | 0 | 32 | 0 | 0 | structured | {'low': 32} |
| KXTEAMSINSC | season_champion | RESEARCH | quadratic/1 | 0 | 256 | 0 | 0 | custom | {'low': 256} |

## Title templates per series

### KXCANADACUP — Canada winning Stanley Cup
- (1) Will a Canadian team win the NAME® by the end of the # season?
- samples: KXCANADACUP-30
- sample fields: `{"ticker": "KXCANADACUP-30", "event_ticker": "KXCANADACUP-30", "market_type": "binary", "title": "Will a Canadian team win the Stanley Cup\u00ae by the end of the 2030 season?", "subtitle": "Before 2031", "yes_sub_title": "Before 2031", "no_sub_title": "Before 2031", "status": "active", "open_time": "2025-06-13T14:00:00Z", "close_time": "2030-06-30T03:59:00Z", "expected_expiration_time": "2030-06-30T14:00:00Z", "result": "", "rules_primary": "If a Canadian hockey team wins the Stanley Cup\u00ae after Issuance and before Jun 30, 2030, then the market resolves to Yes."}`

### KXCONNSMYTHE — Conn Smythe trophy

### KXESPYNHL — BEST NHL PLAYER‬

### KXNBANHL — NBA + NHL Champion Combo

### KXNEXTTEAMNHL — Next Team NHL

### KXNHL — Stanley Cup
- (30) NAME win the #-# NAME® Finals?
- (1) NAME. NAME win the #-# NAME® Finals?
- (1) Will Montréal Canadiens win the #-# NAME® Finals?
- samples: KXNHL-27-WSH, KXNHL-27-WPG, KXNHL-27-VGK, KXNHL-27-VAN, KXNHL-27-UTA, KXNHL-27-TOR
- sample fields: `{"ticker": "KXNHL-27-WSH", "event_ticker": "KXNHL-27", "market_type": "binary", "title": "Will Washington Capitals win the 2026-27 Stanley Cup\u00ae Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-06-15T03:40:00Z", "close_time": "2029-06-30T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals wins the 2026-27 Stanley Cup\u00ae Finals, then the marke`

### KXNHL1P — NHL 1st Period Winner
- (13) #st period tie
- (3) NAME wins the #st period
- (1) Seattle wins the #st period
- (1) Carolina wins the #st period
- (1) Vegas wins the #st period
- (1) Nashville wins the #st period
- (1) Vancouver wins the #st period
- (1) NAME R wins the #st period
- samples: KXNHL1P-26NOV14SEACAR-TIE, KXNHL1P-26NOV14SEACAR-SEA, KXNHL1P-26NOV14SEACAR-CAR, KXNHL1P-26NOV13NSHVGK-VGK, KXNHL1P-26NOV13NSHVGK-TIE, KXNHL1P-26NOV13NSHVGK-NSH
- sample fields: `{"ticker": "KXNHL1P-26NOV14SEACAR-TIE", "event_ticker": "KXNHL1P-26NOV14SEACAR", "market_type": "binary", "title": "1st period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If neither team wins the 1st period of the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, then the market resolves to`

### KXNHL1PBTTS — NHL Both Teams to Score in 1st Period

### KXNHL1PSPREAD — 1st Period Spread
- (3) NAME wins #st Period by over # goals
- (1) Seattle wins #st Period by over # goals
- (1) Carolina wins #st Period by over # goals
- (1) Vegas wins #st Period by over # goals
- (1) Nashville wins #st Period by over # goals
- (1) Vancouver wins #st Period by over # goals
- (1) NAME R wins #st Period by over # goals
- (1) NAME I wins #st Period by over # goals
- samples: KXNHL1PSPREAD-26NOV14SEACAR-SEA2, KXNHL1PSPREAD-26NOV14SEACAR-CAR2, KXNHL1PSPREAD-26NOV13NSHVGK-VGK2, KXNHL1PSPREAD-26NOV13NSHVGK-NSH2, KXNHL1PSPREAD-26NOV13NYRVAN-VAN2, KXNHL1PSPREAD-26NOV13NYRVAN-NYR2
- sample fields: `{"ticker": "KXNHL1PSPREAD-26NOV14SEACAR-SEA2", "event_ticker": "KXNHL1PSPREAD-26NOV14SEACAR", "market_type": "binary", "title": "Seattle wins 1st Period by over 1.5 goals", "yes_sub_title": "Seattle wins by over 1.5 goals", "no_sub_title": "Seattle wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If Seattle wins by more th`

### KXNHL1PTOTAL — NHL 1st Period Total
- (39) #st Period: Over # goals scored
- samples: KXNHL1PTOTAL-26NOV14SEACAR-3, KXNHL1PTOTAL-26NOV14SEACAR-2, KXNHL1PTOTAL-26NOV14SEACAR-1, KXNHL1PTOTAL-26NOV13NSHVGK-3, KXNHL1PTOTAL-26NOV13NSHVGK-2, KXNHL1PTOTAL-26NOV13NSHVGK-1
- sample fields: `{"ticker": "KXNHL1PTOTAL-26NOV14SEACAR-3", "event_ticker": "KXNHL1PTOTAL-26NOV14SEACAR", "market_type": "binary", "title": "1st Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 1st Period of the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, `

### KXNHL1STTEAM — All NHL First Team

### KXNHL2OT — NHL Double Overtime

### KXNHL2P — NHL 2nd Period Winner
- (13) #nd period tie
- (3) NAME wins the #nd period
- (1) Seattle wins the #nd period
- (1) Carolina wins the #nd period
- (1) Vegas wins the #nd period
- (1) Nashville wins the #nd period
- (1) Vancouver wins the #nd period
- (1) NAME R wins the #nd period
- samples: KXNHL2P-26NOV14SEACAR-TIE, KXNHL2P-26NOV14SEACAR-SEA, KXNHL2P-26NOV14SEACAR-CAR, KXNHL2P-26NOV13NSHVGK-VGK, KXNHL2P-26NOV13NSHVGK-TIE, KXNHL2P-26NOV13NSHVGK-NSH
- sample fields: `{"ticker": "KXNHL2P-26NOV14SEACAR-TIE", "event_ticker": "KXNHL2P-26NOV14SEACAR", "market_type": "binary", "title": "2nd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If neither team wins the 2nd period of the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, then the market resolves to`

### KXNHL2PBTTS — NHL Both Teams to Score in 2nd Period

### KXNHL2PSPREAD — 2nd Period Spread
- (3) NAME wins #nd Period by over # goals
- (1) Seattle wins #nd Period by over # goals
- (1) Carolina wins #nd Period by over # goals
- (1) Vegas wins #nd Period by over # goals
- (1) Nashville wins #nd Period by over # goals
- (1) Vancouver wins #nd Period by over # goals
- (1) NAME R wins #nd Period by over # goals
- (1) NAME I wins #nd Period by over # goals
- samples: KXNHL2PSPREAD-26NOV14SEACAR-SEA2, KXNHL2PSPREAD-26NOV14SEACAR-CAR2, KXNHL2PSPREAD-26NOV13NSHVGK-VGK2, KXNHL2PSPREAD-26NOV13NSHVGK-NSH2, KXNHL2PSPREAD-26NOV13NYRVAN-VAN2, KXNHL2PSPREAD-26NOV13NYRVAN-NYR2
- sample fields: `{"ticker": "KXNHL2PSPREAD-26NOV14SEACAR-SEA2", "event_ticker": "KXNHL2PSPREAD-26NOV14SEACAR", "market_type": "binary", "title": "Seattle wins 2nd Period by over 1.5 goals", "yes_sub_title": "Seattle wins by over 1.5 goals", "no_sub_title": "Seattle wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If Seattle wins by more th`

### KXNHL2PTOTAL — 2nd Period Total
- (39) #nd Period: Over # goals scored
- samples: KXNHL2PTOTAL-26NOV14SEACAR-3, KXNHL2PTOTAL-26NOV14SEACAR-2, KXNHL2PTOTAL-26NOV14SEACAR-1, KXNHL2PTOTAL-26NOV13NSHVGK-3, KXNHL2PTOTAL-26NOV13NSHVGK-2, KXNHL2PTOTAL-26NOV13NSHVGK-1
- sample fields: `{"ticker": "KXNHL2PTOTAL-26NOV14SEACAR-3", "event_ticker": "KXNHL2PTOTAL-26NOV14SEACAR", "market_type": "binary", "title": "2nd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 2nd Period of the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, `

### KXNHL30COMEBACK — NHL 3-0 Series Comeback

### KXNHL3P — NHL 3rd Period Winner
- (13) #rd period tie
- (3) NAME wins the #rd period
- (1) Seattle wins the #rd period
- (1) Carolina wins the #rd period
- (1) Vegas wins the #rd period
- (1) Nashville wins the #rd period
- (1) Vancouver wins the #rd period
- (1) NAME R wins the #rd period
- samples: KXNHL3P-26NOV14SEACAR-TIE, KXNHL3P-26NOV14SEACAR-SEA, KXNHL3P-26NOV14SEACAR-CAR, KXNHL3P-26NOV13NSHVGK-VGK, KXNHL3P-26NOV13NSHVGK-TIE, KXNHL3P-26NOV13NSHVGK-NSH
- sample fields: `{"ticker": "KXNHL3P-26NOV14SEACAR-TIE", "event_ticker": "KXNHL3P-26NOV14SEACAR", "market_type": "binary", "title": "3rd period tie", "yes_sub_title": "Tie", "no_sub_title": "Tie", "strike_type": "structured", "custom_strike": {"hockey_team": "570eabab-1214-4e50-a26c-880318169cce"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If neither team wins the 3rd period (excluding overtime) of the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, then t`

### KXNHL3PBTTS — NHL Both Teams to Score in 3rd Period

### KXNHL3PSPREAD — NHL 3rd Period Spread
- (3) NAME wins #rd Period by over # goals
- (1) Seattle wins #rd Period by over # goals
- (1) Carolina wins #rd Period by over # goals
- (1) Vegas wins #rd Period by over # goals
- (1) Nashville wins #rd Period by over # goals
- (1) Vancouver wins #rd Period by over # goals
- (1) NAME R wins #rd Period by over # goals
- (1) NAME I wins #rd Period by over # goals
- samples: KXNHL3PSPREAD-26NOV14SEACAR-SEA2, KXNHL3PSPREAD-26NOV14SEACAR-CAR2, KXNHL3PSPREAD-26NOV13NSHVGK-VGK2, KXNHL3PSPREAD-26NOV13NSHVGK-NSH2, KXNHL3PSPREAD-26NOV13NYRVAN-VAN2, KXNHL3PSPREAD-26NOV13NYRVAN-NYR2
- sample fields: `{"ticker": "KXNHL3PSPREAD-26NOV14SEACAR-SEA2", "event_ticker": "KXNHL3PSPREAD-26NOV14SEACAR", "market_type": "binary", "title": "Seattle wins 3rd Period by over 1.5 goals", "yes_sub_title": "Seattle wins by over 1.5 goals", "no_sub_title": "Seattle wins by over 1.5 goals", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If Seattle wins by more th`

### KXNHL3PTOTAL — 3rd Period Total
- (39) #rd Period: Over # goals scored
- samples: KXNHL3PTOTAL-26NOV14SEACAR-3, KXNHL3PTOTAL-26NOV14SEACAR-2, KXNHL3PTOTAL-26NOV14SEACAR-1, KXNHL3PTOTAL-26NOV13NSHVGK-3, KXNHL3PTOTAL-26NOV13NSHVGK-2, KXNHL3PTOTAL-26NOV13NSHVGK-1
- sample fields: `{"ticker": "KXNHL3PTOTAL-26NOV14SEACAR-3", "event_ticker": "KXNHL3PTOTAL-26NOV14SEACAR", "market_type": "binary", "title": "3rd Period: Over 2.5 goals scored", "yes_sub_title": "Over 2.5 goals", "no_sub_title": "Over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 2.5 goals in the 3rd Period of the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, `

### KXNHL4NATIONS — 4 nations face off

### KXNHLADAMS — NHL Jack Adams Award
- (29) NAME: NAME wins
- (1) NAME: Todd McLellan wins
- (1) NAME: Peter DeBoer wins
- (1) NAME: NAME. Louis wins
- samples: KXNHLADAMS-27-TMCL, KXNHLADAMS-27-TGRE, KXNHLADAMS-27-SKEE, KXNHLADAMS-27-SCAR, KXNHLADAMS-27-SARN, KXNHLADAMS-27-RWAR
- sample fields: `{"ticker": "KXNHLADAMS-27-TMCL", "event_ticker": "KXNHLADAMS-27", "market_type": "binary", "title": "Jack Adams Award: Todd McLellan wins", "subtitle": "::", "yes_sub_title": "Todd McLellan", "no_sub_title": "Todd McLellan", "strike_type": "custom", "custom_strike": {"Person": "Todd McLellan"}, "status": "active", "open_time": "2026-09-28T22:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Todd McLellan wins the NHL Jack Adams Award in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLANYGOAL — Pro Hockey Goalscorer

### KXNHLAST — Pro Hockey Assists
- (264) NAME: #+ assists
- (3) Nathan MacKinnon: #+ assists
- (2) Tony DeAngelo: #+ assists
- (2) MacKenzie Weegar: #+ assists
- (2) Mason McTavish: #+ assists
- (2) Connor McMichael: #+ assists
- (2) Alex DeBrincat: #+ assists
- (2) NAME D'Astous: #+ assists
- samples: KXNHLAST-26NOV12WPGDAL-DALJBENN14-2, KXNHLAST-26NOV12WPGDAL-DALJBENN14-1, KXNHLAST-26NOV12MINTOR-TORGMCKENNA92-1, KXNHLAST-26NOV12MINTOR-MINDYUROV22-1, KXNHLAST-26NOV12STLUTA-UTAMCARCONE53-1, KXNHLAST-26NOV12STLUTA-UTALCROUSE67-1
- sample fields: `{"ticker": "KXNHLAST-26NOV12WPGDAL-DALJBENN14-2", "event_ticker": "KXNHLAST-26NOV12WPGDAL", "market_type": "binary", "title": "Jamie Benn: 2+ assists", "yes_sub_title": "Jamie Benn: 2+", "no_sub_title": "Jamie Benn: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "6c86f425-5e2e-419f-81c4-376474d177b3", "hockey_team": "5cfee6b9-43ff-4dfa-8347-2b9de7ed51b6"}, "status": "active", "open_time": "2026-11-12T21:22:00Z", "close_time": "2026-11-15T01:00:00Z", "expected_expiration_time": "2026-11-13T07:00:00Z", "result": "", "rules_primary": "If Jamie Benn records `

### KXNHLATLANTIC — NHL Atlantic Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLATLANTIC-27-TOR, KXNHLATLANTIC-27-TB, KXNHLATLANTIC-27-OTT, KXNHLATLANTIC-27-MTL, KXNHLATLANTIC-27-FLA, KXNHLATLANTIC-27-DET
- sample fields: `{"ticker": "KXNHLATLANTIC-27-TOR", "event_ticker": "KXNHLATLANTIC-27", "market_type": "binary", "title": "Will the Toronto Maple Leafs win the Atlantic Division?", "yes_sub_title": "Toronto Maple Leafs", "no_sub_title": "Toronto Maple Leafs", "strike_type": "structured", "custom_strike": {"hockey_team": "f61f9daa-407b-4c46-96e8-feee19cd6f51"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Toronto Maple Leafs win the 2026-27 NHL Atlantic Division, then the `

### KXNHLCALDER — NHL Calder Memorial Trophy
- (36) NAME: NAME wins
- (1) NAME: Viggo Björck wins
- (1) NAME: NAME-Nygård wins
- (1) NAME: Gavin McKenna wins
- (1) NAME: Adam Engström wins
- samples: KXNHLCALDER-27-ZBUIUM24, KXNHLCALDER-27-VEKLUND, KXNHLCALDER-27-VBJORCK, KXNHLCALDER-27-TLINDSTEIN, KXNHLCALDER-27-TIGINLA, KXNHLCALDER-27-TCONNELLY
- sample fields: `{"ticker": "KXNHLCALDER-27-ZBUIUM24", "event_ticker": "KXNHLCALDER-27", "market_type": "binary", "title": "Calder Memorial Trophy: Zeev Buium wins", "subtitle": "::", "yes_sub_title": "Zeev Buium", "no_sub_title": "Zeev Buium", "strike_type": "structured", "custom_strike": {"hockey_player": "4e4ad45c-1cda-4e0b-89c3-4e6c27740027"}, "status": "active", "open_time": "2026-09-30T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Zeev Buium wins the NHL Calder Memorial Trophy in the 2026-27 NHL season, then the ma`

### KXNHLCENTRAL — NHL Central Division Winner
- (7) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLCENTRAL-27-WPG, KXNHLCENTRAL-27-UTA, KXNHLCENTRAL-27-STL, KXNHLCENTRAL-27-NSH, KXNHLCENTRAL-27-MIN, KXNHLCENTRAL-27-DAL
- sample fields: `{"ticker": "KXNHLCENTRAL-27-WPG", "event_ticker": "KXNHLCENTRAL-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Central Division?", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Central Division, then the market resolves to Yes."}`

### KXNHLDRAFTPICK — Pro Hockey Draft Pick

### KXNHLDRAFTTOP — Pro Hockey Top Pick

### KXNHLEAST — Eastern Conference Championship
- (16) Will the NAME win the NAME?
- samples: KXNHLEAST-27-WSH, KXNHLEAST-27-TOR, KXNHLEAST-27-TB, KXNHLEAST-27-PIT, KXNHLEAST-27-PHI, KXNHLEAST-27-OTT
- sample fields: `{"ticker": "KXNHLEAST-27-WSH", "event_ticker": "KXNHLEAST-27", "market_type": "binary", "title": "Will the Washington Capitals win the Eastern Conference Finals?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Eastern Conference Finals, t`

### KXNHLEXPANSION — NHL Expansion
- (1) NAME receive an NHL expansion team before #?
- samples: KXNHLEXPANSION-27JAN01HOU-Y
- sample fields: `{"ticker": "KXNHLEXPANSION-27JAN01HOU-Y", "event_ticker": "KXNHLEXPANSION-27JAN01HOU", "market_type": "binary", "title": "Will Houston receive an NHL expansion team before 2027?", "yes_sub_title": "Houston to get an expansion team before 2027", "no_sub_title": "Houston to get an expansion team before 2027", "status": "active", "open_time": "2026-09-01T01:00:00Z", "close_time": "2027-01-01T04:59:00Z", "expected_expiration_time": "2027-01-01T15:00:00Z", "result": "", "rules_primary": "If the NHL officially announces the award of an expansion team franchise to Houston before Jan 1, 2027, then the`

### KXNHLF10G — NHL Goal in First 10 Minutes
- (13) Either team to score in the first # minutes
- samples: KXNHLF10G-26NOV14SEACAR-Y, KXNHLF10G-26NOV13NSHVGK-Y, KXNHLF10G-26NOV13NYRVAN-Y, KXNHLF10G-26NOV12NYILA-Y, KXNHLF10G-26NOV12STLUTA-Y, KXNHLF10G-26NOV12BUFCHI-Y
- sample fields: `{"ticker": "KXNHLF10G-26NOV14SEACAR-Y", "event_ticker": "KXNHLF10G-26NOV14SEACAR", "market_type": "binary", "title": "Either team to score in the first 10 minutes", "yes_sub_title": "Goal in first 10 min", "no_sub_title": "Goal in first 10 min", "strike_type": "greater_or_equal", "floor_strike": 1, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If at least 1 goal is scored by either Seattle or Carolina during the first 10 minutes of the first period (from 0:00 ela`

### KXNHLFINALSEXACT — NHL Championship Series Score

### KXNHLFIRSTGOAL — NHL First Goal
- (328) NAME: NAME
- (1) Tony DeAngelo: NAME
- (1) Kyle MacLean: NAME
- (1) Nick DeSimone: NAME
- (1) MacKenzie Weegar: NAME
- (1) Liam O'Brien: NAME
- (1) Jack McBain: NAME
- (1) Mason McTavish: NAME
- samples: KXNHLFIRSTGOAL-26NOV12NYILA-LASLAUGHTON21, KXNHLFIRSTGOAL-26NOV12STLUTA-UTANSCHMALTZ8, KXNHLFIRSTGOAL-26NOV12DETFLA-FLASVILMANIS95, KXNHLFIRSTGOAL-26NOV12WSHNJ-NJLHAMEENAHO29, KXNHLFIRSTGOAL-26NOV12WSHNJ-NJSNOESEN11, KXNHLFIRSTGOAL-26NOV12DETFLA-DETCMAZUR34
- sample fields: `{"ticker": "KXNHLFIRSTGOAL-26NOV12NYILA-LASLAUGHTON21", "event_ticker": "KXNHLFIRSTGOAL-26NOV12NYILA", "market_type": "binary", "title": "Scott Laughton: First Goalscorer", "yes_sub_title": "Scott Laughton", "no_sub_title": "Scott Laughton", "strike_type": "structured", "custom_strike": {"hockey_player": "ce4454a6-c018-415f-bf53-3e24ba5ed635", "hockey_team": "dbea1e18-0f3c-47a6-9617-e16981181ca2"}, "status": "active", "open_time": "2026-11-12T22:07:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T09:00:00Z", "result": "", "rules_primary": "If Scott Laughton s`

### KXNHLGAME — NHL Game
- (12) NAME wins
- (4) Utah wins
- (4) Montreal wins
- (4) Boston wins
- (4) Dallas wins
- (4) Florida wins
- (3) Colorado wins
- (3) Detroit wins
- samples: KXNHLGAME-26NOV18COLUTA-UTA, KXNHLGAME-26NOV18COLUTA-COL, KXNHLGAME-26NOV18MTLNJ-NJ, KXNHLGAME-26NOV18MTLNJ-MTL, KXNHLGAME-26NOV18BOSDET-DET, KXNHLGAME-26NOV18BOSDET-BOS
- sample fields: `{"ticker": "KXNHLGAME-26NOV18COLUTA-UTA", "event_ticker": "KXNHLGAME-26NOV18COLUTA", "market_type": "binary", "title": "Utah wins", "yes_sub_title": "Utah", "no_sub_title": "Utah", "strike_type": "structured", "custom_strike": {"hockey_team": "7d20591d-c6fa-4b85-8d69-ff05fb3649ac"}, "status": "active", "open_time": "2026-11-12T05:06:00Z", "close_time": "2026-11-21T03:00:00Z", "expected_expiration_time": "2026-11-19T06:00:00Z", "result": "", "rules_primary": "If Utah wins the Colorado vs Utah NHL game originally scheduled for Nov 18, 2026, then the market resolves to Yes."}`

### KXNHLGOAL — NHL Goalscorer
- (565) NAME: #+ goals
- (3) Mason McTavish: #+ goals
- (3) Alex DeBrincat: #+ goals
- (3) Nathan MacKinnon: #+ goals
- (2) Kyle MacLean: #+ goals
- (2) Liam O'Brien: #+ goals
- (2) Jack McBain: #+ goals
- (2) Connor McMichael: #+ goals
- samples: KXNHLGOAL-26NOV12NYILA-LASLAUGHTON21-2, KXNHLGOAL-26NOV12NYILA-LASLAUGHTON21-1, KXNHLGOAL-26NOV12STLUTA-UTANSCHMALTZ8-3, KXNHLGOAL-26NOV12STLUTA-UTANSCHMALTZ8-2, KXNHLGOAL-26NOV12STLUTA-UTANSCHMALTZ8-1, KXNHLGOAL-26NOV12DETFLA-FLASVILMANIS95-2
- sample fields: `{"ticker": "KXNHLGOAL-26NOV12NYILA-LASLAUGHTON21-2", "event_ticker": "KXNHLGOAL-26NOV12NYILA", "market_type": "binary", "title": "Scott Laughton: 2+ goals", "yes_sub_title": "Scott Laughton: 2+", "no_sub_title": "Scott Laughton: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "ce4454a6-c018-415f-bf53-3e24ba5ed635", "hockey_team": "dbea1e18-0f3c-47a6-9617-e16981181ca2"}, "status": "active", "open_time": "2026-11-12T22:07:00Z", "close_time": "2026-11-15T03:00:00Z", "expected_expiration_time": "2026-11-13T09:00:00Z", "result": "", "rules_primary": "If Scott `

### KXNHLHART — NHL Hart Memorial Trophy
- (28) Who will win NAME?
- (10) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- samples: KXNHLHART-27-TSTUTZLE18, KXNHLHART-27-SAHO20, KXNHLHART-27-CKELLER9, KXNHLHART-27-MNECAS88, KXNHLHART-27-LCARLSSON91, KXNHLHART-27-JLACOMBE2
- sample fields: `{"ticker": "KXNHLHART-27-TSTUTZLE18", "event_ticker": "KXNHLHART-27", "market_type": "binary", "title": "Hart Memorial Trophy: Tim Stutzle wins", "yes_sub_title": "Tim Stutzle", "no_sub_title": "Tim Stutzle", "strike_type": "structured", "custom_strike": {"hockey_player": "6df1e248-2084-4229-aa7d-9d6beb8f6b57"}, "status": "active", "open_time": "2026-11-11T16:00:00Z", "close_time": "2027-06-30T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Tim Stutzle wins the NHL Hart Memorial Trophy in the 2026-27 NHL season, then the market resolves to Yes`

### KXNHLLINDSAY — NHL Ted Lindsay Winner
- (35) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLLINDSAY-27-TSTUTZLE18, KXNHLLINDSAY-27-SAHO20, KXNHLLINDSAY-27-CKELLER9, KXNHLLINDSAY-27-MNECAS88, KXNHLLINDSAY-27-LCARLSSON91, KXNHLLINDSAY-27-JLACOMBE2
- sample fields: `{"ticker": "KXNHLLINDSAY-27-TSTUTZLE18", "event_ticker": "KXNHLLINDSAY-27", "market_type": "binary", "title": "Ted Lindsay Award: Tim Stutzle wins", "yes_sub_title": "Tim Stutzle", "no_sub_title": "Tim Stutzle", "strike_type": "structured", "custom_strike": {"hockey_player": "6df1e248-2084-4229-aa7d-9d6beb8f6b57"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Tim Stutzle wins the NHL Ted Lindsay Award in the 2026-27 NHL season, then the market resolves to Yes`

### KXNHLMENTION — NHL Announcer Mentions

### KXNHLMETROPOLITAN — NHL Metropolitan Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLMETROPOLITAN-27-WSH, KXNHLMETROPOLITAN-27-PIT, KXNHLMETROPOLITAN-27-PHI, KXNHLMETROPOLITAN-27-NYR, KXNHLMETROPOLITAN-27-NYI, KXNHLMETROPOLITAN-27-NJ
- sample fields: `{"ticker": "KXNHLMETROPOLITAN-27-WSH", "event_ticker": "KXNHLMETROPOLITAN-27", "market_type": "binary", "title": "Will the Washington Capitals win the Metropolitan Division?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Metropolitan Div`

### KXNHLMVP — NHL Hart Memorial Trophy Winner

### KXNHLNEXTGM — Next NHL GM

### KXNHLNEXTTEAM — NHL Next Team

### KXNHLNORRIS — NHL James Norris Memorial Trophy
- (33) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Charlie McAvoy wins
- samples: KXNHLNORRIS-27-SGOSTISBEHERE4, KXNHLNORRIS-27-SJONES3, KXNHLNORRIS-27-MSEIDER53, KXNHLNORRIS-27-JCHYCHRUN6, KXNHLNORRIS-27-DRADDYSH43, KXNHLNORRIS-27-ZWERENSKI8
- sample fields: `{"ticker": "KXNHLNORRIS-27-SGOSTISBEHERE4", "event_ticker": "KXNHLNORRIS-27", "market_type": "binary", "title": "James Norris Memorial Trophy: Shayne Gostisbehere wins", "yes_sub_title": "Shayne Gostisbehere", "no_sub_title": "Shayne Gostisbehere", "strike_type": "structured", "custom_strike": {"hockey_player": "c07b1390-6d72-4439-8337-a892678d90d5"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Shayne Gostisbehere wins the NHL James Norris Memorial Trophy in`

### KXNHLOT — NHL Overtime
- (13) Game goes to overtime
- samples: KXNHLOT-26NOV14SEACAR-1, KXNHLOT-26NOV13NSHVGK-1, KXNHLOT-26NOV13NYRVAN-1, KXNHLOT-26NOV12NYILA-1, KXNHLOT-26NOV12STLUTA-1, KXNHLOT-26NOV12BUFCHI-1
- sample fields: `{"ticker": "KXNHLOT-26NOV14SEACAR-1", "event_ticker": "KXNHLOT-26NOV14SEACAR", "market_type": "binary", "title": "Game goes to overtime", "yes_sub_title": "Game goes to overtime", "no_sub_title": "Game goes to overtime", "strike_type": "greater", "floor_strike": 0.5, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If at least 1 overtime period is played in the Seattle vs Carolina NHL game originally scheduled for Nov 14, 2026, then the market resolves to Yes."}`

### KXNHLOVERTIME — NHL Overtime

### KXNHLPACIFIC — NHL Pacific Division Winner
- (8) Will the NAME win the NAME?
- samples: KXNHLPACIFIC-27-VGK, KXNHLPACIFIC-27-VAN, KXNHLPACIFIC-27-SJ, KXNHLPACIFIC-27-SEA, KXNHLPACIFIC-27-LA, KXNHLPACIFIC-27-EDM
- sample fields: `{"ticker": "KXNHLPACIFIC-27-VGK", "event_ticker": "KXNHLPACIFIC-27", "market_type": "binary", "title": "Will the Vegas Golden Knights win the Pacific Division?", "yes_sub_title": "Vegas Golden Knights", "no_sub_title": "Vegas Golden Knights", "strike_type": "structured", "custom_strike": {"hockey_team": "d599b5cc-5e06-4679-9303-4d5dad7c4cce"}, "status": "active", "open_time": "2026-08-18T16:00:00Z", "close_time": "2027-05-01T14:00:00Z", "expected_expiration_time": "2027-04-17T14:00:00Z", "result": "", "rules_primary": "If the Vegas Golden Knights win the 2026-27 NHL Pacific Division, then the `

### KXNHLPLAYOFF — Playoff Qualifier
- (30) Will the NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the St. NAME qualify for the playoffs in the #-# NHL season?
- (1) Will the Montréal Canadiens qualify for the playoffs in the #-# NHL season?
- samples: KXNHLPLAYOFF-27-WSH, KXNHLPLAYOFF-27-WPG, KXNHLPLAYOFF-27-VGK, KXNHLPLAYOFF-27-VAN, KXNHLPLAYOFF-27-UTA, KXNHLPLAYOFF-27-TOR
- sample fields: `{"ticker": "KXNHLPLAYOFF-27-WSH", "event_ticker": "KXNHLPLAYOFF-27", "market_type": "binary", "title": "Will the Washington Capitals qualify for the playoffs in the 2026-27 NHL season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-18T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals qualify for the playoffs `

### KXNHLPLAYOFFGOALS — NHL Playoffs Goal Leader (by Round)

### KXNHLPRES — NHL President's Trophy Winner
- (30) Will the NAME win the Presidents' Trophy?
- (1) Will the St. NAME win the Presidents' Trophy?
- (1) Will the Montréal Canadiens win the Presidents' Trophy?
- samples: KXNHLPRES-27-WSH, KXNHLPRES-27-WPG, KXNHLPRES-27-VGK, KXNHLPRES-27-VAN, KXNHLPRES-27-UTA, KXNHLPRES-27-TOR
- sample fields: `{"ticker": "KXNHLPRES-27-WSH", "event_ticker": "KXNHLPRES-27", "market_type": "binary", "title": "Will the Washington Capitals win the Presidents' Trophy?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-14T20:00:00Z", "close_time": "2027-04-25T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals win the 2026-27 NHL Presidents' Trophy, then the market`

### KXNHLPRICE — NHL Ticket Prices

### KXNHLPSEASONGOALS — Player Goals Scored in Season
- (17) NAME: #+ goals in #-# NHL regular season?
- samples: KXNHLPSEASONGOALS-27MCELEBRINI71-60, KXNHLPSEASONGOALS-27MCELEBRINI71-55, KXNHLPSEASONGOALS-27MCELEBRINI71-50, KXNHLPSEASONGOALS-27MCELEBRINI71-45, KXNHLPSEASONGOALS-27MCELEBRINI71-40, KXNHLPSEASONGOALS-27MCELEBRINI71-35
- sample fields: `{"ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71-60", "event_ticker": "KXNHLPSEASONGOALS-27MCELEBRINI71", "market_type": "binary", "title": "Macklin Celebrini: 60+ goals in 2026-27 NHL regular season?", "subtitle": "Macklin Celebrini", "yes_sub_title": "60+ goals", "no_sub_title": "60+ goals", "strike_type": "greater", "floor_strike": 59.5, "custom_strike": {"hockey_player": "264560c4-3624-4c01-924e-879a08799f16"}, "status": "active", "open_time": "2026-10-09T01:30:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Mac`

### KXNHLPTS — Pro Hockey Points
- (349) NAME: #+ points
- (4) Nathan MacKinnon: #+ points
- (3) Mason McTavish: #+ points
- (3) Alex DeBrincat: #+ points
- (3) Charlie McAvoy: #+ points
- (2) Gavin McKenna: #+ points
- (2) Jack McBain: #+ points
- (2) Tony DeAngelo: #+ points
- samples: KXNHLPTS-26NOV12WPGDAL-DALJBENN14-2, KXNHLPTS-26NOV12WPGDAL-DALJBENN14-1, KXNHLPTS-26NOV12MINTOR-TORGMCKENNA92-2, KXNHLPTS-26NOV12MINTOR-TORGMCKENNA92-1, KXNHLPTS-26NOV12MINTOR-MINDYUROV22-2, KXNHLPTS-26NOV12MINTOR-MINDYUROV22-1
- sample fields: `{"ticker": "KXNHLPTS-26NOV12WPGDAL-DALJBENN14-2", "event_ticker": "KXNHLPTS-26NOV12WPGDAL", "market_type": "binary", "title": "Jamie Benn: 2+ points", "yes_sub_title": "Jamie Benn: 2+", "no_sub_title": "Jamie Benn: 2+", "strike_type": "greater", "floor_strike": 1.5, "custom_strike": {"hockey_player": "6c86f425-5e2e-419f-81c4-376474d177b3", "hockey_team": "5cfee6b9-43ff-4dfa-8347-2b9de7ed51b6"}, "status": "active", "open_time": "2026-11-12T21:22:00Z", "close_time": "2026-11-15T01:00:00Z", "expected_expiration_time": "2026-11-13T07:00:00Z", "result": "", "rules_primary": "If Jamie Benn records 2`

### KXNHLRECORDWORST — Worst NHL Record
- (30) Will the NAME have the worst regular season record in the #-# season?
- (1) Will the St. NAME have the worst regular season record in the #-# season?
- (1) Will the Montréal Canadiens have the worst regular season record in the #-# season?
- samples: KXNHLRECORDWORST-27-WSH, KXNHLRECORDWORST-27-WPG, KXNHLRECORDWORST-27-VGK, KXNHLRECORDWORST-27-VAN, KXNHLRECORDWORST-27-UTA, KXNHLRECORDWORST-27-TOR
- sample fields: `{"ticker": "KXNHLRECORDWORST-27-WSH", "event_ticker": "KXNHLRECORDWORST-27", "market_type": "binary", "title": "Will the Washington Capitals have the worst regular season record in the 2026-27 season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-29T16:00:00Z", "close_time": "2027-05-31T14:00:00Z", "expected_expiration_time": "2027-05-01T14:00:00Z", "result": "", "rules_primary": "If the Washington Capitals have the `

### KXNHLRETIRE — NHL Retire

### KXNHLRICHARD — NHL Maurice "Rocket" Richard Trophy
- (41) Maurice "Rocket" NAME: NAME wins
- (1) Maurice "Rocket" NAME: Nathan MacKinnon wins
- (1) Maurice "Rocket" NAME: Connor McDavid wins
- (1) Maurice "Rocket" NAME: Alex DeBrincat wins
- samples: KXNHLRICHARD-27-MMICHKOV39, KXNHLRICHARD-27-LSTANKOVEN22, KXNHLRICHARD-27-ATUCH89, KXNHLRICHARD-27-CGAUTHIER61, KXNHLRICHARD-27-ZHYMAN18, KXNHLRICHARD-27-WNYLANDER88
- sample fields: `{"ticker": "KXNHLRICHARD-27-MMICHKOV39", "event_ticker": "KXNHLRICHARD-27", "market_type": "binary", "title": "Maurice \"Rocket\" Richard Trophy: Matvei Michkov wins", "yes_sub_title": "Matvei Michkov", "no_sub_title": "Matvei Michkov", "strike_type": "structured", "custom_strike": {"hockey_player": "3b72da3e-53e9-4436-8cf2-195612050ff6"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Matvei Michkov wins the NHL Maurice \"Rocket\" Richard Award in the 2026-27 `

### KXNHLROSS — NHL Art Ross Trophy
- (44) NAME: NAME wins
- (1) NAME: Jackson LaCombe wins
- (1) NAME: Nathan MacKinnon wins
- (1) NAME: Connor McDavid wins
- samples: KXNHLROSS-27-MNECAS88, KXNHLROSS-27-LCARLSSON91, KXNHLROSS-27-JLACOMBE2, KXNHLROSS-27-BSENNECKE45, KXNHLROSS-27-AFOX23, KXNHLROSS-27-CGAUTHIER61
- sample fields: `{"ticker": "KXNHLROSS-27-MNECAS88", "event_ticker": "KXNHLROSS-27", "market_type": "binary", "title": "Art Ross Trophy: Martin Necas wins", "yes_sub_title": "Martin Necas", "no_sub_title": "Martin Necas", "strike_type": "structured", "custom_strike": {"hockey_player": "f27d857e-40f4-4ef2-8b89-8f545335f410"}, "status": "active", "open_time": "2026-11-11T17:00:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Martin Necas wins the NHL Art Ross Trophy in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLSAVE — Goaltender Saves
- (17) NAME: #+ saves
- samples: KXNHLSAVE-26NOV12BUFCHI-CHISKNIGHT30-26, KXNHLSAVE-26NOV12DETFLA-DETJGIBSON36-25, KXNHLSAVE-26NOV12NYILA-NYIISOROKIN30-25, KXNHLSAVE-26NOV12NYILA-LADKUEMPER35-25, KXNHLSAVE-26NOV12STLUTA-UTAKVEJMELKA70-23, KXNHLSAVE-26NOV12STLUTA-STLJHOFER30-25
- sample fields: `{"ticker": "KXNHLSAVE-26NOV12BUFCHI-CHISKNIGHT30-26", "event_ticker": "KXNHLSAVE-26NOV12BUFCHI", "market_type": "binary", "title": "Spencer Knight: 26+ saves", "yes_sub_title": "Spencer Knight: 26+", "no_sub_title": "Spencer Knight: 26+", "strike_type": "greater", "floor_strike": 25.5, "custom_strike": {"hockey_player": "3bb13130-50ed-43a6-a6a7-375194db95fc", "hockey_team": "a0e115e4-5a0c-405f-a005-e83ecdc0baa6"}, "status": "active", "open_time": "2026-11-12T20:06:00Z", "close_time": "2026-11-15T01:00:00Z", "expected_expiration_time": "2026-11-13T04:00:00Z", "result": "", "rules_primary": "If `

### KXNHLSAVES — Pro Hockey Saves

### KXNHLSEASONGOALS — Player to score X Goals in Season
- (81) NAME: #+ goals in #-# NHL regular season?
- (2) Nathan MacKinnon: #+ goals in #-# NHL regular season?
- (2) Connor McDavid: #+ goals in #-# NHL regular season?
- (2) Alex DeBrincat: #+ goals in #-# NHL regular season?
- samples: KXNHLSEASONGOALS-27C40-BTKACHUK8, KXNHLSEASONGOALS-27C20-WSMITH2, KXNHLSEASONGOALS-27C20-SCROSBY87, KXNHLSEASONGOALS-27C20-PKANE88, KXNHLSEASONGOALS-27C20-MSCHAEFER48, KXNHLSEASONGOALS-27C20-FNAZAR91
- sample fields: `{"ticker": "KXNHLSEASONGOALS-27C40-BTKACHUK8", "event_ticker": "KXNHLSEASONGOALS-27C40", "market_type": "binary", "title": "Brady Tkachuk: 40+ goals in 2026-27 NHL regular season?", "subtitle": "Brady Tkachuk:: FLA Panthers", "yes_sub_title": "Brady Tkachuk", "no_sub_title": "Brady Tkachuk", "strike_type": "greater", "floor_strike": 39.5, "custom_strike": {"hockey_player": "3d7e2b4d-d4a8-4fe2-904f-fbfb0773ed66"}, "status": "active", "open_time": "2026-10-14T16:35:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If B`

### KXNHLSEASONPPTS — Season Player Points
- (84) NAME: #+ points in #-# NHL regular season?
- (3) Nathan MacKinnon: #+ points in #-# NHL regular season?
- (3) Connor McDavid: #+ points in #-# NHL regular season?
- samples: KXNHLSEASONPPTS-27C110-ZWERENSKI8, KXNHLSEASONPPTS-27C110-WNYLANDER88, KXNHLSEASONPPTS-27C110-WJOHNSTON53, KXNHLSEASONPPTS-27C110-TSTUTZLE18, KXNHLSEASONPPTS-27C110-SCROSBY87, KXNHLSEASONPPTS-27C110-NSUZUKI14
- sample fields: `{"ticker": "KXNHLSEASONPPTS-27C110-ZWERENSKI8", "event_ticker": "KXNHLSEASONPPTS-27C110", "market_type": "binary", "title": "Zach Werenski: 110+ points in 2026-27 NHL regular season?", "subtitle": "Zach Werenski:: Columbus Blue Jackets", "yes_sub_title": "Zach Werenski", "no_sub_title": "Zach Werenski", "strike_type": "greater", "floor_strike": 109.5, "custom_strike": {"hockey_player": "036e0c69-c86a-4ab1-8f63-c6d55b72fe09"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-13T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_pr`

### KXNHLSEASONPTS — NHL Season Point Totals
- (10) Will the WSH Capitals NHL team earn at least # points in the #-# regular season?
- (10) Will the WPG Jets NHL team earn at least # points in the #-# regular season?
- (10) Will the VGK NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the VAN Canucks NHL team earn at least # points in the #-# regular season?
- (10) Will the UTA Mammoth NHL team earn at least # points in the #-# regular season?
- (10) Will the TOR NAME NHL team earn at least # points in the #-# regular season?
- (10) Will the TB Lightning NHL team earn at least # points in the #-# regular season?
- (10) Will the STL Blues NHL team earn at least # points in the #-# regular season?
- samples: KXNHLSEASONPTS-27WSH-95, KXNHLSEASONPTS-27WSH-90, KXNHLSEASONPTS-27WSH-85, KXNHLSEASONPTS-27WSH-80, KXNHLSEASONPTS-27WSH-75, KXNHLSEASONPTS-27WSH-70
- sample fields: `{"ticker": "KXNHLSEASONPTS-27WSH-95", "event_ticker": "KXNHLSEASONPTS-27WSH", "market_type": "binary", "title": "Will the WSH Capitals NHL team earn at least 95 points in the 2026-27 regular season?", "yes_sub_title": "95+ points", "no_sub_title": "95+ points", "strike_type": "greater_or_equal", "floor_strike": 95, "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-08-26T00:47:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-18T14:00:00Z", "result": "", "rules_primary": "If the WSH Capitals earn at le`

### KXNHLSERIES — NHL Series Winner

### KXNHLSERIESGAMES — NHL Series Total Games

### KXNHLSERIESOT — NHL Series Overtime

### KXNHLSERIESSCORE — NHL Series Exact Score

### KXNHLSERIESSPREAD — NHL Series Game Spread

### KXNHLSERIESTOTALGOAL — NHL Series Total Goals

### KXNHLSERIESTOTALGOALS — NHL Series Total Goals

### KXNHLSPREAD — NHL Spread
- (14) NAME wins by over # goals
- (4) NAME I wins by over # goals
- (4) Utah wins by over # goals
- (4) Dallas wins by over # goals
- (4) Buffalo wins by over # goals
- (4) Columbus wins by over # goals
- (4) St. Louis wins by over # goals
- (4) Florida wins by over # goals
- samples: KXNHLSPREAD-26NOV14NYIANA-NYI3, KXNHLSPREAD-26NOV14NYIANA-NYI2, KXNHLSPREAD-26NOV14NYIANA-ANA3, KXNHLSPREAD-26NOV14NYIANA-ANA2, KXNHLSPREAD-26NOV14CGYLA-LA3, KXNHLSPREAD-26NOV14CGYLA-LA2
- sample fields: `{"ticker": "KXNHLSPREAD-26NOV14NYIANA-NYI3", "event_ticker": "KXNHLSPREAD-26NOV14NYIANA", "market_type": "binary", "title": "New York I wins by over 2.5 goals", "yes_sub_title": "New York I wins by over 2.5 goals", "no_sub_title": "New York I wins by over 2.5 goals", "strike_type": "greater", "floor_strike": 2.5, "custom_strike": {"hockey_team": "03f52887-5bb7-4b51-954e-433f73474350"}, "status": "active", "open_time": "2026-11-12T05:05:00Z", "close_time": "2026-11-17T03:00:00Z", "expected_expiration_time": "2026-11-15T06:00:00Z", "result": "", "rules_primary": "If New York I wins by over 2.5 g`

### KXNHLTEAMTOTAL — NHL Team Goals Scored During Game
- (15) NAME over # goals scored
- (5) Seattle over # goals scored
- (5) Carolina over # goals scored
- (5) Vegas over # goals scored
- (5) Nashville over # goals scored
- (5) Vancouver over # goals scored
- (5) NAME R over # goals scored
- (5) NAME I over # goals scored
- samples: KXNHLTEAMTOTAL-26NOV14SEACAR-SEA6, KXNHLTEAMTOTAL-26NOV14SEACAR-SEA5, KXNHLTEAMTOTAL-26NOV14SEACAR-SEA4, KXNHLTEAMTOTAL-26NOV14SEACAR-SEA3, KXNHLTEAMTOTAL-26NOV14SEACAR-SEA2, KXNHLTEAMTOTAL-26NOV14SEACAR-CAR6
- sample fields: `{"ticker": "KXNHLTEAMTOTAL-26NOV14SEACAR-SEA6", "event_ticker": "KXNHLTEAMTOTAL-26NOV14SEACAR", "market_type": "binary", "title": "Seattle over 5.5 goals scored", "yes_sub_title": "Seattle over 5.5", "no_sub_title": "Seattle over 5.5", "strike_type": "greater", "floor_strike": 5.5, "custom_strike": {"hockey_team": "2ed1104c-eb5a-4175-9f05-0561caaa59d2"}, "status": "active", "open_time": "2026-11-12T20:05:00Z", "close_time": "2026-11-16T18:00:00Z", "expected_expiration_time": "2026-11-14T21:00:00Z", "result": "", "rules_primary": "If Seattle scores over 5.5 goals in the Seattle vs Carolina NHL `

### KXNHLTOTAL — NHL Total Goals
- (234) NAME: Over # goals scored
- samples: KXNHLTOTAL-26NOV14NYIANA-9, KXNHLTOTAL-26NOV14NYIANA-8, KXNHLTOTAL-26NOV14NYIANA-7, KXNHLTOTAL-26NOV14NYIANA-6, KXNHLTOTAL-26NOV14NYIANA-5, KXNHLTOTAL-26NOV14NYIANA-4
- sample fields: `{"ticker": "KXNHLTOTAL-26NOV14NYIANA-9", "event_ticker": "KXNHLTOTAL-26NOV14NYIANA", "market_type": "binary", "title": "Full Game: Over 8.5 goals scored", "yes_sub_title": "Over 8.5 goals scored", "no_sub_title": "Over 8.5 goals scored", "strike_type": "greater", "floor_strike": 8.5, "status": "active", "open_time": "2026-11-12T05:06:00Z", "close_time": "2026-11-17T03:00:00Z", "expected_expiration_time": "2026-11-15T06:00:00Z", "result": "", "rules_primary": "If the teams collectively score more than 8.5 goals in the New York I vs Anaheim NHL game originally scheduled for Nov 14, 2026, then th`

### KXNHLVEZINA — NHL Vezina Trophy
- (48) NAME: NAME wins
- samples: KXNHLVEZINA-27-CHART79, KXNHLVEZINA-27-DVLADAR80, KXNHLVEZINA-27-DLEVI27, KXNHLVEZINA-27-JFOWLER32, KXNHLVEZINA-27-JDOBES75, KXNHLVEZINA-27-JWALLSTEDT30
- sample fields: `{"ticker": "KXNHLVEZINA-27-CHART79", "event_ticker": "KXNHLVEZINA-27", "market_type": "binary", "title": "Vezina Trophy: Carter Hart wins", "yes_sub_title": "Carter Hart", "no_sub_title": "Carter Hart", "strike_type": "structured", "custom_strike": {"hockey_player": "7290548a-8894-46f2-ab77-699d8822fb63"}, "status": "active", "open_time": "2026-11-11T16:15:00Z", "close_time": "2027-07-07T14:00:00Z", "expected_expiration_time": "2027-06-30T14:00:00Z", "result": "", "rules_primary": "If Carter Hart wins the NHL Vezina Trophy in the 2026-27 NHL season, then the market resolves to Yes."}`

### KXNHLWEST — Western Conference Champion
- (15) Will the NAME win the NAME?
- (1) Will the St. NAME win the NAME?
- samples: KXNHLWEST-27-WPG, KXNHLWEST-27-VGK, KXNHLWEST-27-VAN, KXNHLWEST-27-UTA, KXNHLWEST-27-STL, KXNHLWEST-27-SJ
- sample fields: `{"ticker": "KXNHLWEST-27-WPG", "event_ticker": "KXNHLWEST-27", "market_type": "binary", "title": "Will the Winnipeg Jets win the Western Conference Finals?", "subtitle": "Winnipeg Jets", "yes_sub_title": "Winnipeg Jets", "no_sub_title": "Winnipeg Jets", "strike_type": "structured", "custom_strike": {"hockey_team": "6f769f6d-161e-43d3-a586-db5451c5050e"}, "status": "active", "open_time": "2026-07-06T20:00:00Z", "close_time": "2027-07-15T14:00:00Z", "expected_expiration_time": "2027-07-01T14:00:00Z", "result": "", "rules_primary": "If the Winnipeg Jets win the 2026-27 NHL Western Conference Fina`

### KXNHLWINS — NHL wins 

### KXNHLWSTREAK — Longest NHL win streak in regular season
- (30) Will the NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the St. NAME have the longest winning streak in the #-# NHL regular season?
- (1) Will the Montréal Canadiens have the longest winning streak in the #-# NHL regular season?
- samples: KXNHLWSTREAK-27-WSH, KXNHLWSTREAK-27-WPG, KXNHLWSTREAK-27-VGK, KXNHLWSTREAK-27-VAN, KXNHLWSTREAK-27-UTA, KXNHLWSTREAK-27-TOR
- sample fields: `{"ticker": "KXNHLWSTREAK-27-WSH", "event_ticker": "KXNHLWSTREAK-27", "market_type": "binary", "title": "Will the Washington Capitals have the longest winning streak in the 2026-27 NHL regular season?", "yes_sub_title": "Washington Capitals", "no_sub_title": "Washington Capitals", "strike_type": "structured", "custom_strike": {"hockey_team": "5b474f02-be1a-4aee-8200-4c4eb6e557e9"}, "status": "active", "open_time": "2026-09-28T17:00:00Z", "close_time": "2027-04-18T14:00:00Z", "expected_expiration_time": "2027-04-11T14:00:00Z", "result": "", "rules_primary": "If Washington Capitals has the longes`

### KXTEAMSINSC — Teams in Stanley Cup
- (1) Will WSH Capitals vs WPG Jets be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VGK NAME be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs VAN Canucks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs UTA Mammoth be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs STL Blues be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SJ Sharks be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs SEA Kraken be the matchup in the #-# NAME?
- (1) Will WSH Capitals vs NSH Predators be the matchup in the #-# NAME?
- samples: KXTEAMSINSC-27-WSHWPG, KXTEAMSINSC-27-WSHVGK, KXTEAMSINSC-27-WSHVAN, KXTEAMSINSC-27-WSHUTA, KXTEAMSINSC-27-WSHSTL, KXTEAMSINSC-27-WSHSJ
- sample fields: `{"ticker": "KXTEAMSINSC-27-WSHWPG", "event_ticker": "KXTEAMSINSC-27", "market_type": "binary", "title": "Will WSH Capitals vs WPG Jets be the matchup in the 2026-27 Stanley Cup Final?", "yes_sub_title": "WSH Capitals vs WPG Jets", "no_sub_title": "WSH Capitals vs WPG Jets", "strike_type": "custom", "custom_strike": {"Matchup": "WSH Capitals vs WPG Jets"}, "status": "active", "open_time": "2026-09-11T22:00:00Z", "close_time": "2027-06-15T14:00:00Z", "expected_expiration_time": "2027-06-15T14:00:00Z", "result": "", "rules_primary": "If WSH Capitals vs WPG Jets is confirmed to be the matchup in t`

## UNRESOLVED samples

- `KXNHLLINDSAY-27-TSTUTZLE18` — Ted Lindsay Award: Tim Stutzle wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-SAHO20` — Ted Lindsay Award: Sebastian Aho wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CKELLER9` — Ted Lindsay Award: Clayton Keller wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MNECAS88` — Ted Lindsay Award: Martin Necas wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-LCARLSSON91` — Ted Lindsay Award: Leo Carlsson wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JLACOMBE2` — Ted Lindsay Award: Jackson LaCombe wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-BSENNECKE45` — Ted Lindsay Award: Beckett Sennecke wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AFOX23` — Ted Lindsay Award: Adam Fox wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CGAUTHIER61` — Ted Lindsay Award: Cutter Gauthier wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-EBOUCHARD2` — Ted Lindsay Award: Evan Bouchard wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-WNYLANDER88` — Ted Lindsay Award: William Nylander wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-SCROSBY87` — Ted Lindsay Award: Sidney Crosby wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-QHUGHES43` — Ted Lindsay Award: Quinn Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-PDOROFEYEV16` — Ted Lindsay Award: Pavel Dorofeyev wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NSUZUKI14` — Ted Lindsay Award: Nick Suzuki wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NMACKINNON29` — Ted Lindsay Award: Nathan MacKinnon wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-NKUCHEROV86` — Ted Lindsay Award: Nikita Kucherov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MTKACHUK19` — Ted Lindsay Award: Matthew Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MRANTANEN96` — Ted Lindsay Award: Mikko Rantanen wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MMARNER93` — Ted Lindsay Award: Mitch Marner wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-MCELEBRINI71` — Ted Lindsay Award: Macklin Celebrini wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-LDRAISAITL29` — Ted Lindsay Award: Leon Draisaitl wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KKAPRIZOV97` — Ted Lindsay Award: Kirill Kaprizov wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-KCONNOR81` — Ted Lindsay Award: Kyle Connor wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JHUGHES86` — Ted Lindsay Award: Jack Hughes wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-JEICHEL9` — Ted Lindsay Award: Jack Eichel wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-ISHESTERKIN31` — Ted Lindsay Award: Igor Shesterkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-DPASTRNAK88` — Ted Lindsay Award: David Pastrnak wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMCDAVID97` — Ted Lindsay Award: Connor McDavid wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CMAKAR8` — Ted Lindsay Award: Cale Makar wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CHELLEBUYCK37` — Ted Lindsay Award: Connor Hellebuyck wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CCAUFIELD13` — Ted Lindsay Award: Cole Caufield wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-CBEDARD98` — Ted Lindsay Award: Connor Bedard wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-BTKACHUK7` — Ted Lindsay Award: Brady Tkachuk wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AVASILEVSKIY88` — Ted Lindsay Award: Andrei Vasilevskiy wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-APANARIN72` — Ted Lindsay Award: Artemi Panarin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AOVECHKIN8` — Ted Lindsay Award: Alex Ovechkin wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLLINDSAY-27-AMATTHEWS34` — Ted Lindsay Award: Auston Matthews wins — series KXNHLLINDSAY not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-60` — Macklin Celebrini: 60+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-55` — Macklin Celebrini: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-50` — Macklin Celebrini: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-45` — Macklin Celebrini: 45+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-40` — Macklin Celebrini: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-35` — Macklin Celebrini: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-30` — Macklin Celebrini: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-25` — Macklin Celebrini: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27MCELEBRINI71-20` — Macklin Celebrini: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-55` — Alex Ovechkin: 55+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-50` — Alex Ovechkin: 50+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-40` — Alex Ovechkin: 40+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-35` — Alex Ovechkin: 35+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-30` — Alex Ovechkin: 30+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-25` — Alex Ovechkin: 25+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-20` — Alex Ovechkin: 20+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title
- `KXNHLPSEASONGOALS-27AOVECHKIN8-15` — Alex Ovechkin: 15+ goals in 2026-27 NHL regular season? — series KXNHLPSEASONGOALS not in ontology; season-scope words in title

## Series decisions (hockey-related)

- skip `KXDELGAME` DEL Game — non-NHL hockey marker 'DEL '
- skip `KXWOWHOCKEY` Winter Olympics Women's Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLHART` NHL Hart Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLRECORDWORST` Worst NHL Record — ticker prefix KXNHL
- NHL  `KXNHL2OT` NHL Double Overtime — ticker prefix KXNHL
- NHL  `KXNHLMETROPOLITAN` NHL Metropolitan Division Winner — ticker prefix KXNHL
- NHL  `KXNHLSERIES` NHL Series Winner — ticker prefix KXNHL
- NHL  `KXNHLVEZINA` NHL Vezina Trophy — ticker prefix KXNHL
- skip `KXELHGAME` ELH Game — no NHL marker
- NHL  `KXNHLRETIRE` NHL Retire — ticker prefix KXNHL
- skip `KXWOMHOCKEYFGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- skip `KXWOMHOCKEYSPREAD` Winter Olympics Men's Hockey Spread — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLATLANTIC` NHL Atlantic Division Winner — ticker prefix KXNHL
- NHL  `KXNHLNORRIS` NHL James Norris Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLGOAL` NHL Goalscorer — ticker prefix KXNHL
- skip `KXAHL` AHL Champion — non-NHL hockey marker 'AHL'
- NHL  `KXNHLRICHARD` NHL Maurice "Rocket" Richard Trophy — ticker prefix KXNHL
- skip `KXELH` ELH Champion — no NHL marker
- NHL  `KXNHL3PTOTAL` 3rd Period Total — ticker prefix KXNHL
- NHL  `KXNHLSERIESGAMES` NHL Series Total Games — ticker prefix KXNHL
- NHL  `KXNHLROSS` NHL Art Ross Trophy — ticker prefix KXNHL
- NHL  `KXNHLPSEASONGOALS` Player Goals Scored in Season — ticker prefix KXNHL
- NHL  `KXNHLPRES` NHL President's Trophy Winner — ticker prefix KXNHL
- skip `KXNCAAHOCKEY` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- skip `KXLIIGA` Liiga Champion — non-NHL hockey marker 'LIIGA'
- skip `KXSHL` SHL Champion — non-NHL hockey marker 'SHL'
- NHL  `KXNHLSEASONGOALS` Player to score X Goals in Season — ticker prefix KXNHL
- skip `KXSHLGAME` SHL Game — non-NHL hockey marker 'SHL'
- skip `KXNL` National League Champion — no NHL marker
- NHL  `KXCONNSMYTHE` Conn Smythe trophy — NHL trophy/futures marker
- NHL  `KXNHLANYGOAL` Pro Hockey Goalscorer — ticker prefix KXNHL
- skip `KXWOMHOCKEYGOAL` Olympic Hockey Goalscorer — non-NHL hockey marker 'OLYMPIC'
- skip `KXKHLGAME` KHL Game — non-NHL hockey marker 'KHL'
- NHL  `KXNHLMVP` NHL Hart Memorial Trophy Winner — ticker prefix KXNHL
- NHL  `KXNHLEXPANSION` NHL Expansion — ticker prefix KXNHL
- skip `KXWOMHOCKEYMVP` Men's Winter Olympics Hockey MVP — non-NHL hockey marker 'OLYMPIC'
- skip `KXLIGMAGGAME` Ligue Magnus Game — no NHL marker
- NHL  `KXNHL1STTEAM` All NHL First Team — ticker prefix KXNHL
- skip `KXHOBEYBAKER` Hobey Baker Award — no NHL marker
- NHL  `KXNEXTTEAMNHL` Next Team NHL — title mentions NHL
- NHL  `KXNHLSERIESTOTALGOAL` NHL Series Total Goals — ticker prefix KXNHL
- skip `KXEUCHLGAME` Champions League Hockey — non-NHL hockey marker 'CHL'
- NHL  `KXNHLWEST` Western Conference Champion — ticker prefix KXNHL
- skip `KXWOMHOCKEYFIRSTGOAL` Winter Olympics Hockey First Goal — non-NHL hockey marker 'OLYMPIC'
- skip `KXWO-HOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLOVERTIME` NHL Overtime — ticker prefix KXNHL
- NHL  `KXNBANHL` NBA + NHL Champion Combo — title mentions NHL
- NHL  `KXNHLTEAMTOTAL` NHL Team Goals Scored During Game — ticker prefix KXNHL
- NHL  `KXNHLSAVES` Pro Hockey Saves — ticker prefix KXNHL
- NHL  `KXNHLSERIESSCORE` NHL Series Exact Score — ticker prefix KXNHL
- NHL  `KXESPYNHL` BEST NHL PLAYER‬ — title mentions NHL
- skip `KXINTHOCKEY` International Hockey — no NHL marker
- skip `KXWOMHOCKEYTOTAL` Winter Olympics Men's Hockey Goal Total — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLFIRSTGOAL` NHL First Goal — ticker prefix KXNHL
- NHL  `KXNHLWINS` NHL wins  — ticker prefix KXNHL
- NHL  `KXNHLSEASONPTS` NHL Season Point Totals — ticker prefix KXNHL
- NHL  `KXNHLEAST` Eastern Conference Championship — ticker prefix KXNHL
- NHL  `KXNHL30COMEBACK` NHL 3-0 Series Comeback — ticker prefix KXNHL
- NHL  `KXNHLSEASONPPTS` Season Player Points — ticker prefix KXNHL
- NHL  `KXNHLSERIESSPREAD` NHL Series Game Spread — ticker prefix KXNHL
- NHL  `KXNHL2PBTTS` NHL Both Teams to Score in 2nd Period — ticker prefix KXNHL
- NHL  `KXNHL` Stanley Cup — ticker prefix KXNHL
- NHL  `KXNHLSERIESOT` NHL Series Overtime — ticker prefix KXNHL
- NHL  `KXNHL1PBTTS` NHL Both Teams to Score in 1st Period — ticker prefix KXNHL
- NHL  `KXNHLCALDER` NHL Calder Memorial Trophy — ticker prefix KXNHL
- NHL  `KXNHLNEXTGM` Next NHL GM — ticker prefix KXNHL
- NHL  `KXNHLF10G` NHL Goal in First 10 Minutes — ticker prefix KXNHL
- skip `KXPHLGAME` Polish Hockey Game — no NHL marker
- NHL  `KXNHLGAME` NHL Game — ticker prefix KXNHL
- NHL  `KXNHLDRAFTTOP` Pro Hockey Top Pick — ticker prefix KXNHL
- NHL  `KXNHLOT` NHL Overtime — ticker prefix KXNHL
- NHL  `KXNHL3PSPREAD` NHL 3rd Period Spread — ticker prefix KXNHL
- skip `KXIIHFCHAMP` IIHF World Championship winner — non-NHL hockey marker 'IIHF'
- skip `KXEARNINGSMENTIONHLT` HILTON — no NHL marker
- NHL  `KXNHLWSTREAK` Longest NHL win streak in regular season — ticker prefix KXNHL
- skip `KXNCAAH` College Hockey National Champion — non-NHL hockey marker 'NCAA'
- NHL  `KXCANADACUP` Canada winning Stanley Cup — NHL trophy/futures marker
- NHL  `KXNHLAST` Pro Hockey Assists — ticker prefix KXNHL
- NHL  `KXNHLPACIFIC` NHL Pacific Division Winner — ticker prefix KXNHL
- NHL  `KXNHL3P` NHL 3rd Period Winner — ticker prefix KXNHL
- NHL  `KXNHLTOTAL` NHL Total Goals — ticker prefix KXNHL
- NHL  `KXNHL1PSPREAD` 1st Period Spread — ticker prefix KXNHL
- NHL  `KXNHL2PSPREAD` 2nd Period Spread — ticker prefix KXNHL
- NHL  `KXNHL3PBTTS` NHL Both Teams to Score in 3rd Period — ticker prefix KXNHL
- skip `KXDEL` DEL Champion — non-NHL hockey marker 'DEL '
- skip `KXIIHFGAME` IIHF Game — non-NHL hockey marker 'IIHF'
- NHL  `KXNHL2P` NHL 2nd Period Winner — ticker prefix KXNHL
- NHL  `KXNHLPLAYOFF` Playoff Qualifier — ticker prefix KXNHL
- skip `KXNLGAME` National League Game — no NHL marker
- NHL  `KXNHLPTS` Pro Hockey Points — ticker prefix KXNHL
- skip `KXLIIGAGAME` Liiga Game — non-NHL hockey marker 'LIIGA'
- NHL  `KXNHL2PTOTAL` 2nd Period Total — ticker prefix KXNHL
- NHL  `KXNHLNEXTTEAM` NHL Next Team — ticker prefix KXNHL
- NHL  `KXNHLCENTRAL` NHL Central Division Winner — ticker prefix KXNHL
- NHL  `KXNHL1PTOTAL` NHL 1st Period Total — ticker prefix KXNHL
- NHL  `KXNHLADAMS` NHL Jack Adams Award — ticker prefix KXNHL
- NHL  `KXNHLLINDSAY` NHL Ted Lindsay Winner — ticker prefix KXNHL
- NHL  `KXNHLPLAYOFFGOALS` NHL Playoffs Goal Leader (by Round) — ticker prefix KXNHL
- NHL  `KXNHLSAVE` Goaltender Saves — ticker prefix KXNHL
- NHL  `KXNHLDRAFTPICK` Pro Hockey Draft Pick — ticker prefix KXNHL
- skip `KXWOMHOCKEY` Winter Olympics Men's Hockey — non-NHL hockey marker 'OLYMPIC'
- skip `KXIIHF` Who will win IIHF championship? — non-NHL hockey marker 'IIHF'
- NHL  `KXNHLSERIESTOTALGOALS` NHL Series Total Goals — ticker prefix KXNHL
- skip `KXKHL` KHL Champion — non-NHL hockey marker 'KHL'
- NHL  `KXNHLSPREAD` NHL Spread — ticker prefix KXNHL
- skip `KXAHLGAME` AHL Game — non-NHL hockey marker 'AHL'
- NHL  `KXNHL1P` NHL 1st Period Winner — ticker prefix KXNHL
- NHL  `KXNHLPRICE` NHL Ticket Prices — ticker prefix KXNHL
- skip `KXWOHOCKEY` Winter Olympics Hockey — non-NHL hockey marker 'OLYMPIC'
- NHL  `KXNHLFINALSEXACT` NHL Championship Series Score — ticker prefix KXNHL
- NHL  `KXNHL4NATIONS` 4 nations face off — ticker prefix KXNHL
- NHL  `KXNHLMENTION` NHL Announcer Mentions — ticker prefix KXNHL
- NHL  `KXTEAMSINSC` Teams in Stanley Cup — NHL trophy/futures marker
- skip `KXNCAAHGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
- skip `KXNCAAHOCKEYGAME` College Hockey Game — non-NHL hockey marker 'NCAA'
