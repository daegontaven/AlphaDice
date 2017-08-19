from io import StringIO
from queue import Queue, Empty

from PyQt5.QtCore import QThread

from AlphaHooks.widgets.signals import BaseSignals

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class DelayedBuffer(QThread):
    """
    A buffer that uses a queue to store strings. It removes the
    first appended string first in a constant interval.
    """
    def __init__(self, output, delay):
        """
        :param output: used to access BaseSignals
        :param delay: delay for emitting
        """
        super().__init__()
        self.output = output
        self.delay = delay
        self.queue = Queue()

    def write(self, string):
        self.queue.put(string)

    def run(self):
        while True:
            try:
                data = self.queue.get(block=False)
                self.output.signal_str.emit(data)
            except Empty:
                pass

    def emit(self, string):
        """
        Force emit of string.
        """
        self.output.signal_str.emit(string)


class ConsoleStream(StringIO):
    """
    Custom StreamIO class that emits a signal on each write.
    """
    def __init__(self, *args, **kwargs):
        """
        Starts a delayed buffer to store writes due to UI
        refresh limitations.
        """
        StringIO.__init__(self, *args, **kwargs)
        self.output = BaseSignals()
        self.buffer = DelayedBuffer(self.output, delay=0.05)
        self.buffer.start()

    def write(self, string):
        """
        Overrides the parent write method and emits a signal
        meant to be received by interpreters.

        :param string: single write output from stdout
        """
        self.buffer.write(string)
