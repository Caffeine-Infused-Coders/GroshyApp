from recipe_scrapers import scrape_me
from recipe_scrapers import _exceptions as exc

def get_recipe(url):
    try:
        recipe = scrape_me(url)
    except exc.WebsiteNotImplementedError:
        try:
            recipe = scrape_me(url, wild_mode=True)
        except exc.NoSchemaFoundInWildMode:
            recipe = False
    finally:
        return recipe
    

if __name__ == "__main__":

    #url = "https://thefirstyearblog.wordpress.com/2013/02/09/homemade-cinnamon-graham-crackers/comment-page-1/" # This link does not work
    url = "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/" # This works thanks to wild mode

    recipe = get_recipe(url)
    
    if recipe is False:
        print("Sorry Chap :(")
    else:
        print(f"""
              {recipe.title()}
              {recipe.category()}
              {recipe.cook_time()}
              {recipe.ingredients()}
              """)