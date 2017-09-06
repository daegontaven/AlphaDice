from PyQt5.QtCore import QObject, pyqtSignal

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class ConsoleStream(QObject):
    """
    Custom StreamIO class that emits a signal on each write.
    """
    written = pyqtSignal(str)

    def write(self, string):
        """
        Overrides the parent write method and emits a signal
        meant to be received by interpreters.

        :param string: single write output from stdout
        """
        self.written.emit(string)
