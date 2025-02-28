"""Defines the Controller class which is a child of Kivy's ScreenManager.
It is responsible for transitioning screens, adding/creating new screens or creating
popup windows."""

from enum import Enum, unique

from kivy.clock import Clock
from kivy.properties import partial, ListProperty
from kivy.uix.screenmanager import ScreenManager

from groshy.gui.recipe_form import RecipeForm
from groshy.gui.cookbook_form import CookBookForm

from groshy.gui.cookbook_toc_screen import CookbookToCScreen
from groshy.gui.bookshelf_screen import BookShelfScreen
from groshy.gui.recipe_screen import RecipeScreen


@unique
class ScreenType(Enum):
    """Enum defining the different types of screen"""

    BOOKSHELF = 1
    COOKBOOK = 2
    RECIPE = 3


class Controller(ScreenManager):
    def __init__(self, **kwargs):
        """Subclass of ScreenManager acts as controller for GUI."""
        super().__init__(**kwargs)
        self.cookbooks = (
            ListProperty()
        )  # Tracks all currently available cookbooks, set in splash screen

    def add_screen(self, screen_type: ScreenType, name: str):
        """Adds a new screen of type `screen_type` to the screenmanager
        Args:
            :param screen_type (ScreenType) The type of screen to add to Controller,
            (i.e. bookshelf, recipe, cookbook)
            :param name (str) Name of new screen"""

        new_widget = None

        if name not in self.screen_names:
            match screen_type:
                case ScreenType.BOOKSHELF:
                    new_widget = BookShelfScreen(name=name)

                case ScreenType.COOKBOOK:
                    new_widget = CookbookToCScreen(name=name)

                case ScreenType.RECIPE:
                    new_widget = RecipeScreen(name=name)

            self.add_widget(new_widget)

    def change_screen(
        self, screen_name: str, screen_type: ScreenType, dt: int | float = 0.5
    ):
        """Changes current screen to new screen specified by `screen_name`.
        Automatically adds a new screen if one with the passed name doesn't already
        exist.

        Args:
            :param screen_name (str) Name of new screen to change to
            :param screen_type (ScreenType) Type of new screen
            :param dt (int | float) Screen transition delay in seconds [defaults to 0.5]
        """

        if screen_name not in self.screen_names:
            self.add_screen(screen_type=screen_type, name=screen_name)

        self.wait_for_trans(screen_name, dt)

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
