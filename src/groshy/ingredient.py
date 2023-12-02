from typing import Optional
from datetime import date


from pydantic import BaseModel, condate


class Ingredient(BaseModel):
    name: str
    isEssential: bool = False
    last_bought: Optional[date] 
    shelf_life: int = 7

