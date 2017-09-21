Installation
============

AlphaHooks can currently be only installed from source. The steps are pretty straightforward.

AlphaHooks only supports Python versions 3.5 and later. Download the `latest version <https://www.python.org/downloads/>`_ of Python.

If it's already installed, check if you have the correct version using one of these commands.

::

    python --version
    py --version

Make sure you have the latest version of ``pip`` installed using one of these commands.

::

    pip -V
    python -m pip -V

Installing from source
----------------------

Requirements
^^^^^^^^^^^^

AlphaHooks needs these packages to work properly.

- `PyQt5 <https://www.riverbankcomputing.com/software/pyqt/download5>`_>=5.9
- `qscintilla <https://www.riverbankcomputing.com/software/qscintilla/download>`_>=2.10.1
- `json_config <http://json-config.readthedocs.io/en/develop/installation.html>`_>=2.0.1
- `Sphinx <http://www.sphinx-doc.org/en/stable/tutorial.html#install-sphinx>`_>=1.6.3


Installation
^^^^^^^^^^^^

Grab the development version from Github.

::

    git clone https://github.com/daegontaven/AlphaHooks.git

Change into the directory and install with ``pip``.

::

    cd AlphaHooks
    pip install .

Run AlphaHooks

::

    python AlphaHooks/main.py

Running directly
----------------

`Installing from source`_ is not required. Installing the requirements and just running ``main.py`` will work fine.

::

    pip install -r requirements.txt
    python AlphaHooks/main.py