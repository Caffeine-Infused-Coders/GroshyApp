from pathlib import Path

from kivy.app import App
from kivy.lang.builder import Builder

from groshy import gui


class GroshyApp(App):
    def __init__(self):
        super().__init__()
        self.screen_manager = gui.Controller()

    def build(self):

        sm = self.screen_manager

        sm.add_widget(gui.SplashScreen(name="splash"))
        # sm.add_widget(BookShelfScreen(name='bookshelf_screen'))

        return sm


temp_dir = Path(__file__).parent
gui_dir = Path(temp_dir, "gui")

## Load Utility Gui Files
Builder.load_file(str(Path(gui_dir, "utils.kv")))

## Load Screen Gui Files
Builder.load_file(str(Path(gui_dir, "splash_screen.kv")))
Builder.load_file(str(Path(gui_dir, "bookshelf_screen.kv")))
Builder.load_file(str(Path(gui_dir, "cookbook_toc_screen.kv")))

## Load Form Gui Files
Builder.load_file(str(Path(gui_dir, "cookbook_form.kv")))
Builder.load_file(str(Path(gui_dir, "recipe_form.kv")))
Builder.load_file(str(Path(gui_dir, "recipe_form_utils.kv")))


GroshyApp().run()
