
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from groshy.cookbook import CookBook

class CookBookButton(Button):
    pass

class BookShelfScreen(Screen):

    def open_cookbook_from_button(self, instance):
        name = CookBook.get_db_name(instance.text)
        self.parent.add_screen(screen_type='cookbook', name=name, change=True, new=False, dt=0.5)

    def on_enter(self):
        cb_list = CookBook.fetch_dbs()
        cb_list_len = len(cb_list)
        if cb_list_len >= 4:
            self.ids.cookbooks.cols = int(cb_list_len / 2)
        else:
            self.ids.cookbooks.cols = cb_list_len

        for cb in cb_list:
            button = CookBookButton(text = CookBook.get_display_name(cb))
            button.bind(on_press=self.open_cookbook_from_button)
            self.ids.cookbooks.add_widget(button)


    def on_leave(self):
        self.ids.cookbooks.clear_widgets()

