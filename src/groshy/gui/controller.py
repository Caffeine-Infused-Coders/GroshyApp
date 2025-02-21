
from kivy.clock import Clock
from kivy.properties import partial, ListProperty
from kivy.uix.screenmanager import ScreenManager

from groshy.gui.recipe_form import RecipeForm
from groshy.gui.cookbook_form import CookBookForm

from groshy.gui.cookbook_toc_screen import CookbookToCScreen
from groshy.gui.bookshelf_screen import BookShelfScreen
from groshy.gui.recipe_screen import RecipeScreen


class Controller(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cookbooks = ListProperty()  # Tracks all currently available cookbooks, set in splash screen


    def add_screen(self, screen_type: str, name: str, change: bool, new: bool, dt: int=2):
        """Adds a new screen of type `screen_type` to the screenmanager"""

        new_widget = None

        if name not in self.screen_names:
            match screen_type.lower():
                case 'cookbook':
                    new_widget = CookbookToCScreen(new, name=name)

                case 'bookshelf':
                    new_widget = BookShelfScreen(name=name)

                case 'recipe':
                    new_widget = RecipeScreen(name=name)

            self.add_widget(new_widget)
            

        if change:
            self.wait_for_trans(name, dt)

        else:
            return True


    def create_new_cookbook(self):
        cookbook_creator = CookBookForm(self)
        cookbook_creator.open()


    def create_new_recipe(self):
        recipe_creator = RecipeForm(self)
        recipe_creator.open()


    def wait_for_trans(self, new_screen, dt=2):
        def _change_current(nscreen, dt):
            self.current = nscreen

        Clock.schedule_once(partial(_change_current, new_screen), dt)
