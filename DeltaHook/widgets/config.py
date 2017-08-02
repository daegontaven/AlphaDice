from DeltaHook.widgets import EditorProperty
from DeltaHook.widgets.console import ConsoleProperty


class WidgetRunner:
    """
    Loads default configurations of each widget.
    """
    def __init__(self, ui):
        self.ui = ui

        # Load Properties
        self.editor = EditorProperty(self.ui)
        self.console = ConsoleProperty(self.ui)
