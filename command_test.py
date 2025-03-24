from py_hambugi.commands import PrintCommand
from py_hambugi import RuntimeManager
from py_hambugi.commands.value_copy_command import ValueCopyCommand

runtime_manager = RuntimeManager()

runtime_manager.a = 4
runtime_manager.b = 5
runtime_manager.c = 6

code = "햄부기 햄부 햄북어"

code = code.replace(" ", "").replace("\n", "")

value_copy_command = ValueCopyCommand.from_code(code)

value_copy_command.run(runtime_manager)

breakpoint()