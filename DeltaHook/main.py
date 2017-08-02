import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication)

from DeltaHook.widgets.config import WidgetRunner


class MainWindow:
    """
    The main GUI window. Opens maximized.
    """
    def __init__(self):

        self.ui = uic.loadUi("main.ui")
        self.ui.showMaximized()

        self.widgets = WidgetRunner(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
