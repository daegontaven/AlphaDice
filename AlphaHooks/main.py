import os
import sys

import json_config
from PyQt5.QtWidgets import (QApplication, QMainWindow)

from AlphaHooks import resources
from AlphaHooks.widgets.config import WidgetRunner
from AlphaHooks.windows.config import MainInterface


class MainWindow(QMainWindow):
    """
    The main GUI window. Opens maximized.
    """
    SETTINGS_PATH = "settings.json"
    DATA_PATH = "data"

    def __init__(self):
        QMainWindow.__init__(self)
        self.resources = resources

        # Build Absolute Paths
        self.main_abs_path = os.path.dirname(__file__)
        self.settings_abs_path = os.path.join(
            self.main_abs_path, self.SETTINGS_PATH
        )

        # Make data folder if it doesn't exist
        if not os.path.isdir(self.DATA_PATH):
            os.mkdir(self.DATA_PATH)

        self.config = json_config.connect(self.settings_abs_path)
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
