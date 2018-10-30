import pytest

from AlphaHooks.widgets.jupyter import TabbedJupyterWidget


def setup_jupyter_kernel(qtbot, kernel):
    widget = TabbedJupyterWidget()
    widget.show()
    qtbot.add_widget(widget)

    # Jupyter Widget Mappings
    kernel_manager = widget.jupyter_widget.kernel_manager

    # Check if the kernel is correct
    assert kernel_manager.kernel_name == kernel


def test_widget_attributes(qtbot):
    setup_jupyter_kernel(
        qtbot,
        kernel="python3"
    )
