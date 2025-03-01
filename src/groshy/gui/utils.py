"""Container for helper classes and methods for the Groshy GUI"""

from enum import Enum, unique

from kivy.uix.gridlayout import GridLayout


@unique
class ScreenType(Enum):
    """Enum defining the different types of screen"""

    BOOKSHELF = 1
    COOKBOOK = 2
    RECIPE = 3


class TextAndLabel(GridLayout):
    pass
