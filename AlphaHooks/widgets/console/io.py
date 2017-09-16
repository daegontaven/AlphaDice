import time

from PyQt5.QtCore import QObject, pyqtSignal, QTimer, pyqtSlot

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class StringBuffer(QObject):
    """
    Buffer used for storing strings.

    :signal output: string(s) to be emitted
    """
    output = pyqtSignal(str)

    def __init__(self, parent=None, delay=0.050):
        super(StringBuffer, self).__init__(parent)
        self.delay = delay
        self.last_time = time.monotonic() - delay
        self.buffer = []

        # Timer
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.flush)

    @pyqtSlot(str)
    def consume(self, string):
        """
        Add a string to the buffer and determine if
        it's time to flush.
        """
        self.buffer.append(string)

        # Flush
        delta = time.monotonic() - self.last_time
        remaining = self.delay - delta
        if remaining <= 0:
            self.flush()
        elif not self.timer.isActive():
            self.timer.start(int(1000 * remaining))

    def flush(self):
        """
        Dump everything out of the buffer and send it
        to console_log.
        """
        self.timer.stop()
        s = ''.join(self.buffer)
        if len(s):
            self.last_time = time.monotonic()
            self.output.emit(s)
        self.buffer = []


class Stream(QObject):
    """
    Custom stream class that emits a signal when written to.

    :signal written: emit what was written
    """
    written = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Stream, self).__init__(parent)

    def write(self, string):
        """
        :param string: single write output from stdout
        """
        self.written.emit(string)
