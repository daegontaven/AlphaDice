import time
from io import StringIO
from queue import Queue

from PyQt5.QtCore import QThread

from AlphaHooks.widgets.signals import PrimitiveSignals

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class BufferQueue(QThread):
    """
    Thread used to get strings from DelayedBuffer.queue and
    emit them as signals in constant intervals.
    """
    WRITE_DELAY = 0.005

    def __init__(self, output):
        super().__init__()
        self.output = output
        self.queue = Queue()

    def update(self, string):
        """
        Populates self.queue with strings

        :param string: string received from stdout

        """
        self.queue.put(string)

    def run(self):
        while True:
            while not self.queue.empty():
                self.output.signal_str.emit(self.queue.get())
                time.sleep(self.WRITE_DELAY)


class DelayedBuffer:
    """
    A buffer that uses a queue to store strings. It removes the
    first appended string first in a constant interval.
    """
    def __init__(self, output):
        """
        Starts the BufferQueue thread.

        :param output: used to access PrimitiveSignals
        """
        self.output = output
        self.buffer = BufferQueue(self.output)
        self.buffer.start()

    def write(self, string):
        self.buffer.update(string)

    def emit(self, string):
        """
        Force emit of string.
        """
        self.output.signal_str.emit(string)


class NewLineIO(StringIO):
    """
    Custom StreamIO class that emits a signal on each write.
    """
    def __init__(self, *args, **kwargs):
        """
        Starts a delayed buffer to store writes due to UI
        refresh limitations.
        """
        StringIO.__init__(self, *args, **kwargs)
        self.output = PrimitiveSignals()
        self.buffer = DelayedBuffer(self.output)

    def write(self, string):
        """
        Overrides the parent write method and emits a signal
        meant to be received by interpreters.

        :param string: single write output from stdout
        """
        self.buffer.write(string)
