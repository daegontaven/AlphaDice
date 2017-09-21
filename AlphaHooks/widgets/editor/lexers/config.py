from PyQt5.Qsci import QsciScintilla


class LexerBase:
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

        # Configurations
        self.ui.code_editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.ui.code_editor.setIndentationsUseTabs(False)
