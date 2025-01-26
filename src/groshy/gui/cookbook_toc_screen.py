
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from groshy.cookbook import CookBook

class RecipeLabel(Label):
    pass

class CookbookToCScreen(Screen):
    def __init__(self, cookbook_data: CookBook, **kwargs):
        super().__init__(**kwargs)
        self.cookbook_data = cookbook_data

    # def on_enter(self, *args):
        