import builtins

from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciAPIs
from qtpy.QtGui import QFontMetrics

from AlphaHooks.widgets.editor.lexers.config import LexerBase


class PythonLexer(LexerBase):
    """
    Customized from QsciLexerPython to provide basic auto-completion.
    """
    def lock(self):
        """
        Sets the default properties for the Python lexer.
        """
        # Lexer Initialization
        lexer = QsciLexerPython(self.ui.code_editor)
        lexer.setDefaultFont(self.font)
        self.ui.code_editor.setLexer(lexer)

        # Auto Completion
        api = QsciAPIs(lexer)
        for var in dir(builtins):
            if not (var[0] == "_"):
                api.add(var)
        api.prepare()

        self.ui.code_editor.setAutoCompletionThreshold(1)
        self.ui.code_editor.setAutoCompletionSource(QsciScintilla.AcsAPIs)

        # Indentation
        self.ui.code_editor.setIndentationWidth(4)

        # Font Settings
        font_metrics = QFontMetrics(self.font)
        self.ui.code_editor.setMinimumSize(
            int(font_metrics.width("0" * 80)),
            0
        )
