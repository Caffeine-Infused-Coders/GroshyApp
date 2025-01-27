from kivy import properties
from kivy.uix.screenmanager import Screen

from groshy.cookbook import CookBook


class SplashScreen(Screen):
    # splash_info = properties.ObjectProperty(None)

    def on_enter(self):
        self.ids.splash_info.text = "Finding Cookbooks..."
        cookbooks = CookBook.fetch_dbs()

        if len(cookbooks) > 1:
            self.ids.splash_info.text = "loading BookShelf..."

        elif len(cookbooks) == 1:
            cookbook_name = cookbooks[0].strip('.json')
            self.ids.splash_info.text = f"Loading {cookbook_name}..."
            self.parent.add_cookbook_screen(cookbook_name, False)
            # self.parent.current =

        else:
            self.ids.splash_info.text = "No CookBooks Found"
            
            self.ids.get_started.opacity = 0.8
            self.ids.get_started.disabled = False


