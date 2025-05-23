from .commands import AbstractCommand, LabelCommand
from .command_sets import hambugi_lang_command_set
from .runtime_manager import RuntimeManager


class Interpreter:
    def __init__(self):
        self.raw_code: str = None
        self.commands: list[AbstractCommand] = None
        self.command_index: int = 0

        self.runtime_manager: RuntimeManager = None

    def set_code(self, raw_code: str):
        self.raw_code = raw_code.replace(" ", "").replace("\n", "")
        code = self.raw_code

        self.commands = list()
        self.command_index = 0

        self.runtime_manager = RuntimeManager()


        while len(code) != 0:

            is_read = False

            for command_cls in hambugi_lang_command_set:

                command = command_cls.from_code(code)

                if command is not None:

                    code, _ = read_code(code, "", command.code)
                    self.commands.append(command)
                    is_read = True

                    break

            if not is_read: code = code[1:len(code)]



    def run(self):
        while True:
            self.commands[self.command_index].run(self.runtime_manager)

            jump_label_id = self.runtime_manager.jump_dispose()

            if jump_label_id is None:
                self.command_index += 1
            else:
                for i, command in enumerate(self.commands):

                    if isinstance(command, LabelCommand):
                        if command.label_id == jump_label_id:
                            self.command_index = i

            if self.command_index == len(self.commands): break



def read_code(code: str, read_code: str, readable_code: str) -> tuple[str, str]:
    if not code.startswith(readable_code): raise ValueError("code 문자열이 readable_code 문자열로 시작하지 않습니다")

    read_code += code[:len(readable_code)]
    code = code[len(readable_code):]

    return code, read_code