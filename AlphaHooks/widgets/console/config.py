from PyQt5.QtGui import QTextOption

from AlphaHooks.widgets.console.display import PythonDisplay


class ConsoleProperty:
    """
    Provides access to methods of console_log.
    """
    def __init__(self, ui):
        """
        Loads default configuration for console_log. A new thread is
        spawned to which the interpreter is moved. This is done to
        increase the responsiveness of the main user interface.

        :param ui: used to access 'main.ui' methods
        """
        self.ui = ui

        # Document
        self.ui.console_log.document().setMaximumBlockCount(1000)
        self.ui.console_log.setWordWrapMode(QTextOption.WrapAnywhere)

        # Display
        self.display = PythonDisplay(self.ui)
