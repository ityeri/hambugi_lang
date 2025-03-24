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
    def read_code(code: str, read_code: str, readable_code: str):
        read_code += code[:len(readable_code)]
        code = code[len(readable_code):]