from typing import Self

from .abstract_command import AbstractCommand, RuntimeManager
from . import syntax_set
from .value import Value


class ValueCopyCommand(AbstractCommand):
    def __init__(self, code: str, copy_variable: Value, target_variable: Value):
        self.code = code
        self.copy_variable: Value = copy_variable
        self.target_variable: Value = target_variable

    def run(self, runtime_manager: "RuntimeManager") -> None:
        self.target_variable.set_value(
            runtime_manager,
            self.copy_variable.get_value(runtime_manager))

    @classmethod
    def from_code(cls, code: str) -> Self | None:

        if code.startswith(syntax_set.COPY_COMMAND):
            read_code = ""
            code, read_code = cls.read_code(code, read_code, syntax_set.COPY_COMMAND)

            copy_value = Value.from_code(code)
            if copy_value is None or not copy_value.is_variable(): return None
            code, read_code = cls.read_code(code, read_code, copy_value.code)

            target_value = Value.from_code(code)
            if target_value is None or not target_value.is_variable(): return None
            code, read_code = cls.read_code(code, read_code, target_value.code)

            return cls(read_code, copy_value, target_value)

        else: return None