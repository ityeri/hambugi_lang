from enum import Enum
from typing import Self


class ValueType(Enum):
    INT = 0

    A = 1
    B = 2
    C = 3


class Value:

    def __init__(self, code: str, value_type: ValueType, value: int | None = None):
        self.code = code
        self.value_type: ValueType = value_type
        self.value: int | None = value

    @classmethod
    def from_code(cls, code: str) -> Self | None:

        read_code = ""

        if code.startswith("햄부"):
            read_code += code[:2]
            code = code[2:]

            current_chr = ""
            decimal_value = [0]

            if code.startswith("가"): current_chr = "우"
            elif code.startswith("우"): current_chr = "가"
            else: return None

            while True:
                old_chr = current_chr

                if code.startswith("가"): current_chr = "가"
                elif code.startswith("우"): current_chr = "우"
                else: break

                read_code += code[1]
                code = code[1:]

                if old_chr != current_chr: decimal_value.append(0)

                decimal_value[-1] += 1


            final_value = int(
                "".join(map(lambda x: str(x), decimal_value))
            )

            return Value(read_code, ValueType.INT, final_value)

        else:
            return None