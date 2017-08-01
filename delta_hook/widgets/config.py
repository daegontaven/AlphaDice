from widgets.console.config import ConsoleProperty
from widgets.editor.config import EditorProperty


class WidgetRunner:
    """
    Loads default configurations of each widget.
    """
    def __init__(self, ui):
        self.ui = ui

        # Load Properties
        self.editor = EditorProperty(self.ui)
        self.console = ConsoleProperty(self.ui)
