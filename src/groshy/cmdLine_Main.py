
from textwrap import dedent
from groshy.abstract_db import AbstractDB

from groshy.recipe import Recipe
from groshy.cookbook import CookBook
from groshy.pantry import Pantry
from groshy.cmd_line_functions import write_recipe

def list_dbs(db_type: AbstractDB):
    def _convert_display_to_db(name: str):
        return name.replace(' ', '_')

    def _convert_db_to_display(name: str):
        return name.replace('_', ' ').strip('.json')

    if dbs := db_type.fetch_dbs():
        print(f"Available {str(db_type)}: ")
        for db in dbs:
            print(_convert_db_to_display(db))
        db = input("Which cookbook would you like to write your recipe into? ")
        db = _convert_display_to_db(db)
        if db in dbs and db_type is CookBook:
            active = CookBook(db, False)
        elif db in dbs and db_type is Pantry:
            active = Pantry(db, False)
        elif db_type is CookBook:
            active = CookBook(db, True)
        elif db_type is Pantry:
            active = Pantry(db, True)

        print(f"Saving Recipe in {active.get_display_name()}")
    else:
        db = input("Please name your first cookbook!\nName:\n\t")
        active = CookBook(db, True)

    return active


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

                if (rec := Recipe.fetch_recipe(url)).name == "N/A":
                    print("Oops something went wrong")
                    continue
                    
                else:
                    print(f"Recipe Name: {rec.name}")
                    print(f"Recipe Category: {rec.category}")
                    print(f"Recipe Cooking Time: {rec.cooking_time}")
                
                    resp = input("Looks like we got some info. Does this look right? (y/n): ")

                    if resp.lower in ["no", "n"]:
                        print("Sorry about that, restarting program :(")
                        continue

            case "m":
                rec = write_recipe()
            case "x":
                print("Bye")
                break
            case _:
                print("Yikes, try again")
                continue

        activeCookbook = list_dbs(CookBook)
        
        print("Saving recipe to cookbook...")

        activeCookbook.db_add([rec.model_dump()])  # type: ignore

        print("Here are the ingredients")
        for ing in rec.ingredients:
            print(ing)

        print("Adding ingredients to pantry")
        activePantry = Pantry("bb1pantry", True)
        ings = rec.prep_ingredients()
        activePantry.pantry_update(ings, True)

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
            