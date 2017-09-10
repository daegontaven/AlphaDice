from queue import Queue, Empty

from PyQt5.QtCore import QObject, pyqtSignal, QTimer

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class ConsoleStream(QObject):
    """
    Custom StreamIO class that handles when send data
    to console_log
    """
    written = pyqtSignal(str)

    def __init__(self, buffer=False, *args, **kwargs):
        super(ConsoleStream, self).__init__(*args, **kwargs)
        self.buffer = buffer

        if buffer:
            self.buffer = Queue()
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.get)
            self.timer.start(0)  # process all events before timeout

    def write(self, string):
        """
        Overrides the parent write method and emits a signal
        meant to be received by interpreters. If the buffer
        is enabled, then it will add the string to a Queue
        where it will wait to be emitted.

        :param string: single write output from stdout
        """
        if self.buffer:
            self.buffer.put(string)
        else:
            self.written.emit(string)

    def get(self):
        """
        Tries to get and emit string from the buffer
        if it's available.
        """
        try:
            string = self.buffer.get(block=False)
            self.written.emit(string)
        except Empty:
            pass
