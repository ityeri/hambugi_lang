from .commands.abstract_command import AbstractCommand
from .command_sets import hambugi_lang


class Interpreter:
    def __init__(self):
        self.raw_code: str = None
        self.commands: list[AbstractCommand] = None

    def set_code(self, raw_code: str):
        self.raw_code = raw_code.replace(" ", "").replace("\n", "")
        self.commands = list()

        while len(self.raw_code) == 0:
            for Command in hambugi_lang:

                command = Command(raw_code)

                if command is not None:

                    self.raw_code = self.raw_code[:len(command.code)]
                    self.commands.append(command)

                    break