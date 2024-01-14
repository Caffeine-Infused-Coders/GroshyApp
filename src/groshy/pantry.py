from pathlib import Path

from groshy.abstract_db import AbstractDB
from groshy.ingredient import Ingredient


class Pantry(AbstractDB):
    def __init__(self, name: str, contents: list[Ingredient]):
        super().__init__(name, "pantry")
        self.contents = contents

        if self.contents:
            self.pantry_write()


    def pantry_write(self):
        """ Dumps Ingredient models into list before passing to db_add. """

        dump_list = []
        for cont in self.contents:
            dump_list.append(cont.model_dump())
        
        self.db_add(dump_list)


    def pantry_update(self, conts: list[Ingredient]):
        """Update Pantry DB with new list of Ingredients."""

        for cont in conts:
            self.contents.append(cont)

        self.pantry_write()



    def fetch_dbs(self) -> list[str]:
        """Reads pantry db file namesj in pantry directory, returns them as a list of strings."""

        dbs = []

        if Path.is_dir(path := Path.joinpath(self.db_root, "pantry")):
            for db in path.iterdir():
                dbs.append(db.name)

        return dbs

    