from typing import Type

from .commands import *

hambugi_lang: list[Type[AbstractCommand]] = [
    PrintCommand
]