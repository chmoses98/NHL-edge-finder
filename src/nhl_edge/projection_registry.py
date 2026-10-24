"""Which model publishes each projection target (RESEARCH_ONLY; never touches prices, stakes, caps or routing).

``data/registry/projection-registry.json`` names, per target, the model whose number appears in the published game-level fields. The default is the current
champion (``DATA_ONLY_V1``). A non-default value is honoured **only** with a complete approval record
``{"approved_by": ..., "approved_at_utc": ..., "evidence": ...}``; without one the loader falls back to the default and says why. Merging this module therefore cannot
promote anything, and promoting is one reviewed change to the JSON (reversible by setting the value back).

The overtime target replaces, per game, ``p_reg_tie``, ``p_overtime``, ``p_home_reg_win``, ``p_away_reg_win`` and ``p_shootout`` of the slate game with the
DATA_ONLY_V2 shadow's values **all together** (never a mixture), records the V1 values and the decision in an additive ``overtime_model`` block, and falls back to V1
for any game whose V2 numbers are missing or not finite. Contract prices (the ``predictions`` rows, including the overtime contract) are not touched.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

from nhl_edge.config import REPO_ROOT

REGISTRY_PATH = REPO_ROOT / "data" / "registry" / "projection-registry.json"
DEFAULT_MODEL = "DATA_ONLY_V1"
OVERTIME_FIELDS = ("p_reg_tie", "p_overtime", "p_home_reg_win", "p_away_reg_win", "p_shootout")
APPROVAL_KEYS = ("approved_by", "approved_at_utc", "evidence")


def _approved(entry: dict[str, Any]) -> bool:
    a = entry.get("approval")
    return isinstance(a, dict) and all(isinstance(a.get(k), str) and a[k].strip() for k in APPROVAL_KEYS)


def published_model(target: str, path: Path | None = None) -> tuple[str, str | None]:
    """(model that publishes ``target``, reason it is the default despite a request, or None). Never raises: any problem means the default."""
    p = Path(path) if path else REGISTRY_PATH
    try:
        entry = json.loads(p.read_text())["targets"][target]
        want = str(entry["published_model"])
    except (OSError, ValueError, KeyError, TypeError) as e:
        return DEFAULT_MODEL, f"registry unreadable ({type(e).__name__}); default {DEFAULT_MODEL}"
    if want == DEFAULT_MODEL:
        return DEFAULT_MODEL, None
    if want != str(entry.get("candidate")):
        return DEFAULT_MODEL, f"{want!r} is not the registered candidate; default {DEFAULT_MODEL}"
    if not _approved(entry):
        return DEFAULT_MODEL, f"{want} requested but no complete approval record; default {DEFAULT_MODEL}"
    return want, None


def _finite(block: dict[str, Any]) -> bool:
    return all(isinstance(block.get(k), (int, float)) and math.isfinite(float(block[k])) and 0.0 <= float(block[k]) <= 1.0 for k in OVERTIME_FIELDS)


def apply_overtime(games: list[dict[str, Any]], v2_blocks: list[dict[str, Any]] | None, path: Path | None = None) -> dict[str, Any]:
    """Mutates ``games`` (slate game dicts) in place when the registry publishes the overtime target from DATA_ONLY_V2; returns a small report.

    At the default nothing is added or changed (byte-identical documents); otherwise every game gets an additive ``overtime_model`` block naming the published model.
    """
    model, why = published_model("overtime", path)
    by_game = {str(b.get("game_id")): b for b in (v2_blocks or [])}
    n_v2 = n_fallback = 0
    for g in games:
        v1 = {k: g.get(k) for k in OVERTIME_FIELDS}
        block = (by_game.get(str(g.get("game_id"))) or {}).get("v2") or {}
        if model == DEFAULT_MODEL:
            continue                                      # default: the published documents are left exactly as they were (byte-identical)
        meta: dict[str, Any] = {"published": DEFAULT_MODEL, "fallback": False, "v1": v1}
        if _finite(block):
            for k in OVERTIME_FIELDS:
                g[k] = float(block[k])
            meta["published"] = model
            n_v2 += 1
        else:
            meta["fallback"] = True
            meta["fallback_reason"] = "DATA_ONLY_V2 numbers missing or not finite for this game"
            n_fallback += 1
        g["overtime_model"] = meta
    return {"target": "overtime", "published_model": model, "default_reason": why, "games": len(games), "from_v2": n_v2, "fallback": n_fallback}
