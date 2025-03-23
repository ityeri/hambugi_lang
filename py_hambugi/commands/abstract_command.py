from abc import ABCMeta, abstractmethod, abstractproperty
from typing import Self

from ..runtime_manager import RuntimeManager



class AbstractCommand(metaclass=ABCMeta):

    code: str

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    def run(self, runtime_manager: "RuntimeManager") -> None: ...

    @classmethod
    @abstractmethod
    def get_command(cls, code: str) -> Self | None: ...