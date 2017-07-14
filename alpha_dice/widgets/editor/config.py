from PyQt5.QtCore import QObject
from PyQt5.QtGui import QFont

from widgets.editor.lexers import PythonLexer


class EditorProperty(QObject):
    """
    Provides access to methods of code_editor.
    """
    def __init__(self, ui):
        """
        Loads default configuration for code_editor including
        the lexer.

        :param ui: used to access 'main.ui' methods
        """
        self.ui = ui

        # Fonts
        self.font = QFont()
        self.font.setFamily('Courier New')
        self.font.setFixedPitch(True)
        self.font.setPointSize(10)
        self.ui.code_editor.setFont(self.font)

        # Lexer
        self.lexer = PythonLexer(self.ui, self.font)
        self.lexer.lock()

