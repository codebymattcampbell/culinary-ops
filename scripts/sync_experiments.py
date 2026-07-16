#!/usr/bin/env python3
"""Create missing v1 experiment files for every recipe.

The recipes directory is the source of truth. For each Markdown recipe at:

    recipes/<category>/<recipe>.md

this script ensures the following file exists:

    experiments/<category>/<recipe>/v1.md

Existing experiment files are never overwritten or deleted.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES_DIR = ROOT / "recipes"
EXPERIMENTS_DIR = ROOT / "experiments"
TEMPLATE_PATH = ROOT / "templates" / "experiment.md"


def title_from_slug(slug: str) -> str:
    """Turn a kebab-case file name into a readable title."""
    return " ".join(word.capitalize() for word in re.split(r"[-_]+", slug))


def build_experiment(recipe_path: Path, destination: Path, template: str) -> str:
    recipe_name = title_from_slug(recipe_path.stem)
    recipe_link = Path("../../../") / recipe_path.relative_to(ROOT)

    content = template.replace(
        "# Experiment - Name - v1",
        f"# Experiment - {recipe_name} - v1",
        1,
    )
    content = content.replace(
        "- Related Recipe:",
        f"- Related Recipe: [{recipe_name}]({recipe_link.as_posix()})",
        1,
    )
    return content


def main() -> int:
    if not RECIPES_DIR.is_dir():
        print(f"Missing recipes directory: {RECIPES_DIR}", file=sys.stderr)
        return 1

    if not TEMPLATE_PATH.is_file():
        print(f"Missing experiment template: {TEMPLATE_PATH}", file=sys.stderr)
        return 1

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    created: list[Path] = []

    for recipe_path in sorted(RECIPES_DIR.rglob("*.md")):
        if recipe_path.name.lower() in {"readme.md", "index.md"}:
            continue

        relative_recipe = recipe_path.relative_to(RECIPES_DIR)
        destination = EXPERIMENTS_DIR / relative_recipe.with_suffix("") / "v1.md"

        if destination.exists():
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            build_experiment(recipe_path, destination, template),
            encoding="utf-8",
        )
        created.append(destination.relative_to(ROOT))

    if created:
        print("Created experiment skeletons:")
        for path in created:
            print(f"  - {path}")
    else:
        print("Experiment structure is already synchronized.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
