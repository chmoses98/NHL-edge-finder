# Official NHL lineup sources: what is published before a puck drop, and when (research only)

Status 2026-10-25: **method in place, no result yet.** This file is updated with measured timings; until then nothing here claims a publication time.

## Question
Do official NHL sources publish scratches, the dressed roster or lines early enough before the drop to improve our ice-time and power-play forecasts, and can they be told apart from projections?

## Sources and how each is measured
| source | what it could add | access | measured by |
|---|---|---|---|
| `api-web` `gamecenter/{id}/right-rail` (`gameInfo.{home,away}Team.scratches`) | scratches by player id | public JSON the pipeline already reads, identifying User-Agent | `nhl_lineup_probe` polls at T-180 … T-5 |
| `api-web` `gamecenter/{id}/landing` | matchup, game state; lineup-like structures if any appear pregame | same | same |
| official HTML game roster sheet (`nhl.com/scores/htmlreports/{season}/RO{gamenumber}.HTM`) | dressed roster, scratches | web page; **probed only if the access audit (robots.txt, terms) allows it** | `--sheets`, off by default |
| DailyFaceoff lines / PP units | projected and "confirmed" lines, PP units | see `DAILYFACEOFF_COMPLIANCE.md` | `context/lines` archive (lines + the source's own `updatedAt` and label) |

## Confirmed vs projected
The NHL endpoints carry no "confirmed" label. For the probe, a structure that first appears only after warmups (late offsets) is treated as confirmed-by-publication; one present at T-180 or earlier is a roster/season list, not a game lineup. DailyFaceoff labels its own source ("Projected", "Practice", "Warmups …", "Last Game (date)" = the previous game's lines, i.e. not a projection for this game). Power-play units exist only in DailyFaceoff data; no official pregame power-play unit source has been found.

## How to read results
`python -m nhl_edge.research.nhl_lineup_probe summarize --out <lineup-probe-data checkout>` (also in each run's summary): per game and endpoint, the first poll at which a lineup-like structure is non-empty, in minutes before the drop. The resolution is the gap between polls (down to 3 minutes near the drop). A source is useful for our forecasts only if its first non-empty poll is earlier than the latest time a forecast can still be published (the 2026-10-23 slate published its last pregame forecasts 12.7 / 17.7 minutes before the drops).
