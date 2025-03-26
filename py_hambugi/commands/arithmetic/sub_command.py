from typing import Self

from ..abstract_command import AbstractCommand, RuntimeManager
from .. import syntax_set
from ..value import Value


class SubCommand(AbstractCommand):
    def __init__(self, code: str, target_variable: Value, sub_value: Value):
        self.code = code
        self.target_value: Value = target_variable
        self.sub_value: Value = sub_value

    def run(self, runtime_manager: "RuntimeManager") -> None:
        self.target_value.set_value(
            runtime_manager,
            self.target_value.get_value(runtime_manager)
            - self.sub_value.get_value(runtime_manager)
        )

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        if code.startswith(syntax_set.SUB_COMMAND):
            read_code = ""
            code, read_code = cls.read_code(code, read_code, syntax_set.SUB_COMMAND)

            target_value = Value.from_code(code)
            if target_value is None or not target_value.is_variable(): return None
            code, read_code = cls.read_code(code, read_code, target_value.code)

            sub_value = Value.from_code(code)
            if sub_value is None: return None
            code, read_code = cls.read_code(code, read_code, sub_value.code)

            return cls(read_code, target_value, sub_value)

        else:
            return None