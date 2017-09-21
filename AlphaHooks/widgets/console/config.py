import readline

from PyQt5.QtCore import QObject, QEvent, Qt
from PyQt5.QtGui import QTextOption

from AlphaHooks.widgets.console.display import PythonDisplay


class ConsoleProperty(QObject):
    """
    Provides access to methods of console_log.
    """
    HISTORY_PATH = "data/.history"

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

        # Console Input History
        self.index = 0
        self.length = 0
        try:
            open(self.HISTORY_PATH, "x")
        except FileExistsError:
            readline.read_history_file(self.HISTORY_PATH)
        self.ui.console_input.installEventFilter(self)

        # Display
        self.display = PythonDisplay(self.ui, self.config, self)

    def eventFilter(self, source, event):

        # Console Input
        if source is self.ui.console_input:
            if event.type() == QEvent.KeyPress:
                if event.key() in (Qt.Key_Enter, Qt.Key_Return):
                    command = self.ui.console_input.text()
                    if command != "":
                        readline.add_history(
                            command
                        )
                    self.length = readline.get_current_history_length()
                    self.index = -1

                if event.key() == Qt.Key_Up:
                    if self.index < self.length:
                        self.index += 1
                        command = readline.get_history_item(
                            self.length - self.index
                        )
                        self.ui.console_input.setText(
                            command
                        )

                if event.key() == Qt.Key_Down:
                    if self.index <= self.length:
                        self.index -= 1
                    command = readline.get_history_item(
                        self.length - self.index
                    )

                    self.ui.console_input.setText(
                        command
                    )

            return False
        return False
