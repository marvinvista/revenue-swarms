#!/usr/bin/env python3
from __future__ import annotations

import sys
from swarm_catalog import (
    CATEGORY_BY_SLUG,
    REQUIRED_METADATA_FIELDS,
    REQUIRED_FRONTMATTER,
    ROOT,
    iter_swarm_dirs,
    load_swarm_metadata,
    parse_frontmatter,
    parse_openai_yaml,
)


REQUIRED_OPENAI_FIELDS = {"display_name", "short_description", "default_prompt"}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    seen_readme_orders: set[tuple[str, int]] = set()
    metadata = load_swarm_metadata()

    swarms = iter_swarm_dirs()
    if not swarms:
        errors.append("No swarm folders found at the repository root.")

    discovered = [path.name for path in swarms]
    missing_metadata = sorted(set(discovered) - set(metadata))
    extra_metadata = sorted(set(metadata) - set(discovered))
    if missing_metadata:
        errors.append(f"Missing metadata entries for swarms: {missing_metadata}")
    if extra_metadata:
        errors.append(f"Metadata entries exist for missing swarms: {extra_metadata}")

    for swarm_dir in swarms:
        skill_md = swarm_dir / "SKILL.md"
        frontmatter = parse_frontmatter(skill_md)
        missing = REQUIRED_FRONTMATTER - set(frontmatter)
        if missing:
            errors.append(f"{swarm_dir.name}: missing frontmatter keys {sorted(missing)}")
            continue

        extra_frontmatter = sorted(set(frontmatter) - REQUIRED_FRONTMATTER)
        if extra_frontmatter:
            errors.append(
                f"{swarm_dir.name}: public SKILL.md frontmatter must only expose "
                f"{sorted(REQUIRED_FRONTMATTER)}; found extra keys {extra_frontmatter}"
            )

        if frontmatter["name"] != swarm_dir.name:
            errors.append(
                f"{swarm_dir.name}: frontmatter name must match folder name "
                f"({frontmatter['name']} != {swarm_dir.name})"
            )

        swarm_metadata = metadata.get(swarm_dir.name, {})
        missing_metadata_fields = REQUIRED_METADATA_FIELDS - set(swarm_metadata)
        if missing_metadata_fields:
            errors.append(
                f"{swarm_dir.name}: missing metadata keys {sorted(missing_metadata_fields)}"
            )
            continue

        category = str(swarm_metadata["category"]).strip()
        if category not in CATEGORY_BY_SLUG:
            errors.append(
                f"{swarm_dir.name}: category must be one of {sorted(CATEGORY_BY_SLUG)}"
            )

        summary = str(swarm_metadata["summary"]).strip()
        if not summary:
            errors.append(f"{swarm_dir.name}: summary must not be empty")

        raw_readme_order = str(swarm_metadata["readme_order"]).strip()
        try:
            readme_order = int(raw_readme_order)
        except ValueError:
            errors.append(f"{swarm_dir.name}: readme_order must be an integer")
        else:
            if readme_order <= 0:
                errors.append(f"{swarm_dir.name}: readme_order must be positive")
            key = (category, readme_order)
            if key in seen_readme_orders:
                errors.append(
                    f"{swarm_dir.name}: duplicate readme_order {readme_order} in category {category}"
                )
            seen_readme_orders.add(key)

        if len(skill_md.read_text(encoding='utf-8').splitlines()) > 500:
            warnings.append(f"{swarm_dir.name}: SKILL.md is longer than 500 lines")

        openai_yaml = swarm_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            ui = parse_openai_yaml(openai_yaml)
            missing_ui = REQUIRED_OPENAI_FIELDS - set(ui)
            if missing_ui:
                errors.append(
                    f"{swarm_dir.name}: agents/openai.yaml is missing {sorted(missing_ui)}"
                )

        references_dir = swarm_dir / "references"
        if references_dir.exists():
            for path in references_dir.iterdir():
                if path.is_file() and path.suffix != ".md":
                    errors.append(
                        f"{swarm_dir.name}: references contains non-markdown file {path.name}"
                    )

    for warning in warnings:
        print(f"warning: {warning}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(swarms)} swarm(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
