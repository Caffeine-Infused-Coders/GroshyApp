import pytest

from groshy.recipe import Recipe
from groshy.ingredient import Ingredient


def test_recipe_building(url):
    recipe = Recipe.fetch_recipe(url)
    ingredients = recipe.prep_ingredients()

    assert recipe
    for ingredient in ingredients:
        assert type(ingredient) is Ingredient


def test_recipe_dummy():
    recipe = Recipe._dummy_recipe()

    recipe_dict = recipe.model_dump()

    for value in recipe_dict.values():
        if isinstance(value, list) and isinstance(value[0], dict):
            assert len(value) == 1
            value = value[0].get("N/A")
        elif isinstance(value, list) and isinstance(value[0], str):
            value = value[0]
        assert value == "N/A" or value == 0

def test_manual_recipe():
    


