from queue import Queue, Empty, Full

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

    def __init__(self, parent=None, buffer=False):
        super(ConsoleStream, self).__init__(parent)
        self.buffer = buffer

        if buffer:
            self.buffer = Queue(500)

        # SingleShot Flush
        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.process)

    def write(self, string):
        """
        Overrides the parent write method and emits a signal
        meant to be received by interpreters. If the buffer
        is enabled, then it will add the string to a Queue
        where it will wait to be emitted.

        :param string: single write output from stdout
        """
        if self.buffer:
            if self.buffer.empty():
                self.timer.start()
            try:
                self.buffer.put(string, block=False)
                self.timer.start()
            except Full:
                self.flush()
                self.timer.stop()
                self.write(string)
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

    def process(self):
        """
        Determines when to flush the buffer.
        """
        if self.buffer.not_empty:
            self.flush()
            self.timer.stop()
        elif self.buffer.empty():
            self.timer.stop()

    def flush(self):
        """
        Flushes the buffer.
        """
        lines = []
        for line in range(self.buffer.qsize()):
            try:
                line = self.buffer.get(block=False)
                lines.append(line)
                continue
            except Empty:
                break
        if lines:
            self.written.emit(''.join(lines))
