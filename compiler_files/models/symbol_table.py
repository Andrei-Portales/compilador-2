from .compiler_types import CompilerType, PrimitiveType


class SymbolTableValue:
    def __init__(self,
                 type: CompilerType = None,
                 name: str = None,
                 var_value_type: CompilerType = None,
                 ) -> None:

        self.type: CompilerType = type
        self.name: str = name
        self.var_value_type: CompilerType = var_value_type

        if self.var_value_type is None and self.type is not None:
            if self.type.compare(CompilerType(PrimitiveType.INTEGER)):
                self.var_value_type = CompilerType(PrimitiveType.INTEGER)
            elif self.type.compare(CompilerType(PrimitiveType.STRING)):
                self.var_value_type = CompilerType(PrimitiveType.STRING)
            elif self.type.compare(CompilerType(PrimitiveType.BOOLEAN)):
                self.var_value_type = CompilerType(PrimitiveType.BOOLEAN)
            else:
                self.var_value_type = CompilerType(
                    PrimitiveType.CUSTOM_TYPE, 'void')

    def to_string(self) -> str:
        return f'value {self.type} {self.name}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class SymbolTableLet(SymbolTableValue):
    def __init__(self,
                 type: CompilerType = None,
                 name: str = None,
                 variables: dict[str, SymbolTableValue] = None,
                 ) -> None:

        super().__init__(type, name)
        self.variables = variables or {}

    def add_variable(self, name: str, variable: SymbolTableValue) -> None:
        self.variables[name] = variable

    def to_string(self) -> str:
        return f'Let {self.name} {{\n\t{self.variables}\n}}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class SymbolTableMethod(SymbolTableValue):
    def __init__(self,
                 type: CompilerType,
                 name: str,
                 params: list[SymbolTableValue] = [],
                 local_vars: dict[str, SymbolTableValue] = {},
                 ):

        super().__init__(type, name)
        self.params: list[SymbolTableValue] = params
        self.local_vars: dict[str, SymbolTableValue] = local_vars

    def add_param(self, param: SymbolTableValue) -> None:
        self.params.append(param)

    def add_local_var(self, name: str, local_var: SymbolTableValue) -> None:
        self.local_vars[name] = local_var

    def to_string(self) -> str:
        return f'Method {self.name} {{\n\t{self.params}\n\t{self.local_vars}\n}}'

    def check_signiture(self, method: 'SymbolTableMethod') -> bool:
        if len(self.params) != len(method.params):
            return False

        if not self.type.compare(method.type):
            return False

        for i in range(len(self.params)):
            if not self.params[i].type.compare(method.params[i].type):
                return False

        return True

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


class SymbolTableClass(SymbolTableValue):
    def __init__(self,
                 type: CompilerType,
                 name: str,
                 inherit: 'SymbolTableClass' = None,
                 attrs: dict[str, SymbolTableValue] = {},
                 methods: dict[str, SymbolTableMethod] = {},
                 ) -> None:

        super().__init__(type, name)
        self.inherit: 'SymbolTableClass' = inherit
        self.attrs: dict[str, SymbolTableValue] = {
            **attrs,
            'self': SymbolTableValue(type, 'self', type),
        }
        self.methods: dict[str, SymbolTableMethod] = methods

    def add_attr(self, name: str, attr: CompilerType) -> None:
        self.attrs[name] = attr

    def add_method(self, name: str, method: SymbolTableMethod) -> None:
        self.methods[name] = method

    def to_string(self) -> str:
        inherit = ''

        if self.inherit:
            inherit = f' inherits {str(self.inherit)} ->'

        return f'Class {self.name}{inherit} {{\n\t{self.attrs}\n\t{self.methods}\n}}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


# BOOLEAN
boolean_type = SymbolTableClass(
    CompilerType(PrimitiveType.BOOLEAN),
    'Boolean',
    None,
    {},
    {},
)

# Integer
integer_type = SymbolTableClass(
    CompilerType(PrimitiveType.INTEGER),
    'Integer',
    None,
    {},
    {},
)

# String
string_type = SymbolTableClass(
    CompilerType(PrimitiveType.STRING),
    'String',
    None,
    {
        'value': SymbolTableValue(CompilerType(PrimitiveType.STRING), 'value'),
    },
    {
        'length': SymbolTableMethod(
            CompilerType(PrimitiveType.INTEGER),
            'length',
        ),
        'concat': SymbolTableMethod(
            CompilerType(PrimitiveType.STRING),
            'concat',
        ),
        'substr': SymbolTableMethod(
            CompilerType(PrimitiveType.STRING),
            'substr',
            params=[
                SymbolTableValue(CompilerType(PrimitiveType.INTEGER), 'i'),
                SymbolTableValue(CompilerType(PrimitiveType.INTEGER), 'l'),
            ],
        ),
    },
)

