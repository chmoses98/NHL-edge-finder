# Data-source access audit, 2026-10-25 (evidence; not a legal opinion)

Run: GitHub Actions `source-audit` run 40151428029 (a runner, because this development environment's egress policy blocks these hosts). Tool: `src/nhl_edge/research/source_audit.py`. Every request used the repository's identifying User-Agent (`nhl-edge-finder/0.1 (+https://github.com/chmoses98/NHL-edge-finder)`), one GET per document, no retries, no header changes.

| host | robots.txt | plain identifying request to the paths we use | terms found |
|---|---|---|---|
| dailyfaceoff.com | HTTP 200; `/teams/*/line-combinations` and `/starting-goalies/*` allowed for our agent and for `*` | **HTTP 200 with the embedded page data on both** (231 KB, 143 KB) | link discovery found only the privacy policy (HTTP 200, nothing about automated access); `/terms-of-service` is HTTP 404. **No terms of use located** |
| api-web.nhle.com | HTTP 200, nothing disallowed | HTTP 200 for schedule, landing, right-rail | no terms for the API host; `nhl.com` terms below |
| api.nhle.com (stats REST) | HTTP 200, nothing disallowed | HTTP 200 | same |
| nhl.com (website) | HTTP 200; the game-sheet path is allowed | game roster sheet `RO020180.HTM`: HTTP 404 (not published or wrong number; not yet informative) | **Terms of Service prohibit "unauthorized spidering, scraping, or harvesting of content or information, or … unauthorized automated means to compile information"; copyright policy: content "may not be reproduced without the prior written consent of NHL Enterprises, L.P."** |
| moneypuck.com | HTTP 200; `/data.htm` allowed | HTTP 200 | privacy policy only; data page (read earlier) says free for non-commercial use and unapproved scraping is blocked |
| site.api.espn.com | robots.txt HTTP 403 (unreadable) | HTTP 200 (1.4 MB injuries JSON) | no terms found; unofficial API |

Consequences recorded by this audit:
1. The spoofed Chrome User-Agent was **not needed**: DailyFaceoff serves both pages to the identifying agent, and robots.txt allows them. It is removed (this PR); no function is lost.
2. Terms of use for DailyFaceoff could not be located by the tool; that is an open question for the owner, not a finding of permission.
3. The NHL website terms prohibit automated compilation of site content. The public `api-web` JSON the pipeline already uses is a different host with no terms found; whether the website terms extend to it is a question for the owner. The HTML game sheets are on nhl.com and are therefore **not** probed (the lineup-probe workflow keeps `sheets=false`).
