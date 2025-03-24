from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Self

from ..runtime_manager import RuntimeManager



class AbstractCommand(metaclass=ABCMeta):

    code: str

    @abstractmethod
    def __init__(self, code: str): ...

    @abstractmethod
    def run(self, runtime_manager: "RuntimeManager") -> None: ...

    @classmethod
    @abstractmethod
    def from_code(cls, code: str) -> Self | None: ...

    @staticmethod
    def read_code(code: str, read_code: str, readable_code: str) -> tuple[str, str]:
        if not code.startswith(readable_code): raise ValueError("code 문자열이 readable_code 문자열로 시작하지 않습니다")

        read_code += code[:len(readable_code)]
        code = code[len(readable_code):]

        return code, read_code