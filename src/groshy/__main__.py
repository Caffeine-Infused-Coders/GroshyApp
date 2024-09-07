import sys
from PyQt6 import QtCore, QtGui, QtWidgets

from groshy.main_menu import Ui_mainMenuWindow


app = QtWidgets.QApplication(sys.argv)
mainMenuWindow = QtWidgets.QWidget()
ui = Ui_mainMenuWindow()
ui.setupUi(mainMenuWindow)
mainMenuWindow.show()
sys.exit(app.exec())
