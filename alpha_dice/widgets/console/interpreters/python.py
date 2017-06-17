import sys
from code import InteractiveConsole

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from widgets.console.interpreters.stream import NewLineIO


class PythonInterpreter(QObject, InteractiveConsole):
    """
    A reimplementation of the builtin InteractiveConsole to work with threads.
    """
    output = pyqtSignal(str)
    signal_command = pyqtSignal(str)

    def __init__(self):
        QObject.__init__(self)
        self.l = {}
        InteractiveConsole.__init__(self, self.l)
        self.out = NewLineIO()
        self.out.output.signal_str.connect(self.console)
        self.signal_command.connect(self.push_command)

    def write(self, string):
        self.output.emit(string)

    def runcode(self, code):
        """
        Overrides and captures stdout and stdin from InteractiveConsole.
        """
        sys.stdout = self.out
        sys.stderr = self.out
        sys.excepthook = sys.__excepthook__
        result = InteractiveConsole.runcode(self, code)
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        return result

    @pyqtSlot(str)
    def push_command(self, command):
        """
        :param command: line retrieved from console_input on returnPressed
        """
        self.push(command)

    @pyqtSlot(str)
    def console(self, string):
        """
        :param string: processed output from a stream
        """
        self.output.emit(string)
