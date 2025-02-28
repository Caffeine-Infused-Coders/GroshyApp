"""Defines CookBook Table Of Contents Screen and helper objects"""

from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

from groshy.cookbook import CookBook


class RecipeLabel(Label):
    """Label object made to be hyperlinks to RecipeScreen"""

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            App.get_running_app().screen_manager.add_screen(
                screen_type="recipe", name="recipe1", dt=1
            )
            return True


class CookbookToCScreen(Screen):
    def __init__(self, name, **kwargs):
        """Cookbook's `open` presentation, subclass of Kivy Screen"""
        super().__init__(name=name, **kwargs)

        self.cookbook_data = CookBook(name, new)

    def on_enter(self, *args):
        self.ids.cookbook_title.text = self.cookbook_data.get_display_name(
            self.cookbook_data.name
        )
        recipes = self.cookbook_data.build_table_of_contents()

        for recipe in recipes:
            new_label = RecipeLabel(text=recipe)
            self.ids.recipe_box.add_widget(new_label)

    def on_leave(self, *args):
        self.ids.recipe_box.clear_widgets()
