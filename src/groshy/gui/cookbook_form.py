
from kivy.uix.popup import Popup


class CookBookForm(Popup):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)

        self.sm = sm

    def name_validator(self):
        new_cookbook_name = self.ids.name_box.text
        current_cookbooks = self.sm.cookbooks

        if new_cookbook_name not in current_cookbooks and new_cookbook_name != '':
            current_cookbooks.append(new_cookbook_name)

            self.sm.add_screen(screen_type='cookbook', name=new_cookbook_name, change=True, new=True, dt=1)
            self.dismiss()

        else:
            self.ids.name_box.text_hint = 'Please choose a name that does not already exist...'
