from typing import Self

from py_hambugi.commands.abstract_command import AbstractCommand, RuntimeManager
from py_hambugi.commands import syntax_set
from py_hambugi.commands.value import Value
from py_hambugi.commands.jump.label_command import LabelCommand



class ZeroJumpCommand(AbstractCommand):
    def __init__(self, code: str, target_value: Value, label_id: int):
        self.code = code
        self.target_value: Value = target_value
        self.label_id: int = label_id

    def run(self, runtime_manager: RuntimeManager) -> None:
        if self.target_value.get_value(runtime_manager) == 0:
            runtime_manager.jump(self.label_id)

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        if code.startswith(syntax_set.ZERO_JUMP_COMMAND):
            read_code = ""
            code, read_code = cls.read_code(code, read_code, syntax_set.ZERO_JUMP_COMMAND)

            target_value = Value.from_code(code)
            if target_value is None: return None
            code, read_code = cls.read_code(code, read_code, target_value.code)

            label = LabelCommand.from_code(code)
            if label is None: return None
            code, read_code = cls.read_code(code, read_code, label.code)

            return cls(read_code, target_value, label.label_id)



        else: return None