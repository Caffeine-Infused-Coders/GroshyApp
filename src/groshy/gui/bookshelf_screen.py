from pathlib import Path

from kivy.uix.screenmanager import Screen
from kivy.clock import mainthread
from kivy.lang import Builder


from groshy.cookbook import CookBook
from groshy.gui.cookbook_button import CookBookButton

# gui_dir = Path(__file__).parent
# Builder.load_file(str(Path(gui_dir, 'cookbook_button.kv')))

class BookShelfScreen(Screen):

    def on_enter(self):
        cb_list = CookBook.fetch_dbs()

        for cb in cb_list:
            button = CookBookButton(text = cb)
            self.ids.cookbooks.add_widget(button)

