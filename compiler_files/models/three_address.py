from enum import Enum


class ThreeAddressOperators(Enum):
    # Aritmetical
    PLUS = '+'
    MINUS = '-'
    TIMES = '*'
    DIVIDE = '/'
    MOD = '%'

    # Boolean
    LESS_THAN = '<'
    LESS_EQUAL = '<='
    EQUAL = '=='
    OR = '||'
    AND = '&&'
    NOT = '!'
    NEGATE = '~'

    # Others
    GOTO = 'Goto'
    RETURN = 'Return'
    PUSHPARAM = 'PushParam'
    POPPARAMS = 'PopParams'
    FUNCTIONCALL = 'FCall'

    ASSIGN = '='


##### CLASES BASICAS #####
class ThreeAddressString:
    def __init__(self, value: str):
        self.value: str = value

    def to_string(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressInteger:
    def __init__(self, value: int):
        self.value: int = value

    def to_string(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressBoolean:
    def __init__(self, value: bool):
        self.value: bool = value

    def to_string(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressTemporal:
    def __init__(self, temporal_id: int):
        self.temporal_id: int = temporal_id

    def to_string(self) -> str:
        return f'_t{self.temporal_id}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()

class ThreeAddressFunctionCall:
    def __init__(self, function_name: str):
        self.function_name: str = function_name

    def to_string(self) -> str:
        return f'{self.function_name}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()

class ThreeAddressLabel:
    def __init__(self, label_id: int):
        self.label_id: int = label_id

    def to_string(self) -> str:
        return f'_L{self.label_id}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressVariable:
    def __init__(self, name: str):
        self.name: str = name

    def to_string(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressIf:
    def __init__(self, condition: ThreeAddressTemporal | ThreeAddressVariable, label: ThreeAddressLabel):
        self.condition: ThreeAddressTemporal | ThreeAddressVariable = condition
        self.label: ThreeAddressLabel = label

    def to_string(self) -> str:
        return f"Ifz {self.condition} {ThreeAddressOperators.GOTO.value} {self.label};"

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressOperation:
    def __init__(
        self,
        operator: ThreeAddressOperators,
        left_exp,
        right_exp,
        result: ThreeAddressTemporal | ThreeAddressVariable | ThreeAddressOperators | None = None
    ):

        self.operator: ThreeAddressOperators = operator
        self.left_exp = left_exp
        self.right_exp = right_exp
        self.result: ThreeAddressTemporal | ThreeAddressVariable | ThreeAddressOperators | None = result

    def to_string(self) -> str:
        text = 'NOT IMPLEMENTED'

        is_two_way = self.operator in [
            ThreeAddressOperators.PLUS,
            ThreeAddressOperators.MINUS,
            ThreeAddressOperators.TIMES,
            ThreeAddressOperators.DIVIDE,
            ThreeAddressOperators.MOD,
            ThreeAddressOperators.LESS_THAN,
            ThreeAddressOperators.LESS_EQUAL,
            ThreeAddressOperators.EQUAL,
            ThreeAddressOperators.OR,
            ThreeAddressOperators.AND,
        ]

        is_oneway_operator = self.operator in [
            ThreeAddressOperators.NOT,
            ThreeAddressOperators.NEGATE,
        ]

        is_one_way = self.operator in [
            ThreeAddressOperators.GOTO,
            ThreeAddressOperators.RETURN,
            ThreeAddressOperators.PUSHPARAM,
            ThreeAddressOperators.POPPARAMS,
            ThreeAddressOperators.FUNCTIONCALL,
        ]

        is_assign = self.operator == ThreeAddressOperators.ASSIGN

        if is_two_way:
            text = f"{self.result} = {self.left_exp} {self.operator.value} {self.right_exp};"
        elif is_one_way:
            text = f"{self.operator.value} {self.left_exp};"
        elif is_oneway_operator:
            text = f"{self.result} = {self.operator.value} {self.left_exp};"
        elif is_assign:
            text = f"{self.result} = {self.left_exp};"

        return text

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class ThreeAddressFunction:
    def __init__(self, name: str, is_main: bool = False, bytes: int = 0):
        self.name: str = name
        self.is_main: bool = is_main
        self.bytes: int = bytes
        self.code: list[ThreeAddressOperation] = []

    def add_operation(self, operation: ThreeAddressOperation):
        self.code.append(operation)

    def get_code(self) -> list[ThreeAddressOperation]:
        return [*self.code]

    def to_string(self) -> str:

        codes = ''

        for code in self.code:
            codes += f"\t\t{code}\n"

        text = f"{self.name}:\n" \
            f"\tBeginFunc {self.bytes};\n" \
            f"{codes}" \
            f"\tEndFunc;\n"

        return text

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()

    def get_three_code(self):
        all_code = []

        for code in self.code:
            if isinstance(code, ThreeAddressLabel):
                all_code.append(f'{code}:')
            else:
                all_code.append(str(code))

        return {
            'name': self.name,
            'is_main': False,
            'bytes': self.bytes,
            'body': all_code,
        }


class ThreeAddress:
    def __init__(self):
        self.temporals_count = 0
        self.label_count = 0
        self.functions: ThreeAddressFunction = []

    def get_functions(self) -> list[ThreeAddressFunction]:
        return [*self.functions]

    def add_function(self, function: ThreeAddressFunction):
        self.functions.append(function)

    def get_temporal(self) -> ThreeAddressTemporal:
        new_temporal = ThreeAddressTemporal(self.temporals_count)
        self.temporals_count += 1
        return new_temporal

    def get_label(self) -> ThreeAddressLabel:
        new_label = ThreeAddressLabel(self.label_count)
        self.label_count += 1
        return new_label

    def get_value_code(self, assosiated_code):

        if isinstance(assosiated_code, ThreeAddressOperation):
            return assosiated_code.result  # Variable o Temporal
        elif isinstance(assosiated_code, ThreeAddressBoolean):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressInteger):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressString):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressTemporal):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressVariable):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressLabel):
            return assosiated_code

        return None  # FIXME encontrar mejor forma de devolver algo y no None

    def filter_operations(self, *assosiated_codes):
        new_code = []

        for assosiated_code in assosiated_codes:
            for code in assosiated_code:
                if isinstance(code, ThreeAddressOperation) or isinstance(code, ThreeAddressLabel) or isinstance(code, ThreeAddressIf):
                    new_code.append(code)

        return new_code
