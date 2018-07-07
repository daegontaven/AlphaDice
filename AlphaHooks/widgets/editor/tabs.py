from PyQt5.QtWidgets import QTabWidget

from AlphaHooks.widgets.editor import Editor


class EditorTabs(QTabWidget):
    def __init__(self, parent=None):
        """
        Generates tab with editor depending on the file and it's type
        selected.
        """
        super(EditorTabs, self).__init__(parent)

        # Tab Properties
        self.setTabsClosable(True)
        self.setMovable(True)

        # Default Editor
        self.editor = Editor(self)
        self.addTab(self.editor, "main.py")

        # Slots
        self.tabCloseRequested.connect(self.handle_tab_closed)

    def handle_tab_closed(self, index):
        self.removeTab(index)