# OBJECT
object_type = SymbolTableClass(
    CompilerType(PrimitiveType.CUSTOM_TYPE, 'Object'),
    'Object',
    None,
    {},
    {
        'abort': SymbolTableMethod(
            CompilerType(PrimitiveType.CUSTOM_TYPE, 'Object'),
            'abort',
        ),
        'type_name': SymbolTableMethod(
            CompilerType(PrimitiveType.STRING),
            'type_name',
        ),
        'copy': SymbolTableMethod(
            CompilerType(PrimitiveType.CUSTOM_TYPE, 'SELF_TYPE'),
            'copy',
        ),
    },
)

# void
void_type = SymbolTableClass(
    CompilerType(PrimitiveType.CUSTOM_TYPE, 'void'),
    'void',
    None,
    {},
    {},
)


class SymbolTableProgram:
    def __init__(self, classes: dict[str, SymbolTableClass] = {}) -> None:
        self.classes: dict[str, SymbolTableClass] = classes

    def add_class(self, name: str, class_scope: SymbolTableClass) -> None:
        self.classes[name] = class_scope

    def to_string(self) -> str:
        return f'Program {{\n\t{self.classes}\n}}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


PRIMITIVE_TYPES = {
    'Boolean': boolean_type,
    'Integer': integer_type,
    'String': string_type,
}


class SymbolTable:
    def __init__(self, context: SymbolTableProgram | SymbolTableClass | SymbolTableMethod | SymbolTableLet) -> None:

        if not context:
            raise Exception('Context is required')

        self.scope_context: SymbolTableValue | SymbolTableClass | SymbolTableMethod | SymbolTableLet = context

        if isinstance(self.scope_context, SymbolTableProgram):
            self.scope_context.classes = {
                **PRIMITIVE_TYPES,
                'Object': object_type,
                'void': void_type,
            }

    def add(self, name: str, type_scope: SymbolTableClass | SymbolTableMethod | SymbolTableValue | SymbolTableLet, is_method_param=False) -> None:

        if isinstance(self.scope_context, SymbolTableProgram):
            if isinstance(type_scope, SymbolTableClass):
                self.scope_context.add_class(name, type_scope)
            else:
                raise Exception('Only classes can be added to the program')

        elif isinstance(self.scope_context, SymbolTableClass):
            if isinstance(type_scope, SymbolTableMethod):
                self.scope_context.add_method(name, type_scope)
            elif isinstance(type_scope, SymbolTableValue):
                self.scope_context.add_attr(name, type_scope)
            else:
                raise Exception(
                    'Only methods and attributes can be added to the class')

        elif isinstance(self.scope_context, SymbolTableMethod):
            if isinstance(type_scope, SymbolTableValue):
                if is_method_param:
                    self.scope_context.add_param(type_scope)
                else: # No hace nada por el momento
                    self.scope_context.add_local_var(name, type_scope)
            else:
                raise Exception(
                    'Only local variables can be added to the method')

        elif isinstance(self.scope_context, SymbolTableLet):
            if isinstance(type_scope, SymbolTableValue):
                self.scope_context.add_variable(name, type_scope)
            else:
                raise Exception('Only variables can be added to the let')

    def consult(self, name: str, search_in_parent=True) -> SymbolTableClass | SymbolTableMethod | SymbolTableValue:
        if isinstance(self.scope_context, SymbolTableProgram):
            return self.scope_context.classes.get(name, None)
        elif isinstance(self.scope_context, SymbolTableClass):            
            if name == 'SELF_TYPE':
                return self.scope_context

            if name in self.scope_context.attrs:
                return self.scope_context.attrs[name]

            if name in self.scope_context.methods:
                return self.scope_context.methods[name]

            # Buscar metodos en la clase padre
            if search_in_parent:
                if self.scope_context.inherit and name in self.scope_context.inherit.attrs:
                    return self.scope_context.inherit.attrs[name]

                if self.scope_context.inherit and name in self.scope_context.inherit.methods:
                    return self.scope_context.inherit.methods[name]

        elif isinstance(self.scope_context, SymbolTableMethod):
            if name in self.scope_context.local_vars: # No hace nada ahorita
                return self.scope_context.local_vars[name]

            for param in self.scope_context.params:
                if param.name == name:
                    return param

        elif isinstance(self.scope_context, SymbolTableLet):
            if name in self.scope_context.variables:
                return self.scope_context.variables[name]

        return None

    def to_string(self) -> str:
        return f'SymbolTable {{\n\t{self.scope_context}\n}}'

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()


def search_scope(name: str, scope: list[SymbolTable], search_in_parent=True, level_search=None) -> SymbolTableClass | SymbolTableMethod | SymbolTableValue:
    for level, table in enumerate(reversed(scope)):
        type_scope = table.consult(name, search_in_parent)
        if type_scope:
            return type_scope

        if level_search is not None and (level + 1) == level_search:
            return None
    return None
