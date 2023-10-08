import re

import nltk
import ingredient_parser as ip
from recipe_scrapers import scrape_me
from recipe_scrapers import _exceptions as exc


from Groshy.errors import BadURLError


def get_recipe(url):
    try:
        recipe = scrape_me(url)
    except exc.WebsiteNotImplementedError:
        try:
            recipe = scrape_me(url, wild_mode=True)
        except exc.NoSchemaFoundInWildMode:
            recipe = False
            raise BadURLError
    finally:
        return recipe


def get_ingredients(ingredients: list) -> list:

    parsed = []
    nltk.download('averaged_perceptron_tagger', quiet=True)

    for gredient in ingredients:
        ingredient = dict.fromkeys(["name", "amount", "unit"])

        parsed_ingredient = ip.parse_ingredient(gredient)

        try:
            ingredient_amount = parsed_ingredient.amount[0]
        except IndexError:
            ingredient_amount = "some"
            pass

        ingredient["name"] = parsed_ingredient.name.text
        if ingredient_amount == "some":
            ingredient["amount"] = ingredient_amount
            ingredient["unit"] = "N/A"
        else:
            ingredient["amount"] = ingredient_amount.quantity
            ingredient["unit"] = ingredient_amount.unit

        parsed.append(ingredient)

    return parsed
    

if __name__ == "__main__":

    # url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    url = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/" # This works thanks to wild mode

    recipe = get_recipe(url)
    
    pi = get_ingredients(recipe.ingredients())

    for ing in pi:
        print(ing)

        