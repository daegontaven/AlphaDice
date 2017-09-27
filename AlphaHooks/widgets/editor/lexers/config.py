from qtpy.QtCore import QObject


class LexerBase(QObject):
    """
    Common properties of all lexers.
    """
    def __init__(self, ui, font):
        """
        :param ui: used to access 'main.ui' methods
        :param font: settings in EditorProperty
        """
        self.ui = ui
        self.font = font
