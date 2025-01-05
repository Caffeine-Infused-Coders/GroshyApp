from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from groshy.gui.main_menu_window import MainMenuWindow

class CookbooksView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Title label
        title_label = Label(
            text="Cookbooks",
            size_hint=(1, None),
            height=50,
            font_size='24sp',
            bold=True,
            halign='center',
            valign='middle'
        )
        self.add_widget(title_label)

        # Scrollable list of cookbooks
        scroll_view = ScrollView(size_hint=(1, 1))

        cookbooks_layout = GridLayout(
            cols=1,
            size_hint_y=None,
            spacing=10,
            padding=20
        )
        cookbooks_layout.bind(minimum_height=cookbooks_layout.setter('height'))

        # Example cookbooks (replace with dynamic data as needed)
        for cookbook_name in ["Breakfast Recipes", "Lunch Ideas", "Dinner Delights", "Desserts"]:
            btn = Button(
                text=cookbook_name,
                size_hint=(1, None),
                height=50,
                background_normal='',
                background_color=(0.6, 0.3, 0.8, 1),
                border=(20, 20, 20, 20)
            )
            cookbooks_layout.add_widget(btn)

        scroll_view.add_widget(cookbooks_layout)
        self.add_widget(scroll_view)

        # Back button
        back_button = Button(
            text="Back to Main Menu",
            size_hint=(1, None),
            height=50,
            background_normal='',
            background_color=(0.8, 0.1, 0.1, 1),
            border=(20, 20, 20, 20)
        )
        back_button.bind(on_press=self.back_to_main_menu)
        self.add_widget(back_button)

    def back_to_main_menu(self, instance):
        # Transition back to the Main Menu
        self.parent.clear_widgets()
        self.parent.add_widget(MainMenuWindow())
