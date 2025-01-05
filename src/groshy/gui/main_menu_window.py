from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MainMenuWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        # Button for "View CookBook"
        self.view_cookbook_btn = Button(
            text="View CookBook",
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.view_cookbook_btn)

        # Button for "Add Recipe Manually"
        self.add_recipe_btn = Button(
            text="Add Recipe Manually",
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.add_recipe_btn)

        # Horizontal layout for "Add" button and TextInput
        self.add_recipe_url_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None),
            height=50
        )

        self.add_btn = Button(
            text="Add",
            size_hint=(None, 1),
            width=100
        )
        self.add_recipe_url_layout.add_widget(self.add_btn)

        self.recipe_url_input = TextInput(
            hint_text="Paste Recipe URL Here",
            multiline=False,
            size_hint=(1, 1)
        )
        self.add_recipe_url_layout.add_widget(self.recipe_url_input)

        self.add_widget(self.add_recipe_url_layout)

class GroshyApp(App):
    def build(self):
        return MainMenuWindow()

if __name__ == "__main__":
    GroshyApp().run()
