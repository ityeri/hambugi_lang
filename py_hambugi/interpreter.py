class Interpreter:
    def __init__(self):
        self.raw_code: str = None
        self.code_read_pointer: int = 0

    def shift_pointer(self, pointer: int):
        self.code_read_pointer += pointer

    def seek(self): self.code_read_pointer = 0


    def set_code(self, raw_code: str):
        self.raw_code = raw_code.replace(" ", "").replace("\n", "")
        self.seek()



