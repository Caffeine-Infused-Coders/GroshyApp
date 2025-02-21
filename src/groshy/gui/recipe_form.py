from kivy.uix.popup import Popup

from groshy.recipe import Recipe
from groshy.gui.utils import TextAndLabel
from groshy.gui.recipe_form_utils import MultiEntryBox, MultiEntryBoxGrid


class RecipeForm(Popup):
    def __init__(self, sm, **kwargs):
        super().__init__(**kwargs)

        self.sm = sm  ## Pass in screen manager for access

    def on_open(self):

        # self.ids.urlbox.ids.data_name.text = 'Recipe Url'
        # self.ids.urlbox.ids.data_name.hint_text = 'Paste Url here to save online recipe'
        self.ids.urlbox.hint_text = 'Paste Url here to save online recipe...'
        for field in Recipe.model_fields.keys():
            tal = TextAndLabel()
            tal.ids.data_name.text = f"{field.upper().replace('_', ' ')}:"

            if field == 'description':
                tal.ids.data_entry.multiline = True
                tal.ids.data_entry.height = 500
            elif field in ('ingredients', 'instructions'):
                tal = MultiEntryBoxGrid()
                tal.ids.data_name.text = f"{field.upper().replace('_', ' ')}:"
                tal.add_widget(MultiEntryBox(field, self.ids.scrollbox))

            self.ids.scrollbox.add_widget(tal)



