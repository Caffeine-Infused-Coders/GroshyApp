import pytest

from groshy.recipe import Recipe
from groshy.ingredient import Ingredient


def test_recipeBuilding(get_urls):

    for url in get_urls:
        recipe = Recipe.get_recipe(url)
        ingredients = recipe.build_ingredients()

        assert recipe
        assert type(ingredients[0]) is Ingredient