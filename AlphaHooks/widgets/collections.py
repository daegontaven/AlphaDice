from qtpy.QtCore import QObject
from qtpy.QtWidgets import QTreeWidgetItem, QWidget


class Populate(QObject):
    """
    General class used for adding items to different widgets.
    """
    def __init__(self, parent=None, display=None):
        super(Populate, self).__init__(parent)
        self.display = display
        self.index = -1

    def tree_widget(self, tree, structure):
        """
        Used to traverse a QTreeWidget and adding the items in a
        dict or list.

        :param tree: pass a QTreeWidget instance
        :param structure: pass a dictionary
        """
        if type(structure) is dict:
            for key, val in structure.items():
                child = QTreeWidgetItem()
                child.setText(0, key)
                tree.addChild(child)
                self.tree_widget(child, val)
        elif type(structure) is str:
            child = QTreeWidgetItem()
            child.setText(0, structure)
            tree.addChild(child)
        elif isinstance(structure, QWidget):
            self.index += 1
            tree.setText(1, str(self.index))
            self.display.addWidget(structure)
