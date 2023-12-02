import os
import json

from recipe import Recipe
from abstract_db import AbstractDB


class CookBook(AbstractDB):
    def __init__(self, db_name: str = "Cookbook1"):
        super().__init__(db_name, "cookbook")


def save_recipe(recipe: Recipe, db_name: str):

    with open(f"db_path") as db:
        recipe.to_dict()


if __name__ == "__main__":

    babys_first_cookbook = CookBook("bb1ckbk")

    print(babys_first_cookbook.name)
    print(babys_first_cookbook.type)
    print(babys_first_cookbook.dir)
    print(babys_first_cookbook.path)
