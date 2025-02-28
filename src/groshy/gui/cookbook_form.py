"""Defines the Popup window responsible for acquiring information to create new
Cookbook DB"""

from kivy.uix.popup import Popup


class CookBookForm(Popup):
    def __init__(self, sm, **kwargs):
        """Cookbook Form, subclass of Kivy Popup. Requests name of new cookbook DB

        Args:
            :param sm (ScreenManager) Active ScreenManager instance"""

        super().__init__(**kwargs)

        self.sm = sm

    def name_validator(self):
        """Validates the user entered string to be the name of the new cookbook db"""
        new_cookbook_name = self.ids.name_box.text
        current_cookbooks = self.sm.cookbooks

        if new_cookbook_name not in current_cookbooks and new_cookbook_name != "":
            current_cookbooks.append(new_cookbook_name)

            self.sm.add_screen(screen_type="cookbook", name=new_cookbook_name, dt=1)
            self.dismiss()

        else:
            self.ids.name_box.text_hint = (
                "Please choose a name that does not already exist..."
            )
