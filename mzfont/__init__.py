from typing import Callable

from .make_font import MzFont


__authors__ = [{'name': 'Jeroen F.J. Laros', 'email': 'jlaros@fixedpoint.nl'}]
__copyright__ = (
    f'Copyright (c) 2025 by {__authors__[0]["name"]} '
    f'<{__authors__[0]["email"]}>')
__description__ = 'Sharp MZ TrueType font.'
__keywords__ = ['Sharp', 'MZ', 'font', 'TrueType']
__project__ = 'MzFont'
__url__ = 'https://github.com/jfjlaros/mzfont'
__version__ = '0.0.1'

__info__ = (
    f'{__project__} version {__version__}\n\n'
    f'{__copyright__}\nHomepage: {__url__}')


def doc_split(func: Callable) -> str:
    return func.__doc__.split('\n\n')[0]
