"""Starting-goalie sources.

Production V1: the NHL boxscore ``starter`` flag (only available once the game starts: used by settlement and for
scoring the pregame projections) and DailyFaceoff's starting-goalies page (optional enrichment; HTML page carrying
a JSON ``__NEXT_DATA__`` blob, shape verified 2026-09-29). If DailyFaceoff is unreachable or its shape drifts, the
context job records the failure and every goalie stays UNKNOWN/PROJECTED — the slate still runs.
"""

from __future__ import annotations

import json
import re
from datetime import datetime
from typing import Any

from nhl_edge.data.http import BROWSER_HEADERS, FetchError, fetch
from nhl_edge.goalies.state import parse_dailyfaceoff_next_data
from nhl_edge.identity.teams import registry
from nhl_edge.log import get_logger, kv
from nhl_edge.schemas.core import GoalieObservation
from nhl_edge.timeutil import parse_iso

log = get_logger(__name__)

DFO_URL = "https://www.dailyfaceoff.com/starting-goalies/{date}"
_NEXT_RE = re.compile(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', re.S)


def extract_next_data(html: str) -> dict[str, Any]:
    m = _NEXT_RE.search(html)
    if not m:
        raise ValueError("no __NEXT_DATA__ blob in page")
    return json.loads(m.group(1))


def _resolve(name: str) -> int | None:
    t = registry().resolve_name(name)
    return t.team_id if t else None


def strip_market_fields(row: dict[str, Any]) -> dict[str, Any]:
    """Sportsbook prices on the DFO row are never archived alongside DATA_ONLY inputs."""
    return {k: v for k, v in row.items() if "moneyline" not in k.lower() and "pointspread" not in k.lower() and "salary" not in k.lower()}


def fetch_dailyfaceoff(date_et: str) -> tuple[list[GoalieObservation], dict[str, Any]]:
    url = DFO_URL.format(date=date_et)
    try:
        f = fetch(url, headers=BROWSER_HEADERS, max_retries=2)
        nd = extract_next_data(f.text())
        pp = nd.get("props", {}).get("pageProps", {})
    except (FetchError, ValueError, json.JSONDecodeError) as e:
        log.warning(kv(event="dailyfaceoff_failed", err=str(e)[:160]))
        return [], {"source": "dailyfaceoff", "url": url, "error": str(e)[:300], "n": 0}
    observed = parse_iso(f.fetched_at_utc)
    obs, problems = parse_dailyfaceoff_next_data(pp, observed, _resolve)
    raw_rows = [strip_market_fields(r) for r in (pp.get("data") or []) if isinstance(r, dict)]
    return obs, {"source": "dailyfaceoff", "url": url, "fetched_at_utc": f.fetched_at_utc, "sha256": f.sha256, "n": len(obs),
                 "page_date": pp.get("date"), "problems": problems, "raw_rows": raw_rows}


def observations_from_boxscore(box: dict[str, Any], observed_at: datetime) -> list[GoalieObservation]:
    """CONFIRMED starters from a started/final game's boxscore. Post-start by definition; used for scoring, never pregame."""
    out = []
    for side, key in (("home", "home_goalies"), ("away", "away_goalies")):
        tid = box.get(f"{side}_team_id")
        for gl in box.get(key) or []:
            if gl.get("starter") and tid is not None:
                out.append(GoalieObservation(game_id=str(box["game_id"]), team_id=int(tid), player_id=gl.get("player_id"), player_name=gl.get("name"),
                                             status="CONFIRMED", observed_at_utc=observed_at, source="nhl_api_boxscore", confidence=1.0,
                                             note="starter flag from boxscore (post-start)"))
    return out
