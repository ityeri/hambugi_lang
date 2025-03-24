from py_hambugi.commands.value import Value, RuntimeManager

runtime_manager = RuntimeManager()

runtime_manager.a = 11
runtime_manager.b = 22
runtime_manager.c = 33

value = Value.from_code("햄부가구구구구가가가구구구우우우")

print(value.get_value(runtime_manager))

# value.set_value(runtime_manager, 100)
#
# print(
#     runtime_manager.a, runtime_manager.b, runtime_manager.c, value.code
# )