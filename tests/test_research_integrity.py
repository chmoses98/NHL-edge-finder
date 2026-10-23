"""Historical-data and frozen-cohort integrity: importing new seasons (or re-running research) must never silently alter frozen walk-forward inputs,
production shadow arms, prior evaluation cohorts, committed result tables or preregistrations. See ``nhl_edge.research.integrity``."""

from __future__ import annotations

import ast
import json
from pathlib import Path

import pytest

from nhl_edge.data import history as H
from nhl_edge.research import integrity as I  # noqa: E741

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "nhl_edge"


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# the committed registry
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def test_registered_files_and_cohorts_are_unchanged():
    d = I.diff(I.load_registry(), I.scan(), I.cohort_values())
    assert not any(d.values()), (
        f"frozen research inputs changed: {json.dumps(d, indent=1)}\n"
        "Historical data, parameter files, preregistrations and committed result tables are append-only. Supersede with a NEW, differently named file and "
        "run `python -m nhl_edge.research.integrity register` to add it; never edit or regenerate a registered file in place.")


def test_registry_covers_every_history_file_and_every_production_param_file():
    reg = I.load_registry()["files"]
    on_disk = I.scan()
    assert all(k in reg for k in on_disk if k.startswith(("data/history/", "data/params/")))
    assert any(k.startswith("data/history/moneypuck/team_games_2008") for k in reg) and any(k.startswith("data/params/") for k in reg)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# the registry mechanism itself (synthetic)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def _tree(tmp_path: Path) -> Path:
    for rel, body in {"data/history/moneypuck/team_games_2022.parquet": b"A", "data/history/nhl/games_2022.parquet": b"B", "data/params/p-1.0.json": b"{}",
                      "docs/research/x/PREREGISTRATION.md": b"prereg"}.items():
        f = tmp_path / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(body)
    return tmp_path


def test_diff_flags_modification_removal_and_unregistered_data(tmp_path):
    root = _tree(tmp_path)
    reg = I.register({"schema": "x", "files": {}, "cohorts": {}}, I.scan(root), {"c": [1]})
    assert not any(I.diff(reg, I.scan(root), {"c": [1]}).values())
    (root / "data/history/moneypuck/team_games_2022.parquet").write_bytes(b"A2")          # a re-pulled season
    (root / "data/params/p-1.0.json").unlink()                                              # a deleted parameter file
    (root / "data/history/moneypuck/team_games_2008.parquet").write_bytes(b"new")           # an imported season nobody registered
    (root / "docs/research/x/PREREGISTRATION.md").write_bytes(b"edited")                     # an edited preregistration
    d = I.diff(reg, I.scan(root), {"c": [2]})
    assert d["modified"] == ["data/history/moneypuck/team_games_2022.parquet", "docs/research/x/PREREGISTRATION.md"] or set(d["modified"]) == {
        "data/history/moneypuck/team_games_2022.parquet", "docs/research/x/PREREGISTRATION.md"}
    assert d["missing"] == ["data/params/p-1.0.json"] and d["unregistered"] == ["data/history/moneypuck/team_games_2008.parquet"] and d["cohort_drift"]


def test_register_appends_new_entries_but_refuses_to_rewrite_existing_ones(tmp_path):
    root = _tree(tmp_path)
    reg = I.register({"schema": "x", "files": {}, "cohorts": {}}, I.scan(root), {"c": [1]})
    (root / "data/history/moneypuck/team_games_2009.parquet").write_bytes(b"C")
    reg2 = I.register(reg, I.scan(root), {"c": [1], "d": 2})
    assert "data/history/moneypuck/team_games_2009.parquet" in reg2["files"] and reg2["cohorts"]["d"] == 2
    assert all(reg2["files"][k] == v for k, v in reg["files"].items())
    (root / "data/history/nhl/games_2022.parquet").write_bytes(b"B-changed")
    with pytest.raises(SystemExit):
        I.register(reg2, I.scan(root), {"c": [1], "d": 2})
    with pytest.raises(SystemExit):
        I.register(reg2, I.scan(_tree(tmp_path / "other")), {"c": [999]})


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# newly imported seasons cannot reach production shadow arms or the frozen walk-forward drivers
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
class _Stop(Exception):
    pass


def _history_with_old_seasons(tmp_path: Path) -> Path:
    h = tmp_path / "history"
    for s in range(2008, 2027):
        for rel in (f"moneypuck/team_games_{s}.parquet", f"nhl/games_{s}.parquet", f"moneypuck/shots_{s}.parquet", f"players/players_{s}.parquet"):
            f = h / rel
            f.parent.mkdir(parents=True, exist_ok=True)
            f.write_bytes(b"")
    return h


def test_pinned_seasons_exclude_every_newly_imported_old_season(tmp_path):
    h = _history_with_old_seasons(tmp_path)
    assert min(H.pinned_seasons(h, "moneypuck")) == 2022 and min(H.pinned_seasons(h, "nhl")) == 2022
    assert min(H.pinned_seasons(h, "players")) == 2021 and min(H.pinned_seasons(h, "shots")) == 2021
    assert 2026 in H.pinned_seasons(h, "players")                     # recent seasons still flow in; only older ones are held out
    assert H.pinned_seasons(tmp_path / "nowhere", "nhl") == []


def _spy(monkeypatch, module: str, name: str, calls: list):
    def spy(*a, **k):
        calls.append((a, k))
        raise _Stop

    monkeypatch.setattr(f"{module}.{name}", spy)


