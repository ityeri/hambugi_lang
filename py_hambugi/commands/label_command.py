from typing import Self

from .abstract_command import AbstractCommand, RuntimeManager
from . import syntax_set
from .value import Value



class LabelCommand(AbstractCommand):
    def __init__(self, code: str, label_id: int):
        self.code = code
        self.label_id = label_id

    def run(self, runtime_manager: RuntimeManager) -> None:
        ...

    @classmethod
    def from_code(cls, code: str) -> Self | None:
        if code.startswith(syntax_set.LABEL_COMMAND):
            read_code = ""
            code, read_code = cls.read_code(code, read_code, syntax_set.LABEL_COMMAND)

            label_id = 0

            while True:
                if code.startswith("우가"):
                    label_id += 1
                    code, read_code = cls.read_code(code, read_code, "우가")
                else: break

            return cls(read_code, label_id)



        else: return None