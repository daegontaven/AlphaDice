from PyQt5.QtCore import QThread, QObject
from PyQt5.QtGui import QTextCursor

from AlphaHooks.widgets.console.interpreters import PythonInterpreter

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class PythonDisplay(QObject):
    def __init__(self, ui, parent=None, *args, **kwargs):
        """
        Loads python configurations for console_log. A new thread is
        spawned to which the interpreter is moved. This is done to
        increase the responsiveness of the main user interface.

        :param ui: used to access 'main.ui' methods
        """
        super(PythonDisplay, self).__init__(parent, *args)
        self.ui = ui

        # Prompts
        self.ps1 = '>>>'
        self.ps2 = '...'
        for key, val in kwargs.items():
            if key == 'ps1':
                self.ps1 = val
            if key == 'ps2':
                self.ps2 = val
        self.ui.console_prompt.setText(self.ps1)

        # Threads
        self.thread = QThread()
        self.thread.start()

        self.interpreter = PythonInterpreter()
        self.interpreter.moveToThread(self.thread)

        # Slots
        self.ui.console_input.returnPressed.connect(self.send_console_input)
        self.interpreter.stream.written.connect(self.send_console_log)
        self.interpreter.multi_line.connect(self.prompt)

    def prompt(self, multi_line):
        """
        Checks and displays the current prompt in console_prompt.

        :param multi_line: Can be True or False for the
                           defined prompts
        """
        if not multi_line:
            self.ui.console_prompt.setText(self.ps1)
        else:
            self.ui.console_prompt.setText(self.ps2)

    def send_console_input(self):
        """
        Push the input to the interpreter where it is run.
        """
        command = self.ui.console_input.text()
        self.ui.console_input.clear()
        self.interpreter.push_command.emit(str(command))

    def send_console_log(self, output):
        """
        Insert the output into console_log and automatically scroll the
        scrollbar.

        :param output: output from the interpreter
        """
        # Move cursor
        cursor = self.ui.console_log.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.ui.console_log.setTextCursor(cursor)

        # Insert Text
        self.ui.console_log.insertPlainText(output)

        # Move scrollbar
        scrollbar = self.ui.console_log.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
