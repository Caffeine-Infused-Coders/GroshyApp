from dataclasses import dataclass

from pydantic import BaseModel
from groshy.ingredient import Ingredient


class Recipe(BaseModel):
    name: str
    description: str
    ingredients: list[dict]
    instructions: list[str]
    cuisine: str
    category: str
    yields: int = 0
    cooking_time: int = 0
    price: float = 0.0

    def build_ingredients(self):

        ingredients_list = []
        for x in self.ingredients:
            ingredients_list.append(Ingredient(name=x['name'], last_bought=None))

        return ingredients_list



if __name__ == "__main__":

    # url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    link = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/"  # This works thanks to wild mode
    link = "https://somuchfoodblog.com/apple-cider-braised-pork-shoulder/"

    snkrddl = Recipe(link)

    print(snkrddl.name)
    print(snkrddl.category)
    print(str(snkrddl.cooking_time) + " Min")
    print(snkrddl.servings)

    for ing in snkrddl.ingredients:
        print(ing)
