import re
from recipe_handler import get_recipe, parse_ingredients

class Recipe():
    def __init__(self, url):

        self.scraped = get_recipe(url)

        self.name = self.scraped.title()
        self.category = self.scraped.category()
        self.cooking_time = self.scraped.total_time()
        self.servings = self.scraped.yields()
        self.ingredients = parse_ingredients()

if __name__ == "__main__":

    # url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    link = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/" # This works thanks to wild mode
    link = "https://somuchfoodblog.com/apple-cider-braised-pork-shoulder/"

    snkrddl = Recipe(link)

    print(snkrddl.name)
    print(snkrddl.category)
    print(str(snkrddl.cooking_time) + " Min")
    print(snkrddl.servings)
    snkrddl.parse_ingredients()

    for ing in snkrddl.ingredients:
        print(ing)

