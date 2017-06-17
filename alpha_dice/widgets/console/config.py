from PyQt5.QtCore import QThread
from PyQt5.QtGui import QTextCursor

from widgets.console.interpreters import PythonInterpreter


class ConsoleProperty:
    """
    Provides access to methods of console_log.
    """
    def __init__(self, ui):
        """
        Loads default configuration for console_log. A new thread is spawned
        to which the interpreter is moved. This is done to increase
        the responsiveness of the main user interface.

        :param ui: used to access 'main.ui' methods
        """
        self.ui = ui

        # Document
        self.ui.console_log.isReadOnly()
        self.ui.console_log.document().setMaximumBlockCount(1000)

        # Threads
        self.thread = QThread()
        self.thread.start()

        self.interpreter = PythonInterpreter()
        self.interpreter.moveToThread(self.thread)

        # Slots
        self.ui.console_input.returnPressed.connect(self.send_console_input)
        self.interpreter.output.connect(self.send_console_log)

    def send_console_input(self):
        command = self.ui.console_input.text()
        self.ui.console_input.clear()
        self.interpreter.signal_command.emit(str(command))

    def send_console_log(self, command):
        self.ui.console_log.moveCursor(QTextCursor.End)
        self.ui.console_log.insertPlainText(command)
