
from kivy.clock import Clock
from kivy.properties import partial, ListProperty
from kivy.uix.screenmanager import ScreenManager

from groshy.gui.cookbook_toc_screen import CookbookToCScreen
from groshy.gui.cookbook_form import CookBookForm
from groshy.gui.recipe_form import RecipeForm
from groshy.gui.bookshelf_screen import BookShelfScreen

class Controller(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cookbooks = ListProperty()  # Tracks all currently available cookbooks, set in splash screen


    def add_cookbook_screen(self, cookbook: str, new: bool, change: bool):
        """Adds a cookbook ToC screen to the screen manager.

        :return: The name of the newly created screen"""

        self.add_widget(CookbookToCScreen(new, name=cookbook))

        if change:
            self.wait_for_trans(cookbook)


    def create_new_cookbook(self):
        cookbook_creator = CookBookForm(self)
        cookbook_creator.open()


    def create_new_recipe(self):
        recipe_creator = RecipeForm(self)
        recipe_creator.open()


    def add_bookshelf_screen(self):
        bookshelf = BookShelfScreen(name='bookshelf')

        self.add_widget(bookshelf)
        self.wait_for_trans('bookshelf')


    def add_recipe_screen(self):
        print('Changing to recipe screen....')

        return True


    def wait_for_trans(self, newscreen, dt=2):
        def _change_current(nscreen, dt):
            self.current = nscreen

        Clock.schedule_once(partial(_change_current, newscreen), dt)
