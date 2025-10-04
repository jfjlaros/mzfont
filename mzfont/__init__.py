from typing import Callable

from .make_font import MzFont


def doc_split(func: Callable) -> str:
    return func.__doc__.split('\n\n')[0]
