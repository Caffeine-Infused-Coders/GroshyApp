from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from groshy.recipe import Recipe

class TextAndLabel(BoxLayout):
    pass

class RecipeForm(Popup):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)

        self.sm = sm  ## Pass in screen manager for access

    def on_open(self):

        for field in Recipe.model_fields.keys():
            tal = TextAndLabel()
            tal.ids.data_name.text = field.upper()

            match field:
                case 'description':
                    tal.ids.data_name.text =
                case 'ingredients':

                case 'instructions':

                case 'cuisine':

                case 'category':

                case 'yields':

                case 'cooking_time':

                case 'price':

                case _:

            self.ids.scrollbox.add_widget(tal)



