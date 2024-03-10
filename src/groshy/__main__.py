from pathlib import Path
from textwrap import dedent

from groshy.recipe import Recipe
from groshy.cookbook import CookBook
from groshy.pantry import Pantry


def main():
    while True:

        activeCookbook = None
        activePantry = None

        
        resp = input(dedent("How would you like to add a new recipe (M)anually or (A)utomatically (or e(X)it): "))

        url = None
        
        match resp.lower():
            case "a":
                url = str(input("Paste URL here: "))

                if (rec := Recipe.fetch_recipe(url)) is not None:
                    print(f"Recipe Name: {rec.name}")
                    print(f"Recipe Category: {rec.category}")
                    print(f"Recipe Cooking Time: {rec.cooking_time}")
                
                    resp = input("Looks like we got some info. Does this look right? (y/n): ")

                    if resp.lower in ["no", "n"]:
                        print("Sorry about that, restarting program :(")
                        continue
                else:
                    print("Oops something went wrong")
                    continue

            case "m":
                rec = Recipe.write_recipe()
            case "x":
                print("Bye")
                break
            case _:
                print("Yikes, try again")
                continue

        
        print("Saving recipe to cookbook...")
        
        if ckbks := CookBook.fetch_dbs():
            print("Available CookBooks: ")
            for ckbk in ckbks:
                print(ckbk)
            ckbk = input("Which cookbook would you like to write your recipe into?")
            if ckbk in ckbks:
                activeCookbook = CookBook(ckbk, False)
            else:
                activeCookbook = CookBook(ckbk, True)
            print(f"Saving Recipe in {activeCookbook}")
        else:
            ckbk = input("Please name your first cookbook!:\n\t")
            activeCookbook = CookBook(ckbk, True)
            
        activeCookbook.db_add([rec.model_dump()])
            

        print("Here are the ingredients")
        for ing in rec.ingredients:
            print(ing)

        print("Adding ingredients to pantry")
        ings = rec.prep_ingredients()
        pan = Pantry("bb1pantry", True)

        print("Ta Da!")
        print(pan.name)
        for x in pan.shelves:
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
            