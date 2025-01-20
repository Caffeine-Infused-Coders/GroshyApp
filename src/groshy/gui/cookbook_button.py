from kivy.lang.builder import Builder
from kivy.uix.button import Button


class CookBookButton(Button):
    def build(self):
        Builder.load_file('cookbook_button.kv')
        