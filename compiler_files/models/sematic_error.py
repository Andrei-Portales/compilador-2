from .compiler_types import CompilerType

class SemanticError:
    def __init__(self, message: str, line: int, column: int, type_scope: CompilerType = None) -> None:
        self.type_scope = type_scope
        self.message = message
        self.line = line
        self.column = column
        
        
    def __str__(self) -> str:
        type_error = ''
        
        if self.type_scope:
            type_error = self.type_scope
                                
        return f'{type_error} Error: {self.message} at line {self.line}, column {self.column}'
        
        
    def __repr__(self) -> str:
        type_error = ''
        
        if self.type_scope:
            type_error = self.type_scope
            
        return f'{type_error} Error: {self.message} at line {self.line}, column {self.column}'