from typing import Self

from . import syntax_set
from .abstract_command import AbstractCommand, RuntimeManager

from.value import Value

# TODO read_code 메서드 사용하도록 변경

class PrintCommand(AbstractCommand):

    def __init__(self, code: str, value: Value):
        self.code = code
        self.value = value

    def run(self, runtime_manager: "RuntimeManager") -> None:
        print(chr(self.value.get_value(runtime_manager)), end="")

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        read_code = ""

        value = Value.from_code(code)
        if value is None: return None
        code, read_code = cls.read_code(code, read_code, value.code)

        if code.startswith(syntax_set.PRINT_COMMAND):
            code, read_code = cls.read_code(code, read_code, syntax_set.PRINT_COMMAND)

            return cls(read_code, value)

        else: return None