#!/usr/bin/env python3
"""Create missing v1 experiment files for every recipe.

The recipes directory is the source of truth. For each Markdown recipe at:

    recipes/<cuisine>/<category>/<recipe>.md

this script ensures the following file exists:

    experiments/<category>/<recipe>/v1.md

Cuisine is omitted from experiment paths. Existing linked histories are reused,
including dated logs and bread histories without the bread-machine subcategory.
Legacy recipes awaiting a cuisine decision are also supported.
Existing experiment files are never overwritten or deleted.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES_DIR = ROOT / "recipes"
EXPERIMENTS_DIR = ROOT / "experiments"
TEMPLATE_PATH = ROOT / "templates" / "experiment.md"

# Food categories distinguish legacy paths from cuisine-first paths.
CATEGORIES = {"beef", "breads", "chicken", "lamb", "pork", "rice", "salads",
              "sauces", "turkey", "vegetables", "seafood", "fish", "shrimp",
              "desserts", "pasta", "soups", "beans", "eggs"}


def experiment_directory(recipe_path: Path) -> Path:
    """Preserve a linked history, or resolve the food-category destination."""
    for link in re.findall(r"\]\(([^\s)]+)\)", recipe_path.read_text(encoding="utf-8")):
        target = (recipe_path.parent / link.split("#", 1)[0]).resolve()
        if target.is_relative_to(EXPERIMENTS_DIR.resolve()) and target.exists():
            return target if target.is_dir() else target.parent

    relative = recipe_path.relative_to(RECIPES_DIR)
    if len(relative.parts) >= 3 and relative.parts[1] in CATEGORIES:
        relative = Path(*relative.parts[1:])
    destination = EXPERIMENTS_DIR / relative.with_suffix("")
    # Bread-machine recipes have historically kept logs directly under breads.
    if len(relative.parts) > 2:
        existing = EXPERIMENTS_DIR / relative.parts[0] / relative.stem
        if existing.is_dir():
            return existing
    return destination


def title_from_slug(slug: str) -> str:
    """Turn a kebab-case file name into a readable title."""
    return " ".join(word.capitalize() for word in re.split(r"[-_]+", slug))


def build_experiment(recipe_path: Path, destination: Path, template: str) -> str:
    recipe_name = title_from_slug(recipe_path.stem)
    recipe_link = Path(os.path.relpath(recipe_path, destination.parent)).as_posix()

    content = template.replace(
        "# Experiment - Name - v1",
        f"# Experiment - {recipe_name} - v1",
        1,
    )
    content = content.replace(
        "- Related Recipe:",
        f"- Related Recipe: [{recipe_name}]({recipe_link})",
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

        history = experiment_directory(recipe_path)
        destination = history / "v1.md"

        if any(history.glob("*.md")):
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
