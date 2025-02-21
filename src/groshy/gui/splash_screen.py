from kivy.uix.screenmanager import Screen

from groshy.cookbook import CookBook


class SplashScreen(Screen):
    # splash_info = properties.ObjectProperty(None)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter(self):
        self.ids.splash_info.text = "Finding Cookbooks..."

        cookbooks = CookBook.fetch_dbs()  # Get list of currently available cookbooks
        for i, cookbook in enumerate(cookbooks, 0):
            cookbooks[i] = cookbook.removesuffix(
                ".json"
            )  # Remove file extension from cookbook names

        self.parent.cookbooks = cookbooks  # Save names to screenmanager

        if len(cookbooks) > 1:
            self.ids.splash_info.text = "loading BookShelf..."
            self.parent.add_screen(
                screen_type="bookshelf", name="bookshelf", change=True, new=False, dt=1
            )

        elif len(cookbooks) == 1:
            cookbook_name = cookbooks[0]
            self.ids.splash_info.text = f"Loading {cookbook_name.replace('_', ' ')}..."
            self.parent.add_screen(
                screen_type="cookbook", name=cookbook_name, change=True, new=False, dt=1
            )

        else:
            self.ids.splash_info.text = "No CookBooks Found"

            self.ids.get_started.opacity = 0.8
            self.ids.get_started.disabled = False
