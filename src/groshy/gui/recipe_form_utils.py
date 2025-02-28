"""Helper classes and methods specific to the Recipe Entry Form."""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class EntryBox(TextInput):
    """TextInput boxes of defined shape for use in Ingredient and step entry"""

    pass


class MultiEntryBox(BoxLayout):
    def __init__(self, boxtype: str, sb, **kwargs):
        """Generic BoxLayout for holding EntryBox objects with the ability to add more.

        Args:
            :arg boxtype (str) Type of entrybox to add to the layout
            :arg sb (ScrollBox) An instance of the"""
        super().__init__(**kwargs)
        self.boxtype = boxtype
        self.sb = sb
        self.stepnum = None

        if self.boxtype == "instructions":
            self.stepnum = 4
            for i in range(self.stepnum):
                step = EntryBox(hint_text=f"Step #{i + 1}")
                self.add_widget(step)
        else:
            for _ in range(4):
                self.add_widget(IngredientEntry())

    def add_another_entry(self):
        """Adds an EntryBox object to self and expands the scrollbox view to
        accommodate."""

        self.sb.height += 40
        if self.boxtype == "instructions":
            self.stepnum += 1
            new_entry = EntryBox(hint_text=f"Step #{self.stepnum}...")

        else:
            new_entry = IngredientEntry()

        self.add_widget(new_entry)


class IngredientEntry(BoxLayout):
    pass


class MultiEntryBoxGrid(GridLayout):
    pass
