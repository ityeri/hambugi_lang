from typing import Self

from .abstract_command import AbstractCommand, RuntimeManager
from . import syntax_set
from .value import Value



class ReadCommand(AbstractCommand):
    def __init__(self, code: str, index_value: Value, target_variable):
        self.code = code
        self.index_value: Value = index_value
        self.target_variable: Value = target_variable

    def run(self, runtime_manager: "RuntimeManager") -> None:
        self.target_variable.set_value(
            runtime_manager,
            runtime_manager.get_memory_at(self.index_value.get_value(runtime_manager))
        )

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        if code.startswith(syntax_set.READ_COMMAND):
            read_code = ""

            index_value = Value.from_code(code)
            if index_value is None or not index_value.is_variable(): return None
            code, read_code = cls.read_code(code, read_code, index_value.code)

            target_value = Value.from_code(code)
            if target_value is None or not target_value.is_variable(): return None
            code, read_code = cls.read_code(code, read_code, target_value.code)

            return cls(read_code, index_value, target_value)

        else: return None