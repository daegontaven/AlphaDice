import sys

from PyQt5.Qsci import QsciScintilla
from qtpy.QtCore import QObject
from qtpy.QtGui import QFont

from AlphaHooks.widgets.editor.lexers import PythonLexer


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

        # Configurations
        self.ui.code_editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.ui.code_editor.setIndentationsUseTabs(False)
        self.ui.code_editor.setIndentationGuides(True)
        self.ui.code_editor.setAutoIndent(True)
        self.ui.code_editor.setTabIndents(True)
        self.ui.code_editor.setUtf8(True)

        # Margin
        self.ui.code_editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.ui.code_editor.setMarginWidth(0, "00")

        # Platform Specific
        if sys.platform.startswith("linux"):
            self.ui.code_editor.setEolMode(QsciScintilla.EolUnix)
        elif sys.platform.startswith("win32"):
            self.ui.code_editor.setEolMode(QsciScintilla.EolWindows)
        elif sys.platform.startswith("darwin"):
            self.ui.code_editor.setEolMode(QsciScintilla.EolMac)

        # Lexer
        self.lexer = PythonLexer(self.ui, self.font)
        self.lexer.lock()

        # Slots
        self.ui.code_editor.linesChanged.connect(self.update_margin)

    def update_margin(self):
        """
        Adjust margin width to accommodate the number lines numbers.
        """
        lines = self.ui.code_editor.lines()
        self.ui.code_editor.setMarginWidth(0, "0" * (len(str(lines)) + 1))
