from pathlib import Path

import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from groshy.gui import main_menu_screen
from groshy.gui import bookshelf_screen
from groshy.gui.main_menu_screen import MainMenuScreen
from groshy.gui.bookshelf_screen import BookShelfScreen

class GroshyApp(App):
    def build(self):

        sm = ScreenManager()

        sm.add_widget(MainMenuScreen(name='main_menu'))
        sm.add_widget(BookShelfScreen(name='bookshelf_screen'))

        return sm

temp_dir = Path(__file__).parent
gui_dir = Path(temp_dir, 'gui')

Builder.load_file(str(Path(gui_dir, 'main_menu_screen.kv')))
Builder.load_file(str(Path(gui_dir, 'bookshelf_screen.kv')))
Builder.load_file(str(Path(gui_dir, 'cookbook_button.kv')))

GroshyApp().run()