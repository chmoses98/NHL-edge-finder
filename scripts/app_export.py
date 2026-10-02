#!/usr/bin/env python
"""Publish the Edge Finder app documents (``edge_finder.app.v1``) from the archive.

    python scripts/app_export.py --data-root data/archive --out data/archive/app/latest \
        [--accounting-dir data/accounting] [--now 2026-10-02T17:30:00Z] [--commit-sha X] [--workflow-run-id Y]

Thin wrapper over :mod:`nhl_edge.app_export` (same as ``nhl app-export``). Exit 1 when the export failed; in that
case only ``health.json`` was rewritten and the previous payload stands.
"""

from __future__ import annotations

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for p in (os.path.join(REPO_ROOT, "src"), os.path.join(REPO_ROOT, "contract")):
    if p not in sys.path:
        sys.path.insert(0, p)

from nhl_edge.app_export import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
