from PyQt5.QtCore import (pyqtSignal, QObject)

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class BaseSignals(QObject):
    """
    Standard set of pyqtSignals.
    """
    signal_str = pyqtSignal(str)
    signal_int = pyqtSignal(int)
    signal_float = pyqtSignal(float)
    signal_list = pyqtSignal(list)
    signal_tuple = pyqtSignal(tuple)
    signal_dict = pyqtSignal(dict)
    signal_object = pyqtSignal(object)

    def __init__(self):
        QObject.__init__(self)
