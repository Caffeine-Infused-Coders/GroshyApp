
from groshy.abstract_db import AbstractDB
from groshy.ingredient import Ingredient


class Pantry(AbstractDB):
    def __init__(self, name: str, contents: list[Ingredient]):
        super().__init__(name, "pantry")
        self.contents = contents

        if self.contents:
            self.pantry_update()

    def pantry_update(self, conts: list[Ingredient] | None=None):

        if conts is not None:
            for cont in conts:
                self.contents.append(cont)
        
        dump_list = []
        for cont in self.contents:
            dump_list.append(cont.model_dump())
        
        self.db_add(dump_list)

    