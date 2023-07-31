from enum import Enum

class PrimitiveType(Enum):
    INTEGER = 1
    STRING = 3
    BOOLEAN = 4
    CUSTOM_TYPE = 7
    
    
class CompilerType:
    def __init__(self, 
                 type_scope: PrimitiveType, 
                 custom_type_name: str | None = None
                 ) -> None:
        
        self.type_scope = PrimitiveType.CUSTOM_TYPE
        
        if type_scope == PrimitiveType.INTEGER:
            self.custom_type_name = 'Integer'
        elif type_scope == PrimitiveType.STRING:
            self.custom_type_name = 'String'
        elif type_scope == PrimitiveType.BOOLEAN:
            self.custom_type_name = 'Boolean'       
        else:
            self.custom_type_name = custom_type_name
            
    def compare(self, other: 'CompilerType') -> bool:
        if self.type_scope != other.type_scope:
            return False
        
        if self.type_scope == PrimitiveType.CUSTOM_TYPE:
            return self.custom_type_name == other.custom_type_name
        else:
            return True
        
    def check_type(self, primitive_type: PrimitiveType, custom_type: str | None = None) -> bool:

        if primitive_type == PrimitiveType.INTEGER:
            custom_type = 'Integer'
        elif primitive_type == PrimitiveType.STRING:
            custom_type = 'String'
        elif primitive_type == PrimitiveType.BOOLEAN:
            custom_type = 'Boolean' 

        return self.custom_type_name == custom_type
        
        
    def __str__(self) -> str:
        if self.type_scope == PrimitiveType.CUSTOM_TYPE:
            return self.custom_type_name
        else:
            return self.type_scope.name
        
    def __repr__(self) -> str:
        if self.type_scope == PrimitiveType.CUSTOM_TYPE:
            return self.custom_type_name
        else:
            return self.type_scope.name
