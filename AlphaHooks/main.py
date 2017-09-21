import os
import sys

import json_config
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
    SETTINGS_PATH = "settings.json"
    DATA_PATH = "data"

    def __init__(self):
        QMainWindow.__init__(self)

        if not os.path.isdir(self.DATA_PATH):
            os.mkdir(self.DATA_PATH)

        self.config = json_config.connect(self.SETTINGS_PATH)
        self.ui = MainInterface(self, self.config)
        self.widgets = WidgetRunner(self.ui, self.config, self)

    def closeEvent(self, event):
        """
        Finish up any tasks.
        """
        self.widgets.stop()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
