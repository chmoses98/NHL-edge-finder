"""HTTP fetch with provenance and an on-disk cache keyed by URL and TTL.

Every fetch returns a ``Fetched`` carrying the exact instant the bytes were obtained, so a snapshot can record
the source-observation time separately from the time we processed it. Retries on transient errors only.
"""

from __future__ import annotations

import hashlib
import json
import random
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

from nhl_edge.config import settings
from nhl_edge.log import get_logger, kv
from nhl_edge.timeutil import iso, utcnow

log = get_logger(__name__)

JSON_HEADERS = {"Accept": "application/json"}
BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "*/*",
}
RETRYABLE = {429, 500, 502, 503, 504}


class FetchError(RuntimeError):
    pass


@dataclass(frozen=True)
class Fetched:
    url: str
    status: int
    content: bytes
    fetched_at_utc: str
    from_cache: bool
    content_type: str | None = None
    last_modified: str | None = None

    def json(self) -> Any:
        return json.loads(self.content.decode("utf-8"))

    def text(self) -> str:
        return self.content.decode("utf-8", "replace")

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.content).hexdigest()


def _cache_path(url: str) -> Path:
    cfg = settings()
    return cfg.cache_root / "http" / (hashlib.sha256(url.encode()).hexdigest()[:32] + ".bin")


def fetch(url: str, ttl_s: float = 0.0, headers: dict[str, str] | None = None, timeout: float | None = None,
          max_retries: int | None = None, transport: httpx.BaseTransport | None = None) -> Fetched:
    """GET ``url``. ``ttl_s > 0`` serves a cached copy younger than that; 0 always hits the network."""
    cfg = settings()
    cp = _cache_path(url)
    meta = cp.with_suffix(".json")
    if ttl_s > 0 and cp.exists() and meta.exists():
        try:
            m = json.loads(meta.read_text())
            if time.time() - m["t"] < ttl_s:
                return Fetched(url, m["status"], cp.read_bytes(), m["fetched_at_utc"], True, m.get("content_type"), m.get("last_modified"))
        except (json.JSONDecodeError, KeyError, OSError):
            pass
    hdrs = {"User-Agent": cfg.user_agent, **JSON_HEADERS, **(headers or {})}
    retries = cfg.http_max_retries if max_retries is None else max_retries
    last: Exception | None = None
    with httpx.Client(timeout=timeout or cfg.http_timeout_s, headers=hdrs, follow_redirects=True, transport=transport) as c:
        for attempt in range(retries + 1):
            try:
                r = c.get(url)
            except (httpx.TransportError, httpx.TimeoutException) as e:
                last = e
                time.sleep(min(2.0**attempt, 15.0) * (0.5 + random.random()))
                continue
            if r.status_code == 200:
                f = Fetched(url, r.status_code, r.content, iso(utcnow()), False, r.headers.get("Content-Type"), r.headers.get("Last-Modified"))
                try:
                    cp.parent.mkdir(parents=True, exist_ok=True)
                    cp.write_bytes(f.content)
                    meta.write_text(json.dumps({"t": time.time(), "status": f.status, "fetched_at_utc": f.fetched_at_utc, "content_type": f.content_type, "last_modified": f.last_modified}))
                except OSError:
                    pass
                return f
            if r.status_code in RETRYABLE:
                last = FetchError(f"HTTP {r.status_code} {url}")
                log.warning(kv(event="http_retry", status=r.status_code, url=url, attempt=attempt))
                time.sleep(min(2.0**attempt, 15.0) * (0.5 + random.random()))
                continue
            raise FetchError(f"HTTP {r.status_code} {url}: {r.text[:200]}")
    raise FetchError(f"exhausted retries for {url}: {last}")
