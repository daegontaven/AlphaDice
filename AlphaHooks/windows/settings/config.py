import sys

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QTreeWidget,
                             QApplication, QStackedWidget)

from widgets.collections import Populate
from windows.settings.root import ConsoleSettings


class SettingsDialog(QWidget):
    """
    Settings dialog opened from File -> Settings...
    """
    def __init__(self, config, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.config = config

        # Widgets
        self.console = ConsoleSettings(self.config)

        # Settings
        self.widget_connections = {
            "Console": self.console
        }

        # Settings Tree
        self.settings_tree = QTreeWidget()
        self.settings_tree.setColumnCount(2)
        self.settings_tree.header().hideSection(1)
        self.settings_tree.header().close()

        # Settings Stacked Widget
        self.stack = QStackedWidget()
        self.populate = Populate(self, display=self.stack)
        self.populate.tree_widget(
            self.settings_tree.invisibleRootItem(),
            self.widget_connections
        )

        # Layouts
        self.tree_layout = QVBoxLayout()
        self.tree_layout.addWidget(self.settings_tree)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addLayout(self.tree_layout)
        self.horizontal_layout.addWidget(self.stack)

        self.setLayout(self.horizontal_layout)

        # Slots
        self.settings_tree.currentItemChanged.connect(self.display)

    def display(self, current):
        """
        Show the corresponding widget for the selected tree item.

        :param current: the current tree item
        """
        try:
            item_connection = int(current.text(1))
            self.stack.setCurrentIndex(item_connection)
        except ValueError as _:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SettingsDialog()
    window.show()
    sys.exit(app.exec_())
