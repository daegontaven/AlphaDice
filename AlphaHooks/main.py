import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow)

from AlphaHooks.widgets.config import WidgetRunner
from AlphaHooks.windows.config import MainInterface

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class MainWindow(QMainWindow):
    """
    The main GUI window. Opens maximized.
    """
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = MainInterface(self)
        self.widgets = WidgetRunner(self.ui)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
