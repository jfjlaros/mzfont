MzFont: Sharp MZ TrueType font generator
========================================

.. image:: https://img.shields.io/github/last-commit/jfjlaros/mzfont.svg
   :target: https://github.com/jfjlaros/mzfont/graphs/commit-activity
.. image:: https://readthedocs.org/projects/mzfont/badge/?version=latest
   :target: https://mzfont.readthedocs.io/en/latest
.. image:: https://img.shields.io/github/release-date/jfjlaros/mzfont.svg
   :target: https://github.com/jfjlaros/mzfont/releases
.. image:: https://img.shields.io/github/release/jfjlaros/mzfont.svg
   :target: https://github.com/jfjlaros/mzfont/releases
.. image:: https://img.shields.io/pypi/v/mzfont.svg
   :target: https://pypi.org/project/mzfont/
.. image:: https://img.shields.io/github/languages/code-size/jfjlaros/mzfont.svg
   :target: https://github.com/jfjlaros/mzfont
.. image:: https://img.shields.io/github/languages/count/jfjlaros/mzfont.svg
   :target: https://github.com/jfjlaros/mzfont
.. image:: https://img.shields.io/github/languages/top/jfjlaros/mzfont.svg
   :target: https://github.com/jfjlaros/mzfont
.. image:: https://img.shields.io/github/license/jfjlaros/mzfont.svg
   :target: https://raw.githubusercontent.com/jfjlaros/mzfont/master/LICENSE.md
----

This package provides a way to generate and test several Sharp MZ TrueType
fonts.


Quick start
-----------

Download the Sharp MZ character and monitor ROMs_ and run the following
command.

.. code:: bash

    mzfont make mz700fon.int 1z-013a.rom ~/.local/share/fonts/SharpMZ.ttf
    fc-cache -fv ~/.local/share/fonts

Open a new terminal that uses the Sharp MZ font.

::

    foot -f SharpMZ

.. image:: https://raw.githubusercontent.com/jfjlaros/mzfont/master/docs/images/normal_font.png

The `default` subcommand additionally changes the default font, uses square
characters and removes line spacing.

.. image:: https://raw.githubusercontent.com/jfjlaros/mzfont/master/docs/images/default_font.png

Please see ReadTheDocs_ for the latest documentation.


.. _ROMs: https://ia803204.us.archive.org/view_archive.php?archive=/29/items/mame-0.221-roms-merged/mz700.zip
.. _ReadTheDocs: https://mzfont.readthedocs.io
