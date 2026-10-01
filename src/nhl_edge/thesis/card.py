"""Card completion gate: a card is NOT COMPLETE unless every recommended bet carries all eighteen fields.

A field that cannot be calculated must be present as ``{"status": "UNKNOWN", "reason": "..."}`` (explained, never
silently omitted); a field that genuinely does not apply (a secondary thesis for a single-idea bet, pairwise
relationships for the only bet in a game) is ``{"status": "NOT_APPLICABLE", "reason": "..."}``. A missing or ``None``
field fails the gate. Every game with two or more recommended bets must also pass the JOINT CARD CHECK: a joint outcome
matrix from the same simulation draws covering EVERY pair of its recommended bets, with each pair's probability
identities satisfied, and each bet listing its relationship to every other same-game recommended bet.
"""

from __future__ import annotations

from typing import Any

from nhl_edge.thesis.joint import check_identities

REQUIRED_FIELDS: tuple[tuple[str, str], ...] = (
    ("contract", "market / exact contract"),
    ("team_opponent", "team and opponent"),
    ("executable_price", "executable price"),
    ("fair_probability", "fair probability"),
    ("estimated_edge", "estimated edge"),
    ("bet_up_to_price", "bet-up-to price"),
    ("recommended_stake", "recommended stake"),
    ("family_reliability", "market-family reliability"),
    ("primary_thesis", "primary thesis"),
    ("secondary_thesis", "secondary thesis if relevant"),
    ("best_alternative", "best alternative expression considered"),
    ("reason_chosen", "reason chosen over alternative"),
    ("thesis_concentration", "thesis concentration"),
    ("same_game_relationships", "relationship to every other same-game recommended bet"),
    ("same_game_exposure", "total same-game exposure"),
    ("thesis_exposure", "total thesis exposure"),
    ("portfolio_impact", "portfolio impact"),
    ("failure_case", "opposing reasons / failure case"),
)
NOT_APPLICABLE_OK = {"secondary_thesis", "best_alternative", "same_game_relationships"}


def unknown(reason: str) -> dict[str, str]:
    return {"status": "UNKNOWN", "reason": reason}


def not_applicable(reason: str) -> dict[str, str]:
    return {"status": "NOT_APPLICABLE", "reason": reason}


def _status(v: Any) -> str | None:
    return v.get("status") if isinstance(v, dict) and v.get("status") in ("UNKNOWN", "NOT_APPLICABLE") else None


def gate_entry(entry: dict[str, Any]) -> tuple[list[str], list[str]]:
    """(failures, unknown fields) for one card entry."""
    fails, unk = [], []
    for key, desc in REQUIRED_FIELDS:
        v = entry.get(key)
        if v is None or v == "" or v == []:
            fails.append(f"{entry.get('bet_id')}: missing '{desc}'")
            continue
        st = _status(v)
        if st and not str(v.get("reason") or "").strip():
            fails.append(f"{entry.get('bet_id')}: '{desc}' is {st} without an explanation")
        if st == "NOT_APPLICABLE" and key not in NOT_APPLICABLE_OK:
            fails.append(f"{entry.get('bet_id')}: '{desc}' cannot be NOT_APPLICABLE")
        if st == "UNKNOWN":
            unk.append(f"{entry.get('bet_id')}: {desc} UNKNOWN ({v.get('reason')})")
    return fails, unk


def joint_card_check(game_id: str, entries: list[dict[str, Any]], joint: dict[str, Any] | None) -> list[str]:
    """Failures for one game's recommended bets."""
    ids = [e["bet_id"] for e in entries]
    if len(ids) < 2:
        return [f"{game_id}: the only recommended bet lists relationships to bets that are not on the card" for e in entries
                if isinstance(e.get("same_game_relationships"), dict) and e["same_game_relationships"] and not _status(e["same_game_relationships"])]
    out = []
    if not joint or not joint.get("pairs"):
        return [f"{game_id}: {len(ids)} same-game bets without a joint outcome matrix (JOINT CARD CHECK failed)"]
    have = {frozenset((p["a"], p["b"])): p for p in joint["pairs"]}
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            p = have.get(frozenset((ids[i], ids[j])))
            if p is None:
                out.append(f"{game_id}: joint matrix lacks the pair {ids[i]} / {ids[j]}")
                continue
            bad = check_identities(p)
            if bad:
                out.append(f"{game_id}: pair {ids[i]} / {ids[j]} violates {bad}")
    for e in entries:
        rel = e.get("same_game_relationships")
        others = set(ids) - {e["bet_id"]}
        listed = set(rel.keys()) if isinstance(rel, dict) and not _status(rel) else set()
        if others - listed:
            out.append(f"{game_id}: {e['bet_id']} does not state its relationship to {sorted(others - listed)}")
    return out


def run_gate(entries_by_game: dict[str, list[dict[str, Any]]], joints: dict[str, dict[str, Any]]) -> dict[str, Any]:
    fails: list[str] = []
    unk: list[str] = []
    n = 0
    for gid, entries in entries_by_game.items():
        for e in entries:
            f, u = gate_entry(e)
            fails += f
            unk += u
            n += 1
        fails += joint_card_check(gid, entries, joints.get(gid))
    multi = [g for g, es in entries_by_game.items() if len(es) >= 2]
    return {"status": "PASS" if not fails else "FAIL", "n_entries": n, "failures": fails, "unknown_fields": unk,
            "games_with_joint_card_check": multi, "required_fields": [d for _, d in REQUIRED_FIELDS]}
