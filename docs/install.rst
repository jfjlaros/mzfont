Installation
============

MzFont depends on FontForge_. For Debian based systems, the following command
will install this dependency.

::

    apt install python3-fontforge

If the software is to be installed in a virtual environment, make sure that
access to system site-packages is enabled.

::

    python -m venv --system-site-packages ~/.venv/mzfont
    . ~/.venv/mzfont/bin/activate

The software is distributed via PyPI_, it can be installed with ``pip``:

::

    pip install mzfont


From source
-----------

The source is hosted on GitHub_, to install the latest development version,
use the following commands.

::

    git clone https://github.com/jfjlaros/mzfont
    cd mzfont
    pip install .


.. _FontForge: https://fontforge.org
.. _GitHub: https://github.com/jfjlaros/mzfont.git
.. _PyPI: https://pypi.python.org/pypi/mzfont

