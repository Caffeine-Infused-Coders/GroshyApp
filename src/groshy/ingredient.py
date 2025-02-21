from datetime import date

from pydantic import BaseModel


class Ingredient(BaseModel):
    name: str
    isEssential: bool = False
    last_bought: date
    shelf_life: int = 7
