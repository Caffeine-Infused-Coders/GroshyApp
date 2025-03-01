"""Defines opening app screen which reads db data and initializes app data."""

from kivy.uix.screenmanager import Screen
from kivy.logger import Logger

from groshy.cookbook import CookBook
from groshy.gui.utils import ScreenType

log = Logger


class SplashScreen(Screen):
    def __init__(self, **kwargs):
        """Subclass of Kivy Screen, first screen created and opened in the app.
        Initializes app data by reading observing database directories."""

        super().__init__(**kwargs)

    def on_enter(self):
        self.ids.splash_info.text = "Finding Cookbooks..."

        cookbooks = CookBook.fetch_dbs()  # Get list of currently available cookbooks
        for i, cookbook in enumerate(cookbooks, 0):
            cookbooks[i] = cookbook.removesuffix(
                ".json"
            )  # Remove file extension from cookbook names

        self.parent.cookbooks = cookbooks  # Save names to screenmanager

        if len(cookbooks) > 1:
            log.info(
                "Splash: More than one cookbook found, going to bookshelf " "screen..."
            )
            self.ids.splash_info.text = "loading BookShelf..."
            self.parent.change_screen(
                screen_name="bookshelf", screen_type=ScreenType.BOOKSHELF, dt=1
            )

        elif len(cookbooks) == 1:
            cookbook_name = cookbooks[0]
            log.info(
                "Splash: Only one cookbook found, going to table of contents for "
                f"{cookbook_name.replace('_', ' ')}..."
            )
            self.ids.splash_info.text = f"Loading {cookbook_name.replace('_', ' ')}..."
            self.parent.change_screen(
                screen_name=cookbook_name, screen_type=ScreenType.COOKBOOK, dt=1
            )

        else:
            self.ids.splash_info.text = "No CookBooks Found"

            self.ids.get_started.opacity = 0.8
            self.ids.get_started.disabled = False
