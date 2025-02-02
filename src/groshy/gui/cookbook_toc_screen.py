
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from groshy.cookbook import CookBook

class RecipeLabel(Label):
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            App.get_running_app().screen_manager.add_recipe_screen()
            return True
        

class CookbookToCScreen(Screen):
    def __init__(self, new: bool, name, **kwargs):
        self.cookbook_data = CookBook(name, new)

        super().__init__(name=name, **kwargs)


    def on_enter(self, *args):
        recipes = self.cookbook_data.build_table_of_contents()

        for recipe in recipes:
            new_label = RecipeLabel(text=recipe)
            self.ids.recipe_box.add_widget(new_label)
