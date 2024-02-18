from pathlib import Path

from groshy.abstract_db import AbstractDB
from groshy.ingredient import Ingredient


class Pantry(AbstractDB):
    def __init__(self, name: str, pantrynew: bool):
        super().__init__(name, "pantry", pantrynew)
        self.shelves = self._data


    def pantry_write(self):
        """Dumps Ingredient models into list before passing to db_add."""

        dump_list = []
        for ingredients in self.shelves:
            dump_list.append(ingredients.model_dump())
            
        self.db_add(dump_list)


    def pantry_update(self, foods: list[Ingredient]):
        """Update Pantry DB with new list of Ingredients."""

        for food in foods:
            self.shelves.update(food)

        self.pantry_write()



    def fetch_dbs(self) -> list[str]:
        """Reads pantry db file namesj in pantry directory, returns them as a list of strings."""

        dbs = []

        if Path.is_dir(path := Path.joinpath(self.db_root, "pantry")):
            for db in path.iterdir():
                dbs.append(db.name)

        return dbs

    