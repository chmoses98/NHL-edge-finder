# Official NHL lineup sources: what is published before a puck drop, and when (research only)

Status 2026-10-26: **first measurement, one slate (5 games, 2026-10-25). Preliminary.**

## Question
Do official NHL sources publish scratches, the dressed roster or lines early enough before the drop to improve our ice-time and power-play forecasts, and can they be told apart from projections?

## Sources and how each is measured
| source | what it could add | access | measured by |
|---|---|---|---|
| `api-web` `gamecenter/{id}/right-rail` (`gameInfo.{home,away}Team.scratches`) | scratches by player id | public JSON the pipeline already reads, identifying User-Agent | `nhl_lineup_probe` polls at T-120 … T-5 (one run per cluster of drops, parallel runs write their own manifests) |
| `api-web` `gamecenter/{id}/landing` | matchup, game state; lineup-like structures if any appear pregame | same | same |
| official HTML game roster sheet (`nhl.com/scores/htmlreports/{season}/RO{gamenumber}.HTM`) | dressed roster, scratches | web page on nhl.com; **not probed**: nhl.com's terms of service prohibit automated compilation of site content (`SOURCE_AUDIT_2026-10-25.md`); the sheet URL tried by the audit was also HTTP 404 | not measured |
| DailyFaceoff lines / PP units | projected and "confirmed" lines, PP units | see `DAILYFACEOFF_COMPLIANCE.md` | `context/lines` archive (lines + the source's own `updatedAt` and label) |

## Confirmed vs projected
The NHL endpoints carry no "confirmed" label. For the probe, a structure that first appears only after warmups (late offsets) is treated as confirmed-by-publication; one present at T-180 or earlier is a roster/season list, not a game lineup. DailyFaceoff labels its own source ("Projected", "Practice", "Warmups …", "Last Game (date)" = the previous game's lines, i.e. not a projection for this game). Power-play units exist only in DailyFaceoff data; no official pregame power-play unit source has been found.

## How to read results
`python -m nhl_edge.research.nhl_lineup_probe summarize --out <lineup-probe-data checkout>` (also in each run's summary): per game and endpoint, the first poll at which a lineup-like structure is non-empty, in minutes before the drop. The resolution is the gap between polls (down to 3 minutes near the drop). A source is useful for our forecasts only if its first non-empty poll is earlier than the latest time a forecast can still be published (the 2026-10-23 slate published its last pregame forecasts 12.7 / 17.7 minutes before the drops).

## First measurement: slate of 2026-10-25 (5 regular-season games, three probe runs, all successful)
Polls at T-120, 90, 75, 60, 45, 30, 20, 12, 8, 5 minutes on `landing` and `right-rail` (identifying User-Agent, HTTP 200 on every poll that ran; two T-120 polls were skipped as late because of runner queueing and are recorded as `skipped_late`). Raw bodies are on the `lineup-probe-data` branch.

| game | first poll at which `right-rail` `gameInfo.{home,away}Team.scratches` was non-empty (minutes before the drop) | `landing` lineup-like content |
|---|---|---|
| 2026020180 | **T-20** (empty at T-30) | none (season goalie statistics only, from T-90) |
| 2026020181 | **T-20** | none |
| 2026020182 | **never before the drop** (10 polls, list stayed empty) | none |
| 2026020183 | **T-8** (empty at T-12) | none |
| 2026020184 | **T-8** (empty at T-12) | none |

Reading (five games, one night: preliminary):
1. The official scratch list appears only **8–20 minutes before the drop**, and for one game not at all before the drop. The resolution is the gap between polls (3–10 minutes), so the true publication instant is up to that much earlier than shown.
2. `landing` carries no lineup: its goalie fields are season statistics, not a starter.
3. **Usefulness for forecasts:** the last pregame projection evaluations on the 2026-10-24 slate ran 18.5–47.7 minutes before the drops. Official scratches therefore arrive after the last evaluation for most games; using them would require evaluating inside the final 10–20 minutes, which the current refresh timing (and runner queue delays of up to ~23 minutes) cannot guarantee. As a pregame input today they are marginal; as an after-the-fact label they are fine.
4. Confirmed vs projected: the NHL feed has no label, but publication this late is itself the confirmation. DailyFaceoff's earlier lines are projections (many rows are "Last Game (date)" at record time); its warmup-sourced rows are the closest to confirmed, and their timing is available from the archived `context/lines` (`updatedAt` and our observation time).
5. Not covered: power-play units (no official pregame source found), the HTML game sheets (not probed: nhl.com terms), and day-to-day variation. More slates are needed before a distribution can be stated; the probe is dispatched per cluster of drops.
