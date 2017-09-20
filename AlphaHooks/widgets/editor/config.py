from PyQt5.QtCore import QObject
from PyQt5.QtGui import QFont

from AlphaHooks.widgets.editor.lexers import PythonLexer

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class EditorProperty(QObject):
    """
    Provides access to methods of code_editor.
    """
    def __init__(self, ui, parent=None):
        """
        Loads default configuration for code_editor including
        the lexer.

        :param ui: used to access 'main.ui' methods
        """
        super(EditorProperty, self).__init__(parent)
        self.ui = ui

        # Fonts
        self.font = QFont()
        self.font.setFamily('Courier New')
        self.font.setFixedPitch(True)
        self.font.setPointSize(10)
        self.ui.code_editor.setFont(self.font)

        # Scrollbar
        self.ui.code_editor.SendScintilla(
            self.ui.code_editor.SCI_SETHSCROLLBAR,
            0
        )

        # Lexer
        self.lexer = PythonLexer(self.ui, self.font)
        self.lexer.lock()

