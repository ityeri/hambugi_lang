from typing import Self

from ..abstract_command import AbstractCommand, RuntimeManager
from .. import syntax_set
from ..value import Value



class WriteCommand(AbstractCommand):
    def __init__(self, code: str, index_value: Value, write_value):
        self.code = code
        self.index_value: Value = index_value
        self.write_value: Value = write_value

    def run(self, runtime_manager: "RuntimeManager") -> None:
        runtime_manager.set_memory_at(
            self.index_value.get_value(runtime_manager),
            self.write_value.get_value(runtime_manager)
        )

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        if code.startswith(syntax_set.WRITE_COMMAND):
            read_code = ""
            code, read_code = cls.read_code(code, read_code, syntax_set.WRITE_COMMAND)

            index_value = Value.from_code(code)
            if index_value is None: return None
            code, read_code = cls.read_code(code, read_code, index_value.code)

            write_value = Value.from_code(code)
            if write_value is None: return None
            code, read_code = cls.read_code(code, read_code, write_value.code)

            return cls(read_code, index_value, write_value)

        else: return None