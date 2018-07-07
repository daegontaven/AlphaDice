from PyQt5.QtCore import QObject


class LexerBase(QObject):
    """
    Common properties of all lexers.
    """
    def __init__(self, code_editor, font):
        """
        :param code_editor: used to access the parent editor's methods
        :param font: settings in CodeEditor
        """
        self.code_editor = code_editor
        self.font = font