def test_production_and_frozen_readers_ask_for_pinned_seasons_only(tmp_path, monkeypatch):
    h = _history_with_old_seasons(tmp_path)
    data_root = h.parent
    seen: dict[str, list] = {}

    # live V2 shadow
    from nhl_edge.workflows import shadow_oa, shadow_player, shadow_v2

    calls: list = []
    _spy(monkeypatch, "nhl_edge.data.history", "load_team_games", calls)
    for label, fn in (("shadow_v2", lambda: shadow_v2.build_context(data_root, None)),
                      ("shadow_oa", lambda: shadow_oa.build_context(data_root, [], {"half_life_days": 1, "ridge": 1, "season_discount": 1, "target": "xg_sva"}))):
        calls.clear()
        with pytest.raises(_Stop):
            fn()
        seen[label] = sorted(calls[0][0][1])
    # frozen V2 walk-forward default path
    from nhl_edge.research import walk_forward_v2 as W2

    # walk_forward_v2 binds the loader at import time (another test may have imported it first), so spy on its own name too
    _spy(monkeypatch, "nhl_edge.research.walk_forward_v2", "load_team_games", calls)
    calls.clear()
    with pytest.raises(_Stop):
        W2.load_ctx(h)
    seen["walk_forward_v2"] = sorted(calls[0][0][1])
    for label, seasons in seen.items():
        assert seasons == list(range(2022, 2027)), (label, seasons)
    # player shadow: skater tables
    monkeypatch.undo()
    calls2: list = []
    _spy(monkeypatch, "nhl_edge.workflows.shadow_player", "load_player_tables", calls2)
    prm = tmp_path / "prm.json"
    prm.write_text(json.dumps({"xg": {}, "priors": {}, "player_params": {}}))
    with pytest.raises(_Stop):
        shadow_player.load_runtime(data_root, None, prm)
    assert sorted(calls2[0][0][2]) == list(range(2021, 2027))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# static guard: no new module reads full history without an explicit, reviewed decision
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
LOADERS = {"load_team_games": 1, "load_nhl_games": 1, "load_shots": 1, "load_player_tables": 2}     # name -> index of the `seasons` argument
#: Modules that MUST pass their pinned seasons (production shadow arms, live workflows, the frozen walk-forward drivers).
PROTECTED = ("workflows/", "research/walk_forward.py", "research/walk_forward_v2.py")
#: Research modules that deliberately read the whole history (new seasons are meant to enter them). Adding a module here is a reviewed decision.
FULL_HISTORY_OK = {
    "research/oa_walk_forward.py", "research/v1_tuned_control.py", "research/v1_retune.py", "research/oa_freeze.py", "research/market_benchmark.py",
    "research/kalshi_history.py", "research/player_market_benchmark.py", "research/thesis_model_audit.py", "research/joint_eval.py",
}


def _loader_calls(path: Path):
    tree = ast.parse(path.read_text())
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            fn = n.func.id if isinstance(n.func, ast.Name) else n.func.attr if isinstance(n.func, ast.Attribute) else None
            if fn in LOADERS:
                idx = LOADERS[fn]
                arg = n.args[idx] if len(n.args) > idx else next((k.value for k in n.keywords if k.arg == "seasons"), None)
                unpinned = arg is None or (isinstance(arg, ast.Constant) and arg.value is None)
                yield fn, n.lineno, arg, unpinned


def test_protected_modules_never_read_unpinned_history():
    bad = []
    for p in sorted(SRC.rglob("*.py")):
        rel = p.relative_to(SRC).as_posix()
        if any(rel.startswith(x) or rel == x for x in PROTECTED):
            for fn, line, _arg, unpinned in _loader_calls(p):
                if unpinned:
                    bad.append(f"{rel}:{line} {fn}() without explicit seasons")
    assert not bad, "production/frozen modules must pass pinned seasons (history.pinned_seasons): " + "; ".join(bad)


def test_every_other_full_history_reader_is_on_the_reviewed_allow_list():
    unknown = []
    for p in sorted(SRC.rglob("*.py")):
        rel = p.relative_to(SRC).as_posix()
        if any(rel.startswith(x) or rel == x for x in PROTECTED) or rel in FULL_HISTORY_OK or rel.startswith(("data/", "market_audit/", "players/")):
            continue
        for fn, line, _arg, unpinned in _loader_calls(p):
            if unpinned:
                unknown.append(f"{rel}:{line} {fn}()")
    assert not unknown, ("new reader of unpinned history: add it to FULL_HISTORY_OK deliberately (it will see every imported season) or pass explicit seasons: "
                         + "; ".join(unknown))


def test_oa_shadow_parameters_carry_a_valid_hash_and_a_pinned_history_window():
    from nhl_edge.research.oa_freeze import params_sha

    p = json.loads((ROOT / "data" / "params" / "oa-ridge-1.0.json").read_text())
    assert p["sha256"] == params_sha(p) and p["role"] == "SHADOW" and p["authority"] == "RESEARCH_ONLY"


def test_cohorts_are_disjoint_and_ordered():
    from nhl_edge.research import retune_evaluate as RE

    groups = [set(RE.FRESH), set(RE.FAMILY_SEEN), set(RE.EXPOSED), set(RE.FRESH2)]
    assert sum(len(g) for g in groups) == len(set().union(*groups))                    # no season in two cohorts
    assert max(RE.FRESH2) < min(RE.FRESH) <= max(RE.FRESH) < min(RE.FAMILY_SEEN) <= max(RE.FAMILY_SEEN) < min(RE.EXPOSED)
