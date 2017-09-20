from PyQt5.QtCore import QObject
from PyQt5.QtGui import QTextOption

from AlphaHooks.widgets.console.display import PythonDisplay


class ConsoleProperty(QObject):
    """
    Provides access to methods of console_log.
    """
    def __init__(self, ui, config, parent=None):
        """
        Loads default configuration for console_log. A new thread is
        spawned to which the interpreter is moved. This is done to
        increase the responsiveness of the main user interface.

        :param ui: used to access 'main.ui' methods
        :param config: used to configure classes
        """
        super(ConsoleProperty, self).__init__(parent)
        self.ui = ui
        self.config = config

        # Document
        self.ui.console_log.document().setMaximumBlockCount(
            self.config["Console"]["Scrollback Buffer"]
        )
        self.ui.console_log.setWordWrapMode(QTextOption.WrapAnywhere)

        # Display
        self.display = PythonDisplay(self.ui, self.config, self)
