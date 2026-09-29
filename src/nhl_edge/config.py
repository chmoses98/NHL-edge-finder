"""Runtime configuration. Everything here is environment-driven; nothing requires a credential."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def _env(name: str, default: str = "") -> str:
    v = os.environ.get(name)
    return v if v not in (None, "") else default


@dataclass(frozen=True)
class Settings:
    # Public read-only Kalshi host. nba-edge-finder runs production capture against this host daily;
    # kalshi-bet-router verified external-api.kalshi.com serves the same /trade-api/v2 space. Overridable.
    kalshi_base_url: str = field(default_factory=lambda: _env("KALSHI_BASE_URL", "https://api.elections.kalshi.com/trade-api/v2"))
    kalshi_historical_base_url: str = field(
        default_factory=lambda: _env("KALSHI_HISTORICAL_BASE_URL", "https://external-api.kalshi.com/trade-api/v2/historical")
    )
    nhl_api_base_url: str = field(default_factory=lambda: _env("NHL_API_BASE_URL", "https://api-web.nhle.com/v1"))
    nhl_stats_base_url: str = field(default_factory=lambda: _env("NHL_STATS_BASE_URL", "https://api.nhle.com/stats/rest/en"))
    moneypuck_base_url: str = field(default_factory=lambda: _env("MONEYPUCK_BASE_URL", "https://moneypuck.com/moneypuck"))
    data_root: Path = field(default_factory=lambda: Path(_env("NHL_EDGE_DATA_ROOT", str(REPO_ROOT / "data"))))
    cache_root: Path = field(default_factory=lambda: Path(_env("NHL_EDGE_CACHE_ROOT", str(REPO_ROOT / ".cache"))))
    http_timeout_s: float = 30.0
    http_max_retries: int = 4
    user_agent: str = "nhl-edge-finder/0.1 (+https://github.com/chmoses98/NHL-edge-finder)"

    @property
    def catalog_dir(self) -> Path:
        return self.data_root / "catalog"

    @property
    def identity_dir(self) -> Path:
        return self.data_root / "identity"

    @property
    def archive_dir(self) -> Path:
        return self.data_root / "archive"


def settings() -> Settings:
    return Settings()
