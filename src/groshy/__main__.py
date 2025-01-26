from pathlib import Path

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from groshy import gui
from groshy.cookbook import CookBook

class GroshyApp(App):
    def __init__(self):
        super().__init__()
        self.screen_manager = ScreenManager()

    def build(self):

        sm = self.screen_manager

        sm.add_widget(gui.SplashScreen(name='splash'))
        # sm.add_widget(BookShelfScreen(name='bookshelf_screen'))

        return sm

    def add_cookbook_screen(self, name: str, new: bool) -> bool:
        """Adds a cookbook screen to the screen manager"""

        CookBook(name, new)

        self.screen_manager.add_widget(gui.CookbookToCScreen(name=f'{name}_ToC'))
        




temp_dir = Path(__file__).parent
gui_dir = Path(temp_dir, 'gui')

Builder.load_file(str(Path(gui_dir, 'splash_screen.kv')))
Builder.load_file(str(Path(gui_dir, 'bookshelf_screen.kv')))
Builder.load_file(str(Path(gui_dir, 'cookbook_button.kv')))

GroshyApp().run()