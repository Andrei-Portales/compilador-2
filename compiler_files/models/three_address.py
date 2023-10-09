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
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressString):
            return False
        
        return self.value == other.value


class ThreeAddressInteger:
    def __init__(self, value: int):
        self.value: int = value

    def to_string(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressInteger):
            return False
        
        return self.value == other.value


class ThreeAddressBoolean:
    def __init__(self, value: bool):
        self.value: bool = value

    def to_string(self) -> str:
        return 'true' if self.value else 'false'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressBoolean):
            return False
        
        return self.value == other.value
    
class ThreeAddressVoid:
    def to_string(self) -> str:
        return 'null'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressVoid):
            return False
        
        return True


class ThreeAddressTemporal:
    def __init__(self, temporal_id: int):
        self.temporal_id: int = temporal_id

    def to_string(self) -> str:
        return f'_t{self.temporal_id}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressTemporal):
            return False
        
        return self.temporal_id == other.temporal_id

class ThreeAddressFunctionCall:
    def __init__(self, function_name: str):
        self.function_name: str = function_name

    def to_string(self) -> str:
        return f'{self.function_name}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressFunctionCall):
            return False
        
        return self.function_name == other.function_name

class ThreeAddressLabel:
    def __init__(self, label_id: int):
        self.label_id: int = label_id

    def to_string(self) -> str:
        return f'_L{self.label_id}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressLabel):
            return False
        
        return self.label_id == other.label_id


class ThreeAddressVariable:
    def __init__(
            self, 
            name: str, 
            value: ThreeAddressInteger | ThreeAddressString | ThreeAddressBoolean | ThreeAddressVoid | None = None
        ):
        
        self.name: str = name
        self.value:  ThreeAddressInteger | ThreeAddressString | ThreeAddressBoolean | ThreeAddressVoid | None = value

    def to_string(self) -> str:
        return self.name
    
    def get_var_value(self) -> ThreeAddressInteger | ThreeAddressString | ThreeAddressBoolean | ThreeAddressVoid | None:
        return self.value

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressVariable):
            return False
        
        return self.name == other.name
    
    def get_three_code(self):
        return {
            'name': self.name,
            'value': str(self.value),
        }


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
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressIf):
            return False
        
        return self.condition == other.condition \
            and self.label == other.label


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
        
        self.optimize()

    def optimize(self): # OPMITIZACION DE OPERACIONES
        is_trivial = type(self.left_exp) in [ThreeAddressInteger, ThreeAddressBoolean] \
            and type(self.right_exp) in [ThreeAddressInteger, ThreeAddressBoolean]
            
        result = None
            
        if is_trivial:
            if self.operator == ThreeAddressOperators.PLUS:
                result = ThreeAddressInteger(self.left_exp.value + self.right_exp.value)
            elif self.operator == ThreeAddressOperators.MINUS:
                result = ThreeAddressInteger(self.left_exp.value - self.right_exp.value)
            elif self.operator == ThreeAddressOperators.TIMES:
                result = ThreeAddressInteger(self.left_exp.value * self.right_exp.value)
            elif self.operator == ThreeAddressOperators.DIVIDE:
                result = ThreeAddressInteger(self.left_exp.value / self.right_exp.value)
            elif self.operator == ThreeAddressOperators.MOD:
                result = ThreeAddressInteger(self.left_exp.value % self.right_exp.value)
            elif self.operator == ThreeAddressOperators.LESS_THAN:
                result = ThreeAddressBoolean(self.left_exp.value < self.right_exp.value)
            elif self.operator == ThreeAddressOperators.LESS_EQUAL:
                result = ThreeAddressBoolean(self.left_exp.value <= self.right_exp.value)
            elif self.operator == ThreeAddressOperators.EQUAL:
                result = ThreeAddressBoolean(self.left_exp.value == self.right_exp.value)
            elif self.operator == ThreeAddressOperators.OR:
                result = ThreeAddressBoolean(self.left_exp.value or self.right_exp.value)
            elif self.operator == ThreeAddressOperators.AND:
                result = ThreeAddressBoolean(self.left_exp.value and self.right_exp.value)
            elif self.operator == ThreeAddressOperators.NOT:
                result = ThreeAddressBoolean(not self.left_exp.value)
            elif self.operator == ThreeAddressOperators.NEGATE:
                result = ThreeAddressInteger(-self.left_exp.value)
        
            if result is not None:
                self.right_exp = None
                self.left_exp = result
                self.operator = ThreeAddressOperators.ASSIGN
                

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
    
    def __eq__(self, other):
        if not isinstance(other, ThreeAddressOperation):
            return False
        
        return self.operator == other.operator \
            and self.left_exp == other.left_exp \
            and self.right_exp == other.right_exp \
            and self.result == other.result


