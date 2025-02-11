
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class TextAndLabel(GridLayout):
    data_entry = ObjectProperty(None)


class StepsEntry(TextInput):
    pass


class MultiEntryBox(BoxLayout):
    def __init__(self, boxtype: str, sb, **kwargs):
        super().__init__(**kwargs)
        self.boxtype = boxtype
        self.sb = sb
        self.stepnum = None

        if self.boxtype == 'instructions':
            self.stepnum = 4
            for i in range(self.stepnum):
                step = StepsEntry(hint_text=f'Step #{i+1}')
                self.add_widget(step)
        else:
            for _ in range(4):
                self.add_widget(IngredientEntry())

    def add_another_entry(self):
        # self.parent.height += 100
        self.sb.height += 60
        if self.boxtype == 'instructions':
            self.stepnum += 1
            new_entry = StepsEntry(hint_text=f'Step #{self.stepnum}')

        else:
            new_entry = IngredientEntry()

        self.add_widget(new_entry)


class IngredientEntry(BoxLayout):
    pass


class MultiEntryBoxGrid(GridLayout):
    pass