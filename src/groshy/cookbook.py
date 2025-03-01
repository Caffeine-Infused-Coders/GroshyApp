"""Defines the Cookbook DB type, a child of the AbstractDB class."""

from pathlib import Path

from kivy.logger import Logger

from groshy.recipe import Recipe
from groshy.abstract_db import AbstractDB

log = Logger


class CookBook(AbstractDB):
    def __init__(self, db_name: str):
        """Cookbook db type"""

        super().__init__(db_name, "cookbook")
        self.pages = self._data

    def save_recipe(self, recipe: Recipe) -> bool:
        """Dumps the provided recipe in json format before saving it to actual db file

        Args:
            :param recipe (Recipe) Recipe object to be saved

        Returns:
            :return bool Status of save operation"""

        success = False

        json_recipe = {recipe.name: recipe.model_dump(exclude={"name"})}

        if self.db_add([json_recipe]):
            log.info(f"Recipe saved to {self.name}")
            success = True

        return success

    def build_table_of_contents(self) -> list:
        """Uses the self.pages attribute to extract the recipe titles saved within the
        cookbook.
            :return: List of Recipe Titles
        """

        recipes = []
        for recipe in self.pages:
            recipes.append(list(recipe)[0])

        return recipes

    @classmethod
    def fetch_dbs(cls) -> list[str]:
        """Reads cookbook db filenames in cookbook directory, returns them as a list of
        strings."""

        dbs = []

        if Path.is_dir(path := Path.joinpath(AbstractDB.db_root, "cookbook")):
            for db in path.iterdir():
                dbs.append(db.name.replace(".json", ""))

        return dbs


if __name__ == "__main__":

    babys_first_cookbook = CookBook("bb3ckbk", True)

    print(f"Name: {babys_first_cookbook.name}")
    print(f"Type: {babys_first_cookbook.db_type}")
    print(f"Location: {babys_first_cookbook.dir}")
    print(f"Full Path: {babys_first_cookbook.path}")

    recipe = Recipe.fetch_recipe(
        "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/"
    )

    print("Got the data")

    babys_first_cookbook.save_recipe(recipe)
