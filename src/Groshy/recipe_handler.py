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
    
def parse_ingredients(ingredients: list) -> list:

    parsed = []
    nltk.download('averaged_perceptron_tagger', "./nltk-packages/", True)

    for ing in ingredients:
        pi = ip.parse_ingredient(ing)
        parsed.append(pi)

    return parsed
    

if __name__ == "__main__":

    #url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    url = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/" # This works thanks to wild mode

    recipe = get_recipe(url)
    
    pi = parse_ingredients(recipe.ingredients())

    for ing in pi:
        print(ing)
        print(ing.name)