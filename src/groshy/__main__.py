import argparse

from groshy.recipe import Recipe

parser = argparse.ArgumentParser(description="A tool to collect recipes")

parser.add_argument("recipe")

args = parser.parse_args()

new_recipe = Recipe(args.recipe)

print(new_recipe.name)

for ingredient in new_recipe.ingredients:
    print(ingredient)