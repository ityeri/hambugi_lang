class PyHambugi:
    def __init__(self):
        self.raw_code: str = None

    def set_code(self, raw_code: str):
        self.raw_code = raw_code.replace(" ", "")