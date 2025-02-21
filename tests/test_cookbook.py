import json
from pathlib import Path

import pytest

from groshy.cookbook import CookBook
from groshy.recipe import Recipe


@pytest.fixture
def make_test_cb():
    ckbktestname = "tstckbk"
    ckbk = CookBook(ckbktestname, True)
    yield ckbk

    ckbk.db_remove()


def test_save_recipe(url, make_test_cb):

    recipe = Recipe.fetch_recipe(url)

    make_test_cb.save_recipe(recipe)

    with open(make_test_cb.path, "rb") as tstfile:
        contents = json.load(tstfile)

    assert recipe.name in contents
    assert recipe.description == contents[recipe.name]["description"]
