from typing import Self

from .abstract_command import AbstractCommand, RuntimeManager
from . import syntax_set
from .value import Value



class TemplateCommand(AbstractCommand):
    def __init__(self, code: str):
        self.code = code
        ...

    def run(self, runtime_manager: "RuntimeManager") -> None:
        ...

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        if code.startswith(...):
            ...

        else: return None