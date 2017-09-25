from PyQt5 import Qsci
from qtpy import QtCore, QtWidgets
from qtpy.QtCore import QObject, QEvent
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QComboBox, QWidget, QSizePolicy, QPushButton

from AlphaHooks.windows.settings.config import SettingsDialog


class MainInterface(QObject):
    def __init__(self, main_window, config):
        super(MainInterface, self).__init__(main_window)
        self.config = config

        # Main Window
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)
        main_window.setTabShape(QtWidgets.QTabWidget.Rounded)

        # Central Widget
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_layout.setObjectName("verticalLayout")

        # Main Splitter
        self.main_splitter = QtWidgets.QSplitter(self.central_widget)
        self.main_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.main_splitter.setObjectName("main_splitter")

        # Library Browser
        self.library_browser = QtWidgets.QTreeWidget(self.main_splitter)
        self.library_browser.setObjectName("library_browser")

        # Main Tab Widget
        self.main_tab_widget = QtWidgets.QTabWidget(self.main_splitter)
        self.main_tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.main_tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tab_widget.setElideMode(QtCore.Qt.ElideNone)
        self.main_tab_widget.setDocumentMode(False)
        self.main_tab_widget.setTabsClosable(False)
        self.main_tab_widget.setMovable(True)
        self.main_tab_widget.setTabBarAutoHide(False)
        self.main_tab_widget.setObjectName("main_tab_widget")

        # Code Tab
        self.code_tab = QtWidgets.QWidget()
        self.code_tab.setObjectName("code_tab")
        self.code_tab_layout = QtWidgets.QHBoxLayout(self.code_tab)
        self.code_tab_layout.setObjectName("horizontalLayout_2")
        self.code_layout = QtWidgets.QVBoxLayout()
        self.code_layout.setObjectName("code_layout")
        self.code_editor = Qsci.QsciScintilla(self.code_tab)
        self.code_editor.setToolTip("")
        self.code_editor.setWhatsThis("")
        self.code_editor.setObjectName("code_editor")
        self.code_layout.addWidget(self.code_editor)
        self.code_tab_layout.addLayout(self.code_layout)
        self.main_tab_widget.addTab(self.code_tab, "")

        # Console Tab
        self.console_tab = QtWidgets.QWidget()
        self.console_tab.setObjectName("console_tab")
        self.console_tab_layout = QtWidgets.QHBoxLayout(self.console_tab)
        self.console_tab_layout.setObjectName("horizontalLayout_3")

        # Console Log
        self.console_layout = QtWidgets.QVBoxLayout()
        self.console_layout.setObjectName("console_layout")
        self.console_log = QtWidgets.QPlainTextEdit(self.console_tab)
        self.console_log.setReadOnly(True)
        self.console_log.setObjectName("console_log")
        self.console_layout.addWidget(self.console_log)

        # Console Prompt
        self.prompt_layout = QtWidgets.QHBoxLayout()
        self.prompt_layout.setObjectName("prompt_layout")
        self.console_prompt = QtWidgets.QLabel(self.console_tab)
        self.console_prompt.setText("")
        self.console_prompt.setObjectName("console_prompt")
        self.prompt_layout.addWidget(self.console_prompt)

        # Console Input
        self.console_input = QtWidgets.QLineEdit(self.console_tab)
        self.console_input.setFrame(True)
        self.console_input.setObjectName("console_input")
        self.prompt_layout.addWidget(self.console_input)
        self.console_layout.addLayout(self.prompt_layout)
        self.console_tab_layout.addLayout(self.console_layout)
        self.main_tab_widget.addTab(self.console_tab, "")
        self.central_layout.addWidget(self.main_splitter)

        # Set Central and Index
        self.main_tab_widget.setCurrentIndex(1)
        main_window.setCentralWidget(self.central_widget)

        # Menu Bar
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menu_bar.setObjectName("menu_bar")
        main_window.setMenuBar(self.menu_bar)

        # Menu Bar -> File
        self.file_menu = self.menu_bar.addMenu('File')

        # Menu Bar -> File -> Settings
        self.settings_dialog = SettingsDialog(config)
        self.settings_action = QtWidgets.QAction('Settings...')
        self.settings_action.setShortcut('Ctrl+Alt+S')
        self.file_menu.addAction(self.settings_action)
        self.settings_action.triggered.connect(self.settings_dialog.show)

        # Tool Bar
        self.tool_bar = main_window.addToolBar('Main Tool Bar')
        self.tool_bar.setMaximumHeight(
            self.tool_bar.height() / 1.10
        )

        # Tool Bar Spacer
        self.tool_bar_spacer = QWidget()
        self.tool_bar_spacer.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Preferred
        )
        self.tool_bar_spacer.setVisible(True)
        self.tool_bar.addWidget(self.tool_bar_spacer)

        # Tool Bar -> Interpreter
        self.interpreter_combo = QComboBox()
        self.interpreter_combo.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.interpreter_combo.addItems(self.config["Languages"])
        self.tool_bar.addWidget(self.interpreter_combo)

        # Tool Bar -> Run
        self.interpreter_run = QPushButton()
        self.interpreter_run.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding
        )
        self.interpreter_run.setIcon(QIcon(":/icons/interpreter_run"))
        self.interpreter_run.setFlat(True)
        self.interpreter_run.installEventFilter(self)
        self.tool_bar.addWidget(self.interpreter_run)

        # Status Bar
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")
        main_window.setStatusBar(self.status_bar)

        self.re_translate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def eventFilter(self, source, event):

        # Hover Effect
        if source is self.interpreter_run:
            if event.type() == QEvent.HoverEnter:
                source.setFlat(False)

            if event.type() == QEvent.HoverLeave:
                source.setFlat(True)

            return False
        return False

    def re_translate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "AlphaHooks"))
        self.library_browser.headerItem().setText(
            0,
            _translate(
                "main_window",
                "Library Browser"
            )
        )
        self.main_tab_widget.setTabText(
            self.main_tab_widget.indexOf(self.code_tab),
            _translate("main_window", "Code")
        )
        self.main_tab_widget.setTabText(
            self.main_tab_widget.indexOf(self.console_tab),
            _translate("main_window", "Console")
        )
