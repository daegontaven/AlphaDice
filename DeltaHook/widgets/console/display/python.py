from PyQt5.QtCore import QThread
from PyQt5.QtGui import QTextCursor

from DeltaHook.widgets.console.interpreters import PythonInterpreter


class PythonDisplay:
    def __init__(self, ui, **kwargs):
        """
        Loads python configurations for console_log. A new thread is
        spawned to which the interpreter is moved. This is done to
        increase the responsiveness of the main user interface.

        :param ui: used to access 'main.ui' methods
        """
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
        self.interpreter.output.connect(self.send_console_log)
        self.interpreter.multi_line.connect(self.prompt)

    def prompt(self, multi_line):
        if not multi_line:
            self.ui.console_prompt.setText(self.ps1)
        else:
            self.ui.console_prompt.setText(self.ps2)

    def send_console_input(self):
        command = self.ui.console_input.text()
        self.ui.console_input.clear()
        self.interpreter.signal_command.emit(str(command))

    def send_console_log(self, command):
        old_cursor = self.ui.console_log.textCursor()
        old_scrollbar = self.ui.console_log.verticalScrollBar().value()
        new_scrollbar = self.ui.console_log.verticalScrollBar().maximum()
        if old_scrollbar == new_scrollbar:
            scrolled = True
        else:
            scrolled = False

        self.ui.console_log.insertPlainText(command)

        if old_cursor.hasSelection() or not scrolled:
            self.ui.console_log.setTextCursor(old_cursor)
            self.ui.console_log.verticalScrollBar().setValue(old_scrollbar)
        else:
            self.ui.console_log.moveCursor(QTextCursor.End)
            self.ui.console_log.verticalScrollBar().setValue(
                self.ui.console_log.verticalScrollBar().maximum()
            )
