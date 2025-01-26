from kivy import properties
from kivy.uix.screenmanager import Screen

from groshy.cookbook import CookBook


class SplashScreen(Screen):
    splash_info = properties.ObjectProperty(None)

    def on_enter(self):
        cookbooks = CookBook.fetch_dbs()

        if len(cookbooks) > 1:
            self.splash_info.text = "loading BookShelf..."

        elif len(cookbooks) == 1:
            self.splash_info.text = f"Loading {cookbooks[0]}..."
            self.parent.add_cookbook_screen()
            # self.parent.current =

        else:
            self.splash_info.text = "No CookBooks Found"
            # self.add_widget(Button, text='Get Started')


