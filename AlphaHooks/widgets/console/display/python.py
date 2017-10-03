from PyQt5.QtCore import QThread, QObject
from PyQt5.QtGui import QTextCursor

from AlphaHooks.widgets.console.interpreters import PythonInterpreter


class PythonDisplay(QObject):
    def __init__(self, ui, config, parent=None, **kwargs):
        """
        Loads python configurations for console_log. A new thread is
        spawned to which the interpreter is moved. This is done to
        increase the responsiveness of the main user interface.

        :param ui: used to access 'main.ui' methods
        :param config: used to configure classes
        """
        super(PythonDisplay, self).__init__(parent)
        self.ui = ui
        self.config = config

        # Prompts
        self.ps1 = '>>>'
        self.ps2 = '...'
        for key, val in kwargs.items():
            if key == 'ps1':
                self.ps1 = val
            if key == 'ps2':
                self.ps2 = val
        self.ui.console_prompt.setText(self.ps1)

        # Widget Controls
        self.cursor = self.ui.console_log.textCursor()
        self.scrollbar = self.ui.console_log.verticalScrollBar()

        # Threads
        self.thread = QThread()
        self.thread.start()

        self.interpreter = PythonInterpreter(self.config)
        self.interpreter.moveToThread(self.thread)

        # Slots
        self.ui.console_input.returnPressed.connect(self.send_console_input)
        self.ui.interpreter_run.clicked.connect(self.send_console_source)
        self.interpreter.stream_buffer.output.connect(self.send_console_log)
        self.interpreter.error.connect(self.send_console_log)
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

    def send_console_source(self):
        source = self.ui.code_editor.text()
        self.interpreter.push_source.emit(source)

    def send_console_log(self, string):
        """
        Insert the output into console_log and automatically scroll the
        scrollbar.

        :param string: output from the interpreter
        """
        # Move cursor
        self.cursor.movePosition(QTextCursor.End)
        self.ui.console_log.setTextCursor(self.cursor)

        # Insert text
        self.ui.console_log.insertPlainText(string)

        # Move scrollbar
        self.scrollbar.setValue(self.scrollbar.maximum())

    def stop_running(self):
        self.thread.quit()
        self.thread.wait()
