# NHL api-web: do the NHL website terms apply, and to which of our uses? (2026-10-26)

Evidence only, not a legal opinion. Sources read on a runner (`source-audit`, identifying User-Agent): the NHL Terms of Service (`nhl.com/info/terms-of-service`, 168 KB of text), the copyright and terms-of-use pages, `robots.txt` of `api-web.nhle.com`, `api.nhle.com` and `www.nhl.com`.

## What the terms say (verbatim extracts)
- **Scope.** "…the digital platforms, websites and online services that display or provide an authorized link to these Terms (collectively, the 'Services'). The Services include, without limitation, nhl.com, and NHL mobile applications…"
- **Permitted use.** "All content, information, computer code, software, and any other materials that are part of the Services … ('NHL Content') … are the property of the NHL. You may access, use, and display the Services, but only for **non-commercial, informational, personal use, without modification or alteration** in any way, and only so long as you comply with these Terms."
- **Prohibited.** "Engage in unauthorized spidering, scraping, or harvesting of content or information, or use any other **unauthorized automated means to compile information**." Team and League marks "may not be reproduced or used commercially without the prior written consent of NHL Enterprises, L.P." Embedded NHL content "must be for non-commercial purposes only".
- **Contact.** Requests for written consent are to be made "via the contact information provided in Section 27" of the Terms; `https://www.nhl.com/contact` (HTTP 200, a web form; no email address on the pages read) and a DMCA-agent postal address/phone are the published channels.

## Do they apply to `api-web.nhle.com` / `api.nhle.com`?
**Not established either way.**
- The endpoints are on a different host, return JSON and neither display nor link to the Terms, which is the test the Terms themselves use ("display or provide an authorized link").
- But they are the data backend of the Services (nhl.com and the NHL app read them), the content is NHL Content as defined, and nothing on the hosts grants a separate licence. Their `robots.txt` disallows nothing; that is a crawler convention, not a grant of rights.
- No developer terms, API licence or documented endpoint list was found for either host. The endpoints are undocumented; absence of a stated restriction is not permission.

## Our uses, classified
| use | what is done | classification |
|---|---|---|
| Internal analysis and model fitting on game data (boxscores, play-by-play, shift charts, schedules, rosters) | automated, a few hundred requests per day, identifying User-Agent, since the project began | "automated means to compile information" from NHL Content; arguably *informational, non-commercial, internal*, but not licensed. **Status quo; not expanded.** |
| Per-game play-by-play fetch inside the final 3 h before a drop (projection-foundation `official roster` late update) | up to ~10 requests per projection run per game starting within 3 h | existing automated use; **not expanded**. |
| Public redistribution of NHL-derived data | `data/history/**` (player-event tables, public), the `data-archive` `player_events` and `results` kinds, probe samples of NHL JSON, and (new) raw bodies on `lineup-probe-data` | **the highest-risk category**: NHL Content republished in a public repository, for a project whose outputs inform betting analysis (the Terms' "non-commercial" test is about the use, not the repository). Derived statistics (ice time, shot counts) are facts, but the repository stores them in bulk. |
| Commercial use of NHL data | none today (research only, PASS-only) | would require written consent; **not authorized by anything found**. |

## Position taken (no new automated compilation)
- No new endpoint, no higher request rate, no new probe. The NHL lineup-timing probe ran once (three runs, 2026-10-25) and its workflow is now **gated off** (it refuses to run without an explicit rights acknowledgement input); no further runs are dispatched.
- The HTML game sheets on nhl.com are not fetched at all.
- Existing uses continue unchanged as internal, non-commercial analysis; they are not claimed to be licensed.
- Public redistribution of NHL-derived raw material stops expanding: no new raw NHL response bodies are stored (the probe's raw-body option is off by default).

## Recommended next steps (owner)
1. Send a written inquiry through `NHL.com/contact` asking whether the project may (a) read `api-web` / `api.nhle.com` automatically for internal research at the current rate, (b) retain derived player-game statistics, and (c) publish derived statistics in a public repository; state the research-only, non-commercial status. Do not claim permission until it is answered in writing.
2. Until answered: treat bulk public redistribution as the risk to reduce first (consider making the data branches private, which loses nothing for the pipeline), before reducing collection.
