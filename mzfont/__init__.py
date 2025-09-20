__authors__ = [{'name': 'Jeroen F.J. Laros', 'email': 'jlaros@fixedpoint.nl'}]
__copyright__ = f'Copyright (c) 2025 by {__authors__[0]["name"]} <{__authors__[0]["email"]}>'
__description__ = 'Sharp MZ TrueType font.'
__keywords__ = ['Sharp', 'MZ', 'font', 'TrueType']
__url__ = 'https://github.com/jfjlaros/mzfont'
__version__ = '0.0.1'

usage = [__description__, __copyright__]


def doc_split(func):
    return func.__doc__.split('\n\n')[0]


def version(name):
    return f'{name} version {__version__}\n\n{__copyright__}\nHomepage: {__url__}'
