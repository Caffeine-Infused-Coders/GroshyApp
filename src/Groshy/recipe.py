from dataclasses import dataclass

from recipe_handler import get_recipe, get_ingredients


@dataclass
class Recipe:

    name: str
    description: str
    ingredients: list
    instructions: list[str]
    instructions: list[str]
    cuisine: str
    category: str
    servings: int = None
    cooking_time: int = None

    def to_dict(self):
        return {
            "recipe": {
                "name": self.name,
                "description": self.description
                "category": self.category,
                "cooking_time": self.cooking_time,
                "servings": self.servings,
                "ingredients": self.ingredients
            }
        }


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
