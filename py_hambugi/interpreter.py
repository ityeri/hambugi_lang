from .commands.abstract_command import AbstractCommand


class Interpreter:
    def __init__(self):
        self.raw_code: str = None
        self.commands: list[AbstractCommand] = None

    def set_code(self, raw_code: str):
        self.raw_code = raw_code.replace(" ", "").replace("\n", "")
        self.commands = list()