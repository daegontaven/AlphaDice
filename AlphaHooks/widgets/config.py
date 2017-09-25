from qtpy.QtCore import QObject

from AlphaHooks.widgets import EditorProperty
from AlphaHooks.widgets.console import ConsoleProperty


class WidgetRunner(QObject):
    """
    Loads default configurations of each widget.
    """
    def __init__(self, ui, config, parent=None):
        super(WidgetRunner, self).__init__(parent)
        self.ui = ui
        self.config = config

        # Load Properties
        self.editor = EditorProperty(self.ui, self)
        self.console = ConsoleProperty(self.ui, self.config, self)

    def stop(self):
        """
        Stop all running widgets, it's threads and any I/O tasks.
        """
        for child in self.findChildren(QObject):
            if hasattr(child, "stop_running"):
                child.stop_running()
