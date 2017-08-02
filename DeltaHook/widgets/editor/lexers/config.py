from PyQt5.Qsci import QsciScintilla

__author__ = "daegontaven"
__copyright__ = "daegontaven"
__license__ = "gpl3"


class LexerBase:
    """
    Common properties of all lexers.
    """
    def __init__(self, ui, font):
        """
        :param ui: used to access 'main.ui' methods
        :param font: set in EditorProperty
        """
        self.ui = ui
        self.font = font

        # Configurations
        self.ui.code_editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.ui.code_editor.setIndentationsUseTabs(False)
