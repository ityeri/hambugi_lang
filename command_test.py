from py_hambugi.commands import WriteCommand
from py_hambugi import RuntimeManager

runtime_manager = RuntimeManager()

runtime_manager.a = 2
runtime_manager.b = 10

code = "햄부거 햄부 햄북어"

code = code.replace(" ", "").replace("\n", "")

command = WriteCommand.from_code(code)

command.run(runtime_manager)

breakpoint()