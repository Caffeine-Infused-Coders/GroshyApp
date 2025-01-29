
import re

from kivy.uix.popup import Popup



class CookBookForm(Popup):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)

        self.sm = sm

    def name_validator(self):
        new_cookbook_name = self.ids.name_box.text
        current_cookbooks = self.sm.cookbooks
        # space = re.compile('[a-z0-9]+( )[a-z0-9]+')
        # new_cookbook_name = re.sub(space, '_', new_cookbook_name)

        if new_cookbook_name not in current_cookbooks and new_cookbook_name != '':
            current_cookbooks.append(new_cookbook_name)

            self.sm.add_cookbook_screen(new_cookbook_name, new=True, change=True)
            self.dismiss()

        else:
            self.ids.name_box.text_hint = 'Please choose a name that does not already exist...'
