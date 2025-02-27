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
        """Subclass of ScreenManager acts as controller for GUI."""
        super().__init__(**kwargs)
        self.cookbooks = (
            ListProperty()
        )  # Tracks all currently available cookbooks, set in splash screen

    def add_screen(
        self, screen_type: str, name: str, change: bool, new: bool, dt: int = 2
    ):
        """Adds a new screen of type `screen_type` to the screenmanager
        Args:
            :param screen_type (str) The type of screen to add to Controller, i.e. bookshelf, recipe, cookbook
            :param name (str) Name of new screen
            :param change (bool) Flag to enable transition to screen after creation
            :param new (bool) Flag indicating the creation of a new db as opposed to opening one
            :param dt (int) Delay for transition to new screen"""

        new_widget = None

        if name not in self.screen_names:
            match screen_type.lower():
                case "cookbook":
                    new_widget = CookbookToCScreen(new, name=name)

                case "bookshelf":
                    new_widget = BookShelfScreen(name=name)

                case "recipe":
                    new_widget = RecipeScreen(name=name)

            self.add_widget(new_widget)

        if change:
            self.wait_for_trans(name, dt)

        else:
            return True

    def create_new_cookbook(self):
        """Creates and opens a Popup form for creating a new cookbook db"""

        cookbook_creator = CookBookForm(self)
        cookbook_creator.open()

    def create_new_recipe(self):
        """Creates and opens a Popup form for creating a new Recipe in a cookbook db"""

        recipe_creator = RecipeForm(self)
        recipe_creator.open()

    def wait_for_trans(self, new_screen, dt=2):
        """Schedules the transition to a new screen on a delay (dt)

        Args:
        :param new_screen (str) Name of screen to transition to.
        :param dt (int | float) Duration of delay in seconds. [defaults to 2]"""

        def _change_current(nscreen, dt):
            self.current = nscreen

        Clock.schedule_once(partial(_change_current, new_screen), dt)
