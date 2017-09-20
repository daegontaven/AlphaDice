from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QSpinBox


class ConsoleSettings(QWidget):
    """
    Input widgets to configure the Console
    """
    def __init__(self, config, parent=None):
        super(ConsoleSettings, self).__init__(parent)
        self.config = config

        # Widgets
        self.write_latency = QLabel("Write Latency")
        self.write_latency_edit = QSpinBox()

        self.scrollback_buffer = QLabel("ScrollBack Buffer")
        self.scrollback_buffer_edit = QSpinBox()

        # Layout
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)

        self.grid_layout.addWidget(self.write_latency, 1, 0)
        self.grid_layout.addWidget(self.write_latency_edit, 1, 1)

        self.grid_layout.addWidget(self.scrollback_buffer, 2, 0)
        self.grid_layout.addWidget(self.scrollback_buffer_edit, 2, 1)

        self.setLayout(self.grid_layout)
