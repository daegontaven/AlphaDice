import sys

from PyQt5 import Qsci
from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QFont

from AlphaHooks.widgets.editor.lexers.python import PythonLexer


class CodeEditor(Qsci.QsciScintilla):
    """
    Provides access to methods of editor.
    """
    def __init__(self, parent=None):
        """
        Loads default configuration for code_editor including
        the lexer depending on the kernel.
        """
        super(CodeEditor, self).__init__(parent)

        # Fonts
        self.font = QFont()
        self.font.setFamily('Courier New')
        self.font.setFixedPitch(True)
        self.font.setPointSize(10)
        self.setFont(self.font)

        # Scrollbar
        self.SendScintilla(
            self.SCI_SETHSCROLLBAR,
            0
        )

        # Configurations
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setIndentationsUseTabs(False)
        self.setIndentationGuides(True)
        self.setAutoIndent(True)
        self.setTabIndents(True)
        self.setUtf8(True)

        # Margin
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, "00")

        # Platform Specific
        if sys.platform.startswith("linux"):
            self.setEolMode(QsciScintilla.EolUnix)
        elif sys.platform.startswith("win32"):
            self.setEolMode(QsciScintilla.EolWindows)
        elif sys.platform.startswith("darwin"):
            self.setEolMode(QsciScintilla.EolMac)

        # Lexer
        self.lexer = PythonLexer(self, self.font)
        self.lexer.lock()

        # Slots
        self.linesChanged.connect(self.update_margin)

    def update_margin(self):
        """
        Adjust margin width to accommodate the number lines numbers.
        """
        lines = self.lines()
        self.setMarginWidth(0, "0" * (len(str(lines)) + 1))