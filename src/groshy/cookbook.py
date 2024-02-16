from pathlib import Path
import json

from groshy.recipe import Recipe
from groshy.abstract_db import AbstractDB


class CookBook(AbstractDB):
    def __init__(self, db_name: str,  newckbk: bool,):
        self.new = newckbk
        super().__init__(db_name, "cookbook", newckbk)



    def save_recipe(self, recipe: Recipe):

        json_recipe = recipe.model_dump_json()

        if self.new:
            if self.db_write(json_recipe):
                

        if self.db_add(json_recipe):
            print(f"Recipe saved to {self.name}")

    @classmethod
    def fetch_dbs(cls) -> list[str]:
        """ Reads cookbook db filenames in cookbook directory, returns them as a list of strings."""

        dbs = []

        if Path.is_dir(path := Path.joinpath(AbstractDB.db_root, "cookbook")):
            for db in path.iterdir():
                dbs.append(db.name)

        return dbs


    


if __name__ == "__main__":

    babys_first_cookbook = CookBook(True, "bb1ckbk")

    print(babys_first_cookbook.name)
    print(babys_first_cookbook.type)
    print(babys_first_cookbook.dir)
    print(babys_first_cookbook.path)
