import random

import json_config
import pytest

from AlphaHooks.main import MainWindow
from AlphaHooks.windows.settings.root import ConsoleSettings


@pytest.fixture
def setup_console_settings(qtbot):
    """
    Load the config file.
    """
    config = json_config.connect(
        "AlphaHooks/{}".format(MainWindow.SETTINGS_PATH)
    )
    widget = ConsoleSettings(config)
    qtbot.addWidget(widget)
    return widget


@pytest.fixture
def setup_input_saves(qtbot, widget_name, minimum, maximum):
    """
    Ensure input passed to widgets are saved.
    """
    widget = setup_console_settings(qtbot)
    widget.show()
    sub_widget = getattr(widget, widget_name)

    first_value = sub_widget.value()
    sub_widget.clear()

    changed_value = random.randrange(minimum, maximum)
    qtbot.keyClicks(
        sub_widget,
        str(changed_value)
    )
    widget.close()
    del sub_widget

    widget = setup_console_settings(qtbot)
    widget.show()
    sub_widget = getattr(widget, widget_name)
    last_value = sub_widget.value()

    assert last_value == changed_value
    assert last_value != first_value


def test_input_saves(qtbot):
    """
    Test input saves for children of ConsoleSettings.
    """
    setup_input_saves(
        qtbot,
        'write_latency_edit',
        minimum=50,
        maximum=500
    )

    setup_input_saves(
        qtbot,
        'scrollback_buffer_edit',
        minimum=50,
        maximum=5000
    )
