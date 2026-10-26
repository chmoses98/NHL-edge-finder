# Draft: permission request to DailyFaceoff (not sent; permission NOT received)

**Verified contact channel.** `https://www.dailyfaceoff.com/contact-us` (HTTP 200 on 2026-10-26, read from a GitHub runner with the project's identifying User-Agent). The pages read (home, contact-us, privacy policy) publish **no email address**; the channel is the site's contact page/form. No terms-of-use page was found (`/terms-of-service` is 404), so the request also asks where the terms are. Send from the project owner's own account and name; keep the reply (it is the permission, if given).

---
**Subject:** Request for written permission: automated collection of your public line-combination and starting-goalie pages for non-commercial hockey research

Hello,

I run a small, non-commercial research project (`github.com/chmoses98/NHL-edge-finder`) that studies how well hockey player ice-time and shot projections can be forecast before a game. Your public team line-combination pages (`/teams/<team>/line-combinations`) and starting-goalie pages (`/starting-goalies/<date>`) are the only source we have found for projected lines, power-play units and starter confirmations.

What we do today, so you can judge it: two collectors read your pages on game days: one roughly hourly (the line-combination page of each team playing that day, plus the starting-goalies pages for today and tomorrow) and one at each projection refresh (the same pages for games in the next ~30 hours). Together that is on the order of several hundred to about a thousand page requests on a busy slate. Each is a single GET with an identifying User-Agent (`nhl-edge-finder/0.1 (+https://github.com/chmoses98/NHL-edge-finder)`), respecting robots.txt, without logging in. We keep, per player, only small derived facts: team, line/power-play unit and slot, status flags, your page's `updatedAt` time and our observation time, and the resolved NHL player id. We have **stopped** publishing any raw page content (HTML or embedded JSON) and removed the sample copies from our going-forward process. We have not used your data for anything commercial; our research is not offered for sale and does not place wagers.

We would like your explicit written permission for:
1. automated collection at the rate above (and your preferred rate limit or schedule);
2. retaining the derived facts described above, including in a public research repository (or, if you prefer, only privately);
3. using them as inputs to our forecasting models;
4. whether any public or commercial use, ever, would need a separate licence, and on what terms.

If you would rather we stop, or use another channel (an API, a feed, a licence), please tell us and we will comply. Could you also point us to your terms of use? We will not assume permission until we have your reply in writing.

Thank you,
[name], [email], on behalf of the project
