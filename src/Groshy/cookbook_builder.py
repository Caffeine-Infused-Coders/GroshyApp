import os
import json

from recipe import Recipe


class CookBook:
    def __init__(self, db_name: str, db_dir: str):
        
def save_recipe(recipe: Recipe, db_name: str):

    with open(f"db_path")
    recipe.to_dict()



def build_db(db_path: str, name: str= "Cookbook", categories: list= ["Breakfast", "Lunch", "Dinner", "Snacks"]):

    if db_path.endswith("/"):
        db_file = f"{db_path}{name}.json"
    else:
        db_file = f"{db_path}/{name}.json"

    cat_dict = dict.fromkeys(categories, {})
    msg = {name: cat_dict}

    result = False

    try:
        with open(db_file, "x") as db:
            json.dump(msg, db, indent= 4)
            print(f"{name} cookbook created successfully")
            result = True
    except FileExistsError:
        print(f"A cookbook named {name} already exists...")

        resp = input("Would you like to choose a new name? (y/n)")

        if resp == "y":
            name = input("Enter new cookbook name: ")
            build_db(db_path, name, categories)
            result = True
        else:
            print("Cookbook creation aborted")

    return result



if __name__ == "__main__":

    dbs = "./.dbs"

    if build_db(dbs, "new"):
        with open(f"{dbs}/new.json", "r") as f:
            skeleton = json.load(f)
    else:
        skeleton = "Well Shit"

    print(skeleton)