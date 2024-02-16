from pathlib import Path
from groshy import cookbook

from groshy.recipe import Recipe
from groshy.cookbook import CookBook
from groshy.pantry import Pantry


def main():
    while True:

        activeCookbook = None
        activePantry = None

        
        resp = input("Would you like to enter a recipe? (y/n): ")

        url = None
        
        match resp.lower():
            case "yes" | "y":
                url = str(input("Paste URL here: "))
            case "no" | "n":
                print("Bye")
                break
            case _:
                print("Yikes, try again")
                continue

        if (rec := Recipe.get_recipe(url)) is not None:
            print(f"Recipe Name: {rec.name}")
            print(f"Recipe Category: {rec.category}")
            print(f"Recipe Cooking Time: {rec.cooking_time}")
            
            resp = input("Looks like we got some info. Does this look right? (y/n): ")

            if resp.lower in ["no", "n"]:
                print("Sorry about that, restarting program :(")
                continue
            
            print("Saving recipe to cookbook...")
            
            if ckbks := CookBook.fetch_dbs():
                print("Available CookBooks: ")
                for ckbk in ckbks:
                    print(ckbk)
                ckbk = input("Which cookbook would you like to write your recipe into?")
                if ckbk in ckbks:
                    activeCookbook = CookBook(False, ckbk)
                else:
                    activeCookbook = CookBook(True, ckbk)
                print(f"Saving Recipe in {activeCookbook}")
            else:
                ckbk = input("Please name your first cookbook!:\n\t")
                activeCookbook = CookBook(True, ckbk)
                
            activeCookbook.db_add(rec.model_dump())
                

            print("Here are the ingredients")
            for ing in rec.ingredients:
                print(ing)

            print("Adding ingredients to pantry")
            ings = rec.build_ingredients()
            pan = Pantry("bb1pantry", True, ings)

            print("Ta Da!")
            print(pan.name)
            for x in pan.contents:
                print(x.model_dump_json())


def question():
    resp = input("Would you like to enter another recipe? (y/n): ")

    match resp.lower():
        case "yes" | "y":
            main()
        case "no" | "n":
            print("Goodbye!")
            exit()
        case _:
            print("You think you're so funny huh")
            exit()



if __name__ == "__main__":

    print("""
          -------------------
                Howdy,
          Welcome to your new
             Recipe Book!
          -------------------""")
    
    main()
            