class ThreeAddressFunction:
    def __init__(self, name: str, is_main: bool = False, bytes: int = 0):
        self.name: str = name
        self.is_main: bool = is_main
        self.bytes: int = bytes
        self.code: list[ThreeAddressOperation] = []

    def add_operation(self, operation: ThreeAddressOperation):
        self.code.append(operation)

    def to_string(self) -> str:
        codes = ''

        for code in self.code:
            if len(code.to_string().strip()) > 0:
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
    
    def optimize(self):
        new_code = []
        
        for code in self.code:
            if len(new_code) > 0:
                if code == new_code[-1] and isinstance(code.result, ThreeAddressVariable):
                    continue
                
            new_code.append(code)
            
        self.code = new_code

    def get_three_code(self):
        self.optimize()
        all_code = []

        for code in self.code:
            
            if code is None:
                return ''
            
            if isinstance(code, ThreeAddressLabel):
                all_code.append(f'{code}:')
            else:
                if len(code.to_string().strip()) > 0:
                    all_code.append(code.to_string())

        return {
            'name': self.name,
            'is_main': False,
            'bytes': self.bytes,
            'body': all_code,
        }
        
class ThreeAddressClassDefinition:
    def __init__(self, name: str):
        self.name: str = name
        
    def to_string(self) -> str:
        return f'{self.name}'
    
    def __str__(self) -> str:
        return self.to_string()
    
    def __repr__(self) -> str:
        return self.to_string()

class ThreeAddressClass:
    def __init__(self, name: str):
        self.name: str = name
        self.functions: list[ThreeAddressFunction] = []
        self.variables: list[ThreeAddressVariable] = []
        
    def add_code(self, function):
        if isinstance(function, ThreeAddressFunction):
            self.functions.append(function)
        elif isinstance(function, ThreeAddressVariable):
            self.variables.append(function)
        
    def get_three_code(self):
        all_code = []
        all_variables = []
        
        for function in self.functions:
            all_code.append(function.get_three_code())
            
        for variable in self.variables:
            all_variables.append(variable.get_three_code())
            
        return {
            'name': self.name,
            'functions': all_code,
            'variables': all_variables,
        }
        
    def to_string(self):
        codes = ''
        
        for function in self.functions:
            codes += f'{function}\n'
        
        return f'class {self.name}:\n{codes}'
    
    def __str__(self):
        return self.to_string()
    
    def __repr__(self):
        return self.to_string()

class ThreeAddress:
    def __init__(self):
        self.temporals_count = 0
        self.label_count = 0
        self.classes: list[ThreeAddressClass] = []
        self.recycled_temporals: list[ThreeAddressTemporal] = []
        
    def add_recycled_temporal(self, temporal: ThreeAddressTemporal):
        self.recycled_temporals.append(temporal)

    def add_class(self, clas: ThreeAddressClass):
        self.classes.append(clas)

    def get_temporal(self) -> ThreeAddressTemporal:
        if len(self.recycled_temporals) > 0:
            new_temporal = self.recycled_temporals[0]
            del self.recycled_temporals[0]
            return new_temporal
        
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
        elif isinstance(assosiated_code, ThreeAddressVoid):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressInteger):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressString):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressTemporal):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressClassDefinition):
            return assosiated_code
        elif isinstance(assosiated_code, ThreeAddressVariable):
            if assosiated_code.value is not None:
                return assosiated_code.value
            
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
