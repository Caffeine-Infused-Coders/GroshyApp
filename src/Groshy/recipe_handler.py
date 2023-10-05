import re

import nltk
import ingredient_parser as ip
from recipe_scrapers import scrape_me
from recipe_scrapers import _exceptions as exc


from errors import BadURLError


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
    nltk.download('averaged_perceptron_tagger', "./nltk-packages/", True)

    for ing in ingredients:
        ingredient = dict.fromkeys(["name", "amount", "unit"])

        pi = ip.parse_ingredient(ing)
        amnt_dt = pi.amount[0]

        ingredient["name"] = pi.name.text
        ingredient["amount"] = amnt_dt.quantity
        ingredient["unit"] = amnt_dt.unit

        parsed.append(ingredient)

    return parsed
    

if __name__ == "__main__":

    #url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    url = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/" # This works thanks to wild mode

    recipe = get_recipe(url)
    
    pi = get_ingredients(recipe.ingredients())

    for ing in pi:
        print(ing)