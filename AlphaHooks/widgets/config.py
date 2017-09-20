from AlphaHooks.widgets import EditorProperty
from AlphaHooks.widgets.console import ConsoleProperty


class WidgetRunner:
    """
    Loads default configurations of each widget.
    """
    def __init__(self, ui, config):
        self.ui = ui
        self.config = config

        # Load Properties
        self.editor = EditorProperty(self.ui)
        self.console = ConsoleProperty(self.ui, self.config)
