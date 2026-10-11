"""Runtime non-leakage proof for NHL_SHOT_VOLUME_V1 with the vendored pure_gate ``rerun`` (RESEARCH_ONLY).

Runs the actual upstream model (``python -m nhl_edge.research.shot_volume_v1 --mode rerun``) on a fixed snapshot of
six 2025-26 games with the market file normal (twice), deleted and randomized; the PURE output must be bit-identical.
The negative control is the same command with ``--use-market-center`` (the existing MARKET_ANCHORED_PLAYER_V1 blend on
quoted assists / points thresholds), which must change or fail under every mutation.

Run from the repository root: ``python scripts/research_pure_rerun.py [--workdir DIR] [--out result.json]``
"""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAMES = "2025020853,2025020854,2025020876,2025020931,2025020946,2025020957"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--n-sims", type=int, default=2000)
    a = ap.parse_args()
    py = shlex.quote(sys.executable)
    model = (f"{py} -m nhl_edge.research.shot_volume_v1 --mode rerun --season 2025 --game-ids {GAMES} --n-sims {a.n_sims} "
             "--history {sports[history]} --wf-games {sports[wf]} --market {market[kalshi_quotes]} --out {out} --seed {seed}")
    control = model + " --use-market-center"
    cmd = [sys.executable, "-I", str(ROOT / "tools" / "pure_gate" / "pure_gate.py"), "rerun",
           "--manifest", str(ROOT / "docs" / "research" / "opportunity_efficiency" / "rerun" / "manifest.json"),
           "--model-cmd", model, "--control-cmd", control, "--seed", "7", "--mutation-seed", "20261011", "--random-draws", "2"]
    if a.workdir:
        cmd += ["--workdir", a.workdir]
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    sys.stdout.write(p.stdout)
    sys.stderr.write(p.stderr)
    if a.out:
        Path(a.out).write_text(p.stdout)
    return p.returncode


if __name__ == "__main__":
    sys.exit(main())
