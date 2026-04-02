#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from swarm_catalog import (
    ROOT,
    build_generated_readme_section,
    iter_swarm_dirs,
    load_swarm_records,
    parse_frontmatter_text,
    parse_openai_yaml,
    replace_generated_readme_section,
)


CONTRACTS_PATH = ROOT / "tests" / "swarm_contracts.json"
REQUIRED_OPENAI_FIELDS = {"display_name", "short_description", "default_prompt"}


def load_contracts() -> dict[str, object]:
    return json.loads(CONTRACTS_PATH.read_text(encoding="utf-8"))


def main() -> int:
    errors: list[str] = []
    contracts = load_contracts()
    defaults = contracts["defaults"]
    swarm_contracts = contracts["swarms"]

    discovered = [path.name for path in iter_swarm_dirs()]
    missing_contracts = sorted(set(discovered) - set(swarm_contracts))
    extra_contracts = sorted(set(swarm_contracts) - set(discovered))

    if missing_contracts:
        errors.append(f"Missing contract entries for swarms: {missing_contracts}")
    if extra_contracts:
        errors.append(f"Contract entries exist for missing swarms: {extra_contracts}")

    for swarm_dir in iter_swarm_dirs():
        name = swarm_dir.name
        text = (swarm_dir / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = parse_frontmatter_text(text)
        contract = swarm_contracts.get(name, {})
        ui = parse_openai_yaml(swarm_dir / "agents" / "openai.yaml")

        if "description" not in frontmatter or "Use when" not in frontmatter["description"]:
            errors.append(f"{name}: frontmatter description must include 'Use when'")

        for heading in defaults["required_headings"]:
            if heading not in text:
                errors.append(f"{name}: missing required heading {heading}")

        for phrase in defaults["required_phrases"]:
            if phrase not in text:
                errors.append(f"{name}: missing required phrase {phrase}")

        for lane in contract.get("required_lane_headings", []):
            if lane not in text:
                errors.append(f"{name}: missing lane heading {lane}")

        for marker in contract.get("required_output_markers", []):
            if marker not in text:
                errors.append(f"{name}: missing output marker {marker}")

        skill_ui_missing = REQUIRED_OPENAI_FIELDS - set(ui)
        if skill_ui_missing:
            errors.append(f"{name}: agents/openai.yaml missing {sorted(skill_ui_missing)}")
        elif f"${name}" not in ui["default_prompt"]:
            errors.append(f"{name}: default_prompt must reference ${name}")

        openai_yaml = swarm_dir / "agents" / "openai.yaml"
        combined = text
        if openai_yaml.exists():
            combined += "\n" + openai_yaml.read_text(encoding="utf-8")

        for banned in defaults.get("banned_terms", []):
            if banned in combined:
                errors.append(f"{name}: banned public term found: {banned}")

    readme_path = ROOT / "README.md"
    current_readme = readme_path.read_text(encoding="utf-8")
    generated_section = build_generated_readme_section(load_swarm_records())
    expected_readme = replace_generated_readme_section(current_readme, generated_section)
    if expected_readme != current_readme:
        errors.append(
            "README.md is out of sync with swarm metadata. Run python3 scripts/generate_readme.py"
        )

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Contract tests passed for {len(discovered)} swarm(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
