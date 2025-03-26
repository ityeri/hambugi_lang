from enum import Enum
from typing import Self
from ..runtime_manager import RuntimeManager
from . import syntax_set


class ValueType(Enum):
    INT = 0

    A = 1
    B = 2
    C = 3


class Value:

    def __init__(self, code: str, value_type: ValueType, int_value: int | None = None):
        self.code = code
        self.value_type: ValueType = value_type
        self._value: int | None = int_value

    def is_variable(self): return self.value_type != ValueType.INT



    def get_value(self, runtime_manager: RuntimeManager) -> int:
        if self.value_type == ValueType.INT: return self._value

        elif self.value_type == ValueType.A: return runtime_manager.a
        elif self.value_type == ValueType.B: return runtime_manager.b
        elif self.value_type == ValueType.C: return runtime_manager.c

    def set_value(self, runtime_manager: RuntimeManager, value: int):
        if self.value_type == ValueType.INT:
            raise TypeError(f"value_type 이 {self.value_type} 인 Value 에 대해서는 set_value 를 수행할수 없습니다")

        elif self.value_type == ValueType.A: runtime_manager.a = value
        elif self.value_type == ValueType.B: runtime_manager.b = value
        elif self.value_type == ValueType.C: runtime_manager.c = value



    @classmethod
    def from_code(cls, code: str) -> Self | None:

        if code.startswith(syntax_set.B): return Value( code[:len(syntax_set.B)], ValueType.B )
        elif code.startswith(syntax_set.C): return Value( code[:len(syntax_set.C)], ValueType.C )

        elif code.startswith(syntax_set.VALUE_PREFIX):
            read_code = ""

            read_code += code[:len(syntax_set.VALUE_PREFIX)]
            code = code[len(syntax_set.VALUE_PREFIX):]

            current_chr = ""
            decimal_value = [0]

            if (not code.startswith("가") and not code.startswith("우")
                   and not code.startswith("구")):

                return Value(read_code, ValueType.A)


            while True:
                old_chr = current_chr

                if code.startswith("가"): current_chr = "가"
                elif code.startswith("우"): current_chr = "우"
                elif code.startswith("구"): current_chr = "구"
                elif len(read_code) == 0: break
                else: break

                read_code += code[:1]
                code = code[1:]

                if old_chr != current_chr: decimal_value.append(0)
                elif current_chr == "구": decimal_value.append(0)

                if current_chr != "구": decimal_value[-1] += 1


            final_value = int(
                "".join(map(lambda x: str(x), decimal_value))
            )

            return Value(read_code, ValueType.INT, final_value)

        elif code.startswith(syntax_set.A):
            ... # 변수 A 를 지칭하는 "햄부" 문법은 윗줄의 code.startswith(syntax_set.VALUE_PREFIX) 에서 감지함

        else:
            return None