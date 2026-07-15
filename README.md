# Culinary Ops

An evidence-based cookbook and cooking knowledge base built around continuous improvement.

The goal is to create reliable recipes, learn from every cook, and make that knowledge easy to use. Engineering principles help organize the work, but the repository is written for cooks rather than software engineers.

## Motto

**Kaizen** - Continuous Improvement

*It Can Always Be Better.*

Every cook is an experiment.
Every experiment produces observations.
Every observation improves the recipe.

## Philosophy

Culinary Ops treats recipes as living documents. Experiments explain how they improve, measurements make results easier to repeat, and equipment notes capture the behavior of the tools in our actual kitchen.

The objective is straightforward:

- Understand why a technique works.
- Prefer measurement over estimation.
- Treat temperature as a variable, not a suggestion.
- Record useful observations.
- Improve one variable at a time when practical.
- Turn successful results into clear, repeatable recipes.

## Inspiration

This project is heavily inspired by the evidence-based cooking philosophies of:

- Chris Young
- Heston Blumenthal

Their emphasis on heat transfer, measurement, experimentation, and scientific reasoning guides how recipes are developed and refined.

## Repository Layout

```text
recipes/
    The current best-known version of each dish, organized by food type.

experiments/
    Notes and results from individual cooks and planned tests.

equipment/
    What each tool can do, how to use it safely, and lessons about our specific equipment.

techniques/
    Reusable cooking skills and methods that apply across recipes.

collections/
    Curated groups of recipes organized by practical needs such as speed, budget, cleanup, or equipment.

meals/
    Complete meal combinations, timelines, shopping plans, and component maps.

templates/
    Consistent starting points for recipes, experiments, equipment guides, and meals.
```

## How the Pieces Work Together

- Open a **recipe** when you want to make something.
- Follow its **Required Equipment** links when you need information about a tool.
- Read an **experiment** when you want to understand what happened during a test cook.
- Use **techniques** to learn skills that apply to many dishes.
- Browse **collections** when deciding what to cook.
- Use **meals** when coordinating multiple recipes into one dinner.

Each piece of information should have one clear home. Other documents link to it rather than copying it.

## Recipe Status

- **Experimental:** Still being actively tested.
- **Tested:** Successfully cooked at least once but still being refined.
- **Validated:** Repeated successfully and reliable enough to recommend.

Recipes are the canonical current version. Git preserves their revision history, and experiment logs preserve the observations behind each change.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the organization rules, recipe structure, equipment guidance, and writing style.

> A recipe is simply the best method we know today. Tomorrow's experiment may improve it.
