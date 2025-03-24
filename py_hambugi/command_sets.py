from typing import Type

from .commands import *
from .commands.value_copy_command import ValueCopyCommand

hambugi_lang_command_set: list[Type[AbstractCommand]] = [
    ValueCopyCommand,

    AddCommand,
    SubCommand,

    ReadCommand,
    WriteCommand,

    PrintCommand
]