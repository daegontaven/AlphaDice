import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication)

from AlphaHooks.widgets.config import WidgetRunner

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class MainWindow:
    """
    The main GUI window. Opens maximized.
    """
    def __init__(self):

        self.ui = uic.loadUi("main.ui")
        self.ui.showMaximized()

        self.widgets = WidgetRunner(self.ui)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
