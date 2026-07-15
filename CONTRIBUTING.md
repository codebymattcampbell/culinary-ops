# Contributing to Culinary Ops

This repository is designed to remain understandable to cooks who have no software or Git background. Engineering ideas may guide the organization, but folder names and documents should use ordinary culinary language.

## One Home for Each Kind of Information

- **Recipes** explain how to make a dish.
- **Experiments** record what happened during a specific cook or test.
- **Equipment** explains what a tool can do, how to use it safely, and what we have learned about our specific model.
- **Techniques** explain reusable cooking skills.
- **Collections** group recipes by practical needs such as speed, budget, or equipment.
- **Meals** combine recipes into a complete menu, timeline, or plan.
- **Templates** provide consistent starting points for new documents.

Do not duplicate a recipe under an equipment folder or collection. Link to its canonical location instead.

## Recipe Structure

A recipe should normally include:

1. Title and brief description
2. Status
3. Yield
4. Required Equipment
5. Helpful but Optional equipment, when relevant
6. Ingredients
7. Method
8. Quality targets or doneness checks
9. Variables to record while experimental
10. Links to related experiments, techniques, or equipment guides

Link major equipment entries from the Required Equipment section.

## Recipe Status

- **Experimental:** Not yet cooked enough to trust without active observation.
- **Tested:** Successfully cooked at least once, but still being refined.
- **Validated:** Repeated successfully with results that are reliable enough to recommend.

Recipes are the current best-known version. Git preserves revision history, while experiment logs preserve the reasoning and observations behind changes.

## Equipment Guides

Equipment guides contain general information and a separate **Our Equipment Notes** section for model-specific details, quirks, maintenance, and lessons learned.

When a cook reveals a tool-specific issue, update the equipment guide. When it reveals a dish-specific issue, update the recipe or its experiment log.

## Writing Style

- Prefer plain language over engineering terminology.
- Explain specialized culinary terms when they first appear.
- Use measurements, temperatures, and observable doneness checks whenever practical.
- Write instructions that a new cook can follow without needing repository knowledge.
