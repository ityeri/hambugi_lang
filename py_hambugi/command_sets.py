from typing import Type

from .commands import *
from py_hambugi.commands.arithmetic.set_command import SetCommand

hambugi_lang_command_set: list[Type[AbstractCommand]] = [
    SetCommand,

    AddCommand,
    SubCommand,

    ReadCommand,
    WriteCommand,

    PrintCommand,

    LabelCommand,
    ZeroJumpCommand
]