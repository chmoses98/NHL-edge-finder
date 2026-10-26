"""Verbatim third-party page content (DailyFaceoff, Rotowire) is not published: not to the archive, not as committed probe samples."""

from __future__ import annotations

import importlib.util
import json
from datetime import UTC, datetime
from pathlib import Path
from types import SimpleNamespace

import pytest

from nhl_edge.archive.ledger import FORBIDDEN_RAW_KINDS, Ledger, RightsError, is_forbidden_kind

ROOT = Path(__file__).resolve().parents[1]


def test_the_ledger_refuses_the_raw_dailyfaceoff_kind(tmp_path):
    led = Ledger(tmp_path)
    assert "context/dailyfaceoff_raw" in FORBIDDEN_RAW_KINDS
    with pytest.raises(RightsError):
        led.write_blob("context/dailyfaceoff_raw", b"{}", observed_at=datetime(2026, 10, 26, tzinfo=UTC))
    with pytest.raises(RightsError):
        led.append_rows("context/dailyfaceoff_raw", [{"a": 1}], observed_at=datetime(2026, 10, 26, tzinfo=UTC))
    led.append_rows("context/goalie_observations", [{"a": 1}], observed_at=datetime(2026, 10, 26, tzinfo=UTC))        # derived kinds are unaffected


def test_no_code_path_writes_the_raw_kind_or_saves_html_samples():
    ctx = (ROOT / "src/nhl_edge/data/context.py").read_text()
    assert "write_blob(\"context/dailyfaceoff_raw\"" not in ctx and "raw_pages" not in ctx
    assert "sample_html\": True" not in (ROOT / "scripts/probe_sources.py").read_text()


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_player_source_probe_saves_no_copy_of_third_party_html(tmp_path, monkeypatch):
    mod = _load("probe_player_sources")
    html = b'<html><script id="__NEXT_DATA__" type="application/json">{"props": {"pageProps": {"a": 1}}}</script></html>'
    monkeypatch.setattr(mod, "fetch", lambda url, **k: SimpleNamespace(content=html, status=200, fetched_at_utc="2026-10-26T00:00:00Z"))
    assert mod.main(["--out", str(tmp_path)]) == 0
    rep = json.loads((tmp_path / "PROBE.json").read_text())
    assert not list(tmp_path.glob("*.html")) and not list(tmp_path.glob("*.next_data.json"))
    assert all(v.get("saved_copy") is False and v.get("next_data_keys") == ["a"] for v in rep.values() if "error" not in v)


def test_slash_case_and_pattern_variants_of_forbidden_kinds_are_refused_too():
    for k in ("context/dailyfaceoff_raw", "context/dailyfaceoff_raw/", "context//dailyfaceoff_raw", "Context/DailyFaceoff_Raw", "./context/dailyfaceoff_raw", "context/rotowire_pages", "x/dailyfaceoff_html_raw"):
        assert is_forbidden_kind(k), k
    for k in ("context/goalie_observations", "context/lines", "predictions_player", "player_events/players"):
        assert not is_forbidden_kind(k), k
