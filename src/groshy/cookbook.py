import os
import json

from groshy.recipe import Recipe
from groshy.abstract_db import AbstractDB


class CookBook(AbstractDB):
    def __init__(self, db_name: str = "Cookbook1"):
        super().__init__(db_name, "cookbook")


    def save_recipe(self, recipe: Recipe):

        json_recipe = recipe.model_dump_json()

        if self.db_add(json_recipe):
            print(f"Recipe saved to {self.name}")

    


if __name__ == "__main__":

    babys_first_cookbook = CookBook("bb1ckbk")

    print(babys_first_cookbook.name)
    print(babys_first_cookbook.type)
    print(babys_first_cookbook.dir)
    print(babys_first_cookbook.path)
