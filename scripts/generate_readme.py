#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys

from swarm_catalog import (
    ROOT,
    build_generated_readme_section,
    load_swarm_records,
    replace_generated_readme_section,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the README swarms section")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if README.md is not up to date",
    )
    args = parser.parse_args()

    readme_path = ROOT / "README.md"
    current = readme_path.read_text(encoding="utf-8")
    generated_section = build_generated_readme_section(load_swarm_records())
    updated = replace_generated_readme_section(current, generated_section)

    if args.check:
        if updated != current:
            print(
                "README.md is out of date. Run python3 scripts/generate_readme.py",
                file=sys.stderr,
            )
            return 1
        print("README.md is up to date")
        return 0

    readme_path.write_text(updated, encoding="utf-8")
    print("Updated README.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
