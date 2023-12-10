
import nltk
import ingredient_parser as ip
from recipe_scrapers import scrape_me
from recipe_scrapers import _exceptions as exc

from groshy.recipe import Recipe


def get_ingredients(json_rec) -> list:

    parsed = []
    nltk.download('averaged_perceptron_tagger', quiet=True)
    ing_str = json_rec['ingredients']

    for gredient in ing_str:
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


def extract_recipe_fields(recdict: dict):
    
    data_fields = ['title', 'description', 'ingredients', 'instructions', 'cuisine', 'category', 'yields', 'total_time']

    model_fields = Recipe.model_fields.keys()

    rec_dict = {}
    for data, field in zip(data_fields, model_fields):
        try:
            if data == 'instructions':
                rec_dict[field] = recdict[data].splitlines()
            else:
                rec_dict[field] = recdict[data]
        except KeyError as ex:
            print(f"Recipe {recdict['title']} does not have attribute {ex}")
            if field == 'description':
                rec_dict[field] = recdict['title']
            elif field == 'cuisine':
                rec_dict[field] = recdict['category']

    return rec_dict


def test_unpacking(**kwargs):
    for k in kwargs.items():
        print(k)


def get_recipe(url) -> bool | Recipe:
    success = False
    _rec = None
    try:
        _rec = scrape_me(url)
        success = True
    except exc.WebsiteNotImplementedError:
        try:
            print("In WILDMODE")
            _rec = scrape_me(url, wild_mode=True)
            success = True
        except exc.NoSchemaFoundInWildMode:
            print("No SCHEMA")
            # raise BadURLError
    finally:
        rec = _rec
        if success:
            recd = _rec.to_json()
            ingredients = get_ingredients(recd)
            recd.update({'ingredients': ingredients})
            test_unpacking(**recd)
            recd = extract_recipe_fields(recd)
            rec = Recipe(**recd)
        
        return rec
    

if __name__ == "__main__":

    # url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    # url = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/"
    url = "https://www.foodnetwork.com/recipes/food-network-kitchen/christmas-monster-cookies-3543357" # This works thanks to wild mode

    recipe = get_recipe(url)

    if recipe:
        print(recipe.model_dump())
        ing_objs = recipe.build_ingredients()

        for ing in ing_objs:
            print(ing.model_dump())

        