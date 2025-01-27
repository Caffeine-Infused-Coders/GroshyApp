from kivy.clock import Clock
from kivy.properties import partial
from kivy.uix.screenmanager import ScreenManager

from groshy.cookbook import CookBook

from groshy.gui.cookbook_toc_screen import CookbookToCScreen

class Controller(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def add_cookbook_screen(self, name: str, new: bool) -> bool:
        """Adds a cookbook screen to the screen manager"""

        cookbook = CookBook(name, new)
        screen_name = f'{name}_ToC'
        self.add_widget(CookbookToCScreen(cookbook_data=cookbook, name=screen_name))
        self.wait_for_trans(screen_name)


    def open_new_cookbook_form(self):
        
        self.add_widget(CookBookForm)


    def wait_for_trans(self, newscreen):
        def _change_current(nscreen, dt):
            self.current = nscreen

        Clock.schedule_once(partial(_change_current, newscreen), 3)
