from typing import Self

from .abstract_command import AbstractCommand, RuntimeManager



class PrintCommand(AbstractCommand):

    def __init__(self):
        ...

    def run(self, runtime_manager: "RuntimeManager") -> None:
        pass

    def from_code(cls, code: str) -> Self | None:
        ...