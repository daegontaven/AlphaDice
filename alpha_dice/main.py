import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QDialog)

from widgets.config import WidgetRunner


class MainWindow(QDialog):
    """
    The main GUI window. Opens maximized.
    """
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.ui = uic.loadUi("main.ui")
        self.ui.showMaximized()

        self.widgets = WidgetRunner(self.ui)


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
