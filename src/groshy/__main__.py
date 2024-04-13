from pathlib import Path
from textwrap import dedent
from groshy.abstract_db import AbstractDB

from groshy.recipe import Recipe
from groshy.cookbook import CookBook
from groshy.pantry import Pantry


def main():
    while True:

        activeCookbook = None
        activePantry = None

        
        resp = input(dedent("""
                            How would you like to add a new recipe:
                                (M)anually
                                (A)utomatically 
                                (or e(X)it)
                            Answer: """))

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

        def list_dbs(type: AbstractDB):
        
            if dbs := type.fetch_dbs():
                print("Available CookBooks: ")
                for db in dbs:
                    print(db)
                db = input("Which cookbook would you like to write your recipe into?")
                if db in dbs and type is CookBook:
                    active = CookBook(db, False)
                elif db in dbs and type is Pantry:
                    active = Pantry(db, False)
                elif type is CookBook:
                    active = CookBook(db, True)
                elif type is Pantry:
                    active = Pantry(db, True)
                print(f"Saving Recipe in {active}")
            else:
                db = input("Please name your first cookbook!\nName:\n\t")
                active = CookBook(db, True)

            return active
            
        activeCookbook.db_add([rec.model_dump()])
            

        print("Here are the ingredients")
        for ing in rec.ingredients:
            print(ing)

        print("Adding ingredients to pantry")
        activePantry = Pantry("bb1pantry", True)
        ings = rec.prep_ingredients()
        activePantry.pantry_update(ings)

        print("Ta Da!")
        print(activePantry.name)
        for x in activePantry.shelves:
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
            