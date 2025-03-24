from py_hambugi.commands.value import Value, RuntimeManager

runtime_manager = RuntimeManager()

runtime_manager.a = 10
runtime_manager.b = 20
runtime_manager.c = 30

value = Value.from_code("햄부기")

value.set_value(runtime_manager, 100)

print(
    runtime_manager.a, runtime_manager.b, runtime_manager.c, value.code
)