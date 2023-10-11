from dataclasses import dataclass
from datetime import datetime

@dataclass
class Ingredient:

    name: str
    isEssential: bool = False
    last_bought: datetime = None
    shelf_life: int = 7

    def to_dict(self):
        return {
            "ingredient":
                {
                    "name": self.name,
                    "isEssential": self.isEssential,
                    "last bought": self.last_bought,
                    "shelf life": self.shelf_life
                }
        }

