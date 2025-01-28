
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from groshy.cookbook import CookBook

class RecipeLabel(Label):
    pass

class CookbookToCScreen(Screen):
    def __init__(self, new: bool, name, **kwargs):
        self.cookbook_data = CookBook(name, new)

        super().__init__(name=name, **kwargs)


    # def on_enter(self, *args):
        