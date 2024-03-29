from enum import Enum
from .three_address import ThreeAddressString, ThreeAddressInteger, ThreeAddressBoolean, ThreeAddressTemporal, ThreeAddressVariable, ThreeAddressOperation

class PrimitiveType(Enum):
    INTEGER = 1
    STRING = 2
    BOOLEAN = 3
    CUSTOM_TYPE = 4
    VOID = 5
    
    
class CompilerType:
    def __init__(self, 
                 type_scope: PrimitiveType, 
                 custom_type_name: str | None = None,
                 associated_code: list[
                     ThreeAddressString | 
                     ThreeAddressInteger | 
                     ThreeAddressBoolean | 
                     ThreeAddressTemporal | 
                     ThreeAddressVariable | 
                     ThreeAddressOperation] | None = None
                 ) -> None:
        
        self.type_scope = PrimitiveType.CUSTOM_TYPE
        self.associated_code: list[
                     ThreeAddressString | 
                     ThreeAddressInteger | 
                     ThreeAddressBoolean | 
                     ThreeAddressTemporal | 
                     ThreeAddressVariable | 
                     ThreeAddressOperation] = associated_code or []
        
        if type_scope == PrimitiveType.INTEGER:
            self.custom_type_name = 'Int'
        elif type_scope == PrimitiveType.STRING:
            self.custom_type_name = 'String'
        elif type_scope == PrimitiveType.BOOLEAN:
            self.custom_type_name = 'Bool'     
        elif type_scope == PrimitiveType.VOID:
            self.custom_type_name = 'void'  
        else:
            self.custom_type_name = custom_type_name
            
    def compare(self, other: 'CompilerType') -> bool:
        if self.type_scope != other.type_scope:
            return False
        
        if self.custom_type_name == 'Bool' and other.custom_type_name == 'Int':
            return True
        elif self.custom_type_name == 'Int' and other.custom_type_name == 'Bool':
            return True
                
        return self.custom_type_name == other.custom_type_name
        
    def check_type(self, primitive_type: 'CompilerType', custom_type: str | None = None) -> bool:

        if primitive_type == PrimitiveType.INTEGER:
            custom_type = 'Int'
        elif primitive_type == PrimitiveType.STRING:
            custom_type = 'String'
        elif primitive_type == PrimitiveType.BOOLEAN:
            custom_type = 'Bool' 
        elif primitive_type == PrimitiveType.VOID:
            custom_type = 'void'
            
        return self.custom_type_name == custom_type
        
    def to_string(self) -> str:
        return f'CompilerType({self.custom_type_name})'
        
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
