from kivy.clock import Clock
from kivy.properties import partial
from kivy.uix.screenmanager import ScreenManager

from groshy.cookbook import CookBook

from groshy.gui.cookbook_toc_screen import CookbookToCScreen

class Controller(ScreenManager):
    def __init__(self):
        super().__init__()

    def add_cookbook_screen(self, name: str, new: bool) -> bool:
        """Adds a cookbook screen to the screen manager"""

        cookbook = CookBook(name, new)
        screen_name = f'{name}_ToC'
        self.add_widget(CookbookToCScreen(cookbook_data=cookbook, name=screen_name))
        Clock.schedule_once(partial(self.wait_for_trans, screen_name), 3)

    def wait_for_trans(self, newscreen, dt):
        self.current = newscreen
