from sys import modules
from types import ModuleType

mock = ModuleType('fontforge')
mock.font = object
mock.open = object
modules['fontforge'] = mock
mock = ModuleType('psMat')
mock.scale = object
modules['psMat'] = mock

from mzfont import __authors__, __copyright__, __project__, __version__


author = __authors__[0]['name']
copyright = __copyright__
project = __project__
release = __version__

autoclass_content = 'both'
extensions = [
    'sphinx.ext.autodoc', 'sphinx_autodoc_typehints', 'sphinxarg.ext']
