"""Defines the Pantry DB type, a child of the AbstractDB class."""

import logging
from pathlib import Path

from groshy.abstract_db import AbstractDB
from groshy.ingredient import Ingredient

log = logging.getLogger(__name__)


class Pantry(AbstractDB):
    def __init__(self, name: str):
        """DB responsible for tracking Ingredients needed and currently 'owned'"""

        super().__init__(name, "pantry")
        self.shelves = self._data

    def pantry_write(self):
        """Dumps Ingredient models into list before passing to db_add."""

        dump_list = []
        for ingredients in self.shelves:
            dump_list.append(
                {ingredients.name: ingredients.model_dump(exclude={"name"})}
            )

        self.db_add(dump_list)

    def pantry_update(self, foods: list[Ingredient], write: bool):
        """Update Pantry DB with new list of Ingredients."""

        self.shelves = foods

        if write:
            self.pantry_write()

    def fetch_dbs(self) -> list[str]:
        """Reads pantry db file names in pantry directory, returns them as a list of
        strings."""

        dbs = []

        if Path.is_dir(path := Path.joinpath(self.db_root, "pantry")):
            for db in path.iterdir():
                dbs.append(db.name)

        return dbs


if __name__ == "__main__":

    from groshy.recipe import Recipe

    open_pantry = Pantry("pantree", True)

    print(f"Name: {open_pantry.name}")
    print(f"Type: {open_pantry.db_type}")
    print(f"Location: {open_pantry.dir}")
    print(f"Full Path: {open_pantry.path}")

    recipe = Recipe.fetch_recipe(
        "https://www.thediaryofarealhousewife.com/snickerdoodle-dip/"
    )

    print("Got the data")

    open_pantry.save_recipe(recipe)
