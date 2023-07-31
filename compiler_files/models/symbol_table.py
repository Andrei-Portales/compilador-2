from .compiler_types import CompilerType, PrimitiveType

class SymbolTable:
    def __init__(self) -> None:
        self.scope_context: dict[str, CompilerType] = {
            'Boolean': CompilerType(PrimitiveType.BOOLEAN),
            'Integer': CompilerType(PrimitiveType.INTEGER),
            'String': CompilerType(PrimitiveType.STRING),
        }
        
    def add(self, name: str, type_scope: CompilerType) -> None:
        self.scope_context[name] = type_scope
        
    def consult(self, name: str) -> CompilerType:
        return self.scope_context.get(name, None)
    
    
def search_scope(name: str, scope: list[SymbolTable]) -> CompilerType:
    for table in reversed(scope):
        type_scope = table.consult(name)
        if type_scope:
            return type_scope
    return None