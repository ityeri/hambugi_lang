class RuntimeManager:
    def __init__(self):
        self.a: int = 0
        self.b: int = 0
        self.c: int = 0

        self._memory: list[int] = list()

    def extend(self, index: int):
        if len(self._memory) < index:
            self._memory.extend(
                [0 for _ in range(index - len(self._memory) + 1)]
            )

    def get_memory_at(self, index: int) -> int:
        self.extend(index)
        return self._memory[index]

    def set_memory_at(self, index: int, value: int):
        self.extend(index)
        self._memory[index] = value