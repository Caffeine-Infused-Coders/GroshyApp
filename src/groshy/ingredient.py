"""Defines Ingredient dataclass object"""

from datetime import date

from pydantic import BaseModel


class Ingredient(BaseModel):
    """Ingredient Dataclass, subclass of Pydantic BaseModel.

    Args:
        :param name (str) Name of Ingredient
        :param isEssential (bool) Should this be considered an 'essential' in your
        pantry
        :param last_bought (date) Last day that the ingredient was purchased
        :param shelf_life (int) Number of days after last_bought that ingredient
        should be put back on list"""

    name: str
    isEssential: bool = False
    last_bought: date
    shelf_life: int = 7
