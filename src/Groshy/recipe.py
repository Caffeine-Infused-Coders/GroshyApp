from dataclasses import dataclass

from ingredient import Ingredient


@dataclass
class Recipe:
    name: str
    description: str
    ingredients: list[dict]
    instructions: list[str]
    cuisine: str
    category: str
    price: float
    servings: int = None
    cooking_time: int = None

    def to_dict(self):
        return {
            "recipe": {
                "name": self.name,
                "description": self.description,
                "cuisine": self.cuisine,
                "category": self.category,
                "servings": self.servings,
                "price": self.price,
                "cooking_time": self.cooking_time,
                "ingredients": self.ingredients,
                "instructions": self.instructions,
            }
        }

    def build_ingredients(self):

        ingredients_list = []
        for x in self.ingredients:
            ingredients_list.append(Ingredient(x["name"]))



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
