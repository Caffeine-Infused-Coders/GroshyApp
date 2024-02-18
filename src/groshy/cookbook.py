from os import name
from pathlib import Path
import json

from groshy.recipe import Recipe
from groshy.abstract_db import AbstractDB


class CookBook(AbstractDB):
    def __init__(self, db_name: str,  newckbk: bool):
        super().__init__(db_name, "cookbook", newckbk)
        self.new = newckbk
        self.pages = self._data



    def save_recipe(self, recipe: Recipe) -> bool:

        success = False

        json_recipe = {recipe.name: recipe.model_dump(exclude={'name'})}

        if self.db_add([json_recipe]):
            print(f"Recipe saved to {self.name}")
            success = True

        
        return success

    @classmethod
    def fetch_dbs(cls) -> list[str]:
        """ Reads cookbook db filenames in cookbook directory, returns them as a list of strings."""

        dbs = []

        if Path.is_dir(path := Path.joinpath(AbstractDB.db_root, "cookbook")):
            for db in path.iterdir():
                dbs.append(db.name)

        return dbs


    


if __name__ == "__main__":

    babys_first_cookbook = CookBook("bb1ckbk", True)

    print(f"Name: {babys_first_cookbook.name}")
    print(f"Type: {babys_first_cookbook.type}")
    print(f"Location: {babys_first_cookbook.dir}")
    print(f"Full Path: {babys_first_cookbook.path}")

    recipe = Recipe.get_recipe("https://www.thediaryofarealhousewife.com/snickerdoodle-dip/")

    print("Got the data")

    babys_first_cookbook.save_recipe(recipe)
