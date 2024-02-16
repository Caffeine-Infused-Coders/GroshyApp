
from groshy.abstract_db import AbstractDB


class ShoppingList(AbstractDB):
    def __init__(self, db_name: str, newsl: bool = False):
        super().__init__(db_name, "ShoppingList", newsl)