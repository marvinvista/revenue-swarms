#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

README_GENERATED_START = "<!-- GENERATED SWARMS START -->"
README_GENERATED_END = "<!-- GENERATED SWARMS END -->"

METADATA_PATH = ROOT / "scripts" / "swarm_metadata.json"

REQUIRED_FRONTMATTER = {"name", "description"}
REQUIRED_METADATA_FIELDS = {"category", "readme_order", "summary"}

CATEGORY_DEFINITIONS = (
    {
        "slug": "narrative-and-product-marketing",
        "title": "Narrative And Product Marketing",
        "description": (
            "Use when you need a sharper story, clearer buyer language, and stronger "
            "problem-solution framing before doing more selling work."
        ),
    },
    {
        "slug": "sales-materials",
        "title": "Sales Materials",
        "description": (
            "Use when you need to turn the core narrative into sales decks, demo structure, "
            "outreach assets, and other reusable selling materials."
        ),
    },
    {
        "slug": "prospecting",
        "title": "Prospecting",
        "description": (
            "Use when you need to define who to target, what signals matter, and which accounts "
            "deserve attention now."
        ),
    },
    {
        "slug": "account-research-and-planning",
        "title": "Account Research And Planning",
        "description": (
            "Use when you need a compact account view before outreach, discovery, or deal work."
        ),
    },
    {
        "slug": "outreach-and-appointment-setting",
        "title": "Outreach And Appointment Setting",
        "description": (
            "Use when you need more disciplined outbound, better hooks, and cleaner sequencing "
            "to earn first meetings."
        ),
    },
    {
        "slug": "inbound-qualification",
        "title": "Inbound Qualification",
        "description": (
            "Use when you need to judge fit, urgency, and the right next step for inbound demand."
        ),
    },
    {
        "slug": "account-penetration",
        "title": "Account Penetration",
        "description": (
            "Use when you need coordinated multi-threading across a buying committee, not just "
            "one message."
        ),
    },
    {
        "slug": "discovery-demo-and-pitching",
        "title": "Discovery, Demo, And Pitching",
        "description": (
            "Use when you need stronger discovery, demo tailoring, objection handling, and "
            "meeting prep for an active opportunity."
        ),
    },
    {
        "slug": "closing-and-pipeline-management",
        "title": "Closing And Pipeline Management",
        "description": (
            "Use when you need sharper deal judgment, close plans, and forecast realism once the "
            "work has moved down-funnel."
        ),
    },
    {
        "slug": "customer-success",
        "title": "Customer Success",
        "description": (
            "Use when you need stronger onboarding, adoption, renewal readiness, and expansion "
            "support after the deal is closed."
        ),
    },
)

CATEGORY_BY_SLUG = {category["slug"]: category for category in CATEGORY_DEFINITIONS}


@dataclass(frozen=True)
class SwarmRecord:
    name: str
    path: Path
    category: str
    readme_order: int
    summary: str
    description: str
    display_name: str
    short_description: str
    default_prompt: str


def parse_frontmatter_text(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}

    lines = text.splitlines()
    end = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break

    if end is None:
        return {}

    frontmatter: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def parse_frontmatter(path: Path) -> dict[str, str]:
    return parse_frontmatter_text(path.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def load_swarm_metadata() -> dict[str, dict[str, object]]:
    return json.loads(METADATA_PATH.read_text(encoding="utf-8"))


def parse_openai_yaml(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def iter_swarm_dirs(root: Path = ROOT) -> list[Path]:
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and not path.name.startswith(".") and (path / "SKILL.md").exists()
    )


def load_swarm_record(swarm_dir: Path) -> SwarmRecord:
    frontmatter = parse_frontmatter(swarm_dir / "SKILL.md")
    metadata = load_swarm_metadata()[swarm_dir.name]
    ui = parse_openai_yaml(swarm_dir / "agents" / "openai.yaml")

    readme_order = int(metadata["readme_order"])

    return SwarmRecord(
        name=frontmatter.get("name", swarm_dir.name),
        path=swarm_dir,
        category=str(metadata["category"]).strip(),
        readme_order=readme_order,
        summary=str(metadata["summary"]).strip(),
        description=frontmatter.get("description", "").strip(),
        display_name=ui.get("display_name", swarm_dir.name),
        short_description=ui.get("short_description", ""),
        default_prompt=ui.get("default_prompt", ""),
    )


def load_swarm_records(root: Path = ROOT) -> list[SwarmRecord]:
    return [load_swarm_record(path) for path in iter_swarm_dirs(root)]


def build_generated_readme_section(records: list[SwarmRecord]) -> str:
    lines = [
        "## Swarms",
        "",
    ]

    for category in CATEGORY_DEFINITIONS:
        swarms = sorted(
            (
                record
                for record in records
                if record.category == category["slug"]
            ),
            key=lambda record: (record.readme_order, record.display_name),
        )
        if not swarms:
            continue

        lines.append(f"### {category['title']}")
        lines.append("")
        lines.append(category["description"])
        lines.append("")
        lines.append("| Swarm | Folder | Description |")
        lines.append("| --- | --- | --- |")
        for swarm in swarms:
            lines.append(
                f"| {swarm.display_name} | `{swarm.name}` | {swarm.summary} |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def replace_generated_readme_section(readme_text: str, generated_section: str) -> str:
    pattern = re.compile(
        rf"{re.escape(README_GENERATED_START)}\n.*?\n{re.escape(README_GENERATED_END)}",
        re.DOTALL,
    )
    replacement = (
        f"{README_GENERATED_START}\n"
        f"{generated_section}"
        f"{README_GENERATED_END}"
    )

    if not pattern.search(readme_text):
        raise ValueError("README.md is missing generated section markers")

    return pattern.sub(replacement, readme_text, count=1)
