from __future__ import annotations
import datetime as dt

import nltk
import requests
import ingredient_parser as ip
from recipe_scrapers import scrape_html
from recipe_scrapers import _exceptions as exc
from pydantic import BaseModel

# import groshy.errors as errs
from groshy.ingredient import Ingredient


class Recipe(BaseModel):
    """Primary data class which holds recipe scraped from internet or manually
        Fields:
            - name (str)
            - description (str)
            - ingredients (list[str])
            - instructions (list[str])
            - cuisine (str): i.e. Soul Food, American, etc...
            - category (str)
            - yields (str): Defaults to '1 Serving'
            - cooking_time (int): Defaults to 0 in units of minutes
            - price (float): Defaults to 0.0
            
        Methods:
            - prep_ingredients -> list[Ingredient]
            - write_recipe -> Recipe
            - fetch_recipe -> Recipe"""
    name: str
    description: str
    ingredients: list[dict]
    instructions: list[str]
    cuisine: str | None = "N/A"
    category: str | None = "N/A"
    yields: str = "1 serving"
    cooking_time: int = 0
    price: float = 0.0

    def prep_ingredients(self) -> list[Ingredient]:
        """ Converts list of strings into a list of Ingredient objects with default 
        last_bought values of today"""

        ingredients_list = []
        for x in self.ingredients:
            ingredients_list.append(Ingredient(name=x["name"], last_bought=dt.date.today()))

        return ingredients_list

    @classmethod
    def fetch_recipe(cls, url:str) -> Recipe:
        """ Retrieves information about the recipe using a provided URL """

        success = False
        rec = cls.make_empty_recipe()
        try:
            html = requests.get(url)
            if html.status_code == 403:
                print("Website has forbidden scraping, please manually enter recipe")
                raise Exception
            _rec = scrape_html(html=html.text, org_url=url)
            success = True
        except exc.WebsiteNotImplementedError:
            try:
                print("In WILDMODE")
                _rec = scrape_html(html=html.text, org_url=url, wild_mode=True)
                success = True
            except exc.NoSchemaFoundInWildMode as e:
                print(e)
                # raise errs.BadURLError
        finally:
            if success:
                recd = _rec.to_json()
                ingredients = Recipe.gather_ingredients(recd['ingredients'])
                recd.update({"ingredients": ingredients})
                # test_unpacking(**recd)
                recd = Recipe._extract_recipe_fields(recd)
                rec = Recipe(**recd)
            
            return rec

    @classmethod
    def make_empty_recipe(cls) -> Recipe:
        return Recipe(name="N/A", 
                      description="N/A", 
                      ingredients=[{"N/A": "N/A"}], 
                      instructions=["N/A"], 
                      cuisine="N/A", 
                      category="N/A",
                      yields="N/A",
                      cooking_time=0,
                      price=0)

    @staticmethod
    def gather_ingredients(ingredient_list: list[str]) -> list[dict]:
        """ Parses str list of ingredients into ingredient dicts using the 
        ingredient_parser package. """

        parsed = []
        try:
            nltk.data.find('averaged_perceptron_tagger')
        except LookupError:
            nltk.download("averaged_perceptron_tagger", quiet=True)

        for gredient in ingredient_list:
            ingredient = dict.fromkeys(["name", "amount", "unit"])

            parsed_ingredient = ip.parse_ingredient(gredient)

            try:
                ingredient_amount = parsed_ingredient.amount[0]
            except IndexError:
                ingredient_amount = "some"
                pass

            ingredient["name"] = parsed_ingredient.name.text # type: ignore
            if ingredient_amount == "some":
                ingredient["amount"] = ingredient_amount
                ingredient["unit"] = "N/A"
            else:
                ingredient["amount"] = ingredient_amount.quantity
                ingredient["unit"] = str(ingredient_amount.unit)

            parsed.append(ingredient)

        return parsed

    @staticmethod
    def _extract_recipe_fields(recdict: dict):
        data_fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "cuisine",
            "category",
            "yields",
            "total_time",
        ]

        model_fields = Recipe.model_fields.keys()

        rec_dict = {}
        for data, field in zip(data_fields, model_fields):
            try:
                if data == "instructions":
                    rec_dict[field] = recdict[data].splitlines()
                else:
                    rec_dict[field] = recdict[data]
            except KeyError as ex:
                print(f"Recipe '{recdict['title']}' does not have attribute {ex}")
                if field == "description":
                    rec_dict[field] = recdict["title"]
                elif field == "cuisine":
                    rec_dict[field] = recdict["category"]

        return rec_dict
