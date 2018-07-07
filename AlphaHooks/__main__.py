import sys

from PyQt5.QtCore import QObject, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget, \
    QTextEdit, QListWidget, QStatusBar

from AlphaHooks.widgets.editor import CodeEditor


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Menu Bar
        self.menu_bar = self.menuBar()
        self.file_menu = self.menu_bar.addMenu("File")
        self.edit_menu = self.menu_bar.addMenu("Edit")
        self.view_menu = self.menu_bar.addMenu("View")
        self.tools_menu = self.menu_bar.addMenu("Tools")

        # Project Browser
        self.project_dock = QDockWidget("Project", self)
        self.project_dock.setFloating(False)
        self.project_dock.setAllowedAreas(Qt.AllDockWidgetAreas)

        self.project = QListWidget(self)  # Mock Project Browser
        self.project.addItem("main.py")
        self.project.addItem("test.java")
        self.project.addItem("stats.r")
        self.project_dock.setWidget(self.project)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.project_dock)

        # Code Editor
        # Move this part to a tabbed widget.
        # Create a bottom tabbed widget and in the first tab "Code", add
        # another tabbed widget with file tabs. The next outer tab
        # should be called "Live" or something similar to represent
        # real-time output like streaming plots and video.
        self.code_editor = CodeEditor(self)
        self.setCentralWidget(self.code_editor)

        # Jupyter Widget
        self.jupyter_dock = QDockWidget("Jupyter", self)
        self.jupyter_dock.setFloating(False)
        self.jupyter_dock.setAllowedAreas(Qt.AllDockWidgetAreas)

        self.jupyter = QTextEdit(self)  # Mock Jupyter Widget
        self.jupyter_dock.setWidget(self.jupyter)
        self.addDockWidget(Qt.RightDockWidgetArea, self.jupyter_dock)

        # Window Properties
        self.setWindowTitle("Mock Layout for AlphaHooks")

        # Status Bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

    def closeEvent(self, event):
        """
        Finish up any tasks. Stop all running widgets, it's threads and
        any I/O tasks.
        """
        for child in self.findChildren(QObject):
            if hasattr(child, "stop_running"):
                child.stop_running()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
