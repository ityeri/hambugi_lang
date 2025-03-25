class RuntimeManager:
    def __init__(self):
        self.a: int = 0
        self.b: int = 0
        self.c: int = 0

        self._memory: list[int] = list()

        self._jump_label_id: int | None = None

    def _extend(self, index: int):
        if len(self._memory) < index:
            self._memory.extend(
                [0 for _ in range(index - len(self._memory) + 1)]
            )


    def get_memory_at(self, index: int) -> int:
        self._extend(index)
        return self._memory[index]

    def set_memory_at(self, index: int, value: int):
        self._extend(index)
        self._memory[index] = value


    def jump(self, label_id: int):
        if self._jump_label_id is not None:
            raise RuntimeError("_jump_label_id 가 None 아 아닐때 jump 메서드는 수행될수 없습니다")

        self._jump_label_id = label_id

    def jump_dispose(self) -> int | None:
        jump_label_id = self._jump_label_id
        self._jump_label_id = None

        return  jump_label_id